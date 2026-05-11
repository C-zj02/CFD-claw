# Distributed Electric Propulsion Configuration Trade Study for the SUSAN Electrofan

Leonardo Machado, Timothy Chau, and Brandon M. Lowe Science & Technology Corporation, Moffett Field, California

Jared C. Duensing Ames Research Center, Moffett Field, California

Michelle N. Banchy and Richard L. Campbell Langley Research Center, Hampton, Virginia

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA scientific and technical information (STI) program plays a key part in helping NASA maintain this important role.

The NASA STI Program operates under the auspices of the Agency Chief Information Officer. It collects, organizes, provides for archiving, and disseminates NASA’s STI. The NASA STI Program provides access to the NTRS Registered and its public interface, the NASA Technical Report Server, thus providing one of the largest collections of aeronautical and space science STI in the world. Results are published in both non-NASA channels and by NASA in the NASA STI Report Series, which includes the following report types:

TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counterpart of peer-reviewed formal professional papers, but having less stringent limitations on manuscript length and extent of graphic presentations.   
TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., quick release reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.   
• CONTRACTOR REPORT. Scientific and technical findings by NASA-sponsored contractors and grantees.

CONFERENCE PUBLICATION. Collected papers from scientific and technical conferences, symposia, seminars, or other meetings sponsored or co-sponsored by NASA.   
• SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
• TECHNICAL TRANSLATION. Englishlanguage translations of foreign scientific and technical material pertinent to NASA’s mission.

Specialized services also include organizing and publishing research results, distributing specialized research announcements and feeds, providing information desk and personal search support, and enabling data exchange services.

For more information about the NASA STI Program, see the following:

• Access the NASA STI program home page at http://www.sti.nasa.gov   
• Help desk contact information: https://www.sti.nasa.gov/sti-contact-form/ and select the “General” help request type.

# Distributed Electric Propulsion Configuration Trade Study for the SUSAN Electrofan

Leonardo Machado, Timothy Chau, and Brandon M. Lowe Science & Technology Corporation, Moffett Field, California

Jared C. Duensing Ames Research Center, Moffett Field, California

Michelle N. Banchy and Richard L. Campbell Langley Research Center, Hampton, Virginia

National Aeronautics and Space Administration

Ames Research Center Moffett Field, California 94035

# Acknowledgments

This work is funded by the NASA Convergent Aeronautics Solutions (CAS) project, which is part of the Transformative Aeronautics Concepts Program (TACP) within the NASA Aeronautics Research Mission Directorate (ARMD). Computational resources were provided by the NASA High-End Computing Capability (HECC) Program through the NASA Advanced Supercomputing (NAS) Division at Ames Research Center.

The use of trademarks or names of manufacturers in this report is for accurate reporting and does not constitute an official endorsement, either expressed or implied, of such products or manufacturers by the National Aeronautics and Space Administration.

# Abstract

Distributed electric propulsion (DEP) is a novel propulsion technology that can reduce aviation energy usage and emissions by enabling ultra-high effective bypass ratios. Further improvements to propulsive efficiency can also be obtained when considering configurations that leverage boundary layer ingestion (BLI). However, the design of DEP systems can prove to be challenging at transonic conditions, especially when considering configurations with high levels of aeropropulsive coupling, such as those including BLI. The aeropropulsive benefits of DEP must also trade favorably against increases in drag that come from including many smaller individual propulsive units. In this paper, a DEP configuration trade study is performed for the hybrid-electric SUSAN Electrofan regional jet aircraft concept based on Reynoldsaveraged Navier-Stokes computational design and analysis tools in order to address aeropropulsive design challenges while assessing the potential benefits of various configurations. Results show that configurations with wing-mounted mail-slotted DEP systems require much less thrust at cruise when compared to a non-DEP configuration. However, the DEP configuration developed for BLI was found to require more thrust than the non-BLI configuration due to the thin boundary layers on the wing and the influence of the wing flow field on the inlet flow of the DEP systems. The shaft power required at cruise across all aircraft configurations was also found to be similar when accounting for propulsion-airframe integration effects, although this may be due in a large part to insufficient inlet diffusion. Nonetheless, the DEP configurations were found to experience significantly less thrust-induced drag than the non-DEP configuration, which appears to be one of the main benefits of the technology.

# Nomenclature

$\eta$ = Semispan location

$\eta _ { a }$ = Adiabatic fan efficiency

$\eta _ { \mathrm { t r a n s } }$ = Electrical transmission efficiency

$\gamma$ = Specific heat ratio of air

$f$ = Force vector

$C _ { L }$ = Lift coefficient

$\ C _ { D }$ = Drag coefficient

$C _ { M }$

$C _ { P }$ = Pressure coefficient

$C _ { P } ^ { * }$ = Critical pressure coefficient

$c _ { p }$ cp = Specific heat capacity of air

$c$ = Chord

$h$ = Specific enthalpy

$M$ = Mach number

m˙ = Mass flow rate

$\mathcal { P } _ { \mathrm { f l o w } }$ = Mechanical flow power

$\mathcal { P } _ { \mathrm { s h a f t } }$ = Mechanical shaft power

$R$ = Gas constant of air

$R e$ = Reynolds number

$r$ = Radius

$T$ = Temperature

$\mathbf { \boldsymbol { v } }$ = Velocity vector

$V$ = Actuator zone volume

$x , y , z$ = Cartesian coordinates

# Acronyms

BLI = Boundary Layer Ingestion

CDISC = Constrained Direct Iterative Surface Curvature

DEP = Distributed Electric Propulsion

EAP = Electrified Aircraft Propulsion

LAVA = Launch, Ascent, and Vehicle Aerodynamics

LE = Leading Edge

NLF = Natural Laminar Flow

PAI = Propulsion-Airframe Integration

SUSAN = SUbsonic Single Aft eNgine

# 1 Introduction

The Subsonic Single Aft Engine (SUSAN) Electrofan is an electrified 180-passenger transonic transport aircraft concept targeting the large regional jet market [1], which aims to reduce aviation energy usage and emissions by integrating a number of

advanced aircraft and propulsion system technologies [2]. Some of the main technologies include electrified aircraft propulsion (EAP), distributed electric propulsion (DEP), boundary layer ingestion (BLI), and natural laminar flow (NLF). At the core of the aircraft concept is a hybrid-electric powertrain primarily driven by a hydrocarbon fuel-burning aft fuselage propulsor, and megawatt-class power generators, which support wing-mounted electric propulsors.

Under nominal operating conditions, the aft fuselage propulsor produces 35% of the total aircraft thrust, while the wing propulsors are responsible for the remaining $6 5 \%$ . The aft fuselage propulsor is an advanced BLI turbofan engine [3], which also produces additional mechanical shaft power to be converted to electric power, via the power generators, to drive the wing-mounted propulsion systems. These wing propulsors can assume a wide range of configurations, given the expanded design space enabled by the SUSAN Electrofan’s hybrid-electric propulsion system architecture.

One possible avenue is a DEP configuration, which can significantly improve propulsive efficiency by increasing the effective bypass ratio of the complete propulsion system. DEP can also be combined with BLI to further enhance propulsive efficiency through the ingestion of low-momentum flow over the surfaces of the wings. However, such a configuration closely integrates the airframe and propulsion systems, invariably increasing the levels of coupling between aerodynamics and propulsion. Although this can be used to an advantage, for example by introducing the benefits of BLI as described or by enhancing high-lift performance, the successful integration of the two systems can be difficult to achieve. This is especially true when considering aircraft operating in the transonic flight regime where designs can be sensitive to shock formation [4, 5, 6, 7].

Current research is focused on investigating the merits of DEP configurations developed for the SUSAN Electrofan through the application of computational fluid dynamics (CFD)-based aeropropulsive design and analysis tools capable of capturing the relevant tradeoffs between aerodynamics and propulsion, and hence capable of addressing the integration design challenges. Specifically, a DEP configuration trade study is being performed [6, 7], with the main goal of obtaining estimates of the relative potential benefits of DEP configurations with and without BLI at cruise. As shown in Figure 1, three electric wing-mounted propulsion system configurations are being considered, which include a non-DEP configuration, a DEP configuration, and a DEP-BLI configuration.

