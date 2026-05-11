# Swept-Wing Ice Accretion Characterization and Aerodynamics

Andy P. Broeren and Mark G. Potapczuk

Glenn Research Center, Cleveland, Ohio

James T. Riley

FAA William J. Hughes Technical Center, Atlantic City Airport, New Jersey

Philippe Villedieu

ONERA, The French Aerospace Laboratory, Toulouse, France

Frédéric Moëns

ONERA, The French Aerospace Lab, Meudon, France

Michael B. Bragg

University of Illinois at Urbana-Champaign, Urbana, Illinois

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA Scientific and Technical Information (STI) program plays a key part in helping NASA maintain this important role.

The NASA STI Program operates under the auspices of the Agency Chief Information Officer. It collects, organizes, provides for archiving, and disseminates NASA’s STI. The NASA STI program provides access to the NASA Aeronautics and Space Database and its public interface, the NASA Technical Reports Server, thus providing one of the largest collections of aeronautical and space science STI in the world. Results are published in both non-NASA channels and by NASA in the NASA STI Report Series, which includes the following report types:

TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counterpart of peer-reviewed formal professional papers but has less stringent limitations on manuscript length and extent of graphic presentations.   
TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., quick release reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.   
CONTRACTOR REPORT. Scientific and technical findings by NASA-sponsored contractors and grantees.

CONFERENCE PUBLICATION. Collected papers from scientific and technical conferences, symposia, seminars, or other meetings sponsored or cosponsored by NASA.   
SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
TECHNICAL TRANSLATION. Englishlanguage translations of foreign scientific and technical material pertinent to NASA’s mission.

Specialized services also include creating custom thesauri, building customized databases, organizing and publishing research results.

For more information about the NASA STI program, see the following:

Access the NASA STI program home page at http://www.sti.nasa.gov   
• E-mail your question to help@sti.nasa.gov   
Fax your question to the NASA STI Information Desk at 443–757–5803   
Phone the NASA STI Information Desk at 443–757–5802   
Write to: STI Information Desk NASA Center for AeroSpace Information 7115 Standard Drive Hanover, MD 21076–1320

# Swept-Wing Ice Accretion Characterization and Aerodynamics

Andy P. Broeren and Mark G. Potapczuk

Glenn Research Center, Cleveland, Ohio

James T. Riley

FAA William J. Hughes Technical Center, Atlantic City Airport, New Jersey

Philippe Villedieu

ONERA, The French Aerospace Laboratory, Toulouse, France

Frédéric Moëns

ONERA, The French Aerospace Lab, Meudon, France

Michael B. Bragg

University of Illinois at Urbana-Champaign, Urbana, Illinois

Prepared for the

5th Atmospheric and Space Environments Conference

sponsored by the American Institute of Aeronautics and Astronautics

San Diego, California, June 24–27, 2013

National Aeronautics and

Space Administration

Glenn Research Center

Cleveland, Ohio 44135

# Acknowledgments

The authors gratefully acknowledge the support of their respective organizations in this collaborative research effort. Specific contributions to this paper were provided by the University of Illinois under NASA Cooperative Agreement NNX12AB04A and FAA Cooperative Agreement 10-G-004. The authors thank Jeff Diebold, Gustavo Fujiwara, Brock Wiberg and Brian Woodard at University of Illinois and Cris Bosetti, Abdi Khodadoust, Adam Malone, Ben Paul and John Vassberg at the Boeing Company for their contributions to this paper. Eric Kreeger and Mary Wadel at NASA Glenn Research Center provided additional technical and management review. The NASA-support portion of this research effort is funded under the Atmospheric Environment Safety Technologies Project of the NASA Aviation Safety Program.

Trade names and trademarks are used in this report for identification only. Their usage does not constitute an official endorsement, either expressed or implied, by the National Aeronautics and Space Administration.

Level of Review: This material has been technically reviewed by technical management.

Available from

NASA Center for Aerospace Information

7115 Standard Drive

Hanover, MD 21076–1320

National Technical Information Service

5301 Shawnee Road

Alexandria, VA 22312

# Swept-Wing Ice Accretion Characterization and Aerodynamics

Andy P. Broeren and Mark G. Potapczuk National Aeronautics and Space Administration Glenn Research Center Cleveland, Ohio 44135

James T. Riley FAA William J. Hughes Technical Center Atlantic City Airport, New Jersey 08405

Philippe Villedieu ONERA, The French Aerospace Lab F-31055, Toulouse, France

Frédéric Moëns ONERA, The French Aerospace Lab F-92190, Meudon, France

Michael B. Bragg University of Illinois at Urbana-Champaign Urbana, Illinois 61801

# Abstract

NASA, FAA, ONERA, the University of Illinois and Boeing have embarked on a significant, collaborative research effort to address the technical challenges associated with icing on large-scale, three-dimensional swept wings. The overall goal is to improve the fidelity of experimental and computational simulation methods for swept-wing ice accretion formation and resulting aerodynamic effect. A seven-phase research effort has been designed that incorporates ice-accretion and aerodynamic experiments and computational simulations. As the baseline, full-scale, swept-wing-reference geometry, this research will utilize the 65 percent scale Common Research Model configuration. Ice-accretion testing will be conducted in the NASA Icing Research Tunnel for three hybrid swept-wing models representing the 20, 64 and 83 percent semispan stations of the baseline-reference wing. Threedimensional measurement techniques are being developed and validated to document the experimental ice-accretion geometries. Artificial ice shapes of varying geometric fidelity will be developed for aerodynamic testing over a large Reynolds number range in the ONERA F1 pressurized wind tunnel and in a smaller-scale atmospheric wind tunnel. Concurrent research will be conducted to explore and further develop the use of computational simulation tools for ice accretion and aerodynamics on swept wings. The combined results of this research effort will result in an improved understanding of the ice formation and aerodynamic effects on swept wings. The purpose of this paper is to describe this research effort in more detail and report on the current results and status to date.

# Nomenclature

c chord length   
s surface distance measured from leading edge   
$x$ chordwise coordinate

<table><tr><td>y</td><td>spanwise coordinate (vertical coordinate for airfoils)</td></tr><tr><td>z</td><td>vertical coordinate</td></tr><tr><td>AR</td><td>aspect ratio</td></tr><tr><td>C1</td><td>sectional lift coefficient</td></tr><tr><td>Cd</td><td>sectional drag coefficient</td></tr><tr><td>CP</td><td>pressure coefficient</td></tr><tr><td>M</td><td>Mach Number</td></tr><tr><td>Re</td><td>Reynolds Number</td></tr><tr><td>V</td><td>velocity</td></tr><tr><td>α</td><td>angle of attack</td></tr><tr><td>λ</td><td>taper ratio</td></tr><tr><td>Λ</td><td>sweep angle</td></tr><tr><td>CFD</td><td>Computational Fluid Dynamics</td></tr><tr><td>CRM</td><td>Common Research Model</td></tr><tr><td>CRM65</td><td>Common Research Model geometry at 65 percent scale</td></tr><tr><td>FAA</td><td>Federal Aviation Administration</td></tr><tr><td>IRT</td><td>Icing Research Tunnel</td></tr><tr><td>LWC</td><td>Cloud liquid water content</td></tr><tr><td>MVD</td><td>Median volumetric diameter</td></tr><tr><td>NACA</td><td>National Advisory Committee for Aeronautics</td></tr><tr><td>NASA</td><td>National Aeronautics and Space Administration</td></tr><tr><td>ONERA</td><td>Office National d&#x27;Etudes et de Recherches Aérospatiales</td></tr><tr><td>RPM</td><td>Rapid Prototyping Manufacturing</td></tr><tr><td>WSU</td><td>Wichita State University</td></tr></table>

# 1.0 Introduction

Ice accretion and its aerodynamic effect on highly three-dimensional swept wings are extremely complex phenomena important to the design, certification and safe operation of small and large transport aircraft. There is increasing demand to balance trade-offs in aircraft efficiency, cost and noise that tend to compete directly with allowable performance degradations over an increasing range of icing conditions. Computational fluid dynamics codes have reached a level of maturity that they are being proposed by manufacturers for use in certification of aircraft for flight in icing. However, sufficient high-quality data to evaluate their performance on iced swept wings are not currently available in the public domain. Significant knowledge gaps remain for swept-wing geometries and supercooled, large-droplet icing conditions including freezing drizzle and freezing rain. NASA, in collaboration with FAA, ONERA and University of Illinois, has developed a multi-phase research effort to address some of these knowledge gaps. This paper provides an overview of this research effort and a summary of progress to date.

This research effort is modeled after a previous successful international collaboration that investigated aerodynamic effects and ice accretion simulation for airfoils and straight wings (Refs. 1 to 18) The overall goal of the previous collaboration was to provide high-fidelity, full-scale, iced-airfoil aerodynamic data and validated subscale-model simulation methods that produce the essential full-scale aerodynamic characteristics. The research was organized into six phases involving icing wind tunnel and aerodynamic wind tunnel experiments with both subscale and full-scale models using the NACA 23012 airfoil. An important initial step in this research was the classification of ice accretion according to the aerodynamic effect on the flowfield. This provided a framework within which the ice accretion and aerodynamic testing was conducted. The NASA IRT was used to generate the ice accretion using both

subscale and full-scale models. Aerodynamic testing was performed at the ONERA F1 pressurized wind tunnel using a 72 in. (1.83 m) chord, full-span, unswept, NACA 23012 airfoil model with high-fidelity, three-dimensional castings of the IRT ice accretions. Performance data were recorded over a large range of Reynolds number, up to $1 5 . 9 \times 1 0 ^ { 6 }$ and Mach numbers from 0.10 to 0.28. This generated a large, highquality, benchmark, iced-airfoil aerodynamic database. Lower-fidelity simulation methods were developed and tested on an 18 in. $( 0 . 4 6 \mathrm { m } )$ chord NACA 23012 airfoil model at the University of Illinois wind tunnel at lower Reynolds number. The aerodynamic accuracy of the lower-fidelity, subscale ice simulations was validated against the full-scale results for a factor of 4 reduction in model scale and a factor of 8 reduction in Reynolds number. Methods were developed for designing lower-fidelity artificial ice shapes for subscale models. The completed research defined the level of geometric fidelity required for artificial ice shapes to yield aerodynamic performance results to within a known level of uncertainty. This previous work has led to a more complete understanding of ice contamination aerodynamic effects on airfoils. This is an important building block, but a fundamental question remains as to how relevant these 2-D data are to 3-D swept-wing geometries.

Swept-wing icing has been a significant research area of interest for many years. This work has mostly focused on icing physics studies aiding in the development of computational simulation tools (Refs. 19 to 30). Icing physics studies have been conducted to understand the physics of formation of ice accretions on swept wings and to develop models that allow their prediction. The development of computational simulation tools centers on the continuous improvement of codes such as LEWICE3D which predict particle trajectories and ice accretions for 3-D configurations. While this work is critical to understanding the relevant physical factors, it has mostly been conducted on small-scale geometries, often using NACA 0012 airfoil sections or circular cylinders. In order to continue the advancement of 3-D icing simulation tools, new validation data are needed for large-scale, modern, swept-wing configurations. Relevant 3-D ice accretion geometries must be documented in order to continue the validation efforts for the current array of icing simulation tools.

