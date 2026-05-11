# Wind Tunnel Interference Effects on Tiltrotor Testing Using Computational Fluid Dynamics

Witold J. F. Koning

Ames Research Center, Moffett Field, California

# NASA STI Program ... in Profile

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA scientific and technical information (STI) program plays a key part in helping NASA maintain this important role.

The NASA STI program operates under the auspices of the Agency Chief Information Officer. It collects, organizes, provides for archiving, and disseminates NASA’s STI. The NASA STI program provides access to the NTRS Registered and its public interface, the NASA Technical Reports Server, thus providing one of the largest collections of aeronautical and space science STI in the world. Results are published in both non-NASA channels and by NASA in the NASA STI Report Series, which includes the following report types:

TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA Programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counterpart of peerreviewed formal professional papers but has less stringent limitations on manuscript length and extent of graphic presentations.   
TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., quick release reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.   
CONTRACTOR REPORT. Scientific and technical findings by NASA-sponsored contractors and grantees.

CONFERENCE PUBLICATION. Collected papers from scientific and technical conferences, symposia, seminars, or other meetings sponsored or cosponsored by NASA.   
SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
TECHNICAL TRANSLATION. English-language translations of foreign scientific and technical material pertinent to NASA’s mission.

Specialized services also include organizing and publishing research results, distributing specialized research announcements and feeds, providing information desk and personal search support, and enabling data exchange services.

For more information about the NASA STI program, see the following:

Access the NASA STI program home page at http://www.sti.nasa.gov   
 E-mail your question to help@sti.nasa.gov   
Phone the NASA STI Information Desk at 757-864-9658   
Write to: NASA STI Information Desk Mail Stop 148 NASA Langley Research Center Hampton, VA 23681-2199

# Wind Tunnel Interference Effects on Tiltrotor Testing Using Computational Fluid Dynamics

Witold J. F. Koning Ames Research Center, Moffett Field, California

National Aeronautics and Space Administration

Ames Research Center Moffett Field, CA 94035-1000

# ACKNOWLEDGMENTS

One of the great advantages to working in a high tech environment is that highly skilled and knowledgeable people are all around you and always willing to help.

Invaluable help came from a multitude of people at the Aeromechanics branch at NASA: Wally Acree, for his patience and guidance during my validation phases of the XV-15 rotor; Eduardo Solis, who despite the work pressure always found time to help with meshing and gridding in RotCFD; Meridith Segall, who never got upset when I asked for even more computers to run my simulations on; as well as Gloria Yamauchi, Larry Young, Natasha Barbely, Shirley Burek, Esma Sahin, and Samalis Santini for all the support throughout my time at Ames. And special thanks to Kristen Kallstrom who has been the kindest of all throughout my research.

Also several interns at Ames have been highly valuable and supportive during my research, especially JeWon Hong and Shelby Mallin for their very valuable research in support of my work.

From Sukra Helitek, I would like to explicitly thank Ganesh Rajagopalan and Luke Novak for their extensive support while I dove into the intricacies of RotCFD. From Science and Technology Corporation, I would like to thank in particular Amar Choudry, Stephen Lesh, and Ravi Deepak for making this experience possible in the first place and supporting me on my way to the U.S., and during my stay here.

At the Delft University of Technology, I would like to thank Roelof Vos for his support and guidance throughout my research.

It is by no means an exaggeration to state that this work could not have been completed without their continued support.

Lastly, I cannot express my gratitude for Dr. William Warmbrodt, chief of the Ames Aeromechanics branch, for his unwavering support. He is undoubtedly one of the most inspiring people I’ve had the pleasure of meeting in my life; an acknowledgments section does not suffice the credit that he deserves.

Available from:

NASA STI Support Services Mail Stop 148 NASA Langley Research Center Hampton, VA 23681-2199 757-864-9658

National Technical Information Service 5301 Shawnee Road Alexandria, VA 22312 webmail@ntis.gov 703-605-6000

# TABLE OF CONTENTS

List of Figures .

List of Tables . . ix

Nomenclature .. . xi

Introduction ..

Rotorcraft Computational Fluid Dynamics (RotCFD) .. 2

The RotCFD Rotor Model . 3

Some Considerations With the Use of RotCFD

National Full-Scale Aerodynamics Complex (NFAC) ..

Wind Tunnel and Test Section Geometry ..

Wind Tunnel Wall Corrections .. 9

Tiltrotor Test Rig (TTR) . . 10

XV-15 Rotor Characteristics 11

XV-15 Rotor Blade Characteristics . . 13

C81 Airfoil Data Structure . . 14

XV-15 Performance Data . . 15

Hover .. 16

Tilt . 17

Airplane Mode .. 19

Aerodynamic Analysis Method . . 19

XV-15 Airfoil Data Corrections .

Stall Delay Model . . 20

Tip Loss Model . 22

C81 Airfoil Adjustment Code . 22

General Setup of Validation Cases . . 27

Boundary Settings . . 27

Spatial and Temporal Resolution Independency . . 28

NFAC Wind Tunnel Cases Setup . . 28

NFAC 80- by 120-Foot Wind Tunnel Cases .

NFAC 40- by 80-Foot Wind Tunnel Cases . . 33

Validation of XV-15 Rotor Model.. . 35

Hover .. . 36

Tilt Mode . . 39

Airplane Mode .. 41

Ground Effect Study . 41

Discussion on Airfoil Data Correction . . 41

Tip Loss Factor . . 41

Stall Delay Factor . 43

Accuracy and Precision . 43

Residual Values . . 44

Performance Convergence . . 45

# TABLE OF CONTENTS (continued)

NFAC Simulation Results . . 46

NFAC 80- by 120-Foot Wind Tunnel Results . . 47

Quasi Trim for Thrust .. 49

NFAC 40- by 80-Foot Wind Tunnel Results . . 52

Quasi Trim for Thrust .. . 53

Performance Convergence . . 55

Forces on the TTR . . 56

Stability-Related Time Step Restrictions . . 58

Conclusions and Recommendations . . 59

Conclusions . . 59

Recommendations .. . 59

References .. . 61

Appendix A—NFAC Characteristics . . 63

Appendix B—C81 Airfoil Adjustment Code Results . 65

Angle of Attack and Mach number interpolation . . 65

Representative Stall Delay Plots . . 67

Appendix C—Steady XV-15 Rotor Validation Results . . 69

Simulation Parameters . 69

Residual Overview .. 70

Data Steady XV-15 Rotor Results . . 72

Appendix D—Unsteady XV-15 Rotor Validation Results .. . 75

Simulations Parameters... . 75

Hover—Unsteady . . 76

Tilt Mode—Unsteady .. . 77

Airplane Mode—Unsteady .. . 78

Data Unsteady XV-15 Rotor Results . . 79

# LIST OF FIGURES

Figure 1. Rotor and coordinate system.. 4   
Figure 2. Blade section nomenclature at a grid point.. 5   
Figure 3. Velocity plot of a steady model (a) and an unsteady model (b). . 6   
Figure 4. Top view of rotor disk grid and flow field grid (a) and an enlarged view (b). .... 7   
Figure 5. The NFAC facility at Ames Research Center.. 8   
Figure 6. The 80- by 120-Foot Wind Tunnel (left) and 40- by 80-Foot Wind Tunnel (right) cross section in the NFAC. 8   
Figure 7. Cross-section geometry of the NFAC.. 9   
Figure 8. Propeller in closed throat wind tunnel. 9   
Figure 9. The 80- by 120-Foot Wind Tunnel Inlet.. . 10   
Figure 10. The TTR on the test bed (a) and a render in the 40- by 80-Foot Wind Tunnel (b). ......... 11   
Figure 11. XV-15 rotor blade chord-line twist distribution. . 13   
Figure 12. XV-15 rotor blade chord distribution. . 13   
Figure 13. XV-15 rotor blade chord distribution. . 14   
Figure 14. Example format of (partial) C81 airfoil data file. . . 15   
Figure 15. XV-15 rotor hover power as a function of thrust.. . 16   
Figure 16. XV-15 rotor hover figure of Merit as a function of thrust. . . 17   
Figure 17. XV-15 rotor power as a function of thrust for different pylon angles at $V / \varOmega R = 0 . 3 2$ . . 18   
Figure 18. XV-15 rotor power as function of thrust, for $a _ { p } = 7 5 ^ { \circ }$ and $M _ { t i p } = 0 . 6 5$ . . . 18   
Figure 19. Rotor propulsive efficiency as function of thrust. . 19   
Figure 20. Spanwise Corrigan stall delay parameter obtained for XV-15 rotor model. .. 21   
Figure 21. AoA and Mach interpolation for representative cases of the NACA 64-X08 airfoil. . 23   
Figure 22. Simplified flowchart of airfoil adjustment code. . 24   
Figure 23. Radial interpolation check of lift coefficient at $M = 0 . 3 0$ .. . 25   
Figure 24. Stall delay as function of angle of attack or Mach number for various radial stations. . . 26   
Figure 25. Lift coefficient as function of radial station at $M = 0 . 3 0$ at continuous zero pitch angle. . . 26   
Figure 26. RotCFD user interface with a hover case loaded.. . 27   
Figure 27. Hover case, gridded centered side view (XZ) of the flow field. Hover case, gridded top view (XY) at rotor height. . 28   
Figure 28. The boundaries of the test sections with TTR in edgewise and axial mode.. . 29   
Figure 29. TTR in 40- by 80-Foot Wind Tunnel cross section shifting from airplane $( a _ { p } = 0 ^ { \circ } )$ ) mode to edgewise flight $( a _ { p } = 9 0 ^ { \circ } ,$ ).. . 30   
Figure 30. The extended test sections with TTR on struts and XV-15 rotor in edgewise and axial mode, respectively. . 31

# LIST OF FIGURES (continued)

Figure 31. The setup of case 3, WTGE. The setup for cases 1 and 2, WTGE. . 32   
Figure 32. Conversion corridor of the XV-15. . 33   
Figure 33. XV-15 height-velocity envelope. . 33   
Figure 34. The geometry for case 4 and 5, FFGE. . 34   
Figure 35. The geometry and grid for case 6, WTGE. The geometry for case 7, WTRO. . 34   
Figure 36. Unsteady results for XV-15 rotor hover power as a function of thrust. . 36   
Figure 37. Unsteady results for XV-15 rotor hover figure of Merit as a function of thrust. .. .. 37   
Figure 38. Steady results for XV-15 rotor hover power as a function of thrust. . . 37   
Figure 39. Steady results for XV-15 rotor hover figure of merit as a function of thrust. . 38   
Figure 40. Rotor thrust as function of collective pitch angle. . . 38   
Figure 41. Rotor power as function of collective pitch angle. . 39   
Figure 42. Steady results for XV-15 rotor power as a function of thrust for various pylon angles at $V / \varOmega R = 0 . 3 2 .$ . . 40   
Figure 43. Steady results for XV-15 rotor power as function of thrust, for $a _ { p } = 7 5 ^ { \circ }$ . . 40   
Figure 44. Steady results for (rotor) propulsive efficiency as function of thrust. . . 41   
Figure 45. Evaluation of the XV-15 rotor in ground effect in RotCFD. . 42   
Figure 46. Sketch of blade loading characteristics.. . 42   
Figure 47. Residual plot for a tilting isolated rotor at 15 degrees pylon angle. . 44   
Figure 48. Hover performance convergence over time. . 45   
Figure 49. Tilt mode (15 degree pylon angle) convergence over time. . 45   
Figure 50. Airplane mode convergence over time. . . 46   
Figure 51. Various computers used to compute each of the cases within the time frame. . . 46   
Figure 52. A velocity plot of a coarse, unfitted body test at $t \approx 6$ (s) showing no re-ingestion. ........ 48   
Figure 53. Linearization to obtain point $( T _ { F F G E } , P ^ { * } )$ .. . 49   
Figure 54. Representative velocity plots for case 3. . 51   
Figure 55. Flow field of FFGE subset for case 7. . . 54   
Figure 56. Performance convergence for case 2, WTGE, hover.. . 55   
Figure 57. Performance convergence for case 7, WTGE, tilt mode. . . 55   
Figure 58. Integrated forces on the TTR for case 5, WTGE. . 56   
Figure 59. Integrated forces on the TTR and struts for case 4, WTGE. . 57   
Figure 60. Performance convergence for case 4, WTGE. . 57   
Figure 61. Meshed TTR nose (no grid) (a), body-fitted TTR nose (b), and gridded TTR nose without body fitting (c). . 58   
Figure 62. Imported C81 data for NACA 64-X08 airfoil. . 65   
Figure 63. Imported C81 data for NACA 64-X12 airfoil. . 66   
Figure 64. Imported C81 data for NACA 64-X18 airfoil. . 66

# LIST OF FIGURES (concluded)

Figure 65. Imported C81 data for NACA 64-X25 airfoil. . 67   
Figure 66. Effect of stall delay on lift curve slope. . . 68   
Figure 67. Effect of stall delay on lift coefficient for set of airfoil data at various radial stations. . 68   
Figure 68. Residual overview for representative airplane mode case. . . 70   
Figure 69. Residual overview for representative tilt mode case with $a _ { p } = 7 5$ . . . 70   
Figure 70. Residual overview for representative hover mode case.. . 71   
Figure 71. Unsteady results for XV-15 rotor hover power as a function of thrust. . 76   
Figure 72. Unsteady results for XV-15 rotor hover figure of Merit as a function of thrust. .. .. 76   
Figure 73. Unsteady results for XV-15 rotor power as a function of thrust for various pylon angles at $V / \varOmega R = 0 . 3 2$ . . 77   
Figure 74. Unsteady results for XV-15 rotor power as function of thrust, for $a _ { p } = 7 5 ^ { \circ }$ and $M _ { t i p } = 0 . 6 5$ . . . 78   
Figure 75. Unsteady results for (rotor) propulsive efficiency as function of thrust. . . 78

# LIST OF TABLES

Table 1. Key TTR Design Capabilities. . 11   
Table 2. XV-15 Rotor Characteristics . . 12   
Table 3. Sea Level Air Properties Used .. . 20   
Table 4. Overview of Four Different Subsets Per Case .. . 31   
Table 5. Final 80- by 120-Foot Wind Tunnel Cases.. . 32   
Table 6. Final 40- by 80-Foot Wind Tunnel Cases. . 35   
Table 7 RotCFD Steady Simulation Parameters for the XV-15 Rotor . . 35   
Table 8. Final 80- by 120-Foot Wind Tunnel Cases.. . 47   
Table 9. NFAC 80- by 120-Foot Wind Tunnel Geometry Results . . 48   
Table 10. Quasi Trimmed NFAC 80- by 120-Foot Wind Tunnel Geometry Results . . 50   
Table 11. NFAC 40- by 80-Foot Wind Tunnel Rotor-Only Results . . 52   
Table 12. NFAC 40- by 80-Foot Wind Tunnel Geometry Results . . 53   
Table 13. Quasi Trimmed NFAC 40- by 80-Foot Wind Tunnel Geometry Results .. 54   
Table 14. 40- by 80-Foot Wind Tunnel Characteristics . 63   
Table 15. 80- by 120-Foot Wind Tunnel Characteristics . . 63   
Table 16. Overview of Steady Simulation Parameters .. 69   
Table 17. Overview of Steady Simulation Results . . 72   
Table 18. Overview of Unsteady Simulation Parameters .. . 75   
Table 19. Overview of Unsteady Simulation Results . . 79

# NOMENCLATURE

# Symbols

$A$ area, rotor disk area, $\pi R ^ { 2 }$ m2

$a$ acceleration m/s2

$a _ { 0 }$ speed of sound at sea level m/s

$B$ tip-loss factor

$b$ number of blades

$c$ blade chord m

$c _ { d }$ section drag coefficient

$c _ { l }$ section lift coefficient

$c _ { l , t a b l e }$ section lift coefficient from C81 table

cm $c _ { m }$ section moment coefficient

cn $c _ { n }$ section normal force coefficient

$C _ { P }$ rotor power coefficient

$C _ { P o }$ rotor induced power coefficient, $P _ { o } / \rho A ( \varOmega R ) ^ { 3 }$

$C _ { T }$ rotor thrust coefficient, $T / \rho A ( \varOmega R ) ^ { 2 }$

$c _ { t }$ section tangential force coefficient

$c _ { z }$ section force in z-direction

cφ $c _ { \varphi }$ section force in $\boldsymbol { \Phi }$ -direction

$f$ body force per unit mass N/kg

$h$ altitude m

$K _ { L }$ stall delay parameter (Corrigan model)

l aerodynamic locus m

$M$ Mach number, figure of merit

m mass kg

݉ሶ mass flux kg/s

$M _ { t i p }$ tip Mach number

$N$ number of blades

$P$ power J/s

$p$ pressure N/m2

$p _ { 0 }$ pressure at sea level $\mathrm { { N / m ^ { 2 } } }$

$P _ { i }$ induced power J/s

$P _ { o }$ profile power J/s

$R$ rotor radius m

$r$ blade or rotor disk radial coordinate m

$R$ gas constant $\mathrm { m } ^ { 2 } / \mathrm { s } ^ { 2 } \mathrm { K }$

$r , \varphi , z$ inertial coordinate system fixed at the center of the rotor NA

$R _ { e }$ effective blade radius m

# NOMENCLATURE (continued)

Symbols   

<table><tr><td>S</td><td>surface</td><td>m2</td></tr><tr><td>sz</td><td>source strength per unit radius in z-direction</td><td>N/m</td></tr><tr><td>sz&#x27;</td><td>averaged source strength per unit radius in z-direction</td><td>N/m</td></tr><tr><td>sφ</td><td>source strength per unit radius in φ-direction</td><td>N/m</td></tr><tr><td>sφ&#x27;</td><td>averaged source strength per unit radius in φ-direction</td><td>N/m</td></tr><tr><td>T</td><td>rotor thrust</td><td>N</td></tr><tr><td>t</td><td>time</td><td>s</td></tr><tr><td>T∞</td><td>rotor thrust out of ground effect</td><td>N</td></tr><tr><td>T0</td><td>temperature at sea level</td><td>K</td></tr><tr><td>u</td><td>velocity component parallel to x-axis</td><td>m/s</td></tr><tr><td>V</td><td>velocity, aircraft or wind tunnel speed</td><td>m/s</td></tr><tr><td>v</td><td>velocity component parallel to y-axis</td><td>m/s</td></tr><tr><td>V</td><td>rotor velocity with respect to air</td><td>m/s</td></tr><tr><td>Vabs</td><td>absolute velocity (of blade element)</td><td>m/s</td></tr><tr><td>Vcal</td><td>calibrated airspeed</td><td>m/s</td></tr><tr><td>vh</td><td>hover induced velocity</td><td>m/s</td></tr><tr><td>vi</td><td>induced velocity</td><td>m/s</td></tr><tr><td>v∞</td><td>velocity in the far wake</td><td>m/s</td></tr><tr><td>Vrel</td><td>relative velocity (at blade section)</td><td>m/s</td></tr><tr><td>Vtas</td><td>true airspeed</td><td>m/s</td></tr><tr><td>w</td><td>velocity component parallel to z-axis</td><td>m/s</td></tr><tr><td>x, y, z</td><td>Cartesian coordinate system</td><td>NA</td></tr><tr><td>z</td><td>height from ground</td><td>m</td></tr></table>

Greek Symbols   

<table><tr><td>α</td><td>angle of attack</td><td>deg</td></tr><tr><td>αp</td><td>pylon angle</td><td>deg</td></tr><tr><td>β</td><td>angle between relative velocity and rotor disk plane</td><td>rad</td></tr><tr><td>βp</td><td>precone angle</td><td>deg</td></tr><tr><td>γ</td><td>ratio of specific heats</td><td>-</td></tr><tr><td>δP</td><td>percentage change of power (compared to FFGE case)</td><td>%</td></tr><tr><td>δT</td><td>percentage change of thrust (compared to FFGE case)</td><td>%</td></tr><tr><td>εct</td><td>chord-line twist</td><td>deg</td></tr><tr><td>θ</td><td>collective angle</td><td>deg</td></tr><tr><td>θ.75</td><td>collective pitch angle at quarter chord</td><td>deg</td></tr></table>

# NOMENCLATURE (continued)

# Greek Symbols

<table><tr><td>θ0</td><td>collective pitch angle</td><td>deg</td></tr><tr><td>μ</td><td>advance ratio</td><td>-</td></tr><tr><td>μ</td><td>dynamic viscosity</td><td>(N.s)/m2</td></tr><tr><td>ρ</td><td>density</td><td>kg/m3</td></tr><tr><td>σ</td><td>rotor solidity</td><td>-</td></tr><tr><td>Ω</td><td>rotor rotational speed</td><td>rad/s</td></tr></table>

# Abbreviations

<table><tr><td>ADM</td><td>Actuator-Disk Model</td></tr><tr><td>AoA</td><td>Angle of Attack</td></tr><tr><td>BEM</td><td>Blade-Element Model</td></tr><tr><td>BL</td><td>Boundary Layer</td></tr><tr><td>C81</td><td>Airfoil Data Format</td></tr><tr><td>CAMRAD</td><td>Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics</td></tr><tr><td>CFD</td><td>Computational Fluid Dynamics</td></tr><tr><td>EPS</td><td>Turbulent Dissipation</td></tr><tr><td>FFGE</td><td>Free Field with Geometry (excluding wind tunnel, including geometry)</td></tr><tr><td>FFRO</td><td>Free Field Rotor Only (excluding wind tunnel and geometry)</td></tr><tr><td>IGE</td><td>In Ground Effect</td></tr><tr><td>ISA</td><td>International Standard Atmosphere</td></tr><tr><td>JVX</td><td>Joint-service Vertical take-off/landing Experimental (Aircraft)</td></tr><tr><td>MA</td><td>Moving Average</td></tr><tr><td>NA</td><td>Not Available</td></tr><tr><td>NFAC</td><td>National Full-Scale Aerodynamics Complex</td></tr><tr><td>NS</td><td>Navier-Stokes</td></tr><tr><td>OARF</td><td>Outdoor Aerodynamic Research Facility</td></tr><tr><td>OGE</td><td>Out of Ground Effect</td></tr><tr><td>PCHIP</td><td>Piecewise Cubic Hermite Interpolating Polynomial</td></tr><tr><td>PTR</td><td>Proprotor Test Rig</td></tr><tr><td>RANS</td><td>Reynolds Averaged Navier-Stokes</td></tr><tr><td>RotCFD</td><td>Rotorcraft CFD</td></tr><tr><td>RotUNS</td><td>Rotor Unstructured Solver</td></tr></table>

# NOMENCLATURE (concluded)

# Abbreviations

<table><tr><td>RotVIS</td><td>Rotor VIScous Solver Application</td></tr><tr><td>SD</td><td>Stall Delay</td></tr><tr><td>SI</td><td>Système International d&#x27;Unités</td></tr><tr><td>SIMPLE</td><td>Semi-Implicit Method for Pressure-Linked Equations</td></tr><tr><td>SIMPLER</td><td>Semi-Implicit Method for Pressure-Linked Equations Revised</td></tr><tr><td>TKE</td><td>Turbulent Kinetic Energy</td></tr><tr><td>TL</td><td>Tip Loss</td></tr><tr><td>TTR</td><td>Tiltrotor Test Rig</td></tr><tr><td>U-mom</td><td>momentum in x-direction</td></tr><tr><td>U-vel</td><td>velocity in x-direction</td></tr><tr><td>URANS</td><td>Unsteady Reynolds Averaged Navier-Stokes</td></tr><tr><td>WTGE</td><td>Wind Tunnel with Geometry (including wind tunnel and geometry)</td></tr><tr><td>WTGE*</td><td>Quasi Trimmed Wind Tunnel with Geometry (incl. wind tunnel and geometry)</td></tr><tr><td>WTGE1</td><td>First set of Wind Tunnel with Geometry (including wind tunnel and geometry)</td></tr><tr><td>WTGE2</td><td>Second set of Wind Tunnel with Geometry (including wind tunnel and geometry)</td></tr><tr><td>WTRO</td><td>Wind Tunnel Rotor Only (including wind tunnel, excluding geometry)</td></tr><tr><td>WTT</td><td>Wind Tunnel Test</td></tr><tr><td>XV-15</td><td>Tiltrotor Research Aircraft</td></tr></table>

# WIND TUNNEL INTERFERENCE EFFECTS ON TILTROTOR TESTING USING COMPUTATIONAL FLUID DYNAMICS

Witold J. F. Koning*

Ames Research Center

# SUMMARY

Experimental techniques to measure rotorcraft aerodynamic performance are widely used. However, most of them are either unable to capture interference effects from bodies, or require an extremely large computational budget. The objective of the present research is to develop an XV-15 Tiltrotor Research Aircraft rotor model for investigation of wind tunnel wall interference using a novel Computational Fluid Dynamics (CFD) solver for rotorcraft, RotCFD.

In RotCFD, a mid-fidelity Unsteady Reynolds Averaged Navier–Stokes (URANS) solver is used with an incompressible flow model and a realizable k-ε turbulence model. The rotor is, however, not modeled using a computationally expensive, unsteady viscous body-fitted grid, but is instead modeled using a blade-element model (BEM) with a momentum source approach.

Various flight modes of the XV-15 isolated rotor, including hover, tilt, and airplane mode, have been simulated and correlated to existing experimental and theoretical data. The rotor model is subsequently used for wind tunnel wall interference simulations in the National Full-Scale Aerodynamics Complex (NFAC) at Ames Research Center in California.

