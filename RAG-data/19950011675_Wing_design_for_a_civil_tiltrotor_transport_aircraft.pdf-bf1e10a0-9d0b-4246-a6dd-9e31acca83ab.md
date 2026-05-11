# WING DESIGN FOR A CIVIL TILTROTOR TRANSPORT AIRCRAFT

Performance Report

for the period of

(1-25-94 to 11-24-94)

Grant No.: NAG-1-1571

by

Dr. Masoud Rais-Rohani, P.I.

Assistant Professor of Aerospace Engineering

and Engineering Mechanics

Mississippi State University

Department of Aerospace Engineering

P. O.Drawer A

Mississippi State, Mississippi 39762

(NASA-CR-197523) WING DESIGN FOR A N85-18000

CIVIL TILTROTOR TRANSPORT AIRCRAFT N99-18090

Performance Report, 25 Jan. - 24

Nov. 1994 (Mississippi State)

Univ.) 6 p

Uncas

G3/05 0034005

# A Brief Background

The goal of this research is the proper tailoring of the civil tiltrotor's composite wing-box structure leading to a minimum-weight wing design. With focus on the structural design, the wing's aerodynamic shape and the rotor-pylon system are held fixed. The initial design requirement on drag reduction set the airfoil maximum thickness-to-chord ratio to $18\%$ . The airfoil section is the scaled down version of the $23\%$ -thick airfoil used in V-22's wing.

With the project goal in mind, the research activities began with an investigation of the structural dynamic and aeroelastic characteristics of the tiltrotor configuration, and the identification of proper procedures to analyze and account for these characteristics in the wing design. This investigation led to a collection of more than thirty technical papers on the subject—some of which have been referenced here. The review of literature on the tiltrotor revealed the complexity of the system in terms of wing-rotor-pylon interactions. The aeroelastic instability or whirl flutter stemming from wing-rotor-pylon interactions is found to be the most critical mode of instability demanding careful consideration in the preliminary wing design. The placement of wing fundamental natural frequencies in bending and torsion relative to each other and relative to the rotor 1/rev frequencies is found to have a strong influence on the whirl flutter. The frequency placement guide based on a Bell Helicopter Textron study is used in the formulation of frequency constraints.

The analysis and design studies are based on two different finite-element computer codes: (a) MSC/NASTRAN, and (b) WIDOWAC<sup>11</sup>. These programs are used in parallel with the motivation to eventually, upon necessary modifications and validation, use the simpler WIDOWAC code in the structural tailoring of the tiltrotor wing. Several test cases were studied for the preliminary comparison of the two codes. The results obtained so far indicate a good overall agreement between the two codes.

# Wing Design Problem

The problem is to find the optimum set of structural parameters that minimize the cantilever wing structural weight while satisfying all structural and dynamic/aeroelastic constraints. The structural constraints are formulated in terms of strength allowable while the dynamic/aeroelastic constraints are formulated in terms of wing fundamental bending and torsion frequencies and the frequencies of the rotor. The design variables include skin ply thicknesses and orientation angles, spar and rib web thicknesses and spar-cap and stringer cross-sectional areas. These design variables enable the tailoring of the composite wing structure to meet the design requirements most efficiently.

# MSC/NASTRAN Based Analysis and Design

A finite-element model of the tiltrotor wing structure was first developed using PATRAN. This model is based on the $18\%$ -thick airfoil section. The model consists of 324 nodes and 856 elements for a total of 1,944 degrees of freedom. In this model the engine, transmission, nacelle, and rotor system are represented as a lumped mass located at their combined C.G. location. This mass is attached to the wing structure at the spindle location via a four-bar truss. In the actual aircraft the entire propulsion/rotor system pivots about the spindle as the aircraft transforms back and forth between vertical and horizontal flight modes. The non-structural masses, associated with fuel, flight control system, etc. inside the wing, are lumped at the finite-element nodes in the vicinity of their corresponding C.G. locations.

This finite-element model was used for preliminary vibration (i.e., natural frequencies and mode shapes) calculations using MSC/NASTRAN. Only the vibration characteristics in the horizontal flight mode (with the rotor mast parallel to the wing chord) were investigated because the whirl flutter instability occurs in forward flight. The results obtained indicated a very strong coupling between the wing uncoupled fundamental frequencies/mode shapes and

the stiffness of the truss support structure. This was not surprising as the mass associated with the propulsion/rotor system, lumped at the vertex of the four-bar truss, is several times greater than the total mass of the wing—with the flexibility of the truss elements influencing the wing-nacelle dynamics. Recognizing the inadequacy of this model, we worked on developing a more accurate model of the wing-nacelle support structure that also captures the influence of the nacelle down-stop, which keeps the rotor mast parallel to the wing chord when the aircraft is in horizontal flight mode.

