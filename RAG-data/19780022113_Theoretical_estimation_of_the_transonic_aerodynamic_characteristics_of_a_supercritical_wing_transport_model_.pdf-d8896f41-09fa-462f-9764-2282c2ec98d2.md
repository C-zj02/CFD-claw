LOAN COPY: RETURN AFWL TECHNICAL LIB KIRTLAND AFB, N:

SSEHETO

图片摘要：该图片为文档封面或首页内容，主题与Theoretical Estimation of the Transonic Aerodynamic Characteristics of a Supercritical Wing Transport Model With Trailing Edge Controls相关。
![](images/ab0fd3607dea25a7f0f9f116972929db01dcf17d291e09701291cb7bba034770.jpg)

NN 'Ee

Theoretical Estimation of the Transonic Aerodynamic Characteristics of a Supercritical-Wing Transport Model With Trailing-Edge Controls

James M. Luckring and Michael J. Mann

AUGUST 1978

# Theoretical Estimation of the Transonic Aerodynamic Characteristics of a Supercritical-Wing Transport Model With Trailing-Edge Controls

James M. Luckring and Michael J. Mann

Langley Research Center

Hampton, Virginia

# SUMMARY

This report presents a method for rapidly estimating the overall forces and moments at supercritical speeds, below drag divergence, of transport configurations with supercritical wings. The method is also used for estimating the rolling moments due to the deflection of wing trailing-edge controls. This analysis is based on a vortex-lattice technique modified to approximate the effects of wing thickness and boundary-layer-induced camber. Comparisons between the results of this method and experiment indicate reasonably good correlation of the lift, pitching moment, and rolling moment. The method required much less storage and run time to compute solutions over an angle-of-attack range than presently available transonic nonlinear methods require for a single angle-of-attack solution.

# INTRODUCTION

The development of the NASA supercritical airfoil has led to aircraft configurations which have demonstrated significant increases in drag divergence Mach number. (See refs. 1 to 4.) As part of this development effort, the results of an experimental study to determine the effects of wing trailing-edge control-surface deflections on the static transonic aerodynamic characteristics of a transport configuration with a supercritical wing have been reported in reference 5.

In recent years several three-dimensional transonic theories have been developed such as the methods due to Boppe (ref. 6), Bailey and Ballhaus (refs. 7 and 8), and Jameson (refs. 9, 10, and 11). These methods require large amounts of computer run time and storage compared with methods based on linear theory. Linear theory, of course, will not account for the nonlinear characteristics of the flow; however, linear theory can frequently be used to estimate certain aerodynamic quantities in the transonic range. Therefore, the present study was undertaken to determine whether linear theory could be used as a rapid method of estimating overall forces and moments (as opposed to detailed pressure distributions) of transport configurations at supercritical speeds. The method includes approximate corrections for the effects of wing thickness and boundary-layer displacement thickness. The analysis has been performed on the transonic transport configurations reported in reference 5 utilizing the vortex-lattice method of reference 12. In addition to calculating lift and pitching-moment characteristics, calculations were made to determine whether linear theory could be used to estimate the rolling moments due to wing trailing-edge control deflections. Because the experimental rolling-moment characteristics reported in reference 5 were obtained by deflecting control surfaces on only one wing, the theoretical method of reference 12 was particularly well suited for this study since calculations with this method may be performed on configurations which have an asymmetric geometry.

The method of reference 12 typically requires $65000_{8}$ storage and 17 seconds of execution time on the Control Data Corporation Cyber 175 system operating under NOS 1.1. This calculation would determine the force and moment characteristics over an entire angle-of-attack range. For the same computer system, the method of reference 9 would require approximately $240000_{8}$ storage and on the order of 90 minutes of computer time to calculate converged pressure distributions for only one angle of attack.

# SYMBOLS

The International System of Units, with the U.S. Customary Units presented in parenthesis, is used for the physical quantities found in this paper. Calculations were made in U.S. Customary Units. The data presented in this report are referenced to the stability-axis system. The moment reference point was taken to be the quarter chord of the mean aerodynamic chord of the reference trapezoidal wing planform.

b wing span, cm (in.)   
$\mathbf{C_L}$ lift coefficient, Lift/qS   
$\mathbf{C}_{\mathbf{L},\mathbf{o}}$ lift coefficient at zero angle of attack   
$\Delta c_{l}$ differential rolling-moment coefficient, defined to be the rollingmoment coefficient for a negative control deflection minus the rolling-moment coefficient for a positive control deflection of same magnitude for same control   
$C_{m}$ pitching-moment coefficient, Pitching moment/qSic   
$C_{m,0}$ pitching-moment coefficient at zero lift   
$C_{p,1}$ pressure coefficient on wing lower surface, $(p_1 - p_\infty) / q_\infty$   
$C_{p,u}$ pressure coefficient on wing upper surface, $(p_u - p_\infty) / q_\infty$   
$\Delta c_{p}$ $= c_{p,1} - c_{p,u}$   
c local chord, cm (in.)   
$\overline{\mathbf{c}}$ mean aerodynamic chord, cm (in.)   
$\mathbf{F_j}$ ith trailing-edge control surface (see fig. 1)   
$\mathbf{M}_{\infty}$ free-stream Mach number   
p local static pressure, Pa (lbf/ft2)   
$\mathbf{p}_{\infty}$ free-stream static pressure, Pa (lbf/ft²)

