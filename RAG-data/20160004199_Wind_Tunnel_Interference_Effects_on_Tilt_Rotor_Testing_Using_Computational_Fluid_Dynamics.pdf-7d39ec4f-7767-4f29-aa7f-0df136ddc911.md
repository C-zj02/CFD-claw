图片摘要：该图片为文档封面或首页内容，主题与Wind Tunnel Interference Effects on Tilt Rotor Testing Using Computational Fluid Dynamics相关。
![](images/dbd93f5891b586869b895de315f52e09d88205f062c663f0590a6edb041f68a2.jpg)

# Wind Tunnel Interference Effects on Tilt Rotor Testing Using Computational Fluid Dynamics

Master’s Thesis Flight Performance and Propulsion Delft University of Technology

Witold J. F. Koning

# Wind Tunnel Interference Effects on Tilt Rotor Testing Using Computational Fluid Dynamics

Master’s Thesis

by

Witold Johannes Folgert Koning

in partial fulfillment of the requirements for the degree of

Master of Science in Aerospace Engineering

at the Delft University of Technology, to be defended publicly on December $1 8 ^ { t h }$ 2015

Supervisor:

Dr. ir. R. Vos, Assistant Professor at Flight Performance and Propulsion Faculty of Aerospace Engineering at Delft University of Technology

Thesis Defense Committee:

Prof. Dr.-Ing. Georg Eitelberg, Director at DNW German-Dutch Wind Tunnels and Professor at Flight Performance and Propulsion

Dr. ir. Ferdinand F. J. Schrijer, Assistant Professor at Aerodynamics, Faculty of Aerospace Engineering at Delft University of Technology

图片摘要：该图片与“Tenacity is one of the greatest skills or talents of a good engineer, particula这部分内容相关。
![](images/7783dd3a2e089232cd44d42620ef62399650a3537181a61515bede7c6e4ae7a8.jpg)

“Tenacity is one of the greatest skills or talents of a good engineer, particularly one who works in R&D. It is not unusual to work on-and-off on a problem for years before one feels like one has accomplished something noteworthy.

The key to having such tenacity in the first place, though, is to believe in your own problem solving ability and to believe in the importance of the problem even in the face of doubt.”

Larry Young, NASA Ames Research Center

# Abstract

Experimental techniques to measure rotorcraft aerodynamic performance are widely used. However, most of them are either unable to capture interference effects from bodies, or require an extremely large computational budget. The objective of the present research is to develop an XV-15 Tilt Rotor Research Aircraft rotor model for investigation of wind tunnel wall interference using a novel Computational Fluid Dynamics (CFD) solver for rotorcraft, RotCFD.

In RotCFD, a mid-fidelity URANS solver is used with an incompressible flow model and a realizable k-ε turbulence model. The rotor is, however, not modeled using a computationally expensive, unsteady viscous body-fitted grid, but is instead modeled using a blade element model with a momentum source approach.

Various flight modes of the XV-15 isolated rotor, including hover, tilt and airplane mode, have been simulated and correlated to existing experimental and theoretical data. The rotor model is subsequently used for wind tunnel wall interference simulations in the National Full-Scale Aerodynamics Complex (NFAC) at NASA Ames Research Center in California.

The results from the validation of the isolated rotor performance showed good correlation with experimental and theoretical data. The results were on par with known theoretical analyses. In RotCFD the setup, grid generation and running of cases is faster than many CFD codes, which makes it a useful engineering tool. Performance predictions need not be as accurate as high-fidelity CFD codes, as long as wall effects can be properly simulated.

For both test sections of the NFAC wall interference was examined by simulating the XV-15 rotor in the test section of the wind tunnel and with an identical grid but extended boundaries in free field. Both cases were also examined with an isolated rotor or with the rotor mounted on the modeled geometry of the Tiltrotor Test Rig (TTR). A ‘quasi linear trim’ was used to trim the thrust for the rotor to compare the power as a unique variable. Power differences between free field and wind tunnel cases were found from $- 7 \%$ to $0 \%$ in the 80- by 120-Foot Wind Tunnel test section and -1.6 $\%$ to $4 . 8 ~ \%$ in the 40- by 80-Foot Wind Tunnel, depending on the TTR orientation, tunnel velocity and blade setting. The TTR will be used in 2016 to test the Bell 609 rotor in a similar fashion to the research in this report.

# Acknowledgements

During the past 9 months I was fortunate enough to have the possibility to perform my thesis research at the Aeromechanics Branch at NASA Ames Research Center in Moffett Field, California. The support and generosity of a large amount of people made it possible for me to endeavor into the world of rotorcraft at NASA.

One of the great advantages to work in such a high tech environment is that highly skilled and knowledgeable people are all around you and always willing to help. The help of a multitude of persons at the Aeromechanics branch was invaluable: Wally Acree, for his patience and guidance during my validation phases of the XV-15 rotor; Eduardo Solis, who despite the pressure always found time to help with meshing and gridding in RotCFD; Meridith Segall, who never got upset when I asked for even more computers to run my simulations on; Gloria Yamauchi, Larry Young, Natasha Barbely and Shirley Burek for all the support throughout my time at Ames. A special shout out to Kristen Kallstrom who has been the kindest of all during my stay in California.

Also several interns at Ames have been highly valuable and supportive during my research. First of all my partner in crime, Esma Sahin, with whom I’ve practically spend 24 hours a day for nine months straight without getting into a fight. JeWon Hong and Shelby Mallin for their highly valuable research in support of my work. An enormous hug for Samalis Santini for her kindness and support during the many stressful moments. Lastly, and by no means less valuable, all the other people, interns and friends who I had the pleasure of meeting at the NASA Lodge, the Rainbow Mansion and throughout California.

From Sukra Helitek I would like to explicitly thank Ganesh Rajagopalan and Luke Novak for their extensive support while I dove into the intricacies of RotCFD. The people from Science and Technology Corporation, in particular Amar Choudry, Stephen Lesh and Ravi Deepak, for making this experience possible in the first place and supporting me in my way to the US, and during my stay there.

At the Delft University of Technology I would like to thank Roelof Vos for his support and guidance throughout my literature study and thesis research. Despite the truly horrible time zones I always enjoyed our bi-weekly updates!

It is by no means an exaggeration to state that this work could not have been completed without their continued support.

Without the financial support and backing of my parents I would have never thought of this possibility. Thank you for your endless support and thinking ahead. Many thanks to the Aeromechanics branch for their indispensable support as well as the contributions from the Prof. dr. ir. H.J. van der Maas Fund, Delft University Fund (Universiteitsfonds Delft) and the KIVI Study and Travel Fund (KIVI Studie –en Reisfonds).

Lastly, I cannot express my gratitude for Dr. William Warmbrodt, chief of the Aeromechanics branch, for his unwavering support. He is undoubtedly one of the most inspiring persons I’ve had the pleasure of meeting in my life. An acknowledgements section does not suffice the credit that he deserves.

Delft, 18 November 2015

Witold J. F. Koning

Nomenclature   

<table><tr><td>Symbols</td><td>Description</td><td>Unit (Metric)</td></tr><tr><td>A</td><td>area, rotor disk area (πR2)</td><td>m2</td></tr><tr><td>a</td><td>acceleration</td><td>m/s2</td></tr><tr><td>a0</td><td>speed of sound at sealevel</td><td>m/s</td></tr><tr><td>B</td><td>tip-loss factor</td><td>-</td></tr><tr><td>b</td><td>number of blades</td><td>-</td></tr><tr><td>c</td><td>blade chord</td><td>m</td></tr><tr><td>cd</td><td>section drag coefficient</td><td>-</td></tr><tr><td>ci</td><td>section lift coefficient</td><td>-</td></tr><tr><td>C1,table</td><td>section lift coefficient from c81 table</td><td>-</td></tr><tr><td>cm</td><td>section moment coefficient</td><td>-</td></tr><tr><td>cn</td><td>section normal force coefficient</td><td>-</td></tr><tr><td>CP</td><td>rotor power coefficient</td><td>-</td></tr><tr><td>CPo</td><td>rotor induced power coefficient, Po/ρA(ΩR)3</td><td>-</td></tr><tr><td>CT</td><td>rotor thrust coefficient, T/ρA(ΩR)2</td><td>-</td></tr><tr><td>ct</td><td>section tangential force coefficient</td><td>-</td></tr><tr><td>cz</td><td>section force in z-direction</td><td>-</td></tr><tr><td>cφ</td><td>section force in φ-direction</td><td>-</td></tr><tr><td>f</td><td>body force per unit mass</td><td>N/kg</td></tr><tr><td>h</td><td>altitude</td><td>m</td></tr><tr><td>KL</td><td>stall delay parameter (Corrigan model)</td><td>-</td></tr><tr><td>I</td><td>aerodynamic locus</td><td>m</td></tr><tr><td>M</td><td>Mach number, figure of merit</td><td>-</td></tr><tr><td>m</td><td>mass</td><td>kg</td></tr><tr><td>m</td><td>mass flux</td><td>kg/s</td></tr><tr><td>Mtip</td><td>tip Mach number</td><td>-</td></tr><tr><td>N</td><td>number of blades</td><td>-</td></tr><tr><td>P</td><td>power</td><td>J/s</td></tr><tr><td>p</td><td>pressure</td><td>N/m2</td></tr><tr><td>po</td><td>pressure at sealevel</td><td>N/m2</td></tr><tr><td>Pi</td><td>induced power</td><td>J/s</td></tr><tr><td>Po</td><td>profile power</td><td>J/s</td></tr><tr><td>R</td><td>rotor radius</td><td>m</td></tr><tr><td>r</td><td>blade or rotor disk radial coordinate</td><td>m</td></tr><tr><td>R</td><td>gas constant</td><td>m2/s2K</td></tr><tr><td>r,φ,z</td><td>inertial coordinate system fixed at the center of the rotor</td><td>NA</td></tr><tr><td>Re</td><td>effective blade radius</td><td>m</td></tr><tr><td>S</td><td>surface</td><td>m2</td></tr><tr><td>sz</td><td>source strength per unit radius in z-direction</td><td>N/m</td></tr><tr><td>sz'</td><td>averaged source strength per unit radius in z-direction</td><td>N/m</td></tr><tr><td>sφ</td><td>source strength per unit radius in φ-direction</td><td>N/m</td></tr><tr><td>sφ'</td><td>averaged source strength per unit radius in φ-direction</td><td>N/m</td></tr><tr><td>T</td><td>rotor thrust</td><td>N</td></tr><tr><td>t</td><td>time</td><td>s</td></tr><tr><td>T∞</td><td>rotor thrust out of ground effect</td><td>N</td></tr><tr><td>To</td><td>temperature at sealevel</td><td>K</td></tr><tr><td>u</td><td>velocity component parallel to x-axis</td><td>m/s</td></tr><tr><td>V</td><td>velocity, aircraft or wind tunnel speed</td><td>m/s</td></tr><tr><td>v</td><td>velocity component parallel to y-axis</td><td>m/s</td></tr><tr><td>V</td><td>rotor velocity with respect to air</td><td>m/s</td></tr><tr><td>Vabs</td><td>absolute velocity (of blade element)</td><td>m/s</td></tr><tr><td>Vcal</td><td>calibrated airspeed</td><td>m/s</td></tr><tr><td>vh</td><td>hover induced velocity</td><td>m/s</td></tr><tr><td>vi</td><td>induced velocity</td><td>m/s</td></tr><tr><td>V∞</td><td>velocity in the far wake</td><td>m/s</td></tr><tr><td>Vrel</td><td>relative velocity (at blade section)</td><td>m/s</td></tr><tr><td>Vtas</td><td>true airspeed</td><td>m/s</td></tr><tr><td>w</td><td>velocity component parallel to z-axis</td><td>m/s</td></tr><tr><td>x,y,z</td><td>Cartesian coordinate system</td><td>NA</td></tr><tr><td>z</td><td>height from ground</td><td>m</td></tr><tr><td>Greek symbols</td><td>Description</td><td>Unit (Metric)</td></tr><tr><td>α</td><td>angle of attack</td><td>deg</td></tr><tr><td>αp</td><td>pylon angle</td><td>deg</td></tr><tr><td>β</td><td>angle between relative velocity and rotor disk plane</td><td>rad</td></tr><tr><td>βp</td><td>precone angle</td><td>deg</td></tr><tr><td>γ</td><td>ratio of specific heats</td><td>-</td></tr><tr><td>δP</td><td>percentage change of power (compared to FFGE case)</td><td>%</td></tr><tr><td>δT</td><td>percentage change of thrust (compared to FFGE case)</td><td>%</td></tr><tr><td>εct</td><td>chord-line twist</td><td>deg</td></tr><tr><td>θ</td><td>collective angle</td><td>deg</td></tr><tr><td>θ.75</td><td>collective pitch angle at quarter chord</td><td>deg</td></tr><tr><td>θ0</td><td>collective pitch angle</td><td>deg</td></tr><tr><td>λ</td><td>bulk viscosity coefficient</td><td></td></tr><tr><td>μ</td><td>advance ratio</td><td>-</td></tr><tr><td>μ</td><td>dynamic viscosity</td><td>(N.s)/m2</td></tr><tr><td>ρ</td><td>density</td><td>kg/m3</td></tr><tr><td>σ</td><td>rotor solidity</td><td>-</td></tr><tr><td>τ</td><td>shear stress</td><td></td></tr><tr><td>Ω</td><td>rotor rotational speed</td><td>rad/s</td></tr><tr><td>Abbreviations</td><td>Description</td><td></td></tr><tr><td>ADM</td><td>Actuator-Disk Model</td><td></td></tr><tr><td>AoA</td><td>Angle of Attack</td><td></td></tr><tr><td>BEM</td><td>Blade-Element Model</td><td></td></tr><tr><td>BL</td><td>Boundary Layer</td><td></td></tr><tr><td>C81</td><td>Airfoil</td><td></td></tr><tr><td>CAMRAD</td><td>Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics</td><td></td></tr></table>

<table><tr><td>CFD</td><td>Computational Fluid Dynamics</td></tr><tr><td>CTR</td><td>Civil Tilt Rotor</td></tr><tr><td>EPS</td><td>turbulent dissipation</td></tr><tr><td>FFGE</td><td>Free Field with GEometry (excluding wind tunnel, including geometry)</td></tr><tr><td>FFRO</td><td>Free Field Rotor Only (excluding wind tunnel, excluding geometry)</td></tr><tr><td>IGE</td><td>In Ground Effect</td></tr><tr><td>ISA</td><td>International Standard Atmosphere</td></tr><tr><td>JVX</td><td>Joint-service Vertical take-off/landing Experimental (Aircraft)</td></tr><tr><td>LCTR</td><td>Large Civil Tilt Rotor</td></tr><tr><td>MATLAB</td><td>MATrix LABoratory program, by The MathWorks, Inc.</td></tr><tr><td>NA</td><td>Not Available</td></tr><tr><td>NFAC</td><td>National Full-Scale Aerodynamics Complex</td></tr><tr><td>OARF</td><td>Outdoor Aerodynamic Research Facility</td></tr><tr><td>OGE</td><td>Out of Ground Effect</td></tr><tr><td>PCHIP</td><td>Piecewise Cubic Hermite Interpolating Polynomial</td></tr><tr><td>RANS</td><td>Reynolds Averaged Navier-Stokes</td></tr><tr><td>RotCFD</td><td>Rotorcraft CFD</td></tr><tr><td>RotUNS</td><td>Rotor Unstructured Solver</td></tr><tr><td>SD</td><td>stall delay</td></tr><tr><td>SIMPLE</td><td>Semi-Implicit Method for Pressure-Linked Equations</td></tr><tr><td>SIMPLER</td><td>Semi-Implicit Method for Pressure-Linked Equations Revised</td></tr><tr><td>TKE</td><td>Turbulent Kinetic Energy</td></tr><tr><td>TP</td><td>tip loss</td></tr><tr><td>TTR</td><td>Tiltrotor Test Rig</td></tr><tr><td>U-mom</td><td>momentum in x-direction</td></tr><tr><td>U-vel</td><td>velocity in x-direction</td></tr><tr><td>URANS</td><td>Unsteady Reynolds Averaged Navier-Stokes</td></tr><tr><td>VS.</td><td>versus</td></tr><tr><td>VTOL</td><td>Vertical Take-Off and Landing</td></tr><tr><td>WTGE</td><td>Wind Tunnel with GEometry (including wind tunnel, including geometry)</td></tr><tr><td>WTGE*</td><td>Quasi Trimmed Wind Tunnel with GEometry (including wind tunnel, including geometry)</td></tr><tr><td>WTGE2</td><td>2nd set of Wind Tunnel with GEometry (including wind tunnel, including geometry)</td></tr><tr><td>WTRO</td><td>Wind Tunnel Rotor Only (including wind tunnel, excluding geometry)</td></tr><tr><td>WTT</td><td>Wind Tunnel Test</td></tr><tr><td>XV-15</td><td>Tilt Rotor Research Aircraft</td></tr></table>

# Table of Contents

1 Introduction ...

1.1 Research Question and Goal

2 Literature Study & Background..

2.1 Rotorcraft Aerodynamics....

2.1.1 Ground Effect Significance...   
2.1.2 The Traditional Actuator Disk Model and Blade Element Model.   
2.1.3 The Figure of Merit..   
2.1.4 Rotor Performance Corrections. .6

2.2 Navier-Stokes Equations and CFD ..

2.2.1 Continuity Equation ......   
2.2.2 Momentum Equation...   
2.2.3 Rotorcraft Computational Fluid Dynamics (RotCFD)   
2.2.4 The RotCFD Rotor Model. .8   
2.2.5 Some considerations with the use of RotCFD.. 11

2.3 National Full-Scale Aerodynamics Complex (NFAC)....... . 11

2.3.1 Wind Tunnel and Test Section Geometry... . 11   
2.3.2 Wind Tunnel Wall Corrections .. . 12

2.4 Tiltrotor Test Rig (TTR). . 13

2.5 XV-15 Rotor Characteristics........... . 15

2.5.1 XV-15 Rotor Blade Characteristics . . 15   
2.5.2 C81 Airfoil Data Structure. . 17

2.6 XV-15 Performance Data.. . 17

2.6.1 Hover.... .. 18   
2.6.2 Tilt . . 19   
2.6.3 Airplane Mode . . 20

3 Aerodynamic Analysis Method.. . 21

3.1 RotCFD Assumptions.. . 21   
3.2 XV-15 Airfoil Data Corrections . .. 21

3.2.1 Stall Delay Model. .. 21   
3.2.2 Tip Loss Model.. . 22   
3.2.3 C81 Airfoil Adjustment Code. . 22

3.3 General Setup of Validation Cases.......... ... 26

3.3.1 Boundary Settings......... . 27   
3.3.2 Spatial and Temporal Resolution Independency ....... .. 28

3.4 NFAC Wind Tunnel Cases Setup.............. .. 28

3.4.1 NFAC 80-by 120-Foot Wind Tunnel Cases................. .. 30   
3.4.2 NFAC 40-by 80-Foot Wind Tunnel Cases .................. .. 31

4 Validation of XV-15 Rotor Model. . 35

4.1 Hover ....... .. 35   
4.2 Tilt Mode ........ .. 38   
4.3 Airplane Mode . . 39   
4.4 Ground Effect Study by Je Won Hong.. . 40   
4.5 Discussion on Airfoil Data Correction ......... . 40

4.5.1 Tip Loss Factor ................. ..... 40   
4.5.2 Stall Delay Factor .... . 41

4.6 Accuracy and Precision... .. 41   
4.7 Residual Values... . 42   
4.8 Performance Convergence ............. . 42

5 Results ..... ... 45

5.1 NFAC 80-by 120-Foot Wind Tunnel Results ........ . 45   
5.1.1 Quasi Trim for Thrust........... . 47   
5.2 NFAC 40-by 80-Foot Wind Tunnel Results.......... . 49   
5.2.1 Quasi Trim . .. 50

5.3 Performance Convergence . . 51   
5.4 Forces on the TTR . . 52   
5.5 Stability Related Time Step Restrictions.. . 54

6 Conclusions and Recommendations .. .. 55

6.1 Conclusions.... .. 55   
6.2 Recommendations.. . 55

Appendix A NFAC Characteristics .. .. 59

Appendix B C81 Airfoil Adjustment Code Results . ... 61

B.1 Angle of Attack and Mach number interpolation... .. 61   
B.2 Representative Stall Delay Plots .. . 63

Appendix C Steady XV-15 Rotor Validation Results.. ... 65

C.1 Simulation Parameters.. ... 65   
C.2 Residual Overview ...... .. 66   
C.3 Data Steady XV-15 Rotor Results. . 67

Appendix D Unsteady XV-15 Rotor Validation Results. . 71

D.1 Simulations Parameters . .. 71   
D.2 Hover - Unsteady .. .. 72   
D.3 Tilt Mode - Unsteady ... .. 72   
D.4 Airplane Mode - Unsteady.. ... 74   
D.5 Data Unsteady XV-15 Rotor Results . ... 74

Appendix E Wind Tunnel Case Plots . 77

E.1 80- by 120-Foot Wind Tunnel Cases.... . 77

E.1.1 Case 1, Edgewise, 0 kts.. .. 77   
E.1.2 Case 2, Edgewise, 10 kts. .. .. 78   
E.1.3 Case 3, Axial, 100 kts. .. .. 79

E.2 40- by 80-Foot Wind Tunnel Cases .... ... 80

E.2.1 Case 5, Edgewise, 100 kts.. . 80   
E.2.2 Case 6, Axial, 200 kts. . ... 81   
E.2.3 Case 7, Tilt, 100 kts.. ... 81

# List of Figures

Figure 2.1 Ground effect; thrust increase at constant power [3]..

Figure 2.2 Ground effect; influence of forward speed on ground effect [3]. .

Figure 2.3 Schematic representation of actuator disk in hover [4]. .

Figure 2.4 Rotor and coordinate system [18]. ........ .. 8

Figure 2.5 Blade section nomenclature at a grid point [18].... .9

Figure 2.6 Velocity plot of a steady model. .. ... 10

Figure 2.7 Velocity plot of an unsteady model. ...... ..... 10

Figure 2.8 Top view of rotor disk grid and flow field grid... ..... 10

Figure 2.9 Enlarged view of the rotor disk grid and flow field grid. . ... 10

Figure 2.10 The NFAC facility at NASA Ames Research Center. .............. . 11

Figure 2.11 Sketch of the 80- by 120-Foot Wind Tunnel and 40- by 80-Foot Wind Tunnel, respectively [20]. ................... 11

Figure 2.12 The 80- by 120-Foot Wind Tunnel and 40- by 80-Foot Wind Tunnel cross section in the NFAC [20], [21].... 12

Figure 2.13 Propeller in closed throat wind tunnel [24].. . 12

Figure 2.14 The author at the (enormous) 80-by 120-Foot Wind Tunnel Inlet. . . 13

Figure 2.15 The TTR on the aft calibration stand, with cowlings open. ................ . 13

Figure 2.16 The author at the TTR with the calibration rig mounted. ........ . 13

Figure 2.17 XV-15 rotor blade chord-line twist distribution [6].. . 16

Figure 2.18 XV-15 rotor blade chord distribution [6]. . 16

Figure 2.19 XV-15 rotor blade aerodynamic loci [6]. .......... ..... 16

Figure 2.20 Example format of (partial) C81 airfoil data file........ .. 17

Figure 2.21 XV-15 rotor hover power as a function of thrust [2], [6], [28].. .. 18

Figure 2.22 XV-15 rotor hover figure of Merit as a function of thrust [2], [6], [28]. .. .. 18

Figure 2.23 XV-15 rotor power as a function of thrust for different pylon angles at V/ΩR = .32 [2]. ................. ....... 19

Figure 2.24 XV-15 rotor power as function of thrust, for ${ \tt G P } = 7 5 ^ { \circ }$ and Mtip $= 0 . 6 5$ [2]. . .. 20

Figure 2.25 Rotor propulsive efficiency as function of thrust [2]. ....... .. 20

Figure 3.1 Spanwise Corrigan stall delay parameter obtained for XV-15 rotor model. .. .. 22

Figure 3.2 Angle of attack and Mach interpolation for representative cases of the NACA 64-X08 airfoil.. .. 23

Figure 3.3 Simplified flowchart of airfoil adjustment code. .... .. 24

Figure 3.4 Radial interpolation check of lift coefficient at $M = 0 . 3 0$ . .. . 25

Figure 3.5 Stall delay influence as function of angle of attack or Mach number for various radial stations........................ 25

Figure 3.6 Lift coefficient as function of radial station at $M = 0 . 3 0$ at continuous zero pitch angle. ............................. ....... 26

Figure 3.7 RotCFD user interface with a hover case loaded. . .. 26

Figure 3.8 Hover case, gridded centered side view (XZ) of the flowfield.. 27

Figure 3.9 Hover case, gridded top view (XY) at rotor height. ................ .. 27

Figure 3.10 TTR in 40- by 80-Cross section shifting from airplane $\angle { \mathsf { a p } } = 0 ^ { \circ }$ ) mode to edgewise flight ${ \mathrm { ( a p = 9 0 ^ { \circ } } }$ ).............. 28

Figure 3.11 The boundaries of the extended test sections with TTR in edgewise and axial mode, respectively. ............. 29

Figure 3.12 The extended test sections with TTR on struts and XV-15 rotor in edgewise and axial mode, respectively.30

Figure 3.13 The setup of case 3, WTGE. . 31

Figure 3.14 The setup for case 1 and 2, WTGE. . 31

Figure 3.15 Conversion corridor of the XV-15 [5].... .. 31

Figure 3.16 XV-15 height-velocity envelope [5]. .. .. 32

Figure 3.17 The geometry for case 4 and 5, FFGE... .. 32

Figure 3.18 The geometry and grid for case 6, WTGE. ..... .. 33

Figure 3.19 The geometry for case 7, WTRO.. . 33

Figure 4.1 Unsteady results for XV-15 rotor hover power as a function of thrust [2], [28]..... .. 35

Figure 4.2 Unsteady results for XV-15 rotor hover figure of Merit as a function of thrust [2], [28]. . ... 36

Figure 4.3 Steady results for XV-15 rotor hover power as a function of thrust [2], [6], [28].... .. 36

Figure 4.4 Steady results for XV-15 rotor hover figure of Merit as a function of thrust [2], [6], [28]. .. ... 37

Figure 4.5 Rotor thrust as function of collective pitch angle........... .. 37

Figure 4.6 Rotor power as function of collective pitch angle......... ... 38

Figure 4.7 Steady results for XV-15 rotor power as a function of thrust for various pylon angles at V/ΩR = .32 [2]. ........ 38

Figure 4.8 Steady results for XV-15 rotor power as function of thrust, for α $) = 7 5 ^ { \circ }$ [2]. .. ... 39

Figure 4.9 Steady results for (rotor) propulsive efficiency as function of thrust [2]. ........... .. 39

Figure 4.10 Evaluation of the XV-15 rotor in ground effect in RotCFD [37]. ...... ..... 40

Figure 4.11 Sketch of blade loading characteristics. .... ... 40

