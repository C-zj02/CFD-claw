# Challenges and Progress in Aerodynamic Design of Hybrid Wingbody Aircraft With Embedded Engines

Meng-Sing Liou

Glenn Research Center, Cleveland, Ohio

Hyoungjin Kim

Science Applications International Corporation, Cleveland, Ohio

May-Fun Liou

Glenn Research Center, Cleveland, Ohio

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA Scientifi c and Technical Information (STI) Program plays a key part in helping NASA maintain this important role.

The NASA STI Program operates under the auspices of the Agency Chief Information Offi cer. It collects, organizes, provides for archiving, and disseminates NASA’s STI. The NASA STI Program provides access to the NASA Technical Report Server—Registered (NTRS Reg) and NASA Technical Report Server— Public (NTRS) thus providing one of the largest collections of aeronautical and space science STI in the world. Results are published in both non-NASA channels and by NASA in the NASA STI Report Series, which includes the following report types:

TECHNICAL PUBLICATION. Reports of completed research or a major signifi cant phase of research that present the results of NASA programs and include extensive data or theoretical analysis. Includes compilations of signifi cant scientifi c and technical data and information deemed to be of continuing reference value. NASA counter-part of peer-reviewed formal professional papers, but has less stringent limitations on manuscript length and extent of graphic presentations.   
TECHNICAL MEMORANDUM. Scientifi c and technical fi ndings that are preliminary or of specialized interest, e.g., “quick-release” reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.

CONTRACTOR REPORT. Scientifi c and technical fi ndings by NASA-sponsored contractors and grantees.   
CONFERENCE PUBLICATION. Collected papers from scientifi c and technical conferences, symposia, seminars, or other meetings sponsored or co-sponsored by NASA.   
SPECIAL PUBLICATION. Scientifi c, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
TECHNICAL TRANSLATION. Englishlanguage translations of foreign scientifi c and technical material pertinent to NASA’s mission.

For more information about the NASA STI program, see the following:

Access the NASA STI program home page at http://www.sti.nasa.gov   
• E-mail your question to help@sti.nasa.gov   
Fax your question to the NASA STI Information Desk at 757-864-6500   
Telephone the NASA STI Information Desk at 757-864-9658   
Write to: NASA STI Program Mail Stop 148 NASA Langley Research Center Hampton, VA 23681-2199

# Challenges and Progress in Aerodynamic Design of Hybrid Wingbody Aircraft With Embedded Engines

Meng-Sing Liou

Glenn Research Center, Cleveland, Ohio

Hyoungjin Kim

Science Applications International Corporation, Cleveland, Ohio

May-Fun Liou

Glenn Research Center, Cleveland, Ohio

National Aeronautics and

Space Administration

Glenn Research Center

Cleveland, Ohio 44135

# Acknowledgments

This work was supported Subsonic Fixed Wing Project, under the Fundamental Aeronautics Program and the Advanced Air Transport Technology project, under the Advanced Air Vehicles Program of NASA.

Level of Review: This material has been technically reviewed by technical management.

Available from

NASA STI Program

Mail Stop 148

NASA Langley Research Center

Hampton, VA 23681-2199

National Technical Information Service

5285 Port Royal Road

Springfi eld, VA 22161

703-605-6000

# Challenges and Progress in Aerodynamic Design of Hybrid Wingbody Aircraft With Embedded Engines

Meng-Sing Liou National Aeronautics and Space Administration Glenn Research Center Cleveland, Ohio 44135

Hyoungjin Kim Science Applications International Corporation Cleveland, Ohio 44135

May-Fun Liou National Aeronautics and Space Administration Glenn Research Center Cleveland, Ohio 44135

# Summary

We summarize the contributions to high-fidelity capabilities for analysis and design of hybrid wingbody (HWB) configurations considered by NASA. Specifically, we focus on the embedded propulsion concepts of the N2–B and N3–X configurations, some of the future concepts seriously investigated by the NASA Fixed Wing Project. The objective is to develop the capability to compute the integrated propulsion and airframe system realistically in geometry and accurately in flow physics. In particular, the propulsion system (including the entire engine core—compressor, combustor, and turbine stages) is vastly more difficult and costly to simulate with the same level of fidelity as the external aerodynamics. Hence, we develop an accurate modeling approach that retains important physical parameters relevant to aerodynamic and propulsion analyses for evaluating the HWB concepts. Having the analytical capabilities at our disposal, concerns and issues that were considered to be critical for the HWB concepts can now be assessed reliably and systematically; assumptions invoked by previous studies were found to have serious consequences in our study. During this task, we establish firmly that aerodynamic analysis of a HWB concept without including installation of the propulsion system is far from realistic and can be misleading. Challenges in delivering the often-cited advantages that belong to the HWB are the focus of our study and are emphasized in this report. We have attempted to address these challenges and have had successes, which are summarized here. Some can have broad implications, such as the concept of flow conditioning for reducing flow distortion and the modeling of fan stages. The design optimization capability developed for improving the aerodynamic characteristics of the baseline HWB configurations is general and can be employed for other applications. Further improvement of the N3–X configuration can be expected by expanding the design space. Finally, the support of the System Analysis and Integration Element under the NASA Fixed Wing Project has enabled the development and helped deployment of the capabilities shown in this report.

# 1.0 Introduction

The past $1 0 0 +$ years of aircraft development since the Wright brothers’ flight has essentially been confined to the tube-and-wing architecture, where the lift generation responsibility rests upon the wings. The blended wingbody (BWB) configuration, nonetheless, is not entirely new: the concept can be traced back nearly 70 years ago, as first envisioned by Northrop for a strategic bomber, the so-called flying wing YB–35 and YB–46 (Ref. 1). It is also noted that the engines, one propeller-powered and the other turbojet-powered, are mounted on the upper surface. Interestingly, the YB–46 has been replaced by a

conventional tube-and-wing design in the subsequent Convair bomber B–35. Today, a BWB aircraft is again in military service, the Stealth B–2, where the engine can be arguably considered as embedded, although the concern of economy and environment here is trumped by the need for minimizing radar detection.

However, to meet the increasing need in reducing the fuel burned and noise generated by future aircraft, NASA has laid out a progressive technological development plan for future generations of concepts, designated as $\mathrm { N } { + } i$ , $i = 1 , 2$ , ...n. For subsonic fixed-wing vehicles, the technological improvement targets relative to the Boeing 737 are given in Table I for concepts to be considered up to the 2030s.

Because of the aggressive demand for meeting NASA’s goals, “unconventional” or past concepts may be worthy of investigating or revisiting with a new perspective. NASA has sponsored a Boeing study on applying the hybrid wingbody (HWB) concept to large commercial transport in the early 1990s; it concluded that the “blended configuration was significantly lighter, had a higher lift-to-drag ratio, and had a substantially lower fuel burn” (Ref. 2), in comparison with the tube-and-wing concept. In the 2000s under the Fundamental Aeronautics Program, two concepts, shown in Figure 1, were proposed: one, designated N2–A, has two podded engines installed sufficiently away from the wingbody to minimize aerodynamic interference between them, and another, designated N2–B. In particular, the many ways to place engines on the upper surface of the vehicle provide a substantial advantage for meeting the noise reduction goal. Based on the Boeing study for both N2–A and N2–B (Ref. 3), “it is doubtful that a wing and tube can come close to meeting $_ { \mathrm { N } + 2 }$ goals of a cum –52 dB noise with a $- 2 5$ percent fuel burn.” At the closure of a NASA-contract study in 2011, Boeing concluded that $_ { \mathrm { N } + 2 }$ goals could be met with a modified N2–A configuration called N2A–EXTE by increasing shielding of noise—by moving nacelles forward and extending the trailing edge; the results are given in Figure 2.

However, the installation of the propulsion system presents significant challenges resulting from embedding the propulsion system into the HWB airframe. As a result, the aerodynamic performance can be severely degraded, and the ingested boundary layer leads to increased flow distortion inside the inlet and increased structural load on the fan. We believe that a new design approach should be taken to analyze the embedded-propulsion concept as it is no longer proper to treat HWB and nacelle aerodynamics separately in the design process. During this task under the Fixed Wing Project, we have focused only on the embedded engine configurations initially the N2–B, in which the propulsor is the conventional turbofan engine, and later the N3–X, where an array of fans drive by electric motors is the propulsor.

In this report, we document the development and applications of computational capabilities for carrying out aeropropulsion analysis for HWB configurations and their redesign via optimization. The computational code, named “GO” (Glenn optimization), consists of two parts: (1) a computational fluid dynamics (CFD) capability necessary for treating as one entity the entire integrated wingbody-propulsion system, and (2) an optimization capability to seek a new, optimized configuration. These two capabilities are also respectively called GO-flow and GO-opt to signify its usage. The aerodynamic performance characteristics of N2–B and N3–X are described separately with their unique features included in the analysis. Optimization of components, especially the nacelle profile, has been attempted to minimize the degradation caused by installation. Finally, we present lessons learned and a future plan for technology development with regards to the embedded propulsion system in general. To aid the reader, acronyms and symbols used in this report are listed in the appendix.

#

GO-flow is a state-of-the-art CFD code and is continually being enhanced and employed to meet task requirements. It is a three-dimensional (3D) unstructured-grid unsteady Reynolds-averaged Navier-Stokes code. The turbulence model used is the two-equation κ-ω shear stress transport model (Ref. 4). The governing equations are time discretized by a second-order-accurate implicit scheme; the numerical schemes for inviscid fluxes include HLLEW (Ref. 5) and AUSM+ -up (Ref. 6), and the viscous terms are

approximated by the standard central differencing. To obtain second-order spatial accuracy with monotone profiles and ensure stability, the usual MUSCL procedure is adopted. The resulting discrete system is then solved by the LU–SGS scheme (Ref. 7). The meshes accepted are of tetrahedra and prism types of polyhedra. Parallel computing was accomplished by domain decomposition of the computational mesh and the Message-Passing Interface. The code has been validated and used to compute a variety of external and internal flows throughout the development. Some validations for problems relevant to the present HWB task have been carried out and are included in this report.

To model the turbomachinery flow, a CFD code written in rotating framework is most appropriate, and we use the well-accepted SWIFT code by Chima (Ref. 8). The SWIFT code is a 3D, multiblock, structured-grid Navier-Stokes analysis code for turbomachinery blade rows. The code solves the Navier-Stokes equations on body-fitted structured grids. The $\mathrm { \ A U S M ^ { + } }$ scheme (Ref. 6) was used for spatial discretization of the inviscid flux. For the thin-layer approximation, viscous terms were included in the blade-to-blade and hub-to-tip directions and were neglected in the streamwise direction. For turbulence effects, Wilcox’s κ-ω model with a stress limiter was selected (Ref. 9). The discretized equations were solved with a multistage Runge-Kutta scheme with local time stepping and residual smoothing to accelerate convergence.

For the “clean” (i.e., wingbody alone) HWB calculations, we also engaged the popular structured overset grid code, OVERFLOW (Ref. 10). It is used primarily as a validation for cross-checking GO-flow solutions, especially the aerodynamic forces.

# 3.0 Optimization Framework

The optimization framework in GO is based on the adjoint formulation in which the objective function is minimized or maximized by knowing the gradient or sensitivity of flow variables with respect to the design variables, such as the geometrical representation of the nacelle. The adjoint formulation is attractive for its efficiency because, by virtue of imposing the condition of satisfying the flow equations, it allows the calculation of the sensitivity matrix essentially independent of the number of design variables. The adjoint solver uses the GMRES method (Ref. 11) for the time integration with LU–SGS as a preconditioner. Mathematical details about the derivation of the sensitivity matrix and the performance of the specific algorithm for numerically obtaining the matrix values can be found in Reference 12.

# 4.0 Technical Challenges in Aerodynamics of HWB

The benefits of a HWB configuration stated in previous studies were derived based on simplified models (e.g., clean configurations) or system-level studies. A true figure of merit of an integrated configuration is yet to be confirmed, computationally or experimentally. Much of the effort for optimization has been spent on dealing with the clean wing only. Quantitative evaluations of the influence of the propulsive system are few. A distinct configuration that can potentially make use of the full benefits of the HWB concept is the embedding of the propulsion system into the body. Because of this tight geometric association, a separate analysis of the “body” alone would be far from realistic. Instead, we have taken the approach of treating the entire aerodynamic and propulsion generating systems as one entity from the outset. As a result, it is no longer feasible to talk about nacelle drag or airframe drag individually as though they were identifiable separately and superimposable, because a metric of one is influenced by the existence of the other. We also envisioned that the following technical challenges, essential or unique to the HWB aircraft, must be properly quantified; these include (1) ingestion of the boundary layer into the inlet, (2) inlet-fan flow interactions, and (3) nozzle-airframe flow interactions. These entail detailed understanding of the complex flow physics involved. Hence, these topics are a major part of our study and they are described in detail below.

# 4.1 Distortion Generation and Total Pressure Loss in Boundary-Layer-Ingestion (BLI) Inlet

As revealed in Figure 1, the engines are located aft, and the flow into each nacelle will have incurred a relatively thick boundary layer (potentially as large as 30 percent of the inlet height) with a significant deficiency in momentum. This can be considered to be a good thing because it increases the engine’s propulsive efficiency (Refs. 2 and 13) because of the reduction of inlet velocity, but on the contrary, it creates a problematic nonuniform flow, which is known to increase distortion and simultaneously decrease recovery of total pressure at the face of the fan or compressor (Refs. 14 and 15). The latter can result in a decrease in structural operability of the fan or compressor and loss of engine efficiency.