The first configuration, shown in Figure 1a, serves as a non-DEP baseline configuration with two underwing podded propulsors modeled based on a modern highbypass ratio turbofan. The second configuration, shown in Figure 1b introduces the DEP concept with two underwing arrays of 8 propulsors distributed along the span of each wing for a total of 16 ducted fan units. These are integrated into a mail-slot nacelle configuration to reduce wetted area penalties, although at the cost of higher levels of propulsor-to-propulsor coupling. The third and final configuration, shown in Figure 1c, integrates the mail-slot nacelles directly onto the lower surface of the wings to benefit from both DEP and BLI. These trade study configurations are herein referred to as Configurations 1, 2, and 3, respectively.

Previous work [6, 7] introduced this study and presented preliminary investi-

图片摘要：该图主要展示 1: Concepts of the SUSAN Electrofan trade study configuratio。
![](images/b9b72259452a62f4b77eb252b9088117db67c88701f6b6b7715150602f162bac.jpg)  
(a) Configuration 1 (non-DEP)

图片摘要：该图主要展示 1: Concepts of the SUSAN Electrofan trade study configuratio。
![](images/1802689380019f252164125a761754e5e04ce8f6d90ba31f422e3f45c7f4fb7b.jpg)  
(b) Configuration 2 (DEP)

图片摘要：该图主要展示 1: Concepts of the SUSAN Electrofan trade study configuratio。
![](images/3b714c58a64156c58665b633c71601c47238d2b7d8a1c3782af931a351f3e143.jpg)  
(c) Configuration 3 (DEP + BLI)   
Figure 1: Concepts of the SUSAN Electrofan trade study configurations. [6].

gations into the design and performance of the three configurations. Conceptual models of the propulsors were first developed based on top-level aircraft requirements and subsequently used to develop three-dimensional representative aircraft configurations. For Configurations 2 and 3, this involved the development of representative mail-slot nacelle geometries with high sweep and splitters, that could meet the thrust requirements at the design fan pressure ratios (FPRs), while encompassing the aeropropulsive trades between bypass ratio, viscous drag, and interference drag from propulsor-to-propulsor coupling. These propulsion systems were then integrated with wing-body models of the SUSAN Electrofan and configuration advantages and disadvantages were assessed. Moreover, key design parameters and challenges were identified, with special attention on those associated with propulsion-airframe integration (PAI).

The impact of PAI on aerodynamic and propulsion system performance was most significant for Configuration 3 given the much higher levels of aeropropulsive coupling [7]. Indeed, CFD-based aeropropulsive analysis indicated a significant influence from the flow field of the wing on the inlet flow of the nacelle, resulting in much lower levels of inlet diffusion. This led to the formation of internal shocks, which diminished the aerodynamic and propulsive efficiency of Configuration 3. Results also suggested negligible benefits from BLI as a result of the thin boundary layers developed over the wings, at least relative to the capture area of the wing propulsors. However, the BLI configuration was found to have much lower wetted area compared to the non-BLI configuration, implying a commensurate reduction in skin-friction drag.

Building on previous work, the present paper aims to address the uncertainties surrounding the previously obtained relative performance estimates by introducing aerodynamic redesign efforts consistently applied to each trade study configuration.

Indeed, with Configuration 3 especially subject to high levels of aeropropulsive coupling, an objective assessment of its performance relative to Configurations 1 and 2 demands a more integrated design process to achieve a similar level of qualitative performance. This is achieved through the application of a knowledge-based aerodynamic design framework based on the RANS equations to wing-body models of the three configurations, with a focus on wing redesign. For Configuration 3, this includes the integrated wing propulsors and hence nacelle redesign as well. The T-tail and aft fuselage propulsor are then re-integrated with the wing-body models for evaluating full-configuration aerodynamic and propulsion system performance.

In order to account for differences in airframe and propulsor performance between each trade study configuration, the present paper uses a power balance method to simulate steady, level flight. This involves a trimming of each aircraft configuration in lift and drag with respect to angle of attack and the thrust input to each propulsor. Estimates of relative aerodynamic and propulsion system performance are then obtained based on cruise thrust and drag, mechanical flow power, and mechanical shaft power. These measures will be described in more detail in Section 5.

The paper is organized as follows. Section 2 describes the airframe and propulsion system design requirements, while Section 3 presents the computational tools and capabilities used to perform aeropropulsive design and analysis. Section 4 presents the aerodynamic redesigns for the three trade study configurations, with the full-configuration analysis results presented in Section 5. Conclusions are presented in Section 6.

# 2 Airframe and Propulsion System Design Requirements

As presented in Machado et al. [6, 7], representative aircraft models are developed from top-level aircraft requirements similar to those of a Boeing 737-8. Specifically, the propulsion systems are sized based on top-of-climb (TOC) thrust requirements at Mach 0.785 and 11,278 km (37,000 ft), which includes the excess thrust required to satisfy a 300 ft/min climb rate. The thrust requirement is 11,500 lb [3], and a 35:65 thrust split is assumed for the aft fuselage propulsor and the wing-mounted propulsion systems, respectively.

For the underwing podded propulsors of Configuration 1, a design FPR of 1.47 is considered based on the R4 fan [8]. For Configurations 2 and 3, the ducted fan units are based on previous work on the NASA N3-X hybrid wing-body, and include two counter-rotating fans with a net fan pressure ratio of 1.25 [9]. The design requirements of the ducted fan units are imposed on the mail-slot nacelles of the DEP and DEP-BLI configurations equally without any prior assumptions on the impact of PAI of the coupled flow field. In this way, PAI effects can become more apparent when performing the aerodynamic redesigns. A summary of the design requirements is provided in Table 1.

For the airframes of each trade study configuration, a typical design lift coefficient is assumed at 0.500, which is considered sufficient for the purposes of this study. These design requirements are used to size the wing propulsion systems based on CFD simulations of the wing-body models shown in Figure 2. Note that

Table 1: Wing propulsor design requirements for each SUSAN Electrofan trade study configuration.   

<table><tr><td>Parameter</td><td>Configuration 1</td><td>Configuration 2</td><td>Configuration 3</td></tr><tr><td>Arrangement</td><td>Non-DEP</td><td>DEP</td><td>DEP + BLI</td></tr><tr><td>Number of propulsors</td><td>2</td><td>16</td><td>16</td></tr><tr><td>Number of fans, per prop.</td><td>1</td><td>2</td><td>2</td></tr><tr><td>Mass flow rate, per prop. (kg/s)</td><td>163.0</td><td>33.6</td><td>33.6</td></tr><tr><td>Fan pressure ratio</td><td>1.47</td><td>1.25</td><td>1.25</td></tr></table>

图片摘要：该图主要展示 1: Wing propulsor design requirements for each SUSAN Electro。
![](images/60e85da9d3971f3248bf70f91c39c4f3b243cdd239de48e1d362a074cdd10da0.jpg)  
(a) Configuration 1

图片摘要：该图主要展示 1: Wing propulsor design requirements for each SUSAN Electro。
![](images/8444fa886c6801916a0667994fa254dd39f9728e976adf176bf604850d9a5d8f.jpg)  
(b) Configuration 2 (DEP)

图片摘要：该图主要展示 2: Representative wing body models used to size the integrat。
![](images/6029d1812699ec86f7b394b570609031cbd9fe7397fb7f0a2d24f91618a87eb7.jpg)  
(c) Configuration 3 (DEP + BLI)   
Figure 2: Representative wing-body models used to size the integrated wing and wing propulsor designs.

these aircraft geometries do not include pylons, as required by Configurations 1 and 2. Although this leads to more conservative relative performance estimates for Configuration 3, this simplification significantly reduces the complexity of the aeropropulsive design problems and are therefore omitted as a first step.

As presented in [6, 7], the wing propulsors are simplified and consist only of a hub and nacelle. Furthermore, for the DEP systems, the mail-slot nacelle geometries are characterized by fictitious square cross-sectional ducts, as opposed to ducts that smoothly vary from square to circle and back to square from the nacelle highlight to the nacelle exit. This is done to significantly reduce the complexity of the transonic design problems. However, care is taken to maintain a similar thrust per unit capture area as that of an isolated ducted fan unit in the development of the baseline designs. This yields similar overall aeropropulsive trends and tradeoffs to first order.