The results from the validation of the isolated rotor performance showed good correlation with experimental and theoretical data. The results were on par with known theoretical analyses. In RotCFD the setup, grid generation, and running of cases is faster than many CFD codes, which makes it a useful engineering tool. Performance predictions need not be as accurate as high-fidelity CFD codes, as long as wall effects can be properly simulated.

For both test sections of the NFAC wall, interference was examined by simulating the XV-15 rotor in the test section of the wind tunnel and with an identical grid but extended boundaries in free field. Both cases were also examined with an isolated rotor or with the rotor mounted on the modeled geometry of the Tiltrotor Test Rig (TTR). A “quasi linear trim” was used to trim the thrust for the rotor to compare the power as a unique variable. Power differences between free field and wind tunnel cases were found from $^ { - 7 }$ to 0 percent in the 80- by 120-Foot Wind Tunnel and $- 1 . 6$ to 4.8 percent in the 40- by 80-Foot Wind Tunnel, depending on the TTR orientation, tunnel velocity, and blade setting. The TTR will be used in 2016 to test the Bell 609 rotor in a similar fashion to the research in this report.

# INTRODUCTION

Experimental techniques to measure rotor and airframe aerodynamic performance are widely used, but the need exists to understand the limitations of ground-based testing by augmenting the analysis of experimental test results with Computational Fluid Dynamics (CFD) modeling. The objective of the present research is to develop an XV-15 Tiltrotor Research Aircraft rotor model for investigation of wind tunnel wall interference. This research is performed to support wind tunnel tests scheduled for 2016. Ultimately the rotor model developed will be used to investigate wind tunnel wall effects on large tiltrotors in the National Full-Scale Aerodynamics Complex (NFAC) facility at Ames Research Center in California. The renewed interest in tiltrotors originates from NASA studies indicating significant reduction in congestion of commercial transport aviation.1

The focus of this research is to understand the limitations and accuracy of tiltrotor performance predictions using a mid-fidelity CFD program. An unsteady RANS solver, RotCFD, is used with an incompressible flow and a k-ε turbulence model. RotCFD uses a model similar to an actuator-disk model (ADM) or blade-element model (BEM) with two-dimensional airfoil data that allows for relatively quick simulations of unsteady rotorcraft cases. The rotor is represented solely through the momentum it imparts to the flow. The coupling of the rotor with the surrounding flow is done by implementing its sources in the momentum equations. This omits the classical way of resolving a very fine grid around the rotor geometry to capture all flow effects. This gives RotCFD a significant advantage in simulation time.

Inherent to the use of two-dimensional airfoil data and a traditional BEM or ADM is the removal of three-dimensional effects. The most notable effects are stall delay, tip loss, yawed flow, and unsteady rotor aerodynamics. Care must be taken to ensure these effects are properly accounted for either within RotCFD or by applying the proper models to the airfoil data tables in C81 format. The model is applied to cases of the XV-15 rotor model on the Tiltrotor Test Rig (TTR) with struts in the two NFAC facilities under various flow conditions, pylon angles, and rotor conditions. The performance with geometry, in terms of thrust and power, is compared to isolated rotor performance in both free field and the wind tunnel test sections of the NFAC.

# ROTORCRAFT COMPUTATIONAL FLUID DYNAMICS (RotCFD)

The flow solver needs to handle unsteady rotor simulations while being computationally inexpensive. Rotorcraft CFD (RotCFD) is a mid-fidelity CFD tool specifically for rotorcraft design efforts and has been developed recently [1]. Young performed a study on complex rotor wake interaction simulation using RotCFD [2]. Rotorcraft Unstructured Solver (RotUNS) is a module within RotCFD that uses three-dimensional, unsteady, incompressible Reynolds Averaged

Navier–Stokes equations (URANS) on a Cartesian unstructured grid with tetrahedral body-fitting near the body. The Semi-Implicit Method for Pressure-Linked Equations Revised (SIMPLER) is used in combination with the under relaxation factors to iteratively obtain the correct flow field in agreement with both the continuity and momentum equations.

The module of RotCFD used in this research is RotUNS and is used synonymous to RotCFD in this report. Spalart discusses the possible pitfalls with the use of URANS, but also indicates it is one of the few feasible unsteady methods when computational budget is limited [3]. Iaccarino et al. show the differences in simulated flow field using both a steady and unsteady Reynolds Averaged Navier– Stokes approach for the flow over a cube [4].

Turbulence is accounted for by the URANS equations combined with a two-equation realizable k-ε turbulence model with special wall treatment. The two transported variables are $k _ { : }$ , the turbulent kinetic energy, and $\varepsilon$ , the turbulent dissipation. Jones and Launder presented and validated the k-ε turbulence model in the 1970s [5], [6]. Yu and Cao have shown that accurate CFD analyses for the flow field and performance of a helicopter in forward flight can be obtained with a k-ε turbulence model with wall function method [7]. The wall function is introduced because the no-slip condition near the wall is found to behave unsatisfactory if the k-ε turbulence model is applied without this correction.

Discretization is done using the finite-volume method, and an implicit solver is used in order to have a less stringent stability criterion and therefore more flexibility for various operations. This allows using consistent spatial and temporal grid under various cases more easily. The time-dependent solution, however, might not follow the exact transients as accurately as an explicit approach [8]. This setup was not further investigated for this research.

# The RotCFD Rotor Model

The rotor is modeled only through the momentum it imparts on the flow. In the first paper on this approach [9], Rajagopalan and Lim stated, “From the point of the fluid particles, the influence of the spinning rotor is to change their momentum.” This momentum change occurs because of the aerodynamic forces exerted on the cells through the spinning blades. The fully viscous, unsteady, body-conforming grid usually chosen for such a computation is no longer necessary, greatly reducing the complexity. Also, the no-slip condition on the rotor is omitted, and no unsteady boundary layer has to be resolved on a very dense grid, which also reduces the complexity. This reduction in complexity, in turn, is manifested with the possibility of running problems on desktopclass computers, where unsteady rotor simulations using full Navier–Stokes equations with turbulence models and body-conforming grid generally require supercomputers [9].

The source depends on the flow properties, rotor geometry, and two-dimensional airfoil data as shown in Equation (1), where $c _ { l }$ and $c _ { d }$ are the airfoil section coefficients; $\alpha$ is the angle of attack; $V _ { a b s }$ is the absolute instantaneous velocity vector at the airfoil section; $\varOmega$ is the rotational velocity; $x , y ,$ and $z$ are the Cartesian coordinates; $t$ is time; $c$ is the chord; $\rho$ is the density; and $b$ is the number of blades.

$$
\pmb {S} = S (c _ {l}, c _ {d}, \alpha , \pmb {V} _ {a b s}, \Omega , x, y, z, t, c, \rho , b) \tag {1}
$$

Figure 1 shows a schematic drawing of the rotor and the $( r , \phi , z )$ inertial coordinate system fixed at the rotor used in the derivation of the momentum sources.

The rotor model uses a version of a blade-element model (BEM) called the “steady” rotor model where the discrete rotor source terms can be averaged over the disc. RotCFD creates a model comparable to the traditional actuator-disk model (ADM), with the major difference being that the disk is not experiencing a homogenous load. An “unsteady” rotor model based on the BEM is also tested; this model does use the discrete blades, hence “unsteady” blade modeling. The effect on the fluid is considered only at the point where the rotor, or disc if the “steady” model is used, intersects with a grid point from the CFD domain. In the unsteady model, a line at the quarter chord location replaces the chord length of the rotor.

Figure 2 shows the nomenclature of a blade section (see A-A in Figure 1) used to derive the source terms $S _ { \phi }$ and $S _ { z } ,$ aligned with tangential force coefficient $c _ { t } ,$ and normal force coefficient $c _ { n }$ . The absolute velocity, $V _ { a b s ; }$ , consists of components $\nu _ { r } , \nu _ { \phi }$ , and $\nu _ { z } ,$ and the relative velocity, $V _ { r e l , }$ consists of components vr’, $\nu _ { \phi } ^ { \mathrm { ~ ~ } } { } ^ { \mathrm { ~ ~ } }$ , and $\nu _ { z } ^ { \mathrm { ~ ~ } }$ .

The normal and tangential (to the disk) coefficients can be derived from Figure 2 as shown in Equations (2) and (3).

$$
c _ {n} = c _ {l} \cos \beta - c _ {d} \sin \beta \tag {2}
$$

$$
c _ {t} = c _ {l} \sin \beta + c _ {d} \cos \beta \tag {3}
$$

图片摘要：该图主要展示 1. Rotor and coordinate system [9]。
![](images/7483179c968973aa3b58a22e8d4d0417e8945382b7bae456e6bafd4c6903c46e.jpg)  
Figure 1. Rotor and coordinate system [9].

图片摘要：该图主要展示 1. Rotor and coordinate system [9]。
![](images/065a6ba10841883653c68831a9f9be3f557dcc6c74fd436876ce72941772a3b0.jpg)  
Figure 2. Blade section nomenclature at a grid point [18].

The angle $\beta _ { ; }$ , the angle between the relative velocity and the disk plane, is obtained from Equation (4). Note that the relative velocity in $\phi$ -direction is composed of the sum of the local flow component and the component through blade rotation at the radial station where the blade section is chosen.

$$
\tan \beta = \frac {v _ {z} ^ {\prime}}{v _ {\varphi} ^ {\prime}} \tag {4}
$$

The angle of attack, $\alpha$ , is now deduced in Equation (5).

$$
\alpha = \theta - \beta \tag {5}
$$

The section properties of the airfoil are determined from the angle of attack and Mach number, derived solely from the relative velocity, and input into Equation (2). The normal and tangential force coefficients can now be converted to $\phi$ - and z-direction, as shown in equations (6) and (7).

$$
c _ {z} = - c _ {n} \tag {6}
$$

$$
c _ {\varphi} = + c _ {t} \tag {7}
$$

The rotor blades are divided into spanwise elements. The blade geometric properties are constant over an element, and hence the source terms per unit element can be derived as shown in Equations (8) and (9).

$$
s _ {z} = c _ {z} \left(\frac {1}{2} \rho V _ {r e l} ^ {2} c\right) \tag {8}
$$

$$
s _ {\varphi} = c _ {\varphi} \left(\frac {1}{2} \rho V _ {r e l} ^ {2} c\right) \tag {9}
$$

图片摘要：该图主要展示 3. Velocity plot of a steady model (a) and an unsteady model。
![](images/cb7d6d0714fb073f71c20431fd2b02d771962aa130fe8aeddf4acba7ee427ce8.jpg)  
a)

图片摘要：该图主要展示 3. Velocity plot of a steady model (a) and an unsteady model。
![](images/0a228187030660cdb33ebbd08af38837972c33f9246c46e7323d761200a3a32e.jpg)  
  
Figure 3. Velocity plot of a steady model (a) and an unsteady model (b).

These terms are changing as the rotor moves through the grid. In case the “steady” model is chosen, the source terms are averaged over the rotor disk while spinning. An example of the differences in the velocity field at the rotor disk for a steady and unsteady rotor model is shown in Figure 3a and Figure 3b, respectively. Defining the time for one rotor revolution as $t _ { r e \nu ; \ l }$ , the time taken by a blade section to go through the width of a cell as $t _ { c e l l } ,$ and the number of blades as $b$ , the averaged source terms for hover can be derived in Equations (10) and (11). For other flight modes, the individual blades have to be averaged as they experience different loading.

$$
s _ {z} ^ {\prime} = \frac {b s _ {z} t _ {c e l l}}{t _ {r e v}} = \frac {\Omega b s _ {z} t _ {c e l l}}{2 \pi} \tag {10}
$$

$$
s _ {\varphi} ^ {\prime} = \frac {b s _ {\varphi} t _ {c e l l}}{t _ {r e v}} = \frac {\Omega b s _ {\varphi} t _ {c e l l}}{2 \pi} \tag {11}
$$

The source terms, defined in the inertial coordinate system fixed at the rotor, can be converted to the Cartesian coordinate system used in RotCFD. Integrating the z-coordinate of the source terms yields thrust whereas the integrated $\phi$ -direction source can be multiplied by the rate of rotation to obtain the (profile) power. The induced power is obtained by multiplying the thrust with the induced velocity.

Note that the rotor precone angle has not been taken into account in this derivation, but is used in RotCFD and this research. No sweep angle is considered in the present research. Note that no component in $r .$ -direction is deduced, implying no radial effects are considered. Figure 4a and Figure 4b show a representative example of the rotor (source) program grid in white with the red cell structure underneath. The blades are only shown for visualization purposes.

图片摘要：该图主要展示 4. Top view of rotor disk grid and flow field grid (a) and a。
![](images/37f935679e7ddfe779305ac6229f4a98c02a74dd76d98f41e3793f8da77c37e6.jpg)  
a)

图片摘要：该图主要展示 4. Top view of rotor disk grid and flow field grid (a) and a。
![](images/42ab8a52cf0cd2fe6af1486b6488fe1f80e807e64f118ef31040a4d169986f05.jpg)  
  
Figure 4. Top view of rotor disk grid and flow field grid (a) and an enlarged view (b).

# Some Considerations With the Use of RotCFD

The RotCFD approach leads to an indirect relationship between the viscous effects and the action of the rotor blades. This approach therefore cannot give the same results as the full Navier–Stokes (NS) solution would. Also dynamic stall, or any effect for which the boundary layers or actual rotor geometry must be known, will not be evaluated properly. An example is the radial flow on the rotor blades that cannot be modeled. The absence of radial flow is also the reason a stall delay model is evaluated in this research.

Even though the rotor is based solely on two-dimensional airfoil data, because of the implementation into a flow field grid some of the three-dimensional effects, for example tip loss, can be expected. RotCFD can incorporate flapping or cyclic pitch, but this is beyond the scope of the current research.

# NATIONAL FULL-SCALE AERODYNAMICS COMPLEX (NFAC)

The isolated rotor wind tunnel tests for the tiltrotor research programs at Ames Research Center are scheduled for May 2016 in the National Full-Scale Aerodynamics Complex (NFAC, Figure 5) 40- by 80-/80- by 120-Foot Wind Tunnels that are managed and operated by the U.S. Air Force. The original XV-15 research was performed in the 40- by 80- Foot Wind Tunnel [10]. Zell wrote elaborate reports on the performance and flow characteristics of both wind tunnels [11], [12]. Further aerodynamic characteristics are described by Corsiglia [13].

# Wind Tunnel and Test Section Geometry

The two wind tunnels that comprise the NFAC facility share portions of their flow path. The cross section of the 80- by 120-Foot Wind Tunnel is an open circuit wind tunnel with a closed, rectangular test section (Figure 6). The 40- by 80-Foot Wind Tunnel is a single-return, closed-section wind tunnel with an oval test section (Figure 6).

图片摘要：该图主要展示 5. The NFAC facility at Ames Research Center.3。
![](images/48d746e2f6949b036b508b979c238fa872352b2df967319a47ef8815700778a4.jpg)  
Figure 5. The NFAC facility at Ames Research Center.3

图片摘要：该图主要展示 5. The NFAC facility at Ames Research Center.3。
![](images/d9056b718c9719a912f317ede2a0f796e163f56cba72d6eb7c457d586c1dcdc3.jpg)

图片摘要：该图主要展示 5. The NFAC facility at Ames Research Center.3。
![](images/3c2caac127dfafac6494cd532bee2171ff1d772eaeb0e06bf7ad1146e98ee327.jpg)  
Figure 6. The 80- by 120-Foot Wind Tunnel (left) and 40- by 80-Foot Wind Tunnel (right) cross section in the NFAC [11], [12].

The geometry of the cross section is obtained from NFAC studies [11], [12] and sketched in Figure 7. The distinct differences in test section cross-sectional geometry result in a different flow behavior when the rotor flow is simulated. Because of the larger test section of the 80- by 120-Foot Wind Tunnel, it is expected to show less interference with wind tunnel walls. The 40- by 80-Foot Wind Tunnel, besides having a smaller test section, is expected to show more wind tunnel interference with the rotor wake because of its smaller, oval cross-sectional test section shape. The dimensions of the actual cross section are reduced slightly after the addition of an acoustic liner. The inner dimensions of the test section are shown in Appendix A. The boundary layer profile was not found to change significantly with any of the tunnel operating variables [12].

图片摘要：该图主要展示 6. The 80 by 120 Foot Wind Tunnel (left) and 40 by 80 Foot W。
![](images/9183ddf9e3572d1e1428d2855489f0866def30fabfaf93898e43062be5d97be4.jpg)

图片摘要：该图主要展示 6. The 80 by 120 Foot Wind Tunnel (left) and 40 by 80 Foot W。
![](images/67ed034397e6fab8e4317bade1bc756b3dfddb79ad2eefad0414b95f9862d5d0.jpg)  
Figure 7. Cross-section geometry of the NFAC.

# Wind Tunnel Wall Corrections

For positive thrust the velocity in the rotor slipstream is higher than the wind tunnel velocity. Because both tunnels are closed-throat, continuity dictates that the velocity outside of the slipstream is lower, and has a higher static pressure that works its way to the back of the rotor, increasing the thrust [14]. The thrust could therefore result in a rotor reaching equal thrust at a lower free-stream velocity. However, it might be possible under low-thrust (i.e., cruise) conditions, that the wake of the struts, with lower than free-stream velocity, counteracts this effect in exactly the opposite way. Pope and Rae [15] describe the influence of rotor testing in tunnels based on earlier work by Glauert [14]. Figure 8 shows a schematic sketch of a rotor with wake in a wind tunnel and generic velocities. This sketch is only valid for airplane mode flight (axial flow).

图片摘要：该图主要展示 7. Cross section geometry of the NFAC。
![](images/6e6e5e6f300781dbd8f316aca60693b524e95394c2627ae56261e4711d5bde27.jpg)  
Figure 8. Propeller in closed throat wind tunnel [15].

图片摘要：该图主要展示 8. Propeller in closed throat wind tunnel [15]。
![](images/c5847de623fef9f881744b17430f817e629e804cf9818e6de2a518f6e1297a43.jpg)  
Figure 9. The 80- by 120-Foot Wind Tunnel Inlet.4

In edgewise flight this wind tunnel interference effect might be combined with an experienced “ground effect” as the wake could reach the wall below a certain free-stream velocity threshold. It is likely this effect is only to be expected in the 40- by 80-Foot Wind Tunnel, if at all. During tilt mode, a combination of this effect with the axial flow interference effects could take place. All in all, it is expected that pressure buildup will result in higher pressure differences on the rotor increasing performance in the wind tunnel, compared to true free field conditions. The characteristics of the NFAC used in this research are presented in Appendix A. Figure 9 shows the 80- by 120-Foot Wind Tunnel inlet.

# Tiltrotor Test Rig (TTR)

During the actual wind tunnel tests in the NFAC, the isolated rotor is mounted on the Tiltrotor Test Rig (TTR) to allow for the control of powered rotor tests. The TTR (Figure 10a and Figure 10b) is the modern version of the Proprotor Test Rig (PTR) after it was replaced to allow for more advanced rotors. The TTR is mounted on three struts, and four refurbished electric wind tunnel engines provide the power to the rotor. Table 1 contains the main design capabilities of the TTR. At the time of writing, the calibration of the TTR was recently finished and the powered tests were started.

Rotor forces are measured on a dedicated balance installed within the TTR, instead of using the wind tunnel balance system. The wind tunnel turntable can rotate the TTR from axial to edgewise flight and all angles in between. The strut geometry in the 80- by 120-Foot Wind Tunnel has not yet been decided on at the time of writing [16] and will therefore be based on the 40- by 80-Foot Wind Tunnel struts.

图片摘要：该图主要展示 10. The TTR on the test bed (a) and a render in the 40 by 80。
![](images/bb058bbd63a5b0d5661118e2edb072d5b11c7d1d514e43fa1926456dcb35de7a.jpg)  
a)

图片摘要：该图主要展示 10. The TTR on the test bed (a) and a render in the 40 by 80。
![](images/ad48f4e16226c8ccd1dcb8fd3a3bfb3a82b8ff87cc731e98d425ac3a24e9d9fd.jpg)  
  
Figure 10. The TTR on the test bed (a) and a render in the 40- by 80-Foot Wind Tunnel (b).

TABLE 1. KEY TTR DESIGN CAPABILITIES [17]   

<table><tr><td colspan="2">Maximum Wind Speed (kts)</td></tr><tr><td>Axial (airplane)</td><td>300</td></tr><tr><td>Edgewise (hover)</td><td>180</td></tr><tr><td colspan="2">Rotational Speed (rpm)</td></tr><tr><td>Minimal</td><td>126</td></tr><tr><td>Maximal</td><td>630</td></tr><tr><td colspan="2">Maximum Thrust (lb)</td></tr><tr><td>Steady</td><td>20,000</td></tr><tr><td>Peak</td><td>30,000</td></tr></table>

# XV-15 ROTOR CHARACTERISTICS

The rotor parameters are summarized in Table 2. The value of the precone is equal to the value used for the Outdoor Aerodynamic Research Facility (OARF) test, which will be discussed later. The NACA 64-X25 airfoil at radial station $r / R = 0 . 2 5 0 0 \left( \sim \right)$ is copied to the root value at the cutout at $r / R = 0 . 0 8 7 5 \ : ( \sim )$ (marked with the “*” in Table 2) to provide aerodynamic information at the root and prevent erroneous extrapolation of airfoil data. This is common practice in rotor research [16], instead of using an extrapolation method. The original airfoil sectional data files and adjusted or corrected files are public domain but were not included because of their size.

TABLE 2. XV-15 ROTOR CHARACTERISTICS [16], [18]–[22]   

<table><tr><td>Blade Geometry</td><td>SI</td><td>Imperial</td></tr><tr><td>diameter</td><td>7.62 m</td><td>(25 ft)</td></tr><tr><td>disc area</td><td>45.6 m²</td><td>(491 ft²)</td></tr><tr><td>blade chord @ 0.0875R</td><td>0.432 m</td><td>(17 in.)</td></tr><tr><td>blade chord @ 1.000R</td><td>0.356 m</td><td>(14 in.)</td></tr><tr><td>blade area</td><td>4.06 m²</td><td>(43.75 ft²)</td></tr><tr><td>root cutout</td><td>0.0875 r/R</td><td></td></tr><tr><td>solidity</td><td>0.089</td><td></td></tr><tr><td>Blade Twist (bilinear)</td><td></td><td></td></tr><tr><td>chord-line aerodynamic</td><td>38.7°</td><td></td></tr><tr><td>total chord</td><td>41.5°</td><td></td></tr><tr><td>Blade Airfoil Section, r/R (~)</td><td></td><td></td></tr><tr><td>0.0875</td><td>NACA 64-X25*</td><td></td></tr><tr><td>0.2500</td><td>NACA 64-X25</td><td></td></tr><tr><td>0.5268</td><td>NACA 64-X18</td><td></td></tr><tr><td>0.8093</td><td>NACA 64-X12</td><td></td></tr><tr><td>1.0000</td><td>NACA 64-X08</td><td></td></tr><tr><td>Rotor Characteristics</td><td></td><td></td></tr><tr><td>hub precone angle</td><td>2.5°</td><td></td></tr><tr><td>Rotor rpm</td><td></td><td></td></tr><tr><td>helicopter mode (hover, edgewise)</td><td>589</td><td></td></tr><tr><td>airplane mode (axial)</td><td>517</td><td></td></tr><tr><td>Blade Tip Speed</td><td></td><td></td></tr><tr><td>helicopter mode (hover, edgewise)</td><td>225.55 m/s</td><td>(740 ft/s)</td></tr><tr><td>airplane mode (axial)</td><td>182.88 m/s</td><td>(600 ft/s)</td></tr></table>

# XV-15 Rotor Blade Characteristics

The main parameters that are needed for the rotor are the twist and chord distribution, twodimensional airfoil data along the span of the XV-15 blade, and the characteristic dimensions of the rotor. Some conflicting values were found in different publications [18]–[22]; for example, the XV-15 was flown with multiple hub configurations leading to differently listed precone angles. The final values were decided in collaboration with experienced XV-15 researchers [16]. All input requirements for the computation of the rotor source, S, in RotCFD are presented in Equation (12).

$$
\boldsymbol {S} = S \left(c _ {l}, c _ {d}, \alpha , \boldsymbol {V} _ {a b s}, \Omega , x, y, z, t, c, \rho , b\right) \tag {12}
$$

The blade chord-line twist distribution is shown in Figure 11 and the blade chord distribution is shown in Figure 12.

图片摘要：该图主要展示 11. XV 15 rotor blade chord line twist distribution [16]。
![](images/4b604371201f601c53502816bfa35e928a39d558319db8705e62974230867e84.jpg)  
Figure 11. XV-15 rotor blade chord-line twist distribution [16].

图片摘要：该图主要展示 11. XV 15 rotor blade chord line twist distribution [16]。
![](images/ef9f2d44cdc76bee96a30f0edd6e1ec6cc63fcd0c71aebcd50c5492617fbdde9.jpg)  
Figure 12. XV-15 rotor blade chord distribution [16].

图片摘要：该图主要展示 12. XV 15 rotor blade chord distribution [16]。
![](images/893082fe1d3e5487e6a463ff1462ac8c456f0807d099cbaf3ba3b9b719ffc61a.jpg)  
Figure 13. XV-15 rotor blade chord distribution [16].

References to “collective” imply the collective pitch angle, $\theta _ { 0 } ,$ which is defined zero when the pitch angle distribution equals the twist distribution in Figure 11. The relation with the quarter chord pitch angle, $\theta _ { . 7 5 } ,$ is defined for the XV-15 rotor model in Equation (13).

