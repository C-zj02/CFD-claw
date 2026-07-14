from pathlib import Path

import matplotlib
import pytest

matplotlib.use("Agg")

from matplotlib.figure import Figure

from aircraft_design.utils.visualization_static import StaticPlotter


def test_plot_3view_frames_realistic_aircraft_geometry(tmp_path, monkeypatch):
    geom = {
        "fuselage": {"length_m": 12.0, "diameter_m": 1.4, "x_m": 1.5, "y_m": 0.2},
        "wing": {
            "s_ref_m2": 28.0,
            "aspect_ratio": 8.0,
            "taper_ratio": 0.45,
            "sweep_deg": 18.0,
            "x_m": 4.2,
            "y_m": 0.35,
            "z_m": 0.1,
        },
        "horizontal_tail": {
            "s_ref_m2": 6.4,
            "aspect_ratio": 4.0,
            "taper_ratio": 0.5,
            "sweep_deg": 25.0,
            "x_m": 10.4,
        },
        "vertical_tail": {
            "s_ref_m2": 3.2,
            "aspect_ratio": 1.6,
            "taper_ratio": 0.55,
            "sweep_deg": 28.0,
            "x_m": 10.1,
            "z_m": 0.7,
        },
    }

    saved_axes = {}
    original_savefig = Figure.savefig

    def capture_axes(figure, destination, *args, **kwargs):
        axis = figure.axes[0]
        saved_axes[Path(destination).name] = {
            "xlim": axis.get_xlim(),
            "ylim": axis.get_ylim(),
            "data_xlim": tuple(axis.dataLim.intervalx),
            "data_ylim": tuple(axis.dataLim.intervaly),
            "aspect": axis.get_aspect(),
            "yaxis_inverted": axis.yaxis_inverted(),
        }
        return original_savefig(figure, destination, *args, **kwargs)

    monkeypatch.setattr(Figure, "savefig", capture_axes)

    paths = StaticPlotter(tmp_path).plot_3view(geom)

    top = saved_axes["view_top_static.png"]
    side = saved_axes["view_side_static.png"]

    wing_half_span = (28.0 * 8.0) ** 0.5 / 2.0
    vertical_tail_height = (3.2 * 1.6) ** 0.5

    for view in (top, side):
        for limits_name, data_limits_name in (("xlim", "data_xlim"), ("ylim", "data_ylim")):
            lower, upper = view[limits_name]
            data_lower, data_upper = view[data_limits_name]
            assert lower < data_lower
            assert upper > data_upper
            assert (upper - lower) / (data_upper - data_lower) < 1.25

    assert top["xlim"][0] < 1.5
    assert top["xlim"][1] > 13.5
    assert top["ylim"][0] < 0.35 - wing_half_span
    assert top["ylim"][1] > 0.35 + wing_half_span
    assert top["aspect"] == pytest.approx(1.0)

    assert side["xlim"][0] < 1.5
    assert side["xlim"][1] > 13.5
    assert side["ylim"][0] < -0.7
    assert side["ylim"][1] > 0.7 + vertical_tail_height
    assert not side["yaxis_inverted"]
    assert side["aspect"] == pytest.approx(1.0)

    assert Path(paths["vsp_top"]).is_file()
    assert Path(paths["vsp_side"]).is_file()
    assert Path(paths["vsp_top"]).stat().st_size > 0
    assert Path(paths["vsp_side"]).stat().st_size > 0
