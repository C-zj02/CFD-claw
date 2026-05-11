# Progress Report

to

# NASA Ames Research Center

for

# NASA Grant NAG2-905

entitled

# "Experiments on the Flow Field Physics of Confluent Boundary Layers for High-Lift Systems"

by

R.C.Nelson,F.O.Thomas,and H.C.Chu

Hessert Center for Aerospace Research

University of Notre Dame

Notre Dame, IN 46556-5684

(NASA-CR-197318) EXPERIMENTS ON N95-21343

THE FLOW FIELD PHYSICS OF CONFLUENT

BOUNDARY LAYERS FOR HIGH-LIFT

SYSTEMS Progress Report (Notre

Dame Univ.) 18 p

G3/02 0039819

# PROGRESS REPORT: EXPERIMENTS ON THE FLOW FIELD PHYSICS OF CONFLUENT BOUNDARY LAYERS FOR HIGH-LIFT SYSTEMS

by

R.C.Nelson,F.O.Thomas and H.C.Chu Hessert Center for Aerospace Research Department of Aerospace and Mechanical Engineering University of Notre Dame Notre Dame,IN 46556 (219)631-5392 or (219)631-7899

# 1. Introduction

The use of sub-scale wind tunnel test data to predict the behavior of commercial transport high lift systems at in-flight Reynolds number is limited by the so-called "inverse Reynolds number effect." This involves an actual deterioration in the performance of a high lift device with increasing Reynolds number. A lack of understanding of the relevant flow field physics associated with numerous complicated viscous flow interactions that characterize flow over high-lift devices prohibits computational fluid dynamics from addressing Reynolds number effects. Clearly there is a need for research that has as its objective the clarification of the fundamental flow field physics associated with viscous effects in high lift systems. In this investigation, a detailed experimental investigation is being performed to study the interaction between the slat wake and the boundary layer on the primary airfoil which is known as a confluent boundary layer. This little-studied aspect of the multi-element airfoil problem deserves special attention due to its importance in the lift augmentation process. The goal of this research is to provide an improved understanding of the flow physics associated with high lift generation.

This progress report will discuss the status of the research being conducted at the Hessert Center for Aerospace Research at the University of Notre Dame. The research is sponsored by NASA Ames Research Center under NASA grant NAG2-905. The report will include a discussion of the models that have been built or that are under construction, a description of the planned experiments, a description of a flow visualization apparatus that has been developed for generating colored smoke for confluent boundary layer studies and some preliminary measurements made using our new 3-component fiber optic LDV system.

# 2. Motivation

It is desirable to design simpler high lift systems whose performance exceeds those that are now in use on commercial aircraft. Achieving this goal demands improved CFD

design tools that can realistically model the high lift system flow field over a wide Reynolds number range. Unfortunately, the flow field physics associated with modern high lift systems is quite complex and is dominated by numerous complex viscous interactions that represent some of the most challenging problems in fluid mechanics. It is futile to expect to use CFD to reliably compute the flow over multi-element airfoils when, at present, we sometimes cannot even reliably compute the individual "viscous building block flows" that together form a high lift system flow field.

Evidence suggests that the leading edge flow and, in particular, the interaction of the leading edge slat wake with the primary airfoil boundary layer is a key flow component in determining $\mathsf{C}_{\mathsf{Lmax}}$ in high lift systems and may even be associated with "inverse Reynolds number effects". Such Reynolds number scaling issues pose disturbing implications regarding how to rationally extrapolate low Reynolds number wind tunnel test data to predict $\mathsf{C}_{\mathsf{Lmax}}$ for flight Reynolds numbers. Indeed, traditional views regarding the effect of increasing Reynolds number on airfoil boundary layer structure is not appropriate for the complex viscous interactions that characterize commercial high lift systems.

