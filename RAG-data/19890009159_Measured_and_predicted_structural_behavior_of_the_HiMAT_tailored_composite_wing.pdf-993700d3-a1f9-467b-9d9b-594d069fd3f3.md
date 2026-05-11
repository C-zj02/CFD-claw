MAR 23 1992

fully ed 3/89

# Measured and Predicted Structural Behavior of the HiMAT Tailored Composite Wing

Lawrence H. Nelson

(BASA-CR-166617) MEASURED AND FERREDICTED N89-18530

STRUCTURAL EEAVIICE CF THE BIEAT TAILED

CCERPOSITE WING FINAL REPORT (California

Ecltytechnic State Univ.) 92 f CSCL 11D Unclas

G3/24 0192939

Contract NCA 2-6

March 1987

# Measured and Predicted Structural Behavior of the HiMAT Tailored Composite Wing

Lawrence H. Nelson

California Polytechnic State University, San Luis Obispo, California

Prepared for

Ames Research Center

Dryden Flight Research Facility

Edwards, California

Under Contract NCA 2-6

1987

# MEASURED AND PREDICTED STRUCTURAL BEHAVIOR

# OF THE HiMAT TAILED COMPOSITE WING

Lawrence H. Nelson

California Polytechnic State University

San Luis Obispo, California

# INTRODUCTION

Graphite-epoxy laminates have assumed a major role in the structural design of modern aircraft. The industry has built a reasonable data base for the more common fiber-dominated laminates. However, little data are available on unbalanced, matrix-dominated laminates such as that used for the aeroelastically tailored outer wing skins of the HiMAT vehicle.

A series of load tests were conducted on the HiMAT outer wing. A variety of unbalanced laminate coupons were fabricated by the HiMAT contractor and tested, primarily at NASA facilities.

Data obtained from these tests are presented in this report together with predicted behavior of the test articles.

# DESCRIPTION OF THE HiMAT OUTER WING

The major effort to aeroelastically tailor the HiMAT vehicle was focused on the outer wing structure. Reference 1 discusses the design methodology. The following description of the final design is taken almost verbatim from reference 2.

The structural layout, shown in Figure 1, consists of a central structural box, a fixed leading edge flap, and trailing edge control surfaces. The structural box is constructed of tailored covers of AS/350l-5 graphite-epoxy oriented with generally $40\%$ of the plies at $50^{\circ}$ , $40\%$ at $-50^{\circ}$ , and $20\%$ at $35^{\circ}$ , with respect to the laminate reference axis. The cover thickness varies from 16 plies or 2.13 mm (.084 inch) near the tip to 54 plies or 7.20 mm (0.284 inch) at the root. Twenty of the 54 plies are boron-epoxy interlayered locally to reinforce the root attachment. The box structure is closed out by leading and trailing edge spars constructed of T300/934 graphite-epoxy fabric. All plies are oriented at $45^{\circ}$ to the centerline of the spar except for one cap and web ply on the leading edge between the root and $X_{F} = 166.8$ cm (46.0 in.) which is at $90^{\circ}$ (F refers to the fuselage-wing Cartesian coordinate reference system). The number of cap (c) plies and web (w) plies along the spars is indicated in Figure 1(b). The root rib is also T300/934

graphite-epoxy three plies thick. A tip fin is mechanically attached to the wing box. The core of the structural box is full depth aluminum honeycomb. The wing box is a $100\%$ bonded structure.

The leading edge of the outboard wing (Figure 1(c)) is constructed of fiberglass-epoxy. It is attached to the wing box by a full length piano hinge at both the top and bottom surfaces. To increase the effective wing twist, the leading edge is cut into three segments with single pin connections near the nose, and the attachment hinges are cut into approximately 10 cm (4 in.) segments.

The elevon and aileron structures are similar having T300/934 graphite-epoxy skins, and a channel of the same material for the leading edge close out. The surfaces are mounted to the wing box on self-aligning ball hinges. The elevon is mounted at only two hinge points so that it does not contribute to the strength or stiffness of the outboard wing. The aileron however, is mounted at three points and must be accounted for. Furthermore, in later stages of the flight test program, the aileron was made inoperative by removing the control linkage and strapping $1 / 16 - 1 / 8$ inch thick steel plates from the aileron to the wing box.

A titanium wing rib mechanically joins the wing box to the inboard wing structure, or in the case of the load tests to be described, to the floor-mounted reaction frame.

# ANALYSIS

Analysis of the outer wing was carried out using the NASTRAN finite element computer program. The structural model, created by the HiMAT contractor, is shown in isometric form in Figure 2(a), and in plan view in Figure 2(b). Figure 2(b) may be viewed to judge the mesh size for the plate (CQUAD2) elements that largely define the top and bottom skins of the wing box. The leading and trailing edge spars as well as the honeycomb core are modeled by rod and shear elements. The leading edge of the wing is defined using CQUAD2 elements, whereas the levon and aileron are modeled using CQUAD1 plate elements. The titanium rib/composite skin bolted joint was modeled to account for fastener flexibility. CBAR elements, modeling the fasteners, serve to connect layers of CTRIA2 and CQUAD2 plate elements that, in turn, model the rib and adjacent composite skins. The wing box model has about 1200 degrees of freedom. Further discussion of the NASTRAN model may be found in reference 1.

The NASTRAN model of the wing box was also used to perform a nonlinear analysis that accounted for the inelastic shear behavior of the lamina of the CQUAD2 elements. This analysis used the incremental, piecewise linear method described by Petit and Waddoups (reference 3). Stresses and strains at both the element and ply levels were monitored in 84 CQUAD2 elements. An increment of load was computed that would cause a predetermined maximum incremental strain in the most highly

strained element in the covers. The strain increment used was 0.001, measured parallel to the laminate reference axis of the wing box. The incremental responses of the wing are added together to get an accumulative response. As each incremental response of the wing is added to prior sets, new tangent moduli of the lamina shear stress-strain curves are computed, based on the current stress levels. A Ramberg-Osgood representation of the stress-strain curve (references 4 and 5) is differentiated to obtain the local tangent modulus. Classical lamination theory (e.g. reference 6) is then used to compute the new laminate stiffness.

Figure 3 is a flow diagram describing the steps in the incremental loads analysis. Referring to Figure 3, it is seen that the input data to NASTRAN consists of two files that are merged: MATMODS, a file containing the MAT2 data defining the stress-strain behavior of the wing cover plate elements, and WNGBOX, containing all other data required to define the model. In addition to the usual NASTRAN output, designated BOXOUT, a considerably smaller subset "punch file" labeled NASOUT, is generated containing only data germane to the incremental loads analysis that is carried out by the program, INCLDS. INCLDS is an ad hoc code set up to specifically handle the wing box analysis. INCLDS examines NASOUT to find the most highly strained CQUAD2 element, an appropriate load increment is determined, and corresponding stress and strain increments are computed. These increments are added to the prior load-stress-strain state, obtaining an updated state for the wing box. The updated state is used to compute new shear stress-strain moduli. For each element, the laminate stress-strain relationship is recomputed, in the form of new MAT2 data, and loaded into the MATMODS file. A new NASTRAN run may now be made. For the analysis done in support of the load tests, l4 strain increments were used. A three times coarser analysis (three times larger increments) gave essentially the same results.

Crucial to all analyses are the estimates of the ply stress-strain properties. These properties are discussed in Appendix A. Confidence in these properties and in the incremental loads analysis was acquired through a laminate coupon test and analysis program that is discussed in Appendix B.

# TEST PLAN AND INSTRUMENTATION

The primary objective of the wing test program was to obtain data that could be compared with the finite element analysis. The test data were also examined for cumulative load cycle effects, and for the effects of the leading and trailing edges on the structural behavior of the wing box. The test program consisted of a series of load cycles that caused progressively higher strain levels in the composite wing skins.

Loads were applied near the tips of the leading and trailing edge spars of the wing box. A rubber-padded, 4-inch-wide steel plate distributed the load supplied by hydraulic cylinders. Early tests used

two cylinders connected to follow the same load-time curve. Most tests used a single hydraulic cylinder. Load cells were installed in series with the cylinders.

Fourteen potentiometric displacement transducers were positioned along the leading and trailing edges of the wing. These transducers, selectively sized for a range varying from 0 - 2.54 cm to 0 - 61 cm, have a resolution of 0.3 percent of full scale (reference 7).

Wing cover strains were measured using both three-element rosettes and single-element gages. The metal-foil gages were 350 ohm and of $1/4$ inch gage length. The gages were installed using a cyanoacrylate cement. The gages were mounted at the centroidal location of specific CQUAD2 elements. One element of each gage (leg A for the rosettes) was mounted parallel to the leading edge of the wing box. These gages were within $+5^{\circ}$ of being parallel to the laminate reference axis of the structural box (see Figure 1(a)). Legs B and C of the rosettes, are within $+5^{\circ}$ of being parallel to the $-45^{\circ}$ and $90^{\circ}$ directions, respectively, measured from the laminate reference axis. Figure 4 shows the general location of the displacement transducers and strain gages, and gives the serial numbers of the gages as they are referred to in this report.

# RESULTS AND DISCUSSION

Table I summarizes the 27-test program. Tests 1-4 investigated the effect of the leading and trailing edges on the structural behavior of the wing box. Tests 4-7 investigated the effect of changing the way in which the wing box was loaded. Tests 8-27 investigated the behavior of the wing box at successively higher loads. In all cases, a linearly increasing, then decreasing load-time profile was applied to the wing. The characteristics of these sawtooth load profiles are given in Table I in terms of peak load (both target and actual values) and the rise and decay times of the linear ramps. Another characteristic of the test program was the use of a 4.5-kN (l000-lb) posttest load cycle to assess, by comparison with prior 4.5-kN tests, any cumulative damage incurred as the testing progressed.

The maximum load applied to the wing box was $22\mathrm{kN}$ (4950 lb). At this load, a test fixture bolt failure occurred at the interface between the root rib of the wing and a set of test fixture mounting lugs.

Reference 1 discusses design iterations that were conducted to determine how various parts of the aircraft structure contribute to the bending and twisting of the wing. Tests 1-4 provided data on the effect of successively removing the leading and trailing edges of the outer wing. Data from Tests 1-4 are presented in Figures 5-8. Figures 5 and 6 compare measured and predicted deflections of the wing box tip. Figures 7 and 8 compare measured and predicted strains at two typical locations on the wing box. Each figure shows a prediction based on the outer wing model, i.e. wing box plus leading and trailing edges, and also a prediction based on just the wing box model. Referring to

Figures 5-8 it is seen that the experimental data for Tests 1 and 4 are reasonably coincident. In other words, the leading and trailing edges have no effect on the wing box behavior. Comparing the predictions in each of Figures 5-8, it is seen that the flaps are predicted to be stiffer than they really are. On the other hand, the wing box model appears more flexible than the test data indicate.

