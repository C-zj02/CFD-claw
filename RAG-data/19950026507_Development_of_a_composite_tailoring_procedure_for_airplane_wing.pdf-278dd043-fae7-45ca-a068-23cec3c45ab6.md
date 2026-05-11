```txt
(NASA-CR-199081) DEVELOPMENT OF A COMPOSITE TAILORING PROCEDURE FOR AIRPLANE WING Progress Report (Arizona State Univ.) 14 p Unclas 
```

G3/05 0061024

# Development of a Composite Tailoring Procedure for Airplane Wing

Grant number: NAG2-908

# Progress Report

Aditi Chattopadhyay - Principal Investigator and

Sen Zhang - Graduate Research Assistant

Department of Mechanical and Aerospace Engineering

Arizona State University

Tempe Arizona 85287

# Objectives

The development of a composite wing box section using a higher order-theory is proposed for accurate and efficient estimation of both static and dynamic responses. The theory includes the effect of through-the-thickness transverse shear deformations which is important in laminated composites and is ignored in the classical approach. The box beam analysis is integrated with an aeroelastic analysis to investigate the effect of composite tailoring using a formal design optimization technique. A hybrid optimization procedure is proposed for addressing both continuous and discrete design variables.

# Accomplishment

In recent years, aeroelastic tailoring has received considerable attention as a means to improve aeroelastic performance through directional stiffening. Fibrous composite materials can further enhance aeroelastic tailoring capabilities by utilizing their unique stiffness and strength properties. Accurate and efficient prediction of the structural response is very important in the investigation of aeroelastic tailoring using composite structures. The analysis of aircraft wings can be done either through a detailed investigation of the wing sections comprising spars, webs, ribs etc., or through the representation of the load carrying member by reduced composite box beam models. The detailed analysis is computationally very expensive and is often impractical in design optimization and/or trade-off studies. Several approaches addressing composite box beam modeling have been proposed over the last few years [1-2]. All of these models have several limitations. In some of these work, classical laminate theory (CLT) was used [3] and transverse deformations through the wall thickness were neglected to make the contour analysis easier. In advanced aircraft applications, the thin wall assumption of CLT is not

Nnn

$N \cdot  {0.5} \cdot  C$

OCT

61024 14

valid for low aspect ratios which typically use moderately thick-walled sections. For composite structure in which strong elastic coupling exists, these transverse stresses and strains heavily influence the structural behavior. The effect of transverse shear stress was shown to be critical even in the buckling of so-called "thin" laminates in a study conducted by Chattopadhyay et al [4]. Secondly, in some of the work, the cross sectional geometry was assumed to remain rigid during beam deformation and thus in-plane warping was neglected [1-2]. However, in-plane warping is important for loaded wing structures with short aspect ratio. Studies by Weisshaar et al. [5] indicate that chordwise bending mode, which is associated with in-plane warping, is important in the prediction of aeroelastic performance. Therefor, in the present research, a composite box beam model is developed based on a higher-order laminate theory, that can effectively predict the dynamic response under unsteady aerodynamic loads. This model accounts for through-the-thickness variations in shear strains and includes both inplane and out-of-plane warping deformation.

# Composite Modeling

A rectangular composite box beam model with taper and sweep is developed to represent the load carrying member of an aircraft wing (Fig. 1). The single-celled composite box beam model is based on a higher-order composite laminate theory [6] and accounts for the distributions of shear strains through the thickness of each wall. The displacement field for each wall section is described by bending, warping and inplane stretching. Continuity between the wall displacement fields is imposed at each of the four corners of the cross section. The analysis is capable of modeling low aspect ratio wings with moderately thick-walled load carrying members while accounting for chordwise bending during flutter analysis. The finite element method is used to formulate the governing equations of motion.

For each of the individual plates, the higher-order displacement field is defined in local coordinate system as follows (Fig.1).

$$
\begin{array}{l} u (x, y, t) = u _ {0} (x, y, t) + z \psi_ {x} (x, y, t) + z ^ {2} \xi_ {x} (x, y, t) + z ^ {3} \zeta_ {x} (x, y, t) \\ v (x, y, t) = v _ {0} (x, y, t) + z \psi_ {y} (x, y, t) + z ^ {2} \xi_ {y} (x, y, t) + z ^ {3} \zeta_ {y} (x, y, t) \tag {1} \\ \end{array}
$$

