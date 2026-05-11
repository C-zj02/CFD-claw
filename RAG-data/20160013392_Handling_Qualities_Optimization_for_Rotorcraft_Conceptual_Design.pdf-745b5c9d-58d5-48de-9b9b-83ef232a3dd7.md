# Handling Qualities Optimization for Rotorcraft Conceptual Design

# Ben Lawrence

San Jose State University,

NASA Ames Research Center,

Moffett Field, CA

# Colin R. Theodore

# Wayne Johnson

National Aeronautics and Space

Administration

NASA Ames Research Center

Moffett Field, CA

# Tom Berger

U.S. Army Aviation Development

Directorate

Moffett Field, CA

# Abstract

Over the past decade, NASA, under a succession of rotary-wing programs has been moving towards coupling multiple discipline analyses in a rigorous consistent manner to evaluate rotorcraft conceptual designs. Handling qualities is one of the component analyses to be included in a future NASA Multidisciplinary Analysis and Optimization framework for conceptual design of VTOL aircraft. Similarly, the future vision for the capability of the Concept Design and Assessment Technology Area (CD&A-TA) of the U.S Army Aviation Development Directorate also includes a handling qualities component. SIMPLI-FLYD is a tool jointly developed by NASA and the U.S. Army to perform modeling and analysis for the assessment of flight dynamics and control aspects of the handling qualities of rotorcraft conceptual designs. An exploration of handling qualities analysis has been carried out using SIMPLI-FLYD in illustrative scenarios of a tiltrotor in forward flight and single–main rotor helicopter at hover. Using SIMPLI-FLYD and the conceptual design tool NDARC integrated into a single process, the effects of variations of design parameters such as tail or rotor size were evaluated in the form of margins to fixed- and rotary-wing handling qualities metrics as well as the vehicle empty weight. The handling qualities design margins are shown to vary across the flight envelope due to both changing flight dynamic and control characteristics and changing handling qualities specification requirements. The current SIMPLI-FLYD capability and future developments are discussed in the context of an overall rotorcraft conceptual design process.

Nomenclature   

<table><tr><td>6-DoF</td><td>Six-degree-of-freedom</td><td>OLOP</td><td>Open Loop Onset Point</td></tr><tr><td>p,q,r</td><td>Angular velocity about body, X, Y, Z-axes</td><td>RCAH</td><td>Rate-Command/Attitude-Hold (control system response type)</td></tr><tr><td>nd</td><td>Non-dimensional units</td><td></td><td></td></tr><tr><td>u,v,w</td><td>Velocity along body X, Y, Z-axes</td><td>RCDH</td><td>Rate-Command/Direction-Hold (control system response type)</td></tr><tr><td>ADD</td><td>Aviation Development Directorate (U.S. Army)</td><td>RCHH</td><td>Rate-Command/Height-Hold (control system response type)</td></tr><tr><td>DM</td><td>Design Margin</td><td></td><td></td></tr><tr><td>HQ</td><td>Handling Qualities</td><td>VTOL</td><td>Vertical Take-Off and Landing</td></tr><tr><td>MDAO</td><td>Multidisciplinary Design Analysis and Optimization</td><td>β1c1, β1s1</td><td>1storder longitudinal and lateral rotor flapping states (subscript is rotor index)</td></tr><tr><td>NDARC</td><td>NASA Design and Analysis of Rotorcraft</td><td>φ,θ,ψ</td><td>Euler angle orientation of body axes w.r.t to inertial frame</td></tr></table>

# Introduction

The process of designing a rotorcraft has remained a largely serial process, such that competing design objectives are not evaluated in a formal, automated fashion. Instead, the outcome of separate optimization processes representing different disciplines (e.g., rotor aerodynamics, propulsion, etc.) are exchanged and discussed by subject-matter experts from the design team and an iterative cycle between design groups ensues until certain objectives — usually empty weight and speed — are met. For new VTOL aircraft manufacturers, especially those engaged with nontraditional configurations, in-house discipline tools appropriate for rotary wing vehicles are rarely available. Formal optimization

tools and analyses are needed now to incorporate the growing number of design constraints and complex system trades needed to assess future rotorcraft designs [1].

Handling qualities analyses have been historically neglected in the aircraft conceptual design process [2] and [3]. In fixed-wing design, requirements for good stability, control and handling qualities are addressed through the use of tail volume coefficients, location of the center of gravity and relatively simple static analyses [3]. Rotorcraft, in particular high performance designs, cannot rely on such methods, since most bare-airframe designs are unstable typically and require a stabilizing control system to make

them adequately flyable. In the context of rotorcraft, Padfield (Ref [4]) notes that $2 5 { - } 5 0 \%$ of flight testing time in an aircraft development program might be spent on fixing handling qualities problems. Furthermore, Padfield suggests that handling qualities were not given their proper place in the early design trade-space, and were often left until flight test to discover and “put right”. During the early days of helicopter development, Padfield notes that handling qualities were extremely difficult to predict and were justifiably treated as an outcome of the series of complex design decisions relating to, for example, overall performance, vehicle layout and structural integrity, and fixing vibration problems.

Ref. [5] emphasizes flying qualities as the vehicle stability, control and maneuvering characteristics and handling qualities as the combination of flying qualities and the broader aspects of the mission task, visual cues and atmospheric environment. In many instances handling qualities is used informally as the vehicle oriented flying qualities, as ref [4] notes, there appears to be no universal acceptance on the distinction. In this paper, handling qualities is used in the “colloquial” sense in that it refers to the vehicle flight dynamic stability and control aspects. As such, the term “handling qualities requirements” refer to the stability and control characteristics that have been determined to lead to good piloted handling/flying qualities.

The lack of detailed flight dynamics modeling at the earliest stages of design disregards a potentially significant contributor to size, weight, and performance estimates for some design activities. Omission of flight dynamics modeling during conceptual design also defers flight dynamics, rotor response lags, and control authority considerations to later in the design process, which have led to problems during flight test. The flight dynamics and control of an air vehicle are fundamentally a function of its inherent control power and damping characteristics and are typically augmented by the feed-forward and feed-back loops programmed into the flight control system. Predicting these characteristics of a yet-to-be-built air vehicle at the conceptual design phase may offer paths to avoid handling qualities issues later in the design lifecycle or to minimize over-design when faced with uncertainty in the handling qualities of a design.

Over the past decade, NASA, under a succession of rotary-wing programs has emphasized the importance of physics-based modeling and interdisciplinary optimization, [1]. NASA has been moving towards coupling multiple discipline analyses in a rigorous consistent manner to evaluate rotorcraft conceptual designs. NASA has developed a state-of-the-art aircraft sizing code, NDARC [6], and is focusing on a more global vehicle approach to the optimization of VTOL configurations. This global approach requires the inclusion the analysis of aerodynamics, acoustics, propulsion, handling qualities, and structures, among others, to capture the critical interdisciplinary aspect of rotary wing vehicle design. NASA’s ultimate goal is to develop formal