Figures 5-8 also contain data from Test 7. These data were acquired after changing the loading configuration to a single cylinder, and increasing the load rate to $11\mathrm{kN / min}$ . Test 7 data are virtually identical to prior data sets, and indicate that neither differences in the loading configuration nor changes in load rate had any substantial effect on the wing behavior.

Test data presented in Figures 5-8 are for both loading and unloading. By comparing adjacent points from the same test a measure of hysteresis during the load cycle can be obtained. Examining the data of Figures 5-8 it is judged that there is little hysteresis in these early tests. Figures 9-12 are similar to Figures 5-8, except that a comparison is made between Tests 4 and 26. Examining Figures 9-12, it is judged that there is a softening of the structure after the 26 tests. Figures 9 and 10 suggest that the amount of hysteresis may also have increased.

A clearer indication of any cumulative load effects may be obtained by making comparisons across all 27 tests. Figure 13 is a plot of the leading edge tip deflection versus load for all tests. For clarity the load axes are shifted and only certain load points are emphasized by symbols (in some cases small extrapolation of data has been allowed). Similar plots for the trailing edge tip deflection, and two strain gages are given in Figures 14-16. Figures 13-16 show a progressive, if somewhat erratic, softening of the wing box structure as test cycles are accumulated.

The behavior of the wing box at relatively high loads is shown in Figures 17-20. These Figures are based on Test 21 in which a maximum load of $19\mathrm{kN}$ (4300 lb) was applied to the wing. Figure 17 shows the rather large bending and twisting deflections that occurred during the test. (The lower skin of the unloaded wing lies approximately in a horizontal plane).

Figures 18 and 19 present strain data for all gages on the top and bottom surfaces of the wing during Test 21. Also presented are the predicted strains according to the linear and nonlinear (incremental) NASTRAN analyses. Generally, there is a clear difference between the two analyses at the higher loads, except in the root region, where the boron-reinforced covers cause both analyses to be linear. Again, generally, the measured load-strain behavior is linear, in marked contrast to the nonlinear prediction. The linear behavior of the wing covers is also in marked contrast to the nonlinearity exhibited by unidirectional coupon test data (see Appendix B, Laminate 0 test results). For the outboard gages (709-716 and 609-616) it is judged that the linear NASTRAN analysis agrees reasonably well with the measured strains. For the root region (Gages 721-724 and 621-624) the agreement

is not nearly as good. It is noted, however, that the root region involves difficult modeling of the mechanical joint between the wing covers and the titanium rib. In addition the CQUAD2 elements, corresponding to gages 721-724 and 621-624, lie in a region where the plies drop off from 54 plies to 34 plies. Generally speaking, the load-strain plots do not exhibit much hysteresis.

Figures 20 and 21 present load-deflection data near the tips of the leading and trailing edge spars of the wing box. Referring to these Figures it is seen that the measured stiffness (slope of the load-deflection curves) of the structure is less than that predicted by the analysis. However, the data points for the loading portion of the cycle lie on a reasonably straight line, indicating linear rather than nonlinear behavior. Hysteresis is evident in the load/unload cycle. There is an approximate $2\%$ offset $(6 - 7\mathrm{mm})$ after unloading. It was observed that roughly one-half of this offset is recovered in the first 15 seconds following complete unloading.

Figure 22 compares the measured deflections of the wing box with predictions. The measured deflection shape of the wing compares favorably with the predicted shape from the linear analysis, and less favorably with the nonlinear analysis. Both analyses appear to predict less rotation in the bolted joint area than was measured. The predicted spar deflections in just the region of the bolted joint are shown in Figures 23 and 24 for the leading edge and trailing edge respectively. The most inboard set of four data points are the deflections of the wing skin/rib interface. It is seen that this region rotates very nearly as a rigid body. It does not appear possible to connect these points with a curve to the next several points outboard without introducing a very sharp change (cusp) in the deflection curve; see Figures 23 and 24 where curves have been drawn through the predicted deflections to show the apparent cusp. Examination of other sets of spanwise deflection data in the root region show a similar apparent discontinuity in slope. Thus, there appears to be an anomaly in the structural model, in the joint area, that cannot presently be explained. It is noted in Figures 23 and 24, that the predicted slope of the deflection curve just outboard of the joint appears less than the joint slope, effectively reducing the joint rotation, and providing a clue as to why the analyses appear to predict less rotation than is measured (see Figure 22).

It is of some interest to compare the wing structural behavior vis-a-vis the behavior of the same laminate configuration as a test coupon subjected to uniaxial loading. The major quantifiable results of the coupon tests (specifically, Laminate 0) are found in Appendix B. In addition, observations were made during both the wing and coupon tests relating to hysteresis, creep, and posttest offset. For the same strain level, the coupon tests showed considerably more hysteresis that was observed during the wing tests. Creep was evident in the Laminate 0 tensile coupon tests during 10-second holds at peak loads. Creep was not observed during Test 21 when a $19\mathrm{kN}$ load was applied to the wing for about 10 seconds. Posttest (no load) offsets in the wing tip deflections, evident in Figures 20 and 21, were observed to decrease by roughly $50\%$ in the first 15 seconds following unloading.

# SUMMARY OF RESULTS

A series of load tests were conducted on the HiMAT outer wing. The objective of these tests was to determine the behavior of this unbalanced, matrix-dominated laminate structure, to loads approaching failure, and to compare test results with predicted behavior.

The leading and trailing edges were found to have no effect on the response of the wing to applied loads. A decrease in the stiffness of the wing box was evident over the 27-test program.

The measured load-strain behavior was found to be linear, in contrast to coupon tests of the same laminate, which were nonlinear. A linear NASTRAN analysis of the wing generally correlated more favorably with measurements than did a nonlinear analysis.

A close examination of the predicted deflections in the root region of the wing revealed an anomalous behavior of the structural model that cannot presently be explained.

Both hysteresis and creep appear to be less significant in the wing tests than in the corresponding laminate coupon tests.

# APPENDIX A

# Stress-Strain Behavior of AS/3501-5

# Introduction

To perform a nonlinear analysis on the wing box requires knowing the stress-strain behavior of the AS/350l-5 ply material in tension and compression, longitudinally (i.e. along the fibers) and transversely, and also in shear. In other words, five stress-strain relationships must be known. Specifically, the following data must be obtained: (1) Shape of the stress-strain curves (i.e. linear/nonlinear), (2) Initial (tangent) moduli and Poisson's ratio, (3) Ultimate strength and strain.

In those cases where substantial nonlinearities exist, a Ramberg-Osgood curve fit (reference 5) was performed. This curve fit is differentiated to obtain a "local" tangent modulus for the curve.

Based on the data found in the literature, it has been difficult to establish, with high confidence, complete ply stress-strain relationships for AS/350l-5. Fairly large variations can exist in most properties. Material characteristics often appear to be a function of the test method. Frequently, insufficient information is given to evaluate test results. It is possible that some properties improve over a period of time, due to changes in the manufacturing process or improvements in quality control.

It appears that sufficient data are available to define with reasonable confidence the shape of the stress-strain curves, including the initial linear range. There is far less confidence in some of the estimates for ultimate stress and strain. It has been necessary to use some property data for AS/3501-6, assuming that it would apply reasonably well to AS/3501-5.

In order to maintain the integrity of the majority of original data cited in this Appendix, English units are used.

# Symbols

$\mathbf{E}_{\mathbf{L}}$ Young's modulus in tension in the longitudinal (fiber) direction.   
E' Young's modulus in compression in the longitudinal (fiber) direction.   
$\mathbf{E}_{\mathrm{T}}$ Young's modulus in tension in the transverse direction.   
Young's modulus in compression in the transverse direction.   
$\mathbf{G}_{\mathrm{LT}}$ Inplane shear modulus.

$\gamma_{\mathrm{LTU}}$ Ultimate shear strain. $\varepsilon_{\mathrm{LU}}$ Ultimate tensile strain in the longitudinal direction. $\varepsilon_{\mathrm{LU}}^{\prime}$ Ultimate compressive strain in the longitudinal direction. $\varepsilon_{\mathrm{TU}}$ Ultimate tensile strain in the transverse direction. $\varepsilon_{\mathrm{TU}}^{\prime}$ Ultimate compressive strain in the transverse direction. $\nu_{\mathrm{LT}}$ Major Poisson's ratio for tensile loading. $\nu_{\mathrm{LT}}^{\prime}$ Major Poisson's ratio for compressive loading. $\sigma_{\mathrm{LU}}$ Ultimate tensile strength in the longitudinal direction. $\sigma_{\mathrm{LU}}^{\prime}$ Ultimate compressive strength in the longitudinal direction. $\sigma_{\mathrm{TU}}$ Ultimate tensile strength in the transverse direction. $\sigma_{\mathrm{TU}}^{\prime}$ Ultimate compressive strength in the transverse direction. $\tau_{\mathrm{L TU}}$ Ultimate shear strength.

# Longitudinal Tensile Stress-Strain Behavior

Table A.l lists Young's modulus, Poisson's ratio, and ultimate strength and strain for AS/350l as compiled from several sources. Referring to Table A.l, it is judged that the variation in properties from one source to another is not severe except for strength. It is generally assumed that the longitudinal stress-strain curve is linear, although reference 13 points out that there is a slight stiffening on the order of 10 percent. For the present purpose, it will be assumed that the stress-strain curve is linear and can be characterized as follows:

$$
\begin{array}{l} E _ {L} = 2 0 M s i \\ \sigma_ {\mathrm {L U}} = 2 4 0 \mathrm {k s i} \\ \varepsilon_ {\mathrm {L U}} = 1 2 0 0 0 \mu \varepsilon \\ \end{array}
$$

Furthermore, a major Poisson's ratio of 0.3 will be used. Analysis has not shown a great sensitivity to Poisson's ratio.

# Longitudinal Compressive Stress-Strain Behavior

Table A.2 lists Young's modulus, Poisson's ratio, and ultimate strength and strain for AS/3501 as compiled from several sources. Referring to Table A.2, it is judged that large variations exist in all of the parameters except Poisson's ratio. Reference 16 states, "Perhaps the most difficult of the intrinsic material properties of composites to measure are the compressive strength properties. This is the

case due to the fact that slight specimen geometric variations result in eccentricity of the applied load thereby enhancing the opportunity for failure to occur due to geometric instability."