A reduction in maximum lift coefficient with Reynolds number could occur by the following mechanism: It may be expected that for swept wings at all but the lowest Reynolds numbers the attachment line boundary layer is turbulent. As it circumnavigates the nose of the airfoil, the flow accelerates and consequently the boundary layer is initially exposed to a strong favorable pressure gradient. If this negative streamwise pressure gradient is strong enough as measured by the so-called "relaminarization parameter" (Lauer and Jones, 1969) then relaminarization can occur. The relaminarization process will greatly reduce the thickness of the boundary layer, and perhaps most importantly, move the location of onset of confluence with the slat wake downstream. The net effect of this will be to move the separation location on the primary airfoil aft. It has been shown experimentally (Garner et al, 1991 and van Dam et al, 1993) that as the Reynolds number increases, the relaminarization parameter is reduced to such a level that relaminarization may not take place. Thus, for sufficiently high Reynolds numbers, relaminarization of the leading edge boundary layer may cease. In such cases, the location of confluence between the slat wake and turbulent boundary layer on the wing moves forward and gives rise to rapid mixing and the generation of a very thick viscous layer that can readily separate due to the adverse pressure gradient aft of the primary airfoil pressure peak. In this manner $C_{\text{Lmax}}$ may be limited at high Reynolds numbers due to the combined effects of the failure of the airfoil boundary layer to relaminarize and its confluence with the slat wake.

Despite its perceived importance in high lift systems we know fairly little about the flow field physics of confluent boundary layers. The most extensive body of experimental work has been performed by the group at Cambridge University (Zhou and Squire (1983, 1985), Agoropoulos and Squire (1988) and Moghadam and Squire(1989)). These experiments have primarily examined the interaction between a wake generated by either a flat plate or symmetric airfoil and the neighboring wind tunnel wall boundary layer. These studies show that the level of turbulence in the wake has the strongest influence on the interaction. In cases where there is strong vortex shedding from the wake generating airfoil, the mixing in the interacting flow is found to be quite strong. The resulting confluent boundary layer is much thicker than the turbulent boundary layer would be in the absence of the upstream wake-generating body.

It is interesting to note here that the fluid dynamics of the leading edge confluent boundary layer occurs at comparatively low Reynolds numbers. For example, a Boeing 737-100 operating at a Reynolds number (based on m.a.c.) of $12 \times 10^{6}$ will have a slat Reynolds number of only about $1.4 \times 10^{6}$ . Similarly, the Reynolds number associated with the leading edge boundary layer, $\mathrm{Re}_{\mathbf{X}} = U_{\infty}x / \nu$ , where $\mathbf{x}$ is a streamline spatial coordinate, will also be of comparable magnitude. Thus it appears that the m.a.c.-based Reynolds number may not be an entirely appropriate correlating parameter in describing the leading edge confluent boundary layer. This observation suggests that Reynolds number effects on $\mathrm{CL}_{\max}$ that occur in high lift systems can actually involve comparatively low Reynolds number fluid dynamic phenomena. This indicates that these effects can be duplicated and studied in fairly low Reynolds number experiments.

# 3. Research Objectives

A primary objective of the current research effort is to perform benchmark experiments on the confluent boundary layer formed by the interaction of the slat wake and primary airfoil boundary layer. These experiments are being performed on a realistic geometry and under pressure gradient conditions that simulate the flow environment of a commercial high lift system. From these experiments we will clarify the role of the confluent boundary layer in determining $\mathrm{CL}_{\max}$ as well as discern the fluid dynamic mechanism(s) responsible for inverse Reynolds number effects. Through novel flow visualization we are isolating cases of strong and weak slat wake / boundary layer confluence and its effect on integrated lift. For selected representative cases, detailed fiber optic LDV confluent boundary layer surveys are being performed. The objectives of these surveys are to (1) provide a better understanding of the structure of the confluent boundary layer and its effect on lift production, (2) to investigate the effect of relaminarization upon the onset of confluence and the structure of the confluent layer and (3) to provide benchmark data that can be used

by computational fluid dynamicists in order to refine predictive capabilities of models. It is well known that the confluent boundary layer gives rise to counter-gradient momentum transfer and thus presents difficulties for standard turbulence models.

The improvement of high lift systems is essential for the United States to retain its leadership and competitiveness in the commercial aviation marketplace. This will require a substantial improvement in the basic understanding of the flow physics of high lift systems and the improvement of high Reynolds number facilities for development work. We believe that only through an understanding of the fundamental flow field physics of the confluent boundary layer can a rational design strategy for simplified high lift systems be developed. Such understanding would set the stage for more meaningful testing in high Reynolds number facilities. This study is providing a unique opportunity to examine the flow physics of high lift systems by controlling some of the major factors that affect high lift performance. This research complements that being planned by NASA as well as providing detailed flow information needed to develop flow models that will be essential for the improvement of computational modelling of high lift systems.

