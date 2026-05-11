# Handling Qualities Optimization for Rotorcraft Conceptual Design

# Ben Lawrence

San Jose State University

NASA Ames Research Center

# Colin Theodore

# Wayne Johnson

National Aeronautics and Space Administration

NASA Ames Research Center

# Tom Berger

U.S. Army Aviation Development Directorate

Moffett Field

Rotorcraft Virtual Engineering Conference,

Liverpool, UK

November 8-10, 2016

# NASA Revolutionary Vertical Lift Technology Project (RVLT)

# Develop and Validate Tools, Technologies and Concepts to Overcome Key Barriers for Vertical Lift Vehicles

# Vision

Enable next generation of vehicles to expand capabilities and develop commercial markets with technologies for noise, speed, safety, mobility, payload, efficiency, environment

# Scope

Spectrum of configurations from very light (UAS) to ultra-heavy (transport size)

# Conceptual Design Tool Development

Developing an OpenMDAO framework to integrate discipline analyses: Sizing, propulsion, acoustics, structural loads and handli

图片摘要：该图片与High fidelity, validated CFD；Noise Modeling这部分内容相关。
![](images/f01c9afe1f9c60a04a88c73865c71ba1790ebca118221e2ed20da9f00b5c1035.jpg)  
High-fidelity, validated CFD

图片摘要：该图片与Noise Modeling；Handling Qualities in Conceptual Design这部分内容相关。
![](images/369305e96aa969dfcfdc65f79ecd2e701e78041bd25d2ec5679c86e7c6bcf159.jpg)

图片摘要：该图片与Noise Modeling；Handling Qualities in Conceptual Design这部分内容相关。
![](images/491032904f69d762c6f8301a906ff2bbe847054eb93f95ca0218b3cf4e374ea3.jpg)

图片摘要：该图片与Noise Modeling；Handling Qualities in Conceptual Design这部分内容相关。
![](images/3231b6a32c5e8fd42ec97ea2cd842983dd33d01ed8ad191d9fc827f41cc2921e.jpg)  
Noise Modeling

# Handling Qualities in Conceptual Design

# R£Df $IGN

# I$ £xpEn$ive

图片摘要：该图片与†Padfield, G. D., 1988. and 2012；Stability, control and handling qualities (HQ) 这部分内容相关。
![](images/6e8d831ac3fa2583365dfbf491cd1755c3e6facf3547953d3a7fa189a8deacec.jpg)

图片摘要：该图片与†Padfield, G. D., 1988. and 2012；Stability, control and handling qualities (HQ) 这部分内容相关。
![](images/98915c256f3a38bb68d3ae54bc3945b936bccd70a2ebd992ecda481c0faa95ea.jpg)

†Padfield, G. D., 1988. and 2012

图片摘要：该图片与Stability, control and handling qualities (HQ) historically given little attenti这部分内容相关。
![](images/1a43d2929eea85341ed4c6f60c82276f7888aa62a9fcf9ccb8b4dec9a8a280fe.jpg)

Stability, control and handling qualities (HQ) historically given little attention in conceptual design

– “not given their proper place in the early design tradespace, and often left until flight test to discover and ‘put right’”†

– Weight savings by addressing over-design

Development of toolset: “SIMPLI-FLYD”

Exploring HQ in conceptual design

– integrate in a MDAO framework

SIMPLI-FLYD   
– CONDUIT optimization and HQ design margins   
• NDARC/SIMPLI-FLYD coupling   
• Results

– Tiltrotor   
– Helicopter

Lessons learned   
Future developments

• “SIMPLIfied FLight dYnamics for conceptual Design”

– NASA/U.S. Army collaboration   
NDARC: NASA Design and Analysis of RotorCraft

Automated process that:

• Calculates linear flight dynamics models   
• Integrates control system optimization for roll, pitch, vertical and yaw response axes   
• Calculates stability and control parameters for handling qualities metrics   
• Generates a real-time flight dynamics and control model for piloted simulation in X-Plane

图片摘要：该图片与Full authority fly by wire；Model following architecture这部分内容相关。
![](images/ca821ab1da7063f2fb460703685e5f9e8cb8d30e4fc62f0001e357209376bdb2.jpg)

Full-authority fly-by-wire   
Model-following architecture

Generic architecture that can applied to multiple vehicle configurations   
Feedback to stabilize, provide gust rejection   
Feed-forward for piloted response, command shaping

图片摘要：该图片与Appropriate piloted response types chosen automatically based on flight regime；C这部分内容相关。
![](images/2bfe32d36cc32bd862dd265bbcd6c700867ea1b44be02beab279bc1b380961d7.jpg)

Appropriate piloted response types chosen automatically based on flight regime   
Control system gains need to be optimized