To aid in reaching a conclusion on how to characterize longitudinal compressive behavior, property data for AS4/350l-6 (reference 15) have been examined. Table A.3 lists the pertinent data from reference 15. Referring to Table A.3, it is seen that two sets of compression data are listed, one for a Celanese test fixture characterized by a short, unsupported test section and the other set for a sandwich beam specimen which inherently provides the support necessary for stable loading. Examining the Young's modulus data, it is seen that the two test methods give about the same value: $20 + \text{Msi}$ . The AS4 fiber is only slightly stiffer than the AS1 fiber (34 Msi versus 32 Msi) so $E_{L}^{\prime} = 20$ Msi is probably applicable to AS1/350l-5. Examining the data for ultimate strength and strain, it is seen that the sandwich beam test yields higher values. This trend is evidently frequently observed (reference 16). The strength/strain data of Table A.3 cannot be directly applied to AS/350l because the AS4 fiber is substantially stronger than the AS1 fiber (fiber strength is 520 ksi for AS4 versus 450 ksi for AS1). However, similar trends in strength might be expected between unsupported test methods [Celanese or ITTRI (ref. 21)] and fully supported test methods (sandwich beam or a full depth honeycomb wing structure). Reference 15 gives the longitudinal tensile strength of AS4/350l-6 as 313 ksi. Thus it appears that with a high quality sandwich beam specimen it is possible to attain a compressive strength (292 ksi) almost equal to the tensile strength (313 ksi). Further examination of Table A.3 shows that the stress-strain curves are only slightly nonlinear.

For the purpose of predicting the behavior of the full depth honeycomb outer wing, it will be assumed that the compressive stress-strain curve equals the tensile stress-strain curve. In other words:

$$
\begin{array}{l} E _ {L} ^ {\prime} = 2 0 \text {M s i} \\ \sigma_ {\mathrm {L U}} ^ {\prime} = 2 4 0 \mathrm {k s i} \\ \varepsilon_ {L U} ^ {\prime} = 1 2 0 0 0 \mu \varepsilon \\ \end{array}
$$

# Transverse Tensile Stress-Strain Behavior

Table A.4 lists Young's modulus and ultimate strength and strain for AS/3501 as compiled from several sources. The stress-strain curve appears to be fairly linear. For the present purposes it will be assumed that the stress-strain curve is linear and can be characterized as follows:

$$
\begin{array}{l} E _ {T} = 1. 5 \text {M s i} \\ \sigma_ {\mathrm {T U}} = 7. 8 \mathrm {k s i} \\ \varepsilon_ {\mathrm {T U}} = 5 2 0 0 \mu \varepsilon \\ \end{array}
$$

Table A.5 lists Young's modulus and ultimate strength and strain for AS/350l as compiled from several sources. Referring to Table A.5 it is judged that there is a fair amount of consistency in the data. There is also a fair amount of nonlinearity in the stress-strain curve.

For the present purposes, the stress-strain curve will be characterized as follows:

$$
\begin{array}{l} E _ {T} ^ {\prime} = 1. 5 \text {M s i} \\ \sigma_ {\mathrm {T U}} ^ {\prime} = 3 6 \mathrm {k s i} \\ \varepsilon_ {T U} ^ {\prime} = 3 1 0 0 0 \mu \varepsilon \\ \end{array}
$$

A Ramberg-Osgood fit, accounting for the nonlinearity, yields the following equation:

$$
\varepsilon_ {T} ^ {\prime} = \frac {\sigma_ {T} ^ {\prime}}{1 . 5 x 1 0 ^ {6}} \left[ 1 + \left(\frac {\sigma_ {T} ^ {\prime}}{5 3 8 0 0}\right) ^ {2. 8 5} \right],
$$

where $\sigma_{\mathbf{T}}^{\prime}$ is in psi.

# Inplane Shear Stress-Strain Behavior

Table A.6 lists the shear modulus and ultimate strength and strain for AS/350l compiled from several sources. Referring to Table A.6 it is judged that there is considerable variation in the data. In some cases there is justification for dismissing the data. For example, the shear modulus of 0.61 Msi given in reference 8 is a secant modulus rather than a tangent modulus. The strength value of 17.1 ksi given in reference 12 is an "effective" strength based on extrapolation of stress-strain data; evidently there was an interference problem between the test fixture and the specimen.

The most complete and best understood shear data in Table A.6 were derived from five AS/3501-6, $+45^{\circ}$ specimens tested in tension (see Table A.6, footnote b). Referring to this data, it is seen that the average tangent modulus of 0.93 Msi appears to be an intermediate value compared to the other values listed in Table A.6. It also compares favorably with two unpublished values of 0.96 Msi measured in rail shear tests at NASA Ames-Dryden. In using the ultimate strength and strain values derived from these $+45^{\circ}$ specimens, it is well to keep in mind the caveat of reference 16 (p. 189) that, "although the $(+45)_S$ laminate tensile test can be employed to establish shear stress-strain response well into the region of nonlinear material response, caution must be exercised in interpretation of the ultimate stress and strain results. This is due to the fact that the lamina is in a state of combined stress rather than pure shear. Hence, it should be expected that the presence of the normal stress components would have a dele

terious effect upon ultimate shear strength." Reference 16 (Table 4-1) goes on to give strength values from $(+ - 45)$ tests to support the quoted statement. These values, given in terms of shear strength in Table A.6, are 11.4 ksi from tension tests and 14.6 ksi from compression tests.

For the present purposes the shear stress-strain curve will be characterized as follows:

$$
\begin{array}{l} G _ {L T} = 0. 9 3 \text {M s i} \\ \tau_ {\mathrm {L T U}} = 1 1. 5 \mathrm {k s i} \\ \gamma_ {\mathrm {L T U}} = 2 9 6 0 0 \mu \varepsilon \\ \end{array}
$$

A Ramberg-Osgood fit to the five sets of shear data, discussed in the previous paragraph, is shown in Figure A.1, together with the experimental data. It is seen that the fit is a good one except at failure where the experimental data show essentially a zero slope, whereas the analytical curve has a positive slope. The Ramberg-Osgood fit has the following form:

$$
\gamma_ {\mathrm {L T}} = \frac {\tau_ {\mathrm {L T}}}{. 9 3 \times 1 0 ^ {6}} \left[ 1 + \left(\frac {\tau_ {\mathrm {L T}}}{1 0 8 0 0}\right) ^ {3. 8 5} \right],
$$

where $\tau_{\mathrm{LT}}$ is in psi. Using $\tau_{\mathrm{LT}} = 11500$ psi, the above equation yields a shear strain of $\gamma_{\mathrm{LT}} = 28100\mu \varepsilon$ which is considered sufficiently close to an average test value of $29600\mu \varepsilon$ .

TABLE A.1. - LONGITUDINAL TENSILE PROPERTIES OF AS/3501  

<table><tr><td>Reference</td><td>8</td><td>9</td><td>10</td><td>13</td><td>14</td></tr><tr><td>EL, Msi</td><td>20</td><td>20</td><td>17.7</td><td>19</td><td>18.5</td></tr><tr><td>vLT</td><td>.30</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>σLU, ksi</td><td>236</td><td>225</td><td>214</td><td>257</td><td>225</td></tr><tr><td>εLU, με</td><td>12100</td><td>--</td><td>--</td><td>12300</td><td>11000</td></tr></table>

TABLE A.2. - LONGITUDINAL COMPRESSIVE PROPERTIES OF AS/3501  

<table><tr><td>Reference</td><td>8</td><td>9</td><td>10</td><td>12</td><td>14</td></tr><tr><td>E&#x27; L, Msi</td><td>16.3</td><td>16</td><td>14.4</td><td>16.4</td><td>20</td></tr><tr><td>v&#x27; LT</td><td>.33</td><td>--</td><td>--</td><td>.34</td><td>.31</td></tr><tr><td>σ&#x27; LU, ksi</td><td>152</td><td>135</td><td>272</td><td>203</td><td>142</td></tr><tr><td>ε&#x27; LU, με</td><td>10200</td><td>--</td><td>--</td><td>15100</td><td>8100</td></tr></table>

TABLE A.3. - LONGITUDINAL COMPRESSIVE PROPERTIES OF AS4/3501-6  

<table><tr><td>Reference</td><td>15</td><td>15</td></tr><tr><td>Test Method</td><td>Celanesea</td><td>Sandwich Beamb</td></tr><tr><td>Number of Tests</td><td>22</td><td>25</td></tr><tr><td>E&#x27;L, Msi</td><td>20.2 (5.)c</td><td>21.1 (3.3)</td></tr><tr><td>o&#x27;LU, ksi</td><td>226 (5.7)</td><td>292 (9.7)</td></tr><tr><td>ε&#x27;LU, με</td><td>13000 (7.3)</td><td>17500 (12.3)</td></tr></table>

a ASTM D 3410 - 75.   
b McDonnell Aircraft, MMS - 549.   
c Numbers in parentheses are coefficients of variations in percent.

TABLE A.4. - TRANSVERSE TENSILE PROPERTIES OF AS/3501  

<table><tr><td>Reference</td><td>8</td><td>11</td><td>13</td><td>14</td></tr><tr><td>ET,Msi</td><td>1.4</td><td>--</td><td>1.6</td><td>1.5</td></tr><tr><td>σTU, ksi</td><td>7.0</td><td>7.5</td><td>7.8</td><td>9.1</td></tr><tr><td>εTU, με</td><td>5100</td><td>--</td><td>5400</td><td>6400</td></tr></table>

TABLE A.5. - TRANSVERSE COMPRESSIVE PROPERTIES OF AS/3501  

<table><tr><td>Reference</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>14</td></tr><tr><td>E&#x27;T, MSI</td><td>1.5</td><td>1.4</td><td>1.6</td><td>--</td><td>1.7</td><td>1.65</td></tr><tr><td>σTU&#x27;, ksi</td><td>37</td><td>27</td><td>28</td><td>30</td><td>37.5</td><td>37.2</td></tr><tr><td>εTU&#x27;, με</td><td>32800</td><td>--</td><td>--</td><td>--</td><td>30300</td><td>31200</td></tr></table>

TABLE A.6. - INPLANE SHEAR PROPERTIES OF AS/3501  

<table><tr><td>Referencea</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>16</td><td>16</td></tr><tr><td>GLT, Msi</td><td>.61</td><td>-</td><td>1.25</td><td>-</td><td>i.4</td><td>.93b</td><td>.78</td><td>-</td><td>-</td></tr><tr><td>TLTU, ksi</td><td>9.6</td><td>12.1</td><td>16.1</td><td>13.5</td><td>17.1</td><td>11.5b</td><td>15.3</td><td>11.4c</td><td>14.6c</td></tr><tr><td>YLTU, με</td><td>18300</td><td>-</td><td>-</td><td>-</td><td>-</td><td>29600b</td><td>92500</td><td>-</td><td>-</td></tr></table>

a References 8 & 10 used a rail shear test specimen.   
Reference 9 used a tubular specimen.   
References 11, 12, 14, and 16 used a $+ - 45^{\circ}$ test specimen.   
b These properties were derived from $+ - 45^{\circ}$ specimen data for AS/3501-6, provided by Dr. Paul Lagace, Massachusetts Institute of Technology. His help is gratefully acknowledged. The present author accepts responsibility for the use of this data in generating these properties, as well as for the shear stress-strain curve shown in Figure A.1.   
c These values are one half the average strengths given in reference 16, Table 4-1. The assumption has been made that the data in Table 4-1 are tensile strengths of $+ - 45^{\circ}$ specimens, rather than shear strengths.