$$
\mathrm {w} (\mathrm {x}, \mathrm {y}, \mathrm {t}) = \mathrm {w} _ {0} (\mathrm {x}, \mathrm {y}, \mathrm {t})
$$

where $\mathbf{u}_0, \mathbf{v}_0$ and $\mathbf{w}_0$ denote the displacements of a point $(\mathbf{x}, \mathbf{y})$ on the midplane and $\psi_x$ and $\psi_y$ are the rotations of the normal to the midplane about the y and x axes, respectively. The higher-order terms $\xi_x, \zeta_x, \xi_y$ and $\zeta_y$ represent beam warping in each plate. By imposing the necessary conditions that the transverse shear stresses must vanish on the plate top and bottom surfaces, the following refined displacement field is obtained.

$$
\mathrm {u} = \mathrm {u} _ {0} + z \left[ \mathrm {y} _ {\mathrm {x}} - \frac {4 z ^ {2}}{3 h ^ {2}} (\frac {\partial \mathrm {w}}{\partial \mathrm {x}} + \mathrm {y} _ {\mathrm {x}}) \right]
$$

$$
u = u _ {0} + z \left[ y _ {x} - \frac {4 z ^ {2}}{3 h ^ {2}} \left(\frac {\partial w}{\partial x} + y _ {x}\right) \right] \tag {2}
$$

$$
\mathbf {w} = \mathbf {w} _ {0}
$$

where $h$ is the plate thickness. Making the assumption of small displacements and rotations, a linear strain-displacement relationship is used. The governing equations of motion for an individual plate is derived using the Hamilton's principle.

$$
\int_ {t _ {1}} ^ {t _ {2}} \delta \left[ U _ {e} + V _ {e} - W _ {e} \right] d t = 0 \tag {3}
$$

where U, V and W denote the kinetic energy, the strain energy and the work done by external forces, respectively. Using the constitutive relations for general orthotropic material along with the strain-displacement relations, the element stiffness matrix, the mass matrix and the forcing vector are derived from Eqn. 3.

The construction of the box beam from plate elements is shown in Fig. 2. The quantities $\mathbf{u}$ , $\mathbf{v}$ , $\mathbf{w}$ are displacements along $x$ , $y$ and $z$ axis, respectively, and $\theta_x$ , $\theta_y$ and $\theta_z$ are rotations along theses directions. To make stiffness transformation possible, continuity of displacements and rotations are imposed at each of the four corners while the generalized forces corresponding to higher order warping terms are set to zero. Through the use of coordinate transformation, the reduced stiffness matrix is expressed in the global form. Assembly of the element matrices leads to the following governing equation for wing dynamic motion.

$$
\mathbf {M} \ddot {\mathbf {x}} + \mathbf {C} \dot {\mathbf {x}} + \mathbf {K} \mathbf {x} = \mathbf {q} \tag {4}
$$

where $\mathbf{M}$ , $\mathbf{C}$ and $\mathbf{K}$ denote the global mass, damping and stiffness matrix, respectively. The vector $\mathbf{x}$ represents structural elastic deformation and the vector $\mathbf{q}$ denotes forcing vector.

# Results

The static results of the composite box beam analysis are presented in this section. The correlations are made with experimental data which was furnished by studies conducted by Chandra et al. [7]. The test beams are single-celled rectangular box beams with three kinds of stacking sequences: cross-ply, symmetric and antisymmetric lay-up.

The beam dimensions are shown in Fig. 3. Table 1 presents the elastic properties for the composite material which is used to fabricate these beams.

Using the higher-order theory, the static response of the composite box beams is computed under unit tip bending and unit tip torque load. Results are shown in Figs. 4-10. It is shown that, for cross-ply and symmetric lay-up cases, correlation between higher-order solution and test data are excellent. Significant differences exist between experimental data and computational results for the $(0 / 30)_3$ antisymmetric lay-up case. For beams with antisymmetric lay-up under unit tip torque, comparisons are also made between the deflections predicted by higher-order theory and computations using three dimensional finite element formulation. Both solutions give identical results.