With no success in obtaining pertinent information from various sources with regard to the specifics of wing-nacelle modeling, we continued our effort into improving the wing-nacelle attachment structure model as best as we could based on very limited information. In the new version the propulsion system and associated structure are modeled by a series of one-dimensional elements with the nodes placed at the C.G. of individual components. The information with regard to each individual component is obtained from Ref. 10. The wing-nacelle attachment points are at the fore and aft spars where the pylon down-stop and spindle are located, respectively. This arrangement is more detailed than in the previous finite-element model, and we feel that it captures the wing-nacelle interaction more accurately. This model is being used for further modal analysis and design studies. The preliminary analysis indicated the existence of low-frequency vibration modes associated with the attachment structure. The entire wing/pylon model is under further examination. If the local low-frequencies of the attachment structure are found to be troublesome, then some fine tuning of element rigidities may be necessary. Upon resolution of various modeling issues, we will proceed with the complete tiltrotor wing structural design using MSC/NASTRAN.

# WIDOWAC Based Analysis and Design

As part of the research task the WIDOWAC wing structural analysis/design code was examined for possible use in the support of structural tailoring activities. Following an extensive effort to make this code compile and execute correctly on a computer system besides Cyber NOS, its capabilities and limitations were explored more closely.

At present, WIDOWAC does not have the capability to determine the wing fundamental horizontal bending frequency, which is necessary for adequate formulation of the frequency constraints. To alleviate this limitation we approximated the straight wing fundamental horizontal bending frequency as $\omega_{h} = \sqrt{I_{h} / I_{v}}\omega_{v}$ , where $\omega_{v}$ is the wing fundamental vertical bending frequency, and $I_{h}$ and $I_{v}$ are the wing section horizontal and vertical moments of inertia. Since MSC/NASTRAN has no restriction with respect to the horizontal vibration modes, the fundamental horizontal bending frequency can be obtained, and compared with that from $\omega_{h}$ formula.

# Preliminary Results

To validate the analysis capabilities of WIDOWAC, several test cases have been examined with the results compared to those obtained from MSC/NASTRAN. These test cases are all based on a straight and untapered wing model with different material properties and loading conditions. Both isotropic and orthotropic materials have been considered. The wing model has a symmetric airfoil with five spars and eight ribs. In WIDOWAC the skin is modeled by linear membrane elements, the spar caps are modeled by linear rod elements and the spar and rib webs are modeled by linear shear web elements. In MSC/NASTRAN the skin is modeled by CQUAD4 elements with membrane properties specified in the Pshell; the spar caps are modeled by BAR elements with the shear webs modeled also by CQUAD4 elements.

In the first test case we examined the static response of a straight isotropic wing to a torsion-inducing couple at the wing tip. The nodal vertical, chordwise and spanwise

displacements were obtained based on WIDOWAC and MSC/NASTRAN analyses. The average wing twist angle distribution was obtained from the vertical displacements. Very good agreement is observed in the twist angle distribution between WIDOWAC and MSC/NASTRAN. The element stress components were also compared. As expected the in-plane shear was the largest component of element stress under the specified torsional loading condition. The overall agreement between the two codes in terms of stress components is very good.

In the second test case we examined the static response of the straight isotropic wing under a single tip load, producing both bending and torsional responses in the wing. The displacement responses from the two analyses are in very good agreement. The axial and shear stress components obtained by MSC/NASTRAN and WIDOWAC are not as close as in the pure torsion case with some differences in the order of 10 to $20\%$ . The stress discrepancies are attributed to some extend to the differences in the two models in terms of two-dimensional elements, and most likely in the way the element strains are calculated from the nodal displacements in the postprocessing. While these differences did not matter in the pure torsion case they did show up in the combined bending-torsion problem.

A modal analysis was also performed on the straight isotropic wing using both WIDOWAC and MSC/NASTRAN. The fundamental wing spanwise-bending frequency is 3.07 rad/sec according to WIDOWAC and 3.05 rad/sec according to MSC/NASTRAN. The fundamental wing chordwise-bending frequency obtained by MSC/NASTRAN is 6.86 rad/sec as compared with 6.95 rad/sec found using the $\omega_{h}$ formula. The torsional frequency obtained by WIDOWAC is 40.46 rad/sec as compared to 36.78 rad/sec obtained by MSC/NASTRAN. The overall agreement in frequencies is good. The difference in torsional frequencies is attributed to the fact that the WIDOWAC model is slightly stiffer in torsion than the MSC/NASTRAN model due to differences in the two-dimensional elements used in these codes.

In the third test case we examined the static response of a straight orthotropic wing (with a $90^{\circ} / 0^{\circ}$ layered skin) to a torsion-inducing couple at the wing tip. The twist angle, vertical, chordwise and spanwise displacements were obtained based on WIDOWAC and MSC/ NASTRAN analyses. Very good agreement is observed in the twist angle distribution between WIDOWAC and MSC/NASTRAN. The element stress components were also compared in the $90^{\circ}$ and $0^{\circ}$ layers, respectively. The in-plane shear is the largest component of element stress under the specified torsional loading condition. The overall agreement between the two stress results is fairly good.