$q_{\infty}$ free-stream dynamic pressure, Pa (lbf/ft²)

S wing reference area of trapezoidal box extended to center line, m² (ft²)

Ulocal local streamwise surface velocity that differs from $\mathbf{U}_{\infty}$ due to thickness effects only, m/sec (ft/sec)

$\mathbf{U}_{\infty}$ free-stream velocity, m/sec (ft/sec)

u streamwise perturbation velocity due to thickness only at ith elemental panel, m/sec (ft/sec)

wi local downwash velocity at ith elemental panel, m/sec (ft/sec)

x/c distance from wing leading edge divided by local chord

y distance measured spanwise from plane of symmetry, cm (in.)

$\alpha$ angle of attack, deg.

$\alpha_{j}$ local angle of attack of ith elemental panel, rad

$\delta \mathbf{F}_{i}$ deflection of control surface $\mathbf{F}_{i}$ (positive when trailing edge is down), deg

$\delta^{*}$ boundary-layer displacement thickness, cm (in.)

n = 2y/b

sweep of wing quarter chord, deg

# Subscripts:

lower surface of wing

upper surface of wing

# THEORETICAL METHOD

# Basic Approach

Linear theory has been employed for the analysis of transport configurations with supercritical wings operating at transonic conditions. The analysis was accomplished by using the vortex-lattice method to model the configurations as planar lifting surfaces. The typical lattice used for this analysis is shown in figure 1.

Because the experimental rolling moments were achieved by the deflection of trailing-edge control surfaces on only one wing, the geometry and flow field were asymmetric when these controls were deflected. Accordingly, the vortex-lattice method briefly described in reference 12 was chosen for the present study since this method can analyze asymmetric geometries and asymmetric flow fields.

Preliminary analysis indicated that the inviscid thin-wing theory was sufficient for the prediction of both the slope of the lift curve and the slope of the pitching-moment curve over the angle-of-attack range of the data. However, the theory did not predict the actual values of the lift and pitching moment. Because of the linear nature of the lift and pitching-moment curves, it would, therefore, be sufficient to obtain a more exact solution at any angle of attack, such as the zero lift angle or, say, the angle for the design lift. For the present study, it was decided to correct the inviscid thin-wing theory at zero angle of attack. In order to obtain a more exact solution, the effects of wing thickness and boundary-layer-induced camber were included in the calculations. Details of these modifications are given in the next two sections.

# Thickness Modification

The conventional method of solving the linear three-dimensional thickness problem employs a distribution of sources (ref. 13, for example). The elemental source strengths are determined by matrix inversion with the appropriate boundary conditions being applied. However, to avoid extensive modification to the vortex-lattice program chosen for this analysis and to be consistent with the order of accuracy of the present linear method, the technique presented in appendix A of reference 14 was chosen to account for the effects of wing thickness. This technique differs from conventional thickness methods because it accounts for the interaction of the thickness and the camber and results in a modification of the camber distribution. A general discussion of this interaction may be found in reference 15. To aid in illustrating the application of this concept by the method of reference 14, the basic approach is reviewed.

In reference 14, Rowe, et al., state that the local perturbation velocities due to wing thickness can be accounted for in the linearized boundary conditions. In doing so, the following formulation is obtained:

$$
\frac {w _ {i}}{U _ {\infty}} = \frac {1}{U _ {\infty}} (\alpha_ {i} U _ {\text {l o c a l}})
$$

where $w_{i}$ represents the local downwash, $\alpha_{i}$ represents the local angle of attack, and $U_{\text{local}}$ is defined as being the local steady streamwise velocity that differs from $U_{\infty}$ due to thickness effects only. For thin-wing theory, $U_{\text{local}}$ is identically equal to $U_{\infty}$ . However, accounting for finite thickness yields

$$
\frac {w _ {i}}{U _ {\infty}} = \frac {1}{U _ {\infty}} \alpha_ {i} \left(U _ {\infty} + u _ {i}\right) = \alpha_ {i} \left(1 + \frac {u _ {i}}{U _ {\infty}}\right)
$$