Figure 4.12 2nd order polynomial fit through the OARF data. .. . 41   
Figure 4.13 Residual plot for a tilting isolated rotor at 15 degrees pylon angle. . 42   
Figure 4.14 Hover performance convergence over time.. . 43   
Figure 4.15 Tilt mode (15 degree pylon angle) convergence over time. . . 43   
Figure 4.16 Airplane mode convergence over time. . 43   
Figure 5.1 Various computers used for months on end to compute each of the cases within the timeframe................... 45   
Figure 5.2 A velocity plot of a coarse, unfitted body test at $\mathrm { t } \approx 6$ [s] showing no re-ingestion... . 46   
Figure 5.3 Linearization to obtain point (TFFGE,P*).. . 47   
Figure 5.4 Representative velocity plots for case 3.. . 48   
Figure 5.5 Flowfield of FFGE subset for case 7.. . 51   
Figure 5.6 Performance convergence for case 2, WTGE, hover. .... . 51   
Figure 5.7 Performance convergence for case 7, WTGE, tilt mode.. . 52   
Figure 5.8 Integrated forces on the TTR for case 5, WTGE. . 52   
Figure 5.9 Integrated forces on the TTR and struts for case 4, WTGE.. . 53   
Figure 5.10 Performance convergence for case 4, WTGE. .... ........ 53   
Figure 5.11 Meshed TTR nose (no grid). . 54   
Figure 5.12 Body fitted TTR nose. .. 54   
Figure 5.13 Gridded TTR nose without body fitting. . . 54   
Figure B.1 Imported C81 data for NACA 64-X08 airfoil.. ... 61   
Figure B.2 Imported C81 data for NACA 64-X12 airfoil.. ... 62   
Figure B.3 Imported C81 data for NACA 64-X18 airfoil.. ... 62   
Figure B.4 Imported C81 data for NACA 64-X25 airfoil.. ... 63   
Figure B.5 Effect of stall delay on lift curve slope.. ... 63   
Figure B.6 Effect of stall delay on lift coefficient for set of airfoil data at various radial stations... . 64   
Figure C.7 Residual overview for representative airplane mode case. . ... 66   
Figure C.8 Residual overview for representative tilt mode case with $a p = 7 5 .$ . ... 66   
Figure C.9 Residual overview for representative hover mode case. . ... 67   
Figure D.10 Unsteady results for XV-15 rotor hover power as a function of thrust [2], [28]. ... . 72   
Figure D.11 Unsteady results for XV-15 rotor hover figure of Merit as a function of thrust [2], [28].. . 72   
Figure D.12 Unsteady results for XV-15 rotor power as a function of thrust for various pylon angles at V/ΩR = .32 [2]. 73   
Figure D.13 Unsteady results for XV-15 rotor power as function of thrust, for ${ \tt G P } = 7 5 ^ { \circ }$ and Mtip $= 0 . 6 5$ [2]. ............ ....... 73   
Figure D.14 Unsteady results for (rotor) propulsive efficiency as function of thrust [2].. . 74   
Figure E.15 The boundaries of the extended test sections with TTR in edgewise and axial mode, respectively............... 77   
Figure E.16 Case 1, WTGE, ZY-plane. . . 77   
Figure E.17 Case 1, WTRO, ZY-plane. . 77   
Figure E.18 Legend for pressure and velocities for case 1. . 77   
Figure E.19 Case 2, FFGE, XY-plane. .. .. 78   
Figure E.20 Case 2, WTGE, XY-plane. . .. 78   
Figure E.21 Legend for pressure and velocities for case 2.. . 78   
Figure E.22 Case 3, WTGE, XZ-plane. . 79   
Figure E.23 Case 3, WTRO, XZ-plane. . 79   
Figure E.24 Legend for pressure and velocities for case 3.. .. 79   
Figure E.25 Case 5, FFGE, XY-plane. . ... 80   
Figure E.26 Case 5, WTGE, XY-plane. ... 80   
Figure E.27 Legend for pressure and velocities for case 5... ... 80   
Figure E.28 Case 6, FFGE, XY-plane. .. .. 81   
Figure E.29 Case 6, WTGE, XY-plane. .. 81   
Figure E.30 Legend for pressure and velocities for case 6.... .. 81   
Figure E.31 Case 7, WTGE, XY-plane. .. 81   
Figure E.32 Case 7, WTRO, XY-plane. . 81   
Figure E.33 Legend for pressure and velocities for case 7.. . 81   
Figure E.34 ZY-plane of case 7, just behind the rotor plane. . 82

# List of Tables

Table 2.1 Key TTR Design Capabilities [25]. . 14   
Table 2.2 XV-15 Rotor Characteristics [5], [6], [26]–[29]. . . 15   
Table 3.1 Sea level air properties used.. . 21   
Table 3.2 Overview of four different subsets per case. .............. ... 30   
Table 3.3 Final 80- by 120-Foot Wind Tunnel Cases . .. 30   
Table 3.4 Final 40- by 80-Foot Wind Tunnel Cases.. . 33   
Table 5.1 NFAC 80-by 120-Foot Wind Tunnel Rotor Only Results. . 45   
Table 5.2 NFAC 80-by 120-Foot Wind Tunnel Geometry Results.. . 46   
Table 5.3 Quasi Trimmed NFAC 80-by 120-Foot Wind Tunnel Geometry Results. . 47   
Table 5.4 NFAC 40-by 80-Foot Wind Tunnel Rotor Only Results............ .. 49   
Table 5.5 NFAC 40-by 80-Foot Wind Tunnel Geometry Results . . 50   
Table 5.6 Quasi Trimmed NFAC 40-by 80-Foot Wind Tunnel Geometry Results . . 50   
Table A.1 $4 0 \times 8 0$ Foot Wind Tunnel Characteristics [21]. . . 59   
Table ${ \sf A } . 2 8 0 \times 1 2 0$ Foot Wind Tunnel Characteristics [20].. . 59   
Table C.3 Overview of steady simulation parameters... .. 65   
Table C.4 Summary of steady RotCFD Validation Data.. . 67   
Table D.5 Overview of steady simulation parameters. ... . 71   
Table D.6 Summary of unsteady RotCFD Validation Data.. . 74

# 1 Introduction

Experimental techniques to measure rotor and airframe aerodynamic performance are widely used but the need exists to understand the limitations of ground based testing by augmenting the analysis of experimental test results with Computational Fluid Dynamics (CFD) modeling. The objective of the present research is to develop an XV-15 Tilt Rotor Research Aircraft rotor model for investigation of wind tunnel wall interference. This research is performed to support wind tunnel tests scheduled for 2016. Ultimately the rotor model developed is used to investigate wind tunnel wall effects on large tilt rotors in the National Full-Scale Aerodynamics Complex (NFAC) facility at NASA Ames Research Center in California. The renewed interest in tilt rotors originates from NASA studies indicating significant reduction in congestion of commercial transport aviation1 .

The focus of this research is to understand the limitations and accuracy of tilt rotor performance predictions using a midfidelity CFD program. An unsteady RANS solver, RotCFD, is used with an incompressible flow and a k-ε turbulence model. RotCFD uses a model similar to an actuator-disk model (ADM) or blade-element model (BEM) with two-dimensional airfoil data that allows for relatively quick simulations of unsteady rotorcraft cases. The rotor is represented solely through the momentum it imparts to the flow. The coupling of the rotor with the surrounding flow is done by implementing its sources in the momentum equations. This omits the classical way of resolving a very fine grid around the rotor geometry to capture all flow effects. This gives RotCFD a significant advantage in simulation time2 .

Inherent to the use of two-dimensional airfoil data and a traditional blade-element model or actuator-disk model is the removal of three-dimensional effects. The most notable effects are stall delay, tip loss, yawed flow effects and unsteady rotor aerodynamics. Care must be taken these are properly accounted for either within RotCFD or by applying the proper models to the airfoil data tables in C81 format.

The model will be applied to cases of the XV-15 rotor model on the Tiltrotor Test Rig (TTR) with struts in the two NFAC facilities under various flow conditions, pylon angles and rotor conditions. The performance with geometry, in terms of thrust and power, will be compared to isolated rotor performance in both free field and the wind tunnel test sections of the NFAC.

# 1.1 Research Question and Goal

The main research question to be solved is phrased as follows:

“To what extent will wind tunnel wall interference influence future performance measurements of the Civil Tilt Rotor (CTR) program in the National Full-Scale Aerodynamics Complex (NFAC) at NASA Ames Research Center?”

The aim is to find the influence of the wind tunnel by modeling the TTR in the wind tunnel and in free field, and to determine the difference – if any - in performance. These deltas can be used to check the currently existing correction code and determine its compatibility with tilt rotor wind tunnel testing. The goal of this research is formally expressed as follows:

“To understand and quantify the influence of wind tunnel testing to LCTR research programs at NASA Ames Research Center by assessing wind tunnel wall interference using a CFD approach. “

The main goal is divided into sub goals that constitute the work breakdown structure as described in the project proposal and plan.

# 2 Literature Study & Background

Tilt rotors have the inherent capability to hover and fly in airplane mode or tilt mode. Because each of these modes has their own characteristics a short section of rotorcraft aerodynamics is included. This section will also provide a brief review on the Navier Stokes equations and CFD, and a short description of the National Full-Scale Aerodynamics Complex (NFAC) and Tiltrotor Test Rig (TTR). Lastly, the general characteristics of the XV-15 rotor are discussed and the selected experimental and theoretical performance data used for validation are presented.

# 2.1 Rotorcraft Aerodynamics

Hover is the defining characteristic of a helicopter; during hover the rotor produces lift but has no relative velocity to the air. A time-accurate representation of the wake and performance is very complicated to accurately compute. The analysis of a free field hover case also poses as the most computationally expensive as the rotor wake and inflow are solely developed by the rotor - no free stream component is present and thus relatively slow convergence occurs because of the slow induced velocity propagation. Furthermore, the boundaries must be set relatively far from the rotor in order to not influence the flow field.

During edgewise forward flight the rotor moves through the air with a small forward tilt. This forward tilt contains the small forward component of the thrust vector that provides the propulsive force for the helicopter. In contrast to hover different flow phenomena arise here. Because of the freestream flow of air the advancing side of the rotor will experience a higher relative velocity than the retreating side of the rotor. This results in dissymmetry of lift and is normally accounted for by rotor trim. For this analysis no rotor trim will be considered and it is assumed that the total trust produced during trimmed forward flight is comparable to the untrimmed, ‘averaged’, rotor. The ratio of relative velocity over tip speed, V/ΩR, is used as definition for the advance ratio in this research.

If the tilt rotor’s pylon is lowered to airplane mode the rotor acts like an airplane propeller. Pylon angles between airplane and hover mode will be called tilt mode and can exhibit characteristics of both modes. Flight modes are considered with thrust values only well within the XV-15’s flight envelope for this research to avoid (excessive) blade stalling. Autorotation will not be considered during this research. Furthermore, neither steady nor unsteady aeroelastic effects will be considered for this research as they are too small for the XV-15 to be important here [2].

# 2.1.1 Ground Effect Significance

When a helicopter descends and reaches a proximity to the ground of around one rotor diameter it can experience ground effect. At the ground the wake velocity is reduced to zero which can result into pressure changes that can be transferred up to the rotor disk. With lower velocity and thus higher pressure on the bottom side of the disk the helicopter consumes less power for equivalent lift. This effect will increase as the distance to the ground is decreased. Figure 2.1 shows the general increase of thrust when the distance to the ground is decreased, according to various analytical models [3].

图片摘要：该图主要展示 2.1 Ground effect; thrust increase at constant power [3]。
![](images/21ffd4f970fae07f22bfb6d0bc3dbfee286cd8c1b1fc441c19e5f22d96fdeaf0.jpg)  
Figure 2.1 Ground effect; thrust increase at constant power [3].

Ground effect influence decreases with forward speed due to deflection of the wake as can be seen in Figure 2.2. The ground effect is generally negligible when the rotor is more than one rotor diameter above ground [3].

图片摘要：该图主要展示 2.1 Ground effect; thrust increase at constant power [3]。
![](images/f9399749db34fbd51f1e4bf2355d282cd6db10747969af27d802d8cd7d95c4f9.jpg)  
Figure 2.2 Ground effect; influence of forward speed on ground effect [3].

The graphs illustrating ground effect are only valid for use with a single ground plane. In a closed throat wind tunnel the complexity is increased as the rotor is effectively placed in a box with two open sides.

# 2.1.2 The Traditional Actuator Disk Model and Blade Element Model

Several well-known models for rotors have been developed. The most well known are the Actuator Disk Model (ADM) based on momentum theory and the Blade Element Model (BEM). The traditional Actuator Disk Model is based on a uniform disk which supports and instantaneous pressure difference on either side of the disk. The pressure jump accelerates air over the disk until it reaches a finite velocity in the wake. Figure 2.3 shows the concept for an actuator disk in hover [4].

图片摘要：该图主要展示 2.2 Ground effect; influence of forward speed on ground effe。
![](images/8899249ec275d1ce020749a7f6c886907ab32e4a0e4c3f64d93a8e385d29fda8.jpg)  
Flow Field

图片摘要：该图主要展示 2.3 Schematic representation of actuator disk in hover [4]。
![](images/bd382493a8a1034923b35219526d4505f79c0dc5b6e4c946c2e89b4f04c01324.jpg)  
Pressure

图片摘要：该图主要展示 2.3 Schematic representation of actuator disk in hover [4]。
![](images/15d6994c3272f0efff6fd66b7a9da1c83ebf10ae5bc7b82bfa7899a70044ac09.jpg)  
Velocity   
Figure 2.3 Schematic representation of actuator disk in hover [4].

Assuming incompressible flow Bernoulli’s equation can be evaluated before and after the rotor disk. Equation ( 2.1 ) shows the balance upstream and just before the rotor disk, while Equation ( 2.2 ) shows the balance just after the rotor disk and far downstream.

$$
p _ {\infty} = p _ {i} + \frac {1}{2} \rho v _ {i} ^ {2} \tag {2.1}
$$

$$
p _ {i} + \Delta p + \frac {1}{2} \rho v _ {i} ^ {2} = p _ {\infty} + \frac {1}{2} \rho v _ {i} ^ {2} \tag {2.2}
$$

From Equation ( 2.1 ) and ( 2.2 ) the increase of pressure, $\Delta p ,$ is found to be $1 / 2 \rho \mathrm { v } _ { \infty } ^ { 2 }$ . This change in pressure is, however, equal to the thrust per unit area, as shown in equation ( 2.3 ). Combined with the knowledge that, for momentum conservation, the thrust on the disc is the rate of increase of momentum, ${ T } = \rho A v _ { i } v _ { \infty }$ a second expression for $\Delta p$ is obtained in equation ( 2.3 ). From Equations ( 2.1 ), ( 2.2 ) and ( 2.3 ) the relation for the downstream wake velocity according to momentum theory is now obtained in Equation ( 2.4 ). These values are used later on in the definition of the figure of merit.

$$
\Delta p = \frac {T}{A} = \frac {\rho A v _ {i} v _ {\infty}}{A} = \rho v _ {i} v _ {\infty} \tag {2.3}
$$

$$
v _ {\infty} = 2 v _ {i} a n d T = 2 \rho A v _ {i} ^ {2} \tag {2.4}
$$

Due to the homogenous disk the traditional actuator disk model is not very accurate when examining, for example, climb or edgewise flight. In these cases the non-uniform loading of the disk results in simulated performance values that can significantly diverge from the experimental ones.

In the Blade Element Model (BEM) basic airfoil theory is applied to a rotating blade. Computation of the resultant velocity, taking into account the inflow, climb and rotational velocities, makes it possible to compute the sectional lift and drag forces. These are integrated to obtain the resulting thrust and torque coefficients. The accuracy was improved by implementing so-called prescribed or free wakes when the model was developed further. These wakes made it possible to generate the induced velocities at the rotor plane, yielding more accurate performance measurements.

In RotCFD the model is placed in a CFD environment and the wake is developed by the NS equations. RotCFD incorporates two rotor models, both based on the sectional coefficients, which are placed in a CFD environment. The ‘steady’ model uses an averaged BEM to come to a model similar to the actuator disk. The term steady is chosen because within the disk the discrete blade loading is averaged. This is advantageous as this can yield less stringent time step restrictions. The disk is however not homogenous, in contrast to the ‘traditional’ ADM. The ‘unsteady’ model is based on a BEM, with discrete blades.

From RotCFD the thrust, power and figure of merit are obtained internally. The thrust and power are non-dimensionalized using equations ( 2.5 ) and ( 2.6 ), respectively. The thrust is normal to the disk plane.

$$
C _ {T} = \frac {T}{\rho A (\Omega R) ^ {2}} \tag {2.5}
$$

The rotor shaft power is positive when power is supplied to the rotor.

$$
C _ {P} = \frac {P}{\rho A (\Omega R) ^ {3}} \tag {2.6}
$$

The geometric blade solidity is equal to the blade area over the rotor disk area. It is used for this calculation since only aerodynamic sections of the blade are modeled in this analysis (no hub or non-aerodynamic blade parts are included), as shown in Equation ( 2.10 ). The solidity value in literature is found to be 0.089 for the physical rotor [5]. The traditional value of this solidity, however, appears to assume that the chord extends all the way inboard to zero radius. The actual blade has both taper and root cutout [6].

$$
\sigma = \frac {N c R _ {e}}{A} = \frac {N c R _ {e}}{\pi R ^ {2}} \approx 0. 0 8 1 \tag {2.7}
$$

The blade chord is assumed constant in this instance. The figure of merit is extracted directly from RotCFD. The full data table for the steady results is included in Appendix C. All plots for the unsteady model and full data table are included in 0.

# 2.1.3 The Figure of Merit

The figure of merit is a quantification of the efficiency of the rotor in hover. It compares the induced power, the power necessary for the lift obtained, to the total power, as shown in Equation ( 2.8 ). The total power consists of the induced power and the profile power, the power necessary to overcome the aerodynamic drag of the blades.

$$
M = \frac {P _ {i}}{P _ {i} + P _ {o}} = \left(1 + \frac {P _ {o}}{P _ {i}}\right) ^ {- 1} = \left(1 + \frac {C _ {P o} \sqrt {2}}{C _ {T} ^ {3 / 2}}\right) ^ {- 1} \tag {2.8}
$$

The last expression is found by substituting the profile power by non-dimensionalizing it with the rotor tip speed, ΩR, as shown in Equation ( 2.9 ). Furthermore the induced power is substituted with the use of Equation ( 2.10 ) and ( 2.11 ) to include the thrust coefficient.

$$
C _ {P _ {o}} = \frac {P _ {o}}{\rho A (\Omega R) ^ {3}} \tag {2.9}
$$

The change in kinetic energy per unit time is $1 / 2 ( \rho A v _ { i } ) v _ { \infty } ^ { 2 }$ which, combined with Equation ( 2.4 ) yields $T v _ { i } ,$ or the definition of the induced power. Equation ( 2.11 ) shows how the thrust is non-dimensionalized using the representative tip speed.

$$
P _ {i} = T v _ {i} = T ^ {3 / 2} \sqrt {2 \rho A} \tag {2.10}
$$

$$
C _ {T} = \frac {T}{\rho A (\Omega R) ^ {2}} \tag {2.11}
$$

# 2.1.4 Rotor Performance Corrections

For a blade element or actuator-disk model there are several factors that might contribute to inaccuracies in the simulations. The most influential ones are: stall delay, tip loss, yawed flow effects and unsteady rotor aerodynamics that might all contribute to inaccuracies. RotCFD is assumed to internally resolve the last two effects due to the gridded rotor disk (or blade) and unsteady nature of the solver. Stall delay and tip loss must, however, be properly accounted for. The detailed approach to these corrections is described in Section 3.2. Because the C81 airfoil data tables and airfoil reference data is all acquired at full scale, no scaling corrections, or Reynolds number corrections, are adopted. The three dimensionality of the blade can, however, never be fully accounted for.

# 2.2 Navier-Stokes Equations and CFD

CFD is the Analysis of fluid flow. One of the key drawbacks was the tremendous complexity of the behavior which let the economical use of CFD to be only possible for the wider industrial community since the 1990s [7]. With the rapid and continuous growth in computing power CFD research and development continues to improve efficiency and capability.

The three important equations are the continuity, the momentum or Navier-Stokes equations, and the energy equations, which are in principal solely based on the conservation of mass, Newton’s second law and the conservation of energy, respectively. RotUNS uses an incompressible flow, this means the energy equation can be decoupled form the analysis, and continuity and momentum equations are sufficient to solve for the velocity and pressure fields. The transfer of heat is not taken into consideration.

# 2.2.1 Continuity Equation

The continuity equation is based on the physical principle that mass can neither be created nor destroyed. The mass conservation is assured by setting the net mass flow out of the control volume through a surface equal to the time rate of decrease of mass inside the control volume. The continuity equation in conservation form is shown in Equation ( 2.12 ).

$$
\frac {\partial \rho}{\partial t} + \nabla \cdot (\rho \boldsymbol {V}) = 0 \tag {2.12}
$$

For an incompressible flow the density is constant so $\begin{array} { r } { \frac { \partial \rho } { \partial t } = 0 } \end{array}$ and since the density is not equal to zero equation ( 2.12 ) can be rewritten to equation ( 2.13 ).

$$
\nabla \cdot \boldsymbol {V} = 0 \tag {2.13}
$$

# 2.2.2 Momentum Equation

The momentum equations for a viscous flow are called the Navier-Stokes equations. The momentum equation is based on Newton’s second law. The momentum equation in conservation form for the x-, y- and z-direction can be derived as shown in equation ( 2.14 ), ( 2.15 ) and ( 2.16 ), respectively [8]. Together they are called the Navier-Stokes equations, with $\tau _ { i j }$ representing the viscous stress tensor.

$$
\frac {\partial (\rho u)}{\partial t} + \nabla \cdot (\rho u \boldsymbol {V}) = - \frac {\partial p}{\partial x} + \frac {\partial \tau_ {x x}}{\partial x} + \frac {\partial \tau_ {y x}}{\partial y} + \frac {\partial \tau_ {z x}}{\partial z} + \rho f _ {x} \tag {2.14}
$$

$$
\frac {\partial (\rho v)}{\partial t} + \nabla \cdot (\rho v \boldsymbol {V}) = - \frac {\partial p}{\partial y} + \frac {\partial \tau_ {x y}}{\partial x} + \frac {\partial \tau_ {y y}}{\partial y} + \frac {\partial \tau_ {z y}}{\partial z} + \rho f _ {y} \tag {2.15}
$$

$$
\frac {\partial (\rho w)}{\partial t} + \nabla \cdot (\rho w \boldsymbol {V}) = - \frac {\partial p}{\partial z} + \frac {\partial \tau_ {x z}}{\partial x} + \frac {\partial \tau_ {y z}}{\partial y} + \frac {\partial \tau_ {z z}}{\partial z} + \rho f _ {z} \tag {2.16}
$$

The left hand terms of these equations correspond to the unsteady and convection forces respectively. The terms on the right hand side correspond to the pressure, diffusion and external forces.

By decomposing the NS equations (and the continuity equation) for incompressible fluids into a time-averaged part and a fluctuating part the Reynolds Averaged Navier-Stokes equations for incompressible flow can be derived. This approach still allows for unsteady simulations because only the random turbulence on small scale will be averaged out. The incompressible RANS equation is shown in Equation ( 2.17 ) [9].

$$
\frac {\partial \left(\rho \bar {u} _ {i}\right)}{\partial t} + \frac {\partial}{\partial x _ {j}} \left(\rho \bar {u} _ {i} \bar {u} _ {j}\right) = - \frac {\partial \bar {p}}{\partial x _ {j}} + \frac {\partial \left(\bar {\tau} _ {i j} - \rho \bar {u} _ {i} ^ {\prime} \bar {u} _ {j} ^ {\prime}\right)}{\partial x _ {j}} \tag {2.17}
$$

# 2.2.3 Rotorcraft Computational Fluid Dynamics (RotCFD)

The flow solver needs to handle unsteady rotor simulations while being computationally inexpensive. Rotorcraft CFD (RotCFD) is a mid-fidelity CFD tool specifically for rotorcraft design efforts and has been developed recently [10]. Young performed a study on complex rotor wake interaction simulation using RotCFD [11]. Rotorcraft Unstructured Solver (RotUNS) is a module within RotCFD that uses three-dimensional, unsteady, incompressible Reynolds-Averaged Navier-

Stokes equations (URANS) on a Cartesian unstructured grid with tetrahedral body-fitting near the body. The SIMPLER (Semi-Implicit Method for Pressure-Linked Equations Revised) is used in combination with the under relaxation factors to iteratively obtain the correct flow field in agreement with both the continuity and momentum equation.

The module of RotCFD used in this research is RotUNS (Rotor Unstructured Solver). This name will be used synonymous to RotCFD from now on. Spalart discusses the possible pitfalls with the use of URANS but also indicates it is one of the few feasible unsteady methods when computational budget is limited [12]. Iaccarino et al. show the differences in simulated flow field using both a steady and unsteady Reynolds Averaged Navier-Stokes approach for the flow over a cube [13].

Turbulence is accounted for by the URANS equations combined with a two-equation realizable k-ε turbulence model with special wall treatment. The two transported variables are $k ,$ the turbulent kinetic energy, and $\varepsilon ,$ the turbulent dissipation. Jones and Launder presented and validated the k-ε turbulence model in the 1970s [14], [15]. Yu & Cao have shown that accurate CFD analyses for the flow field and performance of a helicopter in forward flight can be obtained with a k-ε turbulence model with wall function method [16]. The wall function is introduced because the no-slip condition near the wall is found to behave unsatisfactory if the k-ε turbulence model is applied without this correction.

Discretization is done using the finite-volume method and the implicit solver has been used in order to have a less stringent stability criterion and therefore more flexibility for various operations. This allows using consistent spatial and temporal grid under various cases more easily. The time-dependent solution, however, might not follow the exact transients as accurately as an explicit approach [17]. After the initial choice this has not been further investigated for this research.

# 2.2.4 The RotCFD Rotor Model

The rotor is modeled only through the momentum it imparts on the flow. “From the point of the fluid particles, the influence of the spinning rotor is to change their momentum.” as stated in the original paper on this approach [18]. This momentum change occurs because of the aerodynamic forces exerted on the cells through the spinning blades. The fully viscous, unsteady, body-conforming grid usually chosen for such a problem is not necessary anymore, greatly reducing the complexity. Also the no-slip condition on the rotor is omitted and no unsteady boundary layer has to be resolved on a very dense grid, which also reduced the complexity. This reduction in complexity in turn is manifested through the possibility to run problems on desktop-class computers, where unsteady rotor simulations using full Navier-Stokes equations with turbulence models and body-conforming grid generally require supercomputers [18].

The source depends on the flow properties, rotor geometry, and two-dimensional airfoil data as shown in Equation ( 2.18 ). Where $c _ { I }$ and $c _ { d }$ are the airfoil section coefficients, $\alpha$ is the angle of attack, $V _ { a b s }$ is the absolute instantaneous velocity vector at the airfoil section, Ω is the rotational velocity, $x , y , z$ are the Cartesian coordinates, t is time, $c$ is the chord, $\rho$ is the density and $^ { b }$ is the number of blades.

$$
\boldsymbol {S} = S \left(c _ {l}, c _ {d}, \alpha , \boldsymbol {V} _ {a b s}, \Omega , x, y, z, t, c, \rho , b\right) \tag {2.18}
$$

Figure 2.4 shows a schematic drawing of the rotor and the $( r , \phi , z )$ inertial coordinate system fixed at the rotor used in the derivation of the momentum sources.

图片摘要：该图主要展示 2.4 shows a schematic drawing of the rotor and the inertial 。
![](images/fc60f1ae7c797412a7a9b8f8eb6cb382ae460ad82e4f8603b7186fd77a2e64eb.jpg)  
Figure 2.4 Rotor and coordinate system [18].

The rotor model uses a version of the BEM called the ‘steady’ rotor model where the discrete rotor source terms can be averaged over the disc. This creates a model comparable to the traditional ADM, with the major differences that the disk is not, or doesn’t have to be, experiencing a homogenous load. An ‘unsteady’ rotor model based on the blade-element model is also tested; this model does use the discrete blades, hence ‘unsteady’, blade modeling. The effect on the fluid is considered only at the point where the rotor, or disc if the ‘steady’ model is used, intersects with a grid point from the CFD domain. In the unsteady model a line at the quarter chord location replaces the chord length of the rotor.