# 3 Computational Tools and Capabilities

This section presents the computational tools and capabilities used to develop and evaluate the aeropropulsive performance of the aircraft models representing the SU-SAN Electrofan trade study configurations. For performing aeropropulsive analysis, the present paper uses the Launch, Ascent, and Vehicle Aerodynamics (LAVA) framework [10], which includes a flow solver for the RANS equations and an actuator zone method for modeling propulsor thrust. Although the LAVA framework includes recently developed gradient-based aerodynamic shape optimization capabilities [11], its geometry control and mesh deformation capabilities are not yet sufficiently mature to handle the geometric complexities of the integrated wing and wing propulsor designs considered in this work. This is mainly due to the many component intersections between the mail-slot nacelle and the wing, and the mailslot nacelle geometry itself. Instead, the present paper uses the Constrained Direct Iterative Surface Curvature (CDISC) method [12], which is a knowledge-based aerodynamic design framework also based on the RANS equations that provides the means for direct surface control around these component intersections. Details on the LAVA and CDISC frameworks are provided in the following sections.

# 3.1 LAVA Framework

The LAVA framework is used to perform high-fidelity aeropropulsive analysis. Specifically, the present paper uses the LAVA curvilinear flow solver with structured overset meshes, and considers the RANS equations with the Spalart-Allmaras (SA) turbulence model [13], including rotation curvature [14] and quadratic constitutive relationship corrections [15] (SA-RC-QCR2000). Second-order finite-differences are used for spatial discretization, and convective fluxes are evaluated using a modified Roe scheme with third-order upwind-biased flux reconstruction and the Koren flux limiter [16, 17].

The discrete set of nonlinear equations is marched in pseudo-time to steady-state using automatic CFL ramping to accelerate convergence. At each pseudo-time step, the linear system is solved using the preconditioned generalized minimal residual (GMRES) algorithm [18]. The preconditioner is obtained from an incomplete lowerupper factorization of a first-order approximation of the residual Jacobian.

Propulsion is modeled through an actuator zone method [19], where thrust is distributed over a subset of volume grid nodes representing a given fan through source terms added to the momentum and energy equations. This method has been previously employed in applications involving BLI and PAI [20, 21] and is considered sufficient for resolving aeropropulsive coupling effects to first order. In this work, constant thrust distributions are considered with no torque.

# 3.2 CDISC Framework

For the aerodynamic redesign of each trade study configuration, the CDISC method [12] is used, which is a knowledge-based aerodynamic design framework coupled with a RANS-based flow solver. In this method, airfoil designs are modified at specified

图片摘要：该图主要展示 3: Planform view of the SUSAN Electrofan wing body geometry 。
![](images/95969947bacfc26c15e02da07d37b40ea1d0f19b9af0c9ef0add300bc795c165.jpg)  
Figure 3: Planform view of the SUSAN Electrofan wing-body geometry showing the 11 design stations referenced by CDISC in blue. The numbered stations 2, 5, 8, and 11 are the locations of sample design results presented in Section 4.

design stations on a wing based on target pressure distributions. Figure 3 shows the design stations considered for the wing redesign efforts presented in Section 4, based on best practices. The target pressures are automatically generated from flow constraints based on common engineering parameters, such as lift and pitching moment coefficients, and objectives like reduced shock strength. Prescribed geometry and flow sensitivity derivatives from a knowledge base are then used to drive the deformation of the airfoils and achieve target pressures while subject to a variety of geometric constraints, for example, maximum thickness and minimum leading-edge radius. The use of prescribed sensitivity derivatives eliminates the need to compute them, yielding design times on the order of a given baseline analysis.

The CDISC framework is modular and can be easily coupled with a variety of flow solvers. In the present paper, the USM3D-ME unstructured flow solver is used [22]. This flow solver is interfaced with the CDISC module, along with a method for modifying the grid as shown in Figure 4. The USM3D-ME code is a second-order, cell-centered, upwind RANS solver that runs on mixed-element grids. Analysis runs use the SA-RC-QCR2000 turbulence model to maintain similarity with the LAVA curvilinear flow solver.

For modeling propulsion during the aerodynamic redesign problems, a boundary condition method is used to specify an FPR across the fan inlet and exit planes, with the fan exit set to jet exhaust conditions. However, in order to maintain consistency with LAVA, parameters are set to produce similar thrust levels across the two flow solvers. Comparisons of initial solutions generated by the two flow solvers also showed good agreement based on surface pressures, forces, and moments. This confirmed that design changes made using USM3D-ME with CDISC would be accurately reflected in the subsequent aeropropulsive analyses performed with the LAVA curvilinear flow solver.

图片摘要：该图主要展示 3: Planform view of the SUSAN Electrofan wing body geometry 。
![](images/24bcbfdc30dee05aa81147ddac55b09b52b60e0c5a7414d5829c5687f5769f52.jpg)  
Figure 4: Flow chart of the CDISC design method.

# 4 Aerodynamic Redesign

The main goal of the aerodynamic redesign using CDISC is to reduce the influence of adverse PAI effects for each of the SUSAN Electrofan trade study configurations in order to fairly assess their relative aerodynamic and aeropropulsive performance. This is achieved by targeting consistent aerodynamic features across the three configurations. In all three cases, aerodynamic redesign focuses on the wing as the main design component, as described in Section 3.2. For Configuration 3, however, the mail-slot nacelle is also redesigned using CDISC to accommodate the higher levels of aeropropulsive coupling. This will be discussed further in Section 4.3.

# 4.1 Configuration 1

For Configuration 1, the underwing podded propulsor covers only a small fraction of the total wing span and therefore has a relatively small region of impact on the aerodynamics of the wing. As such, the wing design requires minimal changes from the baseline geometry. In order to begin the aerodynamic redesign, target pressures and geometric constraints are established based on CDISC best practices. The target pressures are automatically generated to hold the sectional lift coefficient at a given design station constant while providing a smooth upper surface pressure distribution that also decreases shock strength. Specifically, CDISC aims to introduce a mild adverse pressure gradient to move the shock further aft, while increasing aft loading to reduce shock strength. To avoid boundary layer separation and excessive pitching moments, however, a maximum value on aft loading is also introduced. Geometric constraints include constant section maximum thickness for structural considerations and curvature limits to improve off-design performance. Geometric smoothing in the chordwise and spanwise directions are also included by default in the CDISC design process to ensure continuity in the final geometry.

Figure 5 shows the pressure and geometry data at the four sample design stations presented in Figure 3. The CDISC target pressures are also included for reference. In addition, note that the airfoils are also shown with local twist removed to more effectively visualize any changes to their shape. Comparing the design and target pressures, a good agreement is achieved, indicating that CDISC is successful at

producing a geometry that provides the desired flow features. From Figure 5a, it can also be seen that the CDISC design process is successful in removing the forward shock due to the presence of the propulsor, which causes flow acceleration over the upper wing surface. At all other design stations, minimal changes are required to achieve the desired flow characteristics across the wing.

The changes to the spanwise characteristics introduced through the CDISC redesign effort are shown in Figure 6. The agreement seen in the sectional lift distribution shown in Figure 6a confirms that the redesign is successful in maintaining the spanwise loading of the baseline configuration. The changes to the sectional pitching moment included in Figure 6b are reflective of the CDISC design strategy to reduce shock strength by increasing aft loading and moving the shock further aft. Geometric characteristics, shown in Figures 6c and 6d, are the result of airfoil changes required to match target pressures and are smoothed throughout the design.

Overall, the Configuration 1 redesign effort requires minimal changes to the baseline geometry due to the limited region of aerodynamic influence the propulsor imparts on the wing. The design provides the desired result of smooth pressure isobars, reducing the influence of the podded propulsor inboard, and producing a wing with consistent aerodynamic features across the three configurations.

# 4.2 Configuration 2

The CDISC redesign of Configuration 2 follows the same procedure as Configuration 1, with the target pressures and geometric constraints unchanged between the two configurations. However, since the DEP system covers a larger spanwise extent compared to the podded propulsor of Configuration 1, the PAI effects are present over a larger range of stations for Configuration 2. Figure 7 shows the pressure and geometry data of the baseline and design solutions for Configuration 2. The effect of the DEP system can most notably be seen in the baseline solution at Station 5, as shown in Figure 7b, where the lower surface leading edge shows excess acceleration compared to other stations. While this feature was reduced during the design process, the lower surface baseline solution for Configuration 2 did not require significant changes to meet the redesign objectives. The spanwise characteristics, illustrated in Figure 8, provide further confirmation that the Configuration 2 redesign effort achieved the design objectives and produces similar aerodynamic features to those of Configuration 1.