$$
\theta_ {. 7 5} = \theta_ {0} + 6. 6 1 ^ {\circ} \tag {13}
$$

Figure 13 shows the blade loci of the quarter chord, leading edge, and trailing edge. The XV-15 rotor blade has approximately a –1-degree sweep angle that is not incorporated into the model because the sweep is only added for structural reasons [16].

# C81 Airfoil Data Structure

The aerodynamic section properties for the blade airfoil elements are loaded from C81 data tables. The C81 airfoil data structure contains the airfoil section properties and originates from a firstgeneration rotorcraft simulation program from Bell Helicopter company. The program is now outdated, but the C81 format is still used, for example, in Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics II (CAMRAD II) [23].

The format holds three two-dimensional arrays for the lift, drag, and moment coefficients, $c _ { l } \left( a , M \right)$ , $c _ { d } \left( a , M \right)$ , and $\mathrm { c } _ { m } \left( \boldsymbol { \alpha } , M \right)$ , respectively, as a function of angle of attack and Mach number. The format allows for an additional set for a trailing edge flap, however this is not used in this report or following analyses. The data format uses a separate rectangular array for each coefficient. The basic format is 10 columns, each 7 characters wide. The first column only holds the reference angle of attack, $\alpha .$ , values. If the amount of Mach number entries is greater than nine, more than one line is used for each table row ( $\alpha$ value). A new table row $\alpha$ value) must start on a new line. An example of the partial data for the lift coefficient in C81 format is shown in Figure 14. A brief summary of the format is further described in the CAMRAD II manual [23].

图片摘要：该图主要展示 13 shows the blade loci of the quarter chord, leading edge, 。
![](images/526c27cb7faad35d354694515b857d31ff72a7de93935559932dac518a1b8eb2.jpg)  
Figure 14. Example format of (partial) C81 airfoil data file.

The C81 files are obtained from the Aeromechanics Branch at Ames Research Center [16]. According to experienced XV-15 researchers, the best available airfoil data set consists of four airfoils. The dataset is obtained using two-dimensional wind tunnel tests at full scale. The airfoil at radial station $r / R = 0 . 2 5 0 0 \left( \sim \right)$ is copied to the root value at the cutout, marked with the “*” in Table 2.

# XV-15 Performance Data

The XV-15 rotor is used for this research because of the existing test data (wind tunnel and flight) and nonproprietary, publically available data. The XV-15 flight test data reports provide background in understanding the XV-15 and its performance [24].

XV-15 outdoor hover tests at Ames Research Center have been documented by Felker and Betzina [21]. This data set was acquired on the Outdoor Aerodynamic Research Facility (OARF) test bed and is referred to as the “OARF Data” later in this report. This is believed to be the only full-scale data without wall effects for an XV-15 isolated rotor in hover. The Bell Helicopter company performed a study on the performance of an XV-15 isolated rotor in the NFAC facility [22] under various conditions including edgewise and airplane mode. Johnson performed an assessment of the capability to calculate tiltrotor aircraft performance from this report [25]. It is unknown to what extent these results are influenced by the wind tunnel walls.

Theoretical results obtained with CAMRAD I are also acquired from reference [25]. The hover case results from CAMRAD II [23], the improved version, are obtained as well. While sharing many characteristics with earlier versions of CAMRAD, CAMRAD II is completely recoded and has far more advanced options for computing rotor performance, loads, stability, etc. For predicting isolated proprotor performance, the most significant change is the introduction of stall-delay models. Here, the model developed by Corrigan and Schillings [26] is used.

It is these two reports (references [21] and [25]) and the hover performance from CAMRAD II [16], [23] that form the main basis for the validation of the rotor model to be developed. Because the V-22 Osprey data is not publically accessible, this is also the only tiltrotor reference data available to validate the code. All performance data is obtained at sea level. The flight tests are assumed to be performed at a low enough altitude to render comparisons with data obtained from sea level reasonable.

# Hover

Figure 15 and Figure 16 show the power curve and figure of merit versus blade loading, respectively. The thrust and power are expressed as their nondimensionalized coefficient values, divided by the rotor solidity. The theoretical power curves obtained from CAMRAD I and CAMRAD II show good agreement with various wind tunnel tests (WTTs), flight data, and the OARF data. Both curves and the corresponding data show an almost linear relation along the blade loading observed.

The data points from the CAMRAD and OARF data are shown for the figure of merit plot in Figure 16. A considerable increase in scatter among the data points is observed. The figure of merit is defined as the ratio of induced power over total power, as shown in Equation (14) [27].

$$
M = \frac {P _ {i}}{P _ {i} + P _ {o}} = \left(1 + \frac {P _ {o}}{P _ {i}}\right) ^ {- 1} = \left(1 + \frac {P _ {o}}{T v _ {i}}\right) ^ {- 1} = \left(1 + \frac {C _ {P o} \sqrt {2}}{C _ {T} ^ {3 / 2}}\right) ^ {- 1} \tag {14}
$$

The peak of the curve consequently corresponds with a relative decrease of the induced power, thus the total power is relatively increasing. This usually is the point where a significant section of the blade is stalling and therefore the figure of merit, a measure for efficiency, drops.

图片摘要：该图主要展示 15. XV 15 rotor hover power as a function of thrust [16], [2。
![](images/bd9ff793be0ac9895d2f3dec0ed5d5622866aeb67e05104a3e0141cb9db4857f.jpg)  
Figure 15. XV-15 rotor hover power as a function of thrust [16], [21], [25].

图片摘要：该图主要展示 15. XV 15 rotor hover power as a function of thrust [16], [2。
![](images/ac5de718b5548d1f66a1ffd6643bd8b9fc8c3519991e64ccb4e45a5b374ea2dc.jpg)  
Figure 16. XV-15 rotor hover figure of merit as a function of thrust [16], [21], [25].

It is thought that the scatter along the figure of merit values is closely related to difficulties in obtaining clean power values in experiments or accurate drag values in theoretical analyses.

# Tilt

Several cases for a tilted rotor are observed in Figure 17. The pylon angle, $\begin{array} { r } { \alpha _ { p } , } \end{array}$ indicates the angle of the pylon, and rotor disk, to the relative wind velocity. For airplane or axial mode, $a _ { p } = 0$ (deg), and for helicopter or edgewise flight, $a _ { p } = 9 0$ degrees. The data is shown to deviate the most from theory at a pylon angle of $a _ { p } = 7 5$ degrees, attributed to deficiencies in the stall computation of CAMRAD I [25].

However, it is crucial to note that the experimental values are obtained in the 40- by 80-Foot Wind Tunnel and might themselves exhibit wind tunnel interference effects. The tunnel interference was minimized by using various vents and panels that could be opened, reducing the blockage and alleviating the pressure. This approach was not, however, further investigated throughout this research.

Figure 18 shows the influence of the advance ratio at a pylon angle of $a _ { p } = 7 5$ degrees. In this report the advance ratio is defined as the relative velocity magnitude over the blade tip speed, as shown in Equation (15).

$$
\mu = \frac {V}{\Omega R} \tag {15}
$$

The variation of advance ratio shows a consistent slope, but a diverging correlation as the advance ratio is increased. This deviation is thought to be attributable to the stall model in CAMRAD I and can serve as a key comparison to rotor performance obtained with RotCFD.

图片摘要：该图主要展示 18 shows the influence of the advance ratio at a pylon angle。
![](images/3989e0bce535083bc9aced2d123091db8e5d735140eb325d4c5e5ea9a889d740.jpg)  
Figure 17. XV-15 rotor power as a function of thrust for different pylon angles at $V / \Omega R = 0 . 3 2$ [25].

图片摘要：该图主要展示 17. XV 15 rotor power as a function of thrust for different 。
![](images/8f1a51bf73ec2026d64a59ff8c43bc9aa8271e365eca398df3adfbfe8bf4bfcf.jpg)  
Figure 18. XV-15 rotor power as function of thrust, for $\alpha _ { p } = 7 5 ^ { \circ }$ and $M _ { t i p } = 0 . 6 5$ [25].

图片摘要：该图主要展示 18. XV 15 rotor power as function of thrust, for and [25]。
![](images/4643b003b98ddd1644dde65b6ae3d7e76270238e04ae2f7e82eab2ec3fbea440.jpg)  
Figure 19. Rotor propulsive efficiency as function of thrust [25].

# Airplane Mode

Figure 19 shows the propulsive efficiency versus the blade loading for various tip speeds. The propulsive efficiency is calculated using Equation (16). Note the inherent difference to figure of merit in Equation (14), which uses the induced velocity (evaluating useful power to obtain thrust) instead of the aircraft velocity (useful power to obtain propulsion).

$$
\eta = \frac {T V}{P} \tag {16}
$$

# AERODYNAMIC ANALYSIS METHOD

During this research RotCFD (RotUNS) is used to obtain rotor performance data isolated or in a wind tunnel. The flow is considered incompressible, hence a Mach number in the whole flow field must be lower than $M = 0 . 3 0$ [28].

The rotor is solely modeled through the momentum it imparts on the flow. The rotor data is obtained from two-dimensional airfoil data. It is assumed that this method, combined with airfoil correction methods, yields accurate rotor performance results. Because the rotor is modeled only through the momentum sources, the tip Mach number is never truly present in the flow, only the momentum changes in the surrounding cells. This makes the incompressibility assumption feasible.

It is assumed that all Mach number and Reynolds number effects are considered through the momentum sources. Also dynamic stall effects, radial (boundary layer) flow effects, cannot be properly obtained because there is no physical boundary layer, just the two-dimensional data.

All simulations in this research are performed with SI units at sea level and International Standard Atmosphere (ISA). The values are summarized in Table 3.

TABLE 3. SEA LEVEL AIR PROPERTIES USED  

<table><tr><td>Symbol</td><td>Description</td><td>Value</td></tr><tr><td>T0</td><td>sea level temperature</td><td>288.16 (K)</td></tr><tr><td>P0</td><td>sea level air pressure</td><td>101325 (Pa)</td></tr><tr><td>ρ0</td><td>sea level air density</td><td>1.225 (kg/m3)</td></tr><tr><td>a0</td><td>speed of sound at sea level</td><td>340.29 (m/s)</td></tr><tr><td>R</td><td>gas constant</td><td>287.05 (m2/s2K)</td></tr><tr><td>μ</td><td>dynamic viscosity</td><td>1.75E-05 (m2/s)</td></tr><tr><td>γ</td><td>ratio of specific heats</td><td>1.4 (~)</td></tr></table>

# XV-15 Airfoil Data Corrections

This section describes the airfoil data corrections performed on the XV-15 rotor model. For hover the inclusion of unsteady aerodynamics and yawed flow aerodynamics has little effect on rotor thrust [26]. Furthermore, it is assumed unsteady aerodynamics and yawed flow aerodynamics are covered to some extent in RotCFD’s flow field computation. The other two main sources of inaccuracies are the stall delay effect and tip loss effect, both described in the following subsections. For forward flight, unsteady aerodynamics and yawed flow effects are sufficient [26].

# Stall Delay Model

The effect of a rotor’s rotation on the boundary layer is crucial for obtaining the correct performance prediction of a rotor [26], primarily during hover. Because the aerodynamic data files provide the properties of the rotor, the boundary layer is not resolved during the simulations. Therefore, the only way of accounting for the boundary layer rotational effect is to alter the C81 airfoil data tables.

Acree describes modeling requirements for analysis and optimization of the Joint-service Vertical take-off/landing Experimental aircraft (JVX) proprotor performance [29]. A similar approach is used by altering the airfoil data tables and applying stall delay according to the Corrigan and Schillings stall delay model [26]. The Corrigan stall delay model uses augmentation of the lift values in the C81 airfoil data tables by multiplying the section lift coefficient with a stall delay factor, $K _ { L }$ .

Radial flow along the blade span retards the point where the boundary layer breaks, which delays stall and, therefore, the maximum lift coefficient. Equation (17) shows the computation of the Corrigan stall parameter [30].

$$
K _ {L} = \left(\frac {c / r}{. 1 3 6} \left(\frac {. 1 5 1 7}{c / r}\right) ^ {1 / 1. 0 8 4}\right) ^ {n} = (1. 2 9 1 (c / r) ^ {. 0 7 7 5}) ^ {n} \tag {17}
$$

The exponent $n$ varies from 0.8 to 1.8, with larger values usually giving better correlation [16]. Using $n = 1 . 8$ for that reason, the $K _ { L }$ values obtained are found in Figure 20.

图片摘要：该图主要展示 20. Spanwise Corrigan stall delay parameter obtained for XV 。
![](images/1471b2aba26d954fcc1fb41e31c40f403162cfcea71962d40999a5403479d582.jpg)  
Figure 20. Spanwise Corrigan stall delay parameter obtained for XV-15 rotor model.

Although the largest effect of stall delay is seen near the root, the tip also shows significant stall delay using this model. For Corrigan stall delay, the stall delayed lift coefficient is obtained in Equation (18).

$$
c _ {l} = K _ {L} c _ {l, \text {t a b l e}} \text {f o r} 0 ^ {\circ} <   \alpha <   3 0 ^ {\circ} \tag {18}
$$

The stall delay is applied from 0-degree angle of attack until 30-degrees angle of attack. From 30 to 60 degrees, the model is washed out using the washout, w, as shown in Equation (19).

$$
w = \left(\frac {6 0 - | \alpha |}{3 0}\right) \tag {19}
$$

The lift for an angle of attack between 30 and 60 degrees can now be derived as shown in Equation (20). Over the angles of attack until 60, the lift coefficient approaches the regular $c _ { l }$ again. After 60 degrees no correction is applied.

$$
c _ {l, \text {w a s h o u t}} = \left(w \left(K _ {L} - 1\right) + 1\right) c _ {l, \text {t a b l e}} \text {f o r} 3 0 ^ {\circ} <   \alpha <   6 0 ^ {\circ} \tag {20}
$$

The stall delay is only applied for positive section lift that is assumed to occur above an angle of attack of 0 degrees. It was found the zero-lift angle of attack was close to, but not exactly equal to, zero, and therefore small errors in the stall delay model might be introduced. However, these errors are found to be negligible as the section lift within the angle of attack range from 0 degrees to the zero-lift angle of attack is very small. Comparison of the empirical model with experimental and theoretical data is presented in the original paper [26].

# Tip Loss Model

Similar to aircraft wings, trailed vortex inflow over the tip of a rotor blade reduces its lifting capability. The RotCFD rotor model does not take this fully into account because it uses twodimensional airfoil data and thus is likely to experience some section lift up to the blade tip. However, the flow field environment of RotCFD alters the relative velocities experienced by the blade.

Leishman [31] describes an effective blade radius, or Prandtl tip loss factor, $B$ ,—usually around 98 percent of the blade radius—that is unaffected by tip loss, as shown in Equation (21). This means the effective blade radius, $R _ { e , \astrosun }$ is a reduction of the actual blade radius, $R$ , (in terms of lift coefficient) based on the tip loss factor, $B$ . The lift at the remaining 2 percent of the blade is set to zero at the tip.

$$
R _ {e} = R B \tag {21}
$$

# C81 Airfoil Adjustment Code

The C81 data for the XV-15 airfoils vary almost linearly with radius, but the stall delay is nonlinear, as shown in Figure 20. Because the stall delay is spanwise nonlinear, the radial stations have to be interpolated—even if the spanwise lift distribution is fairly linear. The airfoil data consists of the lift, drag, and moment coefficients specified for a range of angles of attack and Mach numbers. A code is written to perform a triple interpolation over angle of attack, Mach number, and radial station. The interpolation over angle of attack and Mach number is necessary to make sure that the radial interpolation can be properly evaluated. Once the angle of attack and Mach number matrix data is uniform for all three coefficients over the radial stations, the Corrigan stall delay model is applied over a user-defined set of blade stations.

Figure 21 shows a representative set of coefficients versus angle of attack or Mach number imported for the tip airfoil, the NACA 64-X08 (C81) airfoil data file. For the other airfoils, representative plots are shown in Appendix B.

For all airfoil files the angle of attack data is very well organized, showing high density of data points around the crucial areas. The Mach number data points are, however, less numerous, especially for the root airfoils because they experience a lower relative Mach number.

The green lines in the graph show the interpolation by the code. Because of the numerous data points for the angle of attack, the interpolation is done using a Piecewise Cubic Hermite Interpolating Polynomial (PCHIP) interpolation. This method was found to give the most “natural” interpolation of the rather unpredictable behavior of the curves. It was not found to work well for the interpolation of Mach number data points. Here the PCHIP method could be unpredictable if one data point showed an abrupt deviation of the trend as, for example, the case in Figure 21d. Therefore, the Mach number interpolation is done using a simpler linear interpolation. The following radial interpolation was also done linearly. The interpolated lift curve is colored green in Figure 21. Figure 21a shows a clear stall region, albeit at a higher angle of attack than is usually the case for aircraft wings, attributable to the relatively thick blades. The blade thickness also results in the relatively gradual stall observed. The drop of the lift coefficient in Figure 21d shows the compressibility effects

becoming troublesome. The spike in drag in Figure 21e and the drop in moment coefficient in Figure 21f show the results of the corresponding drag divergence, respectively. The stall delay and tip loss models only affect the lift coefficients, and they are therefore the focus variable in the remainder of this section. Figure 22 shows a simplified flowchart of the whole code for the airfoil adjustment, including the import, the interpolation along angle of attack, Mach number and radial stations, the stall delay and tip loss model implementation, and the re-exporting to C81 format.

The following steps are covered in the code:

1. Start;   
2. Import C81 airfoil data files and verify the radial position of the airfoils;   
3. Decompose the C81 files into matrices for easy manipulation;   
4. Interpolate the angle of attack using PCHIP interpolation for all coefficients;   
5. Interpolate the Mach number linearly for all coefficients ;   
6. Interpolate the radial stations for all coefficients;   
7. Apply stall delay, if selected in program;   
8. Apply tip loss factor, if selected in program;   
9. Convert matrices to C81 format and export to *.c81 files;   
10. End.

图片摘要：该图片与10. End；9. Convert matrices to C81 format and export to .c81 files;这部分内容相关。
![](images/d1c59d1085fd21469fe642caca240d291fe88525424da6ef248ba8498df95252.jpg)

图片摘要：该图片与10. End；9. Convert matrices to C81 format and export to .c81 files;这部分内容相关。
![](images/9bdc9367a4aabff45235901c8159a68f359ddaa1bf46f1118bb3843a54031f50.jpg)

图片摘要：该图主要展示 21. AoA and Mach interpolation for representative cases of t。
![](images/1d770ea8bae28715266f19d3e3ac72e095157d17ee5a4a82fe559761a84cc242.jpg)

图片摘要：该图片与Figure 21. AoA and Mach interpolation for representative cases of the NACA 64 X0这部分内容相关。
![](images/7a6a057ee73896bada8d0f5e35ea08b658f1bd4ba492f7bf5e36b0c0fad9d25f.jpg)

图片摘要：该图主要展示 21. AoA and Mach interpolation for representative cases of t。
![](images/a0f45d628152e21012497820ee6ee9c677c5f006efbf49eea027af448609b503.jpg)

图片摘要：该图主要展示 21. AoA and Mach interpolation for representative cases of t。
![](images/31c4814071573c20050afa9342b921b745b41bc7b54fbdeae5ce82c034fe6d9a.jpg)  
Figure 21. AoA and Mach interpolation for representative cases of the NACA 64-X08 airfoil.

图片摘要：该图主要展示 21. AoA and Mach interpolation for representative cases of t。
![](images/f3f1c466e92669469bb3aa8d0d598695cd585d0da6af990930fe80237695affc.jpg)  
Figure 22. Simplified flowchart of airfoil adjustment code.

Figure 23 shows the spanwise lift coefficient of the original data, the data after angle of attack interpolation and Mach number interpolation, and the data after radial interpolation. The lift coefficient is primarily discussed because both the stall delay and tip loss models only affect the lift coefficient. Note that the vectors specifying the remapping of the angle of attack, Mach number, and radial stations are user specified. The plot is shown for a Mach number of $M = 0 . 3 0$ for continuous zero twist. Therefore, these are not the actual lift coefficients that the blade would exhibit because it exhibits substantial twist as shown in Figure 11.

The results of the stall delay both for angle of attack and Mach number for various representative radial stations are shown in Figure 24. The effects of the model are clearly observed. Figure 24f is evaluated for a negative angle of attack where no stall delay should be present. This is confirmed by the identical curves before and after model application.

Tip loss is applied at $r / R = 9 8$ percent by setting the lift coefficient to zero after $r / R = 9 8$ percent. This drop occurs instantaneously [32] and is programmed to happen between $r / R = 0 . 9 8$ and $r / R = 0 . 9 8 1$ . The final result before stall delay and tip loss compared to the unaltered interpolated data is shown in Figure 25. This plot is shown for zero continuous twist at $M = 0 . 3 0$ and clearly demonstrates the effect on lift coefficient of the application of both models.

The models are tested independently during the validation of the rotor model in RotCFD.

图片摘要：该图主要展示 23 shows the spanwise lift coefficient of the original data,。
![](images/ac27df1679504c2b4c1a4855ec5912d5699dd3d6a8c337227994f06d207e013c.jpg)  
Figure 23. Radial interpolation check of lift coefficient at $M = 0 . 3 0$

图片摘要：该图主要展示 23. Radial interpolation check of lift coefficient at。
![](images/93274d20a5be74d8eac297b51795b6731720b7042562c3cafc08cb599cfcc609.jpg)

图片摘要：该图主要展示 23. Radial interpolation check of lift coefficient at。
![](images/61b0f17f4e819ef36521e31473d06fef9429d446961e50b445e36de100aa588e.jpg)

图片摘要：该图主要展示 23. Radial interpolation check of lift coefficient atFigure 。
![](images/942910080be2d1158deeafc097d5e4b8a05619876547fed5d979a635f1232439.jpg)

图片摘要：该图主要展示 23. Radial interpolation check of lift coefficient atFigure 。
![](images/9f1a98e37094c3323e43511efada2677fa891184c2785beab6743752199c3d1c.jpg)

图片摘要：该图主要展示 24. Stall delay as a function of angle of attack or Mach num。
![](images/78b92f5d0346cda2f7e28e2fb70ae4042214fdb045c94c7fd29a177df5789b20.jpg)

图片摘要：该图主要展示 24. Stall delay as a function of angle of attack or Mach num。
![](images/2a1654228e749ec3fe9edaaefba9b42a96fed9a09ed5b2c757772634b9616dae.jpg)  
Figure 24. Stall delay as a function of angle of attack or Mach number for various radial stations.

图片摘要：该图主要展示 24. Stall delay as a function of angle of attack or Mach num。
![](images/21ec5c9b2389fcfab6426bc6135d1e68bfa90dd5d5cad2c2d4dcb967bda45a5f.jpg)  
Figure 25. Lift coefficient as a function of radial station at $M = 0 . 3 0$ at continuous zero pitch angle.

# General Setup of Validation Cases

The setup of the boundaries and gridding of the flow field is kept consistent through the validation cases. The boundaries consist of a rectangular prism with x-, y-, and $z$ -dimensions of 10D, 10D, and 15D, respectively, with $D$ being the rotor diameter. The rotor is placed in the center of the XY-plane and 5D in negative z-direction from the top plane. Note that positive $z$ is aligned with thrust to eliminate any influence from the ground plane. The cell count is roughly between one and two million cells, depending on the case. The RotCFD user interface is shown in Figure 26 for a hover case: two side views of the applied gridding are shown in Figure 27a and Figure 27b. An overview of the validation of the isolated rotor cases is also published by Koning, Acree, and Rajagopalan [33].

# Boundary Settings

For a hover case all boundaries are pressure boundaries except for the plane in wake direction that is set to a mass outflow boundary correction. Cases where a free-stream velocity is present have according velocity boundary corrections and a mass outflow boundary in the direction of the wake.

图片摘要：该图主要展示 26. RotCFD user interface with a hover case loaded。
![](images/ae0764edda50259733ab2ce6998012b0b57e5f249bbec8250a4fbf2c77992ff2.jpg)  
Figure 26. RotCFD user interface with a hover case loaded.

图片摘要：该图主要展示 26. RotCFD user interface with a hover case loaded。
![](images/414167c1153e56c6035c601a64615c2644e7987b714aa9dc986bbc21864fb190.jpg)

图片摘要：该图主要展示 26. RotCFD user interface with a hover case loaded。
![](images/dabdc2711aa733eda327d00eebe7406d9c62c772ed32862e2a1a61b3062d6151.jpg)  
b)   
Figure 27. Hover case, gridded centered side view (XZ) of the flow field. Hover case, gridded top view (XY) at rotor height.

# Spatial and Temporal Resolution Independency

For all flight modes, spatial and temporal resolution independency was checked by observing the performance parameters power, thrust, and figure of merit to be independent of the chosen cell size and time step. A refinement box was used to confine the rotor in order to improve the result for the smallest cell count. The smallest cell size, found at the rotor disk itself, was equivalent to roughly 8 (cm), whereas the time step for the validation with the steady model was set at 1/400 (s) and the time step for the unsteady model ranged between 1/800 (s) and 1/1200 (s). For the unsteady model, this corresponds to approximately 3 degrees of rotor rotation per time step.

# NFAC WIND TUNNEL CASES SETUP

After the validation the interference in both wind tunnels of the National Full-Scale Aerodynamics Complex (NFAC) at Ames Research Center was examined. The two wind tunnels that comprise the NFAC facility share portions of their flow path. The cross section of the 80- by 120-Foot Wind Tunnel is an open circuit wind tunnel with a closed, rectangular test section. The 40- by 80-Foot Wind Tunnel is a closed-section wind tunnel with an oval test section. For this research it is assumed that the operating conditions are all fixed and at sea level.

The k-ε turbulence model is primarily known for circulation in large areas; a wall function is added for more accurate velocity profiles near no-slip conditions at walls or other surfaces. No effort was made to investigate the effect of a chosen turbulence model versus a laminar approach or other turbulence models.

Only the test section is modeled with constant cross-sectional area. In real life, the test section of the open circuit 80- by 120-Foot Wind Tunnel always experiences influence from outside turbulence. The vane sets and the developed boundary layer and the flow are therefore not uniform. Similarly, the test section of the closed-section 40- by 80-Foot Wind Tunnel is likely, despite the air exchange system, to contain nonuniform flow because of “old” disturbed air from the model. Disturbances can also occur at the test section inflow because of turbulent air from the tunnel walls, vane sets, etc. To reduce the complexity of this research however, the inflow conditions were chosen to be uniform at the test section inlet.

The lengths of the test sections were increased from their real values to eliminate influence on the rotor performance due to the imposed boundary conditions at the inlet and outlet. The test section elongation for both test sections is sketched in Figure 28, with the positive x-direction corresponding to the wind tunnel flow direction. For this research both test sections of the NFAC are therefore modeled as an open tunnel with a closed test section. The pressure was not disturbed around a distance of 2 to 3 rotor diameters from the inlet to the TTR. A render of the TTR in the 40- by 80-Foot Wind Tunnel test section during airplane mode and edgewise flight is shown in Figure 29.

Small features such as pressure tabs, ramps, or the faceting of the acoustic lining are assumed to have negligible influence on the results of this study and are not modeled. The slight faceting on the 40- by 80-Foot Wind Tunnel is ignored and the cross section is assumed to have semicircular walls.

图片摘要：该图主要展示 28. The boundaries of the test sections with TTR in edgewise。
![](images/c0c1b9463e89d5bb9d154fcbad2dde6f7f53d655f8f85611aa5e995307af52f3.jpg)  
Figure 28. The boundaries of the test sections with TTR in edgewise and axial mode.

图片摘要：该图主要展示 28. The boundaries of the test sections with TTR in edgewise。
![](images/a0124c4c529eb1796e551c8aef4ddca7be1660e21bc467cec87a21a62cda16f0.jpg)  
Figure 29. TTR in 40- by 80-Foot Wind Tunnel cross section shifting from airplane $( \mathfrak { a } _ { p } = 0 ^ { \circ } )$ mode to edgewise flight $( \mathfrak { a } _ { p } = 9 0 ^ { \circ }$ ).5

The XV-15 is modeled on the Tiltrotor Test Rig (TTR). In 2016 the TTR will be tested in the NFAC facility with the Bell 609 rotor. Rotor forces will be measured on a dedicated balance installed within the TTR, instead of using the wind tunnel balance system; therefore, the rotor performance from the rotor program in RotCFD can be used as the target variable. The wind tunnel turntable can rotate the TTR from axial $( \boldsymbol { a } _ { p } = 0$ degrees) to edgewise flight $( a _ { p } = 9 0$ degrees) and all angles in between. Note that in edgewise flight the thrust is always aligned with the positive y-axis, and in airplane mode the thrust always aligned with the negative x-axis.

The thrust is manually trimmed using the collective setting to make sure values are similar to the validations results and the rotor is not evaluated far into the stall regime.

RotUNS features a tetrahedral body-fitted grid with a Cartesian unstructured grid in the far field. RotUNS does not support viscous body-fitted grids and therefore cannot accurately capture the boundary layer around geometry in the domain. The thickness of the boundary layers is presented in Appendix A for the 40- by 80-Foot Wind Tunnel and the 80- by 120-Foot Wind Tunnel, but to reduce complexity, implementing the effects of the actual tunnel wall boundary layer on the simulation has not been tried. The choice for RotUNS was made because of the developmental stage of the RotVIS module at the time of writing and the belief that RotUNS should be mastered before attempting the use of RotVIS. Because the prime variable is rotor performance, not measured by forces on the body (i.e., TTR and/or struts), it is assumed that the forces are of less importance to the predictions once performance convergence is guaranteed.

A mass outflow condition is used at the end of the test section if positive wind tunnel speed is modeled. For hover cases, a pressure boundary condition is applied to the inlet and outlet. The physical size of the grid relative to the rotor and in the region of the wake is kept identical to the validation cases. The time grid is kept equal to the one used in the validation cases, sometimes

refined to keep stability at the tetrahedral body-fitted cells. Figure 30 shows two representative planes (XZ-plane or side view, and YZ-plane or front view) of a fitted grid in both test sections. Note that the first (side) view is an extended test section to ensure that uniform inflow due to the imposed boundary condition does not alter rotor performance. Lower grid density at the inlet is used to reduce cell count, while the refinement at the walls is maintained, however, to keep an identical stream tube when the no-slip condition at the walls results in velocity gradients over the adjacent cells. The total cell count for both test sections is between 900,000 and 1,200,000.

For each case evaluated there is a set of four tests consisting of the wind tunnel test section with geometry of the TTR and struts (WTGE) and without geometry of the TTR and struts (WTRO). Its free field counterpart without tunnel geometry but with TTR and strut geometry (FFGE) and without the TTR and strut geometry (FFRO) is also modeled for direct comparison of rotor performance. The subsets for each case are summarized in Table 4.

Rotor convergence is case dependent but usually occurs after the equivalent of around 10–15 rotor rotations and remains steady after that because the flow in the vicinity of the rotor is fully developed. This can be observed visually by plotting the velocity and making sure that the wake has progressed at least 1–2 rotor diameters from the rotor disk. Care must be taken to ensure that the rotor in the tunnel test section is effectively placed in a box (and not just in “ground effect”), which complicates the analysis. In some cases the wake might not have fully settled over the remainder of the geometry and thus force convergence on the TTR might not have occurred yet while rotor performance convergence is found.

图片摘要：该图主要展示 30. The extended test sections with TTR on struts and XV 15 。
![](images/e9b3a9ce9a68552f46504a50447dd05f4df4b32e771cce051a8e92bc41c39480.jpg)

图片摘要：该图主要展示 30. The extended test sections with TTR on struts and XV 15 。
![](images/4cace48bd1d6247dae65b716b656cf355c5f8e16968739a85a2ea824d11c2813.jpg)  
Figure 30. The extended test sections with TTR on struts and XV-15 rotor in edgewise and axial mode, respectively.

TABLE 4. OVERVIEW OF FOUR DIFFERENT SUBSETS PER CASE   

<table><tr><td>Case</td><td>Wind Tunnel</td><td>Free Field</td><td>Rotor</td><td>TTR Geometry</td></tr><tr><td>WTGE</td><td>X</td><td></td><td>X</td><td>X</td></tr><tr><td>WTRO</td><td>X</td><td></td><td>X</td><td></td></tr><tr><td>FFGE</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>FFRO</td><td></td><td>X</td><td>X</td><td></td></tr></table>

No automatic rotor trim is available yet in RotCFD at the time of writing, which means that the thrust cannot be automatically maintained constant for each case. Instead the collective is fixed throughout the subsets.

# NFAC 80- by 120-Foot Wind Tunnel Cases

The test section of the 80- by 120-Foot Wind Tunnel is expected to show little or no interference effect, or only under the most unfavorable conditions. Therefore, axial flow at $V = 1 0 0$ (kts), the highest wind tunnel velocity, and edgewise at $V = 0$ (kts) (hover), are the prime test cases. Hover is normally always measured in axial mode for the least obstruction to the inflow and outflow of the rotor. However, the edgewise hover test is still evaluated to show the theoretical worst-case interference. An increase in tunnel velocity in edgewise mode should decrease the interference with the tunnel walls. Therefore, the last case is an edgewise case at low tunnel velocity, $V = 1 0$ (kts), expected to show smaller interference because of the higher tunnel velocity. Table 5 shows the three final cases for the 80- by 120-Foot Wind Tunnel test section.

Case 1, with an “edgewise” hovering rotor, uses a pressure boundary condition at the inlet and outlet. Using the free field as a reference, it is ensured that the imposed pressure boundary is not altering the pressure changes modified by the rotor disk. Cases 1 and 2 use collective settings equal to those used in the validation of the hover performance. Case 3 uses a collective setting roughly equivalent to low thrust, as would be expected for cruise, of around $T \approx 3 0 0 0$ (N). The WTGE cases for case 3, and cases 1 and 2 are shown in Figure 31a and Figure 31b, respectively. The wind tunnel velocity is aligned with the positive x-axis.

TABLE 5. FINAL 80- BY 120-FOOT WIND TUNNEL CASES   

<table><tr><td>Case</td><td>80- by 120-Foot Wind Tunnel</td><td>V (kts)</td><td>αp(deg)</td><td>θo(deg)</td><td>Mtip(∼)</td><td>Airfoil Correction</td></tr><tr><td>1</td><td>edgewise</td><td>0</td><td>90</td><td>4.00</td><td>0.66</td><td>TL, SD</td></tr><tr><td>2</td><td>edgewise</td><td>10</td><td>90</td><td>4.00</td><td>0.66</td><td>TL, SD</td></tr><tr><td>3</td><td>axial</td><td>100</td><td>0</td><td>14.80</td><td>0.53</td><td>TL</td></tr></table>

图片摘要：该图主要展示 5. FINAL 80 BY 120 FOOT WIND TUNNEL CASES。
![](images/92c8c1d0e46e78d28151f23e0b82b0cab11ae9f8316685948fe7f29f4868238c.jpg)  
a)