There exist in the public domain a small number of aerodynamic studies for iced-swept wings. A fundamental study of the flowfield on a subscale rectangular swept wing using a NACA 0012 airfoil section was conducted with a simulated, glaze-ice accretion (Refs. 31 to 34) The 3-D velocity measurements on the iced wing were complemented with CFD simulations to develop a good understanding of the ice-shape effect on the flowfield. In 2001, a research program involving FAA, NASA and WSU was conducted to develop an experimental database of ice accretion effects on aerodynamic performance of a finite swept wing (Refs. 35 to 37). An icing test was conducted in the NASA IRT on a subscale wing having $2 8 ^ { \circ }$ sweep and GLC-305 airfoil section. High-fidelity ice casting simulations were generated for aerodynamic testing in the WSU 7- by 10-ft wind tunnel at a Reynolds number of $1 . 8 \times 1 0 ^ { \overline { { 6 } } }$ . While this study utilized high-fidelity artificial ice shapes, the small model scale and low-Reynolds number limit the applicability of the results to a full-scale airplane. Reehorst et al. (Refs. 38 and 39). also conducted a low-Reynolds number aerodynamic study of icing effects on a realistic, fully three-dimensional, 12.5 percent scale model of a twin-engine, short-haul commercial transport. The authors considered various roughness size scaling approaches for the small-scale and low-Reynolds number investigation. Despite the low-Reynolds number at which the data were acquired, this effort resulted in a large database of icing effects on a full-aircraft configuration. Aerodynamic testing of a fullscale, swept-wing, business jet, T-tail model was performed under the auspices of the NASA/FAA Tailplane Icing Program, Phase II (Ref. 40 and 41). While the T-tail model results are, in general, certainly applicable to the swept-wing icing aerodynamics research described here, no 3-D ice-shape configurations were tested.

The very brief literature review contained herein has cited a number of significant research efforts in swept-wing ice accretion characterization and aerodynamics. There are a number of low-Reynolds number aerodynamic databases for relatively simple geometries. The ice-accretion research conducted has also led to a good fundamental understanding of the important physical processes, but mostly at small scale. There is very little ice accretion geometry information for large-scale, modern design, swept wings in the public domain known to the authors. For example, the mean aerodynamic chord length can range

from approximately 10 ft (3 m) for regional jets to 30 ft (9.1 m) for wide-body airplanes. Similarly, the authors are also unaware of any high-Reynolds number aerodynamic performance and flowfield data illuminating the effect of ice on swept-wing aerodynamics that is available in the public domain.

Three-dimensional computational and experimental icing simulation tools are becoming increasingly common in icing analysis for modern transport airplanes. Manufacturers are proposing the use of CFD codes for certification of aircraft for flight in icing conditions. However, validation data are very limited, particularly for large-scale swept wings that are typical of modern commercial airplanes. Thus it is difficult to determine how much confidence can be placed in results from CFD codes used in design, and particularly in certification. Furthermore, an understanding of the icing effects on swept-wing aerodynamics is critical to evaluating the accuracy to which ice accretion must be predicted by computational tools or simulated in aerodynamic testing. For example, it is known for some cases that swept-wing ice accretion can be highly three dimensional (e.g., “scallops” or “lobster tails”), which is discussed below in Section 2.1. An important question is how much detail of that three-dimensionality is critical to the aerodynamic performance and therefore must be accurately simulated. In addition, basic swept-wing aerodynamic effects such as the spanwise flow and configuration dependence play an important role. An understanding of scale effects, including Reynolds and Mach number, is needed in order to develop lower cost aerodynamic test techniques for iced swept wings. Valid tests conducted at smaller scale and lower Reynolds number hold potential for developing a more complete understanding of the aerodynamics. Both full-scale and subscale research is needed to develop and validate computational fluid dynamics (CFD) simulation tools used to predict the aerodynamics of iced-wing configurations. All of these factors have provided motivation for collaborative research effort in this arena.

NASA, FAA, ONERA, the University of Illinois and Boeing, have embarked on a significant, collaborative research effort to address the technical challenges associated with swept-wing icing. The overall goal of ensuring continued flight safety will be achieved by improving the fidelity of experimental and computational simulation methods for swept-wing ice accretion formation and resulting aerodynamic effect. There are three specific objectives:

Generate a database of 3-D, swept-wing, ice-accretion geometries for icing-code development and validation and for aerodynamic testing.   
Develop a systematic understanding of the aerodynamic effect of icing on swept wings including: Reynolds and Mach number effects, important flowfield physics and fundamental differences from 2-D.   
Determine the level of ice-shape geometric fidelity required for accurate aerodynamic simulation of swept-wing icing effects.

A seven-phase research effort has been designed that incorporates ice-accretion and aerodynamic experiments and computational simulation to address these objectives. This is depicted schematically in Figure 1. Phase I is a review of the technical literature associated with iced swept-wing aerodynamics with emphasis on classifying ice accretion based upon key aerodynamic features of the flowfield. This research provides an organizational framework for the icing and aerodynamic experiments conducted in later phases. The research conducted in Phase II will identify the baseline swept-wing model to be used for the experiments and computational analysis. In addition, measurement techniques will be developed to document, in 3-D, the experimental ice-accretion geometries. Aerodynamic measurement techniques suitable to iced swept-wing experiments will also be investigated. The icing tests conducted in Phase III will generate a large database of ice-accretion geometries on realistic large-scale swept wings. Artificial ice shapes of varying geometric fidelity will be developed for aerodynamic testing over a large Reynolds number range in Phases IV and V. Exploring the effects of geometric fidelity and Reynolds number will require final validation tests in Phase VI. The research conducted in Phase VII will explore and further develop the use of computational simulation tools for ice accretion and aerodynamics on swept wings.

图片摘要：该图主要展示 1.—Seven phase research effort designed to investigate large。
![](images/a09583a0940f28812bcaeef6c6bf6c85af4e0e7c87901d586dd6705275480edd.jpg)  
Figure 1.—Seven-phase research effort designed to investigate large-scale swept wing ice accretion and aerodynamics.

Each phase has a number of technical challenges that must be overcome in order for the research objectives to be achieved. The purpose of this paper is to describe these technical challenges in more detail and report on the current results and status to date.

# 2.0 Initial Research Results and Plans

# 2.1 Phase I: 3-D Ice Accretion Classification

Ice accretion is often described in terms of its appearance or composition, such as glaze, rime, clear, mixed, runback, beak, and intercycle among others. While this terminology may be useful for characterizing the visual attributes of ice accretion, it may not be as useful when the objective is to understand the aerodynamic effects. Bragg et al. (Refs. 3 and 4) examined the icing aerodynamics literature and developed four fundamental types or categories based upon the flowfield physics that was unique to each category. This research was directed at the essentially 2-D aspects of iced airfoils. Categorizing ice accretion in this way provided an aerodynamic framework for the research designed to quantify the effects of geometric fidelity on iced-airfoil aerodynamics. This proved to be a successful approach and was identified as an important part of the swept-wing icing research effort.

Ice accretion formations on swept wings can have unique characteristics. Depending upon specific icing conditions and sweep angle, the region of the attachment line on the ice accretion may not be smooth as is often the case for straight wings. This is depicted in Figure 2 that shows an example of initial roughness and a large rime-ice accretion on a swept wing. For glaze icing, certain combinations of icing conditions and sweep angle can lead to the formation of highly 3-D features called “scallops” or “lobster tails” that do not exist for ice accretions on airfoils. An example of this type of swept-wing ice accretion is shown in Figure 3. It is also possible to have glaze ice accretion with no scallops or incomplete scallop formations on swept wings (Ref. 19).