<table><tr><td></td><td colspan="2">Rotor-Borne</td><td>Wing-Borne</td></tr><tr><td></td><td>Hover</td><td>Forward-Flight</td><td>Forward-Flight</td></tr><tr><td>Roll</td><td>RCAH</td><td>RCAH</td><td>RCAH</td></tr><tr><td>Pitch</td><td>RCAH</td><td>RCAH</td><td>Angle-of-Attack-
Command</td></tr><tr><td>Yaw</td><td>RCDH</td><td>Sideslip-
Command</td><td>Sideslip-
Command</td></tr><tr><td>Thrust</td><td>RCHH</td><td>Open-loop</td><td>Open-loop</td></tr></table>

RCAH $=$ Rate-Command/Attitude-Hold

RCDH $=$ Rate-Command/Direction-Hold

RCHH $=$ Rate-Command/Height-Hold

# Control System Optimization - CONDUIT

Control Designer’s Unified Interface (CONDUIT®)   
Optimizes control system parameters to meet handling qualities specifications   
Automatic selection of different specification sets from ADS-33E and MIL-STD-1797B criteria for control optimization 17 to 23 specs per axis   
Design margin

% over-/under-design based on ability of aircraft to meet metrics in each axis

• $0 \%$ Just meets Level 1   
• -100% on Level 2/3 boundary

Most limiting specification determines design margin for each axis – 2 per axis

图片摘要：该图片与ADS 33E；MIL STD 1797B这部分内容相关。
![](images/33b5e7943d9f958dfde2bc72fcf21a8f4697fa157be12823cd102b64e122a2e9.jpg)  
ADS-33E

图片摘要：该图片与MIL STD 1797B；Piloted Bandwidth这部分内容相关。
![](images/31bbd34b87365c2156bb3684612bf90ec7f54d928e40e3ea60588d215c4c4d0f.jpg)  
MIL-STD-1797B

图片摘要：该图片与Piloted Bandwidth；Handling qualities levels这部分内容相关。
![](images/afde017cb7305b0503ab4924426ea5a4345479252b191c94b3ff4a59fbd5ead5.jpg)  
Piloted Bandwidth   
Handling qualities levels

■Level 1 - Good   
■Level 2 - Adequate   
■Level 3 - Unsatisfactory

# Objectives and example cases

• Evaluate NDARC/SIMPLI-FLYD coupled analysis to explore handling qualities in conceptual design   
• Example aircraft/HQ scenarios chosen:

– NDARC models with typical missions for sizing task   
– Varied a mix of design and actuator parameters

Tiltrotor pitch axis

– Forward flight only   
– Varied horizontal tail size, location, flap area ratio, actuator rate limit

• Single Main Rotor (SMR) helicopter yaw axis

– Hover & forward flight   
– Varied tail rotor size, location, collective actuator bandwidth and rate limit

图片摘要：该图片与PYTHON；• NDARC sizes aircraft for design mission这部分内容相关。
![](images/0d58b4b95dad1a9a70733cc808dcbb324030e0659db3d7eb155394cf428733e4.jpg)  
PYTHON

• NDARC sizes aircraft for design mission   
Python scripting used to integrate NDARC and SIMPLI-FLYD in single process   
• Design parameter, actuator characteristic and flight condition sweeps   
• Outputs:

CONDUIT computed HQ Design Margins   
– NDARC empty weight

Moments of inertia derived from fixed radii of gyration and weight

# Handling Qualities Design Margin Data

图片摘要：该图片与Tail area =25.25ft2；PITCH AXIS这部分内容相关。
![](images/83120f7adb53aa265e7acb4bb300a93e9a6f15537052c7de3a1d0fa0862c7867.jpg)

图片摘要：该图片与Tail area =25.25ft2；PITCH AXIS这部分内容相关。
![](images/c3d7a1efdc808d52ae33823d6abb0e340d5b06a5b5febfe126db7be97df36f3f.jpg)

图片摘要：该图片与Tail area =25.25ft2；PITCH AXIS这部分内容相关。
![](images/75037a71cf497a7d46edf44b75929be2b1dec3b52467b3151c23276fb1066d2e.jpg)

图片摘要：该图片与Tail area =25.25ft2；PITCH AXIS这部分内容相关。
![](images/85c617aa39806330546ddcf58d6996f00fa3132ea4656b56e6b1b8fc519aff06.jpg)  
Tail area =25.25ft2   
PITCH AXIS   
160 [kts]

图片摘要：该图片与Design Margin [%]；Handling Qualities Design Margin Data这部分内容相关。
![](images/02b2e17efd61b16dd1a0acf411fa6658b542de0852daff1d758512ad8e71dcb5.jpg)  
Design Margin [%]

# Handling Qualities Design Margin Data