图片摘要：该图主要展示 5. FINAL 80 BY 120 FOOT WIND TUNNEL CASES。
![](images/a272ea9c68d4aad86a9baf2d30dbe51aed5255bb92396671af7231443e724c3c.jpg)  
b)   
Figure 31. The setup of case 3, WTGE. The setup for cases 1 and 2, WTGE.

# NFAC 40- by 80-Foot Wind Tunnel Cases

The 40- by 80-Foot Wind Tunnel is likely to show interference under a larger set of conditions and is therefore investigated in greater detail. Figure 32 shows the conversion corridor of the XV-15, which indicates the realistic operating conditions for the XV-15 rotor. This is checked to make sure no excessive stall or rotor mode simulation is required.

For edgewise mode a similar case to the 80- by 120-Foot Wind Tunnel is investigated at $V = 1 0$ (kts) as well as a high velocity, $V = 1 0 0$ (kts), case. Figure 33 shows the height-velocity envelope of the XV-15.

图片摘要：该图主要展示 31. The setup of case 3, WTGE. The setup for cases 1 and 2, 。
![](images/e978ec75df9a66616a9ee1e6e05e5dfb028073f95c8bf35a1b7608cb722ebe11.jpg)  
Figure 32. Conversion corridor of the XV-15 [18].

图片摘要：该图主要展示 32. Conversion corridor of the XV 15 [18]。
![](images/22069851ca0536150c60aaebeec58703bd089626bef68b93cd6a1ee7f63eebcd.jpg)  
Figure 33. XV-15 height-velocity envelope [18].

The torque limit sets the cruise velocity at sea level at around $V _ { t a s } = 2 5 0$ (kts). The 40- by 80-Foot Wind Tunnel can run in excess of $V = 3 0 0$ (kts), but the incompressible solver is limited to Mach $=$ $0 . 3 \ : ( \sim )$ to avoid compressibility effects [28]. Therefore, the axial mode at high speed is considered at $V = 2 0 0$ (kts). The FFGE setup of cases 4 and 5 is shown in Figure 34. Positive wind tunnel velocity is always aligned with the positive x-axis.

Finally, a tilted case with $a _ { p } = 6 0$ degrees is used to check the influence of the rotor disk advancing closer to the curved test section wall at $V = 1 0 0$ (kts). The WTGE subsets of the edgewise and tilt mode are shown in Figure 35a and Figure 35b, respectively. The final cases are summarized in Table 6.

图片摘要：该图主要展示 33. XV 15 height velocity envelope [18]。
![](images/3fb2f042db4d2a768e757f474d1b0c8cb927c8c1f4d4a6a5bf0885a9b1899177.jpg)  
Figure 34. The geometry for cases 4 and 5, FFGE.

图片摘要：该图主要展示 34. The geometry for cases 4 and 5, FFGE。
![](images/7c5fc92e5799af6a18337a124d1f3d8844d93dc1eec04f65a27baba148efcabc.jpg)  
a)

图片摘要：该图主要展示 34. The geometry for cases 4 and 5, FFGE。
![](images/5bbfe49b3150c1c716f9e23e208484bb1a0a69c1df844b1622a302569c667749.jpg)  
b)   
Figure 35. The geometry and grid for case 6, WTGE. The geometry for case 7, WTRO.

TABLE 6. FINAL 40- BY 80-FOOT WIND TUNNEL CASES   

<table><tr><td>Case</td><td>40- by 80-Foot Wind Tunnel</td><td>V (kts)</td><td>αp(deg)</td><td>θo(deg)</td><td>Mtip(∼)</td><td>Airfoil Correction</td></tr><tr><td>4</td><td>edgewise</td><td>10</td><td>90</td><td>4.00</td><td>0.66</td><td>TL</td></tr><tr><td>5</td><td>edgewise</td><td>100</td><td>90</td><td>1.00</td><td>0.66</td><td>TL</td></tr><tr><td>6</td><td>axial</td><td>200</td><td>0</td><td>32.68</td><td>0.53</td><td>TL</td></tr><tr><td>7</td><td>tilt</td><td>100</td><td>60</td><td>8.00</td><td>0.65</td><td>TL</td></tr></table>

# VALIDATION OF XV-15 ROTOR MODEL

The thrust, power, and figure of merit are obtained from RotCFD. The figure of merit is extracted directly from RotCFD. The full data table for the steady results is included in Appendix C. All plots for the unsteady model and full data table are included in Appendix D. Table 7 provides the RotCFD temporal settings, total grid sizes, domain dimensions, and wall boundary conditions for the hover, tilt-, and airplane-mode calculation for the steady calculations.

TABLE 7. RotCFD STEADY SIMULATION PARAMETERS FOR THE XV-15 ROTOR [33]   

<table><tr><td></td><td>Hover</td><td>Tilt Mode</td><td>Airplane Mode</td></tr><tr><td>Tip speed (m/s)</td><td>225.55</td><td>221.17</td><td>183.76</td></tr><tr><td>Number of time steps</td><td>1000</td><td>500</td><td>500</td></tr><tr><td>Step size (degrees azimuth)</td><td>8.5</td><td>8.3</td><td>6.9</td></tr><tr><td>Number of rotor revolutions</td><td>23.6</td><td>11.5</td><td>9.6</td></tr><tr><td>Total number of grid cells</td><td>1,053,948</td><td>2,029,692</td><td>2,029,692</td></tr><tr><td>Computational domain (relative to rotor center):</td><td></td><td></td><td></td></tr><tr><td>±x/R</td><td>±10</td><td>±10</td><td>±10</td></tr><tr><td>±y/R</td><td>±10</td><td>±10</td><td>±10</td></tr><tr><td>±z/R</td><td>±10,-8</td><td>±10,-18</td><td>±10,-18</td></tr><tr><td>Wall boundary conditions</td><td></td><td></td><td></td></tr><tr><td>min x/R</td><td>pressure</td><td>Vx=Vy=0; Vz=-V∞</td><td>Vx=Vy=0; Vz=-V∞</td></tr><tr><td>max x/R</td><td>pressure</td><td>Vx=Vy=0; Vz=-V∞</td><td>Vx=Vy=0; Vz=-V∞</td></tr><tr><td>min y/R</td><td>pressure</td><td>Vx=Vy=0; Vz=-V∞</td><td>Vx=Vy=0; Vz=-V∞</td></tr><tr><td>max y/R</td><td>pressure</td><td>Vx=Vy=0; Vz=-V∞</td><td>Vx=Vy=0; Vz=-V∞</td></tr><tr><td>min z/R</td><td>mass outflow</td><td>mass outflow</td><td>mass outflow</td></tr><tr><td>max z/R</td><td>pressure</td><td>Vx=Vy=0; Vz=-V∞</td><td>Vx=Vy=0; Vz=-V∞</td></tr></table>

# Hover

The hover performance comparison for the unsteady model in terms of the power curve is shown in Figure 36. It shows serious deviation in excess of 10 percent from the reference data. The orange symbols show results where parameters were changed in an effort to find the cause of the inconsistent correlation. In case E1 the grid count was increased from 1.3E6 to 4.0E6 cells. In case E2 a (steady) spinner body was included to check if the missing hub geometry showed a large influence because of root losses. Cases E3 and E4 had a significantly increased amount of iterations per time step and a lower relaxation factor, respectively.

Figure 37 shows the same data points but expressed in terms of figure of merit.

The unsteady model again shows serious deviation from the reference data, generally around 10–20 percent. This error is large and does not justify the use of the unsteady model.

Figure 38 shows the results for XV-15 hover performance with the steady model. The correlation is generally good, although the tip loss (TL) model deviates from the reference data. The tip loss and stall delay models combined (TL SD) and the stall delay model (SD) both show good correlation to the OARF data and the CAMRAD II curve.

图片摘要：该图主要展示 38 shows the results for XV 15 hover performance with the st。
![](images/740c3c90b6c01048d82d3dbcff52be18f6cb28a363de2c0cf337edc727104670.jpg)  
Figure 36. Unsteady results for XV-15 rotor hover power as a function of thrust [21], [25].

图片摘要：该图主要展示 36. Unsteady results for XV 15 rotor hover power as a functi。
![](images/56312dd4c36320ac0d1cc413552b9916644c9bb0fef3f6cbfbc6f0b8863f9c35.jpg)  
Figure 37. Unsteady results for XV-15 rotor hover figure of merit as a function of thrust [21], [25].

图片摘要：该图主要展示 37. Unsteady results for XV 15 rotor hover figure of merit a。
![](images/e71a50930d0daba7087cd711d5365c01bf4f1460031f4efa88ca96baf61af15d.jpg)  
Figure 38. Steady results for XV-15 rotor hover power as a function of thrust [16], [21], [25].

Figure 39 shows the same data points for figure of merit. In this plot it is clear that the stall-delayonly model has the best correlation with the OARF data points. Assuming that the OARF data points are the most accurate dataset, the estimation of highest figure of merit is most accurate using RotCFD. For the chosen tip speed no more OARF data points are available, but CAMRAD II shows serious stall effects as the curve steeply drops towards the higher thrust values. The stall-delay-only model clearly does not show a similar severe drop in performance towards the higher thrusts.

图片摘要：该图主要展示 39 shows the same data points for figure of merit. In this p。
![](images/c3bf315ead578b59c4c15900db15655d7afc35a3c9cd92afedc76a6c7aaa8b90.jpg)  
Figure 39. Steady results for XV-15 rotor hover figure of merit as a function of thrust [16], [21], [25].

The steady model, in contrast to the unsteady model, shows a fairly good correlation with the reference data and has therefore been chosen as the model for the wind tunnel simulations. The thrust and power as a function of collective, for both the steady and unsteady models, are shown in Figure 40 and Figure 41, respectively, in an effort to find the source of the deviation of the unsteady model. It clearly shows the deviation in performance between both models, but no tested explanation has been found yet.

图片摘要：该图主要展示 39. Steady results for XV 15 rotor hover figure of merit as 。
![](images/6e31ca03a9867506fb9a3b0f57848fbab9c09b973b41e13ba55e9bc79b20806e.jpg)  
Figure 40. Rotor thrust as a function of collective pitch angle.

图片摘要：该图主要展示 40. Rotor thrust as a function of collective pitch angle。
![](images/4d638bf5edeb64665ce5e3e14b8fd3cfc1091a84bd4408dc1e0d3d7bbb4bf3e8.jpg)  
Figure 41. Rotor power as a function of collective pitch angle.

Further work could include azimuthal check of lift, angle of attack, and rotor conditions to determine why the power is higher using the unsteady model. The lower figure of merit suggests a lower efficiency and likely a larger stalled area of the rotor blade.

# Tilt Mode

The evaluation of different pylon angles in tilt mode using the steady model is quite successful. No stall delay is applied on models except for hovering rotors. Figure 42 shows good correlation for all pylon angles up to $a _ { p } = 7 5$ degrees. The difference is noticeable in the CAMRAD I results. The influence of tip loss factor is minimal.

Figure 43 shows the sensitivity to aspect ratio changes. The rotor model seems to perform well even up to the most severe aspect ratio tested. The influence of tip loss factor is minimal.

Because of the relatively low thrust and high aspect ratios, the induced velocities at the tip are smaller, and therefore show almost no influence of the tip loss factor in strong contrast to the hover cases. Because the difference is so small, the computational budget was chosen to be saved and not all cases were simulated for both models.

图片摘要：该图主要展示 43 shows the sensitivity to aspect ratio changes. The rotor 。
![](images/c4e2338991da018ce433a30dadd473b0eb022aa332d4ce7b07dd0d3daca1befe.jpg)  
Figure 42. Steady results for XV-15 rotor power as a function of thrust for various pylon angles at $V / \Omega R = 0 . 3 2$ [25].

图片摘要：该图主要展示 42. Steady results for XV 15 rotor power as a function of th。
![](images/49186fb34b402da80b3fb82ec6abe6fe3c6bb7d58c40b99b7b3fb9964dec27fe.jpg)  
Figure 43. Steady results for XV-15 rotor power as a function of thrust, for $\alpha _ { p } = 7 5 ^ { \circ }$ [25].

# Airplane Mode

The final validation case comprises two different tip speeds in axial, or airplane, mode. Correlation is very promising compared to the CAMRAD I curves as shown in Figure 44.

# Ground Effect Study

Je Won Hong from the University of Illinois at Urbana-Champaign offered his help during his internship at Ames Research Center. Under guidance of the author, he investigated the XV-15 rotor, identical to the one used throughout this research, in ground effect. For this study he used the ideal power as this was the case for the theoretical reference models presented in literature [34]. Hong’s work [35] confirms that RotCFD shows expected behavior of rotors operating in ground effect as exhibited in Figure 45.

# Discussion on Airfoil Data Correction

The original tip loss model and stall delay model, and their combinations, were examined in the present validation. The sections below include a discussion on the validity of the models and the obtained results.

# Tip Loss Factor

It is likely that some of the three-dimensional effects of the tip (or root) of the rotor are accounted for. Because the “conventional” tip loss model is applied on top of that, it is expected that the model overcompensates. As can be seen for both the steady and unsteady results, the tip loss factor has a rather detrimental effect on figure of merit and power curve during hover. In particular, the figure of merit plots in Figure 37 and Figure 39 clearly show this influence. The tip loss influence is considerably less during lower thrust modes, for example during airplane mode.

图片摘要：该图主要展示 44. Steady results for (rotor) propulsive efficiency as a fu。
![](images/25477d75c9c1c973d82a4dd4adee97b88ebf5756a4ae7ba25acd4b67199145fe.jpg)  
Figure 44. Steady results for (rotor) propulsive efficiency as a function of thrust [25].

图片摘要：该图主要展示 44. Steady results for (rotor) propulsive efficiency as a fu。
![](images/a0726f44fcd5652f1ed9ac41680ac23b20992ddedc42b20b6f9767b27e5881d9.jpg)  
Figure 45. Evaluation of the XV-15 rotor in ground effect in RotCFD [35].

There are a couple of factors that influence the tip loss: first is the three-dimensionality of the blade tip aerodynamics or the induced velocity due to trailing vortices. Secondly, because of the finiteness of the blade, there is a pressure equalizing effect between the surfaces of the blade or rotor disk.

The first factor is usually present only in the unsteady model, whereas the second factor is applicable to both models. A further investigation of the tip loss model could yield better results. The main problem in RotCFD is thought to be the accurate computation of the angle of attack near the root or hub and its spanwise variation. Figure 46 shows a sketch of a typical observed difference in blade loading during hover between a traditional BEM, RotCFD, and an actual blade loading.

图片摘要：该图主要展示 45. Evaluation of the XV 15 rotor in ground effect in RotCFD。
![](images/c478b520c7c3af96e6884674876d4f4c4f09fe32829849d09e64f747d1c4eccd.jpg)  
Figure 46. Sketch of blade loading characteristics.

# Stall Delay Factor

The stall delay factor is applied because of radial flow of the boundary layer that delays the onset of stall on the blade, particularly near the root of the blade. Because the rotor model only accounts for normal and tangential source components, the radial direction is not taken into account.

Furthermore, it would be very difficult, if not impossible, to create a similar system to also include radial boundary layers, because they would not be oriented in the direction of the main flow, and would be over relatively large lengths (the blade span) and therefore highly unpredictable.

The Corrigan and Schillings stall delay model used is only valid for hover, and it shows very good agreement with experimental and theoretical data. Although methods for (partial) stall delay in other flight modes exist, they were not pursued during this research.

# Accuracy and Precision

An important factor in any simulation is the error observed. If there is a dataset that can be considered a benchmark, the error can be calculated; this is, however, easier said than done.

First of all, each data point represents a collective angle with a combined thrust and power variable. In past research, however, this collective angle has usually been neglected because to date no program is able to accurately match collective setting with thrust and power [16]. A simulation can, however, produce an accurate data point on the power-thrust curve, despite the slight mismatch in collective angle.

Without a way to directly compare data points, another possibility is to compare the RotCFD data points with a curve through the reference data. Neither RotCFD, or the reference data, however, tend to have enough data points to justify a curve fit. The curve fit would also be subjective because no fitting technique is defined. Another problem is that there is no way to know if the power, thrust, or a combination of both, generated the errors observed.

