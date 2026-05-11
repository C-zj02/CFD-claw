# VIPER Integrated MDAO Analysis for Conceptual Design of Supersonic X-Plane Vehicles

Joseph A. Garcia, Jeffrey V. Bowles, David J. Kinney, and John E. Melton

Systems Analysis Branch

NASA Ames Research Center, CA

Xun J. Jiang

Science and Technology Corporation

NASA Research Park, CA

# NASA STI Program ... in Profile

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA scientific and technical information (STI) program plays a key part in helping NASA maintain this important role.

The NASA STI program operates under the auspices of the Agency Chief Information Officer. It collects, organizes, provides for archiving, and disseminates NASA’s STI. The NASA STI program provides access to the NTRS Registered and its public interface, the NASA Technical Reports Server, thus providing one of the largest collections of aeronautical and space science STI in the world. Results are published in both non-NASA channels and by NASA in the NASA STI Report Series, which includes the following report types:

TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA Programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counterpart of peer-reviewed formal professional papers but has less stringent limitations on manuscript length and extent of graphic presentations.   
TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., quick release reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.   
CONTRACTOR REPORT. Scientific and technical findings by NASA-sponsored contractors and grantees.

CONFERENCE PUBLICATION. Collected papers from scientific and technical conferences, symposia, seminars, or other meetings sponsored or co-sponsored by NASA.   
SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
TECHNICAL TRANSLATION. English-language translations of foreign scientific and technical material pertinent to NASA’s mission.

Specialized services also include organizing and publishing research results, distributing specialized research announcements and feeds, providing information desk and personal search support, and enabling data exchange services.

For more information about the NASA STI program, see the following:

Access the NASA STI program home page at http://www.sti.nasa.gov   
• E-mail your question to help@sti.nasa.gov   
Phone the NASA STI Information Desk at 757-864-9658   
Write to: NASA STI Information Desk Mail Stop 148 NASA Langley Research Center Hampton, VA 23681-2199

# VIPER Integrated MDAO Analysis for Conceptual Design of Supersonic X-Plane Vehicles

Joseph A. Garcia, Jeffrey V. Bowles, David J. Kinney, and John E. Melton

Systems Analysis Branch

Ames Research Center, Moffett Field, California

Xun J. Jiang

Science and Technology Corporation

NASA Research Park, CA

National Aeronautics and

Space Administration

Ames Research Center

Moffett Field, CA 94035-1000

# Acknowledgements

This work was done in support of NASA’s Multidisciplinary Design Analysis and Optimization team within the Transformational Tools and Technologies projects as well as the Low-Boom Flight Demonstration project for supporting information.

This report is available in electronic form at

http://

# Abstract

A streamlined Multidisciplinary Design Analysis and Optimization (MDAO) process is being developed to provide feedback on conceptual designs and early airspace modeling assessments of unconventional aircraft. This MDAO process has been demonstrated using a Low-Boom Flight Demonstrator (LBFD) like configuration by performing a trade study of various flap sizes. The results of these trades showed that shorter takeoff distances are achieved with increasing flap chord and flap deflections. This trend is unlike conventional transport type aircraft which typically show increased required takeoff distances due to the increased drag during typical takeoff flap configurations. The LBFD-like configuration trends are attributed to its high engine thrust which overcomes the higher drag associated with its takeoff flap configuration.

# Introduction

The purpose of this work was to develop a streamlined process to assess performance of new unconventional aircraft concepts in order to provide feedback on the conceptual design, address possible vehicle handling quality concerns, as well as provide aerodynamic performance data to inform airspace modeling of these vehicles. The aircraft chosen to demonstrate this capability was based on a Low-Boom Flight Demonstrator (LBFD) configuration.

# Approach

The approach used was to integrate the OpenVSP parametric geometry tool, the VSPAERO aerodynamics performance tool, along with the aircraft synthesis and mission analysis tool, VASCOMP, into our Multidisciplinary Design Analysis and Optimization (MDAO) VIPER framework which in turn provided the vehicle performance datasets. From this, we were able to demonstrate a trade study of flap size and its impact on takeoff and landing performance of the LBFD-like configuration.

图片摘要：该图主要展示 1 VIPER LBFD Study process overview。
![](images/3a304f478f2a68a08c3e10a8ac619751393b4725831f2247b3d79237ba394829.jpg)  
Figure-1 VIPER LBFD Study process overview

OpenVSP was utilized to generate parametric LBFD geometry with variations of the inboard and outboard flap chord, span, and deflections. Subsonic aerodynamics data for the various flap