图片摘要：该图主要展示 2.4 Rotor and coordinate system [18]。
![](images/c37223bfd5c4a20146dc0927a1b5b4ed399bc045135fa21c804aab6a1cd4d15b.jpg)  
Figure 2.5 shows the nomenclature of a blade section (see A-A in Figure 2.4) used to derive the source terms $S \phi$ and $S _ { z } ,$ aligned with tangential force coefficient, $c _ { t } ,$ and normal force coefficient, $c _ { n } ,$ respectively. The absolute velocity, $V _ { a b s , }$ consists of components $V _ { r } , V _ { \phi }$ and $V _ { Z }$ and the relative velocity, $V _ { r e I } ,$ constists of components vr’, $V \phi ^ { ' }$ and ${ v _ { z } } ^ { \prime }$ .   
Figure 2.5 Blade section nomenclature at a grid point [18].

The normal and tangential (to the disk) coefficients can be derived from Figure 2.5 as shown in Equation ( 2.19 ) and ( 2.21 ).

$$
c _ {n} = c _ {l} \cos \beta - c _ {d} \sin \beta \tag {2.19}
$$

$$
c _ {t} = c _ {l} \sin \beta + c _ {d} \cos \beta \tag {2.20}
$$

The angle $\beta ,$ the angle between the relative Velocity, $V _ { r e I _ { \prime } }$ and the disk plane is obtained from Equation ( 2.21 ). Note that the relative velocity in $\phi$ -direction is composed of the sum of the local flow component and the component through blade rotation at the radial station the blade section is chosen.

$$
\tan \beta = \frac {v _ {z} ^ {\prime}}{v _ {\varphi} ^ {\prime}} \tag {2.21}
$$

And the angle of attack, $\alpha ,$ is now deduced in Equation ( 2.22 ).

$$
\alpha = \theta - \beta \tag {2.22}
$$

The section properties of the airfoil are determined from the angle of attack and Mach number, derived solely from the relative velocity, and inputted into Equation ( 2.19 ). The normal and tangential force coefficients can now be converted to $\phi$ and $\mathbf { Z }$ -direction,as shown in equation(2.23) and(2.24).

$$
c _ {z} = - c _ {n} \tag {2.23}
$$

$$
c _ {\varphi} = - c _ {t} \tag {2.24}
$$

The rotor blades are divided into spanwise elements. The blade geometric properties are constant over an element, and hence the source terms per unit element can be derived as shown in Equation ( 2.25 ) and ( 2.26 ).

$$
s _ {z} = c _ {z} \left(\frac {1}{2} \rho V _ {r e l} ^ {2} c\right) \tag {2.25}
$$

$$
s _ {\varphi} = c _ {\varphi} \left(\frac {1}{2} \rho V _ {r e l} ^ {2} c\right) \tag {2.26}
$$

These terms are changing as the rotor moves through the grid. In case the ‘steady’ model is chosen, the sources terms are averaged over the rotor disk while spinning. An example of the differences in the velocity field at the rotor disk for a steady and unsteady rotor model is shown in Figure 2.6 and Figure 2.7, respectively. Defining the time for one rotor revolution as trev and the time taken by a blade section to go through the width of a cell as $t _ { c e I I }$ and $^ { b }$ the number of blades the averaged sources terms can be derived in Equations ( 2.27 ) and ( 2.28 ), assuming hover. For other flight modes the individual blades will have to be averaged as they experience different loading.

$$
s _ {z} ^ {\prime} = \frac {b s _ {z} t _ {c e l l}}{t _ {r e v}} = \frac {\Omega b s _ {z} t _ {c e l l}}{2 \pi} \tag {2.27}
$$

$$
s _ {\varphi} ^ {\prime} = \frac {b s _ {\varphi} t _ {c e l l}}{t _ {r e v}} = \frac {\Omega b s _ {\varphi} t _ {c e l l}}{2 \pi} \tag {2.28}
$$

图片摘要：该图主要展示 2.6 Velocity plot of a steady model。
![](images/15fe17424275d8846ddc7760062014c3de01519713bca60b0dd246992200df24.jpg)  
Figure 2.6 Velocity plot of a steady model.

图片摘要：该图主要展示 2.6 Velocity plot of a steady model。
![](images/320dd6f99e267fbad19f35be5895c920b1b82d7dd19db9043176c1360923d301.jpg)  
Figure 2.7		Velocity plot of an unsteady model.

The source terms, defined in the inertial coordinate system fixed at the rotor, can be converted to the Cartesian coordinate system used in RotCFD. Integrating the z-coordinate of the source terms yields thrust whereas the integrated $\phi$ -direction source can be multiplied by the rate of rotation to obtain the (profile) power. The induced power is obtained by multiplying the thrust with the induced velocity.

Please note the rotor precone angle has not been taken into account in this derivation, but is used in RotCFD and this research. However, no sweep angle is considered. Note how no component in r-direction is deduced, implying no radial effects are considered. Figure 2.8 and Figure 2.9 shows a representative example of the rotor (source) program grid with the cell structure underneath. The blades are only shown for visualization purposes.

图片摘要：该图主要展示 2.7 Velocity plot of an unsteady model。
![](images/993a5c96016b90a407b3896249c54f5326a25ca99891c0da86591362de466959.jpg)  
Figure 2.8 Top view of rotor disk grid and flow field grid.

图片摘要：该图主要展示 2.8 Top view of rotor disk grid and flow field grid。
![](images/42009c2e84d28dd2425e355e21cf85c5cdb80582ac0e8ff2521b275d380812b9.jpg)  
Figure 2.9 Enlarged view of the rotor disk grid and flow field grid.

# 2.2.5 Some considerations with the use of RotCFD

The RotCFD approach leads to an indirect relationship between the viscous effects and the action of the rotor blades. This approach therefore cannot give you the same results as the full NS solution would. Also dynamic stall, or any effect for which the boundary layers or actual rotor geometry must be known will probably not be evaluated properly. An example is the radial flow on the rotor blades that cannot be modeled. This is also the exact reason a stall delay model is evaluated in this research.

Even though the rotor is based solely on two-dimensional airfoil data, because of the implementation into a flow field grid, some of the three-dimensional effects, for example tip loss, can be expected. RotCFD can incorporate flapping or cyclic pitch, but this is thought to be beyond the scope of the current research.

# 2.3 National Full-Scale Aerodynamics Complex (NFAC)

The isolated rotor wind tunnel tests for the tilt rotor research programs at NASA Ames Research Center are scheduled in May 2016 in the National Full-Scale Aerodynamics Complex (NFAC, Figure 2.10) 40- by 80-/80- by 120-Foot Wind Tunnels that are managed and operated by the U.S. Air Force. The original XV-15 research has been performed in the 40- by 80- Foot Wind Tunnel [19]. Zell has written elaborate reports on the performance and flow characteristics of both wind tunnels [20], [21]. Further aerodynamic characteristics are described by Corsiglia [22].

图片摘要：该图主要展示 2.10 The NFAC facility at NASA Ames Research Center. 3。
![](images/d7c5665d55d62c18af236c35855bdf21d14f38dc042bb9ccb4e7953e0852cc86.jpg)  
Figure 2.10 The NFAC facility at NASA Ames Research Center. 3

# 2.3.1 Wind Tunnel and Test Section Geometry

The two wind tunnels that comprise the NFAC facility share portions of their flow path. The cross section of the 80- by 120- Foot Wind Tunnel is an open circuit wind tunnel with a closed, rectangular test section (Figure 2.11). The 40- by 80-Foot Wind Tunnel is a single-return, closed section wind tunnel with an oval test section (Figure 2.11).

图片摘要：该图主要展示 2.10 The NFAC facility at NASA Ames Research Center. 3。
![](images/ca1bea1a2688c547515efc54738a97940bf51411e776690978e5f8458c58a76f.jpg)  
Figure 2.11 Sketch of the 80- by 120-Foot Wind Tunnel and 40- by 80-Foot Wind Tunnel, respectively [20].

The geometry of the cross section is obtained from NFAC studies [20], [21] and sketched in Figure 2.12. The distinct differences in test section cross sectional geometry will result in a different flow behavior when the rotor flow is simulated. Because of the larger test section of the 80- by 120-Foot Wind Tunnel it is expected to show less interference with wind tunnel walls. The 40- by 80-Foot Wind Tunnel, besides having a smaller test section, is expected to show more wind tunnel interference with the rotor wake due to its smaller and oval cross sectional test section shape. The dimensions of the actual cross section are reduced slightly after the addition of acoustic liner. The inner dimensions of the test section are shown in Figure 2.12. The boundary layer profile was found not to change significantly with any of the tunnel operating variables [21].

图片摘要：该图主要展示 2.11 Sketch of the 80 by 120 Foot Wind Tunnel and 40 by 80 F。
![](images/01195b72dd09077d7ac33c67a47821b8cbaec667298a25fe072c687de6108bd4.jpg)

图片摘要：该图主要展示 2.11 Sketch of the 80 by 120 Foot Wind Tunnel and 40 by 80 F。
![](images/90f3eb6d8bdfe2fc4fdd22e0b2e500aa99e77713dd9dd86df125939c9487407d.jpg)  
Figure 2.12 The 80- by 120-Foot Wind Tunnel and 40- by 80-Foot Wind Tunnel cross section in the NFAC [20], [21].

# 2.3.2 Wind Tunnel Wall Corrections

For positive thrust the velocity in the rotor slipstream will have a higher velocity than the wind tunnel velocity. Since both tunnels are closed-throat continuity dictates the velocity outside of the slipstream has a lower velocity. This lower velocity has a higher static pressure that works its way to the back of the rotor increasing the thrust [23]. The thrust could therefore result in a rotor reaching equal thrust at a lower free stream velocity. However, it might be possible under low-thrust (i.e. cruise) conditions, that the wake of the struts, with lower than free stream velocity, counteracts this effect in exactly the opposite way. Pope and Rae [24] describe the influence of rotor testing in tunnels based on earlier work by Glauert [23]. Figure 2.13 shows a schematic sketch of a rotor with wake in a wind tunnel and generic velocities. This sketch is only valid for airplane mode flight (axial flow).

图片摘要：该图主要展示 2.12 The 80 by 120 Foot Wind Tunnel and 40 by 80 Foot Wind T。
![](images/3839a22e5990268744000ea2a58c9997fff61f9f6f029b6091990e6eabf0c4cd.jpg)  
Figure 2.13 Propeller in closed throat wind tunnel [24].

In edgewise flight this wind tunnel interference effect might be combined with an experienced ‘ground effect’ as the wake could reach the wall below a certain free stream velocity threshold. It is likely this effect is only to be expected in the 40- by 80-Foot Wind Tunnel, if at all. During tilt mode, a combination of this effect with the axial flow interference effects could take place. All in all it is expected that pressure buildup will result in higher pressure differences on the rotor increasing performance in the wind tunnel, compared to true free field conditions. The characteristics of the NFAC which have been used in this research are presented in Appendix A.

图片摘要：该图主要展示 2.13 Propeller in closed throat wind tunnel [24]。
![](images/df7db069d4773e5676161f815149c9f94ffc62c55bc0a52ee9ba4efd75911532.jpg)  
Figure 2.14 The author at the (enormous) 80-by 120-Foot Wind Tunnel Inlet.4

# 2.4 Tiltrotor Test Rig (TTR)

During the actual wind tunnel tests in the NFAC, the isolated rotor will be mounted on the Tiltrotor Test Rig to allow for the control of powered rotor tests. The TTR (Figure 2.15 and Figure 2.16) is the modern version of the Proprotor Test Rig (PTR) after it needed replacement to allow for more advanced rotors. The TTR is mounted on three struts and four refurbished electric wind tunnel engines provide the power to the rotor. Table 2.1 contains the main design capabilities of the TTR. At the time of writing the calibration of the TTR has finished a couple of months ago and the stage of powered tests have been started.

图片摘要：该图主要展示 2.14 The author at the (enormous) 80 by 120 Foot Wind Tunnel。
![](images/2367e3ee37ef33e951fdfba1f39cb1212e3185111377ae034bdd9a3bb33fb022.jpg)  
Figure 2.15 The TTR on the aft calibration stand, with cowlings open. 5

图片摘要：该图主要展示 2.15 The TTR on the aft calibration stand, with cowlings ope。
![](images/59f5dbae36dfabc693a35f18014ceb2450c01b8517bad7256d8f06bad445d0d5.jpg)  
Figure 2.16 The author at the TTR with the calibration rig mounted.6

Rotor forces will be measured on a dedicated balance installed within the TTR, instead of using the wind tunnel balance system. The wind tunnel turntable can rotate the TTR from axial to edgewise flight and all angles in between. The strut geometry in the 80- by 120-Foot Wind Tunnel has not yet been decided on at the time of writing [6] and will therefore be based on the 40- by 80-Foot Wind Tunnel struts.

Table 2.1 Key TTR Design Capabilities [25].   

<table><tr><td colspan="2">Maximum Wind Speed (kts)</td></tr><tr><td>Axial (Airplane)</td><td>300</td></tr><tr><td>Edgewise (Hover)</td><td>180</td></tr><tr><td colspan="2">Rotational Speed (rpm)</td></tr><tr><td>Minimal</td><td>126</td></tr><tr><td>Maximal</td><td>630</td></tr><tr><td colspan="2">Maximum Thrust (Ibs)</td></tr><tr><td>Steady</td><td>20,000</td></tr><tr><td>Peak</td><td>30,000</td></tr></table>

# 2.5 XV-15 Rotor Characteristics

The rotor parameters are summarized in Table 2.2. The value of the precone is that used for the Outdoor Aerodynamic Research Facility (OARF) test, which will be discussed later. The NACA 64-X25 airfoil at radial station $r / R = 0 . 2 5 0 0 [ \sim ]$ is copied to the root value at the cutout at $r / R = 0 . 0 8 7 5 \ [ \sim ]$ (marked with the ‘*’ in Table 2.2) to provide aerodynamic information at the root and prevent erroneous extrapolation of airfoil data. This, instead of using an extrapolation method, is common practice in rotor research [6]. The original airfoil sectional data files and adjusted or corrected files are public domain but have not been included because of their size.

Table 2.2 XV-15 Rotor Characteristics [5], [6], [26]–[29].   

<table><tr><td colspan="3">Blade Geometry</td></tr><tr><td>diameter</td><td>7.62 m</td><td>(25 ft.)</td></tr><tr><td>disc area</td><td>45.6 m²</td><td>(491 ft.²)</td></tr><tr><td>blade chord @.0875R</td><td>0.432 m</td><td>(17 in.)</td></tr><tr><td>blade chord @1.000R</td><td>0.356 m</td><td>(14 in.)</td></tr><tr><td>blade area</td><td>4.06 m²</td><td>(43.75 ft.²)</td></tr><tr><td>root cutout</td><td>0.0875 r/R</td><td></td></tr><tr><td>solidity</td><td>0.089</td><td></td></tr><tr><td colspan="3">Blade Twist (bilinear)</td></tr><tr><td>chord-line aerodynamic</td><td>38.7°</td><td></td></tr><tr><td>total chord</td><td>41.5°</td><td></td></tr><tr><td colspan="3">Blade Airfoil Section, r/R [~]</td></tr><tr><td>0.0875</td><td>NACA 64-X25*</td><td></td></tr><tr><td>0.2500</td><td>NACA 64-X25</td><td></td></tr><tr><td>0.5268</td><td>NACA 64-X18</td><td></td></tr><tr><td>0.8093</td><td>NACA 64-X12</td><td></td></tr><tr><td>1.0000</td><td>NACA 64-X08</td><td></td></tr><tr><td colspan="3">Rotor Characteristics</td></tr><tr><td>hub precone angle</td><td>2.5°</td><td></td></tr><tr><td colspan="3">Rotor rpm</td></tr><tr><td>helicopter mode (hover, edgewise)</td><td>589</td><td></td></tr><tr><td>airplane mode (axial)</td><td>517</td><td></td></tr><tr><td colspan="3">Blade tip speed</td></tr><tr><td>helicopter mode (hover, edgewise)</td><td>225.55 m/s</td><td>(740 ft/s)</td></tr><tr><td>airplane mode (axial)</td><td>182.88 m/s</td><td>(600 ft/s)</td></tr></table>

# 2.5.1 XV-15 Rotor Blade Characteristics

The main parameters that are needed for the rotor are the twist and chord distribution, two-dimensional airfoil data along the span of the XV-15 blade, and the characteristic dimensions of the rotor. Some conflicting values were found in different publications [5], [26]–[29]; as an example the XV-15 was flown with multiple hub configurations leading to differently listed precone angles. The final values were decided in collaboration with experienced XV-15 researchers [6]. All input requirements for the computation of the rotor source, S, in RotCFD are presented in Equation ( 2.29 ).

$$
\boldsymbol {S} = S \left(c _ {l}, c _ {d}, \alpha , \boldsymbol {V} _ {a b s}, \Omega , x, y, z, t, c, \rho , b\right) \tag {2.29}
$$

The blade chord-line twist distribution is shown in Figure 2.17 and the blade chord distribution is shown in Figure 2.18.

图片摘要：该图主要展示 2.17 XV 15 rotor blade chord line twist distribution [6]。
![](images/ba185a647ceaddd881461ddb36d5349af31fe7e16224d943d5674b38b70e791e.jpg)  
Figure 2.17 XV-15 rotor blade chord-line twist distribution [6].

References to ‘collective’ will be implying the collective pitch angle, $\theta _ { { \boldsymbol { o } } _ { \prime } }$ which is defined zero when the pitch angle distribution equals the twist distribution in Figure 2.17. The relation with the quarter chord pitch angle, $\theta _ { . 7 5 } ,$ is defined for the XV-15 rotor model in equation ( 2.30 ).

$$
\theta_ {. 7 5} = \theta_ {0} + 6. 6 1 ^ {\circ} \tag {2.30}
$$

图片摘要：该图主要展示 2.17 XV 15 rotor blade chord line twist distribution [6]。
![](images/7a507b18c3256004a23b6c7c386089831cb3b8d984225fea69814a5d3e7a19c5.jpg)  
Figure 2.18 XV-15 rotor blade chord distribution [6].

Figure 2.19 shows the blade loci of the quarter chord, leading edge and trailing edge. The XV-15 rotor blade has approximately a -1 degree sweep angle that is not incorporated into the model because the sweep is only added for structural reasons [6].

图片摘要：该图主要展示 2.19 shows the blade loci of the quarter chord, leading edge。
![](images/22efa84ce14e4e3152f077c0b8c7ffdf597703e34ac631964d117095454a6ea6.jpg)  
Figure 2.19 XV-15 rotor blade aerodynamic loci [6].

# 2.5.2 C81 Airfoil Data Structure

The aerodynamic section properties for the blade airfoils elements are loaded from C81 data tables. The C81 airfoil data structure contains the airfoil section properties and originates from a first generation rotorcraft simulation program from Bell. The program is now outdated but the C81 format is still used, for example in CAMRAD II [30].

The format holds three two-dimensional arrays for the lift, drag and moment coefficients, cl(α,M), $c _ { d } ( \alpha , M )$ and $\mathsf { c } _ { m } ( \alpha , M ) ,$ respectively, as a function of angle of attack and Mach number. The format allows for an additional set for a trailing edge flap, this is however not used in this report or following analyses. The data format uses a separate rectangular array for each coefficient. The basic format is 10 columns, each 7 characters wide. The first column only holds the reference angle of attack, $\alpha ,$ values. If the amount of Mach number entries is greater than 9, more than one line is used for each table row ( $\alpha$ value). A new table row $\alpha$ value) must start on a new line. An example of the partial data for the lift coefficient in C81 format is shown in Figure 2.20. A brief summary of the format is further described in the CAMRAD II manual [30].

图片摘要：该图主要展示 2.19 XV 15 rotor blade aerodynamic loci [6]。
![](images/ba0c89b153d80a058bb01cbf7bd688f533f210c5b07c15d216af0becaf8352fa.jpg)  
Figure 2.20 Example format of (partial) C81 airfoil data file.

The C81 files are obtained from the Aeromechanics Branch at NASA Ames [6]. According to experienced XV-15 researchers the best available airfoil data set consists of four airfoils. The dataset is obtained using two-dimensional wind tunnel tests at full scale. The airfoil at radial station $r / R = 0 . 2 5 0 0 [ \sim ]$ is copied to the root value at the cutout, marked with the ‘*’ in Table 2.2.

# 2.6 XV-15 Performance Data

The XV-15 rotor will be used for this research because of the existing test data (wind tunnel and flight) and non-proprietary, publically available data. The XV-15 flight test data reports provide background in understanding the XV-15 and its performance [31].

XV-15 outdoor hover tests at NASA Ames have been documented by Felker and Betzina [28]. This data set was acquired on the Outdoor Aerodynamic Research Facility (OARF) test bed and will be referenced to as the ‘OARF Data’ further on in this report. This is believed to be the only full-scale data without wall effects for an XV-15 isolated rotor in hover. The Bell Helicopter company performed a study on the performance of an XV-15 isolated rotor in the NFAC facility [29] under various conditions, including edgewise and airplane mode. Johnson performed an assessment of the capability to calculate tilt rotor aircraft performance from this report [2]. It is unknown to what extent these results are influenced by the wind tunnel walls.

Theoretical results obtained with CAMRAD I (Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics) are also acquired from this reference. For the hover cases results from CAMRAD II [30], the improved version, are obtained as well. While sharing many characteristics with earlier versions of CAMRAD, CAMRAD II is completely recoded and has far more advanced options for computing rotor performance, loads, stability, etc. For predicting isolated proprotor performance, the most significant change is the introduction of stall-delay models. Here, the model developed by Corrigan and Schillings [32] is used.

It is these two reports ([28] and [2]) and the hover performance from CAMRAD II [6], [30] that form the main basis for the validation of the rotor model to be developed. Because the V-22 Osprey data is not publically accessible this is also the only

tilt rotor reference data available to validate the code. All performance data is obtained at sea level. The flight tests are assumed to be performed at a low enough altitude to render comparisons with data obtained from sealevel reasonable.

# 2.6.1 Hover

Figure 2.21 and Figure 2.22 show the power curve and figure of merit versus blade loading, respectively. The thrust and power are expressed as their non-dimensionalized coefficient values, divided by the rotor solidity. The theoretical power curves obtained from CAMRAD I and CAMRAD II show good agreement with various wind tunnel tests (WTT), flight data and the OARF data. Both curves and the corresponding data show an almost linear relation along the blade loading observed.

图片摘要：该图主要展示 2.21 and Figure 2.22 show the power curve and figure of meri。
![](images/8830a5a967f89fe82f2b3eec60da38d0d9f4ee9caae2035563556744b96f9031.jpg)  
Figure 2.21 XV-15 rotor hover power as a function of thrust [2], [6], [28].

The data points from the CAMRAD and OARF data are shown for the figure of merit plot in Figure 2.22. A considerable increase in scatter amongst the data points is observed. The figure of merit is defined as the ratio of induced over total power, as shown in Equation ( 2.31 ) [4].

$$
M = \frac {P _ {i}}{P _ {i} + P _ {o}} = \left(1 + \frac {P _ {o}}{P _ {i}}\right) ^ {- 1} = \left(1 + \frac {P _ {o}}{T v _ {i}}\right) ^ {- 1} = \left(1 + \frac {C _ {P o} \sqrt {2}}{C _ {T} ^ {3 / 2}}\right) ^ {- 1} \tag {2.31}
$$

The peak of the curve consequently corresponds with a relative decrease of the induced power, and hence the total power is relatively increasing. This usually is the point where a significant section of the blade is stalling, and therefore the figure of merit, a measure for efficiency, drops.

图片摘要：该图主要展示 2.22 XV 15 rotor hover figure of Merit as a function of thru。
![](images/098c2fcc75646afa22a35e0c7547111ef6bcb879957ac367a0b3207774ed39a3.jpg)  
Figure 2.22 XV-15 rotor hover figure of Merit as a function of thrust [2], [6], [28].

It is thought the scatter along the figure of merit values is closely related to difficulties in obtaining clean power values in experiments or accurate drag values in theoretical analyses.

# 2.6.2 Tilt

Several cases for a tilted rotor are observed in Figure 2.23. The pylon angle, $\alpha _ { p } ,$ indicates the angle of the pylon, and rotor disk, to the relative wind velocity. $\alpha _ { p } = 0$ [deg] corresponds to airplane or axial mode while $\alpha _ { p } = 9 0$ degrees is helicopter or edgewise flight. The data is shown to deviate the most from theory at a pylon angle of $\alpha _ { p } = 7 5$ degrees, attributed to deficiencies in the stall computation of CAMRAD I [2].

It is, however, crucial to note that the experimental values are obtained in the 40-by 80-Foot Wind Tunnel and might themselves exhibit wind tunnel interference effects. The tunnel interference was minimized by using various vents and panels that could be opened, reducing the blockage and alleviating the pressure. This approach has, however, not been further researched throughout this research.

图片摘要：该图主要展示 2.23 XV 15 rotor power as a function of thrust for different。
![](images/1cbfa24f930fd98af5b90b1a05765dfe20c4a975f5af41df9a8fd22a1ae8ed7b.jpg)  
Figure 2.23 XV-15 rotor power as a function of thrust for different pylon angles at $V / \varOmega R = . 3 2$ [2].

Figure 2.24 shows the influence of the advance ratio at a pylon angle of $\alpha _ { p } = 7 5$ degrees. In this report the advance ratio is defined as the relative velocity magnitude over the blade tip speed, as shown in ( 2.32 ).

$$
\mu = \frac {V}{\Omega R} \tag {2.32}
$$

图片摘要：该图主要展示 2.24 shows the influence of the advance ratio at a pylon ang。
![](images/e668f015d14439ba169b90d45531727ffb7a178ddee18b34a6c2224415302891.jpg)  
Figure 2.24 XV-15 rotor power as function of thrust, for $a _ { p } = 7 5 ^ { \circ }$ and $M _ { t i p } = 0 . 6 5$ [2].

The variation of advance ratio shows a consistent slope, but a diverging correlation as the advance ratio is increased. This deviation is thought to be attributable to the stall model in CAMRAD I, and can serve as a key comparison to rotor performance obtained with RotCFD.

# 2.6.3 Airplane Mode

Figure 2.25 shows the propulsive efficiency versus the blade loading for various tip speeds. The propulsive efficiency is calculated using Equation ( 2.33 ). Note the inherent difference to figure of merit, in Equation ( 2.31 ), which uses the induced velocity (evaluating useful power to obtain thrust) instead of the aircraft velocity (useful power to obtain propulsion).

$$
\eta = \frac {T V}{P} \tag {2.33}
$$

图片摘要：该图主要展示 2.25 shows the propulsive efficiency versus the blade loadin。
![](images/12c51dddb1b8df0f1e5fcafd8a20aec8ccb9f6178a3d0d4c83eca816e177765f.jpg)  
Figure 2.25 Rotor propulsive efficiency as function of thrust [2].

# 3 Aerodynamic Analysis Method

This section describes the application and setup of the various validation models and wind tunnel models for this research.

# 3.1 RotCFD Assumptions

During this research RotCFD (RotUNS) is used to obtain rotor performance data, isolated or in a wind tunnel. The flow is considered incompressible, hence a Mach number in the whole flowfield must be lower than $M = 0 . 3$ for the flow to be considered low-subsonic or incompressible [33].

The rotor is solely modeled through the momentum it imparts on the flow. The rotor data is obtained from two-dimensional airfoil data. It is assumed this, combined with airfoil correction methods, will yield accurate rotor performance results. Because the rotor is modeled only through the momentum sources the tip Mach number is never truly present in the flow, only the momentum change in the surrounding cells. This makes the incompressibility assumption feasible.

It is assumed that all Mach number and Reynolds number effects are considered through the momentum sources. Also dynamic stall effects, radial (boundary layer) flow effects cannot be properly obtained because there is no physical boundary layer, just the two-dimensional data.

All simulations in this research are performed with SI units at sea level and International Standard Atmosphere (ISA). The values are summarized in Table 3.1.

Table 3.1 Sea level air properties used.   

<table><tr><td>Symbol</td><td>Description</td><td>Value</td></tr><tr><td>T0</td><td>sea level temperature</td><td>288.16 [K]</td></tr><tr><td>P0</td><td>sea level air pressure</td><td>101325 [Pa]</td></tr><tr><td>ρ0</td><td>sea level air density</td><td>1.225 [kg/m3]</td></tr><tr><td>a0</td><td>speed of sound at sea level</td><td>340.29 [m/s]</td></tr><tr><td>R</td><td>gas constant</td><td>287.05 [m2/s2K]</td></tr><tr><td>μ</td><td>dynamic viscosity</td><td>1.75E-05 [m2/s]</td></tr><tr><td>γ</td><td>ratio of specific heats</td><td>1.4 [~]</td></tr></table>

# 3.2 XV-15 Airfoil Data Corrections

This section describes the airfoil data corrections performed on the XV-15 rotor model. For hover inclusion of unsteady aerodynamics and yawed flow aerodynamics has little effect on rotor thrust [32]. Furthermore it is assumed unsteady aerodynamics and yawed flow aerodynamics are covered to some extent in RotCFD’s flow field computation. The other two main sources of inaccuracies are the stall delay effect and tip loss effect, both described in the following subsections. For forward flight unsteady aerodynamics and yawed flow effects are sufficient [32].

# 3.2.1 Stall Delay Model

The effect of a rotor’s rotation on the boundary layer is crucial for obtaining the correct performance prediction of a rotor [32], primarily during hover. Because the aerodynamic data files will provide the properties of the rotor, the boundary layer will not be resolved during the simulations. Therefore, the only way of taking into account the boundary layer rotational effect is altering the C81 airfoil data tables.

Acree describes modeling requirements for analysis and optimization of the Joint-service Vertical take-off/landing Experimental Aircraft (JVX) proprotor performance [34]. A similar approach is used by altering the airfoil data tables using and applying stall delay according to the Corrigan and Schillings stall delay model [32]. The Corrigan stall delay model uses augmentation of the lift values in the C81 airfoil data tables by multiplying the section lift coefficient with a stall delay factor, $K _ { L } ,$ as shown in Equation ( 3.1 ).

Radial flow along the blade span retards the point where the boundary layers breaks which delays stall, and therefore the maximum lift coefficient. Equation ( 3.1 ) shows the computation of the Corrigan stall parameter [35].

$$
K _ {L} = \left(\frac {c / r}{. 1 3 6} \left(\frac {. 1 5 1 7}{c / r}\right) ^ {1 / 1. 0 8 4}\right) ^ {n} = (1. 2 9 1 (c / r). ^ {0 7 7 5}) ^ {n} \tag {3.1}
$$

The exponent n varies from 0.8 to 1.8, larger values usually giving better correlation [6]. Using $n = 1 . 8$ for that reason the $K _ { L }$ values obtained are found in Figure 3.1.

图片摘要：该图主要展示 3.1 Spanwise Corrigan stall delay parameter obtained for XV 。
![](images/c27bb49af15211c451354aa44c80e0330a0c3840196ea826637814aa458c662f.jpg)  
Figure 3.1 Spanwise Corrigan stall delay parameter obtained for XV-15 rotor model.

Although the largest effect of stall delay is seen near the root, the tip also shows significant stall delay using this model. For Corrigan stall delay the stall delayed lift coefficient is now obtained in Equation ( 3.2 ).