where $(\mathbf{u}_i / \mathbf{U}_{\infty})$ represents the local streamwise perturbation velocity due to thickness only, nondimensionalized by the free-stream reference velocity $U_{\infty}$ . Values of the quantity $1 + (u_i / U_{\infty})$ may be obtained from experimental results or by using the streamwise component of two-dimensional theoretical velocity distributions. In the case of two-dimensional theoretical solutions for the thickness effect, some improvements might be expected if simple sweep theory were used to compute the thickness-induced flow velocity normal to, say, the leading edge and the results transformed to the streamwise direction. However, reference 14 does not indicate the use of simple sweep theory and, since the intent of this modification was to implement and evaluate the simplified approach suggested in reference 14, simple sweep theory has not been used.

The quantity $1 + (u_{i} / U_{\infty})$ could be computed by the use of any two-dimensional solution method. For the present study, the conformal transformation method of Theodorson (refs. 16 and 17) was chosen for this calculation because solutions can be quickly obtained and the method was felt to be consistent with the order of accuracy of the basic approach. The calculations were made for the symmetrical thickness distribution of the supercritical airfoils modified by the Prandtl-Glauert transformation to account for subcritical compressibility effects. The thickness modification was implemented by first establishing the chordwise distributions of the modification near the tip and near the root of the wing and then linearly interpolating in the spanwise direction along constant percent chord lines. No thickness corrections were applied for the fuselage.

# Boundary-Layer Modification

The boundary-layer influence was accounted for on the wing by modifying the local angles of attack of the mean camber surface to include the induced camber effects of the boundary-layer displacement thickness. The additional thickness effects due to the boundary layer were not included in the analysis. No boundary-layer effects were computed for the fuselage.

In order to estimate the effects of the boundary-layer displacement on the longitudinal aerodynamic characteristics, it was assumed that the boundary-layer displacement thickness could be calculated by use of a two-dimensional strip analysis. Initially, calculations were made by using the linear theory of reference 19 which assumes that the flow is subsonic and that the boundary layer is

For the NACA four-digit family of wing sections, reference 18 indicates that values of the total surface velocity (expressed as a ratio to the free stream) for intermediate thickness ratios may be obtained approximately by linearly scaling the tabulated velocity ratios for the nearest thickness ratio. The chordwise distribution of velocity ratio predicted by the method of Theodorsen for the geometries of the present investigation was found to scale linearly with thickness ratio to the same order of accuracy that the velocity ratios for the NACA four-digit series did. The spanwise variation of the chordwise distribution of this velocity ratio (and, hence, of the modification to the boundary conditions) could, therefore, be approximately accounted for by linear spanwise interpolation and thus simplify the computational procedure.

incompressible. However, this theory did not provide the proper pressure distribution for calculation of the boundary layer at transonic speeds, and the resulting boundary layers caused negligible changes in the lift and pitching moment at zero angle of attack. Hence, the two-dimensional transonic theory of Bauer, Garabedian, Korn, and Jameson (ref. 20) was used to compute the displacement thickness.

In order to correct the lift and pitching moment at zero angle of attack, the boundary-layer calculations were made for a model angle of attack of $0^{\circ}$ . Since converged solutions could not be obtained at a Mach number of 0.90, all calculations were made at a Mach number of 0.80. However, calculations indicated that the changes in displacement thickness over this Mach number range and for constant angle of attack (zero) are much less than the changes in displacement thickness over the angle-of-attack range investigated. Since the latter variation in displacement thickness is not being accounted for, it is not inconsistent to neglect the former variation. The experimental unit Reynolds number for all configurations was $9.84 \times 10^{6}$ per meter. All viscous calculations were based on this Reynolds number.

Calculations based on simple sweep theory showed that the effect of sweep on the boundary-layer-induced camber was within the accuracy of the calculations. Thus, to be consistent with the thickness calculation, the 2-D boundary-layer calculations were also made in the streamwise direction.

Bauer, et al. (ref. 20) ignore the laminar boundary layer and assume that the turbulent boundary layer grows from zero thickness at a specified "transition location." A correction for this assumption has been made in the present calculations by the estimation of the laminar Reynolds number at the model transition-strip location. The results for a flat-plate boundary layer with a zero pressure gradient in the streamwise direction were used. It was then assumed that the laminar and turbulent Reynolds numbers based on momentum thickness were equal at the model transition-strip location. Thus, a Reynolds number based on length could be computed for a turbulent boundary layer which began some distance ahead of the model transition-strip location. This Reynolds number was computed by the method of Sommer and Short (ref. 21) and provided a virtual origin of the turbulent boundary layer. The virtual origin was ahead of the model transition-strip location and was input as the "transition location" in the method of reference 20.

The resultant boundary layers were found to vary spanwise approximately in a linear manner. For this reason, the same linear interpolation technique used for the thickness modification was used to compute the boundary-layer effects on the wing. Figure 2 shows the resultant upper and lower surface boundary-layer displacement thickness distributions used for interpolation on the $\Lambda = 33^{\circ}$ configuration.

# COMPARISONS WITH EXPERIMENT

# Description of Models