# 4.3 Configuration 3

The aerodynamic redesign problem of Configuration 3 involves significantly higher levels of aeropropulsive coupling due to its highly integrated wing and DEP systems, which result in substantially more adverse PAI effects to be addressed on the baseline geometry. This led to challenges in achieving converged flow solutions at the design FPR of 1.25 using both the LAVA curvilinear flow solver and USM3D-ME. Preliminary investigations showed that this was caused by the formation of shocks at the inlet of the mail-slot nacelle due to the presence of the wing, which accelerated the flow into the propulsors. This effect was most severe for the inboard propulsor,

图片摘要：该图片与(a) Station 2；(b) Station 5这部分内容相关。
![](images/90be268d400e9ceef39a4ff6d6e01d69645b300fea0e4cc79a6de771420e4462.jpg)  
(a) Station 2

图片摘要：该图主要展示 5: Baseline and design pressure and geometry data for Config。
![](images/9beda076fae03c4bdc01db5d353114559ca772a349e69cdb690e273de20692be.jpg)  
(b) Station 5

图片摘要：该图主要展示 5: Baseline and design pressure and geometry data for Config。
![](images/08bfec5d2043eec87b37803a2a09b5f3821277992e2f44d0bce43c3f1bc92647.jpg)  
(c) Station 8

图片摘要：该图主要展示 5: Baseline and design pressure and geometry data for Config。
![](images/5f7138e9455f2781d0d7436eb8ce3e0fd19af6c17bed273463cffb4f01fbf295.jpg)  
(d) Station 11   
Figure 5: Baseline and design pressure and geometry data for Configuration 1 (C1) at the four sample stations.

图片摘要：该图主要展示 5: Baseline and design pressure and geometry data for Config。
![](images/120d707f0384e41cef3aa4ffd7776a43b530498a56f15828140303975ae8cf1e.jpg)  
(a) Sectional lift coefficient

图片摘要：该图主要展示 5: Baseline and design pressure and geometry data for Config。
![](images/5edbb1bcec78700a85933fe8d17bacbdaba20b53523041573e5cae2aaed54f5f.jpg)  
(b) Sectional pitching moment

图片摘要：该图主要展示 5: Baseline and design pressure and geometry data for Config。
![](images/1bf36de319482940c3ab423f4023587edcf48ba0a73f2361b332cb18494b04ed.jpg)  
(c) Leading-edge radius nondimensionalized by local chord

图片摘要：该图主要展示 6: Baseline and design spanwise characteristics for Configur。
![](images/5d1b61bffed99b7a2eea662ab603fa3f45e799c1165aaf35e672683cdf75b16f.jpg)  
(d) Twist in degrees   
Figure 6: Baseline and design spanwise characteristics for Configuration 1 (C1). All data are plotted against nondimensionalized semispan location (η).

which experienced a fully choked inlet. The inability to operate the propulsion system at the desired FPR resulted in the CDISC redesign effort being divided into two stages: a nacelle redesign, followed by the wing redesign. These redesign stages are discussed in the following two subsections.

# 4.3.1 Nacelle Redesign

The main objective of the CDISC redesign of the mail-slot nacelle is to reduce the inlet shock and unchoke the inboard-most propulsor to enable operation at the design FPR of 1.25. A converged baseline flow solution is required to perform CDISC design, which was not possible on the baseline geometry of Configuration 3 due to the adverse effects described above. To address this problem, the flow solver inlet fan faces were first set to boundary conditions representative of subsonic inflow/outflow planes. This decouples the fan faces and allows the exit fan face to operate normally without the inlet causing the solution to terminate. Although such a solution is not

图片摘要：该图主要展示 6: Baseline and design spanwise characteristics for Configur。
![](images/6a408a6e0f245ff8b232da6d4b398ae5f60c68a267e0a403a9587c00e38def20.jpg)

图片摘要：该图片与(a) Station 2；(b) Station 5这部分内容相关。
![](images/d70d3ed3d972a3a4615c045350dc38558835291e6b6f095e8613ca4878cae54d.jpg)  
(a) Station 2

图片摘要：该图片与(b) Station 5；(c) Station 8这部分内容相关。
![](images/302716b4a8ca2afe58b3577d9993df268d598ed7961838aa7c3ce8916caf489b.jpg)

图片摘要：该图片与(b) Station 5；(c) Station 8这部分内容相关。
![](images/55ab4455e14417a55ea83068f16eb582a4c61d145b587650f8f37f8e0b88bef7.jpg)  
(b) Station 5

图片摘要：该图片与(c) Station 8；(d) Station 11这部分内容相关。
![](images/538f4ae5a0ac215348c15db1b0f3e3cf32bf2d5694b2b18a687edb11f0c61c52.jpg)

图片摘要：该图片与(c) Station 8；(d) Station 11这部分内容相关。
![](images/e5fb901607f47beae844adc2a6349b414cee9a73bbf90c1849e8982fa65ee2ef.jpg)  
(c) Station 8

图片摘要：该图主要展示 7: Baseline and design pressure and geometry data for Config。
![](images/4dba64602820ec951471d8afffaca328ec55c92d11823f14a44e23f7ae3886c2.jpg)

图片摘要：该图片与(d) Station 11；Figure 7: Baseline and design pressure and geometry data for Conf这部分内容相关。
![](images/0baf702ce70e6624dabc48408cfce1bd453e77b943deb20f43531e9dcad746b2.jpg)  
(d) Station 11   
Figure 7: Baseline and design pressure and geometry data for Configuration 2 (C2) at the four sample stations.

图片摘要：该图主要展示 7: Baseline and design pressure and geometry data for Config。
![](images/4f7c92444b87a6e10950e395b68c7d4e44fe862075d817c39d59925e1d9f6be3.jpg)  
(a) Sectional lift coefficient

图片摘要：该图主要展示 7: Baseline and design pressure and geometry data for Config。
![](images/d78cb5f0bf47ae5844510f0056b8b6f78f5d4c54cd4048522ec0637f0919439d.jpg)  
(b) Sectional pitching moment

图片摘要：该图主要展示 7: Baseline and design pressure and geometry data for Config。
![](images/2d9fa9d19804a4dec834b1ca08bd1f861f21235567e51eddb60804d8d084a8aa.jpg)  
(c) Leading-edge radius nondimensionalized by local chord

图片摘要：该图主要展示 8: Baseline and design spanwise characteristics for Configur。
![](images/48ccd760c9c5b3a6a54afe32512ece0bf5efb2f0257e016af8bae1822e532408.jpg)  
(d) Twist in degrees   
Figure 8: Baseline and design spanwise characteristics for Configuration 2 (C2). All data are plotted against nondimensionalized semispan location (η).

representative of a properly modeled propulsion system within USM3D-ME, this was sufficient for initiating the CDISC design process. Once the design reduced the inlet shock, a converged flow solution could be obtained on the new geometry with both the inlet and exit fan faces set to the design FPR as intended.

Figure 9 shows the CDISC design stations for the mail-slot nacelle. These include two design stations for the inboard vertical nacelle, and eight design stations for the horizontal nacelle, with one horizontal nacelle station per propulsor. The stations labeled in Figure 9 are used as sample stations, which include one vertical nacelle station (V1) and three horizontal nacelle stations (H1, H4, and H8). No design is performed on the outboard vertical nacelle since the baseline solution does not have inlet shocks in that region.

In order to preserve as much of the baseline internal flow path as possible, the CDISC design region is limited through a simple flap constraint, which deflects the leading edge of an airfoil forward of a hinge line, while locking the remaining surfaces.

图片摘要：该图主要展示 9 shows the CDISC design stations for the mail slot nacelle.。
![](images/16d3568ea805a7dc5b1269f1721bc42a93cce446902d53f24a214b8172d664ca.jpg)  
Figure 9: Front view of Configuration 3 showing the 10 design stations used in CDISC design of the engine nacelle in blue. The numbered stations (V1, H1, H4, and H8) are the locations of the sample design results.