$$
c _ {l} = K _ {L} c _ {l, \text {t a b l e}} \text {f o r} \alpha <   3 0 ^ {\circ} \tag {3.2}
$$

The stall delay is applied from 0 degrees angle of attack until 30 degrees angle of attack. From 30 degrees to 60 degrees the model is washed out using the washout, w, as displayed in Equation ( 3.3 ).

$$
w = \left(\frac {6 0 - | \alpha |}{3 0}\right) \tag {3.3}
$$

The lift for an angle of attack between 30 and 60 degrees can now be derived as displayed in ( 3.4 ). Over the angles of attack until 60 the lift coefficient approaches the regular cl again. After 60 degrees no correction is applied anymore.

$$
c _ {l, \text {w a s h o u t}} = \left(w \left(K _ {L} - 1\right) + 1\right) c _ {l, \text {t a b l e}} \text {f o r} 3 0 ^ {\circ} <   \alpha <   6 0 ^ {\circ} \tag {3.4}
$$

The stall delay is only applied for positive section lift which is assumed to occur above an angle of attack of 0 degrees. It was found the zero lift angle of attack was close to, but not exactly equal to, zero and therefore small errors in the stall delay model might be introduced. These errors are however found to be negligible as the section lift within the angle of attack range from zero to zero-lift is very small. Comparison of the empirical model with experimental and theoretical data is presented in the original paper [32]. Section 4.5.2 discusses the results of the implementation of this model.

# 3.2.2 Tip Loss Model

Similar to aircraft wings, trailed vortex inflow over the tip of a rotor blade reduces its lifting capability. The RotCFD rotor model does not take this fully into account because it uses two-dimensional airfoil data and thus is likely to experience some section lift up to the blade tip. However, the flow field environment of RotCFD will alter the relative velocities experienced by the blade.

Leishman [36] describes an effective blade radius, or Prandtl tip loss factor, $B ,$ - usually around $9 8 \%$ of the blade radius – that is unaffected by tip loss, as shown in Equation ( 3.5 ). This means the effective blade radius, $R _ { e _ { I } }$ is a reduction of the actual blade radius, R, (in terms of lift coefficient) based on the tip loss factor, B. The lift at the remaining $2 \%$ of the blade is set to zero at the tip. Section 4.5.1 discusses the results of the implementation of the model.

$$
R _ {e} = R B \tag {3.5}
$$

# 3.2.3 C81 Airfoil Adjustment Code

The C81 data for the XV-15 airfoils vary almost linearly with radius, but the stall delay is non-linear, as shown in Figure 3.1. Because the stall delay is spanwise non-linear, the radial stations will have to be interpolated - even if the spanwise lift distribution is fairly linear. The airfoil data consists of the lift, drag and moment coefficients specified for a range of angles of attack and Mach numbers. A MATLAB code is written to perform a triple interpolation over angle of attack, Mach number and radial station. The interpolation over angle of attack and Mach number is necessary to make sure the radial interpolation can be properly evaluated. Once the angle of attack and Mach number matrix data is uniform for all three coefficients over the radial stations, the Corrigan stall delay model will be applied over a user-defined set of blade stations.

图片摘要：该图主要展示 3.2 shows a representative set of coefficients versus angle 。
![](images/7ca0490cc00055d0404e6548d4a2ee2159f81bd8db55afdab016082274fbb12d.jpg)  
Figure 3.2 shows a representative set of coefficients versus angle of attack or Mach number imported for the tip airfoil, the NACA 64-X08 (C81) airfoil data file. For the other airfoils representative plots have been placed in 0.

图片摘要：该图主要展示 3.2 shows a representative set of coefficients versus angle 。
![](images/5944e3a78c2563c0cfa10bb599d24beb4e7b65491602a258fc60a2a4515b8881.jpg)

图片摘要：该图主要展示 3.2 shows a representative set of coefficients versus angle 。
![](images/cdafc0abb0d370879ba22d82de6632a85d7288066c24a0e854129a9225d3e710.jpg)

图片摘要：该图主要展示 3.2 shows a representative set of coefficients versus angle 。
![](images/bac1c3ef6628d16806f94fbf4d06be6c515934bed7334c9321dfab1725ebc571.jpg)

图片摘要：该图主要展示 3.2 shows a representative set of coefficients versus angle 。
![](images/5afea498c727d3d27f19c58bb96619a8625c1d6e7e5d0b7ececd27354627c4ea.jpg)

图片摘要：该图主要展示 3.2 Angle of attack and Mach interpolation for representativ。
![](images/f85f7944e9cf36b3db68de8188b96765cec375f6529328663bc20075c27d98d3.jpg)  
Figure 3.2 Angle of attack and Mach interpolation for representative cases of the NACA 64-X08 airfoil.

For all airfoil files the angle of attack data is very well organized, showing high density of data points around the crucial areas. The Mach number data points are, however, less numerous. Especially for the root airfoils since they experience a lower relative Mach number.

The green lines in the graph show the interpolation made by the code. Because of the numerous data points for the angle of attack the interpolation is done using a Piecewise Cubic Hermite Interpolating Polynomial (PCHIP) interpolation. This method was found to give the most ‘natural’ interpolation of rather unpredictable behavior of the curves. This method was not found to be working well for the interpolation of Mach number data points, here the PCHIP method could be unpredictable if one data point showed an abrupt deviation of the trend, as for example the case in Figure 3.2d. Therefore the Mach number interpolation is done using a simpler linear interpolation. The following radial interpolation has also been done linearly. The interpolated lift curve is colored green in Figure 3.2. Figure 3.2a shows a clear stall region, albeit at a higher angle of attack than usually the case for aircraft wings, attributable to the relatively thick blades. This also manifests in the relatively gradual stall observed. The drop of the lift coefficient in Figure 3.2d shows the compressibility effects becoming troublesome. The spike in drag in Figure 3.2e and the drop in moment coefficient in Figure 3.2f show the results of the corresponding drag divergence, respectively. The stall delay and tip loss models only affect the lift coefficients and they will therefore be the focus variable in the remainder of the section. Figure 3.3 shows a simplified flowchart of the whole code for the airfoil adjustment, including the import, the interpolation along angle of attack, Mach number and radial stations, the stall delay and tip loss model implementation and the re-exporting to C81 format.

# The following steps are covered in the code:

1. Start;   
2. Import of C81 airfoil data files and verification of the radial position of the airfoils;   
3. The C81 files are decomposed into matrices for easy manipulation;   
4. The angle of attack is interpolated using PCHIP-interpolation for all coefficients;   
5. The Mach number is linearly interpolated for all coefficients;   
6. The radial stations are interpolated for all coefficients;   
7. Application of stall delay, if selected in program;   
8. Application of tip loss factor, if selected in program;   
9. Conversion of matrices to C81 format and export to *.c81 files;   
10. End.

图片摘要：该图主要展示 3.3 Simplified flowchart of airfoil adjustment code。
![](images/f09c502d181166b1bb8f2648cb408deeaf53422a12dd2252b93cbaa3b1dc38d0.jpg)  
Figure 3.3 Simplified flowchart of airfoil adjustment code.

图片摘要：该图主要展示 3.3 Simplified flowchart of airfoil adjustment code。
![](images/1cde1705af82cdde7f202d4efb74e483bc1d2cdd65bf2491387b0838361cbbab.jpg)  
Figure 3.4 shows the spanwise lift coefficient of the original data, the data after angle of attack interpolation and Mach interpolation and the data after radial interpolation. The lift coefficient will mostly be discussed because both the stall delay and tip loss model only affect the lift coefficient. Note that the vectors specifying the remapping of the angle of attack, Mach number and radial stations are user specified. The plot is shown for a Mach number of $M = 0 . 3 0$ for continuous zero twist. Therefore these are not the actual lift coefficients the blade would exhibit because it is exhibits substantial twist as shown in Figure 2.17.   
Figure 3.4 Radial interpolation check of lift coefficient at $M = 0 . 3 0$ .

The results of the stall delay both for angle of attack and Mach number for various representative radial stations are shown in Figure 3.5. The effects of the model are clearly observed. Figure 3.5f is evaluated for a negative angle of attack, where no stall delay should be present. This is confirmed by the identical curves before and after model application.

图片摘要：该图主要展示 3.4 Radial interpolation check of lift coefficient at。
![](images/15cbf7b2d2f4d20c4fb80f2085c3471ae49bfe879822e38b76195f95a22c66c3.jpg)

图片摘要：该图主要展示 3.4 Radial interpolation check of lift coefficient at。
![](images/730f2eca2895fb76d9ae1169dc463eaede41c36c812c466ee98b89187357d972.jpg)

图片摘要：该图主要展示 3.4 Radial interpolation check of lift coefficient at。
![](images/8218af769de09d6e859c9dd38da1dee258d420c3b65920d771c2726b6759a79b.jpg)

图片摘要：该图片与Figure 3.5 Stall delay influence as function of angle of attack or Mach number f这部分内容相关。
![](images/cb16a471e7d2454325d52155f1973d695e001f0f82bf43e1ad515995d762a345.jpg)

图片摘要：该图主要展示 3.5 Stall delay influence as function of angle of attack or 。
![](images/e2fce8efe55760e13dc4f8818269fcbe5528d683debe1954b64d1d2994ed3aa0.jpg)

图片摘要：该图主要展示 3.5 Stall delay influence as function of angle of attack or 。
![](images/b313b0deb3c7631c2b8262228e1692efe219a0a11c5e7bd75bfd88058b9dc720.jpg)  
Figure 3.5 Stall delay influence as function of angle of attack or Mach number for various radial stations.

More representative plots are presented in 0.

Tip loss is applied at $r / R = 9 8 \%$ by setting the lift coefficient to zero after $r / R = 9 8 \%$ . This drop occurs instantaneous [37] and is programmed to happen between $r / R = ~ . 9 8$ and $r / R =$ .981. The final result before stall delay and tip loss compared to the unaltered interpolated data is shown in Figure 3.6. This plot shown for zero continuous twist at $M = 0 . 3 0$ and clearly shows the implication on lift coefficient of the application of both models.

图片摘要：该图主要展示 3.5 Stall delay influence as function of angle of attack or 。
![](images/57298973c28471312f7ff36a74332003a8a432da27a04e7e1e746bc9d2f7c2ad.jpg)  
Figure 3.6 Lift coefficient as function of radial station at $M = 0 . 3 0$ at continuous zero pitch angle.

The models will be tested independently during the validation of the rotor model in RotCFD.

# 3.3 General Setup of Validation Cases

The setup of the boundaries and gridding of the flow field is kept consistent through the validation cases. The boundaries consist of a rectangular prism with x,y,z-dimensions of 10D, 10D, 15D, respectively, with D being the rotor diameter. The rotor is placed in the center of the XY-plane and 5D in negative z-direction from the top plane. Note that positive z is aligned with thrust. This is done to eliminate any influence from the ground plane. The cell count is roughly between one and two million cells, depending on the case. The RotCFD user interface is shown in Figure 3.7 for a hover case; two side views of the applied gridding are shown in Figure 3.8 and Figure 3.9.

图片摘要：该图主要展示 3.6 Lift coefficient as function of radial station at at con。
![](images/752d2e8a17a01248be5fd8fa945d27e7b62f9aefd869a1a55500bca62a33e732.jpg)  
Figure 3.7 RotCFD user interface with a hover case loaded.

# 3.3.1 Boundary Settings

For a hover case all boundaries are pressure boundaries except for the plane in wake direction that is set to a mass outflow boundary correction. Cases where a free stream velocity is present have according velocity boundary corrections and a mass outflow boundary in the direction of the wake.

图片摘要：该图主要展示 3.7 RotCFD user interface with a hover case loaded。
![](images/d6bfda0ca44862abbcd08d4c96b8a2ba5bc7d15e5e6517219168c448dff2823f.jpg)  
Figure 3.8 Hover case, gridded centered side view (XZ) of the flowfield.

图片摘要：该图主要展示 3.8 Hover case, gridded centered side view (XZ) of the flowf。
![](images/268f00fbd28f68d5828a97ff6a7c4026fcbdde84eefae66f606dd848f9f67130.jpg)  
Figure 3.9 Hover case, gridded top view (XY) at rotor height.

# 3.3.2 Spatial and Temporal Resolution Independency

For all flight modes spatial and temporal resolution independency was checked by observing the performance parameters power, thrust and figure of merit to be independent of the chosen cell size and time step. A refinement box was used to confine the rotor in order to improve the result for the smallest cell count. The smallest cell size, found at the rotor disk itself, was found to be equivalent to roughly 8 [cm] whereas the time step for the validation with the steady model was set at 1/400 [s] and the time step for the unsteady model ranged between 1/800 [s] and 1/1200 [s]. For the unsteady model this corresponds to approximately 3 degrees of rotor rotation per time step.

# 3.4 NFAC Wind Tunnel Cases Setup

After the validation the interference in wind tunnels is examined for both wind tunnels of the National Full-Scale Aerodynamics Complex (NFAC) at NASA Ames Research Center. The two wind tunnels that comprise the NFAC facility share portions of their flow path. The cross section of the 80- by 120-Foot Wind Tunnel is an open circuit wind tunnel with a closed, rectangular test section. The 40- by 80-Foot Wind Tunnel is a closed section wind tunnel with an oval test section. For this research it is assumed the operating conditions are all fixed and at sealevel.

The k-ε turbulence model is primarily known for circulation in large areas, a wall function is added for more accurate velocity profiles near no-slip conditions at walls or other surfaces. No effort has been made to investigate the effect of chosen turbulence model versus a laminar approach or other turbulence models.

Only the test section will be modeled with constant cross sectional area. In real life the test section of the open circuit 80- by 120-Foot Wind Tunnel will always experience the influence from the turbulence from outside, the vane sets and the developed boundary layer and the flow therefore will therefore not be uniform. Similarly the test section of the closed section 40- by 80-Foot Wind Tunnel is likely to, despite the air exchange system, contain non-uniform flow because of ‘old’ disturbed air from the model. Disturbances can also occur at the test section inflow because of turbulent air from the tunnel walls, vane sets etc. To reduce the complexity of this research the inflow conditions are however chosen to be uniform at the test section inlet.

The length of the test sections has been increased from their real value to eliminate influence on the rotor performance due to the imposed boundary conditions at the inlet and outlet. The test section elongation for both test sections in sketched in Figure 3.11, with the positive x-direction corresponding to the wind tunnel flow direction. For this research both test sections of the NFAC are therefore modeled as an open tunnel with closed test section. The pressure was found not to be disturbed around 2 to 3 rotor diameters distance from the inlet to the TTR. A render of the TTR in the 40- by 80-Foot Wind Tunnel test section during airplane mode and edgewise flight is shown in Figure 3.10. Note that this is the only direction the TTR can be rotated.

图片摘要：该图主要展示 3.10 TTR in 40 by 80 Cross section shifting from airplane ) 。
![](images/67ae1fd76dc727842b02c33596aa2f4b1d07c10eb2493707f9b8c2aa61022c2c.jpg)  
Figure 3.10 TTR in 40- by 80-Cross section shifting from airplane $( a _ { p } = 0 ^ { \circ }$ ) mode to edgewise flight $( a _ { p } = 9 0 ^ { \circ } )$ ) . 7

Small features such as pressure tabs, small ramps or the faceting of the acoustic lining are assumed to have negligible influence on the results of this study and will not be modeled. The slight faceting on the 40- by 80-Foot Wind Tunnel will be ignored and the cross section is thus assumed to have semicircular walls.

The XV-15 will be mounted on the Tiltrotor Test Rig (TTR). In 2016 the TTR will be tested in the NFAC facility with the Bell 609 rotor. Rotor forces will be measured on a dedicated balance installed within the TTR, instead of using the wind tunnel balance system; therefore the rotor performance from the rotor program in RotCFD can be used as the target variable. The wind tunnel turntable can rotate the TTR from axial $\textstyle ( a _ { p } = 0$ degrees) to edgewise flight $( a _ { p } = 9 0$ degrees) and all angles in between. Note that in edgewise flight the thrust will always be aligned with the positive y-axis and in airplane mode the thrust will always be aligned with the negative x-axis.

图片摘要：该图主要展示 3.10 TTR in 40 by 80 Cross section shifting from airplane ) 。
![](images/56d88b6af48970fe58e1e62218d056a62b7f8a3966a3563584aabd838c09b58b.jpg)

图片摘要：该图主要展示 3.10 TTR in 40 by 80 Cross section shifting from airplane ) 。
![](images/bd621e46d3b038c488bdff31be1c660d6d38ca08264e600d7224b299039c12b4.jpg)  
Figure 3.11 The boundaries of the extended test sections with TTR in edgewise and axial mode, respectively.

The thrust is manually trimmed using the collective setting to make sure values are similar to the validations results and the rotor is not evaluated far into the stall regime.

RotUNS features a tetrahedral body-fitted grid with a Cartesian unstructured grid in the far field. RotUNS does not support viscous body-fitted grids and therefore will not accurately capture the boundary layer around geometry in the domain. The thickness of the boundary layers is found in Table A.1 and Table A.2 for the 40-by 80-Foot Wind Tunnel and the 80-by 120- Foot Wind Tunnel, but to reduce complexity it has not been tried to implement the effects of the actual tunnel wall boundary layer on the simulation. The choice for RotUNS was made because of the developmental stage of the RotVIS module at the time of writing and the experience that RotUNS should be mastered before attempting the use of RotVIS. Because the prime variable is rotor performance, not measured by forces on the body (i.e. TTR and/or struts), it is assumed the forces are of less importance to the predictions once performance convergence is guaranteed.

A mass outflow condition is used at the end of the test section if positive wind tunnel speed is modeled. For hover cases a pressure boundary condition is applied to the inlet and outlet. The physical size of the grid relative to the rotor and in the region of the wake is kept identical to the validation cases. The time grid is kept equal to the one used in the validation cases, sometimes refined to keep stability at the tetrahedral body-fitted cells. Figure 3.12 shows two representative planes (XZ-plane or side view and YZ-plane or front view) of a fitted grid in both test sections. Note that the first (side) view is an extended test section to ensure uniform inflow due to the imposed boundary condition doesn’t alter rotor performance. Lower grid density at the inlet is used to reduce cell count while the refinement at the walls is maintained, however, to keep an identical stream tube when the no slip condition at the walls results in velocity gradients over the adjacent cells. The total cell count for both test sections is between 900,000 and 1,200,000 cells.

图片摘要：该图主要展示 3.11 The boundaries of the extended test sections with TTR i。
![](images/4bf295aff6115b21da74b1a5cd9fa37ac22cc61a587c024f4a788f721ae7f419.jpg)  
80- by 120-Foot Wind Tunnel

40- by 80-Foot Wind Tunnel

Figure 3.12 The extended test sections with TTR on struts and XV-15 rotor in edgewise and axial mode, respectively.   
图片摘要：该图主要展示 3.12 The extended test sections with TTR on struts and XV 15。
![](images/bd6d4f8e387ded36f9df1140f0285e12d869f7b25462166cc09e028d5cb3dc5f.jpg)  
(extended) test section length: 62.94 [m]

test section width: 24.38 [m]

For each case evaluated there is a set of four tests consisting of the wind tunnel test section with geometry of the TTR and struts (WTGE) and without geometry of the TTR and struts (WTRO). Its free field counterpart without tunnel geometry but with (FFGE) and without the TTR and strut geometry (FFRO) is also modeled for direct comparison of rotor performance. The subsets for each case are summarized in Table 3.2.

Table 3.2 Overview of four different subsets per case.   

<table><tr><td>Case</td><td>Windtunnel</td><td>Free Field</td><td>Rotor</td><td>TTR Geometry</td></tr><tr><td>WTGE</td><td>×</td><td></td><td>×</td><td>×</td></tr><tr><td>WTRO</td><td>×</td><td></td><td>×</td><td></td></tr><tr><td>FFGE</td><td></td><td>×</td><td>×</td><td>×</td></tr><tr><td>FFRO</td><td></td><td>×</td><td>×</td><td></td></tr></table>

Rotor convergence is case dependent but occurs usually after the equivalent of around 10-15 rotor rotations and remains steady after that because the wake is out the influencing zone of rotor performance. This is observed visually by plotting the velocity and making sure the wake has progressed at least 1-2 rotor diameters from the rotor disk. Care must be taken that the rotor is effectively placed in a box (and not just in ground effect), which complicates the analysis. In some cases the wake might not have fully settled over the remainder of the geometry and thus force convergence on the TTR might not have occurred yet while rotor convergence is found.

No automatic rotor trim is available yet in RotCFD at the time of writing. This means the thrust cannot be automatically maintained constant for each case. Instead the collective is fixed throughout the subsets.

# 3.4.1 NFAC 80-by 120-Foot Wind Tunnel Cases

The test section of the 80- by 120-Foot Wind Tunnel is expected to show little or no interference effect at all, or only under the most unfavorable conditions. Therefore axial flow at $V = 1 0 0$ [kts], the highest wind tunnel velocity, and edgewise at $V =$ 0 [kts] (hover) are the prime test cases. Hover will normally always be measured in axial mode for the least obstruction to the inflow and outflow of the rotor. However, the edgewise hover test is still evaluated to show the theoretical worst-case interference. An increase in tunnel velocity in edgewise mode should decrease the interference with the tunnel walls. Therefore the last case is an edgewise case at low tunnel velocity $V = 1 0$ [kts], expected to show smaller interference because of the higher tunnel velocity. Table 3.3 shows the three final cases for the 80-by 120-Foot Wind Tunnel test section.

Table 3.3 Final 80- by 120-Foot Wind Tunnel Cases   

<table><tr><td>Case</td><td>80- by 120-Foot Wind Tunnel</td><td>V [kts]</td><td>αp [deg]</td><td>θo [deg]</td><td>Mtip [~]</td><td>Airfoil Correction</td></tr><tr><td>1</td><td>edgewise</td><td>0</td><td>90</td><td>4.00</td><td>0.66</td><td>TL, SD</td></tr><tr><td>2</td><td>edgewise</td><td>10</td><td>90</td><td>4.00</td><td>0.66</td><td>TL, SD</td></tr><tr><td>3</td><td>axial</td><td>100</td><td>0</td><td>14.80</td><td>0.53</td><td>TL</td></tr></table>

Case 1, with an ‘edgewise’ hovering rotor, utilizes a pressure boundary condition at the in and outlet. Using the free field as a reference it is made sure the imposed pressure boundary is not altering the pressure changes altered by the rotor disk. Case 1 and 2 use collective settings equal to those used in the validation of the hover performance. Case 3 uses a collective setting roughly equivalent to low thrust, as would be expected for cruise, of around $T \approx 3 0 0 0$ [N]. The WTGE cases for case 3, and case 1 and 2 are shown in Figure 3.13 and Figure 3.14, respectively. The wind tunnel velocity is aligned with the positive x-axis.

图片摘要：该图主要展示 3.3 Final 80 by 120 Foot Wind Tunnel Cases。
![](images/41dce537feca30d80471eca32ae6c288942bc5883efe877b074b51e93b6465a6.jpg)  
Figure 3.13 The setup of case 3, WTGE.

图片摘要：该图主要展示 3.13 The setup of case 3, WTGE。
![](images/7f5d37c6099a3a4aa738c17207efacd00219a6f7ce01ccec8dd94c9a63f8bfe2.jpg)  
Figure 3.14 The setup for case 1 and 2, WTGE.

# 3.4.2 NFAC 40-by 80-Foot Wind Tunnel Cases

The 40- by 80-Foot Wind Tunnel is likely to show interference under a larger set of conditions and will therefore be investigated in greater detail. Figure 3.15 shows the conversion corridor of the XV-15, which indicates the realistic operating conditions for the XV-15 rotor. This is checked to make sure no excessive stall or rotor mode simulation is asked for.

图片摘要：该图主要展示 3.14 The setup for case 1 and 2, WTGE。
![](images/9130ffccb13a58658d6910d5a2fe453a57d47096fdc4069770788b012436f063.jpg)  
Figure 3.15 Conversion corridor of the XV-15 [5].

For edgewise mode a similar case to the 80-by 120-Foot Wind Tunnel is investigated at $V = 1 0$ [kts] as well as a high velocity, $V = 1 0 0$ [kts], case. Figure 3.16 shows the height-velocity envelope of the XV-15.

图片摘要：该图主要展示 3.15 Conversion corridor of the XV 15 [5]。
![](images/fd3d35c36dc6704f99b8916ff2227e4bb4023889a9a112da17138aaa2e56e2af.jpg)  
Figure 3.16 XV-15 height-velocity envelope [5].

It shows that the torque limit sets the cruise velocity at sea level at around $V _ { t a s } = 2 5 0$ [kts]. The 40- by 80-Foot Wind Tunnel can run in excess of $V = 3 0 0$ [kts] but the incompressible solver will be limited to $\mathsf { M a c h } = 0 . 3 \ [ \sim ]$ to avoid compressibility effects [33]. Therefore the axial mode at high speed is considered at $V = 2 0 0$ [kts]. The FFGE setup of cases 4 and 5 is pictured in Figure 3.17. The WTGE up for case 6 and the WTRO setup for case 7 is sketched in Figure 3.18 and Figure 3.19. Positive wind tunnel velocity is always aligned with the positive x-axis.

图片摘要：该图主要展示 3.16 XV 15 height velocity envelope [5]。
![](images/265335b435c24d64e9e750cb55cbe0b8723e4fda3ac46ba08b9fa3f353bbb7bb.jpg)  
Figure 3.17 The geometry for case 4 and 5, FFGE.

Finally a tilted case with $a _ { p } = 6 0$ degrees is used to check the influence of the rotor disk advancing closer to the curved test section wall at $V = 1 0 0$ [kts]. The WTGE subsets of the edgewise and tilt mode are shown in Figure 3.18 and Figure 3.19, respectively. The final cases are summarized in Table 3.4.

图片摘要：该图主要展示 3.17 The geometry for case 4 and 5, FFGE。
![](images/a8ca24933183dca0cacfc6f23b20a63e3ca8b23ae74e9a679e966752d8ada29e.jpg)  
Figure 3.18 The geometry and grid for case 6, WTGE.

图片摘要：该图主要展示 3.18 The geometry and grid for case 6, WTGE。
![](images/cacfa369c23651a86b2c45738144ada91702c13ab13097cdc2f5f05d51bbe9f1.jpg)  
Figure 3.19 The geometry for case 7, WTRO.

Table 3.4 Final 40- by 80-Foot Wind Tunnel Cases   

<table><tr><td>Case</td><td>80- by 120-Foot Wind Tunnel</td><td>V [kts]</td><td>αp [deg]</td><td>θo [deg]</td><td>Mtip [~]</td><td>Airfoil Correction</td></tr><tr><td>4</td><td>edgewise</td><td>10</td><td>90</td><td>4.00</td><td>0.66</td><td>TL</td></tr><tr><td>5</td><td>edgewise</td><td>100</td><td>90</td><td>1.00</td><td>0.66</td><td>TL</td></tr><tr><td>6</td><td>axial</td><td>200</td><td>0</td><td>32.68</td><td>0.53</td><td>TL</td></tr><tr><td>7</td><td>tilt</td><td>100</td><td>60</td><td>8.00</td><td>0.65</td><td>TL</td></tr></table>

# 4 Validation of XV-15 Rotor Model

From RotCFD the thrust, power and figure of merit are obtained. The figure of merit is extracted directly from RotCFD. The full data table for the steady results is included in Appendix C. All plots for the unsteady model and full data table are included in 0.

# 4.1 Hover

The hover performance comparison for the unsteady model in terms of the power curve is shown in Figure 4.1. It shows serious deviation in excess of $1 0 \%$ from the reference data. The orange symbols show efforts in which several parameters were changed in an effort to find the cause of the bad correlation. In case E1 the grid count was increased from 1.3E6 to 4.0E6 cells. In case E2 a spinner body was included, to check if the missing hub geometry showed a large influence because of root losses. Cases E3 and E4 had a significantly increased amount of iterations per time step and a lower relaxation factor, respectively.

图片摘要：该图主要展示 4.1 Unsteady results for XV 15 rotor hover power as a functi。
![](images/ff3b408a62cd8068ef156fdb1e435018a0cff7e04efb50dbe1ea32e63a590312.jpg)  
Figure 4.1 Unsteady results for XV-15 rotor hover power as a function of thrust [2], [28].

图片摘要：该图主要展示 4.1 Unsteady results for XV 15 rotor hover power as a functi。
![](images/076c7a2279fd510e0ab462b4ca3088845d72f7acea89f40407b8a2f791c5054e.jpg)  
Figure 4.2 shows the same data points but expressed in terms of figure of merit.   
Figure 4.2 Unsteady results for XV-15 rotor hover figure of Merit as a function of thrust [2], [28].

The unsteady model again shows serious deviation from the reference data, generally around $1 0 { - } 2 0 \%$ . This error is very large and doesn’t justify the use of the unsteady model.