sizes and deflections was estimated using VSPAERO. VASCOMP was used to assess takeoff and landing mission analysis performance. Figure 1 above shows an overview of the process.

# Tool Descriptions

# OpenVSP

The open source Vehicle Sketch Pad (OpenVSP) software [1-4] is a parametric vehicle geometry tool. It allows the user to create 3D parametric models of generic aircraft configurations defined by common engineering parameters. These parametric models can then be processed into formats suitable for various engineering analyses. The predecessors to OpenVSP were developed internally by NASA in the early 1990s. On January 10, 2012, OpenVSP was released as an open source project under the NASA Open Source Agreement (NOSA) version 1.3.

# VSPAERO

VSPAERO was developed by David Kinney, Ph.D. at NASA Ames Research Center and is a fast, linear, vortex lattice solver for assessing the aerodynamics of a given configuration. VSPAERO also allows for the integration of actuator disks to easily include aero-propulsive effects of engines and propellers [5]. VSPAERO efficiently solves for the strengths of the discrete vortices that are applied to each panel in the OpenVSP degenerate geometry file and generates estimates of the net aerodynamic forces and moments. The flow over a section of panels behind a propeller modifies the local freestream to account for increased speed and vorticity induced by the propeller. The actuator disks may be left inactive (empty) if the freestream/glide condition is to be analyzed. VSPAERO also has the ability to calculate the skin friction drag of each component in a model by applying a simple flat-plate drag model to each panel.

# VASCOMP

The Vertical and/or Short Take-Off and Landing (V/STOL) Aircraft Sizing and Performance Computer Program (VASCOMP) is a vehicle synthesis and design/optimization code, originally developed by the Boeing Vertol Corporation [6] that has been modified and enhanced over the years by the Systems Analysis Office of NASA Ames Research Center. The code uses engineering-based analysis methods across all technical disciplines to perform preliminary design and performance estimates of transport aircraft. The focus of the code is on capturing the synergistic interactions of the various disciplines in the overall design and performance of conceptual vehicles.

Description of the vehicle is represented by gross geometric parameters of the design, and not the exact Outer Mode Line (OML) definition of the configuration. For example, the wing is defined by generalized parameters such as aspect ratio, taper ratio, quarter-chord sweep and thickness-to-chord ratio. Similar parameters are used to define horizontal and vertical tail geometry. Fuselage definition consists of overall length, mean diameter, and nose/tail cone fineness ratio.

Early versions of VASCOMP used engineering methods driven by the gross geometric parameters to predict the vehicle aerodynamic characteristics. The version used in this study has been modified to accept tables of lift and drag coefficients as function of Mach number, altitude, angle-of-attack and flap geometry/deflection. For this activity, VSPAERO was used to

generate the low-speed aerodynamic tables used in the mission performance simulations. Zerolift drag coefficients were extracted from an existing 6DOF simulation of the LBFD and used during the climb and cruise portions of the flight.

Using an engine deck for the LBFD, tables of corrected thrust and fuel flow were generated as functions of corrected turbine inlet temperature. Both wet and dry operation of the engine was modeled, with the takeoff performance computed in non-afterburning mode, as defined by the airframe contractor.

VASCOMP simulates full mission profile performance, including takeoff, climb, cruise, descent and landing. The takeoff model consists of flight in a vertical plane, with time integration of the equations of motion for two degrees-of-freedom. For takeoff performance, all-engine takeoff, engine-out takeoff (not applicable for this study effort) and the accelerate-stop distance are computed. Flap deflection for the takeoff maneuver is specified by the user and the incremental lift and drag coefficients added to the clean configuration coefficients. Maximum lift coefficient is then used to compute the takeoff stall speed as a function of the input flap deflection. Decision speed and rotation speed are computed as ratios of the stall speed. Ground effects resulting in reduced induced drag are modelled using an engineering-based method as a function of height-to-span ratio for the low aspect ratio delta wing of the LBFD.

# VIPER Framework

VIPER (Vehicle Integrated co-oPtimization EnviRonment) is a MDAO framework which enables engineers to build complicated system analysis models, for a given vehicle class, to assess the various subsystem interactions with input from discipline experts. VIPER also enables optimization and trade study assessments. A companion and predecessor framework to VIPER is the COBRA (Co-Optimization Bluntbody Re-entry and Ascent) [7] MDAO framework which was developed specifically for space vehicle systems. Experiences from the development and application of COBRA has enable an efficient development of VIPER which focuses on aircraft vehicle systems. The current version of VIPER utilizes a combination of the Phoenix Integration ModelCenter/CenterLink [8,9] and NASA’s OpenMDAO environments [10,11].