optimization methods that couples these analyses via an OpenMDAO framework [1].

Handling qualities (HQ) is one of the component analyses to be included in a future NASA framework for conceptual design of VTOL aircraft. Similarly, the future vision for the MDAO (Multidisciplinary Analysis and Optimization) capability of the Concept Design and Assessment Technology Area (CD&A-TA) of the U.S Army Aviation Development Directorate also includes a handling qualities component. In response, a new tool “SIMPLI-FLYD” [7] (Simplified Flight Dynamics for Conceptual Design) was developed in a NASA and U.S. Army collaboration. SIMPLI-FLYD was developed to utilize the output of the NDARC [8] sizing code and integrates the CONDUIT [9] control analysis and optimization tool. The SIMPLI-FLYD toolset is designed to perform flight dynamics, control and handling qualities modeling and analysis of rotorcraft conceptual designs, and also provides a capability to “fly” the concept designs in an X-Plane based realtime simulation.

The objective of this paper is to demonstrate and explore SIMPLI-FLYD and NDARC integrated in a coupled process to investigate how handling qualities analyses participate in rotorcraft conceptual design. To develop understanding of handling qualities in conceptual design, evaluations of the SIMPLI-FLYD toolset in “typical” design scenarios were required. The paper will present results of studies using NDARC and SIMPLI-FLYD of the pitch axis handling qualities for conceptual design models of a tiltrotor aircraft in forward flight, and for the yaw axis handling qualities of a single-main rotor helicopter in hover. Also presented are the results of a stability and control derivative sensitivity study developed to address a number issues related to the primary NDARC/SIMPLI-FLYD coupling task. The paper will conclude with a summary of the lessons learned from the analysis so far and outline of planned future developments.

# SIMPLI-FLYD Overview

Figure 1 shows the primary components within the SIMPLI-FLYD process as well as the key interfaces to external components and processes. The dashed blue box indicates the tools and activities encompassed in an overall conceptual design process involving NDARC. The green box is the SIMPLI-FLYD functions. Stage (1) is the primary conceptual design sizing activity using NDARC. In a future context, this process might be represented by a variety of other analyses encompassed in a MDAO environment. Stage (1) is the source of input for SIMPLI-FLYD that encompasses stages (2) through (4) where simplified linear flight dynamics models are calculated, integrated with control laws, and then analyzed and optimized by CONDUIT. The output stages (2) through (4) are set(s) of stability, control and handling qualities parameters (stage 5), and an X-Plane compatible real-time simulation model for use in an X-Plane simulation station (stage 6).

图片摘要：该图主要展示 1 shows the primary components within the SIMPLI FLYD proces。
![](images/557476ff5b1bd93434bb3679ce6f14fac0e5e4a2c31f19481b9e0395f5009866.jpg)  
Figure 1 SIMPLI-FLYD Architecture for including stability and control analysis into conceptual design

Reference [7] reports a full description of the SIMPLI-FLYD toolset and its sub-functions; some of the key aspects are highlighted in the following section.

# Flight Dynamics Modeling

The flight dynamics modeling uses a modular approach to representing a vehicle with various combinations of rotors, wings, other surfaces and auxiliary propulsion, similar to NDARC. The imported data from NDARC consists of geometric, aerodynamic, and configuration data about the vehicle and pre-calculated trim data for the flight conditions to be assessed. The flight dynamic calculations then loop over the flight conditions and components calculating linear stability and control derivatives for each component (a component is a force and moment generating element: rotors, wings, aerodynamic surfaces and fuselage). For the rotors, this process uses a blade element model which is initialized at the NDARC calculated trim state using numerical perturbation to calculate the stability derivatives. For the other components, a simplified calculation of the linear derivatives is performed using a mix of analytical and empirical models. The total vehicle linear models are then computed through the summation of the state-space ‘A’ and $ { \mathrm { ^ { c } B \mathrm { ^ { , } } } }$ matrix terms from the various components. The linear models can be optionally 6- degree-of-freedom (6-DoF) rigid body states only or can include first-order flapping equations, with one longitudinal and one lateral per “main” rotor, following the “hybrid” model formulation in Tischler [10] . As such, a single main rotor configuration has 11 states: 9 rigid body states $( u , v , w , p , q , r , \varphi , \theta , \psi )$ and 2 rotor states $\left( \beta _ { 1 c _ { 1 } } , \beta _ { 1 s _ { 1 } } \right)$ as the tail rotor derivatives are always reduced to their 6-DoF contribution

(no flapping terms in linear model). Other configurations that feature two main rotors for example, such as a tiltrotor or a tandem, contain 13-states, with 4 rotor states.

For the control derivatives, a simplification was imposed for the CONDUIT point analysis flight dynamic models such that any vehicle had a fixed set of four “controls” for the primary roll, pitch, thrust and yaw response axes. The effects of multiple or redundant control effectors such as combinations of rotor controls and wing or aerodynamic surface controls are combined via an NDARC defined “mixing matrix” in advance of analysis at stages (3) and (4) (the separate control derivatives are retained for use in the real-time model). The actuator characteristics are configurable for each analysis point model to allow representation of different actuator classes (i.e. swashplate vs. aerodynamic surfaces) required for particular flight conditions/configurations.

# Control System Modeling, Analysis and Optimization

The control system applied to the vehicle model at stage 3 in Figure 1 is based on an explicit model-following architecture that consists of independent feed-forward and feedback paths, shown in Figure 2. The control laws use a generic architecture with varying modes appropriate for use at different flight conditions as per Table 1.

图片摘要：该图主要展示 2 Explicit Model Following Architecture。
![](images/0fe76f40bd3e31b42582dc61acce639b6a3795035bbd3ed8c0f03fe749eb0750.jpg)  
Figure 2 Explicit Model Following Architecture.

Table 1. Control system response types for various axis and flight modes   

<table><tr><td></td><td colspan="2">Rotor-Borne</td><td>Wing-Borne</td></tr><tr><td></td><td>Hover</td><td>Forward-Flight</td><td>Forward-Flight</td></tr><tr><td>Roll</td><td>RCAH</td><td>RCAH</td><td>RCAH</td></tr><tr><td>Pitch</td><td>RCAH</td><td>RCAH</td><td>Angle-of-Attack-
Command</td></tr><tr><td>Yaw</td><td>RCDH</td><td>Sideslip-
Command</td><td>Sideslip-Command</td></tr><tr><td>Thrust</td><td>RCHH</td><td>Open-loop</td><td>Open-loop</td></tr></table>