# 4. Research Accomplishments To Date

Funding under NASA grant NAG2-905 commenced during the summer of 1994. This section describes research accomplishments to date and describes the planned experimental program. Most of the work to date has involved the design and fabrication of a required multi-element airfoil model and wind tunnel test section as well as the validation of a fiber optic LDV system that will be used extensively for the research. At this juncture all phases of the project are on schedule.

# 4.1 Multi-element Airfoil Design:

The slat and main airfoil section model are both fully two-dimensional. A schematic of the high-lift system model which has been constructed at the Hessert Center for Aerospace Research are shown in Figure 1. Since our experiment is primarily concerned with the leading edge flow physics and the primary wing confluent boundary layer, the airfoil used has an elliptical cross section whose contour in the x-y plane is given by,

$$
\frac {\mathrm {y}}{\mathrm {c}} = \tau \sqrt {\frac {\mathrm {x}}{\mathrm {c}} (1 - \frac {\mathrm {x}}{\mathrm {c}})}
$$

where $c$ is the chord length and $\tau$ is the maximum thickness-to-chord ratio. The slat shape is typical of those used in commercial high lift systems and possesses a sharp trailing edge. As seen in Figure 1, the top surface slat contour is the same as that of the main airfoil leading edge. The slat under-surface contour is generated using a similar elliptical

geometry. The length of the slat is 0.15c. In order to reduce blockage caused primarily by the main airfoil section, the chord length c and thickness ratio $\tau$ of the high-lift model were optimized at 15 in. and 0.15, respectively. The Reynolds number based on the main chord c is approximately $10^6$ .

图片摘要：该图主要展示 1. Schematic of 2 D High lift Model。
![](images/53075a4449c4fd3ffb9fe7d6393ac57fae0ea52c9a776fc6014d91dc403a86dd.jpg)  
Figure 1. Schematic of 2-D High-lift Model

An aluminum mold was first built using a computer-controlled CNC milling machine. Figure 2a shows a photograph of the aluminum mold being machined. The mold was then used to pour epoxy airfoil models. Figure 2b is a photograph showing the epoxy model along with the aluminum mold.

One model contains slots for smoke flow on the slat and airfoil boundary layer; this model is to be used extensively for smoke flow visualization of the confluence between slat wake and airfoil boundary layer. The other is to be used for detailed surface pressure measurements. A total of 64 pressure taps are distributed over the center span of both top and bottom surfaces of the slat and main airfoil in order that the pressure distribution can be experimentally obtained. In addition, a total of 24 spanwise pressure taps are installed at three different chordwise locations on the main airfoil in order to monitor the two-

图片摘要：该图主要展示 1. Schematic of 2 D High lift Model。
![](images/ecad7bc8e82ae755c9c30cfec22ee43d07b566e3797fd3dd39e247ab2497c51f.jpg)  
(2a)

图片摘要：该图主要展示 s 2a, 2b Aluminum Mold and High Lift Model Construction。
![](images/78150946b3a049e47da66d3501ed20f149591736df07a04b81e108887f6485a5.jpg)  
(2b)   
Figures 2a, 2b Aluminum Mold and High-Lift Model Construction

dimensionality of flow over the airfoil. An internal plenum and blown flap is used in conjunction with a suitable angle of attack to obtain the characteristic "peaky" airfoil pressure distribution ( $C_{\text{pmax}} \approx -4$ ) which would be found in a typical high-lift system. The relative position between slat and main airfoil section is completely adjustable in terms of both gap width and overhang parameters.

A complete test matrix involving multiple slat positions, blown flap settings, and angle of attack is quite large. In order to reduce the number of parameters to a manageable level, flow visualization will be used first in order to isolate cases of both strong and weak slat wake / boundary layer confluence. For these cases detailed surface pressure measurements will be made. The flow visualization system constructed for this project is next described.

# 4.2 Design and Construction of Flow Visualization System

