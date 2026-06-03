from pathlib import Path
import sys

BENCHMARK_ROOT = Path(__file__).resolve().parents[2]
if str(BENCHMARK_ROOT) not in sys.path:
    sys.path.insert(0, str(BENCHMARK_ROOT))

from common_eval import evaluate_aircraft_response


def evaluate_llm_response(response):
    return evaluate_aircraft_response(response, Path(__file__).with_name("rubric.json"))