RCAH $=$ Rate-Command/Attitude-Hold   
RCDH $=$ Rate-Command/Direction-Hold   
RCHH $=$ Rate-Command/Height-Hold

The setup and optimization of the control laws is fully automated within CONDUIT $\textsuperscript { \textregistered }$ and the overall SIMPLI-FLYD process (based on certain user configurations). The control system is optimized for each axis where key metrics are used to assess the level of over- or under-design in the control system, for both the feedback and the feed-forward paths. In the case of feedback, the metrics are for the control system's (combined with the vehicle) stabilizing performance robustness and ability to reject disturbances. Starting with a baseline required value for each specification (defining $0 \%$ over-design), the requirements are progressively increased (more over-design) until a feasible design can no longer be achieved. If the baseline design cannot be met, the requirements are decreased (under-design) until a feasible solution is achieved. After the feedback path is optimized, the feed-forward path is optimized using specifications such as piloted bandwidth, quickness, and control power. The optimization is carried out in a phased process; CONDUIT tunes the gains to first meet all of the “Hard Constraints” (stability specifications), then the soft constraints (the handling qualities specifications) are optimized. Finally, CONDUIT tunes the gains to reduce the Summed Objective (“cost of feedback” or performance specifications) to find the design that meets the requirements with the minimum cost (e.g. such as actuator requirements).

The handling qualities specifications used to drive the control system optimization are divided by aircraft type, flight regime, control axis, and feedback or feed-forward. Specification

boundaries are drawn from the rotorcraft specifications in ADS-33E [11] and the fixed-wing specifications of MIL-STD-1797B [12]. For the full list of the specifications currently used in SIMPLI-FLYD see Ref [7].

Once the control system optimization is complete, the block diagram parameters (feedback gains, feed-forward gains, inverse model parameters, etc.) and the HQ specification results of the control system optimization, given individually for each axis, are saved for output and further use.

In addition to the individual specification parameter values and percent over/under margins, the CONDUIT analysis provides a single HQ requirements “design margin” (DM) for each of the primary control axis analyzed (roll, pitch, yaw, vertical) and for both the feedback and feed-forward control paths. The DMs are the percent over/under design for the worst or limiting specification for each feedback/forward/axis combination.

# Method of Analysis of SIMPLI-FLYD/NDARC

# Coupled Process

In this paper, the results of two different analyses will be presented. The motivation for carrying out each of the analyses and the methods applied is first presented. The primary objective was to develop and assess NDARC and SIMPLI-FLYD coupled into a combined analysis. The goal of the NDARC/SIMPLI-FLYD coupled analysis was to run sweeps of design parameter variations relevant to the handling qualities of the design scenarios selected (pitch axis forward flight or yaw axis hover HQs) and examine the impact on both the SIMPLI-FLYD HQ output and NDARC design sizing. The main task for the development of the NDARC/SIMPLI-FLYD coupled analyses was the creation of Python-based “wrapper” scripts which handled the input data and variable initialization, called the NDARC and SIMPLI-FLYD (via Matlab) codes, and handled the data interface and collection in a common environment. The NDARC run and utility functions were drawn from the “rcotools” library, a Python-based toolset being developed by NASA for the integration of NDARC into the OpenMDAO environment.

Another aspect to preparing the SIMPLI-FLYD/NDARC coupled analyses was to down-select a subset of the many possible design variables available. The down-selection of design parameters was primarily necessary to reduce the computational task and avoid the “Curse of Dimensionality” [13] where for k-dimensions (parameters) $\mathtt { n ^ { k } }$ runs or calculations are required for a full factorial sweep of all possibilities. For example, a NDARC/SIMPLI-FLYD coupled analysis run for a single flight condition (all axes) currently takes typically 15-20 minutes on a desktop PC, and computation times would rapidly increase as the number of design parameter dimensions increase. Therefore it was not a realistic task to run sweeps of all potential inputs and evaluate the output. Although for the design scenarios being examined an experienced flight dynamics engineer could likely choose the most relevant design variables it was desirable to devise a method that might verify the down-selection process. A technique was devised to

compute the sensitivity of the stability and control derivatives that SIMPLI-FLYD calculates to the design parameters it imports from NDARC. The design parameters that most influenced the key stability and control derivatives known to influence the handling qualities scenarios selected, could be then identified for investigation in the full NDARC/SIMPLI-FLYD analyses.

Both the derivative sensitivity study and the NDARC/SIMPLI-FLYD coupled process used two example vehicle test cases; a tiltrotor aircraft similar in size and design to XV-15, with the focus being the forward flight pitch axis, and a single-main rotor helicopter (similar in size and weight to a UH-60a), with a focus on the hover yaw axis characteristics.

# Results

# Stability and Control Derivative Sensitivity Analysis

The results of sensitivity analysis of the bare-airframe stability and control derivatives to a subset of the design parameters imported by SIMPLI-FLYD are presented first. The results using the NDARC XV-15-like tiltrotor as the source of input to SIMPLI-FLYD are shown in Figure 3. Each sub-plot is a 3-axis bar chart – one axis is for the stability and control derivatives names, namely key pitch moment (M) and vertical force (Z) derivatives with respect to control inputs, elevator and cyclic and key longitudinal axis states: pitch rate, (q) and vertical velocity, (w) (which reflects the angle of attack response). The derivative naming convention is the force/moment separated by an underscore from the state/control e.g. M_elevator or ${ \cal Z } _ { - } \mathrm { w }$ . The second axis is for the components design parameters being perturbed (each plot is for a single component) – only those that had a non-zero effect are shown. For the purposes of this paper, it is not necessary to specifically identify all the listed design parameters perturbed, however parameters of particular significance are identified in the following section. than The third axis is the value of the stability and control derivative “sensitivity”

which is a form of non-dimensional (to fairly compare different types of derivatives) and reference area “weighted” version of the sensitivity value (to allow equal comparison between components). The color in these plots does not represent any value and is merely intended to help to differentiate between each row of the plot data. For reasons of clarity, only the key derivatives known to influence those dynamics relevant to the pitch or yaw axis HQ Design Margins are presented.

The main premise of the analysis is to focus on the relative values rather than the absolute values computed. The figure show the sensitivities for Rotor1 (Rotor 2 results are identical in this forward flight condition and are thus omitted), the wing, fuselage and, “tail” components (1 being the horizontal stabilizer and 2 and 3 the two end plates of the H-tail configuration).

Intuitively, the design parameters that influence the most are the horizontal tail parameters such as the tail area, X-location (loc(1)), lift curve slope (dclca), elevator size (Scont_S) and control flap lift effectiveness (Lf). The only other parameter that approaches the same level of sensitivity is the wing X-location (loc(1) on the wing subplot).