Development of the flow visualization techniques described below will provide an effective means to visualize the interaction between the wake of the slat and the boundary layer of the main wing of the high lift system under study. The objective of this design is to provide a simple, cost effective means to visualize the nature of the interaction between the wake of the leading edge slat and the boundary layer of the main wing. We propose the use of color smoke to investigate this complex region of viscous flow. Such a flow visualization system would involve injecting one color of smoke into the boundary-layer of the wing and another color at the leading edge of the slat. Analysis of this multi-color flow visualization would allow the point of confluence to be determined as well as the basic flow physics to be better understood. By taking advantage of multiple colors of smoke, the wake of the slat and the boundary layer of the wing could be visualized individually; both before and after the regions of flow merge to form a confluent boundary layer. In addition, the use of multiple colors provides the option of using image processing systems to perform detailed analysis on the location of the flow interaction.

By modifying the technique of using a single smoke wire (see Batill and Mueller (1981, 1982)), a new technique will be used which employs the use of a "smoke screen". The integrated effect of using numerous discrete smoke wires could be obtained by coating the surfaces of a small mesh wire screen with a thin layer of mineral oil. The powdered dye is then applied to the surfaces of the screens. In order to implement this technique, a new experimental apparatus was built.

A basic schematic of this device appears in Figure 3a. Figure 3b presents a photograph of the colored smoke generator. Using off-the-shelf galvanized steel pipe and pipe fittings the basic structure of this device was assembled by simply threading each component together. The 2" diameter size of the pipe and tee at the bottom of the figure was required

图片摘要：该图主要展示 s 3a, 3b Flow Visualization Apparatus。
![](images/0bf7f2571f34d48351f312cc520f4eb7cd2f03b7f3640cdbbd48464863ba5209.jpg)

图片摘要：该图主要展示 s 3a, 3b Flow Visualization Apparatus。
![](images/b7dff62466537ee2703ea887eaf72731668adcdaa10a2a807fe51a299dc27be3.jpg)  
Figures 3a, 3b Flow Visualization Apparatus

for testing combustion products such as standard "smoke-bombs". By using gas ball valves at the compressed air inlet and at the smoke exit, the device can be pressurized and the mass flow rate of smoke exiting to the model can be regulated. For safety precautions, a pressure relief valve opens up a bleed line to maintain the internal pressure below 75 psi. Furthermore, a "check" valve eliminates the possibility of back flow toward the air compressor. The use of compressed air at moderate pressures (5-15 psi) allows the smoke to be forced through the tygon tubing into the model plenum chamber. The steel cap attached to the $2''$ - diameter tee opens to allow the insertion of the smoke producing device into the chamber formed by the $2''$ tee and pipe. Several tests of the device have been conducted by simply igniting one or two color smoke bombs inside the $2''$ tee. The results of these tests were used to determine the performance of the smoke generator, to determine safety procedures, and to observe the color quality of the smoke bombs. Since a relatively small volume of smoke was used, the smoke bombs appeared to provide a similar degree of performance as the smoke screens. Because of safety requirements, a method to employ the smoke screen technique using this device is still being developed. Therefore, the objective of current studies involves selecting a candidate for the heat source used to raise the temperature of the screens to around $200^{\circ}\mathrm{F}$ . Owing to the modular construction of this device, any future design modifications can be applied at low cost with relative ease.

In summary, the smoke screen technique appears to be an effective means to produce colored smoke. The smoke screen technique involves coating wire mesh screens with a thin layer of mineral oil and dye, and then heating the screens to around $200^{\circ}\mathrm{F}$ . Another possible technique involves the combustion of smoke bombs. Both the smoke bomb and smoke screen techniques can employ the use of the smoke generator apparatus described earlier. This apparatus contains the smoke and channels a desired amount into the plenum chamber of a wind tunnel model. The challenges of this study involve the production of a sustained, coherent supply of colored smoke, the application of proper lighting and background techniques in order to visualize the interaction between the slat wake and airfoil boundary layer.

# 4.3 Detailed Measurements of Confluent Boundary Layer Structure:

For a swept wing at all but the lowest Reynolds numbers the attachment line flow is turbulent. Since we are performing the experiments with a two-dimensional model there is obviously no cross flow instability or root chord contamination to produce a turbulent boundary layer on the main airfoil. It is also not possible to trip the boundary layer near the leading edge at Reynolds numbers near $10^{6}$ due to the inherent stability of the boundary layer in the strong favorable pressure gradient. Creation of a turbulent layer on the main element is essential if the effects of relaminarization are to be studied.