The configurations of this report had supercritical wing sections and area-ruled fuselages with vertical tails but no horizontal tails. The wings had quarter-chord sweep angles of $33^{\circ}$ , $38.5^{\circ}$ , and $42^{\circ}$ . The planforms of these wings are shown in figure 3. The reference area for these wings was defined as the area created by extending the outboard leading- and trailing-edge line segments inboard to the wing center line; as a result, the reference planforms were trapezoidal. The moment reference point was taken to be the quarter chord of the mean aerodynamic chord of this reference trapezoidal wing planform. Only the $33^{\circ}$ wing had control surfaces. The controls were installed on the right wing only of the $33^{\circ}$ configuration in order to simplify model construction and testing. It was anticipated that a reasonable estimate of the effects of differential control deflection on both wings could be obtained by combining the effects of opposite deflections on the same wing. For this reason, the present comparisons of rolling moment are based on a differential rolling-moment coefficient $\Delta C_l$ defined as the rolling-moment coefficient for a negative control deflection minus the rolling-moment coefficient for the corresponding positive control deflection. A detailed description of the $33^{\circ}$ wing configuration as well as its experimental characteristics may be found in reference 5. The data for the other two configurations were obtained from unpublished results of wind-tunnel tests by the Langley Research Center.

# Longitudinal Aerodynamic Characteristics

A comparison between the theoretical and experimental chordwise load distributions at two span stations for the $33^{\circ}$ wing configuration at a Mach number of 0.80 is presented in figure 4. In general, the theory underpredicts the experimental loads in the vicinity of the leading edge and overpredicts the experimental loads in the vicinity of the trailing edge. However, the discrepancy between theory and experiment is reduced by accounting for the effects of wing thickness and boundary-layer induced camber.

A comparison between theoretical and experimental longitudinal aerodynamic characteristics of the $33^{\circ}$ wing configuration with no control deflections at Mach numbers of 0.80 and 0.90 is presented in figure 5. The wing pressure distribution data of reference 5 indicate that for these Mach numbers, shock waves and regions of supersonic flow are occurring on the wing. It can be seen that accounting for the thickness and viscous effects substantially improves the correlation between theory and experiment and results in a reasonably good prediction of the experimental characteristics.

In order to assess the effect of wing sweep in the present method of computing wing lift and pitching moment, similar computations were made for the

38.5° and 42° configurations. These results are shown in figures 6 and 7, respectively. It can be seen that similar improvements in the calculation of $C_L$ and $C_m$ were obtained by accounting for wing thickness and boundary-layer-induced camber. The discrepancies between the theory and the experiment are most probably due to the flat-plate representation of the fuselage, the use of linear theory at transonic speeds, and the approximate manner in which viscosity and wing thickness have been accounted for.

Similar results have been obtained by Hess (ref. 13) who estimated the effects of viscosity on a swept, tapered, and untwisted wing with a symmetrical airfoil. At a low free-stream Mach number, Hess demonstrated that inclusion of the boundary-layer displacement thickness in the theory improved the agreement between the theoretical and experimental chordwise pressure distributions and the spanwise lift distribution.

# Rolling-Moment Characteristics

To properly compute rolling-moment effectiveness, both thickness and viscous effects should be included. However, because of the difficulty of performing the boundary-layer analysis for an airfoil with a deflected trailing edge, no viscous effects on control effectiveness were computed.

Insufficient data for comparison with theory were available for control $\mathbf{F}_{1}$ . (See fig. 1 for control-surface locations.) Comparisons of the theoretical and experimental rolling-moment coefficients produced by controls $\mathbf{F}_{2}$ and $\mathbf{F}_{3}$ with the model angle of attack equal to $3.5^{\circ}$ (approximately the design lift condition) are presented in figures 8 and 9, respectively. For the lower Mach numbers and low deflection angles, good agreement was achieved between the linear thin-wing theory and the experimental results. As would be expected, at the higher deflection angles or at the higher Mach numbers, agreement between the inviscid theory and experiment deteriorated.

Figures 10 and 11 summarize these rolling-moment results for controls $\mathbf{F}_2$ and $\mathbf{F}_3$ as a function of Mach number. These figures more clearly show the effects of Mach number for the various control deflection angles. From reference 5, the drag divergence Mach number at the design $C_L$ of 0.50 for this configuration, with controls undeflected, is 0.916. It can be concluded from figures 10 and 11 that below the drag divergence Mach number and near the design lift condition, a reasonably good estimate of the differential rolling moment can be made by use of linear thin-wing theory without wing thickness or boundary-layer effects. Inclusion of the wing thickness effects consistently resulted in a negative increment in the differential rolling-moment coefficient for controls $\mathbf{F}_2$ and $\mathbf{F}_3$ over the range of deflection angles shown.

Rolling moments produced by control $\mathbf{F}_4$ were substantially overpredicted by theory (figs. 12 and 13). This large discrepancy between the theory and the experiment may be attributed to aeroelastic effects or trailing-edge flow separation.