Experimental studies have been conducted at the NASA Langley Research Center to quantify the performance of a flash-mounted S-duct inlet, as shown in Figure 3, with large amounts of BLI into several inlets of different geometrical parameters (Ref. 14). Various flow-control concepts have been tested, notably by installation of arrays of vortex generators (VGs) or bleeding of boundary-layer flow near the throat (Ref. 15). Unfortunately, these approaches can succeed in reducing distortion, but at the expense of total pressure recovery (see, for example, Ref. 15).

Clearly, from the results shown in Figure 4 it does not seem possible to reduce distortion and total pressure loss simultaneously by using the above conventional inlet flow control concepts. Hence, efforts were devoted to finding an alternative concept, with preference to passive flow control for its simplicity and no need of sensor and actuator mechanisms. We also strongly believe it is rather late to do any flow remedies once the thick boundary-layer flow has been ingested into the inlet, and it is much more beneficial to treat (condition) the flow prior to entering the inlet. We employed the adjoint method to reshape the bottom wall geometry. Remarkable results were obtained (Refs. 16 and 17); some are summarized in Figures 5 to 7. It is found that the distortion is reduced drastically from the baseline, and simultaneously, the total pressure loss is minimal. Moreover, this performance gain is maintained over the entire operation conditions as expressed in terms of the mass flow rate. This demonstrated that the concern about negative impacts of a thick boundary layer ingested into a realistic inlet can be successfully resolved.

Figure 5 displays the “oil flow” patterns of both designs; the original design gives rise to a significant “push” of streamlines from sidewalls because of low-momentum-fluid blockage, whereas the streamlines in the optimal design essentially follow the contours of the inlet, producing much less blockage and an increased mass flow rate. This is achieved by altering the bottom wall shape, manifested by the blue and red regions, which begin well ahead of the inlet entrance and end in about the same distance into the inlet, with red color indicating elevation from the baseline shape and blue denoting depression. This result differs from the conventional flow control concept that exclusively focuses on making treatments inside the inlet and after the throat or near the curved part of the “S” duct; here, we emphasize the idea of conditioning the flow before it enters the inlet. It is interesting to note that these geometry alterations are rather regularly placed, although not equally distanced, and the spanwise variations are also observed.

Because of this change in the bottom wall shape, the flow maintains its well-behaved characteristics, as displayed in Figure 6. Comparison is presented of Mach number contours and superimposed cross flow streamlines at various inlet locations for flows of two pressure ratios (static back to total inflow) $P _ { b } / P _ { t 0 } = 0 . 8 1 3 7$ (design condition) and 0.8417. For each condition, results of the baseline geometry are shown on the left column, and that of the optimized inlet are on the right column. The low-momentum region, coinciding with the low-total-pressure region in this case, has been reduced, and its growth dampened significantly by the treatment of wall shaping. This has a very interesting implication: although the optimization is conducted to minimize the distortion, the losses in the flow’s kinetic energy, as manifested by Mach number, are also reduced. This complementary benefit might not be realizable when external devices, such as VGs, bleeding, pulsed jet, plasma, and so forth, are deployed to control distortion (see Ref. 18 for example).

To further appreciate the benefit of the present wall shaping, we focus on the secondary flow pattern, also displayed in Figure 6, by particle traces constructed by the y-z velocity components as a representation of secondary flow. Both designs give completely different flow topologies. As expected in the baseline design, the familiar conventional secondary counter-rotating vortical pairs are found near the symmetry plane; their cores are being lifted off of the low-momentum region and growing toward the downstream aerodynamic interface plane (AIP) at the streamwise location $x / D = 3 . 0$ . The optimized design, however, gives no evidence of this side-by-side pair near the symmetry line $( \boldsymbol { y } = \boldsymbol { 0 } )$ .

Figure 7 shows that the optimized design has for all conditions much smaller distortion values, 50 to 70 percent less, than the baseline design. Also, notice that at the pressure ratio $P _ { b } / P _ { t 0 } = 0 . 9 3 5 3$ , the baseline model is stalled (characterized by rapid loss of mass flux and large flow separation), but the optimized design is not. Concerning the total pressure recovery, the baseline model shows a greater dependence on the mass flux ratio, and the optimized model maintains a relatively constant value of 99 percent for all conditions. This suggests that the concept of distortion minimization by wall contouring is robust, because the performance remains high for all operating conditions.

# 4.2 Inlet-Fan Interaction

There has been an underlying concern about the validity of the conventional approach in inlet flow simulations in which the exit flow condition is typically assumed to be a uniform pressure profile, or at best a specified one, without regard to the presence of a fan or compressor. This assumption is taken mostly for simplicity; otherwise, a complicated procedure of including the fan flow solution would be necessary and problematic. However, for the N2–B and N3–X concepts, the generation of thrust relies on the inlet-fan-nozzle configuration. It is thus important to have a realistic account of the fan influencing the inlet flow, but without taxing excessive computational resources. Hence, a model representing the fan effects by virtue of a body force representation at the location of the fan is developed for this study (Ref. 19). The body force components in algebraic form can be easily and cheaply calculated and added appropriately to the Navier-Stokes equations.

The body force model used for this study is based on the model developed by Gong (Ref. 20), assuming an infinite number of blades in an axisymmetric flow. The cascade blade forces, in the relative frame of reference, are decomposed into normal and tangential components $F _ { n }$ and $F _ { p } ,$ respectively, to the local flow vector $V _ { \mathrm { r e l } , }$ which comprises the normal and tangential components $V _ { n }$ and $V _ { p }$ relative to the blade surface as shown in Figure 8.

For the normal component, Gong proposed the formula

$$
F _ {n} = \frac {K _ {n}}{h} V _ {n} V _ {p} + \frac {2}{c} \sin \left(\frac {\Delta \alpha}{2}\right) V _ {n} ^ {2} \quad \Delta \alpha = \alpha_ {\mathrm {T E}} - \alpha_ {\mathrm {L E}} \tag {1}
$$

where $K _ { n }$ is the normal force coefficient, which can be specified with empirical data or CFD results; $h$ is the blade-to-blade gap-staggered spacing; $c$ the blade’s chord length; and $\Delta \alpha$ is the difference in blade angles between the trailing edge (TE) and leading edge (LE) with respect to the x-axis. In our study, Gong’s form is generalized by

$$
K _ {n} = (4. 2 - 3. 3 \alpha) \mathrm {f} (r) \mathrm {g} (\dot {m} _ {\text {l o c a l}}) \tag {2}
$$

where the radial profile function $\operatorname { f } ( r )$ and the mass-flow-rate-adjusting function $\mathrm { g } \big ( \dot { m } _ { \mathrm { l o c a l } } \big )$ are numerically determined through an iterative process to account for the geometrical and physical effects, by using Chima’s 3D high-fidelity turbomachinery code, SWIFT (Ref. 8). Their profiles are schematically represented in Figure 9.

For the tangential force component, which represents a dissipative mechanism, we follow the formulation by Chima (Ref. 21) by relating it to the entropy variation $\Delta s$ as

$$
F _ {p} = - T \frac {V _ {m}}{V _ {\mathrm {r e l}}} \frac {\partial s}{\partial m}, \quad \frac {\partial s}{\partial m} \approx \frac {\Delta s}{x _ {\mathrm {T E}} - x _ {\mathrm {L E}}} \tag {3}
$$

where $T$ is the temperature, m is the meridional coordinate, and $V _ { m }$ is the meridional component of the velocity; the entropy variation may be related to total pressure $( P _ { t } )$ variation by

$$
\frac {\Delta s}{R} = \frac {\gamma}{\gamma - 1} \ln \left(\frac {T _ {t 2}}{T _ {t 1}}\right) - \ln \left(\frac {P _ {t 2}}{P _ {t 1}}\right) \tag {4}
$$

where $R$ is the gas constant, γ is the specific heat ratio, and stations 1 and 2 refer to the entrance and exit of a fan blade row, respectively.

Alternatively, a CFD-based model for Δs can be constructed in terms of mass flow rate (MFR), as is determined from the solution by the SWIFT code in this study. It is interesting to note in Figure 10 that the entropy decreases as the MFR increases from the near stall to the choke conditions when at low rotating speed, but the trend reverses after a certain MFR on the high-speed lines. These unusual characteristics must also be observed in the model to be built.

To validate the body force modeling, a realistic machine, the R4 fan stage designed by the General Electric Aircraft Engines Company, is chosen. A one-fifth-scale model was tested at the NASA Glenn Research Center. The fan has a 22-in. diameter and 22 wide-chord rotor blades. A sectional side view and a 3D perspective of the nacelle are shown in Figure 11.

Based on the body force model, Figure 12(a) confirms that the Euler solution of the fan rotor pressure ratio versus the corrected mass flow rate at 85 percent of the design rotor speed agrees well with the test data in Reference 22 and the results of the SWIFT code. Figure 12(b) shows that the entropy production calculated by the Euler $^ +$ body force model also matches the test data well, faithfully resolving the reversal of entropy production at approximately $4 2 \mathrm { k g / s }$ , corresponding to the peak-efficiency MFR. After this, the entropy production is proportional to the MFR because the incidence angle of the blade section deviates from the minimum loss angle.

# 4.3 Nozzle-Airframe Integration

As the flow exits the nozzle, a process mirroring the inlet flow, complicated interactions between the nozzle and the external airframe flow occur. As indicated in Section 5.1, Baseline Configuration, the flow separates on a massive scale, suggesting that much effort is needed here to clean up the flow and simultaneously optimize an aerodynamic metric of concern (e.g., thrust, noise, etc.). This is the area on which we will need to focus in the future, and it is of special importance for the N3–X configuration, for which the balance of thrust-generation and aerodynamic interference between the nozzle exhaust and external flows must be carefully executed. Moreover, as thrust vectoring and reversing are to be used in N2–B and N3–X, it is important to have a complete assessment of flow characteristics and performance for various nozzle openings, as sketched in Figure 13.

# 5.0 Aerodynamic Analysis and Design for N2–B

# 5.1 Baseline Configuration

The Boeing Company was contracted by NASA to study hybrid wingbody configuration, starting from the “silent aircraft” SAX–40 (Ref. 23), and produce two configurations, as shown in Figure 1: one, designated N2–A, has twin podded engines installed between two vertical tails to shield lateral

propagation of engine noise, and the other, denoted N2–B, has BLI embedded propulsion systems. Winglets are employed in N2–B to serve as verticals for direction control. Both are specified to cruise at 35 000 ft with Mach number of 0.8 and to have a range of 60 000 nmi with a payload of 103 000 lb. The N2–B is reported to have a better aerodynamic performance than N2–A, but it has a new set of technical challenges, as indicated earlier, and attendant risks.

To set the baseline, we first show the representative aerodynamic characteristics of the “clean” body only, without a propulsion system. Substantial effort has been spent by Boeing to achieve high aerodynamic performance, especially relative to the conventional configuration, as shown in Figure 14.

Anticipating that inlets are to be placed in the rear of the vehicle and boundary layers are ingested into the embedded inlets, the development of a boundary layer along the vehicle’s upper surface is an important factor to consider. Figure 15 shows how the flow decelerates and the boundary layer grows and thickens, manifested by the Mach number and total pressure profiles on the symmetry plane.

The N2–B configuration has three propulsion units, each housing a core turbofan engine together with two side fans individually housed in separate flow paths, as shown in Figure 16. The engine and fan specifications are given in Table II. It is noted that with the two side fans, the effective bypass pressure ratio (BPR) is maintained at over 11.

In order to have a realistic representation of the engine components without incurring prohibitive computational efforts, which will be required for considering numerous scenarios and optimization, we opt to use a system-level engine model—NPSS (Numerical Propulsion System Simulation, Ref. 25). As depicted in Figure 17(a), the core engine block is now replaced by the NPSS model by knowing the flow conditions at the AIP calculated by the high-fidelity RANS code, GO-flow, and returning flow states at the end of turbine stages, illustrated in Figure 17(b). Furthermore, to streamline the coupling of the highfidelity RANS and the NPSS solutions, we implemented a surrogate model of the NPSS solution in the RANS code. The only requirement of this surrogate model is a true representation of the NPSS solution over the entire range of parameters considered.

The NPSS solution provides mass flow rate ݉ሶ , total pressure $P _ { t }$ , and total temperature $T _ { t }$ at the nozzle exit of each flow passage to the CFD model, while taking as an input the total pressure recoveries $\eta$ at the fan faces. After a sensitivity study of the NPSS results for the current engine configuration, shown in Figure 16, the following surrogate model is derived (see Ref. 26 for details):

$$
\dot {m} _ {i} = f _ {m} \left(\eta_ {i}\right), T _ {t i} = (\text {c o n s t a n t}) _ {i}, i = 1, 2, 3
$$

$$
P _ {t i} = f _ {p i} \left(\eta_ {i}\right), i = 1, 2, 3 \tag {5}
$$

$$
f _ {p 2} = f _ {p 3}
$$

where subscript “1” denotes the center passage, while $^ { \mathfrak { c } \mathfrak { c } } 2 ^ { \mathfrak { s } \mathfrak { s } }$ and “3” refer to side ones. These results suggest that

(1) ݉ሶ and $P _ { t }$ are affected only by the recovery η of its own passage.   
(2) $T _ { t }$ remains essentially unaffected the recovery η.   
(3) Functions $P _ { t }$ and $T _ { t }$ for the central passage are not sensitive to the change of the recoveries in side passages, even though arguably they should be affected because the turbine work of the core engine to drive side fans is affected by MFRs of the side passages, which depend on the recovery values.   
(4) Each passage is essentially independent from the neighboring passage insofar as the engine modeling is concerned.

This surrogate model has several appealing features: (1) the function relationships are quite revealing for providing a physical relationship between input and output, (2) they are extremely simple