The RotCFD data for the unsteady model shows good precision in general; any deviation from the reference data seems constant over the modeled thrust range. To get a first indication of the errors involved, a very basic analysis was performed. By taking a representative thrust location on the curve and individually checking the error in power as well as the error in thrust, percentage errors can be obtained that serve as an indication of accuracy. These offsets were around 3 percent for hover, 5 percent for tilt, and 5 percent for airplane mode. The maximum figure of merit was 0.6 percent off from the value listed in the OARF data, which is exceptionally high even for full NS codes and is thought to be coincidentally accurate.

However the precision, not the accuracy, could be considered of higher importance. The precision is a measure of the consistency of the results and is associated with random errors. For the wind tunnel cases, performance differences are obtained by finding the disparity between two cases; this means the precision is considered more important than the accuracy. However no way was found, for the same reasons mentioned above, to obtain a quantitative value of the precision without introducing new unknown errors into the data.

# Residual Values

Most simulations for hover, tilt, or airplane mode show very similar characteristics in terms of residuals. Figure 47 shows the moving average (MA) for the residuals of the main flow variables for a tilting isolated rotor at 15 degrees pylon angle, as shown in Figure 42. The length scale for the sampling of the moving average is the time-equivalent of one rotor rotation. The grey backgrounds show the original variation of the variables while the colored lines show the moving average (and do not obfuscate all the overlapping values). The logarithm on the y-axis has base 10.

It can be observed that momentum in all three directions shows the largest residual or cumulative error, around 10 degrees, over all the cells. Unfortunately the location of the highest errors in the flow field cannot be determined from this number. The noticeable kink in the residuals slightly before time step 1000 is due to the wake of the rotor hitting the mass outflow boundary plane 10 rotor diameters downstream. Residuals vary greatly with rotor wake development.

Because the validation shows promising results, it is concluded that the magnitude of the residuals, although relatively large sometimes, are not enough to offset the required accuracy for the rotor performance simulations. Increasing the iterations per time step or reducing the delta time reduces the residuals, but no effect on rotor performance is observed. The residual overviews for hover, tilt at a 75-degree pylon angle, and airplane mode are presented in Appendix C.

图片摘要：该图主要展示 47. Residual plot for a tilting isolated rotor at 15 degrees。
![](images/e86ddeee909f4d3a801ea144ecbf83268c1e606d2728454541335673e4c7c365.jpg)  
Figure 47. Residual plot for a tilting isolated rotor at 15 degrees pylon angle.

# Performance Convergence

Performance convergence is found to be relatively robust. The thrust tends to converge rapidly, around the equivalent of 5 rotor rotations, while the power tends to take a little longer. Usually around 10–15 rotor rotations the performance parameters, power and thrust for this research, have fully converged. To measure convergence a code has been written that plots the difference in performance compared to the final (averaged) answer versus time steps; from this plot the percentage error can be determined and used as an indicator for convergence. If the difference is less than 0.25–1.00 percent for a sustained amount of time, the solution is said to be converged. This amount of time is usually up to half of the simulated time: 1500 time steps roughly corresponds to 2 seconds of simulated time, or the equivalent of 20 rotor rotations.

Three performance convergence graphs are shown in Figure 48, Figure 49, and Figure 50, for hover, tilt, and airplane mode, respectively.

图片摘要：该图主要展示 47. Residual plot for a tilting isolated rotor at 15 degrees。
![](images/863765b48bc256a8d22d31bec5bf352d74e6824b05267c2bbaf478787821ec7d.jpg)  
Figure 48. Hover performance convergence over time.

图片摘要：该图主要展示 48. Hover performance convergence over time。
![](images/a7f81bbf896f6b0d3bf25f235fd07e5e3e06d3abc2ce97b7cc885903c5d929a5.jpg)  
Figure 49. Tilt mode (15-degree pylon angle) convergence over time.

图片摘要：该图主要展示 49. Tilt mode (15 degree pylon angle) convergence over time。
![](images/bfd42b2651ea5f2cdee99d3265cf5519a3706a810e7cb803b8e8b5a4e49c09f1.jpg)  
Figure 50. Airplane mode convergence over time.

# NFAC SIMULATION RESULTS

The wind tunnel cases required a substantial amount of time to run, varying from 2–6 weeks on a desktop-class computer, depending on the required time difference between time steps for stability and convergence behavior. Figure 51 shows a set of Apple iMacs used uninterrupted for the various subsets for about 2–3 months on end.

图片摘要：该图主要展示 50. Airplane mode convergence over time。
![](images/39066261ae6f3b17ae0cd554470cd22ace672ddc83ddb6b0d70d47d1ec7e0bb4.jpg)  
Figure 51. Various computers used to compute each of the cases within the time frame.

# NFAC 80- by 120-Foot Wind Tunnel Results

The results for the rotor-only cases and geometry cases for both free field and wind tunnel simulations are respectively summarized in Table 8 and Table 9. The last column in both tables shows a top view (XY-plane) sketch of the wind tunnel configurations of the subsets of each case. For the rotor-only cases (FFRO, WTRO) the free field case (FFRO) was chosen as the benchmark as this is the ideal testing ground. Similarly, the free field analogy with geometry (FFGE) was chosen as the benchmark in the geometry cases; FFGE and WTGE. Thus, the changes in power and thrust are expressed as a relative percentage change compared to their free field counterparts. The computation of the change in power and change in thrust for FFRO and WTRO cases is shown in Equations (22) and (23).

$$
\delta_ {p} = \frac {P - P _ {\mathrm {FFRO}}}{P _ {\mathrm {FFRO}}} \times 100 \% \tag{22}
$$

$$
\delta_ {t} = \frac {T - T _ {\mathrm {FFRO}}}{T _ {\mathrm {FFRO}}} \times 100 \% \tag{23}
$$

Cases 1 and 2 show consistent reduction in power and increase in thrust, leading to a performance improvement of the wind tunnel cases compared to the free field cases. As expected the interference is reduced when a slight tunnel velocity of $V = 1 0$ (kts) is used compared to edgewise hover. It is likely the interference will vanish after further increasing the tunnel velocity. Re-ingestion of the wake was studied for case 2 using a coarser model with an unfitted body. At $V = 1 0$ (kts) edgewise no re-ingestion of the wake occurred, as suggested by Figure 52. This “coarse” run was simulated using a time step of around 1/40 (s) that is far below the validation temporal resolution. It does offer a rough idea of the wake propagation over a longer time.

TABLE 8. FINAL 80- BY 120-FOOT WIND TUNNEL CASES   

<table><tr><td>Case</td><td>Variable</td><td>FFRO</td><td>WTRO</td><td colspan="2">Sketch (WTRO)</td></tr><tr><td rowspan="4">1</td><td>power, P (J/s)</td><td>5.78E+05</td><td>5.75E+05</td><td rowspan="4">↑T↓</td><td rowspan="4"></td></tr><tr><td>thrust, T (N)</td><td>2.75E+04</td><td>2.88E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-0.7</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>4.7</td></tr><tr><td rowspan="4">2</td><td>power, P (J/s)</td><td>5.76E+05</td><td>5.71E+05</td><td rowspan="4">V→↑T↓</td><td rowspan="4"></td></tr><tr><td>thrust, T (N)</td><td>2.77E+04</td><td>2.89E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-0.7</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>4.3</td></tr><tr><td rowspan="4">3</td><td>power, P (J/s)</td><td>1.03E+05</td><td>1.02E+05</td><td rowspan="4">V→T↓</td><td rowspan="4"></td></tr><tr><td>thrust, T (N)</td><td>1.21E+03</td><td>1.19E+03</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-1.1</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-2.0</td></tr></table>

Case 3 experiences performance change, but both power and thrust change in identical direction. This means the effect is likely to be less than observed for cases 1 and 2 because the data point may have moved along the thrust power curve. In an actual wind tunnel, the rotor would have been trimmed for thrust.

Differences between the cases in Table 8 and Table 9 are only apparent for case 3, in which the thrust and power of the case with TTR geometry is considerably higher compared to the rotor-only cases, for an identical collective. While a true comparison of the two would require that the thrust values be trimmed, the difference, in part, is assumed to be attributable to an increase in pressure behind the rotor disc due to the inclusion of the wedge-shaped front of the TTR.

TABLE 9. NFAC 80- BY 120-FOOT WIND TUNNEL GEOMETRY RESULTS   

<table><tr><td>Case</td><td>Variable</td><td>FFGE</td><td>WTGE</td><td>Sketch (WTGE)</td></tr><tr><td rowspan="4">1</td><td>power, P (J/s)</td><td>5.77E+05</td><td>5.73E+05</td><td></td></tr><tr><td>thrust, T (N)</td><td>2.75E+04</td><td>2.87E+04</td><td></td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-0.7</td><td></td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>4.6</td><td></td></tr><tr><td rowspan="4">2</td><td>power, P (J/s)</td><td>5.75E+05</td><td>5.70E+05</td><td></td></tr><tr><td>thrust, T (N)</td><td>2.77E+04</td><td>2.88E+04</td><td></td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-0.9</td><td></td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>4.0</td><td></td></tr><tr><td rowspan="4">3</td><td>power, P (J/s)</td><td>1.39E+05</td><td>1.38E+05</td><td></td></tr><tr><td>thrust, T (N)</td><td>1.95E+03</td><td>1.93E+03</td><td></td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-0.5</td><td></td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-1.2</td><td></td></tr></table>

图片摘要：该图主要展示 9. NFAC 80 BY 120 FOOT WIND TUNNEL GEOMETRY RESULTS。
![](images/42c5827eb77397d2616ec4460ae44fd86015f678311165d3abc20d86a9c5e8ec.jpg)  
Figure 52. A velocity plot of a coarse, unfitted body test at $t \approx 6$ (s) showing no re-ingestion.

# Quasi Trim for Thrust

RotCFD lacks the functionality to trim the rotor automatically at the time of this writing. To further investigate cases 1–3, a “quasi thrust trim” is performed for WTGE cases. By looking at the sign of the thrust change in the WTGE column, a very small change in collective can be proposed to yield a second WTGE data point, called $\mathrm { W T G E } _ { 2 }$ if of higher magnitude than the original WTGE value. For this small change in $P$ and T, a linear interpolation is performed to find the power values of a WTGE data point with the same thrust as the FFGE data point. This “quasi thrust-trimmed” WTGE data point is called WTGE*. This method shows the influence of the tunnel by isolating the power variable. A reduction in power suggests improved performance due to the wind tunnel while an increase in power suggests a decrease in performance. The linearization is shown in Figure 53, and the computation is shown in Equations (24) and (25).

$$
\begin{array}{l} P _ {\mathrm {W T G E} *} = \frac {\Delta P _ {\mathrm {W T G E}}}{\Delta T _ {\mathrm {W T G E}}} \left(T _ {\mathrm {F F G E}} - T _ {\mathrm {W T G E} 1}\right) + P _ {\mathrm {W T G E} 1} \tag {24} \\ = \frac {P _ {\mathrm {W T G E} 2} - P _ {\mathrm {W T G E} 1}}{T _ {\mathrm {W T G E} 2} - T _ {\mathrm {W T G E} 1}} \left(T _ {\mathrm {F F G E}} - T _ {\mathrm {W T G E} 1}\right) + P _ {\mathrm {W T G E} 1} \\ \end{array}
$$

$$
T _ {\mathrm {W T G E} *} = T _ {\mathrm {F F G E}} \tag {25}
$$

图片摘要：该图主要展示 53. Linearization to obtain point。
![](images/dca4b9b00c5b8cf17d87646cdccb0ca1a3a1f6198c3febbf8cb8d4d7973652b8.jpg)  
Figure 53. Linearization to obtain point $( T _ { F F G E } , P ^ { \star } )$ .

The results of the linearization are summarized in Table 10. Case 1 (7.2 percent reduction in power) and case 2 (6.7 percent reduction in power) both show an improvement in performance due to the tunnel geometry, and as expected the performance difference decreases as tunnel velocity increases. Case 3, however, does not experience any noticeable tunnel interference (0.0 percent reduction in power). The changes in power for cases 1 and 2 are substantial considering the size of the 80- by 120-Foot Wind Tunnel.

For reference, the blockage fraction, expressed as the ratio of the frontal area of the TTR (without rotor) and struts to the wind tunnel cross-sectional area, is approximately 3.1 and 2.3 percent for the edgewise and axial cases, respectively. These values are approximated using a CAD program. Representative velocity plots for case 3 are shown in Figure 54.

TABLE 10. QUASI TRIMMED NFAC 80- BY 120-FOOT WIND TUNNEL GEOMETRY RESULTS   

<table><tr><td>Case</td><td>Variable</td><td>WTGE1</td><td>WTGE2</td><td>FFGE</td><td>WTGE*</td></tr><tr><td rowspan="4">1</td><td>power, P (J/s)</td><td>4.92E+05</td><td>5.73E+05</td><td>5.77E+05</td><td>5.36E+05</td></tr><tr><td>thrust, T (N)</td><td>2.60E+04</td><td>2.87E+04</td><td>2.75E+04</td><td>2.75E+04</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>-7.2</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">2</td><td>power, P (J/s)</td><td>4.87E+05</td><td>5.70E+05</td><td>5.75E+05</td><td>5.36E+05</td></tr><tr><td>thrust, T (N)</td><td>2.60E+04</td><td>2.88E+04</td><td>2.77E+04</td><td>2.77E+04</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>-6.7</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">3</td><td>power, P (J/s)</td><td>1.38E+05</td><td>1.51E+05</td><td>1.39E+05</td><td>1.39E+05</td></tr><tr><td>thrust, T (N)</td><td>1.93E+03</td><td>2.19E+03</td><td>1.95E+03</td><td>1.95E+03</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr></table>

图片摘要：该图主要展示 10. QUASI TRIMMED NFAC 80 BY 120 FOOT WIND TUNNEL GEOMETRY R。
![](images/67f4b7d4125a8d84ba195bfb42871401a1049cfec90a18f7748500c4bbb1a80a.jpg)

图片摘要：该图主要展示 10. QUASI TRIMMED NFAC 80 BY 120 FOOT WIND TUNNEL GEOMETRY R。
![](images/d414b17c43b469fea4c3ea7b8e522718f151e6be603bab5512dab14718490651.jpg)

图片摘要：该图主要展示 10. QUASI TRIMMED NFAC 80 BY 120 FOOT WIND TUNNEL GEOMETRY R。
![](images/b551cfc454029884f6e6cba8f2b48f0c340f8cb50ce959267d095627a7899d62.jpg)

图片摘要：该图主要展示 54. Representative velocity plots for case 3。
![](images/2cf1c1091964f721a1e345052ffa7d531aa13a05d983df98ec1318d31d7222e6.jpg)

图片摘要：该图主要展示 54. Representative velocity plots for case 3。
![](images/f1e52b6f15772715138fbcb23527e6449a38c2eecc334671d8c1a4aacc234cbd.jpg)

Figure 54. Representative velocity plots for case 3.   
图片摘要：该图主要展示 54. Representative velocity plots for case 3pPa：69E45E / NFA。
![](images/b450bd429d43bcf0a1c31b81a0314bb754ce1812ee07112d59a548e2c7e09738.jpg)  
pPa：69E45E  
/

# NFAC 40- by 80-Foot Wind Tunnel Results

The results for the rotor-only cases and geometry cases for both free field and wind tunnel simulations are respectively summarized in Table 11 and Table 12. The last column in both tables shows a top view (XY-plane) sketch of the wind tunnel configurations of the subset WTRO of each case.

Case 4 indicates low interference with simultaneous drops in both thrust and power. The proximity of the wall to the rotor in the 40- by 80-Foot Wind Tunnel seems to adversely influence the rotor at higher speeds as shown in case 5. A power increase with thrust loss is shown both with geometry and for the isolated rotor case. Care must be taken however, because the rotor in case 5 is operating under a different collective and free-stream velocity, changing the blade loading and thus performance, making a comparison very difficult. Significant differences between isolated rotor and geometry cases are only observed in case 6. The difference is again thought to be caused by the increased pressure at the back of the rotor due to the wedge-like shape of the TTR nose, or by a difference in blade loading. This, in turn, increases the pressure in the vicinity of the TTR thus increasing the thrust. Case 6 with and without rotor shows a significant difference in performance. Because of constraints on the computational budget no “quasi trim” was performed on the rotor-only cases, but it is thought that the operating conditions of the rotor are changed and likely show a positive performance increase. Case 7 shows a thrust and power increase and thus a more favorable interference compared to the fully edgewise TTR in case 5.

TABLE 11. NFAC 40- BY 80-FOOT WIND TUNNEL ROTOR-ONLY RESULTS   

<table><tr><td>Case</td><td>Variable</td><td>FFRO</td><td>WTRO</td><td>Sketch (WTRO)</td></tr><tr><td rowspan="4">4</td><td>power, P (J/s)</td><td>4.84E+05</td><td>4.79E+05</td><td rowspan="4">v→f</td></tr><tr><td>thrust, T (N)</td><td>2.47E+04</td><td>2.44E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-1.1</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-1.1</td></tr><tr><td rowspan="4">5</td><td>power, P (J/s)</td><td>2.92E+05</td><td>2.99E+05</td><td rowspan="4">v→f</td></tr><tr><td>thrust, T (N)</td><td>2.69E+04</td><td>2.65E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>2.6</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-1.4</td></tr><tr><td rowspan="4">6</td><td>power, P (J/s)</td><td>7.70E+05</td><td>7.93E+05</td><td rowspan="4">v→f</td></tr><tr><td>thrust, T (N)</td><td>6.50E+03</td><td>6.73E+03</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>3.0</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>3.6</td></tr><tr><td rowspan="4">7</td><td>power, P (J/s)</td><td>7.26E+05</td><td>7.44E+05</td><td rowspan="4">v→f</td></tr><tr><td>thrust, T (N)</td><td>2.28E+04</td><td>2.37E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>2.5</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>4.0</td></tr></table>

TABLE 12. NFAC 40- BY 80-FOOT WIND TUNNEL GEOMETRY RESULTS   

<table><tr><td>Case</td><td>Variable</td><td>FFGE</td><td>WTGE</td><td>Sketch (WTRO)</td></tr><tr><td rowspan="4">4</td><td>power, P (J/s)</td><td>4.83E+05</td><td>4.75E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T (N)</td><td>2.46E+04</td><td>2.41E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-1.7</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-2.2</td></tr><tr><td rowspan="4">5</td><td>power, P (J/s)</td><td>2.85E+05</td><td>2.94E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T (N)</td><td>2.69E+04</td><td>2.66E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>3.3</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-1.0</td></tr><tr><td rowspan="4">6</td><td>power, P (J/s)</td><td>8.77E+05</td><td>8.63E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T (N)</td><td>7.62E+03</td><td>7.46E+03</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>-1.6</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>-2.0</td></tr><tr><td rowspan="4">7</td><td>power, P (J/s)</td><td>7.30E+05</td><td>7.46E+05</td><td rowspan="4">v→</td></tr><tr><td>thrust, T (N)</td><td>2.33E+04</td><td>2.41E+04</td></tr><tr><td>change of power, δp (%)</td><td>0.0</td><td>2.2</td></tr><tr><td>change of thrust, δt (%)</td><td>0.0</td><td>3.1</td></tr></table>

Similar to the 80- by 120-Foot Wind Tunnel, re-ingestion was examined for low tunnel velocities (i.e., case 4) and was not observed to occur above $V = 1 0$ (kts) edgewise. Similar to the previous section, the geometry cases from Table 12 are trimmed for thrust using a linearized method.

# Quasi Trim for Thrust

The methodology to trim the thrust value is identical to the procedure for the 80- by 120-Foot Wind Tunnel and uses Equations (24) and (25). The results of the quasi trim are shown in Table 13.

Both edgewise cases, case 4 (1.0 percent increase in power) and case 5 (4.8 percent increase in power), show a decrease in performance, seemingly increasing with tunnel velocity. Both the axial and tilt cases, case 6 (1.6 percent decrease in power) and case 7 (0.7 percent decrease in power) respectively, show an increase in performance as expected according to Glauert [14].

For reference, the blockage fraction is found to be approximately 7.7, 3.8, and 7.5 percent for the edgewise, axial, and tilt cases, respectively. These values are approximated using a CAD program. Figure 55 shows the flow field of the FFGE subset for case 7.

TABLE 13. QUASI TRIMMED NFAC 40- BY 80-FOOT WIND TUNNEL GEOMETRY RESULTS   

<table><tr><td>Case</td><td>Variable</td><td>WTGE1</td><td>WTGE2</td><td>FFGE</td><td>WTGE*</td></tr><tr><td rowspan="4">4</td><td>power, P (J/s)</td><td>4.75E+05</td><td>5.08E+05</td><td>4.83E+05</td><td>4.88E+05</td></tr><tr><td>thrust, T (N)</td><td>2.41E+04</td><td>2.54E+04</td><td>2.46E+04</td><td>2.46E+04</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>1.0</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">5</td><td>power, P (J/s)</td><td>2.94E+05</td><td>3.02E+05</td><td>2.85E+05</td><td>2.99E+05</td></tr><tr><td>thrust, T (N)</td><td>2.66E+04</td><td>2.70E+04</td><td>2.69E+04</td><td>2.69E+04</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>4.8</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">6</td><td>power, P (J/s)</td><td>8.63E+05</td><td>9.69E+05</td><td>8.77E+05</td><td>8.63E+05</td></tr><tr><td>thrust, T (N)</td><td>7.46E+03</td><td>8.47E+04</td><td>7.62E+03</td><td>7.62E+03</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>-1.6</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr><tr><td rowspan="4">7</td><td>power, P (J/s)</td><td>7.46E+05</td><td>4.96E+05</td><td>7.30E+05</td><td>7.25E+05</td></tr><tr><td>thrust, T (N)</td><td>2.41E+04</td><td>1.50E+04</td><td>2.33E+04</td><td>2.33E+04</td></tr><tr><td>change of power, δp (%)</td><td>-</td><td>-</td><td>0.0</td><td>-0.7</td></tr><tr><td>change of thrust, δt (%)</td><td>-</td><td>-</td><td>0.0</td><td>0.0</td></tr></table>

图片摘要：该图主要展示 13. QUASI TRIMMED NFAC 40 BY 80 FOOT WIND TUNNEL GEOMETRY RE。
![](images/edc703a5db1f98351627a46af6badc54890731f7cd94a8af4b95c7d97778a95a.jpg)  
Figure 55. Flow field of FFGE subset for case 7.

# Performance Convergence

The performance convergence for cases 2 and 6 is shown in Figure 56 and Figure 57. Performance convergence below 0.25 percent is usually quickly observed following the same procedure as for the validation cases. Case 2 has a high amount of time steps and shows “typical” slower convergence for hover cases. Case 7 shows rapid convergence characteristics for airplane or tilt mode cases.

图片摘要：该图主要展示 55. Flow field of FFGE subset for case 7。
![](images/13ec7a649fa3d92bee095e77434447f781acbea7a87bb6f9d5026cc0ab4e4316.jpg)  
Figure 56. Performance convergence for case 2, WTGE, hover.

图片摘要：该图主要展示 56. Performance convergence for case 2, WTGE, hover。
![](images/5094ee6279abd5fcbcc9a9c4315dcc9cbdcf3d7c344866bde6f755a713fa6273.jpg)  
Figure 57. Performance convergence for case 7, WTGE, tilt mode.

# Forces on the TTR

The rotor performance is directly measured within the TTR axis. Therefore, the wind tunnel scale does not have to be used and the forces on the TTR are, for this research, not significant as RotCFD outputs the rotor performance directly. Moreover, because RotUNS does not allow for viscous bodyfitted grids, chances of an accurate drag measurement greatly diminish as no plausible boundary layer is modeled, or better, sustained. Also the unsteady nature of the URANS solver may show variations in the forces due to unsteady (vortex) shedding.

Two representative graphs with the forces on the TTR show a particular problem of interest. Figure 58 shows the integrated forces on the TTR for an edgewise case at high tunnel velocity—case 5, WTGE. The behavior of these forces over time is as expected, flattening out as the flow and wake are fully established over time.

A particular case, which was run for extra time to investigate its behavior, is that of case 4—the edgewise, low-velocity case in the 40- by 80-Foot Wind Tunnel test section. Figure 59 shows that even after nearly doubling the time steps the forces on the TTR have not converged yet.

The power and thrust only vary 0.5 and 1 percent, respectively, over the last 50 percent of simulated time, as shown in Figure 60. This extremely stable rotor performance behavior was found consistently throughout this report. A recommendation for future work would be to further investigate the transient nature of the forces observed in this case.

图片摘要：该图主要展示 58. Integrated forces on the TTR for case 5, WTGE。
![](images/cbfcc10834c6ce974ffe1a1cc5f4345e12bc85a43c7a2cdc3ffe14577f09fc8d.jpg)  
Figure 58. Integrated forces on the TTR for case 5, WTGE.

图片摘要：该图主要展示 58. Integrated forces on the TTR for case 5, WTGE。
![](images/4c9a76f75b3079d6ff7582d771b6e5d3d4b78e06b579a05003a036e51b988e5d.jpg)  
Figure 59. Integrated forces on the TTR and struts for case 4, WTGE.

图片摘要：该图主要展示 59. Integrated forces on the TTR and struts for case 4, WTGE。
![](images/af86ea88cc2e3e73fa87f990dfa4beef36a58f3732ed2d8c5d03e43e9a4d6f18.jpg)  
Figure 60. Performance convergence for case 4, WTGE.