Figure 14 presents a comparison between theory and experiment for rolling moments produced with multiple control deflections near the design lift coeffi-

cient. As before, rolling moments are reasonably well predicted below the drag divergence Mach number with the thin-wing solution. At high Mach numbers, linear thin-wing theory consistently overpredicted the control effectiveness.

# CONCLUDING REMARKS

A study has been conducted in order to determine the extent to which linear theory can be used as a rapid method of estimating the overall forces and moments of transport configurations with supercritical wings operating at transonic speeds.

Below the drag divergence Mach number, linear thin-wing theory gave a good prediction of both the slope of the lift curve and the slope of the pitching-moment curve against lift. However, the lift coefficient at zero angle of attack $C_{L,0}$ and the pitching-moment coefficients at zero lift $C_{m,0}$ were not well predicted by the thin-wing potential-flow theory.

It was found that for Mach numbers below drag divergence, the prediction of $C_{\mathrm{L},0}$ and $C_{\mathfrak{m},0}$ was greatly improved by inclusion of wing thickness effects which account for the interaction of thickness and camber. With the additional inclusion of two-dimensional boundary-layer-induced-camber effects, as determined from a nonlinear transonic method, the theory gave a reasonably good prediction of the lift coefficient $C_L$ and pitching-moment coefficient $C_{\mathfrak{m}}$ over the linear part of the angle-of-attack range.

For Mach numbers below drag divergence, lift coefficients near the design condition, and control deflection angles up to $\pm 15^{\circ}$ , thin-wing potential-flow theory gave a reasonably good estimate of the rolling moments due to deflection of inboard controls. Including the wing geometric thickness effects in the calculations generally resulted in a less accurate rolling-moment prediction. The effectiveness of the outboard controls was greatly overestimated.

The linear theory method (including thickness and viscous effects) was substantially faster and required much less storage than presently available transonic three-dimensional methods.

Langley Research Center  
National Aeronautics and Space Administration  
Hampton, VA 23665  
June 16, 1978

# REFERENCES

1. Bartlett, Dennis W.; and Re, Richard J.: Wind-Tunnel Investigation of Basic Aerodynamic Characteristics of a Supercritical-Wing Research Air-plane Configuration. NASA TM X-2470, 1972.   
2. Langhans, Richard A.; and Flechner, Stuart G.: Wind-Tunnel Investigation at Mach Numbers From 0.25 to 1.01 of a Transport Configuration Designed To Cruise at Near-Sonic Speeds. NASA TM X-2622, 1972.   
3. Supercritical Wing Technology - A Progress Report on Flight Evaluations. NASA SP-301, 1972.   
4. Whitcomb, Richard T.: Review of NASA Supercritical Airfoils. ICAS Paper No. 74-10, Aug. 1974.   
5. Mann, Michael J.; and Langhans, Richard A.: Transonic Aerodynamic Characteristics of a Supercritical-Wing Transport Model With Trailing-Edge Controls. NASA TM X-3431, 1977.   
6. Boppe, C. W.: Calculation of Transonic Wing Flows by Grid Embedding. AIAA Paper No. 77-207, Jan. 1977.   
7. Bailey, F. R.; and Ballhaus, W. F.: Comparisons of Computer and Experimental Pressures for Transonic Flows About Isolated Wings and Wing-Fuselage Configurations. Aerodynamic Analyses Requiring Advanced Computers, Part II, NASA SP-347, 1975, pp. 1213-1232.   
8. Ballhaus, W. F.; Bailey, F. R.; and Frick, J.: Improved Computational Treatment of Transonic Flow About Swept Wings. Advances in Engineering Science, Vol. 4, NASA CP-2001, 1976, pp. 1311-1320.   
9. Jameson, Antony; Caughey, David A.; Newman, Perry A.; and Davis, Ruby M.: A Brief Description of the Jameson-Caughey NYU Transonic Swept-Wing Computer Program - FLO 22. NASA TM X-73996, 1976.   
10. Jameson, Antony; and Caughey, D. A.: Numerical Calculation of the Transonic Flow Past a Swept Wing. NASA CR-153297, 1977.   
11. Jameson, Antony: Transonic Flow Calculations. Numerical Methods in Fluid Dynamics, H. J. Wirz and J. Smolderen, Jr., eds., Hemisphere Publishing Corp., 1978, pp. 1-88.   
12. Luckring, James M.: Some Recent Applications of the Suction Analogy to Asymmetric Flow Situations. Vortex-Lattice Utilization, NASA SP-405, 1976, pp. 219-236.   
13. Hess, John L.: Calculation of Potential Flow About Arbitrary Three-Dimensional Lifting Bodies. Rep. No. MDC J5679-01 (Contract N00019-71-C-0524), McDonnell Douglas Corp., Oct. 1972. (Available from DDC as AD 755 480.)