In the present paper, the hinge line is set to an $x / c$ location of 0.30 for all design stations except for those of the inboard-most propulsor, which required a further aft hinge line of $x / c = 0 . 4 0$ to properly unchoke it. The flap constraint is used to deflect the geometry down, effectively opening the inlet of the mail-slot nacelle until the flow speed over the flap reduces below a user-specified maximum Mach number. For this design problem, a maximum Mach number of 0.95 is specified.

The results shown in Figure 10 illustrate the flap deflection and its effectiveness toward eliminating the inlet shocks. The pressure plots include a horizontal dashed line to indicate the critical pressure coefficient, $C _ { P } ^ { * }$ , which helps visualize that the supersonic flow on the upper surface of the baseline geometry has been reduced to subsonic conditions using the leading-edge flap. It can be seen, however, that the flap causes an increase in flow speed on the external mail-slot nacelle surface.

The upper surface pressures also show a discontinuity in pressure level that is connected with a linear region, around $x / c = 0 . 4 0 { - 0 . 7 0 }$ depending on the station. This represents the region between the two fan faces modeled in USM3D-ME, where there is no grid and therefore no flow solution. From Figure 10, it can be seen that the inboard stations had stronger inlet shocks on the baseline solution and therefore required more flap deflection to reduce the velocity of the flow than the outboard stations.

Figure 11 shows surface pressure contours over the baseline and design geometries, which highlight some of the main improvements in the flow field around the mail-slot nacelle. Figure 11a, for example, shows the elimination of the inlet shocks, highlighting the effectiveness of the flap design approach used in CDISC. Figures 11b and 11c provide a closer look at the inboard-most propulsor, which show that the flap deflection of both the horizontal and vertical nacelles successfully unchoke the propulsor inlet, albeit while increasing the shock strength over the external nacelle surface. Overall, the CDISC redesign of the mail-slot nacelle is considered a success given that it enables operation at the design FPR. The aerodynamic redesign of the wing is performed next, with the propulsion system geometry held constant.

图片摘要：该图主要展示 11 shows surface pressure contours over the baseline and des。
![](images/f9a62c7eddafbfc4b1137e62c50594986a20025281f9399ff73ffae972ed31d8.jpg)

图片摘要：该图主要展示 11 shows surface pressure contours over the baseline and des。
![](images/9813f8102c8a37409792351d10e91933ada6a4d82147502c0aeb50010b53c689.jpg)

图片摘要：该图主要展示 11 shows surface pressure contours over the baseline and des。
![](images/f6672d2d53a7e911158338df57fa7552669deb8d46b33c40dc61f610d78a385e.jpg)  
(a) Station V1

图片摘要：该图片与(b) Station H1；(c) Station H4这部分内容相关。
![](images/67325caccc09eaf7e1336d5be17dc85aaef1b842561d93533de54b8a7a6dc249.jpg)  
(b) Station H1

图片摘要：该图片与(c) Station H4；(d) Station H8这部分内容相关。
![](images/b40199ef0732c7305c62035c918b71cd5f2cde5ee87b18f16af8332b0c65144c.jpg)

图片摘要：该图主要展示 10: Baseline and design pressure and geometry data for Confi。
![](images/0e849bcd8fb65f9dd636f115367558b3bc9c0892a29848a43e0d517b8ed994eb.jpg)

图片摘要：该图片与(c) Station H4；(d) Station H8这部分内容相关。
![](images/247be5d1e2aeb9f9a9c65f1191c2881f09d290f60e4fd83762e93b96622a7afa.jpg)  
(c) Station H4

图片摘要：该图片与(d) Station H8；Figure 10: Baseline and design pressure and geometry data for Con这部分内容相关。
![](images/9453786c05aaa5e4364065afae34a16ef34bea52f0cec69a27eae063bee16164.jpg)  
(d) Station H8   
Figure 10: Baseline and design pressure and geometry data for Configuration 3 (C3) at the four sample stations.

图片摘要：该图主要展示 10: Baseline and design pressure and geometry data for Confi。
![](images/f265956ea4feffe87c178a061feac3722d6af6c259a1534c0265acdf7091a7d2.jpg)  
(a) Front view of the mail-slot nacelle, highlighting inlet shock reduction

图片摘要：该图主要展示 10: Baseline and design pressure and geometry data for Confi。
![](images/c89e23ffac4aa24c0ac87f119ca509739fe2e17d05b74d9ee86cbe5659e125f6.jpg)  
(b) Zoomed view of the inboard-most propulsor highlighting the unchoked inlet flow.

图片摘要：该图主要展示 10: Baseline and design pressure and geometry data for Confi。
![](images/154ce00325c9ba159f3085487a23a224a51762ca219c88b515f85c4ff85fd814.jpg)  
(c) Zoomed view of inboard-most propulsor showing the increased shock strength over the external mail-slot nacelle surface.   
Figure 11: Baseline and design surface pressure contours for Configuration 3.

# 4.3.2 Wing Redesign

For Configuration 3, the aerodynamic redesign of the wing involves many of the same design objectives as Configurations 1 and 2, but with additional constraints introduced to accommodate the complexity of the integrated wing and DEP systems. For example, since much of the lower wing surface is internal to the propulsion system, geometric constraints are introduced to lock these regions of the wing. This also ensures that the propulsion system remains fixed in space and does not rotate as the wing design is twisted to match target pressures. For the target pressures, similar constraints are included as with the previous two configurations to control the pressure gradient, shock location, and aft loading, reducing shock strength and providing a more uniform isobar distribution across the span.

For integrated quantities such as sectional lift and pitching moment, the internal flow from the propulsors complicate their calculations and result in quantities that are difficult to relate to Configurations 1 and 2, whose components are less coupled. For example, at total lift-matched conditions, the wing of Configuration 3 carries more lift compared to those of Configurations 1 and 2, which is likely due to the need for overcoming the negative lift generated by the underwing BLI mail-slot nacelle. The wing stations that overlap the propulsion system are also unable to maintain as much aft loading without causing boundary layer separation.

Nonetheless, Figures 12 and 13 show the chordwise and spanwise characteristics for the resulting design geometry. As evidenced by the greater mismatch in the design and target pressures, it is clear that the aerodynamic wing redesign of Configuration 3 is notably more difficult due to the added geometric constraints. However, the final design of Configuration 3 is successful in providing a wing that accounts for the PAI effects associated with the DEP-BLI propulsion system, and that more closely matches the aerodynamic characteristics of Configurations 1 and 2.

# 5 Full-Configuration Aeropropulsive Analysis

In order to assess the potential relative benefits of DEP with and without BLI for the SUSAN Electrofan, the refined wing and wing propulsor geometries presented in Section 4 are integrated into full-configuration aircraft models and subjected to aeropropulsive analysis. These representative aircraft models are shown in Figure 14 and include the horizontal and vertical tails, as well as the aft fuselage propulsor design presented in Machado et al. [23]. With the exception of the wing and wing propulsors, all airframe and propulsion system components are common across each of the configurations.

For performing aeropropulsive analysis, the LAVA curvilinear flow solver presented in Section 3 is used, which models propulsor thrust via an actuator zone method. In the present paper, constant thrust distributions are considered with no torque for each propulsor to reduce computational cost. Although such an approach is considered a lower fidelity method, the source terms added to the momentum and energy equations over each actuator zone adequately captures the influence of

图片摘要：该图片与(a) Station 2；(b) Station 5这部分内容相关。
![](images/65f585ce7fedd13a413b08380402587d7ec3e1e4708ac4638d674fffc3c1e6d6.jpg)

图片摘要：该图片与(a) Station 2；(b) Station 5这部分内容相关。
![](images/ce666eecb5138168125be5c747aeb7b7cc30294593e2945a17de5e32426f3869.jpg)  
(a) Station 2

图片摘要：该图片与(b) Station 5；(c) Station 8这部分内容相关。
![](images/9ca5dffe7cf604c7a25470763d91780f11e6b5a3ad3cdfd5938b4f327f1b6a8d.jpg)

图片摘要：该图片与(b) Station 5；(c) Station 8这部分内容相关。
![](images/716c200ccb94a88b392ab242f6bd2a8a8263373a6e490f3886768162f879443c.jpg)  
(b) Station 5