In the fourth test case we examined the static response of the straight orthotropic wing to a single tip load, producing both bending and torsional responses in the wing. The displacement and stress values based on the two codes are again in fairly good agreement with variation in some stress components as observed in the second test case.

A modal analysis was also performed on the straight 2-layered orthotropic wing using both WIDOWAC and MSC/NASTRAN. The fundamental wing spanwise-bending frequency is 4.36 rad/sec according to WIDOWAC and 4.60 rad/sec according to MSC/NASTRAN. The fundamental wing chordwise-bending frequency obtained by MSC/NASTRAN is 10 rad/sec as compared with 9.63 rad/sec found using the $\omega_h$ formula. The torsional frequency obtained by WIDOWAC is 25 rad/sec as compared to 23 rad/sec obtained by MSC/NASTRAN.

The results obtained so far compare favorably in terms of displacements and vibrational characteristics, but there are some discrepancies with regard to the element stresses. The disagreements between some stress components obtained from WIDOWAC and MSC/ NASTRAN are attributed to the way element strains are calculated from the displacement field in the finite-element postprocessing.

Overall, the research effort is progressing satisfactorily. The preliminary findings were presented at the 35th Structures, Structural Dynamics and Materials conference in April of this year. Additional research activity, planned for the remainder of the current grant year, is being performed as planned.

# References

1. Loewy, R.G., "Aeroelasticity and the Tilt-rotor VTOL Aircraft," VERTIFLITE, Vol. 38, No. 3, 1992.   
2. Few, D.D. and Edenborough, H.K., “Tilt-Proprotor Perspective,” Astronautics and Aeronautics, December 1977, pp. 28-31.   
3. Kvaternik, R.G., "Experimental and Analytical Studies in Tilt-Rotor Aeroelasticity," presented at the AHS/NASA Ames Specialists' Meeting on Rotorcraft Dynamics, February 13-15, 1974.   
4. Kvaternik, R.G. and Kohn, J.S., "An Experimental and Analytical Investigation of Proprotor Whirl Flutter," NASA TP-1047, 1977.   
5. Reed, W.H., III, "Propeller-Rotor Whirl Flutter: A State-Of-The-Art Review," Journal of Sound Vibration, Vol. 4, No. 3, 1966.   
6. Edenborough, H.K., "Investigation of Tilt-Rotor VTOL Aircraft Rotor-Pylon Stability," Journal of Aircraft, Vol. 5, No. 6, 1968.   
7. Alexander, H.R., Hengen, L.M. and Weiber, J.A., "Aeroelastic-Stability Characteristics of a V/STOL Tilt-Rotor Aircraft With Hingeless Blades: Correlation of Analysis and Test," presented at the AHS 30th Annual National Forum, Washington, D.C., May 1974.   
8. Vorwald, J.G. and Chopra, I., "Stabilizing Pylon Whirl Flutter on a Tilt-Rotor Aircraft," presented at 32nd AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference, Baltimore, MD, April 8-10, 1991.   
9. Nixon, M.W., "Parametric Studies for Tilt-rotor Aeroelastic Stability in High-Speed Flight," proceedings of the 33rd AIAA/ASME/ASCE/AHS/ ASC Structures, Structural Dynamics and Materials Conference, Dallas, Texas, April 13-15, 1992, Part 4, pp. 2027-2037.   
10. Rogers, C. and Reisdorfer, D., "Civil Tiltrotor Transport Point Design-Model 940A," NASA-CR-191446, 1992.   
11. Haftka, R.T. and Starnes, J.H. Jr., "WIDOWAC: Wing Design Optimization with Aeroelastic Constraints, Program Manual," NASA TM X-3071, 1974.

# Presentation Title and Abstract

Rais-Rohani, M. and Baker, D.J., "Wing Design for a Civil Tilt-Rotor Transport Aircraft: A preliminary Study," Proceedings of the 35th AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics and Materials Conference, Hilton Head, SC, April 18-20, 1994. AIAA Paper No. 94-1469

A preliminary study was conducted toward the optimum design of a composite wing-box structure for a civil tilt-rotor transport aircraft. This effort has been focused on two tasks: (1) to study the intricate dynamic and aeroelastic characteristics of the tilt-rotor configuration, and to identify the proper procedures to analyze these characteristics; and (2) to develop the structural modeling and analysis techniques necessary in the tilt-rotor wing design optimization. Following the completion of this task, and proper formulation of aeroelastic and structural constraints, the design optimization will proceed to develop a minimum-weight, tailored, lower-drag wing design. In the preliminary design of the wing-box structure, the design variables will include only structural parameters such as thicknesses and orientation angles of the upper and lower-skin plies, spar and rib cap areas and web thicknesses, and stringer areas. The wing-rotor-pylon aeroelastic and dynamic interactions will be limited in the preliminary wing design by holding the cruise speed, rotor-pylon system and wing geometric attributes fixed.