图片摘要：该图主要展示 A.1. INPLANE SHEAR STRESS STRAIN RESPONSE FOR AS/3501, DERIV。
![](images/a5d659ae6b4e7ff6181de893223b81d2a24f5cb40cd0c90a70fb84fe0b6dc6b6.jpg)  
FIGURE A.1. INPLANE SHEAR STRESS-STRAIN RESPONSE FOR AS/3501, DERIVED FROM ++45-DEGREE TEST SPECIMENS.

# APPENDIX B

# Measured and Predicted Behavior of Unbalanced Graphite/Epoxy Test Specimens

# Introduction

A series of nonstandard laminates was selected and fabricated by the HiMAT contractor. The specimens were instrumented and tested primarily at NASA facilities. The objective of this program was to determine the load-strain behavior of unbalanced laminates, and to compare the measured behavior with predictions.

# Specimen Description

All test specimens were fabricated from AS/350l-5 graphite-epoxy tape. Fiberglass-epoxy tabs were bonded to each specimen. Table B.l. summarizes the configurations of the coupons. Referring to Table B.l. it is seen that six laminate geometries were tested. Laminate 0 has the ply orientation of the HiMAT outer wing covers. Laminate 2 has the ply orientation of the HiMAT canard covers. Laminates 3-5 are fabricated with a varying mix of $0^{\circ}$ and $45^{\circ}$ plies. Laminate 3 is the most unbalanced with 75 percent $45^{\circ}$ plies and 12.5 percent $0^{\circ}$ plies. Laminate 4 is next with 50 percent $45^{\circ}$ plies and 37.5 percent $0^{\circ}$ plies. Laminate 5 is the least unbalanced with 12.5 percent $45^{\circ}$ plies, and 75 percent $0^{\circ}$ plies. Laminate 6 is a quasiisotropic, $(0 / + - 45 / 90)$ laminate.

From an examination of the ply orientations of the various laminates, it is judged that only Laminate 0 is a matrix-dominated laminate. Laminates 2-5, while unbalanced, possess - at least for the tests conducted - highly loaded fibers.

All laminates were subjected to tensile loading in the direction of the laminate reference axis. Laminates 0, 4, and 5 were also subjected to tensile loading perpendicular to the laminate reference axis. In addition, Laminate 0 was subjected to compressive loading along the reference axis.

# Analysis

There does not exist a widely accepted method for predicting laminate behavior up to fracture. Such a method would contain a ply failure criterion that accounts for the effect of adjacent crossplies, and in the case of unbalanced laminates, also accounts for potentially important nonlinear effects.

For the present analysis, three failure criteria were examined: Tsai-Wu criterion (reference 17), Hashin and Rotem criterion (reference 18), and the maximum strain criterion. The Tsai-Wu theory, as employed in this analysis, follows the suggestion of reference 19, and assumes no interaction between the normal stresses. The Hashin and Rotem

theory (referred to as the Hashin criterion in this report), simpler than Tsai-Wu and applicable to only matrix-dominated laminates, is applied to Laminate 0 only. The maximum strain criterion, perhaps the most widely used strength theory, is applied to Laminates 2-6.

For the purpose of analyzing the laminates described above, initial ply failure would appear to result in matrix cracking. It is assumed that the cracks accumulate gradually, and that no stress relaxation occurs. There is some evidence to support these assumptions; for example, according to reference 20, "no jumps (discontinuities in the stress-strain diagram) are observed in the case of glass, graphite, or boron fiber/epoxy resin crossply composites ...". While it is assumed that the failed ply does not unload, additional transverse loading of the ply is precluded by setting equal to zero, the transverse and shear moduli.

For all the laminates, an incremental loads analysis, as described in the main body of this report, was performed. For Laminates 2-6 an additional analysis was performed in which the ply shear stress-strain curve was assumed linear, and ply failure was based on the maximum strain criterion.

The same ply properties that were used for the wing analysis (discussed in Appendix A) were used for the coupon analysis.

# Test Program

All specimens were instrumented with back-to-back metal foil gages that measured strains along and perpendicular to the load axis. Most gages were three-element rosettes allowing an additional strain to be measured at either $+45^{\circ}$ or $-45^{\circ}$ to the load axis. In the case of Laminate 0 the rosette was used in conjunction with a single-axis gage providing strain measurements at $0^{\circ}$ , $45^{\circ}$ , $-45^{\circ}$ , and $90^{\circ}$ to the load. Laminate 6 had no $45^{\circ}$ gages, but had longitudinal gages at the edges of the specimen, providing a measure of the bending strain induced by any misalignment. All gages were capable of measuring up to 50,000 microstrain, with the exception of the Laminate 0 compression test gages, which were capable of measurements to 15,000 microstrain.

All coupons were tested in analog controlled, hydraulic testing machines. Tensile tests used mechanical wedge grips that self-tighten under load. The compression coupons were tested in an IITRI compression test fixture (reference 21). The load rate varied from 2.6 kN/min. (600 lb/min.) for the compression tests to 22 kN/min. (5000 lb/min.) for the tensile tests.

Most tests were run monotonically to failure. An exception was the Laminate 0 tests, in which two or three intermediate load cycles were applied prior to loading to failure.

# Results and Discussion

Figures B.1 - B.10 present measured and predicted load-strain curves for the laminates. Since, in many cases, the strain gages ceased to function prior to specimen failure, Figures B.1 - B.10 cannot be used to compare measured and predicted failure loads. For this purpose Table B.2 has been prepared.

Since Laminate 0 appears to be a truly matrix-dominated laminate, whereas Laminates 2-6 have highly loaded fibers, the discussion of results treats Laminate 0 separately.

Laminate 0 - Figures B.1 and B.2 present the load-strain behavior of Laminate 0 in tension and compression for loading along the laminate reference axis. Figure B.3 presents similar data for tensile loading perpendicular to the laminate reference axis. Referring to parts (A) and (B) of these Figures it is seen that Laminate 0 exhibits substantial nonlinear behavior. The predicted load-strain behavior compares better with test data for tensile loading than for compressive loading. The predicted initial slopes for these curves are somewhat greater than was measured. There are several possible reasons for this lack of a better correlation. First, the specimens were subjected to a series of load cycles prior to the final loading reported in these Figures. Some "softening" of the specimens did occur due to these prior load cycles. Secondly, specimen creep was observed, although the tests were not designed to quantify the creep effect. Thirdly, there is inherent scatter in results from present test methods and fabrication procedures, that appear to cover the range in discrepancy between the predicted curves and the test data of Figures B.1 - B.3. References 8 and 14 present shear stress-strain response curves for AS/3501 that differ substantially from those used in this report. A more judicious choice of the shear curve could have improved the correlation in Figures B.1 - B.3, but would not offer any guidance on how to assure, a priori, a good choice for the shear curve in future analysis. The kind of correlation shown in Figures B.1 - B.3 is perhaps more typical of what can be currently expected in analyzing matrix-dominated laminates.

Referring to parts (C) and (D) of Figures B.1 - B.3 it is judged that the predicted load-strain behavior in the $+ - 45^{\circ}$ directions correlate reasonably well with test data. It is noted that these strains are governed by the fiber properties in the $+ - 50^{\circ}$ plies.

Careful comparison of the test data of Figures B.1 and B.2, parts (A) and (B), shows that Laminate 0 behaves the same in tension and compression up to about 9,000 microstrain. At higher strain levels the laminate appears stiffer in tension than in compression. It is likely that at these higher strain levels differences in incipient failure modes have an effect.

Referring to Table B.2 and examining the percent difference between average measured failure load and predicted measured failure load, it is seen that the Hashin (and Rotem) failure criterion, on the average, yields a more favorable prediction than does the Tsai-Wu

failure theory. It is also noted that the Hashin and Rotem criterion is consistently conservative, whereas the Tsai-Wu criterion, for Lami-nate 0, is not.

Laminate 2-6 - From an examination of Figures B.4 - B.10, it is judged that the correlation between analysis and test is generally quite good up to the point where ply failure begins. In this region of good correlation the load versus strain, in the direction of the load, is fiber dominated. The least satisfactory correlation occurs with Laminate 5, loaded at 90 degrees to the reference axis (see Figure B.9). In this case 75 percent of the laminate (i.e. the $0^{\circ}$ plies) is subjected to matrix cracking during first ply failure.

Referring to Figure B.10 (A) it is noted that considerable scatter exists in the strain data for Specimen 2, and to a lesser extent, in the data for Specimen 3. The extreme strain values for these specimens are for gages bonded near the edges of the specimen, and indicate the presence of a substantial strain gradient (bending moment) that, in the case of Specimen 2, probably caused premature failure.

Analyses of Laminates 2-6 were carried out using both classical laminate theory, employing the maximum strain failure criterion, and a nonlinear (incremental loads) analysis employing the Tsai-Wu failure criterion. It appears that the nonlinear theory is somewhat better in predicting the load-strain behavior of these laminates. Referring to Table B.2, where percent differences between predicted and measured failure loads are given, it is concluded that the Tsai-Wu criterion predicts failure better than the maximum strain criterion.

It is of some interest to compare Laminates 3, 4, and 5 for the load conditions that apply in Figures 5(A), 7(A), and 9(A): for these three cases the load is aligned in the fiber direction of 12.5 percent of the plies. It is found that Figures 5(A) and 7(A) are very nearly identical, suggesting that the ply mix at $45^{\circ}$ and $90^{\circ}$ has little influence on behavior in the direction of the load. Figure 9(A) shows somewhat diminished stiffness and strength over Figures 5(A) and 7(A), indicated that the mix (and possibly stacking sequence) of $45^{\circ}$ and $90^{\circ}$ plies is beginning to have an effect. A comparison of Figures 5(B), 7(B), and 9(B) is a comparison of the Poisson effect, and a general stiffening of the laminates perpendicular to the load is observed as the percent of plies at $90^{\circ}$ to the load is increased.

# Summary of Results

A series of nonstandard laminate test specimens were instrumented with strain gages and loaded to failure. The objective of these tests was to determine the load-strain behavior of unbalanced laminates, and to compare this behavior with predictions.

Specimens having the ply orientation of the HiMAT wing box laminate (Laminate 0) show a nonlinear load-strain response. For Laminate 0 - a matrix-dominated laminate - the Hashin and Rotem failure cri-

terion generally gave a more favorable and consistent prediction of failure than did the Tsai-Wu criterion.

For Laminates 2-6 - fiber-dominated laminates - a generally good correlation existed between predicted and measured load-strain behavior, at least up to first ply failure. For these same laminates the Tsai-Wu failure criterion gave better predictions than did the maximum strain criterion.

The failure criteria used for the matrix-dominated laminate, Laminate 0, generally gave conservative predictions. The failure criteria used for Laminates 2-6 gave nonconservative predictions.

In general, the load-strain behavior up to first ply failure was predicted better than was failure load.

TABLE B.1. - CONFIGURATION OF LAMINATE TEST SPECIMENS   