14. Rowe, W. S.; Winther, B. A.; and Redman, M. C.: Prediction of Unsteady Aerodynamic Loadings Caused by Trailing Edge Control Surface Motions in Subsonic Compressible Motions in Subsonic Compressible Flow - Analysis and Results. NASA CR-2003, 1972.   
15. Webber, J.: The Calculation of the Pressure Distribution Over the Surface of Two-Dimensional and Swept Wings With Symmetrical Aerofoil Sections. R. & M. No. 2918, British A.R.C., 1956.   
16. Theodorsen, T.: Theory of Wing Sections of Arbitrary Shape. NACA Rep. 411, 1931.   
17. Theodorsen, T.; and Garrick, I. E.: General Potential Theory of Arbitrary Wing Sections. NACA Rep. 452, 1933.   
18. Abbott, Ira H.; and Von Doenhoff, Albert E.: Theory of Wing Sections. Dover Publ., Inc., c.1959.   
19. Smetana, Frederick O.; Summey, Delbert C.; Smith, Neill S.; and Carden, Ronald K.: Light Aircraft Lift, Drag, and Moment Prediction - A Review and Analysis. NASA CR-2523, 1975.   
20. Bauer, Frances; Garabedian, Paul; Korn, David; and Jameson, Antony: Supercritical Wing Sections II. Volume 108 of Lecture Notes in Economics and Mathematical Systems, Springer-Verlag, 1975.   
21. Sommer, Simon C.; and Short, Barbara J.: Free-Flight Measurements of Turbulent-Boundary-Layer Skin Friction in the Presence of Severe Aerodynamic Heating at Mach Numbers From 2.8 to 7.0. NACA TN 3391, 1955.

图片摘要：该图主要展示 1. wing planform with control surface locations. Paneling sc。
![](images/918602db4bf265689377274786ea36bc3a70fd7b1ff8eccb01e80175bd12d841.jpg)  
Figure 1. - $33^{\circ}$ wing planform with control-surface locations. Paneling scheme typical of all configurations.

图片摘要：该图主要展示 1. wing planform with control surface locations. Paneling sc。
![](images/b6ab41028eee28487696f63139147be5de7342d1f35b975a2f488d8abccde005.jpg)  
$\frac{\sigma}{c}^{*}$   
(a) $\eta = 0.2161$   
Figure 2.- Upper and lower surface chordwise boundary-layer displacement thickness distributions. $M_{\infty} = 0.80$ ; zero control deflections; $\alpha = 0^{\circ}$ ; $\Lambda = 33^{\circ}$ .

图片摘要：该图主要展示 2. Upper and lower surface chordwise boundary layer displace。
![](images/bb368fd77a07cfa765a6bc096dae503084cb0bf2ebbef8fb6aecab788276cbb7.jpg)  
Figure 2.- Concluded.

图片摘要：该图主要展示 2. Concluded。
![](images/c3828d39dd4d6e420b6d65045e78ba29e1c2ffca85ecfd69df7fc3ebd7ce70db.jpg)  
Figure 3.- General wing planforms. Sweep angles are given for quarter-chord line of outboard panels.

图片摘要：该图主要展示 3. General wing planforms. Sweep angles are given for quarte。
![](images/84509a97910b11486f0a5ca816f34c87f355f31f7ce7256238d6b47d306b1ed3.jpg)  
(a) $\eta = 0.3809$ .   
Figure 4.- Effect of geometric thickness and boundary-layer-induced camber on chordwise load distributions. $C_L = 0.49$ ; $M_{\infty} = 0.80$ ; zero control deflections; $\Lambda = 33^{\circ}$ .

图片摘要：该图主要展示 4. Effect of geometric thickness and boundary layer induced 。
![](images/aa57a520dd8c751a3819da1d9191db19b9f7e4db90c0fa9c1431853ab16cdf6a.jpg)  
Figure 4.- Concluded.

图片摘要：该图主要展示 4. Concluded。
![](images/f9f99b1b289cf04e6dfb82133e599a38a21c8c1d582fc0e05b12785c4d6ebebe.jpg)  
(a) $\mathbf{M}_{\infty} = 0.80$   
Figure 5.- Effect of geometric thickness and boundary-layer-induced camber on longitudinal aerodynamic coefficients. Zero control deflections; $\Lambda = 33^{\circ}$ .

图片摘要：该图主要展示 5. Effect of geometric thickness and boundary layer induced 。
![](images/b99511f05179bdbdabae52f18f9faeb5ad22eb2768df00f5289b92ea03d0c2f8.jpg)

图片摘要：该图主要展示 5. Effect of geometric thickness and boundary layer induced 。
![](images/e7b97467413b274959e369d1c14052f462979f9038c3cb1360afd7852388ebac.jpg)  
Figure 6.- Effect of geometric thickness and boundary-layer-induced camber on longitudinal aerodynamic coefficients. Zero control deflections; $\Lambda = 38.5^{\circ}$ ; $M_{\infty} = 0.90$ .