# Future Plan

Following is an outline of the future research.

(1) Extend the above analysis technique to model two-cell composite box beams.   
(2) Couple the developed composite analysis procedure with aeroelastic technique.   
(3) Perform aeroelastic tailoring of composite airplane wing using a hybrid optimization method.

Briefing describe of the proposed research follows.

The higher-order box beam theory will be extended to model multi-cell box beam configurations in order to deal with more realistic wing structural layouts. This capability will be verified by applying the analysis procedure to a two-cell composite box beam model.

Next, the higher-order composite box beam theory will be coupled with unsteady aerodynamic computation to perform aeroelastic analysis. Aerodynamic loads will be computed using the Doublet Lattice Method (DLM) as implemented in the analysis code ASTROS [8]. Both static and dynamic aeroelastic analysis, including predictions of flutter and divergence boundaries, will be conducted in the frequency domain. Using the modal approach, problems will be solved in the reduced space. This will substantially save computational time without compromising the accuracy of the results. Thus the procedure will be more suitable for design optimization studies.

Finally, aeroelastic tailoring will be performed based on the developed higher-order composite laminate theory and the aeroelastic analysis. The complex composite tailoring problem will be addressed using a hybrid optimization technique. The hybrid technique will allow the inclusion of both continuous design variables, such as the wing planform geometry, and discrete variables, such as stacking sequence, in the investigation. Objective functions and constraints pertaining to improvement in both structural and

aeroelastic performance will be included using formal multiobjective function formulation technique developed by Chattopadhyay and McCarthy [9].

# References

1. Butler, R., M. Lillico, Banerjee, J. R. and Guo, S. "Optimum Design of High Aspect Ratio Wings Subject to Aeroelastic Constrains," Proceedings of AIAA/ASME/ASCE/AHS/ASC 36th. Structures, Structural Dynamics and Materials Conference and Adaptive Structures Forum, New Orleans, Louisiana, April 10-14, 1995, AIAA-95-1223-CP, pp. 558-566.   
2. Weisshaar, T.A., "Aeroelastic Tailoring of Forward Swept Composite Wings," Journal of Aircraft, Vol. 17, June 1980, pp.442-448.   
3. Agarwal, B. D. and Broutman, L. J., "Analysis and Performance of Fiber Composites," Second Edition, John Wiley & Sons, Inc., 1990   
4. Chattopadhyay, A. and Gu, H., “New Higher Order Plate Theory in Modeling Delamination Bucking of Composite Laminates,” AIAA Journal, Vol. 32, August 1994, pp. 1709-1716.   
5. Weisshaar, T.A. and Foist, B.L., "Vibration And Flutter of Advanced Composite Lifting Surfaces," Journal of Aircraft, Vol. 22, February, 1985, pp. 141-147.   
6. Reedy, J. N., "Energy and Variational Methods in Applied Mechanics," Chapter 4, John Wiley & Sons, Inc. 1984.   
7. Smith, E. C. and Chopra, I., "Formulation and Evaluation of an Analytical Model for Composite Box-Beams," Proceedings of 31st AIAA/AHS/ASME/ASCE/ASC Structures, Structural Dynamics and Materials Conference, Long Beach, Calif., April 2-4, 1990.   
8. Johnson, E. H. and Venkayya, V. B., "Automated Structural Optimization System (ASTROS), Volume 1- Theoretical Manual," AFWAL-TR-88-3028, Dec. 1988.   
9. Chattopadhyay, Aditi and McCarthy, Thomas R., "Multiobjective Design Optimization of Helicopter Rotor Blades with Multidisciplinary Couplings," Optimization of Structural Systems and Industrial Applications, editors, Hernandez, S. and Brebbia, C. A., pp. 451-462, 1991.

图片摘要：该图主要展示 1. Wing layout and composite box beam model。
![](images/02bd0c0351372f6474efcbbe90541895d4ed179f605a9ff78011000dd3dc13d5.jpg)  
Figure 1. Wing layout and composite box beam model.