<table><tr><td rowspan="2">ID</td><td rowspan="2">Laminate Orientation Code</td><td rowspan="2">Testa
Type</td><td colspan="3">Geometry, mm (inch)b</td></tr><tr><td>L</td><td>W</td><td>T</td></tr><tr><td rowspan="3">0</td><td rowspan="3">(+50/35/--+50)4</td><td>LT</td><td>100. (4.0)</td><td>50. (2.0)</td><td>2.77 (0.109)</td></tr><tr><td>LC</td><td>25. (1.0)</td><td>25. (1.0)</td><td>2.77 (0.109)</td></tr><tr><td>TT</td><td>100. (4.0)</td><td>50. (2.0)</td><td>2.77 (0.109)</td></tr><tr><td>2</td><td>(15/45/--45/15/45/15/--45/45/15)S</td><td>LT</td><td>100. (4.0)</td><td>25. (1.0)</td><td>2.18 (0.086)</td></tr><tr><td>3</td><td>(45*2/0/45*3/90/45)S</td><td>LT</td><td>100. (4.0)</td><td>50. (2.0)</td><td>1.96 (0.077)</td></tr><tr><td rowspan="2">4</td><td rowspan="2">((45/0)*3/45/90)S</td><td>LT</td><td>100. (4.0)</td><td>25. (1.0)</td><td>1.96 (0.077)</td></tr><tr><td>TT</td><td>100. (4.0)</td><td>50. (2.0)</td><td>2.01 (0.079)</td></tr><tr><td rowspan="2">5</td><td rowspan="2">(0*2/45/0*3/90/0)S</td><td>LT</td><td>100. (4.0)</td><td>25. (1.0)</td><td>1.96 (0.077)</td></tr><tr><td>TT</td><td>100. (4.0)</td><td>50. (2.0)</td><td>1.96 (0.077)</td></tr><tr><td>6</td><td>(+45/0/90*2/0/--+45)S</td><td>LT</td><td>100. (4.0)</td><td>25. (1.0)</td><td>1.98 (0.078)</td></tr></table>

a LT = Longitudinal Tension (i.e. along the laminate reference axis).  
LC = Longitudinal Compression.  
TT = Transverse Tension (i.e. perpendicular to the laminate reference axis.)   
b Overall length of the tensile specimens, including tabs, is 230 mm (9 inch).   
Overall length of the compression specimen, including tabs, is 100 mm (4 inch).   
L = Gage length of specimen.  
W = Specimen width.  
T = Specimen thickness.

TABLE B.2. MEASURED AND PREDICTED FAILURE LOADS OF THE LAMINATE SPECIMENS   

<table><tr><td rowspan="3">Laminate</td><td rowspan="3">\( Test^{a} \)Type</td><td rowspan="3">\( Spec. No. \)</td><td colspan="4">Failure Load, kN</td></tr><tr><td rowspan="2">Measured Load</td><td colspan="3">Predicted Load</td></tr><tr><td>Tsai-Wu</td><td>Hashin</td><td>Max. Strain</td></tr><tr><td rowspan="4">0</td><td rowspan="4">LT</td><td>1</td><td>36.1</td><td rowspan="4">22.7 (-30)b</td><td rowspan="4">27.0 (-16)</td><td rowspan="4"></td></tr><tr><td>2</td><td>30.8</td></tr><tr><td>3</td><td>31.2</td></tr><tr><td>4</td><td>31.2</td></tr><tr><td rowspan="3">0</td><td rowspan="3">LC</td><td>1</td><td>19.2</td><td rowspan="3">24.7 (35)</td><td rowspan="3">15.1 (-18)</td><td rowspan="3"></td></tr><tr><td>2</td><td>17.8</td></tr><tr><td>3</td><td>18.0</td></tr><tr><td rowspan="4">0</td><td rowspan="4">TT</td><td>1</td><td>47.8</td><td rowspan="4">37.2 (-22)</td><td rowspan="4">34.5 (-27)</td><td rowspan="4"></td></tr><tr><td>2</td><td>50.2</td></tr><tr><td>3</td><td>44.3</td></tr><tr><td>4</td><td>47.3</td></tr><tr><td rowspan="3">2</td><td rowspan="3">LT</td><td>1</td><td>29.3</td><td rowspan="3">37.3 (31)</td><td rowspan="3"></td><td rowspan="3">48.1 (67)</td></tr><tr><td>2</td><td>26.3</td></tr><tr><td>3</td><td>29.9</td></tr><tr><td rowspan="3">3</td><td rowspan="3">LT</td><td>1</td><td>19.4</td><td rowspan="3">22.4 (11)</td><td rowspan="3"></td><td rowspan="3">30.5 (52)</td></tr><tr><td>2</td><td>20.7</td></tr><tr><td>3</td><td>20.2</td></tr><tr><td rowspan="3">4</td><td rowspan="3">LT</td><td>1</td><td>26.3</td><td rowspan="3">27.7 (0)</td><td rowspan="3"></td><td rowspan="3">35.1 (26)</td></tr><tr><td>2</td><td>27.4</td></tr><tr><td>3</td><td>29.6</td></tr><tr><td rowspan="3">4</td><td rowspan="3">TT</td><td>1</td><td>19.4</td><td rowspan="3">22.6 (5)</td><td rowspan="3"></td><td rowspan="3">30.0 (40)</td></tr><tr><td>2</td><td>22.9</td></tr><tr><td>3</td><td>22.0</td></tr><tr><td rowspan="4">5</td><td rowspan="4">LT</td><td>1</td><td>62.2</td><td rowspan="4">56.0 (-1)</td><td rowspan="4"></td><td rowspan="4">64.1 (13)</td></tr><tr><td>2</td><td>52.0</td></tr><tr><td>3</td><td>51.9</td></tr><tr><td>4</td><td>61.1</td></tr><tr><td rowspan="3">5</td><td rowspan="3">TT</td><td>1</td><td>18.8</td><td rowspan="3">21.2 (33)</td><td rowspan="3"></td><td rowspan="3">27.5 (72)</td></tr><tr><td>2</td><td>15.7</td></tr><tr><td>3</td><td>13.5</td></tr><tr><td rowspan="3">6</td><td rowspan="3">LT</td><td>1</td><td>27.9</td><td rowspan="3">30.5 (19)</td><td rowspan="3"></td><td rowspan="3">32.3 (25)</td></tr><tr><td>2</td><td>21.1</td></tr><tr><td>3</td><td>28.0</td></tr></table>

a LT = Longitudinal Tension (i.e. along the laminate reference axis). LC = Longitudinal Compression. TT = Transverse Tension (i.e. perpendicular to the laminate reference axis.)   
b Numbers in parentheses are the differences between the average measured load and the predicted load, as a percentage of the average measured load.

图片摘要：该图主要展示 B.2. MEASURED AND PREDICTED FAILURE LOADS OF THE LAMINATE SP。
![](images/d5e6d721e5aba734786be3782d269b0c80005d949a297b5f0ff55d25d6b845aa.jpg)

图片摘要：该图主要展示 B.1. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/5180ad6be6c1fe73ab66dc8c7e4a1ba455d0759d6a1ab8883f3505fe794da035.jpg)  
FIGURE B.1. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.1. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/2ec61be4c5c1265e9d7db832d8273c1a1b4eae8698142bbf6f5de4190f1bd732.jpg)  
FIGURE B.1. - CONTINUED. (C) STRAINS ARE MEASURED AT -45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.1. CONTINUED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO TH。
![](images/39771f321195da98eafb21b390f76a74a25cb73c3c910e093320c8b6b7e59702.jpg)  
FIGURE B.1. - CONCLED. (D) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.1. CONCLED. (D) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/e818c35ec7a318db957c53c694865f3ac89fa0c592e689e6cde0145daceb62c9.jpg)  
FIGURE B.2. COMPRESSION TESTS OF LAMINATE 0, $(+ - 50 / 35 / - + 50)*4$   
LOAD APPLIED ALONG THE LAMINATE REFERENCE AXIS.   
(A) STRAINS ARE MEASURED PARALLEL TO THE LOAD.

图片摘要：该图主要展示 B.2. COMPRESSION TESTS OF LAMINATE 0,。
![](images/7577fd6c83b3580b686df554fb58f1b85cff5dda91cee5699af7c6e6ebb87d5f.jpg)  
FIGURE B.2. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.2. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/4cf39bd448938925adc22b17449bc67206407fcffbf82fddd2b4d1a47f6ce7a9.jpg)  
FIGURE B.2. - CONTINUED. (C) STRAINS ARE MEASURED AT -45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.2. CONTINUED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO TH。
![](images/39952491e3c51d41507e01d07649cda8192b0ffaf4db56295c1b862cf8bf1b0b.jpg)  
FIGURE B.2. - CONCLED. (D) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.2. CONCLED. (D) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/ba83df0d6ae23db5a7c6c90bccad827c0079de75685280da61a5d672a8697b5b.jpg)

图片摘要：该图主要展示 B.2. CONCLED. (D) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/aaec42651e6de6f11efd11aa6606fd72606e519f73e9a356c685262fd58a5fe1.jpg)  
FIGURE B.3. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.3. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/abe5d50cf17cd2e3f7cd19d1efe1ac15447a2a07c75a6b3b2969218896a1e78b.jpg)  
FIGURE B.3. - CONTINUED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.3. CONTINUED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO TH。
![](images/7296b589cb739b442e4cb079b1186761e13af8f35c71ddfd9e481f07e7e58042.jpg)  
FIGURE B.3. - CONCLED. (D) STRAINS ARE MEASURED AT -45 DEGREES TO THE LOAD.

STRAIN, MICROSTRAIN   
图片摘要：该图主要展示 B.3. CONCLED. (D) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/65fbe302a1829a0a13193a0404aa3e05acdfea59f3cba7b72157b5c6013cc1a7.jpg)  
FIGURE B.4. TENSION TESTS OF LAMINATE 2, (15/45/-45/15/45/15/-45/45/15)*S   
(HIMAT CANARD). LOAD APPLIED ALONG THE LAMINATE REFERENCE AXIS.   
(A) STRAINS ARE MEASURED PARALLEL TO THE LOAD.

图片摘要：该图主要展示 B.4. TENSION TESTS OF LAMINATE 2, (15/45/ 45/15/45/15/ 45/45。
![](images/524fce61bc8f7df142338e56b1d5730cd89f08f9dac06c8b81230963e0672933.jpg)  
FIGURE B.4. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.4. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/127afa5e9d1b9e01b6cbce89b5e664fa4f081b0776c99164feb13aebbf675a5e.jpg)  
FIGURE B.4. - CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.4. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/f240be143bfe4fad90471b2c393c1ff4d48df8001e636ca375da73168b6778f6.jpg)  
FIGURE B.5. TENSION TESTS OF LAMINATE 3, (45*2/0/45*3/90/45)*S. LOAD APPLIED ALONG THE LAMINATE REFERENCE AXIS.  
(A) STRAINS ARE MEASURED PARALLEL TO THE LOAD.