Figure 4 shows the same analysis for the single-main rotor helicopter configuration at hover for the key yaw axis bareairframe stability and control derivatives. At hover, the derivatives are most sensitive to the design parameters defining the tail rotor (rotor 2) that the derivatives are most sensitive to, though the main rotor (rotor 1) equivalent hinge offset parameter (“e”) approaches a similar order of influence. The most sensitive parameter of the tail rotor is the radius, followed by the tail rotor longitudinal location (hub_loc(1)), and blade chord (chord) .The results are mostly intuitive although the inclusion of some of the lateral-directional coupling terms show relationships that are less intuitive, such as the effect of the tail rotor radius and Lock number on the overall vehicle roll due to yaw derivative, Lr.

图片摘要：该图主要展示 4 shows the same analysis for the single main rotor helicopt。
![](images/31252ea0a2df6ed27ccb019c8ba715edd17e9b11cedf6b10cc280d017fc23b2b.jpg)  
Figure 3 Sensitivity of component pitch stability and control derivatives to design parameters imported from NDARC model (tiltrotor, airplane mode, 160 kts)

图片摘要：该图主要展示 3 Sensitivity of component pitch stability and control deriv。
![](images/0247e4ec90de4dc4e5a033651d488411cb4f9304c1efaed6f14bb2ad7fa7254e.jpg)

图片摘要：该图主要展示 3 Sensitivity of component pitch stability and control deriv。
![](images/98e0e566e6b1ef8172b7127877a1f3e46498bff55771791e5299ff02971ae5d1.jpg)  
Figure 4 Sensitivity of component lateral-directional stability and control derivatives to design parameters imported from NDARC model (single-main rotor, hover)

# NDARC/SIMPLI-FLYD Coupled Analysis

The results of applying variations to design parameters in the full coupled NDARC/SIMPLI-FLYD analyses are presented in the following section. The sensitivity analysis of the previous section guided the selection of a subset of design variables to use. The same two NDARC models, an XV-15-like tiltrotor, and a single main rotor helicopter were used as the test example vehicles. These results build upon the work in [7] in two aspects: 1) for each change of variables, NDARC now performs a sizing task (the previous analysis varied the design which affected the weight but did not re-size), and 2), the analyses use multidimensional parameter changes to design variables rather than single parameter sweeps and thus are able to demonstrate coupling effects of design parameters on the HQs.

The NDARC sizing task determines the dimensions, power, and weight of a rotorcraft that can perform a nominal design mission [8]. The aircraft size is characterized by parameters such as design gross weight, weight empty, rotor radius, and engine power available. NDARC calculates the size and weight of certain specified aircraft components while factoring in the weight of other components with a predetermined size (such as the parameters being varied in this analysis). The exceptions to this currently are the actuator parameters which are uncoupled to NDARC and only currently affect the handling qualities and not the design weight and power. In all the results in this paper, the change of the moments of the inertia of the vehicle with respect to the design variations is not directly modeled. Instead, inertia changes are currently represented via the weight change and the use of fixed radii of gyration which SIMPLI-FLYD inherits from NDARC. After NDARC has completed its task, the aircraft design data is input to SIMPLI-FLYD. The final outputs of the SIMPLI-FLYD analysis are the HQ design margins, as calculated by CONDUIT. Conceptually, it appeared reasonable to use the CONDUIT HQ design margins as the overall HQ analysis metrics for two reasons:

1) The design margins offered a mechanism by which multiple feedback and feed-forward HQ specifications are reduced to two HQ design margins per axis – these respectively represent the aircraft’s overall flight dynamic stabilization/disturbance rejection and control response characteristics for each axis.   
2) The design margins are a non-dimensional metric $( \%$ over/under design) based on the worst case HQ specification.

Both of these factors offered a mechanism that avoided a situation where each analysis case presented a large array of multiple specifications with differing units and meanings. Instead, the design margins present more holistic metrics of the HQ “goodness” that are more convenient for integration with an overall MDAO process and for presentation to the design engineer.

Figure 5 (a) to (c) show the tiltrotor pitch axis handling qualities (HQ) design margins (DM) for a sweep of three design parameters: horizontal tail area, tail flap control area ratio and tail

flap actuator rate-limit. Three flight conditions – 160 kts, 230 kts and 300 kts are evaluated for airplane mode. All the values varied for the design parameters are listed in the following bullets (*initial nominal value):

Horizontal tail Area: 25.125, 40.2, 50.25*, 60.3, 75.375 [ft2]   
Horizontal tail flap ratio: 0.0647, 0.1656, 0.2587*, 0.36, 0.45 [nd]   
 Horizontal tail flap actuator rate limit: 10, 20*, 30 [deg/s]

As described earlier, the analysis computes a design margin for both the feedback (stabilization) and feed-forward (response) components of the pitch axis HQs. The figures use 3-D Matlab “slice” plots that provide a color weighted “cloud” of data for the 3 design parameters. The color indicates the design margin value, ranging from red for $- 2 0 0 \%$ under-design margin, to deep blue for the $+ 2 0 0 \%$ over-design margin. The plots are a space-efficient method to presenting data for up to $3 / 4$ -dimensions. The printed versions are somewhat limited in that the slices can only be viewed from a fixed perspective whereas in the Matlab software the user can manipulate the viewing angle to inspect the data from any vantage. Nevertheless, the main intention is to present the broader trends, which in these cases are adequately covered in a more compact manner by this form of data presentation.

The first result to highlight is the trend with flight speed, where the sensitivity of the design margins to variations in the design parameters reduces with greater airspeed. Here, the higher dynamic pressure confers increased bare-airframe stability, damping and control power improving the ability of the aircraft to meet the stabilization (feedback) and control response (feedforward) HQ specifications respectively. As the speed reduces, and particularly at 160 kts (which is approximately $1 . 5 \mathrm { x }$ the stall speed in airplane mode) the boundaries between over-design and under design in the pitch HQs become more apparent. Intuitively, the worst pitch axis feed-forward HQs (under design) are for the smallest tail, flap and lowest actuator rate limit. The trend for the feedback specifications is similar with the exception being that the rate limit is generally unable to impact the under-design margin cases, such as those at the lower tail areas at 160 kts (some coupling effect is seen at the highest tail flap ratio and highest rate limit). Note that throughout these analyses, to save computational time by preventing the CONDUIT optimization continuing to very high positive design margins, a limit was applied that prevented further optimization if a $+ 6 0 \%$ design margin was reached.

In Figure 5(a) shows that another region of reduced design margin emerges indicating that the tail can be “too big” from a HQ perspective. In these cases, the large tail with small control surface, at low rate limit, has under-design for the feed-forward pitch HQs. The aircraft is likely over-damped or too stable and the aircraft is unable to meet certain control response specifications.

In the tiltrotor examples, varying the tail flap actuator rate limit had different effects on the outcome of the feed-forward and feedback design margins. For the feed-forward design margins, rate limit had a graduated effect where increased rate-limit was