图片摘要：该图主要展示 2 VIPER LBFD Model Diagram。
![](images/4076adb71f13c8970028e5973dbb330b1e45a3cbc2a0473ffc4a4dfaeebf7360.jpg)  
Figure-2 VIPER LBFD Model Diagram

Figure 2 above shows an overview diagram of the VIPER model used for this study. OpenVSP (version 3.15.0) was utilized to generate the parametric geometry and the associated analysis mesh. VSPAERO (version 4.4.0) was utilized to assess the aerodynamics. Note that the framework also has other aerodynamic tool options which include Cart3D, Fun3D and Star-CCM+ which are integrated into VIPER using the OpenMDAO analysis server and NAS Access plugin capability. By using OpenMDAO, we are able to extend our computing capability to run some of our tools on NASA’s High-End-Computing (HEC) hardware which can significantly reduce the computing time and make higher fidelity assessment practical in the early stages of design. Finally, VASCOMP is used to perform the mission analysis.

# Results

Using the OpenVSP tool, the parametric geometry of the LBFD-like configuration was developed and the meshes for the various flap deflections were generated. A sample of this is shown in Fig. 3 below.

图片摘要：该图主要展示 2 above shows an overview diagram of the VIPER model used fo。
![](images/df2b13bb2beaa1911aa58db0ac8b2c0c7bc02f607e6d5302a8743b769509f3ad.jpg)  
Figure-3 VSPAERO LBFD Mesh

These meshes were then used in VSPAERO to generate aerodynamic tables for the range of flap chord-to-wing ratios, and selected flap deflections. A combination of 102 VSPAERO simulations were run, including variation in Mach number, angles-of-attack, flap chord size, and flap deflections in order to generate the aerodynamics tables. An example of the solutions obtained from VSPAERO is shown below in Fig. 4.

图片摘要：该图主要展示 3 VSPAERO LBFD Mesh。
![](images/4f1a03e0799319d13ddfd9d9963b16d14226d68bf2fd1c03fcbc976bb2252a4c.jpg)  
Figure-4 VSPAERO sample solution

From these aerodynamic tables, the takeoff performance was computed for the LBFD configuration. Because the LBFD is a single engine design, only the takeoff distance to 35 feet and the accelerate-stop distances were computed. As discussed above, the engine was operated in the non-afterburning (dry) mode. The takeoff gross weight was set at 24,300 lbs, with a wing loading of 49 lbs/ft2 and a break-release thrust-to-weight ratio of slightly below 0.5. Decision speed-to-stall velocity and rotation speed-to-stall velocity ratios were 1.05 and 1.15, respectively. Pitch rate during rotation was assumed to be 2.0 deg/sec. Coefficients of rolling and braking were assumed to be 0.025 and 0.40, respectively. Incremental gear drag of 208 counts was used in the analysis, with the gear retraction initiated above the obstacle height. Maximum allowable normal load factor during the pull-up maneuver was limited to a value of 1.25. Takeoff is performed at sea level for a standard day.

Figure 5 presents the maximum lift coefficient as a function of flap chord and flap deflection. As the flap deflection is increased, the value of CLMAX increases for given flap geometry, and increasing the flap chord results in higher CLMAX values across the flap deflection range. As CLMAX increased, the resulting stall speed is reduced, as shown in Fig. 6. The lowest stall speed is obtained at the maximum value of both the flap chord and flap deflection.

The corresponding takeoff distance to avoid a 35-foot obstacle is presented in Figure 7. As the stall speed is increased, both the decision speed and the rotation speed are reduced. This results in shorter takeoff distances with increased flap chord and flap deflection. Because of the relatively high value of the takeoff thrust-to-weight ratio of the LBFD, the trend of lower takeoff distance with increased flap deflection is maintained, with higher drag associated with increased flap chord and flap deflection overcome by the high engine thrust. For lower values of takeoff

thrust-to-weight ratios, typical of transport type aircraft, higher drag in the takeoff configuration may result in increased takeoff distances, producing a “bucket” in the takeoff distance versus flap deflection curve.

图片摘要：该图主要展示 5 presents the maximum lift coefficient as a function of fla。
![](images/7914daf726c2416f7f1fa911a67664c5a03830fa399018e5ed440a15145649b5.jpg)  
Figure 5. Maximum lift Coefficient versus flap deflection