(surprisingly linear) and accurate, as displayed in Figure 18 where the data points are the exact value from NPSS and the lines are the model predictions, and (3) they can be directly implemented and coupled into the CFD code, completely removing the need for calling the NPSS code.

Based on the CFD procedure described above, we carried out aerodynamic computation of the integrated configuration of N2–B. Figure 19 shows the lift coefficients at different angles of attack (AOAs), clearly revealing that the inclusion of engine installation results in a significant degradation in lift. It is noted that the clean-wing values are comparable to those given in the Boeing study (Ref. 2).

The detailed surface pressure distributions along representative spanwise cross sections are presented in Figure 20 to elucidate how much and how wide the influence of the installed nacelles is on the cleanwing performance. The nacelles act as a porous obstacle, forcing the flow accelerating over the top and side surfaces, but also through the inlet. It is important to note in Figure 21 that (1) the upstream effect is felt significantly ahead of the nacelle entrance, more than 20 percent of the body length corresponding to the nacelle locations, as evident by the pressure deviation; (2) when not directly in front of nacelles the pressure is also altered noticeably; for example, at $y = 0 . 3$ and 0.5; (3) the displacement of fluid is felt spanwise, as far as 50 percent of the span $( \gamma = 0 . 5 )$ ; and (4) the underbody flow field is not entirely free (shielded) from the disturbance of engine exhaust (recalling that some flow has entered through the (modeled) engine and exited with “hot” conditions to meet with the “cold” flow).

The results with the presence of nacelles are (1) the creation of supersonic pockets on the top nacelle surfaces and (2) flow separations around and inside the nacelles. Figures 21(a) and (c) indicate that flow over the upper surface accelerates around the outer surface of the cowl lip to a speed higher than Mach 1.15, and it is terminated with a shock-induced boundary-layer separation. Figures 21(b) and (d) show the envelop of a reversed flow region with velocity $u < - 0 . 0 1$ . Many separation bubbles are seen around the nacelle, inside the inlet ducts, on the nacelle upper surfaces, and at the nacelle base regions. The side nacelle, however, sees a massively separated flow region. As a result of shock wave and boundary-layer interactions, flow separates on the upper surface of the center nacelle, manifested by the thickening of the boundary layer downstream of the shock foot. It is noted that there is a big difference in surface slopes in front of the offset inlet at the symmetric plane and the center plane of the outer inlet. At the symmetry plane, the flow aligns well with the outer surface of the nacelle. At the center plane of the outer inlet, however, the nacelle cowl angle has a large incidence angle relative to the incoming flow along the upper surface. This relative AOA at the cowl lip causes the leading edge separation on the upper surface. This is due to the fact that the location $( x / c ,$ , relative to the sectional chord length) of the inlet entrance is about 77 percent for the symmetric plane and 61 percent for the side inlet. The difference of local $x / c$ means a difference in local slopes of airfoil surfaces. Since a HWB aircraft tends to have a large variation in sectional chord length, the cowl lip angles of embedded engine nacelles must be designed to align with local inflow directions.

Figure 22 depicts further details of flow patterns on the surface with the particle path and “oil flow” rendition, superimposed with colored static pressure contours. Many separation bubbles are present around the nacelle: inside and near entrance of inlets, on the cowl surfaces, and nacelle base regions, shown in close-up view in Figures 22(b) and (c). Streamlines flowing into the engine faces are visualized in Figure 22(a); sideslip (yaw) angles are generated at the outboard inlet, owing to the sweep of the wingbody configuration. This yaw angle to the inlet axis explains the asymmetry of the separation bubble on the cowl surface of the outboard inlet, as seen in Figure 22(b).

Clearly, the intended well-behaved flow pattern created during the clean-wing design is totally spoiled by the presence of engines nacelles, which of course are necessary for the aircraft to fly. Hence, it is necessary to go inside the flow path to investigate how the flow behaves there and how the ingested boundary layer causes distortion that could be tolerated by the fan-blade structure. This issue has been discussed previously as a simplified unit problem in Section 4.1, only this time the discussion is presented with a realistic configuration. First, we compare boundary-layer thicknesses of the N2–B and clean-wing configurations in Figure 23. The boundary-layer thickness in the figure is defined as the contour line of 99 percent total pressure relative to the freestream total pressure. A quantitative comparison of the boundary-layer thicknesses growth is seen, showing that the boundary layer is thickened because of the

obstruction (thus resulting in an adverse pressure gradient) to 0.52 of the throat height $( H )$ from $0 . 4 3 H$ at the symmetry plane for the N2–B, and to $0 . 2 1 H$ from $0 . 1 9 H$ for the outer inlet for the clean wing.

Next, we show total pressure contours inside the S-inlets along various streamwise sections in Figure 24, revealing the evolution of boundary layers in each of these passages. The side inlet has a clear asymmetry in the contours between AIP1 and AIP3, stemming from a sideslip flow entering the inlet shown previously in Figure 22(a).

In Figure 25, recoveries of the side inlet obtained for clean wing and N2–B are compared, where AIP1 is the outmost fan face, and AIP5 is the center fan face. The estimated recoveries (cited in Ref. 24) by Boeing are based on the clean-wing analyses and are seen to be in excellent agreement with the results that take into account the effect of nacelles. It is noted that the recoveries for the center inlet (AIP4 and AIP5) are about a couple of percent lower than the side inlet recoveries, as shown in Figure 25, because of the thicker boundary layer entering the center inlet.

# 5.2 Optimal Design of Nacelle Shape

The optimal shape design in this study is conducted in two separate considerations: one is to minimize the total drag, and the other is to minimize the flow distortion in the inlet. The first consideration aims primarily to improve the external flow characteristics of the integrated airframenacelle by reducing flow separations and shock wave strengths. Hence, the second consideration focuses exclusively on the internal flow and will be based on the newly optimized geometry by assuming little effect on the external flow by the change of the internal geometry. Hereafter, the results of the drag minimization and distortion minimization will be referred to as Design 1 and Design 2, respectively.

First, we describe the overall design procedure, as outlined in Figure 26. We begin by obtaining a baseline flow analysis for the current design configuration. Then an adjoint sensitivity analysis is performed based on the flow analysis results to determine a search direction. A step size along the search direction is selected by a line search method with the slope along the search direction. In the present study, a quadratic polynomial fitting is used for the line search. Then design variables are updated using the gradient information and step size. The design geometry is then modified via a geometry parameterization in our approach, and volume meshes are modified accordingly using the torsion spring analogy (Ref. 27). This loop is repeated until the design converges. For a gradient-based optimizer of the present unconstrained minimization problem, the conjugate gradient method (Ref. 28) is employed.

# 5.2.1 Design 1: Drag Minimization

The design objective is to minimize a drag function expressed below at a fixed flight condition by shaping the nacelle geometry. The objective function is defined as follows:

$$
F = C _ {D} + \frac {\partial C _ {D}}{\partial C _ {L}} \Bigg | _ {C _ {L _ {0}}} \left(C _ {L _ {0}} - C _ {L}\right) + \sum_ {i = 1} ^ {N _ {\mathrm {A I P}}} \frac {\partial C _ {T}}{\partial \eta_ {i}} \left(\eta_ {i _ {0}} - \eta_ {i}\right) \tag {6}
$$

where $C _ { D }$ is the drag coefficient calculated by surface integration of pressure and skin friction forces on wetted surfaces and $C _ { L }$ is the lift coefficient. The second term on the right-hand side is a penalty term that prevents the design from reducing the drag by simply reducing the lift force. The third term is included because a reduction in thrust due to a total pressure loss in the propulsion system amounts to a drag increase. The thrust coefficient $C _ { T }$ is calculated by surface integration of pressure forces and momentum fluxes in the fan and engine exhaust planes.

The gradient $\partial C _ { D } / \partial C _ { L }$ can be calculated by a sensitivity analysis or a finite differencing by a perturbation in AOA. A simple approximate way is to use the quadratic relation between $C _ { L }$ and $C _ { D }$ as follows (Ref. 29):

$$
C _ {D} = C _ {D _ {0}} + K C _ {L} ^ {2} \tag {7}
$$

from which $\left. \frac { \partial C _ { D } } { \partial C _ { L } } \right| _ { C _ { L _ { 0 } } } = 2 K C _ { L _ { 0 } }$ L CC L , where $K = 1 / \pi A R$ and $A R$ is the aspect ratio of the clean HWB.

In the third term, $N _ { \mathrm { A I P } }$ is the number of AIPs of the configuration, $\boldsymbol { \mathsf { \Pi } } \mathfrak { \mathsf { \Pi } } ^ { \mathsf { \Pi } }$ is the total pressure recovery at fan face $i ,$ and $C _ { T }$ is the engine thrust coefficient, which is nondimensionalized by the free-stream dynamic pressure and reference area in the same way as the lift and drag coefficients. The $\partial C _ { T } / \partial \mathfrak { n } _ { i }$ terms are calculated using the NPSS engine model by a finite difference approximation. At the design flow condition with full powered engines, $\hat { \sigma } C _ { T } / \hat { \sigma } \boldsymbol { \eta } = 0 . 6 0 { \times } 1 0 ^ { - 2 }$ for the central AIP and $0 . 3 9 \times 1 0 ^ { - 2 }$ for the side AIPs of the tri-fan engine, which means a 1 percent change in recovery at an AIP results in roughly a half $( 0 . 3 9 { \sim } 0 . 6 0 )$ count variation in thrust force.

The cowl surfaces and diffuser surfaces are designed with 164 parameters: 80 for outer cowl surfaces, 80 for diffuser surfaces, and 4 for cowl lip shape deformation.

# 5.2.2 Design 2: Distortion Minimization

The result of the drag minimization is used as a baseline configuration to minimize the distortion at the same design condition as before. The objective function is the sum of the circumferential distortion indicator $\mathrm { D P C P _ { a v g } }$ at the three AIPs of the side inlet (AIP1, AIP2, and AIP3):

$$
F = \sum_ {i = 1} ^ {3} \mathrm {D P C P} _ {\text {a v g A I P} _ {i}} \tag {8}
$$

The distortion minimization is to be accomplished by changing the diffuser surfaces that are parameterized in terms of control points. The total number of design parameters is 52 for the side inlet only, and the center inlet is not changed in the current study. The amount of geometric variation is restricted to be less than 10 percent of the fan diameter.

For a geometry design, it is important to pay attention to the accuracy and efficiency aspects of describing the geometry surface. It is most efficie7nt to represent the geometry by piecewise polynomials to deal with smooth surfaces with specified discontinuities. In this study we use the NURBS (Non-Uniform Rational B-Spline) function (Ref. 30), an industry standard for a free-form shape representation in computer-aided design (CAD).

In Design 1, $C _ { D }$ was reduced by 45 counts, and $C _ { L }$ was increased from 0.167 to 0.193, which is still lower than the clean wing $C _ { L }$ of 0.237. Further increase in $C _ { L }$ can be expected if the whole topology of the engine nacelle including the base region is changed in the shape design. Figure 27 compares separation bubbles of the baseline design and Design 1. Most separation bubbles are removed from the cowl surfaces by Design 1. However, a new separation bubble appears on the right-hand side of the side nacelle of Design 1, due to an increased yaw angle in the incoming flow. Rear and side views of the separation bubbles in Figure 27 clearly show the change of separation bubble patterns before and after the design.

Local Mach number contours are compared for the baseline and Design 1 in Figure 28. The design shape has a larger cowl lip radius and thicker cowl than the initial shape. In the symmetric plane, flow is less accelerated along the cowl leading edge on the upper surface, and the shock strength is much weakened on the cowl. For the side inlet, the separation bubble is eliminated and flow is more accelerated on the cowl surface as the local flow angle is more aligned with the cowl design. The cowl section shapes of baseline and Design 1 are directly compared in Figure 29 for two spanwise sections.

A comparison of sectional total pressure contours inside the inlets of Design 1 and Design 2 is shown in Figure 30. Noticeably, the low recovery region in AIP1 in Design 2 is smeared out and broken into two distinct regions, and the total pressure recovery is increased. In the passage of AIP3, the concentration of low recovery is lessened, especially in section $x = 0 . 7 4 0$ .

Figure 31 compares distortion indicators of the baseline, Design 1, and Design 2 configurations. Although Design 1 has reduced the drag force remarkably, it has also increased distortion. By minimizing distortion, the objective function (the sum of $\mathrm { D P C P _ { a v g } }$ in AIP1, AIP2, and AIP3) of Design 2 is reduced by 12 percent compared to that of Design 1. The most improvement comes from AIP1, where $\mathrm { D P C P _ { a v g } }$ is reduced by 23.9 percent. AIP4 and AIP5 have no changes in distortion indicator by Design 2 because the distortion design is limited to the side inlet only in the present study. Also shown in Figure 31, Design 1 resulted in slightly reduced recovery values from the initial N2–B configuration for all five AIPs. In Design 2, the recovery is significantly reduced in AIP1, slightly increased in AIP2, and unchanged in AIP3; again AIP4 and AIP5 do not see changes.

From this study, we again see that shaping the diffuser wall only inside the inlet, as done in Design 2, can reduce the distortion, but at the expense of pressure recovery. This substantiates the earlier conclusion reached in Section 4.0 that the flow must be conditioned before entering the inlet, implying that the upper surface of the N2–B must be designed upstream of the nacelle to modulate the flow.

Figure 32 compares the lift coefficients of the clean wing, initial N2–B, Design 1, and Design 2 configurations. As mentioned earlier, the initial N2–B gives rise to a much lower lift force than the clean wing at the same AOA, and Design 1 has recovered a significant portion of the lost lift force by drag minimization. The lift of Design 2, which focuses on improving internal flow behavior, shows little difference from that of Design 1, as expected.