图片摘要：该图片与(c) Station 8；(d) Station 11这部分内容相关。
![](images/f07f35878ee846a695dccd0a252768dc23cc6fdb56893ace64283beee954943b.jpg)

图片摘要：该图片与(c) Station 8；(d) Station 11这部分内容相关。
![](images/cbd5fc195ad0b4043049910dab29f924703bb56cf5193abccb106a6fcb5ed256.jpg)  
(c) Station 8

图片摘要：该图主要展示 12: Baseline and design pressure and geometry data for Confi。
![](images/cd74eddff76b3bdb15f094528ec402c249fabbd75e74b1ee81c40eeb873bf76d.jpg)

图片摘要：该图片与(d) Station 11；Figure 12: Baseline and design pressure and geometry data for Con这部分内容相关。
![](images/ea69796fb3433f205609b3f44a53bafb5b2b8a04872ea253ce4099605dd80115.jpg)  
(d) Station 11   
Figure 12: Baseline and design pressure and geometry data for Configuration 3 (C3) at the four sample stations.

图片摘要：该图主要展示 12: Baseline and design pressure and geometry data for Confi。
![](images/2768b0257b8e829c50a933384609ee98b7447c2af9d8cc11094adf69b0815733.jpg)  
(a) Sectional lift coefficient

图片摘要：该图主要展示 12: Baseline and design pressure and geometry data for Confi。
![](images/502cfce08770a19d651e3f36230779df56e299c134d3e900a4f056b6d43ed31a.jpg)  
(b) Sectional pitching moment

图片摘要：该图主要展示 12: Baseline and design pressure and geometry data for Confi。
![](images/c45148df7219714ecb73a0db89e6c2012cb01efa76d2847cbd360daafe37b399.jpg)  
(c) Leading-edge radius nondimensionalized by local chord

图片摘要：该图主要展示 13: Baseline and design spanwise characteristics for Configu。
![](images/15da8a1d7927cf1cd6c7721e8c2fcd7847942122a4aee1aacdbd7e8e65d4994e.jpg)  
(d) Twist in degrees   
Figure 13: Baseline and design spanwise characteristics for Configuration 3 (C3). All data are plotted against nondimensionalized semispan location (η).

propulsor thrust on the airframe and vice versa, thus resolving the relevant aeropropulsive trades to first order.

In order to account for differences in airframe and propulsion system aerodynamic performance at cruise without introducing special thrust-drag accounting, a force balance method is applied, in which each aircraft configuration is trimmed in $F _ { x }$ through the actuator zone thrust inputs. This is done iteratively through numerical optimization based on the assumed 35:65 thrust split between the aft fuselage and wing propulsors, respectively, with thrust assumed to be uniformly distributed across the wing propulsors. Simultaneously, each aircraft configuration is also trimmed in $F _ { z }$ by including the angle of attack as a degree of freedom. Assessments of relative aerodynamic and aeropropulsive performance can then be performed with the design lift coefficient satisfied at $C _ { L } = 0 . 5 0 0$ and with $F _ { x } = T  – D = 0$ , where $T$ and $D$ are gross thrust and drag, respectively. This operating point is herein referred to as the “trim condition”.

图片摘要：该图主要展示 13: Baseline and design spanwise characteristics for Configu。
![](images/697384737b3ffb95319f89c54c71c40096a111991ec74dc073f94cb72ab2bf97.jpg)  
(a) Configuration 1

图片摘要：该图主要展示 14: Representative aircraft models used to assess the SUSAN 。
![](images/e847eb6fa59d489f4429b439fc036f790fd3ab8c2a9ea692535501b300011c37.jpg)  
(b) Configuration 2 (DEP)

图片摘要：该图主要展示 14: Representative aircraft models used to assess the SUSAN 。
![](images/d7583be0e20bd5460dc5a75ef892428860a357958fa2275cf5e84f27a491b122.jpg)  
(c) Configuration 3 (DEP + BLI)   
Figure 14: Representative aircraft models used to assess the SUSAN Electrofan trade study configurations.

Although each aircraft configuration can be assessed with their propulsion systems operating at their respective design points, it is important to note that the design requirements presented in Section 2 are based on conceptual level design and analysis methods, which do not accurately model the aerodynamic and coupled aeropropulsive performance of the complex geometries considered in this work. The design requirements are also based on aircraft level demands at top of climb, which involve higher thrust levels than those at which aircraft typically operate, i.e. cruise.

These factors give merit to the force balance method described above, which adjusts the thrust requirements of each propulsor at cruise based on the coupled aerodynamic and propulsion system performance predicted by CFD analysis. In addition, the force balance method implicitly captures “snowball effects” between aircraft thrust and drag, which might otherwise be missed if considering a method of thrust-drag bookkeeping that decouples the analysis of the airframe and propulsion systems.

For performance evaluations, comparisons include cruise thrust and drag, as well as mechanical flow and shaft power. In the present paper, mechanical flow power is defined as [24]

$$
\mathcal {P} _ {\text {f l o w}} = \iiint_ {V} (\boldsymbol {v} \cdot \boldsymbol {f}) d V \tag {1}
$$

where $_ { \pmb { v } }$ and $f$ are the velocity and force vectors integrated over the subset of volume

grid nodes defining a given actuator zone, $V$ .

Mechanical shaft power is given by

$$
\mathcal {P} _ {\mathrm {s h a f t}} = \dot {m} \Delta h \tag {2}
$$

where $\dot { m }$ is the mass-averaged mass flow rate and $\Delta h$ is the change in specific enthalpy:

$$
\Delta h = c _ {p} \left(T _ {t _ {3}} - T _ {t _ {0}}\right) = \frac {1}{\eta_ {a}} \left(\frac {\gamma R}{\gamma - 1}\right) T _ {t _ {0}} \left(\mathrm {F P R} ^ {\frac {\gamma - 1}{\gamma}} - 1\right) \tag {3}
$$

Here, $c _ { p }$ , $\gamma$ , and $R$ are the specific heat capacity, specific heat ratio, and gas constant of air, respectively, and $T _ { t _ { 0 } }$ and $T _ { t _ { 3 } }$ are the mass-averaged total temperature at the fan inlet and exit, respectively. Since the modeled flow across the fan is isentropic, losses are accounted for through an approximation for adiabatic fan efficiency [25]

$$
\eta_ {a} = 1. 0 6 6 - 0. 0 8 6 6 \mathrm {F P R} \tag {4}
$$

which is a linear regression based on advanced subsonic transport aircraft. The mechanical shaft power required by the wing propulsors is also modified by $1 / \eta _ { \mathrm { t r a n s } }$ to account for electrical transmission losses, where $\eta _ { \mathrm { t r a n s } } = 0 . 9 0 0$ based on current EAP technology level projections [2]. Generally, mechanical shaft power equals mechanical flow power modified by $\eta _ { a }$ and $\eta _ { \mathrm { t r a n s } }$ .

Tables 2 and 3 provide summaries of the aerodynamic and propulsion system performance for each trade study configuration. For Configuration 2, 18.2% less thrust is required to satisfy the trim condition relative to Configuration 1, which can be attributed primarily to DEP. A performance benefit also comes from the aft fuselage propulsor, which itself has a reduced thrust requirement due to reductions in total airframe and propulsion system drag. In terms of power, Configuration 2 requires 3.9% more mechanical flow power due to the higher speed internal flow experienced by the DEP systems, despite a 0.3% and 1.4% advantage in adiabatic fan efficiency for the aft fuselage and wing propulsors, respectively. Accounting for the assumed 10% loss from electrical transmission for the wing propulsors of all three configurations, the total mechanical shaft power required by Configuration 2 is 3.3% higher than Configuration 1. These results suggest that the main benefit of DEP is aerodynamic in nature, with propulsive efficiency playing a secondary role. However, if the mail-slot nacelle concept can be developed with higher levels of inlet diffusion, the required flow and hence shaft power may be less than that of the non-DEP configuration.

