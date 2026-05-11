图片摘要：该图片为文档封面或首页内容，主题与Control Law/Concept Evaluation Envelope Expansion相关。
![](images/39b58da3e7356f6e2e8d1e89a0b1f9b86e471b7b0a9149c11283e2d3121503bc.jpg)  
Fig 13 The Four Phases in a Control Law Life Cycle

AFCS. But the experimental control laws were the raison d'etre for the ACT Lynx project, and needed a different approach to their development.

# Control Law/Concept Evaluation - Envelope Expansion

Recognising that immaturity would be a normal part of the development of ACT Lynx laws, a Control Law Life Cycle Model and associated working practices and procedures were developed at DRA to ensure a disciplined path to full control law validation (Ref 18, 19). The development cycle was formalised to ensure that when control laws were ultimately exercised in safety critical areas, there would be no possibility of them failing. Thus, along with the hardware redundancy, the system would have a truly comprehensive fail-operate capability. The cycle comprises four phases (Fig 13);

i) The Conceptual Phase (CP) evaluates basic concepts in a form that can capture the operational requirements. It includes simple modelling, design and analysis activities and pilot-in-the-loop simulation. Outputs from this phase include knowledge of the response types and system characteristics required to achieve the various Levels of flying quality.

ii) The Engineering Design Phase (EDP) takes results from the CP and involves full control law design with a representative vehicle model and includes refinements to control system architectures via detailed modelling and extensive piloted simulation.

iii) The Flight Clearance Phase (FCP) consolidates results from earlier stages and achieves a verified implementation for the target flight control computer. Validation of the design, including a loads and stability analysis, is a key activity in the Clearance phase. The techniques of 'Inverse Simulation' (Ref 20), with prescribed MTEs, offer a convenient and efficient method for exercising the control law in a wide range range of representative conditions prior to flight.   
iv) The Flight Test Phase (FTP) evaluates the control system in full scale flight and appropriate operational MTEs. Experiments in this phase will be 'replicas' of tests conducted in ground-based simulation and changes to control laws would cover only those regimes mapped out in the Conceptual and Engineering Design phases. An incremental approach to safety critical, high risk, flight conditions would be normal practice.

The phases are sequential but also iterative, acknowledging that growth in knowledge can lead to a change in the requirement or criteria format, often the objective of the research itself. At all stages, the discovery of a fault, design error or uncertainty will generally require the return to a previous phase. Special care needs to be taken when 'imposing' a procedural discipline on research, that creativity is not inhibited, but the discipline needs to cut even deeper with well defined working practices and activities, if it is to have any real meaning as a safeguard against errors or faults being designed in. Fig 14, taken from Ref 18, illustrates a process structure diagram for the CP with the three principal tasks - problem expression,

图片摘要：该图片为文档封面或首页内容，主题与Control Law/Concept Evaluation Envelope Expansion相关。
![](images/fddcddcda826a55e7a2bf312bcc95f90a28a90f43e55598dcf295f89f881945f.jpg)  
Fig 14 Structure Diagram for the Conceptual Phase

design and review. The JSD notation is again used, ie sequence, iteration $(\ast)$ and selection (o), with the activities corresponding to the lowest level 'leaves' on each branch. Typically, documentation is required as each new piece of knowledge is accumulated and this is reflected in the right hand leaf of the branches.

# Conceptual Phase

Examples of research in the Conceptual Phase can be found in References 21, 22 and 23. The archetypal DRA conceptual simulation model (CSM) was developed in Reference 21, which reported comparative results with different response types and autopilot modes. In Reference 22, the first conceptual results from the DRA/Westland research into carefree handling systems were published, indicating the significant benefits of direct intervention control laws. More recently, the first helicopter trials on the DRA Large Motion Simulator reported the achievement of Level 1 handling qualities for rate response types (Ref 23). Fig 15 shows one set of results from Reference 23, with pilot handling qualities ratings plotted against roll attitude bandwidth for a slalom task. The wide spread of ratings with each configuration illustrate the change in perceived handling as performance is increased, the poorest ratings generally corresponding to the highest levels of pilot aggressiveness.

图片摘要：该图片与Fig 15 HQRs for Slalom MTE Flown With DRA Conceptual Simulation Model；The ADS33C这部分内容相关。
![](images/fd40ff23c34638a810721f62731202e53d78f96181f4cb993d6b12e8cd43899e.jpg)  
Fig 15 HQRs for Slalom MTE Flown With DRA Conceptual Simulation Model

The ADS33C Level1/2 bandwidth boundary for nontracking tasks is 2 rad/s, corresponding with the lowest level of aggressiveness flow in the AFS trials. The degradation at higher performance levels is consistent with flight results (Ref 2), but pilots tend to be more sensitive to task cues and critical of simulator deficiencies as aggressiveness increases. Flying at large attitude angles near the ground is particularly demanding on the fidelity of the simulated visual cues; the limited vertical field of view and texture on the current AFS visual system must be a major factor in the inability to achieve Level 1 at high performance. This deficiency, along with modelling uncertainties, common to all ground-based simulators, is, of course, a primary reason for the vigorous pursuit of high performance in-flight simulators.

# Engineering Design Phase

This phase consists of mapping the required characteristics from the CP onto the simulated target aircraft. As in the CP, problem expression, design and review cover activities in the Engineering Design phase. However, the level of detail will be considerably greater, including environmental constraints and robustness criteria. Internal control system loop performance requirements and stability of uncontrolled airframe modes will form parts of the problem expression. The design sub-phase contains the modelling and evaluation activities, as in the CP, but also includes significant new activities under the synthesis label (Ref 18). The desired flying qualities requirements, embodied in handling and ride quality functions, will be cast in functional form and the associated 'error' cost functions minimised with respect to control system gains and filter frequencies. This is the essence of the synthesis at the centre of control law design and a number of different techniques are available for working the optimisation, involving craft-like skills and trading performance and robustness to achieve the best controller. Examples of results from the Engineering Design phase are reported in Refs 24, 25 and 26.

# Clearance and Flight Test Phases

Activities within this phase have not been well developed at DRA for the helicopter application. The clearance activities will include software verification and a degree of validation using more comprehensive models than in earlier 'real-time' evaluations, with the control law now embedded in the target hardware. Flight tests represent the ultimate research evaluation, although ironically, here there is little scope for design innovation and creativity. Flight test is essentially a knowledge gathering exercise, but there is considerable scope for innovation in experimental design. A procedure sequence in the evaluation of a control law might take the form;

i) engage ACT system when in required flight condition,

ii) build up task complexity and aggressiveness incrementally

iii) curtain function cleared for minimum flight envelope initially (low aggressiveness)   
iv) open curtain incrementally as aggressiveness increased   
v) test control law at safe altitude initially with representative task gain (eg using helmet display)   
vi) test control law at low altitude with representative natural task cues

Throughout this process, regular reviews of the documented results with results from previous phases will be required. A fully developed control law, enabling Level 1 flying qualities at high agility levels, should never experience a software 'failure'. Hardware failures will be protected against to a high reliability through redundancy. Inadvertent excursions beyond flight envelope limits will be protected against with built-in carefree handling functions, working as an integral part of the control law.

# Conclusions and Recommendations

With the aim of developing a high performance ACT research helicopter, the DRA has developed the ACT Lynx concept; focus has been on research at high agility levels to explore carefree handling concepts and the expansion of the helicopter's usable flight envelope. The inherent high agility of the Lynx, with its hingeless rotor, makes it an excellent airframe for establishing requirements for future types. This paper has reviewed this project from the standpoint of the conflict between safety and performance; we can see a way through but a number of concurrent safety nets need to be combined.

1) A highly skilled and motivated safety pilot with backdriven conventional controls is the most important safety net; exploratory simulation studies conducted at DRA have focussed on recoveries to common mode hardover failures. The results have highlighted recovery times generally consistent with past flight experience although torque, rotorspeed and 'g' limits can easily be exceeded.   
2) System redundancy providing a fail-operate/fail-safe capability provides the strongest and most effective safety net against hardware failures.   
(3) A comprehensive requirement specification developed through simulation ensures that the integrated system is well understood and all functions and their operations are fully defined; this approach ensures that the 'fixed' software is coherent and fully validated, hence providing the most effective protection against common mode software failures.   
(4) Control laws developed within the framework of an iterative life-cycle, including ground based simulation, ensures protection against software errors during the early development stages of this critical element of the system. The four phases - conceptual, engineering, clearance and flight - have been briefly described.

5) Curtain functions, limiting the actuator drive signals, can also be used to protect against immaturity in the control laws and can be opened incrementally to allow more agility to be exploited.   
6) A commitment to carefree handling functions embedded within the control laws is considered to be an essential ingredient to ACT research if full agility is to be realised. Ultimately, together with the safety pilot and FOFS hardware, this should complete the triad of safety nets necessary for the synergy of performance and safety.   
At the time of writing, the UK programme is at a hiatus due to funding limitations. In this paper the authors have attempted to provide a candid exposure of some of the issues surrounding the safety/performance conflict, to stimulate a continuing debate with collaborative partners pursuing similar goals. It is believed that flight research at high agility levels will only be possible, with acceptable risk, if these issues are squarely faced.

# Acknowledgement

The research reported in this paper was conducted as part of the UK MoD's Applied Research Programme - Package 3D (Tri-Service Helicopters).

# References

1 Padfield, G.D., Lappos, N., Hodgkinson, J.; "The Impact of Flying Qualities on Helicopter Operational Agility"; AHS/NASA Conference on Flying Qualities and Human Factors of Vertical Flight Aircraft; San Fransisco, Jan 1993   
2 Charlton, M. T., Padfield, G. D., Horton, R. I.; "Helicopter Agility in Low Speed Maneuvres"; Proceedings of the 13th European Rotorcraft Forum, Arles, France, Sept 1987 (also RAE TM FM 22, April 1989)   
3 Morgan, M.; "Airborne Simulation at the National Aeronautical Establishment of Canada", AGARD CP 408 'Flight Simulation', 1985   
4 Hartman, L.J. et al; "Testing of the Advanced Digital Optical Control System" 43rd AHS Forum, St Louis, May 1987   
5 Damotte, S. et al.; "Evaluation of Advanced Control Laws with a Sidestick Controller on the Experimental Fly-by-Wire Dauphin Helicopter"; 18th European Rotorcraft Forum, Avignon, France, Sept 1992   
6 Bouwer, G. et al; "ATTHeS - A Helicopter In-Flight Simulator with High Bandwidth Capability", 48th AHS Forum, Washington, June 1992   
7 Hindson, William S.; "Past Applications and Future Potential of Variable Stability Research Helicopters", Helicopter Handling Qualities, NASA CP 2219, April 1982

8 Gupta, B.P. et al.; "Design, Development and Flight Evaluation of an Advanced Digital Flight Control System", 43rd AHS Forum, St Louis, May 1987   
9 Kimberley, A.M., Charlton, M.T.; "ACT Lynx Safety Pilot Simulation - Trial Runaway"; RAE Working Paper WP(89) 031, June 1989   
10 Padfield, G.D., Bradley, R., Moore, A.; "The Development of a Requirement Specification for an Experimental Active Flight Control System for a Variable Stability Helicopter - an Ada Simulation in JSD"; AGARD CP 503, 'Software for Guidance and Control', Scpt 1991   
11 Padfield, G.D., Bradley, R.; "Creation of a Living Specification for an Experimental Helicopter Active Control System Through Incremental Simulation"; Proceedings of the 17th European Rotorcraft Forum, Berlin, Sept 1991   
12 Jackson, M.; System Development. Prentice Hall, 1983.   
13 Cameron, J. R.; JSP & JSD: The Jackson Approach to System Development. IEEE Computer Society Press, 1983.   
14 Michael Jackson Systems Ltd., Version 3 of Speedbuilder for IBM PC/Compatible: Installation Guide, MJSL, 1989.   
15 Lawton J R & France N. "The Transformations of JSD Specifications in Ada". Ada User, Jan 1988.   
16 Bradley, R., "A Method for Specifying Complex Systems with Application to an Experimental Variable Stability Helicopter", Ph.D. Thesis, Glasgow University, 1992.   
17 Silva, A.; "Mode Synchronisation Algorithm for Asynchronous Autopilot", Fourteenth European Rotorcraft Forum, Milan, 1988.   
18 Tomlinson, B.N., Padfield, G.D., Smith, P.R.; "Computer Aided Control Law Research - from Concept to Flight Test"; AGARD CP 473 'Computer Aided System Design and Simulation', August 1990   
19 Padfield, G.D., Tomlinson, B.N., Smith, P.R.; "Management of Computer Aided Control System Design from Concept to Flight Test"; 'Safecomp'90, Safety of Computer Control Systems, IFAC Symposia Series, 1990, No 17   
20 Bradley, R., Thomson, D.; "The Development and Potential of Inverse Simulation for the Quantitative Assessment of Helicopter Handling Qualities", AHS/NASA Conference on Flying Qualities and Human Factors of Vertical Flight Aircraft, San Francisco, Jan 1993

21 Buckingham, S. L., Padfield, G. D., "Piloted Simulations to Explore Helicopter Advanced Control Systems"; RAE Tech Report 86022, April 1986   
22 Massey, C., Wells, P.M.; "Helicopter Carefree Handling Systems"; Proceedings of RAeSoc Conference on Helicopter Handling Qualities and Control, London, Nov 1988   
23 Padfield, G.D. et al., "Helicopter Flying Qualities in Critical Mission Task Elements"; 18th European Rotorcraft Forum, Avignon, France, Sept 1992   
24 Yue, A., Postlethwaite, I., Padfield, G.D.; "H Design and the Improvement of Helicopter Handling Qualities"; Proceedings of the 13th European Rotorcraft Forum, Arles, France, Sept 1987, Also Vertica, Vol 13 No 2, 1989   
25 Manness, M.A., Murray-Smith, D.J.; "Aspects of Multi-Variable Flight Control Law Design for Helicopters using Eigenstructure Assignment", J. AHS, Vol 37, No 3, July 1992   
26 Walker, D. et al; "Rotorcraft Flying Qualities Improvement Using Advanced Control"; AHS/NASA Conference on Flying Qualities and Human Factors of Vertical Flight Aircraft, San Fransisco, Jan 1993

(C) British Crown Copyright 1993/MoD

Reproduced with the permission of the Controller of Her Britannic Majesty's Stationery Office

Session 3

Modeling and Analysis Techniques

# COMPATIBILITY OF INFORMATION AND MODE OF CONTROL: THE CASE FOR NATURAL CONTROL SYSTEMS

Dean H. Owen

Department of Psychology University of Canterbury Christchurch, New Zealand

The operation of control systems has been determined largely by mechanical constraints. Compatibility with the characteristics of the operator is a secondary consideration, with the result that control may never be optimal, control workload may interfere with performance of secondary tasks, and learning may be more difficult and protracted than necessary. With the introduction of a computer in the control loop, the mode of operation can be adapted to the operator, rather than vice versa. The concept of natural control is introduced to describe a system that supports control of the information used by the operator in achieving an intended goal. As an example, control of speed during simulated approach to a pad by helicopter pilots is used to contrast path-speed control with direct control of global optical flow-pattern information. Differences are evidenced in the performance domains of control activity, speed, and global optical flow velocity.

"Smart" mechanisms for perception and control. It might be supposed that other flying animals have "smart" perceptual mechanisms (Runeson, 1977) for acquiring information that maps directly onto an action system specialized for controlling flight. In contrast, human flight must be mediated by a vehicle. Whereas the human's perceptual mechanisms may be sufficiently smart to pick up the

relevant information, manipulation of the control surfaces is apt to be quite foreign to an animal whose effectiveness (ways of being effective) and prior experiences involve adaptation to terrestrial locomotion. Smart action systems can evolve to support flight control by other flying animals, but for human control of flight they must be developed and tested. The flight environment demands that the principles be the same.

Accordingly, human guidance of flight can be described (a) in terms of the manipulation of controls, control surfaces, and power, (b) control of the path, speed, and orientation of the aircraft, or (c) control of the information which specifies where one is headed, at what speed and orientation, and the consequences of continuing without change. The last description has advantages for the development and evaluation of control systems because it keeps the variables to which the pilot is sensitive and the variables to be controlled in the same currency, i.e., in the domain of visual information. In performing a maneuver, the pilot cycles between sampling the information available and performing control adjustments to reduce deviations from desired optical conditions, repeating the perception-action cycle until satisfactory visual conditions have been achieved. As a consequence, the information

acquired by perceiving and the information controlled by acting must be the same. The compatibility between control adjustments and visual guidance of flight could be maximized by giving the pilot direct control of the informative variables.

The nature of information to be controlled. A canonical assumption of the direct theory of visual perception (Gibson, 1979) is that detection and control of any property of self motion must be supported by information. This holds for selecting and modulating a control action, timing the initiation and termination of the action, and observing the consequences of the action. In the case of visual guidance, the information is assumed to be one or more invariants in the surrounding, transforming optic array along the path of motion. Applications have been extended to rotocraft flight (Owen, 1991), simulation research (Owen & Johnson, 1992; Warren & Owen, 1982), and transfer of training (Lintern 1991).

The research approach first isolates variables in the optic array between the eye and environmental surfaces mathematically and operationally (through manipulation of scene-content and flight parameters). Second, experiments are conducted to determine which of the potential sources of visual information are functional, i.e., useful for detecting changes in speed and direction and for selecting and guiding a control action. To date, functional variables have been exclusively fractional rates of change characterized by higher-order ratios of such lower-order variables as speed, acceleration, altitude, climb or sink rate, and ground-texture-element size and

spacing. The eyeheight of the observer above the ground is an optically privileged scalar for size, distance, and speed, and therefore fundamental to the perception and control of visual information. See Owen & Warren (1987) and Owen (1990) for summaries of the experiments.

Control of optical variables. If the criterion for skillful behavior is taken to be effective control of the informative structure of stimulation, then its study requires an active psychophysics that treats transformations and invariants in the ambient array as dependent variables (Owen & Warren, 1982; Warren & McMillan, 1984; Flach, 1990). Controlling self motion involves maintaining intended conditions of speed and direction of flight, as well as self orientation, relative to environmental surfaces. In the process, variables are linked and unlinked as speed, direction, and orientation change. With knowledge of the relevance of the different kinds of information to different kinds of flight tasks, the variables and their linkages can be controlled to achieve intended goals. The same ambient array properties which were independent variables in passive judgment experiments can be recorded as dependent variables in the study of active control.

Direct or natural control. Using the cyclic and collective, helicopter pilots currently make an average of 50 control adjustments per minute during an approach to hover above a place on the ground. Pilots are instructed to keep "visual streaming" constant at the rate of a brisk walk during an approach to hover. Control systems for helicopters and other

aircraft have been designed primarily around mechanical constraints, including those of cables, levers, and hydraulic systems. The development of electronic and optical systems communicating between controls and control subsystems, including power, allows for the implementation of "smart" control systems designed to provide a match between the sensitivity of the human perceptual system and the effectivities of the human-vehicle action system. Thus, a computer in the control loop can allow a hybrid between manual and supervisory control: The pilot maintains higher-order control (e.g., over path slope), while the computer manages the lower-order control tasks (power, rotor variables).

The logic is similar to that employed by Roscoe and Bergman (1980) in developing a control system that reduced higher-order control loops for bank angle and vertical velocity to first-order control of heading and vertical position (altitude). Compared to normal flight control, their system reduced pilot errors by a factor of ten. Ratio control differs in providing direct control of the higher-order variables to which the pilot is sensitive. (A simple example is the Vernier log scale for acoustic volume control.) The computer can take inputs from the controls and sensors (e.g., radar altimeter, forward-looking radar, a signal transmitted from the ground or a ship) and make adjustments in speed and direction to match the informational properties of the event that the pilot intended to produce. For approach to the ground or to surfaces with vertical extent, a fractional rate controller can reduce speed in the same proportion as distance to the surface is decreased. The pilot selects a fractional rate

which matches the task demands, e.g., a high rate when time is critical, a low rate when accuracy is important. A second mode of control is appropriate for path angle. Whereas magnitude controllers vary the numerator or denominator of the ratio of vertical speed to ground speed, a path-slope controller varies the ratio directly. Since path slope equals the "dip" angle of the point of optical expansion below the horizon, the path-slope controller gives the pilot control over what he intends to achieve visually. Similar ratio modes could be developed for rotational control.

Advantages of natural control. A control system designed around perception-action compatibility should reduce flight-control demands, freeing the pilot's attention for other workload. Maneuvers under difficult conditions should be simplified. Given that control is scaled in units of distance to the ground, fractional-rate control is particularly appropriate to approach, hover, and low-level contour and terrain following. Modes of control compatible with information acquisition should greatly simplify training and increase safety at low altitudes in cluttered environments and under difficult conditions, e.g., high work load or stress. Although experienced helicopter pilots have shown no sign of negative transfer when using ratio controllers, having a computer in the control loop means that traditional modes of control could be programmed and selected, if desired, by a pilot more comfortable with those modes.

A design criterion for some new aircraft is that "trainability" be taken into account during development of

the aircraft itself. Ratio controllers are relevant to this criterion, since training should be considerably simplified with a high compatibility system having independent modes of control, as compared to the current system involving complicated and sometimes arbitrary relationships between control adjustments and visual stimulation as well as interdependent relationships between the controls themselves. Lintern (1991) has discussed the role of optical information in manual control and transfer of training.

Kurlik (1991) proposed that experts make a task easier because they constrain the task in ways that make the variables controlled much simpler to skillfully control. One reason that the novice may have difficulty learning what to attend to and control is that information emerges during an event. The information which the skilled pilot uses to select, initiate, and terminate control actions may not come into existence until the environment is skillfully controlled (Kurlik, 1991). Ratio controllers should give novices an advantage in that they automatically isolate task-relevant optical variables that are transforming in a specificity relationship with the flight event. In this way, they embed a dimension of skillful performance in the control system itself. Automatic braking systems on automobiles perform a similar function by pulsing the brakes in an optimal fashion to achieve deceleration while avoiding locking up the wheels. Braking performance of a novice driver using the automatic pulsing system should be better than without it, even though the driver is unaware of the mode of operation. Just as information is ordinarily transparent to the perceiver of an

event, the means by which control of an event is achieved via the direct control of information can be transparent to the controller of the event. The test is whether direct control of the variable an operator is sensitive to results in better performance than control of a task-relevant property of the self-motion event itself.

Experimental tests. Two experiments will be used to illustrate direct control of optical flow-pattern information. Experienced pilots with an average of 1,500 hours helicopter flight time participated. In the first experiment, each pilot controlled speed for 25 seconds during 136 simulated approaches to a pad along a linear flight path. In one session the pilot controlled path speed, and in the other he controlled global optical flow velocity (path speed/eyeheight). The approaches were made in 68 different environments designed to determine the relative influences of flow velocity and edge rate on speed control. In the second experiment, each pilot controlled vertical speed on a vertical path to maintain hover at 10 meters for 30 seconds, then descended to the ground while attempting to minimize vertical speed at touchdown. A total of 54 events were produced by combinations of disturbances in the three translational axes crossed with environments that isolated three types of information for change in altitude: change in the horizon ratio of a vertical surface, change in perspective angle of runway edges perpendicular to the horizon, and optical expansion and contraction of fields running parallel to the horizon. In one session, the pilot controlled path speed (sink and climb rate) and in the other he controlled global

optical flow velocity (vertical speed/eyeheight, or fractional change in altitude). Comparisons of the two control modes were made in three performance domains: control activity, speed, and global optical flow velocity.   
Acknowledgements. The preparation of this paper and the research exploring the approach described were supported by the National Aeronautics and Space Administration Grant No. NAGW-2170. The author has benefitted from encouragement by and interaction with the scientific monitor for the grant, Walter W. Johnson, NASA Ames Research Center.

# REFERENCES

Flach, J. M. (1990). Control with an eye for perception: Precursors to an active psychophysics. Ecological Psychology, 2, 83-111   
Gibson, J. J. (1979). The ecological approach to visual perception. Boston: Houghton Mifflin.   
Kurlik, A. (1991). Why does the skilled actor make it look easy? Because it is! Proceedings of the Sixth International Conference on Event Perception and Action (p. 61). Amsterdam, The Netherlands.   
Lintern, G. (1991). An informational perspective on skill transfer in human-machine systems. Human Factors, 33, 251-266.

Owen, D. H. (1990). Perception and control of changes in self motion: A functional approach to the study of information and skill. In R. Warren & A. H. Wertheim (Eds.), Perception & control of self-motion (pp. 289-326). Hillsdale, NJ: Erlbaum.   
Owen, D. H. (1991). Perception and control of rotocraft flight. In W. W. Johnson & M. K. Kaiser (Eds.), Visually Guided Control of Movement (NASA Conference Publication 3118) (pp. 87-97). NASA Ames Research Center, Moffett Field, California.   
Owen, D. H., & Johnson, W. W. (1992). An information-based approach to simulation research. In Feik, R. A. (Ed.), Proceedings of the Future Directions in Simulation Workshop. Melbourne, Australia: Defence Science and Technology Organisation, Aeronautical Research Laboratory, Aircraft Systems Division.   
Owen, D. H., & Warren, R. (1982). Optical variables as measures of performance during simulated flight. Proceedings of the Human Factors Society - 26th Annual Meeting, 1, 312-315.   
Owen, D. H., & Warren, R. (1987). Perception and control of self motion: Implications for visual simulation of vehicular control. In L. S. Mark, J. S. Warm, & R. L. Huston (Eds.), Ergonomics and human factors: Recent research and advances (pp. 40-70). New York: Springer-Verlag.

Runeson, S. (1977). On the possibility of "smart" perceptual mechanisms. Scandinavian Journal of Psychology, 18, 172-179.   
Warren, R., & Owen, D. H. (1982). Functional optical invariants: A new methodology for aviation research. Journal of Aviation, Space, and Environmental Medicine, 53, 977-983.

# A Model for Rotorcraft Flying Qualities Studies *

Manoj Mittal

Post-Doctoral Fellow

School of Aerospace Engineering

Mark F. Costello

Research Engineer

Aerospace Laboratory, GTRI

Georgia Institute of Technology

Atlanta, Georgia

# Abstract

This paper outlines the development of a mathematical model that is expected to be useful for rotorcraft flying qualities research. A computer model is presented that can be applied to a range of different rotorcraft configurations. The algorithm computes vehicle trim and a linear state-space model of the aircraft. The trim algorithm uses non-linear optimization theory to solve the non-linear algebraic trim equations. The linear aircraft equations consist of an airframe model and a flight control system dynamic model. The airframe model includes coupled rotor and fuselage rigid body dynamics and aerodynamics. The aerodynamic model for the rotors utilizes blade element theory and a three state dynamic inflow model. Aerodynamics of the fuselage and fuselage empennages are included. The linear state-space description for the flight control system is developed using standard block diagram data.

# Introduction

In the past, rotorcraft flight control system preliminary design used mathematical models which assumed the fuselage to possess six degrees of freedom. The rotor dynamics were assumed to be substantially faster than the fuselage dynamics and were subsequently approximated as quasi-static. The process of fine tuning the flight control system was accomplished through an extensive flight test program comprised of a matrix of control system parameter variations. While fine tuning of the flight control system is still accomplished through flight testing the vehicle, significant improvements in the optimization process have been realized when high order dynamic rotorcraft models are utilized during the preliminary flight control system design stage.

Rotorcraft are now being designed with sophisticated electronic flight control systems. These complex control systems are utilized not only to satisfy standard flying qualities specifications but also to meet aerodynamic performance, vibration, and structural loads criteria. The design of modern rotorcraft flight control systems now stretches across many different individual disciplines and is indeed interdisciplinary. The general trend toward increased reliance on the flight control system for improving overall system performance has lead designers to consider higher bandwidth systems which rely on high levels of sensor feedback to yield desired aircraft stability. The main drawback of this approach is that increased levels of feedback, which in general improve the low frequency fuselage dynamic behavior, can destabilize higher frequency rotor blade motion. In order to make meaningful estimates of the impact of a particular flight control configuration on system requirements it has been found that a mathematical model which includes fuselage and rotor rigid body dynamics and rotor dynamic inflow is necessary [1].

The business of rotorcraft modeling for flight control system design and analysis support has been an active research area for many years. Deriving the equations of motion of a fully coupled fuselage and rotor system for a reasonably general configuration quickly becomes unwieldy due to complicated geometry including many matrix transformations and intricate logic branching. These complexities have lead engineers to develop digital computer programs which more or less relegate model computation to the computer and free the engineer to focus on analysis results.

Talbot, Tinling, Decker, and Chen [2] formulated a helicopter flying qualities model that includes fuselage dynamics and a three degree of freedom tip-pathplane representation for the main rotor flapping dynamics. Some simplifications are made in the analysis in order to formulate compact, analytical force

and moment expressions for the rotor forces and moments. Gibbons and Done [3] derived a numerical method to automatically generate rotorcraft equations of motion. The method uses Lagrange's equations and relies on expressing inertial position vectors of the rotor blades as a matrix multiplied by the position vector in blade coordinates plus a term that is a function of the modal coordinates, time, and spanwise position. The required differentiations of the position vector to form the equations of motion are performed numerically. Miller and White [1] used concepts from Lytwyn [4] and Gibbons and Done [3] to automate generation of the equations of motion for rotorcraft handling qualities analysis. Miller and White [1] expressed all transformation matrices in complex variable form and were able to develop a compact algorithm to analytically obtain long strings of orthogonal transformation matrices along with all necessary derivatives to form nonlinear and linearized dynamic equations. Lagrange's equations were used in the formulation. Zhao and Curtiss [5] derived a set of linearized equations by analytic linearization of a nonlinear model formulated using Lagrange's equations. The symbolic manipulation computer program MACSYMA was used in forming the equations. Subsequent work by McKillip and Curtiss [6] has improved and extended the work by Zhao and Curtiss [5].

The work discussed in this paper derives a rotorcraft flying qualities model which has been implemented into a FORTRAN computer program. A fairly generic rotorcraft configuration, consisting of a rigid fuselage, two rotors, and an arbitrary number of fuselage fixed external surfaces has been assumed, as shown in Figure 1. It is important to note that the type of analysis carried out in this work can accommodate any arbitrary number of rotors in the configuration. The number of rotors has been chosen to be two since the majority of rotorcraft fall under this category. The fuselage possesses six degrees of freedom and the rotor blades have flap, lag, and pitch degrees of freedom. The rotor aerodynamic models are based on blade element theory and include three degree of freedom dynamic inflow. The equations of motion are formulated using Kane's equations [7]. More importantly, derivatives of transformation matrices are formed using angular velocity expressions as opposed to numerical or direct differentiation. The rotor dynamic inflow equations are based on the Pitt and Peters model [8] and include hub motion perturbations. The residual of the equations of motion and the residual gradient expressions are derived analytically and trim is calculated using the residual and residual gradients in concert with a modified New

ton's method. The rotor trim variables are the rotor multiblade coordinates. A linear constant coefficient model of the composite airframe is formulated using a multiblade coordinate transformation with a subsequent constant coefficient approximation. The linear constant coefficient airframe model is coupled to the linear control system dynamic model to form the overall linear model. Linear analysis tools such as eigen values, eigen vectors, transfer functions, frequency response, and linear simulation are directly contained within the computer program.

# Airframe Dynamic Model

As pictured in Figure 1, the airframe dynamic model consists of a rigid fuselage with the standard six degrees of freedom and two fully articulated rotor systems, each with dynamic inflow. The fuselage aerodynamic force and moment components are obtained in the wind axis from a two dimensional data table as functions of fuselage angle of attack and sideslip. The aerodynamic forces exerted on the external surfaces are obtained using standard lifting line theory. The rotor geometry details are shown in Figure 2. Provisions are made in the model to accommodate any of the six possible sequences of flap, lag, and pitch hinges for the rotor blades. Each hinge is accompanied by a linear torsional spring and damper. Each blade also has a non linear translational damper which is attached to the rotor blade from the rotor hub. Hingeless rotor systems can be approximately modeled using a virtual hinge representation. The aerodynamic forces exerted on the rotor blades are calculated using blade element theory. The blades on a rotor have identical yet arbitrary geometric and inertial properties.

The airframe nonlinear dynamic model is obtained using the flat and non-rotating earth assumption. Kane's Equations are then written for each degree of freedom by taking into account the contributions of the generalized inertia forces, the generalized gravity forces, the generalized aerodynamic forces, and the generalized spring-damper forces.

$$
\begin{array}{l} f _ {r} (t) = f _ {I _ {r}} (t) + f _ {G _ {r}} (t) + f _ {A _ {r}} (t) + f _ {S D _ {r}} (t), \\ r = 1, \dots , n _ {R B} \tag {1} \\ \end{array}
$$

In equation 1, $t$ denotes time and $n_{RB}$ is the number of generalized speeds. The origin of each term on the right hand side of Equation 1 is discussed below.

The following nomenclature is introduced for deriving the generalized inertia forces. Let $n_{R1}$ and $n_{R2}$ denote the number of blades on rotor I and rotor

2, respectively. Let $m_{F}$ and $I_{F}$ , $m_{R1,i}$ and $I_{R1,i}$ ( $i = 1, \ldots, n_{R1}$ ), and $m_{R2,j}$ and $I_{R2,j}$ ( $j = 1, \ldots, n_{R2}$ ), respectively, denote the masses and inertia matrices for the fuselage, rotor 1 blades, and rotor 2 blades. Let $\omega_{F}$ , $\omega_{R1,i}$ ( $i = 1, \ldots, n_{R1}$ ), and $\omega_{R2,j}$ ( $j = 1, \ldots, n_{R2}$ ) represent the individual body axis components of the angular velocities of the fuselage, rotor 1 blades, and rotor 2 blades, respectively. Let $v_{F^{\bullet}}$ and $a_{F^{\bullet}}$ , $v_{R1,i^{\bullet}}$ and $a_{R1,i^{\bullet}}$ ( $i = 1, \ldots, n_{R1}$ ), and $v_{R2,j^{\bullet}}$ and $a_{R2,j^{\bullet}}$ ( $j = 1, \ldots, n_{R2}$ ) represent the inertial axis components of the c.g. (center of gravity) velocities and accelerations of the fuselage, rotor 1 blades, and rotor 2 blades, respectively. Then the generalized inertia forces acting on the configuration can be written as,

$$
f _ {I _ {r}} (t) = m _ {F} \left(\frac {\partial v _ {F ^ {*}}}{\partial u _ {r}}\right) ^ {T} a _ {F ^ {*}} +
$$

$$
\sum_ {i = 1} ^ {n _ {R 1}} m _ {R 1, i} \left(\frac {\partial v _ {R 1 , i ^ {*}}}{\partial u _ {r}}\right) ^ {T} a _ {R 1, i ^ {*}} +
$$

$$
\sum_ {i = 1} ^ {n _ {R 2}} m _ {R 2, i} \left(\frac {\partial v _ {R 2 , i ^ {*}}}{\partial u _ {r}}\right) ^ {T} a _ {R 2, i ^ {*}} +
$$

$$
\left(\frac {\partial \omega_ {F}}{\partial u _ {r}}\right) ^ {T} \left\{I _ {F} \dot {\omega} _ {F} + S (\omega_ {F}) I _ {F} \omega_ {F} \right\} +
$$

$$
\sum_ {i = 1} ^ {n _ {R 1}} \left(\frac {\partial \omega_ {R 1 , i}}{\partial u _ {r}}\right) ^ {T} \left\{I _ {R 1, i} \dot {\omega} _ {R 1, i} + S (\omega_ {R 1, i}) I _ {R 1, i} \omega_ {R 1, i} \right\} +
$$

$$
\sum_ {i = 1} ^ {n _ {R 2}} \left(\frac {\partial \omega_ {R 2 , i}}{\partial u _ {r}}\right) ^ {T} \left\{I _ {R 2, i} \dot {\omega} _ {R 2, i} + S \left(\omega_ {R 2, i}\right) I _ {R 2, i} \omega_ {R 2, i} \right\},
$$

$$
r = 1, \dots , n _ {R B} \tag {2}
$$

where an overdot denotes differentiation with respect to time and $S(\cdot)$ is the standard cross product skew-symmetric matrix operator (Appendix). $u$ is the vector of generalized speeds. Letting $g$ be the acceleration due to gravity, the generalized gravity forces can be written as,

$$
\begin{array}{l} f _ {G _ {r}} (t) = - m _ {F} g \frac {\partial \left(v _ {F ^ {*}}\right) _ {3}}{\partial u _ {r}} \\ - \sum_ {i = 1} ^ {n _ {R 1}} m _ {R 1, i} g \frac {\partial (v _ {R 1 , i ^ {*}}) _ {3}}{\partial u _ {r}} \\ - \sum_ {i = 1} ^ {n _ {R 2}} m _ {R 2, i} g \frac {\partial \left(v _ {R 2 , i ^ {*}}\right) _ {3}}{\partial u _ {r}}, \\ r = 1, \dots , n _ {R B} \tag {3} \\ \end{array}
$$

The generalized aerodynamic forces are discussed next. Let $\upsilon_{F}$ , and $F_{F}$ and $M_{F}$ be respectively the body axis components of the velocity and the

aerodynamic force and moment acting on the fuselage aerodynamic center. Let $b_{R1}, b_{R2}$ , and $b_{S_i}$ ( $i = 1, \ldots, n_S$ ) denote the number of elements or sections on any rotor 1 blade, any rotor 2 blade, and the $i$ th external surface. Let $v_{R1,i,j}$ and $F_{R1,i,j}$ ( $i = 1, \ldots, n_{R1}, j = 1, \ldots, b_{R1}$ ), and $v_{R2,k,l}$ and $F_{R2,k,l}$ ( $k = 1, \ldots, n_{R2}, l = 1, \ldots, b_{R2}$ ) be the individual body axis components of the section velocity and the aerodynamic force acting on rotor 1 blades and rotor 2 blades, respectively. Let $v_{S_i,j}$ and $F_{S_i,j}$ ( $i = 1, \ldots, n_S, j = 1, \ldots, b_{S_i}$ ) be the respective body axis components of the section velocity and the aerodynamic force acting on the external surfaces. The generalized aerodynamic forces acting on the configuration can then be written as,

$$
\begin{array}{l} {f _ {A _ {r}} (t)} = {- \left\{\left(\frac {\partial v _ {F}}{\partial u _ {r}}\right) ^ {T} F _ {F} + \left(\frac {\partial \omega_ {F}}{\partial u _ {r}}\right) ^ {T} M _ {F} \right\}} \\ - \sum_ {i = 1} ^ {n _ {R 1}} \sum_ {j = 1} ^ {b _ {R 1}} \left(\frac {\partial v _ {R 1 , i , j}}{\partial u _ {r}}\right) ^ {T} F _ {R 1, i, j} \\ - \sum_ {i = 1} ^ {n _ {R 2}} \sum_ {j = 1} ^ {b _ {R 2}} \left(\frac {\partial v _ {R 2 , i , j}}{\partial u _ {r}}\right) ^ {T} F _ {R 2, i, j} \\ - \sum_ {i = 1} ^ {n _ {S}} \sum_ {j = 1} ^ {b s _ {i}} \left(\frac {\partial v _ {S , j}}{\partial u _ {r}}\right) ^ {T} F _ {S, j}, \\ \end{array}
$$

$$
r = 1, \dots , n _ {R B} \tag {4}
$$

The generalized spring-damper forces are discussed next. Figure 2 shows the typical spring-damper attachment geometry for a typical blade. Let $v_{R1,i,j}^{D}$ and $F_{R1,i,j}^{D}$ ( $i = 1, \ldots, n_{R1}, j = 1, 2$ ), and $v_{R2,k,l}^{D}$ and $F_{R2,k,l}^{D}$ ( $k = 1, \ldots, n_{R2}, l = 1, 2$ ) be the individual rotor hub axis components of the velocities and the forces acting on the translational damper attachment points for rotor 1 blades and rotor 2 blades, respectively. Let $\omega_{R1,i,j}^{D}$ and $M_{R1,i,j}^{D}$ ( $i = 1, \ldots, n_{R1}, j = 1, \ldots, 4$ ), and $\omega_{R2,k,l}^{D}$ and $M_{R2,k,l}^{D}$ ( $k = 1, \ldots, n_{R2}, l = 1, \ldots, 4$ ) denote the individual body axis components of the angular velocities and the torsional spring-damper moments acting on the hub, link 1, link 2, and the blade for rotor 1 blades and rotor 2 blades, respectively. Then the generalized spring-damper forces can be expressed as,

$$
\begin{array}{l} f _ {S D _ {r}} (t) = - \sum_ {i = 1} ^ {n _ {R 1}} \sum_ {j = 1} ^ {2} \left(\frac {\partial v _ {R 1 , i , j} ^ {D}}{\partial u _ {r}}\right) ^ {T} F _ {R 1, i, j} ^ {D} \\ - \sum_ {i = 1} ^ {n _ {R 2}} \sum_ {j = 1} ^ {2} \left(\frac {\partial v _ {R 2 , i , j} ^ {D}}{\partial u _ {r}}\right) ^ {T} F _ {R 2, i, j} ^ {D} \\ \end{array}
$$

$$
\begin{array}{l} - \sum_ {i = 1} ^ {n _ {R 1}} \sum_ {j = 1} ^ {4} \left(\frac {\partial \omega_ {R 1 , i , j} ^ {D}}{\partial u _ {r}}\right) ^ {T} M _ {R 1, i, j} ^ {D} \\ - \sum_ {i = 1} ^ {n _ {R 2}} \sum_ {j = 1} ^ {4} \left(\frac {\partial \omega_ {R 2 , i , j} ^ {D}}{\partial u _ {r}}\right) ^ {T} M _ {R 2, i, j} ^ {D}, \\ r = 1, \dots , n _ {R B} \tag {5} \\ \end{array}
$$

The partial derivatives $\frac{\partial v}{\partial u_r}$ and $\frac{\partial w}{\partial u_r}$ in Equations 2 through 5 are known as partial velocities and partial angular velocities, respectively. The generalized coordinate vector $q$ and the generalized speed vector $u$ are defined as follows:

$$
\begin{array}{l} q = \left\{\left(q _ {F}\right) ^ {T}, \left(q _ {R 1, 1}\right) ^ {T}, \left(q _ {R 1, 2}\right) ^ {T}, \dots , \left(q _ {R 1, n _ {R 1}}\right) ^ {T}, \right. \\ \left. \left(q _ {R 2, 1}\right) ^ {T}, \left(q _ {R 2, 2}\right) ^ {T}, \dots , \left(q _ {R 2, n _ {R 2}}\right) ^ {T} \right\} ^ {T} \tag {6} \\ \end{array}
$$

$$
\begin{array}{l} u = \left\{\left(u _ {F}\right) ^ {T}, \left(u _ {R 1, 1}\right) ^ {T}, \left(u _ {R 1, 2}\right) ^ {T}, \dots , \left(u _ {R 1, n _ {R 1}}\right) ^ {T}, \right. \\ \left. \left(u _ {R 2, 1}\right) ^ {T}, \left(u _ {R 2, 2}\right) ^ {T}, \dots , \left(u _ {R 2, n _ {R 2}}\right) ^ {T} \right\} ^ {T} \tag {7} \\ \end{array}
$$

The subscripts $F$ , $R1$ , and $R2$ refer to fuselage, rotor 1, and rotor 2 variables, respectively. Further,

$$
q _ {F} = \left\{\boldsymbol {x}, y, z, \phi , \theta , \psi \right\} ^ {T} \tag {8}
$$

$$
q _ {R 1, i} = \left\{\alpha_ {R 1, i} ^ {(1)}, \alpha_ {R 1, i} ^ {(2)}, \alpha_ {R 1, i} ^ {(3)} \right\} ^ {T}, \quad i = 1, \dots , n _ {R 1} \tag {9}
$$

$$
\begin{array}{l} q _ {R 2, i} = \left\{\alpha_ {R 2, i} ^ {(1)}, \alpha_ {2 1, i} ^ {(2)}, \alpha_ {R 2, i} ^ {(3)} \right\} ^ {T}, \quad i = 1, \dots , n _ {R 2} (10) \\ u _ {F} = \left\{u, v, w, p, q, r \right\} ^ {T} (11) \\ \end{array}
$$

$$
\begin{array}{l} u _ {R 1, i} = \left\{\dot {\alpha} _ {R 1, i} ^ {(1)}, \dot {\alpha} _ {R 1, i} ^ {(2)}, \dot {\alpha} _ {R 1, i} ^ {(3)} \right\} ^ {T}, \quad i = 1, \dots , n _ {R 1} (12) \\ u _ {R 2, i} = \left\{\dot {\alpha} _ {R 2, i} ^ {(1)}, \dot {\alpha} _ {R 2, i} ^ {(2)}, \dot {\alpha} _ {R 2, i} ^ {(3)} \right\} ^ {T}, \quad i = 1, \dots , n _ {R 2} (13) \\ \end{array}
$$

The quantities $\alpha^{(1)},\alpha^{(2)}$ , and $\alpha^{(3)}$ are one of lag, flap, and pitch angles, depending on the rotor blade hinge sequence.

A brief description of the analysis involved in calculating the terms on the right hand sides of Equations 2 through 5 is given in the following. For simplicity, the analysis for the rotor terms will be restricted to rotor 1; the analysis for rotor 2 terms is analogous.

# Generalized Inertia Forces

The six terms comprising the generalized inertia forces, Equation 2, are discussed here. The orientation of the fuselage with respect to inertial axes and the orientation of the rotors with respect to the fuselage can be described using transformation matrices. Each transformation matrix is composed of one, two, or three single axis transformation matrices. Referring to Figure 2, let $T_{F}$ be the matrix of transformations from the fuselage axes to inertial axes. The following five matrices are defined for rotor 1. $T_{S1}$ is the matrix of transformations from shaft axes to

fuselage axes, $T_{H1,i}$ ( $i = 1, \ldots, n_{R1}$ ) is the matrix of transformations from rotating hub axes to shaft axes, $T_{R1,i}^{(1)}$ ( $i = 1, \ldots, n_{R1}$ ) is the matrix of transformations from link 1 axes to rotating hub axes, $T_{R1,i}^{(2)}$ ( $i = 1, \ldots, n_{R1}$ ) is the matrix of transformations from link 2 axes to link 1 axes, and $T_{R1,i}^{(3)}$ ( $i = 1, \ldots, n_{R1}$ ) is the matrix of transformations from blade axes to link 2 axes. The transformation matrices are expressed as follows:

$$
T _ {F} = \left[ E _ {1} (\phi) E _ {2} (\theta) E _ {3} (\psi) \right] ^ {T} \tag {14}
$$

$$
T _ {S 1} = \left[ T _ {S 1, b} \left(\Gamma_ {S 1, b}\right) T _ {S 1, a} \left(\Gamma_ {S 1, a}\right) \right] ^ {T} \tag {15}
$$

$$
T _ {H 1, i} = \left[ E _ {3} \left(\pi - \psi_ {R 1, i}\right) \right] ^ {T} \tag {16}
$$

$$
T _ {R 1, i} ^ {(1)} = T _ {R 1, i} ^ {(1)} \left(\alpha_ {R 1, i} ^ {(1)}\right) \tag {17}
$$

$$
T _ {R 1, i} ^ {(2)} = T _ {R 1, i} ^ {(2)} \left(\alpha_ {R 1, i} ^ {(2)}\right) \tag {18}
$$

$$
T _ {R 1, i} ^ {(3)} = T _ {R 1, i} ^ {(3)} \left(\alpha_ {R 1, i} ^ {(3)}\right) \tag {19}
$$

In Equation 16, $\psi_{R1,i} = \Omega_{R1}t + \frac{2\pi}{n_{R1}} (i - 1)$ , where $\Omega_{R1}$ is the rotor 1 hub rotational speed. It is assumed that the shaft is inclined with respect to the fuselage by first a rotation with the angle $\Gamma_{S1,a}$ and then a rotation with the angle $\Gamma_{S1,b}$ . Depending on the sequence of rotation, $T_{S1,a}$ and $T_{S1,b}$ are one each among $E_1$ and $E_2$ . $E_1$ , $E_2$ , and $E_3$ are single axis transformation matrices about $x$ , $y$ , and $z$ axes, respectively (Appendix). Clearly, $T^{(1)}$ , $T^{(2)}$ , and $T^{(3)}$ are one each among $E_1$ , $E_2$ , and $E_3$ , depending on the rotor blade hinge sequence.

The body axis components of the angular velocity of the fuselage, $\omega_{F}$ , can be written as,

$$
\omega_ {F} = \{p, q, r \} ^ {T} \tag {20}
$$

Using the transformation matrices defined above, the body axis components of the angular velocity of the ith rotor 1 blade can be written as,

$$
\begin{array}{l} \omega_ {R 1, i} = \left[ T _ {S 1} T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} \omega_ {F} + \\ \left[ T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} \{0, 0, - \Omega_ {R 1} \} ^ {T} + \\ \left[ T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} b _ {R 1} ^ {(1)} \dot {\alpha} _ {R 1, i} ^ {(1)} + \\ \left[ T _ {R 1, i} ^ {(3)} \right] ^ {T} b _ {R 1} ^ {(2)} \dot {\alpha} _ {R 1, i} ^ {(2)} + \\ b _ {R 1} ^ {(3)} \dot {\alpha} _ {R 1, i} ^ {(3)} \tag {21} \\ \end{array}
$$

The unit vectors $b_{R1}^{(1)}, b_{R1}^{(2)}$ , and $b_{R1}^{(3)}$ have been introduced to allow a general rotor blade hinge sequence. For example, if rotor 1 blades undergo a lag, flap, and pitch rotation sequence, then $b_{R1}^{(1)} = \{0,0,1\}^T$ , $b_{R1}^{(2)} = \{0,1,0\}^T$ , and $b_{R1}^{(3)} = \{1,0,0\}^T$ . Equation 21

has been obtained using the concept of simple angular velocities [7].

The body axis components of the fuselage c.g. velocity are given as,

$$
v _ {B} = \{u, v, w \} ^ {T} \tag {22}
$$

The inertial axis components of the fuselage and blade c.g. velocities can be written as,

$$
\begin{array}{l} v _ {F} \cdot = T _ {F} v _ {B} (23) \\ v _ {R 1, i ^ {\bullet}} = v _ {F ^ {\bullet}} + \\ T _ {F} S \left(\omega_ {F}\right) \bar {r} _ {F 1} + \\ T _ {F} T _ {S 1} S (\omega_ {S 1}) \bar {r} _ {H 1} + \\ T _ {F} T _ {S 1} T _ {H 1, i} S \left(\omega_ {H 1, i}\right) \bar {r} _ {R 1} ^ {(1)} + \\ T _ {F} T _ {S 1} T _ {H 1, i} T _ {R 1, i} ^ {(1)} S \left(\omega_ {R 1, i} ^ {(1)}\right) \bar {r} _ {R 1} ^ {(2)} + \\ T _ {F} T _ {S 1} T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} S \left(\omega_ {R 1, i} ^ {(2)}\right) \bar {r} _ {R 1} ^ {(3)} + \\ T _ {F} T _ {S 1} T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} S \left(\omega_ {R 1, i}\right) \bar {r} _ {R 1} ^ {*} (24) \\ \end{array}
$$

In Equation 24, $\omega_{S1}$ represents the body axis components of the angular velocity of rotor 1 shaft. $\omega_{H1,i}$ , $\omega_{R1,i}^{(1)}$ , and $\omega_{R1,i}^{(2)}$ are the individual body axis components of the angular velocities of the rotating hub, link 1, and link 2, respectively. The expressions for these angular velocities are given as follows:

$$
\omega_ {S 1} = \left[ T _ {S 1} \right] ^ {T} \omega_ {F} \tag {25}
$$

$$
\omega_ {H 1, i} = \left[ T _ {H 1, i} \right] ^ {T} \omega_ {S 1} + \left\{0, 0, - \Omega_ {R 1} \right\} ^ {T} \tag {26}
$$

$$
\omega_ {R 1, i} ^ {(1)} = \left[ T _ {R 1, i} ^ {(1)} \right] ^ {T} \omega_ {H 1, i} + b _ {R 1} ^ {(1)} \dot {\alpha} _ {R 1, i} ^ {(1)} \tag {27}
$$

$$
\omega_ {R 1, i} ^ {(2)} = \left[ T _ {R 1, i} ^ {(2)} \right] ^ {T} \omega_ {R 1, i} ^ {(1)} + b _ {R 1} ^ {(2)} \dot {\alpha} _ {R 1, i} ^ {(2)} \tag {28}
$$

In Equation 24, the vectors $\bar{r}_{F1},\bar{r}_{H1},\bar{r}_{R1}^{(1)},\bar{r}_{R1}^{(2)},\bar{r}_{R1}^{(3)}$ and $\bar{r}_{R1}^{*}$ are defined as follows. $\bar{r}_{F1}$ is the position vector from fuselage c.g. to a point on shaft 1, expressed in fuselage axes. $\bar{r}_{H1}$ is the position vector from the point on shaft 1 to the center of hub 1, expressed in shaft 1 axes. For any rotor 1 blade, $\bar{r}_{R1}^{(1)}$ is the position vector from the center of hub 1 to the first hinge, expressed in rotating hub 1 axes; $\bar{r}_{R1}^{(2)}$ is the position vector from the first hinge to the second hinge, expressed in link 1 axes; $\bar{r}_{R1}^{(3)}$ is the position vector from the second hinge to the third hinge, expressed in link 2 axes; and $\bar{r}_{R1}^{*}$ is the position vector from the third hinge to the blade c.g., expressed in blade axes. Equations 20 through 24 are used to compute the partial velocities and partial angular velocities needed in Equation 2.

The angular acceleration vectors $\dot{\omega}_{F}$ and $\dot{\omega}_{R1,i}$ appearing in Equation 2 are obtained by a time-differentiation of the right hand sides of Equations 20 and 21, respectively. Similarly, the translational acceleration vectors $a_{F}$ and $a_{R1,i}$ appearing in Equation 2 are obtained by a time-differentiation of the right hand sides of Equations 23 and 24, respectively. While the equations for the rotor blade acceleration vectors are lengthy and omitted here, it is noticed from an inspection of Equations 20 through 24 that obtaining these equations is straight forward once the expressions for the time-derivatives of the transformation matrices has been obtained. The Appendix gives the derivation of a formula for calculating the time-derivative of a matrix in terms of a matrix product. Using this formula, the following are obtained:

$$
\dot {T} _ {F} = T _ {F} S \left(\omega_ {F}\right) \tag {29}
$$

$$
\dot {T} _ {S 1} = 0 \tag {30}
$$

$$
\dot {T} _ {H 1, i} = T _ {H 1, i} S \left(\left\{0, 0, - \Omega_ {R 1} \right\} ^ {T}\right) \tag {31}
$$

$$
\dot {T} _ {R 1, i} ^ {(1)} = T _ {R 1, i} ^ {(1)} S \left(b _ {R 1} ^ {(1)} \dot {\alpha} _ {R 1, i} ^ {(1)}\right) \tag {32}
$$

$$
\dot {T} _ {R 1, i} ^ {(2)} = T _ {R 1, i} ^ {(2)} S \left(b _ {R 1} ^ {(2)} \dot {\alpha} _ {R 1, i} ^ {(2)}\right) \tag {33}
$$

$$
\dot {T} _ {R 1, i} ^ {(3)} = T _ {R 1, i} ^ {(3)} S \left(b _ {R 1} ^ {(3)} \dot {\alpha} _ {R 1, i} ^ {(3)}\right) \tag {34}
$$

Generalized Gravity Forces

The partial velocities $\frac{\partial v_{F^*}}{\partial u_r}, \frac{\partial v_{R1,i^*}}{\partial u_r}$ , and $\frac{\partial v_{R2,i^*}}{\partial u_r}$ obtained in the computation of generalized inertia forces are used to compute the generalized gravity forces given by Equation 3.

Generalized Aerodynamic Forces Due to Fuselage

The first term in Equation 4 represents the generalized aerodynamic forces due to the fuselage. The quantities comprising this term are obtained as follows. The body axis components of the velocity of the fuselage aerodynamic center (a.c.) can be written as,

$$
v _ {F} = v _ {B} + S \left(\omega_ {F}\right) \bar {r} _ {A C} \tag {35}
$$

where $\bar{r}_{AC}$ is the position vector from the fuselage c.g. to the fuselage a.c., expressed in body axes. Equation 35 is used to compute the partial velocity $\frac{\partial v_{F}}{\partial u_{r}}$ .

For a rotorcraft, the wind-axis components of the aerodynamic force and moment acting at the fuselage a.c. are usually given as a function of fuselage angles of attack and sideslip:

$$
L = L _ {1} (\alpha) + L _ {2} (\beta) \tag {36}
$$

$$
D = D _ {1} (\alpha) + D _ {2} (\beta) \tag {37}
$$

$$
M = M _ {1} (\alpha) + M _ {2} (\beta) \tag {38}
$$

$$
Y = Y _ {1} (\alpha) + Y _ {2} (\beta) \tag {39}
$$

$$
l = l _ {1} (\alpha) + l _ {2} (\beta) \tag {40}
$$

$$
N = N _ {1} (\alpha) + N _ {2} (\beta) \tag {41}
$$

These forces and moments are scaled with respect to the local dynamic pressure and can be in the form of a two dimensional data table or fitted analytical expressions to wind-tunnel data. The force and moment components in the body axes are given as,

$$
F _ {F} = \bar {q} E _ {2} (\alpha) E _ {3} (- \beta) \{- D, Y, - L \} ^ {T} \tag {42}
$$

$$
M _ {F} = \bar {q} E _ {2} (\alpha) E _ {3} (- \beta) \{l, M, N \} ^ {T} \tag {43}
$$

The fuselage velocities, for purposes of calculating the aerodynamic variables $\alpha$ , $\beta$ , and $\bar{q}$ , include the effect of rotor 1 downwash:

$$
\bar {v} = v _ {F} - w _ {R 1, 0} f _ {R 1} \left(\chi_ {R 1}\right) \tag {44}
$$

where $w_{R1,0}$ is the rotor 1 collective inflow, and $\chi_{R1}$ is the rotor 1 wake skew angle. In absence of more sophisticated data, $f_{R1}$ assumes the value $\{0,0,1\}^T$ or $\{0,0,0\}^T$ , depending on whether the a.c. is within or outside of rotor 1 wake. $\chi_{R1}$ is given as,

$$
\chi_ {R 1} = \tan^ {- 1} \left(\frac {\mu_ {R 1}}{- \lambda_ {R 1}}\right) \tag {45}
$$

where $\mu_{R1}$ and $\lambda_{R1}$ are, respectively, the rotor 1 advance ratio and rotor 1 inflow ratio. These quantities can be determined by computing the relative air velocity components at the rotor hub. Using Equation 44, the aerodynamic variables $\alpha$ , $\beta$ , and $\bar{q}$ can be readily computed:

$$
\alpha = \tan^ {- 1} \left(\frac {\bar {v} _ {3}}{\bar {v} _ {1}}\right), \quad \beta = \sin^ {- 1} \left(\frac {\bar {v} _ {2}}{| \bar {v} |}\right) \tag {46}
$$

$$
\bar {q} = \frac {1}{2} \rho | \bar {v} | ^ {2} \tag {47}
$$

# Generalized Aerodynamic Forces Due to Rotors

The second term in Equation 4 represents the generalized aerodynamic forces due to rotor 1. Blade element analysis is used to calculate this term. As mentioned earlier, the rotor blades are allowed to have any arbitrary variation of twist, chord length, and airfoil characteristics along the span. The body axis components of the blade element velocity are given as,

$$
\begin{array}{l} v _ {R 1, i, j} = \left[ T _ {F} T _ {S 1} T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} v _ {F ^ {*}} + \\ \left[ T _ {S 1} T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} S (\omega_ {F}) \bar {r} _ {F 1} + \\ \end{array}
$$

$$
\begin{array}{l} \left[ T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} S (\omega_ {S 1}) \bar {r} _ {H 1} + \\ \left[ T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} S (\omega_ {H 1, i}) \bar {r} _ {R 1} ^ {(1)} + \\ \left[ T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} S \left(\omega_ {R 1, i} ^ {(1)}\right) \bar {r} _ {R 1} ^ {(2)} + \\ \left[ T _ {R 1, i} ^ {(3)} \right] ^ {T} S \left(\omega_ {R 1, i} ^ {(2)}\right) \bar {r} _ {R 1} ^ {(3)} + \\ S \left(\omega_ {R 1, i}\right) \bar {r} _ {R 1, j} \tag {48} \\ \end{array}
$$

The only new quantity introduced in the preceding Equation is $\bar{r}_{R1,j}$ ( $j = 1, \ldots, b_{R1}$ ), which is the position vector from the root of the blade to the $j$ th aerodynamic element, expressed in blade body axes. Equation 48 is used to obtain the partial velocity $\frac{\partial v_{R1,j}}{\partial u}$ .

Figure 3 shows a typical $j$ th element on the $i$ th blade, and the lift and drag forces acting on it. $(y_{R1,i},z_{R1,i})$ are the body axes of the blade. $\theta_{R1,j}$ is the blade twist angle at the $j$ th section. $u_{R1,i,j}^{p}$ and $u_{R1,i,j}^{p}$ are the components of the relative air velocity parallel and perpendicular to the zero lift line. The variables $\alpha_{R1,i,j},L_{R1,i,j}$ ,and $D_{R1,i,j}$ have obvious meanings. The velocity of the $(i,j)$ th element with respect to air is given by the following equation,

$$
\bar {v} _ {R 1, i, j} = v _ {R 1, i, j} + \left[ T _ {H 1, i} T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \right] ^ {T} v _ {R 1, i, j} ^ {A} \tag {49}
$$

The term $v_{R1,i,j}^{A}$ arises due to rotor inflow and can be approximately evaluated as,

$$
\begin{array}{l} \left(v _ {R 1, i, j} ^ {A}\right) _ {1} = 0 \\ (v _ {R 1, i, j} ^ {A}) _ {2} = 0 \\ (v _ {R 1, i, j} ^ {A}) _ {3} = - w _ {R 1, 0} - \left[ h _ {R 1} + \left(\bar {r} _ {R 1, j}\right) _ {1} / R _ {R 1} \right]. \\ \left(w _ {R 1, 1 s} \sin \psi_ {R 1, i} + w _ {R 1, 1 c} \cos \psi_ {R 1, i}\right) \tag {50} \\ \end{array}
$$

where

$$
h _ {R 1} = \frac {\left(\bar {r} _ {R 1} ^ {(1)}\right) _ {1} + \left(\bar {r} _ {R 1} ^ {(2)}\right) _ {1} + \left(\bar {r} _ {R 1} ^ {(3)}\right) _ {1}}{R _ {R 1}} \tag {51}
$$

$w_{R1,1s}$ and $w_{R1,1c}$ are the sin and cos components of the rotor inflow and $R_{R1}$ is the rotor radius. The radial, tangential, and perpendicular components of the air velocity at the airfoil can be computed as,

$$
\left\{u _ {R 1, i, j} ^ {r}, - u _ {R 1, i, j} ^ {s}, u _ {R 1, i, j} ^ {p} \right\} ^ {T} = E _ {1} \left(\theta_ {R 1, j}\right) \bar {v} _ {R 1, i, j} \tag {52}
$$

Using the air velocity components, the section angle of attack and Mach Number can be calculated as follows:

$$
\alpha_ {R 1, i, j} = \tan^ {- 1} \left(\frac {u _ {R 1 , i , j} ^ {p}}{u _ {R 1 , i , j} ^ {s}}\right) \tag {53}
$$

$$
\mathcal {M} _ {R 1, i, j} = \frac {\sqrt {\left(u _ {R 1 , i , j} ^ {s}\right) ^ {2} + \left(u _ {R 1 , i , j} ^ {p}\right) ^ {2}}}{c} \tag {54}
$$

where $c$ is the speed of sound at the altitude where the aircraft is operating. Airfoil lift and drag coefficients are usually specified as a function of the angle of attack and Mach Number. Thus,

$$
c _ {R 1, i, j} ^ {l} = c _ {R 1, i, j} ^ {l} \left(\alpha_ {R 1, i, j}, \mathcal {M} _ {R 1, i, j}\right) \tag {55}
$$

$$
c _ {R 1, i, j} ^ {d} = c _ {R 1, i, j} ^ {d} \left(\alpha_ {R 1, i, j}, \mathcal {M} _ {R 1, i, j}\right) \tag {56}
$$

The above data can be either in the form of a two dimensional data table or in the form of fitted analytical expressions to experimental data. However, in the absence of any data, simple analytical lift and drag models can be used. Based on reference [9], equations were generated for two simple models, one that ignored stall and compressibility effects and another that included the same. The section lift and drag forces are computed next:

$$
L _ {R 1, i, j} = \bar {q} _ {R 1, i, j} c _ {R 1, i, j} ^ {l} c _ {R 1, j} (\Delta \bar {r} _ {R 1, j}) _ {1} \eta_ {R 1, j} \tag {57}
$$

$$
D _ {R 1, i, j} = \bar {q} _ {R 1, i, j} c _ {R 1, i, j} ^ {d} c _ {R 1, j} (\Delta \bar {r} _ {R 1, j}) _ {1} \tag {58}
$$

where

$$
\bar {q} _ {R 1, i, j} = \frac {1}{2} \rho \left[ \left(u _ {R 1, i, j} ^ {s}\right) ^ {2} + \left(u _ {R 1, i, j} ^ {p}\right) ^ {2} \right] \tag {59}
$$

and $c_{R1,j}$ and $\eta_{R1,j}$ are, respectively, the chord length and lift efficiency factors at the $j$ th section. The body axis components of the section aerodynamic force are given by:

$$
F _ {R 1, i, j} = E _ {1} \left(\alpha_ {R 1, i, j} - \theta_ {R 1, j}\right) \left\{0, D _ {R 1, i, j}, - L _ {R 1, i, j} \right\} ^ {T} \tag {60}
$$

# Generalized Aerodynamic Forces Due to Surfaces

The generalized aerodynamic forces due to the external surfaces are derived in much the same way as those due to the rotors. One difference, however, is that the radial drag force due to radial flow is considered here. It is assumed that every surface has a fixed (invariant with time) orientation with respect to the fuselage. The orientation can be specified uniquely in terms of rotation angles about three mutually perpendicular axes. In order to have consistency in describing surfaces with different orientations, the body axes for any surface are defined as follows. The $x$ axis coincides with the zero lift line of the root section and is directed from the trailing edge of the surface to the leading edge of the surface (see Figure 4). The $y$ axis is perpendicular to the $x$ axis, passes through the aerodynamic center of the root section and is directed outboard. $z$ axis completes the right handed set.

The objective is to evaluate the last term in Equation 4. For illustration purposes, the mathematical

analysis involved is outlined for surface 1. Let the surface be oriented with respect to the fuselage by three successive rotations of angles $\gamma_{S_1}$ , $\delta_{S_1}$ and $\epsilon_{S_1}$ about mutually perpendicular axes. The sequence of rotations can be any of the possible six sequences. Let the matrices associated with the above transformations be $T_{S_1}^{(1)}$ , $T_{S_1}^{(2)}$ , and $T_{S_1}^{(3)}$ , respectively. The matrix $T_{ES_1} = T_{S_1}^{(3)}(\epsilon_{S_1})T_{S_1}^{(2)}(\delta_{S_1})T_{S_1}^{(1)}(\gamma_{S_1})$ transforms components of a vector from fuselage axes to surface 1 axes. Let $\bar{r}_{S_1}$ be the position vector from the fuselage c.g. to the surface 1 reference point, expressed in fuselage axes. Let $\bar{r}_{S_1,j}$ be the position vector from the surface reference point to the aerodynamic center of the jth section, expressed in surface axes. Then the velocity of the jth section can be expressed as,

$$
v _ {S _ {1}, j} = T _ {E S _ {1}} \left[ v _ {B} + S \left(\omega_ {F}\right) \bar {r} _ {S _ {1}} + S \left(\omega_ {F}\right) \left[ T _ {E S _ {1}} \right] ^ {T} \bar {r} _ {S _ {1}, j} \right] \tag {61}
$$

This expression is used to obtain the partial velocity $\frac{\partial v_{S_1,j}}{\partial u_r}$ , which is needed for evaluating the generalized aerodynamic force contribution from surface 1.

For purposes of computing the aerodynamic force, the resultant section velocity with respect to air includes the effect of rotor 1 downwash:

$$
\bar {v} _ {S _ {1}, j} = v _ {S _ {1}, j} - T _ {E S _ {1}} w _ {R 1, 0} f _ {S _ {1}} \left(\chi_ {R 1}\right) \tag {62}
$$

Similar to the case of the fuselage, in a simple analysis, $f_{S_1}$ can be taken to be equal to $\{0, 0, 1\}^T$ or $\{0, 0, 0\}^T$ , depending on whether the surface is within or outside of rotor 1 wake.

The effect of radial flow on a surface section is included in the same way as described in reference [10], where profile power is computed due to radial flow at blade sections. Let the free stream velocity at the $j$ th section be yawed, as shown in Figure 5. An estimate of the normal and radial drag forces is desired, preferably in terms of the two dimensional sectional aerodynamic coefficients. It is assumed that the total viscous drag on the yawed section acts in the same direction as the free stream velocity. It is also assumed that the yawed section drag coefficient is given by the two dimensional unyawed airfoil characteristics. The normal section lift coefficient is assumed not to be influenced by yawed flow. The angle of attack and Mach Number for the unyawed and yawed sections are,

$$
\alpha_ {S _ {1}, j} = \tan^ {- 1} \left(\frac {\left(\bar {v} _ {S _ {1} , j}\right) _ {3}}{\left(\bar {v} _ {S _ {1} , j}\right) _ {1}}\right) \tag {63}
$$

$$
\mathcal {M} _ {S _ {1}, j} = \frac {\sqrt {(\bar {v} _ {S _ {1} , j}) _ {1} ^ {2} + (\bar {v} _ {S _ {1} , j}) _ {3} ^ {2}}}{c} \tag {64}
$$

$$
\hat {\alpha} _ {S _ {1}, j} = \tan^ {- 1} \left(\frac {(\bar {v} _ {S _ {1} , j}) _ {3}}{\sqrt {(\bar {v} _ {S _ {1} , j}) _ {1} ^ {2} + (\bar {v} _ {S _ {1} , j}) _ {2} ^ {2}}}\right) \tag {65}
$$

$$
\hat {\mathcal {M}} _ {S _ {1}, j} = \frac {\sqrt {(\bar {v} _ {S _ {1} , j}) _ {1} ^ {2} + (\bar {v} _ {S _ {1} , j}) _ {2} ^ {2} + (\bar {v} _ {S _ {1} , j}) _ {3} ^ {2}}}{c} \tag {66}
$$

The section lift and drag coefficients are given by:

$$
c _ {S _ {1}, j} ^ {I} = c _ {S _ {1}, j} ^ {I} \left(\alpha_ {S _ {1}, j}, \mathcal {M} _ {S _ {1}, j}\right) \tag {67}
$$

$$
c _ {S _ {1}, j} ^ {d} = c _ {S _ {1}, j} ^ {d} \left(\hat {\alpha} _ {S _ {1}, j}, \hat {\mathcal {M}} _ {S _ {1}, j}\right) \tag {68}
$$

As mentioned for the case of rotor aerodynamics, in the absence of lift and drag coefficient data, simple analytical models for the coefficients can be used. The section lift and drag forces are given as,

$$
L _ {S _ {1}, j} = \bar {q} _ {S _ {1}, j} c _ {S _ {1}, j} ^ {l} c _ {S _ {1}, j} (\Delta \bar {r} _ {S _ {1}, j}) _ {2} \eta_ {S _ {1}, j} \tag {69}
$$

$$
D _ {S _ {1}, j} = \hat {q} _ {S _ {1}, j} c _ {S _ {1}, j} ^ {d} c _ {S _ {1}, j} (\Delta \bar {r} _ {S _ {1}, j}) _ {2} \tag {70}
$$

where

$$
\bar {q} _ {S _ {1}, j} = \frac {1}{2} \rho [ (\bar {v} _ {S _ {1}, j}) _ {1} ^ {2} + (\bar {v} _ {S _ {1}, j}) _ {3} ^ {2} ] \tag {71}
$$

$$
\hat {q} _ {S _ {1}, j} = \frac {1}{2} \rho \left[ \left(\bar {v} _ {S _ {1}, j}\right) _ {1} ^ {2} + \left(\bar {v} _ {S _ {1}, j}\right) _ {2} ^ {2} + \left(\bar {v} _ {S _ {1}, j}\right) _ {3} ^ {2} \right] (7 2)
$$

and $\eta_{S_1,j}$ is the section lift efficiency factor. Finally, the body axis components of the section aerodynamic force are given as,

$$
R _ {S _ {1}, j} = \left(L _ {S _ {1}, j} / \sqrt {(\bar {v} _ {S _ {1} , j}) _ {1} ^ {2} + (\bar {v} _ {S _ {1} , j}) _ {3} ^ {2}}\right).
$$

$$
\left\{\left(\bar {v} _ {S _ {1}, j}\right) _ {3}, 0, - \left(\bar {v} _ {S _ {1}, j}\right) _ {1} \right\} ^ {T} +
$$

$$
\left(D _ {S _ {1}, j} / \sqrt {\left(\bar {v} _ {S _ {1} , j}\right) _ {1} ^ {2} + \left(\bar {v} _ {S _ {1} , j}\right) _ {2} ^ {2} + \left(\bar {v} _ {S _ {1} , j}\right) _ {3} ^ {2}}\right).
$$

$$
\left\{- \left(\bar {v} _ {S _ {1}, j}\right) _ {1}, - \left(\bar {v} _ {S _ {1}, j}\right) _ {2}, - \left(\bar {v} _ {S _ {1}, j}\right) _ {3} \right\} ^ {T} \tag {73}
$$

# Generalized Damping Forces Due to Translational Dampers

As shown in Figure 2, one end of the blade translational damper is attached to the rotating hub while the other end is attached to the blade itself. The damper force is assumed to be given as a function of the relative speed between it's two ends. The analysis associated with the first term in Equation 5, which is due to rotor 1, is developed in the following. The position vector from attachment point 1 to attachment point 2, expressed in the rotating hub axes, is given as,

$$
\begin{array}{l} d _ {R 1, i} = \left(\bar {r} _ {R 1} ^ {(1)} - \bar {s} _ {R 1}\right) + \\ T _ {R 1, i} ^ {(1)} \bar {r} _ {R 1} ^ {(2)} + \\ T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} \bar {r} _ {R 1} ^ {(3)} + \\ T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} \bar {t} _ {R 1} \tag {74} \\ \end{array}
$$

$\bar{s}_{R1}$ is the position vector from the center of the hub to attachment point 1, expressed in hub axes. $\bar{t}_{R1}$

is the position vector from the blade root to attachment point 2, expressed in blade axes. The preceding equation is used to determine the velocity of attachment point 2 relative to that of attachment point 1, expressed in hub axes:

$$
\begin{array}{l} \tilde {v} _ {R 1, i} = S \left(\omega_ {H 1, i}\right) \left(\bar {r} _ {R 1} ^ {(1)} - \bar {s} _ {R 1}\right) + \\ T _ {R 1, i} ^ {(1)} S \left(\omega_ {R 1, i} ^ {(1)}\right) \bar {r} _ {R 1} ^ {(2)} + \\ T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} S \left(\omega_ {R 1, i} ^ {(2)}\right) \bar {r} _ {R 1} ^ {(3)} + \\ T _ {R 1, i} ^ {(1)} T _ {R 1, i} ^ {(2)} T _ {R 1, i} ^ {(3)} S \left(\omega_ {R 1, i}\right) \bar {t} _ {R 1} \tag {75} \\ \end{array}
$$

The component of this relative velocity along the damper arm can be written as,

$$
\tilde {v} _ {R 1, i} = (1 / | d _ {R 1, i} |) \left(d _ {R 1, i}\right) ^ {T} \tilde {v} _ {R 1, i} \tag {76}
$$

The damper force $F_{R1,i}$ is assumed to be specified as a function of the above speed. Hence,

$$
F _ {R 1, i} = F _ {R 1, i} \left(\hat {v} _ {R 1, i}\right) \tag {77}
$$

The hub axis components of the forces acting at the attachment points are given as,

$$
F _ {R 1, i, 1} ^ {D} = - \left(F _ {R 1, i} / | d _ {R 1, i} |\right) d _ {R 1, i} \tag {78}
$$

$$
F _ {R 1, i, 2} ^ {D} = \left(F _ {R 1, i} / | d _ {R 1, i} |\right) d _ {R 1, i} \tag {79}
$$

The velocities at the attachment points, expressed in the hub axes, are:

$$
v _ {R 1, i, 1} ^ {D} = \left[ T _ {S 1} T _ {H 1, i} \right] ^ {T} \left(v _ {B} + S \left(\omega_ {F}\right) \bar {r} _ {F 1}\right) +
$$

$$
\left[ T _ {H 1, i} \right] ^ {T} S \left(\omega_ {S 1}\right) \bar {r} _ {H 1} +
$$

$$
S \left(\omega_ {H 1, i}\right) \bar {s} _ {R 1} \tag {80}
$$

$$
v _ {R 1, i, 2} ^ {D} = v _ {R 1, i, 1} ^ {D} + \tilde {v} _ {R 1, i} \tag {81}
$$

The above two equations are used to calculate the required partial velocities, $\frac{\partial v_{R1,i,1}^D}{\partial u_r}$ and $\frac{\partial v_{R1,i,2}^D}{\partial u_r}$ .

# Generalized Spring-Damper Forces Due to Torsional Spring-Dampers

The torsional springs and dampers mounted on the blade hinges are assumed to possess linear stiffness and damping properties. They give rise to the third and fourth terms in Equation 5. The third term in this equation is due to rotor 1 and is discussed below. Referring to Figure 2, the following quantities are defined for the ith blade. $M_{R1,i,1}$ denotes the body axis components of the moment on acting link 1 due to the spring-damper at hinge 1. $M_{R1,i,2}$ denotes the body axis components of the moment on acting link 2 due to the spring-damper at hinge 2. $M_{R1,i,3}$ denotes the body axis components of the moment on acting on

the blade due to the spring-damper at hinge 3. These moments can be expressed as,

$$
M _ {R 1, i, 1} = - b _ {R 1} ^ {(1)} \left(k _ {P _ {R 1}} ^ {(1)} \alpha_ {R 1, i} ^ {(1)} + k _ {D _ {R 1}} ^ {(1)} \dot {\alpha} _ {R 1, i} ^ {(1)}\right) (8 2)
$$

$$
M _ {R 1, i, 2} = - b _ {R 1} ^ {(2)} \left(k _ {P _ {R 1}} ^ {(2)} \alpha_ {R 1, i} ^ {(2)} + k _ {D _ {R 1}} ^ {(2)} \dot {\alpha} _ {R 1, i} ^ {(2)}\right) (8 3)
$$

$$
M _ {R 1, i, 3} = - b _ {R 1} ^ {(3)} \left(k _ {P _ {R 1}} ^ {(3)} \alpha_ {R 1, i} ^ {(3)} + k _ {D _ {R 1}} ^ {(3)} \dot {\alpha} _ {R 1, i} ^ {(3)}\right) (8 4)
$$

where $k_{P}$ and $k_{D}$ denote stizziness and damping constants. The torsional spring-damper moments acting on the hub, link 1, link 2, and the blade, expressed in their individual body axes, are respectively given as,

$$
M _ {R 1, i, 1} ^ {D} = - M _ {R 1, i, 1} \tag {85}
$$

$$
M _ {R 1, i, 2} ^ {D} = M _ {R 1, i, 1} - M _ {R 1, i, 2} \tag {86}
$$

$$
M _ {R 1, i, 3} ^ {D} = M _ {R 1, i, 2} - M _ {R 1, i, 3} \tag {87}
$$

$$
M _ {R 1, i, 4} ^ {D} = M _ {R 1, i, 3} \tag {88}
$$

The individual body axis components of the angular velocities of the hub, link 1, link 2, and the blade, are respectively given as,

$$
\omega_ {R 1, i, 1} ^ {D} = \omega_ {H 1, i} \tag {89}
$$

$$
\omega_ {R 1, i, 2} ^ {D} = \omega_ {R 1, i} ^ {(1)} \tag {90}
$$

$$
\omega_ {R 1, i, 3} ^ {D} = \omega_ {R 1, i} ^ {(2)} \tag {91}
$$

$$
\omega_ {R 1, i, 4} ^ {D} = \omega_ {R 1, i} \tag {92}
$$

The preceding four equations are used to compute the four partial velocities needed for evaluating the third term in Equation 5.

# Airframe Kinematics

To complete the description of the airframe dynamic model, the kinematic relationship between the vectors $q$ , $\dot{q}$ , and $\pmb{u}$ needs to be stipulated. Let the airframe kinematic equations be given as,

$$
f _ {K,} (q, \dot {q}, u) = 0, \quad i = 1, \dots , n _ {R B} \tag {93}
$$

The elements of the vector $f_{K}$ , are given in detail as follows:

$$
\left\{ \begin{array}{c} f _ {K _ {1}} \\ \vdots \\ f _ {K _ {6}} \end{array} \right\} = u _ {F} - \left[ \begin{array}{c c} {[ T _ {F} ] ^ {T}} & 0 \\ 0 & W _ {B} \end{array} \right] \dot {q} _ {F} \tag {94}
$$

$$
\left\{ \begin{array}{c} f _ {K _ {7}} \\ \vdots \\ \vdots \\ f _ {K _ {n _ {R B}}} \end{array} \right\} = \left\{ \begin{array}{c} u _ {R 1, 1} \\ \vdots \\ u _ {R 1, n _ {R 1}} \\ u _ {R 2, 1} \\ \vdots \\ u _ {R 2, n _ {R 2}} \end{array} \right\} - \left\{ \begin{array}{c} \dot {q} _ {R 1, 1} \\ \vdots \\ \dot {q} _ {R 1, n _ {R 1}} \\ \dot {q} _ {R 2, 1} \\ \vdots \\ \dot {q} _ {R 2, n _ {R 2}} \end{array} \right\} \tag {95}
$$

The matrix $W_{B}$ is given as,

$$
W _ {B} = \left[ \begin{array}{c c c} 1 & 0 & - \sin \theta \\ 0 & \cos \phi & \sin \phi \cos \theta \\ 0 & - \sin \phi & \cos \phi \cos \theta \end{array} \right] \tag {96}
$$

# Multiblade Coordinate Transformation

The airframe dynamic and kinematic models, given by Equations 1 and 93, respectively, are derived in the rotating system, with the rotor degrees of freedom describing the motion of individual rotor blades. However, the rotor usually responds as a whole to excitation and for physical insight it is desirable to work with the degrees of freedom which model the entire rotor system rather than the individual blades. To transform the equations of motion with respect to individual blade coordinates to rotor system coordinates, the method of multiblade coordinates is used [11]. Considering the example of rotor 1, for like degrees of freedom, the $k$ th $(k = 1,\dots,n_{R1})$ individual rotor blade degree of freedom is expressed as,

$$
\alpha_ {R 1, k} = \alpha_ {R 1, 0} +
$$

$$
\sum_ {i = 1} ^ {(n _ {R 1} - 1) / 2} \left(\alpha_ {R 1, i c} \cos i \psi_ {k} + \alpha_ {R 1, i s} \sin i \psi_ {k}\right) \tag {97}
$$

for rotors with an odd number of blades and

$$
\alpha_ {R 1, k} = \alpha_ {R 1, 0} +
$$

$$
\sum_ {i = 1} ^ {(n _ {R 1} - 2) / 2} \left(\alpha_ {R 1, i c} \cos i \psi_ {k} + \alpha_ {R 1, i s} \sin i \psi_ {k}\right) +
$$

$$
\alpha_ {R 1, d} (- 1) ^ {k} \tag {98}
$$

for rotors with an even number of rotor blades.

Let the generalized coordinate and generalized speed vectors in the multiblade or non-rotating coordinate system be represented by $q^{\prime}$ and $\pmb{u}^{\prime}$ . Then the following substitutions are made in the airframe kinematic and dynamic model descriptions, given by Equations 93 and 1, respectively.

$$
q = T (t) q ^ {\prime} \tag {99}
$$

$$
u = T (t) q ^ {\prime} + T (t) u ^ {\prime} \tag {100}
$$

$$
\dot {u} = \ddot {T} (t) q ^ {\prime} + 2 \dot {T} (t) u ^ {\prime} + T (t) u ^ {\prime} \tag {101}
$$

Then the resulting airframe kinematic and dynamic equations can be written as,

$$
f _ {K,} \left(q ^ {\prime}, \dot {q} ^ {\prime}, u ^ {\prime}\right) = 0, i = 1, \dots , n _ {R B} \tag {102}
$$

$$
f _ {i} \left(q ^ {\prime}, u ^ {\prime}, w, \dot {u} ^ {\prime}, t\right) = 0, i = 1, \dots , n _ {R B} \tag {103}
$$

where the vector $w$ consists of the inflow coordinates of the two rotors:

$$
w = \left\{w _ {R 1, 0}, w _ {R 1, 1 s}, w _ {R 1, 1 c}, w _ {R 2, 0}, w _ {R 2, 1 s}, w _ {R 2, 1 c} \right\} ^ {T} \tag {104}
$$

# Rotor Dynamic Inflow Model

The rotor dynamic inflow model used in this work is based on the Peters and HaQuang [12] model which is in turn based on the work of Pitt and Peters [8]. The model includes three inflow degrees of freedom that yield the time-varying induced flow parallel to the rotor shaft. Based on the small perturbation potential flow equations, the model accounts for dynamic changes in collective inflow and first harmonic inflow azimuthally. Inflow along the blades varies linearly. The inflow distribution is given by Equation 50. For simplicity only the dynamic inflow model for rotor 1 will be described. The dynamic inflow model for rotor 2 is similar with obvious changes.

The basic model formulation is carried out in the rotor wind axis system and is later transformed to the rotor shaft axis system. The dynamic inflow equations are forced by the averaged (over rotor revolution) rotor thrust, rolling moment, and pitching moment in the shaft axes. The resulting equations can be written in the form,

$$
\left\{ \begin{array}{l} \dot {w} _ {R 1, 0} \\ w _ {R 1, 1 s} \\ w _ {R 1, 1 c} \end{array} \right\} + \left[ A _ {R 1} \right] \left\{ \begin{array}{l} w _ {R 1, 0} \\ w _ {R 1, 1 s} \\ w _ {R 1, 1 c} \end{array} \right\} = \left\{ \begin{array}{l} \frac {- T _ {R 1}}{\rho \pi R _ {1} ^ {3}} \\ \frac {- L _ {R 1}}{\rho \pi R _ {1} ^ {4}} \\ \frac {\bar {M} _ {R 1}}{\rho \pi R _ {1} ^ {4}} \end{array} \right\} \tag {105}
$$

where,

$$
\mathcal {A} _ {R 1} = \mathcal {A} _ {R 1} \left(q ^ {\prime}, u ^ {\prime}\right) \tag {106}
$$

The blade element forces, given by Equation 60, are vectorially summed over all rotor blades to obtain the shaft axis components of the rotor thrust, rolling moment and pitching moment. These forces and moments are then averaged over the period of revolution of the rotor and used in Equation 105.

The complete set of dynamic inflow equations for the two rotors can be functionally represented as,

$$
g _ {i} \left(q ^ {\prime}, u ^ {\prime}, w, \dot {w}\right) = 0, \quad i = 1, \dots , n _ {D I} \tag {107}
$$

where $n_{DI} = 6$ since three state inflow models are being used for each rotor. It should be noted that Equation 107 is written using the multiblade or nonrotating coordinate system.

# Trim Algorithm

Trim of an aircraft is defined as an equilibrium condition where the translational and rotational accelerations of the fuselage are zero. Hence in trim, $\dot{p} = \dot{q} = \dot{r} = \dot{u} = \dot{v} = \dot{w} = 0$ . For straight and level flight, $p = q = r = v = 0$ as well. For a fixed wing airplane this definition is sufficient since one can generally regard an airplane as a single rigid body with six degrees of freedom. For rotorcraft the concept of trim is more complicated because the vehicle is represented as a multibody system consisting of a fuselage, many rotor blades, and a drive system. By virtue of the rotor rotational motion, the blades are always accelerating. For the rotor blade degrees of freedom, trim is considered to be an operating condition such that the individual rotor blades follow a periodic path. This implies that all the first and second derivatives of the rotor multiblate coordinates must be zero in trim. This will force individual blades to track the same periodic path each rotor revolution. However, it should be noted that for even bladed rotors this condition will not force every blade on a rotor to follow the same path. This is due to the warping multiblade coordinate mode for even bladed rotors.

There are many different methods for obtaining the trim condition of a coupled rotor and fuselage combination. Included in these methods are iterative fuselage trim and rotor trim, fully coupled autopilot trim, finite elements in time trim, nonlinear optimization trim, and Galerkin method trim. While no one method for trim is superior in all settings, all the methods are sufficiently different to have qualities which make them more or less attractive in different settings. In this work a nonlinear optimization trim technique is used.

In nonlinear optimization, one seeks to minimize or maximize a certain nonlinear function by iterating on the independent variables of the problem. Here the sum of the squares of the dynamic equation residuals will be minimized and the independent variables will be the system states and controls. A modified Newton's method, sometimes called a damped Newton's method or a quasi Newton method, is used as the nonlinear optimization algorithm to compute the trim state of the vehicle.

The trim algorithm begins by noting that in trim, $\dot{u}^{\prime} = 0$ and $\dot{w} = 0$ necessarily. Hence in trim, the airframe dynamic equations (Equation 1) and the dynamic inflow equations (Equation 107) can be written as,

$$
f _ {i} (x, t) = 0, i = 1, \dots , n _ {R B} \tag {108}
$$

$$
g _ {i} (x) = 0, i = 1, \dots , n _ {D I} \tag {109}
$$

where

$$
\boldsymbol {x} = \left\{\left(q ^ {\prime}\right) ^ {T}, \left(u ^ {\prime}\right) ^ {T}, \left(w\right) ^ {T} \right\} ^ {T} \tag {110}
$$

Clearly, $\pmb{x}$ is the state vector of the airframe dynamic model. Equation 108 contains a set of algebraic nonlinear equations which are periodic in time, with a period of $\tau$ . $\pmb{\tau}$ is the period of revolution common to rotor 1 blades and rotor 2 blades. The goal of the trim algorithm is to minimize the residual of each equation in Equations 108 and 109 for all values of time.

A natural scalar function to minimize for trim is,

$$
\begin{array}{l} J = \frac {1}{\tau} \int_ {0} ^ {\tau} \sum_ {i = 1} ^ {n _ {R B}} f _ {i} (t) ^ {2} d t + \sum_ {i = 1} ^ {n _ {D I}} g _ {i} ^ {2} \\ \approx \frac {\Delta t}{\tau} \sum_ {k = 1} ^ {n _ {T}} \sum_ {i = 1} ^ {n _ {R B}} f _ {i} \left(t _ {k}\right) ^ {2} + \sum_ {i = 1} ^ {n _ {D I}} g _ {i} ^ {2} \tag {111} \\ \end{array}
$$

where $n_T$ is the number of time points chosen for discretization. The function $J$ is termed the cost function. Using the discretized form of the cost function, the gradient and hessian of the cost function can be formed.

$$
\begin{array}{l} \frac {\partial J}{\partial x _ {j}} = 2 \frac {\Delta t}{\tau} \sum_ {k = 1} ^ {n _ {T}} \sum_ {i = 1} ^ {n _ {R E}} f _ {i} \left(t _ {k}\right) \frac {\partial f _ {i} \left(t _ {k}\right)}{\partial x _ {j}} + 2 \sum_ {i = 1} ^ {n _ {D I}} g _ {i} \frac {\partial g _ {i}}{\partial x _ {j}} \tag {112} \\ \frac {\partial}{\partial x _ {l}} \left(\frac {\partial J}{\partial x _ {j}}\right) \approx \\ \end{array}
$$

$$
\begin{array}{l} 2 \frac {\Delta t}{\tau} \sum_ {k = 1} ^ {n _ {T}} \sum_ {i = 1} ^ {n _ {R B}} \left[ \frac {\partial f _ {i} (t _ {k})}{\partial x _ {l}} \frac {\partial f _ {i} (t _ {k})}{\partial x _ {j}} + f _ {i} (t _ {k}) \frac {\partial^ {2} f _ {i} (t _ {k})}{\partial x _ {l} \partial x _ {j}} \right] \\ + 2 \sum_ {i = 1} ^ {n _ {D I}} \left[ \frac {\partial g _ {i}}{\partial x _ {l}} \frac {\partial g _ {i}}{\partial x _ {j}} + g _ {i} \frac {\partial^ {2} g _ {i}}{\partial x _ {l} \partial x _ {j}} \right] \tag {113} \\ \end{array}
$$

The minimization problem described above is essentially a least squares problem. It is known that for least square minimization problems, where the cost function is small at the solution, the second derivative terms in the above equations are relatively small and can be neglected [13]. By definition, this assumption is valid in the trim problem.

In a modified Newton's method, a local optimization problem is solved iteratively. A flow chart for the iteration procedure is given in Figure 6. Using an initial condition or guess for the trim variables, a local quadratic model of the cost function is formed,

$$
J (x + \Delta x) = J (x) + \frac {\partial J}{\partial x} \Delta x + \frac {1}{2} \Delta x ^ {T} \frac {\partial^ {2} J}{\partial x ^ {2}} \Delta x \tag {114}
$$

At the local minimum of this approximation to the actual cost function one must have,

$$
\frac {\partial J}{\partial \Delta x} = 0 \tag {115}
$$

For a local minimum of a quadratic function to exist, hessian matrix of the cost function must be positive definite. Assuming this is the case,

$$
\Delta x = - \left[ \frac {\partial^ {2} J}{\partial x ^ {2}} \right] ^ {- 1} \left\{\frac {\partial J}{\partial x} \right\} \tag {116}
$$

The vector $\Delta x$ is called the search direction because based on this direction a search to reduce the cost function shall be undertaken. For the local quadratic model of the cost function, the minimum is given by $x + \Delta x$ , of course if a minimum exists. A new iteration on the minimum of the actual cost function can now be made by with the equation,

$$
x _ {n e w} = x _ {o l d} + \alpha \Delta x \tag {117}
$$

The parameter, $\alpha$ , is the step length. It is used because the local model is only an approximation to the actual cost. $\alpha = 1$ corresponds to a full Newton's method while $\alpha < 1$ implies a damped or modified Newton's method. The parameter $\alpha$ is determined at each trim iteration and is based on satisfying criteria for tracking sufficient decrease in the cost function at each iteration in the overall minimization problem. The process of determining the step length is called a step length procedure or line search strategy.

There are many criteria for determining sufficient decrease in the cost function at each iteration. Armijo's rule is used here which can be stated as,

$$
J _ {0} - J _ {\alpha} \geq - \mu \alpha \frac {\partial J}{\partial x} \Delta x \tag {118}
$$

where the constant $\mu$ is a positive number. A back tracking strategy is used in the line search strategy. In this method, one always starts with $\alpha = 1$ and tries to use the full Newton's method if possible. If the current $\alpha$ does not fulfill the Armijo condition, then $\alpha$ is divided by a factor and retried. Once an appropriate value for $\alpha$ is obtained, new values for $x$ are computed. Then a new local quadratic model is formed and the optimization procedure is again formed. It should be noted that in solving for the search direction a linear system must be solved. It is solved using a modified Choleski decomposition algorithm as described in reference [13].

# Linear Model of Airframe Dynamics

Linearized rotorcraft dynamic models are extremely useful for flying qualities analyses. To this end, the composite airframe dynamic model consisting of the kinematic, dynamic, and dynamic inflow

models, given by Equations 102, 103, and 107, respectively, is linearized about an arbitrary trim state, $x_0$ . The linear model can be written as,

$$
C _ {p} \left(\boldsymbol {x} _ {0}, t\right) \delta \dot {\boldsymbol {x}} = D _ {p} \left(\boldsymbol {x} _ {0}, t\right) \delta \boldsymbol {x} \tag {119}
$$

The $(2n_{RB} + n_{DI})\times (2n_{RB} + n_{DI})$ square matrices $C_p$ and $D_{p}$ are given as,

$$
C _ {P} = \left[ \begin{array}{c c c} \frac {\partial f _ {K}}{\partial q ^ {\prime}} & 0 & 0 \\ 0 & \frac {\partial f}{\partial u ^ {\prime}} & 0 \\ 0 & 0 & \frac {\partial q}{\partial w} \end{array} \right] \tag {120}
$$

$$
D _ {p} = - \left[ \begin{array}{c c c} \frac {\partial f _ {K}}{\partial q ^ {\prime}} & \frac {\partial f _ {K}}{\partial u ^ {\prime}} & 0 \\ \frac {\partial f}{\partial q ^ {\prime}} & \frac {\partial f}{\partial u ^ {\prime}} & \frac {\partial f}{\partial w} \\ \frac {\partial g}{\partial q ^ {\prime}} & \frac {\partial g}{\partial u ^ {\prime}} & \frac {\partial g}{\partial w} \end{array} \right] \tag {121}
$$

where

$$
f _ {K} = \left\{f _ {K _ {1}}, \dots , f _ {K _ {n _ {R B}}} \right\} ^ {T} \tag {122}
$$

$$
f = \left\{f _ {1}, \dots , f _ {n _ {R B}} \right\} ^ {T} \tag {123}
$$

$$
g = \left\{g _ {1}, \dots , g _ {n _ {D I}} \right\} ^ {T} \tag {124}
$$

In the ensuing analysis, the $\delta$ 's in Equation 119 will be dropped and the perturbation state of the aircraft will be simply denoted as $x_{ac}$ .

# Transformation of the Airframe Linear Dynamic Equations

The multiblade coordinate transformation should be accompanied by a transformation of the equations of motion to the non-rotating coordinate system. This step is accomplished by taking linear combinations of the equations of motion given by Equation 119. The operations can be performed by premultiplying the dynamic equations by a transformation matrix, $\bar{T}(t)$ . The fully transformed linear equations are,

$$
\bar {T} (t) C _ {p} (t) \dot {x} _ {a c} = \bar {T} (t) D _ {p} (t) x _ {a c} \tag {125}
$$

In rotorcraft handling qualities analysis, a linear time invariant system is most convenient to work with due to the powerful linear system analysis tools available. A standard approximation used in rotorcraft handling qualities work is to neglect the harmonic content in Equation 125 and hence obtain a linear time invariant system. This approximation is known as the constant coefficient approximation and it is used in the current effort.

The blade pitch control terms can be separated from the above equations by assuming that the multiblade coordinate blade pitch degrees of freedom do

not possess dynamics. Appropriate rows of the dynamics matrix are deleted and the associated columns form the controls matrix. The final form of the airframe linear dynamic equations is,

$$
\dot {x} _ {a c} = A x _ {a c} + B \vartheta \tag {126}
$$

$$
y _ {a c} = C x _ {a c} + D \vartheta \tag {127}
$$

where the vector $\vartheta$ consists of individual rotor pitch control variables. This system can now be coupled to the flight control system to form the complete system.

# Linear Control System Model

Most aircraft flight control systems are given in block diagram form and there is no standard structure. Although for modeling purposes, a generic flight control system structure could be assumed such that all or at least a majority of current aircraft flight control systems could be accommodated, it is felt this approach may be too restrictive in some cases and far too general, hence inefficient, in other cases. It is desirable to have a flight control system modeling capability which does not assume a structure apriori but uses the input data deck to generate the model. This approach allows for greater flexibility and increased utility of the control system model. With these considerations in mind, a linear state-space flight control system modeling capability was developed that takes the basic block diagram data as input.

The flight control system is assumed to be comprised of an arbitrary number of filters, given in polynomial form. Each filter is a multi input and single output filter as shown in Figure 7.

The inputs to each filter can consist of pilot stick inputs, outputs of other individual filters, aircraft states, and derivatives of aircraft states. A statespace realization is computed for each individual filter in phase variable canonical form. The filters are then assembled into an overll state-space realization.

The realization can be written as,

$$
\dot {x} _ {c s} = A _ {u} x _ {c s} + B _ {u} v _ {u} \tag {128}
$$

$$
y _ {u} = C _ {u} x _ {c s} + D _ {u} v _ {u} \tag {129}
$$

The subscript $u$ signifies that the state-space matrices do not account for the filter coupling. A filter coupling matrix can be computed in the form,

$$
v _ {u} = \zeta_ {u} y _ {u} + \beta_ {u} \delta + \gamma_ {u} x _ {a c} + \sigma_ {u} \dot {x} _ {a c} \tag {130}
$$

It should be noted that Equations 128, 129 and 130 can be constructed in a straight forward manner from the input block diagram data. Substituting Equation

130 into Equations 128 and 129, the coupled statespace model of the control system can be formed.

$$
\dot {x} _ {c s} = F x _ {c s} + G \delta + H x _ {a c} + E \dot {x} _ {a c} \tag {131}
$$

$$
\vartheta = P x _ {c s} + Q \delta + R x _ {a c} + Z \dot {x} _ {a c} \tag {132}
$$

where,

$$
F = A _ {u} + B _ {u} \zeta_ {u} S _ {u} \tag {133}
$$

$$
G = B _ {u} \zeta_ {u} U _ {u} + B _ {u} \beta_ {u} \tag {134}
$$

$$
H = B _ {u} \zeta_ {u} V _ {u} + B _ {u} \gamma_ {u} \tag {135}
$$

$$
E = B _ {u} \zeta_ {u} W _ {u} + B _ {u} \sigma_ {u} \tag {136}
$$

$$
P = X \left[ C _ {u} + D _ {u} \zeta_ {u} S _ {u} \right] \tag {137}
$$

$$
Q = X \left[ D _ {u} \zeta_ {u} U _ {u} + D _ {u} \beta_ {u} \right] \tag {138}
$$

$$
R = X \left[ D _ {u} \zeta_ {u} V _ {u} + D _ {u} \gamma_ {u} \right] \tag {139}
$$

$$
Z = X \left[ D _ {u} \zeta_ {u} W _ {u} + D _ {u} \sigma_ {u} \right] \tag {140}
$$

$$
S _ {u} = [ I - D _ {u} \zeta_ {u} ] ^ {- 1} C _ {u} \tag {141}
$$

$$
U _ {u} = [ I - D _ {u} \zeta_ {u} ] ^ {- 1} D _ {u} \beta_ {u} \tag {142}
$$

$$
V _ {u} = [ I - D _ {u} \zeta_ {u} ] ^ {- 1} D _ {u} \gamma_ {u} \tag {143}
$$

$$
W _ {u} = [ I - D _ {u} \zeta_ {u} ] ^ {- 1} D _ {u} \sigma_ {u} \tag {144}
$$

The matrix $X$ restricts the overall control system outputs to be the aircraft blade pitch angles. It should be noted that if the matrix $[I - D_u\zeta_u]$ is singular, then there is not a valid state-space model for the system and the system is non-causal. This is due to the fact that the flight control system output can be written as,

$$
\left[ I - D _ {u} \zeta_ {u} \right] y = C _ {u} x _ {c s} + D _ {u} \beta_ {u} \delta + D _ {u} \gamma_ {u} x _ {a c} + D _ {u} \sigma_ {u} \dot {x} _ {a c} \tag {145}
$$

For a valid state-space realization the output must be uniquely determined from the state and control. Clearly when $[I - D_u\zeta_u]$ is singular this is not possible. This observation can be used for detecting input data errors.

# Airframe and Control System Coupling

The linear airframe model which describes the rigid body aircraft motion and rotor dynamic inflow is given by Equations 126 and 127. The inputs to the airframe linear equations are blade pitch angles of the two rotor systems. The linear flight control system model is given by Equations 131 and 132. The outputs of the flight control system model are also the blade pitch angles of the two rotors. The linear airframe and control system models are coupled by noting that the output of the flight control system model is the input to the airframe model.

$$
\left\{ \begin{array}{l} \dot {x} _ {a c} \\ \dot {x} _ {c s} \end{array} \right\} = \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1} & A _ {2 2} \end{array} \right] \left\{ \begin{array}{l} x _ {a c} \\ x _ {c s} \end{array} \right\} + \left[ \begin{array}{l} B _ {1} \\ B _ {2} \end{array} \right] \{\delta \} \tag {146}
$$

$$
\left\{y _ {a c} \right\} = \left[ \begin{array}{l l} C _ {1} & C _ {2} \end{array} \right] \left\{ \begin{array}{l} x _ {a c} \\ x _ {c s} \end{array} \right\} + \left[ D _ {1} \right] \left\{\delta \right\} \tag {147}
$$

where,

$$
A _ {1 1} = A + B \Pi \tag {148}
$$

$$
A _ {1 2} = B \Upsilon \tag {149}
$$

$$
A _ {2 1} = H + E (A + B \Pi) \tag {150}
$$

$$
A _ {2 2} = F + E B \Upsilon \tag {151}
$$

$$
B _ {1} = B \Xi \tag {152}
$$

$$
B _ {2} = G + E B \Xi \tag {153}
$$

$$
C _ {1} = C + D \Pi \tag {154}
$$

$$
C _ {2} = D \Upsilon \tag {155}
$$

$$
D _ {1} = D \Xi \tag {156}
$$

$$
\Pi = [ I - Z B ] ^ {- 1} (R + Z A) \tag {157}
$$

$$
\Upsilon = [ I - Z B ] ^ {- 1} P \tag {158}
$$

$$
\equiv = [ I - Z B ] ^ {- 1} Q \tag {159}
$$

# Concluding Remarks

A linear coupled rotor-fuselage-control system dynamic model is presented in this paper. The model is expected to be useful for flying qualities studies, stability and control investigations, and control design parametric studies. Efforts are underway to produce numerical results for the validation of the model.

# References

[1] Miller, D.G., and White, F., “A Treatment of the Impact of Rotor-Fuselage Coupling on Helicopter Handling Qualities,” Proceedings of the 43rd Annual Forum of the American Helicopter Society, St. Louis, MO, May 1987.   
[2] Talbot, P.D., Tinling, B.E., Decker, W.A., and Chen, R.T.N., "A Mathematical Model of a Single Main Rotor Helicopter for Piloted Simulation," NASA TM 84281, September 1982.   
[3] Gibbons, M.P., and Done, G.T.S., "Automatic Generation of Helicopter Rotor Aeroelastic Equations of Motion," Vertica, Vol. 8, No. 3, pp. 229-241, 1984.   
[4] Lytwyn, R.T., "Aeroelastic Stability Analysis of Hingeless Rotor Helicopters in Forward Flight Using Blade and Airframe Normal Modes," Proceedings of the 36th Annual Forum of the American Helicopter Society, Washington DC, May 1980.

[5] Zhao X., and Curtiss H.C., "A Linearized Model of Helicopter Dynamics Including Correlation with Flight Test," Proceedings of the Second International Conference on Rotorcraft Basic Research, University of Maryland, College Park, Maryland, 1988.   
[6] McKillip R., Curtiss H.C., “Approximations for Inclusion of Rotor Lag Dynamics in Helicopter Flight Dynamics Models,” Proceedings of the Seventeenth European Rotorcraft Forum, Berlin, Germany, September 1991.   
[7] Kane, T.R., and Levinson, D.A., Dynamics: Theory and Applications, McGraw Hill Book Company, 1985.   
[8] Pitt, D.M., and Peters, D.A., "Theoretical Prediction of Dynamic Inflow Derivatives," *Vertical Vol.* 5, pp. 21-34, 1981.   
[9] Prouty, R.W., Helicopter Performance, Stability, and Control, PWS Publishers, 1986, pp. 379-441.   
[10] Johnson, W., Helicopter Theory, Princeton University Press, 1980, pp. 213-216.   
[11] Hohenemser K.H., and Yin, S.K., "Some Applications of the Method of Multiblade Coordinates," Journal of the American Helicopter Society, Vol. 17, No. 3, July 1972, pp. 3-12.   
[12] Peters, D.A., HaQuang N., "Dynamic Inflow for Practical Applications," Journal of the American Helicopter Society, Volume 33, Number 4, October 1988.   
[13] Gill, P.E., Murray, W., and Wright, M.H., Practical Optimization, Academic Press, 1989, pp. 105-115.

The matrices $E_{1}, E_{2}$ , and $E_{3}$ represent single axis transformations about $x, y$ , and $z$ axes, respectively, and are defined as follows:

$$
\begin{array}{l} E _ {1} (\kappa) = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \cos \kappa & \sin \kappa \\ 0 & - \sin \kappa & \cos \kappa \end{array} \right] \\ E _ {2} (\kappa) = \left[ \begin{array}{c c c} \cos \kappa & 0 & - \sin \kappa \\ 0 & 1 & 0 \\ \sin \kappa & 0 & \cos \kappa \end{array} \right] \\ E _ {3} (\kappa) = \left[ \begin{array}{c c c} \cos \kappa & \sin \kappa & 0 \\ - \sin \kappa & \cos \kappa & 0 \\ 0 & 0 & 1 \end{array} \right] \\ \end{array}
$$

# Time-Derivative of a Transformation Matrix

Consider the time-derivative of a vector $v$ in two reference frames denoted by $A$ and $B$ . Let the components of $v$ in Frame $A$ be denoted by $v_A$ and those in Frame $B$ be denoted by $v_B$ . Let the angular velocity of Frame $B$ with respect to Frame $A$ be $\omega$ and let the components of $\omega$ in Frame $B$ be denoted by $\omega_B$ . Let $T$ represent the transformation matrix that transforms vector components from Frame $B$ axes to components in Frame $A$ axes. The time-derivatives of $v$ in Frame $A$ and Frame $B$ are related by the following vectorial equation:

$$
^ A \frac {d v}{d t} = ^ B \frac {d v}{d t} + \omega \times v
$$

In matrix-vector format, the preceding equation can be written as,

$$
\dot {v} _ {A} = T \dot {v} _ {B} + T S (\omega_ {B}) v _ {B}
$$

Also, since $v_{A} = Tv_{B}$ , one gets for $\dot{v}_{A}$ the following expression:

$$
\dot {v} _ {A} = T \dot {v} _ {B} + \dot {T} v _ {B}
$$

Comparing the two equations for $\dot{v}_A$ , the following formula is obtained for $\dot{T}$ :

$$
\dot {T} = T S \left(\omega_ {B}\right)
$$

# Appendix

# Skew-Symmetric Matrix Operator

For a vector $a = \{a_1, a_2, a_3\}^T$ , the matrix $S(a)$ is defined as,

$$
S (a) = \left[ \begin{array}{c c c} 0 & - a _ {3} & a _ {2} \\ a _ {3} & 0 & - a _ {1} \\ - a _ {2} & a _ {1} & 0 \end{array} \right]
$$

Single Axis Transformation Matrices

图片摘要：该图主要展示 1: Generic Rotorcraft Configuration。
![](images/0599df4f1a6383c2e62c162f6f2b7b98a451a6dad95806f272d9e0b3527f34bb.jpg)  
Figure 1: Generic Rotorcraft Configuration

图片摘要：该图主要展示 1: Generic Rotorcraft Configuration。
![](images/a81f2201ae07205abbdd9d80600c7f63e5774c8152520346d4ce3281a88539a1.jpg)  
Figure 3: jth Aerodynamic Element of the ith Rotor 1 Blade

图片摘要：该图主要展示 3: jth Aerodynamic Element of the ith Rotor 1 Blade。
![](images/75e829e329dc962b7b2cef996f059f92ef8f4f36c6d289d8ab8ca26e33ea58f5.jpg)  
Figure 4: External Surface Aerodynamic Sections

图片摘要：该图主要展示 4: External Surface Aerodynamic Sections。
![](images/6e8feb302d531504813055620f60f11edf36e99efb6ca033268b9c1798f4581b.jpg)  
Figure 2: Rotor Blade Geometry

图片摘要：该图主要展示 2: Rotor Blade Geometry。
![](images/a0b7d19dbd00f36e685d40fa70c7af513a5b66cc232c2f9afbdeeaab9b84c482.jpg)

图片摘要：该图主要展示 2: Rotor Blade Geometry。
![](images/f9b892456db983e81ebd7e3b1b20a44fcafb50f751057e95f4e7333e3b2f91cd.jpg)  
Figure 5: jth Aerodynamic Section of Surface 1 in Yawed Free Stream

图片摘要：该图主要展示 5: jth Aerodynamic Section of Surface 1 in Yawed Free Stream。
![](images/72635f15b5da90b16775c8772575da89ccad19f9d64430525cc4314dceffbc2f.jpg)  
Figure 6: Trim Procedure Flowchart

图片摘要：该图主要展示 6: Trim Procedure Flowchart。
![](images/cbc1ca85c9135a67c12957266957c6d9eba919271e736d48c346590868d6462f.jpg)  
Figure 7:ith Flight Control System Filter

ni(i) = Number of Inputs to i'th Filter

no(1) = Order of i'th Filter

y(i) = Output of i'th Filter

$k_{i,j} =$ Gain Multiplying $j^{\prime}$ th input of i'th Filter

# INTERPRETED COOPER-HARPER FOR BROADER USE

David L. Green  
President, Starmark Corporation  
Arlington, Virginia

Hal Andrews (retired)  
Technical Director, Research and Technology  
Naval Air Systems Command

Donald W. Gallagher  
Night Vision Operations Project Manager  
FAA Technical Center, Atlantic City International Airport, New Jersey

# ABSTRACT

The current aircraft assessment process typically makes extensive use of operational personnel during simulations and operational evaluations, with increased emphasis on evaluating the many pilot and/or operator/aircraft control loops. The need for a crew assessment in this broader arena has produced a variety of rating scales. The Cooper-Harper Rating Scale is frequently misused and routinely overlooked in the process, for these applications often extend the scale's use beyond its originally intended application. This paper agrees with the broader application of the Cooper-Harper Rating Scale and presents a concept for the development of a "use unique" Interpreted Cooper-Harper Scale to help achieve this objective. This interpreted scale concept was conceived during efforts to support an FAA evaluation of a night vision enhancement system. It includes descriptive extensions, which are faithful to the intent of the current Cooper-Harper Scale and should provide the kind of detail that has historically been provided by trained test pilots in their explanatory comments.

# NOMENCLATURE

<table><tr><td>CHPRS</td><td>Cooper-Harper Pilot Rating Scale</td></tr><tr><td>CM</td><td>Cockpit Management</td></tr><tr><td>DI</td><td>Deck Interface</td></tr><tr><td>EMS</td><td>Emergency Medical Service</td></tr><tr><td>FAA</td><td>Federal Aviation Administration</td></tr><tr><td>HQR</td><td>Handling Quality Rating</td></tr><tr><td>ICHRS</td><td>Interpreted Cooper-Harper Rating Scale</td></tr><tr><td>IFR</td><td>Instrument Flight Rules</td></tr><tr><td>IMC</td><td>Instrument Meteorological Conditions</td></tr><tr><td>IPR</td><td>Interpreted Pilot Rating</td></tr><tr><td>LFE</td><td>Limit Flight Envelope</td></tr><tr><td>MCHRS</td><td>Modified Cooper-Harper Rating Scale</td></tr><tr><td>NAS</td><td>National Airspace System</td></tr><tr><td>NFE</td><td>Normal Flight Envelope</td></tr><tr><td>NOE</td><td>Nap-of-the-Earth</td></tr><tr><td>OFE</td><td>Operational Flight Envelope</td></tr><tr><td>PR</td><td>Pilot Rating</td></tr><tr><td>VMC</td><td>Visual Meteorological Conditions</td></tr></table>

# INTRODUCTION

The Cooper-Harper Pilot Rating Scale (CHPRS) has been very effective in handling qualities research and development applications, serving as an evaluation tool and communications medium in a community of trained experimental and R&D test pilots and engineers. The success of CHPRS has in some measure been due to the discipline involved in its use. This discipline has been instilled thorough training at test pilot schools, use of the scale in the military acquisition process, and because of adherence to the asterisk note which appears on the scale: "Definition of required operation involves designation of flight phase and sub-phases with accompanying conditions".

In Reference 1, Harper and Cooper emphasize the need to follow this stricture. While recognizing the difficulties in doing so, they also recognize the adverse impact of failure to treat this instruction in a comprehensive way.

Currently, the assessment process in new product development for aircraft has taken on a greater operational flavor. This is found both at the project initiation stage, where extensive simulations using operational personnel are becoming the rule, and at the final approval stage where operational personnel hold the final stamp. At the same time, the greatly increased integrated complexity of the pilot machine interface systems increases the emphasis on evaluating the many in-flight dynamic components of the pilot and/or operator/aircraft control loop. This complexity is amplified for rotorcraft, where the total flight regime includes the widest variety of flight path tasks.

The need for a rating scale in this broader arena has required the use of evaluation scales of some sort, and perhaps because piloting considerations are generally involved --- but not always --- the Cooper-Harper scale is frequently used. Sometimes it is misused in this broader context. Sometimes it is not applied because of concern for misuse, or a bureaucratic constraint or because it is simply not understood.

To those who have been trained in the use of the scale, it is clear and provides a concise and useful way for members of the handling qualities community to communicate. To many outside the handling qualities community, a reluctance to apply the scale is evoked by a lack of confidence in the use of subjective pilot evaluations. This group typically desires to use a pass fail criteria pilot (crew) evaluation or alternately base

decisions on quantitative measures alone. It appears that the reservations of some are reinforced by their unsuccessful attempts to use the scale. These attempts may have failed to observe the asterisked stricture of the CHPRS (see Figure 1).

A case can be made for using some other scale, or using the CHPRS with a second overlapping workload scale, or using no subjective scale at all. But because handling qualities are major components of all aircraft pilot/operator assessments, and because the scale has always included consideration of workload, it seems most appropriate to improve our understanding of the existing CHPRS and broaden its applications. To this end, this paper proposes that a well understood, expanded and interpreted version of the CHPRS would:

(1) Help the aviation community define the factors which respond to the asterisk note on the CHPRS, minimizing variance in pilot ratings.   
(2) Include a concept which involves developing "application unique" extensions to the descriptive content of the scale to enhance its use by both trained engineering test pilots and by operational evaluation pilots. These expanded definitions will allow pilots to:   
(a) Select a correct rating which may be a whole number or a half pilot rating (PR), and   
(b) provide additional comments which will help others understand the experience underlying the selected rating (in terms which include flying qualities, flying workload, cockpit management (CM) workload and relevant performance measures).   
(3) Better explain how experienced subject pilots can predict the suitability of an aircraft for operations in environments not specifically evaluated.

In summary, paper supports the broader application of the current CHPRS and it offers a concept for achieving this objective through the introduction of an use-specific, Interpreted Cooper-Harper Pilot Rating Scale.

# COOPER-HARPER RATINGS

# Background

The first widely used pilot rating scale was introduced in 1957 and known as the Cooper Scale (Reference 2). This was followed by an interim scale in 1966 (Reference 3) and finally in 1969 the Cooper-Harper rating scale, presented here as Figure 1, was published in NASA TN D-5153 (Reference 4).

The key to effective use of this scale lies in strict adherence to the guidelines contained in References 1 and 4, and in the thorough understanding of the scale's origins, strengths and limitations. In this regard, Harper and Cooper reported in Reference 1 that the "nearly universal use of the Cooper-Harper rating scale for handling qualities assessments is not commensurate with the general lack of access to and familiarity

with NASA TN D-5153 (which gives background guidance, definition of terms, and recommended use). In other words, everybody uses the scale, but few have studied Reference 4 and/or observe the counsel of Reference 4.

It is important to understand that most of the ideas and suggestions in this paper are not new. For the most part, they are over 30 years old and alluded to in the above references. This paper does provide suggested ways to implement the guidance of References 1 and 4 as well as expanding the application of the scale to address the current needs of the industry. In this regard, the following paragraphs quote, paraphrase, and amplify a number of key concepts and instructions contained in the primary references:

# A Communication Enhancement Tool

There are two parts to the rating process: "The pilot's commentary on the observations he made, and the rating he assigned. --- They are the most important data on the closed-loop pilot-airplane combination which the engineer has." (Reference 1). The rating numbers themselves are an aeronautical short hand developed for recording, quantifying and analyzing subjective data. These ratings are a means to an end. They are not the end of the process.

# Engineering Test Pilots

The scale in Figure 1 was developed for use by experimental and engineering test pilots. These test pilots typically have an operational background and have been trained to communicate with the engineering community. The military pilot becomes a test pilot after acquiring a personal understanding of the environment, threat and related friendly weapons systems which will define the total combat environment. They then learn (civil or military) to evaluate flying qualities in context with the cockpit workload with a readiness to deal with the environment and the adversity introduced by equipment failures.

# Pilot Comments

Engineering test pilots are expected to know how to provide task ratings and comments which are useful in the analysis of the flights they conduct. It is not enough to provide a rating. The pilot must provide comments as to what the pilot experienced. The pilot must report what did and (sometimes) what did not influence the assignment of a given rating. For example, one pilot may use one technique to compensate for a lateral directional oscillation and be very successful, while a second pilot may not understand the best compensatory technique, have a great deal more trouble and assign a poor rating.

# Operational Pilots

There are three probable situations where the operational pilots (unschooled in the methods of the engineering test pilots) could be expected to utilize the CHPRS. --- In the ground based and inflight

图片摘要：该图主要展示 1: The Cooper Harper Pilot Rating Scale。
![](images/5a0cd7f86454fac1c45ebba8195c5f1a61192764cdc51bef3a2131a82acd3d7f.jpg)  
Figure 1: The Cooper-Harper Pilot Rating Scale

simulations cases, the resident simulation staff is very familiar with the use of the CHPRS and they are inclined to attempt to have the operational pilot use the CHPRS. The results of this application are potentially flawed because the operational pilots may not understand the proper use of the scale. --- The scale looks simple, and these otherwise very capable pilots understate their lack of comprehension in an effort to be accommodating.

In the operational evaluation venue, the resident engineers and analysts are much less familiar with the CHPRS and often hesitate to employ it. Here an opportunity for broader use is missed.

In brief, the CHPRS is not sufficiently user friendly for many operational pilot applications unless the pilots and engineers are diligently trained in its use.

# The Scale

The scale presented in Figure 1 incorporates 10 ratings. Cooper and Harper feel that these ratings should be adequate for most evaluations (Reference 4). While they also recognize that the use of half rating gradation is appropriate for some applications (e.g. 3.5 and 4.5), they discourage the practice. One reason for this reluctance is obvious. There are no definitions of half ratings.

Another argument against the use of half ratings asserts that ability of pilots to discriminate between flying qualities (workload and performance) is not sufficient to empower them to assign half ratings. The data in Figure 2 argues against this last assertion, for it contains a family of boundaries which separate areas of the flight envelope which were judged by an engineering test pilot to contain flying qualities that differ by one half of one PR. Boundaries of this sort were first identified in Reference 5, and later defined in flight with a small, modern helicopter. Over 60 pilot ratings were recorded during stabilized, standard rate turning flight, while observing error limits of $\pm 5$ knots and $\pm 50$ ft/min. The actual ratings assigned to each area of the flight envelope vary as a function of the accompanying conditions (e.g., turbulence, lighting, visibility, etc.).

# Pilot Compensation/Workload Factors

The level of pilot compensation necessary to achieve "adequate" or "desired" performance (see Figure 1) is integral to the use of CHPRS. Implicitly, this compensation is directly translatable to workload. Furthermore, the phrase "definition of required operation" (included in the asterisk note of the CHPRS) serves to include both direct flight control and other flight management functions which the pilot must perform to achieve satisfactory task performance.

In the real world, the pilot approaches a flight task with the expectation that the task is doable. That is, pilots look at all of the sources of workload and attempt to cope with each source in the way which produces the best performance with a minimum of effort. As Harper and Cooper observe in Reference 1, "the pilot adapts". From the view of the systems engineer, the pilot learns how to achieve the desired performance while optimally distributing the piloting (handling qualities) workload and cockpit management (CM) workload. In military combat aircraft, mission equipment monitoring and task execution workload is also involved.

The engineer understands that tasks are distributed by the crew in a natural attempt to avoid spikes in workload which are likely to be accompanied by an unwanted dip in performance. It is this effective search for adaptive techniques which exemplifies the pilot's contribution to crew-machine performance.

As the total workload builds, the pilot may have reason to periodically (albeit very briefly) allocate a high priority to CM tasks and allow errors in the flight path to build during a period of deferred attention. The performance during such unattended periods is therefore judged differently. The pilot who is prepared to allow an aircraft to drift off speed, or roll away from level flight, has substituted new (temporary) limits on

图片摘要：该图主要展示 2: Boundaries of Flying Qualities Which Represent A Change o。
![](images/b24a8bb4bbf868d4f8454e1aefa7513f6360e3755590f1eeb778058c904dca7c.jpg)  
Figure 2: Boundaries of Flying Qualities Which Represent A Change of 0.5 Pilot Rating

the allowable flight path errors. These larger allowable errors apply only during the performance of the priority CM task. Typically, the pilot monitors the aircraft's departure from trim, and if every thing goes well, the CM task is completed during one period of unattended flight. If the aircraft departs too quickly, or is difficult to return to trim, several periods of unattended or deferred flight control activity may be utilized to complete the CM task. Pilots evaluate such shared attention requirements and make a determination as to suitability.

Pilots also develop CM techniques which minimize the time required to accomplish CM tasks. For example, they learn how to identify switches by location, shape and mode of operation. This allows them to find a switch while focusing their eyes on a flight control task. The mind is obviously able to share its attention more rapidly than the eyes, especially when head movement is required.

In addition, pilots who are faced with the need to use the right hand to conduct a CM task may use the left hand to control pitch and roll during the CM event. A pilot may also use a knee to hold a collective in position, or use both feet on the directional controls to keep the aircraft level in roll. Such techniques may result in substantially less deviation from the desired flight path with little or no increase in total workload. This is the way pilots learn to get the job done in the real world. Test pilots know these techniques and engineers need to report which ones they use.

When pilots encounter a task which is not doable, many will attribute the failure to a personal inability. But, the more experienced the pilot, the less likely this will occur. Never-the-less, this is one more reason why it is very important for the analyst to understand the attitudes of subject pilots.

In the vein of doable tasking, the "unexpected" typically places the ultimate stress on crew performance. The occurrence of unplanned events such as equipment malfunctions, unexpected route changes and unforecast weather are all a part of the equation. A totally correct evaluation of these events typically requires a concomitant engineering analysis to determine the probability of a given event.

# Defining The Task

The CHPRS (Figure 1) contains a note which is often given less than adequate consideration. The note refers to the "task" or "operation" and alerts us to the effect: "Definition of required operation involves designation of flight phases and sub-phases with accompanying conditions."

Flight Phases and Sub-Phases. If we translate the definitions of flight phase and sub phases as stated in Reference 4, we find that hovering flight and cruise flight are two typical flight phases. Activities

associated with achieving a 40 ft hover is a sub phase. Maintaining a steady 40 ft hover is also a sub phase.

Accompanying Conditions. The factors which collectively define "accompanying conditions" substantially influence the assignment and analysis of pilot ratings. Typically, the project engineer must define accompanying conditions prior to the flight for they at least partially define the test objective or "scope of test". The pilot needs this guidance to accomplish the desired evaluation. The actual accompanying conditions, observed during the execution phase, must be recorded to support the best possible analysis and avoid unexplainable variance in the data.

The factors which define some rotorcraft tasks can normally be selected from a list like the partial one presented below:

(1) VMC or IMC task

-type of cue field and display augmentation   
display system

(2) Performance Objectives

- altitude (absolute or as measured by radar altimeter)   
- horizontal position error (X and Y)   
- heading variation limits   
- main transmission torque limits   
- engine operating limits   
- attitude variation limits during corrections (± degrees)   
- attitude variation allowed as the result of a gust or turbulence   
time available to conduct non flight control cockpit tasks (schedule of shared time)

(3) Environmental Factors

- underlying surface   
- near field visual screen   
- far field visual screen   
- near hazards-obstructions to hover   
- lighting   
- visual range   
- obstructions to visibility   
- precipitation   
- smoke, fog. dust, snow, sun.   
- glare, sun, moon, reflections

While most of the flying qualities community clearly understands the importance of the items listed under (1) and (2) above, the environmental factors under (3) seem to be less appreciated and are more often than not treated in too general a way. For example, limit environmental conditions are sometimes established by as few as one or two parameters (e.g., visibility). Such an abbreviated treatment is often inadequate, especially in the case of helicopters required to operate to and from a variety of fixed and moving platforms, in a rapidly changing air mass, day and night. Figure 3 was adapted from Reference 5 to expand on the list above and to illustrate the variety of conditions which

may be of interest during rotorcraft evaluations. While this figure is admittedly incomplete, figures like this should be provided so that pilots and engineers can accurately define sets of conditions for evaluation. In the real world, we find that rotorcraft pilots are interested in a variety of environmental conditions, any or all of which can represent a limit condition.

Before leaving this subject, it is important to recognize that the introduction of "usable cue environments" in Reference 6 is an important contribution and a significant step in the right direction, as is the Navy's deck interface (DI) testing methodology which recognizes ship motion, lighting, wind, and other factors identified in Figure 3.

图片摘要：该图主要展示 3: Characteristics Defining Operational Environment。
![](images/80f570dec64dd0a6e7ca24430c2c573d25d8e56b327f9749efb888faf67e5b93.jpg)  
Figure 3: Characteristics Defining Operational Environment

图片摘要：该图主要展示 3: Characteristics Defining Operational Environment。
![](images/57093bedc302b6a91fb83ca28c9d433397a8568c671c56582af4d7a30642eca7.jpg)  
Figure 4: Probability Guidelines and Minimum HQ Requirements

# Probability of Encounter

The probability of encountering adverse environmental factors is another important consideration when evaluating the suitability of flying qualities and workload of a real aircraft. It would appear that the probability of encountering certain environments can be treated in a way that is similar to the treatment of failure modes as addressed in References 6, 7, 8 and 9.

In this regard, McElroy does an excellent job in Reference 10 of addressing and the probability of simultaneously encountering specific levels of atmospheric disturbance and failure states in context with flight envelopes. Figure 4 has been reproduced from Reference 10 as it is an excellent summary of the author's concept. In support of this figure, the author observes that the FAA could use subjective pilot ratings (from a scale like that in Figure 1) to determine compliance with the criteria "satisfactory," "adequate," and "controllable" (Figure 4), an idea which is still new to much of the FAA.

# Analyzing Environmental Effects

Plotting pilot rating data as a function of one or more variables will often help the analyst develop the highest degree of confidence in the data. This concept is demonstrated in Reference 11 which presents a family of six data plots (one each for 5, 10, 15, 20, 25, 30 knots of wind), two of which are characterized in Figure 5. Observe that pilot ratings are plotted as a function of azimuth for two wind speeds.

Note that pilot ratings vary as a function of both wind speed and azimuth. Although not shown, the ratings can also vary as a function of gross weight, power available, center of gravity, rotor RPM, turbulence, visibility, lighting, and a host of other variables. If you inspect the 5 and 15 knot data for the wind azimuth of $300^{\circ}$ , you will note that the pilot rating changes from a respectable PR 3 at 5 knots of wind to a relatively poor rating of PR 5 at 15 knots. But why? The pilots comments should provide the best insight. This is a clear demonstration of the need for pilot comments.

图片摘要：该图主要展示 5: Handling Qualities For Various Wind Azimuth Angles (Pre l。
![](images/22d7594eac04f3ea50c9677fd470cca79d430b340570312183a1f79fd17ee33a.jpg)  
Figure 5: Handling Qualities For Various Wind Azimuth Angles (Pre-landing hover) Over Deck of Small Ships

# Evaluating Simulation Facilities

Pilot ratings can also be used to evaluate the authenticity of a simulator. One way to check the authenticity of the simulation is to ask the crews to evaluate (or interpret) the simulator visual and motion systems while simulating an aircraft with which they are familiar.

To illustrate this application, the results of a hypothetical simulator evaluation are presented here as Figure 6. This figure contains the possible result of a day flight and a night flight in an existing helicopter followed by an attempt to replicate the real world test conditions in a ground based simulator. The data shown for "Bright Day - Actual Flight" in this figure is taken directly from Figure 5. In this illustration, the pilot's "actual flight" PRs and "simulated flight" PRs are approximately equal for the dark night case, but the data for the bright day case reveals a significant disagreement. The comments accompanying the pilot's ratings should confirm the ratings and provide insight into the probable cause. Depending upon the comparative evaluation of the pilot's control activity and overall performance, the findings would seem to suggest that the visual representation lacked adequate authenticity in the "bright day" case. In contrast, the dim, night scene was adequate. This is an important finding in and of itself.

The results of a second hypothetical evaluation are presented in Figure 7 which illustrates an alternative format for evaluating the authenticity of a simulator. In this case, the pilot first uses a real helicopter to conduct a demanding task in seven different, real world environments. The seven combinations have been plotted in ascending order for convenience.

When the same pilot attempts the identical task in the simulated environments (duplicated in the simulator), the pilot ratings should agree. If they do not agree, the pilots comments associated with each rating should provide useful data as to the cause of the difficulty.

That is, an analyses of pilot control activity, attitude error, flight path error, etc., should include an equally exhaustive analysis of pilot comments.

# Minimizing Variability In Ratings

Variance in PR data feeds the argument that the subjective rating approach can produce erroneous results. Cooper-Harper tell us to expect a limited amount of variability in ratings. Disparity in pilot background can produce variation in the pilot ratings. In addition, Cooper-Harper tell us that some pilots may be predisposed for or against a given configuration. In addition, some variability in PRs may simply reflect the presence of one or more factor(s) which were not accounted for in the definition of the experiment. That is, an important factor may not have been recorded.

Most of these sources of variability can be minimized through diligent planning. In particular, pilots and engineers are urged develop a table such as that included as Figure 3. Once the data are collected, presentations formats such as those suggested by Figures 5, 6 and 7 can help the analyst develop the best possible understanding of PR data and at the same time minimize the possibility of scatter in the data.

# Extrapolations

The CHPRS authors recognize that some would have pilots evaluate only the situation experienced (first hand) by the subject pilot. Others would have pilots use a simulator evaluation experience to predict/ extrapolate to the real world. For example, assume that during a landing experiment, employing an inflight simulator, the pilot evaluates the test configuration only on a clear, bright sunny day. The pilot could then be asked to rate only the situation flown, (clear day to a runway), or alternately, the pilot could be asked to extrapolate the clear day observations into a dark, wet night environment.

图片摘要：该图主要展示 6: Comparison Of Pilot Ratings To Evaluate A Simulation Faci。
![](images/ed5a88d9c5fb4992d43fb644420b8f9067edcd1e82eef143f27d76b1286aaea4.jpg)  
Figure 6: Comparison Of Pilot Ratings To Evaluate A Simulation Facility

图片摘要：该图主要展示 6: Comparison Of Pilot Ratings To Evaluate A Simulation Faci。
![](images/9c9fdf2836484a2a8a3f3f379f429c5b530c9ab020bac01778baacdbc5fd0eef.jpg)  
Figure 7: An Example Set of Progressively More Difficult Environmental Conditions Which Can be Evaluated in the Real World and Replicated in a Simulator to Collect Pilot Ratings for Evaluation of a Simulation Facility

A. Clear Day, Calm Air.   
B. Clear Day, 10 KT Rt Cross Wind.   
C. Clear Day, 10 KT Rt Cross Wind, Gusting to 17 KT   
D. Night, Full Moon, Stars,   
Landing & Hover Lights, 10 KT Rt Cross Wind, Gusting to 17 KT.   
E. Night, 1/4 Moon, Single Landing LT, 10 KT Rt Cross Wind, Gusting to 17 KT.   
F. Night, Overcast, no surface lights, single landing Lt, 10 KT Rt Cross Wind, Gusting to 17 KT.   
G. Night, Near Thunderstorm, 20 KT Wind, Gusting to 30 KT.

Cooper-Harper agree that a pilot can extrapolate this experience and provide a rating for an environment worse than that observed in a hands-on evaluation. This of course assumes that the pilot has acquired an adequate understanding of the aircraft and is familiar with the operational environment of interest. Cooper-Harper go on to ask the question "... if the pilot doesn't do it, who will?". They also go on to conclude that an experienced pilot is probably the best qualified to extrapolate simulator experience into the real world.

The same ability to extrapolate has been recognized and utilized in the military and FAA evaluations of aircraft for at least forty years. That is, an experienced pilot is often asked to conclude in a few flights, that a given aircraft is, or is not, suitable for flight into instrument conditions without ever flying into instrument conditions. Regardless of the approach taken, the pilot and engineer should agree on which approach they will use and this selection should be reported with the data. This note of caution is supported by Harper and Cooper in Reference 1.

# WORKLOAD AND INTEGRATED EVALUATIONS

With the increased use of computer based systems, the pilot's task has shifted more and more towards the overall flight management function. In minimum crew

(one or two place) military combat aircraft, these system advances have added to the mission system functions over which the pilot has direct control. For military aircraft, the same technology advances have greatly expanded the functions of non-pilot air crew mission system operators - and increased the thrust towards the use of a minimum crew.

On the civil side, there is the potential of single pilot IFR helicopter operations, including approaches to busy airports and slow speed steep approaches into confined landing sites. These operations bring a similar concern for increased cockpit complexity and higher workload.

# Workload

These developments have increased the attention of specialists in human task performance to the measurement of pilot and air crew workload, with recognition that in-flight measurement is needed to fully characterize the actual experience. Issues of objective vs. subjective measurement have received continuing attention in this field as elaborated in References 12 and 13. Due to the complexity of the total in-flight workload and the intrusiveness of available objective measurement techniques, there has been increasing acceptance of and support for subjective measurement.

图片摘要：该图主要展示 8: Modified Cooper Harper Scale。
![](images/72c24bec7cee5b46877477c1fbf1834781d4430d6ab509f3cde13d926d07ffe5.jpg)  
Figure 8: Modified Cooper-Harper Scale

Subjective measurements schemes that have been evaluated (Reference 14) indicate that some of them, while useful in laboratory investigations of pilot or operator workload, are quite cumbersome and too time consuming in ground based flight simulator or in-flight use. Chambers and Hilmer in Reference 14 clearly show the advantages of Weirwille's proposed Modified Cooper-Harper Rating Scale (MCHRS) (Figure 8) for workload assessment in both piloting and non-piloting tasks in these applications. The brief treatment in that paper, however, does not go on to point out other benefits of its use for these applications.

For example, the familiarity of engineering test pilots, simulation staff and flight test engineering personnel with the CHPRS provides a direct carry over to use of the MCHRS. This should allow its use in both workload measurement per se and in the evaluation of non-piloting flight management and mission systems, either individually or as part of the integrated overall pilot/pilot and mission specialist task. In the case of these applications, strictures similar to those which accompany the CHPRS would have to be developed. This would including the need for subject comments similar to those provided by pilots in the CHPRS.

# Need For Single Integrated Rating

While separate assessments of handling qualities and workload can be useful in research investigations, for example Reference 15 contains the results of one such effort, this approach fails to give the decision maker a readily usable answer regarding operational suitability.

Decision makers need an overall rating which reflects the total suitability of the aircraft to accomplish its mission when operated by the typical air crew for which the aircraft was designed. For civil aircraft, FAA certification is the final go/no go decision. For military aircraft, the formal Operational Evaluation is the final stamp. But the use of the CHPRS to primarily evaluate flying qualities (with consideration of flying and CM workload inferred) and the use of the MCHRS as a sub-set to the CHPRS to evaluate workload, does not provide the desired single rating. It also fails to deal with comparative priorities (e.g., the flying task vs. the CM task). Another approach is needed.

# INTERPRETED COOPER-HARPER PILOT RATING SCALE

# Introduction

The preceding discussion has suggested that there is a need to apply the CHPRS more broadly while observing the strictures more diligently. This includes the need for a scale which is easier for operational pilots to use and which treats workload a bit more directly. This need includes both flying and the nonflying, cockpit management workload and the related priorities. In addition, there is the need to define half pilot ratings.

An example of how all of this might be accomplished is presented in Figure 9. The Interpreted Cooper-Harper Pilot Rating Scale (ICHPRS), as addressed here, is meant to have the same meaning as the original CHPRS of References 1 and 4. The concept also applies to the entire scale, but a complete treatment is beyond the scope of this paper. When compared to the CHPRS in Figure 1, it is quickly obvious that the first "pilot decision" steps are not included in Figure 9. In military version of this scale, these pilot decisions steps would be retained. In the civil version, they might not be retained (as suggested in Reference 16).

# Half PRs

As discussed earlier, half PRs accomplish two objectives. First, they allow pilots to evaluate a condition or situation which does not meet the definition of a whole number in the CHPRS. Second, the half ratings allow the pilot or analyst to build a higher degree of confidence as to where the boundaries of interest are located. But the CHPRS does not provide definitions and, depending upon the application, this can represent a serious problem.

In contrast, the ICHPRS does include definitions for half ratings. These half ratings relate to the preceding whole integer rating and not to the subsequent rating. The logic of this approach is more apparent when one considers the transition between PRs of 3 and 4, and the PRs of 6 and 7 (especially when considering many of the military applications). Civil evaluators may draw the lines of suitability elsewhere with the same concern.

# "Use Unique" Interpretative Narrative

The narrative in Figure 9 is meant to suggest an approach, not "the only" or "the recommended" approach. In most cases, the narrative in the ICHPRS should be developed by one or more engineering test pilot(s) and engineer(s) familiar with the test aircraft, its operational characteristics, and its operational requirements. This should produce one or more aircraft-mission unique scale(s), depending upon the scope of the evaluation.

The added descriptors might evolve during the initial shake down of an aircraft or during a familiarization period in the aircraft or in a simulator (if a real aircraft is not available). In any event, the use of a trained engineering test pilot, familiar with the Cooper-Harper scale, is strongly recommended.

Note that the descriptions under "Aircraft Characteristics" in Figure 9 are identical to those found in the CHPRS presented in Figure 1. The narrative under "To Achieve the best attainable performance" has two parts. The first part (left column) repeats the descriptions found in the CHPRS. The second part (right column) is split into two horizontal boxes. These two boxes contain the interpretive narrative for one whole PR and the associated

half pilot rating. Note that this second column contains comments relating to both flight control and CM tasking, including indications of priority and performance.

The final column (under Representative Observations) amplifies the preceding descriptions of the pilot effort required by characterizing performance in terms of operational suitability. Here, examples are provided to aid the pilot in efforts to discriminate. As described in References 1 and 4, failure to meet the intent of any specific rating forces the pilot to assign the next higher rating.

Performance. Performance objectives must be defined prior to commencing an evaluation. These objectives must relate to tasks for which the pilot expects to achieve minimum error, or for situations where the pilot desires to maximize time out of the loop to rest or to conduct a CM task during which some amount of flight path error is acceptable. For example, this might characterize the shared monitoring of the aircraft's flight path and a mission equipment display.

In this regard, CM tasking could to be evaluated to determine the critical tasks and the procedures which apply. What CM tasks must be accomplished during high gain flight control events? This includes consideration of failure modes. For example, if an engine fails, is the pilot expected to continue the task

and deal with the emergency procedures, or does the pilot first transition to a new flight phase?

The interpretative narrative can include detailed references to performance expectations or objectives for both the flying and the CM tasks. That is, there is no reason why performance objectives should not be inserted in the narrative. It seems likely that this approach would reduce the potential for variance, but in some situations, this level of detail would probably not be necessary.

Definitions. Once the performance objectives have been defined, and the narrative has been drafted, definitions should be developed and supported with examples where required.

Performance Priority. The narrative in Figure 9 was developed with the idea that the flight path performance of the aircraft was the primary or critical objective. It is also possible to have situations where CM is of paramount concern. The narrative would be written appropriately for such flight phases to reflect these changing priorities. For example, it may be important accomplish an electronic warfare task in a very precise and timely way, while operating at altitudes and speeds which minimize concern for flight path error.

<table><tr><td rowspan="2" colspan="2">AIRCRAFT CHARACTERISTICS</td><td colspan="2">DEMANDS ON THE PILOT IN SELECTED TASK OR REQUIRED OPERATION *</td><td rowspan="2">PILOT **RATING</td></tr><tr><td>To Achieve the best attainable performance.</td><td>Representative Observations</td></tr><tr><td rowspan="2">Minor, But Annoying Characteristics</td><td rowspan="2">Desired performance requires moderate pilot compensation.</td><td>Pilot must concentrate on flight path errors. CM tasks are accomplished following standard procedures.</td><td>Occasional relaxed control is possible, but workload sometimes results in unwanted deviation. Pilot is impatient and fatigued during extended operations.</td><td>4</td></tr><tr><td>Pilot must concentrate on flight path errors. CM procedures are altered to accommodate reduced pilot capacity to monitor cockpit status.</td><td>Relaxed control is unachievable. Considerable compensation sometimes required. Pilot quickly impatient, quickly fatgued. Not accepted as the norm for the duration of routine or probable flight.</td><td>4.5</td></tr><tr><td rowspan="2">Moderately Objectionable Characteristics</td><td rowspan="2">Adequate performance requires considerable pilot compensation.</td><td>Pilot attention is fully focused on early error detection. Pilot is often unable to effectively plan and execute cockpit management tasking in accordance with standard procedures.</td><td>Performance is marginal for a precision task and is not acceptable for routine or probable operations. Pilot does not have the time to adequately monitor status of CM tasking.</td><td>5</td></tr><tr><td>Concentration on error detection and compensation is intense, and approaching limit. Many cockpit management tasks are deferred, some are precluded.</td><td>Maximum acceptable compensation is required. Unusual attitude may develop while accomplishing CM task. Pilot is confident of success during 15 min precision and 120 min of improbable operations pursuing a non-precision.</td><td>5.5</td></tr><tr><td rowspan="2">Very Objectionable But Tolerable Characteristics</td><td rowspan="2">Adequate performance requires extensive pilot compensation.</td><td>Concentration on flying task is at limit. Critical CM activities are accomplished randomly, as opportunities arise during momentary improvement in flying task performance.</td><td>Excessive pilot compensation is required to continue marginally safe operations for 5 min in precision task and 30 to 60 min in non-precision tasks. Pilot is occasionally alarmed at combinations of error, error buildup rate and total workload.</td><td>6</td></tr><tr><td>Concentration on flying task is at limit. Adequate flight performance can not be attained if any CM tasking is undertaken.</td><td>Compensation is at limit. Acceptable performance will probably only be achieved during very brief periods ranging from seconds to a minute. Pilot will persist only if there is no safer alternative. Aircraft will probably not be damaged is pilot persists. If pilot attempts CM task, aircraft may incur minor damage.</td><td>6.5</td></tr></table>

* Definition of required operation involves designation of flight phase and sub-phases with accompanying conditions.   
** If a mission-flight critical cockpit management task can not be accomplished in a timely and effective way, the PR = 7.

Figure 9: An Example of Interpretive Narrative Added to a Portion of the Cooper-Harper Pilot Rating Scale

图片摘要：该图主要展示 9: An Example of Interpretive Narrative Added to a Portion o。
![](images/21ba49cad9d6db615513b0923d6f77bf7e41daa2b4e47f03c8ce05ffb241137f.jpg)  
Figure 10: NVG Pilot Rating Analysis Classifications

# NIGHT VISION TESTING BY FAA

This paper was in part made possible as the result of work funded by the FAA Rotorcraft Research Program Office in Washington, D.C., and accomplished in support of flight evaluations of night vision devices conducted by the Flight Test Division of the FAA Technical Center, Atlantic City International Airport, New Jersey. The objective of the evaluation was to provide an opportunity for a large number of civil and FAA pilots to fly with night vision goggles (NVGs) to determine their suitability for use by EMS operators.

This evaluation was chartered to use a group of civil helicopter pilots with dissimilar flying backgrounds to examine the safety of flight issues associated with the use of NVGs while operating in a variety of environments. For example, a variety of lighting environments and obstructions to visibility were of interest. None of the evaluation tasks involved Nap of the Earth (NOE) flying techniques.

As a result, a set of evaluation guides (booklets) were developed to help introduce pilots to the evaluation, and to help them understand an early ICHPRS. (References 17, 18, and 19). The interpreted pilot rating scale was meant to be faithful to the intent of the CHPRS. This project is currently underway and the results are yet to be documented. --- The current plan is to sort the pilot rating assessment data and compile the results for each task in a way which is

characterized above in Figure 10. This should provide decision makers with data they need to determine suitability in terms of pilot experience and environmental factors.

# CONCLUSIONS AND OBSERVATIONS

Cooper-Harper is an effective subjective assessment tool when applied in accordance with its creators full instructions. Extensive successful use in the past, and the evolving "test and approval decision processes" are areas where its effectiveness can be enhanced for current and future applications.

The ability of pilots to extrapolate pilot ratings is a well proven capability which is essential to safe, affordable and timely evaluation of aircraft and simulations of proposed aircraft designs.

A suitably tailored Interpreted Cooper-Harper Rating Scale as proposed will provide pilots not having an engineering test pilot background with an effective rating system for use in simulations and final operational evaluations.

The effectiveness of using Cooper-Harper in handling qualities evaluations, where workload is a factor in the assessment, strongly supports the use of a proposed Modified Cooper-Harper, appropriately adapted, in specific subjective workload assessment and non-pilot airborne system evaluations.

# REFERENCES

1. Harper, Robert P., Jr., and Cooper, George E., "Handling Qualities and Pilot Evaluation," J. Guidance, Control and Dynamics, Vol. 9, No. 5, Sept-Oct 1986   
2. Cooper, George E., "Understanding and Interpreting Pilot Opinion," Presented at the 25th Annual Meeting, Institute of the Aeronautical Sciences, 28-31 January 1957   
3. Cooper, George E., et al., "The Revised Pilot Rating Scale for the Evaluation of Handling Qualities," CAL Report No. 153, The AGARD Specialist's Meeting on Stability and Control, Cambridge, England, 20-23 September 1966   
4. Cooper, George E., and Harper, Robert P., Jr., "The Use of Pilot Rating in the Evaluation of Aircraft Handling Qualities," NASA TN D-5153, National Aeronautics and Space Administration, Washington, D.C., April 1969   
5. Green, David L., "Collecting Rotorcraft and Flight Simulator Data for the Purpose of Determining Transferability of Flight Simulator Experience," presented at the Helicopter Simulator Technology Workshop, NASA Ames Research Center, Moffett Field, CA., 24-26 April 1991   
6. "Handling Qualities Requirements for Military Rotorcraft," ADS-33C, U.S. Army Aviation Systems Command, St. Louis, MO., Aug '89   
7. Code of Federal Regulation Part 27, Appendix B, 1 January 1985   
8. Code of Federal Regulation Part 29, Appendix B, 1 January 1985   
9. Anon, Military Specification, Flying Qualities of Piloted Airplanes, MIL-F-8685B (ASG), Aug '69   
10. McElroy, Collet E., "FAA Handling Qualities Assessment - Methodology in Transition," Thirty-Second Symposium Proceedings, Oct '88   
11. Kolwey, Herman G., "Analysis Tools Derived from Investigating Aerodynamic Loss of Tail Rotor Effectiveness (LTE)," presented at the Society of Flight Test Engineers 22nd Annual Symposium, August 1990   
12. "Assessing Pilot Workload," AGARD-AG-233, Advisory Group for Aerospace Research and Development, Paris/NATO, 1978   
13. "Survey of Methods to Assess Workload," AGARD-AG-246, Advisory Group for Aerospace Research and Development, Paris/NATO, 1979

14. Chambers, Randall M., Ph.D., and Kilmer, Kevin J., MA., "Choosing A Pilot Subjective Workload Scale To Fit Flight Operational Requirements," IAR 89-21 (N90-26493), The Wichita State University Institute for Aviation Research, Wichita, KS., October 1989   
15. Baillie, S., Kereliuk, S., and Hoh, R., "An Investigation of Lateral Tracking Techniques, Flight Directors and Automatic Control Coupling on Decelerating IFR Approaches for Rotorcraft," NAE-AN-55, NRC No. 29604, National Research Council, Canada, Oct '88   
16. Hoh, Roger H., and Mitchell, David G., "Flying Qualities of Relaxed Static Stability Aircraft - Volume I," DOT/FAA/CT-82/130-I, Final Report, U.S. Department of Transportation, Federal Aviation Administration, Sept '82   
17. Green, David L., "FAA Flight Test Engineer's Guide for Collecting and Evaluating Pilot Assessments of Workload and Performance While Operating with NVGs," First Draft, 10 June 1991   
18. Green, David L., "Evaluation Pilot's Guide (Part I) for Collecting Civil Helicopter Pilot Assessments of VFR En Route Operations Involving the Use of Helmet Mounted, Night Vision Devices," Second Draft, corrected 18 June 1991   
19. Green, David L., "Evaluation Pilot's Guide (Part II) for Collecting Civil Helicopter Pilot Assessments of VFR Approach and Departure Operations Involving the use of Helmet Mounted, Night Vision Devices," Second Draft, corrected 29 October 1991

# IMPROVEMENTS IN HOVER DISPLAY DYNAMICS FOR A COMBAT HELICOPTER

Jeffery A. Schroeder

Aerospace Engineer

NASA Ames Research Center

Moffett Field, California

Michelle M. Eshow

Aerospace Engineer

Aeroflightdynamics Directorate

U.S. Army ATCOM

Moffett Field, California

# ABSTRACT

This paper describes a piloted simulation conducted on the NASA Ames Vertical Motion Simulator. The objective of the experiment was to investigate the handling qualities benefits attainable using new display law design methods for hover displays. The new display laws provide improved methods to specify the behavior of the display symbol that predicts the vehicle's ground velocity in the horizontal plane; it is the primary symbol that the pilot uses to control aircraft horizontal position. The display law design was applied to the Apache helmet-mounted display format, using the Apache vehicle dynamics to tailor the dynamics of the velocity predictor symbol. The representations of the Apache vehicle used in the display design process and in the simulation were derived from flight data. During the simulation, the new symbol dynamics were seen to improve the pilots' ability to maneuver about hover in poor visual cuing environments. The improvements were manifested in pilot handling qualities ratings and in measured task performance. The paper details the display design techniques, the experiment design and conduct, and the results.

# NOTATION

$A_{x}$ acceleration cue longitudinal position, deg (degrees refer to angle subtended at pilot's eye) $A_{y}$ acceleration cue lateral position, deg $\text{Error}_{\text{north}}$ vehicle earth-axis position error northward, ft $\text{Error}_{\text{east}}$ vehicle earth-axis position error eastward, ft $f_{i}(s)$ sensor equalization filter on signal i $g$ gravity constant, ft/sec² $K_{x}$ display longitudinal conversion factor for hover box, deg/ft

<table><tr><td>Ky</td><td>display lateral conversion factor for hover box, deg/ft</td></tr><tr><td>Kx</td><td>display longitudinal conversion factor for velocity vector, deg/ft/sec</td></tr><tr><td>Ky</td><td>display lateral conversion factor for velocity vector, deg/ft/sec</td></tr><tr><td>Lδa</td><td>vehicle derivative of applied specific rolling moment due to lateral cyclic, rad/sec2/in.</td></tr><tr><td>Mδb</td><td>vehicle derivative of applied specific pitching moment due to longitudinal cyclic, rad/sec2/in.</td></tr><tr><td>Px</td><td>hover box longitudinal position, deg</td></tr><tr><td>Py</td><td>hover box lateral position, deg</td></tr><tr><td>p</td><td>vehicle body-axis roll rate, rad/sec</td></tr><tr><td>q</td><td>vehicle body-axis pitch rate, rad/sec</td></tr><tr><td>s</td><td>Laplace operator</td></tr><tr><td>Vnorth</td><td>northward component of vehicle groundspeed, ft/sec</td></tr><tr><td>Veast</td><td>eastward component of vehicle groundspeed, ft/sec</td></tr><tr><td>Vx</td><td>velocity vector longitudinal position, deg</td></tr><tr><td>Vy</td><td>velocity vector lateral position, deg</td></tr><tr><td>x</td><td>vehicle longitudinal position, ft</td></tr><tr><td>xcmd</td><td>commanded vehicle longitudinal position, ft</td></tr><tr><td>x</td><td>longitudinal heading referenced groundspeed, ft/sec</td></tr><tr><td>xfilt</td><td>filtered longitudinal groundspeed, ft/sec</td></tr><tr><td>xcomp</td><td>complementary filtered longitudinal acceleration, ft/sec2</td></tr><tr><td>xfilt</td><td>estimated longitudinal acceleration, ft/sec2</td></tr><tr><td>Xu</td><td>vehicle longitudinal velocity damping, 1/sec</td></tr><tr><td>y</td><td>lateral heading referenced groundspeed, ft/sec</td></tr><tr><td>yfilt</td><td>filtered lateral groundspeed, ft/sec</td></tr><tr><td>ycomp</td><td>complementary filtered lateral acceleration, ft/sec2</td></tr><tr><td>yfilt</td><td>estimated lateral acceleration, ft/sec2</td></tr><tr><td>Yv</td><td>vehicle lateral velocity damping, 1/sec</td></tr><tr><td>δa</td><td>pilot lateral cyclic control position, in.</td></tr></table>

<table><tr><td>δb</td><td>pilot longitudinal cyclic control position, in.</td></tr><tr><td>ζ</td><td>damping ratio</td></tr><tr><td>θ</td><td>vehicle Euler pitch angle, rad</td></tr><tr><td>θ&#x27;</td><td>vehicle Euler pitch rate, rad/sec</td></tr><tr><td>φ</td><td>vehicle Euler roll angle, rad</td></tr><tr><td>φ&#x27;</td><td>vehicle Euler roll rate, rad/sec</td></tr><tr><td>ψ</td><td>vehicle heading angle, rad</td></tr><tr><td>ω</td><td>natural frequency, rad/sec</td></tr></table>

# INTRODUCTION

A significant effort at Ames Research Center has aimed at developing and flight testing display law design methods for the hover flight regime. The flight experiment of Ref. 1 documented the influence of display dynamics on handling qualities for near-hover maneuvering; the Ref. 2 flight experiment examined the relative merits of two pilot-oriented design goals for the display dynamic response. Both experiments employed a cockpit panel-mounted representation of the AH-64 Pilot Night Vision System (PNVS) symbology (Ref. 3), which is shown in Figure 1. The flight experiment of Ref. 4, following many years of simulation research, examined control and display requirements for VTOL translation, hover, and landing, using an Ames-designed symbology format.

The common theme for all the experiments was the use of a velocity predictor symbol (called the acceleration cue in Figure 1). The emphasis of the research was placed on the specification of that symbol's dynamics. When used with the hover position symbol and the velocity vector, the acceleration cue is the pilot's primary controlled element for regulation of vehicle horizontal position. Although the acceleration cue predicts future horizontal velocities, it is used primarily in combination with another symbol that indicates a desired vehicle horizontal position, to control vehicle horizontal position. For helicopters with angular rate stabilization only, the resulting aircraft position dynamics are difficult to control, as there are approximately three integrations from pilot input to aircraft position response. This separation of the pilot from the vehicle state of interest presents a handling qualities challenge to the display designer. As will be described subsequently, the acceleration cue response to pilot control input must be designed considering the vehicle dynamics and the task requirements to maximize handling qualities and mission effectiveness.

The lessons learned from the three flight experiments provided the foundation for the flight investigation of Ref. 5, whose objectives were 1) to design new display laws tailored specifically to the Apache vehicle dynamics and 2) to compare the resulting handling qualities with those of the existing Apache display laws. While the first objective was achieved, the second was not because the documented representation of the existing Apache display laws used in the flight comparison was not correct. The correct display laws were obtained subsequently, and potential improvements were then shown analytically.

Since that experiment, as will be described, flight data documenting the Apache vehicle response characteristics were obtained that permitted the identification of high-quality design and simulation models. The nature of the identified vehicle response necessitated an extension of the display law design methods described in Ref. 2 and Ref. 4. Thus, the motivation for the simulation experiment described here was to examine the potential benefits of the extended design methods using an improved representation of the Apache vehicle and of its baseline display responses. The following sections detail the display law design methods, the simulation design and conduct, and the results.

# DISPLAY LAW DESIGNS

The term "display laws" refers to the equations and scaling that determine the position of the central symbology, namely the acceleration cue, velocity vector, and hover position box (Figure 1). During hover maneuvering using primarily the symbology, the acceleration cue becomes the pilot's primary controlled element. To achieve a hover over the position box, he moves his stick to place the cue on the box, and he maintains it there as the box converges to the display center. The pilot workload to maintain the cue on the box, and the nature of the resulting vehicle trajectory, are the two issues that most impact the design of the acceleration cue dynamics.

These considerations are illustrated in Figure 2, which presents a block diagram of the pilot-vehicle-display system for the case where the pilot is attempting to zero the longitudinal displayed error between the hover box and acceleration cue. The ease of controlling the acceleration cue's position on the display is determined by the transfer function $A_{x} / \delta_{b}$ , which in turn is determined by the cue's response to each of the aircraft states that drive it.

Given any particular set of dynamics for the cue response to control, the trajectory that the aircraft follows while the pilot maintains the cue on the hover box is determined by the closed loop response $x / x_{cmd}$ . This response must be tailored so that the trajectory is well-damped, with a bandwidth, or "aggressiveness," appropriate for the aircraft mission.

There is a tradeoff between the cue controllability, which affects the pilot workload, and the aircraft position response. In one extreme, the easiest cue to control would be one driven only by pilot control position; however, this would result in poor hovering performance. This problem has been referred to as poor "face validity" (Ref. 6). In the other extreme, the cue position could be driven to show the pilot control inputs required for a quick, well-behaved trajectory, probably resulting in complex control motions and high workload. Finally, the tradeoffs become more critical as the level of vehicle augmentation decreases, since stability margins deteriorate quickly.

图片摘要：该图主要展示 1 AH 64 Pilot Night Vision System symbology。
![](images/df17d21bc7632dcbbb53a5126438f1deda4cd186ed21f294d77127c60108301c.jpg)  
Fig. 1 AH-64 Pilot Night Vision System symbology.

图片摘要：该图主要展示 1 AH 64 Pilot Night Vision System symbology。
![](images/c9a5591fbb5e52481a80b3b69aa2a9edd08b0dce1675e441ee74b1ede23900ab.jpg)  
Fig. 2 Pilot-vehicle-display block diagram.

With these guidelines in mind, three methodologies for specifying display laws were examined for the experiment. After brief discussions of the vehicle dynamics model used for the display designs and of the baseline production display laws, a description of each design method is presented. Finally, all the display laws are compared analytically.

# Vehicle Design Model

To support the display law design, a mathematical model was needed of the AH-64 Apache (Figure 3) with its Digital Automatic Stabilization Equipment (DASE) on. Parameter identification techniques described in Ref. 7 were used to identify from flight data a low-order model for the

DASE-on vehicle near hover. The flight data were part of a larger AH-64 database generated by the Army at the Airworthiness Qualification Test Directorate (AQTD); the flight tests are described in Ref. 8.

The DASE-on design model has decoupled transfer functions with associated equivalent time delays for the longitudinal and lateral responses to pilot input. These were the only responses required for the display design. The following models were identified from flight data that exhibited

图片摘要：该图主要展示 3 AH 64 Apache。
![](images/38f30a3791f7ebc956650b527670455dab6a611c8bc825e79ed75a8604e2f8dc.jpg)  
Fig. 3 AH-64 Apache.

excellent coherence in the frequency range of interest (0.2 to 10 rad/sec):

$$
\frac {q}{\delta_ {b}} (s) = \frac {- 2 . 4 9 (s + 0 . 2 6 2)}{(s + 0 . 3 9 9) [ 0 . 8 0 5 ; 3 . 4 6 ]} e ^ {- 0. 1 0 3 s} \tag {1}
$$

$$
\frac {p}{\delta_ {a}} (s) = \frac {6 . 3 2}{[ 0 . 5 8 2 ; 4 . 2 9 ]} e ^ {- 0. 0 4 2 5 s} \tag {2}
$$

where the shorthand notation indicates the second order system $[\zeta ;\omega ] = s^2 +2\zeta \omega s + \omega^2$ .Note that these high-order rate responses approximate, over the fitted frequency range, the combined dynamic effects of the unaugmented vehicle and its limited-authority augmentation system. Previously, two of the display design methods had been applied to only first-order rate responses; those methods had to be extended to accommodate these high-order identified responses.

# Production Display Laws

The PNVS display mode of interest for this study is the Bob-Up mode, which includes the velocity vector, acceleration cue, and hover box symbols. The symbol deflection definitions are shown in Figure 4. Based on unpublished documentation provided by the manufacturer and by the Army's program management office, the equations governing the movement of each symbol are next described.

# Hover Position Box

In the current production version of the PNVS software, the hover box is an octagon drawn and scaled to have an edge-to-edge width of 8 ft. It is driven relative to the fixed reticle by the heading-referenced, Earth-axis position error to a pilot-selected point:

$$
P _ {x} = K _ {x} \left(E r r o r _ {\text {n o r t h}} \cos \psi + E r r o r _ {\text {e a s t}} \sin \psi\right) \tag {3}
$$

$$
P _ {y} = K _ {y} \left(- E r r o r _ {\text {n o r t h}} \sin \psi + E r r o r _ {\text {e a s t}} \cos \psi\right) \tag {4}
$$

Here, the errors equal the desired position minus the current position, and the desired position is the one existing

图片摘要：该图主要展示 4 Definitions of central symbology deflections。
![](images/79c336762adf6a3a565aa869fd194804c8e5d05959da244f89390f7db48c4b00.jpg)  
Fig. 4 Definitions of central symbology deflections.

when the Bob-Up mode was selected. The hover box moves opposite to the aircraft motion to show the relative location of the desired position. To re-initialize the box to the current vehicle position, centered on the fixed reticle, the pilot deselects then reselects the Bob-Up mode. The scale factors $K_{x}$ and $K_{y}$ are required to convert feet to display displacement, such that full-scale deflection of the center of the box is ±44 ft. The full-scale deflection point is such that the outer edge of the box is just below the heading tape. The values of $K_{x}$ and $K_{y}$ were 0.241 deg/ft, where the degrees refer to the angle of display displacement subtended, on the PNVS monacle, at the pilot's eye.

# Velocity Vector

The velocity vector tip location relative to the fixed reticle is calculated as follows:

$$
\dot {x} = V _ {\text {n o r t h}} \cos \psi + V _ {\text {e a s t}} \sin \psi \tag {5}
$$

$$
\dot {y} = - V _ {\text {n o r t h}} \sin \psi + V _ {\text {e a s t}} \cos \psi \tag {6}
$$

$$
\dot {x} _ {f i l l} (s) = \frac {1}{(s + 1)} \dot {x} (s) \tag {7}
$$

$$
\dot {y} _ {f i l t} (s) = \frac {1}{(s + 1)} \dot {y} (s) \tag {8}
$$

$$
V _ {x} = K _ {\dot {x}} \dot {x} _ {f i l t} \tag {9}
$$

$$
V _ {y} = K _ {y} \dot {y} _ {f i l t} \tag {10}
$$

Where $K_{\dot{x}}$ and $K_{\dot{y}}$ are again scale factors to convert ft/sec to degrees of display displacement. They have the value of 1.03 deg/ft/sec so that the full scale deflection of the vector represents 12.0 ft/sec (7.13 knots). The velocity vector's full-scale deflection point on the display is 15% beyond that of the hover box, or midway into the heading tape.

# Acceleration Cue

The acceleration cue center relative to the fixed reticle is calculated as follows:

$$
\ddot {x} _ {\text {f i l t}} (s) = \frac {s}{s ^ {2} + 2 s + 1} \dot {x} (s) - \frac {3 2 . 2 (s + 2)}{s ^ {2} + 2 s + 1} \dot {\theta} (s) \tag {11}
$$

$$
\ddot {y} _ {f i l t} (s) = \frac {s}{s ^ {2} + 2 s + 1} \dot {y} (s) + \frac {3 2 . 2 (s + 2)}{s ^ {2} + 2 s + 1} \dot {\phi} (s) \tag {12}
$$

$$
A _ {x} = K _ {\dot {x}} \left(\dot {x} _ {f i l t} + 1. 5 0 7 \ddot {x} _ {f i l t} - 3. 0 1 3 \dot {\theta}\right) \tag {13}
$$

$$
A _ {y} = K _ {\dot {y}} \left(\dot {y} _ {f i l t} + 1. 5 0 7 \ddot {y} _ {f i l t} + 3. 0 1 3 \dot {\phi}\right) \tag {14}
$$

Thus the acceleration cue is driven relative to the tip of the velocity vector with an estimate of linear acceleration plus some lead compensation generated by the attitude rate terms.

The three new display design methods applied to the PNVS will next be described. It should be noted that for these new display laws, the display scalings of the three symbols remained invariant and equal to those of the production laws to preserve their operational significance and to provide a consistent basis of comparison among all the laws.

# Modified Production Display Laws

The first display law design method did not fully apply the techniques described in the introduction. Rather, it consisted of simply adjusting the gains on the acceleration and attitude rate terms in the production cue equations and the time constants of the velocity vector filter. The motivation for this design was to investigate whether simple changes in the existing equations, requiring no additional sensor information, would favorably impact handling qualities on AH-64's in the current fleet. The adjustments were made empirically based on a goal of improving the vehicle position trajectory response when the pilot is adopting the guidance strategy of placing the cue on the position box during the capture.

The transfer function of the controlled element, $A_{x}(s) / \delta_{b}(s)$ , that results for the production display laws has an underdamped complex pair of zeros in its numerator (at $-0.48 \pm \mathrm{j}0.66$ rad/sec). These underdamped zeros result from the interaction of the display feedbacks with the heavily filtered groundspeed signal. If the velocity filter breakpoint is moved from 1 rad/sec to 10 rad/sec, the underdamped complex zeros are eliminated. This modification to the sensor filtering alone would likely result in increased cue noise in flight. So in combination with the above filtering change, the gains on high-frequency inputs (accelerations and attitude rates) were lowered. The lowering of these gains was accomplished while trying to achieve vehicle-display dynamics having an integrator-like response to pilot input in the crossover frequency range (Ref. 9). This design was developed during the simulation, and the authors recognize that depending on sensor signal quality in the AH-64, increased gains could improve this cue's response. The final equations for the modified production design were as follows:

$$
\dot {x} _ {f i l t} (s) = \frac {1}{(0 . 1 s + 1)} \dot {x} (s) \tag {15}
$$

$$
\dot {y} _ {\text {f i l t}} (s) = \frac {1}{(0 . 1 s + 1)} \dot {y} (s) \tag {16}
$$

$$
V _ {x} = K _ {\dot {x}} \dot {x} _ {f i l t} \tag {17}
$$

$$
V _ {\mathcal {Y}} = K _ {\mathcal {Y}} \dot {y} _ {f i l t} \tag {18}
$$

$$
A _ {x} = K _ {\dot {x}} \left(\dot {x} _ {f i l t} + 1. 2 9 0 \ddot {x} _ {f i l t} - 0. 2 8 6 \dot {\theta}\right) \tag {19}
$$

$$
A _ {y} = K _ {\dot {y}} \left(\dot {y} _ {f i l t} + 0. 8 0 0 \ddot {y} _ {f i l t} + 0. 1 6 0 \dot {\phi}\right) \tag {20}
$$

with $\ddot{x}_{\text{filt}}$ and $\ddot{y}_{\text{filt}}$ defined in eqn. 11 and eqn. 12.

# Display Laws Based on Workload Design

The second design employed the philosophy developed in Ref. 2 with an extension of that methodology to treat the identified AH-64 aircraft dynamics. Entitled the "workload" design, this method seeks to reduce pilot workload by providing high-frequency proportional, or gain-like, response of

the acceleration cue to pilot input while also assuring desirable trajectory response. The handling qualities benefits of the gain-like response goal were established in the flight experiment of Ref. 2, which compared gain-like responses with integrator-like responses for hover maneuvering using the same display format.

In this method, a display law is specified for the cue in terms of a sum of compensated aircraft states and controls. The aircraft dynamics are then considered in order to define a desirable and achievable cue response to pilot control. This desired transfer function is next adjusted if necessary to achieve acceptable trajectory response. Then, the sensor compensation is determined that provides the desired cue response. The details of this approach are now described for the longitudinal and lateral axes.

# Longitudinal Axis Design

The general display law for this method, as extended for this application, is:

$$
A _ {x} (s) = f _ {\dot {x}} (s) \dot {x} (s) + f _ {\theta} (s) \theta (s) + f _ {q} (s) q (s) + f _ {\delta_ {b}} (s) \delta_ {b} (s) \tag {21}
$$

Where the $f_{i}$ 's represent the sensor signal compensation required to provide the desired cue response. Dividing by $\delta_{b}$ yields:

$$
\begin{array}{l} \frac {A _ {x}}{\delta_ {b}} (s) = f _ {\dot {x}} (s) \frac {\dot {x}}{\delta_ {b}} (s) + f _ {\theta} (s) \frac {\theta}{\delta_ {b}} (s) \\ + f _ {q} (s) \frac {q}{\delta_ {b}} (s) + f _ {\delta_ {b}} (s) \tag {22} \\ \end{array}
$$

For the desired gain-like cue response to pilot input above some frequency, this transfer function's numerator and denominator must be of equal order. The objective is to determine the order and parameter values for each filter to yield this gain-like cue response. The choices are also constrained by the requirement to provide good trajectory response dynamics. The relationship between the two can be seen by referring to Figure 2, where for high values of pilot gain, $K_{p}$ , the open-loop position transfer function may be approximated by:

$$
\frac {x}{x _ {c m d} - x} (s) \approx K _ {x} \frac {x / \delta_ {b}}{A _ {x} / \delta_ {b}} \tag {23}
$$

Thus, for fixed display position and velocity scalings and vehicle response, tailoring the cue response is the only means of assuring an acceptable closed-loop position response. The cue transfer function can be used, for example, to cancel unwanted dynamics in the vehicle position response to control input. Of course, this must be accomplished while still maintaining good cue controllability.

Next recall that the aircraft longitudinal response has the form (neglecting the transport delay):

$$
\frac {\theta}{\delta_ {b}} (s) = \frac {M _ {\delta_ {b}} (s + a)}{s (s + b) [ \zeta ; \omega ]} \tag {24}
$$

Substituting the aircraft responses into eqn. 22 with the approximations:

$$
\frac {\dot {x}}{\theta} (s) = \frac {- g}{s - X _ {u}} \tag {25}
$$

$$
q = \dot {\theta} \tag {26}
$$

yields

$$
\frac {A _ {x}}{\delta_ {b}} (s) = \left[ \text {t e r m s i n} \left(f _ {i}\right) \right] \frac {- g M _ {\delta_ {b}} (s + a)}{s (s + b) (s - X _ {u}) [ \zeta ; \omega ]} \tag {27}
$$

This relation is simply the unaugmented vehicle velocity response with added zeros (in the terms in $f_{i}$ ) that can be used to provide lead to the cue position dynamics.

For the overall transfer function to be proper, the transfer function in the brackets must have an excess of four zeros. In addition, it is desirable to cancel the attitude response's lead-lag pair from the trajectory response, to eliminate position overshoot. For these reasons, the following form is chosen for the cue response transfer function:

$$
\frac {A _ {x}}{\delta_ {b}} (s) = \frac {K _ {\delta_ {b}} (s + z _ {1}) (s + z _ {2}) (s + a) [ \zeta ; \omega ]}{s (s + b) (s - X _ {u}) [ \zeta ; \omega ]} \tag {28}
$$

where $K_{\delta_b}$ is a total gain that represents the high frequency cue sensitivity to control input. Note that two zeros are chosen to cancel the complex poles from the cue response, in order to simplify it. However, this means that they will be present in the trajectory response. This choice of zeros may not be appropriate for very poorly damped vehicles and should therefore be considered for each case. The placement of the zeros $z_1$ and $z_2$ determines the frequency at which the cue response becomes gain-like.

The numerator of eqn. 28 represents a fifth-order polynomial. Each of its terms must be taken with the denominator and considered separately to determine compensation terms $f_{i}$ that are realizable, that is, they must not result in pure differentiation of any sensor signal. Defining the denominator of eqn. 28 as $\Delta$ for convenience and rewriting the numerator as a fifth-order polynomial gives:

$$
\begin{array}{l} \frac {A _ {x}}{\delta_ {b}} (s) = \frac {K _ {\delta_ {b}} \left(a _ {1} s + a _ {0}\right)}{\Delta} + \frac {K _ {\delta_ {b}} \left(a _ {2} s ^ {2}\right)}{\Delta} \\ + \frac {K _ {\delta_ {b}} \left(a _ {3} s ^ {3}\right)}{\Delta} + \frac {K _ {\delta_ {b}} \left(s ^ {5} + a _ {4} s ^ {4}\right)}{\Delta} \tag {29} \\ \end{array}
$$

Now each of these terms can be equated respectively with the terms of eqn. 22 to determine the filters $f_{i}$ . For example, for the pitch rate term:

$$
\begin{array}{l} f _ {q} (s) = \frac {K _ {\delta_ {b}} \left(a _ {3} s ^ {3}\right)}{s (s + b) \left(s - X _ {u}\right) \left[ \zeta ; \omega \right]} \left(\frac {q}{\delta_ {b}} (s)\right) ^ {- 1} (30) \\ \approx \frac {K _ {\delta_ {b}} a _ {3} s}{M _ {\delta_ {b}} (s + a)} (31) \\ \end{array}
$$

$X_{u}$ was included for completeness until eqn. 31, where it has been approximated as zero. This is reasonable since for the Apache it was flight identified to be $-0.02\sec^{-1}$ . Thus, the pitch rate filter is a first-order washout. Repeating the process for each sensor input, the total cue drive law is then:

$$
\begin{array}{l} A _ {x} (s) = \frac {K _ {\delta_ {b}} \left(a _ {1} s + a _ {0}\right)}{- M _ {\delta_ {b}} g (s + a)} \dot {x} (s) + \frac {K _ {\delta_ {b}} a _ {2} s}{M _ {\delta_ {b}} (s + a)} \theta (s) \\ + \frac {K _ {\delta_ {b}} a _ {3} s}{M _ {\delta_ {b}} (s + a)} q (s) + \frac {K _ {\delta_ {b}} s ^ {2} (s + a _ {4})}{(s + b) [ \zeta ; \omega ]} \delta_ {b} (s) \tag {32} \\ \end{array}
$$

Based on iterative examination of the cue controllability and the resulting trajectory response and on preliminary piloted evaluations, the zeros $z_{1}$ and $z_{2}$ were chosen to be equal at -1.765 rad/sec. Once these were selected, the numerator polynomial could be computed. Finally, the gain $K_{\delta_b}$ was chosen such that $f_{\dot{x}}(s)$ has a steady state value of $K_{\dot{x}}$ , so that in the steady state the cue would rest at the tip of the velocity vector. Thus, the cue response transfer function was:

$$
\frac {A _ {\pi}}{\delta_ {b}} (s) = \frac {- 2 . 2 1 (s + 1 . 7 6 5) (s + 1 . 7 6 5) (s + 0 . 2 6 2)}{s (s + . 3 9 9) (s + 0 . 0 2)} \tag {33}
$$

The following represents the corresponding display law that was evaluated in the simulation:

$$
\begin{array}{l} A _ {x} (s) = K _ {\dot {x}} \left[ \frac {1 . 4 2 s + 0 . 2 6 2}{s + 0 . 2 6 2} \dot {x} (s) - 5 9. 3 \frac {s}{s + 0 . 2 6 2} \theta (s) \right. \\ - 3 2. 1 \frac {s}{s + 0 . 2 6 2} q (s) \\ - 2. 1 5 \frac {s ^ {2} (s + 9 . 3 6)}{(s + 0 . 3 9 9) [ 0 . 8 0 5 ; 3 . 4 6 ]} \delta_ {b} (s) \Bigg ] \tag {34} \\ \end{array}
$$

where now the display gain $K_{\dot{x}}$ has been factored out so that the terms in brackets are in physical units of ft/sec.

# Lateral Axis Design

A similar design procedure is followed for the lateral axis, but it is less complex because of the simpler vehicle response in this axis:

$$
\frac {\phi}{\delta_ {a}} (s) = \frac {L _ {\delta_ {a}}}{s [ \zeta ; \omega ]} \tag {35}
$$

This leads to a fourth-order numerator for the cue response transfer function:

$$
\frac {A _ {y}}{\delta_ {a}} (s) = \frac {K _ {\delta_ {a}} (s + z _ {1}) (s + z _ {2}) [ \zeta ; \omega ]}{s (s - Y _ {v}) [ \zeta ; \omega ]} \tag {36}
$$

which is then distributed among the sensor signals. Unlike $X_{u}$ , the derivative $Y_{v}$ cannot be cancelled with a numerator

free $s$ , since it was flight identified to be $-0.279\sec^{-1}$ . The resulting form for the lateral cue law is then:

$$
\begin{array}{l} A _ {y} (s) = \frac {K _ {\delta_ {a}} a _ {0}}{L _ {\delta_ {a}} g} \dot {y} (s) + \frac {K _ {\delta_ {a}} a _ {1} s}{L _ {\delta_ {a}} (s - Y _ {v})} \phi (s) \\ + \frac {K _ {\delta_ {a}} a _ {2} s}{L _ {\delta_ {a}} (s - Y _ {v})} p (s) \\ + \frac {K _ {\delta_ {a}} s ^ {2} (s + a _ {3})}{(s - Y _ {v}) [ \zeta ; \omega ]} \delta_ {a} (s) \tag {37} \\ \end{array}
$$

Again, after iterative examination to optimize the trajectory response, the two zeros and the gain $K_{\delta_a}$ were set such that the cue response transfer function for piloted evaluation was:

$$
\frac {A _ {y}}{\delta_ {a}} (s) = \frac {2 . 7 7 (s + 2 . 0 2 6) (s + 2 . 0 2 6)}{s (s + 0 . 2 7 9)} \tag {38}
$$

and the drive equation was:

$$
\begin{array}{l} A _ {y} (s) = K _ {\dot {y}} \left[ \dot {y} (s) + 4 0. 5 \frac {s}{s + 0 . 2 7 9} \phi (s) \right. \\ + 1 8. 2 \frac {s}{s + 0 . 2 7 9} p (s) \\ \left. + 2. 6 9 \frac {s ^ {2} (s + 9 . 0 5)}{(s + 0 . 2 7 9) [ 0 . 5 8 2 ; 4 . 2 9 ]} \delta_ {a} (s) \right] \tag {39} \\ \end{array}
$$

# Display Laws Based on Performance Design

The third design, based on a methodology developed in Ref. 4, is referred to as the "performance" design. It seeks to ensure good task performance but is balanced by pilot workload considerations. Besides this difference in emphasis, the workload and performance designs differ in the sensor signal distribution used to achieve the desired frequency response characteristics of the cue.

This method begins by selecting a desired transfer function of the vehicle's velocity response to be achieved when the pilot closes the control loop via the display. These dynamics represent how the velocity vector on the display would respond to the pilot maintaining the cue position at a fixed distance from the reticle (i.e., when the pilot is trying to establish a desired horizontal velocity). From Figure 2, if the pilot raises his gain high enough in the inner loop, then

$$
\frac {\delta_ {b}}{P _ {x}} (s) \approx \frac {\delta_ {b}}{A _ {x}} (s) \tag {40}
$$

Consequently, the inverse of the cue-to-stick dynamics may be used as series equalization with the open-loop, potentially poor vehicle velocity and position dynamics. If a desired vehicle velocity transfer function is selected, the cue-to-stick transfer function is

$$
\frac {A _ {\bar {x}}}{\delta_ {b}} (s) = K _ {\dot {x}} \frac {\dot {x}}{\delta_ {b}} (s) \Bigg | _ {A i r c r a f t} \times \left(\frac {\dot {x}}{\dot {x} _ {c}} (s)\right) ^ {- 1} \Bigg | _ {D e s i r e d} \tag {41}
$$

since $A_{x}$ is the pilot commanded velocity. The denominator of the cue-to-stick transfer function contains the dynamics of the open-loop aircraft so that when it is inverted by the pilot's high gain, the open-loop dynamics are effectively cancelled. These cancelled dynamics are replaced by the desired closed-loop velocity dynamics that are achieved when the pilot is controlling the vehicle in response to cue position errors.

For the AH-64, the velocity dynamics are (neglecting the identified delay from eqn. 1 and using eqn. 25)

$$
\frac {\dot {x}}{\delta_ {b}} (s) = \frac {- 2 . 4 9 g (s + 0 . 2 6 2)}{s (s + 0 . 0 2) (s + 0 . 3 9 9) [ 0 . 8 0 5 ; 3 . 4 6 ]} \tag {42}
$$

In order for $A_{x} / \delta_{b}$ to have a gain-like response at high frequencies, its numerator and denominator should be of the same order. Thus, the desired $\dot{x}_c / \dot{x}$ transfer function should be 4th over a 0th order. To prevent any velocity overshoot in the desired response, all of the roots in the desired velocity transfer function were placed on the real axis in the complex plane. The four equal roots were selected at -2.5 rad/sec. The selection of these roots is empirical but is based on some important points. First, the roots should be selected such that the high frequency gain of the cue to pilot inputs (of eqn. 41) is within a desired sensitivity range. If the roots of the desired velocity transfer function are all at low frequency, the high-frequency gain will be too high for a given velocity vector scaling gain. Second, the roots should be at a low enough frequency so that some immediate response to stick input occurs in the 1-10 rad/sec range. Third, as the roots move lower in frequency, the gains on the feedback signals in the display laws tend to increase.

For the design in this experiment,

$$
\frac {A _ {x}}{\delta_ {b}} (s) = K _ {\dot {x}} \frac {\dot {x}}{\delta_ {b}} (s) \Bigg | _ {A i r c r a f t} \times \frac {(s + 2 . 5) ^ {4}}{(2 . 5) ^ {4}} \tag {43}
$$

This controlled-element transfer function then needs to be distributed among the aircraft states rather than depending solely on pilot input. If the cue position is treated as the commanded velocity, $K_{\dot{x}} \dot{x}_{c}$ , then

$$
\begin{array}{l} A _ {\dot {x}} (s) = K _ {\dot {x}} \frac {\dot {x} _ {c}}{\dot {x}} (s) \Bigg | _ {\text {d e s i r e d}} \dot {x} (s) (44) \\ = K _ {\dot {x}} \dot {x} + K _ {\dot {x}} \left[ \frac {(s + 2 . 5) ^ {4}}{(2 . 5) ^ {4}} - 1 \right] \dot {x} (45) \\ = K _ {\dot {x}} \dot {x} + 1. 6 K _ {\dot {x}} \ddot {x} c o m p \\ + K _ {\dot {x}} \left[ \frac {s \left(s ^ {2} + 1 0 s + 3 7 . 5\right)}{(2 . 5) ^ {4}} \right] \ddot {x} (46) \\ \end{array}
$$

$$
\begin{array}{l} = K _ {\dot {x}} \left[ \dot {x} + 1. 6 \ddot {x} _ {c o m p} + \frac {- 2 . 4 9 g s (s + 0 . 2 6 2)}{(2 . 5) ^ {4} (s + 0 . 0 2)} \right. \\ \left. \times \frac {(s ^ {2} + 1 0 s + 3 7 . 5)}{(s + 0 . 3 9 9) [ . 8 0 5 ; 3 . 4 6 ]} \delta_ {b} \right] \tag {47} \\ \end{array}
$$

In the steady state, the cue indicates the scaled velocity $K_{\dot{x}} \dot{x}$ . A gained acceleration term and a 4th over a 4th order washout filter is on the stick. This high order filter indicates that a large portion of the cue response is generated from stick input, which is pure prediction based upon the known open-loop helicopter velocity response and a distributed portion of the desired velocity response. The simulation showed that the sensitivity of this stick term in the cue response for aircraft changes (across the vehicle operational weight and inertia envelope) was acceptable.

The development in the lateral axis is identical. Here the desired velocity roots are -2,-2, and [0.582;4.29]. The complex zeros were chosen to cancel the high frequency lightly damped roll axis natural response in the $A_y / \delta_a$ transfer function. Otherwise, a slight oscillation at the under-damped roll mode would appear in the cue response to pilot input. This jitter was a problem early in the simulation, and the proper placement of the zeros eliminated it. Using the same development as in the longitudinal axis, the lateral axis cue response is

$$
\begin{array}{l} A _ {y} (s) = K _ {\dot {y}} \left[ \dot {y} + 1. 2 5 \ddot {y} _ {c o m p} + \frac {6 . 3 2 g s}{(2) ^ {2} (4 . 2 9) ^ {2} (s + 0 . 2 7 9)} \right. \\ \left. \times \frac {\left(s ^ {2} + 9 . 0 7 s + 4 2 . 9\right)}{\left[ 0 . 5 8 2 ; 4 . 2 9 \right]} \delta_ {a} \right] \tag {48} \\ \end{array}
$$

The quantities $\ddot{x}_{comp}$ and $\ddot{y}_{comp}$ are complementary filtered values. They are comprised of low frequency accelerometer measurements and high-frequency attitude-rate inputs. This filtering attenuates vibratory accelerometer measurements and cuts off the immediate accelerations due to rotor flapping from stick inputs. These immediate accelerations contribute to noise and are not useful in the pilot-vehicle-display crossover frequency range. The filters are

$$
\ddot {x} _ {\text {c o m p}} = \frac {1}{s + 1} \ddot {x} - \frac {g s}{(s + 1) (s + 0 . 0 2)} \dot {\theta} \tag {49}
$$

$$
\ddot {y} _ {\text {c o m p}} = \frac {1}{s + 1} \ddot {y} + \frac {g s}{(s + 1) (s + 0 . 2 7 9)} \dot {\phi} \tag {50}
$$

Comparison of Display Laws and Task Performance Prediction

The analytical frequency responses for the four longitudinal-axis acceleration cues are presented in Figure 5. First, it is seen that the performance and workload designs are nearly identical, though they were developed independently. The gain-like characteristics are apparent above

about 2 rad/sec. The other two designs roll off rapidly above this frequency. In the mid-frequency range around 1 rad/sec, the performance and workload designs have roughly K/s characteristics. The modified production design has more phase lag than the production design in the mid-frequency region, but has better damping characteristics as discussed in the design section. The lateral axis frequency responses, when plotted, show similar trends.

The effect of these differences on task performance can be shown analytically by again referring to Figure 2. The pilot gain was set to 0.3 in/deg, and the control limit was set to $\pm 5$ in. The selected pilot gain resulted in crossover frequencies in the inner loop of Figure 2 to be between 2 and 3 rad/sec for each display cue law. The position loop was closed for each design and then driven with a step position command of 10 feet. The resulting vehicle trajectory and the control inputs required to achieve those trajectories are shown in Figure 6 for all four cue designs. It is seen that the position trajectories for the workload and performance designs are well-damped and relatively smooth. The modified production design is damped but not as smooth, while the production design is oscillatory with undershoot. Regarding the control inputs, the workload and performance traces

图片摘要：该图主要展示 5 Analytical frequency responses of four longitudinal cues。
![](images/f0f7fb3cf9a5148ecded515fb5e8552deb024d8f7cb3944db05ea3ed11b9180f.jpg)

图片摘要：该图主要展示 5 Analytical frequency responses of four longitudinal cues。
![](images/a91723e79030d4f66d40dd4b169c650ae693b7608c7e6746e1b3d17aa4605ff2.jpg)  
Fig. 5 Analytical frequency responses of four longitudinal cues.

show one control reversal, the modified production design shows significant oscillation, and the production design has some oscillation and is generally complex.

Based on these analyses, it could be predicted that the workload and performance designs would yield both the best performance and lowest workload, the modified production design the third best performance and the production design the poorest performance. The piloted assessments of relative workload for the modified production and production designs is difficult to predict from the traces.

The Bode plots for the workload and performance designs show the gain-like characteristics extending indefinitely to high frequency. Although noise is generally not a factor in simulation, in a flight environment the cue response must be attenuated to prevent sensor and pilot control-induced noise from passing through to the cue, causing it to jitter on the display. Therefore, for completeness of the experiment, a first-order 10 rad/sec filter was placed on the total cue displacements $A_{x}$ and $A_{y}$ before they were sent to the display. This was done for the performance and workload designs only, since the other designs already have high-frequency attenuation. While the filter adds phase lag to the

图片摘要：该图主要展示 5 Analytical frequency responses of four longitudinal cues。
![](images/c0315223ccb03206ed6b304d1aa2574d335f6341fb55a5b290c036bce603a377.jpg)

图片摘要：该图主要展示 6 Analytical position responses and control traces for four 。
![](images/70e4003dd3519b09279599076b4bd17499c27b097f7a0f13ab19947ea2f5d410.jpg)  
Fig. 6 Analytical position responses and control traces for four longitudinal cues.

cue response, for these hover maneuvering tasks it does not appear to significantly degrade stability margins. The flight data analyzed in Ref. 2 exhibited measured crossover frequencies of 1-4 rad/sec with the same noise attenuation filter. Other display laws with similar high-frequency gains and the same noise attenuation filters have also been flown successfully (Refs. 1, 4, and 5).

# EXPERIMENT CONDUCT

# Simulator Configuration

The experiment was conducted on the NASA Ames Vertical Motion Simulator (VMS). The main objective was to perform piloted evaluations of the existing production display laws and the three new display designs to assess their impact on handling qualities, using both Apache-rated and non-Apache-rated test pilots. It was recognized that the validity of the results would be highly dependent on the simulation fidelity. Therefore, much attention was devoted to represent accurately the Apache using the simulator elements shown in Figure 7. This effort is described in detail in Ref. 10. To summarize, a nine-state (8 rigid body plus dynamic inflow) linear math model valid for the unaugmented AH-64 near hover was identified from flight data. A verified software representation of the AH-64 DASE was then added to the linear model. The aircraft rotorspeed and torque responses to collective were identified from flight data, to drive the cockpit and helmet-mounted displays. Significant effort was expended to identify also the static and dynamic characteristics of the AH-64's centerstick controller and pedals. These controller characteristics were used to tune the simulator's programmable control loaders. For added fidelity, a sound generator was matched qualitatively to an audio recording made within an Apache cockpit.

Because of the small displacements involved in the hover maneuvers, nearly the full potential of the VMS motion system could be used. At mid-to-high frequencies, 1:1 motion of the simulator with respect to the aircraft was achieved in all axes. In addition, the AH-64 Integrated Helmet and Display Sighting System (IHADSS) flight hardware was used (Figure 8). A simulated forward looking infrared (FLIR) image was shown on the helmet monacle, and the Apache Bob-Up mode symbology was superimposed on it. The FLIR and symbology images were made to match the written specifications and a video record from an AH-64 in terms of symbology placement, size, scaling, and display field-of-view. The total throughput time delay from control input to motion and visual response was matched as closely as possible to the flight-identified values for each axis. Pilot acceptance of the simulator as representative of an AH-64 was generally positive, as described in Ref. 10.

# Piloted Tasks

Two tasks were developed to compare the display laws. In each, the pilot was advised to perform the task using the strategy of minimizing the acceleration cue error from the

图片摘要：该图主要展示 7 AH 64 simulation components。
![](images/cc09ba4ad91df1aff8d991d387d9d3f67b9ca3f9e34422eef25c916005dae360.jpg)  
Fig. 7 AH-64 simulation components.

hover box. This strategy is the one taught to operational pilots. The first task, known as the pad capture, was to acquire the hover box from a diagonal 56 ft offset (40 ft each laterally and longitudinally) within 15 secs. In each run, the task was repeated four times; every 15 secs, the hover box was repositioned in earth axes 56 ft diagonally forward or rearward of its last position. The objective of the task was to achieve a stable hover over the box before it was moved to the new position. The standards for desired performance were: 1) achieve position over/undershoot of less than one hover box width; 2) maintain altitude at $40 \pm 10$ ft; 3) maintain initial heading $\pm 10$ deg. The standards for adequate performance were twice those for desired. This task was meant to expose issues associated with the cue controllability and the position trajectories.

The second task was a Bob-Up/Bob-Down maneuver, in which the pilot began in a hover at 40 ft, ascended to a 70 ft target altitude, then immediately descended to 40 ft again. The objective was to perform the task in 15 secs while maintaining position over the hover box. The standards for desired performance were: 1) achieve target altitudes with over/undershoot less than 10 ft; 2) maintain heading $\pm 5$ deg; 3) maintain position within the hover box. The standards for adequate performance were twice those for desired. This

task was designed to compare the regulation capabilities of each cue during off-axis inputs.

The tasks were conducted using a baseline level of Dryden turbulence that was termed very light. Its root-mean-square (rms) magnitude was 0.3 ft/sec. Three pilots evaluated the display laws in the pad capture task under a light-to-moderate turbulence level (rms of 1.5 ft/sec) to investigate potential disturbance rejection differences among the laws.

# Outside Visual Scene

The pilot's visual information was presented using the AH-64 IHADSS monacle, which displayed the symbology superimposed on a simulated FLIR image of the outside world. The outside view was a head-tracked computer-generated scene. The offset of the FLIR turret from the pilot station was represented. The scene objects were adjusted in color to present a nighttime FLIR-like image once they were sent to the monacle display. Both white-hot and black-hot FLIR modes were available to the pilot. The monacle field of view was 40 Horiz. x 30 Vert. degrees, while the simulated sensor field-of-regard was 240 Horiz. x 90 Vert. degrees.

The pad capture task was flown over a flat area with grid lines at ten foot intervals. The grid lines provided strong heading cues and some position cueing. The bob-up task was

图片摘要：该图主要展示 8 AH 64 Integrated Helmet and Display Sighting System。
![](images/b2012e6037b58f816e6475e9fd570dccffec68b7acfff9b6b9071e4cd7ea11cb.jpg)  
Fig. 8 AH-64 Integrated Helmet and Display Sighting System.

flown over a hover pad area with trees in the near field that provided some altitude cues.

While the simulated FLIR imagery was judged by the pilots to be reasonable in terms of object light intensity, all the pilots felt that the lack of texture and other fine detail made the outside cues far less useful than those of an actual FLIR. This, in combination with the symbology-oriented nature of the tasks and the nominal altitude used (40 ft), forced the pilots to rely more on the symbology than normally would be the case in reality. Some pilots estimated that they used the symbology for $90\%$ of the cuing. Consequently, they were prevented from compensating for poor symbology drive laws by using outside cues, thus perhaps more clearly exposing the differences among the laws. Several Apache pilots stated that this poor-FLIR environment was similar to using the IHADSS at night during high hover operations, where significant ground cues are lost.

# Off-Nominal Configurations

The new display laws were designed for a nominal aircraft configuration, namely the one used for the parameter

identification flight tests that yielded the simple DASE-on transfer function models. The laws were then evaluated in the piloted simulation using the nine-state model with the DASE programmed explicitly. The simulation model had been identified for the same nominal aircraft weight and stores configuration as the display design model. To assure that the new display laws were not overly tuned to one aircraft configuration, the nine-state simulation model's parameters were varied to represent a light and a heavy stores configuration about the nominal. The pad capture task was performed by several pilots at these off-nominal conditions.

# Test Pilot Participants

A total of ten experienced test pilots participated in the simulation as evaluators. Among them were four Apachequalified pilots, including: one instructor pilot from AQTD with over 700 hrs in the Apache and over 400 hours using the PNVS; one from the AQTD with 150 PNVS hours; one from the Aeroflightdynamics Directorate (AFDD) with 25 PNVS hours; and one from the manufacturer, McDonnell Douglas Helicopter Co., with 200 PNVS hours. The non-Apache rated pilots included two from NASA Ames, one from AFDD (with 30 PNVS hours), one from Sikorsky Aircraft (with helmet-mounted display experience), one from Boeing Helicopters, and one from the Navy Test Pilot School.

# Piloted Evaluations

Each pilot was allowed to practice the tasks with all four of the cues until he felt that his performance had stabilized. Several training sessions were generally required. He then completed formal evaluations of all the cues for one task with one aircraft and turbulence configuration. He was not informed of which cue he was evaluating. The order that the cues were presented was varied for each evaluation session. For any one task, the procedure was to finish a session with a re-evaluation of the cue flown first, to see if learning effects were a factor.

# Data Collection

Data collected during evaluations comprised statistical and time history data to document task performance, verbal answers to a questionnaire, and Cooper-Harper pilot ratings (Ref. 11).

# RESULTS

# Task Performance Results

Figure 9 presents positioning performance crossplots for all pilots conducting four pad captures each for each acceleration cue. In terms of deviation from a $45^{\circ}$ horizontal path, the trajectories are seen to be more accurate and more consistent for the workload and performance designs in comparison with both the production and modified production designs.

Figure 10 presents the acceleration cue error from the hover box for the same runs. Since the pilot was advised to place and keep the cue on the box during the acquisition,

图片摘要：该图主要展示 10 presents the acceleration cue error from the hover box fo。
![](images/d06fa3df53e09ff1606624897583b08d22c8770630038893e87ac7f232c9b33c.jpg)

图片摘要：该图主要展示 10 presents the acceleration cue error from the hover box fo。
![](images/78dc18c695a09d0b8e0b131dddd8601f3d56a90e130432347185c04dddc3bbf3.jpg)

图片摘要：该图主要展示 10 presents the acceleration cue error from the hover box fo。
![](images/68cf0c0771bfd7fcf3d562c18906a39cbea1bbd7c0e13550b0b8975c017e6446.jpg)

图片摘要：该图主要展示 10 presents the acceleration cue error from the hover box fo。
![](images/acfc3b0562c9ba1178888c8e9c4cac3a8df8833dbdbe8b9e7ed81d0bdddf2641.jpg)  
Fig. 9 Position crossplots for four cues, pad capture task.

these plots indicate cue controllability and are thus a measure of workload. The workload and performance designs show a narrower concentration of points along a $45^{\circ}$ path and at the origin, indicating lower workload in comparison with the other two.

The altitude performance for four evaluation runs by one pilot is presented in Figure 11. While all the traces remain in the desired performance region, the production and modified production traces exhibit large oscillations that appear nearly divergent compared with the more damped traces for the workload and performance designs. The differences suggest that the improved controllability of the workload and performance cues allowed the pilot to devote more attention

to scanning the altitude tape, thus better controlling the altitude.

As a check of the analytical performance predictions described earlier, Figure 12 presents longitudinal trajectory and control input time histories from analysis and from simulation for a 20 ft longitudinal capture using the performance design. The position trajectories are in good agreement except for pilot and system time delays that were not modeled in the analysis. The simulation control input trace shows a higher frequency component superimposed on a trend that generally matches the analysis. This "dither" may result from the pilot's uncertainty about how much control is required to move the cue to the box.

图片摘要：该图主要展示 10 Cue to box error crossplots for four cues, pad capture ta。
![](images/da826aff74ddc0f870bc720479c02e8d8bee53b76d916525af420b825566aa92.jpg)

图片摘要：该图主要展示 10 Cue to box error crossplots for four cues, pad capture ta。
![](images/7fd9d792151f3f526793c8945420770e16030e5c38180d36dd26163ce54b8acb.jpg)

图片摘要：该图主要展示 10 Cue to box error crossplots for four cues, pad capture ta。
![](images/e825d5fb3110f89ba72273ab5642bad77c12fdaad31b4c12b99f231b6464cb8f.jpg)

图片摘要：该图片与Fig. 10 Cue to box error crossplots for four cues, pad capture task；The performa这部分内容相关。
![](images/3fcfdebf606a4a62b091c63c25802582a21168414ee3bc934e32e6ce100ac6b4.jpg)  
Fig. 10 Cue-to-box error crossplots for four cues, pad capture task.

The performance measure of interest for the bob-up task is the horizontal position error during the vertical maneuver. Figure 13 presents the root-mean-square position errors seen for the bob-up task as a function of cue drive law. Each point represents an individual bob-up maneuver. The modified production law has the lowest position error, followed by the workload, performance, and production laws. The most likely reason for this trend is that since the performance and workload laws use pilot input as one sensor for the cue, the high-frequency part of the cue motion is due to the control rather than to any actual aircraft movement. Thus, less aircraft motion is required to keep the cue on the box than for

the production and modified production laws. While the pilot workload is reduced, for these small inputs the positioning performance may be slightly degraded.

# Pilot Rating Results

Figure 14 presents a compilation of all the pilot ratings for the pad capture task in the baseline turbulence, nominal weight configuration. All the rating means fall in the Level 2 region. According to pilot comments given during the rating procedure, the workload associated with flying the ratedamped aircraft using a narrow field-of-view display with simulated FLIR imagery made the vehicle-display system unsatisfactory without improvement. The workload associated with control of the vertical axis, which required frequent

图片摘要：该图主要展示 14 presents a compilation of all the pilot ratings for the p。
![](images/af17f0c3523624195c7f2ed36fa59de82e0a6a5d9c7fa038955f856bf2f2c964.jpg)  
Fig. 11 Altitude performance for four cues during four pad captures.

图片摘要：该图主要展示 11 Altitude performance for four cues during four pad captur。
![](images/d6fb948fb40e03c117c18c21d49a55bc473ca1180e0088b0183c7113519042cb.jpg)  
Fig. 13 Positioning performance for four cues, bob-up task, all runs.

图片摘要：该图主要展示 13 Positioning performance for four cues, bob up task, all r。
![](images/5be698685db78abcd6ee0e3befeceb45a71c9aca3ab72dcd676e1d3c3307a70f.jpg)

图片摘要：该图主要展示 13 Positioning performance for four cues, bob up task, all r。
![](images/20e317a52a9d1960830e00a8163d7a15a5d88d94dbde0e0b1dde0b3d4fabe72e.jpg)  
Fig. 12 Evaluation of pilot-vehicle-display model for performance design.

scanning away from the central symbology to the altitude tape, also was frequently sighted as a factor contributing to the Level 2 ratings.

However, there are significant differences among the cue drive laws. The mean rating improves from 5.9 for the production law to 4.3 for the workload design, which had a slightly better mean than the performance design. This improvement reflects a reduction in pilot compensation requirements from "extensive" to "moderate" to perform the task. It is important to note that the $90\%$ confidence bars (Ref. 12) do not overlap for the best versus the worst display configurations. Moreover, each of the ten pilots assigned a better rating to the workload and performance designs than to the production laws.

Figure 15 presents the rating data for the bob-up task at nominal weight and baseline turbulence. Again, the workload design received the best ratings, followed by the performance and then the production and modified production designs.

# Summary of Pilot Comments

Following is a summary of the pilot comments for all the cue laws tested. They are extracted from answers given verbally in response to a questionnaire after every evaluation run.

Pilot comments concerning the production law indicated that the cue was unpredictable and difficult to control. A large amount of effort was required to keep the cue within the hover box. In the pad capture task, the cue was said to cause pilot-induced oscillations (PIO's) unless the task aggressiveness was reduced. Over- and undershoots in position were seen with the cue. The workload to control the cue

图片摘要：该图主要展示 15 presents the rating data for the bob up task at nominal w。
![](images/b29cbd5dee65b56b690992f13a42e277015813a203ffb12f0146ad902cb1e1b1.jpg)  
Fig. 14 Mean and $90\%$ confidence values for all ratings, pad capture task.

allowed less time for crosschecking the altitude and heading, degrading performance in those axes. For the bob-up task, the attention required to maintain the cue on the box detracted from the altitude performance.

The modified production law was considered an improvement over the production law in controllability and positioning performance. It was still judged unpredictable,

图片摘要：该图主要展示 14 Mean and confidence values for all ratings, pad capture t。
![](images/8e0dd504044c58b1f60b2d128509e2754bc8e6373aaf34ce288efbdaa9fd5557.jpg)  
Fig. 15 Mean and $90\%$ confidence values for all ratings, bob-up task.

sluggish, and slightly prone to PIO. However, more attention was available to scan the altitude and heading for both tasks.

The workload design was described as very predictable and easily controllable. It allowed more aggressiveness and was felt by the pilots to allow much improved position and velocity performance. There were no PIO tendencies, and the workload was reduced significantly. Thus, there was substantially more attention available for scanning and control of the altitude and heading. These improvements were apparent for both tasks. Pilots noted that the cue sometimes appeared to have a slight overshoot in response to a quick control input, which they referred to as jitter. However, the effect was not judged objectionable. All the AH-64 rated pilots noted that they had no trouble adjusting to the characteristics of this new law.

Comments on the performance design were very similar to those for the workload design, except that no cue jitter was noted. The position trajectories for the pad capture task were described as nicely convergent. There was a wider dispersion of ratings and a slightly worse mean rating with this design for both tasks. The difference in ratings for the bob-up task seems to correlate with the task positioning performance presented in Figure 13. Recall that the performance design assigns more of the cue response to the control input than does the workload design, which may degrade its regulation performance.

# CONCLUSIONS

A piloted simulation was conducted to investigate handling qualities improvements attainable through the application of improved display laws for hover maneuvering, using FLIR imagery with superimposed symbology. Three new display law methods were applied to the AH-64 Apache and compared with its existing display laws. The new laws, termed the modified production, performance, and workload designs, were compared analytically, and then tested using a pilot-in-the-loop simulation that was extensively validated and well accepted by the pilots. The analytical comparisons showed an improvement in both performance and workload for the new laws. These analytical improvements were confirmed in the piloted evaluations by ten test pilots, four of whom were AH-64 rated. The new performance and workload laws, which use stick position to achieve an immediate response of the acceleration cue to pilot input, were determined to benefit significantly handling qualities in comparison with the production and modified production laws. First, the new laws yielded improved performance for the horizontal positioning primary task, while allowing more attention for improved performance in secondary tasks such as altitude regulation. Second, the new laws elicited favorable pilot comments; all ten pilots said they preferred the new laws over the existing laws. Finally, all ten pilots assigned a better pilot rating to each of the new laws than to the existing laws.

# REFERENCES

1 Eshow, M. M., Aiken, E. W., and Hindson, W. S., "Preliminary Results of a Flight Investigation of Rotorcraft Control and Display Laws for Hover," American Helicopter Society National Specialists' Meeting in Flight Controls and Avionics, Cherry Hill, New Jersey, October 1987.   
2Eshow, M. M., "Flight Investigation of Variations in Rotorcraft Control and Display Dynamics for Hover," Journal of Guidance, Control, and Dynamics, Vol. 15, No., 2, 1992, pp. 482-490.   
3 Tsoubanos, C. M., and Kelley, M. B., "Pilot Night Vision System (PNVS) for Advanced Attack Helicopter (AAH)," Proceedings of the 34th Annual National Forum of the American Helicopter Society, Washington, D. C., 1978.   
4 Schroeder, J. A., and Merrick, V. K., "Flight Evaluations of Several Hover Control and Display Combinations for Precise Blind Vertical Landings," Journal of Guidance, Control, and Dynamics, Vol. 15, No. 3, 1992, pp. 751-760.   
5 Schroeder, J. A., Eshow, M. M., and Hindson, W. S., "An In-Flight Investigation of Display Drive Law Improvements to an Operational Attack Helicopter," Proceedings of the 46th Annual National Forum of the American Helicopter Society, Washington, D. C., 1990.   
<sup>6</sup>Weir, D. H., Klein, R. H., and McRuer, D. T., "Principles for the Design of Advanced Flight Director Systems

Based on the Theory of Manual Control Displays," NASA CR-1748, 1971.   
7Tischler, M. B., and Cauffman, M. G., "Frequency-Response Method for Rotorcraft System Identification with Applications to the BO-105 Helicopter," Proceedings of the 46th Annual National Forum of the American Helicopter Society, Washington, D. C., 1990.   
8Ham, J. A., Butler, C. P., "Flight Testing the Handling Qualities Requirements of ADS-33C - Lessons Learned at ATTC," Proceedings of the 47th Annual National Forum of the American Helicopter Society, Phoenix, AZ, 1991.   
9McRuer, D. T., and Krendel, E. S., "Mathematical Models of Human Pilot Behavior," AGARDograph No. 188, Jan. 1974.   
10 Schroeder, J. A., Tischler, M. B., Watson, D. C., and Eshow, M. M., "Identification and Simulation Evaluation of an AH-64 Helicopter Hover Math Model," AIAA Paper 91-2877, August 1991.   
11 Cooper, G. E., and Harper, R. P., "The Use of Pilot Rating in the Evaluation of Aircraft Handling Qualities," NASA TN D-5153, 1969.   
12Mack, C., Essentials of Statistics for Scientists and Technologists, Plenum Press, New York, New York, 1967, pp. 65-66.

# The Development and Potential of Inverse Simulation for the Quantitative Assessment of Helicopter Handling Qualities

Professor Roy Bradley

Department of Mathematics Glasgow Polytechnic Glasgow, U.K.

Dr Douglas G. Thomson

Department of Aerospace Engineering University of Glasgow Glasgow, U.K.

# Abstract

In this paper it is proposed that inverse simulation can make a positive contribution to the study of handling qualities. It is shown that mathematical descriptions of the MTEs defined in ADS-33C may be used to drive an inverse simulation thereby generating, from an appropriate mathematical model, the controls and states of a subject helicopter flying it. By presenting the results of such simulations it is shown that, in the context of inverse simulation, the attitude quickness parameters given in ADS-33C are independent of vehicle configuration. An alternative quickness parameter, associated with the control displacements required to fly the MTE is proposed, and some preliminary results are presented.

# Nomenclature

<table><tr><td>API</td><td>Agility Performance Index</td></tr><tr><td>ns, nc</td><td>number of states and controls in API function</td></tr><tr><td>p, q, r</td><td>components of aircraft angular velocity in body axes</td></tr><tr><td>qi, rj</td><td>weighting constants for API</td></tr><tr><td>ta</td><td>time to reach maximum acceleration in Rapid Sidestep MTE</td></tr><tr><td>td</td><td>time to reach maximum deceleration in Rapid Sidestep MTE</td></tr><tr><td>tl</td><td>time in acceleration phase of Rapid Sidestep MTE</td></tr><tr><td>tm</td><td>time taken to complete manoeuvre</td></tr><tr><td>u</td><td>control vector</td></tr><tr><td>u, v, w</td><td>components of aircraft velocity in body axes</td></tr><tr><td>Vf</td><td>airspeed</td></tr><tr><td>Vmax</td><td>maximum airspeed reached in manoeuvre</td></tr></table>

<table><tr><td>Vmax</td><td>maximum acceleration during Rapid
Sidestep MTE</td></tr><tr><td>Vmin</td><td>maximum deceleration during Rapid
Sidestep MTE</td></tr><tr><td>x</td><td>state vector</td></tr><tr><td>y</td><td>output vector</td></tr><tr><td>x̂</td><td>turn rate</td></tr><tr><td>φ, θ, ψ</td><td>aircraft attitude angles</td></tr><tr><td>θ0</td><td>main rotor collective pitch angle</td></tr><tr><td>θls, θlc</td><td>longitudinal and lateral cyclic pitch angles</td></tr><tr><td>θ0tr</td><td>tailrotor collective pitch angle</td></tr></table>

# 1. Introduction

The need to assess the overall handling qualities of a helicopter by its performance and handling characteristics in a range of typical manoeuvres has been recognised by the authors of the U.S. Handling Qualities for Military Rotorcraft [1]. As part of demonstrating compliance with these requirements, a set of standard manoeuvres, or Mission Task Elements (MTEs) has been defined and criteria for performance and handling have been specified. In addition, the authors of this document have indicated that mathematical models are an appropriate basis for evaluation and analysis at the design stage. By its nature, inverse simulation encapsulates this combination of precisely defined manoeuvre and mathematical modelling. With inverse simulation, a mathematical representation of a MTE is used to drive a helicopter model in such a way that the vehicle's response and control displacements may be derived. In effect, a flight trial of the modelled helicopter flying a given MTE is performed, and the information collected from such simulations is

as extensive as that recorded in a real trial. It follows that inverse simulation has the potential of being a useful validation tool for manoeuvring flight, [2], but the question arises as to whether the data collected can be analysed for the evaluation of handling qualities in the same manner as that from a flight test of the real aircraft. The two conditions:

i) The mathematical model of the helicopter must have a suitably high level of fidelity for the flight conditions encountered in the MTE;   
ii) The mathematical model of the MTE must be representative, in some sense, of the real manoeuvre;

might reasonably be considered as necessary before a positive response can be made but whether these conditions are, in addition, sufficient is the subject of current research at Glasgow.

This paper describes the rationale behind the belief that inverse simulation has an important contribution to make in the evaluation of helicopter handling qualities. A number initial studies have been performed using the helicopter inverse simulation package Helinv, [3] and some preliminary results will be presented in later sections of this paper. In the section that follows some of the main features of inverse simulation and manoeuvre description are discussed. Next, in section 3, a number of exploratory studies are described. These studies involve three methods of extracting information from the results of inverse simulation: performance comparisons, handling qualities indices and quickness parameters. It will be argued that the first two methods are likely to be limited both in their potential and in their applicability, while the quickness parameter approach shows particular promise since it goes some way towards resolving the question of the sufficiency of the two conditions listed above.

# 2. Inverse Simulation of Mission Task Elements

It is convenient to begin the discussion relating to the assessment of handling qualities by clarifying the term 'inverse simulation' as it is employed in relation to the work at Glasgow. Other authors [4, 5] have different interpretations related to the context in which it is employed. Also, the technique is not universally familiar, so that the feasibility of deriving a unique set of control responses from a given flight path is often questioned. The general problem is a good starting point for the discussion.

# 2.1 Inverse Simulation - The General Problem

The simulation exercise of calculating a system's response to a particular sequence of control inputs is well known. It is conveniently expressed as the initial value problem:

$$
\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, \mathbf {u}); \quad \mathbf {x} (0) = \mathbf {x} _ {0} \tag {1}
$$

$$
\mathbf {y} = \mathbf {g} (\mathbf {x}) \tag {2}
$$

where $\mathbf{x}$ is the state vector of the system and $\mathbf{u}$ is the control vector. Equation (1) is a statement of the mathematical model which describes the time-evolution of the state vector in response to an imposed time history for the control vector $\mathbf{u}$ . The output equation, (2), is a statement of how the observed output vector $\mathbf{y}$ is obtained from the state vector.

Inverse simulation is so called because, from a pre-determined output vector $\mathbf{y}$ it calculates the control time-histories required to produce $\mathbf{y}$ . Consequently, equations (1) and (2) are used in an implicit manner and, just as conventional simulation attaches importance to careful selection of the input $\mathbf{u}$ , inverse simulation places emphasis on the careful definition of the required output $\mathbf{y}$ .

# 2.2 Application to the Helicopter

In the helicopter application discussed here, the state vector is $\mathbf{x} = [\mathbf{u}\mathbf{v}\mathbf{w}\mathbf{p}\mathbf{q}\mathbf{r}\phi \theta \psi ]^{\mathrm{T}}$ and the control vector is $\mathbf{u} = [\theta_0\theta_{1s}\theta_{1c}\theta_{0t}]^{\mathrm{T}}$ . The focus of the work at Glasgow is on manoeuvres that are defined in terms of motion relative to an Earth-fixed frame of reference so that the output equation is the transformation of the body-fixed velocity components into Earth axes. For a unique solution to the inverse problem it is necessary to add a further output, a prescribed heading or sideslip profile being the most appropriate choice. The four scalar constraints - three velocity components and one attitude angle - serve to define uniquely the four control axes of the helicopter.

The sophistication of the modelling implied by the form of $\mathbf{f}$ in equation (1) is of central importance since the more complex the basic formulation, the more difficult it is to cast into a useful inverse form. The mathematical model used for this early work was Helistab [6]; Thomson and Bradley [3] have described a method for the unique solution of the inverse problem in this case. Current work at Glasgow University employs an enhanced model, Helicopter Generic Simulation (HGS), [7] which is accessed by the inverse algorithm, Helinv. The main features of HGS include a multiblade description of main rotor flapping, dynamic inflow, an engine model, and lookup tables for fuselage aerodynamic forces and

moments. The host package, Helinv, incorporates several sets of pre-programmed manoeuvre descriptions which are required as system outputs from the simulation. In fact, the manoeuvres are essentially the input into the simulation and much of the value of Helinv lies in the scope and validity of the library of manoeuvre descriptions which have been accumulated. They include those relating to Nap of the Earth [8], Air-to-air Combat, Off-shore Operations [9], and of particular interest in this study, Mission Task Elements [10]. There is also a facility for accessing flight test data. Some examples of these manoeuvres are discussed in the following section below.

# 2.3 Mathematical Representation of Mission Task Elements for Use with Inverse Simulation

The need for careful attention to the modelling of the required output - here the flight-path - has been emphasised in 2.1 above. It might appear, at first sight, that for a given general description of a manoeuvre that there is a wide choice of possible definitions of the trajectory. This turns out not to be the case, however, because given such freedom, the obvious starting point is to choose the simplest option but, as is discussed below, the simplest option appears to omit key qualitative features and, subsequently, in section 3 it will be argued that this view can be confirmed by applying quantitative criteria to the manoeuvre definition. However, the simplest case is a useful entry point for the discussion.

# 2.3.1 Mathematical Representation of Manoeuvres Using Global Polynomial Functions

Part of the early work on inverse simulation at Glasgow involved creating a library of models on helicopter nap-of-the-earth manoeuvres. The approach used was to fit simple polynomial functions to the known profiles of the primary manoeuvre parameters; velocity, acceleration, turn rate, or simply

the helicopter's position. For example, an acceleration from a trimmed hover state to some maximum velocity, followed by a deceleration back to the hover is one of the most basic forms of manoeuvre which might be encountered. Consequently the approach used to derive a model of it is fairly simple. As the vehicle is to be in a trimmed hover state at both entry and exit, implying both zero velocity and acceleration at these points, and applying the condition that the maximum velocity, $\mathbf{V}_{\max}$ should be reached half way through the manoeuvre, it is possible to fit a sixth order polynomial to these conditions to give the velocity profile

$$
\begin{array}{l} V (t) = V _ {\max } \left[ - 6 4 \left(\frac {t}{t _ {m}}\right) ^ {6} + 1 9 2 \left(\frac {t}{t _ {m}}\right) ^ {5} - 1 9 2 \left(\frac {t}{t _ {m}}\right) ^ {4} \right. \\ + 6 4 \left(\frac {t}{t _ {\mathrm {m}}}\right) ^ {3} ] \tag {3} \\ \end{array}
$$

where $t_m$ is the time taken to complete the manoeuvre.

图片摘要：该图主要展示 1 Velocity Profile for Acceleration and Deceleration Maneuvr。
![](images/da69be64f9d1b7c5f41aa4973b7b7c57bd4ff09c32cd22f5e392dfbc9b8cb152.jpg)  
Figure 1 Velocity Profile for Acceleration and Deceleration Maneuvre Using a 6th Order Polynomial

This velocity profile, shown in Figure 1, can be applied to any of the three component axes of the helicopter to give quick-hop (x), sidestep (y) and bob-up (z) manoeuvres, Figure 2.

图片摘要：该图主要展示 1 Velocity Profile for Acceleration and Deceleration Maneuvr。
![](images/5b72bb2b7417b6c92b133df80cf4c91a0c187a96d3075706434c35f6056d1818.jpg)  
a) The Sidestep

图片摘要：该图主要展示 1 Velocity Profile for Acceleration and Deceleration Maneuvr。
![](images/0bc37d8018ad80912b509937377ac70ecac5af4bf52b83d1f8702a42383cfa1c.jpg)  
b) The Bob-up   
Figure 2 Acceleration and Deceleration Maneuvres

图片摘要：该图主要展示 2 Acceleration and Deceleration Maneuvres。
![](images/90bb31a03ad61b86d0b1082fc4243d0d2059e9c0af8db7e47188c7baa22eef82.jpg)  
c) The Quick-hop   
Figure 2 Continued

To establish the validity of the mathematical representation of a manoeuvre it is necessary to have a sufficient quantity of appropriate data from flight testing to allow comparison to be made. In the context of inverse simulation this data should consist of vehicle component velocities and accelerations as well as its position throughout the manoeuvre. When a comprehensive set of vehicle data, including ground based tracking measurements, was made available, it was clear that these simple functions compared well with the measured data [11]. However, subsequent analysis, reported below in section 3.3, has revealed that a direct comparison of velocities does not provide the appropriate measure of discrimination between candidate profiles and that the profile of equation (3) is not sufficiently aggressive to represent a MTE. Because of the smoothness of the global approximation described earlier in this section it is termed a 'non-aggressive' profile.

# 2.3.2 Mathematical Representation of Manoeuvres Using Piecewise Polynomial Functions

For the current work a series of models of the Mission Task Elements detailed in the ADS-33C document have been used. When these models were first created, [10] there was little published data on which to base the functions representing the geometry, or indeed the velocity or acceleration profiles, of the MTEs. The ADS-33C document itself gives clear descriptions of the MTEs in terms of performance levels which must be reached in key phases of the MTEs, but stops short of presenting an additional definitive geometry or positional time history. This is of course necessary, as imposing a rigid flight profile on top of a series of performance related targets will lead to a task with intolerable pilot workload. Thus, although the MTEs are described in sufficient detail for piloting purposes, further information is needed to describe the MTE in mathematical terms.

Care was taken when creating the mathematical models of the MTEs to encompass all of the features

described in the ADS-33C document. For example, the key elements of the Rapid Sidestep MTE are described as follows

"Starting from a stabilised hover, ..., initiate a rapid and aggressive lateral translation at approximately constant heading up to a speed of between 30 and 45 knots. Maintain 30 to 45 knots for approximately 5 seconds followed by an aggressive lateral deceleration back to the hover."

The following performance is also required

maintain the cockpit station within $\pm 3\mathfrak{m}$ of the ground reference line,

altitude is to be maintained within $\pm 3m$

maintain heading within $\pm 10$ degrees,

attain maximum achievable lateral acceleration within 1.5 seconds of initiating the manoeuvre,

attain maximum achievable deceleration within 3 seconds of initiating the deceleration phase.

It is quite clear from this description that the non-aggressive profile given by equation (3) will not meet all of these requirements. Instead, an alternative approach has been adopted where the MTE is considered as a sequence of polynomial sections where each section is chosen to represent one or more primary manoeuvre parameters of the MTE. A piecewise smooth function, involving one or more of the manoeuvre parameters for the whole MTE, can then be constructed. For the Rapid Sidestep described above there are five distinct sections, and after consideration of the ADS-33C description, it was decided that the most appropriate variable to specify was the vehicle's flight acceleration. This acceleration profile is shown in Figure 3, and the five sections consist of:

i) a rapid increase of lateral acceleration to a maximum value of $\dot{\mathbf{V}}_{\mathrm{max}}$ after a time of $t_a$ seconds.   
ii) a constant acceleration section to allow the flight velocity to approach its required maximum value, $\mathbf{V}_{\max}$ .   
iii) a rapid transition from maximum acceleration to maximum deceleration $\dot{\mathbf{V}}_{\min}$ in a time of $t_d$ seconds,   
iv) a constant deceleration to allow the flight velocity to be reduced towards zero,   
v) a rapid decrease in deceleration bringing the helicopter back to the hover.

图片摘要：该图主要展示 3 Piecewise Polynomial Representation of an Acceleration Pro。
![](images/317aca02f8f9abb4f5b4e55528accfd3e52d5334953087215f1db479545de73c.jpg)  
Figure 3 Piecewise Polynomial Representation of an Acceleration Profile for a Rapid Sidestep MTE

The control strategy and state time histories which this profile produces will be discussed in section 3.3. The values of $\dot{\mathbf{V}}_{\mathrm{max}}$ and $\dot{\mathbf{V}}_{\mathrm{min}}$ are inputs (effectively dependent on the vehicle being simulated) whilst in order to ensure that the performance limits are met, the values of $t_{\mathrm{a}}$ and $t_{\mathrm{d}}$ are set such that

$$
t _ {a} <   1. 5 s \quad a n d \quad t _ {d} <   3. 0 s
$$

Referring to Figure 3, the times $t_1$ and $t_m$ are calculated to give

$$
\int_ {0} ^ {t _ {1}} \dot {\mathbf {V}} (t) d t = \mathbf {V} _ {\max } \quad \text {a n d} \quad \int_ {t _ {1}} ^ {t _ {m}} \dot {\mathbf {V}} (t) d t = 0
$$

where $\mathbf{V}_{\max}$ is the maximum velocity reached during the manoeuvre and from Reference 1 is required to be such that $30 < \mathbf{V}_{\max} < 45$ knots. The transient acceleration profiles are expressed a cubic functions of time so that, for example in the range $t < t_{a}$ ,

$$
\dot {V} (t) = \left[ - 2 \left(\frac {t}{t _ {m}}\right) ^ {3} + 3 \left(\frac {t}{t _ {m}}\right) ^ {2} \right] \dot {V} _ {\max } \tag {4}
$$

The other performance requirements are readily incorporated into an inverse simulation. For example, heading can be constrained to be constant, whilst constant altitude flight along a reference line is guaranteed by ensuring that the off-axis components of velocity are set to zero. The only feature of the Rapid Sidestep MTE as given in ADS-33C which has been disregarded is the necessity to maintain the maximum velocity, lateral flight state between the acceleration and deceleration phases of the manoeuvre for approximately 5 seconds. For the purposes of flight trials this 5 second period may yield useful information on the handling characteristics of the vehicle - for example, poor handling might be indicated if any transient motions present in the vehicle's response do not diminish rapidly once the steady flight state had been attained. For inverse simulation this 5 second period would be modelled as a constant velocity, straight line flight path, and the calculated vehicle response would consist simply of a series of identical trim states. This will yield little useful information, and this phase of the MTE has therefore been ignored.

Developed in this way, in order to capture the aggressive nature of the MTE, the piecewise representation is termed an 'aggressive profile'. A comparison of sidestep manoeuvres generated by both aggressive and non-aggressive profiles can be obtained by differentiating equation (4) to obtain the acceleration for the global polynomial definition. This comparison is shown in Figure 4 from which it is apparent that if the manoeuvre is to be performed in the same time for both cases, then the peak acceleration encountered will be significantly greater in the global polynomial case. This effect is discussed further in section 3.3.1.

图片摘要：该图主要展示 4 Comparison of Acceleration Profiles for Rapid Sidestep MTE。
![](images/b58a55ff7bb10bebc3d1aafb196b4cd913c9b63ceb5d42ccc9a2ef31c5caed99.jpg)  
Figure 4 Comparison of Acceleration Profiles for Rapid Sidestep MTE

Not all of the MTEs described in Reference 1 can be converted in quite such a straightforward manner as the Rapid Sidestep described above. For

example, the Pull-up/push-over which is described only in terms of the load factor profile requires the imposition of additional criteria to complete the flight-path definition. In creating the mathematical representations of the MTEs used here, certain assumptions have been made based mainly on the experience gained modelling the earlier NOE manoeuvres. As further information on flight testing using MTEs becomes available it will be possible to validate these models, and improve them as necessary.

# 3. Inverse Simulation as a Tool for Handling Qualities Assessment

In this section several approaches to handling qualities assessment through inverse simulation are discussed, and some examples are presented to illustrate their effectiveness. Comparisons are made between the results obtained for two configurations of the same helicopter, a battlefield/utility type (based on the Westland Lynx). The baseline configuration, Helicopter 1, has a mass of $3500\mathrm{kg}$ , and a rotor which is rigid in flap. The second configuration, Helicopter 2, differs from Helicopter 1 in that it has a fully articulated rotor and is $500\mathrm{kg}$ heavier, the increase in mass causing the centre of gravity to shift approximately $7.5\mathrm{cm}$ aft of a position directly below the rotor hub. The aim here was to create two configurations with a high degree of similarity (both have identical fuselage and rotor aerodynamic characteristics, for example), but with differing performance and agility characteristics.

# 3.1 Confirmation of Helicopter Performance when Flying Mission Task Elements

Although ADS-33C [1], is directed towards handling qualities, it is unavoidable that the Mission Task Elements that form part of the aggressive task requirements contain a significant element of performance related criteria which refer to the particular configuration being flown. Therefore, the ability to confirm that an existing or projected design can satisfy the criteria, in a performance sense, over the full range of MTEs is of some significance. Section 2.3 discussed how the descriptions of MTEs given in Reference 1 may be converted to a flight path trajectory definition. When the definition is complete, the availability of an inverse simulation enables a range of performance criteria of candidate helicopters to be investigated against configuration parameters - such as control limits, rotor stiffness and installed power. While it is recognised that these criteria may not be the primary considerations which drive the design of the helicopter, inverse simulation can quickly establish the performance limitations of a given design over the full range of MTEs. The

following example has been chosen to illustrate this facility.

# 3.1.1 Comparison of Performance in the Transient Turn MTE

This particular MTE is of interest as, in order to fly it, high roll rates and large roll angles are inevitable, and the parametric differences between the two configurations will have a marked effect on the control time histories generated by inverse simulation.

# a) Mathematical Description of the Transient Turn MTE

The main features of this MTE, as described in Reference 1, are that a 180 degree heading change should be completed within 10 seconds of initiating the manoeuvre at a flight velocity of 120 knots. Previous experience of creating models of turning manoeuvres [10] has indicated that the most appropriate parameter to specify is the vehicle turn rate. Following the technique used to model the Rapid Sidestep MTE discussed in section 2.3, the transient turn is assumed to be composed of three distinct sections, as shown in Figure 5 and described below:

i) from a rectilinear flight trajectory, the turn rate is increased rapidly to some maximum value, $\dot{x}_{\max}$ ,   
ii) the turn rate is maintained at the maximum value until the heading approaches 180 degrees,   
iii) the turn rate is rapidly decreased to zero thereby returning the vehicle to straight line flight.

图片摘要：该图主要展示 5 Turn Rate Profile for a Transient Turn MTE。
![](images/220b07144a974037c608ac0c9d687035099b98870b3524deccf45b5aadcce3ed.jpg)  
Figure 5 Turn Rate Profile for a Transient Turn MTE

This turn rate profile will force the simulated helicopter to roll to an appropriate bank angle, then hold this angle until the 180 degree heading change is approached, at which point the aircraft will be rolled in the opposite direction to return to straight line flight. If it is further assumed that constant altitude is desirable, and that to perform the task as quickly as possible, the entry speed of 120 knots is maintained

图片摘要：该图主要展示 5 Turn Rate Profile for a Transient Turn MTE。
![](images/697ae3ff6faf7cc497ba0f8f50bd8a19d2b8534dac4b134c068e137b173d4fb9.jpg)  
Figure 6 State and Control Time Histories from Inverse Simulation of a Transient Turn MTE

throughout, then the turn rate profile shown in Figure 5 is sufficient to obtain the required mathematical representation. A full description of how the flight path can be obtained from the turn rate profile and airspeed is given by Thomson and Bradley, [10], but the basic principle involves varying the maximum turn rate, $\dot{x}_{\max}$ , until the manoeuvre is completed within 10 seconds, and the heading change (effectively the area under the turn rate profile in Figure 5) is 180 degrees. This situation is reached when the turn radius is $155\mathrm{m}$ and the resulting maximum normal load factor is 2.75. Note that the fraction of the manoeuvre spent in the entry and exit transients must also be specified and in this case a value of $15\%$ was chosen after examination of flight test data from similar manoeuvres [8].

# b) Inverse Simulation of Two Configurations Flying Transient Turn MTE - Control Strategy

Having defined the helicopter configurations and specified the manoeuvre, it is possible to perform inverse simulations of the two configurations flying it. The control time histories generated are shown in Figure 6, from which the overall control strategy can be deduced. The manoeuvre is initiated by a pulse in lateral cyclic to roll the aircraft, note that there is little difference in the amount required between the two configurations. As the aircraft rolls, also shown in Figure 6, collective (and hence thrust) must be added to maintain altitude. There is also a forward motion of the longitudinal stick (denoted by negative longitudinal cyclic) to maintain constant forward speed. The manoeuvre is performed without sideslip and tail rotor collective is used to ensure this condition is met. The initial pulse in lateral cyclic is opposed by a similar pulse in tailrotor collective

which then increases beyond its level flight trim position to offset the extra torque produced by increased main rotor collective. The main differences between the time histories of the two aircraft lie in the collective and longitudinal plots. The baseline configuration, Helicopter 1, requires less collective firstly because it is lighter, but one must also consider the effect of shifting the centre of gravity aft of the rotor hub. This produces a nose up pitching moment which must be countered by forward stick if velocity is to be maintained, which explains the 2 degrees of extra forward longitudinal cyclic required by the less agile configuration, Helicopter 2. The longitudinal tilt of the thrust vector is in addition to the lateral tilt required for rolling, and hence is a contributory factory in the 2.5 degrees of extra collective required by Helicopter 2. Examination of Figure 6 shows that the roll angle history which was suggested by the manoeuvre definition is obtained, and the maximum bank angle reached was approximately 70 degrees, with roll rates of approximately 70 degrees/second encountered in the transients.

# c) Inverse Simulation of Two Configurations Flying Transient Turn MTE - Confirmation of Performance

The advantage of using inverse simulation becomes apparent when it is realised that the collective limit of this configuration is 20 degrees. Consequently, on examination of the collective time history in Figure 6, it is clear that Helicopter 2 is close to the limiting case for this manoeuvre. It then follows that the limiting case for various aircraft masses and centre of gravity positions could be obtained by repeated inverse simulation of the manoeuvre thereby allowing the aircraft configuration envelope for this MTE to be derived. This type of investigation may be extended to include a range of MTEs and configurational parameters.

For performance comparisons the application of inverse simulation is clear cut. Given the availability of a helicopter model of appropriate validity, it is straightforward to measure comparative control margins and control activity for a given set of manoeuvres. Experience has shown that the facilities offered by flight mechanics models such as HGS are adequate for such investigations. Therefore the remaining task is to compile a suite of validated manoeuvre definitions - and although several of the descriptions of Reference 10 have been validated against flight data there are several manoeuvres for which flight tests are required to provide practical validation. The conclusion to be drawn is that while performance comparisons of this kind are straightforward to conduct, the handling qualities information that it can provide is limited and likely to remain so.

# 3.2 The Handling Qualities Index

One of the earliest applications of inverse simulation was an attempt to quantify the agility of a given helicopter configuration through an Agility Performance Index (API) [12]. The difficulty of producing a general definition of the term agility is well known [4] but the API was based on the concept of installed agility, that is, it was dependant on the particular configuration of the helicopter and independent of any pilot model. This independence of a pilot model is a feature of the inverse formulation since it generates a precise piloting task and leaves no scope for other than ideal piloting of the helicopter. The API of a helicopter for a given manoeuvre was determined from the formula:

$$
\begin{array}{l} \mathrm {A P I} = \sum_ {\mathrm {i} = 1} ^ {\mathrm {n},} q _ {\mathrm {i}} \int_ {0} ^ {t _ {\mathrm {m}}} f (x _ {\mathrm {i}} (t)) d t + \\ \sum_ {j = 1} ^ {n _ {c}} \mathrm {i} \int_ {0} ^ {\mathrm {t} _ {m}} g (u _ {j} (t)) d t \tag {5} \\ \end{array}
$$

where $t_m$ is the time taken to complete the manoeuvre, $q_i$ and $r_j$ are weighting constants related to state $i$ and control $j$ . The integers $n_s$ and $n_c$ are the number of states and controls to be included in the performance index. The functions $f(x_i(t))$ and $g(u_j(t))$ were selected to penalise large state and control deviations during the manoeuvre: for example,

$$
f \left(x _ {i} (t)\right) = \left[ \frac {x _ {i} (t) - x _ {i t r i m}}{x _ {i \max} - x _ {i t r i m}} \right] ^ {2}
$$

where $\mathbf{x}_{\mathrm{trim}}$ is the value of state i, in the steady flight condition at the entry to the manoeuvre, and $\mathbf{x}_{\mathrm{max}}$ is the maximum value of the state encountered during the manoeuvre. Using this definition low values of API (i.e. small control and state displacements) will imply good agility. The obvious difficulty with such an approach is the appropriate choice of the weights $\mathbf{q}_i$ and $\mathbf{r}_j$ and, in practice, zero or unity were commonly employed in comparative studies of different helicopter configurations on the basis of whether it was felt that those quantities were significant or not in a particular manoeuvre. Nevertheless, despite this simplified approach, the work established the principle whereby different helicopters could be comparatively assessed for their agility over a range of standard manoeuvres by a reproducible simulation study.

Having established the principle for agility studies, it is attractive to consider a similar approach for handling qualities and define a Handling Qualities

Index (HQI) using a similar form to that in equation (5). It may be necessary to include other terms such as auto- and cross-correlations of the control responses but from the whole of the attitude, rate, velocity, acceleration and control information, it should not be unreasonable to expect that an appropriate balance of the coefficients in the formulation of the HQI could produce a formula which reflects, in large measure, an assessment of handling qualities. Unfortunately, the question of finding the values of the coefficients necessary to achieve the appropriate balance is impracticable - just as in the case of the API. Therefore, although conceptually attractive and demonstrable in principle, the HQI falls at the present time because of the lack of essential knowledge about the coefficient values, and if it were to be seriously considered for development in the future then an extensive validation programme would be needed to establish its credibility.

# 3.3 Quickness Parameters

In addition to the calculation of the time responses of the control displacements, inverse simulation of a given manoeuvre calculates the responses of the full range of kinematic variables. Included in this information, are the time-histories of roll rate $\mathfrak{p}$ and roll angle $\phi$ , so that when a Rapid Sidestep manoeuvre is simulated according to the translation velocity profile defined by Figure 3 it is a

图片摘要：该图主要展示 7 Calculation of Roll Quickness from Inverse Simulation of H。
![](images/b77544ec3f0fee8f3940fddd4c7d42d6fd3abcf0d0e7961143fd1020cc431f63.jpg)  
Figure 7 Calculation of Roll Quickness from Inverse Simulation of Helicopter 1 Flying a Rapid Sidestep MTE

straight forward matter to calculate the quickness parameter chart $p_{pk} / \Delta \phi_{pk}$ against $\Delta \phi_{\min}$ in a manner described by the ADS-33C document, section 3.3. The time histories of $p$ and $\phi$ shown in Figure 7 for the sidestep manoeuvre with $t_a = 1.5s$ , $t_d = 3s$ , $V_{\max} = 35$ Knots, $\dot{V}_{\max} = 5m/s^2$ and $\dot{V}_{\min} = -5m/s^2$ , are obtained from the inverse simulation of Helicopter 1 for the Rapid Sidestep using the aggressive profile defined by Figure 3. They are annotated to show the calculations of the quickness parameters of the main pulses of roll rate. First there is the roll into the manoeuvre then, at about the midpoint, there is a roll in the opposite direction to bring the rotor into a position to decelerate the helicopter, and finally there is a roll back to the level, trim, position. The attitude quickness parameters corresponding to this data and data from a variety of similar manoeuvres (obtained by varying the parameters used to define the MTE model) are shown in Figure 8 and it can be seen that the values mainly lie in the Level 1 region.

The corresponding control displacement time-histories are shown in Figure 9 but it should be borne in mind that the attitude quickness parameters have been calculated solely as a result of a defined manoeuvre so are not, in the context of inverse simulation, necessarily an appropriate measure of the

图片摘要：该图主要展示 7 Calculation of Roll Quickness from Inverse Simulation of H。
![](images/b058ca9230424235c2a4b1cd4b0adf5d9b2d2c561d691cd4ed0776754e800c02.jpg)  
Figure 8 Roll Quickness Chart for Helicopter 1 from Inverse Simulation of Rapid Sidesteps

图片摘要：该图主要展示 8 Roll Quickness Chart for Helicopter 1 from Inverse Simulat。
![](images/9968ee240c040e723b747c719ec5712e73d83fed48cd1dacb03e28a3ac41498d.jpg)  
Figure 9 Control Displacements for Helicopter 1 Flying a Rapid Sidestep MTE

handling qualities of a particular configuration. These issues are further elaborated in sections 3.3.1 and 3.3.2 but before leaving the current discussion it is opportune to give some initial attention to the output of the inverse analysis - that is the set of control time histories - and pose the question of how to process it to afford some measure of handling quality or pilot workload. The lateral cyclic control displacement, $\theta_{1c}$ , certainly does not have the characteristics of the bank angle so that the parameter $\dot{\theta}_{1cpk} / \Delta \theta_{1cpk}$ is unlikely to be useful - and indeed experimentation has shown this to be the case. In fact, it may be observed that the pulses of lateral cyclic away from the trim position are of a similar character to the pulses of roll

rate, p, and this similarity suggests that $\Theta_{1c}$ , the integral of $\theta_{1c}$ :

$$
\Theta_ {l _ {c}} = \int^ {t} \theta_ {l _ {c}} (t) d t
$$

relates to the value of the bank angle so that a control quickness parameter $\theta_{\mathsf{l}_{\mathsf{cpk}}} / \Delta \Theta_{\mathsf{l}_{\mathsf{cpk}}}$ may be the equivalent parameter, and when plotted against $\Delta \Theta_{\mathsf{l}_c}$ , would give a chart equivalent to that used to plot attitude quickness. The manner of calculation is identical to that of the attitude quickness as illustrated in Figure 10. That this quantity is a useful measure to invoke from the inverse simulation method is discussed in more depth in section to follow.

图片摘要：该图主要展示 10 Calculation of Lateral Cyclic Quickness Parameter from In。
![](images/d3b5fee50ad6555a1ba433f4e8dec749765c414bab8b71ad7341e5bf3c1d8371.jpg)

图片摘要：该图主要展示 10 Calculation of Lateral Cyclic Quickness Parameter from In。
![](images/0d36fcc9f6caf82c2f02463a4360e9d46e6472c9663ad816978160aa9838817b.jpg)  
Figure 10 Calculation of Lateral Cyclic Quickness Parameter from Inverse Simulation of Helicopter 1 Flying Rapid Sidestep MTE

# 3.3.1 Influence of MTE Model

In this section we return to the issues raised above regarding the calculation of quickness parameters for predefined manoeuvres. The first aim of this discussion is to qualify the observations made on previous occasions that the details of the manoeuvre profile definition have not appeared to be significant. When faced with the requirement to specify the velocity profile of a sidestep MTE, for

example, it is natural, as described in section 2.3.1 above, to write down in the first instance the nonaggressive profile, since it is the computationally simplest description. It gives a smoother change in acceleration than the aggressive profile described in section 2.3.2 as has been illustrated in Figure 4. When this manoeuvre is simulated using the Helicopter1 configuration, the attitude quickness parameters vary significantly from those derived from the more sharply executed aggressive manoeuvre and lie mainly in the Level 2 region as is shown in Figure 11. Here then is a further criterion by which to select a manoeuvre description: if it is to be used for handling qualities studies within the ambit of ADS-33C then a description must be employed which sets the manoeuvre in the Level 1 region. The attitude quickness parameters have discriminated quantitatively between the aggressive and nonaggressive profiles, confirming the quantitative discrimination noted earlier.

图片摘要：该图主要展示 10 Calculation of Lateral Cyclic Quickness Parameter from In。
![](images/099fc4f8bf9bd44fd96264db5a35f2a34379970c403ce6c2a86c6df159247733.jpg)  
Figure 11 Roll Quickness Chart for Helicopter 1 from Inverse Simulation Using Non-aggressive Sidestep Profile

# 3.3.2 Influence of Configuration

Now consider the effect of altering the helicopter's configuration to a less agile version. The Helicopter 2 configuration of the vehicle has more weight and significantly reduced rotor stiffness. Applying the same manoeuvre to it produces, as seen

in Figure 12, almost identical attitude quickness values - in fact occurring in closely positioned pairs. This result is typical of many simulations which have been conducted and which lead to the initially surprising conclusion that the attitude quickness parameters are largely independent of the configuration used in the inverse simulation. A little reflection will show that this effect is not unusual since the roll rates and attitude angles through a manoeuvre are largely dictated by the manoeuvre profile itself and one should expect some agreement for other than gross configurational changes.

图片摘要：该图主要展示 11 Roll Quickness Chart for Helicopter 1 from Inverse Simula。
![](images/80cb5e01c36c514c01335c1f8dcad7b7eac7aafb1b85fa9155c21e70e3d6e4e3.jpg)  
Figure 12 Roll Thickness Chart for 2 Configurations from Inverse Simulation of Rapid Sidestep MTE

However, the control quickness is influenced by the variation in configuration. Figure 13 shows quite clearly that it increases significantly for the Helicopter 2 configuration, representing the additional effort required by the pilot to drive the inferior configuration through the same manoeuvre. The control quickness parameter, as defined in Section 3.3, is remarkably effective in discriminating between different configurations.

Figure 13 Lateral Cyclic Quickness Chart for 2 Configurations from Inverse Simulation of Rapid Sidestep MTE   
图片摘要：该图主要展示 13 Lateral Cyclic Quickness Chart for 2 Configurations from 。
![](images/b937c8331b38f9e90b24e3fc24d2cb93ed0c19d04a731b048e0796e10bc3974e.jpg)  
$\times$ Helicopter 1   
Helicopter 2

# 3.4 Handling Criteria

These simple illustrations suggest a procedure to be followed when using inverse simulation for handling qualities studies. One must use the requirements, such as ADS-33C, in an inverse manner. First the manoeuvre must be refined until it satisfies the level of handling demanded by the requirements regarding attitude quickness, then various configurational changes can be compared by examining the corresponding control quickness values. An increase in the value of the control quickness indicates an increased work load and hence a worsening of the handling qualities. In addition to there being a relative measure it may be possible, as indicated speculatively on Figure 14 to identify regions in the control quickness chart which correspond to particular levels of pilot workload or handling rating.

# 4. Conclusions

The potential of three approaches for employing inverse simulation to assess handling qualities have been discussed. Two of them, the Handling Qualities Index and the performance comparisons have been shown to have limited potential while the third, the use of attitude and

图片摘要：该图主要展示 14 Lateral Cyclic Quickness Chart with Suggested Workload/Ha。
![](images/86e8255cd6f903bccc3284b3876c6584a904fc4025999b4f6965eaf550fcba77.jpg)  
Figure 14 Lateral Cyclic Quickness Chart with Suggested Workload/Handling Qualities Boundaries

control quickness parameters in a dual relationship, promises useful exploitation.

Two general conclusions may be made about the current state of inverse simulation:

(a) Current mathematical models, such as HGS, are adequate for basing inverse flight mechanics studies on.   
(b) Flight tests should be made to validate the flight-path models currently being developed.

The main conclusion of this work resides in the significance of the quickness parameters in association with inverse simulation.

It is important to emphasise that these investigations have indicated a practical criterion for deciding on the appropriate modelling of an MTE for inverse simulation. That is, the model must generate attitude quickness parameters which lie in the Level 1 region. Moreover, the choice of manoeuvre model is practically independent of helicopter configuration. Therefore, referring to the conditions set out in the introduction, this is the sense in which manoeuvres must be representative.

The approach has been taken further and it has been shown to be possible to define a control quickness parameter which can discriminate between different helicopter configurations flying the same manoeuvre. While it is acknowledged that the choice of definition for the control quickness may require future development, it is clear from the work done so far that this general approach can potentially extend the scope of simulation in demonstrating compliance with handling qualities requirements. It does appear from this work that in using quickness parameters the conditions are sufficient for the successful use of inverse simulation providing that it is realised that it is the control quickness that is the determining factor in the assessment.

# Acknowledgements

The authors wish to thank The Royal Society for their continued support of this work. The cooperation Dr Gareth Padfield of the Defence Research Agency, RAE Bedford, is also appreciated, with particular reference to the use of look-up tables and helicopter configurational data.

# References

1. Anon, "Aeronautical Design Standard, Handling Qualities Requirements for Military Rotorcraft." ADS-33C, August 1989.   
2. Bradley, R., Padfield, G.D., Murray-Smith, D.J., Thomson, D.G., "Validation of Helicopter Mathematical Models." Transactions of the Institute of Measurement and Control, Vol. 12, No. 4, 1990.   
3. Thomson, D.G., Bradley, R., "Development and Verification of an Algorithm for Helicopter Inverse Simulation." _Vertical_, Vol. 14, No. 2, May 1990.   
4. Whalley, M.S., "Development and Evaluation of an Inverse Solution Technique for Studying Helicopter Maneuverability and Agility." NASA TM 102889, July 1991.

5. McKillip, R.M., Perri, T.A., "Helicopter Flight Control System Design and Evaluation for NOE Operations Using Controller Inversion Techniques." 45th Annual Forum of the American Helicopter Society, Boston, May 1989.   
6. Padfield, G.D., "A Theoretical Model for Helicopter Flight Mechanics for Application to Piloted Simulation." Royal Aircraft Establishment, TR 81048, April 1981.   
7. Thomson, D.G., "Development of a Generic Helicopter Mathematical Model for Application to Inverse Simulation." University of Glasgow, Department of Aerospace Engineering, Internal Report No. 9216, June 1992.   
8. Thomson, D.G., Bradley, R., "Modelling and Classification of Helicopter Combat Maneuvres." Proceedings of ICAS Congress, Stockholm, Sweden, September 1990.   
9. Taylor, C.D., Thomson, D.G., Bradley, R., "The Mathematical Definition of Helicopter Take-off and Landing Manoeuvres for Offshore Operations." University of Glasgow, Department of Aerospace Engineering, Internal Report No. 9243, October 1992.   
10. Thomson, D.G., Bradley, R., "The Use of Inverse Simulation for Conceptual Design." 16th European Rotorcraft Forum, Glasgow, September 1990.   
11. Thomson, D.G., Bradley, R., "Validation of Helicopter Mathematical Models by Comparison of Data from Nap-of-the-Earth Flight Tests and Inverse Simulations." Paper No. 78, Proceedings of the 14th European Rotorcraft Forum, Milan, Italy, September 1988.   
12. Thomson, D.G., "An Analytical Method of Quantifying Helicopter Agility." Paper 45, Proceedings of the 12th European Rotorcraft Forum, Garmisch-Partenkirchen, Federal Republic of Germany, September 1986.

图片摘要：该图片与An Analytic Modeling And System Identification Study of Rotor/Fuselage Dynamics 这部分内容相关。
![](images/48716184cbbc09c4ff448bcebedf936d82b35af6ff2d262e70f04bf178eb0e6a.jpg)

# An Analytic Modeling And System Identification Study of Rotor/Fuselage Dynamics At Hover

Steven W. Hong  
United Technologies Research Center  
East Hartford, Connecticut

H.C.Curtiss,Jr.,Professor Princeton University Princeton,New Jersey

# Abstract

A combination of analytic modeling and system identification methods have been used to develop an improved dynamic model describing the response of articulated rotor helicopters to control inputs. A high-order linearized model of coupled rotor/body dynamics including flap and lag degrees of freedom and inflow dynamics with literal coefficients is compared to flight test data from single rotor helicopters in the near hover trim condition. The identification problem was formulated using the maximum likelihood function in the time domain. The dynamic model with literal coefficients was used to generate the model states, and the model was parametrized in terms of physical constants of the aircraft rather than the stability derivatives, resulting in a significant reduction in the number of quantities to be identified. The likelihood function was optimized using the genetic algorithm approach. This method proved highly effective in producing an estimated model from flight test data which included coupled fuselage/rotor dynamics. Using this approach it has been shown that blade flexibility is a significant contributing factor to the discrepancies between theory and experiment shown in previous studies. Addition of flexible modes, properly incorporating the constraint due to the lag dampers, results in excellent agreement between flight test and theory, especially in the high frequency range.

Presented at Piloting Vertical Flight Aircraft: A Conference On Flying Qualities and Human Factors, San Francisco, California, 1993.

# Introduction

The investigation of rotorcraft dynamics, and specifically the coupled fuselage/rotor dynamics, is motivated by increasing sophistication in rotorcraft stability analyses and by the emergence of high-performance flight control system design requirements. The past few years have seen a concentrated effort directed toward providing an analytic simulation model of coupled fuselage/rotor dynamics and model validation against flight test data.

Helicopter dynamics include the rigid-body responses demonstrated by fixed-wing aircraft, plus higher-frequency modes generated by the interactions of the rotor system with the fuselage. For earlier flight control system designs with lower bandwidth requirements, it was satisfactory to use low-order analytic models which did not accurately model the high-frequency rotor dynamics; with the recent introduction of high-performance, high-bandwidth control system specifications, it has become increasingly necessary to correctly model the coupled fuselage/rotor dynamic modes. It has long been known that flap dynamics introduce significant time delays into the rotor system, and more recently, Curtiss has shown that inclusion of the lag dynamics is important in the design of high performance control systems (Curtiss, 1986). Recent studies have explored the possibility of using rotor state feedback designs to damp blade motion (Ham, 1983). An accurate understanding of the coupled fuselage/rotor dynamics is therefore important in rotorcraft control system design and stability analyses.

Recent flight test experiments have shown that existing simulation models do not accurately

predict these high-frequency modes (Ballin et. al, 1991, Kaplita et. al, 1989, and Kim et. al, 1990). These studies show significant differences between theory and experiment associated with the coupled rotor/body dynamics, especially in the frequency region dominated by the rotor lag motion. This research is therefore directed toward providing an improved understanding of the aeroelastic and aeromechanical phenomena which determine the coupled rotor/body dynamics at hover.

In order to gain physical insight into helicopter dynamics, development of linear models incorporating coupled rotor/fuselage dynamics has long been a research objective. Past approaches to linear model development have included direct numerical perturbation of nonlinear simulations (Diftler, 1988), identification of state-space stability and control matrix elements (Tischler, 1987), and analytic derivation of linear equations of motion (Zhao and Curtiss, 1988). This study uniquely combines system identification methods with analytic modeling techniques in order to investigate helicopter hover dynamics and to arrive at an improved linear model. The emphasis is on the high-frequency dynamics of the coupled rotor/body motion.

The identification study is carried out on flight test data from a Sikorsky H-53E helicopter at hover, using previously published data (Kaplita et. al, 1987, and Mayo et. al, 1990).

# Research Objectives

This paper describes an investigation into the response of articulated rotor helicopters to control inputs in hover. The goal is an improved understanding of the coupled rotor/fuselage dynamics in hover directed toward a validated analytic simulation model including high-frequency rotor/fuselage dynamics for use in stability analyses and high-performance control system design studies.

Identification of linear, time-invariant state-space models representing high-order helicopter dynamics including main rotor degrees of freedom has long been an objective of engineers involved in rotorcraft simulation and control system design. The state and control matrix elements in an identified state-space model can provide physical insight

into system dynamics and can be used in combination with mathematical modeling techniques to analyze differences between theory and experiment.

State-space identification techniques have been applied to conventional fixed-wing aircraft with useful results. Since identification of state-space models using directly parametrized state and control matrix elements requires the estimation of a large number of parameters, a reduced order model is often used, assuming six degree-of-freedom rigid body dynamics and decoupling between the longitudinal and lateral axes.

Identification of reduced order state-space models for rotorcraft have generally produced unsatisfactory results. The presence of the rotor produces significant rotor/body coupling, requiring additional states to describe the high-frequency dynamics, and also introduces significant interaxis coupling. The complete rotorcraft identification problem is therefore required to use a high-order, multi-input, multi-output model with as many as 18 or more states.

In order to avoid the inevitable problem of overparametrization which results when attempting to identify a directly parametrized high-order helicopter model, this study uses an analytic model to generate state time histories. The model used in this study has been developed at Princeton using the Lagrangian formulation. It includes the coupled fuselage/rotor dynamics, main rotor inflow, tail rotor thrust, and provides for tail rotor inflow dynamics. It was analytically linearized about hover. This model provides a state-space description of the helicopter at hover which is completely analytic and dependent only on an input set of physical parameters. A subset of these inputs are considered uncertain, and are to be estimated from flight test data. The flight-test derived parameter estimates can be used in combination with the mathematical formulation to trace various physical aspects of coupled rotor/body dynamics and thereby obtain physical insight. The complete high-order model including rotor dynamics can be reasonably parametrized by 15 or fewer physically meaningful input coefficients, resulting in a substantial reduction in the number of parameters to be estimated.

The framework of the identification approach is the time-domain maximum likelihood methodology. The likelihood function is formulated assuming the presence of Gaussian measurement and process noise. The process noise may be nonwhite. The noise covariances as well as process noise dynamics may be parametrized. With Gaussian noise assumptions, the likelihood function becomes the weighted least-square of the residual errors. The Kalman filter is the natural way to produce these residuals for state-space dynamic systems.

The maximum likelihood estimate is obtained by finding the global maximum of the likelihood function. The parameters are nonlinearly related to the cost function and the resulting parameter space is highly multimodal. Traditional function optimization techniques based on gradient methods generally become trapped in local optima.

The genetic algorithm is an alternative function optimization approach which does not rely on the use of local gradient information. The genetic algorithm is an adaptive scheme, based on the analogy with natural evolution, which efficiently searches a large parameter space for the 'fittest' solution to a given objective. This method has been demonstrated to be highly effective in obtaining the global maximum in a multimodal parameter space.

The formulation of the system identification problem in the maximum likelihood framework leads to estimates of physical coefficients which have attractive statistical optimality properties and represent the best possible combination of physical coefficients necessary to match the given test data set.

This identification methodology allows an assessment of model assumptions inherent in the mathematical model used to generate the state time histories. In this study, emphasis is placed on the frequency region associated with coupled rotor/fuselage dynamics. In the frequency domain, the dominant feature in the rotor magnitude response is a notch characteristic produced by the presence of the in-plane blade degree of freedom. Using rotor blade constants derived through the identification procedure, rotor blade modeling assumptions may be examined, resulting in analytic model improve

ments. This study examines in detail the blade structural modeling assumption and investigates the effect of accounting for blade flexibility effects generated by the presence of a large mechanical damper at the blade hinge.

# Analytic Model Description

Research at Princeton has resulted in the development of a linearized rotor/body helicopter dynamic model. The dynamic equations are formulated using a Lagrangian approach in order to capture all the important inertial coupling terms. The model includes rigid-body translation and rotation (pitch, roll, and yaw rates, longitudinal and lateral velocities), rigid blade lag and flap multimodal coordinates, and main rotor cyclic dynamic inflow. The controls are main rotor cyclic and pedals. The version of the model used in this study was analytically linearized about the hover trim condition and does not include the collective degree of freedom.

Rotorcraft dynamics includes coupling between the motion of the fuselage which is in rotational and translational motion relative to inertial space, and the motion of individual rotor blades. The final set of equations of motion are referenced to the body-fixed axis system which has its origin at the fuselage center of gravity. In the Newtonian approach to modeling coupled rotor/fuselage equations of motion, blade acceleration terms are first written referenced to the hub axis which is rotating at constant velocity; coordinate transformations are then used to obtain acceleration terms in the body-fixed frame. The complexity of the resulting acceleration terms, combined with the number of degrees of freedom necessary to model rotor dynamics properly, has led to the use of Lagrange's equations for the derivation of the coupled rotor/ body model.

The development of Lagrange's equations proceeds from the evaluation of the Lagrangian, which requires only position and velocity terms in order to relate the system generalized forces to changes in the system kinetic and potential energies. The generalized coordinates in Lagrange's approach represent the degrees of freedom in the system and are chosen to correspond to the system

states. The kinetic energy term includes the motion of the fuselage and rotor blades, and the potential energy includes the gravitational potential energy of the fuselage and stored energy in the mechanical springs in the rotor system. Mechanical dampers are accounted for by use of the dissipation function. The generalized forces include aerodynamic forces due to fuselage and blade aerodynamics. Evaluation of the time and partial derivatives in the Lagrangian can be time consuming for a high-order model and can be assigned to a symbolic manipulation program such as MACSYMA.

# Identification Methodology

This paper describes an approach for identification of a coupled fuselage/rotor model for rotorcraft hover dynamics from flight test measurements. The identified model includes flap and lag degrees of freedom, main rotor inflow, and process and measurement noise disturbances. The process noise may be colored. The approach uses an analytically derived, linear time-invariant state-space model with literal coefficients which is parametrized in terms of aeromechanical input coefficients. The model order and structure may therefore be assumed to be determined by this approach, and the system parameters are to be estimated from observations. The parameter estimation problem is formulated using the statistical framework of maximum likelihood (ML) estimation theory, thereby benefitting from known optimality properties of ML estimators. This discussion first presents the parametrized dynamic model to be used in the identification methodology, and then describes the application of the maximum likelihood estimation approach to dynamic systems.

# Model Parametrization

The helicopter is modeled as a continuous-time dynamic system whose measurements are discretely sampled as sensor outputs. Thus the identification algorithm is required to estimate continuous-time model parameters from discrete sensor measurements. This continuous/discrete formulation is well known and is discussed by

Ljung (1987). The linear time-invariant state equations are derived using the Lagrangian approach, and are given by

$$
\dot {x} (t) = A _ {c} (\theta) x (t) + B _ {c} (\theta) u (t) + F _ {c} (\theta) w (t) \tag {1}
$$

The model form accounts for the presence of process noise, where $w(t)$ is assumed to be zero-mean white noise with unity spectral density. The continuous-time matrices, $A_{c}(\theta), B_{c}(\theta)$ , and $F_{c}(\theta)$ , are parametrized by a vector of parameters, $\theta$ , which are to be estimated from observations.

The observations are sampled at discrete time intervals, where

$$
\begin{array}{l} y (k T) = C (\theta) x (k T) + G (\theta) v _ {T} (k T) \\ t = k T, \quad k = 0, 1, 2, \dots \tag {2} \\ \end{array}
$$

and $\nu_{T}(kT)$ are the disturbance effects at the sampled time intervals.

For digital implementation of the identification algorithm, the continuous-time state equation given in Equation (1) is discretized using zero-order hold. The input is assumed to be held constant over the sampling time interval, and the continuous-time state equation can then be integrated analytically over the interval in order to obtain the discrete-time state equation. The zero-order hold discretization introduces a phase lag equivalent to one-half sample interval, which is taken into account by advancing the control input by the corresponding one-half time interval.

Eliminating time subscripts for simplicity, the discrete-time state-space equations are given by

$$
\begin{array}{l} x (t + 1) = A (\theta) x (t) + B (\theta) u (t) + F (\theta) w (t) \\ y (t) = C (\theta) x (t) + G (\theta) v (t) \tag {3} \\ \end{array}
$$

This equation is now understood to be a discrete-time equation. Here, $w(t)$ and $v(t)$ are sequences of independent random variables with zero mean and unit covariance.

# Maximum Likelihood Formulation

Let $Y^{N}$ be a vector of observations which are supposed to be realizations of stochastic variables,

and let $y(t)$ be a multi-dimensional observation taken at time t:

$$
Y ^ {N} = [ y (1), y (2), \dots , y (N) ]
$$

The observations, $Y^{N}$ , depend on a vector of parameters, $\theta$ , which are also considered to be random variables. The conditional probability density function for $\theta$ , given the observations, $Y^{N}$ , is then given by

$$
p (\theta | Y ^ {N}) = \frac {p (Y ^ {N} \theta) \cdot p (\theta)}{p (Y ^ {N})} \tag {4}
$$

where $p(\theta)$ is the prior distribution of the random parameter vector. A reasonable estimate for $\theta$ can then be obtained by finding the value of $\theta$ which maximizes the conditional density function given by Equation (4). With no prior knowledge of the distribution of $\theta$ , $p(\theta)$ may be assumed to be uniform. The best estimate for $\theta$ is then obtained by maximizing the likelihood of obtaining the observations. This leads to the ML, or maximum likelihood, estimator, given by

$$
\hat {\theta} _ {M L} = \underset {\theta} {\operatorname {a r g m a x}} p \left(Y ^ {N} | \theta\right) \tag {5}
$$

For parametrized dynamical systems, with Gaussian noise assumptions, the maximum likelihood estimator has the form

$$
\begin{array}{l} \hat {\theta} _ {M L} = \underset {0} {\arg \max } p (Y ^ {N} | \theta) \\ = \arg \max  _ {\theta} - \frac {1}{2} \sum_ {t = 1} ^ {N} \varepsilon^ {T} (t, \theta) A ^ {- 1} (\theta) \varepsilon (t, \theta) - \\ \frac {N}{2} \log | A (\theta) | - \frac {N m}{2} \log 2 \pi \tag {6} \\ \end{array}
$$

where

$$
m = \text {n u m b e r o f m e a s u r e m e n t s}
$$

$$
\varepsilon (t, \theta) = y (t) - \hat {y} (t, \theta)
$$

$$
\Lambda (\theta) = E \varepsilon (\theta) \varepsilon^ {T} (\theta)
$$

and $\hat{y}(t, \theta)$ is generated using Equation (3) with the discrete-time Kalman filter formulation.

# The Genetic Algorithm

The evaluation of the likelihood function as presented in Equation (6) requires a search for the global maximum of the likelihood function over a multimodal parameter space whose contours are not known. Specifically, the identification methodology has led to a function optimization problem where the performance measure is a highly nonlinear function of many parameters. The principal challenge facing the identification problem is the very large set of possible solutions and the presence of many local optima. Hill-climbing methods for function optimization based on finding local gradients become trapped in local optima and are inadequate for this problem. Genetic algorithms overcome these difficulties by efficiently searching the parameter space while preserving and incorporating the best characteristics as the search progresses.

The problem of function optimization can be addressed using the paradigm of adaptive systems, where some objective performance measure (the cost function) is to be maximized (i.e., adaptation occurs) in a partially known and perhaps changing environment. The idea of artificial adaptive plans, based on an analogy with genetic evolution, was formally described by John Holland in the seventies and have recently become an important tool in function optimization and machine learning (Holland, 1975, and Goldberg, 1989). Holland's artificial adaptive plans have come to be known in recent literature as genetic algorithms.

Genetic algorithms are based on ideas underlying the process of evolution; i.e., natural selection and survival of the fittest. Using biological evolution as an analogy, genetic algorithms maintain a population of candidate solutions, or 'individuals,' whose characteristics evolve according to specific genetic operations in order to solve a given task in an optimal way.

As a general overview, genetic algorithms have the following attributes which distinguish them from traditional hill-climbing optimization methods (Goldberg, 1989):

1. GA's work with a representation of the parameter values rather than with the parameters themselves.   
2. GA's search from a population of points, not from a single point.   
3. GA's use objective function information, not gradient information.   
4. GA's use probabilistic transition rules, not deterministic ones.

The genetic algorithm maintains a population of 'individuals'; i.e., possible solutions to the function optimization problem. In the context of the identification problem, each individual corresponds to a vector of parameters. The population of individuals 'evolves' according to the rules of reproduction and mutation analogous to those found in natural evolutionary processes, with the result that the population preserves those characteristics favoring the best solution to the cost function.

The following steps were described by Holland (Holland, 1975) and contain the essentials properties of the basic genetic algorithm.

1. Select one individual from the initial population probabilistically, after assigning each individual a probability proportional to its observed performance.   
2. Copy the selected individual, then apply genetic operators to the copy to produce a new individual.   
3. Select a second individual from the population at random (all elements equally likely) and replace it by the new individual produced in step 2.   
4. Observe and record the performance of the new structure.   
5. Return to step 1.

This deceptively simple set of instructions contains the ability to test large numbers of new combinations of individual characteristics and the ability to progressively exploit the best observed characteristics. It does so through the use of genetic operators.

# Genetic Operators

Parent selection based on fitness, and the subsequent application of genetic operators to produce new individuals are the steps by which the algorithm modifies the initial population and continually tests new combinations while maintaining those parameter sets which give high fitness. Each of these operations are performed probabilistically.

The initial population of individuals is selected randomly with a uniform distribution over the defined parameter space. After one generation, parent individuals are selected randomly, with a probability which is proportional to the fitness assigned to that individual. The selection procedure resembles spinning a roulette wheel whose circumference is divided into as many segments as there are individuals. The arc length of each segment is made proportional to the fitness value of the corresponding individual. Thus, the chance of choosing a given individual is uniformly random and yet proportional to its fitness.

The genetic operations of crossover and mutation are then applied to the selected parent individuals in order to introduce new characteristics into the population, enabling an efficient search for the optimal combination of parameters.

The crossover operation involves a recombination of two selected individuals at a randomly selected point. Thus the crossover operation produces two new individuals, each of whom inherit characteristics from both parents.

The mutation operation involves a random alternation of an individual's characteristic with a very low probability. This serves to introduce new information into the pool of structures and serves to guard against the possibility of becoming trapped in local optima.

# Genetic Coding

Each individual is a candidate parameter set and is represented as a concatenation of individual parameters:

$$
\theta = \left[ \begin{array}{l l l l} \theta_ {1} & \theta_ {2} & \dots & \theta_ {N} \end{array} \right]
$$

In a digital implementation, each parameter $\theta_{i}$ is encoded using a binary alphabet, and the individual is thus represented by a binary-valued string. The following specific coding scheme was suggested by Starer (Starer, 1990).

Let each parameter $\theta_{i}$ be bounded by $\theta_{i_{\max}}$ and $\theta_{i_{\min}}$ . If each parameter is coded in binary with a word length of $l$ , then the interval $\left[\theta_{i_{\max}}, \theta_{i_{\min}}\right]$ is discretized by $2^{l}$ values. A representation of the parameter $\theta_{i}$ can be obtained from the $l$ -bit binary coding of

$$
\mathrm {m o d} \left[ \frac {\left(\theta_ {i} - \theta_ {i _ {m i n}}\right) (2 ^ {l} - 1)}{\theta_ {i _ {m a x}} - \theta_ {i _ {m i n}}} \right]
$$

To illustrate, let an individual represent a candidate parametrization where

$$
\theta = \left[ \begin{array}{l l} \theta_ {1} & \theta_ {2} \end{array} \right] = \left[ \begin{array}{l l} 3 & 4. 5 \end{array} \right]
$$

and bounds are given as

$$
1 <   \theta_ {1} <   4, 2 <   \theta_ {2} <   7, l = 6
$$

The binary-valued string representing this candidate vector is then

$$
\theta_ {\text {b i n a r y}} = [ 1 0 1 0 1 0 0 1 1 1 1 ]
$$

The genetic algorithm is illustrated in Figure

图片摘要：该图主要展示 1 The Genetic Algorithm。
![](images/c149ab6f936313fcd837874a9877549b04643d1223ded3ad05995117e9d740b7.jpg)  
Figure 1 The Genetic Algorithm

# Implicit Parallelism

Genetic algorithms efficiently conduct a search over a defined parameter space, converging

to a near-optimal solution. The basic unit of processed information in this genetic search is the schema, defined by Holland (1975). In the context of a digital implementation of genetic algorithms, a schema is a template specifying similarities at certain string positions.

Thus, an individual is a string of binary digits, and the alphabet is composed of $\{0,1,\# \}$ , where $\#$ denotes 'don't care' (i.e., the value at this position has no effect on the performance measurement). As an example, an individual may be represented as

$$
[ 0 0 1 1 1 0 1 1 0 0 0 1 0 ]
$$

A schema is a similarity template within this individual; so that this individual contains the schemata given by

$$
[ 0 0 \# \# 1 0 1 1 0 0 0 1 0 ]
$$

Given $l$ positions, a single individual is an instance of $2^l$ distinct combinations, and an instance of $3^l$ distinct schemata. Further, a population of size $N$ contains between $3^l$ and $N3^l$ distinct schemata. Holland has shown that each schemata are evaluated and processed independently of the others, providing a tremendous computational leverage on the number of function evaluations. Therefore, the use of genetic operators in the reproductive plan provides i) intrinsic parallelism in the testing and use of many schemata, and ii) compact storage and use of large amounts of information resulting from prior observations of schemata.

The concept of implicit parallelism is fundamental to the efficiency of genetic algorithms. Each schemata is processed and evaluated independently of other schema in the population; this provides a tremendous computational leverage. A very weak lower bound states that for a population of $(n)$ individuals, more than $o(n^{3})$ useful 'pieces' of information is processed in each iteration (Goldberg, 1989).

# An Example

As an illustration of the genetic algorithm, consider the following example.

$$
\begin{array}{l} f (x, y) = \\ 3 (I - y) ^ {2} e ^ {- y ^ {2} - (x + I) ^ {2}} - \\ 1 0 \left(\frac {y}{5} - y ^ {3} - x ^ {5}\right) e ^ {- y ^ {2} - x ^ {2}} - \frac {1}{3} e ^ {- (y + I) ^ {2} - x ^ {2}} \\ \end{array}
$$

The function surface is shown in Figure 2, along with the contour lines. This multimodal function has a global maximum at (1.5814, -0.0093).

A genetic algorithm was run on this function with a population size of 20. The initial guesses were chosen randomly, and were bounded as $-3 < x < 3$ , $-3 < y < 3$ . A binary code with wordlength of 8 was used, which means that both $x$ and $y$ were discretized by 256 points. An exhaustive grid search under these conditions would involve evaluating 65536 possible points to find the global maximum.

Snapshots of the population distribution up to 7 generations are shown in Figure 2. The snapshots show the population converging upon the global maximum; by the $7^{th}$ generation, most of the individuals have converged on the maximum. The genetic algorithm in this case converges on $(1.5412, -0.0353)$ as the global optimum.

This convergence has occurred after 7 generations. With a population size of 20 individuals, this is 140 function evaluations as compared to the 65536 necessary for the grid search.

This relatively simple example serves to illustrate the ability of the genetic algorithm to find the optimum of a given function, using no gradient information.

# Analytic Model Validation

The mathematical model is correlated with flight test data using nominal values for input coefficients. The correlation plots in Figure 3 show transfer function comparisons for pitch and roll axes. The data represent separate flights. In each

图片摘要：该图片与Sample Function；Generation I这部分内容相关。
![](images/6b1bddb46aa104a5fba4b833c4c27eb34d5965ad139c4fc88b2d87d30435f1a9.jpg)  
Sample Function

图片摘要：该图片与Generation I；Generation 3这部分内容相关。
![](images/f6f505bce498505fffa6cd50686c423106a5202581d20331b5ddebfe7ea0ff3b.jpg)  
Generation I

图片摘要：该图主要展示 2 Genetic Algorithm Example。
![](images/774a2b17c9031c8564f2ac08f73440f9ffde5812ea12e5c9c740ef882a0a53e5.jpg)  
Generation 3

图片摘要：该图主要展示 2 Genetic Algorithm Example。
![](images/b8b4ceffb5cdf7ea7816361a46dcebfa12af7bc14c3fa96049bcf5d033e89a3c.jpg)  
Generation 5

图片摘要：该图主要展示 2 Genetic Algorithm Example。
![](images/ca54179f2e259f4630d3e216a9eeeefab67b2f72a60a92d4109081d0f2b7b799.jpg)  
Generation 7   
Figure 2 Genetic Algorithm Example

case, the comparison is between the flight test rate gyro output and the model state. The comparison is made between $0.5\mathrm{Hz}$ (3.14 rad/sec) and $6\mathrm{Hz}$ (37.7 rad/sec) since the input signal was designed to cover this frequency range. The fuselage structural bending modes are lightly damped and dominate the frequency above $\sim 20$ rad/sec. Therefore the identification procedure uses a bandpass filter with the upper cutoff frequency at 15.7 rad/sec. The frequency range of interest is therefore between 0.5 Hz to $2.5\mathrm{Hz}$ (3.14 rad/sec to 15.7 rad/sec).

The choice of physical coefficients used to parametrized dynamic model must allow adjustments to account for differences between test and theoretical responses using nominal physical input values. The gain differences at low frequencies, implying a mismatch in rigid body response, requires parametrization of the rigid body acceleration. The coupled fuselage/lagwise modes are a lightly damped pole-zero pair and create a notch-filter effect in the frequency response between 10 - 15 rad/sec. This frequency is near the -180 degree crossover, and a mismatch in this region adversely impacts the gain and phase margin calculations. Modeling the dynamics of this mode is important for control system design and stability analysis and will be the primary focus of modeling in this study.

# Validation Of Identification Procedure Using Simulated Data

The maximum likelihood identification methodology for parametrized dynamic systems is validated first on a simulation with known parameters. These results demonstrate the feasibility of using genetic algorithms to estimate physical coefficients from noisy data, and establish the population size and crossover and mutation rates for this application.

The simulation model is driven by flight test control inputs from the hovering condition. Main rotor pitch and roll cyclic and tail rotor pedals are all active, with primary excitation into roll cyclic. The output states used to form the cost function are pitch, roll, and yaw rates, and pitch and roll attitudes. No velocity information is necessary.

# Simulation Model Parametrization

The model structure and parametrization was presented in Equations (1) through (3). The continuous-time state space model is analytically derived using the Lagrangian approach and using a vector of physical input coefficients, $\theta$ . For the purposes of this simulation study, the model structure has been augmented to include a first order time constant on process noise. The process noise dynamics are to be parametrized and estimated from output data.

The simulation model was parametrized as follows:

aerodynamic coefficients:

lift curve slope, $a$

inflow equivalent cylinder height, hhnd

inflow wake rigidity factor, wrf

hover trim values:

trim flap angle, $\beta_{o}$

trim main rotor pitch angle, $t_0$

trim inflow velocity, $\nu_{o}$

main rotor blade constants:

lag damper constant, $\overline{C}_c$

lag spring constant, $K_{\varsigma}$

flapspringconstant. $K_{\beta}$

inertias:

fuselage cross-moment, $I_{xz}$

tail rotor:

tail rotor thrust scale factor, $K_{TR}$

noise parameters:

noise covariance ratio, NR

process noise time constant, $\pmb{\tau}$

Kalman filter theory allows optimal state estimates to be obtained in the presence of state and measurement noise, where the Kalman gain is uniquely determined up to the ratio of process to measurement noise. The noise covariance estimate is therefore parametrized by the ratio of process to measurement noise.

# Genetic Algorithm Procedure

The genetic algorithm was implemented using a population size of 500 individuals; a crossover

图片摘要：该图片与Pitch Rate/B1S. Pitch Input；Roll Rate/A1S. Roll Input这部分内容相关。
![](images/3168104e6fcfee8cc129480e042c96b6779bcb4074db20cbd22166ca01030ad3.jpg)  
Pitch Rate/B1S. Pitch Input

图片摘要：该图主要展示 3 Model Validation。
![](images/aa804da750ef1153aaeba6b7f67d4092bf6879756bc8b70f194ff58a13fe0bbb.jpg)

图片摘要：该图主要展示 3 Model Validation。
![](images/dbe614e5e021964d6930a9ea0d39493e1386f04133b2a0e693d50643c0490c07.jpg)  
Roll Rate/A1S. Roll Input

图片摘要：该图主要展示 3 Model Validation。
![](images/80f737bbe35c879a57c13ba2d5feafdeddd74a1289c71a0cae57490953a2e30d.jpg)  
Figure 3 Model Validation

rate of 2/3; and a mutation rate of 1/1000. The parameters were allowed to vary within 50 percent of the known simulation values.

图片摘要：该图主要展示 3 Model Validation。
![](images/1b966a0e52ce5261c346c19c95c49e9955e57a4f47961baf1a02e47940f146b0.jpg)  
Figure 4 Best Likelihood Values

The sensitivity of the cost function to the parameter values vary widely. Therefore, as parameters begin to show convergence, the range of allowable values is progressively narrowed in order to demonstrate convergence for all parameters.

The identification proceeds by running 10-12 separate genetic algorithms simultaneously, where each algorithm begins with a new random number generator seed to select the initial guesses. Each set of runs therefore produces a scatter band of near optimal guesses for each parameter. The parameters which influence the cost function most are identified most tightly.

Figure 4 shows the progression of the best fitness values out of the population at each generation. The results are shown in Figure 5. The solid line in each figure denotes the true value.

The noise covariance ratio parameter couples only very weakly to the cost function and displays an almost random distribution until the physical coefficient estimates sufficiently converge. Therefore a two-step estimation procedure is required, where the noise ratio is allowed to remain free until physical coefficients have converged. The physical coefficients are then fixed while the noise ratio is estimated.

This methodology clearly demonstrates convergence. Twenty iterations of the genetic algorithm were run. Table 1 tabulates the parameter estimates.

Table 1 Estimated Parameters, Simulation Study   

<table><tr><td>Parameters</td><td>θo</td><td>θo</td><td>std</td></tr><tr><td>lift curve slope, a</td><td>5.73</td><td>5.72</td><td>3.98e-4</td></tr><tr><td>inflow equivalent cylinder height, hhnd</td><td>0.46</td><td>0.46</td><td>2.23e-4</td></tr><tr><td>inflow wake rigidity factor, wrf</td><td>2.0</td><td>2.0</td><td>1.34e-4</td></tr><tr><td>trim flap angle, βo</td><td>0.02</td><td>0.02</td><td>4.99e-7</td></tr><tr><td>trim main rotor pitch angle, to</td><td>0.05</td><td>0.0497</td><td>9.75e-6</td></tr><tr><td>trim inflow velocity, v0</td><td>0.02</td><td>0.0196</td><td>2.61e-6</td></tr><tr><td>lag damper constant, Cs</td><td>5.0</td><td>4.978</td><td>7.7e-3</td></tr><tr><td>lag spring constant, Ks</td><td>75.0</td><td>75.0</td><td>7.06e-2</td></tr><tr><td>flap spring constant, Kβ</td><td>45.0</td><td>44.92</td><td>6.3e-3</td></tr><tr><td>fuselage cross-moment of inertia, Ixx</td><td>30,000</td><td>30,035</td><td>4.98</td></tr><tr><td>tail rotor thrust factor, KTR</td><td>1.0</td><td>0.99</td><td>9.35e-4</td></tr><tr><td>covariance ratio, process/measurement, NR</td><td>1.0</td><td>0.97</td><td>0.11</td></tr><tr><td>process noise time constant, τ</td><td>-1.0</td><td>-0.99</td><td>1.8e-3</td></tr></table>

图片摘要：该图主要展示 1 Estimated Parameters, Simulation Study。
![](images/9d40b9273e26b0bc9eb2c3bf7362cea3dfcc44a292fa6ecfa3b91698bbd5dbd0.jpg)

图片摘要：该图主要展示 1 Estimated Parameters, Simulation Study。
![](images/0f73a39bc614a4d00ac7a9428e49477d39e90f5b835103fd8a2c0ab43b6fcbaf.jpg)

图片摘要：该图主要展示 1 Estimated Parameters, Simulation Study。
![](images/4f825b0225e344ce3b800e4a43197c24563cd43a34b5072d6754ba1db0f11d93.jpg)

图片摘要：该图片展示了Control Law/Concept Evaluation Envelope Expansion相关内容。
![](images/7761b7b82c6a708f31e689825cadc353fce70fc7d23d23f499b5971dbabb1575.jpg)

图片摘要：该图片展示了Control Law/Concept Evaluation Envelope Expansion相关内容。
![](images/18519e835eb978e78beaf0fe74f5a04bea7809874ec447720d59c4545d4bc1c3.jpg)

图片摘要：该图片展示了Control Law/Concept Evaluation Envelope Expansion相关内容。
![](images/566fb1754e7e22058dbbe50ea25e92f332ece031fe655f01f96c1565a5684c28.jpg)

图片摘要：该图片展示了Control Law/Concept Evaluation Envelope Expansion相关内容。
![](images/55b62393f95d58b5c270c201a56eb3e0c4e48935b0f438a045151d36220e6762.jpg)

图片摘要：该图片展示了Control Law/Concept Evaluation Envelope Expansion相关内容。
![](images/3a35b0338faec7e6c5d0aa976b5dd61dcc47adebb6af5756213126ce763afe46.jpg)

图片摘要：该图片展示了Control Law/Concept Evaluation Envelope Expansion相关内容。
![](images/2e87de4a9c81459c09a39017f2b8d9c4019d8dff3e5c5b18185e057c229c6ba6.jpg)

图片摘要：该图主要展示 5 Simulation Identification Results。
![](images/c6a69437fc28c2df9437b5891e5d6649c2af3b2990adb968aad30f1192e315ac.jpg)

图片摘要：该图主要展示 5 Simulation Identification Results。
![](images/157adc243a61336dcaa950a3e1775b3495aa0bde3a613d5883351e09b2243d2b.jpg)

图片摘要：该图主要展示 5 Simulation Identification Results。
![](images/573dce0c20da8dc959c6850d1b187e649719236927a030306b0f51430a976f69.jpg)

图片摘要：该图主要展示 5 Simulation Identification Results。
![](images/3847440848ea87d7470fc5104616ef6944132cbea98c93e30bf96d5566742078.jpg)  
Figure 5 Simulation Identification Results

# Flight Test Identification Results

Data consistency checks ensure that errors in data collection do not interfere with the estimation procedure. The requirements for this step were minimal in this study, since this estimation methodology requires only rate and attitude information. Consistency was checked by integrating accelerations and rates, and ensuring that sensor attitudes and rates match the integrated rates and attitudes.

The flight test data was processed by 1) applying a bandpass filter, and 2) decimating the data from $80\mathrm{Hz}$ to $8\mathrm{Hz}$ . The filter passband was from 0.5 to $2.5\mathrm{Hz}$ (3.1416 to 15.708 rad/sec). The lower bound corresponds to the beginning frequency of the frequency sweep input used to drive the system, and the upper bound is imposed to exclude the first fuselage bending mode at $3.4\mathrm{Hz}$ .

The flight test identification parametrization was modified to reflect information available from comparison between test and theoretical responses generated from the analytic model using nominal parameter values. The parameter list used in flight test identification runs is shown in Table 2. The modifications are explained below.

The parametrization of body inertias accounts for significant differences between theory and test in rigid body response, especially in the roll axis. Further, due to significant differences in

cross-axis predictions, the roll and yaw rigid body responses could not be simultaneously satisfied. Therefore, yaw axis parameters were eliminated, and the identification scheme therefore attempts to fit pitch and roll responses only. This is permissible since for small motions about hover, yaw rate does not couple with main rotor cyclic multiblade coordinates and has no effect on pitch and roll responses in the rotor/body frequency region.

The inflow equivalent cylinder height (hhnd) is related to the main rotor dynamic inflow time constant. This parameter had no effect on the cost function in the bandpass frequency region used in this study. Therefore a quasistatic main rotor inflow formulation was used and this parameter was dropped.

The process noise dynamics, parametrized by a first order time constant, was also eliminated. This parameter is uniquely identifiable apart from the noise power ratio only if the time constant falls within the bandpass frequency range, and was found to have no effect on the cost function.

The identification run was carried out using flight test data from hover, with primary excitation into roll cyclic. The analytic model, parametrized as given in Table 2, was driven by main rotor pitch and roll cyclic and tail rotor pedal. The likelihood function was formed using pitch and roll rates only.

Table 2 Estimated Parameters, Flight Test   

<table><tr><td>Parameters</td><td>θo</td><td>std</td><td>bounds</td><td>nominal</td></tr><tr><td>scale factor, fuselage roll moment of inertia, Ix</td><td>0.44</td><td>0.011</td><td>0.35-1.0</td><td>1.0</td></tr><tr><td>scale factor, fuselage pitch moment of inertia, Iy</td><td>1.15</td><td>0.033</td><td>0.7-1.3</td><td>1.0</td></tr><tr><td>lift curve slope, a</td><td>8.4</td><td>0.066</td><td>5-10</td><td>5.73</td></tr><tr><td>inflow wake rigidity factor, wrf</td><td>8.0</td><td>0.23</td><td>2-11</td><td>2.0</td></tr><tr><td>trim flap angle, βo</td><td>0.162</td><td>0.0013</td><td>0.05-0.25</td><td>0.0848</td></tr><tr><td>trim main rotor pitch angle, to</td><td>0.0172</td><td>0.00016</td><td>0.005-0.15</td><td>0.1304</td></tr><tr><td>trim inflow velocity, v0</td><td>0.048</td><td>0.0007</td><td>0.01-0.1</td><td>0.0613</td></tr><tr><td>lag damper constant, Cc</td><td>5.5</td><td>0.10</td><td>4-10</td><td>9.5</td></tr><tr><td>lag spring constant, Kc</td><td>85.0</td><td>0.735</td><td>0-100</td><td>0</td></tr><tr><td>flap spring constant, Kβ</td><td>16</td><td>1.34</td><td>0-20</td><td>0</td></tr><tr><td>noise covariance ratio, NR</td><td>-</td><td>-</td><td>0.001-0.1</td><td>-</td></tr></table>

The initial choice of boundary limits on each parameter defines the parameter space to be searched in the identification algorithm. The bounds applied to each parameter are shown in Table 2; in each case, the bounds are chosen to include the nominal value.

Table 2 shows the identification results for flight test data. It was found that the noise ratio parameter did not converge while the remaining physical coefficients did, indicating that relative to the aeromechanical coefficients, noise powers affect the cost function only very weakly.

The correlation with flight test data using the identified parameters is shown in Figure 6, where the roll axis response is correlated with the data set used in the identification, and the pitch axis response is an independent check. The roll axis correlation shows clear improvement in model correlation using identified coefficients. The low frequency gain prediction has been corrected through the inertia adjustment, and the notch in gain response due to the coupled lag/body response has been corrected.

The differences between identified and nominal parameters can provide physical insight into rotor phenomena when analytic explanations can be found for parameter differences. The identified parameters for lift curve slope, $a$ , and wake rigidity factor, $wrf$ , have produced significant improvement in model response, indicating a possible requirement for refinement of the aerodynamic theory used in the model. The identified parameters for main rotor spring and damping constants indicate necessary refinements in the prediction of frequency and damping of blade motion. A model improvement for blade in-plane dynamics is now presented.

# Modeling Blade Elasticity

The identification procedure has resulted in estimated values for rotor blade spring and damping parameters which are different from nominal values. The nominal mechanical damper value may be assumed to be known since it can be independently verified through available data.

A procedure for modeling blade elasticity is presented which accurately accounts for differences between nominal and estimated values for inplane motion frequency and damping. The method of assumed modes is used to model the case of a flexible beam with damper and spring constraints. This procedure is first demonstrated on a nonrotating beam, for which an exact solution can be obtained. The method of assumed modes will be shown to be a good approximation of the exact solution. This approximate solution can then be used in the flexible beam analysis in the analytic hover helicopter model. The beam formulations for both rotating and nonrotating blades with both spring and damper constraints at the root is given in detail in Appendices A and B.

Approximate solution methods such as the method of assumed modes display convergence toward the analytic solution as more assumed mode shapes are added to the set of basis functions. The first approach to the lagwise bending problem was to use increasing numbers of mode shapes that fulfilled the boundary conditions for a hinged beam. However, with this approach, convergence was not achieved after even after using 5 assumed modes. In order to avoid using an unacceptably large number of basis polynomials in the model, an alternative approach using a combination of modes that satisfy hinged and cantilever boundary conditions was used.

Figure 7 illustrates the assumed modes solution method using both the nonrotating and rotating beam formulations. For a nonrotating beam with spring and damper constraints, an exact expression for the beam eigenvalues is available and is given in detail in Appendix B. The analytic eigenvalue equation is solved numerically. In this case, the root finding problem was converted into a function optimization problem and solved using the genetic algorithm. This solution to the exact formulation is shown against approximate solutions in Figure 7. The approximate solution using the Lagrangian approach, when using only basis functions which fulfill hinged beam boundary conditions, approach the exact solution slowly. With 4 hinged basis polynomials, the solution has not yet converged. However, the assumed modes approach with only one hinged plus one cantilever mode shapes matches

图片摘要：该图主要展示 7 illustrates the assumed modes solution method using both t。
![](images/4674b2722a04b9649daff23fd6ee902cb4ddcd839021344fe319bd7cdbfe59f0.jpg)  
Pitch Rate/B1S, Pitch Input

图片摘要：该图主要展示 7 illustrates the assumed modes solution method using both t。
![](images/52f6572ff1872eceab88e69a4b87f6575c2a6a5fc8d97e6040c00e47ac611da1.jpg)

图片摘要：该图主要展示 7 illustrates the assumed modes solution method using both t。
![](images/0468c8acdd6764d4d1f661ee338f64dcf87b0ee1ad19ad5e1cf1eb65b57a8405.jpg)  
Roll Rate/AIS, Roll Input

图片摘要：该图主要展示 6 Identified Model Validation。
![](images/a5712b712a4e05c521834617665e08bf6e7a1fbe0dd6756933fb016484a521aa.jpg)  
Figure 6 Identified Model Validation

图片摘要：该图主要展示 6 Identified Model Validation。
![](images/e980b5756ac20c74d5c4a52e8c1d65353f846cc746be32d969ee93cd5b92c32e.jpg)  
Nonrotating Beam

图片摘要：该图主要展示 6 Identified Model Validation。
![](images/dd66698db110eb1cf7b6e2a13e0fc3f9fd2b7beec2372d77368db40b8510ef1d.jpg)  
Rotating Beam   
Figure 7 Modal Solutions For Beam Equations

the analytic solution exactly. Convergence is demonstrated by the fact that addition of either hinged or cantilever mode shapes do not further change the eigenvalue solution.

Figure 7 then shows the convergence of the approximate solution for the rotating beam, for which there exists no known exact solution. Here, the sum of 2 hinged plus 2 cantilever modes is near convergence. The addition of either one more hinged or one more cantilever mode does not change the solution appreciably. The combination of 2 hinged plus 2 cantilever modes is chosen for model development as a good compromise between model order and accuracy of solution.

图片摘要：该图主要展示 7 then shows the convergence of the approximate solution for。
![](images/b825bb7d94ac4ebef2233daf7612ffb9fd80122a5165cc41846e7c845e027d31.jpg)  
Figure 8 Rotating Frame Lag Roots

Figure 8 shows the location of the rotating frame lag mode eigenvalues. The elastic blade model using two hinged and two cantilever mode shapes is used to show the progression of the root location as damper value is increased from zero to the nominal value. The predicted root location for the elastic model with the nominal damper constant agrees reasonably well with the predicted location for the rigid blade model using a fictitious spring and using identified spring and damper constants. The rigid blade model using nominal damper constant only (no spring) predicts a much higher damping and lower frequency than is indicated by test data.

# Conclusions

An analytically derived linear model of coupled rotor/body dynamics at hover has been validated against flight test data.

The analytic model with literal coefficients has been parametrized using 11 physically meaningful coefficients, including noise covariances. This model has been used to formulate a multi-input, multi-output likelihood function in the time domain. The analytic model is used to generate the state time histories. Only body rates are necessary in the cost function.

The likelihood function is globally maximized using the genetic algorithm approach, resulting in statistically optimal maximum likelihood parameter estimates.

The estimated parameters indicate that lag mode damping in flight is approximately one-half of the value expected from rigid blades.

The correct analytic prediction for lagwise motion is obtained using an elastic blade formulation. The flexible blade model was formulated using a normal mode approach and checked using the closed form solution for a nonrotating beam. The convergence results using assumed mode shapes indicate that the correct lagwise bending mode shapes are obtained using a combination of cantilever and hinged assumed modes.

# Acknowledgement

One of the authors (S. Hong) would like to thank Mr. Bill Twomey in the Dynamics Section at Sikorsky Aircraft for key discussions on the effect of blade flexibility on blade motion, Professor P. M. Schultheiss at Yale University for insights into the identification framework, and Dr. Richard Williams at the United Technologies Research Center for generously supporting this research effort.

Part of this work was carried out at Princeton University under NASA Ames grant NAG2-561.

# Appendix A. Modeling Blade Elasticity

Equation (A.1) gives the in-plane bending equation for a rotating beam. The derivation can be

found in Bramwell (1976), and in Johnson (1980). This partial differential equation relates the moments due to the inertial, centrifugal, and aerodynamic forces to the moment expression from engineering beam theory.

$$
\begin{array}{l} \frac {\partial^ {2}}{\partial r ^ {2}} \left[ E I \frac {\partial^ {2} Y}{\partial r ^ {2}} \right] - \frac {\partial}{\partial r} \left[ G (r) \frac {\partial Y}{\partial r} \right] + \\ m \left[ \frac {\partial^ {2} Y}{\partial t ^ {2}} - \Omega^ {2} Y \right] = 0 \tag {A.1} \\ \end{array}
$$

All quantities are understood to refer to lagwise bending motion. Here, $G(r)$ is the centrifugal tension force at a point at a distance $r$ from the hub center, $E$ is the modulus of elasticity, $I$ is the lagwise area moment, and $\Omega$ is the rotor rotational velocity.

The boundary conditions for a hinged blade are:

At the hinge:

$$
\begin{array}{l} Y (e) = 0 \\ E I \frac {\partial^ {2} Y}{\partial r ^ {2}} = m o m e n t = 0 \\ \end{array}
$$

At the tip:

$$
\begin{array}{l} E I \frac {\partial^ {2} Y}{\partial r ^ {2}} = 0 \\ \frac {\partial^ {3} Y}{\partial r ^ {3}} = \text {s h e a r f o r c e} = 0 \\ \end{array}
$$

There is no known analytic solution for Equation (A.1) due to the presence of the centrifugal term. A solution based on the method of assumed modes is presented.

Let the lagwise displacement be of the form

$$
Y (x, t) = R \sum_ {n} \phi_ {n} (x) q _ {n} (t) \tag {A.2}
$$

where $\mathbf{R} =$ blade length. This solution method follows the method of separation of variables. $\phi_n(x)$ are a sequence of functions, not necessarily orthogonal, which approximate the expected blade shape and which satisfy the blade boundary conditions.

Substituting into Equation (A.1),

$$
\begin{array}{l} \frac {\partial^ {2}}{\partial x ^ {2}} E I \sum_ {n} q _ {n} \frac {\partial^ {2}}{\partial x ^ {2}} \phi_ {n} - R ^ {2} \frac {\partial}{\partial x} G \sum_ {n} q _ {n} \frac {\partial}{\partial x} \phi_ {n} + \\ \sum_ {n} \left(\ddot {q} _ {n} - \Omega^ {2} q _ {n}\right) \phi_ {n} R ^ {4} m = 0 \tag {A.3} \\ \end{array}
$$

Multiply Equation (A.3) by $\phi_{m}$ and integrate from $\frac{e}{R} < x < R$ , or $\overline{e} < x < 1$ where $\overline{e}$ is understood to be a nondimensional offset value.

This gives

$$
\begin{array}{l} \sum_ {n} q _ {n} \int_ {\varepsilon} ^ {1} \phi_ {m} \frac {\partial^ {2}}{\partial x ^ {2}} E I \phi_ {n} ^ {\prime \prime} d x - R ^ {2} \sum_ {n} q _ {n} \int_ {\varepsilon} ^ {1} \phi_ {m} \frac {\partial}{\partial x} G \phi_ {n} ^ {\prime} d x \\ + R ^ {4} \sum_ {n} \left(\ddot {q} _ {n} - \Omega^ {2} q _ {n}\right) \int_ {\varepsilon} ^ {1} m \phi_ {m} \phi_ {n} d x = 0 (A. 4) \\ \end{array}
$$

Integrating each term by parts, the first term gives

$$
\begin{array}{l} \sum_ {n} q _ {n} \int_ {\pi} ^ {1} \phi_ {m} \frac {\partial^ {2}}{\partial x ^ {2}} E I \phi_ {n} ^ {\prime \prime} d x = \left[ \sum_ {n} q _ {n} \phi_ {m} \frac {\partial}{\partial x} E I \phi_ {n} ^ {\prime \prime} \right] _ {\varepsilon} ^ {1} \\ - \left[ \sum_ {n} q _ {n} \phi_ {M} ^ {\prime} E I \phi_ {n} ^ {\prime \prime} \right] _ {\bar {z}} ^ {1} + \int_ {\bar {z}} ^ {1} \sum_ {n} q _ {n} E I \phi_ {n} ^ {\prime \prime} \phi_ {m} ^ {\prime \prime} d x \\ = R D \sum_ {n} \phi_ {n} ^ {\prime} \phi_ {m} ^ {\prime} \dot {q} _ {n} + \int_ {\pi} ^ {1} \sum_ {n} q _ {n} E I \phi_ {n} ^ {\prime \prime} \phi_ {m} ^ {\prime \prime} d x \tag {A.5} \\ \end{array}
$$

Equation (A.4) was obtained using the boundary conditions for the hinged blade, along with the end constraint imposed by the damper, which is given by

$$
\begin{array}{l} E I \left. \frac {\partial^ {2} Y}{\partial r ^ {2}} \right| _ {r = e} = - D \left. \frac {\partial^ {2} Y}{\partial t \partial r} \right| _ {r = e} = \\ - D R \sum_ {n} \frac {\partial \phi_ {n}}{\partial x} \frac {\partial q _ {n}}{\partial t} \Big | _ {x = \frac {e}{R}} \\ \end{array}
$$

where $D =$ damping constant.

Similarly, the second term gives

$$
R ^ {2} \sum_ {n} q _ {n} \int_ {\tau} ^ {1} \phi_ {m} \frac {\partial}{\partial x} G \phi_ {n} ^ {\prime} d x =
$$

$$
- R ^ {2} \sum_ {n} q _ {n} \int_ {\theta} ^ {1} G \phi_ {n} ^ {\prime} \phi_ {m} ^ {\prime} d x \tag {A.6}
$$

Using Equations (A.4) through (A.6).

$$
\begin{array}{l} \int_ {\varepsilon} ^ {1} \sum_ {n} q _ {n} E I \phi_ {n} ^ {\prime \prime} \phi_ {m} ^ {\prime \prime} d x + R D \sum_ {n} \phi_ {n} ^ {\prime} \phi_ {m} ^ {\prime} \dot {q} _ {n} \\ + R ^ {2} \sum_ {n} q _ {n} \int_ {\mathbb {Z}} ^ {1} G \phi_ {n} ^ {\prime} \phi_ {m} ^ {\prime} d x \\ + R ^ {4} \sum_ {n} \left(\ddot {q} _ {n} - \Omega^ {2} q _ {n}\right) \int_ {\Sigma} ^ {1} m \phi_ {m} \phi_ {n} d x = 0 \\ \end{array}
$$

To evaluate this, nondimensionalize by $m\Omega^2 R^4$ and collect terms, which results in

$$
A _ {n m} \dot {q} _ {n} + D _ {n m} \dot {q} _ {n} + B _ {n m} q _ {n} = 0
$$

where

$$
A _ {n m} = \int_ {\pi} ^ {1} \left[ \frac {R ^ {4} m}{m \Omega^ {2} R ^ {4}} \phi_ {n} \phi_ {m} \right] d x
$$

$$
D _ {n m} = \frac {R D \Omega}{m \Omega^ {2} R ^ {4}} \phi_ {x} ^ {\prime} \phi_ {m} ^ {\prime}
$$

$$
B _ {n m} = \int_ {\pi} ^ {1} \left[ \frac {E I}{m \Omega^ {2} R ^ {4}} \phi_ {n} ^ {\prime \prime} \phi_ {m} ^ {\prime \prime} + \frac {R ^ {2} G}{m \Omega^ {2} R ^ {4}} \phi_ {n} ^ {\prime} \phi_ {m} ^ {\prime} - \phi_ {n} \phi_ {m} \right] d x
$$

# Basis Functions For Assumed Mode Shapes

Polynomials are used as the basis functions, $\phi_n(x)$ . Two sets of polynomials, meeting the necessary boundary conditions for hinged-free and cantilever-free beams, were used in this study. They are:

hinged-free:

$$
\phi (x) = x
$$

$$
\phi (x) = x ^ {6} - 2 x ^ {5} - \frac {5}{6} x ^ {4} + \frac {1 0}{3} x ^ {3} + x
$$

cantilever-free:

$$
\phi (x) = x ^ {4} - 4 x ^ {3} + 6 x ^ {2}
$$

$$
\phi (x) = x ^ {5} - 1 0 x ^ {3} + 2 0 x ^ {2}
$$

Since these polynomials meet boundary conditions at $x = 0$ and at $x = I$ , and the blade formulation is integrated from $x = e$ to $x = I$ , the basis polynomials are transformed to new coordinates, where

$$
x ^ {\prime} = (1 - \bar {e}) x + \bar {e}.
$$

With this coordinate transformation, the new set of polynomials, which now fulfill the necessary boundary conditions at the hinge offset and at the blade tip, are now

hinged-free:

$$
\begin{array}{l} \phi (x) = x - \bar {e} \\ \phi (x) = 1. 4 8 x ^ {6} - 3. 3 3 x ^ {5} - 0. 1 2 x ^ {4} + 4. 2 x ^ {3} - \\ 0. 7 9 x ^ {2} + 1. 1 2 x - 0. 0 7 \\ \end{array}
$$

cantilever-free:

$$
\begin{array}{l} \phi (x) = 1. 3 x ^ {4} - 5. 2 x ^ {3} + 7. 8 x ^ {2} - 0. 9 2 x + 0. 0 3 \\ \phi (x) = 1. 3 9 x ^ {5} - 0. 4 4 x ^ {4} - 1 2. 1 1 x ^ {3} + \\ 2 5. 1 0 x ^ {2} - 3. 0 3 x + 0. 0 9 \\ \end{array}
$$

# Appendix B. Exact Equations Of Motion For A Nonrotating Beam

The modal analysis assumes that the beam displacement is written as a sum of modal displacements:

$$
Y (x, t) = R \sum_ {n} \phi_ {n} (x) q _ {n} (t)
$$

To find the exact analytic solution in the case of root constraint with both spring and damper, note that the boundary conditions are given by

$$
\phi (0) = 0
$$

$$
\phi^ {\prime \prime} (O) = \left[ \frac {K R}{E I} + i \lambda \frac {D R}{E I} \right] \phi^ {\prime} (O)
$$

$$
\phi^ {\prime \prime} (I) = 0
$$

$$
\phi^ {\prime \prime} (I) = 0
$$

where $\mathbf{K}$ and $\mathbf{D}$ are spring and damper constants and all quantities are understood to refer to lagwise motion and are defined as in Appendix A.

These boundary conditions are satisfied by writing the mode summation equation as

$$
\phi (x) = \phi_ {F} (x) + \left[ \frac {K R}{E I} + i \lambda \frac {D R}{E I} \right] \frac {\phi_ {F} ^ {\prime} (0)}{\phi_ {C} ^ {\prime \prime} (0)} \phi_ {C} (x)
$$

where $\phi_F(x)$ and $\phi_C(x)$ refer to hinged and cantilever mode shapes.

The hinged end mode shape solutions are given by

$$
\phi_ {F} (x) = \cos (A) \sinh (A x) + \cosh (A) \sin (A x)
$$

$$
\phi_ {F} (0) = 0
$$

$$
\phi_ {F} ^ {\prime} (0) = A [ \cos (A) + \cosh (A) ]
$$

$$
\phi_ {F} ^ {\prime \prime} (0) = 0
$$

$$
\phi_ {F} ^ {\prime \prime} (1) = A ^ {2} [ \cos (A) \sinh (A) - \cosh (A) \sin (A) ]
$$

$$
\phi_ {F} ^ {\prime \prime} (I) = A ^ {3} [ \cos (A) \cosh (A) - \cosh (A) \cos (A) ] ]
$$

The cantilever mode shape solutions are given by

$$
\phi_ {C} (x) = (\sin (A) - \sinh (A)) (\sin (A x) - \sinh (A x)) +
$$

$$
(\cos (A) + \cosh (A)) (\cos (A x) - \cosh (A x))
$$

$$
\phi_ {C} (0) = 0
$$

$$
\phi_ {C} ^ {\prime} (0) = 0
$$

$$
\phi_ {C} ^ {\prime \prime} (0) = - 2 A ^ {2} [ \cos (A) + \cosh (A) ]
$$

$$
\phi_ {C} ^ {\prime \prime} (I) = - A ^ {2} [ I + \cosh (A) \cos (A) ]
$$

$$
\phi_ {C} ^ {\prime \prime \prime} (I) = A ^ {3} [ (\sin (A) - \sinh (A)) (- \cos (A) - \cosh (A)) +
$$

$$
\left. \left(\cos (A) + \cosh (A)\right) \left(\sin (A) - \sinh (A)\right) \right]
$$

Now use these known solutions for hinged and cantilever mode shapes in the combined solution given above:

$$
\begin{array}{l} \phi (0) = 0 \\ \phi^ {\prime} (0) = \phi_ {F} ^ {\prime} (0) \\ \phi^ {\prime \prime} (0) = [ K + i \lambda D ] \left[ - \frac {1}{2 A} \right] \phi_ {C} ^ {\prime \prime} (0) \\ \phi^ {\prime \prime} (1) = \phi_ {F} ^ {\prime \prime} (1) + [ K + i \lambda D ] \left[ - \frac {I}{2 A} \right] \phi_ {C} ^ {\prime \prime} (1) \\ \phi^ {\prime \prime} (I) = A ^ {2} [ \cos (A) \sinh (A) - \cosh (A) \sin (A) + \\ \left[ \bar {K} + i \bar {D} \right] \left[ - \frac {I}{2 A} \right] \left[ - 2 A ^ {2} [ I + \cosh (A) \cos (A) ] \right] \\ \phi^ {\prime \prime} (I) = 0 \\ \end{array}
$$

where

$$
K = \frac {K R}{E I}
$$

and

$$
D = \frac {D R}{E I}
$$

The boundary condition at the tip gives the eigenvalue equation:

$$
\phi^ {\prime \prime} (I) = 0
$$

or

$$
\begin{array}{l} A ^ {2} [ \cos (A) \sinh (A) - \cosh (A) \sin (A) ] + \\ A [ K + i D ] [ I + \cosh (A) \cos (A) ] = 0 \\ \end{array}
$$

# References

Ballin, M. G., and Dalang-Secretan, M. (1991). Validation Of The Dynamic Response Of A Blade-Element UH-60 Simulation Model In Hovering Flight. J. of the American Helicopter Society, Vol. 36, no. 4.

Bramwell, A.R.S. (1976). Helicopter Dynamics. Edward Arnold Ltd., London, U.K.   
Curtiss, H.C. (1986). Stability and Control Modeling. Proceedings 12<sup>th</sup> European Rotorcraft Forum, Garmish Partenkirchen, Germany.   
Curtiss, H.C. and Zhao, X. (1988). A Linearized Model of Helicopter Dynamics Including Correlation With Flight Test. Paper presented at the 2nd International Conference on Rotorcraft Basic Research, College Park, MD.   
Diftler, M. A. (1988). UH-60A Helicopter Stability Augmentation Study. Paper presented at the 14th European Rotorcraft Forum, Milan, Italy.   
Goldberg, David E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning. Addison-Wesley Publishing Co., Reading, MA.   
Ham, N. D., Behal, B., and McKillip, R. M., Jr. (1983). Lag Damping Augmentation Using Individual Blade Control. Vertica, Vol. 7, No. 4.   
Holland, John H. (1975). Adaptation in Natural and Artificial Systems. The University of Michigan Press, Ann Arbor, Michigan.   
Johnson, W. (1980). Helicopter Theory. Princeton University Press, Princeton, New Jersey.   
Kaplita, T.K., Driscoll, J.T., Diftler, M.A., and Hong, S.W. (1989). Helicopter Simulation

Development By Correlation With Frequency Sweep Flight Test Data. AHS 45th Annual National Forum, Boston, MA.   
Kim, F. D., Celi, R., and Tischler, M. B. (1990). High-Order State Space Simulation Models Of Helicopter Flight Mechanics. 16th European Rotorcraft Forum, Glasgow, Scotland.   
Ljung, L. System Identification: Theory for the User. (1987). Prentice-Hall, Inc., Englewood Cliffs, NJ.   
Maine, R. E. and IIiff, K. W. (1985). Identification of Dynamic Systems - Theory and Formulation. NASA Reference Publication 1138.   
Mayo, J. R., Occhiato, J. J., and Hong, S. W. (1990). Helicopter Modeling Requirements For Full Mission Simulation And Handling Qualities. AHS 47th Annual National Forum.   
Milne, G. W. (1986). Identification of a Dynamic Model of a Helicopter from Flight Tests. Ph.D. Thesis, Stanford University.   
Starer, David (1990). Algorithms for Polynomial-Based Signal Processing. Ph.D. Thesis, Center For System Science, Yale University.   
Tischler, Mark B. (1987). Frequency-Response Identification of XV-15 Tilt-Rotor Aircraft Dynamics. Ph.D. Thesis, Stanford University.

# Session 4

# Understanding Visual Cues

图片摘要：该图片与Visual Cueing Aids for Rotorcraft Landings；Walter W. Johnson这部分内容相关。
![](images/78f9916aa5a66c23380658cc85dce84d707e8fb31aa1ccfc83ffef00bd6c7cf4.jpg)

# Visual Cueing Aids for Rotorcraft Landings

Walter W. Johnson

Rotorcraft Human Factors Research Branch

NASA Ames Research Center

Moffett Field, CA

Anthony D. Andre

Western Aerospace Laboratories, Inc.

NASA Ames Research Center

Moffett Field, CA

# ABSTRACT

The present study used a rotorcraft simulator to examine descents-to-hover at landing pads with one of three approach lighting configurations. The impact of simulator platform motion upon descents to hover was also examined. The results showed that the configuration with the most useful optical information led to the slowest final approach speeds, and that pilots found this configuration, together with the presence of simulator platform motion, most desirable. The results also showed that platform motion led to higher rates of approach to the landing pad in some cases. Implications of the results for the design of vertiport approach paths are discussed.

# INTRODUCTION

Rotorcraft landings in physically constrained environments, such as urban vertiports, present potential hazards not commonly faced by fixed-wing or rotorcraft landings at conventional airports. One major hazard is the presence of buildings or other obstructions beneath their glideslope and directly behind the landing pad. In such environments it is necessary for pilots to accurately maintain their assigned glideslope and to reliably regulate their speed so as to achieve zero velocity at the landing pad.

The present study examined the effect of different combinations of visual and motion information upon simulated descents to hover. Specifically, the study was designed to determine the effects upon performance and

subjective ratings of 1) three approach lighting configurations, and 2) the presence/absence of simulator motion. It was also designed to explore how theoretically significant types of optical and motion information combine to yield different deceleration and glideslope profiles.

# Optical Cues For Speed Control

Pilots in aircraft and aircraft simulators require information in order to accomplish their tasks. However, selecting what information to supply the pilot is not easy, especially since many potential information sources are costly (e.g., simulator motion) and/or may not provide much benefit in terms of training effectiveness, performance or flight safety (Andre and Johnson, 1992). Understanding the pilots' reactions to optical information in the environment during flight and in piloted flight simulation can lead to improved visual approach training procedures and may have an impact on the design of heliport approach paths.

There are three important optical variables that a pilot could use to control speed during the descent to hover. Optical Expansion Rate is the relative rate of growth in the optical size of the landing pad, and is proportional to the vehicle velocity divided by distance to the pad (i.e., physical closure rate). This optical variable provides information useful for deceleration since maintaining its value at or below some critical positive value will ensure that the vehicle arrives at the landing pad with zero touchdown velocity, with lower values yielding more gradual decelerations. Further, this cue is insensitive to altitude deviations. Figure 1a shows how constancy of optical expansion rate requires speed to be proportional to distance-to-go.

Optical Flow Rate is the angular velocity of surface elements in any one area of the field of view. This velocity in turn is proportional to vehicle velocity divided by the distance to the viewed surface, and is typically scaled in units of eye heights per second (Owen, Wolpert, and Warren, 1984). This is different from Optical Expansion Rate since that variable is defined with respect to contour expansion rate, while Optical Flow Rate is simply optical (angular) speed. When descending over a ground surface, deceleration can be governed by maintaining optical speed, at some locus in the field of view, at or below some critical positive value. (US Army training manuals instruct rotorcraft trainees to "make it look like a brisk walk" during landings. This is an explicit instruction to maintain a constant Optical Flow Rate). Figure 1b shows how constancy of angular flow rate requires speed to be proportional to altitude.

Finally, there is Optical Edge Rate, the frequency at which optical elements pass through some visual locale (e.g., the lower portion of the windscreen). For descents over a surface this is proportional to vehicle velocity divided by the spacing between the elements on that surface. When the elements are spaced apart evenly, this yields a frequency that is directly proportional to speed. To the extent that information about true speed is important in managing decelerations, this variable may prove valuable for speed regulation. Figure 1c shows how constancy of edge rate requires texture

elements and speed to be proportional to distance-to-go.

Previous research by Moen, DiCarlo and Yenni (1976) examined altitude, ground-speed and deceleration profiles of visual approaches for helicopters. One goal of their research was to define the mathematical relationships describing nominal visual deceleration profiles. However, the effects of visual cues in the environment were not examined. More recent research has specifically addressed the influence of visual environmental cues on vehicle deceleration control.

For example, Denton (1980), in a somewhat related context, examined the influence of ground texture spacing (i.e., optical edge rate information) on driver's control of forward speed. Using an automobile simulator, he found that gradually reducing the spacing between horizontal stripes on a simulated roadway surface resulted in drivers reducing their speed. He then applied this finding in a field study where he placed horizontal stripes with gradually reduced spacing across the roadway at a highway exit ramp. This resulted in a reduction of a previously high accident rated caused by excessive speeding upon exiting the highway to lower speed roads. Other research has shown edge rate and flow rate to have roughly equal impact on the perception of self-speed (Larish and Flach, 1990; Owen et al., 1984).

图片摘要：该图主要展示 1. Optical variables useful for controlling deceleration. a)。
![](images/10142a5001e26de6e6a13dd8105479bd71d10d98e610849476f6310df2de6448.jpg)  
Figure 1. Optical variables useful for controlling deceleration. a) constancy of optical expansion rate requires speed to be proportional to distance-to-go; b) constancy of angular flow rate requires speed to be proportional to altitude; c) constancy of edge rate requires texture elements and speed to be proportional to distance-to-go.

# Optical Cues for Glideslope Control

There are two important optical variables potentially useful for glideslope control: 1) Form Ratio, the angular optical height of the pad divided by its optical width, and 2) aim point Declination Angle, the optical angle subtended between the center of the landing pad and the horizon. If the pilot acts to keep either of these constant after the glideslope intercept, then he will still be on the initial glideslope (see Lintern and Liu, 1991 and Mertens, 1981, for a more complete discussion of these variables). Similarly, pilots can maintain a constant glideslope by simply keeping the image of the landing pad at a fixed point below the horizon.

# THE PRESENT STUDY

The present study examined visual approaches in a rotorcraft simulator with various approach lighting configurations, under platform motion and non-motion conditions. These configurations were designed to highlight the utility of one or more of the three types of optical information about vehicle speed discussed above.

In one condition, only the landing pad itself, together with the horizon line, was visible. For control of speed, this makes available closure rate information in the form of the relative rate of the optical expansion of the landing pad surface itself. The reciprocal of this value, called tau, is the time to arrival at the landing pad if present vehicle speed is kept constant. By either maintaining relative closure rate information at a constant value, or by not allowing it to exceed some critical value, a pilot would be ensured of arriving at the pad with zero velocity.

A second condition added two rows of regularly spaced approach lights extending out from the edges of the landing pad. Now, in addition to the closure rate information mentioned above, the optical motion of the lights passing beneath the simulated vehicle provide information, in the form of optical flow rate and optical edge rate, about vehicle speed. For descents along a given glideslope, flow rate will be proportional to speed divided by altitude. By maintaining flow rate at a constant value, or not allowing it to exceed some critical value, one will ensure arrival at the landing pad with zero velocity. For descents over regularly spaced

ground elements, optical edge rate is proportional to speed, but does not afford the pilot any simple available optical strategy for ensuring arrival at the pad with zero velocity. Similarly, there is no simple or obvious optical cue associated with the approach lights that a pilot can use to judge glideslope.

Finally, a third condition added a middle row of lights to the second condition configuration. This middle row light spacing was proportional to distance from the pad, so that the lights were spaced half as far apart when the distance to the pad was decreased in half (i.e., exponential). Here, the pilot could hold the edge rate associated with this middle exponential light string at or below some fixed value, and thus ensure arrival at the landing pad with zero velocity.

The impact of simulator platform motion upon descents to hover was also examined in the present study. Previous research has shown that the presence of flight simulator motion appears to help performance, but not transfer to the aircraft (Koonce, 1979; Lintern, 1987). Our interest here was in assessing if simulator motion interacted with the utility of the approach light patterns under investigation.

# METHOD

# Design

Five factors were manipulated in the present study: 1) Flight Control Instruction (undirected and directed), 2) Simulator Motion (moving and fixed), 3) Approach Lighting Pattern (no lights, linear lights, and exponential +linear lights), 4) Initial Closure Rate (slow vs. fast--see Figure 2), and 5) Initial Range (near vs. far--see Figure 2). These variables were factorial crossed in a $2 \times 2 \times 3 \times 2 \times 2$ within-subjects design. Pilots performed 2 repetitions of each of the 48 unique factorial combinations for a total of $96$ landing trials. An overview of the experimental design is shown in the top panel of Figure 2.

# Simulation Apparatus

All trials were performed in the Vertical Motion Simulator (VMS) at the NASA Ames Research Center. The VMS, shown in Figure 3, is a large motion-base simulator which utilizes a four-window computer-

图片摘要：该图主要展示 2. Experimental Design. Description of Factorial Structure (。
![](images/ba24b56d7c216f4594a442d2ddd7ac6d620f47d55953fd61b085de1c89b9ccd7.jpg)  
Figure 2. Experimental Design. Description of Factorial Structure (top panel) and of Flight Profiles (bottom panel).

图片摘要：该图主要展示 2. Experimental Design. Description of Factorial Structure (。
![](images/ad8f0ec4832b912ca35dcc10ce898735523726c82a68ac5352fcc2cc50f2a428.jpg)  
Figure 3. NASA's Vertical Motion Simulator

generated image system for displaying visual scenes to the pilot. The simulator was outfitted with a rotorcraft cab with conventional controls.

Vehicle Model. The experiment utilized a modified rotorcraft model with only two degrees of freedom: longitudinal and vertical. The three angles that describe the orientation of the vehicle and the lateral position were fixed at zero. Thus longitudinal velocity changes were achieved without pitching the aircraft. Physically, this situation would be realized with a helicopter that had an auxiliary x-force device to control longitudinal acceleration.

This simplification was made for several experimental reasons. First, since straight-in, decelerating approaches were of interest, the three lateral-directional degrees of freedom were unnecessary. Second, since the vertical field-of-view in the simulator was substantially less than in a typical helicopter, pitch-up maneuvers in simulation would result in a drastic loss of visual ground cues. Accordingly, to ensure that the approach lights

were always in view during the approach, pitch attitude and rate was held constant. The pilots had acceleration command in the longitudinal axis. Acceleration command was proportional to longitudinal center stick position, with a sensitivity of 5 ft/sec²/in. The longitudinal travel of the center stick was +/- 5 in.

The vertical axis dynamics were more complicated than the longitudinal axis. The collective sensitivity and the aircraft's vertical damping depended upon airspeed. The aircraft was also given a steep power required curve, so that as the helicopter slowed, increased collective was required. The combination of these dynamics made the vehicle sufficiently challenging to fly, thereby inhibiting the pilots from flying the task open-loop (i.e., essentially flying the vehicle without regard to the visual cues). Pilot comments indicated that while the vertical axis exhibited helicopter-like qualities, the longitudinal axis did not (due to the lack of pitching required to change speed).

# Visual Landing Configurations

As shown in Figure 4, Three visual landing scenes were examined: 1) no approach lights with only a landing pad present (None); 2) the landing pad plus two linear strings of equally spaced lights leading up to the landing pad (Regular); and 3) the landing pad, the two linear strings, and an exponentially spaced string of lights (Exponential).

图片摘要：该图主要展示 4. Approach light configurations。
![](images/d7a82b52946d6ed603011dde31688ce88dfcb15b817d43f19ef45d28b9f54ade.jpg)  
Figure 4. Approach light configurations.

Regular. The Regular configuration presented two rows of white approach lights in addition to a 100 ft x 100 ft landing pad and the horizon. These lights were aligned with the sides of the landing pad, spaced either 23 ft or 46 ft apart (a manipulation of light density used to affect initial edge rate), and extended out 5000 ft from the landing pad. The lights at 1610 and 805 ft out were green, while the rest of the lights were white, and the pilots were instructed to intercept the glideslope when these lights passed out of view at the bottom of their windscreen. They were instructed to use the first set of green lights when flying at the higher altitude (278 ft) and the second set of green lights when flying at the lower altitude (139 ft). The left panel of Figure 4 depicts this lighting configuration. The bottom panel of Figure 2 shows how the combination of initial altitude and positions of the intercept lights combined to yield a $6^{\circ}$ glideslope capture.

None. This configuration was similar to the Regular configuration, but the approach lights were truncated at 805 ft from the pad for the 139 ft initial altitude, and 1610 ft from the pad for the 238 ft initial altitude. The pilots were told to intercept the glideslope when the last approach light passed out of view, and thus during the descent to hover only the landing pad and the horizon were visible. This configuration, depicted in the middle panel of Figure 4, does not provide either Optical Flow Rate or Edge Rate information, but provides all of the other information contained in the Regular configuration.

Exponential. This configuration was similar to the Regular configuration with the addition of a third row of lights aligned with the center of the landing pad. These extended out either 816 ft or 1609 ft (depending on initial altitude), and were exponentially spaced such that the inter-light spacing was 0 at the threshold of the landing pad, 53.9 ft at 816 ft, and 106 ft at 1609 ft for conditions using the high-density light spacing, and 106.9 ft and 212 ft for the low-density light spacing (inter-light separation divided by distance to the landing pad was approximately 0.066). (For the low-density spacing every other light in the Exponential light array was removed, so that

inter-light spacing divided by distance to the landing pad was approximately 0.132). In both cases the lights in the center row were continued, using the final spacing found at 816 or 1609 ft so that the pilots would already be using the lights when they intercepted the glideslope. The pilots were again instructed to intercept the glideslope when the appropriate set of green lights passed from view. This configuration, depicted in the right panel of Figure 4, provides all of the information contained in the regular configuration, plus the exponential string of lights makes it possible to reach zero velocity by maintaining an edge rate for this middle row at or below some critical value. As in the other examples, the lower this critical value the milder the deceleration.

# Procedure

Each landing trial consisted of a cruise phase and an approach phase. The cruise phase, which lasted approximately 10 seconds, did not require manual control as the vehicle maintained its initial level attitude. During this phase, a set of linear lights was present extending from the initial position to the glideslope intercept lights, regardless of the approach light condition (see Figure 4 above). This was done to allow the pilots to determine any altitude deviations due to the collective trim.

The approach phase began when the pilot crossed the glideslope capture position. This is the point where the green glideslope intercept lights just passed out of the lower field-of-view. At this point, the pilot was instructed to intercept the 6 deg glideslope down towards the center of the landing pad. The trial ended when the pilots reached a point approximately 15 ft AGL with the VTOL sign in their view.

The 96 experimental trials were completed over 4-6 sessions. Simulator motion and flight control instruction conditions were blocked between groups of 12 trials, while initial position and approach light pattern were counterbalanced and randomized within each block of 12 trials.

Following each trial, pilots were given feedback on their glideslope variation only.

Instruction. This task was performed under two sets of flight control instructions. In the undirected trials, the pilots were instructed to perform the approach in a way that was "comfortable" or "normal" for them. In the directed trials, the pilots were instructed to maintain a velocity profile that was proportional to their distance from the pad.

Subjective Ratings. Test pilots are trained to fly to some specified degree of performance and then judge difficulty in terms of the effort necessary to attain that degree of performance (e.g., Cooper-Harper Ratings). To this end test pilots generally want that level of performance to be made explicit (e.g., do not deviate more than $\pm 10$ ft in altitude). However, when exploring flight performance on tasks where no standardized measure of goodness exists, or even where it may be presumed to vary across pilots, this is a difficult method to implement.

In this situation we can only try to use the inverse method, and require pilots to fly to some fixed level of effort, and then have them judge difficulty in terms of what they see as good flight performance. This is what we required in this study, defining the level of effort as "flying as well as possible". Thus difficulty (which we called "doability" to focus the pilots on task constraints) was judged in terms of performance variations relative to this fixed high level of effort. In addition we also asked pilots to judge their own performance in terms that took into account the "doability" of the task. Thus, average performance on a difficult task should get the same performance rating as good performance on a more simple task. If the pilots could truly distinguish these ratings, then the performance ratings should not vary as a function of the doability ratings (i.e., task condition).

Pilots were asked to provide the two subjective ratings, each on a 7-point scale, following each trial. For the doability (difficulty) rating, we asked, "how difficult was the task, independent of how well you performed?" The performance rating was to be considered relative to the doability rating. Here we asked, "given the doability of the task, how well did you perform?"

Practice. Each pilot received a practice session of 12 landing trials under motion, undirected conditions. Before the practice session, each pilot was given a set of instructions which explained the various approach conditions and experimental procedures. In addition, the visual information afforded by each approach light pattern, in the form of edge rate and closure information, was described.

# Subjects

Six NASA helicopter test pilots participated in the experiment. Each had previous experience in the VMS.

# RESULTS

# Dependent Measures

Only the data from the undirected trials (where the pilots were free to choose their own approach speed) were analyzed to date.

Subjective Ratings. Prior to analysis normalized subjective difficulty and performance ratings $(\mathsf{NR}_{\mathbf{i}})$ were computed for each subject using the equation

$$
N R _ {i} = \frac {R _ {i} - M _ {R}}{S D _ {R}}
$$

where $\mathbf{R}_{\mathrm{i}}$ is the rating given by the subject, $\mathbf{M}_{\mathbb{R}}$ is the mean difficulty or performance rating given by that subject, and $\mathbf{SD}_{\mathbb{R}}$ is the standard deviation of the ratings given by the subject. This transformation was used to adjust for individual differences in the amount of the rating scale used by the pilots to make their judgments.

Performance Data. For each trial the descent trajectory was divided into 100 foot segments beginning 2600 ft from the pad for the far initial range trials, and at 1300 ft from the pad for the near initial range trials. This yielded 26 segments in the first case and 13 segments in the latter case. Since no approach lights would have been within view, and final adjustments to hover position were not of immediate interest, data in the final segment was not included beyond the point at which the front of the landing pad was not visible. Within each

segment, mean velocity, glideslope, and closure rate were calculated.

# Subjective Ratings Analysis

A 2 (Replication) x 2 (Initial Closure Rate) x 2 (Initial Range) x 2 (Motion) x 3 (Approach Lighting) repeated measures analysis of variance (ANOVA) was used to analyze the Normalized Difficulty and Performance ratings.

The analysis of the Difficulty ratings yielded statistically significant main effects for Initial Range $(\mathbf{F}(1,4) = 21.221, \mathbf{p} = .01)$ and for Motion $(\mathbf{F}(1,4) = 35.144, \mathbf{p} = .004)$ , and a statistically significant Range x Approach Lighting interaction $(\mathbf{F}(2,8) = 10.533, \mathbf{p} = .006)$ . Figure 5 shows that the presence of approach lighting also led to the task being judged as easier, although follow-up tests showed that the differences between ratings of the Exponential and Regular lighting configurations were not statistically significant. It also shows that trials with longer Initial Ranges were judged as more difficult, particularly when approach lights were absent. This pattern is not surprising since, at longer ranges to the pad, the absolute (not relative) rates of optical expansion are lower, and therefore probably less discernible. Figure 6 shows that trials with a moving platform were reliably rated as being less difficult, although this was not a very large effect.

The analysis of the Normalized Performance ratings yielded a statistically significant main effect for Initial Closure Rate $(\mathbf{F}(1,4) = 9.97, \mathbf{p} = .034)$ and a statistically significant Trial x Initial Closure Rate x Initial Range x Approach Lighting interaction $(\mathbf{F}(2,8) = 7.924, \mathbf{p} = .013)$ . The effect of initial closure rate (not depicted) showed that the pilots rated their performance as lower on trials with high initial closure rates. The four way interaction is difficult to interpret.

Squared correlations of the Performance and Difficulty ratings yielded $\mathbf{r}^2$ measures of .43, .43, .15, .10, and .003, showing that three of the five pilots succeeded well in keeping the estimates independent, while the other two had some problems in doing this. Together, these show that the pilots were moderately successful in separating task difficulty and performance contributions in making their judgements.

图片摘要：该图主要展示 5. Average normalized difficulty ratings as a function of ap。
![](images/4ec7304212779c8745b6a6ceb76ab2f99354de520fec40339d483a2f8081e28d.jpg)  
Figure 5. Average normalized difficulty ratings as a function of approach lighting and initial range for undirected descents to hover.

图片摘要：该图主要展示 5. Average normalized difficulty ratings as a function of ap。
![](images/d5292441aae53765e87d55b6cfa497c418e219eea3a68a96680ea9379138777a.jpg)  
Figure 6. Average normalized difficulty ratings as a function of simulator platform motion for undirected descents to hover.

# Performance Analysis

2 (Replication) x 2 (Motion) x 3 (Approach Lighting) x 13 (Segment) repeated measures multivariate analyses of variance (MANOVAs) were used to analyze glideslope and relative closure rate (i.e., ground approach velocity divided by distance-to-go) for the self-directed descents for each of the two initial closure rates in the near initial range condition. Similar analyses using 26 segments were conducted for the two initial closure rates in the far initial range condition. Where appropriate, Huynh-Feldt adjusted degrees of freedom were used to compensate for correlated data in the repeated measures (due primarily to the correlation of measures between adjacent trajectory segments).

Glideslope Analysis. Table 1 shows all statistically significant $(p < .05)$ effects on glideslope. In addition to significant variations in glideslope across Segments for all four types of descents (refer to Figure 2, top panel), there were also significant effects involving the Approach Lighting factor in all four types of descents, and significant effects of Motion in all but the Type C descent.

Figures 7-10 show the glideslope profiles as a function of Motion (left panels) and Approach Lighting (right panels) for all four initial conditions. All figures also show an increase in glideslope with proximity to the landing pad (where distance-to-go approaches 0). This is not unexpected since an approach to hover at some distance above the landing pad will, necessarily, lead to increasing glideslopes as measured from the center of the landing pad. All four show the presence of motion yielded a higher glideslope during the final portions of the descent (upper panels), although this is not easily seen in the figures plotting height as a function of distance-to-go (lower panels). In addition, only the approaches from the farther range (types "B" and "D" descents--Figures 8

and 10) yielded statistically significant Motion x Segment interactions.

The absence of approach lighting ("None" condition) led to consistently higher glideslopes in all four conditions, with no consistent direction to the difference in average glideslope of the Regular and Exponential Approach Lighting patterns (i.e., the Regular pattern led to a higher average glideslopes in conditions A and C, and a lower average glideslope in condition B, with the glideslopes for the two being about equal in condition D).

Finally, there were two statistically significant interactions involving both Approach Lighting and Motion in Type B descents. These were an Approach Lighting x Motion interaction, and an Approach Lighting x Motion x Segment interaction. Figure 11 shows that the two-way interaction was due primarily to motion leading to an increased glideslope in the presence of the Exponential pattern, and to a decreased glideslope without approach lighting. The three way interaction (not shown) was due to high variance across segments in the no lights condition.

Table 1. Statistically Significant Effects Upon Glideslope by Descent Type   

<table><tr><td>EFFECTS</td><td>Type A Descents</td><td>Type B Descents</td><td>Type C Descents</td><td>Type D Descents</td></tr><tr><td>Replication</td><td></td><td>F(1,4) = 14.2p = .0197</td><td></td><td></td></tr><tr><td>Lights</td><td>F(2,8) = 10.5p = .0058</td><td>F(2,8) = 6.06p = .025</td><td>F(2,8) = 10.4p = .0059</td><td></td></tr><tr><td>Path Segment</td><td>F(2,15,8.59) = 69.7p &lt; .0001</td><td>F(1.58,6.3) = 23.9p = .0015</td><td>F(5.84, 23.6) = 120.3p = &lt; .0001</td><td>F(2.16,8.62) = 37.8p &lt; .0001</td></tr><tr><td>Motion x Lights</td><td></td><td>F(2,8) = 5.1p = .0374</td><td></td><td></td></tr><tr><td>Motion x Segment</td><td></td><td>F(3.75,14.98) = 3.7p = .0293</td><td></td><td>F(5.96,23.84) = 3.8p = .008</td></tr><tr><td>Lights x Segment</td><td>F(3.8,15.21) = 3.97p = .0224</td><td></td><td></td><td>F(10.79,43.17) = 2.4p = .021</td></tr><tr><td>Motion x Lights x Segment</td><td></td><td>F(6.51,26.06) = 3.3p = .0129</td><td></td><td></td></tr></table>

图片摘要：该图主要展示 1. Statistically Significant Effects Upon Glideslope by Desc。
![](images/c8c2aead286650933e1834addae17e074f1a48e612752c3fa5aa03d6f7cfd82d.jpg)  
- Moving Base   
Fixed Base

图片摘要：该图主要展示 1. Statistically Significant Effects Upon Glideslope by Desc。
![](images/fee3e15c47c5c0b8b5e1666dfaa37655b2545820793bb8c1ca08eee809394e84.jpg)

图片摘要：该图主要展示 7. Average Glideslope as a Function of Motion and Lighting C。
![](images/43ba802b8b2b84403a391e4bacca1afcc74aef4b3d53b20e63f24b256ed329ae.jpg)  
- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 7. Average Glideslope as a Function of Motion and Lighting C。
![](images/1f840c9ee158dc3b67af8edbfe5191dbb6262a38ea39211967943130d9242a0c.jpg)  
Figure 7. Average Glideslope as a Function of Motion and Lighting Configuration During Undirected Type 'A' Descents to Hover.

图片摘要：该图主要展示 7. Average Glideslope as a Function of Motion and Lighting C。
![](images/000d14b4cfcebedfe2e8d5f7cce664b6f2bdefa8cba1de729272720a16bcbe51.jpg)

- Moving Base   
Fixed Base

图片摘要：该图主要展示 7. Average Glideslope as a Function of Motion and Lighting C。
![](images/1ad856c905442221ee91284163e95fe4e01b8a53d697e15f496d0633ece59ece.jpg)

- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 8. Average Glideslope as a Function of Motion and Approach L。
![](images/dabc5bdd6336613fd9697542a2ff39fc7ea7363ce07579c1f0b5236c0ec4eee3.jpg)

图片摘要：该图主要展示 8. Average Glideslope as a Function of Motion and Approach L。
![](images/23ba40e6c5c26143dfa5a9535f16686baa929d6d22bfce4913fe1099503bbe68.jpg)  
Figure 8. Average Glideslope as a Function of Motion and Approach Lighting During Undirected Type 'B' Descents to Hover.

00ε   
图片摘要：该图主要展示 8. Average Glideslope as a Function of Motion and Approach L。
![](images/7816df4cba37e9dd2313046d8321b57a8057dced24e86af9d6b7879b728b1c68.jpg)  
- Moving Base   
Fixed Base

图片摘要：该图主要展示 8. Average Glideslope as a Function of Motion and Approach L。
![](images/67d317df627ab6b736cd1646221239ae645eb8cd965c68bc59f1fd8986c8a280.jpg)  
Distance-to-Go (ft)

图片摘要：该图主要展示 9. Average Glideslope as a Function of Motion and Approach L。
![](images/b83fd4799c13a999ad4885155f7bc34029c3afa222134c08a74afd0191089438.jpg)  
Approach Lighting   
- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 9. Average Glideslope as a Function of Motion and Approach L。
![](images/212a7c6d6d1cb64d4e25ce0df0ca1b74e0b8ae9e85ba973a539d1e6b8f94f045.jpg)  
Distance-to-Go (ft)   
Figure 9. Average Glideslope as a Function of Motion and Approach Lighting During Undirected Type 'C' Descents to Hover.

图片摘要：该图主要展示 9. Average Glideslope as a Function of Motion and Approach L。
![](images/40d21fc42143084c9be3db278302c103caba19e66e7ac8a35f3191f56b9ad43a.jpg)

- Moving Base   
Fixed Base

图片摘要：该图主要展示 9. Average Glideslope as a Function of Motion and Approach L。
![](images/d084c1ad919c6c1ecff52f92e937f405266857c03ede114190a3c2e79a154c5e.jpg)  
Distance-to-Go (ft)

图片摘要：该图片与Approach Lighting；Exponential & Regular Spacing这部分内容相关。
![](images/3cf5509635eccb4fc504032bb29a29935a1551f05f89f67e01149fde9aa753e9.jpg)

Approach Lighting

- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 10. Average Glideslope as a Function of Motion and Approach 。
![](images/5c6bce5241c1f072ea02f1113f26ce16b0a52d88e8f8e7c6a0a10cb4859cb9ae.jpg)  
Distance-to-Go (ft)   
Figure 10. Average Glideslope as a Function of Motion and Approach Lighting During Undirected Type 'D' Descents to Hover.

图片摘要：该图主要展示 10. Average Glideslope as a Function of Motion and Approach 。
![](images/764257199949593ac98a93ff628e0c3b181cbb0dfb2b780b90610529642127a0.jpg)  
Figure 11. Glideslope as a function of approach lighting and platform motion for undirected Type B descents.

Closure Rate Analysis. Table 2 shows all statistically significant $(p < .05)$ closure rate effects. Approach Lighting had a significant affect on closure rate for the Type A and Type D Descents, while Motion affected closure rate for both the Type B and Type D descents.

Figures 12-15 depict velocity (top panels) and closure rate (bottom panels) profiles as a function of Motion (left panels) and Approach Lighting (right panels) for all four descent types (refer to Figure 2, top panel). Similar to the findings for glideslope control,

the Motion x Segment interactions were statistically significant only for the descents from the longer initial ranges (Type B and D descents), although Figures 12-15 show that the presence of motion tended to yield higher closure rates towards the end of all descents. This dependence of closure rate upon initial range may be due to reasons similar to those suggested for the glideslope effects. That is, at the more extreme initial ranges, the pilots may have been more strongly influenced by the vestibular cues provided by motion and therefore responded less vigorously.

Only Type A and Type D descents yielded significant effects of lighting configuration upon closure rate, but the average final closure rate was lowest in the Exponential light configuration for all four initial conditions. Since the most critical impact of the Approach Lighting factor is upon closure rates closest to the landing pad, a follow-up 2 (Replication) x 2 (Initial Closure Rate) x 2 (Initial Range) x 2 (Motion) x 3 (Approach Lighting) repeated measures ANOVA was conducted using just the closure rate from the final segment. This yielded statistically significant interactions of Initial Closure Rate x Initial Range $(\mathbf{F}(1,4) = 0.04)$ , Initial Closure Rate x Motion $(\mathbf{F}(1,4) = 9.61, \mathbf{p} = .036)$ , and Replication x Approach Lighting $(\mathbf{F}(2,8) = 6.346, \mathbf{p} = .022)$ .

Table 2. Statistically Significant Effects Upon Closure Rate   

<table><tr><td>EFFECTS</td><td>Type A Descents</td><td>Type B Descents</td><td>Type C Descents</td><td>Type D Descents</td></tr><tr><td>Lights</td><td>F(1.67,6.69) = 7.09 p = .0249</td><td></td><td></td><td></td></tr><tr><td>Path Segment</td><td>F(1.58,6.31) = 17.5 p = .0033</td><td>F(1.76,7.05) = 14.47 p = .0037</td><td>F(1.34,5.34) = 50.06 p = .0005</td><td>F(1.42,5.68) = 33.37 p = .001</td></tr><tr><td>Motion x Segment</td><td></td><td>F(5.43,21.73) = 2.95 p = .0324</td><td></td><td>F(2.23,8.92) = 4.99 p = .0327</td></tr><tr><td>Lights x Segment</td><td>F(9.63,38.54) = 3.88 p = .0012</td><td></td><td></td><td>F(7.19,28.78) = 4.40 p = .0019</td></tr></table>

图片摘要：该图主要展示 2. Statistically Significant Effects Upon Closure Rate。
![](images/b0014b411ab9acaf5abeb68952b3e6db1c820da116ac1381299f6e41742192c7.jpg)  
- Moving Base   
Fixed Base

图片摘要：该图主要展示 2. Statistically Significant Effects Upon Closure Rate。
![](images/10ab2a03a90f0e297418e8a18f5cac2895708e90dc7601178a68272562af8f51.jpg)  
- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 12. Average Velocity and Closure Rate as a Function of Motio。
![](images/98d5e3415582bea169430d6502744017e1a4316a1f11154126fc02ce21866731.jpg)

图片摘要：该图主要展示 12. Average Velocity and Closure Rate as a Function of Motio。
![](images/1264d143216afa9424180bbbe5a1ec74353e0bfcd9aa8a9e1eacdd7e7328981a.jpg)  
Figure 12. Average Velocity and Closure Rate as a Function of Motion and Approach Lighting During Undirected Type 'A' Descents to Hover.

图片摘要：该图主要展示 12. Average Velocity and Closure Rate as a Function of Motio。
![](images/f5de646b23adf5327a892160ad21d406d51e5c609aa297d3d5eb211a560779d4.jpg)  
POE

- Moving Base   
Fixed Base

图片摘要：该图主要展示 12. Average Velocity and Closure Rate as a Function of Motio。
![](images/343885b5b6296d9063ccda281ff2b4c73f02433ae411f25a25a844f7dd746865.jpg)

- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 13. Average Velocity and Closure Rate as a Function of Motio。
![](images/bc8568cd5c66563035dee65cd0d31c5bf4ab552a574d75c1d4b810ecb8b998c1.jpg)

图片摘要：该图主要展示 13. Average Velocity and Closure Rate as a Function of Motio。
![](images/827afd95ee74cfffc325efdfb9cc556bdc7b9bc47592caa768014fe4743fa9f3.jpg)  
Figure 13. Average Velocity and Closure Rate as a Function of Motion and Approach Lighting During Undirected Type 'B' Descents to Hover.

图片摘要：该图主要展示 13. Average Velocity and Closure Rate as a Function of Motio。
![](images/0ef0ef8ba04d199804ba7e421b0d692e6558017e9947fdfd8a6e16ebb0a345ca.jpg)  
- Moving Base   
Fixed Base

图片摘要：该图主要展示 13. Average Velocity and Closure Rate as a Function of Motio。
![](images/084326091d77433049f13a17a1e74d8e9e8fb72fc64d4f8ef198f36fc5a64a7e.jpg)  
- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 14. Average Velocity and Closure Rate as a Function of Motio。
![](images/74eeb2cedbce9a3547073274ff98bcfe321c5b450006f6f50861615ad1cc7032.jpg)  
Distance-to-Go (ft)

图片摘要：该图主要展示 14. Average Velocity and Closure Rate as a Function of Motio。
![](images/a574496ad0c77e724d18fd4f53166e82c079a69af59df63be4719f94087de907.jpg)  
Distance-to-Go (ft)   
Figure 14. Average Velocity and Closure Rate as a Function of Motion and Approach Lighting During Undirected Type 'C' Descents to Hover.

90ε   
图片摘要：该图主要展示 14. Average Velocity and Closure Rate as a Function of Motio。
![](images/0743d9e830af81703ef356852386fc42767a658b340abad09ae55de2438d5a20.jpg)  
- Moving Base   
Fixed Base

图片摘要：该图主要展示 14. Average Velocity and Closure Rate as a Function of Motio。
![](images/d8bf5aba05912ea401599f49ca4c35f4459ab39dc10a44ff033ceee4154ea66f.jpg)  
- Exponential & Regular Spacing   
Regularly Spaced   
No Approach Lighting

图片摘要：该图主要展示 15. Average Velocity and Closure Rate as a Function of Motio。
![](images/2baef6d9fafa897d8e83fa6b6e9ce46f6e8e7eb39096c75661e7c573f2ce9c32.jpg)  
Distance-to-Go (ft)

图片摘要：该图主要展示 15. Average Velocity and Closure Rate as a Function of Motio。
![](images/e1dc1c21c78513517d97b718513c7de1b0c6acfc24b2f6bdf8268ad9680e80dd.jpg)  
Distance-to-Go (ft)   
Figure 15. Average Velocity and Closure Rate as a Function of Motion and Approach Lighting During Undirected Type 'D' Descents to Hover.

The top panel of Figure 16 shows that descents over shorter ranges led to smaller final closure rates that were unaffected by Initial Closure Rate, but that higher Initial Closure Rates led to higher final closure rates, especially for the descents from the farther Initial Range. The middle panel of Figure 16 shows that the presence of platform motion led to lower final closure rates for the lower Initial Closure Rate, but not for the higher Initial Closure Rate. Finally, the bottom panel of Figure 16 shows that the advantage of the exponential lighting configuration strongly increased in the second replication, suggesting that the pilots were still learning to use the information afforded by this configuration.

图片摘要：该图主要展示 15. Average Velocity and Closure Rate as a Function of Motio。
![](images/d0553f2a2857c026865527fb4ed8e8f12cf8ba6a77da3440938d0d947156680d.jpg)

图片摘要：该图主要展示 15. Average Velocity and Closure Rate as a Function of Motio。
![](images/4fe5c7185eb377f96647deee48df2613b31d3b529c2433f4259cc318b0200628.jpg)

图片摘要：该图主要展示 15. Average Velocity and Closure Rate as a Function of Motio。
![](images/14074b0357dacfa2392e53e2220948cd012d03d3481ff4fc4263cae9954f261a.jpg)  
Figure 16. Final Closure Rate as a Function of Initial Closure Rate and Initial Range (top panel), Initial Closure Rate and Motion (middle panel), and Replication and Approach Lighting (bottom panel).

# DISCUSSION

Collectively, these results have shown that glideslope and speed control can both be affected by the pattern of approach lights to helipads, as well as the presence of platform motion.

# Approach Lights

The proposed impact of additional optical information afforded by the linear, and to a greater degree, the exponential approach light configuration on control of deceleration was generally supported, although its effects tended to be confined to the most close in segments. This suggests that the effects of edge rate are most consequential during the final, and slowest, phase of the deceleration to hover. This may reflect an increased perceptual salience of this information in this phase, or perhaps more likely, a shift in relative emphasis, with pilots using the exponential pattern edge rate more during this phase.

The absence of approach lights also led to higher glideslopes, showing the influence of optical information in the linear and exponential approach light configurations other than form ratio and declination angle, since only these information sources were available in the no-light configuration. The specific nature of this beneficial information needs to be determined, but may reflect sensitivity to sink rate, since this will be heightened by having approach lights passing under the vehicle.

Finally, and perhaps not surprisingly, the pilots generally rated the linear and exponential $^+$ linear configurations as less difficult than the no lights configuration.

# Simulator Motion

Generally, the presence of platform motion led to slightly higher closure rates and glideslopes, although the pilots rated motion trials as less difficult than non-motion trials.

The effects of motion on glideslope performance suggest that, for longer ranges, motion may have led to an initial descent with an aimpoint substantially beyond the landing pad. At these longer ranges, vertical displacements lead to smaller changes in glideslope and thus to the visual information specifying glideslope. However, the detectibility of sink rate, as given by platform motion, is not as strongly affected by range to the pad. Thus, increased reliance on the vestibular cues may have led to these results.

The impact of Approach Lighting and Motion appears to be generally additive, except

for glideslope control during the Type B Descents. There, motion appeared to help most when visual cues were weakest (i.e., in the no lights configuration).

# Applications to Vertiport Design

The present findings may have important implications for the design of vertiport approach paths and other physically constrained landing sites. Specifically, they suggest that approach lights, or similar markings, that afford the pilot accurate edge rate information, might aid in regulating speed (and perhaps glideslope as well), especially as the pilot approaches the landing pad. An added and important benefit of such information is that it is a "natural" optical cue rather than an artificial information display. As such, abstracting the optical information should not require the attention of the pilot, leaving his/her attention to other aspects of the approach task.

# CONCLUSION

The present study used a rotorcraft simulator to examine descents-to-hover at landing pads with one of three approach lighting configurations. The impact of simulator platform motion upon descents to hover was also examined. The results showed that the configuration with the most useful optical information led to the slowest final approach speeds, and that pilots found this configuration, together with the presence of simulator platform motion, most desirable.

Future research should aim to generalize the current findings to actual flight conditions or to more complex simulated approaches.

# ACKNOWLEDGMENTS

The authors gratefully acknowledge Mr. Jeffrey Schroeder for his assistance with, and support of, this project. Thanks also to the staff of the NASA Ames Vertical Motion Simulator for providing the technical support for

this project. The second author was supported by Cooperative Agreement No. NCC 2-486 from the NASA Ames Research Center. Sandra Hart was the technical monitor.

# REFERENCES

Andre, A.D., and Johnson, W.W., Stereo effectiveness evaluation for precision hover tasks in a helmet-mounted display simulator. In Proceedings of the IEEE International Symposium on Systems, Man and Cybernetics, Vol. 2, Chicago, IL: IEEE, 1992

Denton, G.G., The influence of visual pattern on perceived speed, Perception, Vol. 9, 1980.

Koonce, J.M., Predictive validity of flight simulators as a function of simulator motion. Human Factors, Vol. 21, 1979.

Larish, J.F., and Flach, J.M., Sources of optical information useful for the perception of speed of rectilinear self-motion, Journal of Experimental Psychology: Human Perception and Performance, Vol. 16, 1990.

Lintern, G. and Liu, Y-T., Explicit and implicit horizons for simulated landing approaches, Human Factors, Vol. 33 (4), Aug. 1991.

Mertens, H.W., Perception of runway image shape and approach angle magnitude by pilots in simulated night landing approaches, Aviation, Space, and Environmental Medicine, Vol. 52, 1981.

Moen, G.C., DiCarlo, D.J., and Yenni, K.R., A parametric analysis of visual approaches for helicopters. NASA Technical Note TN D-8275, 1976.

Owen, D.H., Wolpert, L., and Warren, R. Effects of optical flow acceleration, edge acceleration, and viewing time on the perception of ego speed acceleration. NASA Scientific and Technical Information Facility, 1984.

# Visual Information for Judging Temporal Range

Mary K. Kaiser

Principal Scientist

NASA Ames Research Center

Moffett Field, California

Lyn Mowafy

Research Scientist

University of Dayton Research Institute

Higley, Arizona

# ABSTRACT

Work in our laboratory suggests that pilots can extract temporal range information (i.e., the time to pass a given waypoint) directly from out-the-window motion information. This extraction does not require the use of velocity or distance, but rather operates solely on a 2-D motion cue. In this paper, we present the mathematical derivation of this information, psychophysical evidence of human observers' sensitivity, and possible advantages and limitations of basing vehicle control on this parameter.

# INTRODUCTION

Helicopter control and navigation require the pilot to orchestrate a complex set of control inputs in response to visual information gleaned from the external scene and cockpit instruments. We suggest that a temporal scaling of the external environment, i.e., gauging the time to reach a chosen way-point at current vehicle speed, is a highly useful metric for the pilot. And, in fact, there is sufficient information in the optical flow to support such temporal metrics.

In this paper, we delineate the visual information that specifies temporal range, describe laboratory research demonstrating people's sensitivity to this information, discuss how this information can be used in vehicular control, and consider specific situations in which this information leads to errors in perceived range.

# TEMPORAL RANGE INFORMATION

In the mid-1950s, astrophysicist and novelist Fred Hoyle allowed one of the more clever

characters in his book, The Black Cloud, to develop a proof showing that the time to impact of an approaching body can be calculated from the size of the object's image and its rate of expansion. Specifically, the time to contact (TTC) is approximated as:

$$
\mathrm {T T C} \equiv \phi_ {\mathrm {t}} / \delta \phi / \delta_ {\mathrm {t}} \tag {1}
$$

where $\phi_t$ is the angle subtended by the object at time $t$ and $\delta \phi / \delta_t$ is that angle's temporal derivative (i.e., expansion rate). This equation is an approximation in that it assumes the Law of Small Angles (i.e., $\tan \phi = \phi$ ). The derivation of this equation can be found in Ref. 1.

This elegant observation that TTC can be derived without knowing either target distance or velocity was "rediscovered" by perceptual psychologists, most notably David Lee (Ref. 1), who recognized its significance for perception and control, and derived general formulations for such visual-temporal (or tau) variables. The one most relevant for our discussion describes a moving observer and a target not directly on the observer's motion track, i.e., the passage situation. In this case, an analogous approximation can be made for when the target will pass the observer (i.e., intersect the eyeplane perpendicular to the track vector, as shown in Figure 1):

$$
\mathrm {T T P} \equiv \theta_ {\mathrm {t}} / \delta \theta / \delta_ {\mathrm {t}} \tag {2}
$$

where TTP is time to passage, $\theta_{t}$ is the angle between the observer's track vector and the proximal edge of the target, and $\delta \theta /\delta_{t}$ is that angle's temporal derivative. As before, this equation requires the tangent approximation.

图片摘要：该图主要展示 1. Passage geometry for Equation 2. An observer (O) is movin。
![](images/0065193bd61ecebe15166abeb439a9d42bb946aa0b6195fa84f3e52c6c56f22a.jpg)  
Figure 1. Passage geometry for Equation 2. An observer (O) is moving with velocity (V). A target (P) lies some distance (R) from the track vector, forming angle $\theta$ .

Despite the generality of Lee's formulations, empirical studies of human performance have focused almost exclusively on the direct collision, or TTC, situation (Ref. 2 and 3). These studies examined people's intercept (e.g., catching) and avoidance behaviors. However, for many skilled activities, particularly vehicular control, it is also important to judge the temporal range of objects which are not on a direct collision course. In our laboratory, we have examined observers' sensitivity to visually specified TTP information. Our findings suggest that people are adept at making both relative and absolute TTP judgments.

# TTP EMPIRICAL STUDIES

We conducted a series of studies in a low-fidelity, fixed-based simulator. Observers were required to make either relative (i.e., which of two targets they would pass first) or absolute judgments (i.e., indicate when a target that was no longer visible would pass them).

# Method

The experimental setting is shown in Figure 2. Observers were seated $2.13\mathrm{m}$ from a $2.44\mathrm{m}X1.83$ m rear-projection screen, creating a horizontal field of view (FOV) of $46^{\circ}$ . Viewing was monocular to reduce anomalous depth cues. Displays were generated by a Silicon Graphics Personal IRIS 4D/25TG, with a refresh rate of 60 Hz, and a vertical resolution of 1024 lines. Displays consisted of a cloud of white dots $(n = 600)$ distributed in a virtual volume $17.37\mathrm{m}$ deep. The eyepoint was translated forward at 1.5 m/s. The projected size of the dots did not vary as a function of distance (or change as the observer approached). Thus, there were no object-expansion cues to temporal range.

For the relative TTP judgments, two of the dots were color-coded (green and purple) as targets. The two targets appeared on opposite sides of the heading vector. After viewing durations of 3 or 4 sec, the display was terminated, and observers predicted which of the two targets they would pass first. In the absolute judgment task, only one colored target was visible. It would pass from the observers' FOV after 3 to 5 seconds. The observers estimated when the target would pass their eyeplane by pressing a mouse button. This button press terminated the display.

Target positions were selected such that TTP was fully independent of the time the target was visible on screen, and largely independent of its initial angular projection from the heading vector. In the relative judgment task, the display terminated when the far target was 2 to 4 sec to passage. In the absolute judgment task, the target was between 1 and 3 seconds from passage when it exited the FOV.

The relative judgement task was conducted with feedback, i.e., observers were informed after each trial whether their response was correct or incorrect. The absolute judgment task was conducted both with and without feedback. When feedback was given, observers were informed by a message on the screen after each trial how early or late their response was (in msec).

Eight observers (four males and four females) participated in both the relative judgment and absolute judgment with feedback tasks. They

图片摘要：该图主要展示 2. The experimental setting for laboratory experiments. Obse。
![](images/aec8b47911cb68e64c7cb680ad80f8e181a081a4b10b4a93b7e2c045c8b8c7f8.jpg)  
Figure 2. The experimental setting for laboratory experiments. Observers viewed events monocularly with their dominant eye.

ranged in age from 19 to 42 yr; all had normal or corrected to normal vision and were right-eye dominant. Four additional observers (3 males, 1 female) participated in both the feedback version and the no-feedback version absolute judgment task (performing the no-feedback task first). They ranged in age from 24 to 34 yr.

For the relative judgment task, observers completed a total of 160 experimental trials, 80 at the 3-sec duration and 80 at the 4-sec duration. For the absolute judgment task, trials were arranged in blocks of 66 trials. Following initial training trials, observers completed 3 blocks of trials, with 10 min breaks between blocks.

# Results

Analyses of the relative judgment data indicated that observers were able to judge above chance level which target they would pass first for all but the shortest (250 msec) temporal

图片摘要：该图主要展示 3. Average percent correct on relative TTP task for the four。
![](images/2a4950201782e65a42762c5319c9c5d6045163d54d1fac7eeeb028c4b2daeed9.jpg)  
Figure 3. Average percent correct on relative TTP task for the four temporal separation and two display exposure times.

separation. The percentages of correct responses averaged across observers are shown in Figure 3. Performance was not affected by whether observers viewed the targets for 3 or 4 seconds. Percent correct differed for the longest temporal difference (1000 msec) only, however this difference was not statistically significant $\left[\mathrm{F}(1,15) = 1.05,\mathrm{ns}\right]$ .

The absolute judgment data were analyzed by performing linear regressions. Judged TTP was regressed against actual TTP. The linear fits $(\mathbb{R}^2)$ for the data ranged from 0.55 to 0.85, with a mean of 0.73. The regression slopes for all observers were less than 1 (the mean value was 0.84), indicating a temporal compression (i.e., an additional sec in actual time resulted in less than one sec increase in judged time). The intercepts were all positive (the mean value was about 500 msec). This, coupled with the less-than-unity slopes, indicates that shorter TTPs were overestimated and longer TTPs were underestimated. Across observers, the correlation between constant error and extrapolation time was $r = -0.94$ .

For the four observers who participated in both the feedback and no-feedback conditions, the presence of feedback did not significantly impact the linear regression fits, either in terms of slope and intercept, or the goodness of fit.

# Discussion

Taken together, the findings from our empirical studies suggest that people are able to make reasonably reliable TTP judgments.

Observers could reliably discriminate differences in TTP of a half sec or more.

Observers' absolute judgments did demonstrate non-veridical temporal scaling (i.e., slopes less than unity and positive intercepts). This bias, however, could either represent a warping of the perceptual space (e.g., a target four sec distant appears to be less than twice as far as a target two sec distant), or result from systematic error in the cognitive extrapolation component of the judgment task. Further research is needed to decompose this bias into its components. Despite this bias, however, observers' judged TTPs were highly correlated with actual TTPs. Further, observers did not require any training or feedback to achieve well-calibrated judgments.

# USING TTP TO CONTROL FLIGHT

Optical tau variables thus provide a useful metric for control related activities. Given such temporal metrics, how might a pilot utilize them for vehicular control? We propose that pilots tend to maintain a window of safe maneuverability, which is defined in terms of the handling qualities of the aircraft. For example, consider the geometry shown in Figure 4. For any given eyeheight (i.e., altitude), the forward field can be scaled in terms of eyeheights: the terrain along the $45^{\circ}$ declination is one eyeheight distant, a gaze angle of $-26.5^{\circ}$

corresponds to 2 eyeheights, $-18^{\circ}$ to 3 eyeheights, and so forth. The time it takes to traverse 1 eyeheight is a function of speed relative to altitude (AGL). If the vehicle is at an altitude of $31\mathrm{m}$ , a speed of 30 knots will create a flow of 1 eyeheight/sec. If that altitude is doubled, the speed must likewise double to create the same flow rate (or TTP) at a given gaze angle. We suggest that pilots are most comfortable with speed/altitude profiles which allow them to maintain acceptable TTP values at some nominal gaze angle. Acceptable TTP values are defined by the time required to allow the pilot to safely perform necessary flight maneuvers.

In a normal walking gate, people move at about 1 eyeheight/sec. Our sense of subjective speed is geared to this metric. The same objective speed feels faster at lower eyeheights (thus the thrill of low-slung sports cars) and slower at higher ones (thus the boredom of minivans and the early tendency of pilots to taxi B747s too fast). Likewise, as a pilot reduces altitude, the natural tendency will be to reduce speed such that the temporal lead time along a given gaze line is consistent. The flight environment is scaled in a temporal, rather than spatial domain. This temporal scaling is highly relevant for flight control. However, this metric will bias the pilot against maintaining constant speed during altitude change.

图片摘要：该图主要展示 4. Eyeheight geometry for forward flight. Gaze angle for thr。
![](images/b3d40bf5cbc8475820d09d4d14ff66b54ea0015176892c44b23a26964b998cb1.jpg)  
Figure 4. Eyeheight geometry for forward flight. Gaze angle for three look-aheads given. Temporal value of look-ahead determined by velocity in eyeheights/sec.

# LIMITATION OF TTP INFORMATION

Given that pilots may utilize optical tau variables to orchestrate control and avoidance maneuvers, it is important to consider limitations and degenerate cases of these variables. As mentioned above, such temporal scaling can result in undesired speed changes during altitude transitions (although a consistent "safety window" is maintained). In addition, there is an interesting degenerative case of TTP that occurs when the observer and a moving target are on a collision course, but the object is not on the observer's track vector. If the observer and object maintain constant velocities, the center of the object maintains a fixed angle to the observer's track vector, as shown in Figure 5.

图片摘要：该图主要展示 4. Eyeheight geometry for forward flight. Gaze angle for thr。
![](images/0a5fa374ae6b0c55895d0b492d5918d7c9419d2efc228e0aa3e847fb60d15639.jpg)  
Figure 5. Geometry for moving observer and moving target on collision course. If both maintain a constant velocity and track, $\theta$ is constant.

Thus, $\theta$ for the centroid of the target is constant (i.e., $\delta \theta / \delta t$ is zero), and $\delta \theta / \delta t$ for all other points is small, reflecting only image expansion. Consider what value of TTP is specified in this

condition: $\mathrm{TTP} = \theta / \delta \theta / \delta t$ , so as $\delta \theta / \delta t$ approaches zero, TTP approaches infinity. Thus, an object on such a collision course can be mistaken for an object at a very large distance, since the TTP information is virtually identical. Image expansion will differentiate these cases, but may not be salient at large distances. Only when image expansion becomes noticeable (or if the observer is cued by some non-motion information, such as familiar size) are the two cases discriminable. Since image expansion may not become salient until the object is temporally proximal, the observer may be required to make a last second correction to avoid collision. Such maneuvers are highly undesirable in flight situations. This examination of the TTP information lends insight into how such mishaps may occur, particularly in visually impoverished (e.g., night flight) environments.

# CONCLUDING REMARKS

This "unmoving objects on a collision course" scenario, however, represents a degenerate (albeit interesting) case of TTP information. Most of the time, optical tau variables provide reliable information concerning objects' temporal distance. Moreover, our empirical studies demonstrate that observers possess a robust ability to utilize this information. We propose that these tau cues provide a useful temporal metric for pilots to employ in planning and orchestrating vehicular control. However, the maintenance of such temporal windows result in altitude-related speed changes, which are undesirable in some flight profiles.

# REFERENCES

1. Lee, D. N., "A Theory of Visual Control of Braking Based on Information About Time-to-Collision," Perception, Vol. 5, 1976.   
2. Tresilian, J. R., "Empirical and Theoretical Issues in the Perception of Time to Contact," Journal of Experimental Psychology: Human Perception and Performance, Vol. 17, 1991.   
3. Kaiser, M. K. and Mowafy, L., "Optical Specification of Time-to-Passage: Observers' Sensitivity to Global Tau," Journal of Experimental Psychology, Vol. 19, in press.

图片摘要：该图片与Visual Cueing Considerations in Nap of the Earth Helicopter Flight by Head Slave这部分内容相关。
![](images/541943213319cd3313a2ea5984ce2273952c747313b61ba28338d7435d07d775.jpg)

# Visual Cueing Considerations in Nap-of-the-Earth Helicopter Flight by Head-Slaved Helmet-Mounted Displays<sup>1</sup>

Arthur J. Grunwald

NRC Senior Research Associate

Aerospace Human Factors Research Divisions

NASA Ames Research Center

Moffett Field, California, 94035

# ABSTRACT

The Pilot's ability to derive Control-Oriented Visual Field Information from teleoperated Helmet-Mounted displays in Nap-of-the-Earth flight, is investigated. The visual field with these types of displays, commonly used in Apache and Cobra helicopter night operations, originates from a relatively narrow field-of-view Forward Looking Infrared Radiation Camera, gimbal-mounted at the nose of the aircraft and slaved to the pilot's line-of-sight, in order to obtain a wide-angle field-of-regard. Pilots have encountered considerable difficulties in controlling the aircraft by these devices. Experimental simulator results presented here, indicate that part of these difficulties can be attributed to head/camera slaving system phase lags and errors. In the presence of voluntary head rotation, these slaving system imperfections are shown to impair the Control-Oriented Visual Field Information vital in vehicular control, such as the perception of the anticipated flight path or the vehicle yaw rate. Since, in the presence of slaving system imperfections, the pilot will tend to minimize head rotation, the full wide-angle field-of-regard of the line-of-sight slaved Helmet-Mounted Display, is not always fully utilized.

# INTRODUCTION

With head-slaved Helmet-Mounted Displays (HMD's), the image of a forward looking camera, such as an Infrared Radiation or a low-light level camera, mounted on a servo-driven gimbals system at the front of the helicopter, is transferred to a miniature helmet mounted Cathode Ray Tube (CRT). By means of collimating optics and a beam splitter, the image is presented to a single eye so that it appears to be superimposed on the visual field at infinity. The camera motions are slaved to the pilot's Line-of-Sight (LOS), by measuring the pilot's head angles in pitch and yaw, and by imparting this information to the camera servo drives. The LOS slaving system of HMD's allows the field-of-regard of the pilot to be

Silvia Kohn  
Faculty of Aerospace Engineering  
Technion, Haifa, Israel

extended well beyond the limits of the narrow field-of-view of the HMD's viewing optics. Thus, just by rotation of the head, the pilot is able to cover a field-of-regard of nearly up to 180 deg horizontally, and 90 deg vertically. In addition, in most cases, the camera is positioned such that its view is not obstructed by the aircraft body. This allows the pilot to view areas which are usually blocked out by the cockpit. This wide-angle coverage is very essential in Nap-of-the-Earth (NOE) flight, both for vehicular control by allowing the pilot the necessary spatial orientation with respect to terrain and obstacles, and for the detection and location of targets or mission threats in military missions, or survivors in rescue missions.

Although the LOS slaved HMD apparently solves the problem of providing a wide-angle coverage for the given narrow field-of-view of the HMD optics, vehicular control with such systems is still very difficult, and demands high pilot proficiency and work load. Part of these difficulties can be attributed the fact that the viewpoint of the camera is displaced with respect to the actual eye position. In the presence of fast vehicle pitch or yaw rotations this might result in misjudged vehicle motions. Furthermore, for a camera mounted in front of the pilot, near objects will appear larger than they actually are.

Additional difficulties arise from the relatively narrow field-of-view of the HMD's viewing optics, resulting from practical limitations on the miniature CRT face-plate dimensions, the dimensions and shape of the beam splitter and its minimal safe distance to the pilot's eye, and the collimating system design. Thus, essential parts of the pilot's peripheral vision are missing, which may result in impaired motion perception.

Considerable difficulties are also encountered in the interpretation of FLIR images, which are basically different from visible light images, usually resulting in misjudged object size and impaired depth perception.

The head-slaved HMD resembles a viewing aperture without optics, attached to the pilot's head, which allows him to frame-in different areas of the outside world by rotation of the head. The HMD one-to-one slaving system and the deliberate choice of a

unity image magnification, attempt to give the pilot the illusion of viewing a natural visual scene through such an aperture. For an ideal slaving system, the viewed image would appear to be part of an inertially stable background. However, slaving system errors will be experienced by the pilot as undesired shifts of the displayed visual field with respect to the true "natural" visual field. The effect of these shifts is twofold: (1) they will alter the optical flow-field pattern and result in incorrect estimation of the self-motion; and (2) the visually estimated self-motion will be different from the motion estimated by vestibular cues. This might lead to visuo-vestibular conflicts or motion sickness, Oman [1]. In coordinated fixed-wing aircraft flight, the velocity vector will coincide with the vehicle longitudinal axis and the pilot can infer the direction of motion from vehicle-based references, by means of his kinesthetic sense of straight ahead. However, in helicopter flight, the direction of motion can deviate substantially from the vehicle axis. Thus helicopter control in NOE flight, is susceptible in particular to these slaving system imperfections, since the Control-Oriented Information has to be derived entirely from the visual field, and can not rely on vehicle based references.

This paper deals with the basic experiments for understanding the Visual Field Information in HMD's Displays, and investigates how this information is affected by slaving system imperfections. Two types of experiments were carried out: (1) a flight path estimation experiment, in which the pilot had to judge the anticipated vehicle path, while being flown passively in a straight or curved horizontal path over flat textured terrain, and (2) a simulated Nap-of-the-Earth flight experiment, in which the pilot subject had to fly actively through a winding canyon, in the presence of purposefully induced head motions.

# VISUAL FLOW FIELD CUES

A detailed geometrical analysis of visual flow field cues in horizontal flight over textured flat terrain, is given in Ref. [2]. In this paper we shall suffice with a brief qualitative description.

The visual flow field resulting from an observer's self-motion, is given by the time derivative of a set of line-of-sight (LOS) vectors extending from the pilot's eye to conspicuous points in the visual field (texture points). The flow field is the pattern traced by the intersection of these LOS vectors with a unity sphere about the observer's head. These traces are commonly referred to as the "streamer" pattern. For straight or constantly curved motion at fixed velocity and altitude above a flat surface, the flow field is constant.

# Flow field cues in straight flight

The horizontal situation for straight and level flight is shown in Fig. 1a. The center of gravity of the vehicle moves along a straight path in the direction of the velocity vector $\underline{\mathbf{V}}$ , while the longitudinal vehicle axis is $x_{b}$ is rotated with respect to $\underline{\mathbf{V}}$ by the crabbing angle $\beta$ . The camera axis $x_{h}$ is rotated with respect to the vehicle axis by the angle $\psi_{h}$ . The corresponding streamer pattern is shown in Fig. 1b. The horizontal and vertical axes in Fig. 1b are the viewing azimuth angle and elevation angle, (the latter is measured positive in upwards direction).

For straight flight the streamer pattern appears to expand from a common focal point on the horizon, point F, see Fig. 1b. This point has often been called the "focus of expansion", Gibson [3-5]. The straight vehicle path is defined by the set of points which do not have an azimuth LOS rate component, see solid line. This is also the streamer that is apparently vertical, i.e. perpendicular to the horizon or to the base of the HMD image frame, for zero vehicle roll angle. The dotted box in Fig. 1a indicates the area of the visual field, viewed by the HMD. The center of this box, H, indicates the camera axis $x_{h}$ and coincides with the pilot's direction of gaze. The vehicle longitudinal axis $x_{b}$ is indicated by point C. The head angle $\psi_{h}$ is the angle between H and C, and the vehicle crabbing angle $\beta$ is the angle between F and C. In case the crabbing angle $\beta$ is zero, F and C coincide and the direction of motion is presented to the pilot implicitly by kinesthetic head position cues. However, for arbitrary large angles of $\beta$ this is not the case, and the direction of motion has to be derived solely from the streamer pattern.

Fig. 1b. indicates that the focal point F is not necessarily located within the HMD field-of-view. In this case, the direction of motion is derived by estimating the point where the streamers line segments, visible within the HMD viewing area, would intersect. It has been shown in Ref. [2] that the detectability of the direction of motion depends on the local expansion, which is defined as the derivative of the streamer direction with respect to the azimuth angle. This local expansion is shown to be proportional to the viewing distance to the texture point, measured along the LOS. It therefore appears, that the direction of motion is most easily perceived in the far visual field, where the local expansion is the largest. However, the streamer pattern can only be perceived when the magnitude of the LOS rates are above a certain threshold. It is shown in Ref. [2] that these LOS rates are inverse proportional to the squared viewing distance. A possible mechanism for estimating the straight vehicle path is to extrapolate the focal point from converging streamer segments, located within an area of the visual field, at the farthest

viewing distance at which the streamer direction can still be detected, and at which the local expansion is the largest. It is clear that when this area is not within the HMD field-of-view, the pilot will have to shift his gaze to a different area of the visual field.

# Flow field cues in curved flight

The horizontal situation for steady curved flight over flat terrain is shown in Fig. 2a. The instantaneous velocity vector is $\underline{\mathbf{V}}$ , and $\beta$ is again the crabbing angle. However, the actual vehicle path is a circle with radius $\mathbb{R}$ , tangential to $\underline{\mathbf{V}}$ and with its center at point M. The corresponding streamer pattern

is shown in Fig. 2b. This pattern shows a converging, curved set of lines, and a common focal point on the horizon no longer exists. The curved vehicle path is the dashed, central line in the bundle. The vehicle path is defined by the streamer which, for very close viewing ranges, will have a zero azimuth LOS rate component and which tend to be tangential to the velocity vector (solid vertical line). This tangent is again apparently vertical, i.e. perpendicular to the horizon or to the base of the HMD image frame, for zero vehicle roll angle.

图片摘要：该图主要展示 1. (a) Horizontal Situation for Straight and Level Flight; (。
![](images/1b167356ea7289a0ce72c1a741c846d7b386f1e975e599b28f77e3ac39db6edb.jpg)

图片摘要：该图主要展示 1. (a) Horizontal Situation for Straight and Level Flight; (。
![](images/05c77313ed3895b580dcd41e843c15fa1e2021259ca6309a575791064e78b804.jpg)  
Figure 1. (a) Horizontal Situation for Straight and Level Flight; (b) Streamer Pattern for Straight and Level Flight over Flat Textured Terrain

图片摘要：该图主要展示 1. (a) Horizontal Situation for Straight and Level Flight; (。
![](images/bfef644a8135815be47457a131741be57fa6cbc9e7eeb2dd26400b87830478e0.jpg)  
CURVED MOTION VELOCITY VECTOR

图片摘要：该图主要展示 1. (a) Horizontal Situation for Straight and Level Flight; (。
![](images/9db595bbe3fa07e5c76175f734f402da5e3b992693cb3dcb998195902e826bbd.jpg)  
Figure 2. (a) Horizontal Situation for Curved Level Flight; (b) Streamer Pattern for Curved Level Flight over Flat Textured Terrain

It is of interest to consider points in the visual field, which do not have an azimuth LOS rate component. It is shown in Ref. [2] that the locus of these points is formed by the circle, tangential to $\underline{\mathbf{V}}$ and with radius 0.5R, hereafter referred to as the "halfradius circle". This locus is shown in Fig. 2b as the dotted line. For viewing distances $D << R$ , the azimuth angle of a point on the vehicle path is about half way in between the azimuth angle of the velocity vector and of a point on the half-radius circle.

A possible mechanism for estimating a point on the vehicle path, would look for the azimuth angle of the area at viewing distance D, with a zero azimuth LOS rate component, (on the half-radius circle). In addition, the mechanism would estimate the azimuth of the velocity vector by looking, at very close distances, for points with a zero azimuth LOS rate component. It would then estimate the azimuth of a point on the vehicle path at distance D to be half way in between the two angles. A shortcoming of this

mechanism is that it will break down when the point on the half-radius circle is outside the field-of-view.

Another possible mechanism would be to look for continuity of motion between points in the visual field. It would select a set of points which belong to a certain section of the streamer, by following the motion of a texture point over a given interval of time. It would then find the correspondence between streamer sections which would add up to the central streamer, i.e. the one of which the azimuth LOS rate component for close viewing distances, is zero, or, alternatively, the streamer which tends to be tangential to the apparent vertical. This would involve viewing near as well as far areas of the visual field.

The dotted box in Fig. 2b. again shows the area of the visual field, viewed by the HMD. Regardless of the mechanism used, active head motions of the pilot will be required, since the estimation of the curved

图片摘要：该图主要展示 3: Streamer Pattern "Bending" Effect Resulting From Line of 。
![](images/beb4ab22b31952e1bdfeda7bc853a03ff4dca8c3c830d744450a0df01f6a9e9b.jpg)  
Figure 3: Streamer Pattern "Bending" Effect Resulting From Line-of-Sight Slaving System Lags

vehicle path is based on different areas of the visual field, which involve either points on the half-radius circle or points nearby.

# Flow field cues in helmet mounted displays

As mentioned before, for an observer in straight or steady curved level flight, a stationary streamer pattern is obtained. Under natural, unconstrained viewing conditions, the streamer pattern and consequently the ability to estimate the vehicle path, will not be affected by voluntary head rotations. This can be attributed to the visuo-ocular reflex, which will inertially stabilize the eye line-of-sight with respect to the viewed background. In this situation, changes in the pattern only result from changes in self-motion parameters. However, the viewing conditions for LOS slaved HMD's differs from natural unconstrained conditions in two ways: (1) the narrow viewing aperture and (2) slaving system imperfections. Due to the narrow viewing aperture, areas essential for estimating the vehicle path might not be in view. Attempts of the pilot to acquire the information might require quick scans of different areas of the visual field, resulting in rapid head motions. However, due to the frame-of-reference effect caused by the narrow viewing aperture, the observer might experience an apparent yaw motion in opposite direction of the voluntary head rotation, Boff [6]. This illusion is caused by strong edge rate effects of image elements passing the edge of the HMD image frame during rotation. The smaller the reference frame, the stronger the effect.

Slaving system imperfections are detrimental in particular in perceiving self-motion information from the visual field. Random tracking errors, scaling errors, or phase lags will result in undesired shifts of the displayed visual field with respect to the true "natural" visual field. These undesired image shifts will make the viewed visual scene appear to move with respect to an inertially stable background. The negative effects of this apparent motion are twofold: (1) Since, during voluntary head rotation, the eye LOS is stabilized with respect to inertial space, the parasitic image shifts will alter the visual field information. (2) The self-motion estimated from the shifted visual field is in conflict with the vestibular signals. This visuo-vestibular conflict might cause motion sickness or disorientation. The following example demonstrates the effect of parasitic image shifts due to LOS slaving system servo lags, on the visual field information contents.

Consider the LOS slaving system to be a second-order system with an natural frequency of $\omega_{\mathrm{n}} = 94.3$ rad/s (15 Hz) and with a damping factor of $\zeta = 0.707$ . Consider the head yaw rotation to be sinusoidal with amplitude A deg and frequency $\omega$ rad/s. It is easily shown that for $\omega < \omega_{\mathrm{n}}$ the image shift rate amplitude

is given by: $s = 2\zeta A \omega^2 / \omega_n \deg / s$ .

For example, for $A = 10$ deg and $\omega = 1.0$ rad/s the image shift rate amplitude is $s = 0.15$ deg/s. This parasitic yaw rate will add a constant azimuth component to all LOS vector rates. For an observer in straight motion the parasitic yaw rate will make the expanding pattern appear to "bend" momentarily, just as if the observer were in curved motion. It is clear that the larger the ratio between parasitic yaw rate and LOS rate, the larger the "bending" effect. Therefore the negative effects of servo lags are noticed in particular for low self-motion velocities. Fig. 3 shows examples of this "bending" effect, for $A = 10$ deg and $\omega = 1.0$ rad/s, for various velocities. Both the velocity $V$ and the viewing distance $D$ are expressed in units of the height $h$ above the terrain. For $V / h$ ratios of $0.25$ s and $4.0$ s, the angular errors introduced by the bending effect at viewing distance $D = 7.5h$ are $2.26$ deg and $0.14$ deg, respectively.

# EXPERIMENTAL PROGRAM

# Experimental setup

The visual scene was generated at a Silicon Graphics IRIS 4D 50/GT work station. The pilot subject was seated in a general aviation simulator cabin, wearing an operational flight helmet, on which a Hughes Aircraft miniature CRT with beam splitter and collimating optics was mounted. The monochromatic image, of aperture 22.8 deg horizontally and 18.4 deg vertically, was presented to the subject's left eye only. The right eye was uncovered, viewing the low-light level cockpit background, normally present in night helicopter missions. No outside view or panel mounted display images were presented. A Polhemus head tracking system was used to measure the angular orientation of the head. The measured yaw, pitch and roll head angles were send to the graphics work station, and used for generating the image corresponding with the subject's line-of-sight. Although the Polhemus was sampling at $30\mathrm{Hz}$ , the image was updated at about $15\mathrm{Hz}$ . Thus, the system roughly simulated a line-of-sight slaving system with a bandwidth of $15\mathrm{Hz}$ . Pilot controls included a two-axis high-precision strain gauge operated side-arm controller with response buttons.

# Flight path estimation experiment

Each trial represented the situation of passively being flown over nominally flat terrain at height h, either in a straight or constantly curved, level motion pattern. The terrain consisted of a field of randomly placed poles with constant density and with no visible alignment. The average distance between the poles was 1.17 units of h, and their average height was 0.25h. Both the vehicle velocity vector $\underline{\mathbf{V}}$ , and the vehicle

longitudinal axis $x_b$ were parallel to the ground plane. The vehicle axis was deviating from the velocity vector $V$ by the crabbing angle $\beta$ , and the curved path was tangential to $V$ . In order to conserve computational resources and realize an update rate of $15\mathrm{Hz}$ , the field was not drawn beyond a viewing distance of $D = 15h$ .

The subjects initiated an experimental trial by pressing a response button, after which the visual field became visible from an initially blank screen. For each trial the side slip (crabbing) angle $\beta$ and/or the path curvature radius R were uncorrelated and chosen randomly. A marker was visible in the visual field at viewing distance D, in the direction of gaze, consisting of a circular base of diameter 0.625 h placed in the ground plane with a vertical pole at its center of height 0.125 h. The marker remained at the center of the HMD image, and the subjects could change the marker azimuth just by turning their head. It should be noted that through appropriate geometrical transformations, the marker was kept at all times perpendicular to the ground plane and at a fixed viewing distance D, regardless of head pitch and roll. The subjects were asked to place the marker on the estimated flight path. They were instructed to do this

intuitively, as quickly as possible and to acknowledge their choice by pressing a response button. During the training runs, after each trial, a dotted line was displayed for two additional seconds, indicating the true flight path.

Three types of experiments were conducted: (1) Straight and level flight in the presence of a constant side slip angle $\beta$ , chosen from a uniformly distributed random set, ranging from -45 to +45 deg. (2) Steady curved and level flight with zero side slip, where the path curvature radius was chosen from a uniformly distributed random set ranging from 15h to 40h and where the curvature could be to the left or to the right with equal probability, and (3) Steady curved and level flight in the presence of side slip, with the curvature chosen as in (2) and with the side slip angle $\beta$ chosen from an uncorrelated uniformly distributed random set, ranging from -14 to +14 deg.

The relevant parameters investigated were: the velocity-to-height ratio and the viewing distance. Five velocity-to-height ratios were chosen, ranging from 0.25s to 4s. Two viewing distances were chosen, $D = 7.5h$ for the far field, and $D = 3.0h$ for the near field.

图片摘要：该图主要展示 4: Image of the Randomly Curved Canyon used in the Simulated。
![](images/ee49602e5ab11b0c4b08f8d7e845a2eaae076005c9b3a58e3ce4a0f136f910a9.jpg)  
Figure 4: Image of the Randomly Curved Canyon used in the Simulated NOE Flight Experiments

# Simulated NOE flight experiment

This experiment simulated the task of actively flying a control-augmented H-19 helicopter through a V-shaped randomly curved canyon, shown in Fig. 4. The horizontal canyon path, and the vertical path profile were generated by passing band-limited white noise processes through a series of shaping filters. The horizontal and vertical path correlation length was about 1500 ft. Two trajectory shapes were considered: a "moderately" curved trajectory with maximum horizontal curvature radii of 500 ft and a strongly curved trajectory with maximum radii of 250 ft. For each run, lasting 180 s, a different random path was generated. The canyon was formed by randomly shaped cross sections spaced 30 ft apart and interconnected by monochrome, solidly drawn polygons of randomly different brightness, simulating a FLIR image. The subjects were instructed to follow the canyon while staying as close as possible to its base without hitting the sides.

Deliberate head rotation was introduced by a secondary task. At random intervals, a diamond-shaped target appeared at a location, fixed with respect to the canyon, see Fig. 4. The target became first visible at a viewing range of 550 ft and disappeared at 300 ft. The subject had to lock his line-of-sight on the target, by bringing it within a 5.7 by 5.7 deg tick mark area in the center of the image. After a successful lock-on, the target and tick marks disappeared. During each run a total of 15 targets were presented. The target locations were chosen such that they involved considerable head rotation, in addition to the rotation needed for following the canyon.

# Subject training and experimental procedure

Eight male and one female subject, all of them Technion Aerospace undergraduate students, participated in the experiment. Subject age was between 19 and 24. Subject training for the vehicle path estimation experiments included several one-hour training sessions. After that each subject carried out a series of runs for each one of the three experiments (straight, curved, curved with side slip, in this order). Each series included a number of configurations, each of which was repeated four times and addressed in a random fashion. Each configuration consisted of a set of 20 consecutive trials, each of which was initiated by the subject by pressing a response button. Each trial lasted for about 2-8 seconds, depending on the time needed by the subject to estimate the direction of motion. About 8 one-hour sessions were needed for each subject to finish the experimental program.

Training for the simulated NOE flight experiment required several one hour sessions. Production included simulation runs of 180 s duration, repeated 5 times for each subject and for each configuration. Subject

motivation was enhanced by a reward system based on competition.

# Experimental measurements

In the flight-path estimation task, for each trial in a set, the error in azimuth angle between the true and estimated location of a point on the flight path at viewing distance D, were recorded, together with the time needed to make the estimate. The upper limit on the estimation time was 8 seconds, after which the run was terminated and marked as a failed run. In addition, the head activity was recorded in terms of the standard deviation of the head yaw angle and yaw angle rate.

For each set of 20 trials, the average and the standard deviation of the estimation error and estimation time, were computed. Since the average of the estimation error was found to be almost zero, i.e. no preference for an error in left or in right direction existed, the standard deviation of the estimation error was adopted as the representative estimation error score of each set. For the estimation time, the average of the set was taken as the representative score.

Performance scores for the NOE flight experiments included the power of the deviation from the bottom of the canyon, standard deviations of head activity, stick activity, vehicle roll and roll rate and the average time needed to lock the line-of-sight on the target.

# EXPERIMENTAL RESULTS

# Flight path estimation task

# Effect of the velocity-to-height ratio:

Figs. 5-8 show the various performance scores as a function of the $\mathrm{V} / \mathrm{h}$ ratio, for the three motion patterns. For straight motion, (dotted line) the estimation error score strongly decreases with $\mathrm{V} / \mathrm{h}$ , both for the "far" viewing distance of $\mathrm{D} / \mathrm{h} = 7.5\mathrm{h}$ (Fig. 5a) and for the "near" viewing distance of $\mathrm{D} / \mathrm{h} = 3.0\mathrm{h}$ (Fig. 5b). In contrast, the downslope of the curves for curved motion and curved motion with side slip, is considerably less. For the near viewing distance the curves are even sloping upwards (Fig 5b). Furthermore, the curves for straight motion for the estimation time and the head yaw rate activity are markedly above the ones for the curved motion patterns, see Figs. 6a,b. This indicates that the subjects probably used a different strategy in the straight motion task. The curves for the head yaw angle and yaw angle rate activity show pronounced and consistent upward slopes, Figs. 7 and 8. This effect can be attributed to the LOS slaving system imperfections, discussed in Section 2.4. The smaller $\mathrm{V} / \mathrm{h}$ , the stronger the "bending" of the streamer pattern

图片摘要：该图主要展示 5a. Estimation Error Score for。
![](images/97763e762e664abc5a634f07c60a8c11e6af240a4b7b72047bd8d1fa79ded45e.jpg)  
Figure 5a. Estimation Error Score for $D = 7.5h$

图片摘要：该图主要展示 5a. Estimation Error Score for。
![](images/314a84d886d711a0418154975032f96f6b3f7dd3278da67eb13b721e73d8e5b0.jpg)  
Figure 5b. Estimation Error Score for $D = 3.0h$

图片摘要：该图主要展示 5b. Estimation Error Score for。
![](images/4328feb04fca25fce764b2aaed61969db961b1c6069635544060cc2aa6c0f162.jpg)  
Figure 6a. Estimation Time for $D = 7.5h$

图片摘要：该图主要展示 6a. Estimation Time for。
![](images/397ea99516bb83d5e5b2c2058d6419f3414a9977d2a9d27d0c470daf0ec34f61.jpg)  
Figure 6b. Estimation Time for $\mathbf{D} = 3.0\mathbf{h}$

图片摘要：该图主要展示 6b. Estimation Time for。
![](images/24e133eef88432c1133f5f8225391120fb57c246343cb50d6eb0165cdcca4ab4.jpg)  
Figure 7a. Head Yaw Angle Activity for D=7.5h

图片摘要：该图主要展示 7a. Head Yaw Angle Activity for D=7.5h。
![](images/04022278f1bbde4adcb260160eefe39864ec1aab8a15b4944b072852b6870e71.jpg)  
Figure 7b. Head'Yaw Angle Activity for D=3.0h

图片摘要：该图主要展示 7b. Head'Yaw Angle Activity for D=3.0h。
![](images/93b82a35d7d231941203b45a71e4c0b5ac1974bf33b8b6563a96a680483a99e9.jpg)  
Figure 8a. Head Yaw Rate Activity for D=7.5h

图片摘要：该图主要展示 8a. Head Yaw Rate Activity for D=7.5h。
![](images/275a93ad7477fec0b0bd8047b6fc6201bb3effbea3a1fc8e5328a5c1947d6acd.jpg)  
Figure 8b. Head Yaw Rate Activity for D=3.0h

图片摘要：该图主要展示 8b. Head Yaw Rate Activity for D=3.0h。
![](images/77cf4bd11a668f0588c6b1b34f85303b826b4dbef3f59cbe0fccd81921f8cacc.jpg)  
Figure 9a. Effect of Reduced Field-of-View and LOS Slaving Lags on Estimation Error Score

图片摘要：该图主要展示 9a. Effect of Reduced Field of View and LOS Slaving Lags on 。
![](images/ef550c83c2a9fea0e14812af4b54b42d898f168b23489b57bb1a6d14d055c6aa.jpg)  
Figure 9c. Effect of Reduced Field-of-View and LOS Slaving Lags on Head Yaw Angle Activity

图片摘要：该图主要展示 9c. Effect of Reduced Field of View and LOS Slaving Lags on 。
![](images/bded0971d41bd86066533168f994bd15b41a7009c98af8e00d6e08c85ac26f21.jpg)  
Figure 9b. Effect of Reduced Field-of-View and LOS Slaving Lags on Estimation Time

图片摘要：该图主要展示 9b. Effect of Reduced Field of View and LOS Slaving Lags on 。
![](images/c313334d951a9a7ac437878031e7bae2d961a6f541e742d79d915f9df089194d.jpg)  
Figure 9d. Effect of Reduced Field-of-View and LOS Slaving Lags on Head Yaw Rate Activity

during head rotation resulting from slaving system lags, and the less accurate the perception of the streamer direction. This is detrimental in particular in the straight motion task, in which the streamer "bending" makes it almost impossible to find the apparent vertical streamer. As a result, for small velocities subjects will minimize their head rotation, estimates will take longer and estimation errors will be larger. This explains the strong downward slope of the estimation error curve for straight motion, as compared to the more flat curves for curved motion, see Fig. 5a.

Strategy differences between straight and curved tasks are apparent when considering that the subjects are expecting a straight expanding motion pattern in the straight task. Thus, bending effects due to slaving system lags will be identified immediately, and estimates are made only at moments at which the head is stationary. The subjects might have employed a "null measurement" method, in which a sequence of correcting steps is made aimed at placing the apparent vertical streamer at the center. In contrast, in the curved task the subjects might have employed a "deflection measurement" method in which the vehicle path is found intuitively, more or less in an open manner, triggered by the amount of streamer "bending" in the field. Consequently, estimation times and head yaw activity are much larger for the straight task.

# Effect of side slip on curved motion:

The estimation error score curves for motion with and without side slip have similar characteristics, i.e. for the far viewing distance a minimum at $\mathrm{V} / \mathrm{h} = 1.0$ s (Fig. 5a), and for the near viewing distance similar up slopes, (Fig.5b). This up slope might be due to motion "blurring" effects, which prevent the subject from making accurate estimates on the streamer pattern direction. However, the error score curve for motion with side slip is on the average about 3 deg above the one for motion without side slip. This was expected, since in the first case, in the process of estimating the vehicle path, the observer has to derive the direction of motion from the near visual field, whereas in the latter case the direction of motion is at zero azimuth. This direction is presented to him implicitly by kinesthetic head position cues. The increased difficulty to estimate the vehicle path in the presence of side slip is also noticed in the higher head yaw angle and yaw angle rate activity, see Figs. 7 and 8.

# Effect of the viewing distance:

A comparison of the curves of Figs. 5a and 5b shows that the near viewing distance yields generally larger estimation errors than the far distance. This might result from the smaller local expansion in the near field. The difference is large in particular for high

V/h ratios, probably as a result of image blurring. In contrast, the head yaw rate activity shown in Fig. 8a,b for the near and far viewing distance were found to be very similar. It would be expected that the near field, with its higher LOS rates, would allow larger head rotation, since less streamer "bending" will occur. However, the negative effect of the "bending" will be stronger, due to the smaller local expansion. Therefore, the subjects will still minimize their head rotation for low V/h and for the near viewing distance.

# Effect of reduced field-of-view:

The results for an HMD field-of-view reduced to 13.7 deg horizontally and 11.0 deg vertically (40% reduction), are shown in Fig. 9. Contrary to what was expected, estimation errors for all three motion patterns were about the same as for the nominal viewing situation, Fig 9a. However, estimation times were slightly higher (by 9%), and head yaw rate activity lower (by 15%), in particular for straight motion, Fig 9b,c. This indicates that although the reduced field-of-view did not affect estimation accuracy, the subjects might have reduced their head yaw rates due to increased edge rate effects. On the other hand, as expected, the reduced field-of-view demanded slightly more head motions, as seen in the 6.5% increase in head yaw angle activity

# Effect of LOS slaving system lags:

A first-order slaving system lag with a time constant of 0.5 s was introduced. Although the phase lag yielded an only $4\%$ higher error score as compared to the nominal viewing situation, the head yaw rate activity was markedly smaller (by $53\%$ ) and, consequently, the estimation time higher (by $30\%$ ), see Fig. 9. This clearly demonstrates that slaving system phase lags primarily constrain the subject from making fast head motions, they require from him to make more corrections ( $14\%$ larger head yaw angle activity), and they result in longer estimation times.

# Simulated NOE flight task

Results for the NOE flight task are summarized in Table I. For flight without target capture secondary task, the increase in path curvature has its primary effect on the tracking performance (a $65\%$ increase in tracking error score). The increased path curvature is also strongly noticed in the $31\%$ larger head yaw angle rate. Thus, the high-curvature canyon demands more head activity, which, in the presence of inherent LOS slaving system lags, adversely affects tracking performance. As expected, the increased curvature also yields larger control activity and vehicle roll motions.

The effect of adding the target capture secondary task to the vehicular control task is strongly noticed both in the markedly higher tracking error and in the larger head yaw rates (tracking error scores increase by

Table 1. Simulated NOE Flight Experiment   

<table><tr><td></td><td colspan="2">Without Task</td><td colspan="2">With Target Task</td></tr><tr><td></td><td>Low Curva-ture</td><td>High Curva-ture</td><td>Low Curva-ture</td><td>High Curva-ture</td></tr><tr><td>Tracking Error [ft2]</td><td>390.1</td><td>643.9</td><td>1168.6</td><td>1072.5</td></tr><tr><td>Head Yaw rate [deg/s]</td><td>3.2</td><td>4.2</td><td>7.4</td><td>8.4</td></tr><tr><td>Comm. Roll rate [deg/s]</td><td>25.7</td><td>27.7</td><td>27.2</td><td>29.1</td></tr><tr><td>Comm. Pitch rate [deg/s]</td><td>2.6</td><td>3.1</td><td>3.2</td><td>3.7</td></tr><tr><td>Vehicle Roll Angle [deg]</td><td>7.5</td><td>9.4</td><td>8.8</td><td>10.7</td></tr><tr><td>Vehicle Roll Rate [deg/s]</td><td>15.6</td><td>16.7</td><td>16.3</td><td>17.5</td></tr><tr><td>Target Cap-ture Time [s]</td><td>-</td><td>-</td><td>1.48</td><td>1.94</td></tr><tr><td>% Missed Targets/Run</td><td></td><td></td><td>6.6</td><td>13.0</td></tr></table>

116% and head yaw rates by 113%). In contrast, control activity and vehicle roll activity increase only slightly. The high correlation between head yaw activity and tracking errors, again demonstrate that head rotation, in excess to the amount needed for the vehicular control task, negatively affects performance. As expected, due to increased main task difficulty, the high-curvature canyon resulted in a 31% higher average target capture time and yielded twice as much missed targets.

Although in this experiment the head rotation is artificially and purposefully induced, similar performance degradation is expected to occur, when the pilot voluntarily moves his head in search of targets or mission threats. Consequently, for HMD's subjected to line-of-sight slaving system lags, the pilot will tend to reduce his head rotation to the minimum required for carrying out the vehicular control task. However, under these conditions, the wide-angle coverage of the line-of-sight slaving system will not be fully utilized and target search performance and spatial orientation will be seriously impaired.

# Summary of results

1. The experimental results have clearly shown that line-of-sight slaving system imperfections in HMD's seriously impair the pilot's ability to derive Control-Oriented Information from the visual field. Since, under these conditions, the pilot will tend to minimize head rotations, the wide-angle coverage provided by the slaving system, will not be utilized and search performance and spatial orientation will be impaired.   
2. Canyon following performance was found to deteriorate with increased head rotation, either when introduced in a "natural manner" through a higher path curvature, or when induced purposefully by using the target capture secondary task.   
3. The vehicle path estimation accuracy and head yaw rate activity generally increase with the V/h ratio. Due to the larger "local expansion" the far viewing distances yield more accurate estimates than close distances. However, due to blurring effects, close distance estimates no longer improve with V/h.   
4. The flight path for curved motion is considerably more difficult to estimate than for straight motion, since it relies on the entire streamer pattern rather than on local field estimates. Since in curved flight the near as well as the far field is used, the estimates are less accurate and improve less with increasing V/h ratio.

# DISCUSSION

The display system discussed in this paper can be classified as a virtual environment display. Head-mounted displays have become a vital component of virtual environments, which attempt to give the operator the illusion of being physically present in a remotely existing or synthetically generated world. Frequently this objective is achieved by fully immerging the operator in the visual scene by completely blocking out the direct view of the outside world and by presenting the operator with a stereo image of the environment, which is derived either from a remotely located stereo camera pair or computer generated. Although state-of-the-art miniature display technology and computer generated image techniques enable to display images of high quality, detail and authenticity, most system fail to provide the operator with the confidence to move around freely without the fear of stumbling or falling.

The main findings in this paper are valid for this general class of displays as well. While designers of virtual environments are devoting considerable attention to picture contents, quality and detail, the dynamic aspects are often neglected. Detrimental

factors are insufficient update rates, too large time delays due to time-consuming signal communication or highly band limited camera slaving systems. Other factors are inaccurate head position measurements and a lack of rigidity between the display and the head. While these displays may be adequate for a seated person in a near-static environment, in the presence of slow head motions, they often fall short in situations in which self-motion estimation is essential, such as walking, running or controlling a vehicle. Since correct motion estimation from visual cues is only possible when the illusion of an inertially stable background is preserved, deviations induced by system lags or slaving system errors, will result in estimation errors in the self-motion variables. Furthermore, for the person immersed in the environment, the visual cues will be in conflict with the vestibular ones, resulting in disorientation, loss of balance or even motion sickness.

The display, discussed in this paper provides only "partial immersion" since the outside world remains directly visible both to the uncovered eye and to the covered one through the beam-splitter. This arrangement allows the pilot to maintain direct visual contact with the outside world in case of HMD system failures, or for scanning the cockpit instruments. Part of the task difficulty can be attributed to this dichoptic viewing situation, in which the pilot has to switch his attention consciously between the two eyes.

Future research effort should be devoted to exploring ways to eliminate the need for maintaining direct visual contact with the outside world by incorporating all necessary information in a stereoscopic, full immersion display. This might require integrating the present cockpit panel information in the HMD image, and the use of superimposed display symbology, such as a vehicle path trace, a vehicle axis or velocity vector symbol. This superimposed symbology would serve in compensating for the lack of peripheral vision resulting from the narrow HMD field-of-view. Engineering efforts should be devoted primarily to solving the display-to-head rigidity problem, minimizing slaving system errors and enlarging the effective HMD field-of-view.

# ACKNOWLEDGEMENTS

This research has been supported by a grant from NASA Ames Research Center, Aerospace Human Factors Research Division, Moffett Field, Ca. 94035, under cooperative agreement No. NAGW-1128. Dr. S. Hart and Dr. D. Foyle of Ames Research Center have been the Scientific monitors for this grant.

# REFERENCES

1. Oman, C.M., "Sensory Conflict in Motion Sickness: an Observer Theory Approach," in: Pictorial Communication in Virtual and Real Environments, Eds. Ellis, S.R., Kaiser, M.K. and Grunwald, A.J., Taylor and Francis, 1991.   
2. Grunwald, A.J., Kohn, S. and Merhav, S.J., "Visual Field Information in Nap-of-the-Earth Flight by Teleoperated Helmet-Mounted Displays," SPIE/SPSE Symposium on Electronic Imaging: Science and Technology, Feb. 24 - March 1, 1991, San Jose, Ca., Paper No. 1456-17, 1991.   
3. Gibson, J.J., "The Perception of the Visual World," Houghton Mifflin, Boston, Mass., 1950.   
4. Gibson, J.J., Olum, P. and Rosenblatt, F., "Parallax and Perspective During Aircraft Landings," American Journal of Psychology, Vol.68, 1955, pp.372-385.   
5. Gibson, J.J., Visually Controlled Locomotion and Visual Orientation in Animals," British Journal of Psychology, Vol.49, 1958, pp.182-194.   
6 Boff, K.R., Kaufman, L. and Thomas, J.P., "Handbook of Perception and Human Performance," Vol. 1, Wiley N.Y., 1986, page 16-18, pages 17-18 to 17-20.

# Handling Qualities Effects of Display Latency

# David W. King Technical Specialist Flying Qualities

# Boeing Defense & Space Group, Helicopters Division Philadelphia, Pennsylvania

# Abstract

Display latency is the time delay between aircraft response and the corresponding response of the cockpit displays. Currently, there is no explicit specification for allowable display lags to ensure acceptable aircraft handling qualities in instrument flight conditions. This paper examines the handling qualities effects of display latency between 70 and 400 milliseconds for precision instrument flight tasks of the V-22 Tiltrotor aircraft. Display delay effects on the pilot control loop are analytically predicted through a second order pilot crossover model of the V-22 lateral axis, and handling qualities trends are evaluated through a series of fixed-base piloted simulation tests. The results show that the effects of display latency for flight path tracking tasks are driven by the stability characteristics of the attitude control loop. The data indicate that the loss of control damping due to latency can be simply predicted from knowledge of the aircraft's stability margins, control system lags, and required control bandwidths. Based on the relationship between attitude control damping and handling qualities ratings, latency design guidelines are presented. In addition, this paper presents a design philosophy, supported by simulation data, for using flight director display augmentation to suppress the effects of display latency for delays up to 300 milliseconds.

# Notation

<table><tr><td>AFCS</td><td>Automatic Flight Control System</td></tr><tr><td>CHPR</td><td>Cooper-Harper Pilot Rating</td></tr><tr><td>FCSIR</td><td>V-22 Flight Control System. Interface Rig</td></tr><tr><td>ILS</td><td>Instrument Landing System</td></tr><tr><td>IMC</td><td>Instrument Meteorological Conditions</td></tr><tr><td>K</td><td>Pilot control gain (in/deg)</td></tr><tr><td>Ncw</td><td>Pilot workload metric</td></tr><tr><td>Npartf</td><td>Tracking performance metric</td></tr><tr><td>MFD</td><td>V-22 cockpit Multi-Function Display</td></tr><tr><td>P</td><td>Aircraft roll rate (deg/sec)</td></tr><tr><td>TL,TI</td><td>Pilot model lead, lag time constants (sec)</td></tr><tr><td>Yc(jω)</td><td>Aircraft + control system transfer funct.</td></tr></table>

Presented at Piloting Vertical Flight Aircraft: A Conference on Flying Qualities and Human Factors, San Francisco, California, 1993.

<table><tr><td>Yp(jω)</td><td>Pilot model transfer function</td></tr><tr><td>δ</td><td>Lateral stick control input (inches)</td></tr><tr><td>Φ</td><td>Phase of pilot-a/c-display system (deg.)</td></tr><tr><td>Φm</td><td>Phase margin pilot-a/c-disp. systm. (rad)</td></tr><tr><td>Φ∞</td><td>Phase margin of aircraft system(rad)</td></tr><tr><td>σ</td><td>Tracking error standard deviation(deg)</td></tr><tr><td>Δγ</td><td>Localizer tracking error (deg)</td></tr><tr><td>ΔΓ</td><td>Glideslope tracking error (deg)</td></tr><tr><td>ΔV</td><td>Airspeed tracking error (kts)</td></tr><tr><td>ξ</td><td>Pilot-a/c-display system damping ratio</td></tr><tr><td>ωc</td><td>Pilot crossover frequency (rad/sec)</td></tr><tr><td>τc</td><td>Control system delay (sec)</td></tr><tr><td>τd</td><td>Display delay (sec)</td></tr><tr><td>tr</td><td>Display low-pass filter time constant (sec)</td></tr><tr><td>tp</td><td>Pilot delay (sec)</td></tr></table>

# Introduction

The next generation of military rotorcraft are being designed to fulfill an astonishingly wide range of mission objectives. Due to an explosive growth in avionic system technology tasks which were unthinkable ten years ago, including nap-of-the-earth flight in low visibility, are now possible. Crew station designers are challenged to integrate the state-of-the-art technologies to provide the means to accomplish ambitious mission objectives, while also assuring that the performance of "routine" flight tasks is not degraded. Unfortunately, one side effect of complex avionic systems, known as display latency, stands as an obstacle to this challenge.

Display latency is defined as "the time delay between sensor detection of aircraft movement and the corresponding indication on the cockpit displays." The advent of the fully integrated all-glass cockpit allows pilots to selectively access a wide range of flight information including aircraft attitude, rates, navigation information, threat and/or target status, aircraft systems information, and engine parameters. Aircraft sensor information is digitally processed in onboard computers and may be accessed by the pilot through selectable cockpit displays, or through head-up/helmet-mounted display systems. However, the processing and

transportation of the flight data takes time. During nighttime or adverse weather conditions the delay of fundamental flight information, such as aircraft attitude and rates, may adversely affect the pilot's ability to control his aircraft. Currently, there is no explicit military specification for display latency and little research data on the subject. Designers of new aircraft are thus faced with the unanswered question of how much latency is acceptable.

This paper evaluates the relationship between display latency and instrument flight handling qualities for the V-22 Tiltrotor aircraft. The three goals of this study were to quantify handling qualities trends (performance, workload, and pilot ratings) from varying levels of display latency, to generate methods to predict aircraft sensitivity to display latency, and to investigate methods to subdue latency effects. Using classical control theory, a second order linear model of the pilot-aircraft-display system was developed to analyze latency effects. Extensive piloted simulation was performed to support the analytical model and gather handling qualities data for different levels of latency. Finally, flight director displays were investigated as a means to augment the pilot control loop and suppress the latency effects.

# Background

The V-22 Osprey Tiltrotor is a revolutionary aircraft designed to meet the mission requirements of all four military services. Besides providing basic control functions in multiple flight modes (helicopter - conversion - airplane), the V-22 digital flight control system and fully integrated avionic system provide maneuver limiting, fully coupled flight path tracking, integrated cockpit management, and thrust - power management regulation. Subsequently, the V-22 exhibits a substantial amount of display latency due to the digital processing and transportation of the sensor data as it is passed from an avionics data bus to the Flight Control Computer and the Mission Computer, where it is processed,

图片摘要：该图主要展示 1. Avionics architecture。
![](images/48632a308903da7eefd048ce0dc26e90b31b24c006768bf4a508f247bd5de70c.jpg)  
Figure 1. Avionics architecture

and then passed to the Display Electronics Unit (DEU) where the symbology is drawn on the cockpit Multi-Function Displays (MFD) as shown in Figure 1. Measurements indicate an average latency of 211 milliseconds (ms) for the V-22 attitude display.

It is intuitive to assume that in the absence of any out-the-window visual cues, a quarter-second display delay might be troublesome. For a precision flight task in instrument conditions, the pilot controls his aircraft by closing the loop between the cockpit displays and the aircraft control inputs as shown in Figure 2. The pilot acts as an optimal, adaptive, multi-loop control element by applying control inputs to track a prescribed flight condition indicated on the displays. System delays, such as control system and aircraft lags, have been shown to degrade aircraft handling qualities for tasks requiring high frequency control inputs (Ref. 1). Extensive research (Refs. 2,3) has shown that control system delays in excess of $100\mathrm{ms}$ are likely to degrade the ease and accuracy at which a pilot can successfully perform demanding visual tasks. Subsequently, control system lags are limited to $100\mathrm{ms}$ (for level 1 handling qualities) in flying qualities military specifications (Refs. 4,5). However, fundamental differences in pilot technique between visual flight and instrument flight preclude the direct application of control system delay specifications to display delay. Pilots are trained to fly instrument tasks with milder and more deliberate control inputs than corresponding visual tasks. Furthermore, precision instrument tasks often require display augmentation, visual aids, or selectable automatic control modes which are not considered in visual flight task specifications. Unfortunately, most of the previous research on display delays has been limited to simulator delays (Ref. 6) and highly maneuverable fixed-wing aircraft (Ref. 7).

The bottom-line handling qualities criterion for a developmental aircraft such as the V-22 is to provide Level 1 Cooper-Harper pilot ratings. Cooper-Harper pilot ratings (Ref. 8) provide a qualitative assessment of the pilot's ability to successfully perform a given task with a tolerable amount of workload. A Level 1 rating implies the aircraft is "acceptable without improvement." In order to substantiate Level 1 compliance, the aircraft must be flight-tested

图片摘要：该图主要展示 1. Avionics architecture。
![](images/ef32968fb9a9667e418b54bd317258181b73ade11e802ff6fd294b6d6ccaf80f.jpg)  
Figure 2. Pilot control loop

throughout its flight envelope including the full range of mission tasks. Subsequent handling qualities ratings depend on several variables including performance requirements, aircraft stability characteristics, flight control system functionality, cockpit displays, crew station format, and pilot proficiency. It is therefore not straightforward to isolate the effects of a single factor such as display latency on handling qualities results during limited flight testing of a developmental aircraft. In order to prevent display latency from unexpectedly handicapping a developmental aircraft late in its flight test program, system designers require either specific latency guidelines or simple techniques to evaluate latency effects.

# Evaluation Procedure

Handling qualities engineers often employ analytical models of the pilot-aircraft closed-loop system to predict and analyze the effects of specific aircraft and control system parameters on simple flight task performance. The pilot is modelled as a servo-actuator control element which provides aircraft control inputs to follow a command profile. Various linear pilot models have been developed including single-input/single-output, multiple-input/multiple-output (Ref. 9), optimal control (Ref. 10), and structural models (Ref. 11). One of the simplest and most often used is the classical control theory pilot crossover model. The crossover model (Refs. 12,13) states that a sufficiently trained pilot linearly relates a control input to a tracking error such that the open-loop pilot-aircraft system provides the following frequency domain characteristics (Figure 3):

1) Sufficient bandwidth (crossover frequency) for task tracking and disturbance rejection,   
2) Adequate stability margins (phase margin $>45$ degrees), and   
3) An integrator-like response at the crossover frequency.

Use of the crossover model has several advantages including: a) ease of implementation, b) flight task and aircraft characteristics sufficiently define pilot parameters, c) straightforward validation from flight or simulator data, and d) frequency-domain approach easily related to physical system. The primary limitation of the crossover model is that pilot behavior for most flight tasks cannot be accurately described in a fixed, linear, single-input/single-output (SISO) context. However, the display latency problem is well suited to the crossover model. Most instrument tasks are characterized by a control objective to maintain a displayed parameter (i.e. attitude, airspeed, vertical velocity) in a desired position (i.e. level, fixed speed, constant altitude). This results in a relatively simple control loop and describes the pilot's innermost control loop for each input axis. Also, there is less likelihood of "nonlinear" pilot behavior due to external stimuli such as abrupt motion and peripheral visual

cues for instrument flight compared to visual flight. Research has shown (Refs. 12,13) that handling qualities ratings are best correlated with the stability characteristics of the inner control loop for the most difficult control axis. For the V-22 in helicopter and conversion modes (Ref. 17), the roll axis exhibits the lowest stability margins and will thus be the focus of the analytical study.

Fixed-base piloted simulation was used extensively to evaluate the handling qualities effects of display latency in a controlled environment. Since the reduced visual cue environment of simulators is not an issue for instrument flight, simulation provides a high fidelity platform for handling qualities testing. The display generator of the V-22 simulator at the Boeing Helicopters Flight Simulation Laboratory (Ref. 18) was reconfigured to allow latency to be varied from $70~\mathrm{ms}$ to $400~\mathrm{ms}$ in $33~\mathrm{ms}$ increments. Two flight tasks were simulated in instrument meteorological conditions (IMC) to serve the dual purpose of validating the single-loop crossover model analysis and evaluating latency effects for a high-gain operational task. The first task consisted of single-axis roll attitude tracking where the pilot maneuvered the aircraft to track a commanded bank angle symbol which prescribed moderate rate roll maneuvers. In the second task, the pilot was required to capture and track the final leg of an Instrument Landing System (ILS) approach to a vertical landing at a VTOL pad. Both moderate and high speed approaches were tested with visibility lim

图片摘要：该图主要展示 3. Pilot/aircraft system crossover model。
![](images/42d4fa81eec1647541e4c15a1364fbca1602b724cd9fff14046dec2f07a7e46a.jpg)  
Figure 3. Pilot/aircraft system crossover model

ited to 2500 feet so that the landing pad was not observable until the approach Decision Height (200 feet above ground level) was reached. Moderate levels of turbulence, wind shear, and crosswind were utilized to demand constant pilot control inputs.

# Attitude Loop Analysis

Time delay effects on aircraft controllability are best described by the innermost (attitude) control loop. For attitude control, the crossover model relates the pilot control input to the displayed attitude error in the transfer function form:

$$
Y _ {p} = K \frac {T _ {L} S + 1}{T _ {I} S + 1} e ^ {- T _ {P} S} \tag {1}
$$

where $\mathbf{K}$ is the pilot control gain and $T_{L}, T_{r}$ , and $\tau_{p}$ are the pilot lead, lag, and neuromuscular delay time constants, respectively. The neuromuscular delay is defined as "the time required for the pilot to comprehend display information, determine, and physically apply the appropriate input." Included in the pilot delay parameter are fixed and variable components. The fixed component, estimated at around 60 ms - 100 ms (Ref. 12), is due to inherent physiological delays, and the adjustable component is due to the pilot display scan rate and concentration level. The adjustable delay component can be reduced, where necessary, at the expense of increased cognitive workload. The control gain and lead compensation parameters are optimized by the pilot in the same hierarchical fashion as a control system designer tunes a servomechanism. That is, the gain is set for stability, then compensation is added to meet bandwidth requirements with the parameters subject to energy constraints. For example, during a high frequency target tracking task the pilot will provide a control gain sufficient to minimize the tracking error while maintaining adequate stability margins. If system delays, or aircraft dynamics, do not allow stable, high frequency control, the pilot will be forced to add lead compensation to perform the task. Lead compensation, which may be perceived as "stick pulsing", significantly increases the pilot control workload. On the other hand, if the task is simply to maintain level flight with only moderate disturbances, the pilot will act to minimize workload in the form of lower control gain, no lead compensation, and a comfortable scan rate.

Simply stated, the pilot-aircraft crossover frequency may be estimated based on control theory given knowledge of the aircraft stability characteristics, system delays, and task control bandwidth requirements. In order to accommodate demanding visual tasks (i.e. shipdeck hovering, in-flight refueling), the V-22 digital flight control system provides high bandwidth control throughout its operational envelope. Figure 4 shows the frequency response of the lateral axis for the augmented V-22 (AFCS on, rate command

图片摘要：该图主要展示 4. frequency response at 120 kts。
![](images/21c60750a70a4872883e4c0f908da07399741950be29766d37b716f2e0b781c9.jpg)

图片摘要：该图主要展示 4. frequency response at 120 kts。
![](images/b47bbccc6e7afa71e96b778392e93d08cd4495faa5eff05bd20e31d7c0eeb76d.jpg)  
Figure 4. $P / \text{Stat}(\text{deg/sec/in})$ frequency response at 120 kts.

attitude hold system) at a 120 knot flight condition. It is seen from the Bode diagram that if the pilot-aircraft-display system contained no time delays, the pilot could maintain integrator response (-20 db/decade gain slope) for control bandwidths up to 6 rad/sec with pure gain compensation and sufficient stability margins. High gain flight tasks, such as precision hover, mandate control bandwidths in the range 1 rad/s < ωe < 4 rad/s (Refs. 15,16).

The most demanding operational requirements for the V-22 in IMC consist of "flight path tracking tasks" at high speed and low altitude such as terrain following and aggressive approach-to-landings. Flight path tracking may be viewed as an "outer-loop" control function, as shown in Figure 5, where the pilot corrects for low-frequency flight path errors by adjusting commands to the high-frequency attitude control loop. In general, the flight path tracking outer-loop requires a bandwidth one-quarter of the attitude tracking inner loop. Therefore, for limited amounts of delay, the V-22 stability bandwidth (based on phase characteristics) is significantly greater than the required task bandwidth for flight path tracking instrument tasks. This implies that the pilot crossover frequency will be determined by workload factors alone. A general rule-of-thumb in this case (Ref. 16) is that the crossover frequency will equal the maximum of the phase plot such that

$$
\omega_ {c} = \omega_ {\text {f e m a x}}.
$$

Applying the rule to Figure 4 indicates that for the V-22 lateral axis at 120 knots,

$$
\omega_ {c} = 2 \mathrm {r a d / s e c}. \tag {2}
$$

图片摘要：该图主要展示 5. Pilot control structure for flight path tracking。
![](images/3ae5e7068e4221f8eb56df9e137ebb6460058662a9506be1c071c4ae936c81b8.jpg)  
Figure 5. Pilot control structure for flight path tracking

Assuming that the crossover frequency is 2 rad/s for V-22 precision instrument tasks, the crossover model may be used to predict the effects of pilot and display delays. System delays act to linearly reduce the phase of the pilot-aircraft system such that,

$$
\Phi = \Phi_ {o} - \omega_ {c} \left(\tau_ {p} + \tau_ {d} + \tau_ {c}\right) \tag {3}
$$

where $\Phi_{\mathrm{o}}$ is the phase of the aircraft alone and $\tau_{p},\tau_{d},\tau_{c}$ are the delay times of the pilot, displays, and control system, respectively. Control system delays for the V-22 have been measured through frequency response testing on the Boeing Helicopters Flight Control System Interface Rig (FCSIR) (Ref. 17) and the data is presented in Table 1. Using the second order system approximation between phase margin and damping ratio, and combining the maximum control system delay of 50 milliseconds with a conservative estimate of the pilot neuromuscular delay of $250~\mathrm{ms}$ (based on simulator time history matches), the system damping ratio is related to the latency such that

$$
\begin{array}{l} \xi = \Phi_ {m} \left(\frac {5 7 . 3 \mathrm {d e g} / \mathrm {r a d}}{1 0 0 1 / \mathrm {d e g}}\right) \tag {4} \\ = 0. 5 7 3 \Phi_ {\infty} - 0. 5 7 3 \omega_ {c} (\tau_ {d} + 0. 3) \\ \end{array}
$$

where $\Phi_{\mathfrak{m}}$ is the phase margin of the pilot-aircraft-display system, and $\Phi_{\mathfrak{m0}}$ is the aircraft phase margin (1.92 radians). Figure 6 shows the system damping reduction due to

Table 1. V-22 control system delays   

<table><tr><td>Input</td><td>Output</td><td>FCSIR delay</td><td>SIM delay</td></tr><tr><td>longitudinal stick</td><td>longitudinal cyclic</td><td>50.75 ms</td><td>50.0 ms</td></tr><tr><td>longitudinal stick</td><td>elevator</td><td>26.25 ms</td><td>50.0 ms</td></tr><tr><td>lateral stick</td><td>diff. collective pitch</td><td>50.75 ms</td><td>50.0 ms</td></tr><tr><td>lateral stick</td><td>flaperon</td><td>25.00 ms</td><td>50.0 ms</td></tr><tr><td>pedals</td><td>diff. collective pitch</td><td>50.75 ms</td><td>50.0 ms</td></tr><tr><td>pedals</td><td>rudder</td><td>34.85 ms</td><td>50.0 ms</td></tr><tr><td>thrust control lever</td><td>collective pitch</td><td>50.75 ms</td><td>50.0 ms</td></tr><tr><td>thrust control lever</td><td>engine command (FADEC)</td><td>38.75 ms</td><td>50.0 ms</td></tr></table>

display latency increases between 70 milliseconds and 400 milliseconds. Handling qualities studies (Refs. 17,18) have shown that for phase margins less than 45 degrees, task performance may be limited by overshoot tendencies for abrupt control inputs, and this corresponds to the required aircraft phase margin in the military specifications (Ref. 5). Therefore, it is expected that the pilot will reduce the control gain, or add lead compensation, to continually maintain stability margins over 45 degrees. It is observed from Figure 6 that the pilot is unable to sustain this criterion with pure gain compensation for latencies exceeding 317 milliseconds.

# Piloted Simulation

The V-22 simulator consists of a validated aircraft mathematical model operated real-time on a multi-processor computer with a fixed-base emulation of the V-22 dualplace crew station. Cockpit cues are provided to the pilot through out-the-window scenes produced by an Evans and Sutherland CT-6 computer image generation system, a displacement cyclic controller with a programmable forcefeel system, a small-displacement $(+ / - 2$ inches) thrust control lever, and two CRT multi-function displays per pilot station. The simulator has been shown to be a high fidelity representation of the aircraft through time histories and handling qualities evaluations matched to flight test (Ref. 14). Real-time simulation processing is run at a

图片摘要：该图主要展示 6. Predicted damping ratio vs. latency。
![](images/5057650ae8c327fa8ed94025ee57483036c9a0f5ed7098e99857a00a08f9cd59.jpg)  
Figure 6. Predicted damping ratio vs. latency

frequency of 20 hertz which yields, on average, a control delay of 50 milliseconds. This falls within 25 ms of the aircraft control delays as shown in Table 1. A high performance Silicon Graphics IRIS-4D/80 CG display generator computer drives the simulator displays interlaced at a frequency of 60 hertz. In order to vary the display latency, a software buffer was inserted in the display generator which held the symbology data in multiples of two display cycles according to an operator selectable index. The inherent display delay, from the mathematical model output until completion of the display generation cycle, was measured at an average of 73 milliseconds. Therefore, the possible display latency test points were 73 ms, 107 ms, 140 ms, etcetera. In order to verify the latency values, measurements were taken prior to each simulation test by sending a discrete signal through the mathematical model and measuring the analog time difference between the model output and display generator optical output.

# Attitude tracking task

Display delay effects on the attitude control loop were evaluated with a pilot-in-the-loop through an attitude tracking task simulation. The pilot was asked to track a commanded attitude symbol with the aircraft nose symbol on the displays, as shown in Figure 7, "to the best possible control accuracy." Moderate rate (3 to 5 deg/sec) bank angle captures of 10 degree amplitude were used to drive the command symbol. The commands were interjected in a random manner to prevent "pilot anticipation" from masking the results. Results were obtained with two highly trained V-22 evaluation pilots during a total of 4.6 hours simulation time. The data consisted of both tracking performance and workload measurements which were digitally recorded and statistically processed real-time, combined with qualitative pilot comments. All tests were run at a flight condition of 120 knots airspeed with the nacelles tilted at a 60 degree incidence (where 90 degrees is referenced at helicopter mode). This flight condition was chosen as representative of precision instrument tasks for the V-22.

A straightforward metric, referred to as the $2\sigma$ -bound, was used to gauge the attitude tracking accuracy. During each test run, which consisted of bank angle captures in each direction over a one minute test period, the $2\sigma$ -bound was calculated by doubling the standard deviation of the bank angle tracking error and adding the mean value. In simple terms, this statistic measures the aircraft dispersion about the commanded attitude. For a normally distributed tracking error, the $2\sigma$ -bound represents the absolute value such that the probability of exceeding the bound is approximately $5\%$ at any instant in time.

In a similar manner, a workload metric referred to as the control workload index was used to quantify the magnitude of pilot control activity. The control workload index $(\mathbf{N}_{cw})$ was calculated as

$$
N _ {c w} = \frac {1}{2} \left(\frac {\delta_ {r m s}}{\delta_ {r m s - r q}} + \frac {\stackrel {\bullet} {\delta} _ {r m s}}{\delta_ {r m s - r q}}\right) \tag {5}
$$

where,

$$
\begin{array}{l} \delta_ {\text {r m s}} = \text {r o o t - m e a n - s q u a r e o f l a r e l a r s t i c k d e f l e c t i o n} \\ \dot {\delta} _ {\text {r m s}} = \text {r o o t - m e a n - q u a r e o f l a r e l a r s t i c k r a t e .} \end{array}
$$

The normalizing parameters represent the minimum required stick activity to track the command as determined from the V-22 autopilot. By combining a measure of stick deflection variance and stick rate variance, the control workload index measures the amount the pilot is forced to move the controls and vary the control frequency. This provides a basis for comparing control activity between test runs.

Figure 8 presents the simulation performance and workload measurements plotted against latency value. The plots indicate the average values from four data runs at each latency value (for each latency test point the pilots were allowed a few training runs prior to data collection). From the workload plot it is clear that the display delay effects can be broken into three regions:

1) $\tau_{d} < 140$ ms: a no-effect region where the latency does not significantly impact attitude control,   
2) $140\mathrm{ms} < \tau_{\mathrm{d}} < 307\mathrm{ms}$ : a degraded attitude control region where the pilot works harder to maintain desired attitude, and   
3) $\tau_{\mathbf{d}} > 307$ ms: a gain reduction region where the pilot is forced to ease control aggressiveness to assure adequate system stability.

图片摘要：该图主要展示 8 presents the simulation performance and workload measureme。
![](images/32118d7e6c30372eb30082b049ab801a7b76858d5a23dc3b169a4064b5173a34.jpg)  
Figure 7. Attitude tracking display

图片摘要：该图主要展示 7. Attitude tracking display。
![](images/50aee12c5bcfeb28d916f4589d3ff2fe7e41eef75d2259fc9cd4e352503a34fa.jpg)

图片摘要：该图主要展示 7. Attitude tracking display。
![](images/3526f465251439f0b1c5097d91a7857618d58456c123dd47180f8e97d08f5e36.jpg)  
Figure 8. Attitude tracking simulation results

The pilot gain reduction breakpoint corresponds well with the pilot model analysis which predicted that the 45 degree phase margin criterion would not be met for latencies exceeding $317\mathrm{ms}$ . Sample time histories for one run in each of the three regions are shown in Figure 9 and illustrate the loss of control damping with latency variations. Superimposed on the plots are time histories from the second order analytical model. At the higher latency values, the control oscillations of the simulator data were more prominent than the model predicted and are most likely due to nonlinearities in the pilot compensation.

Accordingly, the tracking performance plot indicates that as the delay increases and stability margins are reduced, tracking difficulty increases. A linear regression fit to the tracking performance data shows a bank angle control degradation of one-half degree for every $100\mathrm{ms}$ of added latency. Pilot comments indicated that lead compensation was applied for latencies over $240~\mathrm{ms}$ in an attempt to alleviate tendencies to overshoot the commanded attitude.

# ILS approach task

The final leg of a low-visibility ILS precision approach was simulated with six different latency values between 70 ms and 400 ms. The task was initialized with an initial offset from the desired glidepath at approximately 2000 feet above ground level, challenging the pilot to acquire the ILS glidepath and track to a decision height of 200 feet. The approaches were flown at airspeeds of 85 knots and 120 knots, and the task was terminated at decision height. Turbulence, wind shear, and crosswind models were implemented in the simulation to induce disturbances. The turbulence consisted of a body-fixed sampling Dryden model with the intensity and scale length parameters set according to "moderate" specifications of MIL-F-8785C (Ref. 4). In addition, a 20 knot wind at a 45 degree azimuth from the approach course was implemented with a "moderate" wind shear profile added per MIL-F-8785C.

The flight displays consisted of the vertical situation display

图片摘要：该图主要展示 9. Attitude tracking time histories。
![](images/2ead292e9da212237ed401c5b523afe53a470f03e7c7c81725c1bbf59dcbbb8c.jpg)  
Figure 9. Attitude tracking time histories

of Figure 7 plus a horizontal situation display with the ILS localizer and glideslope deviation indicators as shown in Figure 10. In order to receive pilot handling qualities ratings per the Cooper-Harper scale, performance constraints were issued to the pilot. For "desired" performance the pilot was required to track the glidepath within the following constraints for more than $80\%$ of the approach and be within constraints at decision height: localizer deviation $(\Delta \gamma)$ less than $+/-1$ degree, glideslope deviation $(\Delta \Gamma)$ less than $+/-0.25$ degree, and airspeed deviation $(\Delta V)$ less than $+/-5$ knots. Yaw axis control was not required since the V-22 control system automatically provides trun coordination and heading hold features. "Adequate" performance constraints were set at double the desired constraints. It should be noted that in the V-22 the pilot is required to scan an azimuth of approximately 10 degrees to monitor all necessary ILS flight information on the two displays.

Data was recorded for five highly trained evaluation pilots during simulation spanning over 34 hours. In addition to 126 data runs, more than 200 runs were performed for pilot training purposes. Simulation studies (Refs. 18,19) have shown that biases may result in handling qualities evaluations between alternate configurations due to cross-training effects. This means that variations in pilot rating between different configurations may depend on the order in which they are tested. To subdue cross-training effects, latency values were tested in varying sequence and several runs were allotted for training at each test point. For each data run, performance and workload metrics were calculated real-time. The performance metric consisted of the normalized $2\sigma$ -bound averaged between the three tracking variables such that

$$
N _ {\text {p e r f}} = \frac {1}{3} \left(\frac {\Delta V _ {2 \sigma}}{5 \mathrm {k t s}} + \frac {\Delta \gamma_ {2 \sigma}}{1 \mathrm {d e g}} + \frac {\Delta \Gamma_ {2 \sigma}}{0 . 2 5 \mathrm {d e g}}\right) \tag {6}
$$

图片摘要：该图主要展示 10. ILS displays。
![](images/8f655e2282e7f2123100bbfbc15a7954d5ae481b858396d911d191b2db13f522.jpg)  
Figure 10. ILS displays

图片摘要：该图主要展示 10. ILS displays。
![](images/518031b79626a40a6536efd0a61770b11387b3eaa720b49623602d7ab259eac1.jpg)

图片摘要：该图主要展示 10. ILS displays。
![](images/eaa79d3247257e0f52654624c2c032f3725c7476149df3af554bd692a698dca9.jpg)

图片摘要：该图主要展示 10. ILS displaysFigure 11. ILS task simulation results The d。
![](images/a44e5fc473e30a4e810e207ab99e53a61d71ceec4119a6b57968884470e51e0d.jpg)  
Figure 11. ILS task simulation results

The desired constraint parameters were used as the normalizing factors such that performance indices less than unity indicate that the aircraft was maintained within desired constraints for at least $95\%$ of the run. The root-mean-square of the control deflections from trim were used as the workload metric.

Figure 11 displays the median performance indices, Cooper-Harper pilot ratings (CHPR), and lateral stick workload metric (lateral inputs were by far the most active) versus display latency. Median values, as opposed to averages, were used to eliminate the weighting effect of poor performance data during a few runs when the pilot aborted the approach and prepared for a go-around. The performance plot indicates that, although variations in performance resulted, there were no discernable trends relating tracking performance to latency for test points between 70 ms and 300 ms, and only a slight reduction in tracking accuracy at 400 ms, as indicated by the relatively flat distribution of the median values. This was predicted by the attitude loop analysis which showed that delays up to 300 ms are not sufficient to degrade the performance of the low bandwidth flight path tracking outer loop. However, the pilot ratings and workload plots do indicate a control degradation for latencies between 140 ms and 300 ms which is consistent with the "degraded attitude control region" identified in the attitude tracking task. Comments indicated that the pilots were perceptually unaware of latency changes between configurations, but that they acquired different control techniques due to "slight changes in aircraft response characteristics." The altered control techniques appeared as lateral stick pulsing during small heading changes at the 270 ms and 400 ms latencies which was not required at 70 ms. This was caused by the loss of attitude control damping and resulted in a one-half Cooper-Harper point degradation between 140 and 270 milliseconds.

# Corrective Measures

At 211 ms of display latency, the loss of attitude control damping produced a slight degradation (less than 1/2 CHPR point) in V-22 instrument approach handling qualities relative to a minimum latency of 70 ms. Furthermore, the handling qualities ratings for all latency values tested were consistently a level 2 classification which implies that "deficiencies warrant improvement." Pilot comments indicated that workload issues mandated the level 2 ratings, and the workload was increased by a difficulty in assimilating all the necessary flight information and determining the proper input to zero the ILS tracking deviations. It is therefore desirable to 1) suppress the latency-induced attitude damping reduction and 2) reformat the presentation of ILS information to the pilot. These two objectives may be accomplished by the addition of flight director displays.

# Flight director

Flight director displays provide the pilot with pursuit-type cues to steer the aircraft along a commanded path. The command path is based on the flight path tracking error, such as an ILS deviation, and all control cues are presented to the pilot in a centralized location. Figure 12 shows the V-22 flight director symbology on the vertical situation display which consists of power, roll, and pitch cues. The dynamics of the flight director cues are selected to augment the stability characteristics of the closed-loop pilot-aircraft-display system to provide sufficient tracking performance with only pure gain pilot compensation. Several methodologies to optimize flight director designs are presented in the literature (Refs. 20,21) but do not address the issue of display latency.

Flight director designs can be used to suppress latency effects to only a limited degree. From Equation 3 it is observed that for pure gain pilot compensation and a fixed amount of display latency, the phase margin of the pilot-aircraft-display system can be increased by 1) reducing the pilot delay, 2) adding phase lead at the crossover frequency through display compensation, or 3) decreasing the crossover frequency. The ability of a flight director to reduce the pilot delay is easily recognizable. By using centralized cues, the display scan time will be reduced. And any time spent from pilot cognition (deduction of control input from flight path deviation indicators) will lessen since the flight director processor assumes the responsibility of calculating control inputs from the tracking error. However, benefits gained from adding phase lead or reducing the crossover frequency are mostly counter-productive since a reduction in the crossover frequency, through smaller gains or low-pass filtering, precludes any effect of phase lead. Similarly, adding phase lead in the displays will increase the crossover frequency unless the display gains are reduced. Therefore, with inherent display latency, the potential performance

图片摘要：该图主要展示 12. Flight director symbology。
![](images/93af3916f53610c379bf6b9439c66118e3be84e72f049f9cd813699f75b09f25.jpg)  
Figure 12. Flight director symbology

图片摘要：该图主要展示 12. Flight director symbology。
![](images/9c4e4b87288e7bd14affbfaf0f9e6bfc92b5191bb75e92be7b95acf06a4b409d.jpg)  
Figure 13. Flight director lateral cue processing

gains of a flight director are limited, but the flight director can improve instrument handling qualities by reducing the pilot delay and forcing the pilot to control at an "acceptable" crossover frequency.

For an ILS task the V-22 flight director lateral cue (Ref. 22) is driven by the localizer deviation shaped by washed-out bank angle and ground track angle feedback signals as shown in Figure 13. The gain ratios between the three feedback loops determine the relationship between the localizer deviation and the commanded lateral stick input. By increasing the gain on the bank angle loop, lead compensation is introduced which increases the crossover frequency of the pilot's attitude control loop. By adjusting the flight director gains, the inner loop crossover frequency can be selected to tradeoff the adverse effects of display latency with the benefits of increased tracking bandwidth. For the V-22 ILS task, the tradeoff can be biased toward subdueing the latency effects since sufficient tracking performance was obtained with raw-data displays.

# ILS re-simulated

The ILS approach task was repeated with the V-22 flight director active at a fixed latency value of 300 ms. Initially, several training runs were used to tune the flight director parameters at the fixed latency value. Since the baseline design did not account for large latency values, underdamped control responses were initially observed, and the flight director parameters were adjusted to reduce the system bandwidth. Figure 14 presents the median tracking performance and pilot rating results for six flight director runs with two evaluation pilots superimposed on the results from the raw-data runs. Level 1 pilot ratings, with tracking performance well within performance constraints, were consistently obtained with the flight director active. Furthermore, it was observed that consistency between runs was greatly improved, described by one pilot as "an improvement in damping and predictability with milder control inputs commanded from the flight director." Apparently, by forcing the pilot to control at a lower crossover frequency, the flight director improved the overall response characteristics of the pilot-aircraft-display system.

# Conclusions

It is the general belief in the rotorcraft handling qualities community that display latency degrades an aircraft's instrument flight capabilities, but, up to this point, no requirements on allowable latency have been produced. This paper investigates the handling qualities effects of varying levels of display latency analytically through the pilot crossover

图片摘要：该图主要展示 14. Flight director simulation results。
![](images/0f2ddcf2ee44c64b041ab7d357ae00521a8e2471a18dba3bf288e28d0285e1b7.jpg)

图片摘要：该图主要展示 14. Flight director simulation results。
![](images/b2b7a0e302ce4adb5bbe0fc4e4290bfffafc8d7c9ee0c8c817935fe61914881e.jpg)  
Figure 14. Flight director simulation results

model and experimentally through piloted simulation of the V-22 Tiltrotor aircraft. Latency effects on the lateral axis of the V-22 Tiltrotor aircraft were predicted through a second order crossover model of the attitude control loop, and the effects were tested through piloted simulation of both an attitude tracking task and a precision ILS approach. The results showed that the pilot workload involved in the ILS approach was directly related to a linear reduction in the damping ratio of the roll attitude control loop from 0.60 to 0.45 as latency was increased from $140\mathrm{ms}$ to $310\mathrm{ms}$ . The control damping reduction was predicted by the model based on the V-22 frequency response characteristics, control system lags, and instrument task bandwidth requirements. The display latency did not degrade flight path tracking performance, due to its low bandwidth, until the attitude loop phase margins fell below 45 degrees and the pilot was forced to reduce control gain. For an ILS approach task, the results indicated that pilot workload was increased as the attitude control damping was reduced, resulting in pilot rating degradations of $1/2$ CHPR between $140\mathrm{ms}$ and $270\mathrm{ms}$ of latency.

Flight director displays were then investigated as a means to suppress the increased workload effects of display latency. The results showed that flight director displays improve instrument flight handling qualities by reducing pilot cognitive workload, and they can suppress latency effects by regulating pilot control at an "optimal" crossover frequency.

Based on the results of this study the following conclusions were reached:

1) The handling qualities effects of display latency, in terms of pilot workload and task performance, are driven by the stability characteristics of the pilot's inner control loop.   
2) In general, an aircraft's robustness to display latency is proportional to its stability margins, and inversely proportional to the bandwidth required for its instrument flight mission tasks. Based on the test results which showed that damping ratios below 0.6 induce difficulties in precise attitude control, and damping ratios below 0.45 degrade precise flight path control, proposed latency guidelines are presented in Figure 15. The guidelines specify maximum delay values such that the latency will not significantly degrade handling qualities. The maximum delay values (display latency plus control system delay) are shown as a function of the aircraft phase margin and crossover frequency.   
3) The benefits of flight director lead compensation ("display quickening" - which increases control bandwidth), often used for high bandwidth instrument tasks, is limited by display latency since latency-induced reductions in control damping are linearly proportional to the crossover frequency.   
4) The V-22 exhibited "satisfactory" (level 1) handling qualities for latency values less than $300\mathrm{ms}$ based on its instrument task requirements and the use of flight director displays. Without flight director displays, an aggressive ILS approach task with moderate disturbances yielded level 2 handling qualities even at a minimum display latency of 70 milliseconds.

图片摘要：该图主要展示 15. Proposed latency guidelines。
![](images/f07bd3d157557da0f41f1e5ec5694d375f537e51ff14f26e64e17fe8edfb503f.jpg)

图片摘要：该图主要展示 15. Proposed latency guidelines。
![](images/6cab0b4e97e5315c8d576b7c454022a644b5820cc070a6edeed2d7136ed66c36.jpg)  
Figure 15. Proposed latency guidelines

# References

1. Smith, R.E., and Sarrafian, S.K., "Effect of Time Delay on Flying Qualities: an Update", AIAA Journal of Guidance, Control, and Dynamics, Sept.-Oct., 1986.   
2. Hoh, R.H., and Ashkenas, I.L., "Development of VTOL Flying Qualities Criteria for Low Speed and Hover," Systems Technology, Inc., Hawthorne, CA, TR-1116-1, Dec. 1979.   
3. Cooper, F.R., Harris, W.T., and Sharkey, V.J., "The Effect of Delay in the Presentation of Visual Information on Pilot Performance," NAVTRAEQIPCEN IH-250, Orlando, FL, Naval Training Equipment Center, 1975.   
4. Military Specification: "Flying Qualities of Piloted Airplanes," MIL-F-8785C, 5 Nov. 1980.   
5. Military Specification: "Flight Control Systems - Design, Installation, and Test of Piloted Aircraft, General Specification for," MILF-9490D, 6 June 1975.   
6. Ricard, G.E., and Puig, J.A., "Delay of Visual Feedback in Aircraft Simulators," NAVTRAIEQUIPCEN TN-56, Orlando, FL, Naval Training Equipment Center, 1976.   
7. Bailey, R.E., Knotts, L.E., Horoweitz, S.J., and Malone, H.L., "Effect of Time Delay on Manual Flight Control and Flying Qualities During In-Flight and Ground-Based Simulation," Proceedings of the AIAA Flight Simulation Technologies Conference, 1987.   
8. Cooper, G.E., and Harper, R.P., "The Use of Pilot Rating in the Evaluation of Aircraft Handling Qualities," NASA TN D-5153, April 1969.   
9. Hess, R.A., "Feedback Control Models," Handbook of Human Factors, edited by G. Salvendy, Wiley, New York, 1987, pp. 663-676.   
10. Kleinman, D.L., Baron, S., and Levison, W.H., "An Optimal Control Model of Human Response, Parts I, II," Automatica, Vol. 6, 1970, pp. 357-373.   
11. Hess, R.A., "A Theory for Aircraft Handling Qualities Based Upon a Structural Pilot Model," AIAA Journal of Guidance, Control, and Dynamics, Vol. 12, No. 6, 1989, pp. 792-797.

12. McRuer, D.T., and Jex, H.R., "A Review of Quasilinear Pilot Models," Transactions of Human Factors in Electronics, Vol. HFE-8, No. 3, Sept. 1967, pp. 231-249.   
13. McRuer, D.T., and Krendel, E.S., "Mathematical Models of Human Pilot Behavior," AGARDograph No. 188, Jan. 1974.   
14. Dabundo, C., White, J., and Joglekar, M., "Flying Qualities Evaluation of the V-22 Tiltrotor," presented at the 47th Annual Forum of the AHS, May 1991.   
15. Heffley, R.K., and Bourne, S.N., "Helicopter Handling Requirements Based on Analysis of Flight Maneuvers," presented at the 41st Annual Forum of the AHS, May 1985.   
16. Tischler, M.B., Fletcher, J.W., Morris, P.M., and Tucker, G.E., "Flying Qualities Analysis and Flight Evaluation of a Highly Augmented Combat Rotorcraft," AIAA Journal of Guidance, Control, and Dynamics, Vol. 14, No.5, 1991, pp. 954-963.   
17. Robinson, C., Dabundo, C., and White, J., "Hardware-in-the-Loop Testing of the V-22 Flight Control System Using Piloted Simulation," presented at the AIAA Flight Simulation Technologies Conference, Aug. 14-16, 1989, Boston, MA.   
18. Riccio, G.E., Cress, J.D., and Johnson, W.V., "The Effects of Simulator Delays on the Acquisition of Flight Control Skills: Control of Heading and Altitude," Proceedings of the Human Factors Society - 31st Annual Meeting, 1987.   
19. Ricard, G.L., Norman, D.A., and Collyer, S.C., "Compensation for Flight Simulator CGI System Delays," Proceedings of the 9th NTEC/Industry Conference, 1976.   
20. Garg, S., and Schmidt, D.K., "Cooperative Synthesis of Control and Display Augmentation," AIAA Journal of Guidance, Navigation, and Control, Vol.12, No. 1, 1989, pp. 54-61.   
21. Weir, D.H., Klein, R.H., and McRuer, D.T., "Principles for the Design of Advanced Flight Director Systems Based on the Theory of Manual Control Displays," NASA CR-1748, March 1971.   
22. Kilmer, R., "Design Analysis Report for the V-22 Guidance and Flight Director Sybsystem", submitted to Boeing Military Airplane Company by IBM Federal Systems Division - Oswego, NY, June 1987.

# EFFECTS OF SIMULATOR MOTION AND VISUAL CHARACTERISTICS ON ROTORCRAFT HANDLING QUALITIES EVALUATIONS

David G. Mitchell

Systems Technology, Inc.

Hawthorne, CA 90250

Daniel C. Hart

Aeroflightdynamics Directorate

U.S. Army Aviation and Troop Command

Ames Research Center

Moffett Field, CA 94035

# ABSTRACT

The pilot's perceptions of aircraft handling qualities are influenced by a combination of the aircraft dynamics, the task, and the environment under which the evaluation is performed. When the evaluation is performed in a ground-based simulator, the characteristics of the simulation facility also come into play. Two studies were conducted on NASA Ames Research Center's Vertical Motion Simulator to determine the effects of simulator characteristics on perceived handling qualities. Most evaluations were conducted with a baseline set of rotorcraft dynamics, using a simple transfer-function model of an uncoupled helicopter, under different conditions of visual time delays and motion command washout filters. Differences in pilot opinion were found as the visual and motion parameters were changed, reflecting a change in the pilots' perceptions of handling qualities, rather than changes in the aircraft model itself. The results indicate a need for tailoring the motion washout dynamics to suit the task. Visual-delay data are inconclusive but suggest that it may be better to allow some time delay in the visual path to minimize the mismatch between visual and motion, rather than eliminate the visual delay entirely through lead compensation.

# INTRODUCTION

Ground-based simulation is an important tool in the assessment of handling qualities for both research and development. The strengths and limitations of simulation are well known and recognized in the handling qualities community. What is not as well documented, however, is the relative impact of various elements in the simulator itself on perceived handling qualities. For example, past studies

(Ref. 1) have demonstrated that rate-augmented vehicles that exhibit good handling qualities in flight are much more difficult to control on ground-based simulators (e.g., Fig. 1).

Besides the obvious issues of simulation fidelity and flight/simulation transference (Ref. 2), there are other fundamental issues in simulation design that also impact the use of ground-based simulators for handling qualities research. All of these issues, such as inherent time delays and their compensation (Refs. 3 and 4), simulator sickness (Ref. 5), and the requirements on motion (Refs. 6, 7, 8, and 9), have been investigated in great detail in terms of their impact on human operator response dynamics and assessments of fidelity. Few studies, however, have explored the specific impact of these issues on handling qualities evaluations.

A two-part study was conducted on NASA Ames Research Center's Vertical Motion Simulator (VMS) to evaluate the effects of simulator characteristics on handling qualities. The primary focus of the two piloted simulations was on piloted assessment of the variations - i.e., Cooper-Harper Handling Qualities Ratings (HQRs; Ref. 11) and comments. Evaluations were conducted with several sets of vehicle dynamics, using a simple transfer-function model of an uncoupled helicopter, with Level 1 handling qualities based on Aeronautical Design Standard ADS-33C (Ref. 10). Changes in the simulation environment were made by adding time delays in the visual path and in the overall simulated response, and by changing motion system washout filter dynamics. The pilots were instructed to evaluate each variation in the environment as if it were a new aircraft; therefore, it may be assumed that differences in HQRs were due entirely to the pilots' perceptions of handling qualities, rather than to changes in the aircraft model itself.

in the second simulation (Simval II). This paper reports on the overall results and conclusions from both simulations.

# FACILITY

# Hardware

The VMS is a six-degree-of-freedom simulator with a cab mounted on a Rotorcraft Simulator Motion Generator (RSMG) gimbal (Fig. 2). Translational motion is limited by hard stops at $\pm 30$ ft vertically, $\pm 20$ ft laterally, and $\pm 4$ ft longitudinally. Software trips in the motion system further limited the available range of linear travel from center position to $\pm 25$ ft vertically, $\pm 18$ ft laterally, and $\pm 2.5$ ft longitudinally. The cockpit was representative of a single-pilot helicopter configuration. In the first simulation three horizon-level monitors provided the out-the-window view; the rightmost window included a view of the ground environment near the helicopter as well. In this simulation visual display generation was via a Singer-Link Digital Image Generator (DIG I). In the second simulation, a four-window cab was used with three forward-looking windows and one downward-looking chin window. For this simulation a three-channel CT5A CGI system was used; since only three channels were available for four windows, the leftmost forward display was not used. In both simulations the cockpit head-down instruments were conventional, with the addition of a digital altimeter. No head-up displays were used. Cockpit controls were also conventional, with a center-mounted cyclic, left-hand collective, and pedals. The command signals were displacement for all controllers.

# Motion Description

The general structure of the VMS cockpit stick-to-motion response is shown in Figure 3. Control inputs made by the pilot result in aircraft model accelerations, rates, and positions. The motion washout software generates motion commands in the simulator axes reference frame from the aircraft model accelerations. In the motion washout software, first the aircraft accelerations are transformed into simulator axes. Then, each of the six simulator axes accelerations is sent through a washout filter. The washout filter is a linear, constant-coefficient, second-order high-pass filter of the following form:

$$
\frac {\text {s i m u l a t e d a c c e l e r a t i o n}}{\text {m o d e l a c c e l e r a t i o n}} = \frac {K _ {\mathrm {w o}} s ^ {2}}{[ s ^ {2} + 2 \zeta_ {\mathrm {w o}} \omega_ {\mathrm {w o}} s + \omega_ {\mathrm {w o}} ^ {2} ]}
$$

Different sets of motion washout filter gains, damping ratios, and break frequencies were devised and evaluated in

the two experiments. These washout filter sets were designed to transmit different forms of acceleration information to the pilots. Details of the washout filter sets are given in the Description of the Experiment section of this paper.

The washed-out commands are sent to the lead compensation software, where phase lead is added to the motion drive commands to compensate for some of the lags in the motion drive hardware. No modifications were made to the lead compensation software.

The motion drive has dynamics associated with the hardware in each axis. The response of the combination of lead compensation and motion hardware constitutes the motion response. If the effective delay of the motion response is large enough, then it will be noticeable to the pilot. The effective delays in each axis of the motion response (feedforward and motion drive hardware dynamics combined) are presented in the next section.

The roll-lateral washout configuration will be explained in more detail as an example of the interplay between the motion system axes. Without compensation, the rotational accelerations of the Vertical Motion Simulator induce a spurious linear acceleration since the rotational axis of the simulator is below the pilot's seat. This effect is compensated by subtracting the induced angular acceleration term from the linear motion command. The correction factor is washed out through the same filter as the rotation that generated the lateral acceleration; it is multiplied by the rotational washout filter and divided by the lateral washout filter before the command is sent to the lateral washout.

In a constant lateral acceleration maneuver, the aircraft linear accelerations are eventually washed-out by the high-pass filter. In this case, the cab is tilted to change the relative orientation of the gravity vector to the cab, simulating the sustained lateral accelerations that are not achievable with finite linear motion. Similar coordination is achieved between the pitch and surge axes.

# Time Delays

Delays in the Motion System. During the simulation, the dynamics of the motion response to motion command were quantified by measuring these responses to a cockpit controller input. The inputs, generated by a random number generator, were shaped with a Gaussian distribution over the frequency range of 0.1 to 30 rad/sec and added directly to the cockpit control signal of interest. The result of the Gaussian distribution was that the higher frequency inputs were of smaller magnitude, and no saturation occurred in

the motion hardware. The resulting motion command and motion response to these inputs were recorded, CIFER (Ref. 12) was used to generate frequency responses and the generalized transfer-function fitting program NAVFIT (Ref. 13) was used to identify an effective time delay of the combined feedforward and motion drive dynamics.

The effective delays in each axis of the motion response are presented in Table 1. Recall that the sway and roll axes were necessary to provide rotation about the aircraft center: although the motion washout software generates the correct commands for an aircraft rotation, the sway and roll motion responses were asynchronous (a time difference of 30 to 40 msec existed between the responses). It was found that this difference between the sway and roll axes in the lateral response was noticeable in many of the evaluated configurations.

Delays in the Visual System. The sources of time delay in the stick-to-visual response with the CT5A CGI (used in Simval II) are shown in Figure 4 and identified delays are listed in Table 2. It takes 10 msec for the cockpit stick position signal to get to the host computer, and the host computer updates the model states based upon the stick position and the aircraft rates. The computation time of the model acceleration is $\mathbf{T}_{\text{cycle}}$ , but the model positions and rates are forward integrated by one cycle so that they are concurrent with the accelerations of the next time frame (when they will be used in the calculation of the next frame's accelerations). The forward integrated positions and rates are sent to the Image Generator (IG); there is a 2 msec transport delay in this transmission. The IG takes 3 internal CGI cycles to display the visual scene, consisting of one cycle for the object manager, one cycle for the geometric processor and the polygon manager, and one cycle for the display processor. The IG then requires 1/2 cycle to prepare the data and 1/4 cycle to draw half of the model response to the stick on the screen. The IG computer cycles at 60 Hz (16.67 msec), resulting in an IG transport delay of 62.5 msec (3.75 cycles). The overall delay of stick-to-visual response is 74.5 msec - $\mathbf{T}_{\text{comp}}$ , with a standard deviation of 3 msec. The overall stick-to-visual response was varied by adjusting the visual lead compensation, $\mathbf{T}_{\text{comp}}$ (Ref. 16).

While Simval II used the Evans and Sutherland CT5A CGI as described above, Simval I used a Singer-Link Digital Image Generator (DIG I). There is a small difference in the update rates between these systems resulting in an IG transport delay for the DIG I of 83.3 msec compared to 62.5 msec for the CT5A. The visual variations for the experiments are outlined in the Description of the Experiment section of this paper.

# Interactions of Motion and Visual Delays

The dynamics of the tested configurations were characterized in terms of their pitch and roll attitude Bandwidth parameters (Ref. 10), i.e., Bandwidth frequency $\omega_{\mathrm{BW}}$ and phase delay $\pmb{\tau}_{\mathfrak{p}}$ . Each of the time-delay sources in the VMS facility outlined above can have a very large effect on the values of these parameters. For ground-based simulation, it is necessary to properly account for three separate response elements, the math model, the visual scene, and the motion system, since the pilot is, to some extent, aware of and operating in response to all of them. In the case of the VMS it is possible for the Bandwidths of these three responses to be quite different for the same configuration. An example of this is shown in Figures 5 and 6.

The frequency-response plot of Figure 5 illustrates the dramatic effects of cascading the individual elements of the simulation onto the ideal math model. The model (shown as solid lines in Figure 5) is the transfer function for an ideal rate-augmented helicopter model with roll damping $\mathbf{L}_{\mathfrak{p}} = -4$ rad/sec; $\mathfrak{p} / \delta$ represents the model response to measured control actuator position (i.e., after the A/D and D/D interfaces in Figure 4). As expected, in the absence of time delays this ideal system exhibits a Bandwidth frequency of $\omega_{\mathrm{BW}\phi} = -\mathbf{L}_{\mathfrak{p}} = 4$ rad/sec, and phase delay $\tau_{\mathfrak{p}\phi} = 0$ .

The response of the compensated visual display $(\mathfrak{p}_{\mathrm{v}} / \delta_{\mathrm{as}})$ in Figure 5 introduces the 10-msec control position measurement delay for the A/D and D/D (Fig. 4). This delay has no effect on magnitude and only a slight effect on phase angle. Bandwidth frequency is reduced from 4 rad/sec to 3.7 rad/sec, and phase delay increased from zero to 0.01 sec. Turning the visual compensation filter off also does not affect the magnitude curve, but there is further phase lag, with $\omega_{\mathrm{BW}_{\phi}} = 2.4$ rad/sec and $\tau_{\mathrm{p}_{\phi}} = 0.07$ sec.

The motion response of the VMS cab $(\mathfrak{p}_{\mathrm{m}} / \delta_{\mathrm{as}}$ in Figure 5) is quite different from the model and visual responses. The combination of washout filter and effective motion time delay contributes low-frequency phase lead and high-frequency phase lag. The low-frequency lead introduced by the motion washout serves to increase the Bandwidth frequency to $\omega_{\mathrm{BW}} = 3.9$ rad/sec, but the motion-system lags increase phase delay to $\tau_{\mathbf{p}\phi} = 0.05$ sec.

Figure 5 serves to illustrate several important points. First, it shows the beneficial effect of the visual compensation filter, since the phase curve of the compensated response is closer to ideal to higher frequencies. Second, the phase distortions and gain reductions introduced by the washout are evident, as the responses of the ideal

math model and cab roll motion are in phase for effectively only a single frequency. Third, Figure 5 shows that in terms of visual-motion synchronization, the uncompensated visual response actually corresponds most closely to the motion response, especially at high frequencies.

The significance of the Bandwidth differences of Figure 5 is illustrated by Figure 6. This figure shows the eight possible measurements of the Bandwidth parameters to describe the responses of Figure 5. The parameters for the ideal model are the most straightforward, especially for position-referenced values of measured roll rate to measured control actuator deflection $(\mathfrak{p} / \delta)$ . The visual-display Bandwidth, with compensation on, is referenced back to cockpit control position inputs, $\phi_{\mathrm{v}} / \delta_{\mathrm{as}}$ , and hence reflects 10 msec of time delay; with compensation removed the Bandwidth decreases and phase delay increases. The phase delays for motion are about equal to those for the uncompensated visual display, but with increased Bandwidths due to the washouts. Addition of stick force feel dynamics, typical of those used in the two simulations, greatly increases $\tau_{\mathbf{p}_{\phi}}$ and decreases $\omega_{\mathrm{BW}_{\phi}}$ when these values are referenced to force.

# DESCRIPTION OF THE EXPERIMENT

Effects of variations in the three major elements of the simulation — the motion and visual systems and math model — were evaluated. Specific variations and the philosophies behind them were as follows.

# Motion System

Even though the VMS provides a large range of linear and angular travels, there are still very tight limitations on maneuvering space that necessitate lowered response gains and high washout break frequencies (Ref. 9). The selection of such gains and washouts is a compromise between the desire for realism in motion and the realities of space limitations. Potential criteria for determining washout limits (both gain and break frequency) for linear washouts have been developed (Refs. 14 and 15). These limits generally indicate that for minimum loss of motion fidelity, washout filter break frequencies should be no greater than about 0.3 rad/sec (for a second-order filter with damping ratio of 0.7). Ideally, the values selected reflect the requirements of the particular maneuvers to be flown and the expectations of the pilot.

As Figure 5 indicates, the combined effects of motion washouts and delays results in only a narrow range of frequencies for which the phase angle of the motion response accurately reflects the model response. In addition,

the reduced gain in the motion system results in an attenuation in the motion response at all frequencies. This difference between the ideal system and the achieved motion is complex and is a function of frequency. Nonetheless, it is useful to find a simpler metric for judging the fidelity of the motion response. In terms of phase differences, it has been suggested (e.g., Refs. 14 and 17) that a phase distortion of less than about 30 deg corresponds to high motion fidelity. Therefore, in this paper we will consider two parameters to define the model-to-motion differences as shown in Figure 5: 1) the washout gain, or reduction in motion response as compared to full-scale motion; and 2) the frequency range for which the phase distortion (difference in phase angles between model and motion) is 30 deg or less. While these parameters are not as explicit as complete transfer-function plots, they will greatly facilitate the comparison of the different motion washout values evaluated in these simulations.

# Baseline Washout Dynamics

The Baseline set of motion washouts used in this experiment was developed for the Simval I simulation by NASA engineers. This Baseline set followed the NASA philosophy of transmitting initial accelerations at the expense of motion/visual/model phasing (Ref. 9). Scaling of the initial response was on the order of $30\%$ to $60\%$ of full scale, with washout break frequencies of 0.2 to 0.7 rad/sec.

The frequency range where the phase distortion of the motion washout filter is less than 30 degrees is plotted versus washout filter gain for the Baseline washouts in Figure 7. The plots were produced by concatenating the identified motion system dynamics with the washout filters. The high-frequency end of this low-phase-distortion range is almost entirely a function of motion dynamics and delays and cannot be increased. At the low-frequency end, the low-distortion range can be improved by reducing washout break frequency. The gain of the washout filter must also be reduced, however; otherwise, saturation of the motion drive occurs in position, rate, or acceleration.

The Baseline motion system represents a typical design for helicopter low-speed handling qualities studies on the VMS. The washout filters were selected conservatively, so that the motion system did not saturate during any of the Simval I tasks. The motion washout filters can be designed independently for each task of a simulation, to take full advantage of the capabilities of the motion system; the gain and phase distortion would be dependent on the task aggressiveness in each of the motion system axes and on the simulator capabilities. This is not always done, however, as

it is a difficult and sometimes time consuming process to perform. The more that is understood about the effects of the motion washout filters on pilot performance and pilot opinion, the better they can be adjusted for handling qualities evaluations.

Modified Washout Dynamics (Simval I). An alternate set of Modified washouts was developed during the Simval I simulation. This set was designed with the specific goal of reducing the phase distortions in motion around the frequencies of pilot closed-loop control (and maximum acceleration sensitivity), 0.5-5 rad/sec. Since this requires a washout break frequency below that of the Baseline washouts, the decreased phase distortion comes at the expense of further attenuated amplitude of motion. The phase-distortion ranges for the Modified washouts are compared with the Baseline set in Figure 7. These washouts emphasized the large-amplitude axes of response of the VMS — pitch, roll, and heave.

Systematic Variations in Washout Dynamics (Simval II). In the second experiment, only two tasks were evaluated, a precision hover and a sidestep, so that the development of the motion washout filters could be studied in greater detail. The precision hover allows for a substantial increase in gains (including one-to-one), due to the relatively small aircraft positions and attitudes generated during the task. Schroeder et al. performed a VMS simulation that successfully utilized gains of one in all six motion system axes (Ref. 18). The Simval II hover task actually consisted of a 6-8 knot translation to hover and a precision hover, and consequently the gains had to be reduced below one-to-one.

The sidestep task is an aggressive task that primarily emphasizes the roll and sway axes, secondarily emphasizing the heave axis. The design of the motion washout filters for the sidestep task addressed the interplay between roll, sway, and heave axes of the simulator; the yaw, surge, and pitch washout filters were not varied among the sidestep configurations.

Three motion washout configurations were designed for the sidestep to investigate the gain attenuation versus phase distortion trade-off. Phase-distortion plots are shown in Figure 8. The washout break frequency for the roll, sway, and heave axes was systematically varied and the gains adjusted so that the pilots did not run into any motion limits while flying the task. The yaw, surge, and pitch washout filters were similar to the Baseline washouts. The roll and sway washouts cannot be designed independently because of the interdependence of the rotational and linear axes of the VMS, mentioned previously. It can be seen in Figure 8 that

while variation was made in the roll gain, sway gain remained 0.3 or less for all three Sidestep washout configurations.

# Visual System Delays

While the visual compensation filter (Ref. 3) used on simulations on the VMS effectively removes the overall visual delays, it increases the mismatch in phasing between the visual and motion responses: the motion system experiences unavoidable delays due to anti-aliasing filters, mass, inertia, and control limiting effects that cannot be removed entirely. Past studies of time delays in either the visual or motion path, resulting in a visual/motion mismatch, show mixed results. For example, a simulation on the NASA Ames Six-Degree-of-Freedom (S.01) simulator (Ref. 19) suggests that based upon measures of pilot performance, 1) it is better to have the motion response lag visual rather than to intentionally lag the visual just to reduce mismatch, and 2) in terms of pilot high-frequency lead generation, motion compensation is more important than visual compensation. A study of a vertical pursuit tracking task on the NASA Langley Visual/Motion Simulator (Ref. 20) investigated visual/motion mismatch by introducing delays in the visual system. Pilot performance measures of total tracking error and control activity were taken. Slight improvements in performance were found for the case where total visual delay most closely matched the effective delays of the motion system (approximately 97 ms).

Effects of removing the visual delay compensation were evaluated in both simulations. The total visual time delays for both Simval I and II are listed in Table 3.

# MATH MODEL

The mathematical model for the rotorcraft was a generic, uncoupled stability-derivative model that has been used for several simulations at Ames (Ref. 21). Changes in dynamic response characteristics are effected by altering the basic aircraft stability and control derivatives; for example, the transfer function for pitch attitude response to longitudinal cyclic for the rate-augmented aircraft was represented by

$$
\frac {\theta}{\delta_ {\Theta}} = \frac {M _ {\delta_ {\Theta}}}{s ^ {2} - M _ {q} s}
$$

# TASKS

# Simval I

Seven tasks were evaluated in the preliminary simulation. These tasks consisted of precision and aggressive maneuvers at hover and in low-speed flight as defined by Section 4 of ADS-33C (Ref. 10). The precision tasks were a one-minute hover, vertical translation (a surrogate for landing), and pirouette. The aggressive tasks were a bob-up/bob-down, dash/quickstop, and sidestep. A 40-kt lateral slalom task, which has no counterpart in ADS-33C, was included to emphasize a combination of precision and aggressiveness. Desired and adequate performance limits were defined for each task, based as much as possible on ADS-33C limits but adapted when necessary to the specific visual environment of the DIG. Details of the tasks are given in Refs. 22 and 23.

# Simval II

The second simulation focused on two tasks, a precision hover and a sidestep. The visual scenes for these tasks were tailored to adhere to recently revised task definitions, and performance limits were consistent with those for the revised tasks.

Because of the emphasis on these two tasks for the systematic study of motion and visual variations, an analysis of the pilots' control activity was performed to verify that the tasks were sufficiently demanding (i.e., exhibited sufficient task bandwidth) to elicit the desired effects in pilot performance and opinion. Figure 9 shows frequency-response plots of an example power-spectral density (PSD) for lateral cyclic activity. These plots show that 70 percent of all input power (corresponding to the pilot's "cut-off frequency," Ref. 24) occurs at 2.4 rad/sec for the hover (Fig. 9a) and 1.1 rad/sec for the sidestep (Fig. 9b). As expected, these frequencies confirm that the hover is a higher-bandwidth task than the sidestep. They also suggest that the pilots will be more sensitive to visual delay variations in the hover (where visual delay introduces high-frequency phase rolloff), and more sensitive to motion delay variations in the sidestep (where the cut-off frequency is very near the low edge of phase distortion as introduced by the washouts, Fig. 8).

# PILOTS

Seven pilots, with varying backgrounds and levels of experience, participated in the first simulation. Two pilots had relatively little previous experience in ground-based simulation, and none in the VMS. In Simval II four pilots

participated, including two with over 300 hours in the VMS. The other two pilots in Simval II had no previous VMS exposure. Two of the experienced pilots flew in both simulations.

# RESULTS

# Effects of Task

Motion and task effects were evaluated in Simval I. The seven tasks were evaluated fixed-base and with the Baseline and Modified motion washouts. Figure 10 is a summary plot of the HQRs for the tasks. Average HQRs are depicted by solid symbols that are connected by a solid line for clarity. Each data symbol represents a single rating. There is evidence in Figure 10 of rating differences across the tasks. Generally, the easiest tasks (in terms of best average HQR) were the hover, bobup/bobdown, and dash/quickstop. Since no turbulence, gusts, or winds were simulated, the one-minute precision hover was low-workload as long as the helicopter was reasonably well stabilized before starting the formal maneuver. Pilot comments indicated that the bobup/bobdown was relatively easy because of the decoupled helicopter model, making this almost entirely a single-axis task, while the dash/quickstop was rated well because of the ample forward field-of-view for initiating the maneuver. By contrast, the vertical translation, pirouette, and slalom maneuvers were inherently multi-axis and thus tended to receive higher HQRs, while pilot comments indicate that the poor ratings for the sidestep maneuver are due primarily to the lack of a sideward field-of-view for adequately determining the endpoints of the maneuver.

# Effects of Motion Washout Filters

The effects of motion washout filters were investigated in both of the experiments. Simval I was an exploratory study that looked at a variety of tasks for only two motion washout configurations (Fig. 10). Simval II concentrated on understanding washout filter design for two tasks; results for the sidestep task are discussed below.

Simval I. Figure 10 illustrates the importance of motion on pilot opinion: all tasks were Level 2 fixed-base, and average HQRs improved by $\frac{1}{2}$ to 2 rating points when motion was introduced. Comparison of the HQRs for the Baseline and Modified washouts in Figure 10 shows a general trend for slightly improved ratings with the Modified set. There are exceptions, however, as the average ratings for the bobup/bobdown and sidestep tasks are slightly worse. The slight improvements for the other tasks suggest that the pilots were either aware of the more consistent motions

provided by the Modified set, or, conversely, that the rapid washouts of the Baseline set mitigated the beneficial effect of the increased initial accelerations provided by the higher gains. It is likely that the answer is a blend of the two, supported by the degraded ratings for the bobup/bobdown (where initial accelerations are an important cue to the pilot) and the sidestep (where the Modified motion washouts overdrove the vertical axis in response to lateral commands).

By their nature, aggressive tasks involve rapid changes of state - i.e., large initial accelerations - compared to the precision tasks. Since the Baseline motion gains transmitted more of the initial acceleration onset cues, it might be expected that this set would be preferred for the aggressive tasks, and this is the case for the bobup/bobdown and sidestep (Figs. 10e and 10g). By contrast, the Modified motion set was designed to provide more accurate phasing of the motion and visual responses, at the cost of reduced gain. Therefore, it is reasonable to expect this system to be preferred for those tasks that involve continuous closed-loop operations, such as the precision tasks, and this is the case as well (Figs. 10a, 10b, and 10c).

Several important factors must be considered in comparing the HQRs for the two motion gain/washout sets: first, the Modified set as developed for Simval I was intended to be exploratory in nature, and it did not take advantage of all axes (see Fig. 7); and second, since the basic aircraft was good to begin with, small changes in average HQR may or may not be significant. Simval I indicated that further testing was required, in a more systematic fashion, as was conducted on Simval II.

Simval II. The pilot ratings for the Sidestep task with the medium bandwidth helicopter dynamics are shown versus the motion washout configuration in Figure 11. As was found in Simval I, there is a substantial improvement in the pilot ratings for all the motion configurations over the fixed-base case (1/2 to 1-1/2 rating points). Of the three configurations developed for the sidestep task, the lowest phase distortion (and lowest gain) configuration, SS1, was preferred by all the pilots, as indicated by the pilot ratings in Figure 11 and the pilot comments outlined below.

Pilot A thought that both the Baseline and the low-phase-distortion, low-gain combination (SS1) were good configurations $(\mathrm{HQR} = 3)$ . He perceived stronger motion cues in the medium phase distortion case (SS2), "Motion seemed a little strong ... you got bounced around pretty good... [I] could feel the difference between this and the previous configuration (SS1) just by the high level of motion... and that lowered the rating" $(\mathrm{HQR} = 4.5)$ . The highest gain washouts brought the impression that the

simulator was always moving around, and "[the motion response] felt like it was not in sync with the control movements or visual movements" (HQR = 4).

Pilot B was the most sensitive of the pilots to the strong movements of the simulator, preferring the low phase distortion (SS1) configuration over all the others. For example, with SS2, the medium gain configuration, "Every time I made any kind of aggressive rollout, then I was feeling a negative motion cue during the roll out to the hover" $(\mathrm{HQR} = 5)$ . But for SS1, "I was getting good positive cues, but the negative cues that I felt before weren't present... In most of these cases where you do have a problem, you excite the problem by being more aggressive... [this] system lets me be more aggressive and then attain a tighter performance... this is good" $(\mathrm{HQR} = 3)$ . It is possible that the pilots were feeling the effect of the mis-coordination between the roll and sway responses, in which the sway motion response to a lateral stick input was delayed by 30-40 msec behind the roll response (Table 1). The roll-axis bandwidth in this case was 4.3 rad/sec, and the effect of the asynchronous responses would have been magnified as the gain of the motion system was increased. These results suggest that the higher gain, higher phase distortion cases are not as robust to changes in pilot technique.

Pilot C's comments indicate that out of the three sidestep washout configurations, SS1 was the best because it was less jerky, easier to control, and required slightly less workload than the others. SS1 was also the only configuration where he noted that the motion system felt like it was in synchronization with what he was seeing and doing.

The low-phase-distortion, low-gain configuration SS1 offered two advantages over the others. The first advantage was that the phase distortion between the visual and motion responses was minimized for the roll, sway, and heave axes, as described earlier (Fig. 8). This was apparent in the pilot comments where they noted that the responses were more in synch and the helicopter was easier to control. The second advantage of the low-phase-distortion, low-gain configuration was that any motion miscues, such as those mentioned above, were diminished by lowering the gains. The pilots were very attuned to these motion miscues, as indicated in their comments.

For this study, the 30 degree phase distortion has been used as a reference by which the motion configurations were compared. The lower end of the low-distortion frequency range of the SS2 configuration is well above 1 rad/sec in all axes, while the SS1 configuration range spans down to almost 0.7 rad/sec (Fig. 8). The PSD of the Sidestep in Figure 9b indicates that the pilot cut-off frequency (the

frequency below which 70 percent of control power is contained) was 1.1 rad/sec. So 70 percent of the control power is below the lower bound of the 30-deg phase-distortion frequency range for SS2, while more control power is contained above the lower bound of the SS1 configuration. It is therefore suggested that pilots preferred the SS1 washout configuration because they perceived lower phase distortion in the frequency range in which they were operating, i.e., below 1.1 rad/sec, even though it had lower motion gains.

# Effects of Visual Delays

The baseline visual transport delay of the Vertical Motion Simulator is 63 - 83 msec, depending on the Computer Image Generator, as seen in Table 2. The effect of adding lead to the visual command to compensate for visual delay was investigated in both studies. When comparing the results from the two studies, the baseline visual delay case refers to the uncompensated visual delay for both studies, while the compensated visual case refers to the added visual lead compensation.

Sensitivity to Visual Delays. Before reviewing the pilot ratings for the visual-delay evaluations on the moving-base simulation, it is important to establish that the pilots were sensitive to the relatively small change in visual delay resulting from the addition of the lead compensation. To answer this question, we look at the results of fixed-base evaluations, where the pilots' only cue is visual. Five pilots flew back-to-back evaluations of the compensation on and off for the hover task, fixed base during the two simulations. The HQRs, shown in Figure 12, indicate that there was a preference for the compensated visual case, as expected.

Effects of visual delays were further investigated by calculating the improvement in phase margin at the pilot cutoff frequency (Fig. 9b) for the compensated visual case. For the Simval II high-bandwidth helicopter response, the phase margin at 2.4 rad/sec was increased from 67 to 75 degrees when the visual delay was compensated. This eight-degree increase in the phase margin alone is not enough to explain the improvement in ratings from Level 2 to Level 1. The bandwidth of the stick-to-visual response was greatly improved with the compensated case, from 4.8 rad/sec to 8.9 rad/sec in roll, and from 2.8 rad/sec to 4.0 rad/sec in pitch. So it is assumed that the reduction in pure time delay in the open-loop aircraft response was the major factor in the improved ratings.

Simval I. For this simulation, the baseline visual delay was 83.3 msec (Table 2), and the compensated

visual delay was effectively zero; the model and motion responses remain unchanged. These evaluations were made with the Baseline motion washout filters (Fig. 7).

The pilot ratings for two precision tasks from the Simval I simulation, chosen because the same pilots flew both visual delay configurations and because the tasks are similar to the Simval II hover, are shown in Figures 13a and 13b. The results indicate that Pilots Mc and M preferred the visual-delay case over the no-delay case, while the third pilot (Pilot S) was just the opposite.

Comments by pilot S for the baseline visual delay case deal almost exclusively with motion problems, rather than visual. It is not clear whether the adverse comments about motion for these evaluations reflect the change in the motion/visual relationship, or simply Pilot S's dissatisfaction with the motion response.

Pilots M and Mc had relatively little previous exposure to ground based simulation. These pilots generally preferred the baseline visual delay case over the compensated case because of the reduction in the crispness of the response. For pilot M, "The [baseline visual configuration] was the least as far as the crispness goes... This last one is more in tune... It was easier to control." Pilot Mc commented that "[The baseline visual case]..., overall, felt more like flying than any of the others... The motion and visual cues seemed to be the most consistent between my inputs and the aircraft response."

Simval II. For this simulation, the baseline visual delay was 62.5 msec, and the compensated visual delay was effectively zero; the motion dynamics were held constant for the visual delay evaluations, but they were slightly different than the Simval I motion dynamics. These dynamics were used because the Simval II pilots felt that this set of washouts was slightly better than the baseline dynamics. However, the one pilot who flew both simulations gave almost identical ratings for these precision tasks, so the motion system difference does not appear to have affected results.

Pilot ratings for the hover task evaluations of the baseline and compensated visual are shown in Figures 13c and 13d. Two helicopter response configurations are represented here. The pilots rated the high-bandwidth helicopter better than the medium-bandwidth helicopter, but the trends are the same for both sets of dynamics. Pilots B and A, experienced VMS pilots, preferred the compensated visual in both cases, and the novice VMS pilot (Pilot C) preferred the baseline visual.

Pilot B, a veteran VMS pilot who flew both simulations (Pilot S in Simval I), noticed the motion system more with the baseline visual: "The visual system seems to be still correlating with the inputs, however, the motion seems to be giving me some uncorrelated response... causing me to make inputs to correct something that I don't think was wrong." It appears that Pilot B was compelled to pay more attention to the motion response with the baseline visual: "Maintaining the precision took all of my capacity... [the response] was slow when I gave my first input to move over to the hover position." With the compensated visual, however, "I didn't detect any time delay in the visual displays or the motion...the cues seemed very succinct and very in tune with the inputs... I could be as aggressive as I felt necessary... actually it did have spare capacity in this case...even though I was pretty active on the control.... The initial inputs to arrest the translation seem just a hair abrupt... It is a very sharp response, but very predictable."

Pilot B's ratings and comments are backed up by his performance, shown for the hover task with the medium bandwidth helicopter model in Figure 14a. The lateral and longitudinal errors are appreciably reduced with the compensated visual configuration.

Pilot C, the novice VMS pilot, agreed with the novice pilots in Simval I (Pilots M and Mc), but directly contradicted the other two pilots from Simval II. For the baseline case, "The motion I was picking up and the visual scene seemed to be in sync... minimal pilot compensation" $(\text{HQR} = 3)$ , whereas for the compensated case, "Motion/display cues were worse than the [baseline case]... the visual and motion felt out of phase.... [I] was working a lot harder to control height, and there was a lot of cyclic activity.... [Compared to the baseline, this system was] less sensitive. I thought you changed the control system, it seemed like lower bandwidth" $(\text{HQR} = 4)$ .

An example of Pilot C's performance for the hover task with the medium bandwidth helicopter model is shown in Figure 14b. Here we can see that, in contrast to Pilot B's performance, Pilot C's longitudinal and lateral errors were reduced in the baseline visual case.

General Conclusions on Visual Delay Effects. While the pilots do not agree on the visual configurations, the results are consistent between the two simulations. A summary of the HQRs from the two simulations is presented in Figure 15.

Based on the HQRs, the experienced VMS pilots prefer the visual compensated. It was seen that these pilots actually get better performance with this configuration,

because they use primarily the visual cues for the task. Even Pilot B mentioned, however, that the response for the compensated visual was abrupt; it was this same abruptness that made some of the other pilots dislike the compensated case. It seems that the pilots with experience on the VMS have the ability to filter out the adverse motion responses.

The novice pilots prefer the baseline visual, where the motion and visual responses were most closely matched (Fig. 15). There is some rationale for this, since the high-frequency response of the visual scene with the baseline visual exhibits approximately 63-83 msec of total delay (depending on the CIG), and the VMS cab motion in pitch and roll exhibits 70-90 msec of effective delay due to high-frequency lags. Thus the baseline visual and motion responses are nearly in phase, whereas the implementation of the visual filter actually increases the discordance between visual and motion responses (Fig. 5).

It appears that the most practical solution is to match the motion and visual responses as closely as possible in the frequency range that is being exercised, even though some pilots may be able to achieve better performance with the visual response leading the motion response. With the visual and motion responses in phase, the simulation represents a more realistic helicopter response.

# CONCLUSIONS

This two-phase study of the interactions of simulator motion, visual, and response dynamics on rotorcraft handling qualities has both confirmed previous observations and revealed areas deserving of more indepth study. Unlike most previous motion/visual simulation studies, the primary goal of this study was the measurement of these interactions on perceived handling qualities, rather than on objective performance measures.

Motion was necessary to obtain satisfactory handling qualities: none of the tasks received Level 1 average HQRs fixed-base. Improvements in HQRs when motion was added were generally $1/2$ to 2 rating points.

Based on average HQRs, motion washouts with low break frequency and low response gain are slightly better than correspondingly high-gain, but high-break-frequency, washouts for the low-speed tasks evaluated. This may be a function of task aggressiveness.

The data suggests that the best handling qualities occur with the lowest motion/model phase distortion, even though this occurs at the cost of a reduction in the motion gain. The results of the motion washout configurations may have

been mitigated by anomalies encountered in the motion system.

Pilots with little or no experience in the VMS or other ground-based simulators expect the visual and motion responses to be synchronized, and they are sensitive to changes in the phasing between the motion and visual responses. As a result, they prefer the situation where the visual response, although delayed, best matches the motion response. On the other hand, experienced VMS pilots were able to improve their performance with the visual delays compensated, apparently because they were able to filter out the mismatched motion responses and use the visual response as their primary cue.

The best solution to problems with visual/motion/model mismatches would be to improve the delays in the motion response, but this has proven to be difficult due to hardware limitations. The most practical solution may be to match the motion and visual responses as closely as possible in the frequency range that is being exercised, even though some pilots may be able to achieve better performance with the visual response leading the motion response. With the visual and motion responses in phase, the simulation represents a more realistic helicopter response.

# ACKNOWLEDGEMENTS

The authors wish to thank the pilots, Messrs. Monroe Dearing, Rickey Simmons, and George Tucker of NASA, Freddie Mills, Gerald McVaney, and Tom Reynolds of the U.S. Army, Ron Gerdes of SYRE, Kevin Emerson of the RAF (on assignment with the U.S. Army), and Roger Hoh of Hoh Aeronautics for their efforts in this simulation. Appreciation is also extended to the SYRE simulation personnel and NASA engineers, especially Messrs. Richard E. McFarland and Richard Bray.

# REFERENCES

1. Mitchell, D. G., Hoh, R. H., and Morgan, J. M., "Flight Investigation of Helicopter Low-Speed Response Requirements," J. Guidance, Control, and Dynamics, Vol. 12, No. 5, Sept.-Oct. 1989, pp. 623-630.   
2. Ferguson, S. W., Clement, W. F., Cleveland, W. B., and Key, D. L., "Assessment of Simulation Fidelity Using Measurements of Piloting Technique in Flight," AHS Paper No. A-84-40-08-4000, May 1984.

3. McFarland, R. E., Transport Delay Compensation for Computer-Generated Imagery Systems, NASA TM 100084, Jan. 1988.   
4. Jewell, W. F., Clement, W. F., and Hogue, J. R., "Frequency Response Identification of a Computer-Generated Image Visual Simulator With and Without a Delay Compensation Scheme," AIAA Flight Simulation Technologies Conference, Monterey, CA, Aug. 1987, pp. 71-76.   
5. McCauley, M. E., ed., Research Issues in Simulator Sickness: Proceedings of a Workshop, National Academy Press, Washington, DC, 1984.   
6. Stapleford, R. L., Peters, R. A., and Alex, F. R., Experiments and a Model for Pilot Dynamics With Visual and Motion Inputs, NASA CR-1325, May 1969.   
7. Jex, H. R., Magdaleno, R. E., and Junker, A. M., "Roll Tracking Effects of G-Vector Tilt and Various Types of Motion Washout," Fourteenth Annual Conference on Manual Control, NASA CP-2060, Nov. 1978, pp. 463-502.   
8. Jex, H. R., Jewell, W. F., Magdaleno, R. E., and Junker, A. M., "Effects of Various Lateral-Beam-Motion Washouts on Pilot Tracking and Opinion in the 'LAMAR' Simulator," 15th Annual Conference on Manual Control, AFFDL-TR-79-3134, Nov. 1979, pp. 244-266.   
9. Bray, R. S., Visual and Motion Cueing in Helicopter Simulation, NASA TM 86818, Sept. 1985.   
10. Handling Qualities Requirements for Military Rotorcraft, U.S. Army AVSCOM Aeronautical Design Standard, ADS-33C, Aug. 1989.   
11. Cooper, G. E., and Harper, R. P., Jr., The Use of Pilot Ratings in the Evaluation of Aircraft Handling Qualities, NASA TN D-5153, Apr. 1969.   
12. Tischler, M. B., and Cauffman, M. G., "Frequency Response Method for Rotorcraft System Identification: Flight Applications to the BO-105 Coupled Rotor/Fuselage Dynamics," J. American Helicopter Society, Vol. 37, No. 3, pp. 3-17, July 1992.

13. Hodgkinson, J., LaManna, W. J., and Heyde, J. L., "Handling Qualities of Aircraft With Stability and Control Augmentation Systems — A Fundamental Approach," Aeron. Journal, Vol. 80, No. 782, Feb. 1976, pp. 75-81.   
14. Sinacori, J. B., The Determination of Some Requirements for a Helicopter Flight Research Simulation Facility, NASA CR 152066, Sept. 1977.   
15. Jex, H. R., Magdaleno, R. E., and Jewell, W. F., Effects on Target Tracking of Motion Simulator Drive-Logic Filters, AFAMRL-TR-80-134, Oct. 1981.   
16. McFarland, R. E., and Bunnell, J. W., "Analyzing Time Delays in a Flight Simulation Environment," AIAA-90-3174, presented at the AIAA Flight Simulation Technologies Conference, Dayton, OH, Sept. 1990.   
17. Sinacori, J. B., Stapleford, R. L., Jewell, W. F., and Lehman, J. M., Researcher's Guide to the NASA Ames Flight Simulator for Advanced Aircraft, NASA CR-2875, Aug. 1977.   
18. Schroeder, J. A., Watson, D. C., Tischler, M. B., and Eshow, M. M., "Identification and Simulation Evaluation of an AH-64 Helicopter Hover Math Model," AIAA-91-2877, presented at the AIAA Atmospheric Flight Mechanics Conference, New Orleans, LA, Aug. 1991.

19. Shirachi, D. K., and Shirley, R. S., The Effect of a Visual/Motion Display Mismatch in a Single Axis Compensatory Tracking Task, NASA CR2921, Oct. 1977.   
20. Miller, G. K., Jr., and Riley, D. R., The Effect of Visual-Motion Time Delays on Pilot Performance in a Simulated Pursuit Tracking Task, NASA TN D-8364, Mar. 1977.   
21. Blanken, C. L., Hart, D. C., and Hoh, R. H., "Helicopter Control Response Types for Hover and Low-Speed Near-Earth Tasks in Degraded Visual Conditions," American Helicopter 47th Annual Forum Proceedings, May 1991, pp. 169-193.   
22. Mitchell, D. G., Hoh, R. H., Atencio, A., Jr., and Key, D. L., Ground-Based Simulation Evaluation of the Effects of Time Delays and Motion on Rotorcraft Handling Qualities, US Army AVSCOM TR-91-A-010, Jan. 1992.   
23. Mitchell, D. G., Hoh, R. H., Atencio, A., Jr., and Key, D. L., "The Use of Ground Based Simulation for Handling Qualities Research: A New Assessment," Piloted Simulation Effectiveness, AGARD-CP-513, Feb. 1992, pp. 23-1 - 23-14.   
24. Pausder, H.-J., and Blanken, C. L., "Investigation of the Effects of Bandwidth and Time Delay on Helicopter Roll-Axis Handling Qualities," Paper No. 80, presented at the 18th Annual European Rotorcraft Forum, Avignon, France, Sept. 1992.

图片摘要：该图主要展示 1. Comparison of HQR Ranges from Simulation and Flight for L。
![](images/cce1a50ab68a9ff6a86ae82274397ebd0bef92ae9efb4f8ea9b537ef8b3bc2d4.jpg)  
a) ACAH Response-Type

图片摘要：该图主要展示 1. Comparison of HQR Ranges from Simulation and Flight for L。
![](images/34ffcc0673def13594fa1d61db8c15ca3dd860c2d01131aed14fa05a0bdc4472.jpg)  
b) RCAH Response-Type   
Figure 1. Comparison of HQR Ranges from Simulation and Flight for Landing (Ref. 1)

图片摘要：该图主要展示 1. Comparison of HQR Ranges from Simulation and Flight for L。
![](images/58ebebbcd4c20c9d382de4448eebd582d89967eb2bc5a732940f121767f602d6.jpg)  
Figure 2. Vertical Motion Simulator

图片摘要：该图主要展示 2. Vertical Motion Simulator。
![](images/3e825df002c207ac86095305a84c3e40b9938b72f1dd2a53cab371f2b753ac55.jpg)

图片摘要：该图主要展示 2. Vertical Motion Simulator。
![](images/ebdac22836a6345171beba63eefa02f1d129df0e65ccb781f34cfc9e5b861f82.jpg)  
Figure 3. General Structure for the VMS Motion Response   
Figure 4. Stick-to-Visual Path Timing Diagram

图片摘要：该图主要展示 4. Stick to Visual Path Timing Diagram。
![](images/d1fdaeedb7ea200178ff9dd2414c9cb27fc0dd988fdf7af129f19349b5394d2e.jpg)

图片摘要：该图主要展示 4. Stick to Visual Path Timing Diagram。
![](images/e2354af3f5bda134815a1e1a3a455ecb4e7ff87173ff994747465f3f26749690.jpg)  
Figure 5. Frequency-Response Comparisons of Roll Rate to Control Input (Inputs are Measured Control Position, $\delta$ , and Cockpit Control Actuator Position, $\delta_{\mathrm{as}}$ ; Outputs are Roll Rate for Model, p, Visual Display, $p_v$ , and Motion, $p_m$ )

图片摘要：该图主要展示 5. Frequency Response Comparisons of Roll Rate to Control In。
![](images/9c0a4eca824019265ceeba5d80ea60314afe3891636e54cadd8065c1ccc89991.jpg)  
Figure 6. Migration of Bandwidth Parameters as Stick Force/Deflection, Visual, and Motion Effects are Introduced

图片摘要：该图主要展示 6. Migration of Bandwidth Parameters as Stick Force/Deflecti。
![](images/f1389fd9ff9e8b5fe3a0c7332b8289f765310f1309d1993d584b6db0a3cd4486.jpg)  
Figure 7. Frequency Range for Less than $30^{\circ}$ Motion-to-Model Phase Distortion for Baseline and Modified Washout Configuration

图片摘要：该图主要展示 7. Frequency Range for Less than Motion to Model Phase Disto。
![](images/49633454479f92ae04bcadd0f8738e19f190024fd03f32562edb236e22cb1cf5.jpg)

图片摘要：该图主要展示 7. Frequency Range for Less than Motion to Model Phase Disto。
![](images/c6f81d2f1140d3122d838eb15516ad0988034ac8b117175836007ab53a4d2a97.jpg)  
Figure 8. Frequency Range for Less than $30^{\circ}$ Motion-to-Model Phase Distortion for Sidestep Washout Configurations   
Figure 9. Lateral Stick Frequency Content (Pilot A)

图片摘要：该图主要展示 9. Lateral Stick Frequency Content (Pilot A)。
![](images/feecc15961ef44ccbd5165a3e2af5471749bd9ff567ebbce9c0eb0dc27f68949.jpg)  
a) Hover

图片摘要：该图主要展示 9. Lateral Stick Frequency Content (Pilot A)。
![](images/c91253f3ac160d255a4b74e73fe16f973f1e5fe7d94c7a0be3422791b118001b.jpg)  
b) Vertical Translation

图片摘要：该图主要展示 9. Lateral Stick Frequency Content (Pilot A)。
![](images/ea0a09f0a69905034c72d7e93b2506f7276539d91443434518dd0d9d426061e4.jpg)  
c) Pirouette

图片摘要：该图片与d) Sialom；e) Bobup这部分内容相关。
![](images/4e8a1633900661eda91719f2d2d872d88d473d5c4de994179c6f7a7b7e54107e.jpg)  
d) Sialom

图片摘要：该图片与e) Bobup；1) Dash/Quickstop这部分内容相关。
![](images/98fad4f4b75ebf5fabfb0ff23ada2c0acaaa874b5931935b90d3eb96b3aede87.jpg)  
e) Bobup

图片摘要：该图主要展示 10. Effects of Task and Motion on HQRs from Simval I (Baseli。
![](images/7d9f1c3d25f26ddcc8f3537b925921a327c5f1b98f0f2521c632b33a3a793a7f.jpg)  
1) Dash/Quickstop

图片摘要：该图主要展示 10. Effects of Task and Motion on HQRs from Simval I (Baseli。
![](images/eb813b9f666f06077d8283ef94d7c88f615fe328ca3b231e1df0898982bd8ca4.jpg)  
g) Sidestep

图片摘要：该图主要展示 10. Effects of Task and Motion on HQRs from Simval I (Baseli。
![](images/eda0325aad26284a34f231a253ba84d0a1b7bbd86fa085e59402de8f832a599d.jpg)  
Figure 10. Effects of Task and Motion on HQRs from Simval I (Baseline Motion, Visual Compensation On)

图片摘要：该图主要展示 10. Effects of Task and Motion on HQRs from Simval I (Baseli。
![](images/e268d524a28f3bd96f541588bd3f4c0fe4091afeb85e9c78ca6f97b53ad5e11f.jpg)  
Figure 11. Pilot Ratings for Sidestep, Motion Variations from Simval II (Medium-Bandwidth Helicopter)

图片摘要：该图主要展示 11. Pilot Ratings for Sidestep, Motion Variations from Simva。
![](images/539543e5daf0f0e4cc5a0c1febc83aa724eb36e12a334adb48e3cd0f31f8f20e.jpg)  
Figure 12. Effects of Visual Time Delay on Average HQR, Fixed Base

Simval I -- Baseline Washouts

图片摘要：该图主要展示 12. Effects of Visual Time Delay on Average HQR, Fixed Base。
![](images/e58f6a2e986fc8862c87bf3ddf9d6fe44175199078c04e1a2cdc6b96c6eae4ee.jpg)  
a) Hover

图片摘要：该图主要展示 12. Effects of Visual Time Delay on Average HQR, Fixed Base。
![](images/bcb4b08cd89e5064378a4da2f23c70c02382a29c71af8bbd72cc74eb81b4b54b.jpg)  
b) Vertical Translation

Simval II -- Hover Washouts

<table><tr><td colspan="2">Simval I</td><td colspan="2">Simval II</td></tr><tr><td>Pilot</td><td>Sym</td><td>Pilot</td><td>Sym</td></tr><tr><td>D</td><td>◇</td><td>A</td><td>◇</td></tr><tr><td>S</td><td>□</td><td>B</td><td>□</td></tr><tr><td></td><td></td><td>C</td><td>○</td></tr><tr><td>G</td><td>○</td><td></td><td></td></tr><tr><td>T</td><td>△</td><td></td><td></td></tr><tr><td>M</td><td>◇</td><td></td><td></td></tr><tr><td>Mc</td><td>△</td><td></td><td></td></tr></table>

Open -- No Experience on VMS Solid -- Familiar with this Simulator

图片摘要：该图主要展示 13. HQRs for Hover Task with Visual Delay Compensation (Movi。
![](images/80824754391c19bbd76000e708fb4e74f5b098631bdb8ac9bb2df3aa09208e43.jpg)  
c) Hover, Medium Bandwidth

图片摘要：该图主要展示 13. HQRs for Hover Task with Visual Delay Compensation (Movi。
![](images/a06d2f519cd6b6bfbea2060c8819add1f1aeeaef2a932ea3c50746048fdde6b9.jpg)  
d) Hover, High Bandwidth   
Figure 13. HQRs for Hover Task with Visual Delay Compensation (Moving Base)

图片摘要：该图主要展示 13. HQRs for Hover Task with Visual Delay Compensation (Movi。
![](images/e95c4f270535b571cb77efe571f83893a16cd086f18552cdee5f71d46eff38b8.jpg)

图片摘要：该图主要展示 13. HQRs for Hover Task with Visual Delay Compensation (Movi。
![](images/81b4ce7a255e7ba3ca1714cd7e12f0cad1d9a9ab861ee954957178da832aa332.jpg)

图片摘要：该图主要展示 13. HQRs for Hover Task with Visual Delay Compensation (Movi。
![](images/e5dc691ed1b68aa210208f4307d41eff6b3595dfd46bb8c2b78d0aa639997009.jpg)  
a) Experienced VMS Pilot (pilot B)

图片摘要：该图片与b) Novice VMS Pilot (pilot C)；Figure 14. Hover Performance with Visual Delay Com这部分内容相关。
![](images/98800febe1a5b2518d232c422d4d568dc8097af114f0cd69adc52405cab849af.jpg)

图片摘要：该图片与b) Novice VMS Pilot (pilot C)；Figure 14. Hover Performance with Visual Delay Com这部分内容相关。
![](images/9c831940ca3e0bc1b933b436336682922bcc98305afeb4187e1d1b7ef2da532c.jpg)  
b) Novice VMS Pilot (pilot C)   
Figure 14. Hover Performance with Visual Delay Compensation On and Off for Experienced and Novice VMS Pilots (Simval II)   
Visual Delay   
Figure 15. Effect of Visual Delay Compensation on HQRs for Experienced and Novice VMS Pilots

TABLE 1. EFFECTIVE TRANSPORT DELAY OF MOTION SYSTEM (INCLUDING MOTION LEAD COMPENSATION)   

<table><tr><td rowspan="2">Axis</td><td colspan="2">Delay (msec)</td></tr><tr><td>Simval I</td><td>Simval II</td></tr><tr><td>Pitch</td><td>70</td><td>91</td></tr><tr><td>Roll</td><td>70</td><td>88</td></tr><tr><td>Yaw</td><td>70</td><td>157</td></tr><tr><td>Surge</td><td>170</td><td>169</td></tr><tr><td>Sway</td><td>100</td><td>128</td></tr><tr><td>Heave</td><td>130</td><td>168</td></tr></table>

TABLE 2. SOURCES OF VISUAL TIME DELAY   

<table><tr><td rowspan="2">Source</td><td colspan="2">Delay (msec)</td></tr><tr><td>Simval I</td><td>Simval II</td></tr><tr><td>A/D (Stick measurement)</td><td>8</td><td>8</td></tr><tr><td>D/D</td><td>2</td><td>2</td></tr><tr><td>Host Computer (Tcycle)</td><td>20</td><td>25</td></tr><tr><td>Forward Integration (−Tcycle)</td><td>-20</td><td>-25</td></tr><tr><td>Visual Lead (Tcomp)</td><td>variable</td><td>variable</td></tr><tr><td>D/D</td><td>2</td><td>2</td></tr><tr><td>Visual Transport Delay</td><td>83.3</td><td>62.5</td></tr><tr><td>Overall</td><td>95.3 - Tcomp</td><td>74.5 - Tcomp</td></tr></table>

TABLE 3. VALUES OF STICK-TO-VISUAL DELAY EVALUATED   

<table><tr><td></td><td>Simval I</td><td>Simval II</td></tr><tr><td>COMP ON</td><td>12</td><td>14.2</td></tr><tr><td>COMP OFF</td><td>95.3</td><td>74.5</td></tr></table>

图片摘要：该图主要展示 3. VALUES OF STICK TO VISUAL DELAY EVALUATED。
![](images/7ae0a19cf37a6085fd9cc72c433636514b03ee52d166a411536e2d02b603b1c0.jpg)

# Primary Display Latency Criteria

# Based on

# Flying Qualities and Performance Data

by

John D. Funk, Jr.

and

Corin P. Beck

Naval Air Warfare Center

Aircraft Division

Warminster, PA

and

John B Johns*

Army Aeroflightdynamics Directorate

Ames Research Center

Moffet Field, CA

# ABSTRACT

With a pilots' increasing use of visual cue augmentation, much requiring extensive pre-processing, there is a need to establish criteria for new avionics/display design. The timeliness and synchronization of the augmented cues is vital to ensure the performance quality required for precision mission task elements (MTEs) where augmented cues are the primary source of information to the pilot. Processing delays incurred while transforming sensor-supplied flight information into visual cues are unavoidable. Relationships between maximum control system delays and associated flying qualities levels are documented in MIL-F-83300 and MIL-F-8785. While cues representing aircraft status may be just as vital to the pilot as prompt control response for operations in instrument meteorological conditions, presently, there are no specification requirements on avionics system latency. To produce data relating avionics system latency to degradations in flying qualities, the Navy conducted two simulation investigations. During the investigations, flying qualities and performance data were recorded as simulated avionics system latency was varied. Correlated results of the investigation indicates that there is a detrimental impact of latency on flying qualities. Analysis of these results and consideration of key factors influencing their application indicate that: (1) Task performance degrades and pilot workload increases as latency is increased. Inconsistency in task performance increases as latency increases. (2) Latency reduces the probability of achieving Level I handling qualities with avionics system latency as low as 70 ms. (3) The data suggest that the achievement of desired performance will be ensured only at display latency values below 120 ms. (4) These data also suggest that avoidance of inadequate performance will be ensured only at display latency values below 150 ms.

# INTRODUCTION

This paper documents the results of two piloted simulations conducted to generate data regarding display latency effects on flying qualities. A theoretical foundation is presented first to facilitate discussion. In this introduction, latency, flying qualities and a general closed-loop system are defined. The predictions that provided the impetus for the simulation investigations are presented.

# Definition of Latency

Latency associated with a system component can be viewed as a pure time delay between some input or change and the corresponding output. Avionics system latency can be defined as the time delay between aircraft motion and the corresponding indication of that motion on the aircraft displays. Based on this definition, the terms

latency, time delay, and delay are considered equivalent and are interchanged throughout this paper.

# Definition of Flying Qualities

The acceptability of aircraft dynamics and control characteristics can be quantified in terms of achievable mission task performance and resulting pilot workload. This quantification is typically performed using the Cooper-Harper pilot opinion scale shown in Figure 1. Aircraft flying qualities evaluations and specification development are based on results obtained from the use of this scale tempered with actual task performance data. Military flying qualities specifications typically quantify acceptability in terms of flying qualities levels. Explicit in the definition of these levels is not only pilot workload, but also mission task performance as indicated in Figure 1.

图片摘要：该图主要展示 1. Handling Qualities Rating Scale。
![](images/54b58deb2f25586caf9677f802b0daee4bc9744d7c6c4c16b8244c94955bb1f9.jpg)  
Figure 1. Handling Qualities Rating Scale

MIL-F-83300² and MIL-F-8785C³ have been used to define the flying qualities requirements for many military V/STOL aircraft. These requirements are established with respect to the flying qualities levels as defined above. Most Navy aircraft in normal state conditions are required to exhibit Level I flying qualities. This level of flying qualities is required even during the more demanding tasks intended to be flown and in the more adverse environments expected to be encountered. In general Navy aircraft will be required to perform routine and tactical flight operations satisfactorily (including high-speed terrain following flight and shipboard operations) in adverse weather and combat conditions.⁴

# General Latency Effects and Flight Control System (FCS) Latency Specifications

The effect of time delays on flying qualities is common knowledge in the flying qualities community. In summary, data from numerous experiments indicates that time delays reduce closed-loop system stability, thereby increasing pilot workload and degrading task performance. These data further indicate that latency will have an increas

ingly detrimental effect as task difficulty, aggressiveness and precision requirements are increased.

The data referenced above was generated in experiments designed to identify the effects of FCS latency and has been used to define FCS latency limits. Shown in Table 1, these limits have been associated with handling qualities levels and incorporated into military flying qualities specifications. 2,3

Table 1. FCS Delay Specifications   

<table><tr><td colspan="2">Specification</td><td colspan="2">Requirement</td></tr><tr><td></td><td>Flying Qualities</td><td>Time Delay</td><td></td></tr><tr><td>MIL-F-83300</td><td>Level I</td><td>≤ 100 ms</td><td></td></tr><tr><td>MIL-F-8785</td><td>Level I</td><td>≤ 100 ms</td><td></td></tr><tr><td></td><td></td><td>II ≤ 200 ms</td><td></td></tr><tr><td></td><td></td><td>III ≤ 250 ms</td><td></td></tr></table>

图片摘要：该图主要展示 1. FCS Delay Specifications。
![](images/ca77865958dbcdb7eaa2d73e823ab4342df83b92250c0d2f989a45ab0671db19.jpg)  
Figure 2. Standard Closed-Loop System

The time delay limits shown are typical of delay limitations associated with high difficulty/high gain/high precision tasks and may appear conservative. However, it should be noted that most experiments used to support these limits have investigated delay effects with delays inserted in only a single axis of control. Delays in all axes, which is more representative of a real system may result in an even more severe degradation than that indicated above. In this sense, the specifications may be liberal.

# Definition of a Closed-Loop System

A simplified closed-loop system is illustrated in Figure 2 and includes airframe, control, pilot and information components. A typical loop closure will involve pilot control of an aircraft state or flight parameter. During control, the pilot will attempt to minimize the difference or error between a reference or desired value of the selected state and the actual or perceived value of the selected state. Information on the reference value, controlled parameter and the error between the two will be available to the pilot through outside world visual cues, motion cues and displays. To close the loop, the pilot will apply control proportional to the error.

As an example, consider a precision approach to a ship. The pilot's goal is to track the instrument landing system (ILS) beacon, both vertically (glodeslope) and laterally (localizer), with precision sufficient to allow a safe landing. Outer loop control is accomplished with closure around the pilot's reference parameters, glideslope angle, localizer and recovery heading. Inner loop control is accomplished with closure around descent rate, airspeed, and pitch and roll attitude.

Since precise glideslope and localizer error are available only from the displays, the displays can be considered the primary source of information in the above task. This is clearly the case during an approach with degraded visibility, where the displays are the pilot's only reliable source of flight

information.5 Under these circumstances, the pilot would find it difficult, if not impossible, to distinguish between display dynamics, control dynamics and airframe dynamics. The effect of a delay in displayed information could, therefore, be considered equivalent to the effect of an airframe or control delay of the same magnitude.

The most severe delay-induced degradations in flying qualities are expected during high difficulty, high gain, high precision tasks requiring the use of displays as the primary source of flight information. In particular, the concern lies with the performance of manual, high frequency, precision control of aircraft attitude, position and vertical speed in degraded visual conditions (instrument meteorological conditions (IMC), visual meteorological conditions (VMC) with an obscured horizon, and night VMC). Under these circumstances, the head-down displays or helmet-mounted displays would most likely be used to provide the required flight information, either alone or superimposed on a Forward Looking Infra-red (FLIR) image.

# FLIGHT SIMULATION INVESTIGATIONS AND RESULTS

Two manned flight simulations, one in an engineering simulator and one in a high fidelity developmental simulator, were conducted to generate data specific to avionics or display system latency effects on aircraft flying qualities. The first, conducted in a basic engineering simulator to generate initial data, simulated avionics system latency which was swept from 47 ms to 447 ms. The second, conducted in a high fidelity developmental simulator to produce high quality data, was conducted with latency values varying from 70 ms to 240 ms.

A precision approach task was selected as the primary task for the simulation. Performance constraints were established based on mission or safety requirements. Adequate performance constraints were based on maximum safe or

acceptable spatial deviations. Desired performance constraints were established as limits reflecting a desired margin of performance or safety beyond adequate performance constraints. The tasks and the corresponding performance constraints are described below.

Unless specified otherwise, "Latency", "Delay", "Display Delay" and are used in short for 'Avionics System Latency' in the following text.

# Engineering Simulation

# Simulation Facility

This investigation utilized a fixed-base engineering research simulator. This simulator employs standard fixed-wing controls: center stick, pedals, and throttle. The computer generated outside-world image is projected onto a single, forward screen. For this investigation, primary flight information was superimposed on the outside-world image in a standard uncluttered format. This format presented glideslope as a fly-to horizontal bar and localizer as a fly-to vertical bar. Range and airspeed data were digitally represented. The symbology is shown in Figure 3.

The aircraft model used was a generic medium weight, medium agility fixed-wing aircraft with level I baseline handling qualities.

# Evaluation Task

The primary task consisted of a precision approach on a 3.5 degree glideslope to a ship. Environmental conditions were extremely limited visibility and crosswinds up to 45 kt. Direction and magnitude were selected at random, prior to each evaluation run. The initial conditions were glideslope (GS) and localizer (LOC) offsets of 1 degree and 5 degrees, respectively. These were combined randomly to result in four initial positions: above GS and left of LOC, below GS and right of LOC, etc.. Range at the initial position was 24000 ft. Trim approach speed was 128 kt.

The pilot was instructed to capture GS/LOC prior to reaching a 15,000 ft range and to track GS/LOC to 1,500 ft range within the following performance tolerances:

# Desired

$\pm 5$ kt

# Adequate

$\pm 10\mathrm{kt}$

$\pm 1 / 4$ degree GS

$\pm 1 / 2$ degree GS

$\pm 1$ degree LOC

$\pm 2$ degrees LOC

A given level of performance was to be maintained for at least 80-percent of the approach (between 15,000 and 1,500 ft range) for that level to be considered achievable during evaluation.

A secondary task was used to examine the effect of side task workload on primary task performance. This secondary task consisted of the pilot physically setting and verbally repeating the barometric altitude pressure reference to random values called by the engineer every 3000 ft range (with the last call made at 4000 ft). No degradation in performance was tolerated in this task.

# Latency Matrix and Evaluation Technique

Limited by hardware, minimum achievable simulated delays were 57 ms flight controls (from stick displacement to aircraft motion) and 47 ms displays (from aircraft motion to head-up display update). The matrix of delay configurations evaluated is shown in Table 2.

Table 2. Delay Evaluation Matrix   

<table><tr><td>Flight Control Delay (ms)</td><td>Display Delay (ms)</td></tr><tr><td rowspan="4">57</td><td>47</td></tr><tr><td>167</td></tr><tr><td>327</td></tr><tr><td>447</td></tr><tr><td rowspan="4">107</td><td>47</td></tr><tr><td>167</td></tr><tr><td>327</td></tr><tr><td>447</td></tr></table>

Two Marine Corps operational test and evaluation pilots performed as evaluation subjects. Each pilot was given between four and eight hours familiarization time. During evaluation, each pilot was given as many runs as necessary to confidently assess achievable task performance and his workload. This technique resulted in as many as eight flights per delay configuration evaluation (single pilot rating). Further, each pilot evaluated each configuration at least twice.

# Results

Result are presented in the form of pilot ratings and sample time histories of stick activity and tracking error. Pilot ratings as a function of display delay are shown in Figure 4. Sample longitudinal and lateral stick activity with glideslope and localizer tracking error are shown in Figure 5 and 6, respectively.

图片摘要：该图主要展示 3. Engineering Simulation Head Up Display for Precision Appr。
![](images/b563591fc02b761363ae0675ffdd3b2f2101e42c33ef88b823114f3d61a2aaae.jpg)  
Figure 3. Engineering Simulation Head Up Display for Precision Approach

The engineering simulation study supported the following conclusions:

a. No significant, quantifiable differences in handling qualities were observable between evaluations with 57 and 107 ms control delays. As a result, the data for these control system delay configurations were combined and plotted together.   
b. A handling qualities degradation with increasing display delay, although shallow, is observable. This trend, apparent in the pilot rating data, is supported by stick activity and actual tracking performance.   
c. A transition from Level I to Level II occurs between 47 and 167 ms display delay for the primary task alone. A transition from desired to adequate performance (HQR 4 to 5) or the primary and secondary task also occurs between 47 and 167 ms.

# High Fidelity Simulation

# Simulation Facility

The fixed-base simulator used in this investigation employs a representative tilt-rotor cockpit with a multi-window, high-resolution, computer-generated, outside-world image. The simulator mathematical model represents a low to medium agility medium weight tilt rotor aircraft.

# Evaluation Task

Again, the evaluation involved the performance of a precision approach task. This task is similar to that of the engineering simulation. The precision approach task was flown at 85 kt $(75^{\circ}\mathrm{in})$ on a 3.5 degree glideslope. Environmental conditions consisted of mild-to-moderate turbulence with a mild (10 kt) windshear (between 1000 and 100 ft AGL) in addition to a moderate (20 kt) crosswind. A ceiling was simulated at 300 ft AGL. A constant altitude, 30 degree ILS intercept profile was flown from the initial conditions. Tracking constraints for evaluation were identical to those used in the engineering simulation, with one exception. The pilots were instructed to place emphasis on the performance and the workload near decision height, 200 AGL, which was the task termination point.

The approach configuration flown was at 120 kt, $60^{\circ}$ nacelle angle $(\mathrm{in})$ and represented a nominal combat or expedited recovery. Environmental conditions were fixed with mild-to-moderate turbulence, 10 kt windshear, 20 kt crosswind, 200 ft ceiling. As illustrated in Figure 7, initial positions were located at 5.9 nm range with randomly selected offsets of 1 degree in glideslope and 5 degrees in localizer. The initial heading corresponded to the recovery heading with a minor trim adjustment for the crosswind.

The pilot was instructed to maneuver from his initial position to intercept glideslope and localizer by 4.8 nm range and to track glideslope and localizer to decision height (300 ft AGL). For evaluation purposes the task began at initial glideslope and localizer intercept and terminated at decision height.

Tracking constraints were also similar to those used in the engineering simulation, with additional emphasis placed on the last half of the approach. Because of the evolution of these constraints, they are summarized in Table 3. Precision approach flight symbology was mildly cluttered with a vertical bar for localizer, and an arrow indicator for the glideslope and is shown in Figure 8. The above desired, geometric, GS and LOC constraints corresponded to 1/2 of a display tic and 2/3 of a display tic, respectively. Airspeed was indicated with a digital numeric display.

图片摘要：该图主要展示 4. Handling Qulaities as a Function of Display Delay Enginee。
![](images/72e37326ef46f9c70741da39f7232ee721c1e6f2b3d304c6f41801b9e6bd20c7.jpg)

图片摘要：该图主要展示 4. Handling Qulaities as a Function of Display Delay Enginee。
![](images/7d1c3ed9fb486af30131e6b0945cc3880cf26e569c9602254a718d6f342efc12.jpg)  
Figure 4. Handling Qulaities as a Function of Display Delay - Engineering Simulation   
Figure 5. Longitudinal Stick Activity and Glideslope Tracking Error - Engineering Simulation

图片摘要：该图主要展示 5. Longitudinal Stick Activity and Glideslope Tracking Error。
![](images/552d960146b53704bca602ddc1c1eb93dd57c9ac8fb933c3389a31f1ca9197fa.jpg)  
Figure 6. Lateral Stick Activity and Localizer Tracking Error - Engineering Simulation

图片摘要：该图主要展示 6. Lateral Stick Activity and Localizer Tracking Error Engin。
![](images/a8cbf7b2a7fe25cf914885eb9b11802100398bbb055db9292f8240551fa4ed6c.jpg)

图片摘要：该图主要展示 6. Lateral Stick Activity and Localizer Tracking Error Engin。
![](images/47972501ade7e9383efd4945a57157709f09c1e01656f6011b20c0b73aa2a7bb.jpg)  
Figure 7. Precision Approach Geometry

图片摘要：该图主要展示 7. Precision Approach Geometry。
![](images/5e06e3f03206380625095e18b424e9cf1ae5d9478c02273ce5420da3ca8bdfcc.jpg)  
A) Horizontal Situation Display

图片摘要：该图主要展示 7. Precision Approach Geometry。
![](images/6564f8c5a2daef0f284ed4b97d41e3e160b18c323746f59ce7638f891943f081.jpg)  
B) Vertical Situation Display   
Figure 8. High-Fidelity Simulation Display - Simulated Precision Approach Mode

Table 3. Tracking Constraints   

<table><tr><td>Geometry: Desired: ± 5 kt A/S
± 1/4 degree GS
± 1 degree LOC
Adequate: ± 10 kt A/S
± 1/2 degree GS
± 2 degree LOC
Time: - maintain given level of performance for at least 80% of task for given level to be considered achievable
- exceedance of adequate performance constraints for 5 seconds or more could not be considered desirable
Emphasis: - performance and workload during last half of approach (approximately 60 seconds, 1000 ft to 300 ft AGL)
- performance and workload at decision height</td></tr></table>

# Latency Matrix, Pilots, Evaluation Technique

i. Latency Matrix - The FCS latency was fixed at 50 ms. Three display latency configurations (73, 179, and 241 ms) were evaluated.   
ii. Pilots - Four military test pilots served as evaluation subjects. The pilots and their backgrounds are listed in Table 4.

Table 4. Government Pilot Evaluation Team   

<table><tr><td rowspan="4">PILOT A</td><td>2100 HRS HELO (H-53)</td></tr><tr><td>250 HRS FW</td></tr><tr><td>HMX-1 OT+E 1 YR</td></tr><tr><td>V-22 SIM</td></tr><tr><td rowspan="5">PILOT B</td><td>1900 HRS HELO (H-1)</td></tr><tr><td>1500 HRS FW (T-34)</td></tr><tr><td>HMX-1 OT+E 4 YRS</td></tr><tr><td>HQ EVAL EXPERIENCE</td></tr><tr><td>V-22 SIM</td></tr><tr><td rowspan="3">PILOT C</td><td>4000 HRS HELO</td></tr><tr><td>1000 HRS FW</td></tr><tr><td>TPS RW INSTRUCTOR 2 YRS</td></tr><tr><td rowspan="4">PILOT D</td><td>3400 HRS HELO (H-3)</td></tr><tr><td>400 HRS FIXED WING</td></tr><tr><td>TPS/RW</td></tr><tr><td>V-22 SIM + FLT</td></tr></table>

iii. Evaluation Technique - Each pilot underwent extensive familiarization prior to evaluations. This familiarization was accomplished with the mini

mum latency and proceeded as follows. Each pilot took approximately 1 hour of free-flight without turbulence or wind to become familiar with the cockpit and math model. An additional 2 hours was taken by each pilot to fly approximately 20 precision approaches with and without turbulence and wind. During evaluations, the pilots provided an HQR following each run. A complete evaluation consisted of, at least, three runs. When both the pilot and the engineer were satisfied that the delay configuration had been adequately evaluated, the engineer informed the pilot that the delay configuration was to be changed and the next evaluation commenced. The pilot was not informed of the latency value during evaluations. Each pilot performed a minimum of two evaluations per latency configuration.

# Results

Among all pilots, 254 approaches were flown during six days of simulation. Results presented here take the form of pilot ratings and tracking performance as a function of display delay. Pilot rating data is shown in Figure 9. Tracking performance, in terms of time outside desired glideslope envelope, weighted time outside desired glideslope envelope, and time outside adequate glideslope envelope, is shown in Figures 10, 11, and 12 respectively.

Localizer tracking and airspeed maintenance performance is not shown for the following reasons:

- with two exceptions in 254 runs, airspeed error was within desired performance constraints for all values of latency evaluated;   
- even though lateral-axis workload seemed to increase as latency increased, no trend in localizer tracking error as a function of latency was apparent;   
- glideslope tracking performance drove both pilot ratings and comments.

Returning to the glideslope tracking performance data shown in Figures 10, 11, 12, several issues are worth mentioning. First, these data represent the last 60 seconds of the task (from approximately 1000 to 300 ft AGL). Following the time constraints and evaluation emphasis specified, 12 seconds (20% of 60 seconds) can be considered the time constraint associated with desired performance. Any runs with excursions outside of the desired glideslope envelope beyond 12 seconds, during the last 60 seconds of the task, were considered to have, at best, adequate performance. Second, examining time outside of constraints as an isolated performance metric may be misleading if the magnitude of the angular excursion is inversely related to the time of the excursion. To examine this possibility, the time of the excursions were weighted by the corresponding magnitude of the excursions outside of the desired glideslope envelope. These weighted values are plotted in Figure 11. A trend similar to that of the

unweighted data exists. This indicates that time outside of constraints may legitimately be used as a measure of performance.

Finally, considering adequate performance (Figure 12) and following the time constraints and evaluation emphasis, 5 seconds can be considered the time constraint associated with adequate performance. With the time constraint defined, specifying that "exceedance of adequate performance constraints for 5 seconds or more could not be considered desired," any excursion beyond 5 seconds could legitimately be classified as either adequate or inadequate. Nearly all excursions outside of the adequate glideslope envelope occurred, however, just prior to decision height. The pilots, observing the emphasis on performance near decision height, typically classified the excursions beyond the adequate glideslope envelope of 5 seconds or more as inadequate.

Examining the results, one general observation can be made:

A handling qualities degradation with increasing display delay is apparent in both the pilot ratings and tracking performance.

The nature of this degradation and its applicability to defining an acceptable level of latency is discussed in the following section.

# DEFINING AN ACCEPTABLE LATENCY LEVEL

When attempting to define a limit on any flying qualities parameter, several criteria may be considered:

- achievement of Level I handling qualities   
- achievement of desired performance (note that achievement of desired performance does not mean that Level I handling qualities are achievable; Level II handling qualities (HQR 4) could result if workload is moderate or greater - see Figure 1)   
- avoidance of inadequate performance

Regarding these criteria the results will first be considered in isolation. A discussion of the issues affecting the definition of delay limits will be discussed subsequently.

PILOTS A B C D

图片摘要：该图主要展示 9. Handling Qualities Ratings for Precision Approach。
![](images/f5d1c12062dcb25973bc28acc4d049271c5fefc5df112681692cc0efb69f12b7.jpg)  
70 ms DELAY

图片摘要：该图主要展示 9. Handling Qualities Ratings for Precision Approach。
![](images/295f6a137ff074030d59e0a5a5ea4aa0eb3071c7d477da0dbb2a4fc9aaade4c9.jpg)

Figure 9. Handling Qualities Ratings for Precision Approach   
图片摘要：该图主要展示 9. Handling Qualities Ratings for Precision Approach。
![](images/a80000d224c2bf42c25627e1da76b1bdd0ac49c0ccb0af11adfbe9653a5c8e1b.jpg)  
NOTE: The data shown above are the result of two modifications of the raw data. During the evaluation process pilots were permitted to give a rating of 4.5 for either of two reasons: desired performance was achievable with maximum pilot compensation only adequate performance was achievable but with minimal pilot compensation. Ratings of 4.5 with desired performance achievable and 4.5 with adequate performance achievable redistributed to HQR 4 and 5 respectively. The other modification involved adjustment of ratings to reflect r ponding actual performance. In this case, the minimal possible adjustments were made and only when the original ng clearly was not supported by actual performance. Here, 3, 1, and 8 ratings were adjusted at 70, 170, and 240 ms; pectively. Neither of these modifica-tions altered the true nature of the results.

图片摘要：该图主要展示 9. Handling Qualities Ratings for Precision Approach。
![](images/3bbab376b279d8f66169975150adea56324ccefbf5e639b01377307c3718fa2e.jpg)  
Figure 10. Tracking Performance - Time Outside of Desired Glideslope Envelope

图片摘要：该图主要展示 10. Tracking Performance Time Outside of Desired Glideslope 。
![](images/92fc05c9e707776afe31e1ab763bf7b9b2c9d08ebee71053b720e635c821c696.jpg)  
Figure 11. Tracking Performance - Weighted Time Outside of Desired Glideslope Envelope

图片摘要：该图主要展示 11. Tracking Performance Weighted Time Outside of Desired Gl。
![](images/eec5ddf5ea86a6e35a3d0b7bb7dafbda05f148f068cfdeef6aa3472ebf7e516c.jpg)  
Figure 12. Tracking Performance - Time Outside of Adequate Glideslope Envelope

# Achievement of Level I Handling Qualities

In applying the first criterion, pilot rating data (Figure 9) and performance data (Figure 10) must be examined. From Figure 9, it is apparent that, although there is a clear improvement in handling qualities between 170 and 70 ms, consistent Level I handling qualities are still not achievable at 70 ms. Further, from Figure 10, an improvement in

tracking performance through a reduction in time outside of constraints is apparent with decreasing latency. A continuation of this trend, although shallow, is reasonable to assume if latency were dropped below 70 ms. It may also be reasonable to assume based on the available data that, as latency is reduced below 70 ms, workload would first incrementally decrease and then level off at some baseline. Taken together, these observations and assumptions lead to the conclusion that reducing latency below 70 ms should result in consistent Level I handling qualities.

# Achievement of Desired Performance

Workload is not a consideration when applying this criteria. Tracking performance may therefore be examined directly. For this purpose, time outside of the desired glideslope envelope as a function of latency is shown in Figures 13 A, B, C.

The probability bands in Figure 13 are defined by the worst 10, 20, or 30 percent of the main body of the performance data. Examination of these bands reveals the nature of latency effects on flying qualities. The following observations are made regarding achievement of desired performance.

- As latency increases, an increasing rate of performance degradation is apparent.

- Extrapolating the bands below 70 ms, very little performance benefit is expected with a latency reduction below 70 ms.

- If an increased probability of exceeding overall desired performance constraints is tolerable, then a higher latency is acceptable. As an example, if a 10-percent probability of exceeding desired constraints is tolerable, then a latency of 120 ms is acceptable. If a 20 percent probability of exceeding desired constraints is tolerable, then a latency of 170 ms is acceptable.

However, noting that there are significant occurrences of inadequate performance at 170 and 240 ms (see Figure 9), avoidance of inadequate performance must be considered.

图片摘要：该图片与A) 10 percent probability；A) 10 Percent Probability这部分内容相关。
![](images/12e8a13565451024f3c4d66b9cbff42588d99c55a7345fba4485ba35320c90ca.jpg)  
A) 10 percent probability

图片摘要：该图片与A) 10 Percent Probability；B) 20 percent probability这部分内容相关。
![](images/0330c5c5ea40ea4491e4c73c1e4bd37be293a4fb35ca21b9cd35318db4145d10.jpg)  
A) 10 Percent Probability

图片摘要：该图主要展示 14. Probability of Exceeding Adequate Performance Envelope f。
![](images/f25c8d003b404626ae7e99cb638ca0be80d47dbd1564341e9f7113a09a9678ab.jpg)  
B) 20 percent probability

图片摘要：该图主要展示 14. Probability of Exceeding Adequate Performance Envelope f。
![](images/37a627db63d21f72575ad756a42683e1c76e853fa9cdab1ee21c344a0e008558.jpg)  
B) 20 Percent Probability

图片摘要：该图主要展示 14. Probability of Exceeding Adequate Performance Envelope f。
![](images/15bb9b6d3c6517b6f7ea7a5ab100598770aa0b384db4f18901f0e5e1cc12c24f.jpg)  
C) 30 percent probability   
Figure 14. Probability of Exceeding Adequate Performance Envelope for More Than 5 Seconds During the Last Half of the Approach   
Figure 13. Probability of Exceeding Desired Performance Envelope for More Than 20 Percent of the Last Half of the Approach

# Avoidance of Inadequate Performance

Tracking performance can also be examined directly in this section. Here, however, time outside of adequate glideslope envelope is used in the analysis. As in Figure 13, the probability bands shown in Figures 14 A and B are defined by the worst 10 and 20 percent of the main body of the performance data.

Examination of these bands provides additional insight into the effects of latency on flying qualities. The following observations can be made regarding the avoidance of inadequate performance:

- A linear degradation in tracking performance and consistency with increased latency is apparent.   
- Extrapolating the bands below 70 ms, a substantial performance benefit is expected with a latency reduction below 70 ms. This extrapolation indicates that below 10 to 20 ms no excursions outside of adequate constraints would occur.   
- If an increased probability of exceeding overall adequate performance constraints is tolerable, then a higher latency is acceptable. As an example, if a 10-percent probability $\mathcal{P}$ of exceeding adequate constraints is to be able, then a latency of 150 ms is acceptable. If a 20-percent probability of exceeding adequate constraints is tolerable, then a latency of 240 ms is acceptable.

# ISSUES AFFECTING DEFINITION OF A LATENCY LIMIT

Due to the origin and quantity of data used in the analysis, the following issues must be considered when applying the results of the previous section to definition of a latency limit:

- Data Quality   
- Simulation vs. Actual Flight   
- Simulation Fidelity   
- Cues Available to the Pilot   
- Pilot Gain

- Severity of Task/Environment

- Training

# Data Quality

The data used in the previous analysis were generated under controlled conditions using accepted flying qualities evaluation techniques. The evaluation pilot population was diverse and representative of the general pilot population. Minor adjustments were made to the pilot rating data to better reflect actual performance; actual performance data were used "as is."

A general qualitative check on both the experiment and data validity can be made by examining the trends in Figures 10, 13, and 14. These trends are what is physically expected from the effects of latency on tracking performance and workload.

Based on the above, the data used in the analysis are considered to be 'high quality.'

# Simulation vs Actual Flight

Motion cues are not available in a fixed-base simulator. As a result, lead information available through actual commanded aircraft acceleration was not available. In the task used in evaluation this is not a factor for several reasons. First, tracking error information is only available to the pilot from the display. Motion cues do not provide any tracking error information. Even though motion cues aid inner-loop control this provides only marginal benefit in a primary visual tracking task. Second, during precision approach in IMC, the displays are the only reliable source of flight information. Anomalous aircraft motion cues, from both the pilot's head orientation and turbulence, force the pilot to rely on display information for an accurate assessment of the flight condition. A detrimental effect, if any, is expected due to the display latency induced mismatch between actual dynamics and display dynamics.

Finally, pilot gain would be higher in flight than in the simulator. Pilots would be less tolerant of tracking errors. This tolerance change would manifest itself through an increase in control activity. In turn, this increase in control activity would accentuate the effects of latency.

Therefore, given the same task, configuration and conditions, tracking performance and workload in flight are expected to be worse than that in the simulator.

# Severity of Task and Environment

The precision approach evaluation task used was representative of a nominal combat or expedited recovery in IMC. This task should be able to be performed with Level I handling qualities. Potentially more demanding tasks such as terrain following or target tracking have not been explored.

The wind and turbulent environment can be classified as mild to moderate. Much more severe environments are frequently encountered in the field.

A lower limit than that associated with a nominal precision approach may be required to ensure satisfactory performance of potentially more demanding tasks or nominal tasks in more severe environments.

# Training and Pilot Compensation Techniques

Pilots, with sufficient training will develop delay compensation techniques. In compensation, the pilot would reduce his input magnitude and frequency. This technique would not only allow the aircraft and display to respond, but also limit the response magnitude to a controllable level. This technique, by its nature prohibits high frequency precision control, and requires the acceptance of task performance degradations.

Another technique that can be used is lead compensation. This technique involves an initial control overshoot by the pilot to quicken the response followed by a reduced steady state input to limit the response magnitude. As with lead compensation implemented with the avionics or FCS, pilot lead is effective, but only over a given frequency range. Furthermore, this technique, by its nature, requires the pilot to stay in the control loop, with his energy split between two primary control frequencies, one associated with his application of lead (high frequency), and one associated with the fundamental task requirements.

Under normal conditions, pilot compensation can be effective. In emergency conditions or during sudden severe disturbances, the pilot tends to abandon compensation techniques instinctive control. Under these circumstances, the pilot will increase input magnitude and frequency in an attempt to retain control of his aircraft. This, however, accentuates the detrimental effects of latency and only aggravates the control problem. In the extreme, an aircraft with large delays, but readily controllable with appropriate pilot compensation, will become uncontrollable in emergency conditions or during sudden severe disturbances.

Negative training is also an issue. Although the compensation techniques described above can be effective with large delays, they can be detrimental if applied to a system with low delays. If compensation techniques used in IMC are retained in performance of a visual task, a degradation in task performance and increase in workload are expected.

Integrating the above issues, the net impact on the application of the simulation data is minimal. Any latency limit, based on analysis of the previously presented simulation data, is expected to be applicable to an actual production aircraft.

# CONCLUSIONS

The results from the Navy simulations correlate well. These studies further indicate that performance and flying qualities degradations can be expected to occur with increasing avionics system latency. Considering the simulation data, several latency limits are suggested.

- 70 ms or below to ensure Level I handling qualities.   
- 120 ms or below to ensure desired performance (with a maximum 10-percent probability of exceeding constraints).   
- 150 ms or below to ensure the avoidance of inadequate performance (with a maximum 10-percent probability of exceeding adequate performance constraints).

These limits were established from analysis of data generated during simulation where the flight control latency was 50 ms. If actual flight control latency differs significantly from 50 ms, the above limits must be examined from a system latency point of view.

# ACKNOWLEDGEMENTS

The authors would like to thank pilots USAF Maj. Joe Bonin, USMC Majs. Kevin Dodge and Doug Isleib, and USA CWO4 Reggie Murrell for participating in the study.

# REFERENCES

1. Cooper, G.E. and Harper, R.P., The Use of Pilot Rating in Evaluation of Aircraft Handling Qualities, NASA TN D-5153, April 1969.   
2. Anon., Military Specification, Flying Qualities of Piloted V/STOL Aircraft, MIL-F-83300, 31 Dec 1969.   
3. Anon., Military Specification, Flying Qualities of Piloted Airplanes, MIL-F-8785C, 5 Nov 1980.

4. Anon., Joint Services Operational Requirements, Joint Services Vertical Lift Aircraft, 14 Dec 1982.   
5. U.S. Department of Transportation, Federal Aviation Administration, Instrument Flying Handbook, AC 61-27C, 1980.   
6. Jex, H.R., et al., Roll Tracking Effects of G-Vector Tilt and Various Types of Motion Washout, Fourteenth Annual Conference on Manual Control, NASA Conference Publication 2060, November 1978.   
7. Clement, W.F., et al., Systematic Manual Control Display Design, 13th AGARD Guidance and Control Panel Symposium, Paris, France, Oct 1971.

# Session 5

Aircraft Applications and Development

# HUMAN FACTOR IMPLICATIONS OF THE EUROCOPTER AS332L-1 SUPER PUMA COCKPIT

R. RANDALL PADFIELD

Flight Instructor, AS332L

Helikopter Service A/S, Norway

# ABSTRACT

The purpose of this paper is to identify and describe some of the human factor problems which can occur in the cockpit of a modern civilian helicopter. After examining specific hardware and software problems in the cockpit design of the Eurocopter (Aerospatiale) AS332L-1 Super Puma, the author proposes several principles that can be used to avoid similar human factors problems in the design of future cockpits. These principles relate to the use and function of warning lights, the design of autopilots in two-pilot aircraft, and the labeling of switches and warning lights, specifically with respect to abbreviations and translations from languages other than English. In the final section of the paper, the author describes current trends in society which he suggests should be taken into consideration when designing future aircraft cockpits.

# NOMENCLATURE

ADF Automatic Direction Fin

ADI Attitude Deviation Indicator

CDI Course Direction Indicator

DECCA Area Navigation System

DME Distance Measuring Equipment

EFIS Electronic Flight Info. System

FFCL Fuel Flow Control Lever

HSI Heading Situation Indicator

IFR Instrument Flight Rules

ILS Instrument Landing System

LORAN Area Navigation System

MGB Main Gear Box

NG Gas Generator Speed

NR Rotor Speed

T4 Engine Exhaust Gas Temp.

VLF/OMEGA Area Navigation System

VOR VHF Omnidirectional Receiver

# INTRODUCTION

The Eurocopter (Aerospatiale) AS332L-1 Super Puma is a twin-engine commercial helicopter, primarily designed for passenger transport. It is a derivative of the SA 330 Puma which was developed initially to meet a French Air Force requirement for a medium-sized helicopter able to operate day or night in all weather and in all climates. Although used very little in the United States, the Super Puma is popular in many parts of the world and has been particularly successful in offshore oil market in the North Sea. The AS332L-1 is equipped with Turbomeca Makila 1A1 engines, can carry up to 24 passengers, has a maximum gross weight of 18,960 pounds, and has a maximum cruise speed of 150 knots.

The author flew and instructed in Super Pumas for Helikopter Service A/S of Norway, a North Sea offshore operator, and Trump Air of New Jersey, a FAR Part 135 operator. The information contained in this report comes from over five years and 2000 hours of flying experience in the Super Puma and from over 600 hours of instruction and observation of other experienced professional pilots in a six-axis AS332L-1 Rediffusion simulator owned by Helikopter Service.

It is the author's contention that the optimum cockpit design for any aircraft will not be found by the manufacturer alone. Line pilots and instructors can and should help manufacturers decrease the incidence of human factor errors by providing enlightened feedback about ergonomic problems encountered in the cockpit.

# THE SHELL MODEL

The SHELL Model (Fig. 1) is one conceptual model of human factors. In the center of the model, is the human operator, or LIVEWARE. When working with a machine, the operator must contend with SOFTWARE, HARDWARE, the ENVIRONMENT, and other LIVEWARE. A mismatch anywhere in the system causes stress, which decreases efficiency and safety.

图片摘要：该图主要展示 1. The SHELL model of human factors。
![](images/3f626e63def86ba0534acfd85fa59964e35c37730db29f0875cacf66ffc8880d.jpg)  
FIGURE 1. The SHELL model of human factors.

HARDWARE relates to the machine itself and, with respect to aircraft, includes such things as controls, displays, warning systems, safety equipment, seat design, and cabin facilities.

SOFTWARE, again in relation to aircraft, includes operating procedures, format of manuals, checklist design, language of information, graphs/tabulation design, and symbology.

ENVIRONMENT includes temperature, noise, vibration, humidity, pressure, light, pollution, and circadian/biorhythmic cycles.

LIVeware includes personal relations, crew coordination, discipline, communications, and leadership.1

The main concerns of this paper are with the hardware and software portions of the SHELL model. Although there is room for improvement of

environmental factors in many aircraft and particularly helicopters, problems with these factors are generally well-known. Liveware factors, i.e. the human-to-human interactions, are usually outside the realm of the designer's influence, although such things as radio and intercom systems, which are also hardware items, have obvious effects on communications. Therefore, both environmental and liveware concerns are outside the scope of this paper.

# HARDWARE FACTORS OF THE AS332L-1 COCKPIT

# Engine MalfunctionWarnings

"OVSPD" warning switch/light. To protect against an engine and rotor overspeed, the fuel control on the Aerospatiale AS332L-1 Super Puma is designed to shut down the engine automatically if the power turbine speed goes too high. Because the main conditions that can cause a power turbine overspeed (high speed shaft or free-wheeling unit failure) happen so quickly, an overspeed warning light (Fig. 2) is provided so that the pilots realize the engine has shut itself down due to an overspeed. This is a good thing to know because one should normally not re-start an engine if this happens.

图片摘要：该图主要展示 2. "OVSPD" warning switch/light。
![](images/1f5a900798fbe436188ab6b5db0485e0891774437dc8580e889adfc201433af1.jpg)  
FIGURE 2. "OVSPD" warning switch/light.

A relevant point is that the "OVSPD" light burns steadily when the engine is shut down normally, but the light flashes when the overspeed mechanism shuts the engine down.

This creates a human factors problem. Most pilots have a built-in aversion (although actually it is a conditioned response) to flashing lights in the cockpit. Their immediate gut reaction to a flashing lighted switch is to press the switch to make it stop blinking. A typical example is the master caution light in some aircraft. Another

example is the RACAL Avionics RNAV 1 DECCA system which flashes a warning light that must be depressed when there is a problem. There are certainly many other good examples.

How can a flashing light be a problem? Consider the following scenario. First, one engine fails due to an overspeed. The copilot sees the flashing "OVSPD" light, says nothing, and then, unconsciously, presses the light to stop it flashing. Many companies even specify that the first action during any emergency procedure is to extinguish the master warning light.

A few minutes later, the captain, who up to this point has been concentrating on flying the aircraft, considers trying a restart because he didn't see the overspeed warning light flashing and the light is now steady. The copilot, who cancelled the only indication that would tell them they had an engine overspeed, readily agrees to a restart because he cancelled the light without consciously thinking about it. The engine starts normally, because the broken engine-to-MGB shaft has no effect during the starting sequence, but as the pilots increase power, the unburdened power turbine and its broken shaft spin faster and faster until something else breaks. Although this has never happened in flight, there is one instance of a Super Puma engine being re-started by a mechanic on the ground after the engine had shut down due to an overspeed. The aircraft caught fire and was destroyed.2

Three lessons can be learned from this example. First, flashing warning lights should only be used for the most serious of malfunctions. Too many flashing lights in a cockpit defeats their purpose, which is to catch the pilots' attention and alert them to a particular problem.

Second, it should only be possible to extinguish a flashing warning light by taking the proper corrective action and removing the hazard. For example, a flashing fire warning light should only go out when the fire itself has been extinguished.

Third, extreme care must be used when designing a switch to function as both a switch and a warning light. If the light in a switch does more

than simply indicate whether an item is off or on, the function of the switch must be easily understood at all times and under all conditions. One should not assume that a task people can do under normal conditions will still be error-free when a panic is on.3

"POWER" light. Another engine light that causes problems is the "POWER" light. The "POWER" light is under the direction of the power calculation system which is designed to help the pilots determine which engine is malfunctioning under various conditions. Very basically, the power calculation system examines the Ng (gas generator rpm) readings from both engines and the Nr (rotor rpm) to determine which engine has malfunctioned and why; then it illuminates the "POWER 1" or "POWER 2" light as appropriate.

This is particularly good information to provide the pilot when the automatic fuel control of one engine fails and that engine, although still operating, must be controlled manually. Because the other engine automatically varies its power output in order to maintain Nr within limits, it can be difficult to determine which engine is malfunctioning.

The problem with the "POWER" lights is that they don't illuminate until Nr varies approximately $6 - 7\%$ above or below the usual inflight setting of $100 - 101\%$ . Although these Nr values are neither dangerously high nor low, they are well outside the "usual" Nr values.

Notice the use of the word "usual" and not "normal." After one hundred or so hours in any aircraft, most pilots know what the "usual" values are for pressures, temperatures, rpm, etc. As a result, they become suspicious when they see "unusual" values, even if these values are within the specified "normal" limits. When a helicopter pilot observes an "unusually" high or low $\mathbf{Nr}$ , his first reaction is to adjust collective pitch to bring the $\mathbf{Nr}$ back to its "usual" normal value.

What happens when an automatic fuel control malfunctions and causes the Nr to vary is that the pilot instinctively adjusts the collective pitch to bring the Nr back to where it belongs. This defeats the intention of the power calculator

system because it cannot illuminate a "POWER" light unless the Nr is above $107\%$ or below $94\%$ . The pilot is left to figure out which engine is malfunctioning by interpreting the Ng and T4 indications; or he can choose to raise or lower the collective until the Nr changes enough to cause the power calculator to illuminate a "POWER" light, an action which many pilots are reluctant to do.

# Autopilot System

General. Any pilot who has ever worked with an advanced autopilot knows that the most frequent mistakes made by pilots, even after they know how the system operates, are:

1) pushing the wrong buttons at the right time,   
2) pushing the right buttons at the wrong time,   
3) pushing the right buttons in the wrong sequence,   
4) thinking that an autopilot function is off when it is on, and   
5) thinking that an autopilot function is on when it is off.

A primary cause of these errors is the manner by which the autopilot functions are displayed. Usually, the annunciator lights are shown on one central autopilot panel, which is often on the center cockpit console (easy to reach, but out of sight). Sometimes the annunciators are duplicated elsewhere in the cockpit, on the panels in front of the pilots or even on the flight instruments themselves. For example, airspeed hold may be displayed on the airspeed indicator, altitude hold on the barometric or radar altimeter, localizer and glide slope hold on the HSI (Horizontal Situation Indicator) or artificial horizon (ADI).

Of the three methods, indicating autopilot functions on the flight instruments is the best because this is the method the autopilot annunciators will be seen most often by the pilot. The simple reason is that the flight instruments are an integral part of every experienced pilot's cockpit scan. The autopilot annunciator panel on the center console is not a frequent part of most pilots' instrument cross-check.

AS332L-1 autopilot system. The Helikopter Service AS332L-1 Super Pumas are equipped with SFIM 155 duplex autopilot systems, SFIM CDV 85 four-axis couplers, Collins ADI-77 Attitude Direction Indicators, and Astronautics 133640 Horizontal Situation Indicators.

Mixing boxes from different manufacturers may not always be desirable, but due to economic reasons (mixing may be less expensive), operational considerations (one system may not provide all things to all operators), and marketing aspects (compatibility of systems means greater potential sales), mixing systems is not going to go away. As a consequence, designers of the various components have to pay even more attention to human factor problems and, equally important, there must be someone in the loop who is able to examine the resulting system in its entirety.

With respect to the autopilots in Helikopter Service's Super Pumas, when they work as designed, the autopilots are truly impressive. If there is a malfunction, there are, for the most part, sufficient back-ups and warnings for the pilot. In other words, the autopilot hardware, per se, is generally very good.

However, of all the systems in the Super Puma, it is universally agreed in Helikopter Service that the autopilot is the most difficult for pilots to master. Many of the difficulties with the autopilot stem from human factor problems in the design of the system.

Single- or dual-pilot system? The most basic problem with the system is that it can not be fully operated from the left seat. Certain functions, for example coupled ILS and coupled vertical speed, can only be controlled by the pilot in the right seat. The system favors the captain's side of the cockpit to the detriment of the copilot's side.

The reason was Aerospatiale's original intention to obtain single-pilot IFR certification for the Super Puma. This has not been obtained and may never be, but the result is an autopilot system that makes it difficult or impossible to set up, among other things, a coupled ILS approach from the left seat.

Why is this lack of full dual-pilot capability not good? Consider this scenario: The captain becomes incapacitated, the weather at the airport is at minima, and the copilot is young and inexperienced. He needs all the help he can get, but because he can't reach the necessary switches on the right side of the cockpit, he has to fly the ILS uncoupled.

A good general principle to use when designing autopilot and coupler systems is to make all autopilot functions fully controllable from both seats in the cockpit. There should also be one switch, easily accessible to both pilots, that passes autopilot authority from left to right and back again. And there must be a well-defined annunciator prominently located on the front panel (the best place would be right on the artificial horizon) telling the pilots who has the authority.

With respect to single-pilot IFR, the following policy statement from the International Federation of Air Line Pilot Associations (IFALPA) is appropriate:

"Although IFALPA recognizes that presently single-pilot commercial operations are in widespread use, this type of operation is not acceptable during international public transport flights, including all off-shore flights, because of the reduced level of safety."

Single-pilot IFR capability is great, but it should be available to both captain and copilot alike.

Heading select switch. The Helikopter Service machines have a switch which is used to transfer autopilot authority between the pilot and copilot, however it only controls the heading select function of the system (Fig. 3). Both pilots have a selected heading index, or heading "bug," on their horizontal situation indicator (HSI) which is used to set a desired heading the autopilot coupler should maintain. The heading select switch tells the autopilot which heading index to follow.

图片摘要：该图主要展示 3. Heading select switch。
![](images/64077e1f4b73da8446f66d3190f6fb7d2aba20a2d50edeba33bd0fccdc3c9f29.jpg)  
FIGURE 3. Heading select switch.

The idea is simple enough and easy to understand, but the switch and its associated annunciator lights indicating which pilot has heading authority are located on the pedestal console between the pilots, far away from the HSIs and other primary flight instruments. The error, which happens frequently, is that one pilot sets his heading index to the desired heading and, forgetting to check the heading select switch, engages the coupler heading hold. If the switch is still set to the other pilot and his heading index is set at another heading, the autopilot will obviously turn the helicopter to an undesired heading.

This problem could have been avoided by putting the annunciator lights for the heading select switch on the heading indices of the HSIs. When the pilot has heading control, his index is illuminated (or some other way highlighted); when the copilot has heading control, his heading index is highlighted.

Localizer and glide slope capture modes. The problem with these modes is deceptively small, yet potentially extremely dangerous. The "fix" is probably relatively simple, given the complexities of the rest of the autopilot system.

An Instrument Landing System (ILS) provides precision guidance to a runway while providing very specific obstruction clearances throughout the approach. By regulation and common sense, an aircraft is not allowed to descend on the glide path until it is established on the localizer course.

With the SFIM CDV 85 four-axis coupler, it is possible to arm both the localizer and glide slope modes before being established on either one. This makes sense because the pilots can set up the autopilot before they reach the localizer. What doesn't make sense is that it is possible to capture the glide slope before the localizer is captured, and, in fact, even with the localizer mode unarmed. As a result, the aircraft will descend on the glide slope beam while outside the limits of the localizer, which means that the aircraft could be descending below the minimum altitudes designated for that part of the approach.

Coupler and flight director annunciation. Human factor specialists have often observed that people adapt well to design deficiencies in their working environment. One way Super Puma pilots have adapted to the poor annunciation of the coupler functions is to use the flight director command bars (Fig. 4, #2 & 6) on the ADI as an indication to them that the coupler is on. With the command bars right on the instrument they look at most often, the presence of the bars is not hard to overlook. The pilots simply make it a personal habit to always engage the flight director whenever they engage the coupler.

图片摘要：该图主要展示 4. Attitude Deviation Indicator。
![](images/4367cd682e307df41a1f2aa55cb1aa689c6225500b4f086807a5296b16c0011b.jpg)  
FIGURE 4. Attitude Deviation Indicator

This practice does, however, have one big disadvantage. If the autopilot disengages, due to a malfunction, on purpose, or inadvertently (and it is disengaged inadvertently from time to time), the coupler drops out, but not the flight director. This makes sense because it is useful to have flight direction when the autopilot is out. The problem occurs when the autopilot is switched back on.

It is not difficult to know when the autopilot disengages: one feels the difference in the cyclic at once. The non-flying pilot usually notices the change in the stability of the flight, as well, and if he is alert, he reaches down and re-engages the autopilot within seconds. Both pilots breathe a sigh of relief.

Unfortunately, their problems are not over. For although the autopilot is back on and the

flight director command bars are still in view on the ADIs, the coupler is not engaged. The only indication that tells the pilots the green coupler function lights are sending signals to the flight director only and not to the autopilot, is a small, dimly-lit "F/D" light tucked away above the ADIs.

It usually takes some time and perhaps large heading or altitude deviations before the pilots discover that the autopilot coupler functions are not flying the helicopter for them. If this happens during a critical phase of flight, such as during an instrument approach to an oil rig at night, the consequences could be tragic.

"CPL" warning light. Whenever a coupler function fails or is turned off, the "CPL" light on the master annunciator panel and the master "WARN" lights illuminate. Pilots like to have warnings when something fails, but to receive a warning every time something is purposely switched off is counterproductive.

The human factor reason is so obvious that it is difficult to understand how it was overlooked: If a warning light comes on numerous times during every flight, eventually it will be ignored.

The first time a pilot new to the Super Puma switches off a coupler hold function he immediately notices the "CPL" and "WARN" lights illuminating, and, being new to the machine, he logically assumes something has failed. However, by his third or fourth flight, he is already ignoring the "CPL" light or canceling it without thought.

The story about the boy who cried "Wolf!" is a good lesson in human nature which was apparently forgotten when the SFIM designers were working on this part of the CDV 85 four-axis coupler.

# Navigation Equipment

NAV-HSI switching panel. Another very confusing part of the Super Puma is the navigation switching panel (FIG. 5). Basically, each pilot has two pointers on the HSI, and he has switches by which he can choose which navigation radios

he wants to monitor. There is also a switch that controls the Course Direction Indicator (CDI) which accepts signals from VOR 1 or VOR 2. However, there is an inflexibility in the system in that the autopilot will accept coupled ILS signals only from VOR 2 and only when the right-seat pilot has selected VOR 2 on his CDI and only when the heading select switch is set to "PILOT." This automatically, restricts the pilots' choices if they want to fly a coupled ILS.

图片摘要：该图主要展示 5. NAV HSI switching panel。
![](images/1763dde4e7e616d1d8df0eb8fc3cf44c88e322272ac114bb3c711ac22ac534c0.jpg)  
FIGURE 5. NAV-HSI switching panel

The number 1 (green) pointer on both pilots' HSIs takes signals from either VOR 1 or the ADF (or ADF 1 if two are installed). The number 2 (orange) pointer takes signals from VOR 2 and the ADF (or ADF 2 if two are installed).

The confusion occurs because BOTH pointers can indicate either VORs or ADFs and it is common to use both a VOR and an ADF during many VOR and ILS approaches. What can easily happen is that the copilot has the ADF on pointer 1 and the VOR on pointer 2 and the pilot has the opposite indications.

A better system, given the limitations of only two pointers, would be to designate one pointer as the VOR pointer and the other pointer as the ADF pointer, with a switch to reverse these functions in case of a pointer failure. That way both pilots would always know that they have VOR information on the green pointer, for example, and ADF information on the orange pointer. To remove the question of which VOR or ADF is being monitored, the pointers themselves could display a "1" or "2," indicating, respectively, VOR 1 or VOR 2 on the VOR pointer and ADF 1 or ADF 2 on the ADF pointer. The navigation pointers incorporated in many EFIS installations the author has seen are labelled in this manner.

One could monitor two VORs on the same HSI by switching the CDI to one VOR and the VOR pointer to the other. It would not be possible to monitor two ADFs simultaneously on one HSI, but this is a relatively infrequent requirement. (The Helikopter Service Super Pumas are only equipped with one ADF anyway.) If there is a requirement to monitor two ADFs, the pilot could monitor one and the copilot the other, or, as an alternative, either pilot could switch between ADF 1 and ADF 2 every few minutes to check the relative bearings to the NDB stations.

DME selection. It is possible to monitor one of six different DME stations depending on how the switches are set. However, the only indication of which VOR frequency is giving the DME reading is by the position of the switch and a light on the radio itself. The light indicates that the DME is coming from that box (number one or two), but it could be from one of three possible frequencies, one of which may not be displayed, depending on the position of the HOLD switch.

This can and does create so much confusion that Helikopter Service instructors recommend setting the DME function switch to VOR 2 (because this is the only VOR that can be used to fly a coupled ILS approach) and just leaving it there all the time, except in those rare cases when DME information from a second VOR is required. The problem is that there are just too many choices -- too many frequencies from which one can receive DME information. In the heat of an approach or a missed approach, it's easy to forget which DME one is monitoring.

Radio frequency selection. This is a generic problem to many aircraft, not just the Super Puma. Many operators do not have $100\%$ standardized fleets. In fact, there are probably very few operators that have the same radios in all their aircraft. This is obviously a matter of economics that pilots just have to live with.

With most radios, the frequency selected increases when one rotates the knobs clockwise, but on a few the frequencies increase when the knobs are turned counter-clockwise. Some radios allow one to rotate the knob past the highest useable frequency and continue turning to the lowest

frequency on the scale, and vice versa. Others stop at the highest and lowest frequencies, making it necessary to turn the knob back the other way. Most two-tiered knobs (like wedding cakes) work so that the lower, bigger knob adjusts the numbers in the left window (therefore the higher numbers) and the higher, smaller knob adjusts the numbers in the right window (therefore the lower numbers); other radios work just the opposite.

It goes without saying that pilots are going to have trouble tuning frequencies when they have to use different radio sets. This may seem like a relatively small thing, and most of the time it is, but it can be a time-waster. In the worst case a pilot may accidentally set the wrong frequency, not have time to check the windows, and miss a critical radio call. Standardizing how frequencies are dialed in will eliminate one area in the cockpit that is prone to mistakes.

# Landing Lights

When the search light switch in the Super Puma is pushed down, the search light moves up. When the switch is pushed up, the search light moves down.

This is exactly opposite from the way the moveable search light in the S-61 and Bell 212 work and since all Helikopter Service pilots flew one or both of these helicopters before transitioning to the Super Puma, it's no wonder that this causes difficulty.

Most of the time landing lights are not needed until short final when they need to be positioned quickly and accurately. When the light moves in the opposite direction from what is expected, it's not only irritating, but potentially dangerous as well.

As a rule, moveable landing and search lights should move up when the switch is pushed up and move down when the switch is pushed down.

# Intercom Switching

The pilot's and co-pilot's intercom switches are two-position switches, "NORM" and "EMER". In the normal position, the voice-actuated system

works, which is an extremely good system to use. The emergency position is there in case the normal power supply to the system is lost. When in "EMER," the pilots have to key the microphone switches on the cyclics or the intercom control panel in order to talk to each other.

The intercom system would be better if the need to switch to "EMER" in case of a normal supply failure were eliminated. In other words, once the pilots discover that the voice-actuated system no longer works, all they have to do is use the cyclic or panel microphone switches.

Trouble-shooting an electrical fire is one emergency when the emergency intercom system is needed. Various electrical suppliers must be switched off, including the normal power supply to the intercom and the autopilot. One pilot must therefore concentrate exclusively on flying while the other pilot is trying to isolate the fire. This is no time for communication difficulties. Requiring both pilots to switch to "EMER" just adds an additional burden and stress factor to the emergency.

# SOFTWARE FACTORS OF THE AS332L-1 COCKPIT

# General

As noted before, software factors include many items, all of them concerned with information. Often, good, well-designed operating procedures and checklists can make up for design faults in the aircraft. For example, with reference to the flashing "OVSPD" light problem, Helikopter Service has a prominent note in the company Emergency Checklist under "Engine Malfunctions," stating that a failed engine should not be re-started if the "OVSPD" light is flashing.

It is not the intention of this paper to try to examine the flight manual, operating procedures, and all other information sources about the Super Puma, but rather to limit the discussion to the information presented to the pilot in the cockpit. In the author's opinion, the "AS332L-1 Super Puma Instruction Manual" is is very well written. However, there are two main problems with the

manual, which also apply to the cockpit indications. The first is the occasional inconsistency among terms and the second is occasional poor translations from French to English, including abbreviations. These two problems are probably related in many instances.[6]

An example of the first is the use of both "generator" and "alternator" to describe the same thing in the electrical system. Examples of the second type of problems, translations and abbreviations, are discussed below.

# "MGB COOL" Warning Light

The Super Puma main gear box has two lubrication pumps, a normal one and an emergency one. Both pumps are essentially the same and both run continuously. The main differences are (1) the main pump delivers a slightly higher pressure, (2) the input to the emergency pump is positioned below the input to main pump, and (3) the emergency pump system bypasses the transmission oil cooler.

If the main pump stops delivering oil, either due to a leak in the system or failure of the pump itself, the emergency pump will continue to supply oil to the main gear box. The emergency pump bypasses the transmission oil cooler because a leak in the system will most likely be in the plumbing to the oil cooler. The emergency pump lubricates everything in the main gear box, but the oil is no longer cooled. As a consequence, one can expect a gradual rise in transmission oil temperature with a failure of the main pump or a leak.

It's obviously important to warn the pilot that this has happened and the "MGB COOL" light (Fig. 6, #6) serves this function. It is triggered by a pressure switch which senses the drop in pressure in the line downstream of the oil cooler.

The theory is very good and the light works in practice, but the language on the light creates confusion. "MGB COOL" does not mean that the MGB is now cool or will become cool. Quite to the contrary, the oil will now become hotter. Nor

图片摘要：该图主要展示 6. Main gear box lubrication system。
![](images/643e91fbad15a82c8fcafdf3f600ff273013acf20368d6c14dad34aa1d33c2db.jpg)  
FIGURE 6. Main gear box lubrication system.

does the light mean that the MGB cooler has failed. If the cooler fails, due to a broken drive shaft or shattered fan blades (both of which have happened a number of times), the "MGB COOL" light does not illuminate; what one sees is a rise in MGB temperature and, eventually, a "MGB TEMP" warning light. "MGB COOL" means that the MGB cooler has been bypassed. This is not, however, the most important thing the pilot needs to know at this point, even if he does remember what the light signifies.

The important thing is that the main pump is no longer delivering oil to the system, either because of a failure or a leakage. Therefore, it would seem to make more sense for the light to be labelled so that it better conveys this information, for example, "MGB PUMP." The point is: The wording used on warning lights must be carefully chosen so that the most critical factor of a given malfunction is immediately comprehended.

# Hydraulic Panel

The labelling on the hydraulic panel is particularly confusing, even to pilots who have flown the Super Puma for many years (Fig. 7A & 7B). The problem is that the abbreviations are not consistent and this was a result of translating abbreviations from French to English.

图片摘要：该图主要展示 7A. Hydraulic panel with French abbreviations。
![](images/7ca1583f9d58251a2fc46691b9849a080b531bfd660a285e0435bc5a1f76b010.jpg)  
FIGURE 7A. Hydraulic panel with French abbreviations.

The culprits on the English switches are the letters "P" and "H." On some of the switches, the letter "P" stands for "pump" and on other switches it stands for "pressure." On every switch "P" appears, it could logically stand for either "pump" or "pressure."

On some of the switches, the letter "H" stands for "hand" and on others it stands for "hydraulic." On many of the switches, "H" could stand for either "hand" or "hydraulic." On one switch, "H" stands for both "hand" and "hydraulic."

The correct meanings are as follows:

$$
\mathbf {L H . P} = \text {L E F T H A N D P R E S S U R E (l o w)}
$$

$$
\mathbf {L H . L E V} = \text {L E F T H A N D L E V E L} (\text {l o w})
$$

LH.H.MP = LEFT HAND HYDRAULIC MAIN PUMP (failure)

AP.H.P = AUTOPILOT HYDRAULIC PRESSURE (low)

AUX.HP = AUXILIARY HYDRAULIC PRESSURE (low)

$$
\mathbf {A U X . P} = \text {A U X I L I A R Y P U M P (f a i l u r e)}
$$

$$
A U X. P = A U X I L I A R Y P U M P (o n / o f f s w i t c h)
$$

$$
\mathbf {R H . P} = \text {R I G H T H A N D P R E S S U R E (l o w)}
$$

$$
R H. L E V = R I G H T H A N D L E V E L (l o w)
$$

图片摘要：该图主要展示 7B. Hydraulic panel with English abbreviations。
![](images/ee21f103843801cab45b58c20ce0e5f3b32a4b32373f26315a2ddf66ef417001.jpg)  
FIGURE 7B. Hydraulic panel with English abbreviations.

It's easy to understand how this creates confusion. Anything that does this, particularly during an emergency, is going to increase the stress level and the chances for mistakes. The lesson is obvious: Make all abbreviations readily understandable and consistent.

# "THROT" Light

This light indicates that one or both of the fuel flow control levers (FFCL) is not in the "FLIGHT" position, where they normally should be if they are working normally. It's a useful light with an engine failure and subsequent shut-down because it is the only warning light that remains illuminated after the FFCL has been set in the shut-off position. (The "DIFF NG" and "PRESS 1" or "PRESS 2" lights extinguish when the FFCL is in the shut-off position.)

But why is it called the "THROT" light, and not, for example, the "FFCL" light? The term "throttle" is not used anywhere in the Instruction Manual or the Flight Manual. The proper term is "Fuel Flow Control Lever." The use of the word "throttle" and its abbreviation "THROT" is, perhaps, either a carry-over from the days when most helicopters had reciprocating engines and, therefore, throttles (admittedly, some still do) or perhaps it's just another translation problem from French to English.

The point is: Consistency. Items should always be referred to by the same correct name, both in the flight manual and in the cockpit.

# Autopilot Panel

The hardware aspects of the autopilot were discussed previously. The software aspects of the panel are actually quite good, with only a few minor exceptions.

To test the basic autopilot system, one moves the test switch from "TEST" to "RUN," meaning, apparently, that one is "running the test."

On the other hand, to test the collective part of the autopilot (the fourth-axis), one moves the test switch from "NORMAL" to "TEST."

Again, it's a small point, but one that is easily corrected.

# "RB.SAFE" and "ROT.BR" Lights

The Super Puma has a two-lever rotor

brake system with a rotor brake safe lever and a rotor brake lever. It is possible to move the rotor brake lever to the braking position in flight (which obviously should not be done), but it will do nothing more than cause the "ROT.BR" light to illuminate (Fig. 8). Hydraulic pressure to the rotor brake is obtained only when both levers are pushed forward, a sensible system which just about guarantees that the rotor brake won't be engaged inadvertently at the wrong time.

图片摘要：该图主要展示 8. "RB.SAFE" AND "ROT.BR" lights。
![](images/11b80d5bc82c9daee81b903e548018882559c95005b6e0519f25545bc60851b0.jpg)  
FIGURE 8. "RB.SAFE" AND "ROT.BR" lights

"RB. SAFE" means that the rotor brake safety lever is in the forward position, not, as one may be lead to suspect, that the rotor brake is safe. Actually, one could argue that with the safety lever in the forward position, the rotor brake system is unsafe because, now, if the rotor brake lever is moved forward, braking pressure will be applied to the rotor system. In effect, moving the rotor brake safety lever forward arms the rotor brake system.

So why not label the "RB. SAFE" light "RB ARM?" One could also change the "ROT.BR" light to "RB ON" to make the abbreviation of "rotor brake" consistent.

# Heater Distributor Valve Control

The heater has a three-position distributor valve control lever so that the pilots can choose where they want the heat directed. In the forward position, the heat is divided between the cockpit and the autopilot; in the middle position, heat goes to the cockpit, the autopilot, and the cabin; in the aft position, all heat distribution to the aircraft is cut off. The problem with the heater lies in the

fact that the distributor valve control lever has been poorly labelled.

The forward position is labelled "COCKPIT POSTE PILOTE." This looks like a blending of English and French -- it probably means the cockpit will be heated. But it says nothing about the autopilot which is also heated.

The middle position is labelled "O." A person who knows a little French might conclude that "O" is an abbreviation for "ouvert" which means "open." But what is being heated with the switch open? There's no way to determine this from the labelling of the switch. On the other hand, a person who knows no French might think the "O" (oh) is a "0" (zero) and that it means the heater is off or closed.

The aft position is labelled vertically "F C." Again, a French speaker might assume the "F" stands for "ferme" which means "closed" and the "C" might be an English abbreviation for "closed." Then again, both letters could be either French abbreviations or English abbreviations. It's very hard to tell.

This may seem like a small thing again; after all, it's only the heater switch. But it is also confusing, annoying, and totally unnecessary. With only a bit more thought and effort, the lever could have been labelled so that the function of the three positions were obvious.

# SPURIOUSWARNINGS

As was mentioned before concerning the "CPL" light illuminating every time a coupler function is switched off, continuous unnecessary warnings eventually are ignored. Complacency with respect to the warning is the result. In some aircraft, pilots have gone so far as to pull circuit breakers for certain specific warning lights because they were so prone to false warnings. MGB chip warning lights are notorious examples.

Sophisticated electronic systems seem to be all too prone to spurious warnings. The numerous

landing gear position switches in the Super Puma are particularly sensitive, and if it weren't for the aircraft's emergency electrical and hydraulic extension possibilities, there would be a lot of gear-up landings at Helikopter Service. These switches are not, however, just a problem for the landing gear, but also for all the auxiliary equipment which receive "GROUND" or "FLIGHT" signals from these same switches.

For example, a common problem with the Super Puma is for the area navigation system (be it VLF/OMEGA, DECCA, LORAN, or whatever) to "freeze up" in flight. The solution is to re-cycle the landing gear. The cause is the loss of the "FLIGHT" signal to the area nav system because one of the landing gear has moved out of position far enough to open a switch which should have been closed.

Another related problem concerns the autopilot. Once the author found it impossible to run the autopilot test, even though the switch was moved from "TEST" to "RUN" several times. All the functions worked, but the test just wouldn't run. A mechanic was notified and he immediately realized the problem was a position switch in the nose gear. He grabbed a tow bar, jiggled the nose wheel, and the autopilot test worked as designed.

Incorrect fire warning system tests during start-up are another headache. Mechanics have changed system control cards, wiring harnesses, and fire detectors, but usually the problem is simply moisture. Most of the time the system will test properly after the engines are started and everything is allowed to warm up and dry out.

The point is that pilots quickly loose faith in a warning system if it continually gives false warnings. When a warning system cries "Wolf!" all the time when there is no wolf, the one time there really is a wolf at the door, it may be ignored. The increased use of electronics and computers in helicopters promises numerous advantages for the pilots, but the systems must be constructed so that they are not adversely affected by the environment.

# FUTURE CONSIDERATIONS

"New technologies incorporating multiple redundancy and fail-safe concepts are becoming so reliable that, in future years, the proportion of human factor accidents may reach 100 percent simply because the total, irrecoverable failure of machine components of the man-aircraft system will be eliminated."

Dr. Robert B. Lee

Australian Bureau of Air Safety

Investigation

"The Space Invader-playing kids of today will be the fighter and bomber pilots of tomorrow."

Ronald Reagan

40th President of the United States

Even though former President Reagan didn't mention helicopter pilots in the above quote, they certainly must be included. What is just as certain is that his prediction is already coming true.

How will this effect human factor problems in the cockpit?

Not more than ten or fifteen years ago, the space and aircraft industries were the epitome of high-tech. In many ways, they still are, but since the advent of inexpensive micro-chips, "smart" machines are now commonplace in most homes. Today, the gap between sophisticated aircraft and sophisticated household machines has narrowed. Entire houses can now be controlled by a central computer. In late 1988, the Electronic Industries Association/Consumer Electronics Group announced a new wiring standard called the Consumer Electronics Bus which will enable microprocessor-equipped appliances built by one company to communicate with those built by another.[8]

This means that more and more people will use sophisticated electronic and computer-controlled devices on a daily basis. Today, many children learn to operate machines even before they can read. At age four, the author's youngest son knew how to operate the remote controls of a video cassette recorder and television, find and play games on a Macintosh computer, use various

cassette players, and heat food in a microwave oven. Operating machines is second nature to him.

Aircraft designers will have a new human factor element to consider. Instead of the automobile, electronic, and other industries mimicking the designs of equipment found in aircraft, the aircraft manufacturers may find themselves copying panel designs from these industries in order to avoid human factor problems in the cockpit. This is not to say that aircraft will loose their place on the cutting edge of technology, but that aircraft designers will have to be more aware of the designs of equipment made by other industries.

For example, affordable, hand-held GPS systems are now available for less than $1000 from a number of manufacturers. It won't be long before a dashboard-mounted GPS becomes a common option in automobiles and trucks. If the GPS receivers pilots find in their aircraft are very dissimilar from these car systems and hand-helds, human factor errors will occur.

In the past, pilots had to contend with transfer of learning problems between their airplanes and their automobiles. These problems will seem minor to the pilots of future generations who will have to contend with transfer of learning problems between their aircraft and their cars, their computers, their home entertainment systems, and numerous other gadgets, appliances, and machines, some of which have yet to be invented.

There will be international "standards" developed and accepted, sometimes by agreements and official decrees, but perhaps more often by the company that is able to sell the most of a particular product first. If a similar machine does not fit the accepted "norm" or the standard that people have become accustomed to, problems will arise.

A human factors problem occurred when Helikopter Service installed a new security system in the main office and hanger. Like the old system, the new one required the use of magnetic-strip identity cards. The old system required one to insert the card in the controller and punch in a four-digit code before the door would open. The new system required that the code be punched in first,

then the card inserted. If the card was inserted first and then the code punched in, as with the old system, a red light blinked indicating something was wrong.

On the first day, hardly anyone could get into the building. Even though instructions had been distributed beforehand, few bothered to read them, assuming wrongly that the new system worked the same way as the old one. Most people thought there was something wrong with their card or their code. The problem was the system itself; the fault was that of the engineer who had not realized that a "standard" for card-and-code door opening systems had already been established at the company.

There may have to be a radical change in the way aircraft are designed. In the past, the machine was foremost. The goal was to make the machine work and if a switch or lever was in an awkward position for the pilot, then he just had to adapt to it. Fortunately, this attitude has changed a great deal since World War II and aircraft designers spend much more attention to ergonomic factors inside the cockpit.

In the future, however, designers will also have to look outside the cockpit, at the numerous other sophisticated machines that are becoming or are already commonplace, when considering human factors problems.

Everything in the cockpit will have to be considered in this light. From the simplest mechanical things, such as the way the seats are adjusted, to the most sophisticated computer-driven systems. Designers will have to stay up-to-date with currently accepted standards in the "outside world." Are computer pull-down menus and "windows" so widespread that they should be considered standards to be used in the cockpit? Should the "QWERTY" keyboard found on typewriters or the keypad used on touch-tone telephones be the standard for aircraft navigation and computer systems? Should the clock be digital or analog, or both? Should the artificial feel in a fly-by-wire control stick have the same "feel" as a Nintendo joystick? These are the kinds of questions that must be constantly and continually asked.

To help answer questions like these, manufacturers must establish, promote, and use an effective feedback system so that ideas and suggestions from line pilots in the field can be obtained on a regular basis.

Every successful company believes it is "the man on the shop floor" who best knows how to do his job and who has the most useful suggestions about how to do it better. Good companies solicit information from every level.

In the author's experience, aviation companies are often very conservative and many even have military-like organizations. Information in military hierarchies goes up and down the chain of command, although it usually flows down a lot easier than it goes up. If the chief pilot or chief of maintenance does not agree with a line pilot's or mechanic's suggestion, the idea stops there and never gets to the manufacturer where it might have been accepted. The only exception is in the case of an accident. Then people are listened to.

A reporting system connecting line pilots directly to manufacturers would be an excellent way to get feedback about present and future cockpits.[11]

# CONCLUSIONS

The author readily concedes the subjective nature of this paper. However, given the fact that the very nature of the applied technology of human factors presupposes a degree of subjectivity, the author hopes his departure from the scientific method will not cause his conclusions to be summarily disregarded. In lieu of a feedback system described above, a forum such as this is one of the few ways a line pilot can make his observations and opinions known to people who can make a difference.

1. Flashing warning lights should only be used for the most serious of malfunctions; taking the proper corrective action and removing the hazard, should be the only possible way to extinguish a flashing warning light.