Comparison of distributions of pressure coefficients $C p$ at selected constant-y sections for the initial N2–B and design configurations is shown in Figure 33, along with the result of the clean wing to illustrate the considerable influence of nacelle installation.

# 6.0 Aerodynamic Analysis and Design for N3–X

The N3–X was proposed as a candidate to meet the $_ { \mathrm { N } + 3 }$ goals (Ref. 31). The N3–X is a 300- passenger HWB aircraft employing turboelectric distributed propulsion (TeDP), which utilizes superconducting electric generators, motors, and transmission lines (see Fig. 34(a)). The TeDP system allows power generation and thrust generation to be separated and enables a small number of turboshaft engines to drive tens of propulsors, each of which is composed of an electric motor and a fan. The N3–X was designed to have two large turboshaft engines at each wing tip. In addition, BLI propulsors are distributed in a mail-slot-like nacelle on the upper surface of N3–X near its trailing edge. A sectional view of an electric-motor-driven propulsor is depicted in Figure 34(b). According to the system study in Reference 31, the N3–X is expected to reduce the mission fuel burn by more than 70 percent relative to the reference aircraft, Boeing B777–200LR, flying 7500 nmi with a cruise of Mach 0.84 and a 118 100-lb payload.

It is noted that the airframe of N3–X is a smoothed N2–A (or N2–B with its winglets bent, flattened). Thus, the differences between N2 and N3–X lie in the propulsors employed and the missions defined. Since the nacelle geometry and propulsor passages for N3–X were not available, here we describe a baseline design of the nacelle geometry based on the parameters defined in the engine system analysis. The overall size and performance specifications of the propulsor fan and nacelle were interpolated from the data in Table 5 of Reference 31 for 16 fans: fan diameter $= 4 0 . 2 5$ in., corrected $\mathrm { M F R } = 3 3 2 . 5 1 \mathrm { b / s }$ , pressure ratio $= 1 . 3 2 5$ , and corrected rotor speed $= 5 3 2 9 . 5 7 5 \mathrm { r p m }$ . The width and height of inlet entrance are 45.2 and 24.35 in., respectively. The mass-averaged total pressure ratio and Mach number at inlet entrance were used to calculate the MFR per each flow passage. For sizing of the nozzle exit section, the nozzle width was kept the same as the inlet width and the nozzle exit height was determined using the MFR and flow choking condition at the nozzle exit plane. The internal hub and shroud geometries of the fan section were scaled up by the ratio 40.25/22 from the R4 fan stage. The bottom surface of the S-duct

in each flow passage was defined by a cubic spline and requiring smooth transitions from a rectangular inlet, to a circular fan section, and back to a rectangular nozzle exit. The inlet cowl leading edge is aligned with the upper surface of the clean airframe in order to have a zero local flow incidence angle.

# 6.1 Geometry Description by Parameterization

As in N2–B, we anticipate a redesign of the baseline configuration after the initial evaluation of the N3–X aerodynamic performance. Here, the same CAD-free shape parameterization approach described previously is employed to efficiently generate and modify the complex mail-slot nacelle geometry. The entire mail-slot nacelle geometry is defined by the outer cowl and the inner flow passages divided by walls. Each passage is composed of an S-shape inlet and a nozzle, connected by a cylindrical duct, and a fairing center body that houses an electrical motor and holds fan blades, as shown in Figure 35, which depicts a half model of a mail-slot nacelle housing 16 fans and their internal flow passages. The S-duct serves as a diffuser, transitioning from a rectangular to circular cross section. The nozzle, however, transitions from a circular to rectangular shape.

The mail-slot propulsor is built up by 206 surface patches. Each surface patch has a structured plot3D (Ref. 32) data format. The neighboring patches are precisely joined so that they share the same nodes; as a result they are ensured to be “water tight” and ready for unstructured surface grid generation. Figure 36 shows some relevant parameters used to define the mail-slot propulsor geometry. Other parameters such as sectional areas are also needed; any new parameters can be readily added if necessary. In the present study, the nacelle is installed at 85 percent chord position on the symmetry plane of the airframe. The streamwise location of the nacelle is also an adjustable design variable for optimization. The nacelle cowl follows the spanwise variation of the wing upper surface, with the cowl lips twisted down in the outboard direction according to local slopes of the inlet leading edge on the wing surface. The HWB airframe can be parameterized independently from the propulsor, and then both are combined to build the full integrated configuration. The geometry definition code will be used later in optimal shape-design studies for distributed propulsion systems with a mail-slot nacelle. It is noted that the geometry handling (merging and removing of two objects) can be problematic (see detailed steps in Ref. 19).

Once the water-tight nacelle surface is generated, the nacelle surface meshes are combined with the surface meshes of the clean HWB configuration. Subsequently, a computational unstructured surface mesh system can be generated for the combined configuration. About 31 million computational mesh points are used for the half model of the N3–X configuration, and the first nodes off the viscous walls are clustered to the wall so that the $y +$ values at the first nodes are less than 2.

# 6.2 Fan Model

The conventional uniform-back-pressure boundary condition for fan faces has been used widely to simulate flow for propulsion-airframe integration problems (Refs. 33 to 35). However, for highly distorted flows at the fan face, this assumption may not be valid: Considerable interactions between the fan flow and inlet flow can take place and the boundary condition is not known a priori. The low momentum in a low-pressure-recovery region at a fan face causes a large local incidence angle for the fan rotor blade. This causes the fan to have a stronger suction effect, which in turn mitigates the flow distortion. Consequently, the use of a uniform back-pressure boundary condition has produced conservative results for flow distortion at the fan face, although it is still valid for a qualitative evaluation of inlet-fan interactions when the diffuser flow separation does not reach to the fan face (Ref. 36).

A direct coupling of the inlet and full-annulus fan blades in the computational domain would give a more realistic simulation of the inlet-fan interactions, but the computational cost would be prohibitively large, especially if shape-design iterations are engaged, which usually require more than tens of flow simulations. The body force approach (Refs. 20 and 36), also described earlier in Section 4.2, is considered to be a viable alternative to account for the effects of full-annulus fan blades. This approach uses body force terms to model flow turning and loss due to rotor-stator blade rows. The body force terms

are added as source terms in the flow equations for grid cells swept by blade rows. Body force coefficients or parameters are based on either the Navier-Stokes solution results for a single-passage flow or experimental data. The body force approach allows a relatively accurate flow simulation of BLI inletfan interactions that consider blade force effects without committing an expensive full-annulus simulation of the rotor/stator geometry.

In the context of the N3–X concept, we are especially interested in how a distorted boundary layer that has been ingested into a nacelle will affect the performance of a fan situated behind an S-inlet. A physical setup of this problem is depicted in Figure 37, in which the inlet A was scaled up and connected to the R4 fan stage, so that a direct comparison can be assessed with the performance of the R4 fan subject to a clean inflow.

As a first step for the validation of the present body force method, a body force model was generated for the 100 percent design rotor speed of the R4 fan stage. Figure 38 shows that the fan pressure ratio and stage efficiency (entropy production) are well matched both for fan rotor and stator stages with the data taken by Hughes et al. (Ref. 22) for the data with uniform inlet flow. Next, we extend the model to consider the situation of a distorted inlet flow generated for inlet A in which the R4 fan is fitted. Mesh size for the present simulation was about 30 million. Figure 38 also includes the fan pressure ratio versus MFR for a distorted inflow. Severe degradation by the ingested boundary layer is found in the pressure ratio by about 3 percent, and stage efficiency by about 5 percent; moreover, the choke MFR is decreased by nearly 5 percent. The fan pressure ratio by the full annular simulation for inlet A+fan R4 again validates the accuracy of the present body force model.

In Figure 39, we show the comparison of the solutions at the fan face by the full-annulus simulation and body force model. The full annulus of blades was considered in Reference 37 by using an unsteady unstructured grid approach, with 59.1 million mesh points; it is an excellent benchmark for the present body force model to compare against. The body force model gives an averaged description of the circumferential and radial variation of flow quantities on the fan face, showing comparable quantitative values with negligible computational cost and complexity.

# 6.3 CFD Analysis of Baseline N3–X

First, we show representative aerodynamic characteristics of the clean wing in Figures 40 and 41. As mentioned earlier, the N2 airframe is used for the N3–X study defined for a different design point: $\mathrm { M } = 0 . 8 4$ , $\mathrm { \ A O A } = 2 ^ { \circ }$ at the same altitude of 35 000 ft. Hence, the aerodynamic performance is expected to be suboptimal. However, an optimal clean-wing geometry would not necessarily hold its superiority after a propulsion system is installed; that the combined system should be considered together is the notion we have attempted to stress while considering a HWB with an embedded propulsion system. Figures 40 and 41 can be viewed more appropriately as how the clean wing N2 performs at an off-design condition; of special interest is the pressure profile at 80 percent spanwise section where there is a shock wave near the leading edge on upper surface and near the trailing edge on lower surface, which are not observed at the design point of N2, ${ \mathrm { M } } = 0 . 8$ and $\mathrm { A O A } = 3 . 5 ^ { \circ }$ . The drag polar, corresponding to $\mathrm { M } = 0 . 8 4$ and $\mathrm { \ A O A } = 2 ^ { \circ }$ , also reveals a deteriorated aerodynamic performance in Figure 41, in comparison with Figures 14, 19, and 32.

Equipped with the prediction capability of including fans in the mail-slot propulsor, we now turn our attention to the full configuration of N3–X. A body force model was built for each N3–X fan, for which the R4 fan was scaled up to fit the duct diameter of 40.25 in. as described earlier, and the blade stagger angle and rotor speed were adjusted to match the specifications. The blade stagger and rotor speed were modified, and the SWIFT code was run to check the modifed fan’s performance. Through an iterative procedure, the stagger angle was reduced by $5 ^ { \circ }$ and the corrected rotor speed was determined to be 5913.667 rpm.

Figure 42 confirms that the numerical results from the SWIFT code and the current Euler simulation with the body force model are well matched except near high-MFR conditions. Because the body force model will actually be applied here to a viscous flow simulation of the N3–X configuration, Navier-Stokes simulations of the modifed R4 rotor with the body force model were tested. The pressure ratio

does not differ significantly for the Euler and Navier-Stokes simulations, but entropy production should be increased in the viscous simulation. The triangular symbols in Figure 42 represent the results for the corrected body force model. There is little difference in the pressure ratio, and there is good agreement in the entropy production for the SWIFT code and the Euler and Navier-Stokes simulation with the body force model.

A flow simulation of the N3–X HWB configuration was conducted for a cruise flight condition: Mach 0.84, an altitude of 35 000 ft, and an AOA of $2 ^ { \circ }$ . We used about 20 million mesh points for the half model, of which the first nodes off the viscous walls are clustered to the wall so that the $y +$ values at the first nodes are less than 2. Figures 43 and 44 show sectional side views of local Mach number and total pressure contours for the first and last propulsor passages (counting from the symmetry plane to outboard). The difference in the ingested boundary-layer thickness affects the total pressure contours. The inner passages have thicker boundary layers than the outer passages because of the longer distance from the airframe leading edge. As a result, the outer passages have higher total pressure recoveries and larger mass flow rates than the inner passages. The region coincident to the fan blade and represented by the body force model can be easily recognized with a steep axial gradient in the total pressure contours across the fan. The figure also suggests that the duct and hub afterbody shapes need to be improved in order to reduce flow blockages and partial supersonic flows. As shown in Figure 43, the first propulsor has a strong shock wave on the cowl surface and shock-induced flow separation, which need to be removed for better aerodynamic performance. However, the cowl flow seems to behave well, with shock-free Mach contours.

Figure 45 visualizes the separation bubbles with negative streamwise velocity envelopes; the most significant ones are outer cowl surface and trailing edge surfaces in the midspan section, with a minor one in the outboard nacelle exit region.

Again, because of the thickest boundary layer, the inner passage has the lowest pressure recovery at the fan face, as displayed in Figure 46. However, the higher inlet performance of the outer passage does not yield higher fan performance, namely the fan pressure ratio or fan efficiency, because there is another factor in the flow that determines the fan efficiency significantly—the three dimensionality. Figure 47 shows that the inboard fans have a better performaces than the outboard fans. This is due to the fact that the streamlines are turned toward inboard as shown in Figure 48, resulting in less aligned streamlines for the outboard passages than the inboard passages.

According to the above study, the benefit of ingested boundary layer (as often cited in the literature for drag reduction reared by the HWB concept) is only derived from one consideration; the ingested lowmomentum boundary layer can also have undesirable effects on the propulsion performance manifested by the mutual interference of propulsion system and airframe, which leads to flow distortion impact on structural durability of the fan, reduced fan pressure ratio and stage efficiency, and reduced aerodynamic performance with a significant increase in drag. For N2–B, we resorted to shape optimization strategies to improve aerodynamic characteristics: the benefits are substantial and shown in Figures 14, 19, and 32 where the drag coefficient is cut by 50 counts for the design point. Hence, the same approach is taken for N3–X, as described below.

# 6.4 Shape Design Results

To improve the aerodynamic performance of the mail-slot nacelle, the cowl surface shape was designed to minimize the aerodynamic drag using the above-described optimization approach. For geometry parameterization of this application, the CST (Class-Shape-Transformation) method (Ref. 38) is employed, which allows an easy specification of the leading-edge radius and trailing-edge angles of airfoil shapes. The number of design parameters was 55, resulting from 11 parameters per design section for 5 design sections.