able to affect the design margin achievable for varying tail area and flap area ratios. The feed-forward specifications have a number of time-domain specifications which are sensitive to nonlinearity such as rate-limiting. Conversely, the feedback design margins had weak sensitivity to rate limiting (for the range of values evaluated), probably because the feedback specifications are predominately linear system analyses and the non-linear effect of rate-limiting essentially plays no part in determining the margin to these specifications. The OLOP (Open Loop Onset Point) specification [14] is included to capture the effect of rate-limiting but closer inspection of these cases discovered that the OLOP specification was not determining the under-design, and in fact eigenvalue stability and crossover frequency were the limiting specifications. OLOP was primarily developed to predict handling qualities issues due to pilot input induced rate limiting and there are clear guidelines to use the maximum pilot input as the disturbance input for the OLOP test. However, OLOP has also been included as a feed-back HQ specification in SIMPLI-FLYD– an extrapolation of its original design. As such, the concept of the disturbance input is no longer a pilot input but some external disturbance (gust etc.) for a which nominal value of 5ft/s in the vertical velocity (w) was selected. This value is relatively small and thus OLOP limits are not approached even for the smallest tails which should require the greatest feedback stabilization due to the reduction in bare-airframe stability. Hence OLOP, the only feedback specification that would be sensitive to actuator rate limiting, does not act as a limiting specification and no relationship is observed with rate limit for the overall feedback design margin.

The relationship of the empty weight with respect to the three design variables is shown in Figure 5(d). The tail area dominant factor affecting the aircraft weight. The tail flap area ratio has a relatively weak effect. The actuator characteristics have no effect as NDARC does not know anything about those. Currently the actuator properties are only an input to SIMPLI-FLYD and thus can only influence the HQ DMs. The “cost” of changing the actuator performance on the design, such as in terms of weight, is not yet modelled and is a planned future development.

Figure 6 is a second, comparative set of sweeps for the tiltrotor at the 160 kts airplane condition. In these cases however, the actuator rate limit is fixed at the nominal $2 0 ~ \mathrm { d e g / s }$ and the third axis (vertical) of design parameter variation is now the horizontal tail longitudinal position, expressed in non-dimensional terms, X/L (X-location divided by the reference length of rotor radius), for values of 1.4317, $1 . 7 8 9 6 ^ { \ast }$ , 2.1475 (*nominal). Sensitivity of the design margins in (a) is observed for all three variables. Vehicle empty weight in (b) is mostly affected by the tail area and X-location. Comparing the feedback and feed-forward design margins it can be seen a trade-off exists between an optimal configuration for stability (feedback) and response (feedforward). The feed-forward tends to prefer a larger control surface on a smaller tail for the intermediate tail location and the feedback prefers a larger tail, at the largest X-location and is only weakly sensitive to the flap size (the very smallest tail is improved by having a bigger fraction of control surface).

图片摘要：该图主要展示 6 is a second, comparative set of sweeps for the tiltrotor a。
![](images/920710b92c0e0434a32dfd59b6989af9897748b0bf3cbaef7af1be5003b98a78.jpg)  
Tail area [f]

图片摘要：该图主要展示 6 is a second, comparative set of sweeps for the tiltrotor a。
![](images/6cee553739ea9f2aa762e54801583bc2283fb9daba201b61d3f54494ece4e44e.jpg)  
Tailarea[]

图片摘要：该图主要展示 6 is a second, comparative set of sweeps for the tiltrotor a。
![](images/f31a27095679a31841d10a1485200c5b4433e6be62c0e765811af281d734d32d.jpg)  
(a) Pitch axis HQ design margins v design parameters, 300kts

图片摘要：该图片与(b) Pitch axis design HQ margins v design parameters, 230kts；(c) Pitch axis HQ d这部分内容相关。
![](images/a9c098e9166700103a85765843ed9dbe4d0fa145f5a88911f7794e07c0fb071e.jpg)  
(b) Pitch axis design HQ margins v design parameters, 230kts

图片摘要：该图主要展示 5 Tiltrotor Feed forward/Feedback Pitch Axis HQ design margi。
![](images/94e8391c075e1268b23f449d8e365433381dccea2b0b73b85644ec25429dba90.jpg)

图片摘要：该图主要展示 5 Tiltrotor Feed forward/Feedback Pitch Axis HQ design margi。
![](images/9d7f194d8229840b8d6a5c58e143a03424f589b82bbeeba650f5f1f7a861fa9d.jpg)  
(c) Pitch axis HQ design margins v design parameters, 160kts

图片摘要：该图主要展示 5 Tiltrotor Feed forward/Feedback Pitch Axis HQ design margi。
![](images/738ba266d5a8d0e253e24059f02f447f52c2332531d1e206fc33eefc079cd487.jpg)  
(d) Empty weight v design parameters   
Figure 5 Tiltrotor Feed-forward/Feedback Pitch Axis HQ design margins and empty weight for variations in tail area, tail flap area ratio, tail flap actuator rate limit, at various speeds (airplane mode, sea level)

图片摘要：该图主要展示 5 Tiltrotor Feed forward/Feedback Pitch Axis HQ design margi。
![](images/94e91bb5bfc5322098d5eed973081e2c48e723784131d02c88a5fdd1d9f224f3.jpg)

图片摘要：该图主要展示 5 Tiltrotor Feed forward/Feedback Pitch Axis HQ design margi。
![](images/2fe76df924b16aac335983e825bf4aa667db321c5409fb1358cb824a9ebbf472.jpg)  
(a) Pitch axis HQ design margins v design parameters, 160kts

图片摘要：该图主要展示 5 Tiltrotor Feed forward/Feedback Pitch Axis HQ design margi。
![](images/dcf0c4857b68cba347fbcac0cdb88ee07d9f943e9e4088c8f7cd5109d5aa9cc2.jpg)  
(b) Empty weight v design parameters   
Figure 6 Tiltrotor Feed-forward/Feedback Pitch Axis HQ design margins and empty weight for variations in tail area, tail flap area ratio, tail nondimensional longitudinal position (X/L), at 160kts (airplane mode, sea level)

The results of the NDARC/SIMPLI-FLYD coupling applied to the single main rotor example, with the focus on the yaw axis handling qualities are shown in Figure 7. The design margins are shown for a sweep of the tail rotor size (a coupled increment in rotor radius at constant solidity and tip speed), non-dimensional longitudinal tail rotor location (X/L) and tail rotor actuator bandwidth. The range of parameters was chosen to investigate whether an optimum size/position existed for rotors smaller than the nominal 6ft radius. Hence, the rotor size variations ranged from 6 ft to 3.6 ft radius (a $4 0 \%$ reduction) and a longitudinal position, X/L, from 1.3 to 1.82 (a $5 0 \%$ increase from nominal). Note that there is a region of the plot for radii below 5ft and the smallest X-locations that is empty. Here, NDARC was unable to converge on a sizing or trim solution and thus these cases were discarded as invalid.