In order to overcome this difficulty the following strategy was developed. Based upon the results of the flow visualization study, selected cases involving strong and weak confluence will be examined in detail. That is, detailed surface pressure distributions will be obtained along with measurements of the slat wake width and airfoil boundary layer thickness variation. A "viscous pressure gradient parameter" like $\delta_{\mathrm{w}} dP / dx$ will be obtained from these measurements where $\delta_{\mathrm{w}}$ is a relevant viscous flow parameter like the thickness of the boundary layer at the slat trailing edge. This parameter will be matched in an experiment in a specially designed test section in which the slat wake interacts with a flat plate boundary layer in the wind tunnel test section as shown in Figure 4. The boundary layer on the flat plate will be artificially tripped near the plate leading edge.

In order to facilitate the study of wake interactions with boundary layers on the airfoil surface, an experiment will be carried out in the specially design test section in which the confluent boundary layers will be created by the interaction of a slat wake and the boundary layer on a flat plate. The slat used in this experiment will be the same as the slat used with the high-lift model. It is important to understand that the shape of 2-D bump shown in Figure 4 is not arbitrary and is dictated by the previous static pressure measurement on the airfoil model. That is, the pressure gradient over the flat plate caused by the 2-D bump should be identical to the pressure gradient measured on the high-lift airfoil model. An inviscid code will transform the variation of static pressure distribution to the corresponding contour coordinates which can be saved for a later surface machining by a CNC machine. It stands to reason that if the plate boundary layer develops under identical pressure gradient conditions as in the multi-element airfoil model, and if we match the slat wake viscous parameter, then the confluent layers should be identical. The arrangement shown in Figure 4 has the additional advantages of allowing relaminarization effects to be studied as well as allowing LDV measurements of much finer spatial resolution than could possibly be obtained directly from the multi-element model.

图片摘要：该图主要展示 4. Schematic of Test Section Setup with Slat, Flat plate, an。
![](images/9a0ec81c76f5428fbd9ff5789dcd79b564a5638380a29e4f3a3f47b05cb0e604.jpg)  
Figure 4. Schematic of Test Section Setup with Slat, Flat plate, and 2-D Bump

The experiment depicted in Figure 4 will be performed in an in-draft tunnel which is shown in the schematic in Figure 5. The test section of indraft tunnel has a $2\mathrm{ft} \times 2\mathrm{ft}$ ( $0.51\mathrm{m} \times 0.51\mathrm{m}$ ) cross section and is $6\mathrm{ft}$ ( $1.52\mathrm{m}$ ) in length. The air flow into the inlet was driven by a eight-bladed fan connected to a $18.6\mathrm{kW}$ AC induction motor. The contraction ratio of tunnel is 22:1 with 12 anti-turbulence screens which leads to a low turbulence intensity level of approximately $0.05\%$ as determined by a straight hot-wire.

图片摘要：该图主要展示 4. Schematic of Test Section Setup with Slat, Flat plate, an。
![](images/9cfa1f6757eb82fe1d4b2c6248227dc19cd52cad28d0d1db63094c82b72cd42b.jpg)  
Figure 5 Schematic of a Subsonic Wind Tunnel At the University of Notre Dame

The experiment depicted in Figure 4 requires a smooth flat plate with the ability to maintain attached, flow over the majority of its surface and of sufficient length to generate a boundary layer thickness of suitable size. The leading and trailing edges of the plate were similar to that designed by Sullivan, et al (1994) using the MCARFA program originally developed at NASA/Langley.

A schematic of the flat plate for the experiment are shown in Figures 6. The total length of the flat plate is $\frac{65 \times 11}{16}$ inches which corresponds to a Reynolds number of $3.48 \times 10^{6}$ at a tunnel speed of 100 ft/s. The leading edge of flat plate consists of a 1 inch high, quarter ellipse over the upper surface with a 4:1 ratio in the streamwise direction and a 0.25 inch radius, quarter circle as the lower surface contour. The upper trailing edge is flat while the lower trailing edge tapered from 1.25 inch to 0 inch over a 6 inch distance. The flat plate has 44 pressure taps longitudinally distributed along the model centerline on the top surface for the measurement of streamwise pressure distribution. In order to check

图片摘要：该图主要展示 5 Schematic of a Subsonic Wind Tunnel At the University of N。
![](images/e5897682d2de16d9ed6fec049d57b224a81bcca8b66f9c5dff37e4d9b3f90a4b.jpg)  
Figure 6. Schematic of a Flat Plate with Static Pressure Taps