图片摘要：该图主要展示 B.5. TENSION TESTS OF LAMINATE 3, (45 2/0/45 3/90/45) S. LOA。
![](images/38e99052cb06f2531626a04351caffc38082e7741e04e26692e2ec4755439b64.jpg)  
FIGURE B.5. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.5. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/a766e749a56d1f218d8459ffb1d7f9cd3458e7011d061e5a14dd29fa1d7ea728.jpg)  
FIGURE B.5. - CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.5. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/f0b984abdb86d642a2123f906a899ad44d6bcf0bafcf3a8cbc93529450b2702f.jpg)  
FIGURE B.6.TENSION TESTS OF LAMINATE 4. $(45 / 0)*3 / 45 / 90)\ast S$   
LOAD APPLIED ALONG THE LAMINATE REFERENCE AXIS.   
(A) STRAINS ARE MEASURED PARALLEL TO THE LOAD.

图片摘要：该图主要展示 B.6.TENSION TESTS OF LAMINATE 4。
![](images/4e11da075f0d2ce031096887a153a98055aab71b91f0c448a20453ae5890f2af.jpg)  
FIGURE B.6. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.6. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/135f1e1b615d16fc92baeb30fbd3a5ae3672bf45ade6bb056d092b8a21cbc75f.jpg)  
FIGURE B.6. - CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.6. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/21fac5fc19b7a8c8260230a675b7f663b045de4e1f236d528aeab6f2b4a08d59.jpg)

图片摘要：该图主要展示 B.6. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/3a5f73c7738f3d27fe4665fb3dfdf19c819967090c71a073f7dad59b1c6da947.jpg)  
FIGURE B.7. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.7. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/a952c4e361053b754aa69e315e9082e52a61d5ba6ea4fb380418ac9160806d99.jpg)  
FIGURE B.7. - CONCLED. (C) STRAINS ARE MEASURED AT -45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.7. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/6d754bb91529bfb93a36b48dc40def294e749fae1e01e8719b2eeffbd4e26677.jpg)

图片摘要：该图主要展示 B.7. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/6dc7bf2276f36411288a39f2026ed8f5c479f9edf9c22cda386b381340530eda.jpg)

图片摘要：该图主要展示 B.7. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/a07e63c586b2ba0d77264f72c881ddf5c3abbfde299b127c8eb50acc5c474262.jpg)  
FIGURE B.8. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.8. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/02867897e6fd9ec7217f8cb3c009f880f681a90ac1fbc39af9654c037a69aa5a.jpg)  
FIGURE B.8. - CONCLED. (C) STRAINS ARE MEASURED AT -45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.8. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/bccceb4a03c2f337ac86a026e555e53faadac1feaf17690a633463b4d70ba8d0.jpg)  
FIGURE B.9. TENSION TESTS OF LAMINATE 5, (0*2/45/0*3/90/0)*S.   
LOAD APPLIED AT 90 DEGREES TO THE LAMINATE REFERENCE AXIS.   
(A) STRAINS ARE MEASURED PARALLEL TO THE LOAD.

图片摘要：该图主要展示 B.9. TENSION TESTS OF LAMINATE 5, (0 2/45/0 3/90/0) S。
![](images/377e174245559552c7ce6485a38de8806b587741f27842b516c9ed184dc491e1.jpg)  
FIGURE B.9. - CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.9. CONTINUED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO TH。
![](images/504edd190ada79ebb92ac716a3e493a007b85ca6d0df3b0284b803bfe2cb88e3.jpg)  
FIGURE B.9. - CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE LOAD.

图片摘要：该图主要展示 B.9. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/f8b6c578f2e8fc5c49fe5494eb990344428da08478ba76cb05933fdd26215819.jpg)

图片摘要：该图主要展示 B.9. CONCLED. (C) STRAINS ARE MEASURED AT 45 DEGREES TO THE 。
![](images/4a19b31259dd11aac6fce841c6b93c2b8dacd49abe67d0f98fb6961330d9348b.jpg)  
FIGURE B.10. - CONCLED. (B) STRAINS ARE MEASURED AT 90 DEGREES TO THE LOAD.

# REFERENCES