For the feedback design margin, there is very little sensitivity to the design parameter variations, and almost all cases reached the upper limit of $+ 6 0 \%$ design margin. The feed-forward margins exhibited much greater sensitivity to the design parameter variations. The design margin improved with increased radius and X-location but only reached $+ 1 0 \%$ positive design margin case with largest rotor, longest tail rotor location, and greatest actuator bandwidth value. The design margins at forward speed are shown in the adjacent Figure 7(b). Essentially the same trends as hover are reflected but the region of positive design margin is enlarged. This can be partly attributed to different performance of the

vehicle in this flight condition (such as the empennage becoming effective in forward flight) but also due to different HQ specification requirements being applied for this forward flight condition, which also has a secondary effect in that the CONDUIT control system gains are optimized differently. The design margin concept is useful here, as many of HQ specifications are not common between hover and forward flight, and the concept of the margins provides a constant metric of HQ performance across the changing requirements.

The outcome of only achieving a positive design margin in a small portion of the parameter space led to a second sweep for the single main rotor configuration, the results are shown in Figure 8. The plots show the yaw axis design margins but for a slightly different set of design parameter variations. The variation in the tail rotor size is retained but this time larger tail rotors are examined. However, to ensure design geometry “consistency”, instead of specifying the location of the tail rotor directly, a tail rotor clearance (modifying its longitudinal position with respect to the main rotor) was varied. Specifying the clearance was necessary to ensure that the larger tail rotors did not impinge the main rotor disk – and was a more convenient and efficient method than manually recalculating the rotor positions, especially when the NDARC sizing automatically configures the main rotor disk size. Finally, and simply for comparative purposes, instead of actuator bandwidth, the tail rotor actuator rate limit was varied.

图片摘要：该图片与(a) yaw axis HQ design margins v design parameters, 0kts；(b) yaw axis HQ design 这部分内容相关。
![](images/68fc04fa3442ccdad9829852bc9e06f3d4e7ed02ea9a7c7a1bebe2a11fac2be0.jpg)

图片摘要：该图片与(a) yaw axis HQ design margins v design parameters, 0kts；(b) yaw axis HQ design 这部分内容相关。
![](images/b64051a2035970592dbea7415455d9c01b9df4a2988ffecf58838aa96dc2aad2.jpg)

图片摘要：该图主要展示 7 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/ab7300462c34299d7e5f543c058f06678aab5f50181e7e45151b3b1e20348e1f.jpg)

图片摘要：该图片与(a) yaw axis HQ design margins v design parameters, 0kts；(b) yaw axis HQ design 这部分内容相关。
![](images/71b914afa85d368234c74952f185b59fdbd978845674bc7ea1a2b202b74ca2b9.jpg)  
(a) yaw axis HQ design margins v design parameters, 0kts   
(b) yaw axis HQ design margins v design parameters, 80kts

图片摘要：该图主要展示 7 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/f736d6856bfb16fd3b3c3492c00b01bc8bc4da757304d682409bb62171cd0b09.jpg)  
Figure 7 Single main rotor helicopter feed-forward/feedback yaw axis HQ design margins v tail rotor radius, tail rotor non-dimensional longitudinal position (X/L), tail rotor collective actuator bandwidth at various speeds, sea level

图片摘要：该图主要展示 7 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/77e0fd6590099963cc45caa0d27edc60bc6ebba9f6c3ad9788746c536462eea5.jpg)

图片摘要：该图主要展示 7 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/fec5cc355c9148b514b8dfb60c88f05e1f026d8320623c47945750d9d2f7baf5.jpg)

图片摘要：该图主要展示 7 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/7d2b75f17846e4266f0f3ba61d07042f9f4868d3b8a385fb895fed26cfc88b56.jpg)  
(a) yaw axis HQ design margins v design parameters, 0kts   
(b) yaw axis HQ design margins v design parameters, 80kts   
Figure 8 Single main rotor helicopter feed-forward/feedback yaw axis HQ design margins v tail rotor radius, tail rotor non-dimensional longitudinal clearance, tail rotor collective actuator rate limit at various speeds, sea level

图片摘要：该图主要展示 8 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/825df4a55d4eb92b2974cfe0a04eed6c6be9af0e278cceee2d4d4b8a00cf4c3c.jpg)

图片摘要：该图主要展示 8 Single main rotor helicopter feed forward/feedback yaw axi。
![](images/e8c03ea6c18fcc0ec20b58e37b3630f4ab3d231614f3d08357078eef0347d363.jpg)  
(a) tail rotor radius, longitudinal position (X/L), actuator bandwidth (b) tail rotor radius, longitudinal clearance, actuator rate limit   
Figure 9 Single main rotor helicopter empty weights v design parameters for two different parameter sweeps

At hover in Figure 8(a), a larger region of cases now equal or exceed the $0 \%$ design margin in feed-forward (feedback is at the $+ 6 0 \%$ limit in all cases). Actuator rate limiting is an influential factor, with its increase enabling a greater proportion of the rotor size/clearance cases to meet the $0 \%$ or better yaw axis design margin. The change to the forward flight speed condition (b) again enlarges the region of cases with positive design margins.

The empty weight for the two sweep sets for the single main rotor configuration is compared in Figure 9 . Figure 9(a) shows that for the tail rotor size reduction the vehicle empty weight actually increases. The reduced size tail rotors are increasingly inefficient and require greater power, which increases weight for a number of the other components of the vehicle. In the second set of sweep cases in Figure 9(b) a minimum weight region is observed between the smallest and largest tail rotors and toward the larger tail rotor clearance positions.

# Discussion of SIMPLI-FLYD in conceptual design and future developments

The current paradigm for the use of SIMPLI-FLYD in an overall vehicle conceptual design process is that the computed HQ design margins would set the constraints for an optimization i.e. some minimum is required, $0 \%$ or perhaps a positive margin while other design objectives are maximized or minimized, such as the empty weight. Defining appropriate design margin levels more conclusively for conceptual design will require the analysis of SIMPLI-FLYD in an analysis with many more multidisciplinary design constraints. Additionally, an assessment of the HQ constraints choices made in SIMPLI-FLYD will require retrospective analysis from later in the design lifecycle –i.e. using higher fidelity tools, models and data available in detailed design

to analyze the assumptions and constraints made in the conceptual design phase.