Figure 49 compares Mach contours of baseline and design configurations in midsections of passages 3, 4, and 5. Using the optimal shape design procedure discussed above, the strength of shock waves in the middle region on the cowl surface is remarkably reduced, which amounts to a drag reduction of 13 counts. But there are still exit flow separations in the inboard region as can be seen in Figure 49(a), although with a much reduced size. The design thickens the cowl section and increases its convexity. It is believed that an increased dimension in design space should be explored such as inclusion of sweep angle, in order to further reduce the drag count by minimizing the flow separation in the inboard region.

# 7.0 Conclusion and Future Plans

In summary, the objectives of the technical activities described above are as follows: (1) Perform aerodynamic performance analysis and optimization for an embedded propulsion system in hybrid wingbody configurations of NASA’s interest in high-fidelity modes, (2) Assess critical challenges belonging to N2–B and N3–X configurations, (3) Make input and parameters derived from the highfidelity solution available to low-order system-level simulations, (4) Develop and enhance analysis and design capabilities for handling complex geometries and physics inherent in real-world configurations, and (5) Develop efficient and accurate surrogate models for performing multicomponent and multidisciplinary analysis and design.

During the period of performing the results reported herein, we focused on two hybrid wingbody (HWB) concepts. The first one is denoted as N2–B for which three independent nacelles are installed aft near the trailing edge of the vehicle—each nacelle houses a traditional turboengine along with two turbofans on its sides. The second is denoted as N3–X for which numerous small turbofans are tucked inside a common nacelle, but each compartmentalized inside an S-duct, and the fans are driven by two turboengines located away from the nacelle (e.g., at the wingtips). For each of these configurations, we first carried out computational fluid dynamics (CFD) solutions for establishing the corresponding aerodynamic performance for the design cruise condition. Then deficiencies and challenges of the baseline designs were assessed and optimization strategies for shape redesign to reduce drag and internal flow distortions ensued. Engine surrogate models were respectively developed for both configurations to reflect the engine concepts employed; the models were subject to benchmark validations to ensure accuracy of the models. Consequences to the optimization are significant improvements in the objective functions to be optimized.

The approach deployed has proven valid and useful for delivering quantitative evaluation of the complex systems considered here. Numerous findings are the first of their kind and should give valuable insights and serve as a reference for future study on the subject of HWB with embedded propulsion.

Areas of interest for future developments include (1) a preliminary design system for the integrated HWB-propulsion configuration, (2) inclusion of multiple disciplines such as structure dynamics, and (3) further improvement in the design of N3–X.

# Appendix—Nomenclature

3D three-dimensional

$A ( x )$ sectional area at axial location x

ADP aerodynamic design point

AIP aerodynamic interface plane

AOA angle of attack

AR aspect ratio

BLI boundary layer ingestion

BPR bypass pressure ratio

BWB blended wingbody

$C$ coefficient

c blade chord length

CAD computer-aided design

CFD computational fluid dynamics

$D$ diameter of inlet at AIP

DPCP circumferential distortion indicator

$F$ objective function

$F _ { n } , F _ { p }$ body force components normal and tangential to the local flow vector, respectively

f radial profile function

FPR fan pressure ratio

g mass-flow-rate-adjusting function

$H$ throat height

HWB hybrid wingbody

h blade-to-blade gap-staggered spacing, $h { = } 2 \pi r \sqrt { \sigma } ( \mathrm { c o s d } ) / B$

$K$ body force coefficient

M Mach number

MFR, ݉ሶ mass flow rate

m meridional coordinate

N number

OML outer mold line

$P$ pressure

R gas constant

Re Reynolds number

r radius

s specific entropy

SLS sea level standard

T temperature

TeDP turboelectric distributed propulsion

TOC top of climb

u velocity component in x-direction

$V$

$V _ { n } , V _ { p }$ velocity components normal and tangential to the blade, respectively

VG vortex generator

$x , y , z$ Cartesian coordinates

$\mathfrak { a }$ blade camber angle

γ ratio of specific heats

 total pressure recovery

# Subscripts

0 baseline or inflow

$^ { * 1 }$ station 1, fan blade row entrance

$^ { * 2 }$ station 2, fan blade row exit

AIP aerodynamic interface plane

avg average

$^ { b }$ exit (back) plane

$D$

$h$ hub of blade

inf freestream

$L$

LE leading edge

local local value

m meridional component

*n $^ * n$ normal

$P$ pressure

$^ { * } p$ tangential

rel relative to the blade

$T$ thrust

t total (stagnation) condition

TE trailing edge

# References

1. Flying Wing. Wikipedia, San Jose, CA, 2015. http://en.wikipedia.org/wiki/Flying_wing (Accessed Dec. 14, 2015).   
2. Liebeck, R.H.: Design of the Blended Wing Body Subsonic Transport. J. Aircraft, vol. 41, no. 1, 2004.   
3. Kawai, R., et al.: Acoustic Prediction Methodology and Test Validation for an Efficient Low-Noise Hybrid Wing Body Subsonic Transport. NASA Contract Number NNL07AA54C, Final Report, 2011.   
4. Menter, F.R.: Two-Equation Eddy-Viscosity Turbulence Models for Engineering Applications. AIAA J., vol. 32, no. 8, 1994, pp. 1598–1605.   
5. Obayashi, S.; and Wada, Y.: Practical Formulation of a Positively Conservative Scheme. AIAA J., vol. 31, no. 5, 1994, pp. 1093–1095.   
6. Liou, M.-S.: A Sequel to AUSM, Part II: AUSM+-up for All Speeds. J. Comput. Phys., vol. 214, no. 1, 2006, pp. 137–170.   
7. Yoon, S.; and Jameson, A.: Lower-Upper Symmetric-Gauss-Seidel Method for the Euler and Navier-Stokes Equations. AIAA J., vol. 26, no. 9, 1988, p. 1025.   
8. Chima, R.V.: SWIFT—Multiblock Analysis Code for Turbomachinery User’s Manual and Documentation. NASA Glenn Research Center, Version 400, 2011.   
9. Wilcox, D.C.: Turbulence Modeling for CFD. Third ed., DCW Industries, Inc., La Canada, CA, 2006.   
10. Nichols, R.H.; and Buning, P.G.: User's Manual for OVERFLOW 2.2. NASA Langley Research Center, Hampton, VA, 2010.   
11. Saad, Y.; and Schultz, M.H.: GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems. SIAM J. Sci. Stat. Comput., vol. 7, 1986, pp. 856–869.   
12. Kim, H.; and Nakahashi, K.: Unstructured Adjoint Method for Navier-Stokes Equations. JSME International J., Series B, vol. 48, no. 2, 2005, pp. 202–207.   
13. Douglass, W.M.: Propulsive Efficiency With Boundary Layer Ingestion. MDC J0860, McDonnell Douglas Corp., Long Beach, CA, 1970.   
14. Berrier, B.L.; Carter, M.L.; and Allan, B.G.: High Reynolds Number Investigation of a Flush-Mounted, S-Duct Inlet With Large Amounts of Boundary Layer Ingestion. NASA/TP—2005- 213766, 2005. http://ntrs.nasa.gov   
15. Owens, L.R.; Allan, B.G.; and Gorton, S.A.: Boundary-Layer-Ingesting Inlet Flow Control. J. Aircraft, vol. 45, no. 4, 2008, pp. 1431–1440.   
16. Lee, B.J.; Liou, M.-S.; and Kim, C.: Optimizing Shape of Boundary-Layer-Ingestion Offset Inlet Using Discrete Adjoint Method. AIAA J., vol. 48, no. 9, 2010, pp. 2008–2016.   
17. Liou, M.-S.; and Lee, B.J.: Minimizing Inlet Distortion for Hybrid Wing Body Aircraft. ASME J. Turbomachinery, vol. 134, no. 031020, 2012.   
18. Anabtawi, A.J., et al.: An Experimental Investigation of Boundary Layer Ingestion in a Diffusing S-Duct With and Without Passive Flow Control. AIAA–1999–0739, 1999.   
19. Kim, H.; and Liou, M.-S.: Flow Simulation of N3–X Hybrid Wing-Body Configuration. AIAA– 2013–0221, 2013.   
20. Gong, Y.: A Computational Model for Rotating Stall Inception and Inlet Distortion in Multistage Compressors. Ph.D. Dissertation, Massachusetts Institute of Technology, 1998.   
21. Chima, R.V.: A Three-Dimensional Unsteady CFD Model of Compressor Stability. ASME GT2006–90040, 2006.   
22. Hughes, C.E.: Aerodynamic Performance of Scale-Model Turbofan Outlet Guide Vanes Designed for Low Noise. AIAA–2002–0374 (NASA/TM—2001-211352), 2002. http://ntrs.nasa.gov   
23. Hileman, J.I., et al.: Airframe Design for Silent Fuel-Efficient Aircraft. J. Aircraft, vol. 47, no. 3, 2010, pp. 956–969.

24. Tong, M., et al.: Engine Conceptual Design Studies for a Hybrid Wing Body Aircraft. NASA/TM—2009-215680, 2009. http://ntrs.nasa.gov   
25. Lytle, J.K.: Numerical Propulsion System Simulation: An Overview. NASA/TM—2000-209915, 2000. http://ntrs.nasa.gov   
26. Kim, H.; and Liou, M.-S.: Flow Simulation of N2B Hybrid Wing Body Configuration. AIAA–2012–0838, 2012.   
27. Murayama, M.; Nakahashi, K.; and Matsushima, K.: Unstructured Dynamic Mesh for Large Movement and Deformation. AIAA–2002–0122, 2002.   
28. Vanderplaats, G.N.: Numerical Optimization Techniques for Engineering Design: With Applications. McGraw-Hill, New York, NY, 1984, pp. 88–89.   
29. Takenaka, K.; Hatanaka, K.; and Nakahashi, K.: Efficient Aerodynamic Design of Complex Configurations by Patch-Surface Approach. J. Aircraft, vol. 48, no. 5, 2011, pp. 1473–1481.   
30. Lepine, J., et al.: Optimized Nonuniform Rational B-Spline Geometrical Representation for Aerodynamic Design of Wings. AIAA J., vol. 39, no. 11, 2001, pp. 2033–2041.   
31. Felder, J.; Kim, H.D.; and Brown, G.V.: An Examination of the Effects of Boundary Layer Ingestion on Turboelectric Distributed Propulsion Systems. AIAA–2011–300, 2011.   
32. Walatka, Pamela P., et al.: PLOT3D User's Manual. NASA TM–101067, 1990. http://ntrs.nasa.gov   
33. Rodriguez, D.L.: Multidisciplinary Optimization Method for Designing Boundary Layer Ingestion Inlets. J. Aircraft, vol. 46, no. 3, 2009, pp. 883–894.   
34. Kim, H., et al.: Numerical Propulsion Flow Simulation of Supersonic Inlet With Bypass Annular Duct. J. Propul. Power, vol. 27, no. 1, 2011, pp. 29–39.   
35. O’Brien, Jr., D.M.; Calvert, M.E.; and Butler, S.L.: An Examination of Engine Effects on Helicopter Aeromechanics. AHS Specialist’s Conference on Aeromechanics, San Francisco, CA, 2008.   
36. Chima, R.V.: Rapid Calculations of Three-Dimensional Inlet/Fan Interaction. NASA Fundamental Aeronautics 2007 Annual Meeting, New Orleans, LA, 2007.   
37. Webster, R.S., et al.: Demonstration of Sub-system Level Simulations: A Coupled Inlet and Turbofan Stage Aerodynamic Performance of Scale-Model Turbofan Outlet Guide Vanes Designed for Low Noise. AIAA–2012–4282, 2012.   
38. Kulfan, B.M.: Universal Parameteric Geometry Representation Method. J. Aircraft, vol. 45, no. 1, 2008, pp. 142–158.

TABLE I.—NASA FIXED WING PROJECT METRICS   
v2013.1   

<table><tr><td rowspan="2">TECHNOLOGY BENEFITS*</td><td colspan="3">TECHNOLOGY GENERATIONS (Technology Readiness Level = 4-6)</td></tr><tr><td>N+1 (2015)</td><td>N+2 (2020**)</td><td>N+3 (2025)</td></tr><tr><td>Noise (cum margin rel. to Stage 4)</td><td>-32 dB</td><td>-42 dB</td><td>-52 dB</td></tr><tr><td>LTO NOx Emissions (rel. to CAEP 6)</td><td>-60%</td><td>-75%</td><td>-80%</td></tr><tr><td>Cruise NOx Emissions (rel. to 2005 best in class)</td><td>-55%</td><td>-70%</td><td>-80%</td></tr><tr><td>Aircraft Fuel/Energy Consumption† (rel. to 2005 best in class)</td><td>-33%</td><td>-50%</td><td>-60%</td></tr></table>

Projected benefitsonce technologiesare maturedand implementedbyindustry.Benefits vary byvehicle sizeand mision. $N + 1$ and $_ { \mathsf { N } + 3 }$ values arereferenced toa737-800 with CFM56-7B engines, $_ { N + 2 }$ valuesare referenced toa 777-200 with GE90 engines   
**ERA'stime-phasedapproach includesadvancing"long-pole"technologies to TRL6by 2015   
‡ CO2 emission benefits dependent on life-cycle CO2e per MJ for fuel and/or energy source used

TABLE II.—NASA N2–B EMBEDDED-ENGINE CYCLE INFORMATION   
[From Reference 3.]   