With regard to Configuration 3, 12.9% less thrust is required compared to Configuration 1, although Configuration 3 requires 7.6% more thrust than Configuration 2. This suggests that the aerodynamic benefit of DEP is still present for the DEP-BLI configuration but diminished from PAI effects. One possibility is that the internal flow speeds within the DEP systems are much higher due to the influence of the wing, as observed by Machado et al. [7]. This was the cause for the inlet shocks that were the focus of the aerodynamic redesign efforts presented in Section 4. Regardless, these higher flow speeds lead to higher drag penalties, which are likely the main contributions to the performance deficit. Based on mechanical flow power, Configuration 3 requires 16.3% more than Configuration 1 to maintain the

Table 2: Aerodynamic performance summary for the three SUSAN Electrofan wing propulsor configurations.   

<table><tr><td>Parameter</td><td>Configuration 1</td><td>Configuration 2</td><td>Configuration 3</td></tr><tr><td>Angle of attack (deg)</td><td>2.37</td><td>2.41</td><td>2.20</td></tr><tr><td>Lift coefficient</td><td>0.500</td><td>0.500</td><td>0.500</td></tr><tr><td>Drag coefficient*</td><td>0.0511</td><td>0.0421</td><td>0.0453</td></tr></table>

*No special thrust-drag bookkeeping.

trim condition and 11.9% more than Configuration 2. In this case, it is clear that the higher internal flow speeds described above are the cause for reduced propulsive efficiency. Accounting for the electrical transmission efficiency of the hybrid-electric propulsion system, Configuration 3 requires 15.9% more mechanical shaft power than Configuration 1 to maintain cruise.

Table 4 provides a comparison of power on and power off drag coefficient between each SUSAN Electrofan trade study configuration, which provides more insight into the benefits of DEP. In the present paper, $\Delta C D$ is referred to as “thrust-induced drag” or the drag cost of generating thrust. Here, it can be seen that the two DEP configurations experience approximately half the thrust-induced drag of Configuration 1. Configuration 2 also experiences less thrust-induced drag than Configuration 3, although this can be explained by the difference in thrust between the two configurations. Comparisons of power off drag coefficients also provide hints toward the impact of PAI, which appears to lead to higher drag for the two DEP configurations relative to Configuration 1. The higher drag coefficient of Configuration 3 compared to Configuration 2 also suggests higher adverse PAI effects, despite its reduced wetted area [7].

# 6 Conclusions

This paper presents a DEP configuration trade study for the SUSAN Electrofan based on the application of RANS-based aeropropulsive design and analysis. The DEP trade study includes three wing-mounted electric propulsion system configurations, namely, a non-DEP variant, which serves as a reference configuration, a DEP configuration, and a DEP-BLI configuration. These configurations, first introduced previously by Machado et al. [6, 7], are referred to as Configurations 1, 2, and 3, respectively, and are refined in the current work through the aerodynamic design method CDISC [12].

Specifically, aerodynamic redesigns are performed for the wing of each trade study configuration at cruise, accounting for first-order PAI effects from the integration of the wing and wing propulsors. For Configuration 3, the mail-slot nacelle is also refined in order to address additional adverse PAI effects encountered by the more coupled arrangement. These redesign efforts are successful in achieving a consistent level of aerodynamic design across the three configurations, allowing for more fair comparisons of their performance.

Table 3: Propulsion system performance summary for the three SUSAN Electrofan trade study configurations.   

<table><tr><td>Parameter</td><td>Configuration 1</td><td>Configuration 2</td><td>Configuration 3</td></tr><tr><td colspan="4">Aft Fuselage Propulsor</td></tr><tr><td>Number of propulsors</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Fan pressure ratio</td><td>1.19</td><td>1.16</td><td>1.17</td></tr><tr><td>Fan adiabatic efficiency</td><td>0.963</td><td>0.966</td><td>0.965</td></tr><tr><td>Mass flow rate (kg/s)</td><td>151.4</td><td>144.3</td><td>146.5</td></tr><tr><td>Mach number, inlet</td><td>0.412</td><td>0.397</td><td>0.406</td></tr><tr><td>Total temperature, inlet (K)</td><td>243.2</td><td>242.9</td><td>243.0</td></tr><tr><td>Flow power (MW)</td><td>1.89</td><td>1.50</td><td>1.60</td></tr><tr><td>Shaft power (MW)</td><td>1.96</td><td>1.56</td><td>1.66</td></tr><tr><td colspan="4">Wing Propulsors</td></tr><tr><td>Number of propulsors</td><td>2</td><td>16</td><td>16</td></tr><tr><td>Fan pressure ratio*</td><td>1.35</td><td>1.20</td><td>1.23</td></tr><tr><td>Fan adiabatic efficiency*</td><td>0.949</td><td>0.962</td><td>0.960</td></tr><tr><td>Mass flow rate* (kg/s)</td><td>150.9</td><td>35.2</td><td>35.5</td></tr><tr><td>Mach number, inlet</td><td>0.637</td><td>0.757</td><td>0.799</td></tr><tr><td>Total temperature, inlet* (K)</td><td>243.6</td><td>243.7</td><td>243.6</td></tr><tr><td>Transmission efficiency, electrical</td><td>0.900</td><td>0.900</td><td>0.900</td></tr><tr><td>Flow power* (MW)</td><td>3.33</td><td>0.46</td><td>0.52</td></tr><tr><td>Shaft power* (MW)</td><td>3.90</td><td>0.53</td><td>0.60</td></tr><tr><td colspan="4">All Propulsors</td></tr><tr><td>Mass flow rate (kg/s)</td><td>453.2</td><td>708.1</td><td>715.6</td></tr><tr><td>Thrust (kN)</td><td>57.8</td><td>47.3</td><td>50.9</td></tr><tr><td>Flow power (MW)</td><td>8.55</td><td>8.88</td><td>9.94</td></tr><tr><td>Shaft power (MW)</td><td>9.76</td><td>10.08</td><td>11.31</td></tr></table>

*Average per propulsor value

Table 4: A comparison of power on and off drag coefficients for the three SUSAN Electrofan trade study configurations.   

<table><tr><td>Setting</td><td>Configuration 1</td><td>Configuration 2</td><td>Configuration 3</td></tr><tr><td>Power off</td><td>0.0298</td><td>0.0323</td><td>0.0340</td></tr><tr><td>Power on</td><td>0.0512</td><td>0.0421</td><td>0.0452</td></tr><tr><td>ΔCD</td><td>0.0214</td><td>0.0099</td><td>0.0112</td></tr></table>

Representative three-dimensional full-configuration aircraft models were then developed based on the refined designs, and subjected to RANS-based aeropropulsive analysis using the LAVA curvilinear flow solver [10]. These trade study configurations are assessed based on thrust and drag, and mechanical flow and shaft power

following a force balance to simulate cruise. Results indicate that the DEP and DEP-BLI configurations of the SUSAN Electrofan require 18.2% and 12.9% less thrust at cruise than the non-DEP configuration, respectively, suggesting an aerodynamics benefit associated with DEP. Moreover, comparisons of power off and power on drag show that thrust-induced drag savings are significant for Configurations 2 and 3, which can be associated with the lower operating FPRs or thrust levels of the individual propulsors. Overall, Configuration 2 has the best aerodynamic performance. However, this may change if Configuration 3 can be designed with increased inlet diffusion to reduce the high internal flow speeds caused by the influence of the wing’s flow field, which in turn causes drag penalties.

In terms of the flow power required to maintain cruise, the DEP and DEP-BLI configurations are less efficient than the non-DEP variant. This is likely due to the overall higher internal flow speeds experienced by the DEP systems, which again come from insufficient inlet diffusion. When considering mechanical shaft power, a marginal reduction in the relative power required is obtained. This comes from the higher adiabatic fan efficiencies of the DEP systems, and also accounts for a 10% loss from electrical transmission applied to all wing propulsors.

These results indicate that the main benefit of DEP at cruise is to improve aerodynamic performance through reductions in thrust-induced drag. However, in order to recover a net benefit in mechanical flow and hence shaft power, which relate to propulsive efficiency, mail-slot nacelles must be developed for increased inlet diffusion. This is especially the case for the DEP-BLI configuration, in which the flow field of the wing causes significant flow acceleration leading into the underwing propulsors.

# References