the nominal two-dimensionality of the turbulent boundary layer over the flat plate surface, five streamwise locations (i.e., at 10, 20, 30, 40, and 50 inches from the leading edge) on the same side of top surface have been chosen to mount a total of 40 spanwise static pressure taps which leads to eight pressure taps for each streamwise location.

# 4.4 Fiber Optic LDV System: Some Preliminary Flow Diagnostics

The measurement of slat wake interactions with airfoil boundary layers will be performed non-intrusively with an Aerometrics fiber optic, 3-component Laser Doppler Velocimeter System equipped with a high speed Aerometerics Doppler Signal Analyzer. Photographs of the LDV system with computer-controlled traverses and the experimental wind tunnel facilities are shown in Figures 7a and 7b. The state-of-the-art LDV system will be used to measure the $\mathbf{u}^{\prime}(\mathbf{x},\mathbf{y},\mathbf{t})$ and $\mathbf{v}^{\prime}(\mathbf{x},\mathbf{y},\mathbf{t})$ digital time-series required to fully characterize the confluent boundary layer. Wind tunnel seeding is performed as shown in Figure 7a with an Aerometrics Particle Generator Model APG-100 in conjunction with Propylene Glycol and water at a 1:2 ratio. This combination provides droplets with diameters nominally in the 1-4 micron range.

In order to demonstrate that the LDV system is capable of reliably characterizing the details of the flow field, preliminary flow field measurement of a canonical flat plate turbulent boundary layer was first carried out. The tunnel speed was set at 66 ft/s which corresponds to a Reynolds number of $2.26 \times 10^{6}$ based on the flat plate length. The angle-of-attack of the flat plate was set at zero incidence throughout the measurement. All velocity and turbulence intensity profiles were obtained by computer-controlled traverses normal to the flat plate surface. All data acquisition and subsequent data reduction were made by an Aerometrics Doppler Signal Analyzer.

Figure 8 compares mean velocity profiles as obtained at $x = 15, 20, 30,$ and 40 inch, respectively. The local mean velocities $U(y)$ are nondimensionalized by the free stream

(7a)

图片摘要：该图主要展示 8 compares mean velocity profiles as obtained at and 40 inch。
![](images/0a9926957be97dfa094ed04a37e4d0e9d7ece571f0e69b0bd2696c3a2f020319.jpg)

(7b)

图片摘要：该图主要展示 8 compares mean velocity profiles as obtained at and 40 inch。
![](images/e3e60ede0c827fd6969d0feff1c8ed8c2e896f0509d269fe9a075a9899f7741b.jpg)  
Figures 7a, 7b LDV System, Flow Seeding, and Wind Tunnel Facility

velocity, $\mathbf{U}_{\infty}$ , and the corresponding lateral coordinates $y$ are nondimensionalized by the local boundary layer thickness, $\delta$ . It is clearly seen from this figure that the mean velocity profiles at $x = 15$ and 20 inch are still influenced by the disturbances caused by the trip wire. At locations 30 and 40 inches from the leading edge, both mean velocity profiles show quite a similar profile, suggesting that the mean velocity has reached a state of similarity.

Figure 9 presents the corresponding turbulent intensity profiles at the same streamwise locations. It is clear that the disturbances caused by the trip wire lead to higher turbulence intensities at streamwise locations 15 and 20 inches. Both turbulence intensity profiles at locations 30 and 40 inches do show self-similar behavior as the mean quantities do.

In order to further analyze the turbulence characteristics at streamwise location $x = 30$ inch, it was desired to express the results in terms of inner wall variables. For this reason it was necessary to obtain the local skin-friction coefficient. This was accomplished by plotting mean velocity profiles from LDV measurements in a semi-log form or as a "Clauser-Chart".

Figure 10 presents the mean velocity profile at $x = 30$ inch in terms of inner wall variable scaling. The profile exhibits the familiar log law of the wall behavior in good agreement with published data.

Figure 11 compares LDV measurements of the longitudinal turbulence intensity variation through the boundary layer as obtained at $x = 30$ inch with the published hot-wire measurements of Klebanoff (1954). The agreement is observed to be excellent. These data (as well as others that are not presented) indicate that the LDV system may be used to accurately study confluent boundary layer structure in a non-intrusive manner.