1. Price, M.A.: HiMAT Structural Development Design Methodology. NASA CR-144886, 1979.   
2. Monaghan, Richard C.: Description of the HiMAT Tailored Composite Structure and Laboratory Measured Vehicle Shape under Load. NASA TM-81354, 1981.   
3. Petit, P.H.; and Waddoups, M.E.: A Method of Predicting the Nonlinear Behavior of Laminated Composites. J. Composite Mats., vol. 3, Jan. 1969, pp. 2-19.   
4. Hashin, Zvi; Bagchi, Debal; and Rosen, B. Walter: Non-linear Behavior of Fiber Composite Laminates. NASA CR-2313, 1974.   
5. Ramberg, Walter; and Osgood, William R.: Description of Stress-Strain Curves by Three Parameters. NACA-TN-902, 1943.   
6. Jones, Robert M.; Mechanics of Composite Materials. McGraw-Hill Book Co., 1975, pp. 147-156.   
7. Sefic, Walter J.: NASA Dryden Flight Loads Research Facility. NASA TM-81368, 1981.   
8. "Structural Criteria for Advanced Composites", AFFDL-TR-76-142, Northrop Corporation/Aircraft Division, March 1977.   
9. Kerr, J.R.; Haskins, J.F.: "Time-Temperature-Stress Capabilities of Composite Materials for Advanced Supersonic Technology Applications", NASA CR-159267, General Dynamics/Convair Aerospace Division, April 1980.   
10. DOD/NASA Advanced Composites Design Guide. Vols. I-IV. Air Force Wright Aeronautical Laboratories, Wright-Patterson Air Force Base, July 1983. (Primary source - Development of a Low-Cost Composite Vertical Stabilizer", AFFDL-TR-78-5, Rockwell International/Los Angeles Aircraft Division, June 1978.)   
ll. Kim, R.Y., "On the Off-Axis and Angle-Ply Strength of Composites", Test Methods and Design Allowables for Fibrous Composites, ASTM STP 734, C.C. Chamis, Ed., American Society for Testing and Materials, 1981, pp. 91-108.   
12. Grimes, G.C., "Experimental Study of Compression-Compression Fatigue of Graphite/Epoxy Composites", Test Methods and Design Allowables for Fibrous Composites, ASTM STP 734, C.C. Chamis, Ed., American Society for Testing and Materials, 1981, pp. 281-337.

13. Lagace, Paul A., "Nonlinear Stress-Strain Behavior of Graphite/Epoxy Laminates", Presented at AIAA/ASME/ ASCE/AHS 25th Structures, Structural Dynamics and Materials Conference, Palm Springs, California; AIAA Paper No. 84-0860-CP. Also available from Technology Laboratory for Advanced Composites, MIT, as TELAC Report 84-7.   
14. Sandhu, R.S. and Sendeckyj, G.P., "On Design of Off-Axis Specimens", AFWAL-TR-84-3098, March 1985, Flight Dynamics Laboratory, Air Force Wright Aeronautical Laboratories.   
15. Anonymous, "Magnamite AS4/3501-6 Graphite Prepreg Tape and Fabric Module"; undated; published by Hercules Incorporated, Magna, Utah.   
16. Whitney, James M., Daniel, Isaac M., and Pipes, R. Byron, Experimental Mechanics of Fiber Reinforced Composite Materials, SESA Monograph No. 4, The Society for Experimental Stress Analysis, 1982.   
17. Tsai, Stephen W.; and Wu, Edward M., "A General Theory of Strength for Anisotropic Materials", J. Composite Mats., vol. 5, no. 1, Jan. 1971, pp. 58-80.   
18. Hashin, Z.; and Rotem, A., "A Fatigue Failure Criterion for Fiber Reinforced Materials", J. Composite Mats., vol. 7, Oct. 1973, pp. 448-464.   
19. Narayanaswami, R.; and Adelman, Howard M., "Evaluation of the Tensor Polynomial and Hoffman Strength Theories for Composite Materials", J. Composite Mats., vol. 11, Oct. 1977, pp. 366-377.   
20. Hahn, H.T.; and Tsai, S.W., "On the Behavior of Composite Laminates After Initial Failures", J. Composite Mats., vol. 8, July 1974, pp. 288-305.   
21. Hofer, K.E., Jr.; and Rao, P.N., "A New Static Compression Fixture for Advanced Composite Materials", J. Testing & Evaluation, vol. 5, no. 4, July 1977, pp. 278-283.

TABLE I. - HiMAT WING TEST SUMMARY   

<table><tr><td rowspan="2">Test</td><td rowspan="2">Peak Load Nominal</td><td rowspan="2">kN (1b) Actual</td><td colspan="2">Time, sec.</td><td rowspan="2">Notes</td></tr><tr><td>Rise</td><td>Decay</td></tr><tr><td>1</td><td>4.45 (1000)</td><td>4.48 (1010)</td><td>61.</td><td>58.</td><td>(1)</td></tr><tr><td>2</td><td>4.45 (1000)</td><td>4.49 (1010)</td><td>54.</td><td>59.</td><td>(2)</td></tr><tr><td>3</td><td>4.45 (1000)</td><td>4.53 (1020)</td><td>56.</td><td>57.</td><td>(3)</td></tr><tr><td>4</td><td>4.45 (1000)</td><td>4.34 (975)</td><td>58.</td><td>60.</td><td>(4)</td></tr><tr><td>5</td><td>4.45 (1000)</td><td>4.31 (970)</td><td>24.</td><td>24.</td><td>(5)</td></tr><tr><td>6</td><td>4.45 (1000)</td><td>4.36 (980)</td><td>61.</td><td>60.</td><td>(6)</td></tr><tr><td>7</td><td>4.45 (1000)</td><td>4.46 (1000)</td><td>25.</td><td>24.</td><td>(7)</td></tr><tr><td>8</td><td>6.67 (1500)</td><td>6.65 (1490)</td><td>36.</td><td>36.</td><td></td></tr><tr><td>9</td><td>4.45 (1000)</td><td>4.45 (1000)</td><td>36.</td><td>36.</td><td>(8)</td></tr><tr><td>10</td><td>8.90 (2000)</td><td>8.93 (2010)</td><td>49.</td><td>48.</td><td></td></tr><tr><td>11</td><td>4.45 (1000)</td><td>4.11 (925)</td><td>50.</td><td>45.</td><td>(8)</td></tr><tr><td>12</td><td>11.1 (2500)</td><td>11.0 (2470)</td><td>61.</td><td>59.</td><td></td></tr><tr><td>13</td><td>4.45 (1000)</td><td>4.37 (980)</td><td>26.</td><td>24.</td><td>(8)</td></tr><tr><td>14</td><td>13.3 (3000)</td><td>13.3 (2990)</td><td>73.</td><td>72.</td><td></td></tr><tr><td>15</td><td>4.45 (1000)</td><td>4.45 (1000)</td><td>24.</td><td>24.</td><td>(8)</td></tr><tr><td>16</td><td>15.6 (3500)</td><td>15.5 (3480)</td><td>85.</td><td>84.</td><td></td></tr><tr><td>17</td><td>4.45 (1000)</td><td>4.45 (1000)</td><td>24.</td><td>24.</td><td>(8)</td></tr><tr><td>18</td><td>17.8 (4000)</td><td>17.7 (3990)</td><td>97.</td><td>96.</td><td></td></tr><tr><td>19</td><td>4.45 (1000)</td><td>4.45 (1000)</td><td>24.</td><td>25.</td><td>(8)</td></tr><tr><td>20</td><td>4.45 (1000)</td><td>4.71 (1060)</td><td>27.</td><td>26.</td><td>(9)</td></tr><tr><td>21</td><td>20.0 (4500)</td><td>19.2 (4310)</td><td>106.</td><td>105.</td><td></td></tr><tr><td>22</td><td>4.45 (1000)</td><td>4.51 (1010)</td><td>25.</td><td>25.</td><td>(8)</td></tr><tr><td>23</td><td>22.2 (5000)</td><td>21.6 (4850)</td><td>117.</td><td>116.</td><td></td></tr><tr><td>24</td><td>4.45 (1000)</td><td>4.43 (995)</td><td>24.</td><td>24.</td><td>(8)</td></tr><tr><td>25</td><td>17.8 (4000)</td><td>17.6 (3950)</td><td>96.</td><td>95.</td><td></td></tr><tr><td>26</td><td>4.45 (1000)</td><td>4.49 (1010)</td><td>24.</td><td>24.</td><td>(8)</td></tr><tr><td>27</td><td>24.5 (5500)</td><td>22.0 (4950)</td><td>117.</td><td>1.</td><td>(10)</td></tr></table>

(1) Complete outer wing; load rate $= 4.45 \, \text{kN/min}$ .   
(2) Leading edge removed.   
(3) Configuration as per Test 2, but with elevon removed.   
(4) Configuration as per Test 3, but with aileron removed; i.e. wing box only.   
(5) Load rate = 11.1 kN/min.   
(6) 1 hydraulic cylinder @ 4.45 kN/min.   
(7) 1 hydraulic cylinder @ 11.1 kN/min.   
(8) Posttest damage evaluation.   
(9) Benchmark test; to be compared with Test 19.   
(10) Root rib/mounting lug bolt shear failure.

图片摘要：该图主要展示 1. HiMAT tailored composite wing. Dimensions in centimeters 。
![](images/2b2f1a00ab74d92257703ec4352b35509cb02e0b5c00a1262c948d10859a42d6.jpg)  
Figure 1. HiMAT tailored composite wing. Dimensions in centimeters (inches).

图片摘要：该图主要展示 1. HiMAT tailored composite wing. Dimensions in centimeters 。
![](images/34ebae9269843f0d5ddd90080fe6296006b334ec117b3770c2900b3956e865e5.jpg)  
(b)Structural box.   
Figure 1. Continued.

图片摘要：该图主要展示 1. Continued。
![](images/f0c0ce5fd1cd57b1b55cb5a722c6794346be8e5de48d52c104c21c1f7312246b.jpg)  
(c) Aileron, elevon, and leading edge structure.   
Figure 1. Concluded.   
ORIGINAL PAGE IS OF POOR QUALITY

(a) Isometric view.   
图片摘要：该图主要展示 1. Concluded。
![](images/f375d8bf84e2230926b6fb7c777b9102050ad7df5f3db1e18a031823e46c301c.jpg)  
Figure 2. NASTRAN structural model of the HiMAT outer wing.

图片摘要：该图主要展示 2. NASTRAN structural model of the HiMAT outer wing。
![](images/8dc24b2c9a546285ae8cf1071eecd48d5a3d00bb3b3a51ae95baa980acef6d30.jpg)  
(b) Plan view. For clarity node numbers in root region are omitted.   
Figure 2. Concluded.

图片摘要：该图主要展示 2. Concluded。
![](images/03f8a2420c34c1c72e566a7ce825280802b29a31b41700e3cdcca5a4b4024552.jpg)  
Figure 3. Flow diagram for the files and programs used in the incremental loads analysis.

图片摘要：该图主要展示 3. Flow diagram for the files and programs used in the incre。
![](images/ca7226e5c80bf0a404bd1b483fb9d25a67f42a0a98a7ce7b3ac1d8eea29f4bb8.jpg)  
Figure 4. HiMAT outer wing box showing the location of test instrumentation: three-  
element strain rosettes (K), single-element strain gages (-), and   
displacement transducers ( ). Hidden instrumentation is shown by   
symbols with dotted and dashed lines.

图片摘要：该图主要展示 4. HiMAT outer wing box showing the location of test instrum。
![](images/c26c40f3709fee4ee035fc0fad2d2e772830031ea3828da4e653e99687184c72.jpg)  
FIGURE 5. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE LEADING EDGE OF THE WING BOX. TESTS 1, 4 AND 7.

图片摘要：该图主要展示 5. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE LEADI。
![](images/6be656ccf0f8751be17705f63a8f6dffadd9c5b63ed1575290efb114a860d86b.jpg)  
FIGURE 6. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE TRAILING EDGE OF THE WING BOX. TESTS 1, 4 AND 7.

图片摘要：该图主要展示 6. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE TRAIL。
![](images/d19a1100cf1c98dd2b607fb29b0485f07ad142e39ae016f94932710bd01922cd.jpg)  
FIGURE 7. MEASURED AND PREDICTED STRAIN FOR ROSETTE 712. TESTS 1, 4 AND 7.

图片摘要：该图主要展示 7. MEASURED AND PREDICTED STRAIN FOR ROSETTE 712. TESTS 1, 4。
![](images/98229bcb7d391961a4b7b385e4c5346ff545aa279702b875fda18c5455e16b9f.jpg)  
FIGURE 8. MEASURED AND PREDICTED STRAIN FOR ROSETTE 612. TESTS 1, 4 AND 7.

图片摘要：该图主要展示 8. MEASURED AND PREDICTED STRAIN FOR ROSETTE 612. TESTS 1, 4。
![](images/6e76121f5bece0416b69325f39fe69fd832d50dd337fffd97e48a86443c21490.jpg)  
FIGURE 9. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE   
LEADING EDGE OF THE WING BOX. TESTS 7 AND 26.

图片摘要：该图主要展示 9. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE。
![](images/5e162b1fb62d81c2487e544a926efd7b24f92a16e9e70ba18484e67998ec5cde.jpg)  
FIGURE 10. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE TRAILING EDGE OF THE WING BOX. TESTS 7 AND 26.

图片摘要：该图主要展示 10. MEASURED AND PREDICTED DEFLECTION OF THE TIP OF THE TRAI。
![](images/81b5927e0ffa48764a77787e2346fcc963a8ed006564fd071b7c0730ebab9d1a.jpg)  
FIGURE 11. MEASURED AND PREDICTED STRAIN FOR ROSETTE 712. TESTS 7 AND 26.

图片摘要：该图主要展示 11. MEASURED AND PREDICTED STRAIN FOR ROSETTE 712. TESTS 7 A。
![](images/9c476688535df1c035ee51ac6a316de5c3f5e7391ad2da1864dfdf1fa188b7e5.jpg)  
FIGURE 12. MEASURED AND PREDICTED STRAIN FOR ROSETTE 612. TESTS 7 AND 26.

APPLIED LOAD   
图片摘要：该图主要展示 12. MEASURED AND PREDICTED STRAIN FOR ROSETTE 612. TESTS 7 A。
![](images/492330095d913f771b1c32fac6df2a3a2eb47ce236375d1077806b5476ba824a.jpg)  
FIGURE 13. TIP DEFLECTION OF THE LEADING EDGE SPAR OF THE WING BOX VERSUS LOAD FOR THE 27 LOAD TESTS. TESTS ARE PLOTTED IN SEQUENCE WITH SHIFTS IN THE LOAD AXIS.

APPLIED LOAD   
图片摘要：该图主要展示 13. TIP DEFLECTION OF THE LEADING EDGE SPAR OF THE WING BOX 。
![](images/545b75cd55660a2f82bf31b87b003da418d5e17ba2c384901c4df826abe74be8.jpg)  
FIGURE 14. TIP DEFLECTION OF THE TRAILING EDGE SPAR OF THE WING BOX   
VERSUS LOAD FOR THE 27 LOAD TESTS. TESTS ARE PLOTTED IN   
SEQUENCE WITH SHIFTS IN THE LOAD AXIS.

APPLIED LOAD   
图片摘要：该图主要展示 14. TIP DEFLECTION OF THE TRAILING EDGE SPAR OF THE WING BOX。
![](images/40e57b621846d06bb58b14b0ee9bfc0f3fd7bbc79bfa58fbcf02f1fe02aece4a.jpg)  
FIGURE 15. STRAIN IN GAGE 712A VERSUS LOAD FOR THE 27 LOAD TESTS. TESTS ARE PLOTTED IN SEQUENCE WITH SHIFTS IN THE LOAD AXIS.

APPLIED LOAD   
图片摘要：该图主要展示 15. STRAIN IN GAGE 712A VERSUS LOAD FOR THE 27 LOAD TESTS. T。
![](images/271b949d216aabeb22cf15f7a3ecf6188774688c04f643e9c5b15b6d0aae229f.jpg)  
FIGURE 16. STRAIN IN GAGE 612A VERSUS LOAD FOR THE 27 LOAD TESTS.   
TESTS ARE PLOTTED IN SEQUENCE WITH SHIFTS IN THE   
LOAD AXIS.

图片摘要：该图主要展示 16. STRAIN IN GAGE 612A VERSUS LOAD FOR THE 27 LOAD TESTS。
![](images/a821476128611b2c46e26b0acf3a0c4b330a8ebda1aee6857e82bb2c4ccc1bf0.jpg)

# ORIGINAL PAGE IS OF POOR QUALITY

图片摘要：该图主要展示 16. STRAIN IN GAGE 612A VERSUS LOAD FOR THE 27 LOAD TESTS。
![](images/bf8d78b4601bd74711de2c1e96b833e5865789ae8dba6279d7ed64d7ec628774.jpg)  
Figure 17. Wing box subjected to an approximate load of $18\mathrm{kN}$ (4000 lb) during Test 21.

图片摘要：该图主要展示 17. Wing box subjected to an approximate load of (4000 lb) d。
![](images/b15c56371ae55b93bbfc419206f28ed6029f2e973af64cfc18516b4acdb0be61.jpg)  
ORIGINAL PAGE IS OF POOR QUALITY

图片摘要：该图主要展示 17. Wing box subjected to an approximate load of (4000 lb) d。
![](images/380a0e131466039b8509d6faaa5c9580f208639f00f97823b2b17decf8320010.jpg)

图片摘要：该图主要展示 17. Wing box subjected to an approximate load of (4000 lb) d。
![](images/ab8aa9f0ddabddb182987ead5280898502157fce744eb3f24560d276ec0ef8e5.jpg)

图片摘要：该图片与Figure 18. Measured and predicted strain for the strain gages on the bottom surf这部分内容相关。
![](images/92b710f289047b74f4e8b96e12cf3390e71546b60bdcc63f8a98daa496ff20da.jpg)

图片摘要：该图片与Figure 18. Measured and predicted strain for the strain gages on the bottom surf这部分内容相关。
![](images/8057e3aa37372801994f8b87e69e10770878c15ef6f33e576719548180c386d5.jpg)

图片摘要：该图主要展示 18. Measured and predicted strain for the strain gages on th。
![](images/891b060d67caa254adcd87f8456f6b3044a0321435142d85af8083a4eb1eaad9.jpg)  
Figure 18. Measured and predicted strain for the strain gages on the bottom surface of the wing.

图片摘要：该图主要展示 18. Measured and predicted strain for the strain gages on th。
![](images/cc060e1001c694958d09270f15d4261c7da6bd7d15bcb9a94c987fb52c0817a0.jpg)  
ORIGINAL PAGE IS OF POOR QUALITY

图片摘要：该图主要展示 18. Measured and predicted strain for the strain gages on th。
![](images/d039edd36d2392c7145cdc92291824fda43c0fc7f1113ab55d572a796a774f17.jpg)

图片摘要：该图主要展示 18. Measured and predicted strain for the strain gages on th。
![](images/7ba714aee983b09865e6c3da569c07cfab021557ea443cbf6e981a721c6d7f3d.jpg)

图片摘要：该图片与Figure 18. Concluded；ORIGINAL PAGE IS OF POOR QUALITY这部分内容相关。
![](images/4868a896682d2e589cc95750feddd5450eedb5c418bf88a652c81952b4dd181d.jpg)

图片摘要：该图片与Figure 18. Concluded；ORIGINAL PAGE IS OF POOR QUALITY这部分内容相关。
![](images/98865bf7dc8be5161f0cbaae5fc7c186a6aea6644206eb41b6027cea77906b73.jpg)

图片摘要：该图主要展示 18. Concluded。
![](images/e76e0fd729039ad33afc2e18875368b083dd562f9af77225100c8ab57e19cf13.jpg)  
Figure 18. - Concluded.

图片摘要：该图主要展示 18. ConcludedORIGINAL PAGE IS OF POOR QUALITY。
![](images/7351f64b7fc0dd6cde1671476994225e262baa5dbafc3b49c698d126c4105c5f.jpg)  
ORIGINAL PAGE IS OF POOR QUALITY

图片摘要：该图主要展示 18. Concluded。
![](images/08cdcb24b749a305e45f95358d432301c2aa24ce41daa51ff76f26a1801a70ec.jpg)

图片摘要：该图主要展示 18. Concluded。
![](images/49647270c8da4b0dcb5e829471916b9774c6dafe5c24acceb83b76532f15c68d.jpg)

图片摘要：该图片与Figure 19. Measured and predicted strain for the strain gages on the top surface这部分内容相关。
![](images/dd0f90f7e473e84f70ff5b538955b163766e0d41a3bb6476ef10ab8ae34ea1d3.jpg)

图片摘要：该图片与Figure 19. Measured and predicted strain for the strain gages on the top surface这部分内容相关。
![](images/bafda5fa1c11a96f8687f107bc410ddb52f66530146374749b71cdf036148784.jpg)

图片摘要：该图主要展示 19. Measured and predicted strain for the strain gages on th。
![](images/611d94fee6a19f49f4ca6092f9dd855831a274eceb795e83dc28e85c0b1956af.jpg)  
Figure 19. Measured and predicted strain for the strain gages on the top surface of the wing.

图片摘要：该图主要展示 19. Measured and predicted strain for the strain gages on th。
![](images/e9a8d48091ef65c2a1fb5b3ac3935c4db6204ebc3dffb1a4944e94dfc5f2853d.jpg)  
ORIGINAL PAGE IS OF POOR QUALITY

图片摘要：该图主要展示 19. Measured and predicted strain for the strain gages on th。
![](images/e92859f9d012030ae3b1c949d3a3f8141eb8847e9c114645be6efd31a9b7214c.jpg)

图片摘要：该图主要展示 19. Measured and predicted strain for the strain gages on th。
![](images/6b1aa54f2be5e613f0f160d678a75d82734c187687362a3cd54d47c0bdb40ce4.jpg)

图片摘要：该图片与Figure 19. Concluded；FIGURE 20. MEASURED AND PREDICTED DEFLECTION OF THE TIP这部分内容相关。
![](images/87f0fdf24cc491fb5ac2680e143544331545df9abcbd57f40c839d3fc0eecfe2.jpg)

图片摘要：该图片与Figure 19. Concluded；FIGURE 20. MEASURED AND PREDICTED DEFLECTION OF THE TIP这部分内容相关。
![](images/81df94d770452f54db43e9506dfa41db1a3899928bcf5b70db9d0b95f11aa870.jpg)

图片摘要：该图主要展示 19. Concluded。
![](images/ab739e0ef897e14deaf786ad33641882a4fef597aabff08694743b99be8a364f.jpg)  
Figure 19. - Concluded.

图片摘要：该图主要展示 19. ConcludedFIGURE 20. MEASURED AND PREDICTED DEFLECTION OF。
![](images/270e9b54902c8988107b993d34e43332e54f7403578247ceafa76a5582c1c363.jpg)  
FIGURE 20. MEASURED AND PREDICTED DEFLECTION OF THE TIP   
OF THE LEADING EDGE OF THE WING BOX. TEST 21.

图片摘要：该图主要展示 20. MEASURED AND PREDICTED DEFLECTION OF THE TIP。
![](images/db77af67e6d665d843a11557381674d8e03d578a76ab1c6634ce8bb3225de543.jpg)  
FIGURE 21. MEASURED AND PREDICTED DEFLECTION OF THE TIP   
OF THE TRAILING EDGE OF THE WING BOX. TEST 21.

图片摘要：该图主要展示 21. MEASURED AND PREDICTED DEFLECTION OF THE TIP。
![](images/35f107faa3e19caa33f5523c9fc6c735a96164abe7d6b10b47e26c295d0d667b.jpg)  
FIGURE 22. DEFLECTION OF THE LEADING EDGE (LE) AND TRAILING EDGE (TE) SPARS FOR AN APPLIED LOAD OF 19.2 KN (4310 LB). TEST 21.

图片摘要：该图主要展示 22. DEFLECTION OF THE LEADING EDGE (LE) AND TRAILING EDGE (T。
![](images/5d64c5e5a159326686907263ae7bc3650f356ee76cb6059b5887a14d8b9e158c.jpg)  
HONI ' NOILDE

图片摘要：该图主要展示 22. DEFLECTION OF THE LEADING EDGE (LE) AND TRAILING EDGE (T。
![](images/df46f1b3dfd9bcbff95a943e6ade9a1da2ec5b86b6042912d81689c20cca28c7.jpg)  
ww NOILLDE   
FIGURE 23. PREDICTED DEFLECTION OF THE LEADING EDGE SPAR IN THE REGION OF THE BOLTED JOINT. APPLIED LOAD IS 19.2 KN (4310 LB).

图片摘要：该图主要展示 23. PREDICTED DEFLECTION OF THE LEADING EDGE SPAR IN THE REG。
![](images/4d0df7abe1774f181ca239d7bcff0913250055197d2ed34b7b5009a4b947e1ff.jpg)  
FIGURE 24. PREDICTED DEFLECTION OF THE TRAILING EDGE SPAR IN THE REGION OF THE BOLTED JOINT. APPLIED LOAD IS 19.2 KN (4310 LB).

<table><tr><td>1. Report No.
NASA CR-166617</td><td colspan="2">2. Government Accession No.</td><td colspan="2">3. Recipient&#x27;s Catalog No.</td></tr><tr><td rowspan="2" colspan="3">4. Title and Subtitle
Measured and Predicted Structural
Behavior of the HiMAT Tailored Composite Wing</td><td colspan="2">5. Report Date
March 1987</td></tr><tr><td colspan="2">6. Performing Organization Code</td></tr><tr><td rowspan="2" colspan="3">7. Author(s)
Lawrence H. Nelsen</td><td colspan="2">8. Performing Organization Report No.
H-1376</td></tr><tr><td colspan="2">10. Work Unit No.
RTOP 505-63-21</td></tr><tr><td rowspan="2" colspan="3">9. Performing Organization Name and Address
California Polytechnic State University
San Luis Obispo, California</td><td colspan="2">11. Contract or Grant No.
NCA2-6</td></tr><tr><td colspan="2">13. Type of Report and Period Covered
Contract Report-Final</td></tr><tr><td colspan="3">12. Sponsoring Agency Name and Address
National Aeronautics and Space Administration
Washington, DC 20546</td><td colspan="2">14. Sponsoring Agency Code</td></tr><tr><td colspan="5">Supplementary Notes
NASA Technical Monitor: Alan L. Carter, Ames Research Center,
Dryden Flight Research Facility, Edwards, California 93523-5000.</td></tr><tr><td colspan="5">16. Abstract
A series of load tests were conducted on the HiMAT tailored composite wing. Coupon tests
were also run on a series of unbalanced laminates, including the ply configuration of the wing.
The purpose of these tests was to compare the measured and predicted behavior of unbalanced
laminates, including - in the case of the wing - a comparison between the behavior of the full
scale structure and coupon tests. Both linear and nonlinear finite element (NASTRAN) analyses
were carried out on the wing. Both linear and nonlinear point-stress analyses were performed
on the coupons. All test articles were instrumented with strain gages. In addition, wing
deflections were measured.
The leading and trailing edges were found to have no effect on the response of the wing to
applied loads. A decrease in the stiffness of the wing box was evident over the 27-test pro-
gram. The measured load-strain behavior of the wing was found to be linear, in contrast to
coupon tests of the same laminate, which were nonlinear. A linear NASTRAN analysis of the wing
generally correlated more favorably with measurements than did a nonlinear analysis. A close
examination of the predicted deflections in the root region of the wing revealed an anomalous
behavior of the structural model that cannot presently be explained. Both hysteresis and creep
appear to be less significant in the wing tests than in the corresponding laminate coupon tests.</td></tr><tr><td colspan="2">17. Key Words (Suggested by Author(s))
Aeroelastic tailoring
Composite laminates
Composite structure
Graphite-epoxy
HiMAT structure</td><td colspan="3">18. Distribution Statement
Subject category 24</td></tr><tr><td>19. Security Classif. (of this report)
Unclassified</td><td colspan="2">20. Security Classif. (of this page)
Unclassified</td><td>21. No. of Pages
89</td><td>22. Price*
A05</td></tr></table>