# Stability-Related Time Step Restrictions

A problem encountered during this research was the stability-related time step restriction. The “clean” rectilinear Cartesian grid, such as the one used in the isolated rotor cases for the validation, was combined with the tetrahedral cells for the body fitting. The tetrahedron show higher aspect ratios per cell, and sharp angles compared to the near-squared cells in the far field. In the case of stability-related time step restrictions, it is thought that the turbulent kinetic energy, $k _ { ; }$ , and turbulent dissipation values, ε, diverge over time and, as they are coupled back into the RANS equations, cause flow field divergence.

The addition of these cells therefore limits the maximum time step used; this time step is often much smaller than the time step necessary for accurate rotor performance values as used for the validation of the isolated rotor cases. In some cases, a time step equivalent to half a degree of rotor rotation would be necessary, resulting in a tremendously increased computational effort.

Investigating the effect of another gridding technique is left for future work; perhaps using RotVIS or another module within RotCFD and investigating the performance results running with more refined unfitted bodies solely using a Cartesian grid. Figure 61a, Figure 61b, and Figure 61c show the TTR with the used body fitting, an unfitted version, and the ungridded (only meshed) nose, respectively.

图片摘要：该图主要展示 61. Body fitted TTR nose (a), gridded TTR nose without body 。
![](images/90682bc4fd831a233c2feca8cac68a21bd61c344b6d8f47289bca13c086ed9ec.jpg)  
a)

图片摘要：该图主要展示 61. Body fitted TTR nose (a), gridded TTR nose without body 。
![](images/41cfe98b260925c2d2576d2d3be29380d5266085cdcc6fc71378d262e57b38f0.jpg)  
b)

图片摘要：该图主要展示 61. Body fitted TTR nose (a), gridded TTR nose without body 。
![](images/809968e7c2df835ed9b3913bec2ff37c3154e30616db0513d3a142302710b413.jpg)  
c)   
Figure 61. Body-fitted TTR nose (a), gridded TTR nose without body fitting (b), and meshed TTR nose (no grid, c).

# Conclusions and Recommendations

# Conclusions

The setup and grid generation in RotCFD is faster than many CFD codes and therefore makes it a useful engineering tool. The validation results show very good correlation with performance data over the thrust range examined. The results for the XV-15 isolated rotor in hover with a Corrigan stall delay method showed excellent performance correlation compared to the OARF data set. The tip loss model was found to overcorrect, most likely caused by the generated tip vortex or pressure equalization over the blade tip. The tip loss is, however, not fully accounted for by RotCFD, as shown from the obtained blade loading. For the tilt and airplane mode cases, the XV-15 rotor model showed accurate results compared to wind tunnel data, with only minor differences observed between the tip loss model and clean variant. These differences are due to the lower thrust settings and lower induced velocities at the tips, mostly because of the advance ratio. Overall the author believes a very good compromise between accuracy and efficiency was achieved. For hover tests the Corrigan and Schillings stall delay model with $n = 1 . 8$ is advised, and for tilt and airplane mode the clean XV-15 rotor suffices for very reasonable performance predictions in complicated flows.

For the 80- by 120-Foot Wind Tunnel no influence was found for the XV-15 rotor in axial mode at the highest tunnel velocity of $V = 1 0 0$ (kts). For the case with (near) hover in edgewise mode, the performance showed a power decrease of $- 7 . 2$ and –6.7 percent for hover and edgewise flight with $V = 1 0$ (kts). The large interference at this very unfavorable configuration is attributed to the boxedin effect of the rotor facing the tunnel wall.

For the 40- by 80-Foot Wind Tunnel, interference was found under all tested conditions as was expected because of the smaller cross-sectional area of the test section. In edgewise mode, both at tunnel velocities of $V = 1 0$ (kts) and $V = 1 0 0$ (kts), an increase in power was observed of 1.0 and 4.8 percent, respectively. Differences between the two edgewise cases are difficult to justify because of the different operating conditions of the rotor. Both the axial case at $V = 2 0 0$ (kts) and the tilted case at $V = 1 0 0$ (kts) show a decrease in power of –1.6 and 0.7 percent, respectively. This is expected for a thrusting rotor in airplane mode in a duct. The axial case at $V = 2 0 0$ (kts) shows a wake velocity slightly over $M = 0 . 3 0$ , which could be questioned for its validity due to compressibility effects. Researchers at Ames were not convinced it would yield any substantial difference in this case, especially because the delta was obtained between two similar cases.

# Recommendations

The investigation of the effect of stall delay in other flight modes as well as a better tip loss model— either by reducing the tip loss factor or finding a better suitable method—are left for future work. At the time of writing, a new model has been introduced for use with RotCFD. The approach corrects the local angle of attack to achieve zero lift at the tip based on the local pressure difference between the top and bottom of the rotor.

All performance validation data is expressed as function of thrust coefficient over solidity. A better picture of the correlation is obtained if this solidity value is not used and only the coefficients are used as parameters. This leads to more direct comparisons of the thrust and power. Because of the ambiguous solidity data (not every report is clear on what value is used) the solidity value is incorporated in the present calculations.

A considerable amount of work can be done to investigate the blade loading of the XV-15 rotor. Because of the changing blade loading at different azimuthal stations, and numerous flight modes and thrust values, this is a considerable effort. The thrust modeled in this research is well within the normal range of the XV-15. More research may lead to performance data in the rotor stall region. The assumption that the rotor was not trimmed, to reduce the rolling moment, might also cause adverse rotor effects. Therefore, cyclic pitch variation and its effect on performance can also be further investigated.

RotUNS is capable of adaptive grids, but for this research the gridding and flow field cell sizes were kept nearly identical over the cases for consistent performance values and comparison. A tailored adaptive grid, however, could improve the wake propagation through the domain and, because of the specified high cell density, could yield a more efficient simulation or a more accurate result in equal computation time. It is highly interesting to contemplate whether an adaptive grid could yield improved computed velocities at the blade or disk tips and thus discard the need for a tip model at all.

The reason for the performance mismatch using the unsteady model was not found. One hypothesis is that even at a considerably small delta time, the implicit method fails to follow the exact time variations of the flow field. When this mismatch is then incorrectly matched with the “hard coded” timing of the discrete rotor blades, the time of the blade position and wake state are not correct, which could lead to different pressures over the rotor disk. Also the rotor trim could affect the unsteady results more aggressively than those of the steady model.

A substantial issue with the use of RotUNS and body-fitted grids was the stability-related time step restriction. Because of the need to reduce the time step considerably, the computational time per case increased significantly. A finer grid does not necessarily solve the problem because the effective cell shape at the body fit remains similar. An investigation into the use of RotVIS, which can handle body-fitted viscous grids and therefore should simulate boundary layers more accurately as well, might be useful as the body-fitted cells are much more organized. The use of RotVIS for this research was highly discouraged before the author was fully familiar with RotUNS. If the computation time can be considerably reduced using RotVIS, it might be possible to generate enough performance data points per case to create actual power curves, which are much more useful to compare than individual data points.

Another area of interest is the wall pressure along the longitudinal axis of the tunnel test sections. Wall pressure can be obtained by extracting the pressure along the centerlines of the walls, presumably excluding the floor-plane, however a second set of simulations for empty test sections must be performed.

# REFERENCES

[1] R. G. Rajagopalan; V. Baskaran; A. Hollingsworth; A. Lestari; D. Garrick; E. Sous; and B. Hagerty: RotCFD - A Tool for Aerodynamic Interference of Rotors: Validation and Capabilities. AHS International - Future Vertical Lift Aircraft Design Conference, 2012, pp. 311–327.   
[2] L. A. Young; G. K. Yamauchi; and G. Rajagopalan: Simulated Rotor Wake Interactions Resulting From Civil Tiltrotor Aircraft Operations Near Vertiport Terminals. 51st AIAA Aerospace Sciences Meeting inc. the New Horizons Forum and Aerospace Exposition, 2013.   
[3] P. R. Spalart: Strategies for Turbulence Modelling and Simulations. Int. J. Heat Fluid Flow, vol. 21, no. 3, pp. 252–263, 2000.   
[4] G. Iaccarino; A. Ooi; P. A. Durbin; and M. Behnia: Reynolds Averaged Simulation of Unsteady Separated Flow. Int. J. Heat Fluid Flow, vol. 24, no. 2, pp. 147–156, 2003.   
[5] B. E. Launder and D. B. Spalding: The Numerical Computation of Turbulent Flows. Comput. Methods Appl. Mech. Eng., vol. 3, no. 2, pp. 269–289, 1974.   
[6] W. P. Jones and B. E. Launder: The Prediction of Laminarization With a Two-Equation Model of Turbulence. Int. J. Heat Mass Transf., vol. 15, no. 2, pp. 301–314, 1972.   
[7] Z. Yu and Y. Cao: Three Dimensional Turbulence Numerical Simulation of Rotor in Forward Flight. Beijing Hangkong Hangtian Daxue Xuebao/Journal Beijing Univ. Aeronaut. Astronaut., vol. 32, no. 7, pp. 751–755, 2006.   
[8] J. D. Anderson: Computational Fluid Dynamics: The Basics With Applications. McGraw-Hill Inc., pp. 37–94, 1995.   
[9] R. G. Rajagopalan and C. K. Lim: Laminar Flow Analysis of a Rotor in Hover. J. Am. Helicopter Soc., vol. 36, no. 1, pp. 12–23, 1991.   
[10] H. K. Edenborough: Research at NASA’s NFAC Wind Tunnels. Int. Sess. Japan Soc. Aeronaut. Sp. Sci. Aircr. Symp., pp. 1–9, 1990.   
[11] P. T. Zell: Performance and Test Section Flow Characteristics of the National Full-Scale Aerodynamics Complex 80- by 120-Foot Wind Tunnel. NASA TR 103920, pp. 1–66, 1993.   
[12] P. T. Zell and K. Flack: Performance and Test Section Flow Characteristics of the National Full-Scale Aerodynamics Complex 40- by 80-Foot Wind Tunnel. NASA TM 101065, pp. 1–81, Feb. 1989.   
[13] V. R. Corsiglia; L. E. Olson; and M. D. Falarski: Aerodynamic Characteristic of the 40- by 80/80- by 120-Foot Wind Tunnel at NASA Ames Research Center. NASA TM 85946, pp. 1–22, April 1984.   
[14] H. Glauert: Wind Tunnel Interference on Wings, Bodies and Airscrews. Aeronaut. Res. Comm., pp. 1–52, 1933.   
[15] A. Pope and W. H. J. Rae: Low-Speed Wind Tunnel Testing. 2nd ed. Seattle: John Wiley & Sons, 1984.

[16] C. W. Acree: Private Correspondence. NASA Ames Aeromechanics Office, Moffett Field, CA, 2015.   
[17] NASA Ames Research Center: Tiltrotor Test Rig. 2015. http://rotorcraft.arc.nasa.gov/Research/facilities/ttr.html# (accessed 24-Mar-2015).   
[18] M. D. Maisel; D. J. Giulianetti; and D. C. Dugan: The History of The XV-15 Tilt Rotor Research Aircraft From Concept to Flight. NASA SP 4517, pp. 1–194, 2000.   
[19] M. D. Maisel; D. C. Borgman; and D. D. Few: Tilt Rotor Research Aircraft Familiarization Document. NASA TM X-62407, pp. 1–105, 1975.   
[20] D. C. Dugan; R. G. Erhart; and L. G. Schroers: The XV-15 Tilt Rotor Research Aircraft. NASA TM 81244, pp. 1–18, 1980.   
[21] F. F. Felker; M. D. Betzina; and D. B. Signor: Performance and Loads Data from a Hover Test of a Full-Scale XV-15 Rotor. NASA TM 86833, pp. 1–94, 1985.   
[22] Anon.: Task II - Wind Tunnel Test Results. NASA CR 114363, 1976.   
[23] W. Johnson: CAMRAD II Comprehensive Analytical Model of Rotorcraft Aerodynamics and Dynamics. Johnson Aeronautics, Palo Alto, CA, 2005.   
[24] W. L. Arrington; M. Kumpel; R. L. Marr; and K. G. McEntire: PXV-15 Tilt Rotor Research Aircraft Flight Test Data Report. NASA CR 177406, vol. 1–5, pp. 1–202, 1985.   
[25] W. Johnson: An assessment of the Capability to Calculate Tilting Prop-Rotor Aircraft Performance, Loads, and Stability. NASA TP 2291, pp. 1–21, 1984.   
[26] J. J. Corrigan and J. J. Schillings: Emprical Model for Stall Delay Due to Rotation. AHS Aeromechanics Spec. Conf., pp. 8.4–1 to 8.4–15, 1994.   
[27] J. Seddon: Basic Helicopter Aerodynamics. Oxford: BSP Professional Books, 1990.   
[28] S. Forth; P. Hovland; E. Phipps; J. Utke; and A. Walther: Recent Advances in Algorithmic Differentiation. Springer Science & Business Media, 2012.   
[29] C. W. Acree: Modeling Requirements for Analysis and Optimization of JVX Proprotor Performance. AHS 64th Annual Forum, Montreal, Canada, 2008, pp. 1–21.   
[30] W. Johnson: CAMRAD II. vol. VI, no. 4.9, pp. 1–294.   
[31] J. G. Leishman: Helicopter Aerodynamics, 2nd ed. Maryland: Cambridge University Press, 2006.   
[32] W. Warmbrodt: Private Correspondence. NASA Ames Aeromechanics Office, Moffett Field, CA, 2015.   
[33] W. J. F. Koning; C. W. Acree; and G. Rajagopalan: Using RotCFD to Predict Isolated XV-15 Rotor Performance. AHS Tech. Mtg. Aeromechanics Des. Vert. Lift, pp. 1–15, 2016.   
[34] W. Johnson: Rotorcraft Aeromechanics. Moffett Field: Cambridge University Press, 2013.   
[35] J. W. Hong: Hover and Cruise Flight Simulation of XV-15 Experimental Aircraft Using RotCFD. Moffett Field, CA, 2015.

# APPENDIX A—NFAC CHARACTERISTICS

The main characteristics of the NFAC wind tunnel test sections are summarized in Table 14 and Table 15.

TABLE 14. 40- BY 80-FOOT WIND TUNNEL CHARACTERISTICS [12]   

<table><tr><td>40- by 80- Foot Wind Tunnel</td><td>SI</td><td>Imperial</td></tr><tr><td>Width test section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Height test section</td><td>12.19 m</td><td>(40 ft )</td></tr><tr><td>Length test section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Actual width test section</td><td>24.08 m</td><td>(79 ft)</td></tr><tr><td>Actual height test section</td><td>11.89 m</td><td>(39 ft)</td></tr><tr><td>Actual length test section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Approximate BL thickness floor (start-end)</td><td>0.25–0.46 m</td><td>(10–18 in.)</td></tr><tr><td>Approximate BL thickness top (start-end)</td><td>0.08–0.15 m</td><td>(3–6 in.)</td></tr><tr><td>Approximate BL thickness sides (start-end)</td><td>&gt;0.25–0.46 m</td><td>(&gt;10–18 in.)</td></tr><tr><td>Maximal test section velocity</td><td>154.33 m/s</td><td>(300 kts)</td></tr></table>

TABLE 15. 80- BY 120-FOOT WIND TUNNEL CHARACTERISTICS [11]   

<table><tr><td>80- by 120-Foot Wind Tunnel</td><td>SI</td><td>Imperial</td></tr><tr><td>Width test section</td><td>36.58 m</td><td>(120 ft)</td></tr><tr><td>Height test section</td><td>24.38 m</td><td>(80 ft)</td></tr><tr><td>Length test section</td><td>36.58 m</td><td>(120 ft)</td></tr><tr><td>Actual width test section</td><td>35.97 m</td><td>(118 ft)</td></tr><tr><td>Actual height test section</td><td>23.93 m</td><td>(78.5 ft)</td></tr><tr><td>Actual length test section</td><td>36.58 m</td><td>(120 ft)</td></tr><tr><td>Approximate BL thickness floor (start-end)</td><td>0.76–1.12 m</td><td>(30–44 in.)</td></tr><tr><td>Maximal test section velocity</td><td>51.44 m/s</td><td>(100 kts)</td></tr></table>

# APPENDIX B—C81 AIRFOIL ADJUSTMENT CODE RESULTS

# Angle of Attack and Mach Number Interpolation

The C81 airfoil files are obtained from experienced XV-15 researchers [16]. The interpolation for angle of attack and Mach number is performed. Figure 62 shows part of the imported data for the 64-X08 airfoil and the PCHIP interpolation for angles of attack and linear interpolation for Mach numbers.

Similar data is shown in Figure 63, Figure 64, and Figure 65 for the 64-X12, 64-X18, and 64-X25 airfoils, respectively.

图片摘要：该图片与Similar data is shown in Figure 63, Figure 64, and Figure 65 for the 64 X12, 64 这部分内容相关。
![](images/03af6b7c2f72c9ac449a1fb2a0900b37cb6353f27e61b1298c4b3f68b85df661.jpg)

图片摘要：该图片与Similar data is shown in Figure 63, Figure 64, and Figure 65 for the 64 X12, 64 这部分内容相关。
![](images/e547debf5ba92185619b8ba2af3253eca142d7c5bd1fac78e466ada1d61667eb.jpg)

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoil。
![](images/98c62653f62332e1d7bbf2b0f6d96c27ad8b96646ad5f272d8e42561a547e451.jpg)

图片摘要：该图片与Figure 62. Imported C81 data for NACA 64 X08 airfoilSimilar data is shown in Fig这部分内容相关。
![](images/ef1481998f85247ca40ff0bcfb2c2433e3b3ebcb7c739032fb974cbc4dbcc2b6.jpg)

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoil。
![](images/09a1098e1829890886412d6933efbce09bebf0617a7b668087496702e12e7b34.jpg)

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoil。
![](images/11887eaddf77cc8f0108251c47909154605943e138413359c1626b169d42c89a.jpg)  
Figure 62. Imported C81 data for NACA 64-X08 airfoil.

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoil。
![](images/66106254d2ff8edd2be0ddd19435b763bfd098df10361cd293cda9ec6ded0a19.jpg)

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoil。
![](images/d84ad333e3cb8ce73a8c56f0db0f5b0ef64d4263cf43e8f3baf1b8134ee5323f.jpg)

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoilFigure 63. Impo。
![](images/c43aaad87e65c1d71954da6eb7dc65ea0458c94d6efef77f6eb6745b897764b8.jpg)

图片摘要：该图主要展示 62. Imported C81 data for NACA 64 X08 airfoilFigure 63. Impo。
![](images/45ae72741d2ab56ba436a0d1492079e784613ad0c4b426c95672b028045814d4.jpg)

图片摘要：该图主要展示 63. Imported C81 data for NACA 64 X12 airfoil。
![](images/b2a801e7fedbc3ebd9904f26a1b7c7bc2fc5f89b9289f69541029da985879370.jpg)

图片摘要：该图主要展示 63. Imported C81 data for NACA 64 X12 airfoil。
![](images/35d615f855d1eea626c0a3f3b2258b7627410ce8569195162de5a38003257c85.jpg)  
Figure 63. Imported C81 data for NACA 64-X12 airfoil.

图片摘要：该图主要展示 63. Imported C81 data for NACA 64 X12 airfoil。
![](images/c5cf384b4a7ee4d478ad53b3b38c35fef884529b9102110466a077cb7b55f5d3.jpg)

图片摘要：该图主要展示 63. Imported C81 data for NACA 64 X12 airfoil。
![](images/680b0e7f2183eab0613b275fe468c214d73ad9f6b274c4917a7b732fe78ef1a3.jpg)

图片摘要：该图主要展示 63. Imported C81 data for NACA 64 X12 airfoilFigure 64. Impo。
![](images/0b53d6e0326c5a0d73b3f3dbbed5218e1a0becd5bedb5d292471dd8856d8b59e.jpg)

图片摘要：该图主要展示 63. Imported C81 data for NACA 64 X12 airfoilFigure 64. Impo。
![](images/a630f0816572a6e7197bf6e11a8e9877ccbcde91fa032cab2fb3e9b5defd0c7d.jpg)

图片摘要：该图主要展示 64. Imported C81 data for NACA 64 X18 airfoil。
![](images/8aa6e560b39514740b16edd6bd80f45789b57ad87d336433c576a3900ffe1086.jpg)

图片摘要：该图主要展示 64. Imported C81 data for NACA 64 X18 airfoil。
![](images/a42dafe0472b10a23698c50d90dfb31ddd402c15d6e798df24797be0cdf9b7ae.jpg)  
Figure 64. Imported C81 data for NACA 64-X18 airfoil.

图片摘要：该图主要展示 64. Imported C81 data for NACA 64 X18 airfoil。
![](images/d6b0fc27c1b537b48d2f9ae3580bcf0d74b5995dee6cd44b7772345ad25c3c87.jpg)

图片摘要：该图主要展示 64. Imported C81 data for NACA 64 X18 airfoil。
![](images/d8341b490e084c1e1e9c1a5909245e07e0b934433ede711b76ed35b2ab2184ec.jpg)

图片摘要：该图主要展示 64. Imported C81 data for NACA 64 X18 airfoilFigure 65. Impo。
![](images/23aa692caf068d1f399cb6e983369e10a73e7a1a7d18030e92b5403157e7847c.jpg)

图片摘要：该图主要展示 64. Imported C81 data for NACA 64 X18 airfoilFigure 65. Impo。
![](images/0a02364b9068822d89069f0cc206b304af6a3739c245483670ea5b597061c88c.jpg)

图片摘要：该图主要展示 65. Imported C81 data for NACA 64 X25 airfoil。
![](images/55242e9ebb33bd31c3e2a4903a7d3849fd8a2c50a1723e659200a49d561eb8af.jpg)

图片摘要：该图主要展示 65. Imported C81 data for NACA 64 X25 airfoil。
![](images/ea74a9b579ddceed434a1aa1d72fcd1867bed726ce891046869e3a639d432679.jpg)  
Figure 65. Imported C81 data for NACA 64-X25 airfoil.

# Representative Stall Delay Plots

Figure 66 and Figure 67 show the effect of stall delay on the lift curve slope for a set of interpolated airfoil data at various radial stations.

Figure 67d shows the result of the assumption that the zero lift angle of attack is equal to zero. Consequently, the lift coefficient is slightly lowered at high Mach numbers. While the observed effect is small, future work could eliminate this error from the program.

图片摘要：该图主要展示 67d shows the result of the assumption that the zero lift an。
![](images/3b706c5cd739f821bd7e9d3dc22682197fb7e9a392d7210f0ea545379553ffbf.jpg)

图片摘要：该图主要展示 67d shows the result of the assumption that the zero lift an。
![](images/1a2edf71c73e0f2c7d465b6ef1977108648d6f000073665992f7fe3f35f1553a.jpg)

图片摘要：该图主要展示 67d shows the result of the assumption that the zero lift an。
![](images/f98d0218c3a272a07c49ef035ef15a32f089cda0edeeabfaad6562af10ea6689.jpg)

图片摘要：该图主要展示 67d shows the result of the assumption that the zero lift an。
![](images/b8001b7184d02d922230568d3297ae27eaa7d357b1dcf44701a5855e07ef3d62.jpg)

图片摘要：该图主要展示 66. Effect of stall delay on lift curve slope。
![](images/5113ef43457d23bba8fc28fd8a34ca99f9b2f40fdaa74a42b88a2037a7a2e399.jpg)

图片摘要：该图主要展示 66. Effect of stall delay on lift curve slope。
![](images/9c841997a399106fb932c23bda8995f1319a450edad11dcdd1cf0780f612991f.jpg)  
Figure 66. Effect of stall delay on lift curve slope.

图片摘要：该图主要展示 66. Effect of stall delay on lift curve slope。
![](images/43406e91872d13f7395d3056939d3bcec098ae732de48f225980881383c3909c.jpg)

图片摘要：该图主要展示 66. Effect of stall delay on lift curve slope。
![](images/f0e1db542a6ec94914000ca80414d87f4617b366508263291dde60a69f21aa1a.jpg)

图片摘要：该图主要展示 66. Effect of stall delay on lift curve slopeFigure 67. Effe。
![](images/6566775b00933e65eb86c9bd53b8bc5ae77c4816d44d28f9e9603645876f9822.jpg)

图片摘要：该图主要展示 66. Effect of stall delay on lift curve slopeFigure 67. Effe。
![](images/b7f4a9a53ea0ed8ddd1c1236a43792a532a9a20ed39b676ac99afbed1c43f2f0.jpg)

图片摘要：该图主要展示 67. Effect of stall delay on lift coefficient for a set of a。
![](images/3ce384bf7a992c2a5fd04a34d9e03d9c3265eca3f31b3daf447f7915848be76a.jpg)

图片摘要：该图主要展示 67. Effect of stall delay on lift coefficient for a set of a。
![](images/25b49e8db1232f5d659a5195948ccb0b6a329dd064a24e42b02eb5e27e80ddea.jpg)  
Figure 67. Effect of stall delay on lift coefficient for a set of airfoil data at various radial stations.

# APPENDIX C—STEADY XV-15 ROTOR VALIDATION RESULTS

# Simulation Parameters

Table 16 shows a compact overview of the simulation parameters. ND stands for nondimensionalized; the boundary size is expressed as the coordinates of the corners of a rectangular prism. The grid cells indicate the amount of cells on the x, y, and z edge of the boundary, respectively. Rotor Grid Ref. and Grid Refinement indicate refinement of cells by multiplying the amount of cells by a certain factor.