图片摘要：该图主要展示 2.—Photographs of initial roughness (left) and rime ice (rig。
![](images/3f285b1c8cddcf2855980d9ef18099db6496009c0507d75a340b8a283a554e58.jpg)

图片摘要：该图主要展示 2.—Photographs of initial roughness (left) and rime ice (rig。
![](images/8bb1b080ccf285bbc49b3eb8d2c2aedeee161db0402eb35c9f62054964e489bd.jpg)  
Figure 2.—Photographs of initial roughness (left) and rime ice (right) accreted on a NACA 0012 wing having $4 5 ^ { \circ }$ leading-edge sweep in the NASA Glenn Icing Research Tunnel. Aerodynamic and icing conditions were $\mathsf { V } = 2 0 0 \mathsf { k n }$ , $\mathtt { a } = 0 ^ { \circ }$ , $\mathsf { L W C } = 0 . 4 5 \ : \mathsf { g } / \mathsf { m } ^ { 3 }$ , ${ \mathsf { M V D } } = 3 2 { \mu \mathrm { m } }$ , total temperature $= 2 0 ^ { \circ } \mathsf { F }$ (left) and $1 ^ { \circ } \mathsf { F }$ (right), exposure time $^ { \circ 2 }$ min (left) and 20 min (right); adapted from Broeren et al. (Ref. 42).

图片摘要：该图主要展示 2.—Photographs of initial roughness (left) and rime ice (rig。
![](images/d49d491d5fb30224bd65d690e8434f912ab9cec86a809156494690e54e1908ee.jpg)

图片摘要：该图主要展示 2.—Photographs of initial roughness (left) and rime ice (rig。
![](images/3821e289db10bba92fc814132ab9c5b64353948882d1fe8b475abd86fa54d2de.jpg)

图片摘要：该图主要展示 2.—Photographs of initial roughness (left) and rime ice (rig。
![](images/b71fca556d70e743d040b12d8400cc205726724cec65ff4ee82ca5dd906c511d.jpg)  
Figure 3.—Photographs of complete scallop glaze ice accreted on a NACA 0012 wing having $4 5 ^ { \circ }$ leading-edge sweep in the NASA Glenn Icing Research Tunnel. Aerodynamic and icing conditions were $\mathsf { V } = 2 0 0 \mathsf { k n }$ , $\mathtt { a } = 0 ^ { \circ }$ , $\mathsf { L W C } = 0 . 4 5 \ : \mathrm { \check { g } } / \mathsf { m } ^ { 3 }$ , ${ \mathsf { M V D } } = 3 2 { \mu \mathrm { m } }$ , total temperature $=$ $20 \%$ , exposure time $= 2 0$ min; after Broeren et al. (Ref. 42).

Broeren et al. (Ref. 42) have prepared an extensive review of the existing data on swept-wing ice accretion and aerodynamics. The existing data tend to be: (1) mostly at low-Reynolds number and (2) applicable to simple swept-wing geometries that do not have high-lift systems, wing-mounted engines, fuselages and other features of actual airplane wings. These factors can significantly alter the iced aerodynamics for particular configurations and so extreme caution must be exercised in terms of making general conclusions based upon the current, limited database. Given what is known from the existing data, the same four classifications, or fundamental categories used for iced airfoils were suggested: (1) roughness, (2) horn ice, (3) streamwise ice and (4) spanwise-ridge ice. Instead of relying upon iceaccretion terminology such as rime and glaze, the four aerodynamic groups have names associated with ice-shape geometry. Broeren et al. (Ref. 42) describe the unique flowfield features of each group that determine the iced-swept-wing aerodynamics.

Ice roughness represents initial leading-edge ice accretion and a key aerodynamic characteristic is that the scale of the boundary-layer separation is of the same order as the size of the roughness. How this small, separated flow region interacts with the spanwise flow is unknown.   
Horn ice is large, leading-edge ice accretion that can be associated with glaze icing conditions. The flowfield is characterized by large-scale, boundary-layer separation originating at the horn. This separation leads to the formation of a spanwise-running, leading-edge vortex that is similar to that found on clean swept wings with leading-edge separations. The small amount of existing data indicate that there are fundamental flowfield differences between nominally 3-D horn ice characterized by no scallop formations versus highly 3-D horn ice characterized by fully developed scallop formations. Diebold et al. (Ref. 43) provide a more detailed description of this complex flowfield.   
• Streamwise ice can be associated with rime icing conditions and is generally conformal to the wing leading edge, or may form a horn-like feature (or protuberance) oriented into the flow direction. The only example of this group cited by Broeren et al. (Ref. 42) showed an increase in wing maximum lift coefficient with the streamwise ice. While this effect is thus known to be possible, it is not expected to hold for most cases and illustrates the need for further wing performance data and flowfield information with realistic streamwise ice simulations.   
• Spanwise-ridge ice can be associated with droplet impingement and ice formation aft of the area covered by an ice-protection system in supercooled, large-droplet icing conditions or with incomplete evaporation of impinging water. The leading edge is free of ice with an ice ridge located downstream often in the range of 10 to 15 percent chord. Broeren et al. (Ref. 42) describe data from only one low-Reynolds number study for very simple geometric representations of spanwise-ridge ice on a swept wing.

The lack of data noted for streamwise and spanwise-ridge ice was also true to a lesser degree for roughness and horn ice. The result was an inability to fully develop the classification system. Therefore, Broeren et al. (Ref. 42) make a number of specific recommendations where more data are needed and thus provide additional guidance for this research effort. It is likely that the classification system will be revisited as more data become available. In this sense, the Phase I research is an ongoing effort throughout the course of the project.

# 2.2 Phase II: Ice Accretion and Aerodynamic Measurement Methods Development

The research conducted in Phase II provides the necessary foundation for the experimental and computational work to be conducted in the latter phases. The Phase II research is organized into three areas:

1. Defining the baseline, full-scale, swept-wing model geometry to be used for the research effort;   
2. Developing and validating methods to measure highly 3-D ice accretion;

3. Developing the appropriate measurement methods to quantify the iced-swept wing aerodynamics.

Significant progress has been achieved in each of these areas and is briefly described here.

# 2.2.1 Baseline Model Selection

For this research to be useful and relevant, it is important to select a baseline, swept-wing model geometry that is representative of current, modern design civilian transport airplanes. The selection process was complex given the large number of variables, such as sweep angle, aspect ratio, mean aerodynamic chord and wing span. An additional requirement was for all of the geometry to be nonproprietary and non-export controlled. After reviewing the available options, the Common Research Model geometry was selected (Ref. 44). The Boeing Company provided the design of the CRM for a previous joint experimental effort with NASA which fabricated test articles and conducted aerodynamic testing (Refs. 45 and 46). The CRM geometry was also used as part of the AIAA Drag Prediction Workshops (Ref. 47). The model, shown in Figure 4 with and without the engine nacelle/pylon, includes a fuselage that is representative of a wide-body commercial transport airplane. The $3 5 ^ { \circ }$ swept wing has a contemporary transonic supercritical design that is well behaved with and without the nacelle/pylon structure. Table I provides a comparison of the CRM wing geometry with existing wide-body airplanes. A key advantage to the CRM is that all of the geometry information, CFD analysis and experimental data are available in the public domain. This fact, coupled with its modern design, make the CRM an ideal baseline reference model for this research.

The fact that the CRM is representative of a wide-body transport airplane means that the physical size is very large compared to that of many other swept-wing airplanes such as single-aisle commercial transports including regional and business jets. The large physical size of the CRM wing presents specific challenges to both the ice-accretion and aerodynamic testing. Large-scale wing ice-accretion testing requires the design of “hybrid” or “truncated” models where the full-scale leading-edge geometry is matched to a shortened or truncated afterbody. This design process is the subject of Phase III of the

图片摘要：该图主要展示 4.—Conceptual design of the Common Research Model with and w。
![](images/c881ab8ceba04e244aa365bee09753c69165753d45e06924b545e1f8fb15b270.jpg)  
Figure 4.—Conceptual design of the Common Research Model with and without engine nacelle/pylon, after Vassberg et al. (Ref. 44).

TABLE I.—COMPARISON OF CRM WING GEOMETRY WITH EXISTING WIDE-BODY AIRPLANES(a)   

<table><tr><td>Airplane</td><td>Span, ft</td><td>Mean aerodynamic chord, ft</td><td>Area, ft2</td><td>Aspect ratio(b)</td><td>Taper ratio(b)</td><td>Sweep angle, c/4</td></tr><tr><td>CRM</td><td>192.8</td><td>23.0</td><td>4,130</td><td>9.0</td><td>0.28</td><td>35°</td></tr><tr><td>Airbus A330-200/300</td><td>198.0</td><td>23.9</td><td>3,892</td><td>9.5</td><td>0.22</td><td>30°</td></tr><tr><td>Boeing 777-200</td><td>199.9</td><td>26.5</td><td>4,389</td><td>8.7</td><td>0.27</td><td>31°</td></tr><tr><td>Boeing 787-9</td><td>197.0</td><td>20.6</td><td>3,880</td><td>9.6</td><td>0.18</td><td>32°</td></tr><tr><td>Boeing 747-400</td><td>211.4</td><td>29.8</td><td>5,417</td><td>7.7</td><td>0.28</td><td>37°</td></tr></table>

(a) Data for existing wide-body airplanes was compiled from publically available sources that may use different conventions to define the geometric parameters.

research effort described in Section 2.3. The large physical size of the CRM wing requires a very aggressive design for the hybrid model that presents greater risk of adverse effects when installed in the NASA IRT. For aerodynamic wind-tunnel testing, the full-scale CRM wing can be scaled to an appropriate size for the facility. In the case of the ONERA F1 wind-tunnel, an 8 percent scale model of the CRM would be of appropriate size. While this is not unreasonable for the clean, baseline model geometry, such a large scale reduction becomes challenging when the goal is to accurately simulate iceaccretion geometry that typically includes small roughness. Typical ice-roughness sizes on the full-scale model ice accretion could be in the range of 0.04 to 0.08 in. (1 to $2 \mathrm { m m }$ ) which is equivalent to 0.003 to 0.006 in. (0.08 to $0 . 1 6 \mathrm { m m }$ ) on the 8 percent scale aerodynamic model. Small roughness features of this size are very challenging to accurately reproduce on the artificial ice shapes developed for aerodynamic testing. Based upon these factors, the research team decided to use a 65 percent scale version of the CRM as the full-scale, baseline, reference geometry for this research. Table II provides a comparison of the CRM65 geometry with that of existing single-aisle commercial transport airplanes. The geometries are similar in scale with only the CRM65 sweep angle being considerably larger. More detailed geometry information for the CRM65 wing semispan is shown in Figure 5. Using the CRM65 as the full-scale, baseline, reference geometry for this research reduces potential risks associated with the ice-accretion and aerodynamic testing while still being representative of current transport airplanes.

TABLE II.—COMPARISON OF CRM65 WING GEOMETRY WITH EXISTING SINGLE-AISLE AIRPLANES(a)   

<table><tr><td>Airplane</td><td>Span, ft</td><td>Mean aerodynamic chord, ft</td><td>Area, ft2</td><td>Aspect ratio(b)</td><td>Taper ratio(b)</td><td>Sweep angle, c/4</td></tr><tr><td>CRM65</td><td>125.3</td><td>15.0</td><td>1,745</td><td>9.0</td><td>0.28</td><td>35°</td></tr><tr><td>Airbus A320</td><td>112.0</td><td>14.1</td><td>1,320</td><td>9.5</td><td>0.21</td><td>25°</td></tr><tr><td>Boeing 737-800</td><td>112.6</td><td>13.0</td><td>1,341</td><td>9.5</td><td>0.16</td><td>25°</td></tr><tr><td>Boeing 757-200</td><td>124.8</td><td>16.7</td><td>1,847</td><td>7.8</td><td>0.21</td><td>25°</td></tr></table>

(a) Data for existing single-aisle airplanes was compiled from publically available sources that may use different conventions to define the geometric parameters.

# CRM 65 Wing Geometry

Semispan $= 6 2 . 7$ ft   
• Root chord (symmetry plane) $= 2 9 . 0$ ft   
Root chord (fuselage side of body) $= 2 5 . 4$ ft   
• Tip chord $= 5 . 8$ ft   
• Mean aerodynamic chord $= 1 5 . 0$ ft   
Semispan area $= 8 7 3$ ft2   
• Aspect Ratio $= 9 . 0$   
• Taper Ratio $= 0 . 2 8$   
• Sweep angle $( c / 4 ) = 3 5 ^ { \circ }$

Yehudi break, $3 7 \%$ semispan

Fuselage side of body, $10 \%$ semispan

Symmetry plane

Figure 5.—Summary of CRM65 wing geometric characteristics, adapted from Vassberg et al. (Ref. 44)

# 2.2.2 3-D Ice Accretion Measurement

Generating a database of 3-D experimental ice-accretion geometries and associated artificial ice shapes for subsequent aerodynamic testing requires a robust measurement system. Standard ice-accretion documentation methods are generally 2-D, such as cross-sectional tracings and qualitative, such as photographs. While these methods have been used for many years, they have significant shortcomings when used for the potentially highly 3-D ice accretions that can occur on swept wings (cf. Figure 2 and Figure 3). For example, Bosetti et al. (Ref. 48) show a comparison of three dissimilar tracings of the same ice shape along the span of a swept wing. The best current technology for capturing 3-D features of ice accretion is the mold and casting method. This has been used for many years using various materials and was improved at NASA Glenn during the 1980s using more robust materials to improve accuracy and durability (Ref. 49). A significant disadvantage to this method is that there is no digitized record of the ice accretion. Therefore, the present objective is to develop a method to accurately and efficiently digitize ice accretion in 3-D. Furthermore, the data must be processed and archived so that: (1) comparisons to iceaccretion code results can be performed; (2) artificial ice shapes can be readily fabricated for aerodynamic testing; and (3) the geometry may be readily adapted for CFD simulations.

NASA is leading the effort to adapt commercial laser-based scanning methods that can quantify the full three-dimensional features of ice accretion in the IRT. Lee et al. (Ref. 50) describe the significant progress that has already been made in accomplishing this task. Demonstration tests of several different scanning systems and software were conducted in the IRT and evaluated against a set of pre-defined criteria. It was found that the scanning technology and capability was similar over the range of systems evaluated. An articulated-arm based system was selected because it required minimal modifications to the existing IRT test-section resulting in fewer risks during use.

Several different software packages were considered for post-processing of the data. The processing steps included combining individual scans, developing a surface mesh and filling holes or gaps in the scan data. The most critical software function for working with ice scan data is the ability to create closed, watertight surfaces of the highly irregular, rough features of ice accretion. Through a series of hardware demonstrations, it was determined that the Geomagic software package has the capability to process irregular “organic” surfaces like those typical of ice accretion. The software is also able to create data files that can be used for various rapid prototyping manufacturing methods. Such methods can be used to fabricate artificial ice shapes from the scan data. The software also has exact surfacing capability that can be used to develop grids for computational analysis. Having selected and purchased the scanner and software system, the next step was conducting validation research to define the capability.

The scanner system validation research was divided into two parts: one for straight wing ice shapes and another part dedicated to swept-wing ice shapes. Both of these activities are currently underway. In the former case, an aerodynamic validation will be conducted. Ice-accretion testing has been completed using an 18-in. chord NACA 23012-airfoil, straight-wing model in the IRT. Several different ice accretions were generated ranging from small roughness to large, glaze-horn shapes. The ice accretion was measured with the scanning system and then a mold was made of that ice accretion. Subsequently, artificial ice shapes were fabricated using the casting method from the molds and from RPM methods based upon the 3-D scan data. These artificial ice shapes will be mounted to the leading edge of a NACA 23012 airfoil model for aerodynamic testing at the University of Illinois Low-Speed, Low-Turbulence wind tunnel. The result will be an aerodynamic effect comparison between artificial ice shapes produced from molds and castings vs. shapes produced from 3-D scans and RPM methods. Figure 6 shows a comparison of pencil tracing of the ice castings to cross-sections extracted from the scan data. A common feature in the comparison is that the pencil tracings tend to be much smoother than the scan data. This was expected since the pencil tracing does not have high enough resolution to capture small geometry variations in the ice accretion. More significant differences such as that observed for the ED1978 case on the upper surface near $x / c = 0 . 0$ can usually be attributed to spanwise variation in the ice accretion geometry combined with small differences in the spanwise location of a pencil tracing vs. the scan-data cross section. Overall, there is excellent agreement in Figure 6 between the digitized pencil tracings and the cross-sections extracted from the scan data.

图片摘要：该图主要展示 6.—Comparison of ice accretion cross sections taken from dig。
![](images/23d4f9449a1e7f7b3a3b5975ed96dcc7df5d44f03bd1c6fa4d2b0a54d85f2122.jpg)

图片摘要：该图主要展示 6.—Comparison of ice accretion cross sections taken from dig。
![](images/98b6f5d9bd53b3d79704f90ce169259916e7959c6aad783f1dd4b38c478c3f5a.jpg)

图片摘要：该图主要展示 6.—Comparison of ice accretion cross sections taken from dig。
![](images/576775a41d5a6da83754e0b447ab1d277d6799cdbf45e482e6140f1eca204ec7.jpg)

图片摘要：该图片与Figure 6.—Comparison of ice accretion cross sections taken from digitized pencil这部分内容相关。
![](images/6a0f4c3438e0751dc097d9dca92ec96fb9a85173874ee2d1c6c92293038e85e2.jpg)  
Figure 6.—Comparison of ice accretion cross-sections taken from digitized pencil tracings and 3-D digital scan data for four IRT runs (ED1966, ED1967, ED1977 and ED1978) on an 18-in. chord NACA 23012 straigt wing model.

The validation plan for swept-wing ice shapes includes a geometric comparison between the 3-D laser scan data and 3-D obtained from other methods such as commercial computed tomography (CT) scanning. A significant challenge associated with swept-wing ice accretion is obtaining scan data within the highly 3-D features such as “scallops” or “lobster tails.” The arm-based, laser-scanning system uses a “line-of-sight” method that cannot acquire data within small surface gaps. In this case, more manual intervention during post-processing is required in order to create closed or watertight surfaces. As shown in Figure 7, reasonable qualitative results can be obtained. Non-line-of-sight based scanning methods will be investigated to evaluate the accuracy of the laser-based system for highly 3-D ice geometries. The results of this work will be presented in future reports and papers.

图片摘要：该图主要展示 6.—Comparison of ice accretion cross sections taken from dig。
![](images/79fdd3a851c47ec6543786fd44eb3be850448f70f64a5f55ec26320f1cb589ac.jpg)

图片摘要：该图主要展示 6.—Comparison of ice accretion cross sections taken from dig。
![](images/59ae320b746c7fad48abe1bcf05e1f50fc78be3ec2635b875be7a553ce720f12.jpg)  
Figure 7.—Comparison of 3-D scan data (left) with photograph (right) of an IRT ice accretion, after Lee et al. (Ref. 50).

# 2.2.3 Aerodynamic Measurement Methods

An aerodynamic framework for classifying swept-wing ice accretion based upon unique flowfield features was described in Section 2.1. Identifying these flowfield features and their contribution to the resulting aerodynamic performance degradation is key to satisfying the objectives of this research effort as described in the Introduction (Section 1.0). In addition to analyzing standard performance data such as lift, drag and pitching moment, it is important to understand the characteristics of the flowfield that drive the changes in performance. Flowfield information is also required for the continued development and validation of computational simulation tools. The development of flowfield measurement methods contributes to the planned high- and low-Reynolds number testing of the scaled CRM swept wing with artificial ice shapes.

This methods development effort has been carried out at small scale and very low-Reynolds numbers at the University of Illinois. Diebold et al. (Refs. 51 to 53) describe the application of pressure sensitive paint and wake survey techniques to iced swept wings. These experiments were conducted on an approximately 2 percent-scale, modified CRM wing model with an artificial leading-edge ice shape. Figure 8 shows a comparison of pressure-sensitive paint results with surface-oil flow visualization on the iced wing upper surface. The iced wing is stalled at this angle of attack. The flow visualization indicates that there was a spanwise-running, leading-edge vortex on the inboard portion of the wing. The reattachment line (also shown in Figure 9) is evident in the sharp streamwise pressure gradient between the low- and high pressure regions (centered near $C _ { p } \approx - 1 . 2 )$ measured using pressure-sensitive paint. The surface-pressure data have the ability to quantify the three-dimensional flow separation features observed in the oil-flow patterns. These results are especially encouraging given the known challenges associated with pressure-sensitive paint measurements at low-dynamic pressure.

The wake flowfield surveys were conducted using a 5-hole pressure probe to yield total and static pressure in addition to all three velocity components. Shown in Figure 9 is again the surface-oil flow visualization image from Figure 8 along with the velocity measured in the wake. In this figure, the regions of significant flow separation on the iced wing are correlated to regions of higher streamwise momentum deficit in the wake. For example, consider the stalled region on the wing nominally located at $0 . 6 < 2 y / b < 0 . 8$ which the wake survey data have quantified. It is expected that the contribution to the iced wing profile drag measured in this region would be significant.

图片摘要：该图主要展示 8.—Comparison of surface oil flow visualization (left) with 。
![](images/82cc560bb18c75f26736f2b7126d2c06dc03d64f3af0d137c4ca538ee7bb710d.jpg)

图片摘要：该图主要展示 8.—Comparison of surface oil flow visualization (left) with 。
![](images/545a08a925ee8bdcfa354252d774d24596aea619587fdd111841c621e10c89ad.jpg)  
Figure 8.—Comparison of surface oil flow visualization (left) with pressure-sensitive paint (right) results for scale swept wing with artificial ice shape at $\mathtt { q } = 6 . 5 ^ { \circ }$ , $\mathsf { R e } = 0 . 6 \times 1 0 ^ { 6 }$ and $M = 0 . 1 5$ , after Diebold et al. (Ref. 51).

图片摘要：该图主要展示 8.—Comparison of surface oil flow visualization (left) with 。
![](images/607c7762c23e05cc24b374ce505d298f47168d9f8806941fb57ef28c42112079.jpg)  
Figure 9.—Comparison of surface oil flow visualization (top image) with 3-D wake surface data; contours of streamwise velocity with vectors of transverse velocity for scale swept wing with artificial ice shape at $\mathtt { q } = 6 . 5 ^ { \circ }$ , $\mathsf { R e } = 0 . 6 \times \mathsf { i } 0 ^ { 6 }$ and $M = 0 . 1 5$ , after Diebold et al. (Ref. 51).

In fact Diebold et al. (Ref. 52 and 53) have demonstrated this to be the case through careful integration of the wake survey data. As shown in Figure 10, the integration yields the spanwise distributions of lift and both profile and induced drag for the stalled flowfield of the clean and iced wing. Comparison of the absolute values for the clean and iced configurations is complicated by the significant difference in angle of attack. The results for the iced configuration, however, can be directly compared to the results in Figure 8 and Figure 9. The spanwise distribution of lift shows a significant decrease in the region nominally located at $0 . 6 < 2 y / b < 0 . 8$ identified in Figure 9 as stalled. As indicated, this corresponds to a significant increase in the profile drag. Data similar to that shown in Figure 8 to Figure 10, acquired for realistic ice shapes at reasonable Reynolds number, have the potential to provide the flowfield information necessary to understand changes in swept-wing performance due to the artificial ice shapes as well as the effects of ice-shape geometric fidelity.

图片摘要：该图主要展示 9.—Comparison of surface oil flow visualization (top image) 。
![](images/77d542e34162196aada8a5ce267301b73109800c390fad17ae9be27c3c9480ac.jpg)

图片摘要：该图主要展示 9.—Comparison of surface oil flow visualization (top image) 。
![](images/52631bcf5b3e961bb183629dc07cb1c493a91fcae64cdf777ca72142c286e4fa.jpg)

图片摘要：该图主要展示 9.—Comparison of surface oil flow visualization (top image) 。
![](images/ad0421117faa9bf47426b8950a01593c13dadf7cb5c285f0793460695cf8a986.jpg)  
c) Profile Drag

图片摘要：该图片与d) Induced Drag；Figure 10.—Comparison of spanwise distributions of lift and drag这部分内容相关。
![](images/c32ee73c8b6894d5ceddfa5fd71636e18d21880edfa0479a7314646f9fa9cc65.jpg)  
d) Induced Drag   
Figure 10.—Comparison of spanwise distributions of lift and drag as measured on the scale swept wing at $\bar { \mathsf { a } } = 6 . 5 ^ { \circ }$ , $\mathsf { R e } = \dot { 0 } . 6 \times 1 0 ^ { 6 }$ and $M = 0 . 1 5$ , after Diebold (Ref. 52).

These methods have been investigated by many researchers and are well established. What is unique in this case is the potential challenges presented by the complexities of an iced swept-wing flowfield. For airfoils, it was found that the addition of artificial ice geometries often resulted in large-scale unsteady, three-dimensional and separated flow. These situations can challenge the implementation of and interpretation of results from the selected measurement methods. The research conducted in Phase II will work to address these concerns while building a foundation of experience in processing and analyzing these data.

# 2.3 Phase III: Ice-Accretion Testing

Ice-accretion testing will be conducted during Phase III generating an ice-accretion geometry database to be used for icing code validation and aerodynamic experiments. The design of ice-accretion experiments for the IRT is complicated by the typical large scale of swept wings on transport airplanes such as the CRM. As previously described in Section 2.2.1, the large chord length of the CRM65 wing requires a hybrid design approach in order to generate representative, full-scale ice accretion in the 6- by 9-ft IRT test section. A hybrid swept-wing model preserves the full-scale leading-edge geometry in order to obtain ice accretions representative of the full-scale airplane, but requires a custom-designed aft section to maintain the droplet impingement and leading-edge flow characteristics and resulting ice shape. Since the span of CRM65 wing is much larger than the IRT test section, certain spanwise sections of the wing must be selected for the hybrid model design and subsequent ice accretion testing. The University of Illinois-Boeing team is leading the research effort to address these technical challenges to help ensure the successful completion of the ice-accretion testing. This work is being conducted under four main tasks:

1. Selection of airplane mission and corresponding flight and icing conditions;   
2. Simulation of the full-scale icing conditions;   
3. Design and simulation of hybrid model wing sections in 2-D;   
4. Design and simulation of hybrid model wing sections in 3-D.

As described in Section 2.2.1, the full-scale flight baseline airplane selected for this work is the CRM65. The approach in the first two tasks is to generate flowfield and ice-shape information in realistic flight and icing conditions. These results, such as the location of the attachment line along the wing, collection efficiency and ice-shape profiles then become the reference standard for the 2-D and 3-D hybrid model design studies carried out in the latter two tasks. Significant progress has been achieved in these areas and is briefly described here. The development of these hybrid model design methods is also a significant outcome of this phase of the research effort.

# 2.3.1 Selection of Airplane Mission and Corresponding Flight and Icing Conditions

A set of icing mission scenarios was defined that were typical of large commercial transport airplanes and included climb, cruise, hold and descent phases of flight. The selection of airplane weights, flight speeds, altitudes and angles of attack for each flight phase was appropriate for an airplane of the CRM65 class. The selected icing conditions were based upon the Code of Federal Regulations Part 25 Appendix C continuous maximum envelope and thus defined droplet MVD, cloud LWC and temperature.

# 2.3.2 Simulation of Full-Scale Icing Conditions

The large matrix of flight and icing conditions defined in task 1 were reviewed and a smaller number of cases were selected for further analysis. This subset of icing scenarios provided for a range of ice accretion on the full-scale airplane, while significantly reducing the workload associated with analyzing all cases. Flow simulations were performed at each of the selected flight conditions using the 3-D RANS code OVERFLOW (Ref. 54), thus generating a large database of flowfield information for the clean, flight baseline of the full-scale airplane. The flowfield solution was used as input to the LEWICE3D iceaccretion prediction code to generate ice-shape results for the corresponding flight conditions. Some

results are shown in Figure 11 and Figure 12 for a flight condition at 10,000 ft altitude, speed $= 2 3 2 \mathrm { k n }$ , static temperature $= - 4 ^ { \circ } \mathrm { C } .$ , airplane angle of attack $= 3 . 7 ^ { \circ }$ , droplet $\mathrm { M V D } = 2 0 \mu \mathrm { m } ,$ , cloud $\mathrm { L W C } = 0 . 5 5$ ${ \mathrm { g } } / { \mathrm { m } } ^ { 3 }$ and an exposure time of $4 5 \mathrm { { m i n } }$ . The contours of local collection efficiency in Figure 11 show the location of water impingement on the nose section of the fuselage and wing leading edge. The close-up view near the wing tip illustrates the regions of highest local collection efficiency. Figure 12 depicts the LEWICE3D generated ice shapes at several locations along the span of the wing. Close up views are shown near the wing root and tip sections. For this case, the predicted ice shape is a large upper-surface horn. Results of this type were generated for all of the icing cases selected for analysis.

图片摘要：该图主要展示 11.—LEWICE3D local collection efficiency results for CRM65, 。
![](images/6424f167eeb347e815667ad1382b5c35142e4a2c0c3f171f9f24b3f5693d9027.jpg)  
Figure 11.—LEWICE3D local collection efficiency results for CRM65, droplet ${ \mathsf { M V D } } = 2 0 { \mathsf { \mu m } }$ , $\mathsf { V } = 2 3 2 \mathsf { k n }$ , altitude = 10,000 ft.

图片摘要：该图主要展示 11.—LEWICE3D local collection efficiency results for CRM65, 。
![](images/796f017187c309b2490d42831486f03315ba85dfe15dcbab0416bd03dce49851.jpg)  
Figure 12.—LEWICE3D ice shape results for CRM65, droplet ${ \mathsf { M V D } } = 2 0 { \mathsf { \mu m } }$ , $\mathsf { V } = 2 3 2 \mathsf { k n }$ , altitude $=$ 10,000 ft, $\mathsf { L W C } = 0 . 5 5 \ : \mathsf { g } / \mathsf { m } ^ { 3 }$ , static temperature $= - 4 ~ ^ { \circ } \mathsf C$ , 45-min exposure.

图片摘要：该图主要展示 12.—LEWICE3D ice shape results for CRM65, droplet , , altitu。
![](images/793681cff419bbd35df8184ed54964078f4c03308f4a8c8570a200ae0dccf6f9.jpg)

图片摘要：该图主要展示 12.—LEWICE3D ice shape results for CRM65, droplet , , altitu。
![](images/d287fd5cbed95b1ac8595d3eaa81ed2fe68b5853fe5177d25dd1c1878440a66c.jpg)  
Figure 13.—Normalized horn thickness and horn angle taken from the LEWICE3D results shown in Figure 12.

The LEWICE3D results were analyzed to understand the spanwise variation in the predicted ice geometry. The maximum thickness of the ice and the angle associated with that maximum thickness location were calculated along the span of the wing. For the ice shapes shown in Figure 12, this represents the length of the ice horn and the angle of the horn with respect to the chord line at each wing station. These data are plotted in Figure 13 where the horn length and ice thickness are normalized by the local chord length. In this figure, the horn length is measured from the tip of the horn to the center of the leading-edge radius whereas the ice thickness is the portion of this length from the wing surface to the horn tip. The data show that for this case, the normalized ice thickness tends to increase from the root to about 50 percent semispan, where there is a decrease. The normalized ice thickness then tends to increase from about 55 percent semispan outward to the wing tip. These plots were generated and scrutinized for each set of LEWICE3D cases.

A major outcome of this task was the selection of the spanwise locations to be used for the hybrid model designs. Determining the number of spanwise locations to select required a balance of competing factors. In this research effort, each of the selected locations will be used as the basis for the design of a hybrid swept-wing model to be constructed and tested in the IRT. Selecting a large number of spanwise locations provides the highest fidelity representation of the ice accretion along the entire wing. Since the hybrid model design process will result in large and complex models, practical considerations of time and resources limit the total number that can be successfully constructed and tested in the IRT. Estimates of model size, time to complete the hybrid-model designs, fabrication cost, number of IRT test days required, and cost of IRT testing were developed. After reviewing these estimates it was decided that selecting three spanwise stations for further analysis provided a reasonable balance of the competing factors.

An additional factor for selecting three spanwise stations was driven by the expectation that these stations should be located near the wing: (1) root, (2) midspan and (3) tip. The section near the wing root, or inboard station, was selected to be at 20 percent semispan because this corresponded to the minimum horn-ice angle for nearly all of the icing cases analyzed. This is the case for the data shown in Figure 13.

图片摘要：该图主要展示 13.—Normalized horn thickness and horn angle taken from the 。
![](images/40ab4cbdc19adc39396ad80b51717cc7dcbd19192a85877656446d92667ec8aa.jpg)  
Figure 14.—Sketches of CRM65 wing showing selected hybrid model design stations at 20, 64, 83 percent semispan.

The midspan station was selected to be at 64 percent semispan because this corresponded to the maximum horn-ice angle for nearly all of the icing cases analyzed. This is also illustrated in Figure 13. The section near the tip, or outboard station, was selected to be at 83 percent semispan. This location approximates the outboard extent of the wing leading-edge ice protection system in some cases, thus making the icing characteristics significant for that reason. This location is also about halfway between the 64 percent semispan station and the wing tip. These three wing stations are shown graphically in Figure 14.

# 2.3.3 Design and Simulation of Hybrid Model Wing Sections in 2-D

The design of hybrid models for icing tests where the full-scale leading-edge geometry is combined with a truncated afterbody has been explored by Saeed et al. (Refs. 55 to 57 Past research was conducted primarily for 2-D wing sections and for moderate model sizes that did not require special consideration of tunnel wall interference effects. In the current effort, these 2-D design methods were adapted to the swept-wing geometry and extended to include the effects of the tunnel walls on the large-blockage-model flowfield. Fujiwara et al. (Ref. 58) provide a detailed description of this process along with the results to date. Therefore, only a brief example of interim results is provided here. As the design process is currently on-going, these results are likely to change prior to the completion of this task.

In simple infinite-swept wing theory, the flow at a spanwise wing station is approximated by the flow about the leading-edge-normal airfoil section at the appropriate 2-D Mach number and angle of attack. Since 2-D hybrid airfoil design methods are relatively well developed, the first step in the swept-wing wind-tunnel model design process takes advantage of these 2-D tools to produce a representative 2-D hybrid airfoil. Then, in a later process (Section 2.3.4), this is extended into a 3-D swept-wing model and validated using 3-D simulation tools and results.

As an example, the hybrid model design process was conducted for the wing station at 64 percent semispan. The airfoil used for the analysis was taken perpendicular to the leading edge. A comparison of the airfoil geometries and surface pressure coefficient results are shown in Figure 15. The full-scale leading edge was maintained in the hybrid airfoil to $x / c = 0 . 0 5$ on the upper surface and $x / c = 0 . 1 0$ on the lower surface. These limits were set based upon the expected ice accretion limits from the LEWICE3D results on the full-scale airplane described in the previous section. Downstream of these locations the hybrid airfoil contour was significantly different from the full-scale airfoil and includes a single-element, trailing-edge flap. The total chord length of the hybrid airfoil (including the flap) is about half the size of the full-scale chord length. The flap plays an important role in the hybrid design method since it can be used to adjust the airfoil circulation and thus the leading-edge flowfield (stagnation point, minimum pressure coefficient, etc.) and as a result, provides additional means of matching the full-scale conditions.

The pressure coefficient comparison in Figure 15 shows what is considered to be typical matching of the hybrid and full-scale surface pressure in the region of the leading edge and stagnation point which is of importance for matching the local collection efficiency and resulting ice shape. It is not expected that the hybrid and full-scale pressures should match downstream of the leading-edge region since the airfoils are significantly different. The goal of the hybrid airfoil design methodology is to provide the best matching to the full-scale local collection efficiency and leading-edge flowfield and, as a result, the ice shape. This comparison is shown in Figure 16 where the agreement is very good for this optimized hybrid design. These hybrid and full-scale airfoil results were generated using LEWICE (a 2-D code). However, the 3-D, full-scale, OVERFLOW and LEWICE3D ice-shape results are also used in the hybrid design process. Figure 16 shows a comparison of the hybrid model and full-scale, LEWICE3D ice shapes. This example illustrates that the hybrid model design process can effectively simulate the full-scale icing results with a significantly smaller model. Additional research is underway to address the effects of the tunnel walls in both 2-D and 3-D simulations.

图片摘要：该图主要展示 15.—Comparison of full scale and hybrid airfoil geometry and。
![](images/71cac3b29abbdc5a38d178e9177ca7ff406fdeef65efe424994924e8aec733c1.jpg)

图片摘要：该图主要展示 15.—Comparison of full scale and hybrid airfoil geometry and。
![](images/b884312cb3f0ebc71b860ade8f09682be0887d5757674c91c109f9aa0183e65e.jpg)  
Figure 15.—Comparison of full-scale and hybrid airfoil geometry and surface pressure distribution for 64 percent semispan station. (Note: these are interim results intended as an illustrative example.)

图片摘要：该图主要展示 15.—Comparison of full scale and hybrid airfoil geometry and。
![](images/1b74ef4e51955088c8d1a196a905f74f1b6235713a1629dffcab18b44557af42.jpg)

图片摘要：该图主要展示 15.—Comparison of full scale and hybrid airfoil geometry and。
![](images/870d6f419c463a1f1d6b3821367dfe2b1e5df5765f67ffa559649b469509be18.jpg)  
Figure 16.—Comparison of full-scale and hybrid airfoil local collection efficiency and ice shape results for 64 percent semispan station. (Note: these are interim results intended as an illustrative example.)

图片摘要：该图主要展示 16.—Comparison of full scale and hybrid airfoil local collec。
![](images/8bf138b56de707306e3b10ec868ae9613f3d604149dc4524410f3f7963473c1b.jpg)

图片摘要：该图主要展示 16.—Comparison of full scale and hybrid airfoil local collec。
![](images/34453dac7b153b32a139c737ef60b813a8f867f8656803c740fe87371f3e3110.jpg)

图片摘要：该图主要展示 16.—Comparison of full scale and hybrid airfoil local collec。
![](images/af9060a977528503518c294cbe96090f5954753c7a7e694f034cb2bccc846ff3.jpg)  
Figure 17.—Conceptual sketch of 3-D hybrid swept-wing model in IRT test section.

# 2.3.4 Design and Simulation of Hybrid Model Wing Sections in 3-D

Having demonstrated computationally in task 3 that the 2-D hybrid airfoil, coupled with infinite swept-wing theory, can accurately generate the ice accretion at a section of a finite swept wing, the fullspan, 3-D IRT model can be designed. In the IRT testing, the 3-D hybrid model is used to generate the ice accretion found at one spanwise station of the full-scale swept wing, which significantly simplifies the hybrid model design process. The 2-D hybrid airfoil sections are extended and swept to create the 3-D models for testing in the IRT. Consistent with infinite-swept-wing theory, these models have zero twist and zero taper greatly simplifying the design and ultimately, the construction of the models.

Once the models are designed, they must be validated using sophisticated 3-D computational tools capable of modeling the aerodynamics, droplet impingement and ice accretion in the realistic, highly 3-D, IRT environment. The analysis to be carried out includes 3-D flow simulations along with LEWICE3D simulations for the hybrid model in the IRT test section. These results will be evaluated against the fullscale flight baseline results described in Section 2.3.2 to determine if any design changes are needed. A conceptual sketch of a 3-D hybrid model in the IRT test section is shown in Figure 17. The large size of the model relative to the test-section dimensions indicates the importance of the 3-D flow simulations. This work is currently in progress and the results will be presented in future reports and papers.

The completion of the hybrid model design tasks will lead to the construction of the three models representing the 20, 64 and 83 percent semispan stations of the full-scale wing. A series of ice-accretion test campaigns in the NASA IRT are planned in order to build the database of swept-wing ice accretion required for validation of icing simulation tools, fabrication of artificial ice shapes for aerodynamic testing and for CFD simulations of the iced swept wing.

# 2.4 Phase IV: High-Reynolds Number Aerodynamic Testing

High-Reynolds number aerodynamic testing will be conducted in Phase IV. A test campaign is planned for the ONERA F1 wind tunnel to investigate the aerodynamic effect of artificial ice shapes on the CRM65 wing. The F1 wind tunnel is a large-scale pressure tunnel having a test section 11.5 ft high by 14.8 ft wide. A scaled, semispan model of the CRM65 wing will be designed and built to mount in the wind-tunnel force balance. A preliminary model sizing analysis has been carried out for the swept wing. The main constraints on the geometry are the model span relative to the test-section height and the blockage defined as the ratio of the model planform area relative to the test-section area. While a large model is desirable to increase Reynolds number and the physical size of the artificial ice-shape geometries, a small model is desirable to mitigate tunnel-wall interference effects that can compromise the quality of the aerodynamic data. A sizing study was conducted to investigate these trade-offs. The best compromise was determined to be a 12.8 percent scale model with semispan that is 70 percent of the test-

section height and planform area that is 8.5 percent of the test-section area. Dimensionally, this corresponds to a semispan of 8 ft and mean aerodynamic chord of 1.8 ft. The model aspect ratio and taper ratio are the same as for the full-scale CRM65 wing.

Aerodynamic testing will be performed up to a Reynolds number based upon mean aerodynamic chord of $1 0 \times 1 0 ^ { 6 }$ and up to a Mach number of 0.3. In addition to standard force balance and surface pressure measurements, more detailed measurements are being investigated as described in Section 2.2.3. A series of full-span artificial ice shapes will be designed and built using the 3-D scan geometries from the IRT tests of the 20, 64 and 83 percent semispan stations of the CRM65 wing. One technical challenge associated with this effort is developing the full-span artificial ice shapes based upon the 3-D scan data from only three discrete spanwise stations tested in the IRT. It is anticipated that different lofting and interpolation methods will be used to design the artificial ice shapes. In addition, artificial ice shapes based upon the LEWICE3D simulation results may also be tested. A large number of configurations will be explored with varying levels of geometric fidelity. An important objective for the Phase IV research is determining the level of geometric fidelity required for the artificial ice shapes in order to yield accurate iced-wing aerodynamics. This will result in a large database of high-fidelity, iced-swept wing aerodynamic data at Reynolds numbers significantly higher than what is currently available in the public domain.

# 2.5 Phase V: Low-Reynolds Number Aerodynamic Testing

A series of low-Reynolds number aerodynamic test campaigns are planned for Phase V in order to develop a lower cost test capability for iced swept wings. There are several closed-return atmospheric wind tunnels in the United States with test section sizes of approximately 7 ft by 10 ft. One of these facilities will be selected for a series of low-Reynolds number aerodynamic test campaigns using a scaled, semispan model of the CRM65 wing that is very similar to that used for testing in the ONERA F1 wind tunnel. It is anticipated that the maximum Reynolds number based upon mean aerodynamic chord will be $2 \times 1 0 ^ { 6 }$ at a Mach number of 0.25. Aerodynamic measurements similar to Phase IV are planned. An important objective of Phase V is to quantify the differences in aerodynamic performance and key flowfield features between the low- and high-Reynolds number testing. If these differences prove to be small, the low-Reynolds number facility can be used for a variety of other investigations. For example, a series of ice-shape sensitivity tests could be conducted to explore the effects of ice feature size, shape and location making it possible to identify certain critical cases. The low-Reynolds number facility could also be used for more detailed flowfield measurements using more sophisticated methods such as Particle Image Velocimetry (PIV).

# 2.6 Phase VI: High-Reynolds Number Validation Testing

For Phase VI, a second high-Reynolds number test campaign using the ONERA F1 wind tunnel is planned in order to conduct validation testing of critical ice shape cases identified in Phase V. In a large effort such as this, it is anticipated that all iced-wing configurations of interest cannot be tested in Phase IV. After conducting more detailed research at low-Reynolds number (in Phase V), it is expected that more ice-shape configurations of interest will be identified. It is also possible that significant Reynolds number effects will be identified. Therefore, further tests may be required at the end of this research effort in order to validate the final conclusions. The research conducted in this phase will “close-the-loop” on our understanding of swept-wing icing effects, generating an improved understanding and both experimental and computational simulation tools.

# 2.7 Phase VII: 3-D Ice Accretion and Flowfield Computational Simulation

In Phase VII, computational studies will be performed to identify the elements of the computational simulation process that are critical for accurate ice-shape predictions and reproduction of the aerodynamics of iced swept-wing geometries. This research is being conducted in parallel with the other tasks throughout the duration of the project. Computational research efforts will be undertaken using the geometric data of the CRM, ice shapes and the aerodynamic data from the experiments to evaluate current CFD capabilities with respect to simulation of iced swept-wing aerodynamics.

Prior to any ice-accretion prediction, an accurate evaluation of the aerodynamic performance of the clean semispan wing as designed for the aerodynamic testing in Phases IV and V has to be performed, as it will be used as reference for the estimation of the performance degradation due to ice. Therefore, a first part of the computational activity will consider some parametric studies on the semispan clean wing in the windtunnel configuration. Among the different factors to be considered for simulation are clean aircraft flow characteristics, proper selection of grid resolution, turbulence models, and steady or unsteady calculations. Other factors that can have a significant influence on the final solution (experimental set-up, Reynolds number effect, model deformations under loaded conditions due to pressurization) will also be investigated.

The added complexity of ice-shape geometries introduces the need to determine the degree of surface feature fidelity that can be and must be captured in the simulation to produce acceptable computational results. The evaluation of the aerodynamic performance of the wing with ice shapes will be mainly investigated using “standard” grid techniques (structured or unstructured meshes), with a detailed resolution up to the wall.

An initial look at what might be done with ice shape information from this program is show in Figure 18. This figure demonstrates the process of using 3-D scan data from an actual ice shape as input to a standard grid generation software package. Figure 18(a) shows the full detail data from a scan of ice build-up on a NACA 23012 airfoil model. The discrete set of surface geometry coordinates from the laser scanner were post-processed to produce a watertight surface consisting of numerous triangles which were provided in a format compatible with most grid generation software. The surface description was then modified using smoothing algorithms within the post-processing software to obtain a lower resolution version of the surface, as seen in Figure 18(b). That file was then used as input to the grid generation software to produce the surface grid shown in Figure 18(c) and the volume grid in Figure 18(d). Different levels of smoothing will be examined to determine the influence on the aerodynamics very close to the surface as guidance for CFD modeling of the full CRM model geometry both with and without leadingedge ice shapes.

图片摘要：该图片与(c)An initial look at what might be done with ice shape information from this pr这部分内容相关。
![](images/1f5a0ff61ed01b8dd5c282518b44574b2728c6292950324778d6c6f95279158e.jpg)

图片摘要：该图主要展示 18.—Development of CFD grid from 3 D scanned ice shape。
![](images/f85e5103d5c2ddce7d5da9b38d3a25424bc7c7dadbf44ba23879469b0b99ba96.jpg)

图片摘要：该图主要展示 18.—Development of CFD grid from 3 D scanned ice shape。
![](images/c81f294f846171880144deff03bb5b45e230fdf039484e0b9cdebe52b16e1e1e.jpg)  
(c)

图片摘要：该图片与Figure 18.—Development of CFD grid from 3 D scanned ice shape；In parallel, ONERA这部分内容相关。
![](images/d66be78e1b416a7d00139efdc7dc4f258f6adf36ece87f0b0bc2fd601bdaf979.jpg)  
  
Figure 18.—Development of CFD grid from 3-D scanned ice shape.

In parallel, ONERA will investigate the use of the “Immersed Boundary Conditions” (IBC) method in order to take the exact ice shape into account without having to mesh it explicitly (Ref. 59). A source term method will be introduced to accurately take into account the ice-shape boundaries. This IBC technique is currently under development in the ONERA elsA code (Ref. 60), and the validation phase for an application to iced wing shapes is planned to be carried out in the current project, according to the following sequence:

Use of a 2-D configuration for preliminary evaluation, and development/improvement of tools for ice-shape problems;   
Use a spanwise extension of the 2-D case to investigate the degree of geometrical refinement to be considered for ice shapes, and comparison with “standard” RANS computations in 2-D/2.5-D flow;   
Finally, 3-D applications on the configurations tested in F1, and comparison with “standard” RANS computations in 3D flow.

Concerning ice-accretion prediction, ONERA and NASA will perform calculations using their own 3-D icing suites. Initially, the ice shapes to be generated in the Phase III IRT test campaigns will be computed. The results of these simulations will be used for refining the definition of the test matrix and will be compared to the experimental results in a second step. ONERA will also work on the implementation of an automatic multistep procedure in its 3-D icing suite. With the current version of the suite (Ref. 61), the generation of new meshes for taking into account the ice-shape growth is done manually. This is complex and highly time consuming. Therefore the code is often used in a single step mode, which may not be accurate for complex ice shapes. The objective is to develop an automatic mesh adaptation and/or a re-meshing technique and to evaluate both its benefits and its range of application for the computation of 3-D ice shapes on a swept wing. A selected set of the tests performed in the IRT campaigns will be used for the assessment phase and comparisons with the NASA icing code will also be performed.

# 3.0 Summary

Ice accretion and its aerodynamic effect on highly three-dimensional swept wings are extremely complex phenomena important to the continued design, certification and safe operation of small and large transport aircraft. Computational fluid dynamics codes have reached a level of maturity that they are being proposed by manufacturers for use in certification of aircraft for flight in icing. However, sufficient high-quality data to evaluate their performance on iced swept wings are not available. Thus, it is difficult to determine how much confidence can be placed in the results from CFD codes used in design, and particularly in certification. NASA, FAA, ONERA, the University of Illinois and Boeing, have embarked on a significant, collaborative research effort to address the technical challenges associated with sweptwing icing. The overall goal of ensuring continued flight safety will be achieved by improving the fidelity of experimental and computational simulation methods for swept-wing ice accretion formation and resulting aerodynamic effect. The purpose of this paper is to describe this research effort in more detail and report on the current results and status to date.

A seven-phase research effort has been designed that incorporates ice-accretion and aerodynamic experiments and computational simulation. Conducted in Phase I was a review of the technical literature associated with iced swept-wing aerodynamics with emphasis on classifying ice accretion based upon key aerodynamic features of the flowfield. This research has provided a framework for the icing and aerodynamic experiments to be conducted in later phases. The research conducted in Phase II has identified the 65 percent scale Common Research Model as the baseline, full-scale, swept-wing reference geometry utilized for the experiments and computational research. In addition, 3-D measurement techniques are being developed and validated to document, the experimental ice accretion geometries.

Aerodynamic measurement techniques including pressure-sensitive paint and 5-hole probe wake surveys suitable to iced swept-wing experiments are being investigated. In Phase III, ice accretion testing will be conducted in the NASA IRT for three hybrid swept-wing models representing the 20, 64 and 83 percent semispan stations of the baseline wing. Hybrid models preserve the full-scale, leading-edge geometry combined with a custom-designed truncated afterbody to reduce the overall model size and blockage in the IRT test section. A significant research effort is currently underway to develop the large-scale, hybrid swept-wing model design methods. Artificial ice shapes of varying geometric fidelity will be developed for aerodynamic testing over a large Reynolds number range in Phases IV and V. Exploring the effects of geometric fidelity and Reynolds number will require final validation tests in Phase VI. The ONERA F1 pressurized wind-tunnel will be used for aerodynamic testing of a 12.8 percent scale semispan model of the baseline wing in Phases IV and VI. Data will be acquired for Reynolds numbers up to $\overline { { 1 0 \times 1 0 ^ { 6 } } }$ and Mach numbers of 0.3. Lower-Reynolds number aerodynamic testing will also be conducted on a smaller scale semispan wing model in an atmospheric 7- by 10-ft size wind tunnel in Phase V. The research conducted in Phase VII will explore and further develop the use of computational simulation tools (CFD codes) for ice accretion and aerodynamics on swept wings.

The combined results of this research effort will result in an improved understanding of the icing on swept wings. The ice accretion testing will generate a large database of ice-accretion geometries on realistic large-scale swept wings. An additional outcome is the advanced method for designing hybrid icing wind-tunnel models. The aerodynamic testing will generate a large database of performance and flowfield information for swept wings with artificial ice shapes of varying geometric fidelity over a large range of Reynolds number. Concurrent computational research will be conducted to develop and validate ice accretion and aerodynamic simulation tools for large-scale swept wings. These databases will be available to manufacturers to evaluate the performance of CFD codes which they propose to use in the certification of aircraft for flight in icing conditions. These results will be used to determine the accuracy to which ice accretion must be predicted by computational tools or simulated in aerodynamic testing. For example, it is known for some cases that swept-wing ice accretion can be highly three dimensional (e.g., “scallops” or “lobster tails”). This research will help define how much detail of that three-dimensionality is critical to the aerodynamic performance and therefore must be accurately simulated.

# References

1. Broeren, A.P., Addy, H.E., Jr., Bragg, M.B., Busch, G.T., Guffond, D., and Montreuil, E., “Aerodynamic Simulation of Ice Accretion on Airfoils,” NASA TP—2011-216929, June 2011.   
2. Bragg, M.B., Broeren, A.P., Addy, H.E., Jr., Potapczuk, M., Guffond, D., and Montreuil, E., “Airfoil Ice-Accretion Aerodynamics Simulation,” AIAA Paper 2007-0085, Jan. 2007.   
3. Bragg, M.B., Broeren, A.P., and Blumenthal, L.A., “Iced-Airfoil and Wing Aerodynamics,” SAE Paper 2003-01-2098, June 2003.   
4. Bragg, M.B., Broeren, A.P., and Blumenthal, L.A., “Iced-Airfoil Aerodynamics,” Progress in Aerospace Sciences, Vol. 41, No. 5, July 2005, pp. 323-418.   
5. Busch, G.T., Broeren, A.P., and Bragg, M.B., “Aerodynamic Simulation of a Horn-Ice Accretion on a Subscale Model,” AIAA Paper 2007-0087, Jan. 2007.   
6. Busch, G.T., Broeren, A.P., and Bragg, M.B., “Aerodynamic Simulation of a Horn-Ice Accretion on a Subscale Model,” Journal of Aircraft, Vol. 45, No.2, Mar.-Apr. 2008, pp. 604-613.   
7. Blumenthal, L.A., “Surface Pressure Measurements on a Three-Dimensional Ice Shape,” M.S. Thesis, Dept. of Aerospace Eng., Univ. of Illinois, Urbana, IL, 2005.   
8. Busch, G.T., “Ice Accretion Aerodynamic Simulation on a Subscale Model, M.S. Thesis, Dept. of Aerospace Engineering, Univ. of Illinois, Urbana, IL, 2006.   
9. Blumenthal, L.A., Busch, G.T., Broeren, A.P., and Bragg, M.B., “Issues in Ice Accretion Aerodynamic Simulation on a Subscale Model,” AIAA Paper 2006-0262, Jan. 2006.

10. Busch, G.T., Broeren, A.P., and Bragg, M.B., “Aerodynamic Fidelity of Sub-scale Two-Dimensional Ice Accretion Simulation,” AIAA Paper 2008-7062, Aug. 2008.   
11. Broeren, A.P., Busch, G.T., and Bragg, M.B., “Aerodynamic Fidelity of Ice Accretion Aerodynamic Simulation on a Subscale Model,” SAE 2007 Transactions: Journal of Aerospace, Vol. 116, Aug. 2008, pp. 560-575; also SAE Paper 2007-01-3285, Sept. 2007.   
12. Moens, F., “SUNSET Project: Numerical Investigations for the Preparation of the F1 Test Campaign,” ONERA Report Nº RT 1/12405 DAAP, April 2007.   
13. CassouDeSalle, D. and Gilliot, A., “SUNSET (Studies on Scaling Effects due to Ice) Tests at High Reynolds Number in F1 Wind Tunnel,” ONERA Report Nº PV 4/12361 DSFM, December 2008.   
14. CassouDeSalle, D., Gilliot, A., Geiler, C., Monnier, J.-C., Broeren, A.P., and Addy, H.E., Jr., “Experimental Investigations of Simulated Ice Accretions at High Reynolds Numbers in the Onera F1 Wind Tunnel,” AIAA Paper 2009-4265, June 2009.   
15. Broeren, A.P., Bragg, M.B., Addy, H.E., Jr., Lee, S., Moens, F., and Guffond, D., “Effect of High-Fidelity Ice-Accretion Simulations on Full-Scale Airfoil Performance,” Journal of Aircraft, Vol. 47, No. 1, Jan.-Feb. 2010, pp. 240-254.   
16. Broeren, A.P., Bragg, M.B., Addy, H.E., Jr., Lee, S., Moens, F., and Guffond, D., “Effect of High-Fidelity Ice-Accretion Simulations on Full-Scale Airfoil Performance,” AIAA Paper 2008-0434, Jan. 2008.   
17. Busch, G.T., “Experimental Study of Full-Scale Iced-Airfoil Aerodynamic Performance using Subscale Simulations,” Ph.D. dissertation, Dept. of Aerospace Eng., Univ. of Illinois, Urbana, IL, 2010.   
18. Duclercq, M., Brunet, V., and Moens, F., “Physical Analysis of the Separated Flow Around an Iced Airfoil Based on ZDES Simulations,” AIAA Paper 2012-2798.   
19. Vargas, M., “Current Experimental Basis for Modeling Ice Accretions on Swept Wings,” Journal of Aircraft, Vol. 44, No. 1. Jan-Feb 2007.   
20. Vargas, M., “Swept Wing Icing Studies at NASA Glenn Research Center 1996-2006,” SAE Aircraft & Engine Icing International Conference, Seville, Spain, 2007, Paper No. 2007-01-3332.   
21. Bidwell, C.S. and Mohler Jr., S.R., “Collection Efficiency and Ice Accretion Calculations for a Sphere, a Swept MS(1)-317 Wing, a Swept NACA-0012 Wing Tip, an Axisymmetric Inlet, and a Boeing 737-300 Inlet,” AIAA Paper 95-0755, Jan. 1995.   
22. Bidwell, C.S. and Potapczuk, M.G., “User’s Manual for the NASA Lewis Three-Dimensional Ice Accretion Code (LEWICE3D),” NASA TM–105974, Dec. 1993.   
23. Potapczuk, M.G. and Bidwell, C.S., “Swept Wing Ice Accretion Modeling,” NASA TM–103114, Jan. 1990.   
24. Potapczuk, M.G. and Bidwell, C.S., “Numerical Simulation of Ice Growth on a MS-371 Swept Wing Geometry,” NASA TM 103705, Jan. 1991.   
25. Potapczuk, M., Papadakis, M. and Vargas, M., “LEWICE Modeling of Swept Wing Ice Accretions,” AIAA Paper 2003-6565, Jan. 2003.   
26. Hedde, T., and Guffond, D., “Development of a Three-Dimensional Icing Code, Comparison with Experimental Shapes,” AIAA Paper 92-0041, Jan. 1992.   
27. Hedde, T., and Guffond, D., “Improvement of the ONERA 3D Icing Code Comparison with 3D Experimental Shapes,” AIAA Paper 93-0169, Jan. 1993.   
28. Szilder, K., McIlwain, S., and Lozowski, E.P., “Numerical Simulation of Complex Ice Shapes on Swept Wings,” ICAS Paper 2006-2.5.1, Sept. 2006.   
29. Presteau, X., Montreuil, E., Leroy, A., Guffond, D., Henry, R., and Personne, P, “Experimental Study of the Scallop Formation on Swept Cylinder,” SAE Paper 2007-01-3296, Sept. 2007.   
30. Presteau, X., Montreuil, E., Chazottes, A., Vancassel, X., and Personne, P, “Experimental and Numerical Study of Scallop Ice on Swept Cylinder,” AIAA Paper 2009-4124, June 2009.   
31. Bragg, M.B., Kerho, M.F., and Khodadoust, A., “LDV Flowfield Measurements on a Straight and Swept Wing with a Simulated Ice Accretion,” AIAA Paper 93-0300, Jan. 1993.

32. Kwon, O.J., and Sankar, L.N., “Numerical Study of the Effects of Icing on Fixed and Rotary Wing Performance,” AIAA Paper 91-0662, Jan. 1990.   
33. Khodadoust, A., and Bragg, M.B, “Measured Aerodynamic Performance of a Swept Wing with a Simulated Ice Accretion,” AIAA Paper 90-0490, Jan. 1990.   
34. Bragg, M.B., Khodadoust, A., Soltani, R., Wells, S., Kerho, M., “Effect of a Simulated Ice Accretion on the Aerodynamics of a Swept Wing,” AIAA Paper 91-0442, Jan. 1991.   
35. Vargas, M., Papadakis, M., Potapczuk, M., Addy, H., Sheldon, D. and Giriunas, J., “Ice Accretions on a Swept GLC-305 Airfoil,” SAE Paper 02GAA-43 and NASA TM-2002-211557, April 2002.   
36. Papadakis, M., Yeong, H. W., Won, S. C., Vargas, M. and Potapczuk, M., “Aerodynamic Performance of a Swept Wing with Ice Accretions,” AIAA Paper 2003-0731, Jan. 2003.   
37. Papadakis, M., Yeong, H.W., Wong, S, Vargas, M and Potapczuk, M., “Experimental Investigation of Ice Accretion Effects on a Swept Wing,” DOT/FAA/AR-05/39, Aug. 2005.   
38. Reehorst, A.L., Potapczuk, M.G., Ratvasky, T.P., and Gile-Laflin, B.E., “Wind Tunnel Measured Effects on a Twin-Engine Short-Haul Transport Caused by Simulated Ice Accretions,” AIAA Paper 96-0871, also NASA TM 107143, Jan. 1996.   
39. Reehorst, A.L., Potapczuk, M.G., Ratvasky, T.P., and Gile-Laflin, B.E., “Wind Tunnel Measured Effects on a Twin-Engine Short-Haul Transport Caused by Simulated Ice Accretions Data Report,” NASA TM–107419, May 1997.   
40. Papadakis, M., Yeong, H.W., Chandrasekharan, R., Hinson, M., Ratvasky, T., and Giriunas, J., “Experimental Investigation of Simulated Ice Accretions on a Full-Scale T-tail,” AIAA Paper 2001- 0090, Jan. 2001.   
41. Papadakis, M., Yeong, H.W., Chandrasekharan, R., Hinson, M., and Ratvasky, T. “Effects of Roughness on the Aerodynamic Performance of a Business Jet Tail,” AIAA Paper 2002-0242, Jan. 2002.   
42. Broeren, A.P., Diebold, J.M., and Bragg, M.B., “Aerodynamic Classification of Swept-Wing Ice Accretion,” NASA/TM—2013-216381, May 2013, also DOT/FAA/TC-13/21.   
43. Diebold, J.M., Broeren, A.P. and Bragg, M.B., “Aerodynamic Classification of Swept-Wing Ice Accretion,” AIAA 5th Atmospheric and Space Environments Conference, San Diego, CA, June 24- 27, 2013 (submitted for publication).   
44. Vassberg, J.C., DeHann, M.A., Rivers, S.M., and Wahls, R.A., “Development of a Common Research Model for Applied CFD Validation Studies,” AIAA Paper 2008-6919, Aug. 2008.   
45. Rivers, M.B., and Dittberner, A., “Experimental Investigation of the NASA Common Research Model,” AIAA Paper 2010-4218, June 2010.   
46. Rivers, M.B., and Dittberner, A., “Experimental Investigations of the NASA Common Research Model in the NASA Langley National Transonic Facility and the NASA Ames 11-Ft Transonic Wind Tunnel,” AIAA Paper 2011-1126, Jan. 2011.   
47. Vassberg, J. C., Tinoco, E. N., Mani, M., Rider, B., Zickuhr, T., Levy, D.W., Brodersen, O., Eisfeld, B., Crippa, S., Wahls, R. A., Morrison, J. H., Mavriplis, D.J., and Murayama, M., “Summary of the Fourth AIAA CFD Drag Prediction Workshop,” AIAA Paper 2010-4547, June 2010.   
48. Bosetti, C., Paul, B.P., Jr., and Malone, A.M., “Ice Shape Characterization to Aid in Replicating Ice Shapes for Subsequent Analysis,” AIAA Paper 2010-7534, Aug. 2010.   
49. Reehorst, A.L., and Richter, G.P., “New Methods and Materials for Molding and Casting Ice Formations,” NASA TM-100126, Sept. 1987.   
50. Lee, S., Broeren, A.P., Addy, H.E., Jr., Sills, R., and Pifer, E.M., “Development of 3-D Ice Accretion Measurement Method,” AIAA Paper 2012-2938, June 2012, also NASA/TM—2012-217702, Sept. 2012.   
51. Diebold, J.M., Monastero, M.C., and Bragg, M.B., “Aerodynamics of a Swept-Wing with Ice Accretion at Low Reynolds Number,” AIAA Paper 2012-2795, June 2012.   
52. Diebold, J.M., “Aerodynamics of a Swept Wing with Leading-Edge Ice at Low Reynolds Number” M.S. Thesis, Department of Aerospace Engineering, University of Illinois, Urbana, IL, Aug. 2012.

53. Diebold, J.M., and Bragg, M.B., “Study of a Swept-Wing with Leading-Edge Ice Using a Wake Survey Technique,” AIAA Paper 2013-0245, Jan. 2013.   
54. Sclafani, A.J., Slotnick, J.P., Vassberg, J.C., and Pulliam, T.H., “Extended OVERFLOW Analysis of the NASA Trap Wing Wind Tunnel Model,” AIAA Paper 2012-2919, June 2012.   
55. Saeed, F., Selig, M.S., and Bragg, M.B., “Hybrid Airfoil Design Procedure Validation for Full-Scale Ice Accretion Simulation,” Journal of Aircraft, Vol. 36, No. 5, Sept.-Oct., 1999, pp. 769-776.   
56. Saeed, F., Selig, M.S., and Bragg, M.B., “Hybrid Airfoil Design to Simulate Full-Scale Ice Accretion Throughout a Given α Range,” Journal of Aircraft, Vol. 35, No. 2, Mar.-Apr., 1998, pp. 233-239.   
57. Saeed, F., Selig, M.S., and Bragg, M.B., “Design of Subscale Airfoils with Full-Scale Leading Edges for Ice Accretion Testing,” Journal of Aircraft, Vol. 34, No. 1, Jan.-Feb., 1997, pp. 94-100.   
58. Fujiwara, G.E.C., Woodard, B.S., Wiberg, B.D., Mortonson, A.J., Bragg, M.B., “A Hybrid Airfoil Design Method for Icing Wind Tunnel Tests,” AIAA 5th Atmospheric and Space Environments Conference, San Diego, CA, June 24-27, 2013 (submitted for publication).   
59. Terracol M., Manoha E., and Lemoine B., “Investigation of the Unsteady Flow and Noise Sources Generation in a Slat Cove: Hybrid Zonal RANS/LES Simulation and Dedicated Experiment,” AIAA Paper 2011-3203, 20th AIAA Computational Fluid Dynamics Conference 2011, Honolulu, HI, 27-30, June 2011.   
60. Reneaux J., Beaumier P. and Giroudroux-Lavigne P. “Advanced Aerodynamic Applications with the elsA Software,” The Onera Journal, AerospaceLab Journal, Issue 2, March 2011. (www.aerospacelab-journal.org).   
61. Villedieu, P., Bobo, D., Guffond, D., Trontin, P. “SLD Lagrangian Modelling and Capability Assessment in the Frame of ONERA 3D Icing Suite,” AIAA Paper 2012-3132, New Orleans, 2012.

图片摘要：该图片与61. Villedieu, P., Bobo, D., Guffond, D., Trontin, P. “SLD Lagrangian Modelling 这部分内容相关。
![](images/62a6ac472faf4f3ad522754262fe46a9c4c8cb3034ac4057871473fc851f88dd.jpg)