# 5. Summary and Plan for Remainder of Year One

At this juncture all phases of the project are on schedule. The required high-lift models, wind tunnel test section, flow visualization instrumentation and LDV flow diagnostics have been developed such that the objectives outlined under NASA grant NAG2-905 for year one will be met. Activities for the remainder of the year will include: (1) the use of flow visualization to isolate cases of strong and weak slat wake / airfoil boundary layer confluence and its effect on integrated lift. (2) the use of the specially designed test section and fiber optic LDV flow diagnostics to study the detailed structure of the confluent layer for key cases (3) investigate the effect of relaminarization on confluent boundary layer structure. A detailed time table for these measurements as well as plans for year two will be presented and discussed at our meeting at NASA Ames on January 9, 1995.

图片摘要：该图主要展示 11 compares LDV measurements of the longitudinal turbulence 。
![](images/600e9009d09d6b6a7d87f9bf6cc393ffb07d79ba84a920eb1ebcb83203441e36.jpg)  
Figure 8 Flat Plate Boundary Layer Mean Velocity Profiles at $x = 15, 20, 30$ , and 40 inch.

图片摘要：该图主要展示 8 Flat Plate Boundary Layer Mean Velocity Profiles at , and 。
![](images/e9cc606d225c7c27ad4fac69abc00bd9fee50bf7d675c7b03c7a03871b7d55f5.jpg)  
Figure 9 Flat Plate Boundary Layer Mean Turbulence Intensity Profiles at $x = 15, 20, 30$ , and 40 inch.

图片摘要：该图主要展示 9 Flat Plate Boundary Layer Mean Turbulence Intensity Profil。
![](images/a9e25e65eab60c1aae15346a2dfd791d565bfde41519d34867b7bf1154cb0285.jpg)  
Figure 10 Boundary Layer Mean Velocity Profile at $x = 30$ inch in terms of Inner Wall Variable Scaling

图片摘要：该图主要展示 10 Boundary Layer Mean Velocity Profile at inch in terms of 。
![](images/4331ea308e0c3df69a8a67fa1d94feb8b46bd3cc48b6a3c7723fc5c91ac26208.jpg)  
Figure 11 Comparison of LDV Measurement with the Published Hot-Wire Measurement of Kelbanoff (1954)

# 6. References

Agoropoulos, D. and Squire, L.C., 1988, "Interactions Between Turbulent Wakes and Boundary Layers," AIAA Journal, 26,10, pp. 1194-1200.   
Batill, S. M. and Mueller, T. J., 1981, "Visualization of Transition Flow over an Airfoil Using the Smoke-Wire Technique", AIAA J., 19, pp. 340-345.   
Batill, S. M. and Mueller, T. J., 1982, "Experimental Studies of Separation on a Two-Dimensional Airfoil at Low Reynolds Numbers", AIAA J., 20, pp. 457-463.   
Garner, P. L., Meredith, P. T., and Stoner, R. C., 1991, "Areas for CFD Development as Illustrated by Transport Aircraft Applications," AIAA paper 91-1527.   
Klebanoff, P. S., 1954, Natl. Advisory Comm. Aeronaut. Tech. Notes No. 3178.   
Lauer, B. E. and Jones, W. P., 1969, "On the Prediction of Laminarisation," Great Britain Aeronautical Research Council, CP 1036.   
Moghadam, A., and Squire, L.C., 1989, "The Mixing of Three-Dimensional Turbulent Wakes and Boundary Layers," Aeronautical Journal, pp. 153-161.   
Sullivan, J. P., 1994, private communication.   
van Dam, C.P., Vijgen, P.M.H.W., Yip, L.P., and Potter, R.C., 1993, "Leading Edge Transition and Relaminarization Phenomena on a Subsonic High-Lift System," AIAA paper 93-3   
Zhou, M. D. and Squire, L. C., 1985, "The Interaction of a Wake with a Turbulent Boundary Layer," Aeronautical Journal, pp. 72-81.   
Zhou, M. D. and Squire, L. C., 1983, "The Interaction of a Wake with a Boundary Layer," in Structure of Complex Turbulent Shear Flow, R. Dumas and L. Fulachier, Ed., Springer-Verlag, New York.