图片摘要：该图主要展示 4.2 Unsteady results for XV 15 rotor hover figure of Merit a。
![](images/8d0e32542a38d95c381b6624454fca38959f881bc0e9ba6067731a15a9f2790c.jpg)  
Figure 4.3 shows the results for XV-15 hover performance with the steady model. The correlation is generally good, although the tip loss (TL) model deviates from the reference data. The tip loss and stall delay model combined (TL SD) and the stall delay model (SD) both show very good correlation to both the OARF data and CAMRAD II curve.   
Figure 4.3 Steady results for XV-15 rotor hover power as a function of thrust [2], [6], [28].

Figure 4.4 shows the same data points for figure of merit. In this plot it is clear the stall delay only model has the best correlation with the OARF data points. Assuming the OARF data points are the most accurate dataset, the estimation of highest figure of merit is done most accurate using RotCFD. For the chosen tip speed not more OARF data points are available, but CAMRAD II shows serious stall effects as the curve steeply drops towards the higher thrust values. The stall delay only model clearly doesn’t show a similar severe drop in performance towards the higher thrusts.

图片摘要：该图主要展示 4.4 shows the same data points for figure of merit. In this 。
![](images/c03073a6337555abb31eb4d9a0847e09c79320b4e150a5c60044347d448c2a1e.jpg)  
Figure 4.4 Steady results for XV-15 rotor hover figure of Merit as a function of thrust [2], [6], [28].

The steady model, in contrast to unsteady model, shows a fairly good correlation with the reference data and has therefore been chosen as the model for the wind tunnel simulations. The thrust and power as function of collective, for both the steady and unsteady model, are shown in Figure 4.5 and Figure 4.6, respectively, in an effort to find the source of the deviation of the unsteady model. It clearly shows the deviation in performance between both models, but no tested explanation has been found yet.

图片摘要：该图主要展示 4.4 Steady results for XV 15 rotor hover figure of Merit as 。
![](images/fee0ea88fffad58c3f2096b282df0a6ab4ed29eeb5b085932cc1c63482e84f6c.jpg)  
Figure 4.5 Rotor thrust as function of collective pitch angle.

图片摘要：该图主要展示 4.5 Rotor thrust as function of collective pitch angle。
![](images/506b5158a13339c993e0dc0f1913e6df2cc96ce935f4b27d7d0a04b1f832c9d3.jpg)  
Figure 4.6 Rotor power as function of collective pitch angle.

Further work could include azimuthal check of lift, angle of attack and rotor conditions, to find out why the power is so much higher using the unsteady model. The lower figure of merit suggest a lower efficiency and thus more stall over the blade.

# 4.2 Tilt Mode

The evaluation of different pylon angles in tilt mode using the steady model is quite successful. No stall delay is applied on models except for hovering rotors. Figure 4.7 shows good correlation for all pylon angles up to $\alpha _ { p } = 7 5$ degrees. Noticeable is the difference with CAMRAD I results. The influence of tip loss factor is shown to be minimal.

图片摘要：该图主要展示 4.6 Rotor power as function of collective pitch angle。
![](images/9dc57e9ab0189aa60cc26d43490c408ce5cdc286a4ce315a2f7cd39726afd44b.jpg)  
Figure 4.7 Steady results for XV-15 rotor power as a function of thrust for various pylon angles at V/ΩR = .32 [2].

图片摘要：该图主要展示 4.7 Steady results for XV 15 rotor power as a function of th。
![](images/11319792438b37b6c21b0964129640cb1dd7b00ceb4d46c0ffc4f5c62851b106.jpg)  
Figure 4.8 shows the sensitivity to aspect ratio changes. The rotor model seems to perform well even up to the most severe aspect ratio tested. The influence of tip loss factor is shown to be minimal.   
Figure 4.8 Steady results for XV-15 rotor power as function of thrust, for $a _ { p } = 7 5 ^ { \circ }$ [2].

Because the relatively low thrust and high aspect ratios the induced velocities at the tip are relatively smaller, therefore showing almost no influence of the tip loss factor, in strong contrast to the hover cases. Because the difference is so small the computational budget is chosen to be saved and not all cases are simulated for both models.

# 4.3 Airplane Mode

The final validation case is for two different tip speeds in axial, or airplane, mode. Correlation is very promising compared to the CAMRAD I curves.

图片摘要：该图主要展示 4.8 Steady results for XV 15 rotor power as function of thru。
![](images/6983224a5437d7a745eca3994dda9240ae21c974d603940e30fe9e92e1a5cefb.jpg)  
Figure 4.9 Steady results for (rotor) propulsive efficiency as function of thrust [2].

# 4.4 Ground Effect Study by Je Won Hong

Je Won Hong from the University of Illinois at Urbana-Champaign offered his help during his internship at NASA Ames Research Center. He investigated, under guidance of the author, the XV-15 rotor, identical to the one used throughout this research, in ground effect. For this study he used the ideal power as this was the case for the theoretical reference models presented in literature [3]. Hong’s work [38] shows that RotCFD shows expected behavior of rotors operating in ground effect as shown in Figure 4.10.

图片摘要：该图主要展示 4.9 Steady results for (rotor) propulsive efficiency as func。
![](images/7d1fffbcf3275fce1bb5997c7741e70df94c9d6909ce00c06274fb8c05801fa5.jpg)  
Figure 4.10 Evaluation of the XV-15 rotor in ground effect in RotCFD [38].

# 4.5 Discussion on Airfoil Data Correction

The original, tip loss model and stall delay model and their combinations have been examined in the present validation. The sections below include a discussion on the validity of the models and the obtained results.

# 4.5.1 Tip Loss Factor

It is likely that some of the three-dimensional effects of the tip (or root) of the rotor will be accounted for. Since the ‘conventional’ tip loss model is applied, it would be expected the model overcompensates. As can be seen for both the steady and unsteady results the tip loss factor has a rather detrimental effect on figure of merit and power curve during hover. Especially the figure of merit plots in Figure 4.2 and Figure 4.4 clearly show this influence. The tip loss influence is considerably less during lower thrust modes, for example during airplane mode.

There are a couple of factors that influence the tip loss; first of all the three-dimensionality of the blade tip aerodynamics or the induced velocity due to trailing vortices. Secondly because of the finiteness of the blade there is a pressure equalizing effect between the surfaces of the blade or rotor disk.

The first mentioned reason is mostly present only in the unsteady model, whereas the second reason is applicable to both models. A further investigation of the tip loss model could yield better results. The main problem in RotCFD is thought to be the accurate computation of the angle of attack near the root or hub and its spanwise variation. Figure 4.11 shows a sketch for a typical observed difference in blade loading during hover between a traditional BEM, RotCFD and an actual blade loading.

图片摘要：该图主要展示 4.11 Sketch of blade loading characteristics。
![](images/c6c96f80b4c303d04f8cb448cd1561eb0c23f85505968cc9c8b2a1511341ec61.jpg)  
Figure 4.11 Sketch of blade loading characteristics.

# 4.5.2 Stall Delay Factor

The stall delay factor is applied because of radial flow of the boundary layer that delays the onset of stall on the blade, particularly near the root of the blade. Since the rotor model described in Section 2.2.4 only accounts for normal and tangential source components, the radial direction is not taken into account. It would furthermore be very difficult, if not impossible, to create a similar system to also include radial boundary layers, because they would not be oriented in the direction of the main flow, and over relatively large lengths (the blade span) and therefore highly unpredictable.

The Corrigan and Schillings stall delay model used is only valid for hover, for which is shows very good agreement with experimental and theoretical data. Although methods for (partial) stall delay in other flight modes exist, they are not pursued during this research.

# 4.6 Accuracy and Precision

An important factor in any simulation is the error observed. If there is a dataset that can be considered a benchmark the error can be calculated – this is, however, easier said than done.

First of all, each data point represents a collective angle with a combined thrust and power variable. In past research, however, this collective angle has usually been neglected because to date no program is able to match collective setting with thrust and power accurately [6]. It can, however, produce an accurate data point on the power-thrust curve, despite a mismatch in collective angle.

Without a way to directly compare data points, another possible way is to compare the RotCFD data points with a curve through the reference data. Nor RotCFD, nor the reference data, however, tend to have enough data points to justify a curve fit. The curve fit would also be subjective because no fitting technique is defined, or known. Another problem is that there is no way to know if the power, thrust or what combination of both generated the errors observed.

The RotCFD data for the unsteady model shows good precision in general; any deviation from the reference data seems constant over the modeled thrust range. To get a first indication of the errors involved a very basic analysis has been performed. Figure 4.3 is repeated below in Figure 4.12, however, only including the RotCFD steady SD data points and the OARF data set. A second order polynomial fit has been added to the OARF data points.

图片摘要：该图主要展示 4.12 2nd order polynomial fit through the OARF data。
![](images/e279aaf9d39b849810398fd5038ec1e31e42ce153fec4a7576a329601d4b5a6f.jpg)  
Figure 4.12 2nd order polynomial fit through the OARF data.

By taking a representative thrust location on the curve and individually checking the error in power and the error in thrust, percentage errors can be obtained that serve as an indication of accuracy. These offsets where found to be around $3 \%$ for hover, $5 \%$ for tilt and $5 \%$ for airplane mode. The maximum figure of merit was $0 . 6 \%$ off from the value listed in the OARF data, which is exceptionally high, even for full NS codes, and is partially thought to be coincidentally this accurate.

Of higher importance could be considered not the accuracy, but the precision. The precision is a measure of the consistency of the results and is associated with random errors. For the wind tunnel cases performance differences are obtained by finding the difference between two cases. This means the precision might be more important than the accuracy. The precision is, however, for the same reasons mentioned above, not obtainable without introducing new unknown errors into the data. The precision in the most important flight modes, hover, tilt and airplane mode, see Figure 4.3, Figure 4.7 and Figure 4.9, respectively is believed to be very good, as the data almost stays a consistent distance from the reference data.

# 4.7 Residual Values

Most simulations for either hover, tilt or airplane mode show very similar characteristics in terms of residuals. Figure 4.13 shows the moving average (MA) for the residuals of the main flow variables for a tilting isolated rotor at 15 degrees pylon angle, as shown in Figure 4.7. The length scale for the sampling of the moving average is the time-equivalent of one rotor rotation. The grey backgrounds show the original variation of the variables, while the colored lines show the moving average. This is done in order to not obfuscate all the overlapping values. The logarithm on the y-axis has base 10.

图片摘要：该图主要展示 4.13 Residual plot for a tilting isolated rotor at 15 degree。
![](images/7a8b16e5cf2b9a919db4e8c92930fa4767922e04635111cffe4ae949a1794891.jpg)  
Figure 4.13 Residual plot for a tilting isolated rotor at 15 degrees pylon angle.

It can be observed that momentum in all three directions shows the largest residual, or cumulative error over all the cells, of around $1 0 ^ { \circ }$ . From this number the location of highest errors in the flow field can unfortunately not be determined. The noticeable kink in the residuals slightly before time step 1000 is due to the wake of the rotor hitting the mass outflow boundary plane 10 rotor diameters downstream. Residuals can be seen to vary greatly with rotor wake development.

Since the validation shows promising results it is concluded that the magnitude of the residuals, although relatively large sometimes, are not enough to offset the required accuracy for the rotor performance simulations. Increasing the iterations per time step or reducing the delta time will reduce the residuals, but no effect on rotor performance is observed. The residual overviews for hover, tilt at a 75 degree pylon angle and airplane mode are presented in Appendix C.2.

# 4.8 Performance Convergence

Performance convergence is found to be relatively robust. The thrust tends to converge rapidly, around the equivalent of 5 rotor rotations, while the power tends to take a little longer. Usually around 10-15 rotor rotations the performance parameters, power and thrust for this research, have fully converged. To measure convergence a code has been written that plots the difference in performance compared to the final answer versus time steps; from this plot the percentage error can be determined which is used as indicator for convergence. If the difference is less than $. 2 5 \%$ to $1 \%$ for a sustained amount of time, the solution is set to be converged. This amount of time is usually up to half of the simulated time. RotCFD has no internal convergence monitoring. 1500 time steps roughly corresponds to 2 seconds of simulated time, or the equivalent of 20 rotor rotations.

Three performance convergence graphs are shown in Figure 4.14, Figure 4.15 and Figure 4.16, for hover, tilt and airplane mode, respectively.

图片摘要：该图主要展示 4.14 Hover performance convergence over time。
![](images/52f68fcb01e0c377936d4dfc38eaa3e41d09c5cddb7b755dbbb7a428a4ab5883.jpg)  
Figure 4.14 Hover performance convergence over time.

图片摘要：该图主要展示 4.14 Hover performance convergence over time。
![](images/a77d85dea38945ec27f615f1ab45897630ce3529f6f54750528b8f0785f1777c.jpg)  
Figure 4.15 Tilt mode (15 degree pylon angle) convergence over time.

图片摘要：该图主要展示 4.15 Tilt mode (15 degree pylon angle) convergence over time。
![](images/8578fef77bd211052064a88067bad14dc83553b0cb60841506136919b518c3a0.jpg)  
Figure 4.16 Airplane mode convergence over time.

# 5 Results

The wind tunnel cases required a substantial amount of time to run, varying from 2 – 6 weeks, depending on the required time difference between time steps for stability and convergence behavior of the case. Figure 5.1 shows a set of Apple iMacs used uninterrupted for the various subsets for about 2 – 3 months on end.

图片摘要：该图主要展示 4.16 Airplane mode convergence over time。
![](images/6bdf3ee0611e7cc860a595af4f38bdcfe3150dd25f44d437307498d6d5df7ce8.jpg)  
Figure 5.1 Various computers used for months on end to compute each of the cases within the timeframe.

# 5.1 NFAC 80-by 120-Foot Wind Tunnel Results

The results for the rotor only cases and geometry cases for both free field and wind tunnel simulations are summarized in Table 5.1 and Table 5.2, respectively. The last column in both tables shows a top view (XY-plane) sketch of the wind tunnel configurations of the subset WTRO of each case. For the rotor only cases (FFRO, WTRO) the free field case (FFRO) is chosen as benchmark as this is the ideal testing ground. Similarly, the free field analogy with geometry (FFGE) is chosen as the benchmark in the geometry cases; FFGE and WTGE. Thus, the changes in power and thrust are expressed as relative percentage change compared to their free field counterpart. The computation of the change in power and change in thrust for FFRO and WTRO cases is shown in Equations ( 5.1 ) and ( 5.2 ).

$$
\delta_ {p} = \frac {P - P _ {\mathrm {FFRO}}}{P _ {\mathrm {FFRO}}} \times 100 \% \tag{5.1}
$$

$$
\delta_ {t} = \frac {T - T _ {\mathrm {FFRO}}}{T _ {\mathrm {FFRO}}} \times 100 \% \tag{5.2}
$$

Table 5.1 NFAC 80-by 120-Foot Wind Tunnel Rotor Only Results.   

<table><tr><td>Case</td><td>Variable</td><td>FFRO</td><td>WTRO</td><td colspan="2">Sketch (WTRO)</td></tr><tr><td rowspan="4">1</td><td>power, P [J/s]</td><td>5.78E+05</td><td>5.75E+05</td><td></td><td></td></tr><tr><td>thrust, T [N]</td><td>2.75E+04</td><td>2.88E+04</td><td></td><td></td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-0.7</td><td></td><td></td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>4.7</td><td></td><td></td></tr><tr><td rowspan="4">2</td><td>power, P [J/s]</td><td>5.76E+05</td><td>5.71E+05</td><td></td><td></td></tr><tr><td>thrust, T [N]</td><td>2.77E+04</td><td>2.89E+04</td><td></td><td></td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-0.7</td><td></td><td></td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>4.3</td><td></td><td></td></tr><tr><td rowspan="4">3</td><td>power, P [J/s]</td><td>1.03E+05</td><td>1.02E+05</td><td></td><td></td></tr><tr><td>thrust, T [N]</td><td>1.21E+03</td><td>1.19E+03</td><td></td><td></td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-1.1</td><td></td><td></td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-2.0</td><td></td><td></td></tr></table>

Case 1 and 2 show consistent reduction in power and increase in thrust, leading to a performance improvement of the wind tunnel cases compared to the free field cases. As expected the interference is reduced when a slight tunnel velocity of $V =$ 10 [kts] is used compared to edgewise hover. It is likely the interference will vanish after further increasing the tunnel velocity. Re-ingestion of the wake was studied for case 2 using a coarser model with an unfitted body. At $V = 1 0$ [kts] edgewise no re-ingestion of the wake occurred, as indicated in Figure 5.2. This ‘coarse’ run was simulated using a time step of around 1/40 [s] that is far below the validation temporal resolution. It does offer a rough idea of the wake propagation over longer time.

Case 3 experiences performance change, but both power and thrust change in identical direction. This means the effect is likely to be less than observed for cases 1 and 2 because the data point can have moved along the thrust power curve. In an actual wind tunnel the rotor would have been trimmed for thrust.

Table 5.2 NFAC 80-by 120-Foot Wind Tunnel Geometry Results.   

<table><tr><td>Case</td><td>Variable</td><td>FFGE</td><td>WTGE</td><td colspan="2">Sketch (WTGE)</td></tr><tr><td rowspan="4">1</td><td>power, P [J/s]</td><td>5.77E+05</td><td>5.73E+05</td><td></td><td></td></tr><tr><td>thrust, T [N]</td><td>2.75E+04</td><td>2.87E+04</td><td></td><td></td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-0.7</td><td></td><td></td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>4.6</td><td></td><td></td></tr><tr><td rowspan="4">2</td><td>power, P [J/s]</td><td>5.75E+05</td><td>5.70E+05</td><td></td><td></td></tr><tr><td>thrust, T [N]</td><td>2.77E+04</td><td>2.88E+04</td><td></td><td></td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-0.9</td><td></td><td></td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>4.0</td><td></td><td></td></tr><tr><td rowspan="4">3</td><td>power, P [J/s]</td><td>1.39E+05</td><td>1.38E+05</td><td></td><td></td></tr><tr><td>thrust, T [N]</td><td>1.95E+03</td><td>1.93E+03</td><td></td><td></td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-0.5</td><td></td><td></td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-1.2</td><td></td><td></td></tr></table>

Differences between the cases in Table 5.1 and Table 5.2 are only apparent for case 3, in which the thrust and power of the case with TTR geometry is considerably higher compared to the rotor only cases, for an identical collective. While a true comparison of the two would need the thrust values to be trimmed, the difference, in part, is assumed to be attributable to an increase in pressure behind the rotor disc due to the inclusion of the wedge shaped front of the TTR.

图片摘要：该图主要展示 5.2 NFAC 80 by 120 Foot Wind Tunnel Geometry Results。
![](images/980d3b33657f267e819ece5d8c7be2b5e17b871ec5db67c4807d676bad57f20b.jpg)  
Figure 5.2 A velocity plot of a coarse, unfitted body test at $t \approx 6$ [s] showing no re-ingestion.

# 5.1.1 Quasi Trim for Thrust

RotCFD lacks the functionality to trim the rotor automatically, at the time of writing. To further investigate case 1-3 a ‘quasi thrust trim’ is performed for WTGE cases. By looking at the sign of the thrust change in the WTGE column, called WTGE1 for now, a very small change in collective can be proposed to yield a second WTGE data point, called WTGE2. For this small change in $P$ and T a linear interpolation is performed to find the power values of a WTGE data point with the same thrust as the FFGE data point. This ‘quasi thrust-trimmed’ WTGE data point is called WTGE*. This method allows showing the influence of the tunnel by isolating the power variable. A reduction in power suggests improved performance due to the wind tunnel, while an increase in power suggest a decrease in performance. The linearization is shown in Figure 5.3 and the computation is shown in Equation ( 5.3 ) and ( 5.4 ).

图片摘要：该图主要展示 5.2 A velocity plot of a coarse, unfitted body test at [s] s。
![](images/aad19e7a8ee12df72ed996892a5ef2216a84ce81de15ffb5922b7c33b4e47a83.jpg)  
Figure 5.3 Linearization to obtain point (TFFGE,P*).

$$
P _ {\mathrm {W T G E} *} = \frac {\Delta P _ {\mathrm {W T G E}}}{\Delta T _ {\mathrm {W T G E}}} \left(T _ {\mathrm {F F G E}} - T _ {\mathrm {W T G E} 1}\right) + P _ {\mathrm {W T G E} 1} = \frac {P _ {\mathrm {W T G E} 2} - P _ {\mathrm {W T G E} 1}}{T _ {\mathrm {W T G E} 2} - T _ {\mathrm {W T G E} 1}} \left(T _ {\mathrm {F F G E}} - T _ {\mathrm {W T G E} 1}\right) + P _ {\mathrm {W T G E} 1} \tag {5.3}
$$

$$
T _ {\mathrm {W T G E} *} = T _ {\mathrm {F F G E}} \tag {5.4}
$$

The results of the linearization are summarized in Table 5.3. It can be seen the case 3 does not experience any noticeable tunnel interference. Case 1 and 2 both show and improvement in performance due to the tunnel geometry and as expected the performance difference decreases as tunnel velocity increases. The changes in power are, however, substantial, considering the size of the 80-by 120-Foot Wind Tunnel, primarily attributable to the influence of the walls as the differences with and without geometry are thought to be negligible.

Table 5.3 Quasi Trimmed NFAC 80-by 120-Foot Wind Tunnel Geometry Results.   

<table><tr><td>Case</td><td>Variable</td><td>WTGE1</td><td>WTGE2</td><td>FFGE</td><td>WTGE*</td></tr><tr><td rowspan="4">1</td><td>power, P [J/s]</td><td>4.92E+05</td><td>5.73E+05</td><td>5.77E+05</td><td>5.36E+05</td></tr><tr><td>thrust, T [N]</td><td>2.60E+04</td><td>2.87E+04</td><td>2.75E+04</td><td>2.75E+04</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>-7.2</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">2</td><td>power, P [J/s]</td><td>4.87E+05</td><td>5.70E+05</td><td>5.75E+05</td><td>5.36E+05</td></tr><tr><td>thrust, T [N]</td><td>2.60E+04</td><td>2.88E+04</td><td>2.77E+04</td><td>2.77E+04</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>-6.7</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">3</td><td>power, P [J/s]</td><td>1.38E+05</td><td>1.51E+05</td><td>1.39E+05</td><td>1.39E+05</td></tr><tr><td>thrust, T [N]</td><td>1.93E+03</td><td>2.19E+03</td><td>1.95E+03</td><td>1.95E+03</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr></table>

For reference, the blockage fraction, expressed as the ratio of the frontal area of the TTR (without rotor) and struts to the wind tunnel cross sectional area, is found to be approximately $3 . 1 \%$ and $2 . 3 \%$ for the edgewise and axial case, respectively. These values are approximated using a CAD program. Representative velocity plots for case 2 are shown in Figure 5.4, more plots are presented in Appendix E.

图片摘要：该图主要展示 5.3 Quasi Trimmed NFAC 80 by 120 Foot Wind Tunnel Geometry R。
![](images/8a325566157d0eec0beed8736a328bef76f59a5e33752db3deff3edf1e9766e2.jpg)

图片摘要：该图主要展示 5.3 Quasi Trimmed NFAC 80 by 120 Foot Wind Tunnel Geometry R。
![](images/fa2d3f1608a67a44fcef34d0e2141758514152e54bc11c426ecfd94bcf4e99df.jpg)

图片摘要：该图片与Figure 5.4 Representative velocity plots for case 3；For reference, the blockage 这部分内容相关。
![](images/8585673bb5b1911c3cc3aebcb402dce914439be9911b6755e2fb894b6ebb1848.jpg)

图片摘要：该图片与Figure 5.4 Representative velocity plots for case 3；pPa:969E+5这部分内容相关。
![](images/bc05859538cb89cf524b6c257f71407130cbe9e60b43110cead9df1ab7fee91e.jpg)

图片摘要：该图主要展示 5.4 Representative velocity plots for case 3。
![](images/c2d1fe91b7ad4fa6356d46e31a5605420978f0e2fce433abfe8ca317a2ce3cbd.jpg)

Figure 5.4 Representative velocity plots for case 3.   
图片摘要：该图主要展示 5.4 Representative velocity plots for case 3V/ pPa:969E+5 5.。
![](images/0de9dd72b2ab6176af955bcb42989a65479f9df2b220995de52ee03e9588a318.jpg)  
V/

pPa:969E+5

# 5.2 NFAC 40-by 80-Foot Wind Tunnel Results

The results for the rotor only cases and geometry cases for both free field and wind tunnel simulations are summarized in Table 5.4 and Table 5.5, respectively. The last column in both tables shows a top view (XY-plane) sketch of the wind tunnel configurations of the subset WTRO of each case.

Case 4 indicates low interference with both drops in thrust and power simultaneously. The proximity of the wall to the rotor in the 40- by 80-Foot Wind Tunnel seems to adversely influence the rotor at higher speeds as shown in case 5. A power increase with thrust loss is shown both with geometry and for the isolated rotor case. Care must be taken however, that the rotor in Case 5 is operating under a different collective and other free stream velocity, changing the blade loading and thus performance, making a comparison very difficult.

Significant differences between isolated rotor and geometry cases are only observed in case 6. The difference is again thought to be caused by the increased pressure at the back of the rotor due to the wedge-like shape of the TTR nose, or by a difference in blade loading. This in turn increases the pressure in the vicinity of the TTR increasing the thrust. Case 6 with and without rotor shows a significant difference in performance. Due to constraints on the computational budget no ‘quasi trim’ has been performed on the rotor only cases, but it is thought that the operating conditions of the rotor are changed and likely shows a positive performance increase. Case 7 shows a thrust and power increase and therefore more favorable interference compared to the fully edgewise TTR in case 5.

Table 5.4 NFAC 40-by 80-Foot Wind Tunnel Rotor Only Results   

<table><tr><td>Case</td><td>Variable</td><td>FFRO</td><td>WTRO</td><td>Sketch</td></tr><tr><td rowspan="4">4</td><td>power, P [J/s]</td><td>4.84E+05</td><td>4.79E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>2.47E+04</td><td>2.44E+04</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-1.1</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-1.1</td></tr><tr><td rowspan="4">5</td><td>power, P [J/s]</td><td>2.92E+05</td><td>2.99E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>2.69E+04</td><td>2.65E+04</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>2.6</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-1.4</td></tr><tr><td rowspan="4">6</td><td>power, P [J/s]</td><td>7.70E+05</td><td>7.93E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>6.50E+03</td><td>6.73E+03</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>3.0</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>3.6</td></tr><tr><td rowspan="4">7</td><td>power, P [J/s]</td><td>7.26E+05</td><td>7.44E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>2.28E+04</td><td>2.37E+04</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>2.5</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>4.0</td></tr></table>

Similarly to the 80-by 120-Foot Wind Tunnel, re-ingestion has been examined for low tunnel velocities, i.e. case 4, and has been observed not to occur above at $V = 1 0$ [kts] edgewise. Similarly to the previous section, the geometry cases from Table 5.5 are trimmed for thrust using a linearized method.

Table 5.5 NFAC 40-by 80-Foot Wind Tunnel Geometry Results   

<table><tr><td>Case</td><td>Variable</td><td>FFGE</td><td>WTGE</td><td>Sketch</td></tr><tr><td rowspan="4">4</td><td>power, P [J/s]</td><td>4.83E+05</td><td>4.75E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>2.46E+04</td><td>2.41E+04</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-1.7</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-2.2</td></tr><tr><td rowspan="4">5</td><td>power, P [J/s]</td><td>2.85E+05</td><td>2.94E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>2.69E+04</td><td>2.66E+04</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>3.3</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-1.0</td></tr><tr><td rowspan="4">6</td><td>power, P [J/s]</td><td>8.77E+05</td><td>8.63E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>7.62E+03</td><td>7.46E+03</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>-1.6</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>-2.0</td></tr><tr><td rowspan="4">7</td><td>power, P [J/s]</td><td>7.30E+05</td><td>7.46E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T [N]</td><td>2.33E+04</td><td>2.41E+04</td></tr><tr><td>change of power, δp [%]</td><td>0.0</td><td>2.2</td></tr><tr><td>change of thrust, δt [%]</td><td>0.0</td><td>3.1</td></tr></table>

# 5.2.1 Quasi Trim

The methodology to trim the thrust value is identical to the procedure in Section 5.1.1 and Equation ( 5.3 ) and ( 5.4 ). The results of the quasi trim are show in Table 5.6.

Table 5.6 Quasi Trimmed NFAC 40-by 80-Foot Wind Tunnel Geometry Results   