图片摘要：该图主要展示 6. Effect of geometric thickness and boundary layer induced 。
![](images/cae212ab24fa8fbf897424264cedfdaeefddaf82b0b71aa0fd0c53f278dfb6d6.jpg)  
(a) $\mathbf{M}_{\infty} = 0.80$   
Figure 7.- Effect of geometric thickness and boundary-layer-induced camber on longitudinal aerodynamic coefficients. Zero control deflections; $\Lambda = 420$ .

图片摘要：该图主要展示 7. Effect of geometric thickness and boundary layer induced 。
![](images/3e3863f47551a66ea5e331a80da2818bb2e67c4c6a7bc77740014b26ffdc54ae.jpg)  
(b) $\mathbf{M}_{\infty} = 0.90$   
Figure 7.- Concluded.

图片摘要：该图主要展示 7. Concluded。
![](images/1a03c8bb8f1b3b0f49e06934dc53eed14a1e5ebe936bc094104a23f0a27c862e.jpg)  
Experiment Thin-wing theory Thick-wing theory Thick-wing theory with boundary-layerinduced camber

Experiment

Thin-wing theory

Thick-wing theory

图片摘要：该图主要展示 8. Comparison of theoretical and experimental differential r。
![](images/554976ea4a02e9e4be9ce195576488b0cbb43d7cf2fd29c873c4b29b6723a6c7.jpg)  
(a) $M_{\infty} = 0.80$

图片摘要：该图主要展示 8. Comparison of theoretical and experimental differential r。
![](images/8b62a47e99aa026a53215b0102e6b3086c7766067614e1fd1bdce61715e3f0f6.jpg)  
△C   
(b) $M_{\infty} = 0.90.$   
Figure 8.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by control $\mathbf{F}_2$ . $\alpha = 3.50^\circ$ ; $\Lambda = 33^\circ$ .

图片摘要：该图主要展示 8. Comparison of theoretical and experimental differential r。
![](images/ca7f05f5e151dfb59ad2e295b92a3bd16ff04d6361d3f12fb3f5f6c7cfe8b3e2.jpg)

图片摘要：该图主要展示 8. Comparison of theoretical and experimental differential r。
![](images/c09f59da8e62a694cf9db5293adeb427da291a1e0c5ce66265294b11e58c158a.jpg)  
(c) $M_{\infty} = 0.92$

图片摘要：该图主要展示 8. Comparison of theoretical and experimental differential r。
![](images/65bd67c72f853342bf73dee17132918be8b7a6f67d4f8411252c951085c07f92.jpg)  
(d) $M_{\infty} = 0.94.$   
Figure 8.- Concluded.

图片摘要：该图主要展示 8. Concluded。
![](images/d04c67047eabbcac1edade33246d93bdebe6404f157a690d09892c50c3b1a333.jpg)

图片摘要：该图主要展示 8. Concluded。
![](images/f17e98dab444d6896e0ed7cf01fb067b21e74ab47f356c1a3021a259541a9a36.jpg)  
(a) $\mathbf{M}_{\infty} = 0.80.$

图片摘要：该图主要展示 8. Concluded。
![](images/dad564cc75bf078db1054745e204b87cb9af401fe162333d5adae2bf4f2c1c4d.jpg)  
(b) $\mathbf{M}_{\infty} = 0.90$   
Figure 9.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by control $\mathbf{F}_3$ . $\alpha = 3.50^\circ$ ; $\Lambda = 33^\circ$ .

图片摘要：该图主要展示 9. Comparison of theoretical and experimental differential r。
![](images/8b819d330a7e4fa4d168c0b500fdc3fed00eecfe517223c62840e1aab1d1dbf6.jpg)  
(c) $\mathbf{M}_{\infty} = 0.92$

图片摘要：该图主要展示 9. Comparison of theoretical and experimental differential r。
![](images/71a493a3bff29e5a3ced8a1d4731cc7d0d990e3704ad46057fb12e2d6f1b7392.jpg)  
(d) $\mathbf{M}_{\infty} = 0.94$   
Figure 9.- Concluded.

图片摘要：该图主要展示 9. Concluded。
![](images/fde0c05d3827ed5755d70dc384fe31fcbfa1ae87565cd450e973c66d8711cdd9.jpg)

图片摘要：该图主要展示 9. Concluded。
![](images/5b02e9b8b21eb5a0ac6c8784d10bdb74760414f21d0acd77d2b97ecdcfe47659.jpg)  
Figure 10.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by three different deflections of control $F_{2}$ . $\alpha = 3.50^{\circ}$ ; $\Lambda = 33^{\circ}$ .