TABLE 16. OVERVIEW OF STEADY SIMULATION PARAMETERS   

<table><tr><td colspan="2">Hover Parameters</td><td colspan="2">Boundary Conditions and Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.1)</td><td>Simulated time</td><td>2.5 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells (#)</td><td>30,30,42</td><td>Time steps</td><td>3000</td></tr><tr><td>Tip speed</td><td>225.55 m/s</td><td>Rotor box ref.</td><td>1,1</td><td>ΔT</td><td>2.50E-03</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor grid ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid refinement box (m)</td><td>(-7.62, -7.62, -68.58) (7.62, 7.62, 38.1)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.41E+08</td><td>Grid refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.84E+06</td><td>Volume ratio max</td><td>8</td><td>Flight condition</td><td>hover</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td>Rotor model</td><td>steady</td></tr><tr><td colspan="2">Tilt and Advance Ratio</td><td colspan="2">Boundary Conditions and Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells (#)</td><td>30,30,42</td><td>Time steps</td><td>1000</td></tr><tr><td>Tip speed</td><td>221.17 m/s</td><td>Rotor box ref.</td><td>1,1</td><td>ΔT</td><td>2.50E-03</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor grid ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid refinement box (m)</td><td>(-15.24, -7.62, -68,58) (7.62, 7.62, 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.05E+08</td><td>Grid refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.73E+06</td><td>Volume ratio max</td><td>8</td><td>Flight condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>2,029,692 (at 30 degree tilt)</td><td>Rotor model</td><td>steady</td></tr><tr><td colspan="2">Airplane Mode</td><td colspan="2">Boundary Conditions and Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells (#)</td><td>30,30,42</td><td>Time steps</td><td>1000</td></tr><tr><td>Tip speed</td><td>183.76 m/s</td><td>Rotor box ref.</td><td>1,1</td><td>ΔT</td><td>2.50E-03</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor grid ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid refinement box (m)</td><td>(-15.24, -7.62, -68,58) (7.6, 7.62, 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>3.47E+08</td><td>Grid refinement</td><td>4x</td><td>Relaxation (u, v, w, p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>1.89E+06</td><td>Volume ratio max</td><td>8</td><td>Flight condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td>Rotor model</td><td>steady</td></tr></table>

# Residual Overview

This section shows the residuals for a representative airplane mode, tilt mode, and hover mode cases in Figure 68, Figure 69, and Figure 70, respectively.

图片摘要：该图主要展示 16. OVERVIEW OF STEADY SIMULATION PARAMETERS。
![](images/7e89795200536e4bbf98531f06ce3b99aacf8e8fe81887067a7514299a5ae244.jpg)  
Figure 68. Residual overview for representative airplane mode case.

图片摘要：该图主要展示 68. Residual overview for representative airplane mode case。
![](images/18bccf7ffc6af311e2c258c6697099ff7224968ea5c93a43198d0d3c1941529a.jpg)  
Figure 69. Residual overview for representative tilt mode case with $\alpha _ { p } = 7 5$ .

图片摘要：该图主要展示 69. Residual overview for representative tilt mode case with。
![](images/1d7eebdebe535d6555fb17ab925764e919c96b23c772f8711aae61f66c0577a2.jpg)  
Figure 70. Residual overview for representative hover mode case.

# Data Steady XV-15 Rotor Results

The data used in the various plots is tabulated in Table 17.

TABLE 17. OVERVIEW OF STEADY SIMULATION RESULTS   

<table><tr><td>#</td><td>Flight Mode</td><td>File</td><td>\( \alpha_p \) (deg)</td><td>V/ΩR (m/s)</td><td>\( \theta_0 \) (deg)</td><td>T L</td><td>S D</td><td>T (N)</td><td>P (J/s)</td><td>\( C_T / \sigma (-) \)</td><td>\( C_P / \sigma (-) \)</td><td>M (-) or η (-)</td></tr><tr><td>1</td><td>Hover</td><td>0.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>N</td><td>1.467E+04</td><td>2.487E+05</td><td>6.373E-02</td><td>4.790E-03</td><td>0.675</td></tr><tr><td>2</td><td>Hover</td><td>2.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>N</td><td>1.952E+04</td><td>3.483E+05</td><td>8.480E-02</td><td>6.708E-03</td><td>0.741</td></tr><tr><td>3</td><td>Hover</td><td>4.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>N</td><td>2.457E+04</td><td>4.799E+05</td><td>1.067E-01</td><td>9.243E-03</td><td>0.759</td></tr><tr><td>4</td><td>Hover</td><td>6.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>N</td><td>2.972E+04</td><td>6.474E+05</td><td>1.291E-01</td><td>1.247E-02</td><td>0.738</td></tr><tr><td>5</td><td>Hover</td><td>8.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>N</td><td>3.466E+04</td><td>8.578E+05</td><td>1.506E-01</td><td>1.652E-02</td><td>0.710</td></tr><tr><td>6</td><td>Hover</td><td>10.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>N</td><td>3.867E+04</td><td>1.122E+06</td><td>1.680E-01</td><td>2.161E-02</td><td>0.640</td></tr><tr><td>7</td><td>Hover</td><td>0_TL_rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>N</td><td>1.450E+04</td><td>2.485E+05</td><td>6.299E-02</td><td>4.786E-03</td><td>0.665</td></tr><tr><td>8</td><td>Hover</td><td>2_TL_rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>N</td><td>1.909E+04</td><td>3.464E+05</td><td>8.293E-02</td><td>6.672E-03</td><td>0.718</td></tr><tr><td>9</td><td>Hover</td><td>4_TL_rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>N</td><td>2.373E+04</td><td>4.810E+05</td><td>1.031E-01</td><td>9.264E-03</td><td>0.720</td></tr><tr><td>10</td><td>Hover</td><td>6_TL_rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>N</td><td>2.844E+04</td><td>6.612E+05</td><td>1.235E-01</td><td>1.273E-02</td><td>0.685</td></tr><tr><td>11</td><td>Hover</td><td>8_TL_rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>N</td><td>3.282E+04</td><td>8.967E+05</td><td>1.426E-01</td><td>1.727E-02</td><td>0.678</td></tr><tr><td>12</td><td>Hover</td><td>10_TL_rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>N</td><td>3.643E+04</td><td>1.180E+06</td><td>1.583E-01</td><td>2.273E-02</td><td>0.557</td></tr><tr><td>13</td><td>Hover</td><td>0_TL_SD_rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>Y</td><td>1.669E+04</td><td>2.906E+05</td><td>7.250E-02</td><td>5.597E-03</td><td>0.703</td></tr><tr><td>14</td><td>Hover</td><td>2_TL_SD_rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>Y</td><td>2.183E+04</td><td>4.060E+05</td><td>9.483E-02</td><td>7.819E-03</td><td>0.752</td></tr><tr><td>15</td><td>Hover</td><td>4_TL_SD_rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>Y</td><td>2.712E+04</td><td>5.617E+05</td><td>1.178E-01</td><td>1.082E-02</td><td>0.753</td></tr><tr><td>16</td><td>Hover</td><td>6_TL_SD_rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>3.245E+04</td><td>7.686E+05</td><td>1.410E-01</td><td>1.480E-02</td><td>0.721</td></tr><tr><td>17</td><td>Hover</td><td>8_TL_SD_rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>Y</td><td>3.759E+04</td><td>1.031E+06</td><td>1.633E-01</td><td>1.986E-02</td><td>0.669</td></tr><tr><td>18</td><td>Hover</td><td>10_TL_SD_rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>Y</td><td>4.207E+04</td><td>1.338E+06</td><td>1.828E-01</td><td>2.577E-02</td><td>0.609</td></tr><tr><td>19</td><td>Tilt</td><td>15_18_TL_rpr</td><td>15</td><td>0.32</td><td>18.0</td><td>Y</td><td>N</td><td>8.109E+03</td><td>6.146E+05</td><td>3.663E-02</td><td>1.255E-02</td><td>NA</td></tr><tr><td>20</td><td>Tilt</td><td>15_19_TL_rpr</td><td>15</td><td>0.32</td><td>19.0</td><td>Y</td><td>N</td><td>1.208E+04</td><td>9.008E+05</td><td>5.457E-02</td><td>1.840E-02</td><td>NA</td></tr><tr><td>21</td><td>Tilt</td><td>15_20_TL_rpr</td><td>15</td><td>0.32</td><td>20.0</td><td>Y</td><td>N</td><td>1.600E+04</td><td>1.193E+06</td><td>7.227E-02</td><td>2.436E-02</td><td>NA</td></tr><tr><td>22</td><td>Tilt</td><td>15_21_TL_rpr</td><td>15</td><td>0.32</td><td>21.0</td><td>Y</td><td>N</td><td>1.985E+04</td><td>1.496E+06</td><td>8.966E-02</td><td>3.055E-02</td><td>NA</td></tr><tr><td>71</td><td>Tilt</td><td>15_175_TL_rpr</td><td>15</td><td>0.32</td><td>17.5</td><td>Y</td><td>N</td><td>6.133E+03</td><td>4.765E+05</td><td>2.770E-02</td><td>9.731E-03</td><td>NA</td></tr><tr><td>72</td><td>Tilt</td><td>15_185_TL_rpr</td><td>15</td><td>0.32</td><td>18.5</td><td>Y</td><td>N</td><td>1.009E+04</td><td>7.559E+05</td><td>4.558E-02</td><td>1.544E-02</td><td>NA</td></tr><tr><td>23</td><td>Tilt</td><td>30_155_TL_rpr</td><td>30</td><td>0.32</td><td>15.5</td><td>Y</td><td>N</td><td>8.998E+03</td><td>5.399E+05</td><td>4.064E-02</td><td>1.103E-02</td><td>NA</td></tr><tr><td>24</td><td>Tilt</td><td>30_165_TL_rpr</td><td>30</td><td>0.32</td><td>16.5</td><td>Y</td><td>N</td><td>1.289E+04</td><td>7.906E+05</td><td>5.822E-02</td><td>1.615E-02</td><td>NA</td></tr><tr><td>25</td><td>Tilt</td><td>30_175_TL_rpr</td><td>30</td><td>0.32</td><td>17.5</td><td>Y</td><td>N</td><td>1.673E+04</td><td>1.046E+06</td><td>7.557E-02</td><td>2.136E-02</td><td>NA</td></tr><tr><td>26</td><td>Tilt</td><td>30_185_TL_rpr</td><td>30</td><td>0.32</td><td>18.5</td><td>Y</td><td>N</td><td>2.045E+00</td><td>1.312E+06</td><td>9.237E-06</td><td>2.679E-02</td><td>NA</td></tr><tr><td>73</td><td>Tilt</td><td>30_15_TL_rpr</td><td>30</td><td>0.32</td><td>15.0</td><td>Y</td><td>N</td><td>7.030E+03</td><td>4.174E+05</td><td>3.175E-02</td><td>8.524E-03</td><td>NA</td></tr><tr><td>74</td><td>Tilt</td><td>30_16_TL_rpr</td><td>30</td><td>0.32</td><td>16.0</td><td>Y</td><td>N</td><td>1.095E+04</td><td>6.644E+05</td><td>4.946E-02</td><td>1.357E-02</td><td>NA</td></tr><tr><td>27</td><td>Tilt</td><td>60_8_TL_rpr</td><td>60</td><td>0.32</td><td>8.0</td><td>Y</td><td>N</td><td>1.512E+04</td><td>5.360E+05</td><td>6.830E-02</td><td>1.095E-02</td><td>NA</td></tr><tr><td>28</td><td>Tilt</td><td>60_9_TL_rpr</td><td>60</td><td>0.32</td><td>9.0</td><td>Y</td><td>N</td><td>1.865E+04</td><td>6.911E+05</td><td>8.424E-02</td><td>1.411E-02</td><td>NA</td></tr><tr><td>29</td><td>Tilt</td><td>60_10_TL_rpr</td><td>60</td><td>0.32</td><td>10.0</td><td>Y</td><td>N</td><td>2.207E+04</td><td>8.546E+05</td><td>9.969E-02</td><td>1.745E-02</td><td>NA</td></tr><tr><td>30</td><td>Tilt</td><td>60_11_TL_rpr</td><td>60</td><td>0.32</td><td>11.0</td><td>Y</td><td>N</td><td>2.525E+04</td><td>1.027E+06</td><td>1.141E-01</td><td>2.097E-02</td><td>NA</td></tr><tr><td>#</td><td>Flight Mode</td><td>File</td><td>\( \alpha_p \)(deg)</td><td>V/ΩR(m/s)</td><td>\( \theta_o \)(deg)</td><td>T L</td><td>S D</td><td>T (N)</td><td>P (J/s)</td><td>\( C_T / \sigma (-) \)</td><td>\( C_P / \sigma (-) \)</td><td>M (-) or η (-)</td></tr><tr><td>75</td><td>Tilt</td><td>60_6_TL.rpr</td><td>60</td><td>0.32</td><td>6.0</td><td>Y</td><td>N</td><td>7.823E+03</td><td>2.571E+05</td><td>3.534E-02</td><td>5.250E-03</td><td>NA</td></tr><tr><td>76</td><td>Tilt</td><td>60_7_TL.rpr</td><td>60</td><td>0.32</td><td>7.0</td><td>Y</td><td>N</td><td>1.149E+04</td><td>3.904E+05</td><td>5.190E-02</td><td>7.972E-03</td><td>NA</td></tr><tr><td>31</td><td>Tilt</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>1.374E+04</td><td>3.304E+05</td><td>6.206E-02</td><td>6.747E-03</td><td>NA</td></tr><tr><td>32</td><td>Tilt</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.716E+04</td><td>4.160E+05</td><td>7.751E-02</td><td>8.495E-03</td><td>NA</td></tr><tr><td>33</td><td>Tilt</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>2.041E+04</td><td>5.117E+05</td><td>9.219E-02</td><td>1.045E-02</td><td>NA</td></tr><tr><td>34</td><td>Tilt</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>2.358E+04</td><td>6.180E+05</td><td>1.065E-01</td><td>1.262E-02</td><td>NA</td></tr><tr><td>77</td><td>Tilt</td><td>75_1_TL.rpr</td><td>75</td><td>0.32</td><td>1.0</td><td>Y</td><td>N</td><td>1.030E+04</td><td>2.575E+05</td><td>4.652E-02</td><td>5.258E-03</td><td>NA</td></tr><tr><td>35</td><td>Advance Ratio</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>1.374E+04</td><td>3.304E+05</td><td>6.206E-02</td><td>6.747E-03</td><td>NA</td></tr><tr><td>36</td><td>Advance Ratio</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.716E+04</td><td>4.160E+05</td><td>7.751E-02</td><td>8.495E-03</td><td>NA</td></tr><tr><td>37</td><td>Advance Ratio</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>2.041E+04</td><td>5.117E+05</td><td>9.219E-02</td><td>1.045E-02</td><td>NA</td></tr><tr><td>38</td><td>Advance Ratio</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>2.358E+04</td><td>6.180E+05</td><td>1.065E-01</td><td>1.262E-02</td><td>NA</td></tr><tr><td>81</td><td>Advance Ratio</td><td>75_1_TL.rpr</td><td>75</td><td>0.32</td><td>1.0</td><td>Y</td><td>N</td><td>1.030E+04</td><td>2.575E+05</td><td>4.652E-02</td><td>5.258E-03</td><td>NA</td></tr><tr><td>39</td><td>Advance Ratio</td><td>27_75_2_TL.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.534E+04</td><td>3.345E+05</td><td>6.929E-02</td><td>6.831E-03</td><td>NA</td></tr><tr><td>40</td><td>Advance Ratio</td><td>27_75_3_TL.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>1.857E+04</td><td>4.099E+05</td><td>8.388E-02</td><td>8.371E-03</td><td>NA</td></tr><tr><td>41</td><td>Advance Ratio</td><td>27_75_4_TL.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>2.165E+04</td><td>4.965E+05</td><td>9.779E-02</td><td>1.014E-02</td><td>NA</td></tr><tr><td>82</td><td>Advance Ratio</td><td>27_75_1_TL.rpr</td><td>75</td><td>0.27</td><td>1.0</td><td>Y</td><td>N</td><td>1.209E+04</td><td>2.673E+05</td><td>5.463E-02</td><td>5.459E-03</td><td>NA</td></tr><tr><td>42</td><td>Advance Ratio</td><td>18_75_3_TL.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>2.053E+04</td><td>3.982E+05</td><td>9.273E-02</td><td>8.132E-03</td><td>NA</td></tr><tr><td>43</td><td>Advance Ratio</td><td>18_75_4_TL.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>2.325E+04</td><td>4.704E+05</td><td>1.050E-01</td><td>9.606E-03</td><td>NA</td></tr><tr><td>44</td><td>Advance Ratio</td><td>18_75_5_TL.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>2.596E+04</td><td>5.519E+05</td><td>1.173E-01</td><td>1.127E-02</td><td>NA</td></tr><tr><td>86</td><td>Advance Ratio</td><td>18_75_1_TL.rpr</td><td>75</td><td>0.18</td><td>1.0</td><td>Y</td><td>N</td><td>1.490E+04</td><td>2.792E+05</td><td>6.730E-02</td><td>5.702E-03</td><td>NA</td></tr><tr><td>87</td><td>Advance Ratio</td><td>18_75_2_TL.rpr</td><td>75</td><td>0.18</td><td>2.0</td><td>Y</td><td>N</td><td>1.771E+04</td><td>3.349E+05</td><td>8.000E-02</td><td>6.839E-03</td><td>NA</td></tr><tr><td>45</td><td>Airplane Mode</td><td>40_23_TL.rpr</td><td>0</td><td>0.40</td><td>23.0</td><td>Y</td><td>N</td><td>2.906E+03</td><td>2.762E+05</td><td>1.902E-02</td><td>9.837E-03</td><td>0.777</td></tr><tr><td>46</td><td>Airplane Mode</td><td>40_24_TL.rpr</td><td>0</td><td>0.40</td><td>24.0</td><td>Y</td><td>N</td><td>5.753E+03</td><td>4.902E+05</td><td>3.765E-02</td><td>1.746E-02</td><td>0.866</td></tr><tr><td>47</td><td>Airplane Mode</td><td>40_25_TL.rpr</td><td>0</td><td>0.40</td><td>25.0</td><td>Y</td><td>N</td><td>8.577E+03</td><td>7.101E+05</td><td>5.613E-02</td><td>2.529E-02</td><td>0.892</td></tr><tr><td>48</td><td>Airplane Mode</td><td>40_26_TL.rpr</td><td>0</td><td>0.40</td><td>26.0</td><td>Y</td><td>N</td><td>1.140E+04</td><td>9.343E+05</td><td>7.461E-02</td><td>3.328E-02</td><td>0.901</td></tr><tr><td>78</td><td>Airplane Mode</td><td>40_225_TL.rpr</td><td>0</td><td>0.40</td><td>22.5</td><td>Y</td><td>N</td><td>1.480E+03</td><td>1.706E+05</td><td>9.686E-03</td><td>6.076E-03</td><td>0.640</td></tr><tr><td>79</td><td>Airplane Mode</td><td>40_255_TL.rpr</td><td>0</td><td>0.40</td><td>25.5</td><td>Y</td><td>N</td><td>9.988E+03</td><td>8.215E+05</td><td>6.537E-02</td><td>2.926E-02</td><td>0.898</td></tr><tr><td>49</td><td>Airplane Mode</td><td>70_375_TL.rpr</td><td>0</td><td>0.70</td><td>37.5</td><td>Y</td><td>N</td><td>3.328E+03</td><td>5.535E+05</td><td>2.178E-02</td><td>1.971E-02</td><td>0.777</td></tr><tr><td>50</td><td>Airplane Mode</td><td>70_385_TL.rpr</td><td>0</td><td>0.70</td><td>38.5</td><td>Y</td><td>N</td><td>7.193E+03</td><td>1.054E+06</td><td>4.707E-02</td><td>3.754E-02</td><td>0.882</td></tr><tr><td>51</td><td>Airplane Mode</td><td>70_395_TL.rpr</td><td>0</td><td>0.70</td><td>39.5</td><td>Y</td><td>N</td><td>1.098E+04</td><td>1.559E+06</td><td>7.186E-02</td><td>5.553E-02</td><td>0.910</td></tr><tr><td>52</td><td>Airplane Mode</td><td>70_405_TL.rpr</td><td>0</td><td>0.70</td><td>40.5</td><td>Y</td><td>N</td><td>1.471E+04</td><td>2.073E+06</td><td>9.627E-02</td><td>7.383E-02</td><td>0.917</td></tr><tr><td>80</td><td>Airplane Mode</td><td>70_37_TL.rpr</td><td>0</td><td>0.70</td><td>37.0</td><td>Y</td><td>N</td><td>1.369E+03</td><td>3.036E+05</td><td>6.184E-03</td><td>6.200E-03</td><td>0.583</td></tr><tr><td>53</td><td>Hover</td><td>6_TL_SD_GC.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>54</td><td>Hover</td><td>6_TL_SD_GE.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>55</td><td>Hover</td><td>6_TL_SD_IR.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>56</td><td>Hover</td><td>10_TL_SD_IR2.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>57</td><td>Advance Ratio</td><td>27_75_2_TL_SD.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.812E+04</td><td>3.915E+05</td><td>8.185E-02</td><td>7.995E-03</td><td>NA</td></tr><tr><td>58</td><td>Advance Ratio</td><td>27_75_3_TL_SD.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>2.173E+04</td><td>4.780E+05</td><td>9.815E-02</td><td>9.761E-03</td><td>NA</td></tr></table>

TABLE 17. (concluded)   

<table><tr><td>#</td><td>Flight Mode</td><td>File</td><td>\(a_p\)(deg)</td><td>V/ΩR(m/s)</td><td>\(θ_o\)(deg)</td><td>T L</td><td>S D</td><td>T (N)</td><td>P (J/s)</td><td>\(C_T/σ (-)\)</td><td>\(C_P/σ (-)\)</td><td>M (-) or η (-)</td></tr><tr><td>59</td><td>Advance Ratio</td><td>27_75_4_TL_SD.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>2.530E+04</td><td>5.765E+05</td><td>1.143E-01</td><td>1.177E-02</td><td>NA</td></tr><tr><td>88</td><td>Advance Ratio</td><td>27_75_1_TL_SD.rpr</td><td>75</td><td>0.27</td><td>1.0</td><td>Y</td><td>N</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>87</td><td>Advance Ratio</td><td>27_75_0_TL_SD.rpr</td><td>75</td><td>0.27</td><td>0.0</td><td>Y</td><td>N</td><td>1.089E+04</td><td>2.507E+05</td><td>4.919E-02</td><td>5.120E-03</td><td>NA</td></tr><tr><td>61</td><td>Advance Ratio</td><td>18_75_3_TL_SD.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>2.368E+04</td><td>4.659E+05</td><td>1.070E-01</td><td>9.514E-03</td><td>NA</td></tr><tr><td>62</td><td>Advance Ratio</td><td>18_75_4_TL_SD.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>2.681E+04</td><td>5.488E+05</td><td>1.211E-01</td><td>1.121E-02</td><td>NA</td></tr><tr><td>63</td><td>Advance Ratio</td><td>18_75_5_TL_SD.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>2.988E+04</td><td>6.429E+05</td><td>1.350E-01</td><td>1.313E-02</td><td>NA</td></tr><tr><td>83</td><td>Advance Ratio</td><td>18_75_1_TL_SD.rpr</td><td>75</td><td>0.18</td><td>1.0</td><td>Y</td><td>N</td><td>1.733E+04</td><td>3.264E+05</td><td>7.828E-02</td><td>6.666E-03</td><td>NA</td></tr><tr><td>84</td><td>Advance Ratio</td><td>18_75_2_TL_SD.rpr</td><td>75</td><td>0.18</td><td>2.0</td><td>Y</td><td>N</td><td>2.049E+04</td><td>3.915E+05</td><td>9.255E-02</td><td>7.995E-03</td><td>NA</td></tr><tr><td>85</td><td>Advance Ratio</td><td>18_75_3_TL_SD.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>2.368E+04</td><td>4.659E+05</td><td>1.070E-01</td><td>9.514E-03</td><td>NA</td></tr><tr><td>86</td><td>Advance Ratio</td><td>18_75_0_TL_SD.rpr</td><td>75</td><td>0.18</td><td>0.0</td><td>Y</td><td>N</td><td>1.415E+04</td><td>2.704E+05</td><td>6.392E-02</td><td>5.522E-03</td><td>NA</td></tr><tr><td>64</td><td>Hover</td><td>10_SD.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>Y</td><td>4.447E+04</td><td>1.291E+06</td><td>1.932E-01</td><td>2.486E-02</td><td>0.688</td></tr><tr><td>65</td><td>Hover</td><td>0_SD.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>Y</td><td>1.682E+04</td><td>2.903E+05</td><td>7.307E-02</td><td>5.591E-03</td><td>0.711</td></tr><tr><td>66</td><td>Hover</td><td>2_SD.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>Y</td><td>2.237E+04</td><td>4.075E+05</td><td>9.718E-02</td><td>7.848E-03</td><td>0.773</td></tr><tr><td>67</td><td>Hover</td><td>4_SD.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>Y</td><td>2.800E+04</td><td>5.617E+05</td><td>1.216E-01</td><td>1.082E-02</td><td>0.790</td></tr><tr><td>68</td><td>Hover</td><td>6_SD.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>Y</td><td>3.391E+04</td><td>7.559E+05</td><td>1.473E-01</td><td>1.456E-02</td><td>0.781</td></tr><tr><td>69</td><td>Hover</td><td>8_SD.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>Y</td><td>3.962E+04</td><td>9.945E+05</td><td>1.721E-01</td><td>1.915E-02</td><td>0.749</td></tr><tr><td>89</td><td>Tilt</td><td>15_18.rpr</td><td>15</td><td>0.32</td><td>18.0</td><td>N</td><td>N</td><td>8.523E+03</td><td>6.435E+05</td><td>3.850E-02</td><td>1.314E-02</td><td>NA</td></tr><tr><td>90</td><td>Tilt</td><td>75_3.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>N</td><td>N</td><td>1.705E+04</td><td>4.130E+05</td><td>7.701E-02</td><td>8.434E-03</td><td>NA</td></tr><tr><td>91</td><td>Advance Ratio</td><td>18_75_3.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>N</td><td>N</td><td>2.075E+04</td><td>3.998E+05</td><td>9.373E-02</td><td>8.164E-03</td><td>NA</td></tr><tr><td>92</td><td>Airplane Mode</td><td>40_24.rpr</td><td>0</td><td>0.40</td><td>24.0</td><td>N</td><td>N</td><td>6.246E+03</td><td>5.274E+05</td><td>4.088E-02</td><td>1.878E-02</td><td>0.874</td></tr></table>

# APPENDIX D—UNSTEADY XV-15 ROTOR VALIDATION RESULTS

# Simulations Parameters

Table 18 shows a compact overview of the simulation parameters. ND stands for nondimensionalized; the boundary size is expressed as the coordinates of the corners of a rectangular prism. The grid cells indicate the amount of cells on the x, y, and z edge of the boundary, respectively. Rotor Grid Ref. and Grid Refinement indicate refinement of cells by multiplying the amount of cells by a certain factor.

TABLE 18. OVERVIEW OF UNSTEADY SIMULATION PARAMETERS   

<table><tr><td colspan="2">Hover Parameters</td><td colspan="2">Boundary Conditions and Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.1)</td><td>Simulated time</td><td>2.5 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells (#)</td><td>30,30,42</td><td>Time steps</td><td>3000</td></tr><tr><td>Tip speed</td><td>225.55 m/s</td><td>Rotor box ref.</td><td>1,1</td><td>ΔT</td><td>8.33E-04</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor grid ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid refinement box (m)</td><td>(-7.62, -7.62, -68.58) (7.62, 7.62, 38.1)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.41E+08</td><td>Grid refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.84E+06</td><td>Volume ratio max</td><td>8</td><td>Flight condition</td><td>hover</td></tr><tr><td></td><td></td><td>Cells</td><td>1,053,948</td><td>Rotor model</td><td></td></tr><tr><td colspan="2">Tilt and Advance Ratio</td><td colspan="2">Boundary Conditions and Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells (#)</td><td>30,30,42</td><td>Time steps</td><td>1000</td></tr><tr><td>Tip speed</td><td>221.17 m/s</td><td>Rotor box ref.</td><td>1,1</td><td>ΔT</td><td>8.33E-04</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor grid ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid refinement box (m)</td><td>(-15.24, -7.62, -68,58) (7.62, 7.62, 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>6.05E+08</td><td>Grid refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>2.73E+06</td><td>Volume ratio max</td><td>8</td><td>Flight condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td>2,029,692 (at 30 degree tilt)</td><td></td><td></td></tr><tr><td colspan="2">Airplane Mode</td><td colspan="2">Boundary Conditions and Grid</td><td colspan="2">Simulation Variables</td></tr><tr><td>Radius</td><td>3.81 m</td><td>Boundary size</td><td>(-38.1, -38.1, -68.58) (38.1, 38.1, 38.10)</td><td>Simulated time</td><td>1.25 s</td></tr><tr><td>Cone angle</td><td>2.5 deg</td><td>Grid cells (#)</td><td>30,30,42</td><td>Time steps</td><td>1000</td></tr><tr><td>Tip speed</td><td>183.76 m/s</td><td>Rotor box ref.</td><td>1,1</td><td>ΔT</td><td>8.33E-04</td></tr><tr><td>Cutout</td><td>0.0875 r/R</td><td>Rotor grid ref.</td><td>6x</td><td>ΔXmin</td><td>0.0784</td></tr><tr><td>Solidity</td><td>0.081</td><td>Grid refinement box (m)</td><td>(-15.24, -7.62, -68,58) (7.6, 7.62, 38.10)</td><td>Iterations</td><td>10</td></tr><tr><td>Power ND</td><td>3.47E+08</td><td>Grid refinement</td><td>4x</td><td>Relaxation (u,v,w,p)</td><td>0.1</td></tr><tr><td>Thrust ND</td><td>1.89E+06</td><td>Volume ratio max</td><td>8</td><td>Flight condition</td><td>general</td></tr><tr><td></td><td></td><td>Cells</td><td colspan="2">1,053,948</td><td></td></tr></table>

# Hover—Unsteady

Figure 71 and Figure 72 show, analogous to the steady results, the hover performance for the unsteady model of the XV-15 rotor in RotUNS.

Both graphs show serious error in excess of 10 percent, compared to the presented theoretical and experimental data.

图片摘要：该图主要展示 71 and Figure 72 show, analogous to the steady results, the 。
![](images/9fe19e7fbca99351af1e42c88e4f4105e9085a120fdcab7c6fae831244643c52.jpg)  
Figure 71. Unsteady results for XV-15 rotor hover power as a function of thrust [21], [25].

图片摘要：该图主要展示 71. Unsteady results for XV 15 rotor hover power as a functi。
![](images/2a15c50f6e142ac6b8069d8d25406c19f60c7a5eb21c9a83f39c01c8515bf0c8.jpg)  
Figure 72. Unsteady results for XV-15 rotor hover figure of merit as a function of thrust [21], [25].

# Tilt Mode—Unsteady

Figure 73 and Figure 74 show, analogous to the steady results, the tilt mode performance and the sensitivity to advance ratio variations for the unsteady model of the XV-15 rotor in RotUNS.

The results for the various tilt modes correlate slightly better than the hover performance; the steady model, however, outperforms the unsteady model in terms of accuracy.

图片摘要：该图主要展示 73 and Figure 74 show, analogous to the steady results, the 。
![](images/153d7d042f401306e42e71186e1c3edba4cd49464ab0f2f67343f0d7af010b3c.jpg)  
Figure 73. Unsteady results for XV-15 rotor power as a function of thrust for various pylon angles at $V / \Omega R = 0 . 3 2$ [25].

图片摘要：该图主要展示 73. Unsteady results for XV 15 rotor power as a function of 。
![](images/721ebda3335bd91d5f4196550155a2d58b99b926447e1b134993b996fc4705e2.jpg)  
Figure 74. Unsteady results for XV-15 rotor power as a function of thrust, for $\alpha _ { p } = 7 5 ^ { \circ }$ and $M _ { t i p } = 0 . 6 5$ [25].

The variation of advance ratio shows similar performance to CAMRAD I.

# Airplane Mode—Unsteady

Figure 75 shows, analogous to the steady results, airplane mode performance for the unsteady model of the XV-15 rotor in RotUNS.

图片摘要：该图主要展示 75 shows, analogous to the steady results, airplane mode per。
![](images/edb722efef6ef5d0d4cf53ae3449d0f6ff1618c9109478ff388ba951395c2cdc.jpg)  
Figure 75. Unsteady results for (rotor) propulsive efficiency as a function of thrust [25].

# Data Unsteady XV-15 Rotor Results

The data used in the various plots is tabulated in Table 19.

TABLE 19. OVERVIEW OF UNSTEADY SIMULATION RESULTS   

<table><tr><td>#</td><td>Flight Mode</td><td>File</td><td>\( \alpha_p \) (deg)</td><td>V/ΩR (m/s)</td><td>\( \theta_o \) (deg)</td><td>T L</td><td>S D</td><td>T (N)</td><td>P (J/s)</td><td>\( C_T / \sigma (-) \)</td><td>\( C_P / \sigma (-) \)</td><td>M (-) or η (-)</td></tr><tr><td>1</td><td>Hover</td><td>0.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>N</td><td>1.100E+04</td><td>2.170E+05</td><td>4.778E-02</td><td>4.179E-03</td><td>0.505</td></tr><tr><td>2</td><td>Hover</td><td>2.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>N</td><td>1.460E+04</td><td>3.020E+05</td><td>6.342E-02</td><td>5.816E-03</td><td>0.552</td></tr><tr><td>3</td><td>Hover</td><td>4.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>N</td><td>1.820E+04</td><td>4.130E+05</td><td>7.906E-02</td><td>7.954E-03</td><td>0.562</td></tr><tr><td>4</td><td>Hover</td><td>6.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>N</td><td>2.170E+04</td><td>5.510E+05</td><td>9.427E-02</td><td>1.061E-02</td><td>0.552</td></tr><tr><td>5</td><td>Hover</td><td>8.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>N</td><td>2.500E+04</td><td>7.170E+05</td><td>1.086E-01</td><td>1.381E-02</td><td>0.524</td></tr><tr><td>6</td><td>Hover</td><td>10.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>N</td><td>2.800E+04</td><td>9.080E+05</td><td>1.216E-01</td><td>1.749E-02</td><td>0.489</td></tr><tr><td>7</td><td>Hover</td><td>0_TL.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>N</td><td>1.070E+04</td><td>2.160E+05</td><td>4.648E-02</td><td>4.160E-03</td><td>0.481</td></tr><tr><td>8</td><td>Hover</td><td>2_TL.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>N</td><td>1.400E+04</td><td>3.000E+05</td><td>6.082E-02</td><td>5.778E-03</td><td>0.526</td></tr><tr><td>9</td><td>Hover</td><td>4_TL.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>N</td><td>1.730E+04</td><td>4.070E+05</td><td>7.515E-02</td><td>7.839E-03</td><td>0.531</td></tr><tr><td>10</td><td>Hover</td><td>6_TL.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>N</td><td>2.040E+04</td><td>5.410E+05</td><td>8.862E-02</td><td>1.042E-02</td><td>0.513</td></tr><tr><td>11</td><td>Hover</td><td>8_TL.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>N</td><td>2.350E+04</td><td>7.100E+05</td><td>1.021E-01</td><td>1.367E-02</td><td>0.483</td></tr><tr><td>12</td><td>Hover</td><td>10_TL.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>N</td><td>2.620E+04</td><td>9.070E+05</td><td>1.138E-01</td><td>1.747E-02</td><td>0.442</td></tr><tr><td>13</td><td>Hover</td><td>0_TL_SD.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>Y</td><td>Y</td><td>1.270E+04</td><td>2.540E+05</td><td>5.517E-02</td><td>4.892E-03</td><td>0.545</td></tr><tr><td>14</td><td>Hover</td><td>2_TL_SD.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>Y</td><td>Y</td><td>1.698E+04</td><td>3.492E+05</td><td>7.375E-02</td><td>6.726E-03</td><td>0.584</td></tr><tr><td>15</td><td>Hover</td><td>4_TL_SD.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>Y</td><td>Y</td><td>2.020E+04</td><td>4.750E+05</td><td>8.775E-02</td><td>9.148E-03</td><td>0.573</td></tr><tr><td>16</td><td>Hover</td><td>6_TL_SD.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.390E+04</td><td>6.310E+05</td><td>1.038E-01</td><td>1.215E-02</td><td>0.554</td></tr><tr><td>17</td><td>Hover</td><td>8_TL_SD.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>Y</td><td>Y</td><td>2.730E+04</td><td>8.170E+05</td><td>1.186E-01</td><td>1.574E-02</td><td>0.520</td></tr><tr><td>18</td><td>Hover</td><td>10_TL_SD.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>Y</td><td>Y</td><td>3.040E+04</td><td>1.040E+06</td><td>1.321E-01</td><td>2.003E-02</td><td>0.480</td></tr><tr><td>19</td><td>Tilt</td><td>15_18_TL.rpr</td><td>15</td><td>0.32</td><td>18.0</td><td>Y</td><td>N</td><td>4.660E+03</td><td>3.970E+05</td><td>2.105E-02</td><td>8.107E-03</td><td>NA</td></tr><tr><td>20</td><td>Tilt</td><td>15_19_TL.rpr</td><td>15</td><td>0.32</td><td>19.0</td><td>Y</td><td>N</td><td>7.020E+03</td><td>5.770E+05</td><td>3.171E-02</td><td>1.178E-02</td><td>NA</td></tr><tr><td>21</td><td>Tilt</td><td>15_20_TL.rpr</td><td>15</td><td>0.32</td><td>20.0</td><td>Y</td><td>N</td><td>9.390E+03</td><td>7.670E+05</td><td>4.241E-02</td><td>1.566E-02</td><td>NA</td></tr><tr><td>22</td><td>Tilt</td><td>15_21_TL.rpr</td><td>15</td><td>0.32</td><td>21.0</td><td>Y</td><td>N</td><td>1.160E+04</td><td>9.610E+05</td><td>5.240E-02</td><td>1.962E-02</td><td>NA</td></tr><tr><td>23</td><td>Tilt</td><td>30_155_TL.rpr</td><td>30</td><td>0.32</td><td>15.5</td><td>Y</td><td>N</td><td>4.918E+03</td><td>3.443E+05</td><td>2.221E-02</td><td>7.031E-03</td><td>NA</td></tr><tr><td>24</td><td>Tilt</td><td>30_165_TL.rpr</td><td>30</td><td>0.32</td><td>16.5</td><td>Y</td><td>N</td><td>7.218E+03</td><td>5.011E+05</td><td>3.260E-02</td><td>1.023E-02</td><td>NA</td></tr><tr><td>25</td><td>Tilt</td><td>30_175_TL.rpr</td><td>30</td><td>0.32</td><td>17.5</td><td>Y</td><td>N</td><td>9.489E+03</td><td>6.648E+05</td><td>4.286E-02</td><td>1.358E-02</td><td>NA</td></tr><tr><td>26</td><td>Tilt</td><td>30_185_TL.rpr</td><td>30</td><td>0.32</td><td>18.5</td><td>Y</td><td>N</td><td>1.175E+04</td><td>8.360E+05</td><td>5.307E-02</td><td>1.707E-02</td><td>NA</td></tr><tr><td>27</td><td>Tilt</td><td>60_8_TL.rpr</td><td>60</td><td>0.32</td><td>8.0</td><td>Y</td><td>N</td><td>8.855E+03</td><td>3.655E+05</td><td>4.000E-02</td><td>7.463E-03</td><td>NA</td></tr><tr><td>28</td><td>Tilt</td><td>60_9_TL.rpr</td><td>60</td><td>0.32</td><td>9.0</td><td>Y</td><td>N</td><td>1.104E+04</td><td>4.647E+05</td><td>4.985E-02</td><td>9.489E-03</td><td>NA</td></tr><tr><td>29</td><td>Tilt</td><td>60_10_TL.rpr</td><td>60</td><td>0.32</td><td>10.0</td><td>Y</td><td>N</td><td>1.316E+04</td><td>5.738E+05</td><td>5.944E-02</td><td>1.172E-02</td><td>NA</td></tr><tr><td>30</td><td>Tilt</td><td>60_11_TL.rpr</td><td>60</td><td>0.32</td><td>11.0</td><td>Y</td><td>N</td><td>1.524E+04</td><td>6.855E+05</td><td>6.884E-02</td><td>1.400E-02</td><td>NA</td></tr><tr><td>31</td><td>Tilt</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>8.970E+03</td><td>2.660E+05</td><td>4.052E-02</td><td>5.432E-03</td><td>NA</td></tr><tr><td>32</td><td>Tilt</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.120E+04</td><td>3.250E+05</td><td>5.059E-02</td><td>6.637E-03</td><td>NA</td></tr><tr><td>33</td><td>Tilt</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>1.330E+04</td><td>3.920E+05</td><td>6.008E-02</td><td>8.005E-03</td><td>NA</td></tr><tr><td>34</td><td>Tilt</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>1.543E+04</td><td>4.673E+05</td><td>6.970E-02</td><td>9.544E-03</td><td>NA</td></tr><tr><td>35</td><td>Advance Ratio</td><td>75_2_TL.rpr</td><td>75</td><td>0.32</td><td>2.0</td><td>Y</td><td>N</td><td>8.970E+03</td><td>2.660E+05</td><td>4.052E-02</td><td>5.432E-03</td><td>NA</td></tr><tr><td>36</td><td>Advance Ratio</td><td>75_3_TL.rpr</td><td>75</td><td>0.32</td><td>3.0</td><td>Y</td><td>N</td><td>1.120E+04</td><td>3.250E+05</td><td>5.059E-02</td><td>6.637E-03</td><td>NA</td></tr><tr><td>37</td><td>Advance Ratio</td><td>75_4_TL.rpr</td><td>75</td><td>0.32</td><td>4.0</td><td>Y</td><td>N</td><td>1.330E+04</td><td>3.920E+05</td><td>6.008E-02</td><td>8.005E-03</td><td>NA</td></tr><tr><td>38</td><td>Advance Ratio</td><td>75_5_TL.rpr</td><td>75</td><td>0.32</td><td>5.0</td><td>Y</td><td>N</td><td>1.543E+04</td><td>4.673E+05</td><td>6.970E-02</td><td>9.544E-03</td><td>NA</td></tr><tr><td>39</td><td>Advance Ratio</td><td>27_75_2_TL.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.007E+04</td><td>2.710E+05</td><td>4.548E-02</td><td>5.533E-03</td><td>NA</td></tr><tr><td>40</td><td>Advance Ratio</td><td>27_75_3_TL.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>1.220E+04</td><td>3.260E+05</td><td>5.511E-02</td><td>6.657E-03</td><td>NA</td></tr><tr><td>41</td><td>Advance Ratio</td><td>27_75_4_TL.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>1.424E+04</td><td>3.911E+05</td><td>6.431E-02</td><td>7.987E-03</td><td>NA</td></tr><tr><td>42</td><td>Advance Ratio</td><td>18_75_3_TL.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>1.390E+04</td><td>3.330E+05</td><td>6.279E-02</td><td>6.800E-03</td><td>NA</td></tr><tr><td>43</td><td>Advance Ratio</td><td>18_75_4_TL.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>1.577E+04</td><td>3.913E+05</td><td>7.123E-02</td><td>7.991E-03</td><td>NA</td></tr><tr><td>44</td><td>Advance Ratio</td><td>18_75_5_TL.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>1.760E+04</td><td>4.560E+05</td><td>7.950E-02</td><td>9.312E-03</td><td>NA</td></tr><tr><td>45</td><td>Airplane Mode</td><td>40_23_TL.rpr</td><td>0</td><td>0.40</td><td>23.0</td><td>Y</td><td>N</td><td>1.404E+03</td><td>1.670E+05</td><td>6.341E-03</td><td>3.410E-03</td><td>0.621</td></tr><tr><td>46</td><td>Airplane Mode</td><td>40_24_TL.rpr</td><td>0</td><td>0.40</td><td>24.0</td><td>Y</td><td>N</td><td>3.128E+03</td><td>3.016E+05</td><td>1.413E-02</td><td>6.159E-03</td><td>0.766</td></tr><tr><td>47</td><td>Airplane Mode</td><td>40_25_TL.rpr</td><td>0</td><td>0.40</td><td>25.0</td><td>Y</td><td>N</td><td>4.820E+03</td><td>4.385E+05</td><td>2.177E-02</td><td>8.955E-03</td><td>0.811</td></tr><tr><td>48</td><td>Airplane Mode</td><td>40_26_TL.rpr</td><td>0</td><td>0.40</td><td>26.0</td><td>Y</td><td>N</td><td>6.478E+03</td><td>5.794E+05</td><td>2.926E-02</td><td>1.183E-02</td><td>0.825</td></tr><tr><td>49</td><td>Airplane Mode</td><td>70_375_TL.rpr</td><td>0</td><td>0.70</td><td>37.5</td><td>Y</td><td>N</td><td>1.397E+03</td><td>3.099E+05</td><td>6.308E-03</td><td>6.329E-03</td><td>0.582</td></tr><tr><td>50</td><td>Airplane Mode</td><td>70_385_TL.rpr</td><td>0</td><td>0.70</td><td>38.5</td><td>Y</td><td>N</td><td>3.607E+03</td><td>6.043E+05</td><td>1.629E-02</td><td>1.234E-02</td><td>0.771</td></tr><tr><td>51</td><td>Airplane Mode</td><td>70_395_TL.rpr</td><td>0</td><td>0.70</td><td>39.5</td><td>Y</td><td>N</td><td>5.737E+03</td><td>9.014E+05</td><td>2.591E-02</td><td>1.841E-02</td><td>0.822</td></tr><tr><td>52</td><td>Airplane Mode</td><td>70_405_TL.rpr</td><td>0</td><td>0.70</td><td>40.5</td><td>Y</td><td>N</td><td>7.800E+03</td><td>1.200E+06</td><td>3.523E-02</td><td>2.451E-02</td><td>0.840</td></tr><tr><td>53</td><td>Hover</td><td>6_TL_SD_GC.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.390E+04</td><td>6.159E+05</td><td>1.038E-01</td><td>1.186E-02</td><td>NA</td></tr><tr><td>54</td><td>Hover</td><td>6_TL_SD_GE.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.390E+04</td><td>6.300E+05</td><td>1.038E-01</td><td>1.213E-02</td><td>0.552</td></tr><tr><td>55</td><td>Hover</td><td>6_TL_SD_IR.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.359E+04</td><td>6.299E+05</td><td>1.025E-01</td><td>1.213E-02</td><td>0.545</td></tr><tr><td>56</td><td>Hover</td><td>10_TL_SD_IR2.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>Y</td><td>Y</td><td>2.980E+04</td><td>1.030E+06</td><td>1.295E-01</td><td>1.984E-02</td><td>0.472</td></tr><tr><td>58</td><td>Advance Ratio</td><td>27_75_2_TL_SD.rpr</td><td>75</td><td>0.27</td><td>2.0</td><td>Y</td><td>N</td><td>1.202E+04</td><td>3.146E+05</td><td>5.428E-02</td><td>6.425E-03</td><td>NA</td></tr><tr><td>59</td><td>Advance Ratio</td><td>27_75_3_TL_SD.rpr</td><td>75</td><td>0.27</td><td>3.0</td><td>Y</td><td>N</td><td>1.435E+04</td><td>3.789E+05</td><td>6.482E-02</td><td>7.738E-03</td><td>NA</td></tr><tr><td>60</td><td>Advance Ratio</td><td>27_75_4_TL_SD.rpr</td><td>75</td><td>0.27</td><td>4.0</td><td>Y</td><td>N</td><td>1.669E+04</td><td>4.516E+05</td><td>7.539E-02</td><td>9.222E-03</td><td>NA</td></tr><tr><td>61</td><td>Advance Ratio</td><td>18_75_3_TL_SD.rpr</td><td>75</td><td>0.18</td><td>3.0</td><td>Y</td><td>N</td><td>1.619E+04</td><td>3.868E+05</td><td>7.313E-02</td><td>7.899E-03</td><td>NA</td></tr><tr><td>62</td><td>Advance Ratio</td><td>18_75_4_TL_SD.rpr</td><td>75</td><td>0.18</td><td>4.0</td><td>Y</td><td>N</td><td>1.832E+04</td><td>4.538E+05</td><td>8.275E-02</td><td>9.267E-03</td><td>NA</td></tr><tr><td>63</td><td>Advance Ratio</td><td>18_75_5_TL_SD.rpr</td><td>75</td><td>0.18</td><td>5.0</td><td>Y</td><td>N</td><td>2.037E+04</td><td>5.276E+05</td><td>9.201E-02</td><td>1.077E-02</td><td>NA</td></tr><tr><td>64</td><td>Hover</td><td>10_SD.rpr</td><td>90</td><td>0.00</td><td>10.0</td><td>N</td><td>Y</td><td>3.267E+04</td><td>1.044E+06</td><td>1.419E-01</td><td>2.010E-02</td><td>0.526</td></tr><tr><td>65</td><td>Hover</td><td>0_SD.rpr</td><td>90</td><td>0.00</td><td>0.0</td><td>N</td><td>Y</td><td>1.278E+04</td><td>2.525E+05</td><td>5.552E-02</td><td>4.863E-03</td><td>0.526</td></tr><tr><td>66</td><td>Hover</td><td>2_SD.rpr</td><td>90</td><td>0.00</td><td>2.0</td><td>N</td><td>Y</td><td>1.696E+04</td><td>3.515E+05</td><td>7.368E-02</td><td>6.769E-03</td><td>0.608</td></tr><tr><td>67</td><td>Hover</td><td>4_SD.rpr</td><td>90</td><td>0.00</td><td>4.0</td><td>N</td><td>Y</td><td>2.118E+04</td><td>4.801E+05</td><td>9.201E-02</td><td>9.246E-03</td><td>0.601</td></tr><tr><td>68</td><td>Hover</td><td>6_SD.rpr</td><td>90</td><td>0.00</td><td>6.0</td><td>N</td><td>Y</td><td>2.512E+04</td><td>6.389E+05</td><td>1.091E-01</td><td>1.231E-02</td><td>0.593</td></tr><tr><td>69</td><td>Hover</td><td>8_SD.rpr</td><td>90</td><td>0.00</td><td>8.0</td><td>N</td><td>Y</td><td>2.903E+04</td><td>8.273E+05</td><td>1.261E-01</td><td>1.593E-02</td><td>0.563</td></tr></table>