Compact visualization of 3-D/4-D data   
Primary intent is to illustrate trends and sensitivities

图片摘要：该图片与Tiltrotor Pitch Axis HQ Introduction；Feed forward这部分内容相关。
![](images/afde1b4b3ef0eda003cf2b02647aa74e65213d3c5fabbbd9c0ff64d1253b05a3.jpg)

# Tiltrotor Pitch Axis HQ - Introduction

Feed-forward:

– Maneuver response

Feedback:

Stabilization, disturbance rejection

Tail size varied at constant Aspect Ratio   
Elevator flap area ratio:

– 1.0 = all moving tail   
– 0.0 = no flap

Elevator flap control actuator rate limit

图片摘要：该图片与PITCH AXIS；Tiltrotor Pitch Axis HQ – Effect of Speed这部分内容相关。
![](images/3992da78ba75931c04735fe8bdb503047c46125c198d93ff5d4e2a3cb407fb86.jpg)  
PITCH AXIS

图片摘要：该图片与Tiltrotor Pitch Axis HQ – Effect of Speed；PITCH AXIS这部分内容相关。
![](images/a3101235d2582a8b37749ea882825c888a32bee5d9edb9f90b5b86463a40becd.jpg)

# Tiltrotor Pitch Axis HQ – Effect of Speed

# PITCH AXIS

图片摘要：该图片与PITCH AXIS；Tiltrotor Pitch Axis HQ – Effect of Speed这部分内容相关。
![](images/7cc623adcc1315618d270703a6d6ec880220111fc31fe1a1bc68850ba151fbab.jpg)

图片摘要：该图片与PITCH AXIS；Tiltrotor Pitch Axis HQ – Effect of Speed这部分内容相关。
![](images/5d64937e914176c40760f092b4470a94d670b79e69a055fb1e026e1684928abb.jpg)

图片摘要：该图片与300 ktsPITCH AXIS Tiltrotor Pitch Axis HQ – Effect of Speed这部分内容相关。
![](images/812a970171cf7583e1c306026a72662a901517649d3bb4f6055bda7c51283aba.jpg)

图片摘要：该图片与300 kts；230 kts这部分内容相关。
![](images/e6914cc709c4a53d277fe1bfc61dedbb88d20564f78a09da1e20e050b67c9890.jpg)

图片摘要：该图片与300 kts；230 kts这部分内容相关。
![](images/54c7bf5431a5193fdadf0b177fac93c790cbd01978ca26ecc5708a8fb3c988ce.jpg)

图片摘要：该图片与300 kts；230 kts这部分内容相关。
![](images/e266f67e4d4630767f58ee4ba47d2e3e2be5e91df871f69ee023e41c1dcffd4e.jpg)

300 kts

230 kts

160kts

Reducing Speed

Low airspeed is critical for sizing tail but important to check whole envelope

# Tiltrotor Pitch Axis HQ vs. Empty Weight

图片摘要：该图片与160kts；Tradeoff between minimum weight and handling qualities constraints这部分内容相关。
![](images/1dfedf7053b82f381716d613948bf6d3a1b6e2c96d88b4281f0675775d1b5129.jpg)

图片摘要：该图片与160kts；Tradeoff between minimum weight and handling qualities constraints这部分内容相关。
![](images/9630b31b9e8d7a341ed0000d5039dfbffd698bc012dc055e945d5670a2993305.jpg)  
160kts

图片摘要：该图片与Tradeoff between minimum weight and handling qualities constraints；Tiltrotor Pit这部分内容相关。
![](images/07005d3a423cbf541f855c924eb6036770351dd7e15622170218e3efbdf605e5.jpg)

Tradeoff between minimum weight and handling qualities constraints

# Tiltrotor Pitch Axis HQ – Tail length Variation

图片摘要：该图片与Rate limit = 20 deg/s, Tail length varied；160kts这部分内容相关。
![](images/e8df1067259c3d8b662f66b043cf7035ce33d623bdddefab91d143d6b155dc79.jpg)  
Rate limit = 20 deg/s, Tail length varied

图片摘要：该图片与160kts；Tradeoff between minimum weight and handling qualities constraints这部分内容相关。
![](images/d8bb3e5982747992d69798f0ab095480ffa7b078a824a403eca29441d21cd673.jpg)  
160kts

图片摘要：该图片与Tradeoff between minimum weight and handling qualities constraints；Single Main R这部分内容相关。
![](images/56130f26b5406c12ce826ef917316cf6038902ac99f4a7ca76e8dea7cdf90e08.jpg)

Tradeoff between minimum weight and handling qualities constraints

# Single Main Rotor Yaw Axis HQ - Introduction

Tail rotor size varied at constant solidity and tip speed   
Tail rotor longitudinal location   
Actuator bandwidth limit for tail rotor collective   
Region of no data for non-converged NDARC cases