The handling qualities characteristics and subsequent design margins vary across the flight envelope due to both the changing performance of the vehicle and the specifications applied. For the tiltrotor, using the pitch axis in airplane mode example, greater criticality emerges mostly at low speed, but not exclusively, with design margin degradations occurring at the higher speed for other reasons. This raises questions about how many handling qualities flight condition analyses should be included. Clearly, if the vehicle can hover and fly at some forward speed a minimum of two should be assessed, but more could be incorporated. NDARC’s sizing typically uses 3-5 critical flight conditions and a similar approach could be taken for the handling qualities analysis with the approach of some baseline characteristics at a couple of nominal flight conditions being “ensured”. Alternatively, an approach that perhaps brackets the operational envelope with min/max airspeed, min/max altitude plus certain configuration changes (e.g. rotor tilt) might be required or considered prudent. The results thus far tend toward a recommendation for the latter but it may be dependent on the level of effort required/appropriate for handling qualities in conceptual design.

Currently, there is no requirement for how much computational time should be allowed for the handling qualities analysis in conceptual design but if the objective is to explore very large parameter spaces rapidly, the 15-20 minute time per flight condition of the current approach is likely a limiting factor. For comparison, NDARC typically completes its sizing task in times of the order of seconds. Possible solutions might be a faster running version of SIMPLI-FLYD by streamlining its tasks or

incorporating an analogous but alternative approach to the full CONDUIT optimization. Alternatively, a framework that analyzes the handling qualities in a less tightly-coupled approach might allow for the current computational times.

During the development of derivative sensitivity analysis, it became apparent that the process of importing the NDARC parameters to SIMPLI-FLYD for the calculation of the stability and control derivatives is one of a series of steps in a process of translation and reduction of parameters, as outlined in Figure 10. At the beginning is an aircraft design in NDARC, defined by hundreds, if not thousands, of parameters defining the geometry, aerodynamics, weights and power. Of these parameters, on the order of 150-250 are imported by SIMPLI-FLYD to define the flight dynamics models with a few additional parameters to define the control actuator characteristics. The flight dynamics (if restricted to rigid-body, 6-DoF) are essentially described by 36 stability derivatives and a minimum of 24 control derivatives. These, in conjunction with the optimized control system gain parameters, determine the approximately 10-20 HQ (feedback and feedforward) specifications per axis. The most limiting specifications then determine the overall HQ design margins which number up to eight, two parameters per axis, for feedback and feedforward. Examining the steps of the overall NDARC/SIMPLI-FLYD coupled process it appeared there might be utility in studying the sensitivity between the parameters of all of the constituent steps. The basis of such an approach would be to allow a piece-wise “chain of sensitivity” to be identified instead of treating the whole process as a “black box”. For example, a user may trace the sensitivity of a subset of specifications to a subset of derivatives which in turn are only sensitive to a particular subset of input parameters.

Thus far, the only NDARC/SIMPLI-FLYD sub-stage sensitivity study that has been carried out is the sensitivity of the stability and control derivatives to the SIMPLI-FLYD internal parameters. The method offers useful insight into which design parameters are the most important to determining the key stability derivatives for the handling qualities. Admittedly in the cases examined, the aircraft designs are well understood (a main wing-aft tail “airplane” and single main rotor/ tail rotor configuration), so any experienced flight dynamics engineer would have been able to predict the majority of the outcomes of the sensitivity sweeps. There are, however, a number of limitations of the approach which should be highlighted. The results are likely configuration-specific, and they are a further simplification, as coupling effects between design parameters on the models are neglected as per classical linear theory. Furthermore, the technique does not consider the effect of performing a re-optimization of the CONDUIT control system gains after a design change. The re-optimization would attempt to rebalance the gains to maximize HQ performance and thus any determined sensitivity is not at the “optimal control design” point, which may lead to further inaccuracies when compared to the full process.

Nevertheless, the key advantage is that the calculations for the stability and control derivative and the other sub-stage sensitivity analyses are much faster to calculate. In fact, the whole chain of sensitivities are faster to calculate than the full process, and for many more parameters, due to the fact that no re-optimization of the control system would be carried out. It is the CONDUIT optimization that is the major computational cost to the current process. If a simplified surrogate analysis could be developed, a framework incorporating frequent calls of the fast, simplified analysis alongside the more computationally expensive full CONDUIT optimization might lead to an overall more computationally efficient approach for conceptual design.

图片摘要：该图主要展示 10 Schematic showing the reduction of the number of paramete。
![](images/f658b24c60f403c70fe9d3126cdd8065ae34f14e586a71cb83dd1123bc2c6328.jpg)  
Figure 10 Schematic showing the reduction of the number of parameters from NDARC model to SIMPLI-FLYD handling qualities design margins

There is clearly a tradeoff between computational resources and the number of analyses and the rigor they contain. This tradeoff, coupled with the number of potential variables that could be involved also highlights challenges in how handling qualities should be managed in an optimization. A human in the loop would seemingly be overwhelmed by the number of potential variables that could be used to influence the handling qualities although other design constraints (with greater priority) may rapidly reduce the number of variables that the handling qualities aspects may reasonably be allowed to influence. Solutions to this challenge have not yet been identified but techniques like the stability and control sensitivity analysis could also form the basis of a tool to guide an engineer using SIMPLI-FLYD, either to help users that do not possess the relevant handling qualities knowledge or to inform when a configuration is non-classical and where usual rules-of-thumb cannot be relied upon.

Another important aspect of the current SIMPLI-FLYD capability to highlight is the method of representing inertia changes via the weight change combined with radii of gyration. This method is likely to be only satisfactory for gross changes in design weight, and as long as the vehicle configuration does not vary drastically, and probably does not possess the level of sensitivity/fidelity for the design changes such as those being applied in these examples. A future development that will improve this is the anticipated integration with the U.S. Army ADD developed “ALPINE” (Automated Layout with a Python Integrated NDARC Environment) tool ref [15]. ALPINE provides a capability to generate a 3-D geometry in OpenVSP (Open Vehicle Sketch Pad [16]) from NDARC output and thus enables a calculation of the mass and inertia properties using OpenVSP’s mass properties functions which are more sensitive to arbitrary configuration changes.

Indeed, a 3-D geometry engine approach to managing the design configuration such as that provided by OpenVSP would be also advantageous when manipulating a design’s geometry (manually or automatically). This became apparent during the work in this paper, as even for these relatively simple cases, such as when moving a tail, or changing its size, so that the fuselage adjusts to support the tail, ensuring geometry consistency is difficult to manage (NDARC has features that addresses some aspects but is not comprehensive). Geometry consistency is not only important to ensure that the design is valid structurally (i.e., components are attached), but also for capturing design cross-couplings from a handling qualities perspective. For example, moving the horizontal tail for better handling qualities/weight savings may impact the vertical tail location, depending on the configuration, and thus may affect the lateral-directional characteristics. This experience in ensuring geometry consistency correlates with the considerations of Ref [17], which also places great value in integrating a 3-D geometry engine at the heart of any future conceptual design environments.