<table><tr><td>Case</td><td>Variable</td><td>WTGE1</td><td>WTGE2</td><td>FFGE</td><td>WTGE*</td></tr><tr><td rowspan="4">4</td><td>power, P [J/s]</td><td>4.75E+05</td><td>5.08E+05</td><td>4.83E+05</td><td>4.88E+05</td></tr><tr><td>thrust, T [N]</td><td>2.41E+04</td><td>2.54E+04</td><td>2.46E+04</td><td>2.46E+04</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>1.0</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">5</td><td>power, P [J/s]</td><td>2.94E+05</td><td>3.02E+05</td><td>2.85E+05</td><td>2.99E+05</td></tr><tr><td>thrust, T [N]</td><td>2.66E+04</td><td>2.70E+04</td><td>2.69E+04</td><td>2.69E+04</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>4.8</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">6</td><td>power, P [J/s]</td><td>8.63E+05</td><td>9.69E+05</td><td>8.77E+05</td><td>8.63E+05</td></tr><tr><td>thrust, T [N]</td><td>7.46E+03</td><td>8.47E+04</td><td>7.62E+03</td><td>7.62E+03</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>-1.6</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">7</td><td>power, P [J/s]</td><td>7.46E+05</td><td>4.96E+05</td><td>7.30E+05</td><td>7.25E+05</td></tr><tr><td>thrust, T [N]</td><td>2.41E+04</td><td>1.50E+04</td><td>2.33E+04</td><td>2.33E+04</td></tr><tr><td>change of power, δp [%]</td><td>-</td><td>-</td><td>0.0</td><td>-0.7</td></tr><tr><td>change of thrust, δt [%]</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr></table>

Both edgewise cases, case 4 and 5, show a decrease in performance, seemingly increasing with tunnel velocity. Both the axial and tilt case, case 6 and 7 respectively, show an increase in performance, as expected according to Glauert [23]. For

reference, the blockage fraction, is found to be approximately $7 . 7 \%$ , $3 . 8 \%$ and $7 . 5 \%$ for the edgewise, axial and tilt case, respectively. These values are approximated using a CAD program. Figure 5.5 shows the flow field of the FFGE subset for case 7, more flow field solutions are presented in Appendix E.

图片摘要：该图主要展示 5.6 Quasi Trimmed NFAC 40 by 80 Foot Wind Tunnel Geometry Re。
![](images/97f28deecdb6f6f7aed4bfbfdb053898e83a719517bfc4743f5fb13d02b69ab5.jpg)  
Figure 5.5 Flowfield of FFGE subset for case 7.

# 5.3 Performance Convergence

The performance convergence for case 2 and 6 is shown in Figure 5.6 and Figure 5.7. Performance convergence below . $. 2 5 \%$ is usually quickly observed, following the same procedure as for the validation cases. Case 2 has a high amount of time steps and shows ‘typical’ slower convergence for hover cases. Case 7 shows rapid convergence characteristic for airplane or tilt mode cases.

图片摘要：该图主要展示 5.5 Flowfield of FFGE subset for case 7。
![](images/ca55450176d6390a4e1e4926deef10f0b62cfff3971eff2621ce7969ad76cc67.jpg)  
Figure 5.6 Performance convergence for case 2, WTGE, hover.

图片摘要：该图主要展示 5.6 Performance convergence for case 2, WTGE, hover。
![](images/314bdf72dbecb16e56a25cba74bc85f346ccc59cdd2689a9926e1000341451d3.jpg)  
Figure 5.7 Performance convergence for case 7, WTGE, tilt mode.

# 5.4 Forces on the TTR

The rotor performance will be directly measured within the TTR axis. Therefore the wind tunnel scale doesn’t have to be used and the forces on the TTR are, for this research, not of much importance as RotCFD outputs the rotor performance directly. Moreover, since RotUNS doesn’t allow for viscous body-fitted grids, chances of an accurate drag measurement greatly diminish as no plausible boundary layer will be modeled, or better, sustained. Also the unsteady nature of the URANS solver may show slight variations in the forces due to unsteady (vortex) shedding.

Two representative graphs with the forces on the TTR are outputted, however, to show particular problem of interest. Figure 5.8 shows the integrated forces on the TTR for an edgewise case at high tunnel velocity - case 5, WTGE. The behavior of these forces over time is as expected, flattening out as the flow and wake are fully established over time.

图片摘要：该图主要展示 5.7 Performance convergence for case 7, WTGE, tilt mode。
![](images/d2e379a741687c7d561c9dabe9e80e024a50bc2306fe46cfdf404407a88cf991.jpg)  
Figure 5.8 Integrated forces on the TTR for case 5, WTGE.

A particular case, which has been run for extra time to investigate its behavior, is that of case 4. The edgewise low velocity case in the 40-by 80-Foot Wind Tunnel test section. It shows that even after nearly doubling the time steps the forces on the TTR have not converged yet.

图片摘要：该图主要展示 5.8 Integrated forces on the TTR for case 5, WTGE。
![](images/873f998cec7f55537670e32d56df35e8c9f8fece3f6e5453b18b0100615d77ff.jpg)  
Figure 5.9 Integrated forces on the TTR and struts for case 4, WTGE.

The power and thrust only vary . $. 5 \%$ and $1 \%$ respectively over the last $5 0 \%$ of simulated time, as is shown in Figure 5.10. This extremely stable performance behavior of the rotor was found consistently throughout this report. It recommended for future work to further investigate the transient nature of the forces observed in this case.

图片摘要：该图主要展示 5.9 Integrated forces on the TTR and struts for case 4, WTGE。
![](images/0137bb65891d2bab020bb741c80699d05ac87d9eb9edb42a776cfa275c74ed5f.jpg)  
Figure 5.10 Performance convergence for case 4, WTGE.

# 5.5 Stability Related Time Step Restrictions

A problem encountered during this research was the stability related time step restriction. The ‘clean’ rectilinear Cartesian grid, such as that one used in the isolated rotor cases for the validation, was combined with the tetrahedral cells for the body fitting. The tetrahedrals show higher aspect ratios per cell and sharp angles, compared to the near-squared cells in the far field. In the case of stability related time step restrictions it is thought the turbulent kinetic energy, $k ,$ and turbulent dissipation values, ε, diverge over time, which, as they are coupled back into the RANS equations, cause flow field divergence.

The addition of these cells therefore limit the maximum time step used, often much smaller than the time step necessary for accurate rotor performance values as used in Section 0. In some cases a time step equivalent to half a degree of rotor rotation would be necessary, tremendously increasing the computational effort.

It is left for future work to investigate the effect of another gridding technique, perhaps using RotVIS or another module and investigate the performance results running with more refined unfitted bodies solely using a Cartesian grid. Figure 5.11, Figure 5.12 and Figure 5.13 show the TTR nose ungridded (only meshed), with the used body fitting, and an unfitted version, respectively.

图片摘要：该图主要展示 5.11 Meshed TTR nose (no grid)。
![](images/ace736f5757d4a306273f614146bb3bb5e580c599beb896a6287e4aafb58c1e6.jpg)  
Figure 5.11 Meshed TTR nose (no grid).

图片摘要：该图主要展示 5.11 Meshed TTR nose (no grid)。
![](images/70b2869016bec08fbaec41533a2ee0a89100bd02f1ace4253c083de623354c70.jpg)  
Figure 5.12 Body fitted TTR nose.

图片摘要：该图主要展示 5.12 Body fitted TTR nose。
![](images/95e1ff407ed5be41adbdbaa109acb58ca1bb2a6b447730690fa5c7139bc04813.jpg)  
Figure 5.13 Gridded TTR nose without body fitting.

# 6 Conclusions and Recommendations

# 6.1 Conclusions

The setup and grid generation in RotCFD is faster than many CFD codes and therefore makes it a useful engineering tool. The validation results show very good correlation with performance data over the thrust range examined. The results for the XV-15 isolated rotor in hover with a Corrigan stall delay method showed excellent performance correlation compared the OARF data set. The tip loss model was found to overcorrect, most likely caused by the generated tip vortex or pressure equalization over the blade tip. The tip loss is, however, not fully accounted for by RotCFD, as can be seen from the obtained blade loading. For the tilt and airplane mode cases the XV-15 rotor model showed accurate results compared to wind tunnel data, with only minor differences observed between the tip loss model and clean variant. These differences are due to the lower thrust settings and lower induced velocities at the tips mostly because of the advance ratio. Overall the author believes a very good compromise between accuracy and efficiency is achieved. For hover tests the Corrigan and Schillings stall delay model with $n = 1 . 8$ is advised and for tilt and airplane mode the clean XV-15 rotor will suffice for very reasonable performance predictions in complicated flows.

For the 80-by 120-Foot Wind Tunnel no influence was found for the XV-15 rotor in axial mode at the highest tunnel velocity of $V = 1 0 0$ [kts]. For the case with (near) hover in edgewise mode, the performance shows a power decrease of $- 7 . 2 \%$ and - $6 . 7 \%$ for hover and edgewise flight with $V = 1 0$ [kts], respectively. The large interference at this very unfavorable configuration is attributed to the boxed-in effect of the rotor facing the tunnel wall.

For the 40-by 80-Foot Wind Tunnel interference was found under all tested conditions as is to be expected due to the smaller cross sectional area of the test section. In edgewise mode both at tunnel velocities of $V = 1 0$ [kts] and $V = 1 0 0$ [kts] an increase in power is observed of $1 . 0 \%$ and $4 . 8 \% ,$ respectively. Differences between the two edgewise cases are hard to justify because of the different operating conditions of the rotor. Both the axial case at $V = 2 0 0$ [kts] and the tilted case at V $= 1 0 0$ [kts] shows a decrease in power of - $- 1 . 6 \%$ and $0 . 7 \% ,$ respectively. This is expected for a thrusting rotor in airplane mode in a duct. The axial case at $V = 2 0 0$ [kts] shows a wake velocity slightly over $M = 0 . 3 0$ , which could be questioned for its validity due to compressibility effects. Researchers at Ames were not convinced it would yield any substantial difference in this case, especially since the delta is obtained between two similar cases.

# 6.2 Recommendations

The investigation of the effect of stall delay in other flight modes is left for future work. A better tip loss model, either by reducing the tip loss factor or finding a better suitable method is also left for future work. At the time of writing a new model has been introduced for use with RotCFD. The approach corrects the local angle of attack to achieve zero lift at the tip based on the local pressure difference between the top and bottom of the rotor.

All performance validation data is expressed as function of thrust coefficient over solidity. A better picture of the correlation is obtained if this solidity value is not used, and hence the coefficients only are used as parameters. This leads to more direct comparisons of the thrust and power. Because of the ambiguous solidity data (not every report is clear on what value is used) the solidity value is incorporated in the present calculations.

Considerable amount of work can be done to investigate the blade loading of the XV-15 rotor. Because of the changing blade loading at different azimuthal stations and numerous flight modes and thrust values this is a considerable effort. The thrust modeled in this research is well in the normal range of the XV-15. More research can lead to performance data into the rotor stall region. The assumption that the rotor was not trimmed, to reduce the rolling moment, might also cause adverse rotor effects. Therefore cyclic pitch variation and its effect on performance can also be further investigated.

RotUNS is capable of adaptive grids. For this research it was chosen to keep the gridding and flow field cell sizes nearly identical over the cases for consistent performance values and comparison. A tailored adaptive grid, however, could improve the wake propagation through the domain and due to the specified high cell density could yield a more efficient simulation or a more accurate result in equal computation time. It is highly interesting if an adaptive grid can yield improved computed velocities at the blade or disk tips and hence discard the need for a tip model at all.

The reason for the performance mismatch using the unsteady model is not found. One hypothesis is that, even at a considerably small delta time, the implicit method fails to follow the exact time variations of the flow field. When this mismatch is then incorrectly matched with the ‘hard coded’ timing of the discrete rotor blades the time of the blade position and wake state are not correct and could lead to different pressures over the rotor disk. Also the rotor trim could affect the unsteady results more aggressively compared to the steady model.

A substantial issue found with the use of RotUNS and body fitted grids was the stability related time step restriction. Because of the need to reduce the time step considerably the computational time per case increased significantly. A finer grid doesn’t necessarily solve the problem because the effective cell shape at the body fit remains similar. An investigation into the use of RotVIS, which can handle body-fitted viscous grids, and therefore should simulate boundary layers more accurately as well, might present useful as the body fitted cells are much more organized. The use of RotVIS for this research was highly discouraged before the author was fully familiar with RotUNS. If the computation time can be considerably reduced using RotVIS it might be possible to generate enough performance data points per case to actually generate power curves. These are much more useful to compare than individual data points. Another area of interest is the wall pressure along the longitudinal axis of the tunnel test sections. These can be obtained by extracting the pressure along the centerlines of the walls, presumable excluding the floor-plane. A second set of simulations for empty test sections must be performed, however.

# References

[1] E. Solis, “LCTR Fuselage.” [Online]. Available: http://rotorcraft.arc.nasa.gov/Images/Pictures for Wall/LCTR_fuselageV2.jpg. [Accessed: 09-Mar-2015].   
[2] W. Johnson, “An assessment of the Capability To Calculate Tilting Prop-Rotor Aircraft Performance, Loads, and Stability,” NASA TP 2291, pp. 1–21, 1984.   
[3] W. Johnson, Rotorcraft Aeromechanics. Moffett Field: Cambridge University Press, 2013.   
[4] J. Seddon, Basic Helicopter Aerodynamics. Oxford: BSP Professional Books, 1990.   
[5] M. D. Maisel, D. J. Giulianetti, and D. C. Dugan, “The History of The XV-15 Tilt Rotor Research Aircraft From Concept to Flight,” NASA SP 4517, pp. 1–194, 2000.   
[6] J. C. W. Acree, “Private Correspondence.” NASA Ames Aeromechanics Department, Moffett Field, 2015.   
[7] Anon., “Future Vertical Lift (FVL) Joint Multi-Role (JMR) Technology Demonstrator (TD),” 2014.   
[8] J. D. Anderson, “Fundamentals of Aerodynamics,” McGrawhill Inc, vol. 1984, pp. 1–772, 1991.   
[9] R. Vos and S. Farokhi, Introduction to Transonic Aerodynamics. Delft: Springer, 2015.   
[10] R. G. Rajagopalan, V. Baskaran, A. Hollingsworth, A. Lestari, D. Garrick, E. Sous, and B. Hagerty, “RotCFD - A tool for aerodynamic interference of rotors: Validation and capabilities,” in American Helicopter Society International - Future Vertical Lift Aircraft Design Conference 2012, 2012, pp. 311–327.   
[11] L. A. Young, G. K. Yamauchi, and G. Rajagopalan, “Simulated rotor wake interactions resulting from civil tiltrotor aircraft operations near vertiport terminals,” in 51st AIAA Aerospace Sciences Meeting including the New Horizons Forum and Aerospace Exposition 2013, 2013.   
[12] P. R. Spalart, “Strategies for turbulence modelling and simulations,” Int. J. Heat Fluid Flow, vol. 21, no. 3, pp. 252–263, 2000.   
[13] G. Iaccarino, A. Ooi, P. a. Durbin, and M. Behnia, “Reynolds averaged simulation of unsteady separated flow,” Int. J. Heat Fluid Flow, vol. 24, no. 2, pp. 147–156, 2003.   
[14] B. E. Launder and D. B. Spalding, “The numerical computation of turbulent flows,” Comput. Methods Appl. Mech. Eng., vol. 3, no. 2, pp. 269–289, 1974.   
[15] W. P. Jones and B. E. Launder, “The prediction of laminarization with a two-equation model of turbulence,” Int. J. Heat Mass Transf., vol. 15, no. 2, pp. 301–314, 1972.   
[16] Z. Yu and Y. Cao, “Three dimensional turbulence numerical simulation of rotor in forward flight,” Beijing Hangkong Hangtian Daxue Xuebao/Journal Beijing Univ. Aeronaut. Astronaut., vol. 32, no. 7, pp. 751–755, 2006.   
[17] J. D. Anderson, “Computational Fluid Dynamics: The Basics with Applications,” McGrawhill Inc, pp. 37–94, 1995.   
[18] R. G. Rajagopalan and C. K. Lim, “Laminar Flow Analysis of a Rotor in Hover,” J. Am. Helicopter Soc., vol. 36, no. 1, pp. 12–23, 1991.   
[19] H. K. Edenborough, “Research at NASA’s NFAC wind tunnels,” Int. Sess. Japan Soc. Aeronaut. Sp. Sci. Aircr. Symp., pp. 1–9, 1990.   
[20] P. T. Zell, “Performance and test section flow characteristics of the National Full-Scale Aerodynamics Complex 80- by 120-Foot Wind Tunnel,” NASA TR 103920, pp. 1–66, 1993.   
[21] P. T. Zell and K. Flack, “Performance and test section flow characteristics of the National Full-Scale Aerodynamics Complex 40- by 80-foot wind tunnel,” NASA TM 101065, no. February, pp. 1–81, 1989.   
[22] V. R. Corsiglia, L. E. Olson, and M. D. Falarski, “Aerodynamic Characteristic of the 40- by 80/80- by 120-Foot Wind Tunnel at NASA Ames Research Center,” NASA TM 85946, no. April, pp. 1–22, 1984.   
[23] H. Glauert, “Wind Tunnel Interference on Wings, Bodies and Airscrews,” Aeronaut. Res. Comm., pp. 1–52, 1933.   
[24] A. Pope and W. H. J. Rae, Low-Speed Wind Tunnel Testing, 2nd ed. Seattle: John Wiley & Sons, 1984.   
[25] NASA Ames Research Center, “Tiltrotor Test Rig,” 2015. [Online]. Available: http://rotorcraft.arc.nasa.gov/Research/facilities/ttr.html#. [Accessed: 24-Mar-2015].   
[26] M. D. Maisel, D. C. Borgman, and D. D. Few, “Tilt Rotor Research Aircraft Familiarization Document,” NASA TM X-62, 407, pp. 1–105, 1975.

[27] D. C. Dugan, R. G. Erhart, and L. G. Schroers, “The XV-15 Tilt Rotor Research Aircraft,” NASA TM 81244, pp. 1–18, 1980.   
[28] F. F. Felker, M. D. Betzina, and D. B. Signor, “Performance and Loads Data from a Hover Test of a Full-Scale XV-15 Rotor,” NASA TM 86833, pp. 1–94, 1985.   
[29] Anon., “Task II - Wind Tunnel Test Results,” NASA CR 114363, 1976.   
[30] W. Johnson, “CAMRAD II Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics.” Johnson Aeronautics, Palo Alto, 2005.   
[31] W. L. Arrington, M. Kumpel, R. L. Marr, and K. G. McEntire, “PXV-15 Tilt Rotor Research Aircraft Flight Test Data Report,” NASA CR 177406, vol. 1–5, pp. 1–202, 1985.   
[32] J. J. Corrigan and J. J. Schillings, “Emprical Model for Stall Delay Due to Rotation,” Am. Helicopter Soc. Aeromechanics Spec. Conf., pp. 8.4 – 1 to 8.4 – 15, 1994.   
[33] S. Forth, P. Hovland, E. Phipps, J. Utke, and A. Walther, Recent Advances in Algorithmic Differentiation. Springer Science & Business Media, 2012.   
[34] C. Acree, “Modeling Requirements for Analysis and Optimization of JVX Proprotor Performance,” in American Helicopter Society 64th Annual Forum, Montreal, Canada, 2008, pp. 1–21.   
[35] W. Johnson, “CAMRAD II,” vol. VI, no. 4.9, pp. 1–294.   
[36] J. G. Leishman, Helicopter Aerodynamics, 2nd ed. Maryland: Cambridge University Press, 2006.   
[37] D. W. Warmbrodt, “Private Correspondence.” NASA Ames Aeromechanics Department, Moffett Field, 2015.   
[38] J. W. Hong, “Hover and Cruise Flight Simulation of XV-15 Experimental Aircraft Using RotCFD,” Moffett Field, 2015.

# Appendix A NFAC Characteristics

The main characteristics of the NFAC wind tunnel test sections are summarized in Table A.1 and Table A.2.

Table A.1 40 x 80 Foot Wind Tunnel Characteristics [21].   

<table><tr><td colspan="3">40 x 80 Foot Wind Tunnel</td></tr><tr><td>Width Test Section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Height Test Section</td><td>12.19 m</td><td>(40 ft)</td></tr><tr><td>Length Test Section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Actual Width Test Section</td><td>24.08 m</td><td>(79 ft)</td></tr><tr><td>Actual Height Test Section</td><td>11.89 m</td><td>(39 ft)</td></tr><tr><td>Actual Length Test Section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Approximate BL Thickness Floor (Start - End)</td><td>.25 - .46 m</td><td>(10 - 18 in)</td></tr><tr><td>Approximate BL Thickness Top (Start - End)</td><td>.08 - .15 m</td><td>(3 - 6 in)</td></tr><tr><td>Approximate BL Thickness Sides (Start - End)</td><td>&gt;.25 - .46 m</td><td>(&gt; 10 - 18 in)</td></tr><tr><td>Maximal Test Section Velocity</td><td>154.33 m/s</td><td>(300 kts)</td></tr></table>

Table A.2 80 x 120 Foot Wind Tunnel Characteristics [20].   

<table><tr><td colspan="3">80 x 120 Foot Wind Tunnel</td></tr><tr><td>Width Test Section</td><td>36.58 m</td><td>(120 ft)</td></tr><tr><td>Height Test Section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Length Test Section</td><td>36.58 m</td><td>(120 ft)</td></tr><tr><td>Actual Width Test Section</td><td>35.97 m</td><td>(118 ft)</td></tr><tr><td>Actual Height Test Section</td><td>23.93 m</td><td>(78.5 ft)</td></tr><tr><td>Actual Length Test Section</td><td>36.58 m</td><td>(120 ft)</td></tr><tr><td>Approximate BL Thickness Floor (Start - End)</td><td>.76 - 1.12 m</td><td>(30 - 44 in)</td></tr><tr><td>Maximal Test Section Velocity</td><td>51.44 m/s</td><td>(100 kts)</td></tr></table>

# Appendix B C81 Airfoil Adjustment Code Results

# B.1 Angle of Attack and Mach number interpolation

The C81 airfoil files are obtained from experienced XV-15 researchers [6]. The interpolation for angle of attack and Mach number is performed. Figure B.1 shows part of the imported data for the 64-X08 airfoil and the PCHIP interpolation for angles of attack and linear interpolation for Mach numbers.

图片摘要：该图片与The C81 airfoil files are obtained from experienced XV 15 researchers [6]. The i这部分内容相关。
![](images/285cc610bfc8ca5a6ee6312d2b994cf55ea5a6f7da3cc85b81355581283c7c9b.jpg)

图片摘要：该图片与The C81 airfoil files are obtained from experienced XV 15 researchers [6]. The i这部分内容相关。
![](images/e413f50887cc3dc0fde78c50dabeb2f5b93cd8d1c9cb56897667a938caab8898.jpg)

图片摘要：该图主要展示 B.1 Imported C81 data for NACA 64 X08 airfoil。
![](images/ad97a979b558247e6aaa454db5a05a77ea6b94abec33314b9a74391f801b976b.jpg)

图片摘要：该图片与Figure B.1 Imported C81 data for NACA 64 X08 airfoil；Similar data is shown in Fi这部分内容相关。
![](images/2aab1f0a8a3ddca4f97b4ee5fae7ed23b01f3cbabdd655587ce8b387ed154b7b.jpg)

图片摘要：该图主要展示 B.1 Imported C81 data for NACA 64 X08 airfoil。
![](images/f5a2976ce7ce76202000b12626ef0da827c1a846f9a9e618ff03786c04d73e1e.jpg)

图片摘要：该图主要展示 B.1 Imported C81 data for NACA 64 X08 airfoil。
![](images/22a81647cee3c97e41b606474888dc336a824012a06a25ea30b181f904719781.jpg)  
Figure B.1 Imported C81 data for NACA 64-X08 airfoil.

Similar data is shown in Figure B.2, Figure B.3 and Figure B.4 for the 64-X12, 64-X18 and 64-X25 airfoils, respectively.

图片摘要：该图主要展示 B.1 Imported C81 data for NACA 64 X08 airfoil。
![](images/13eeff53728659d66bd8a1f754a3af9bbee3ffe8c0bc85cd3e74f1e0e05c440e.jpg)

图片摘要：该图主要展示 B.1 Imported C81 data for NACA 64 X08 airfoil。
![](images/8f47cdffc9616839de3731d6eb136057e0fcbda10432816e7dfe801c54e0c49e.jpg)

图片摘要：该图主要展示 B.1 Imported C81 data for NACA 64 X08 airfoil。
![](images/fc2193aeea7fa2ca1802215d3cd3195db680895779b523daf22417e03893ceaf.jpg)

图片摘要：该图片与Figure B.2 Imported C81 data for NACA 64 X12 airfoilSimilar data is shown in Fig这部分内容相关。
![](images/e9517f7d0ba29710abac8a79a154231ebcdec8a2be7521f4d8a281487e7bc7ef.jpg)

图片摘要：该图主要展示 B.2 Imported C81 data for NACA 64 X12 airfoil。
![](images/c3bac836f984574f7fc2f91c896c9350926523135dd95ab6291cdf30c1435bfa.jpg)

图片摘要：该图主要展示 B.2 Imported C81 data for NACA 64 X12 airfoil。
![](images/2a81c4cecff9946649b812833a553ebbaa145fffa9bf90ff61dd3a4c697ef815.jpg)  
Figure B.2 Imported C81 data for NACA 64-X12 airfoil.

图片摘要：该图主要展示 B.2 Imported C81 data for NACA 64 X12 airfoil。
![](images/3a90192815fd083be560afc5e777467ef3e94f606155892a846f99ad60d6c613.jpg)

图片摘要：该图主要展示 B.2 Imported C81 data for NACA 64 X12 airfoil。
![](images/b09594bc619a4ba245e1c677a0c60a3891f9f30fea6ab10ae809bf8a9fd734ac.jpg)

图片摘要：该图主要展示 B.2 Imported C81 data for NACA 64 X12 airfoilFigure B.3 Impo。
![](images/5ecacde21920fe543f4219b2bcabc9a6f45d9c578ee16ff9ee5bf94c2970b70b.jpg)

图片摘要：该图主要展示 B.2 Imported C81 data for NACA 64 X12 airfoilFigure B.3 Impo。
![](images/615118ec0e9e6f3ba66ae8685d9873ef3dd59f40387a3f6e20a3a71a9c900cfb.jpg)

图片摘要：该图主要展示 B.3 Imported C81 data for NACA 64 X18 airfoil。
![](images/155604687927d0e3c5e9ba978c06a6f616d4b6971fa91eb0480dfedaa168a91c.jpg)

图片摘要：该图主要展示 B.3 Imported C81 data for NACA 64 X18 airfoil。
![](images/a0f26fc31d7f846da86b7e2b5f74ab11d7f0e4b28ee53c66636089ffe236c441.jpg)  
Figure B.3 Imported C81 data for NACA 64-X18 airfoil.

图片摘要：该图主要展示 B.3 Imported C81 data for NACA 64 X18 airfoil。
![](images/2d910c4df7baf98684cbd9f2eaada45b1948c1f71d8d8211a3ddfd9bb4866c0e.jpg)

图片摘要：该图主要展示 B.3 Imported C81 data for NACA 64 X18 airfoil。
![](images/5fd5bf08bd6256f4259a141c99327ab0ff492e8e4e300ac8bfb52395b7cdaea2.jpg)

图片摘要：该图主要展示 B.3 Imported C81 data for NACA 64 X18 airfoilFigure B.4 Impo。
![](images/a4326741e0def129e34928e622a0bb6551dbff41a285d615399676acc1937466.jpg)

图片摘要：该图主要展示 B.3 Imported C81 data for NACA 64 X18 airfoilFigure B.4 Impo。
![](images/0597b172ad896cbd98183ecb202610189dfb9c35d6a17b785ae48003a840b269.jpg)

图片摘要：该图主要展示 B.4 Imported C81 data for NACA 64 X25 airfoil。
![](images/9c5e3d78a223544686583eec8d1fe42fc8b647eebc8610a9760789d4178da80c.jpg)

图片摘要：该图主要展示 B.4 Imported C81 data for NACA 64 X25 airfoil。
![](images/c4b556815be6e0abf12273c4621514f5eb3612414bdb9dfaee6d32c172323f8a.jpg)  
Figure B.4 Imported C81 data for NACA 64-X25 airfoil.

# B.2 Representative Stall Delay Plots

Figure B.5 and Figure B.6 show the effect of stall delay on the lift curve slope on a set of interpolated airfoil data at various radial stations.

图片摘要：该图主要展示 B.5 and Figure B.6 show the effect of stall delay on the lif。
![](images/ddd38233444da217bdc5f0de8feaed72399791006129597bad25634af7a41ef3.jpg)

图片摘要：该图主要展示 B.5 and Figure B.6 show the effect of stall delay on the lif。
![](images/2c3d598fd616fd6ee6dfb3cefb11a6a000214d9b22c0ac002e54e47e25c4c7a3.jpg)

图片摘要：该图主要展示 B.5 and Figure B.6 show the effect of stall delay on the lif。
![](images/ece243051f95d27d56dd33cc33f3ab0de4bf06954f5e8683d4f0533171a0341e.jpg)

图片摘要：该图主要展示 B.5 and Figure B.6 show the effect of stall delay on the lif。
![](images/cfdde902b9cf95721c2f68716b0dc4a37d9fdd9a5507ca4559b78c3de71a4bc9.jpg)

图片摘要：该图主要展示 B.5 Effect of stall delay on lift curve slope。
![](images/6f9333a77f4b295f3622f8d10d99464bdf52ff9ac36f927c3a642e1dcc9ce136.jpg)