图片摘要：该图片与Single Main Rotor Yaw Axis HQ – Effect of SpeedRegion of no data for non converg这部分内容相关。
![](images/129ffa2d83aa5b130ad9adcd74049aab6a66a6dea83795426093e0e78e0b250d.jpg)

图片摘要：该图片与Single Main Rotor Yaw Axis HQ – Effect of SpeedRegion of no data for non converg这部分内容相关。
![](images/d130c6c8f43022254d55a6a7d100326dcde857a045b1313bec67945fb4859071.jpg)

# Single Main Rotor Yaw Axis HQ – Effect of Speed

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/29fdbdb1a64b0a81758a531783265575e7f8ee1e92dd204f43e2f9ec9c650905.jpg)

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/875aa7f96d11c0161805467ddcb39e6a261880517802249acf8e0e906c39c288.jpg)

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/f12fb601ea9194ac0b4db461b0756dcb8bf7a164d5c3cd03c992811a499c2187.jpg)

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/fcfd0d0e7683432e155e6b14cc986ae395a41db1eeef36868ed007f004b6de41.jpg)  
0 kts(hover)  
80 kts

Speed change includes change of control mode and HQ spec requirements

# Single Main Rotor Yaw Axis HQ – Larger Tail Rotors

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/03bc1ceb429000dce9ab40f3b2a974d15bfc20926bbaa79741384a36e1ffe4e7.jpg)

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/2ac17fdcf554819d597d9b2bd1a8bd811c74c3ffb616e12971872be765e00fc9.jpg)

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/5709169245cdf8bc295c4077cbab41a5989a582bb94834e378e79945408c3c09.jpg)

图片摘要：该图片与0 kts(hover)；80 kts这部分内容相关。
![](images/14857ef60bd16c29330bf7bf4ddcd0afc7d0aa8703703436415462ef2863ba30.jpg)  
0 kts(hover)  
80 kts

# Increasing Speed

# Single Main Rotor – Empty Weight

图片摘要：该图片与Lessons Learned From Application Of The Tools；• Handling qualities vary with fli这部分内容相关。
![](images/f23de4da9b541277c7aa58ae34eca94b6109636101c6d33349371c04744cb394.jpg)

图片摘要：该图片与Lessons Learned From Application Of The Tools；• Handling qualities vary with fli这部分内容相关。
![](images/e4f110796b15c0da1f338e0319b67bd49821bf65049160b17c896d69e5c847ff.jpg)

# Lessons Learned From Application Of The Tools

• Handling qualities vary with flight condition:

– Due to different characteristics and different HQ requirements   
– CONDUIT Design Margin helps to provide a consistent metric

• Actuator characteristics important factor   
– “Cost” (weight) needs to be accounted for in design   
• Inertia modeling probably not sensitive enough to design changes relevant to HQs   
• Ensuring geometry “consistency” also important   
• Current SIMPLI-FLYD process approx. 15-20 min per flight condition

# OpenVSP and ALPINE

OpenVSP is a 3D geometry tool with focus on conceptual design   
ALPINE tool (Automated Layout with Python Integrated NDARC Environment) developed by US Army ADD to generate OpenVSP models from NDARC output

OpenVSP sub functions:

mass properties tool offers a higher resolution prediction of moments of inertia   
– Integration plans underway

OpenVSP offers possibilities to addre geometry management

图片摘要：该图片与• Current SIMPLI FLYD process approx. 15 20 min per flight condition；• CONDUIT o这部分内容相关。
![](images/8a74de63fd8ff85225cdef201392462156357d42addf708ed26bbf8c80979ffc.jpg)

图片摘要：该图片与• Current SIMPLI FLYD process approx. 15 20 min per flight condition；• CONDUIT o这部分内容相关。
![](images/3077f21279cc2bf9b53e8f41d2ed47e77b37d7417e6e70adcfc38aea95966537.jpg)

• Current SIMPLI-FLYD process approx. 15-20 min per flight condition   
• CONDUIT optimization main computational cost   
• NDARC/SIMPLI-FLYD process is sequence of parameter reductions   
Many sub-stage parameter sets faster to compute   
• Stability and control derivative sensitivity study example (in paper)

• Coupled NDARC/SIMPLI-FLYD analysis to examine:

– Different vehicle types   
– Mix of design parameters and flight conditions   
– Different handling qualities problems

Future Developments:

– OpenMDAO integration – tradeoffs with other disciplines   
– Inertia modeling – ALPINE integration   
– Actuator modeling – weight/cost, greater fidelity   
– Other configurations – e.g. rotor interference   
– Computational requirements – SIMPLI-FLYD role in conceptual design

# Questions?