1. Jansen, R. H., Kiris, C. C., Chau, T., Kenway, G. K. W., Machado, L. G., Duensing, J. C., Mirhashemi, A., Haglage, J. M., Dever, T. P., Chapman, J. W., French, B. D., Goodnight, T. W., Miller, L. R., Litt, J. S., Denham, C. L., Lynde, M., Campbell, R., Hiller, B., and Heersema, N., “Subsonic Single Aft Engine (SUSAN) Transport Aircraft Concept and Trade Space Exploration,” AIAA SciTech Forum, AIAA 2022-2179, San Diego, CA, January 2022. https: //doi.org/10.2514/6.2022-2179.   
2. Chau, T., and Duensing, J., “Conceptual Design of the Hybrid-Electric Subsonic Single Aft Engine (SUSAN) Electrofan Transport Aircraft,” AIAA SCITECH 2024 Forum, AIAA 2024-1326, Orlando, FL, January 2024. https://doi.org/10. 2514/6.2024-1326.   
3. Chapman, J. W., Kratz, J. L., Dever, T. P., Mirhashemi, A., Stalcup, E. J., Sixel, W. R., Woodworth, A. A., and Jansen, R. H., “Update on SUSAN Concept Vehicle Power and Propulsion System,” AIAA SciTech Forum and Exposition, AIAA 2023-1749, National Harbor, MD, January 2023. https: //doi.org/10.2514/6.2023-1749.

4. Wick, A. T., Hooker, J. R., and Hardin, C. J., “Integrated Aerodynamic Benefits of Distributed Propulsion,” AIAA SciTech Forum, AIAA 2015-1500, Kissimmee, FL, January 2015. https://doi.org/10.2514/6.2015-1500.   
5. Schmollgruber, P., Donjat, D., Ridel, M., Cafarelli, I., Atinault, O., Fran¸cois, C., and Paluch, B., “Multidisciplinary Design and Performance of the ONERA Hybrid Electric Distributed Propulsion Concept (DRAGON),” AIAA SciTech Forum, AIAA 2020-0501, Orlando, FL, January 2020. https://doi.org/10.2514/ 6.2020-0501.   
6. Machado, L. M., Chau, T., Kenway, G. K., Duensing, J. C., and Kiris, C. C., “Preliminary Assessment of a Distributed Electric Propulsion System for the SUSAN Electrofan,” AIAA SCITECH 2023 Forum, AIAA 2023-1748, National Harbor, MD, January 2023. https://doi.org/10.2514/6.2023-1748.   
7. Machado, L. M., Chau, T., and Duensing, J., “Toward the Development of an Underwing Boundary Layer Ingesting Distributed Propulsion System for the SUSAN Electrofan,” AIAA SCITECH 2024 Forum, AIAA 2023-1748, Orlando, FL, January 2024. https://doi.org/10.2514/6.2024-1327.   
8. Zante, D. E. V., Podboy, G. G., Miller, C. J., and Thorp, S. A., “Testing and Performance Verification of a High Bypass Ratio Turbofan Rotor in an Internal Flow Component Test Facility,” Tech. rep., NASA, September 2009. NASA/TM 2009-215661.   
9. Lee, B. J., and Liou, M.-F., “Conceptual Design of Propulsors for the SUSAN Electrofan Aircraft,” AIAA SciTech Forum and Exposition, AIAA 2022-2305, San Diego, CA, January 2022. https://doi.org/10.2514/6.2022-2305.   
10. Kiris, C. C., Housman, J. A., Barad, M. F., Brehm, C., Sozer, E., and Moini-Yekta, S., “Computational Framework for Launch, Ascent, and Vehicle Aerodynamics (LAVA),” Aerospace Science and Technology, Vol. 55, No. 1, 2016, pp. 189–219. https://doi.org/10.1016/j.ast.2016.05.008.   
11. Lowe, B. M., Ashby, C. P., Koch, J. R., Craig Penner, D. A., Housman, J. A., and Duensing, J. C., “Towards Aerodynamic Shape Optimization using an Immersed Boundary Overset Grid Method,” AIAA Aviation Forum, AIAA 2024- 4229, Las Vegas, NV, July 2024. https://doi.org/10.2514/6.2024-4229.   
12. Campbell, R. L., “Efficient Viscous Design of Realistic Aircraft Configurations,” 29th AIAA, Fluid Dynamics Conference, AIAA 1998-2539, Albuquerque, NM, June 1998. https://doi.org/10.2514/6.1998-2539.   
13. Spalart, P. R., and Allmaras, S. R., “A One-Equation Turbulence Model for Aerodynamic Flows,” 30th AIAA Aerospace Sciences Meeting and Exhibit, AIAA 92-0439, Reno, Nevada, January 1992. https://doi.org/10.2514/ 6.1992-439.

14. Shur, M. L., Strelets, M. K., Travin, A. K., and Spalart, P. R., “Turbulence Modeling in Rotating and Curved Channels: Assessing the Spalart-Shur Correction,” AIAA Journal, Vol. 38, No. 5, 2000, pp. 784–792. https: //doi.org/10.2514/2.1058.   
15. Spalart, P. R., “Strategies for Turbulence Modelling and Simulations,” International Journal of Heat and Fluid Flow, Vol. 21, No. 3, 2000, pp. 252–263. https://doi.org/10.1016/S0142-727X(00)00007-2.   
16. Housman, J. A., Kiris, C. C., and Hafez, M. M., “Time-Derivative Preconditioning Methods for Multicomponent Flows - Part I: Riemann Problems,” Journal of Applied Mechanics, Vol. 76, No. 2, 2009, pp. 1–13. https://doi.org/10.1115/ 1.3072905.   
17. Housman, J. A., Kiris, C. C., and Hafez, M. M., “Time-Derivative Preconditioning Methods for Multicomponent Flows—Part II: Two-Dimensional Applications,” Journal of Applied Mechanics, Vol. 76, No. 3, 2009, pp. 1–12. https://doi.org/10.1115/1.3086592.   
18. Saad, Y., and Schultz, M. H., “GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems,” SIAM Journal on Scientific and Statistical Computing, Vol. 7, No. 3, 1986, pp. 856–869. https: //doi.org/10.1137/0907058.   
19. Stich, G.-D., Fernandes, L. S., Duensing, J. C., Housman, J. A., Kenway, G. K. W., and Kiris, C. C., “Validation of Actuator Disk, Actuator Line and Sliding Mesh Methods within the LAVA Solver,” International Conference on Computational Fluid Dynamics 11, ICCFD, Maui, HI, July 2022.   
20. Fernandes, L. S., Machado, L. G., Duensing, J. C., and Kiris, C. C., “Computational Aerodynamics Analysis in Support of the CRM Tail Cone Thruster Configuration Wind Tunnel Test,” AIAA SciTech Forum, AIAA 2022-1171, San Diego, CA, January 2022. https://doi.org/10.2514/6.2022-1171.   
21. Hall, D. K., Greitzer, E. M., and Tan, C. S., “Analysis of Fan Stage Conceptual Design Attributes for Boundary Layer Ingestion,” Journal of Turbomachinery, Vol. 139, No. 7, 2017, pp. 1–10. https://doi.org/10.1115/1.4035631.   
22. Pandya, M. J., Jespersen, D. C., Diskin, B., Thomas, J. L., and Frink, N. T., “Efficiency of Mixed-Element USM3D for Benchmark Three-Dimensional Flows,” AIAA Journal, Vol. 59, No. 8, 2021, pp. 2997–3011. https://doi.org/ 10.2514/1.J059720.   
23. Machado, L. M. G., Chau, T., Kenway, G. K. W., Duensing, J., and Kiris, C. C., “High Fidelity Computational Analysis and Optimization of the SUSAN Electrofan Concept,” AIAA SciTech Forum and Exposition, AIAA 2022-2304, San Diego, CA, January 2022. https://doi.org/10.2514/6.2022-2304.

24. Yildirim, A., Gray, J. S., Mader, C. A., and Martins, J. R. R. A., “Boundary-Layer Ingestion Benefit for the STARC-ABL Concept,” Journal of Aircraft, Vol. 59, No. 4, 2022, pp. 896–911. https://doi.org/10.2514/1.C036103.   
25. Gray, J., “Design Optimization of a Boundary Layer Ingestion Propulsor Using a Coupled Aeropropulsive Model,” Ph.D. thesis, University of Michigan, 2018.