图片摘要：该图主要展示 5. Maximum lift Coefficient versus flap deflection。
![](images/a80e51b8953d679b9f8dbdcec3095890a24226329ce426d7008c45f78f6ad1ca.jpg)  
Figure 6. Stall speed versus flap chord and flap chord and flap deflection.

图片摘要：该图主要展示 6. Stall speed versus flap chord and flap chord and flap def。
![](images/0cf9aa14287fb4870bb4ede07cb64c604b41456de72e6d79d560d688a6538fc7.jpg)  
Figure 7. Takeoff distance vs. flap chord and flap deflection

图片摘要：该图主要展示 7. Takeoff distance vs. flap chord and flap deflection。
![](images/e5fca59068786ae2c9f4ca41be685f25a0361ffdc2641afa81d906e8e7fd82a6.jpg)  
Figure 8. Accelerate-stop distance vs. flap chord and flap deflection

Finally, the accelerate-stop distance is shown in Fig. 8 as a function of flap chord and flap deflection. Again, increased flap chord and flap deflection result in higher CLMAX, lower stall

speed in the takeoff configuration, and hence shorter accelerate-stop distances. For the range of flap chord-to-wing ratios and flap deflection, the accelerate-stop distance is greater than the all-engine takeoff distance.

# Conclusions

A streamlined MDAO process to provide feedback into the conceptual design and inform airspace modeling of unconventional aircraft has been demonstrated. This was achieved by performing a trade study of various flap sizes on a Low-Boom Flight Demonstrator (LBFD)-like configuration. The results of this study showed a continuous decrease in takeoff distance with increased flap chord and flap deflections. This predicted trend is unlike typical transport aircraft which normally show an increase in takeoff distances due to the higher drag associated with increasing flap deflection producing a “bucket” in the takeoff distance versus flap deflection curve. The LBFD-like vehicle trend of shorter takeoff distance with increased flap deflection, is attributed to the high engine thrust-to-weight ratio which allows it to overcome the higher drag associated with increased flap chord and flap deflections.

# References

1. Hahn, A., “Vehicle Sketch Pad: Parametric Geometry for Conceptual Aircraft Design”, 48th AIAA Aerospace Sciences Meeting, Orlando, FL, Jan 4 - 7 2010, AIAA-2010-657   
2. Fredericks, W., “Aircraft Conceptual Design Using Vehicle Sketch Pad”, 48th AIAA Aerospace Sciences Meeting, Orlando, FL, January 4-7, 2010, AIAA-2010-658   
3. Gloudemans, J. R., McDonald, R., “Improved Geometry Modeling for High Fidelity Parametric Design”, 48th AIAA Aerospace Sciences Meeting and Exhibit, AIAA-2010-659   
4. Gloudemans, J. R., Davis, P. C., and Gelhausen, P. A., “A rapid geometry modeler for conceptual aircraft”, 34th Aerospace Sciences Meeting and Exhibit, AIAA-1996-52, Jan. 15- 18, 1996.   
5. Online user's manual for VSPAERO, http://openvsp.org/wiki/doku.php?id=vspaerotutorial   
6. VASCOMP II user’s manual, the V/stol Aircraft Sizing and performance Computer Program, D8-0375 Volume VI, $3 ^ { \mathrm { r d } }$ revision 1980 http://www.dtic.mil/dtic/tr/fulltext/u2/a088833.pdf   
7. Garcia, J. A., Brown, J. L., Kinney, D. J., Bowles J. V., Huynh L. C., Jiang X. J., Lau, E., and Dupzyk, I. C., “Co-Optimization of Mid Lift to Drag Vehicle Concepts for Mars Atmospheric Entry,” AIAA 2010-5052, 10th AIAA Thermophysics Conference, June 2010.   
8. Phoenix Integration: Software for Engineers: Using ModelCenter and Analysis Server Worldwide - Homepage. http://www.phoenix-int.com/, August 2002.   
9. Improving The Engineering Process with Software Integration- Integrating Engineering Applications for Design. www.phoenix-int.com/publications/, July 2002.   
10. K. T. Moore, B. A. Naylor, and J. S. Gray, “The Development of an Open-Source Framework for Multidisciplinary Analysis and Optimization,” in 10th AIAA/ISSMO Multidisciplinary Analysis and Optimization Conference, Victoria, Canada, 2008.   
11. NASA OpenMDAO publications: http://openmdao.org/publications