图片摘要：该图主要展示 1. Wing layout and composite box beam model。
![](images/cda3ec56b3cd5a49216e1e62177281d2355caa76f001e38266ccd97a67bba2f8.jpg)  
Figure 2. Box beam construction

图片摘要：该图主要展示 2. Box beam construction。
![](images/6d3a679f2c682e276e6c142a59de24841da1705f9d3be06c60b792bc0d4d6163.jpg)  
Figure 3 Test beam dimensions

<table><tr><td rowspan="6">d</td><td colspan="2">L/d=56</td><td colspan="2">L/d=29</td></tr><tr><td>L (in)</td><td>30</td><td>30</td><td></td></tr><tr><td>d (in)</td><td>0.537</td><td>1.025</td><td></td></tr><tr><td>c (in)</td><td>0.953</td><td>2.060</td><td></td></tr><tr><td>Ply thickness (in)</td><td>0.005</td><td>0.005</td><td></td></tr><tr><td>Wall thickness (in)</td><td>0.03</td><td>0.03</td><td></td></tr></table>

Table 1. Material properties.   

<table><tr><td>EL(msi)</td><td>20.59</td></tr><tr><td>ET(msi)</td><td>1.42</td></tr><tr><td>GLT(msi)</td><td>0.87</td></tr><tr><td>GTT(msi)</td><td>0.5</td></tr><tr><td>YLTI</td><td>0.42</td></tr><tr><td>YTT</td><td>0.42</td></tr></table>

图片摘要：该图主要展示 1. Material properties。
![](images/64052ac05116206310ddc16842e9c1d47af1f0af97e09f2a4eba2fa82407a89b.jpg)  
Figure 4. Bending slop under unit tip bending load of cross-ply lay-up beam; $(0 / 90)_3$ , $L / d = 29$ .

图片摘要：该图主要展示 4. Bending slop under unit tip bending load of cross ply lay。
![](images/ce4ab0d3ed1561434bda0e83c47e98d3261bcd1608194c2d4cd8b2b15b47c855.jpg)  
Figure 5. Twist under unit tip torque of cross-ply lay-up beam; $(0 / 90)_3$ , $L / d = 29$ .

图片摘要：该图主要展示 5. Twist under unit tip torque of cross ply lay up beam; ,。
![](images/fb1da65b03d4694caeff4607814d88f027569294f3eb49b42628450dcd38d9fc.jpg)  
Figure 6. Twist at $x / L = 0.5$ under tip torque of anti-symmetric lay-up beams; $L / d = 56$ .

图片摘要：该图主要展示 6. Twist at under tip torque of anti symmetric lay up beams;。
![](images/747c97cfa21dd83bea30d7daedf1db917d3a8869ee81b2d84d135878bdcad370.jpg)  
Figure 7. Bending slope under unit tip bending load of symmetric lay-up beam; top & bottom $(15)_6$ , sides $(15/-15)_3$ , $L/d = 56$ .

图片摘要：该图主要展示 7. Bending slope under unit tip bending load of symmetric la。
![](images/0803a70b424c1ff27ff3bbfd08ae2dc62ee6b5bd72b8384d67f80757dd9bd73a.jpg)  
Figure 8. Twist under unit tip bending load of symmetric lay-up beam; top & bottom $(15)_6$ , sides $(15/-15)_3$ , $L/d = 56$ .

图片摘要：该图主要展示 8. Twist under unit tip bending load of symmetric lay up bea。
![](images/c18be944593600d50eb10ceeb1371f4fa1beeaa5536e80c4cbb265a667cc1aa5.jpg)  
Figure 9. Bending slope under unit tip bending load of symmetric lay-up beam; top & bottom $(30)_6$ , sides $(30/-30)_3$ , $L/d = 56$ .

图片摘要：该图主要展示 9. Bending slope under unit tip bending load of symmetric la。
![](images/c2428c839e4f691112b89c5e14ac16ed5ff1086e4e83b0ef7d0e160b3837fc94.jpg)  
Figure 10. Twist under unit tip bending load of symmetric lay-up beam; top & bottom $(30)_6$ , sides $(30/-30)_3$ , L/d=56.