<table><tr><td></td><td>Sea level standard, SLS, (ISA+27 °F)</td><td>Aerodynamic design point, ADP, (M0.80/31 kft/ISA+0 °F)</td><td>Top of climb, TOC, (M0.80/35 kft/ISA+0 °F)</td></tr><tr><td>Fan pressure ratio</td><td>1.49</td><td>1.50</td><td>1.50</td></tr><tr><td>Bypass pressure ratio (core engine + central fan only)</td><td>3.2</td><td>3.1</td><td>3.1</td></tr><tr><td>Effective BPR (3 fans)</td><td>11.5</td><td>11.3</td><td>11.3</td></tr><tr><td>Overall pressure ratio</td><td>45</td><td>46</td><td>46</td></tr><tr><td>Net thrust per engine, lb</td><td>49 060</td><td>10 000</td><td>8286</td></tr><tr><td>Specific fuel consumption, lb/(lb-hr)</td><td>0.288</td><td>0.564</td><td>0.553</td></tr><tr><td>High-pressure turbine (HPT) inlet temperature, °R</td><td>3460</td><td>3010</td><td>2920</td></tr><tr><td>HPT rotor inlet temperature, °R</td><td>3310</td><td>2876</td><td>2789</td></tr><tr><td>Low-pressure turbine rotor inlet temperature, °R</td><td>2460</td><td>2113</td><td>2044</td></tr></table>

图片摘要：该图主要展示 II.—NASA N2–B EMBEDDED ENGINE CYCLE INFORMATION。
![](images/7d01440156d36c1d8f5685bbc8c404f28e689f23ca478858c0bf2466e27618fa.jpg)  
(a)

图片摘要：该图主要展示 II.—NASA N2–B EMBEDDED ENGINE CYCLE INFORMATION。
![](images/b988e970c58b6b7378d7144396ea9bafbec844020e2b850953f682a36d8ded7a.jpg)  
(b)

图片摘要：该图主要展示 1.—Hybrid wingbody (HWB) aircraft configurations considered 。
![](images/fb3e31d65856935299118cafe20b56fbabefc3eaed5fdf9ebc0bfc5adddeb233.jpg)

Figure 1.—Hybrid wingbody (HWB) aircraft configurations considered by NASA. (a) N2–A. (b) N2–B. (c) N3–X.

图片摘要：该图主要展示 1.—Hybrid wingbody (HWB) aircraft configurations considered 。
![](images/4134c5f952a85b4e3bd2305f6685ef12b0b13a4daf1678c635676064291420a0.jpg)  
Figure 2.—Fuel efficiency and noise results for N2–A, N2–B, and N2A–EXTE hybrid wingbody (HWB) configurations from the Boeing study (from Ref. 3). EPNdB is effective perceived noise in decibels, and FPR is fan pressure ratio. (a) Fuel efficiency comparison. (b) Noise relative to Far 36 Stage 3.

(a)

Payload, 1000 Ib

(b)   

<table><tr><td></td><td>FPR = 1.6</td></tr><tr><td>Cumulative EPNdB with elevon noise</td><td>251.0</td></tr><tr><td>Cumulative EPNdB without elevon noise</td><td>244.3</td></tr><tr><td>N + 2 goal</td><td>250.4</td></tr><tr><td>EPNdB margin with elevon noise</td><td>+0.6</td></tr><tr><td>EPNdB margin without elevon noise</td><td>-6.1</td></tr></table>

图片摘要：该图主要展示 3.—Boundary layer ingestion (BLI) offset inlet configuration。
![](images/9bd7232c49f9377818fc396a15bf5def92f212d9857f7176a9eba363514009e5.jpg)  
Figure 3.—Boundary layer ingestion (BLI) offset inlet configuration: Inlet A model (Ref. 14).

图片摘要：该图主要展示 3.—Boundary layer ingestion (BLI) offset inlet configuration。
![](images/1b9c0b808b7e5360c41844ca6ee968c859320fff876cd4522a20e0376867b472.jpg)

图片摘要：该图主要展示 3.—Boundary layer ingestion (BLI) offset inlet configuration。
![](images/12a99ea36deee24ffb8afa5cd1f8cf97874ddf32579afd02a7fa0d7ba7371c21.jpg)

图片摘要：该图主要展示 3.—Boundary layer ingestion (BLI) offset inlet configuration。
![](images/75ef652637fdb8258d78de3a8ff7f15ecdd713cae45f4acfc0af4add683ce4b6.jpg)

图片摘要：该图主要展示 3.—Boundary layer ingestion (BLI) offset inlet configuration。
![](images/da3adbfb34e902ba576c0d7ab46efeb0ee09321a6aa7ae21631318efcd6aedf5.jpg)  
(b)   
Figure 4.—Factors affecting distortion and total pressure Pt (from Ref. 15). D is inlet diameter, and Re is Reynolds number. (a) Wall jets mass flow ratio; inflow Mach number $\mathsf { M } = 0 . 8 5$ . (b) Vortex generator (VG) vanes.

图片摘要：该图主要展示 4.—Factors affecting distortion and total pressure Pt (from 。
![](images/806d180104d2f3577d40cbf0cf662240065c43333ea9e37ba75a2ff28fa31f77.jpg)  
（a)

图片摘要：该图主要展示 4.—Factors affecting distortion and total pressure Pt (from 。
![](images/f4506d2eb33e450a2a736a6c7ac5c8713ad8a7e0d8d8eb9dcd3d8bb0e8740e38.jpg)  
  
Figure 5.—”Oil flow” pattern of inlet superimposed on pressure contours. Red color indicates elevation towards flow, and blue areas are depressed from original. (a) Original inlet. (b) Optimal inlet.

图片摘要：该图主要展示 5.—”Oil flow” pattern of inlet superimposed on pressure cont。
![](images/4100936ce8633a3ae805d6eebf38502b060f83404610d396aeb3ee6f04654005.jpg)

图片摘要：该图主要展示 5.—”Oil flow” pattern of inlet superimposed on pressure cont。
![](images/28bf06503c9fd2ed4d8ac71c692586d488711aaf5f22e5325ff4bb0fdba864b4.jpg)  
$x / D = 0 . 5$

图片摘要：该图主要展示 5.—”Oil flow” pattern of inlet superimposed on pressure cont。
![](images/6f37df6036bd37d7ca37535dff96b6a74ae7467d1122f5ae98adca7d97c87a70.jpg)

图片摘要：该图片与x/D= 1.0；x/D= 2.0这部分内容相关。
![](images/c8bfe650f510a663115be3ada1a4415fdabafcf72e7d466b05bc80466c9d19ec.jpg)  
x/D= 1.0

图片摘要：该图片与x/D= 2.0；x/D= 2.5这部分内容相关。
![](images/3eb5a8bdbe028229c21ccf50265d1f4b9d2b618b0201bf4f5444f54ddf46acd4.jpg)

图片摘要：该图片与x/D= 2.0；x/D= 2.5这部分内容相关。
![](images/1a671405d63098f92158fa1aeb193227d85b3a48d3beb40a0255e8062d02af77.jpg)  
x/D= 2.0

图片摘要：该图片与x/D= 2.5；x/D= 3.0这部分内容相关。
![](images/4077d8db6e94453d8d6dec77a908e0facee284fbbf0254b5121a6d92154b752d.jpg)

图片摘要：该图片与x/D= 2.5；x/D= 3.0这部分内容相关。
![](images/6ea3772b925127deb11e44f982f35988b70497a872e66b979e6c4e1a8ecda91f.jpg)  
x/D= 2.5

图片摘要：该图主要展示 6.—Cross sectional Mach number contours at various streamwis。
![](images/6212282790aaf9aeb65d212e0985370b28b8134bc18b0372f1785b9fd125efad.jpg)

图片摘要：该图片与x/D= 3.0；Figure 6.—Cross sectional Mach number contours at various streamwise lo这部分内容相关。
![](images/a43ea3472f345d67c1395e7fcfb20a90d7f7e8be9617b45d2e9cab880c580e62.jpg)  
x/D= 3.0

(b)   
Figure 6.—Cross-sectional Mach number contours at various streamwise locations $x / D$ , with superimposed cross flow streamlines. (a) Design condition,   
图片摘要：该图主要展示 6.—Cross sectional Mach number contours at various streamwis。
![](images/11f44772d84fa19710a5707dcc850674b74b7dad35effbe16bd33151995c48ac.jpg)  
$P _ { b } / P _ { t 0 } = 0 . 8 1 3 7$ . (b) Off-design condition,   
$P _ { b } / P _ { t 0 } = 0 . 8 4 1 7$

图片摘要：该图主要展示 6.—Cross sectional Mach number contours at various streamwis。
![](images/142a36d36c4de6e68ebfec5a1aff28621a51656b724cc922139fe2ef9ad7a3ef.jpg)

图片摘要：该图主要展示 6.—Cross sectional Mach number contours at various streamwis。
![](images/7cffef50ea8db1ffbb93bc9898f34c3715f97f88b147de115921c17eb8eaeb2b.jpg)  
Figure 7.—Comparison of performance indices of baseline and optimized inlets at various mass flow rates. (a) Distortion. (b) Total pressure recovery.

图片摘要：该图主要展示 7.—Comparison of performance indices of baseline and optimiz。
![](images/7140c6a05bac7cc379de3d61a1696522c1e52922edeb9b4d8bcb0eca2c7f491d.jpg)  
Figure 8.—Illustration of body force components at blade-to-blade section.

图片摘要：该图主要展示 8.—Illustration of body force components at blade to blade s。
![](images/6e79d8029b1319bc9e91031d42649d383542d4d947cd19d323f011fb7409d47d.jpg)

图片摘要：该图主要展示 8.—Illustration of body force components at blade to blade s。
![](images/6b48a76e8f830412084dc14a8ca03a11b2f03c17d2821c7a22804fac29c0b3c8.jpg)  
Figure 9.—Representative variations of radial profile function $\pmb { f } ( \boldsymbol { r } )$ and mass-flow-rate-adjusting function $\mathfrak { g } ( m _ { \mathrm { l o c a l } } )$ , used in Equation (2). Subscripts $h$ and t, respectively, denote hub and tip of a blade.

图片摘要：该图主要展示 9.—Representative variations of radial profile function and 。
![](images/c2f4170742ce0bdcebaaf43ebb30aa81a20105760917bf41cf50f99b2e242e30.jpg)  
Figure 10.—Entropy production s versus corrected mass flow rate of R4 fan rotor blade row for different rotor speeds.

图片摘要：该图主要展示 10.—Entropy production s versus corrected mass flow rate of。
![](images/8f1266111399d8c62107199aa1c77d866676446ae98857372206d0d93d6a5074.jpg)  
(a)

图片摘要：该图主要展示 10.—Entropy production s versus corrected mass flow rate of。
![](images/0b126073593c522aec887163cac7b2b4739bfc2423eb5c7a733d029f48197ff6.jpg)  
（b)  
Figure 11.—R4 fan and nacelle. (a) Side view. (b) Computational mesh.

图片摘要：该图主要展示 11.—R4 fan and nacelle. (a) Side view. (b) Computational mes。
![](images/477263952e511afe68bd27b1a7b46a8b98a04391183d6a590a8743312e859a6a.jpg)

图片摘要：该图主要展示 11.—R4 fan and nacelle. (a) Side view. (b) Computational mes。
![](images/6204782d48caa28dab3c49b97a0b45e7d6cfa4873a8fad3d2513d15ed8bc730d.jpg)  
Figure 12.—Comparison of body force model results with test data (Ref. 22) and SWIFT code at 85 percent speed. (a) Fan pressure ratio (FPR). (b) Entropy production s.

图片摘要：该图主要展示 12.—Comparison of body force model results with test data (R。
![](images/f1969b7e4d778e355a715616451401103351ff0d9f4128de6c519ada4f88a2ce.jpg)  
Figure 13.—Thrust vectoring and reversing nozzle.

图片摘要：该图主要展示 13.—Thrust vectoring and reversing nozzle。
![](images/e6650a591bcd00be381e4efb9fd7795690533a453e637891459c590ed8f5c6f3.jpg)  
Figure 14.—Drag polar of N2–B for Mach 0.80, showing result of clean wing by Boeing (Ref. 3) and that of engines-installed configuration with baseline and redesigned nacelle.

图片摘要：该图主要展示 14.—Drag polar of N2–B for Mach 0.80, showing result of clea。
![](images/760678c969d2b319b61586dcd0b56da33a0a94a5d0d2daad420aedfb9b2c65bf.jpg)

图片摘要：该图主要展示 14.—Drag polar of N2–B for Mach 0.80, showing result of clea。
![](images/fd8220a846244c3f38ea82e5e8ca00474ead3bb2ff81cce26c79e80cef96c898.jpg)

图片摘要：该图主要展示 14.—Drag polar of N2–B for Mach 0.80, showing result of clea。
![](images/1b433882e1b7e99db63958b98d196b64502d336ddf6b8da69b9b007e186eed06.jpg)

图片摘要：该图主要展示 14.—Drag polar of N2–B for Mach 0.80, showing result of clea。
![](images/9f9ed0efbfb71f3bc5589e30847f5a28c0cfe0c4991d7e64944ae87679aab52e.jpg)  
Figure 15.—Mach number and total pressure $P _ { t } / P _ { t , \mathrm { i n f } }$ profiles in boundary layers at different streamwise locations x on symmetry plane of clean geometry of N2–B, where $d$ is normal distance measured from wall and c is a reference length. (a) $x / c = 0 . 6$ . (b) $x / c = 0 . 7$ . (c) $x / c = 0 . 8$ . (d) $x / c = 0 . 9$ .

图片摘要：该图主要展示 15.—Mach number and total pressure profiles in boundary laye。
![](images/3f6d3e5ec645f118dce89f2f0903c571000261438f993698d064213c46184017.jpg)

图片摘要：该图主要展示 15.—Mach number and total pressure profiles in boundary laye。
![](images/169b6d3e064e9b2fc92ac52c0fce266e58ae8e485ab075037ec4da5c3d758e67.jpg)  
Figure 16.—Multiple-fan embedded turbofan engine for N2–B (Ref. 3). (a) Tri-fan $^ +$ core engine. (b) Internal layout of embedded engine (Ref. 24).

图片摘要：该图主要展示 16.—Multiple fan embedded turbofan engine for N2–B (Ref. 3).。
![](images/9ca7f19fdb9500b380bee87227456c2e042fd60b93a431aa2ce718748fca5fa8.jpg)  
（a)