图片摘要：该图主要展示 B.5 Effect of stall delay on lift curve slope。
![](images/7be145a329eb07ee3ee0ef0623e104e1b4b7bfbd0b07710588d3ef3226bde67f.jpg)  
Figure B.5 Effect of stall delay on lift curve slope.

图片摘要：该图主要展示 B.5 Effect of stall delay on lift curve slope。
![](images/8a16fffc00ce2af652e1b1d450cc2a9c619d88a34b058ef3848f64b22ac3166c.jpg)

图片摘要：该图主要展示 B.5 Effect of stall delay on lift curve slope。
![](images/dd0a5e467d6c4f72b671bc07d6b0e6daf311c59d6b8dda64727ca866a99a0064.jpg)

图片摘要：该图主要展示 B.5 Effect of stall delay on lift curve slopeFigure B.6 Effe。
![](images/3de54554c7d22af656d56e4f4a6d6703b534a4bf78380bacf14341bc472d6969.jpg)

图片摘要：该图主要展示 B.5 Effect of stall delay on lift curve slopeFigure B.6 Effe。
![](images/c21e57620befa97ec63493312c39862edd9394d64001ad4ed94da824a094df62.jpg)

图片摘要：该图主要展示 B.6 Effect of stall delay on lift coefficient for set of air。
![](images/96df737d5a83a93b7f6e96bb4c120e9d88380146648a46d215d6d7821907ffbb.jpg)

图片摘要：该图主要展示 B.6 Effect of stall delay on lift coefficient for set of air。
![](images/0e7c9768aba059f5c2aeba6b46c5cde1c2c16ab694ee6cb12e658784664de18a.jpg)  
Figure B.6 Effect of stall delay on lift coefficient for set of airfoil data at various radial stations.   
Figure B.6d shows the result of the assumption that the zero lift angle of attack is equal to zero. As a result the lift coefficient is slightly lowered at high Mach numbers. While the observed effect is small, future work could eliminate this error from the program.

# Appendix C Steady XV-15 Rotor Validation Results

All the plots for the steady results are presented in Section 0.

# C.1 Simulation Parameters

Table C.3 shows a compact overview of the simulation parameters. ND stands for non-dimensionalized, the boundary size is expressed as the coordinates of the corners of a rectangular prism. The grid cells indicate the amount of cells on the x,y and z edge of the boundary, respectively. Rotor Grid Ref. and Grid Refinement indicate refinement of cells by multiplying the amount of cells by a certain factor.

Table C.3 Overview of steady simulation parameters.   