Finally, the results in this paper reinforce the conclusions of prior results using SIMPLI-FLYD Ref [7] that the actuator characteristics play an important role in determining the handling

qualities design margins. Cost models for the actuators in terms of weight, size, power and cost as function of their performance characteristics must be incorporated into this analysis so their selection can be properly accounted for if the handling qualities are to be considered in a conceptual design.

# Summary and Conclusions

This paper has reported the continued exploration of the recently developed SIMPLI-FLYD toolset. The use of Python-based scripting has enabled the integration of NDARC and SIMPLI-FLYD in fully automated analyses for design parameter variations that has accelerated the learning of how a handling qualities analysis interacts with conceptual design models. Processes have been demonstrated that can calculate design margins with respect to handling qualities specification criteria while also evaluating the vehicle design weight and other design metrics. Also, secondary techniques like the bare-airframe stability and control derivative sensitivity analysis offer insight to the inner-workings of a complex process. They may also offer pathways to mitigate the computational cost of running full CONDUIT optimization so frequently if faster run times become a requirement.

Through using the tools in a coupled approach to examine different vehicle types while varying a mix of design parameters and flight conditions, and evaluating different handling qualities problems, the following items are highlighted:

The calculated handling qualities design margins vary across the flight envelope due to both changing flight dynamic and control characteristics and the handling qualities requirements specifications applied.   
The current SIMPLI-FLYD analysis process for a single flight condition, compared to other conceptual design tools, is relatively computationally expensive. This cost is either likely to impose constraints on how to deploy the tool in an overall design process or will require further evaluation of what HQ aspects should be incorporated in attempt to gain computational efficiencies.   
The challenge of ensuring a consistent vehicle geometry when performing the analysis in this paper have highlighted the advantages for representing and maintaining a consistent geometry while adjusting a design such through using a 3-D geometry engine such as OpenVSP.   
The actuator performance characteristics influence the handling qualities design margins strongly and therefore including their cost (in terms of weight, power requirements etc.) is critical if handling qualities are to be included in an overall design optimization.

# Acknowledgements

The authors would particularly like to acknowledge Larry Meyn, NASA Ames Research Center, for his support in the development of the Python scripts and the provision of the “rcotools” library that supported their development. Andrew Gallaher, U.S. Army ADD, Moffett Field is acknowledged for his OpenVSP insight and Python development advice.

# References

[1] Gorton, S.A., Lopez, I., and Theodore, C.R, “NASA Technology for Next Generation Vertical Lift Vehicles”, AIAA SciTech, $5 6 ^ { \mathrm { { t h } } }$ AIAA/ASCE/AHS/ASC Structures, Structural Dynamics and Materials Conf., Kissimmee, FL, USA, $5 { \cdot } 9 ^ { \mathrm { t h } }$ January, 2015.   
[2] Morris, C. C., Sultan, C., Allison, D. L., Schetz, J. A., & Kapania, R. K., “Towards Flying Qualities Constraints in the Multidisciplinary Design Optimization of a Supersonic Tailless Aircraft.”, 12th AIAA Aviation Technology, Integration, and Operations (ATIO) Conference and 14th AIAA/ISSM, Indianapolis, IN, USA, 17-19 Sep 2012.   
[3] Raymer, D.P., “Aircraft Design: A Conceptual Approach”, American Institute of Aeronautics and Astronautics Inc, $5 ^ { \mathrm { t h } }$ Ed., 2006.   
[4] Padfield, G. D. “Rotorcraft Handling Qualities Engineering; managing the tension between safety and performance”. Journal of the American Helicopter Society, Vol. 58 (no. 1). pp 1–28, January, 2013.   
[5] Andrews, Harold, Technical Evaluation Report on the Flight Mechanics Panel Symposium on Flying Qualities, AGARD-AR-311, April 1992.   
[6] Johnson, W., “NDARC — NASA Design and Analysis of Rotorcraft, Theoretical Basis and Architecture”, American Helicopter Society Aeromechanics Specialists’ Conference Proceedings, San Francisco, CA, January 20-22, 2010.   
[7] Lawrence, B., Berger, T., Theodore, C.R., Tischler, M.B., Tobias, E.L., Elmore, J., and Gallaher, A., “Integrating Flight Dynamics & Control Analysis and Simulation in Rotorcraft Conceptual Design”, 72nd American Helicopter Society Annual Forum, West Palm Beach, FL, USA, May 17-19, 2016.   
[8] Johnson, W. “NDARC, NASA Design and Analysis of Rotorcraft.” NASA TP 2009-215402, 2009.   
[9] Tischler, M. B., Colbourne, J., Morel, M., Biezad, D., Cheung, K., Levine, W., and Moldoveanu, V., “A Multidisciplinary Flight Control Development Environment and Its Application to a Helicopter,” IEEE Control Systems Magazine, Vol. 19, No. 4, pg. 22-33, August, 1999.   
[10] Tischler, M. B., Remple, R. K., Aircraft and Rotorcraft System Identification: Engineering Methods and Flight Test Examples, 2nd Edition, AIAA, 2012, pp 332-333.   
[11] Anon., "Handling Qualities Requirements for Military Rotorcraft", Aeronautical Design Standard-33 (ADS-33E-PRF), US Army Aviation and Missile Command, March 21, 2000.   
[12] Anon., “Flying Qualities of Piloted Aircraft,” MIL-STD-1797B, Department of Defense Interface Standard, February, 2006.   
[13] Forrester, I.J., Sóbester, A. Keane, A.J., Engineering Design via Surrogate Modelling: A Practical Guide, John Wiley & Sons, 2008.   
[14] Duda, H., “Prediction of Pilot-in-the-Loop Oscillations due to Rate Saturation”, Journal of Guidance, Navigation, and Control, Vol. 20, No. 3, May-June 1997.

[15] Perry, T. " ALPINE: Automated Layout with a Python Integrated NDARC Environment, OpenVSP Workshop 2016, NASA Ames Research Center, Moffett Field, CA, USA, $2 5 ^ { \mathrm { t h } }$ Aug 2016 [PDF File] https://nari.arc.nasa.gov/sites/default/files/attachments/34A LPINE%20%28002%29_Perry.pdf   
[16] Gloudemans, J. R., Davis, P. C., and Gelhausen, P. A., “A rapid geometry modeler for conceptual aircraft”, 34th Aerospace Sciences Meeting and Exhibit, AIAA-1996-52, Jan. 15-18 1996.   
[17] Johnson, W., and Sinsay, J.D., “Rotorcraft Conceptual Design Environment”, $2 ^ { \mathrm { n d } }$ International Forum on Rotorcraft Multidisciplinary Technology, Seoul, Korea, Oct 19-20, 2009.