图片摘要：该图主要展示 16.—Multiple fan embedded turbofan engine for N2–B (Ref. 3).。
![](images/e7662063b1e0b8c80191dc1d1fb86c2a6bcb68766535d4d49a95f4bfd1763920.jpg)  
(b)   
Figure 17.—Engine boundary conditions by Numerical Propulsion System Simulation (NPSS) model for N2–B. (a) Engine block replaced with NPSS model in computational fluid dynamics (CFD) domain. Dark blue region indicates base flow separation. (b) Coupling between CFD flow solver and NPSS. AIP is aerodynamic interface plane.

图片摘要：该图主要展示 17.—Engine boundary conditions by Numerical Propulsion Syste。
![](images/8ce854e219a720752b7785c796458fab7fbb2d084ed78524b705d206f0194298.jpg)

图片摘要：该图主要展示 17.—Engine boundary conditions by Numerical Propulsion Syste。
![](images/88c28fb8271f6f1422179e8c0e57861e58a8c24bec6e936cfe3a7a80b8e23984.jpg)

图片摘要：该图主要展示 17.—Engine boundary conditions by Numerical Propulsion Syste。
![](images/27ac471ddaa3580b17bdfb528eb799aff2122ad24171cc3791986606864f53a8.jpg)  
Figure 18.—Response surfaces for Numerical Propulsion System Simulation (NPSS) engine model at maximum power condition with Mach 0.8 and altitude of 35 000 ft, where data points are from NPSS code. Symbols denote NPSS results and lines are the prediction of the model constructed by Equation (5). (a) Mass flow rate m at passages 1, 2, and 3, $m _ { 1 , 2 , 3 }$ . (b) Total exit pressure at center passage 1, $P _ { t , \mathrm { e x i t } 1 }$ . (c) Total exit pressure at side passages 2 and 3, $P _ { { t , \tt e x i t } 2 , 3 }$ .

图片摘要：该图主要展示 18.—Response surfaces for Numerical Propulsion System Simula。
![](images/8b782f869ea7fe4d0edc71748ab6d7e92d94a6f443235109b46808407930d259.jpg)  
Figure 19.—Comparison of lift coefficients $\mathsf { C } _ { L }$ at different angles of attack (AOAs) between clean wing and N2–B configurations at Mach 0.8 and altitude of 35 000 ft.

图片摘要：该图主要展示 19.—Comparison of lift coefficients at different angles of a。
![](images/c6b8424b6e562a2d981491fc4163acce9de58b16ca6a51c74897937d7ff8b272.jpg)

图片摘要：该图主要展示 19.—Comparison of lift coefficients at different angles of a。
![](images/b3d22ff57bfbcdbac4ac6352ac1bc4da34365245ef6f6870579e22f446e16242.jpg)

图片摘要：该图主要展示 19.—Comparison of lift coefficients at different angles of a。
![](images/e83ea90596942fa047443597dddb96ab88797941978afe2d2e30ba4d77923a97.jpg)

图片摘要：该图主要展示 19.—Comparison of lift coefficients at different angles of a。
![](images/ed18f2c1a723d3f795e1381efe33b1786fc79d755bc49bf1a31c37d468bfb23b.jpg)

图片摘要：该图主要展示 20.—Comparison of sectional pressure distributions between c。
![](images/d5b2eac5334c268dae4d8ad09f54d0b48353287e1b1109df5e189970410b9dc7.jpg)

图片摘要：该图主要展示 20.—Comparison of sectional pressure distributions between c。
![](images/1019cba2064c09603106479c5380f18017ad3167b7dde6e4b26c57b591c02c2e.jpg)  
Figure 20.—Comparison of sectional pressure $( C _ { p } )$ distributions between clean wing and N2–B at Mach 0.8, altitude of 35 000 ft, and angle of attack (AOA) of $3 5 ^ { \circ }$ . (a) $\mathsf { y } = 0 . 0 1 0$ . (b) $\mathsf { y } = 0 . 0 8 3$ . (c) $\mathsf { y } = 0 . 1 6 7$ . (d) $\mathsf { y } = 0 . 3 0 0$ . (e) $\mathsf { y } = 0 . 5 0 0$ .

图片摘要：该图主要展示 20.—Comparison of sectional pressure distributions between c。
![](images/8677de0539275b01dec13cb74d1444470c4dbb6744465c420b05163cbd3d6ae2.jpg)  
(a)

图片摘要：该图主要展示 20.—Comparison of sectional pressure distributions between c。
![](images/6bf8cbf834b4cfef8f744e08008ca38d701b59f8465aeaa1dcf255189ea376e0.jpg)  
(b)

图片摘要：该图主要展示 20.—Comparison of sectional pressure distributions between c。
![](images/4c7d6c6195a9b8cf7cf954b011913e66fe04b5ede1fa179c57d5333b4c7598ae.jpg)  
（c）

图片摘要：该图主要展示 21.—Flow field rendition by pressure and Mach number contour。
![](images/e991e84198307e2c0937c6e5087470cc4bf3c1d2813aadce32e37bdc35ff7573.jpg)  
（d）  
Figure 21.—Flow-field rendition by pressure and Mach number contours. (a) Pressure contours around inlets together with supersonic envelop enclosing region (denoted by white color) with $\mathsf { M } > 1 . 1 5$ . (b) Separated flow regions (denoted with grey color) plotted over normalized static pressure contours. (c) Mach number contours on symmetry section of center nacelle. (d) Mach number contours on symmetry section of side nacelles.

图片摘要：该图主要展示 21.—Flow field rendition by pressure and Mach number contour。
![](images/65afeeb5af8e41634aad031f7a7bdf261de27eb790a059228e73a7f0c7b4614d.jpg)  
(a)

图片摘要：该图主要展示 21.—Flow field rendition by pressure and Mach number contour。
![](images/3fb24fe7cb61488efece1fe77a75b689939966de370cf355b743531370df1bc2.jpg)  
(b)

图片摘要：该图主要展示 21.—Flow field rendition by pressure and Mach number contour。
![](images/a14bf4fd1530579b72dd19c9c2a0221f4af351d99af36c375bb3c9f83294ee97.jpg)  
（c）

图片摘要：该图主要展示 22.—Flow path and separation patterns. (a) Particle path flo。
![](images/05ddf5b406bcca07f34612a01a834d400fe50d26ebaf4301b0a8e2ffd6f81483.jpg)  
Figure 22.—Flow path and separation patterns. (a) Particle path flowing into nacelles. Color contour are normalized static pressure. (b) Separation expressed by “oil flow” on surfaces via top view. (c) Separation expressed by “oil flow” on surfaces via side view.   
(a)

图片摘要：该图主要展示 22.—Flow path and separation patterns. (a) Particle path flo。
![](images/92bcd44f7083bfba9ce9de3e151fd2875b9c49b70c70413dc328ab5e3a6c82a3.jpg)  
  
Figure 23.—Comparison of boundary-layer thicknesses of N2–B and clean-wing configurations measured from their outer mold line (OML) at nacelle symmetry planes. (a) Center nacelle. (a) Side nacelle.

图片摘要：该图主要展示 23.—Comparison of boundary layer thicknesses of N2–B and cle。
![](images/cb06a05519bd5674b2b8e71b4370e1a1830566287bddfdfad1de31841f4a0dc6.jpg)  
Figure 24.—Normalized total pressure $( P _ { t } )$ contours inside N2–B diffusers (outmost flow passage is denoted 1 and center passage is 5). Streamwise coordinate x is measured from inlet highlight, and last planes are at fan face (AIP, aerodynamic interface plane). (a) Outer inlet. (b) Center inlet.

图片摘要：该图主要展示 24.—Normalized total pressure contours inside N2–B diffusers。
![](images/fd713791cf8a91e9a6aadcc19d0d1f0c9799acce79ffe8c9315dfddb69bbc523.jpg)  
Figure 25.—Comparison of total pressure recovery at AIPs (fan faces) for N2–B of present CFD results and Boeing’s estimation (Ref. 24). AIP1 is outmost fan face, and AIP5 is center fan.