<table><tr><td colspan="2">Hover Parameters</td><td colspan="2">Boundary Conditions &amp; Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary Size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.1)</td><td>Simulated time</td><td>2.5 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells [#]</td><td>30,30,42</td><td>Timesteps</td><td>3000</td></tr><tr><td>Tip speed</td><td>225.55 m/s</td><td>Rotor Box Ref.</td><td>1,1</td><td>ΔT</td><td>2.50E-03</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor Grid Ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid Refinement Box [m]</td><td>(-7.62, -7.62, -68.58) (7.62, 7.62, 38.1)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.41E+08</td><td>Grid Refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.84E+06</td><td>Volume Ratio Max</td><td>8</td><td>Flight Condition</td><td>hover</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td>Rotor Model</td><td>steady</td></tr><tr><td colspan="2">Tilt and Advance Ratio</td><td colspan="2">Boundary Conditions &amp; Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary Size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells [#]</td><td>30,30,42</td><td>Timesteps</td><td>1000</td></tr><tr><td>Tip speed</td><td>221.17 m/s</td><td>Rotor Box Ref.</td><td>1,1</td><td>ΔT</td><td>2.50E-03</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor Grid Ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid Refinement Box [m]</td><td>(-15.24, -7.62, -68,58) (7.62, 7.62, 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.05E+08</td><td>Grid Refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.73E+06</td><td>Volume Ratio Max</td><td>8</td><td>Flight Condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>2,029,692 (at 30 degree tilt)</td><td>Rotor Model</td><td>steady</td></tr><tr><td colspan="2">Airplane Mode</td><td colspan="2">Boundary Conditions &amp; Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary Size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells [#]</td><td>30,30,42</td><td>Timesteps</td><td>1000</td></tr><tr><td>Tip speed</td><td>183.76 m/s</td><td>Rotor Box Ref.</td><td>1,1</td><td>ΔT</td><td>2.50E-03</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor Grid Ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid Refinement Box [m]</td><td>(-15.24, -7.62, -68,58) (7.02, 7.62, 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>3.47E+08</td><td>Grid Refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>1.89E+06</td><td>Volume Ratio Max</td><td>8</td><td>Flight Condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td>Rotor Model</td><td>steady</td></tr></table>

# C.2 Residual Overview

The present section shows the residuals for a representative airplane mode, tilt mode and hover mode case in Figure C.7, Figure C.8 and Figure C.9, respectively.

图片摘要：该图主要展示 C.3 Overview of steady simulation parameters。
![](images/f37509e183ce4294663494d6c14c20de1cd269f0fa2c04f8644b623f8aa4f7ae.jpg)  
Figure C.7 Residual overview for representative airplane mode case.

图片摘要：该图主要展示 C.7 Residual overview for representative airplane mode case。
![](images/def74b2b97706da87eb79bc306e7cdc2708e6c29ede7f9da022fa29216262b85.jpg)  
Figure C.8 Residual overview for representative tilt mode case with ${ \tt a p } = 7 5$ .

图片摘要：该图主要展示 C.8 Residual overview for representative tilt mode case with。
![](images/e7b97c86cb8d2910ced7ac9fa1b7a7f49385d865367d317d8b1c66721afe6270.jpg)  
Figure C.9 Residual overview for representative hover mode case.

# C.3 Data Steady XV-15 Rotor Results

The data used in the various plots is tabulated in Table C.4.

Table C.4 Summary of steady RotCFD Validation Data   

<table><tr><td>#</td><td>Flight Mode</td><td>File</td><td>\( a_p \) [deg]</td><td>V/ΩR [m/s]</td><td>\( θ_0 \) [deg]</td><td>TL</td><td>SD</td><td>T [N]</td><td>P [J/s]</td><td>\( C_T / \sigma [-] \)</td><td>\( C_P / \sigma [-] \)</td><td>M [-] or η [-]</td></tr><tr><td>1</td><td>Hover</td><td>0.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>N</td><td>1.467E+04</td><td>2.487E+05</td><td>6.373E-02</td><td>4.790E-03</td><td>0.675</td></tr><tr><td>2</td><td>Hover</td><td>2.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>N</td><td>1.952E+04</td><td>3.483E+05</td><td>8.480E-02</td><td>6.708E-03</td><td>0.741</td></tr><tr><td>3</td><td>Hover</td><td>4.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>N</td><td>2.457E+04</td><td>4.799E+05</td><td>1.067E-01</td><td>9.243E-03</td><td>0.759</td></tr><tr><td>4</td><td>Hover</td><td>6.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>N</td><td>2.972E+04</td><td>6.474E+05</td><td>1.291E-01</td><td>1.247E-02</td><td>0.738</td></tr><tr><td>5</td><td>Hover</td><td>8.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>N</td><td>3.466E+04</td><td>8.578E+05</td><td>1.506E-01</td><td>1.652E-02</td><td>0.710</td></tr><tr><td>6</td><td>Hover</td><td>10.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>N</td><td>3.867E+04</td><td>1.122E+06</td><td>1.680E-01</td><td>2.161E-02</td><td>0.640</td></tr><tr><td>7</td><td>Hover</td><td>0_TL.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>N</td><td>1.450E+04</td><td>2.485E+05</td><td>6.299E-02</td><td>4.786E-03</td><td>0.665</td></tr><tr><td>8</td><td>Hover</td><td>2_TL.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>N</td><td>1.909E+04</td><td>3.464E+05</td><td>8.293E-02</td><td>6.672E-03</td><td>0.718</td></tr><tr><td>9</td><td>Hover</td><td>4_TL.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>N</td><td>2.373E+04</td><td>4.810E+05</td><td>1.031E-01</td><td>9.264E-03</td><td>0.720</td></tr><tr><td>10</td><td>Hover</td><td>6_TL.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>N</td><td>2.844E+04</td><td>6.612E+05</td><td>1.235E-01</td><td>1.273E-02</td><td>0.685</td></tr><tr><td>11</td><td>Hover</td><td>8_TL.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>N</td><td>3.282E+04</td><td>8.967E+05</td><td>1.426E-01</td><td>1.727E-02</td><td>0.678</td></tr><tr><td>12</td><td>Hover</td><td>10_TL.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>N</td><td>3.643E+04</td><td>1.180E+06</td><td>1.583E-01</td><td>2.273E-02</td><td>0.557</td></tr><tr><td>13</td><td>Hover</td><td>0_TL_SD.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>Y</td><td>1.669E+04</td><td>2.906E+05</td><td>7.250E-02</td><td>5.597E-03</td><td>0.703</td></tr><tr><td>14</td><td>Hover</td><td>2_TL_SD.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>Y</td><td>2.183E+04</td><td>4.060E+05</td><td>9.483E-02</td><td>7.819E-03</td><td>0.752</td></tr><tr><td>15</td><td>Hover</td><td>4_TL_SD.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>Y</td><td>2.712E+04</td><td>5.617E+05</td><td>1.178E-01</td><td>1.082E-02</td><td>0.753</td></tr><tr><td>16</td><td>Hover</td><td>6_TL_SD.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>3.245E+04</td><td>7.686E+05</td><td>1.410E-01</td><td>1.480E-02</td><td>0.721</td></tr><tr><td>17</td><td>Hover</td><td>8_TL_SD.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>Y</td><td>3.759E+04</td><td>1.031E+06</td><td>1.633E-01</td><td>1.986E-02</td><td>0.669</td></tr><tr><td>18</td><td>Hover</td><td>10_TL_SD.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>Y</td><td>4.207E+04</td><td>1.338E+06</td><td>1.828E-01</td><td>2.577E-02</td><td>0.609</td></tr><tr><td>19</td><td>Tilt</td><td>15_18_TL.rpr</td><td>15</td><td>0.32</td><td>18.0</td><td>Y</td><td>N</td><td>8.109E+03</td><td>6.146E+05</td><td>3.663E-02</td><td>1.255E-02</td><td>NA</td></tr><tr><td>20</td><td>Tilt</td><td>15_19_TL.rpr</td><td>15</td><td>0.32</td><td>19.0</td><td>Y</td><td>N</td><td>1.208E+04</td><td>9.008E+05</td><td>5.457E-02</td><td>1.840E-02</td><td>NA</td></tr><tr><td>21</td><td>Tilt</td><td>15_20_TL.rpr</td><td>15</td><td>0.32</td><td>20.0</td><td>Y</td><td>N</td><td>1.600E+04</td><td>1.193E+06</td><td>7.227E-02</td><td>2.436E-02</td><td>NA</td></tr><tr><td>22</td><td>Tilt</td><td>15_21_TL.rpr</td><td>15</td><td>0.32</td><td>21.0</td><td>Y</td><td>N</td><td>1.985E+04</td><td>1.496E+06</td><td>8.966E-02</td><td>3.055E-02</td><td>NA</td></tr><tr><td>71</td><td>Tilt</td><td>15_175_TL.rpr</td><td>15</td><td>0.32</td><td>17.5</td><td>Y</td><td>N</td><td>6.133E+03</td><td>4.765E+05</td><td>2.770E-02</td><td>9.731E-03</td><td>NA</td></tr><tr><td>72</td><td>Tilt</td><td>15_185_TL.rpr</td><td>15</td><td>0.32</td><td>18.5</td><td>Y</td><td>N</td><td>1.009E+04</td><td>7.559E+05</td><td>4.558E-02</td><td>1.544E-02</td><td>NA</td></tr><tr><td>23</td><td>Tilt</td><td>30_155_TL.rpr</td><td>30</td><td>0.32</td><td>15.5</td><td>Y</td><td>N</td><td>8.998E+03</td><td>5.399E+05</td><td>4.064E-02</td><td>1.103E-02</td><td>NA</td></tr><tr><td>24</td><td>Tilt</td><td>30_165_TL.rpr</td><td>30</td><td>0.32</td><td>16.5</td><td>Y</td><td>N</td><td>1.289E+04</td><td>7.906E+05</td><td>5.822E-02</td><td>1.615E-02</td><td>NA</td></tr><tr><td>25</td><td>Tilt</td><td>30_175_TL.rpr</td><td>30</td><td>0.32</td><td>17.5</td><td>Y</td><td>N</td><td>1.673E+04</td><td>1.046E+06</td><td>7.557E-02</td><td>2.136E-02</td><td>NA</td></tr><tr><td>26</td><td>Tilt</td><td>30_185_TL.rpr</td><td>30</td><td>0.32</td><td>18.5</td><td>Y</td><td>N</td><td>2.045E+00</td><td>1.312E+06</td><td>9.237E-06</td><td>2.679E-02</td><td>NA</td></tr><tr><td>73</td><td>Tilt</td><td>30_15_TL.rpr</td><td>30</td><td>0.32</td><td>15.0</td><td>Y</td><td>N</td><td>7.030E+03</td><td>4.174E+05</td><td>3.175E-02</td><td>8.524E-03</td><td>NA</td></tr><tr><td>74</td><td>Tilt</td><td>30_16_TL.rpr</td><td>30</td><td>0.32</td><td>16.0</td><td>Y</td><td>N</td><td>1.095E+04</td><td>6.644E+05</td><td>4.946E-02</td><td>1.357E-02</td><td>NA</td></tr><tr><td>27</td><td>Tilt</td><td>60_8_TL.rpr</td><td>60</td><td>0.32</td><td>8.0</td><td>Y</td><td>N</td><td>1.512E+04</td><td>5.360E+05</td><td>6.830E-02</td><td>1.095E-02</td><td>NA</td></tr><tr><td>28</td><td>Tilt</td><td>60_9_TL.rpr</td><td>60</td><td>0.32</td><td>9.0</td><td>Y</td><td>N</td><td>1.865E+04</td><td>6.911E+05</td><td>8.424E-02</td><td>1.411E-02</td><td>NA</td></tr><tr><td>29</td><td>Tilt</td><td>60_10_TL.rpr</td><td>60</td><td>0.32</td><td>10.0</td><td>Y</td><td>N</td><td>2.207E+04</td><td>8.546E+05</td><td>9.969E-02</td><td>1.745E-02</td><td>NA</td></tr><tr><td>30</td><td>Tilt</td><td>60_11_TL.rpr</td><td>60</td><td>0.32</td><td>11.0</td><td>Y</td><td>N</td><td>2.525E+04</td><td>1.027E+06</td><td>1.141E-01</td><td>2.097E-02</td><td>NA</td></tr><tr><td>75</td><td>Tilt</td><td>60_6_TL.rpr</td><td>60</td><td>0.32</td><td>6.0</td><td>Y</td><td>N</td><td>7.823E+03</td><td>2.571E+05</td><td>3.534E-02</td><td>5.250E-03</td><td>NA</td></tr><tr><td>76</td><td>Tilt</td><td>60_7_TL.rpr</td><td>60</td><td>0.32</td><td>7.0</td><td>Y</td><td>N</td><td>1.149E+04</td><td>3.904E+05</td><td>5.190E-02</td><td>7.972E-03</td><td>NA</td></tr><tr><td>31</td><td>Tilt</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>1.374E+04</td><td>3.304E+05</td><td>6.206E-02</td><td>6.747E-03</td><td>NA</td></tr><tr><td>32</td><td>Tilt</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.716E+04</td><td>4.160E+05</td><td>7.751E-02</td><td>8.495E-03</td><td>NA</td></tr><tr><td>33</td><td>Tilt</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>2.041E+04</td><td>5.117E+05</td><td>9.219E-02</td><td>1.045E-02</td><td>NA</td></tr><tr><td>34</td><td>Tilt</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>2.358E+04</td><td>6.180E+05</td><td>1.065E-01</td><td>1.262E-02</td><td>NA</td></tr><tr><td>77</td><td>Tilt</td><td>75_1_TL.rpr</td><td>75</td><td>0.32</td><td>1.0</td><td>Y</td><td>N</td><td>1.030E+04</td><td>2.575E+05</td><td>4.652E-02</td><td>5.258E-03</td><td>NA</td></tr><tr><td>35</td><td>Advance Ratio</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>1.374E+04</td><td>3.304E+05</td><td>6.206E-02</td><td>6.747E-03</td><td>NA</td></tr><tr><td>36</td><td>Advance Ratio</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.716E+04</td><td>4.160E+05</td><td>7.751E-02</td><td>8.495E-03</td><td>NA</td></tr><tr><td>37</td><td>Advance Ratio</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>2.041E+04</td><td>5.117E+05</td><td>9.219E-02</td><td>1.045E-02</td><td>NA</td></tr><tr><td>38</td><td>Advance Ratio</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>2.358E+04</td><td>6.180E+05</td><td>1.065E-01</td><td>1.262E-02</td><td>NA</td></tr><tr><td>81</td><td>Advance Ratio</td><td>75_1_TL.rpr</td><td>75</td><td>0.32</td><td>1.0</td><td>Y</td><td>N</td><td>1.030E+04</td><td>2.575E+05</td><td>4.652E-02</td><td>5.258E-03</td><td>NA</td></tr><tr><td>39</td><td>Advance Ratio</td><td>27_75_2_TL.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.534E+04</td><td>3.345E+05</td><td>6.929E-02</td><td>6.831E-03</td><td>NA</td></tr><tr><td>40</td><td>Advance Ratio</td><td>27_75_3_TL.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>1.857E+04</td><td>4.099E+05</td><td>8.388E-02</td><td>8.371E-03</td><td>NA</td></tr><tr><td>41</td><td>Advance Ratio</td><td>27_75_4_TL.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>2.165E+04</td><td>4.965E+05</td><td>9.779E-02</td><td>1.014E-02</td><td>NA</td></tr><tr><td>82</td><td>Advance Ratio</td><td>27_75_1_TL.rpr</td><td>75</td><td>0.27</td><td>1.0</td><td>Y</td><td>N</td><td>1.209E+04</td><td>2.673E+05</td><td>5.463E-02</td><td>5.459E-03</td><td>NA</td></tr><tr><td>42</td><td>Advance Ratio</td><td>18_75_3_TL.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>2.053E+04</td><td>3.982E+05</td><td>9.273E-02</td><td>8.132E-03</td><td>NA</td></tr><tr><td>43</td><td>Advance Ratio</td><td>18_75_4_TL.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>2.325E+04</td><td>4.704E+05</td><td>1.050E-01</td><td>9.606E-03</td><td>NA</td></tr><tr><td>44</td><td>Advance Ratio</td><td>18_75_5_TL.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>2.596E+04</td><td>5.519E+05</td><td>1.173E-01</td><td>1.127E-02</td><td>NA</td></tr><tr><td>86</td><td>Advance Ratio</td><td>18_75_1_TL.rpr</td><td>75</td><td>0.18</td><td>1.0</td><td>Y</td><td>N</td><td>1.490E+04</td><td>2.792E+05</td><td>6.730E-02</td><td>5.702E-03</td><td>NA</td></tr><tr><td>87</td><td>Advance Ratio</td><td>18_75_2_TL.rpr</td><td>75</td><td>0.18</td><td>2.0</td><td>Y</td><td>N</td><td>1.771E+04</td><td>3.349E+05</td><td>8.000E-02</td><td>6.839E-03</td><td>NA</td></tr><tr><td>45</td><td>Airplane Mode</td><td>40_23_TL.rpr</td><td>0</td><td>0.40</td><td>23.0</td><td>Y</td><td>N</td><td>2.906E+03</td><td>2.762E+05</td><td>1.902E-02</td><td>9.837E-03</td><td>0.777</td></tr><tr><td>46</td><td>Airplane Mode</td><td>40_24_TL.rpr</td><td>0</td><td>0.40</td><td>24.0</td><td>Y</td><td>N</td><td>5.753E+03</td><td>4.902E+05</td><td>3.765E-02</td><td>1.746E-02</td><td>0.866</td></tr><tr><td>47</td><td>Airplane Mode</td><td>40_25_TL.rpr</td><td>0</td><td>0.40</td><td>25.0</td><td>Y</td><td>N</td><td>8.577E+03</td><td>7.101E+05</td><td>5.613E-02</td><td>2.529E-02</td><td>0.892</td></tr><tr><td>48</td><td>Airplane Mode</td><td>40_26_TL.rpr</td><td>0</td><td>0.40</td><td>26.0</td><td>Y</td><td>N</td><td>1.140E+04</td><td>9.343E+05</td><td>7.461E-02</td><td>3.328E-02</td><td>0.901</td></tr><tr><td>78</td><td>Airplane Mode</td><td>40_225_TL.rpr</td><td>0</td><td>0.40</td><td>22.5</td><td>Y</td><td>N</td><td>1.480E+03</td><td>1.706E+05</td><td>9.686E-03</td><td>6.076E-03</td><td>0.640</td></tr><tr><td>79</td><td>Airplane Mode</td><td>40_255_TL.rpr</td><td>0</td><td>0.40</td><td>25.5</td><td>Y</td><td>N</td><td>9.988E+03</td><td>8.215E+05</td><td>6.537E-02</td><td>2.926E-02</td><td>0.898</td></tr><tr><td>49</td><td>Airplane Mode</td><td>70_375_TL.rpr</td><td>0</td><td>0.70</td><td>37.5</td><td>Y</td><td>N</td><td>3.328E+03</td><td>5.535E+05</td><td>2.178E-02</td><td>1.971E-02</td><td>0.777</td></tr><tr><td>50</td><td>Airplane Mode</td><td>70_385_TL.rpr</td><td>0</td><td>0.70</td><td>38.5</td><td>Y</td><td>N</td><td>7.193E+03</td><td>1.054E+06</td><td>4.707E-02</td><td>3.754E-02</td><td>0.882</td></tr><tr><td>51</td><td>Airplane Mode</td><td>70_395_TL.rpr</td><td>0</td><td>0.70</td><td>39.5</td><td>Y</td><td>N</td><td>1.098E+04</td><td>1.559E+06</td><td>7.186E-02</td><td>5.553E-02</td><td>0.910</td></tr><tr><td>52</td><td>Airplane Mode</td><td>70_405_TL.rpr</td><td>0</td><td>0.70</td><td>40.5</td><td>Y</td><td>N</td><td>1.471E+04</td><td>2.073E+06</td><td>9.627E-02</td><td>7.383E-02</td><td>0.917</td></tr><tr><td>80</td><td>Airplane Mode</td><td>70_37_TL.rpr</td><td>0</td><td>0.70</td><td>37.0</td><td>Y</td><td>N</td><td>1.369E+03</td><td>3.036E+05</td><td>6.184E-03</td><td>6.200E-03</td><td>0.583</td></tr><tr><td>53</td><td>Hover</td><td>6_TL_SD_GC.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>54</td><td>Hover</td><td>6_TL_SD_GE.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>55</td><td>Hover</td><td>6_TL_SD_IR.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>56</td><td>Hover</td><td>10_TL_SD_IR2.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>57</td><td>Advance Ratio</td><td>27_75_2_TL_SD.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.812E+04</td><td>3.915E+05</td><td>8.185E-02</td><td>7.995E-03</td><td>NA</td></tr><tr><td>58</td><td>Advance Ratio</td><td>27_75_3_TL_SD.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>2.173E+04</td><td>4.780E+05</td><td>9.815E-02</td><td>9.761E-03</td><td>NA</td></tr><tr><td>59</td><td>Advance Ratio</td><td>27_75_4_TL_SD.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>2.530E+04</td><td>5.765E+05</td><td>1.143E-01</td><td>1.177E-02</td><td>NA</td></tr><tr><td>88</td><td>Advance Ratio</td><td>27_75_1_TL_SD.rpr</td><td>75</td><td>0.27</td><td>1.0</td><td>Y</td><td>N</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>87</td><td>Advance Ratio</td><td>27_75_0_TL_SD.rpr</td><td>75</td><td>0.27</td><td>0.0</td><td>Y</td><td>N</td><td>1.089E+04</td><td>2.507E+05</td><td>4.919E-02</td><td>5.120E-03</td><td>NA</td></tr><tr><td>61</td><td>Advance Ratio</td><td>18_75_3_TL_SD.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>2.368E+04</td><td>4.659E+05</td><td>1.070E-01</td><td>9.514E-03</td><td>NA</td></tr><tr><td>62</td><td>Advance Ratio</td><td>18_75_4_TL_SD.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>2.681E+04</td><td>5.488E+05</td><td>1.211E-01</td><td>1.121E-02</td><td>NA</td></tr><tr><td>63</td><td>Advance Ratio</td><td>18_75_5_TL_SD.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>2.988E+04</td><td>6.429E+05</td><td>1.350E-01</td><td>1.313E-02</td><td>NA</td></tr><tr><td>83</td><td>Advance Ratio</td><td>18_75_1_TL_SD.rpr</td><td>75</td><td>0.18</td><td>1.0</td><td>Y</td><td>N</td><td>1.733E+04</td><td>3.264E+05</td><td>7.828E-02</td><td>6.666E-03</td><td>NA</td></tr><tr><td>84</td><td>Advance Ratio</td><td>18_75_2_TL_SD.rpr</td><td>75</td><td>0.18</td><td>2.0</td><td>Y</td><td>N</td><td>2.049E+04</td><td>3.915E+05</td><td>9.255E-02</td><td>7.995E-03</td><td>NA</td></tr><tr><td>85</td><td>Advance Ratio</td><td>18_75_3_TL_SD.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>2.368E+04</td><td>4.659E+05</td><td>1.070E-01</td><td>9.514E-03</td><td>NA</td></tr><tr><td>86</td><td>Advance Ratio</td><td>18_75_0_TL_SD.rpr</td><td>75</td><td>0.18</td><td>0.0</td><td>Y</td><td>N</td><td>1.415E+04</td><td>2.704E+05</td><td>6.392E-02</td><td>5.522E-03</td><td>NA</td></tr><tr><td>64</td><td>Hover</td><td>10_SD.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>Y</td><td>4.447E+04</td><td>1.291E+06</td><td>1.932E-01</td><td>2.486E-02</td><td>0.688</td></tr><tr><td>65</td><td>Hover</td><td>0_SD.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>Y</td><td>1.682E+04</td><td>2.903E+05</td><td>7.307E-02</td><td>5.591E-03</td><td>0.711</td></tr><tr><td>66</td><td>Hover</td><td>2_SD.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>Y</td><td>2.237E+04</td><td>4.075E+05</td><td>9.718E-02</td><td>7.848E-03</td><td>0.773</td></tr><tr><td>67</td><td>Hover</td><td>4_SD.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>Y</td><td>2.800E+04</td><td>5.617E+05</td><td>1.216E-01</td><td>1.082E-02</td><td>0.790</td></tr><tr><td>68</td><td>Hover</td><td>6_SD.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>Y</td><td>3.391E+04</td><td>7.559E+05</td><td>1.473E-01</td><td>1.456E-02</td><td>0.781</td></tr><tr><td>69</td><td>Hover</td><td>8_SD.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>Y</td><td>3.962E+04</td><td>9.945E+05</td><td>1.721E-01</td><td>1.915E-02</td><td>0.749</td></tr><tr><td>89</td><td>Tilt</td><td>15_18.rpr</td><td>15</td><td>0.32</td><td>18.0</td><td>N</td><td>N</td><td>8.523E+03</td><td>6.435E+05</td><td>3.850E-02</td><td>1.314E-02</td><td>NA</td></tr><tr><td>90</td><td>Tilt</td><td>75_3.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>N</td><td>N</td><td>1.705E+04</td><td>4.130E+05</td><td>7.701E-02</td><td>8.434E-03</td><td>NA</td></tr><tr><td>91</td><td>Advance Ratio</td><td>18_75_3_rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>N</td><td>N</td><td>2.075E+04</td><td>3.998E+05</td><td>9.373E-02</td><td>8.164E-03</td><td>NA</td></tr><tr><td>92</td><td>Airplane Mode</td><td>40_24.rpr</td><td>0</td><td>0.40</td><td>24.0</td><td>N</td><td>N</td><td>6.246E+03</td><td>5.274E+05</td><td>4.088E-02</td><td>1.878E-02</td><td>0.874</td></tr></table>

# Appendix DUnsteady XV-15 Rotor Validation Results

# D.1 Simulations Parameters

Table D.5 shows a compact overview of the simulation parameters. ND stands for non-dimensionalized, the boundary size is expressed as the coordinates of the corners of a rectangular prism. The grid cells indicate the amount of cells on the x,y and z edge of the boundary, respectively. Rotor Grid Ref. and Grid Refinement indicate refinement of cells by multiplying the amount of cells by a certain factor.

Table D.5 Overview of steady simulation parameters.   

<table><tr><td colspan="2">Hover Parameters</td><td colspan="2">Boundary Conditions &amp; Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary Size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.1)</td><td>Simulated time</td><td>2.5 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells [#]</td><td>30,30,42</td><td>Timesteps</td><td>3000</td></tr><tr><td>Tip speed</td><td>225.55 m/s</td><td>Rotor Box Ref.</td><td>1,1</td><td>ΔT</td><td>8.33E-04</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor Grid Ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid Refinement Box [m]</td><td>(-7.62, -7.62, -68.58) (7.62, 7.62, 38.1)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.41E+08</td><td>Grid Refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.84E+06</td><td>Volume Ratio Max</td><td>8</td><td>Flight Condition</td><td>hover</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td>Rotor Model</td><td></td></tr><tr><td colspan="2">Tilt and Advance Ratio</td><td colspan="2">Boundary Conditions &amp; Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary Size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells [#]</td><td>30,30,42</td><td>Timesteps</td><td>1000</td></tr><tr><td>Tip speed</td><td>221.17 m/s</td><td>Rotor Box Ref.</td><td>1,1</td><td>ΔT</td><td>8.33E-04</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor Grid Ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid Refinement Box [m]</td><td>(-15.24, -7.62, -68,58) (7.62, 7.62 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.05E+08</td><td>Grid Refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.73E+06</td><td>Volume Ratio Max</td><td>8</td><td>Flight Condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>2,029,692 (at 30 degree tilt)</td><td></td><td></td></tr><tr><td colspan="2">Airplane Mode</td><td colspan="2">Boundary Conditions &amp; Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary Size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells [#]</td><td>30,30,42</td><td>Timesteps</td><td>1000</td></tr><tr><td>Tip speed</td><td>183.76 m/s</td><td>Rotor Box Ref.</td><td>1,1</td><td>ΔT</td><td>8.33E-04</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor Grid Ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid Refinement Box [m]</td><td>(-15.24, -7.62, -68,58) (7.52, 7.62 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>3.47E+08</td><td>Grid Refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>1.89E+06</td><td>Volume Ratio Max</td><td>8</td><td>Flight Condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td></td><td></td></tr></table>

# D.2 Hover - Unsteady

图片摘要：该图主要展示 D.5 Overview of steady simulation parameters。
![](images/5e21fd5bd349e67ce2e407f0c80fdcf4922dabed7a24d5889afb257f5283b4c0.jpg)  
Figure D.10 and Figure D.11 show, analogous to the steady results obtained in Section 4.1, the hover performance for the unsteady model of the XV-15 rotor in RotUNS.   
Figure D.10 Unsteady results for XV-15 rotor hover power as a function of thrust [2], [28].

Both graphs show serious error in excess of $1 0 \%$ , compared to the presented theoretical and experimental data.

图片摘要：该图主要展示 D.10 Unsteady results for XV 15 rotor hover power as a funct。
![](images/4b60c9621b542ef0f87526bc34531eafe848fe5b421b94726e122001ecbaeeb3.jpg)  
Figure D.11 Unsteady results for XV-15 rotor hover figure of Merit as a function of thrust [2], [28].

# D.3 Tilt Mode - Unsteady

Figure D.12 and Figure D.13 show, analogous to the steady results obtained in Section 4.2, the tilt mode performance and the sensitivity to advance ratio variations for the unsteady model of the XV-15 rotor in RotUNS.

图片摘要：该图主要展示 D.12 and Figure D.13 show, analogous to the steady results o。
![](images/9895ec50f211dc36f5f16ef638279952be502152cedba9e6738dc7fc19142a46.jpg)  
Figure D.12 Unsteady results for XV-15 rotor power as a function of thrust for various pylon angles at V/ΩR $=$ .32 [2].

The results for the various tilt modes correlate slightly better than the hover performance, the steady model, however, outperforms the unsteady model in terms of accuracy.

图片摘要：该图主要展示 D.12 Unsteady results for XV 15 rotor power as a function of。
![](images/a119bef8e0bc9024a212d9c66420976276414f253788b3dfd8684bf2e3c1f334.jpg)  
Figure D.13 Unsteady results for XV-15 rotor power as function of thrust, for $\mathtt { a } _ { \mathsf { p } } = 7 5 ^ { \circ }$ and $\mathsf { M } _ { \mathrm { t i p } } = 0 . 6 5$ [2].

The variation of advance ratio shows similar performance to CAMRAD I.

# D.4 Airplane Mode - Unsteady

图片摘要：该图主要展示 D.13 Unsteady results for XV 15 rotor power as function of t。
![](images/27ea4d2031778b39a57c33ee2b0fedae320b79e44d8a5a1e3845d47bfdcc0c2a.jpg)  
Figure D.14 shows, analogous to the steady results obtained in Section 4.3, airplane mode performance for the unsteady model of the XV-15 rotor in RotUNS.   
Figure D.14 Unsteady results for (rotor) propulsive efficiency as function of thrust [2].

# D.5 Data Unsteady XV-15 Rotor Results

The data used in the various plots is tabulated in Table D.6.

Table D.6 Summary of unsteady RotCFD Validation Data.   

<table><tr><td>#</td><td>Flight Mode</td><td>File</td><td>\(a_p\) [deg]</td><td>V/ΩR [m/s]</td><td>\(θ_0\) [deg]</td><td>TL</td><td>SD</td><td>T [N]</td><td>P [J/s]</td><td>\(C_T/\sigma [-]\)</td><td>\(C_P/\sigma [-]\)</td><td>M [-] or η [-]</td></tr><tr><td>1</td><td>Hover</td><td>0.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>N</td><td>1.100E+04</td><td>2.170E+05</td><td>4.778E-02</td><td>4.179E-03</td><td>0.505</td></tr><tr><td>2</td><td>Hover</td><td>2.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>N</td><td>1.460E+04</td><td>3.020E+05</td><td>6.342E-02</td><td>5.816E-03</td><td>0.552</td></tr><tr><td>3</td><td>Hover</td><td>4.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>N</td><td>1.820E+04</td><td>4.130E+05</td><td>7.906E-02</td><td>7.954E-03</td><td>0.562</td></tr><tr><td>4</td><td>Hover</td><td>6.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>N</td><td>2.170E+04</td><td>5.510E+05</td><td>9.427E-02</td><td>1.061E-02</td><td>0.552</td></tr><tr><td>5</td><td>Hover</td><td>8.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>N</td><td>2.500E+04</td><td>7.170E+05</td><td>1.086E-01</td><td>1.381E-02</td><td>0.524</td></tr><tr><td>6</td><td>Hover</td><td>10.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>N</td><td>2.800E+04</td><td>9.080E+05</td><td>1.216E-01</td><td>1.749E-02</td><td>0.489</td></tr><tr><td>7</td><td>Hover</td><td>0_SL_rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>N</td><td>1.070E+04</td><td>2.160E+05</td><td>4.648E-02</td><td>4.160E-03</td><td>0.481</td></tr><tr><td>8</td><td>Hover</td><td>2_SL_rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>N</td><td>1.400E+04</td><td>3.000E+05</td><td>6.082E-02</td><td>5.778E-03</td><td>0.526</td></tr><tr><td>9</td><td>Hover</td><td>4_SL_rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>N</td><td>1.730E+04</td><td>4.070E+05</td><td>7.515E-02</td><td>7.839E-03</td><td>0.531</td></tr><tr><td>10</td><td>Hover</td><td>6_SL_rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>N</td><td>2.040E+04</td><td>5.410E+05</td><td>8.862E-02</td><td>1.042E-02</td><td>0.513</td></tr><tr><td>11</td><td>Hover</td><td>8_SL_rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>N</td><td>2.350E+04</td><td>7.100E+05</td><td>1.021E-01</td><td>1.367E-02</td><td>0.483</td></tr><tr><td>12</td><td>Hover</td><td>10_SL_rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>N</td><td>2.620E+04</td><td>9.070E+05</td><td>1.138E-01</td><td>1.747E-02</td><td>0.442</td></tr><tr><td>13</td><td>Hover</td><td>0_SL_SD_rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>Y</td><td>1.270E+04</td><td>2.540E+05</td><td>5.517E-02</td><td>4.892E-03</td><td>0.545</td></tr><tr><td>14</td><td>Hover</td><td>2_SL_SD_rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>Y</td><td>1.698E+04</td><td>3.492E+05</td><td>7.375E-02</td><td>6.726E-03</td><td>0.584</td></tr><tr><td>15</td><td>Hover</td><td>4_SL_SD_rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>Y</td><td>2.020E+04</td><td>4.750E+05</td><td>8.775E-02</td><td>9.148E-03</td><td>0.573</td></tr><tr><td>16</td><td>Hover</td><td>6_SL_SD_rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.390E+04</td><td>6.310E+05</td><td>1.038E-01</td><td>1.215E-02</td><td>0.554</td></tr><tr><td>17</td><td>Hover</td><td>8_SL_SD_rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>Y</td><td>2.730E+04</td><td>8.170E+05</td><td>1.186E-01</td><td>1.574E-02</td><td>0.520</td></tr><tr><td>18</td><td>Hover</td><td>10_SL_SD_rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>Y</td><td>3.040E+04</td><td>1.040E+06</td><td>1.321E-01</td><td>2.003E-02</td><td>0.480</td></tr><tr><td>19</td><td>Tilt</td><td>15_18_TL.rpr</td><td>15</td><td>0.32</td><td>18.0</td><td>Y</td><td>N</td><td>4.660E+03</td><td>3.970E+05</td><td>2.105E-02</td><td>8.107E-03</td><td>NA</td></tr><tr><td>20</td><td>Tilt</td><td>15_19_TL.rpr</td><td>15</td><td>0.32</td><td>19.0</td><td>Y</td><td>N</td><td>7.020E+03</td><td>5.770E+05</td><td>3.171E-02</td><td>1.178E-02</td><td>NA</td></tr><tr><td>21</td><td>Tilt</td><td>15_20_TL.rpr</td><td>15</td><td>0.32</td><td>20.0</td><td>Y</td><td>N</td><td>9.390E+03</td><td>7.670E+05</td><td>4.241E-02</td><td>1.566E-02</td><td>NA</td></tr><tr><td>22</td><td>Tilt</td><td>15_21_TL.rpr</td><td>15</td><td>0.32</td><td>21.0</td><td>Y</td><td>N</td><td>1.160E+04</td><td>9.610E+05</td><td>5.240E-02</td><td>1.962E-02</td><td>NA</td></tr><tr><td>23</td><td>Tilt</td><td>30_155_TL.rpr</td><td>30</td><td>0.32</td><td>15.5</td><td>Y</td><td>N</td><td>4.918E+03</td><td>3.443E+05</td><td>2.221E-02</td><td>7.031E-03</td><td>NA</td></tr><tr><td>24</td><td>Tilt</td><td>30_165_TL.rpr</td><td>30</td><td>0.32</td><td>16.5</td><td>Y</td><td>N</td><td>7.218E+03</td><td>5.011E+05</td><td>3.260E-02</td><td>1.023E-02</td><td>NA</td></tr><tr><td>25</td><td>Tilt</td><td>30_175_TL.rpr</td><td>30</td><td>0.32</td><td>17.5</td><td>Y</td><td>N</td><td>9.489E+03</td><td>6.648E+05</td><td>4.286E-02</td><td>1.358E-02</td><td>NA</td></tr><tr><td>26</td><td>Tilt</td><td>30_185_TL.rpr</td><td>30</td><td>0.32</td><td>18.5</td><td>Y</td><td>N</td><td>1.175E+04</td><td>8.360E+05</td><td>5.307E-02</td><td>1.707E-02</td><td>NA</td></tr><tr><td>27</td><td>Tilt</td><td>60_8_TL.rpr</td><td>60</td><td>0.32</td><td>8.0</td><td>Y</td><td>N</td><td>8.855E+03</td><td>3.655E+05</td><td>4.000E-02</td><td>7.463E-03</td><td>NA</td></tr><tr><td>28</td><td>Tilt</td><td>60_9_TL.rpr</td><td>60</td><td>0.32</td><td>9.0</td><td>Y</td><td>N</td><td>1.104E+04</td><td>4.647E+05</td><td>4.985E-02</td><td>9.489E-03</td><td>NA</td></tr><tr><td>29</td><td>Tilt</td><td>60_10_TL.rpr</td><td>60</td><td>0.32</td><td>10.0</td><td>Y</td><td>N</td><td>1.316E+04</td><td>5.738E+05</td><td>5.944E-02</td><td>1.172E-02</td><td>NA</td></tr><tr><td>30</td><td>Tilt</td><td>60_11_TL.rpr</td><td>60</td><td>0.32</td><td>11.0</td><td>Y</td><td>N</td><td>1.524E+04</td><td>6.855E+05</td><td>6.884E-02</td><td>1.400E-02</td><td>NA</td></tr><tr><td>31</td><td>Tilt</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>8.970E+03</td><td>2.660E+05</td><td>4.052E-02</td><td>5.432E-03</td><td>NA</td></tr><tr><td>32</td><td>Tilt</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.120E+04</td><td>3.250E+05</td><td>5.059E-02</td><td>6.637E-03</td><td>NA</td></tr><tr><td>33</td><td>Tilt</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>1.330E+04</td><td>3.920E+05</td><td>6.008E-02</td><td>8.005E-03</td><td>NA</td></tr><tr><td>34</td><td>Tilt</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>1.543E+04</td><td>4.673E+05</td><td>6.970E-02</td><td>9.544E-03</td><td>NA</td></tr><tr><td>35</td><td>Advance Ratio</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>8.970E+03</td><td>2.660E+05</td><td>4.052E-02</td><td>5.432E-03</td><td>NA</td></tr><tr><td>36</td><td>Advance Ratio</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.120E+04</td><td>3.250E+05</td><td>5.059E-02</td><td>6.637E-03</td><td>NA</td></tr><tr><td>37</td><td>Advance Ratio</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>1.330E+04</td><td>3.920E+05</td><td>6.008E-02</td><td>8.005E-03</td><td>NA</td></tr><tr><td>38</td><td>Advance Ratio</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>1.543E+04</td><td>4.673E+05</td><td>6.970E-02</td><td>9.544E-03</td><td>NA</td></tr><tr><td>39</td><td>Advance Ratio</td><td>27_75_2_TL.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.007E+04</td><td>2.710E+05</td><td>4.548E-02</td><td>5.533E-03</td><td>NA</td></tr><tr><td>40</td><td>Advance Ratio</td><td>27_75_3_TL.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>1.220E+04</td><td>3.260E+05</td><td>5.511E-02</td><td>6.657E-03</td><td>NA</td></tr><tr><td>41</td><td>Advance Ratio</td><td>27_75_4_TL.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>1.424E+04</td><td>3.911E+05</td><td>6.431E-02</td><td>7.987E-03</td><td>NA</td></tr><tr><td>42</td><td>Advance Ratio</td><td>18_75_3_TL.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>1.390E+04</td><td>3.330E+05</td><td>6.279E-02</td><td>6.800E-03</td><td>NA</td></tr><tr><td>43</td><td>Advance Ratio</td><td>18_75_4_TL.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>1.577E+04</td><td>3.913E+05</td><td>7.123E-02</td><td>7.991E-03</td><td>NA</td></tr><tr><td>44</td><td>Advance Ratio</td><td>18_75_5_TL.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>1.760E+04</td><td>4.560E+05</td><td>7.950E-02</td><td>9.312E-03</td><td>NA</td></tr><tr><td>45</td><td>Airplane Mode</td><td>40_23_TL.rpr</td><td>0</td><td>0.40</td><td>23.0</td><td>Y</td><td>N</td><td>1.404E+03</td><td>1.670E+05</td><td>6.341E-03</td><td>3.410E-03</td><td>0.621</td></tr><tr><td>46</td><td>Airplane Mode</td><td>40_24_TL.rpr</td><td>0</td><td>0.40</td><td>24.0</td><td>Y</td><td>N</td><td>3.128E+03</td><td>3.016E+05</td><td>1.413E-02</td><td>6.159E-03</td><td>0.766</td></tr><tr><td>47</td><td>Airplane Mode</td><td>40_25_TL.rpr</td><td>0</td><td>0.40</td><td>25.0</td><td>Y</td><td>N</td><td>4.820E+03</td><td>4.385E+05</td><td>2.177E-02</td><td>8.955E-03</td><td>0.811</td></tr><tr><td>48</td><td>Airplane Mode</td><td>40_26_TL.rpr</td><td>0</td><td>0.40</td><td>26.0</td><td>Y</td><td>N</td><td>6.478E+03</td><td>5.794E+05</td><td>2.926E-02</td><td>1.183E-02</td><td>0.825</td></tr><tr><td>49</td><td>Airplane Mode</td><td>70_375_TL.rpr</td><td>0</td><td>0.70</td><td>37.5</td><td>Y</td><td>N</td><td>1.397E+03</td><td>3.099E+05</td><td>6.308E-03</td><td>6.329E-03</td><td>0.582</td></tr><tr><td>50</td><td>Airplane Mode</td><td>70_385_TL.rpr</td><td>0</td><td>0.70</td><td>38.5</td><td>Y</td><td>N</td><td>3.607E+03</td><td>6.043E+05</td><td>1.629E-02</td><td>1.234E-02</td><td>0.771</td></tr><tr><td>51</td><td>Airplane Mode</td><td>70_395_TL.rpr</td><td>0</td><td>0.70</td><td>39.5</td><td>Y</td><td>N</td><td>5.737E+03</td><td>9.014E+05</td><td>2.591E-02</td><td>1.841E-02</td><td>0.822</td></tr><tr><td>52</td><td>Airplane Mode</td><td>70_405_TL.rpr</td><td>0</td><td>0.70</td><td>40.5</td><td>Y</td><td>N</td><td>7.800E+03</td><td>1.200E+06</td><td>3.523E-02</td><td>2.451E-02</td><td>0.840</td></tr><tr><td>53</td><td>Hover</td><td>6_TL_SD_GC.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.390E+04</td><td>6.159E+05</td><td>1.038E-01</td><td>1.186E-02</td><td></td></tr><tr><td>54</td><td>Hover</td><td>6_TL_SD_GE.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.390E+04</td><td>6.300E+05</td><td>1.038E-01</td><td>1.213E-02</td><td>0.552</td></tr><tr><td>55</td><td>Hover</td><td>6_TL_SD_IR.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.359E+04</td><td>6.299E+05</td><td>1.025E-01</td><td>1.213E-02</td><td>0.545</td></tr><tr><td>56</td><td>Hover</td><td>10_TL_SD_IR2.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.980E+04</td><td>1.030E+06</td><td>1.295E-01</td><td>1.984E-02</td><td>0.472</td></tr><tr><td>58</td><td>Advance Ratio</td><td>27_75_2_TL_SD.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.202E+04</td><td>3.146E+05</td><td>5.428E-02</td><td>6.425E-03</td><td>NA</td></tr><tr><td>59</td><td>Advance Ratio</td><td>27_75_3_TL_SD.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>1.435E+04</td><td>3.789E+05</td><td>6.482E-02</td><td>7.738E-03</td><td>NA</td></tr><tr><td>60</td><td>Advance Ratio</td><td>27_75_4_TL_SD.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>1.669E+04</td><td>4.516E+05</td><td>7.539E-02</td><td>9.222E-03</td><td>NA</td></tr><tr><td>61</td><td>Advance Ratio</td><td>18_75_3_TL_SD.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>1.619E+04</td><td>3.868E+05</td><td>7.313E-02</td><td>7.899E-03</td><td>NA</td></tr><tr><td>62</td><td>Advance Ratio</td><td>18_75_4_TL_SD.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>1.832E+04</td><td>4.538E+05</td><td>8.275E-02</td><td>9.267E-03</td><td>NA</td></tr><tr><td>63</td><td>Advance Ratio</td><td>18_75_5_TL_SD.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>2.037E+04</td><td>5.276E+05</td><td>9.201E-02</td><td>1.077E-02</td><td>NA</td></tr><tr><td>64</td><td>Hover</td><td>10_SD.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>Y</td><td>3.267E+04</td><td>1.044E+06</td><td>1.419E-01</td><td>2.010E-02</td><td>0.526</td></tr><tr><td>65</td><td>Hover</td><td>0_SD.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>Y</td><td>1.278E+04</td><td>2.525E+05</td><td>5.552E-02</td><td>4.863E-03</td><td>0.526</td></tr><tr><td>66</td><td>Hover</td><td>2_SD.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>Y</td><td>1.696E+04</td><td>3.515E+05</td><td>7.368E-02</td><td>6.769E-03</td><td>0.608</td></tr><tr><td>67</td><td>Hover</td><td>4_SD.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>Y</td><td>2.118E+04</td><td>4.801E+05</td><td>9.201E-02</td><td>9.246E-03</td><td>0.601</td></tr><tr><td>68</td><td>Hover</td><td>6_SD.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>Y</td><td>2.512E+04</td><td>6.389E+05</td><td>1.091E-01</td><td>1.231E-02</td><td>0.593</td></tr><tr><td>69</td><td>Hover</td><td>8_SD.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>Y</td><td>2.903E+04</td><td>8.273E+05</td><td>1.261E-01</td><td>1.593E-02</td><td>0.563</td></tr></table>

# Appendix E Wind Tunnel Case Plots

Each of the wind tunnel subsets would have at least a couple of interesting velocity or vector plots to show, however, since a total of 28 subsets have been processed this would pose too much images in this Appendix. Therefore only a selection of view per subset is presented here. The used coordinate system in the NFAC wind tunnels is shown in Figure E.15. The TTR will always rotate for the thrust to be (partially) aligned with the positive y-axis.

图片摘要：该图主要展示 D.6 Summary of unsteady RotCFD Validation Data。
![](images/40d25e7a1e17d358c71dffee69c191568db7f73f39fe59d233a4fca012bb054d.jpg)

图片摘要：该图主要展示 E.15 The boundaries of the extended test sections with TTR i。
![](images/cb337403285d37b6ea68c74394320874ed502fcc6c7c9669732062fa35560444.jpg)  
Figure E.15 The boundaries of the extended test sections with TTR in edgewise and axial mode, respectively.

# E.1 80- by 120-Foot Wind Tunnel Cases

# E.1.1 Case 1, Edgewise, 0 kts.

图片摘要：该图主要展示 E.15 The boundaries of the extended test sections with TTR i。
![](images/db0e1fe48ad0fefeb796bd3b08829bf1deb4bab85c47fa68c77a45e6879cdcfc.jpg)  
Figure E.16 Case 1, WTGE, ZY-plane.

图片摘要：该图主要展示 E.16 Case 1, WTGE, ZY plane。
![](images/444918c087e4b045c27545b34b06b191a3f1ed789896f3d7f224238c6bd13925.jpg)  
Figure E.17 Case 1, WTRO, ZY-plane.

图片摘要：该图主要展示 E.17 Case 1, WTRO, ZY plane。
![](images/ad4ffac563b42dfa1b3f6e5073c76644dabe5f27c9ea52e2651b2af9dc24be8c.jpg)  
Figure E.16 and Figure E.17 show a velocity plot (with pressure plot on the geometry) of the ZY-plane of case 1 for WTGE and WTRO, respectively. Figure E.18 serves as the legend for the plots of case 1, all units are SI.   
Figure E.18 Legend for pressure and velocities for case 1.

# E.1.2 Case 2, Edgewise, 10 kts.

图片摘要：该图主要展示 E.18 Legend for pressure and velocities for case 1。
![](images/1f423c23be64e80ee2ee143386da0be166e26a30754d1ef73bf44e455794df74.jpg)  
Figure E.19 Case 2, FFGE, XY-plane.

图片摘要：该图主要展示 E.19 Case 2, FFGE, XY plane。
![](images/c98c64cf69165fdf29b43857009452401af3adb0e320ab80e0a6757f8fab0580.jpg)  
Figure E.20 Case 2, WTGE, XY-plane.

图片摘要：该图主要展示 E.20 Case 2, WTGE, XY plane。
![](images/b1dd0a45e20ec488b7d6c113eeebfea12d5eab4a2e834e864af28b3635e33678.jpg)  
Figure E.19 and Figure E.20 show a velocity plot (with pressure plot on the geometry) of the XY-plane of case 2 for FFGE and WTGE, respectively. Figure E.21 serves as the legend for the plots of case 2.   
Figure E.21 Legend for pressure and velocities for case 2.

# E.1.3 Case 3, Axial, 100 kts.

图片摘要：该图主要展示 E.21 Legend for pressure and velocities for case 2。
![](images/d51f60b6a5a3cf96933ad069a174b9200f8d4fa8ce496b070759577392685850.jpg)  
Figure E.22 Case 3, WTGE, XZ-plane.

图片摘要：该图主要展示 E.22 Case 3, WTGE, XZ plane。
![](images/9b9604a5f34fd1e6bc2a7bd6be11e19aeca540d365c6d720097fd52c2dca190b.jpg)  
Figure E.23 Case 3, WTRO, XZ-plane.

图片摘要：该图主要展示 E.23 Case 3, WTRO, XZ plane。
![](images/6c3ae2c4477588cf239ec1db9ec4dffe69ee0f7bceed08b4d0ddd6c9010b3e48.jpg)  
Figure E.22 and Figure E.23 show a velocity plot (with pressure plot on the geometry) of the ZY-plane of case 3 for WTGE and WTRO, respectively. Figure E.24 serves as the legend for the plots of case 3.   
Figure E.24 Legend for pressure and velocities for case 3.

# E.2 40- by 80-Foot Wind Tunnel Cases

# E.2.1 Case 5, Edgewise, 100 kts.

图片摘要：该图主要展示 E.24 Legend for pressure and velocities for case 3。
![](images/9c413f77a040786b464d7cdd2f84b767c755fc88e0d544da5a7c64f9484cab49.jpg)  
Figure E.25 Case 5, FFGE, XY-plane.

图片摘要：该图主要展示 E.25 Case 5, FFGE, XY plane。
![](images/25a0cef9a1cefbe2ddaf116c45ebb8326ceace220e86a087dac47ddb63973c59.jpg)  
Figure E.26 Case 5, WTGE, XY-plane.

图片摘要：该图主要展示 E.26 Case 5, WTGE, XY plane。
![](images/102dae7d97501443c16edfa24b86031b2e2bf8ef2870184d6fec75788cabc880.jpg)  
Figure E.25 and Figure E.26 show a velocity plot (with pressure plot on the geometry) of the XY-plane of case 5 for FFGE and WTGE, respectively. Figure E.27 serves as the legend for the plots of case 5.   
Figure E.27 Legend for pressure and velocities for case 5.

# E.2.2 Case 6, Axial, 200 kts.

图片摘要：该图主要展示 E.27 Legend for pressure and velocities for case 5。
![](images/96332dff38cedccd9b6a201d3205f3d19bce27b442f86592fa67ae35a977dfe7.jpg)  
Figure E.28 Case 6, FFGE, XY-plane.

图片摘要：该图主要展示 E.28 Case 6, FFGE, XY plane。
![](images/9fe8be69cdda85932cffca1bc9f0992992c165633081b922d2e376650d1bd6dc.jpg)  
Figure E.29 Case 6, WTGE, XY-plane.

图片摘要：该图主要展示 E.29 Case 6, WTGE, XY plane。
![](images/f49b316821672d4ea1da55cd1d713e7ec67452ddfef6c30ca899d946e41fbae7.jpg)  
Figure E.28 and Figure E.29 show a velocity plot (with pressure plot on the geometry) of the XY-plane of case 6 for FFGE and WTGE, respectively. Figure E.30 serves as the legend for the plots of case 6.   
Figure E.30 Legend for pressure and velocities for case 6.

# E.2.3 Case 7, Tilt, 100 kts.

图片摘要：该图主要展示 E.30 Legend for pressure and velocities for case 6。
![](images/f6633229ad4c327426169789a14ff3ed1daeda4b193833207b62a0d68ce5e7e9.jpg)  
Figure E.31 Case 7, WTGE, XY-plane.

图片摘要：该图主要展示 E.31 Case 7, WTGE, XY plane。
![](images/2e353a7f0cb8cb8eb32c39a46d973f8c7adde4bc4a4f84d9e0d915854063b4d5.jpg)  
Figure E.32 Case 7, WTRO, XY-plane.

图片摘要：该图主要展示 E.32 Case 7, WTRO, XY plane。
![](images/887a003a2a1df5d5dcc52df4ccf293ab9416939acc551e3050410c4f03d35b95.jpg)  
Figure E.31 and Figure E.32 show a velocity plot (with pressure plot on the geometry) of the XY-plane of case 7 for WTGE and WTRO, respectively. Figure E.33 serves as the legend for the plots of case 7. The grid at the walls of the 40-by 80-Foot Wind Tunnel shows problems with gridding clearly, as shown in Figure E.34.   
Figure E.33 Legend for pressure and velocities for case 7.

图片摘要：该图主要展示 E.33 Legend for pressure and velocities for case 7。
![](images/33698304583692ca75f50604b5f92a1153553221b4eb95819239ece7c9df72dc.jpg)  
Figure E.34 ZY-plane of case 7, just behind the rotor plane.