图片摘要：该图主要展示 10. Comparison of theoretical and experimental differential 。
![](images/f1db48e9ce2f39622fd68189cc087522b81b2828e1fa4bc7839b76245f95d837.jpg)  
Figure 11.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by three different deflections of control $\mathbf{F}_3$ . $\alpha = 3.50^\circ$ ; $\Lambda = 33^\circ$ .

图片摘要：该图主要展示 11. Comparison of theoretical and experimental differential 。
![](images/0a7986b26f6fde0ba2609ad74d2dc3974077e20c14bed71d7a726f5b80f342ea.jpg)  
Figure 12.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by control $\mathbf{F}_4$ . $\mathbf{M}_{\infty} = 0.80$ ; $\alpha = 3.50^{\circ}$ ; $\Lambda = 33^{\circ}$ .

图片摘要：该图主要展示 12. Comparison of theoretical and experimental differential 。
![](images/3db725cca2f732cef9eff02bb5d88360396d42ba1741f4d159d137b8fbccd131.jpg)  
Figure 13.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by two different deflections of control $\mathbf{F}_4$ . $\alpha = 3.50^\circ$ ; $\Lambda = 33^\circ$ .

图片摘要：该图主要展示 13. Comparison of theoretical and experimental differential 。
![](images/eab93638e3f134512845d78079e971dad7cab3f1f7123216838b110566153d77.jpg)  
Figure 14.- Comparison of theoretical and experimental differential rolling-moment coefficients produced by multiple control deflections. $\alpha = 3.50^{\circ}$ ; $\Lambda = 33^{\circ}$ .

<table><tr><td>1. Report No.
NASA TP-1253</td><td>2. Government Accession No.</td><td>3. Recipient&#x27;s Catalog No.</td></tr><tr><td rowspan="2" colspan="2">4. Title and Subtitle
THEORETICAL ESTIMATION OF THE TRANSONIC AERODYNAMIC
CHARACTERISTICS OF A SUPERCRITICAL-WING TRANSPORT
MODEL WITH TRAILING-EDGE CONTROLS</td><td>5. Report Date
August 1978</td></tr><tr><td>6. Performing Organization Code</td></tr><tr><td colspan="2">7. Author(s)
James M. Luckring and Michael J. Mann</td><td>8. Performing Organization Report No.
L-11257</td></tr><tr><td rowspan="2" colspan="2">9. Performing Organization Name and Address
NASA Langley Research Center
Hampton, VA 23665</td><td>10. Work Unit No.
505-11-16-07</td></tr><tr><td>11. Contract or Grant No.</td></tr><tr><td rowspan="2" colspan="2">12. Sponsoring Agency Name and Address
National Aeronautics and Space Administration
Washington, DC 20546</td><td>13. Type of Report and Period Covered
Technical Paper</td></tr><tr><td>14. Sponsoring Agency Code</td></tr><tr><td colspan="3">Supplementary Notes</td></tr><tr><td colspan="3">16. Abstract
This report presents a method for rapidly estimating the overall forces and moments
at supercritical speeds, below drag divergence, of transport configurations with
supercritical wings. The method is also used for estimating the rolling moments
due to the deflection of wing trailing-edge controls. This analysis is based on a
vortex-lattice technique modified to approximate the effects of wing thickness and
boundary-layer induced camber. Comparisons between the results of this method and
experiment indicate reasonably good correlation of the lift, pitching moment, and
rolling moment. The method required much less storage and run time to compute
solutions over an angle-of-attack range than presently available transonic non-
linear methods require for a single angle-of-attack solution.</td></tr><tr><td colspan="2">17. Key Words (Suggested by Author(s))
Longitudinal aerodynamic characteristics
Trailing-edge controls
Supercritical speed
Rolling moments
Vortex lattice Transonic aircraft</td><td>18. Distribution Statement
Unclassified - Unlimited
Subject Category 02</td></tr><tr><td rowspan="2">19. Security Classif. (of this report)
Unclassified</td><td rowspan="2">20. Security Classif. (of this page)</td><td>21. No. of Pages
31</td></tr><tr><td>22. Price*
$4.50</td></tr></table>

National Aeronautics and Space Administration

Washington, D.C. 20546

Official Business

Penalty for Private Use, $300.

THIRD-CLASS BULK RATE

Postage and ees Paid National Aeronautics and Space Administration NASA-451

图片摘要：该图片与072178 S00903DS；7 1 10. A. DEPT OF THE AIR FORCE AF WEAPONS LABORATORY ATTN: TEC这部分内容相关。
![](images/78fb40915858ee827d9e5749955c2c8dca3cd8dd6ea8688d5e33eeae13b0761a.jpg)

072178 S00903DS

7 1 10. A. DEPT OF THE AIR FORCE AF WEAPONS LABORATORY ATTN: TECHNICAL LIBRARY (SUL) KIRTLAND AFB NM 87117

NASA

POSTMASTER: If Undeliverable (Section 158) Postal Manual) Do Not Return