图片摘要：该图主要展示 25.—Comparison of total pressure recovery at AIPs (fan faces。
![](images/371b9fdcc225410b8eb4b06bc7609f99a24ded5ed2371ce14fd7aebfa28168b8.jpg)  
Figure 26.—N2–B nacelle shape design procedure.

图片摘要：该图主要展示 26.—N2–B nacelle shape design procedure。
![](images/8bfdef7ee37fd16659ee2e7ca511143fde1a54e162258f54875f459f55d4e5c4.jpg)

图片摘要：该图主要展示 26.—N2–B nacelle shape design procedure。
![](images/2ac08f80c70002159bddf72cae471d7b82a500c449f49e22ba406996a0df3d68.jpg)

图片摘要：该图主要展示 26.—N2–B nacelle shape design procedure(b) Figure 27.—Separa。
![](images/018c3eba4d96f5b12589517728f7af7d6bde5105b52a838bca144d3246577096.jpg)

图片摘要：该图主要展示 26.—N2–B nacelle shape design procedure(b) Figure 27.—Separa。
![](images/b18414acb2c1b13f56e5f0da10733a5c2f721c4f1c019900a93e6c6e10c0863a.jpg)  
(b)   
Figure 27.—Separation bubble envelops (shown in grey) for N2–B initial (left) and Design 1 (right) configurations of nacelle shape. (a) Front view. (b) Side view.

图片摘要：该图主要展示 27.—Separation bubble envelops (shown in grey) for N2–B init。
![](images/738e34e2d06b7e8d36054c63a5c0c761e8dd262c0be9d7d6c39de907897c1a78.jpg)

图片摘要：该图主要展示 27.—Separation bubble envelops (shown in grey) for N2–B init。
![](images/da3f08cc13e93153648dd3589317b6e4da5e0d8aac8ee893e20f7b9fcb846a5b.jpg)  
(a)

图片摘要：该图主要展示 27.—Separation bubble envelops (shown in grey) for N2–B init。
![](images/4d7a62a19774c0f176cb89f23e4ec5465da634d9f89c1456100a4ce3c9c9674a.jpg)

图片摘要：该图片与Figure 28.—Mach contours of nacelle shape for N2–B baseline (left) and Design 1 这部分内容相关。
![](images/65488984299609ea8860a91a41ab27c6823b28e21db05387e779a9c613327b5e.jpg)  
(b)   
Figure 28.—Mach contours of nacelle shape for N2–B baseline (left) and Design 1 (right) configurations. (a) Symmetric plane. (b) Center plane of outer inlet.

图片摘要：该图主要展示 28.—Mach contours of nacelle shape for N2–B baseline (left) 。
![](images/a2900d366a9f778ad890e595e35056ff79b756c930c10800223687a9a44c441d.jpg)

图片摘要：该图主要展示 28.—Mach contours of nacelle shape for N2–B baseline (left) 。
![](images/b17b1935fb5a48b29ebe90fa7895539c7a38eca3c7b08ad3ea64131d82575f34.jpg)  
Figure 29.—Comparison of cowl shapes in two constant-y sections for N2–B baseline and Design 1 configurations.

图片摘要：该图主要展示 29.—Comparison of cowl shapes in two constant y sections for。
![](images/d51beb5afc0fb95a20ce83b22e8dae6c7e946b7e1c3c22274dfccfcb7badf70b.jpg)

图片摘要：该图主要展示 29.—Comparison of cowl shapes in two constant y sections for。
![](images/ca2ed20346c183d963062aa7bb2adff78874e8aa9f39926e52e72c522603bf5b.jpg)  
x=0.718

图片摘要：该图主要展示 29.—Comparison of cowl shapes in two constant y sections for。
![](images/c82bcba427c1fe005d89df75472b8df88381a602e0fad1e17fcc69871de3cfa1.jpg)  
x= 0.718

图片摘要：该图片与x=0.740；x=0.740这部分内容相关。
![](images/3f6893e47cbe5ebde9f6e52fb26dc127b5fea659c2eebd21c3effb1cbc99d158.jpg)  
x=0.740

图片摘要：该图片与x=0.740；AIP2这部分内容相关。
![](images/44f331ee1a16d08c29f6072a813645c9226be44800d4c1f167f8d4101af0fe9b.jpg)  
x=0.740

图片摘要：该图片与AIP2；AIP2这部分内容相关。
![](images/182dc8fc05f00cb1f96c25da17a07132fec49dd248ef7cad40ada61a00ad8a65.jpg)  
  
AIP2

图片摘要：该图主要展示 30.—Comparison of normalized total pressure contours inside 。
![](images/f480e4b6a005e8f1433e27bb0048933276b7e9743c3bce946f0d8837d5b4c2d3.jpg)  
  
AIP2   
  
  
Figure 30.—Comparison of normalized total pressure $P _ { t }$ contours inside diffuser of side inlet for N2–B Design 1 and Design 2 configurations. Streamwise coordinate x is measured from inlet highlight, and last planes are at fan face (AIP, aerodynamic interface plane). (a) Design 1. (b) Design 2.

<table><tr><td>Initial</td><td>Design 1</td><td>Design 2</td></tr><tr><td>AIP1, 0.0749</td><td>AIP1, 0.0857</td><td>AIP1, 0.0654</td></tr><tr><td>AIP2, 0.0489</td><td>AIP2, 0.0532</td><td>AIP2, 0.0514</td></tr><tr><td>AIP3, 0.0666</td><td>AIP3, 0.0741</td><td>AIP3, 0.0706</td></tr><tr><td>AIP4, 0.0752</td><td>AIP4, 0.0773</td><td>AIP4, 0.0773</td></tr><tr><td>AIP5, 0.0574</td><td>AIP5, 0.0594</td><td>AIP5, 0.0594</td></tr></table>

<table><tr><td>Initial</td><td>Design 1</td><td>Design 2</td></tr><tr><td>AIP1, 0.9650</td><td>AIP1, 0.9628</td><td>AIP1, 0.9583</td></tr><tr><td>AIP2, 0.9758</td><td>AIP2, 0.9724</td><td>AIP2, 0.9726</td></tr><tr><td>AIP3, 0.9644</td><td>AIP3, 0.9624</td><td>AIP3, 0.9624</td></tr><tr><td>AIP4, 0.9401</td><td>AIP4, 0.9368</td><td>AIP4, 0.9368</td></tr><tr><td>AIP5, 0.9553</td><td>AIP5, 0.9523</td><td>AIP5, 0.9523</td></tr></table>

图片摘要：该图主要展示 30.—Comparison of normalized total pressure contours inside 。
![](images/2238b2e353349b523ea87a40a7299b0530fbbee4b7647fee8a1960765e6826f5.jpg)

图片摘要：该图主要展示 30.—Comparison of normalized total pressure contours inside 。
![](images/704a41f83647b05e13907d6baf5b09b0bc8c1d1a0c0b1bc51f6097c1155c4040.jpg)  
Figure 31.—Comparison of circumferential distortion and recovery at various aerodynamic interface planes (AIPs) for N2–B baseline, Design 1, and Design 2 configurations. (a) Circumferential distortion indicator ${ \tt D P C P } _ { \tt a v g }$ . (b) Recovery.

图片摘要：该图主要展示 31.—Comparison of circumferential distortion and recovery at。
![](images/8d1c37375fed151828ae78825c9dc42f9bdb24d6d63efa2b78b14eb88a1b935d.jpg)  
Figure 32.—Comparison of lift coefficient $( C _ { L } )$ at top of climb (TOC) condition and different angles of attack (AOAs) for clean wing and N2–B baseline, Design 1, and Design 2 configurations.

图片摘要：该图主要展示 32.—Comparison of lift coefficient at top of climb (TOC) con。
![](images/243ed08f9b4a86c8cf8f1c52e8b9e55e1d53cf576f0522b7c170b05c0386a8f9.jpg)

图片摘要：该图主要展示 32.—Comparison of lift coefficient at top of climb (TOC) con。
![](images/82db4d6c38c416a3df9c0ded8d3fd97cd63e3a92308b1f57c1ddd44da11944f6.jpg)  
(a)

图片摘要：该图主要展示 32.—Comparison of lift coefficient at top of climb (TOC) con。
![](images/bd41bdbf64e9160fe944c22d945f1b797172ae1398c93953f4c2fbbfc9480fae.jpg)

图片摘要：该图片与Figure 33.—Comparison of section pressure distributions (pressure coefficient ) 这部分内容相关。
![](images/087bc5d4a383d8ab4b86e8b75472b344fddc472aa5fbc86449186be6128eb4f6.jpg)  
Figure 33.—Comparison of section pressure distributions (pressure coefficient $C _ { p }$ ) between N2–B baseline and Design 1 configurations at Mach 0.8, altitude of 35 000 ft, and blade $\alpha = 3 . 5 ^ { \circ }$ . Plots on right are enlargements of sections of plots on left. (a) $y = 0 . 0 1$ . (b) $y = 0 . 1 6 7$ .

图片摘要：该图主要展示 33.—Comparison of section pressure distributions (pressure c。
![](images/c9a7efb83714beec6b5e90da103ea4b49e238921ba611899c82819234ac21a86.jpg)

图片摘要：该图主要展示 33.—Comparison of section pressure distributions (pressure c。
![](images/2fed70e6a2e80cf45c08a7a4659277e58101c5606b28864b8127aee29e4bb445.jpg)  
（a)  
Figure 34.—N3–X configuration with turboelectric distributed propulsion (TeDP) system (from Ref. 31). (a) Overall configuration. (b) Section view of nacelle including fan and electric motor.

图片摘要：该图主要展示 34.—N3–X configuration with turboelectric distributed propul。
![](images/2ef56c5164afb6cbc731679727c02cea718fee8e666f90e55b5d59000a923791.jpg)

图片摘要：该图主要展示 34.—N3–X configuration with turboelectric distributed propul。
![](images/13392826f17411fbb72f44f2d8105ce7befaeb73379705bf44b03cceb570c186.jpg)  
Figure 35.—N3–X configuration with installed mail-slot propulsor. (a) Mail-slot nacelle installed. (b) Inside flow passages.

图片摘要：该图主要展示 35.—N3–X configuration with installed mail slot propulsor. (。
![](images/34add838a7eb05d741db71652eccccf3cfe5f343cc676c8d672bc9dd65cded6c.jpg)  
Rectangular/Transitional/Circular/Transitional/Rectangular   
Figure 36.—Parameterization used for sectional representation of N3–X propulsor, where l signifies component length, H indicates throat height, and $X _ { \mathrm { i n l e t , L E } }$ is x-coordinate value.

图片摘要：该图主要展示 36.—Parameterization used for sectional representation of N3。
![](images/0f87f84ecfe64d80799e1860181197409bcd552e9fdd9911d21610b979c3fd00.jpg)  
Figure 37.—Combined N3–X system of R4 fan stage in scaled inlet A (from Ref. 37).

图片摘要：该图主要展示 37.—Combined N3–X system of R4 fan stage in scaled inlet A (。
![](images/d000f1fded37458b47f33023abb3538b80238e5b08bd7f13d0b5581d0c064d95.jpg)

图片摘要：该图主要展示 37.—Combined N3–X system of R4 fan stage in scaled inlet A (。
![](images/ac3a36614a577a24cabd3682af543f0d71dffc65b7145710706e599c15c2bad0.jpg)  
Figure 38.—Comparison of N3–X body force model results with experimental data and full annulus computational fluid dynamics (CFD) results at 100 percent speed under two inflow conditions: clean and boundary-layer-ingesting flows. (a) Fan pressure ratio. (b) Stage efficiency.

图片摘要：该图主要展示 38.—Comparison of N3–X body force model results with experim。
![](images/fc166bced26b4a59d9230ad91cfbb12682bd1031529cbb26d1cff6482d403fdd.jpg)  
Figure 39.—Comparison of Mach number contours at rotor-stator interface position for N3–X. (a) Full annulus computational fluid dynamics (CFD) (from Ref. 37). (b) Present body force method.

图片摘要：该图主要展示 39.—Comparison of Mach number contours at rotor stator inter。
![](images/05e8905687266ee007f1788e13541986caa878d836fea59219eb31d830573b9d.jpg)

图片摘要：该图主要展示 39.—Comparison of Mach number contours at rotor stator inter。
![](images/0014b1fb54ddbae282233cdeeded458f2dd49759d8bb04a6c65fffd3fcc87229.jpg)

图片摘要：该图主要展示 39.—Comparison of Mach number contours at rotor stator inter。
![](images/af5cfebc3d20f30d7d4444ff9c2622e37c814ade1b0c2cb043d213fb99ff3222.jpg)  
Figure 40.—Comparison of computed sectional pressure coefficients $( C _ { p } )$ using different GO-Flow and OVERFLOW codes and airfoil shapes of clean-wing N3–X for Mach 0.84, angle of attack (AOA) of $2 ^ { \circ }$ , and altitude of 35 000 ft at three spanwise sections y. (a) $y = 0$ . (b) $y = 0 . 2$ . (c) $y = 0 . 8$ .

图片摘要：该图主要展示 40.—Comparison of computed sectional pressure coefficients u。
![](images/bfaf6825bc8a17da650073b30e11d15527fb51f621b12302d8782f066fdd7ec3.jpg)  
Figure 41.—Drag polar of clean wing N3–X for Mach 0.84 and altitude of 35 000 ft.

图片摘要：该图主要展示 41.—Drag polar of clean wing N3–X for Mach 0.84 and altitude。
![](images/f0bf62d6ceee43be46d218863d07e1564fe60a86d243122792ead952b7506ca9.jpg)

图片摘要：该图主要展示 41.—Drag polar of clean wing N3–X for Mach 0.84 and altitude。
![](images/3d19e7934e3696f38a4907273be574d48cb241edcc8572f6129b8d24eb184dbf.jpg)  
Figure 42.—Comparison of fan pressure ratio and entropy change predicted by various methods for the scaled R4 fan installed on N3–X. (a) Fan pressure ratio. (b) Entropy production s.

图片摘要：该图主要展示 42.—Comparison of fan pressure ratio and entropy change pred。
![](images/c600148efea76c1bd71284b1709b342bcab044476b2e4334be9c35bf63d389aa.jpg)  
(a)

图片摘要：该图主要展示 42.—Comparison of fan pressure ratio and entropy change pred。
![](images/97f8e17d83f8b70453a6beab146213ec0295de2f91b317537a83b1148ee59957.jpg)  
(b)   
Figure 43.—Center section contours for N3–X propulsor passage 1 (on symmetry plane). (a) Mach contours. (b) Normalized total pressure $P _ { t }$ contours at Mach 0.84, altitude of 35 000 ft, and angle of attack of $2 ^ { \circ }$ .

图片摘要：该图主要展示 43.—Center section contours for N3–X propulsor passage 1 (on。
![](images/a9b6603264fcc848631abf9182b6c489db60174d291dcc0cd6a45b79b4acf419.jpg)  
(a)

图片摘要：该图主要展示 43.—Center section contours for N3–X propulsor passage 1 (on。
![](images/31973442062103efc1815f49492634fcb2b596842f80f8f952a34a05ef690d8f.jpg)  
(b)   
Figure 44.—Center section contours for the outermost propulsor passage 8. (a) Mach contours. (b) Normalized total pressure $P _ { t }$ contours.

图片摘要：该图主要展示 44.—Center section contours for the outermost propulsor pass。
![](images/64b7b773ec2c86d03a799a60b677c62781192f29de629cbb02cdcb34fe5d9cac.jpg)

图片摘要：该图主要展示 44.—Center section contours for the outermost propulsor pass。
![](images/1062be873cb5b01c7ba10492d0eb14986e299350d876ee0e16d38e8f90ed2286.jpg)  
Figure 45.—Surface pressure contours and visualization of separation bubbles with negative streamwise velocity isosurfaces.

图片摘要：该图主要展示 45.—Surface pressure contours and visualization of separatio。
![](images/057b40d9d77242aa9d2724e34a924ab93308921baeb18ddee24b32313f310fe7.jpg)  
Figure 46.—Comparison of fan face pressure recoveries from inboard to outboard propulsor passages.

图片摘要：该图主要展示 46.—Comparison of fan face pressure recoveries from inboard 。
![](images/ea93befcf1997ee38c5d675611420e0e0ae0fc999c69dec06c76c1d701c3aa79.jpg)

图片摘要：该图主要展示 46.—Comparison of fan face pressure recoveries from inboard 。
![](images/3ace30fbfa5954659e51f6c24506d92d33207c47113fdc400b8fb73befab1050.jpg)  
Figure 47.—N3–X fan performance, affected by inflow conditions: uniform inflow from CFD code SWIFT and ingested boundary layers fed into fans 1 and 8 of N3–X configuration. (a) Fan efficiency. (b) Fan pressure ratio.

图片摘要：该图主要展示 47.—N3–X fan performance, affected by inflow conditions: uni。
![](images/f31b694868fec35a95a8a24eddff723de77c6646a859be7ca4430c63711fa499.jpg)  
Figure 48.—Normalized surface pressure contours and streamlines that flow into passages of N3–X propulsor.

图片摘要：该图主要展示 48.—Normalized surface pressure contours and streamlines tha。
![](images/ed52b41292db0eeae3dfc619e261f92b60859353d1d7922c5a173d5c2b8692a8.jpg)

图片摘要：该图主要展示 48.—Normalized surface pressure contours and streamlines tha。
![](images/a091d484b53e38ff2c43dc47c841682baa2e4738a3e36119460183bce2dc5c2f.jpg)  
(a)

图片摘要：该图主要展示 48.—Normalized surface pressure contours and streamlines tha。
![](images/7ab9dd21dbe635cd7fc5f902fd13320ea050720f9d1c5f93ada3031a05ce58ec.jpg)

图片摘要：该图片与Figure 49.—Mach contours at center section of selected passages for baseline and这部分内容相关。
![](images/56150099579f0835c32ee0262818607e8a9fc08c9067d8c79e4aad993f9911c5.jpg)  
(b)

图片摘要：该图主要展示 49.—Mach contours at center section of selected passages for。
![](images/15e23a8a650ad54bf74cac2514e5b3354b7bcb3b7ad6854649cbfb3cae3927b0.jpg)

图片摘要：该图片与Figure 49.—Mach contours at center section of selected passages for baseline and这部分内容相关。
![](images/49cdc8c5f5fdb9fdd3e0287cd4ee37fe9823ddc9aa49eeda4ef8a422a369f21f.jpg)  
(c)   
Figure 49.—Mach contours at center section of selected passages for baseline and design configurations. (a) Passage 3. (b) Passage 4. (c) Passage 5.

图片摘要：该图主要展示 49.—Mach contours at center section of selected passages for。
![](images/de785c64a800e38d8d8d1bc364238f1574fee5e5e7d3cec9ceeb8172dcb8d938.jpg)
