# SYSTEM DYNAMIC ANALYSIS OF A WIND TUNNEL MODEL WITH

# APPLICATIONS TO IMPROVE AERODYNAMIC DATA QUALITY

A Dissertation submitted to the

Division of Research and Advanced Studies of the University of Cincinnati

in partial fulfillment of the requirements for the degree of

DOCTOR OF PHILOSOPHY

in the Department of Mechanical, Industrial, and Nuclear Engineering of the College of Engineering

1997

by

Ralph David Buehrle

B.S.M.E., University of Akron 1985  
M.S.M.E., University of Cincinnati 1988

Committee Chair: Randall J. Allemang, Ph.D.

# SYSTEM DYNAMIC ANALYSIS OF A WIND TUNNEL MODEL WITH APPLICATIONS TO IMPROVE AERODYNAMIC DATA QUALITY

# ABSTRACT

The research investigates the effect of wind tunnel model system dynamics on measured aerodynamic data. During wind tunnel tests designed to obtain lift and drag data, the required aerodynamic measurements are the steady-state balance forces and moments, pressures, and model attitude. However, the wind tunnel model system can be subjected to unsteady aerodynamic and inertial loads which result in oscillatory translations and angular rotations. The steady-state force balance and inertial model attitude measurements are obtained by filtering and averaging data taken during conditions of high model vibrations. The main goals of this research are to characterize the effects of model system dynamics on the measured steady-state aerodynamic data and develop a correction technique to compensate for dynamically induced errors. Equations of motion are formulated for the dynamic response of the model system subjected to arbitrary aerodynamic and inertial inputs. The resulting modal model is examined to study the effects of the model system dynamic response on the aerodynamic data. In particular, the equations of motion are used to describe the effect of dynamics on the inertial model attitude, or angle of attack, measurement system that is used routinely at the NASA Langley Research Center and other wind tunnel facilities throughout the world. This activity was prompted by the inertial model attitude sensor response observed during high levels of model vibration while testing in the National Transonic Facility at the NASA

Langley Research Center. The inertial attitude sensor cannot distinguish between the gravitational acceleration and centrifugal accelerations associated with wind tunnel model system vibration, which results in a model attitude measurement bias error. Bias errors over an order of magnitude greater than the required device accuracy were found in the inertial model attitude measurements during dynamic testing of two model systems. Based on a theoretical modal approach, a method using measured vibration amplitudes and measured or calculated modal characteristics of the model system is developed to correct for dynamic bias errors in the model attitude measurements. The correction method is verified through dynamic response tests on two model systems and actual wind tunnel test data.

# ACKNOWLEDGMENTS

I wish to thank my adviser, Dr. Randall J. Allemang, and my graduate review committee, Dr. Dave Brown, and Dr. Robert Rost, for their guidance and support. I am especially grateful to Dr. Clarence P. Young, Jr. for his technical review of this document and his advice during this research program. I thank my NASA supervisors, Mr. Richard A. Foss, Dr. William F. Hunter, Dr. William S. Lassiter, Mr. Melvin H. Lucy, and Mr. William F. Fernald, for their encouragement during my Ph.D. studies. I would also like to thank Mrs. Genevieve Dixon of the NASA Langley Research Center for assistance in the finite element modeling area. Finally, I would like to thank my wife, Barbara, and children, Bridget, Joseph and Blaine, for their patience and understanding during my studies. This work was completed under the NASA research program, RTR 274-00-95-01, entitled "Modal Correction for AOA Bias Errors".

# TABLE OF CONTENTS

# 1.0 INTRODUCTION

1.1 Introduction 1   
1.2 Problem Description 2   
1.3 Literature Review 11   
1.4 Solution Approach 16

# 2.0 EFFECTS OF MODEL DYNAMICS ON AERODYNAMIC DATA

2.1 Introduction 18   
2.2 Force Balance Measurements 19   
2.3 Transformation of Balance Forces 19

# 3.0 THEORETICAL FORMULATION

3.1 Introduction 25   
3.2 Dynamic Equations of Motion 25

3.2.1 Lagrange's Equations 28   
3.2.2 Kinetic Energy 28   
3.2.3 Potential Energy 29   
3.2.4 Energy Dissipation Function 30   
3.2.5 Generalized Forces 30   
3.2.6 Equations of Motion 31

3.3 Modal Analysis 31   
3.4 Simplified Model 34   
3.4.1 Two Degree of Freedom Example 35

2.4.2 Extension to Multiple Degree of Freedom System 42

# 4.0 MODEL ATTITUDE BIAS ERROR CORRECTION

4.1 Introduction 44   
4.2 Modal Correction Theory 45   
4.3 Modal Correction Implementation 55

# 5.0 EXPERIMENTAL VERIFICATION

5.1 Introduction 59   
5.2 Wind-Off Dynamic Response Tests 59

5.2.1 Test Setup and Procedure 59   
5.2.2 Commercial Transport Model Test Results 64   
5.2.3 High Speed Transport Model Test Results 72

5.3 High Speed Transport Model Wind Tunnel Tests 84

5.3.1 Test Setup in Wind Tunnel 84   
5.3.2 Dynamic Response Tests in Wind Tunnel 86   
5.3.3 Wind Tunnel Test Results 90

6.0 CONCLUDING REMARKS 98   
7.0 REFERENCES 102

APPENDIX A: Effect of Aerodynamic Forces on Modal Characteristics 105

# LIST OF FIGURES

Figure 1.1 National Transonic Facility model support system. 4   
Figure 1.2 Schematic of wind tunnel model system. 5   
Figure 1.3 Effect of vibration on inertial model attitude measurement. 9   
Figure 1.4 Wind tunnel model instrumentation cavity. 10   
Figure 2.1 Aerodynamic forces and model coordinate axes. 20   
Figure 2.2 Influence of angle of attack error on drag coefficient for $C_{\mathrm{L}\alpha} = 0.05$ . 23   
Figure 3.1 Reference coordinate systems. 26   
Figure 3.2 Sting bending in yaw plane, $9.0\mathrm{Hz}$ vibration mode. 36   
Figure 3.3 Sting bending in pitch plane, $9.2\mathrm{Hz}$ vibration mode. 37   
Figure 3.4 Two degree of freedom model. 38   
Figure 3.5 Mode shapes for two degree of freedom example. 41   
Figure 4.1 Harmonic motion of model at natural frequency of $\omega_{\mathrm{ry}}$ 47   
Figure 4.2 Yaw plane mode of model system. 53   
Figure 4.3 Pitch plane mode of model system. 54   
Figure 4.4 Flowchart of modal correction method. 57   
Figure 5.1 Test setup in model assembly bay. 60   
Figure 5.2 Shaker attachment for excitation in the yaw plane. 62   
Figure 5.3 Sting bending in yaw plane, $10.3\mathrm{Hz}$ vibration mode. 65   
Figure 5.4 Model yawing on balance, $14.4\mathrm{Hz}$ vibration mode. 66   
Figure 5.5 Measured mean AOA, estimated bias, and corrected mean AOA versus yaw moment for sinusoidal input at $10.3\mathrm{Hz}$ 68   
Figure 5.6 Measured mean AOA, estimated bias, and corrected mean AOA versus yaw moment for sinusoidal input at $14.4\mathrm{Hz}$ 69

Figure 5.7 Measured mean AOA, estimated bias, and corrected mean AOA versus pitch moment for sinusoidal input at $11.2\mathrm{Hz}$ 70   
Figure 5.8 Measured mean AOA, estimated bias, and corrected mean AOA versus pitch moment for sinusoidal input at $16.2\mathrm{Hz}$ 71   
Figure 5.9 Sting bending in yaw plane, $9.0\mathrm{Hz}$ vibration mode. 74   
Figure 5.10 Model yawing on balance, $29.8\mathrm{Hz}$ vibration mode. 75   
Figure 5.11 Inertial AOA measurement, yaw acceleration, and yaw moment versus time for $9.0\mathrm{Hz}$ sinusoidal input in yaw plane. 76   
Figure 5.12 Inertial AOA measurement, yaw acceleration, and yaw moment versus time for $29.8\mathrm{Hz}$ sinusoidal input in yaw plane. 77   
Figure 5.13 Measured mean AOA, estimated bias, and corrected mean AOA versus yaw moment for sinusoidal input at $9.0\mathrm{Hz}$ 79   
Figure 5.14 Measured mean AOA, estimated bias, and corrected mean AOA versus pitch moment for sinusoidal input at $9.2\mathrm{Hz}$ 80   
Figure 5.15 (Top) Measured AOA and estimated bias error for $9.2\mathrm{Hz}$ sinusoidal excitation in pitch with $0.25\mathrm{Hz}$ modulation. (Bottom) Corresponding measured balance pitch moment. 82   
Figure 5.16 (Top) Measured AOA and estimated bias error for random excitation in pitch. (Bottom) Corresponding measured balance pitch moment. 83   
Figure 5.17 Measured and corrected mean angle-of attack for sinusoidal excitation at $7.3\mathrm{Hz}$ 88   
Figure 5.18 (Top) Measured and corrected AOA for sinusoidal excitation at $7.3\mathrm{Hz}$ with $0.5\mathrm{Hz}$ modulation. (Bottom) Corresponding balance yaw moment. 89   
Figure 5.19 Angle-of-Attack (AOA) for first sixty-four seconds of a wind tunnel test on a high speed transport model. 91   
Figure 5.20 (Top) Time domain response of the AOA measured with the servo-accelerometer sensor and the corrected AOA after removal of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment. 93

Figure 5.21 (Top) Time domain response of the AOA measured with the servo-accelerometer sensor and the corrected AOA after removal of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment. 94   
Figure 5.22 (Top) Time domain response of the AOA measured with the servo-accelerometer sensor and the corrected AOA after removal of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment. 95   
Figure 5.23 (Top) Time domain response of the AOA measured with the servo-accelerometer sensor and the corrected AOA after removal of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment. 96

# LIST OF TABLES

Table 5.1 Modal Parameters for Commercial Transport Model 64   
Table 5.2 Modal Parameters for High Speed Transport Model 72   
Table 5.3 Modal Parameters for High Speed Transport Model in Test Section 86   
Table 5.4 Summary of Wind Tunnel Results 90   
Table 5.5 Summary of Wind Tunnel Results for One Second Data Acquisition Intervals 97   
Appendix A Table 1 Transport model Worst Case Loading Conditions 107   
Appendix A Table 2 Transport Model Natural Frequency Comparison 108   
Appendix A Table 3 Transport Model Mode Radius Comparison 109

# LIST OF SYMBOLS

$a_{B}(t)$ acceleration bias error estimate

$a_{c}$ （204 centrifugal acceleration

$a_{n}(t)$ time dependent normal acceleration

$a_{t}(t)$ time dependent tangential acceleration

$a_{x}(t)$ time dependent longitudinal acceleration

$A_{fil}$ filtered AOA signal from inertial device

$A_{r}$ peak acceleration for $\mathbf{r}^{\mathrm{th}}$ mode

$A_{unf}(t)$ time dependent unfiltered AOA signal

$c_{ij}$ damping coefficients

$C_D$ drag coefficient

$C_{F_i}$ force coefficient for degree of freedom i

$C_L$ （20 lift coefficient

$C_{L\alpha}$ slope of lift coefficient versus angle of attack

$C_M$ 1 pitching-moment coefficient

$C_{M_i}$ moment coefficient for degree of freedom i

$CC_{r}$ correlation coefficient for least square fit of model

$d_{cg / bc}$ distance from model mass center of gravity to model balance center

$d_{F / bc}$ distance from point of force application to model balance center

$d_{i}$ （20 characteristic length corresponding to degree of freedom i

D energy dissipation function

$f_{r}$ natural frequency of $\mathbf{r}^{\mathrm{th}}$ mode in Hertz

$F_{A}$ axial force

$F_{c}$ （204 centrifugal force

$F_{D}$ drag force

$F_{L}$ lift force

$F_{N}$ normal force

$g$ （204 gravitational constant

$\pmb{i}$ scalar index

$I_{ybc}$ inertia about the y-axis for a reference at the model balance center

$k_{ij}$ （204 stiffness influence coefficients

$k_{B}$ bending stiffness

$k_{T}$ torsional stiffness

m number of included modes

$m_{ij}$ inertia coefficients

$m_{m}$ model mass

number of lumped masses used to represent the wind tunnel model system

N number of degrees of freedom in the analytical model

$p_r$ modal coordinate for mode $r$

$P_{ry}$ amplitude for mode $r_y$

$q_{i}$ （20 $i^{th}$ generalized coordinate

$\dot{q}_i$ derivative of $i^{th}$ generalized coordinate with respect to time

$q_{\infty}$ dynamic pressure

$Q_{i}$ non-conservative generalized applied force (or moment) associated with $q_{i}$

$Q_{Fi}$ generalized aerodynamic force for translation degree of freedom $i$

$Q_{Mi}$ generalized aerodynamic moment for translation degree of freedom $i$

$r$ （20 current mode number

$r_p$ designates pitch plane mode

$r_y$ designates yaw plane mode

$S$ reference area of the model

$S_{i}$ （20 reference area for degree of freedom i

$T$ kinetic energy of the system

time in seconds

U potential energy of the system

$\nu_{r}(t)$ time dependent velocity for $r^{th}$ mode

$V_{r}$ peak velocity for mode $r$

$V_{\infty}$ free-stream wind velocity

$y_{r}(t)$ time dependent displacement for $r^{th}$ mode

$Y_{r}$ peak displacement for $r^{th}$ mode

$\alpha_{s}$ pitch rotation angle between undeflected sting and inertial coordinates

$\alpha$ model attitude, or angle of attack

$\hat{\alpha}$ estimate of model attitude with bias error correction

$\Delta$ difference

$\pmb{\varepsilon}$ model attitude error

$\rho_{r}$ effective radius of $r^{th}$ vibration mode

$\omega_{r}$ circular frequency of $r^{th}$ mode

$\frac{d}{dt}$ derivative with respect to time

$\zeta_r$ modal damping for mode $r$

$[C]$ matrix of damping coefficients

$\left[\overset{\cdot}{I},\right]$ identity matrix

$[K]$ matrix of stiffness coefficients

$[M]$ matrix of inertia coefficients

$\{q\}$ vector of generalized coordinates

$\{\hat{q}\}$ subset of generalized coordinates representing rigid model

$\{Q\}$ vector of generalized forces

$\{Q^{\prime}\}$ vector of generalized forces transformed to modal space

$\{p\}$ vector of modal coordinates

$\{\phi \} _r$ mass normalized modal vector for mode $r$

$[\Phi]$ mass normalized modal matrix

$\left[\omega^{2},\right]$ diagonal matrix of natural frequency squared

[Ψ] modal, or eigenvector matrix

$\left[2\zeta \omega_{\bullet}\right]$ diagonalized damping matrix

(x,y,z) inertial coordinate system

$(x_{s},y_{s},z_{s})$ undeflected sting coordinate system

$(\mathbf{x}_{s0}, \mathbf{y}_{s0}, \mathbf{z}_{s0})$ origin of sting coordinate system relative to the inertial coordinate system

$\left(\mathbf{x}_{\mathrm{Bi}}, \mathbf{y}_{\mathrm{Bi}}, \mathbf{z}_{\mathrm{Bi}}\right)$ body axis coordinate system for ith concentrated mass

$(\mathbf{x_i},\mathbf{y_i},\mathbf{z_i})$ position of ith body coordinate axes relative to sting axes

$(\gamma, \alpha, \beta)$ rotation of $i$ th body coordinate axes relative to sting axes

# LIST OF ACRONYMS

AOA Angle of Attack

BPF bandpass filter

c.g. mass center of gravity

FEM finite element model

Hz Hertz

LPF lowpass filter

NTF National Transonic Facility

# Chapter 1

# INTRODUCTION

# 1.1 Introduction

Model vibrations are a significant problem when testing in high pressure wind tunnels. As discussed by Young [1], model vibrations can jeopardize model structural integrity, overload force balances and support stings, cause models to foul, affect aerodynamic data, and often limit test envelopes.

The National Transonic Facility [2], NTF, is a transonic wind tunnel located at NASA Langley Research Center which has the capability for testing models at Reynolds number up to 140 million at Mach 1 and dynamic pressure up to 7000 pounds per square foot. The NTF is a cryogenic facility with operating temperatures as low as $-290^{\circ}\mathrm{F}$ . Severe model vibrations have been encountered on a number of models since the tunnel began operation in 1984. References 3 through 6 document studies of model and model support vibrations in the facility. During a 1993 wind tunnel test, increased uncertainty in the model attitude data was observed for periods of high model vibration. The response of the onboard instrumentation to electrodynamic shaker input to the model without tunnel airflow, "wind-off", was examined for two transport model systems [7, 8] at the NTF. These wind-off dynamic tests found model vibration induced errors over an order of magnitude greater than the required accuracy for the inertial model attitude measurements.

This research investigates the effect of wind tunnel model system dynamics on measured aerodynamic data. The objective is to improve the aerodynamic data quality during conditions of high model vibrations. The equations of motion are developed using Lagrange's equations for the generalized problem of a cantilevered wind tunnel model. This was the first time a system dynamic analysis approach was used to examine the effects of model vibrations on the aerodynamic data. The modal solution of the equations of motion provides valuable insight into the underlying physics and provides the basis for the proposed "modal correction method" for dynamically induced errors in wind tunnel model attitude measurements. The proposed correction method uses the modal properties of the model system to minimize the number of transducers required for implementation. This is critical due to limited interior model space and thermal considerations associated with cryogenic wind tunnels where heated instrumentation packages are required. The method was the first time domain technique developed to compensate for multiple modes in both the pitch and yaw planes of the model system. The ability to correct in the time domain is necessitated by the random nature of the measured model dynamic response and the increased emphasis on correlating time dependent changes in model attitude with aerodynamic loads.

# 1.2 Problem Description

The majority of wind tunnel tests are conducted with a model supported on the end of a long tapered cylinder, referred to as a "sting", which is cantilevered from an arc sector or movable vertical strut-type of support. A schematic of the NTF model support system is

shown in Figure 1.1. Pitch attitude of the model is adjusted by rotation of the arc sector. The arc sector system is designed such that the center of rotation of the arc sector is at the model, so that changing the model pitch angle does not translate the model to a different position relative to the wind tunnel test section. Roll attitude of the model can be adjusted by rotation of the sting. A six component force balance is used as the single point of attachment between the model and support sting as shown in Figure 1.2. In order to achieve the desired measurement accuracy on three force and three moment aerodynamic load components, the balance is designed to be flexible as compared to the sting. The flexibility of the balance results in vibration modes characterized by the model vibrating as a rigid body on a spring (force balance) in pitch, yaw and roll. These modes are typically lightly damped and often excited during wind tunnel testing [6]. Other primary low frequency vibration modes are associated with sting bending in the pitch and yaw planes, where most of the bending deformation occurs over the small diameter portion of the sting near the model.

This dissertation will focus on the "pitch-pause" [9] wind tunnel test technique since the supporting wind tunnel test data were acquired using this technique at the NTF. The pitch-pause technique is a common test method used to obtain aerodynamic loads data in continuous flow, closed circuit wind tunnels. In the pitch-pause technique, the model is moved to a prescribed angle of attack with respect to the velocity vector, the transient responses are allowed to decay, and then the force balance, pressure, and angle of attack data are measured. At the NTF, the data measurement period is one second. The

图片摘要：该图主要展示 1.1 National Transonic Facility model support system。
![](images/157861fb39e097236e3fb691f51db4a3c909a6b3194ea98de4fdb5536fdeffe6.jpg)  
Figure 1.1 National Transonic Facility model support system.

图片摘要：该图主要展示 1.1 National Transonic Facility model support system。
![](images/0bec6e8eab479efd9b2a1bdd237fcdcde44891c406cdea0e8d078f88f96f3f3c.jpg)  
Figure 1.2 Schematic of wind tunnel model system.

procedure is then repeated for a series of model attitudes, which is referred to as a polar. Increasing emphasis on wind tunnel productivity is pushing facilities towards shorter test times (less time on point for transient dynamics to decay) and the effect on the aerodynamic data accuracy must be evaluated.

During wind tunnel tests, free stream turbulence produce fluctuations in dynamic pressure and flow angularity leading to unsteady forces on the model. The force balance and angle of attack measurements are typically low-pass filtered and averaged to obtain "steady-state" model attitude, aerodynamic force and moment data [10]. It is not unusual for the peak-to-peak variation of the dynamic component of the "steady-state" force data to be $50\%$ or more of the true mean. In Reference [11], the unsteadiness of the airflow and the resulting model vibration is discussed. It is noted that, if the model vibration response due to the flow unsteadiness is excessive, the ability to accurately measure the aerodynamic quantities of interest may be compromised. Mabey [11] approaches the problem by examining methods to reduce the flow unsteadiness in the wind tunnel. In the Advisory Group for Aerospace Research and Development (AGARD) report entitled "Wind Tunnel Flow Quality and Data Accuracy Requirements" [12], one of the data accuracy issues is the measurement of, and correction for, aeroelastic deformations and vibrations of models and support systems. Accuracy requirements [12] for lift, drag, and pitching moment for transport type aircraft in the high speed regime are: Lift Coefficient $\Delta C_L = 0.01$ ; Drag Coefficient $\Delta C_D = 0.0001$ ; Pitching-moment coefficient $\Delta C_M = 0.001$ . In order to maintain the required accuracy, the tunnel free-stream

conditions must be repeatable within the following boundaries: Tunnel total and stagnation pressure, $\Delta P = 0.1\%$ ; Model angle of attack, $\Delta \alpha = 0.01^{\circ}$ ; and Mach Number: $\Delta M = 0.001$ . As an example, for conditions near a maximum lift to drag ratio, an increase of 1 drag count ( $\Delta C_{D} = 0.0001$ ) will decrease the payload by approximately $1\%$ for the long-range mission of a large transport aircraft.

The predominant instrumentation used to measure model attitude or angle of attack (AOA) in wind tunnel testing at NASA Langley Research Center and wind tunnels throughout the world is the servo accelerometer device described in Reference 13. The inertial AOA package is shown installed in the nose of a test model in Figure 1.2. The AOA package uses a servo accelerometer with its sensitive axis parallel with the longitudinal axis of the model. For quasi-static conditions, this sensor provides a model attitude measurement with respect to the local gravity field to an accuracy of $\pm 0.01^{\circ}$ over a range of $\pm 20^{\circ}$ . An increment of $0.01^{\circ}$ corresponds to an acceleration of 175 micro-g's. During wind tunnel testing, the model mounted at the end of the sting experiences dynamic oscillations due to unsteady flows that result in a bias error in the model attitude measurement.

Young et. al [7] conducted an experimental study on the inertial model attitude sensor response to a simulated dynamic environment in 1993 at the NTF. The experimental study [7] clearly established that AOA bias error is due to centrifugal forces associated with model vibration. For a single mode in simple harmonic motion, this is shown

schematically in Figure 1.3. The AOA package moves on a circular arc about a center of rotation that is mode dependent. For a single mode, the motion of the AOA package can be treated similar to that of a simple pendulum. The centrifugal acceleration will act outward from the center of rotation and be equal to the tangential velocity squared divided by the radius arm. During wind-off dynamic tests, centrifugal acceleration due to model vibration created a bias error over an order of magnitude greater than the desired device accuracy of 0.01 degree. The bias error was found to be dependent on the vibration mode and amplitude. The study revealed the complexity of the problem when multiple vibration modes were present involving both pitch and yaw motions.

Although the Reference 7 study was conducted at the NTF, the AOA measurement error due to model dynamics is not unique to this wind tunnel or to cryogenic wind tunnels. The problem exists anytime model attitude is being measured by an inertial device in the presence of significant model system vibrations. The amount of error in the inertial model attitude measurement is dependent on the model system dynamics (i.e. will vary for each model system) and is very difficult to quantify during actual wind tunnel tests.

Space limitations in wind tunnel models require that the number of additional transducers used to implement a correction be minimized. This is illustrated by the wind tunnel model instrumentation cavity shown in Figure 1.4. Also, in a cryogenic facility, such as the NTF, special AOA sensor packages [13] are required. The instrumentation must be placed in a heated package to maintain the sensors and obtain accurate and calibrated

图片摘要：该图主要展示 1.3 Effect of vibration on inertial model attitude measureme。
![](images/7748d8869957a1a782635823cb32455b81cddfbaaf8b22b2e9a8cc79634267d4.jpg)

图片摘要：该图主要展示 1.3 Effect of vibration on inertial model attitude measureme。
![](images/45f9a4a4192841e7362bf879179d4100bdf921ad77339bcc2a88832ed31e5aac.jpg)  
Figure 1.3 Effect of vibration on inertial model attitude measurement.

图片摘要：该图主要展示 1.3 Effect of vibration on inertial model attitude measureme。
![](images/19377b20ab9726c012b34bf1f3579d0ebd0fcdb8aaa5a9f5281ea4eea30713ce.jpg)  
Wind tunnel model instrumentation cavity.   
Figure 1.4

measurements at extreme temperatures $(-290^{\circ}\mathrm{F})$ . Past experience with accelerometers placed outside of the heated instrumentation package has revealed problems ranging from sensitivity shifts due to temperatures variations to complete signal loss. The extreme temperatures conditions, limited interior model space, and stringent accuracy requirements necessitate placing the additional transducers necessary for correction of the inertial AOA sensor output in the heated instrumentation package. The centrifugal acceleration not only affects the inertial AOA device but can, if amplitudes are sufficiently high, affect the desired axial force or drag measurement accuracy. The effect of dynamics on pressure measurements can be a factor but is not addressed in this dissertation.

# 1.3 Literature Review

Previous analyses of wind tunnel model system dynamics were restricted to a planar problem. Burt and Uselton [14] examined the effects of sting vibrations on measured dynamic stability derivatives. The equations of motion were derived for model rigid body motion in the pitch plane using Newton's second law. Billingsley [15] uses Lagrange's equations to derive the equations of motion for a cantilevered sting-model system. Again, the derivation is restricted to motion in the pitch plane. Young et. al [7] have shown that model yaw vibration can result in an error in the measured pitch angle for a model-mounted inertial angle of attack device. Therefore, an analytical model is required that includes both pitch and yaw plane dynamics to better evaluate the effects of model dynamics on the measured aerodynamic data.

The first correction technique for model vibration induced errors in inertial wind tunnel model attitude measurements was developed in 1984 by Peiter Fuijkschot of the National Aerospace Laboratory in the Netherlands[16]. This time domain technique was developed for one vibration mode in each the yaw and pitch plane. Two additional accelerometers are used to measure the tangential accelerations due to the yaw and pitch motion of the model. The tangential accelerations are integrated to obtain velocity, squared, and divided by a scale factor to compensate for the effective radius of the vibration mode. This signal is then added to the unfiltered AOA output to cancel the bias term. The mode radius in the yaw and pitch plane is determined by tuning a potentiometer while manually exciting the model in the yaw and pitch plane, respectively. A major drawback is that this technique does not address the case where multiple yaw and pitch modes are present.

Renewed interest in the effects of model vibrations on the measured aerodynamic quantities was prompted by the 1993 study of Young et. al. [7]. Prior to this investigation, only a single mode in the model pitch and yaw planes was considered. This study showed the potential for multiple modes in each plane to participate. Several recent studies have been conducted at NASA Langley Research Center to examine the effects of model vibration on model attitude measurement devices [7, 8, 17, 18]. In addition, analysis of the vibration effects on gravity sensing inclinometers is underway by Fuijkschot [19, 20] of the National Aerospace Laboratory in the Netherlands.

Frequency domain correction techniques have been proposed by Young et. al [7] and Tcheng et. al [18]. The correction method of Young et. al is derived using an average displacement of the model through one cycle of vibration. This method requires the measurement of the natural frequencies and corresponding peak acceleration magnitudes from the frequency spectra of the yaw and pitch accelerations. Young proposes that the required scale factor, effective radius, be determined empirically during wind-off ground vibration tests. The correction method of Tcheng [18] requires the measurement of the natural frequencies from the frequency spectra of the tangential accelerations and the second harmonic components from the frequency spectrum of the unfiltered AOA signal. This technique is difficult to implement due to the participation of multiple modes and the required data accuracy to measure small magnitudes at the second harmonic frequency. Both techniques have implementation problems due to the required frequency domain signal processing of random wind tunnel test data over short (1 second) data acquisition periods.

Another method under development by Tripp [8] uses time and frequency domain analyses to estimate and correct for the dynamic bias error. The proposed time and frequency domain bias error correction algorithm is based on the bias term for a single yaw mode being represented by the square of the velocity divided by the mode radius. A sensitive correlation test between time series is provided by the cross spectral density coherence function. Correlated spectral components common to both the unfiltered AOA signal and square of the dynamic yaw or pitch measurement appear in the cross spectral density coherence function. Other spectral components common to the auto spectra

which are not phase coherent, i.e. unsynchronized, tend to be removed from the cross spectrum by averaging and canceled by normalization, and do not appear in the cross spectral coherence function. The coherence function and cross spectrum thus provide a means of detecting and quantifying AOA bias errors due to angular oscillation. The cross spectral density coherence function is examined for spectral correlation within the AOA passband and the corresponding modal frequencies are identified. The modal radius corresponding to each natural frequency is estimated by a least squares fit of the integral-squared yaw (or pitch) measurement to the dynamic AOA output. This requires a longer data record initially ( $\geq 10$ seconds) to obtain a good estimate of the mode radius. This mode radius is then used as a constant for the remainder of the data points. A bandpass filter about the modal frequency is used to isolate a particular mode. The resulting signal is then numerically integrated and squared and divided by the scalar mode radius to give the bias error associated with a particular mode. The correct AOA output is then found by subtracting off the contributions from all of the modes shown to have spectral correlation and low-pass filtering the result. In wind-off dynamic tests [8], this method had implementation problems due to significant low frequency random disturbances in the integral-squared yaw (or pitch) measurements which were absent in the AOA time series.

After the need to compensate for multiple vibration modes was demonstrated at NASA Langley Research Center [7,8,17], Fuijkshot extended his time domain correction technique to compensate for multiple modes [19, 20] using Euclidean kinematics of a

solid body. This work was done in parallel with the proposed time domain "modal correction method" that is the subject of this dissertation. For a given plane of motion, Fuijkshot proposes measuring both the rotational rate and the velocity of the rigid model and determining the correction term from the product of the two signals. The rotational rate and velocity signals for the yaw (or pitch) plane will contain the contributions for all modes acting in that plane. The radius for each of the modes will not need to be determined explicitly. The correction terms for the pitch and yaw planes are then added to the unfiltered AOA signal prior to filtering. The method is currently under evaluation and has been verified for sinusoidal tests [20]. The velocity can be determined through integration of an accelerometer signal. In application, the rotational rate has been obtained by integrating the difference from two linear accelerometers attached to the model fuselage, oriented in the yaw (or pitch) plane, divided by the accelerometer separation distance. This assumes the accelerometers are connected by a rigid model fuselage. This correction technique requires four additional transducers in order to determine the rotational rate and velocity in the pitch and yaw planes. The limited interior space in models and extreme temperature environments in some wind tunnels, where heated instrumentation packages are required, may prohibit this number of transducers. This method does not provide a means of checking the rigid-body model assumptions upon which it is based.

In general, the proposed time domain corrections provide several advantages. First, time domain signal processing can be applied to the random wind tunnel test data acquired

over short data sampling periods. Secondly, the inertial AOA package output can be corrected for the dynamically induced errors to give an accurate time domain model attitude signal. The measurement of time varying signals and analysis of this data is becoming a more significant requirement for subsonic and transonic experimental researchers[21]. The measurement of instantaneous and average values of model attitude and correlation with measured model loads is gaining increased interest.

# 1.4 Solution Approach

The research is divided into the following four areas: examination of the effects of models dynamics on aerodynamic data; development of a theoretical model; development of a correction for model vibration induced errors in inertial wind tunnel model attitude measurements; and experimental verification.

In Chapter 2, the significance of the problem is shown by examining the effects of model dynamics on the measured drag force and corresponding drag coefficient. Errors introduced by the centrifugal forces associated with model vibration are quantified. The propagation of the angle of attack errors during the transformation of the measured forces from the model body axes to the wind axes is also examined.

In Chapter 3, the governing equations of motion for a cantilevered wind tunnel model system are derived in discrete form using Lagrange's equations. This formulation describes both pitch and yaw plane dynamics. The equations of motion are solved using a

modal analysis approach to obtain the generalized, modal, solution. Based on observed behavior of wind tunnel model systems, the problem is simplified.

In Chapter 4, the theoretical model is used to develop a time domain correction method for model vibration induced errors in inertial wind tunnel model attitude measurements. The implementation of the proposed "modal correction method" using digital signal processing techniques is also described.

In Chapter 5, the modal correction method is verified through a combination of wind-off dynamic tests on two transport model systems and wind tunnel test data. The modal correction method is applied to wind-off model dynamic response data for sinusoidal, modulated sinusoidal and random shaker inputs in the pitch and yaw plane. In addition, the modal correction method is applied to measured dynamic response data recorded during wind tunnel testing of a transport model in the NTF.

In Chapter 6, the research results are summarized and recommendations for future work are described.

# Chapter 2

# EFFECTS OF MODEL DYNAMICS ON AERODYNAMIC DATA

# 2.1 Introduction

For wind tunnel data acquisition, Steinle and Stanewsky [12] recommend that samples of data be taken over a time interval sufficient to average out the effects of dynamic response and unsteady flow to establish the desired confidence interval. However, as discussed by Buehrle and Young [17], the centrifugal acceleration created by model vibration results in a bias error in the inertial wind tunnel model attitude measurement. For wind-off sinusoidal model response, it is shown that the inertial angle of attack measurement has a mean offset which cannot be removed by filtering or averaging. Errors over an order of magnitude greater than the required device accuracy of $0.01^{\circ}$ are possible [7, 8].

In this chapter, the effect of model vibration on the force balance measurements is quantified. The direct effect of the vibration induced centrifugal force on the accuracy of the measured forces is examined. Typically, the forces and moments are measured by an internally mounted strain-gage balance which has a coordinate system that is fixed to the model. This data is transformed to obtain the desired lift and drag force components using the measured model attitude. The propagation of the model attitude error during the transformation process is also examined.

# 2.2 Force Balance Measurements

Model vibration induced centrifugal forces result in errors being introduced into the balance forces. The centrifugal force $F_{c}$ can be written

$$
F _ {c} = m _ {m} a _ {c} \tag {2.1}
$$

where $m_{m}$ is the model mass and $a_{c}$ is the total centrifugal acceleration. It is anticipated that the centrifugal force acting on the model will be small. For the servo accelerometer, a centrifugal acceleration of .00175 g's corresponds to a model attitude error of 0.1 degrees, which is 10 times the required device accuracy. This same centrifugal acceleration will result in only a 0.26 pound centrifugal force for a model weighing 150 pounds. For the high dynamic pressure wind tunnel tests that produce significant model dynamics, this would result in a drag coefficient error less than the required accuracy.

# 2.3 Transformation of Balance Forces

A more significant error in the measured forces may occur due to errors in the measured model attitude. The propagation of the model attitude error into the measured drag force was described by Owen et. al. [22]. The strain gage balance forces are measured in the model body axes, which are fixed to the model, and transformed to the lift and drag force components using the measured model attitude. Figure 2.1 shows the relevant forces and coordinate axes. The axial force, $\mathbf{F}_{\mathrm{A}}$ , and normal force, $\mathbf{F}_{\mathrm{N}}$ , are the balance forces measured relative to the body axes, $(\mathbf{x}_{\mathrm{B}}, \mathbf{z}_{\mathrm{B}})$ . The lift force, $\mathbf{F}_{\mathrm{L}}$ , and drag force, $\mathbf{F}_{\mathrm{D}}$ , are defined relative to the wind axes, $(\mathbf{x}, \mathbf{z})$ , which have one axis parallel to the flow direction. The measured model attitude, $\alpha$ , defines the transformation between the two

图片摘要：该图主要展示 2.1 Aerodynamic forces and model coordinate axes。
![](images/3740b6b81fca41f1658b6c366c8d94a044e0a011826045ccd16cab4d98936a38.jpg)  
Figure 2.1 Aerodynamic forces and model coordinate axes.

coordinate systems. The lift and drag forces can be written

$$
F _ {L} = F _ {N} \cos (\alpha) - F _ {A} \sin (\alpha) \tag {2.2a}
$$

$$
F _ {D} = F _ {A} \cos (\alpha) + F _ {N} \sin (\alpha) \tag {2.2b}
$$

If the model attitude has an error, $\varepsilon$ , the lift and drag forces can be written

$$
F _ {L} = F _ {N} \cos (\alpha + \varepsilon) - F _ {A} \sin (\alpha + \varepsilon) \tag {2.3a}
$$

$$
F _ {D} = F _ {A} \cos (\alpha + \varepsilon) + F _ {N} \sin (\alpha + \varepsilon) \tag {2.3b}
$$

The errors in the lift and drag forces due to the model attitude error, $\varepsilon$ , are defined by the differences of Equations 2.2 and 2.3.

$$
\Delta F _ {L} = F _ {N} \left(\cos (\alpha + \varepsilon) - \cos (\alpha)\right) - F _ {A} \left(\sin (\alpha + \varepsilon) - \sin (\alpha)\right) \tag {2.4a}
$$

$$
\Delta F _ {D} = F _ {A} \left(\cos (\alpha + \varepsilon) - \cos (\alpha)\right) + F _ {N} \left(\sin (\alpha + \varepsilon) - \sin (\alpha)\right) \tag {2.4b}
$$

Expanding the trigonometric expressions and applying small angle assumptions for $\varepsilon$ ,

$$
\Delta F _ {L} = - \varepsilon \left(F _ {N} \sin (\alpha) + F _ {A} \cos (\alpha)\right) \tag {2.5a}
$$

$$
\Delta F _ {D} = \varepsilon \left(F _ {N} \cos (\alpha) - F _ {A} \sin (\alpha)\right) \tag {2.5b}
$$

Substituting from Equation 2.2 for the terms in parentheses results in

$$
\Delta F _ {L} = - \varepsilon F _ {D} \tag {2.6a}
$$

$$
\Delta F _ {D} = \varepsilon F _ {L} \tag {2.6b}
$$

The aerodynamic forces are expressed in coefficient form as

$$
C _ {L} = \frac {F _ {L}}{q _ {\infty} S} \text {a n d} C _ {D} = \frac {F _ {D}}{q _ {\infty} S} \tag {2.7}
$$

where $C_L$ is the coefficient of lift, $C_D$ is the coefficient of drag, $q_\infty$ is the dynamic pressure, and $S$ is the reference area of the model.

Rewriting Equation 2.6 in coefficient form gives

$$
\Delta C _ {L} = - \varepsilon C _ {D} \tag {2.8a}
$$

$$
\Delta C _ {D} = \varepsilon C _ {L} \tag {2.8b}
$$

As discussed in Chapter 1, the accuracy requirements [12] for lift and drag measurements for transport-type aircraft in the high speed regime are: Lift Coefficient, $\Delta C_L = 0.01$ ; Drag Coefficient, $\Delta C_D = 0.0001$ . Except for conditions near zero lift, the coefficient of drag is significantly less than the coefficient of lift [23]. Therefore, the error in drag coefficient will be more critical with regard to its required measurement accuracy. Assuming the lift coefficient can be represented as a linear function of model attitude, gives

$$
C _ {L} = C _ {L _ {\alpha}} \alpha + \text {C o n s} t \tag {2.9}
$$

where $C_{L\alpha}$ is the slope of the lift coefficient versus model attitude plot. Substituting the results of Equation 2.9 into Equation 2.8b gives

$$
\Delta C _ {D} = \frac {\pi}{1 8 0} \varepsilon \left(C _ {L \alpha} \alpha + \operatorname {C o n s} \tan t\right) \tag {2.10}
$$

where $\alpha$ and $\varepsilon$ are expressed in degrees. The slope of the lift coefficient versus model attitude plot for several characteristic wing shapes range from 0.05 to 0.1 per degree [23]. Using the most conservative, lower, value of $C_{L\alpha} = 0.05$ per degree, the error in drag coefficient versus model attitude is plotted for several values of model attitude error in Figure 2.2. For this plot, the constant term in Equation 2.10 is set to zero. For a nonzero constant term the lines will be shifted, however, the basic trends will be consistent with those shown.

图片摘要：该图主要展示 2.2 Influence of angle of attack error on drag coefficient f。
![](images/c402d505e1178980140338fb678332328398c050f1c75d83df70fc574517adfa.jpg)  
Figure 2.2 Influence of angle of attack error on drag coefficient for $C_{L\alpha} = 0.05$ .

As can be seen from Figure 2.2, significant errors in drag coefficient can occur due to the propagation of the errors in the model attitude measurement. Model attitude errors equivalent to those measured in wind-off dynamic tests $(\varepsilon \geq 0.1^{\circ})$ [7, 8] would result in an error in the drag coefficient that is an order of magnitude greater than the required accuracy at high angles of attack.

# Chapter 3

# THEORETICAL FORMULATION

# 3.1 Introduction

In this chapter, the equations of motion for a cantilevered wind tunnel model system are derived using Lagrange's Equations [24- 26]. The Lagrange method provides a generalized systematic energy approach for defining the equations of motion in any convenient coordinate system. The resulting equations of motion are formulated in terms of the generalized, modal, coordinates. Based on observed behavior of the model system during wind tunnel tests, the analytical model is simplified. This simplified model provides the basis for development of the modal correction method in Chapter 4.

# 3.2 Dynamic Equations of Motion

A lumped mass model will be used to represent the wind tunnel model and its support system. This work extends the planar analysis of Billingsley [15] to include both pitch and yaw dynamics of the sting-balance-model system.

In order to represent the model system during pitch-pause wind tunnel testing, three coordinate systems are defined in Figure 3.1. The coordinate system $(\mathbf{x}, \mathbf{y}, \mathbf{z})$ is the inertial coordinate system with the x-axis parallel to the wind direction. The coordinate system $(\mathbf{x}_s, \mathbf{y}_s, \mathbf{z}_s)$ is fixed to the undeflected sting axis and has its origin at the arc sector center of rotation. Recall from Chapter 1, that the arc sector is the movable portion of the model support system that provides the pitch adjustment for the model. The arc sector is

图片摘要：该图主要展示 3.1 Reference coordinate systems。
![](images/2da8ef232161c76d812cc0acc7855e07d719d689bbcfc3a757f1af92f4f4c914.jpg)  
Figure 3.1 Reference coordinate systems.

designed such that its center of rotation is at the model, so that changing the model pitch angle does not translate the model to a different position relative to the wind tunnel test section. The coordinate system $(\mathbf{x}_{s},\mathbf{y}_{s},\mathbf{z}_{s})$ can be defined by the location of its origin $(\mathbf{x}_{s0},\mathbf{y}_{s0},\mathbf{z}_{s0})$ relative to the inertial coordinate system and the pitch angle $(\alpha_{s})$ . The body axes $(\mathbf{x}_{Bi},\mathbf{y}_{Bi},\mathbf{z}_{Bi})$ are fixed to the $i$ th concentrated mass. The position and orientation of the body axes for the $i$ th concentrated mass relative to the undeflected sting axes are defined by the translations $(\mathbf{x}_i,\mathbf{y}_i,\mathbf{z}_i)$ and rotations $(\gamma_i,\alpha_i,\beta_i)$ .

In the pitch-pause method of wind tunnel testing, the model is pitched to a desired angle $(\alpha_{s})$ and paused to establish "steady-state" conditions. This results in:

$$
\dot {x} _ {s 0} = \dot {y} _ {s 0} = \dot {z} _ {s 0} = \dot {\alpha} _ {s} = 0 \tag {3.1}
$$

where the " $\cdot$ " denotes the derivative with respect to time. The time varying components representing the motion of the $i$ th mass are the translations $(x_i, y_i, z_i)$ and rotations $(\gamma_i, \alpha_i, \beta_i)$ relative to the undeflected sting. The generalized coordinates describing the motion of the cantilevered sting-balance-model system can be written:

$$
\left\{q \right\} = \left\{x _ {1} \quad y _ {1} \quad z _ {1} \quad \gamma_ {1} \quad \alpha_ {1} \quad \beta_ {1} \quad \dots \quad x _ {n} \quad y _ {n} \quad z _ {n} \quad \gamma_ {n} \quad \alpha_ {n} \quad \beta_ {n} \right\} ^ {T} \tag {3.2}
$$

where $n$ is the number of lumped masses used to represent the wind tunnel model system. The rotation angles $(\gamma_{i}, \alpha_{i}, \beta_{i})$ induced by inertial and aerodynamic loading are small. Therefore, in the subsequent derivations, small angle approximations (i.e., $\sin(\alpha) \approx \alpha$ ; $\cos(\alpha) \approx 1$ ) can be used and higher order terms can be neglected.

# 3.2.1 Lagrange's Equations

For a lumped mass model, Lagrange's Equations [26] can be written as:

$$
\frac {d}{d t} \left(\frac {\partial T}{\partial \dot {q} _ {i}}\right) - \frac {\partial T}{\partial q _ {i}} + \frac {\partial D}{\partial \dot {q} _ {i}} + \frac {\partial U}{\partial q _ {i}} = Q _ {i} \quad \text {f o r} \quad i = 1, \dots , N \tag {3.3}
$$

where:

$$
\mathbf {D} = \text {e n e r g y}
$$

$$
n = \text {n u m b e r o f l u m p e d m a s s e s u s e d t o r e p r e s e n t t h e w i n d t u n n e l m o d e l s y s t e m}
$$

$$
\mathbf {N} = 6 ^ {*} \mathbf {n} = \text {n u m b e r o f d e g r e e s o f f r e e d o m}
$$

$$
q _ {i} = \text {i t h g e n e r a l i z e d c o o r d i n a t e}
$$

$$
\dot {q} _ {i} = \text {d e r i v a t i v e o f i t h g e n e r a l i z e d c o o r d i n a t e w i t h r e s p e c t t o t i m e}
$$

$$
Q _ {i} = \text {n o n - c o n s e r v a t i v e g e n e r a l i z e d a p p l i e d f o r c e (o r m o m e n t) a s s o c i a t e d w i t h q} _ {i}
$$

$$
\mathrm {T} = \text {k i n e t i c e n e r g y o f t h e s y s t e m}
$$

$$
\mathrm {U} = \text {p o t e n t i a l}
$$

# 3.2.2 Kinetic Energy

The kinetic energy of the system can be written [26]:

$$
T = \frac {1}{2} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} m _ {i j} \dot {q} _ {i} \dot {q} _ {j} \tag {3.4}
$$

where the $\mathfrak{m}_{\mathrm{ij}}$ are inertia coefficients. For small oscillations about the equilibrium, the inertia coefficients are constants and the kinetic energy is a function of $\{\dot{q}\}$ only. The mass matrix is symmetric, i.e., $\mathfrak{m}_{\mathrm{ij}} = \mathfrak{m}_{\mathrm{ji}}$ . Since the kinetic energy is not a function of $\{q\}$ ,

$$
\frac {\partial T}{\partial q _ {i}} = 0 \tag {3.5}
$$

Taking the derivative of the kinetic energy with respect to the time derivative of the ith generalized coordinate gives:

$$
\frac {\partial T}{\partial \dot {q} _ {i}} = \sum_ {j = 1} ^ {N} m _ {i j} \dot {q} _ {j} \tag {3.6}
$$

The time derivative of Equation 3.6 is:

$$
\frac {d}{d t} \left(\frac {\partial T}{\partial \dot {q} _ {i}}\right) = \sum_ {j = 1} ^ {N} m _ {i j} \ddot {q} _ {j} \tag {3.7}
$$

# 3.2.3 Potential Energy

For the cantilevered wind tunnel model, the potential energy is equal to the strain energy stored in the sting-model system. A detailed derivation of the strain energy is given by Fung [27]. The potential energy can be written in terms of the stiffness influence coefficients as:

$$
U = \frac {1}{2} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} k _ {i j} q _ {i} q _ {j} \tag {3.8}
$$

where the stiffness influence coefficient, $k_{ij}$ , is the force required at point (i) due to a unit deflection at point (j) with all other points held fixed. The stiffness influence coefficients are symmetric, i.e., $k_{ij} = k_{ji}$ . Taking the derivative of the potential energy function with respect to the generalized coordinate ( $q_i$ ) gives:

$$
\frac {\partial U}{\partial q _ {i}} = \sum_ {j = 1} ^ {N} k _ {i j} q _ {j} \tag {3.9}
$$

# 3.2.4 Energy Dissipation Function

For the case of viscous damping, a dissipation function, $D$ , analogous to the potential energy function can be defined [26].

$$
D = \frac {1}{2} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} c _ {i j} \dot {q} _ {i} \dot {q} _ {j} \tag {3.10}
$$

where the damping coefficients, $c_{ij}$ , are symmetric, i.e., $c_{ij} = c_{ji}$ . Taking the derivative of the dissipation function with respect to the time derivative of the $i$ th generalized coordinate gives:

$$
\frac {\partial D}{\partial \dot {q} _ {i}} = \sum_ {j = 1} ^ {N} c _ {i j} \dot {q} _ {j} \tag {3.11}
$$

# 3.2.5 Generalized Forces

The primary generalized forces are the unsteady aerodynamic loads. The aerodynamic loads will be modeled using a quasi-steady approximation [15]. The generalized aerodynamic forces associated with the translation degrees of freedom are modeled as:

$$
Q _ {F _ {i}} = q _ {\infty} S _ {i} C _ {F _ {i}} \tag {3.12}
$$

where, $q_{\infty}$ is the dynamic pressure and $S_{i}$ is the characteristic area. The coefficient $C_{Fi}$ will be assumed linear and is a function of the model attitude. Similarly, the generalized aerodynamic moments associated with the rotational degrees of freedom are modeled as:

$$
Q _ {M _ {i}} = q _ {\infty} S _ {i} d _ {i} C _ {M _ {i}} \tag {3.13}
$$

where $\mathbf{d}_{\mathrm{i}}$ is a characteristic length and the coefficient $C_{\mathrm{Mi}}$ is assumed to be a linear function of model attitude.

# 3.2.6 Equations of Motion

The equations of motion for the $i$ th lumped mass can be obtained by substituting the results from Equations 3.5, 3.7, 3.9, 3.11, 3.12 and 3.13 into Equation 3.3. In matrix form this yields:

$$
[ M ] \{\ddot {q} \} + [ C ] \{\dot {q} \} + [ K ] \{q \} = \{Q \} \tag {3.14}
$$

where,

$$
\left\{q \right\} = \left\{x _ {1} y _ {1} z _ {1} \gamma_ {1} \alpha_ {1} \beta_ {1} \dots x _ {n} y _ {n} z _ {n} \gamma_ {n} \alpha_ {n} \beta_ {n} \right\} ^ {T}
$$

$[C]$ is a square matrix of the damping coefficients, $\mathbf{c}_{\mathrm{ij}}$   
$[K]$ is a square matrix of the stiffness coefficients, $\mathbf{k}_{ij}$   
$[M]$ is a square matrix of the inertia coefficients, $\mathfrak{m}_{\mathrm{ij}}$   
$\{Q\}$ is a vector containing the generalized forces, $\mathbf{Q}_{i}$

# 3.3 Modal Analysis

The modal analysis technique [24, 28] will be used to solve for the dynamic response of the multiple degree of freedom system described by Equation 3.14 with initial conditions $\{q(0)\} = \{q_0\}$ and $\{\dot{q}(0)\} = \{\dot{q}_0\}$ . The modal analysis technique is based on the transformation of the coupled equations of motion represented by Equation 3.14 into an independent set of equations using the normal modes of the system.

In the modal analysis technique, the first step is to obtain the eigenvalues and eigenvectors associated with the mass and stiffness matrices of the system. Numerical

methods for solving the eigenvalue problem are discussed in References 21, 23 and 26. Another approach is to obtain the eigenvalues and eigenvectors through experimental modal analysis [29, 30]. Once the natural frequencies and mode shapes are obtained, the solution to the eigenvalue problem can be written as:

$$
[ M ] [ \Psi ] \left[ \dot {\omega} ^ {2}, \right] = [ K ] [ \Psi ] \tag {3.15}
$$

where, $[\Psi]$ is the modal or eigenvector matrix

$$
\left[ \begin{array}{l} \omega^ {2}. \end{array} \right] \text {i s a d i a g o n a l m a t r i x o f t h e n a t u r a l f r e q u e n c y s ,} \omega_ {\mathrm {r}}, \text {s q u a r e d}
$$

Normalizing the modal matrix with respect to the mass matrix yields:

$$
[ \Phi ] ^ {T} [ M ] [ \Phi ] = \left[ \begin{array}{l l} \dot {I} & \end{array} \right] \tag {3.16a}
$$

$$
[ \Phi ] ^ {T} [ K ] [ \Phi ] = \left[ \begin{array}{l} \dot {\omega} ^ {2}, \end{array} \right] \tag {3.16b}
$$

where, $[\Phi]$ is the mass normalized modal or eigenvector matrix, and

$$
\left[ \begin{array}{l} I _ {1} \end{array} \right] \text {i s t h e i d e n t i t y m a t r i x}
$$

The transformation from the generalized coordinates, $\{\mathbf{q}\}$ , to the modal coordinates, $\{\mathfrak{p}\}$ , can be written:

$$
\left\{q (t) \right\} = [ \Phi ] \left\{p (t) \right\} = \sum_ {r = 1} ^ {N} \left\{\phi \right\} _ {r} p _ {r} (t) \tag {3.17}
$$

where, $\{\phi\}_r$ is the mass normalized modal vector for mode r. Substituting Equation 3.17 into Equation 3.14, and premultiplying by $[\Phi]^T$ yields,

$$
\left\{\ddot {p} \right\} + \left[ \Phi \right] ^ {T} [ C ] \left[ \Phi \right] \left\{\dot {p} \right\} + \left[ \omega^ {2}, \right] \{p \} = \left[ \Phi \right] ^ {T} \{Q \} \tag {3.18}
$$

Assuming the damping is a linear combination of the mass and stiffness matrices, the transformation will also diagonalize the damping matrix.

$$
[ \Phi ] ^ {T} [ C ] [ \Phi ] = \left[ \begin{array}{l} 2 \zeta \omega_ {\cdot} \end{array} \right] \tag {3.19}
$$

where the modal damping for mode $r$ can be written:

$$
\zeta_ {r} = \frac {1}{2 \omega_ {r}} \left\{\phi \right\} _ {r} ^ {T} [ C ] \left\{\phi \right\} _ {r} \tag {3.20}
$$

Substituting Equation 3.19 into 3.18 results in

$$
\left\{\ddot {p} \right\} + \left[ 2 \zeta \omega_ {\cdot} \right] \left\{\dot {p} \right\} + \left[ \omega^ {2} \cdot \right] \left\{p \right\} = \left\{Q ^ {\prime} \right\} \tag {3.21}
$$

where

$$
\left\{Q ^ {\prime} \right\} = \left[ \Phi \right] ^ {T} \left\{Q \right\} \tag {3.22}
$$

The N independent equations corresponding to Equation 3.21 can be written as

$$
\ddot {p} _ {r} (t) + 2 \zeta_ {r} \omega_ {r} \dot {p} (t) + \omega_ {r} ^ {2} p (t) = Q _ {r} ^ {\prime} (t), r = 1, 2, \dots , N \tag {3.23}
$$

This is the form of a single degree of freedom system with viscous damping. Using the transformation equation (3.17), the initial conditions can be written

$$
\left\{q (0) \right\} = [ \Phi ] \left\{p (0) \right\} \text {a n d} \left\{\dot {q} (0) \right\} = [ \Phi ] \left\{\dot {p} (0) \right\} \tag {3.24}
$$

Premultiplying these equations by $[\Phi]^T[M]$ and solving for the modal initial conditions gives

$$
p _ {r} (0) = \left\{\phi \right\} _ {r} ^ {T} [ M ] \left\{q (0) \right\} \text {a n d} \dot {p} _ {r} (0) = \left\{\phi \right\} _ {r} ^ {T} [ M ] \left\{\dot {q} (0) \right\}, f o r r = 1, 2, \dots , N \tag {3.25}
$$

The solution to Equation 3.23 can be obtained using the Laplace transform method [24]. This results in

$$
\begin{array}{l} p _ {r} (t) = \frac {1}{\omega_ {d _ {r}}} \int_ {0} ^ {t} Q _ {r} ^ {\prime} (\tau) e ^ {- \zeta_ {r} \omega_ {r} (t - \tau)} \sin \omega_ {d _ {r}} (t - \tau) d \tau \\ + e ^ {- \zeta_ {r} \omega_ {r} t} \left(p _ {r} (0) \cos \left(\omega_ {d _ {r}} t\right) + \frac {\dot {p} _ {r} (0) + \zeta_ {r} \omega_ {r} p _ {r} (0)}{\omega_ {d _ {r}}} \sin \left(\omega_ {d _ {r}} t\right)\right) \tag {3.26} \\ \end{array}
$$

where $\omega_{d_r} = \omega_r\sqrt{(1 - \zeta_r^2)}$ is the damped natural frequency for mode r.

For a given set of generalized forces and initial conditions, Equations 3.22, 3.25 and 3.26 can be used to solve for the modal coordinates, $\{\mathfrak{p}\}$ . The solution in terms of the generalized coordinates, $\{\mathbf{q}\}$ , can then be found from Equation 3.17. The problem is now in generalized form and can be used to estimate and correct for model vibration induced centrifugal accelerations. However, the problem can be simplified as developed in the following section.

# 3.4 Simplified Model

Once the natural frequencies and mode shapes have been obtained, the dynamic model of the sting-model system can be simplified based on behavior observed during wind tunnel testing. The primary dynamic components affecting the wind tunnel model instrumentation are in the model pitch and yaw planes [7, 8]. Since the inertial angle of attack device has its sensitive axis parallel to the longitudinal axis of the model, the

device is not sensitive to roll motions about this axis. Also, the effects of axial modes on the inertial angle of attack device can be removed through filtering. Therefore, only the pitch and yaw plane motions will be considered in subsequent derivations.

Figures 3.2 and 3.3 show measured mode shapes of a high speed commercial transport model in the National Transonic Facility (NTF). These mode shapes demonstrate several important characteristics common to models tested in the NTF. The lower frequency modes ( $<50\mathrm{Hz}$ ) of the model system are characterized by rigid body motion of the model on the more flexible sting-balance combination. The first two modes are associated with sting bending motion in the pitch and yaw plane. In order to achieve the desired measurement accuracy for the "steady-state" aerodynamic loads, the force balance is relatively flexible as compared to the model and sting. The strain gage balance systems used in the NTF [31] are designed with flexures that separate the loads into its planar components with minimal interactions. This results in predominantly pitch or yaw plane motion of the model for the lower frequency modes of the system. For a given mode, the rigid-body model motion can be defined by a translation y or z along with a corresponding rotation $\beta$ or $\alpha$ (see Figures 3.2 and 3.3).

# 3.4.1 Two Degree of Freedom Example

A two degree of freedom example will be used to define some useful properties associated with the planar motion of the "rigid" model. The modal characteristics of the two degree of freedom system shown in Figure 3.4 will be examined. This is similar to an

图片摘要：该图主要展示 s 3.2 and 3.3 show measured mode shapes of a high speed comm。
![](images/808b786d2db8871984dbccfe4bf030bf8de6c94bb6c4eb0ed966548e200bc6fb.jpg)  
Figure 3.2 Sting bending in yaw plane, $9.0\mathrm{Hz}$ vibration mode.

图片摘要：该图主要展示 3.2 Sting bending in yaw plane, vibration mode。
![](images/4b770dcbc7357e85ee2b1fc4d4e9785666acdee83b915522d39f08dde6f4b457.jpg)  
Figure 3.3 Sting bending in pitch plane, $9.2\mathrm{Hz}$ vibration mode.

图片摘要：该图主要展示 3.3 Sting bending in pitch plane, vibration mode。
![](images/5f753cfe868213f2abda8a81eb8075f8daad0f965971654caba7f579bb71c5b5.jpg)  
Figure 3.4 Two degree of freedom model.

example for vehicle suspension given by Thompson [32]. In this example, the translation and rotation coordinates at the balance moment center will be used in defining the model motion. Using the Lagrange Method, the equations of motion are derived. For small angles, the equations of motion are

$$
\left[ \begin{array}{c c} m _ {m} & - m _ {m} \cdot d _ {c g / b c} \\ - m _ {m} \cdot d _ {c g / b c} & I _ {y _ {b c}} \end{array} \right] \left\{ \begin{array}{l} \ddot {z} \\ \ddot {\alpha} \end{array} \right\} + \left[ \begin{array}{c c} k _ {B} & 0 \\ 0 & k _ {T} \end{array} \right] \left\{ \begin{array}{l} z \\ \alpha \end{array} \right\} = \left\{ \begin{array}{c} - 1 \\ d _ {F / b c} \end{array} \right\} F (t) \tag {3.27}
$$

where, $m_{m}$ is the model mass, $d_{cg/bc}$ is the distance from the mass center to the balance center; $d_{F/bc}$ is the distance from the force to the balance center; $I_{y/bc}$ is the inertia about the balance center; $k_{B}$ is the bending stiffness; $k_{T}$ is the torsional stiffness; $z$ and $\alpha$ are the displacement and rotation from the equilibrium position; and $F(t)$ is the applied force.

The main interest is in the form of the mode shapes. The eigenvalue problem corresponding to Equation 3.27 can be written

$$
\left[ \begin{array}{l l} k _ {B} & 0 \\ 0 & k _ {T} \end{array} \right] \left\{ \begin{array}{l} z \\ \alpha \end{array} \right\} = \omega^ {2} \left[ \begin{array}{c c} m _ {m} & m _ {m} \cdot d _ {c g / b c} \\ m _ {m} \cdot d _ {c g / b c} & I _ {y _ {b c}} \end{array} \right] \left\{ \begin{array}{l} z \\ \alpha \end{array} \right\} \tag {3.28}
$$

Based on measured weight, physical dimensions, and natural frequencies of a typical transport model system, the following constants were determined.

$$
m _ {m} = 0. 3 3 1 3 \text {p o u n d - s e c o n d} ^ {2} / \text {i n c h}
$$

$$
I _ {y b c} = 1 9. 5 1 \text {i n c h - p o u n d - s e c o n d} ^ {2}
$$

$$
\mathrm {d} _ {\mathrm {c g / b c}} = 5 \text {i n c h e s}
$$

$$
\mathrm {k} _ {\mathrm {B}} = 1 3 0 8 \text {p o u n d / i n c h}
$$

$$
k _ {T} = 2 7 7 0 8 9 \text {i n c h - p o u n d}
$$

Substituting these values into Equation 3.28, and solving the eigenvalue problem yields

$$
f _ {1} = \frac {\omega_ {1}}{2 * \pi} = 9. 3 8 H z; \left\{\phi \right\} _ {1} = \left\{ \begin{array}{l} - 1. 5 1 3 \\ 0. 0 4 1 5 \end{array} \right\} \tag {3.29a}
$$

$$
f _ {2} = \frac {\omega_ {2}}{2 * \pi} = 2 6. 7 \mathrm {H z}; \left\{\phi \right\} _ {2} = \left\{ \begin{array}{l} 1. 7 1 9 \\ 0. 2 9 5 5 \end{array} \right\} \tag {3.29b}
$$

The mode shapes are depicted graphically in Figure 3.5. Note that for each mode there is a node (point of zero motion) about which the rigid body model rotates. The position of this node is defined by the ratio of the translation and rotation degrees of freedom. Scaling the modes to unit rotation gives

$$
\left\{\phi \right\} _ {1} = 0. 0 4 1 5 \left\{ \begin{array}{c} - 3 6. 4 \\ 1 \end{array} \right\} = 0. 0 4 1 5 \left\{ \begin{array}{c} - \rho_ {1} \\ 1 \end{array} \right\} \tag {3.30a}
$$

$$
\left\{\phi \right\} _ {2} = 0. 2 9 5 5 \left\{ \begin{array}{c} 5. 8 2 \\ 1 \end{array} \right\} = 0. 2 9 5 5 \left\{ \begin{array}{c} - \rho_ {2} \\ 1 \end{array} \right\} \tag {3.30b}
$$

where the $i$ th mode radius, $\rho_{i}$ , is defined as the ratio of the translation and rotation mode shape coefficients with the modal vector scaled to unit rotation. This yields a physical interpretation of the mode radius as the distance from the node to the reference point on the model with the positive direction defined by the model $x$ -axis. For this example, the mode radius values are $\rho_{1} = 36.4$ inches, and $\rho_{2} = -5.82$ inches. The radius by definition can be positive or negative based on the mode shape. The effect of the sign of the radius will be discussed in Chapter 5.

图片摘要：该图主要展示 3.5 Mode shapes for two degree of freedom example。
![](images/fef2204fe18fada5a4b05577423c9ab1c0c4b1bfc2f175b5cd0b9a8e654d3cd0.jpg)

图片摘要：该图主要展示 3.5 Mode shapes for two degree of freedom example。
![](images/86eb1a318de4ead77ae9165e394252e64ac02c9fb90e4be7a3b1adc8055a7310.jpg)  
Figure 3.5 Mode shapes for two degree of freedom example.

# 3.4.2 Extension to Multiple Degree of Freedom System

The results of the two degree of freedom example can be used to simplify the transformation Equation 3.17. Recognizing the planar characteristics of the model response for the lower frequency modes, Equation 3.17 can be expanded as

$$
\left\{q (t) \right\} = [ \Phi ] \left\{p (t) \right\} = \sum_ {r _ {y}} \left\{\phi \right\} _ {r _ {y}} p _ {r _ {y}} (t) + \sum_ {r _ {p}} \left\{\phi \right\} _ {r _ {p}} p _ {r _ {p}} (t) + \sum_ {r \neq r _ {y}, r _ {p}} \left\{\phi \right\} _ {r} p _ {r} (t) \tag {3.31}
$$

The low frequency yaw modes denoted by $\mathbf{r_y}$ are characterized by rigid body motion of the model. Letting $\{\hat{q}\}$ be the subset of the generalized coordinates required to represent the model fuselage, yields:

$$
\left\{\hat {q} \right\} _ {r _ {y}} = \sum_ {r _ {y}} \left\{\hat {\phi} \right\} _ {r _ {y}} p _ {r _ {y}} (t) = \sum_ {r _ {y}} \left\{ \begin{array}{l} 0 \\ \phi_ {y} \\ 0 \\ 0 \\ 0 \\ \phi_ {\beta} \end{array} \right\} _ {r _ {y}} p _ {r _ {y}} (t) = \sum_ {r _ {y}} \phi_ {\beta r _ {y}} \left\{ \begin{array}{c} 0 \\ - \rho_ {r _ {y}} \\ 0 \\ 0 \\ 0 \\ 1 \end{array} \right\} p _ {r _ {y}} (t) \tag {3.32}
$$

The coordinates shown represent the $x, y, z, \gamma, \alpha$ , and $\beta$ degrees of freedom for a point on the "rigid" model fuselage.

Similarly, for the low frequency pitch plane modes, $\mathbf{r_p}$ , the rigid body motion of the model is approximated by

$$
\left\{\hat {q} \right\} _ {r p} = \sum_ {r p} \left\{\hat {\phi} \right\} _ {r p} p _ {r p} (t) = \sum_ {r p} \left\{ \begin{array}{l} 0 \\ 0 \\ \phi_ {z} \\ 0 \\ \phi_ {\alpha} \\ 0 \end{array} \right\} _ {r p} p _ {r p} (t) = \sum_ {r p} \phi \left\{ \begin{array}{c} 0 \\ 0 \\ - \rho_ {r p} \\ 0 \\ 1 \\ 0 \end{array} \right\} p _ {r p} (t) \tag {3.33}
$$

For a given mode, the rotation and translation degrees of freedom in the predominant plane of motion are related by the mode radius. The mode radius is defined as the ratio of the translation and rotation mode shape coefficients in the predominant plane of motion with the modal vector scaled to unit rotation. This simplified form of the solution, given by Equations 3.32 and 3.33, will be used to develop a correction for vibration induced errors in Chapter 4.

# Chapter 4

# MODEL ATTITUDE BIAS ERROR CORRECTION

# 4.1 Introduction

In this chapter, the theoretical model is used to develop the proposed time domain "modal correction method" for model vibration induced errors in inertial wind tunnel model attitude measurements. The modal correction theory and implementation procedure are described. The proposed modal correction method extends the early work of Fuijkschot [16] to compensate for multiple yaw and pitch vibration modes. This was the first time domain correction technique developed to compensate for multiple modes of vibration in the model pitch and yaw planes. A time domain correction is required due to the short data acquisition periods (1 second) for the random wind tunnel data. This is also important in order to meet future testing needs [21] involving the correlation of instantaneous changes in model attitude and force balance data. The modal correction method also minimizes the number of additional transducers required by using measured modal properties of the wind tunnel model system. This is especially critical for models with limited interior space and in wind tunnels that have extreme temperature conditions where heated instrumentation packages are required.

Prior to the modal correction technique, the model attitude corrections were based on the assumption that the instrumentation package moved on a circular arc with no detailed analysis of the underlying system dynamics. The theoretical and experimental modal

analyses performed during the development of the modal correction technique provided valuable insight into the dynamic behavior of cantilevered wind tunnel model systems. Observation of the relevant animated mode shapes revealed that the model moved as a rigid body on the more flexible sting-balance combination. The assumption of rigid body model motion is critical to the development of multi-mode time domain correction techniques.

# 4.2 Modal Correction Theory

The primary generalized forces are associated with the "quasi-steady" aerodynamic loads acting on the model. Unsteady flow in the wind tunnel results in a broadband random input to the model system. The input for this process is not directly known or measured. For the metallic sting-model structure, the damping is low and the system acts as a narrow band filter passing energy (or responding) at the natural frequencies of the model system [33]. If the modes are well separated and lightly damped, the response motion at a natural frequency, $\omega_{\mathrm{r}}$ , will be described by the corresponding mode shape, $\{\phi\}_{r}$ , with residual effects of other modes assumed negligible.

The physics of the problem can now be studied by considering the response of a single mode as depicted in Figure 4.1. Using Equation 3.32, the response for a single yaw mode in simple harmonic motion can be written

$$
\left\{\hat {q} (t) \right\} = \left\{ \begin{array}{l} x \\ y \\ z \\ \gamma \\ \alpha \\ \beta \end{array} \right\} _ {r _ {y}} = \left\{ \begin{array}{c} 0 \\ \phi_ {y} \\ 0 \\ 0 \\ 0 \\ \phi_ {\beta} \end{array} \right\} _ {r _ {y}} p _ {r _ {y}} (t) = \phi_ {\beta r _ {y}} \left\{ \begin{array}{c} 0 \\ - \rho_ {r _ {y}} \\ 0 \\ 0 \\ 0 \\ 1 \end{array} \right\} P _ {r _ {y}} \sin \left(\omega_ {r _ {y}} t\right) \tag {4.1}
$$

where $P_{r_y}$ is a scalar constant related to the amplitude of motion. The reference coordinates on the rigid fuselage will be taken at the location of the on-board inertial angle of attack (AOA) package. The translation and rotation of the AOA package can then be written

$$
y _ {r _ {y}} (t) = Y _ {r _ {y}} \sin \left(\omega_ {r _ {y}} t\right) \tag {4.2}
$$

$$
\beta_ {r _ {y}} (t) = \frac {1}{- \rho_ {r _ {y}}} y _ {r _ {y}} (t) \tag {4.3}
$$

where $Y_{r_y}$ is a constant representing the amplitude of motion. Taking the derivative with respect to time gives

$$
\dot {y} _ {r _ {y}} (t) = V _ {r _ {y}} \cos (\omega_ {r _ {y}} t) \quad \text {w h e r e} V _ {r _ {y}} = Y _ {r _ {y}} \omega_ {r _ {y}} \tag {4.4}
$$

$$
\dot {\beta} _ {r y} (t) = \frac {1}{- \rho_ {r y}} \dot {y} _ {r y} (t) \tag {4.5}
$$

图片摘要：该图主要展示 4.1 Harmonic motion of model at natural frequency of。
![](images/ae9a501fbe48781cf0045e061cb898679e9bd6827c67a9864e21b4a4f5b1bc6c.jpg)  
Figure 4.1 Harmonic motion of model at natural frequency of $\omega_{\mathrm{ry}}$

The corresponding tangential and normal acceleration components, $a_{t}$ and $a_{n}$ , are:

$$
a _ {t} (t) = \ddot {y} _ {r _ {y}} (t) = A _ {r _ {y}} \sin \left(\omega_ {r _ {y}} t\right); \text {w h e r e} A _ {r _ {y}} = - V _ {r _ {y}} \omega_ {r _ {y}} \tag {4.6}
$$

$$
a _ {n} (t) = \dot {\beta} _ {r y} (t) \dot {y} _ {r y} (t) = \frac {\dot {y} _ {r y} ^ {2} (t)}{- \rho_ {r y}} \tag {4.7}
$$

Substituting for $\dot{y}_{r_y}$ from Equation 4.4 gives

$$
a _ {n} (t) = - \frac {V _ {r _ {y}} {} ^ {2}}{\rho_ {r _ {y}}} \cos^ {2} \left(\omega_ {r _ {y}} t\right) = - \frac {V _ {r _ {y}} {} ^ {2}}{2 \rho_ {r _ {y}}} \left(1 + \cos \left(2 \omega_ {r _ {y}} t\right)\right) \tag {4.8}
$$

Recall from Chapter 1 that the on-board inertial AOA package uses a servo-accelerometer with its sensitive axis parallel to the longitudinal axis of the model. The vibration induced normal acceleration results in the AOA package sensing a centrifugal acceleration coincident with its sensitive axis. The AOA package output prior to filtering, $A_{unf}$ , becomes:

$$
A _ {u n f} (t) = g \sin \alpha + \dot {\beta} _ {r _ {y}} (t) \dot {y} _ {r _ {y}} (t) - a _ {x} (t) \tag {4.9}
$$

The first term on the right hand side of the equation is the gravitational acceleration due to the true model attitude, $\alpha$ , relative to the local vertical. The second term is the centrifugal acceleration (from Equation 4.7) caused by the model yaw motion. The third term represents the accelerations, $a_{x}(t)$ , resulting from flow induced longitudinal model vibrations (typically greater than $50~\mathrm{Hz}$ ). In this equation, the positive output for the AOA package corresponds to a positive change in angle of attack. Using the modal

radius to relate the translation and rotation degrees of freedom (Equation 4.5) of the rigid model, the equation can be written

$$
A _ {u n f} (t) = g \sin \alpha - \frac {\dot {y} _ {r _ {y}} ^ {2} (t)}{\rho_ {r _ {y}}} - a _ {x} (t) \tag {4.10}
$$

Expanding $\dot{y}_{r_y}$ and using the trigonometric relations from Equation 4.8 gives

$$
A _ {u n f} (t) = g \sin \alpha - \frac {V _ {r _ {y}} {} ^ {2}}{2 \rho_ {r _ {y}}} \left(1 + \cos \left(2 \omega_ {r _ {y}} t\right)\right) - a _ {x} (t) \tag {4.11}
$$

This form of the equation shows that the centrifugal acceleration for sinusoidal model response results in the angle of attack sensor having a constant, bias, term and a harmonic component at twice the natural frequency. The harmonic component and the longitudinal acceleration, $a_{x}(t)$ , can be removed by filtering. Lowpass filtering (0.4 Hz cut-off frequency) the AOA signal yields

$$
A _ {f i l} \approx g \sin \alpha - \frac {V _ {r _ {y}} {} ^ {2}}{2 \rho_ {r _ {y}}} \tag {4.12}
$$

The filtered AOA signal, $A_{fil}$ , has a bias error due to model vibration that cannot be removed by filtering or averaging. From Equation 4.12, it is evident that in order to remove the bias error, a correction method that compensates for both the amplitude of vibration, $V_{ry}$ , and the mode shape, $\rho_{ry}$ , is required.

Model pitch vibration causes a similar bias error term, where the tangential velocity is acting in the pitch plane. If the vibration response is composed of multiple yaw and pitch modes, the total bias error will be a linear summation of the error contributions for the $m$ modes.

$$
A _ {f i l} \approx g \sin \alpha - \sum_ {r = 1} ^ {m} \frac {V _ {r} {} ^ {2}}{2 \rho_ {r}} \tag {4.13}
$$

Or, in terms of the peak acceleration, from Equation 4.6,

$$
A _ {f i l} \approx g \sin \alpha - \sum_ {r = 1} ^ {m} \frac {A _ {r} {} ^ {2}}{2 \omega_ {r} {} ^ {2} \rho_ {r}} \tag {4.14}
$$

The above discussion is based on the case of continuous sinusoidal model motion. In the wind tunnel, the data is random in nature. This results in a time varying bias error that is dependent on the number of modes participating and the amplitudes of motion for those modes. In order to compensate for a time varying bias errors, a time domain correction appears to be the most suitable.

The proposed time domain modal correction technique is based on the single mode model given by Equation 4.10. Assuming the model system behaves linearly, the total bias error will be a linear superposition of the individual mode effects. This can be written as

$$
A _ {u n f} (t) = g \sin \alpha - \sum_ {r = 1} ^ {N} \frac {\nu_ {r} ^ {2} (t)}{\rho_ {r}} - a _ {x} (t) \tag {4.15}
$$

where $\nu_{r}(t)$ is the velocity (pitch or yaw plane) at the AOA location for mode r and $\rho_r$ is the corresponding mode radius. For m modes, the bias error estimate, $a_B(t)$ , can be written

$$
a _ {B} (t) = \sum_ {r = 1} ^ {m} \frac {v _ {r} ^ {2} (t)}{\rho_ {r}} \tag {4.16}
$$

Adding the bias error estimate to the unfiltered AOA output yields

$$
A _ {u n f} (t) + \sum_ {r = 1} ^ {m} \frac {v _ {r} ^ {2} (t)}{\rho_ {r}} = g \sin \alpha - \sum_ {r = m + 1} ^ {N} \frac {v _ {r} ^ {2} (t)}{\rho_ {r}} - a _ {x} (t) \tag {4.17}
$$

The longitudinal accelerations, $a_{x}(t)$ , can be removed through low pass filtering. The experimental data in Chapter 5 will show the majority of the dynamic response in the pitch and yaw plane will be concentrated in the first four to six modes. Therefore, the effects of the higher frequency modes (denoted by $r = m + 1$ to $N$ ) will be assumed negligible. An estimate of the true model attitude is given by

$$
\hat {\alpha} (t) \approx \sin^ {- 1} \left(\frac {L P F \left(A _ {u n f} (t) + \sum_ {r = 1} ^ {m} \frac {\nu_ {r} ^ {2} (t)}{\rho_ {r}}\right)}{g}\right) \tag {4.18}
$$

where the accelerations are measured in g's and LPF designates a low pass filter with a cut-off frequency of 0.4 Hertz.

In the modal correction technique, natural frequencies, $\omega_r$ , and mode shapes, $\{\phi\}_r$ must first be determined. This can be done using analytical or experimental techniques. In most cases, a detailed analytical model is not available. Experimental modal analysis

techniques [29, 30] have been used to determine the required natural frequencies, $\omega_r$ , and mode shapes, $\{\phi\}_r$ , of the cantilevered model systems. Recall from Chapter 3 that the low frequency "rigid-model" modes of interest have predominant motion in the pitch or yaw plane due to the model-balance design. This is shown graphically in Figures 4.2 and 4.3. For a given mode, the radius is estimated by assuming the fuselage moves as a rigid body and using a least square linear regression fit of the fuselage mode shape coefficients to determine an effective point of rotation (node). A vibration mode's effective radius is estimated as the distance from the mode's point of rotation to the inertial AOA sensor location in the model fuselage.

The rigid body assumption used in the mode radius estimation appears to be satisfactory for the low frequency ( $< 50\mathrm{Hz}$ ) modes that are being evaluated. The accuracy of the rigid body assumption can be assessed using the correlation coefficient for the linear regression fit of the fuselage mode shape coefficients. For a linear regression fit of a yaw plane mode (see Figure 4.2), the line estimate, $y_{i}$ , is defined by

$$
y _ {i} = a x _ {i} + b \tag {4.19}
$$

The correlation coefficient [34] is defined as

$$
C C _ {r} = \frac {\sum x y - \frac {\sum x \sum y}{n}}{\sqrt {\left(\sum x ^ {2} - \frac {(\sum x) ^ {2}}{n}\right) \left(\sum y ^ {2} - \frac {(\sum y) ^ {2}}{n}\right)}} \tag {4.20}
$$

图片摘要：该图主要展示 4.2 Yaw plane mode of model system。
![](images/5b1070ae332ecd463af58241556b7d78729a960488317841b43fd8107d08b05e.jpg)  
Figure 4.2 Yaw plane mode of model system.

图片摘要：该图主要展示 4.2 Yaw plane mode of model system。
![](images/512755ffe5b5cd7d00dd233115d007c1fb08ee1207349c68504eee1527e0e61d.jpg)  
Figure 4.3 Pitch plane mode of model system.

The correlation coefficient is always between -1 and +1. For values close to zero, there is no linear relationship. For values near $\pm 1$ , there is a very strong linear relationship. In Chapter 5, the correlation coefficient is used to assess the linear regression fit of the measured fuselage mode shape coefficients.

A second assumption is that the mode shapes do not change significantly under the wind tunnel test conditions. This enables wind-off estimates of the mode effective radii to be used for correction of the model attitude measurement during wind tunnel testing. In Appendix A, the effect of aerodynamic forces on the measured modal radius were evaluated using a finite element model of a cantilevered wind tunnel model system. The aerodynamic forces were applied to generate a prestressed model and then the eigensolution was performed for this prestressed loading condition. For the largest aerodynamic forces measured on a representative transport model in the National Transonic Facility, the predicted shifts in the modal radius were less than $4\%$ , which is negligible.

# 4.3 Modal Correction Implementation

Once the effective radius and natural frequency are obtained for each mode of interest, the next step in the modal correction technique is the on-line measurement of the unfiltered AOA signal, and the lateral and normal accelerations at the AOA location. Due to the model attitude accuracy requirements ( $\pm 0.01^{\circ}$ over a range of $\pm 20^{\circ}$ ), a 16-bit analog-to

digital converter is required for the data acquisition system. Once the data is acquired, the digitized measurements are processed off-line using MATLAB® [35].

A flow chart of the data analysis routine is shown in Figure 4.4. The lateral and normal acceleration measurements are numerically integrated using the trapezoidal rule [36] and scaled to obtain the lateral and normal velocity, respectively. The velocity signals are squared using array, or element by element, multiplication. For each lateral mode of interest, a linear phase finite impulse response filter is used to define a passband about the natural frequency. This isolates the velocity squared components of the individual modes. The filters are applied in both the forward and reverse directions to obtain zero-phase distortion and double the filter order. This is critical for a time domain correction where the phase relationship of the unfiltered AOA signal and the lateral and normal dynamic response must be maintained. The squared velocity components for each mode are divided by their corresponding mode radius and then combined using linear superposition to give the estimated bias error due to lateral dynamics. This procedure is then repeated for the normal, or pitch, modes to determine the bias error due to pitch dynamics. The errors due to the lateral and pitch dynamics are then combined using linear superposition to yield the total bias error. The bias estimate is then added to the unfiltered AOA and the result is filtered with a $0.4\mathrm{Hz}$ lowpass filter as described by Equation 4.18. This gives a corrected time varying model attitude signal that can be used to determine the instantaneous or mean angle of attack over the data acquisition period.

图片摘要：该图主要展示 4.4 Flowchart of modal correction method。
![](images/66698f6774c0975e535252ab6213de7bac94144faa18351f13948e09341de72f.jpg)  
Figure 4.4 Flowchart of modal correction method.

图片摘要：该图主要展示 4.4 Flowchart of modal correction method。
![](images/52b612ffbec6c48b1986e5afafd1996a518f91108e01376357cfb2d46418b542.jpg)  
Figure 4.4(continued) Flowchart of modal correction method.

# Chapter 5

# EXPERIMENTAL VERIFICATION

# 5.1 Introduction

In this chapter, the modal correction method is verified through a combination of wind-off dynamic tests on two transport model systems and wind tunnel test data. The modal correction method is applied to wind-off model dynamic response data to compensate for model vibration induced errors in the inertial model attitude measurement for defined shaker inputs in the pitch and yaw plane. In addition, the modal correction method is applied to measured dynamic response data recorded during wind tunnel testing of a high speed transport model in the National Transonic Facility (NTF).

# 5.2 Wind-off Dynamic Response Tests

This section will describe the test setup and results of wind-off dynamic response tests on two transport models [7, 8]. The modal correction method is validated for sinusoidal, modulated sinusoidal and random inputs to the model in the pitch and yaw plane.

# 5.2.1 Test Setup and Procedure

Wind-off dynamic response tests were conducted on two transport models [7, 8] in a model assembly bay at the National Transonic Facility. The test setup for the high speed transport is shown in Figure 5.1. The mounting consists of a "rigidly" supported cantilever sting that is positioned by a pitch-roll-translation mechanism. The model is attached to the sting through a six component strain gage balance.

图片摘要：该图主要展示 5.1 Test setup in model assembly bay。
![](images/40fb375b15164d0d6674397413d506cd612a35b2f9ee55105f10297f2cb1bf57.jpg)  
Figure 5.1 Test setup in model assembly bay.

The model was instrumented with an inertial AOA package [13] maintained at a constant temperature of $160^{\circ}\mathrm{F}$ . The signal conditioner for the AOA package provides both an unfiltered, "dynamic", 0 to $300\mathrm{Hz}$ bandwidth signal, and filtered, "static", 0 to $0.4\mathrm{Hz}$ bandwidth signal. Two miniature accelerometers were installed on the face of the AOA package to measure yaw and pitch motions. In addition, accelerometers were installed at several locations on the model fuselage and sting to measure the dynamic response and natural mode characteristics.

An experimental modal analysis was performed on the model systems. Frequency response function data were acquired for point force excitation and transferred to a personal computer. The STAR® [36] modal analysis software was used to determine the modal parameters from the measured frequency response functions. A least square fit of the fuselage mode shape coefficients was used to estimate the mode radius and corresponding correlation coefficient (see Chapter 4).

For the dynamic response tests, an electrodynamic shaker was used to excite the model system through a single point force linkage as shown in Figure 5.2. Due to the desired high vibration amplitudes, the model surface was protected with tape and safety wire was used in case the glue attaching the force mounting block failed during testing. The excitation was applied in the pitch and yaw planes at the model fuselage hard points. Sine, modulated sine and band limited random shaker input were used. A Hewlett Packard (HP) 3566A dynamic signal analyzer was used to provide the shaker stimulus and record the shaker force input, model force balance outputs, AOA static and dynamic

图片摘要：该图主要展示 5.1 Test setup in model assembly bay。
![](images/9b566504118628f6e3271e7fc11af274c27568e37b228db8017cd8df0468c28c.jpg)  
Figure 5.2 Shaker attachment for excitation in the yaw plane.

outputs, and model accelerations. This system was used to monitor the model yaw and pitch moments which established the dynamic test conditions for acquiring model attitude measurements. Data was also recorded using a 16-bit Analog to Digital Converter (ADC) board in a personal computer.

The model was set at a prescribed angle of attack under static conditions. The model system natural frequencies were identified using sine sweep excitation in the pitch and yaw planes. For each natural frequency of interest, a sinusoidal forced response test was conducted by controlling the shaker input amplitude to provide a defined peak to peak pitch or yaw moment on the model force balance. The control test variables were pitch moment for modes that had predominantly pitch motion, and yaw moment for modes that had predominantly yaw motion. The model attitude was measured at a series of moment amplitude levels for sinusoidal excitation at a prescribed natural frequency of the model system.

In addition to the sinusoidal forced response tests, the high speed transport model dynamic response was measured for modulated sine and random excitation. The modulated sine and random excitations and responses are more representative of the model dynamics observed in actual wind tunnel tests. The majority of the modulated sine tests were conducted with a $0.25\mathrm{Hz}$ modulation of the first natural frequency in the pitch and yaw planes. In each case, the inertial AOA package was used to measure the model attitude for a series of moment amplitude levels.

# 5.2.2 Commercial Transport Model Test Results

During wind tunnel tests, the commercial transport model had significant yaw vibrations at 14 Hertz. Discrepancies in the aerodynamic data provided the stimulus for the investigation of the AOA device [7] and its sensitivity to model vibrations. The AOA investigation concentrated on the first four modes. An experimental modal analysis was conducted on the model system and the results are tabulated in Table 5.1. Figures 5.3 and 5.4 show characteristic yaw plane modes described by sting bending and balance rotation. The mode radii and corresponding correlation coefficients are also listed in the table. Recall from Chapter 4 that correlation coefficients near $\pm 1$ indicate a very strong linear relationship. The correlation coefficient for the least square fit of the fuselage mode shape coefficients shows the appropriateness of the linear regression fit and validates the rigid body model assumption for the tabulated modes.

Table 5.1 Modal Parameters for Commercial Transport Model   

<table><tr><td>Mode
No.</td><td>Frequency
(Hz)</td><td>Damping
(%)</td><td>Radius
(Inch)</td><td>Corr.
Coeff.</td><td>Mode Description</td></tr><tr><td>1</td><td>10.3</td><td>1.01</td><td>38.2</td><td>.9998</td><td>Sting Bending-Yaw Plane</td></tr><tr><td>2</td><td>11.2</td><td>1.78</td><td>70.5</td><td>.9971</td><td>Sting Bending-Pitch Plane</td></tr><tr><td>3</td><td>14.4</td><td>0.46</td><td>7.05</td><td>-.9973</td><td>Model Yaw on Balance</td></tr><tr><td>4</td><td>16.5</td><td>0.59</td><td>12.0</td><td>.9998</td><td>Model Pitch on Balance</td></tr></table>

图片摘要：该图主要展示 5.3 Sting bending in yaw plane, vibration mode。
![](images/12a3a2a120acf172996dba7ba6a210b934db1a31bbc248d6937447ec0e66c483.jpg)  
Figure 5.3 Sting bending in yaw plane, $10.3\mathrm{Hz}$ vibration mode.

图片摘要：该图主要展示 5.3 Sting bending in yaw plane, vibration mode。
![](images/e4492f563b05991ab49ef153a4bed775a9b900dd2c39bcca32785252399475a5.jpg)  
Figure 5.4 Model yawing on balance, $14.4\mathrm{Hz}$ vibration mode.

For the AOA investigation, the model system was locked at near zero degree angle of attack under static conditions. Single frequency forced response tests were conducted by controlling the shaker input to provide a defined peak to peak pitch or yaw moment on the model force balance. The test variable was yaw moment for modes that had predominantly yaw motion, and pitch moment for modes that had predominantly pitch motion. The AOA response data and model accelerations were recorded for several moment levels. This data was transferred to the MATLAB® [35] program for application of the modal correction technique. The measured mean AOA output, estimated bias, and corrected mean AOA output, after application of the modal correction technique, are shown versus balance moment in Figures 5.5 through 5.8. Recall that for sinusoidal input, the model vibration creates a bias error or offset in the mean value. After application of the modal correction technique, the error is reduced to the AOA device accuracy of $\pm 0.01$ degrees for all measurements except the second pitch mode. For this case, an order of magnitude reduction is obtained.

The accuracy of the correction for the pitch axis tests may be improved by locating the accelerometers adjacent to or inside the heated AOA package. The pitch plane accelerometer on the face of the AOA package failed early in the test. A triax set of accelerometers located externally on the fuselage upper surface was subsequently used to obtain the off-axis accelerations required for the modal correction technique.

图片摘要：该图主要展示 5.4 Model yawing on balance, vibration mode。
![](images/e8e5e34a10f5cca50e594b21b4cd35b00dde4d77a3188defe2d636bd18ce84b4.jpg)  
Figure 5.5 Measured mean AOA, estimated bias, and corrected mean AOA versus yaw moment for sinusoidal input at $10.3\mathrm{Hz}$

图片摘要：该图主要展示 5.5 Measured mean AOA, estimated bias, and corrected mean AO。
![](images/0d1fa8ab4f3fb6dd8608cab8f07fb49abc2c03c841f493235660f1689a9f19a7.jpg)  
Figure 5.6 Measured mean AOA, estimated bias, and corrected mean AOA versus yaw moment for sinusoidal input at $14.4\mathrm{Hz}$

图片摘要：该图主要展示 5.6 Measured mean AOA, estimated bias, and corrected mean AO。
![](images/97603145675caa676a9f706a706af9752b769bb7373b1d980a44931da053d8ac.jpg)  
Figure 5.7 Measured mean AOA, estimated bias, and corrected mean AOA versus pitch moment for sinusoidal input at $11.2\mathrm{Hz}$

图片摘要：该图主要展示 5.7 Measured mean AOA, estimated bias, and corrected mean AO。
![](images/a607b69c4aa68d4c02edfd3f8a503c589f6516ec0d974cad5212117982d11c21.jpg)  
Figure 5.8 Measured mean AOA, estimated bias, and corrected mean AOA versus pitch moment for sinusoidal input at $16.2\mathrm{Hz}$

# 5.2.3 High Speed Transport Model Test Results

A high speed transport model system that experienced high levels of vibration [6] during previous wind tunnel tests was selected to further investigate the effects of dynamics on the inertial AOA package. Measurements taken during wind tunnel tests indicated that the primary modes being excited were at approximately $8 - 10\mathrm{Hz}$ and $28 - 30\mathrm{Hz}$ [6]. An experimental modal analysis of the model system was conducted and the results are listed in Table 5.2. The radii and corresponding correlation coefficients for the vibration modes were estimated using a least square linear regression fit of the modal deformations as described in Chapter 4. The correlation coefficient for the least square fit of the fuselage mode shape coefficients shows the appropriateness of the linear regression fit and validates the rigid body model assumption for the tabulated modes.

Table 5.2 Modal Parameters of High Speed Transport Model   

<table><tr><td>Mode
No.</td><td>Frequency
(Hz)</td><td>Damping
(%)</td><td>Radius
(Inch)</td><td>Corr.
Coeff.</td><td>Mode Description</td></tr><tr><td>1</td><td>9.0</td><td>1.32</td><td>31.0</td><td>.9997</td><td>Sting Bending-Yaw Plane</td></tr><tr><td>2</td><td>9.2</td><td>1.68</td><td>30.2</td><td>.9997</td><td>Sting Bending-Pitch Plane</td></tr><tr><td>3</td><td>20.5</td><td>2.75</td><td>0.18</td><td>-.9993</td><td>Model Yaw on Balance</td></tr><tr><td>4</td><td>21.7</td><td>2.70</td><td>-1.07</td><td>.9999</td><td>Model Pitch on Balance</td></tr><tr><td>5</td><td>29.8</td><td>2.28</td><td>-7.16</td><td>-.9983</td><td>Model Yaw on Balance
with Sting Second Bending</td></tr><tr><td>6</td><td>34.9</td><td>2.59</td><td>-7.65</td><td>0.9999</td><td>Model Pitch on Balance
with Sting Second Bending</td></tr></table>

It is important to note that the mode radius may be positive or negative dependent on the vibration mode shape. Previously, this bias error was described as a "sting whip" [13] error and associated with the first sting bending modes in the pitch and yaw planes. The analyses and experimental data presented in this dissertation show that the model system dynamics is more complex than previously assumed. The physical interpretation of the sign of the radius is more easily understood by examining the $9.0\mathrm{Hz}$ and $29.8\mathrm{Hz}$ yaw modes shown in Figures 5.9 and 5.10. For the case where the radius is negative, the point of rotation for the vibration mode is forward of the AOA package. A positive radius is defined for a point of rotation aft of the AOA package.

The significance of the sign of the radii is that the bias error may be positive or negative dependent upon the vibration mode being excited. This is demonstrated by the response of the two yaw plane modes shown in Figures 5.11 and 5.12. For the $9.0\mathrm{Hz}$ yaw mode, the indicated model angle change is negative when the model is being driven with sinusoidal excitation at the natural frequency and then returns to its nominal angle when the shaker system is shutoff. The $29.8\mathrm{Hz}$ yaw mode, which has a negative radius value, shows an indicated positive angle change when the model is being driven with sinusoidal excitation at the natural frequency and then returns to its nominal angle when the shaker system is shutoff. The excitation system was adequate to show the above trends, however, only the first mode in each the yaw and pitch planes were excited to levels that showed significant shifts in the indicated model attitude from the onboard inertial AOA package. Difficulty in driving the higher frequency modes is attributed to the rigid

图片摘要：该图主要展示 5.10 Model yawing on balance, vibration mode。
![](images/00fcba6f7c4ffe3543e5c07e03de578ee84215460009b4e5d9fc6fe2bed185a1.jpg)

图片摘要：该图主要展示 5.10 Model yawing on balance, vibration mode。
![](images/2dbddd9c39499b3482b1f4cd35ad7476d12fcaa6ee04be07d9ea16d40572f1a6.jpg)  
Figure 5.10 Model yawing on balance, $29.8\mathrm{Hz}$ vibration mode.

图片摘要：该图主要展示 5.10 Model yawing on balance, vibration mode。
![](images/1db82fea8217636eb6101a6310db8e6fb747ce55a19d8f699a36135a148604d0.jpg)

图片摘要：该图主要展示 5.10 Model yawing on balance, vibration modeYaw Acceleration。
![](images/07cf7eb0a5a9a2c1c7836fe157decbd6205964953970cdf57d86e40f02e28752.jpg)  
Yaw Acceleration   
Yaw Moment

图片摘要：该图主要展示 5.10 Model yawing on balance, vibration mode。
![](images/3c32bd6cc99956c38dcfafff47e1576e0bd57c58208af933136a32e3f4740502.jpg)  
Figure 5.11 Inertial AOA measurement, yaw acceleration, and yaw moment versus time for $9.0\mathrm{Hz}$ sinusoidal input in yaw plane.

图片摘要：该图主要展示 5.11 Inertial AOA measurement, yaw acceleration, and yaw mom。
![](images/71ac1a1790c891562cf0d147d72ce78599a149b261337eefad2533d4bc29e101.jpg)

图片摘要：该图主要展示 5.11 Inertial AOA measurement, yaw acceleration, and yaw mom。
![](images/69c498c361e72214147e864dac599f1f662f2a77fb63777bbffe451ce0735a11.jpg)

图片摘要：该图主要展示 5.11 Inertial AOA measurement, yaw acceleration, and yaw mom。
![](images/734787350814552babec2803a4ffe05032adb3f565c2f8e03442504235278153.jpg)  
Figure 5.12 Inertial AOA measurement, yaw acceleration, and yaw moment versus time for $29.8\mathrm{Hz}$ sinusoidal input in yaw plane.

backstop support in the model assembly bay. During previous wind tunnel tests [6], the model coupled with the model support structure resulting in high dynamic yaw moments with energy in the $28 - 30\mathrm{Hz}$ band. This points out the need to do dynamic testing with the model installed in the tunnel.

The results of sinusoidal excitation tests for the first mode in each the yaw and pitch plane are shown in Figures 5.13 and 5.14. The model was set at a nominal angle of $0^{\circ}$ for these tests. For a set excitation level, time domain data were acquired and stored using the dynamic signal analyzer. These data were transferred to a personal computer where the modal correction technique, implemented in an m-file in the MATLAB® [35] language, was used to estimate the bias error in the inertial device. This procedure was repeated for several excitation levels as defined by the moment amplitude level.

As shown in Figures 5.13 and 5.14, the estimated bias error is in good agreement with the indicated mean angle change measured with the onboard inertial AOA sensor. After application of the modal correction method, the bias error is reduced from a maximum of $-0.146^{\circ}$ to $-0.009^{\circ}$ for the first mode in the yaw plane and from $-0.175^{\circ}$ to $-0.006^{\circ}$ for the first mode in the pitch plane. These corrected mean angle of attack values are within the AOA accuracy requirement of $0.01^{\circ}$ . Similar results were obtained for sinusoidal input tests with the model set to nominal angles of $4.3^{\circ}$ and $6^{\circ}$ .

图片摘要：该图主要展示 5.12 Inertial AOA measurement, yaw acceleration, and yaw mom。
![](images/05304b74a052f3192817c59abc6c30f2b6e1bc3da4f1c30e4bde929126d34812.jpg)  
Figure 5.13 Measured mean AOA, estimated bias, and corrected mean AOA versus yaw moment for sinusoidal input at $9.0\mathrm{Hz}$

图片摘要：该图主要展示 5.13 Measured mean AOA, estimated bias, and corrected mean A。
![](images/6b6a7bd575f67296f448f76cea3b5014753282527fc247ed431bb6ce0e201ca3.jpg)  
Figure 5.14 Measured mean AOA, estimated bias, and corrected mean AOA versus pitch moment for sinusoidal input at $9.2\mathrm{Hz}$

In order to obtain a corrected time domain angle of attack measurement that can be used for instantaneous or average values, it is important to maintain the phase relationship between the measured and estimated bias error. To verify that the modal correction method maintains this phase relationship, the bias error was examined for modulated sine and random inputs. The measured response for modulated sine and random inputs is also more representative of actual wind tunnel test data.

Figure 5.15 shows the measured angle of attack and estimated bias error as a function of time for a $9.2\mathrm{Hz}$ pitch excitation with a $0.25\mathrm{Hz}$ modulation. Excellent agreement is obtained with the difference between the measured angle of attack and estimated bias error being less than $0.005^{\circ}$ . Modulated sine tests were conducted at several excitation amplitude levels for the first mode in each the y and z axes and consistent results were obtained between the measured angle of attack and predicted bias errors for all cases.

In addition, the response of the AOA package for two levels of random excitation in the pitch plane were also examined. Figure 5.16 shows an eight second record of the inertial AOA sensor response for the highest level random excitation. The random response measured by the pitch accelerometer on the face of the AOA package was composed of primarily $9.2\mathrm{Hz}$ response. The bias error estimate based on only the $9.2\mathrm{Hz}$ mode contribution is also shown in Figure 5.16. Again, the measured angle of attack and estimated bias error are in very good agreement.

图片摘要：该图主要展示 5.15 shows the measured angle of attack and estimated bias e。
![](images/e246a7d30567fd6e3b1e60e8194dc1d183cb0d818689e56aa334f82605802a88.jpg)  
Figure 5.15. (Top) Measured AOA and estimated bias error for $9.2\mathrm{Hz}$ sinusoidal excitation in pitch with $0.25\mathrm{Hz}$ modulation. (Bottom) Corresponding measured balance pitch moment.

图片摘要：该图主要展示 5.15. (Top) Measured AOA and estimated bias error for sinuso。
![](images/07aa8029d725e962fc377bf230a3533620734263cdaf451ffa185518ab2ff431.jpg)  
Figure 5.16. (Top) Measured AOA and estimated bias error for random excitation in pitch. (Bottom) Corresponding measured balance pitch moment.

# 5.3 High Speed Transport Model Wind Tunnel Tests

Dynamic response studies were conducted on a high speed transport model installed in the test section of the NTF. The dynamic response characteristics were also recorded for high speed (Mach=0.95) wind tunnel runs.

# 5.3.1 Test Setup in Wind Tunnel

The model was instrumented with a re-designed inertial AOA package that has two servo-accelerometers for measuring model AOA and two dynamic accelerometers to measure the accelerations tangent to the sensitive axis of the AOA sensors. The package is maintained at a constant temperature of $160^{\circ}\mathrm{F}$ . The signal conditioner for the AOA sensors provide both an unfiltered, dynamic, 0 to $300\mathrm{Hz}$ bandwidth signal and a filtered, static, 0 to $0.4\mathrm{Hz}$ bandwidth signal.

Initial wind-off dynamic response studies were performed in the wind tunnel test section using shaker excitation of the model with the arc sector in a fixed position. For the windoff shaker excitation tests, six additional accelerometers were mounted external to the model fuselage to measure model yaw and pitch motion at three locations.

Data were acquired using a 16 channel digital data acquisition system with 16-bit resolution. All dynamic signals were filtered to $100\mathrm{Hz}$ prior to recording. Data were recorded at 200 samples per second per channel. Recorded channels included the dynamic and static inertial AOA outputs, the tangential accelerations in yaw and pitch, and the six

force balance components. Data were recorded for both the wind-off shaker excitation tests and the high speed wind tunnel runs.

For the wind-off shaker excitation tests, a Hewlett Packard model 3566A dynamic signal analyzer was used to provide the shaker stimulus and perform on-line time and frequency domain signal analysis. The 16 channel signal analyzer was used to monitor and record the shaker force input, and the response of the six accelerometers mounted external to the model fuselage.

The shaker excitation tests were performed with the model installed in the test section and the arc sector in a fixed position. An electrodynamic shaker was used to excite the model in the yaw plane through a single point force linkage 13 inches aft of the model nose. Due to schedule constraints, the forced response tests were conducted in the yaw plane only. The model system natural frequencies were identified using sine sweep excitation. The dynamic and static inertial AOA outputs, the tangential accelerations in yaw and pitch, and the six force balance components were recorded for a series of shaker force amplitude levels for sinusoidal excitation at a prescribed natural frequency of the model system. In addition to the sinusoidal forced response tests, modulated sine excitation tests were performed for a series of shaker force levels. The modulated sine excitations and responses are more representative of the model dynamics observed in actual wind tunnel tests.

For a given test condition, time domain data were acquired and stored on the 16-channel data acquisition system. These data were transferred to a personal computer where a software routine implementing the modal correction method, written as an M-file in the MATLAB® [35] language, was used to estimate and correct for the bias error in the inertial device.

# 5.3.2 Dynamic Response Tests in Wind Tunnel

An experimental modal analysis was performed for a high speed research model installed in the NTF wind tunnel and the dominant modes are listed in Table 5.3. The model was configured differently than in previous wind-off vibration tests, therefore, the modal characteristics are different than those presented in the previous section. The mode radii and corresponding correlation coefficients are also listed in the table. The correlation coefficients again confirms the rigid body model assumption.

Table 5.3   
Modal Parameters for Survey of High Speed Transport Model in Test Section   

<table><tr><td>Mode
No.</td><td>Frequency
(Hz)</td><td>Damping
(%)</td><td>Radius
(Inch)</td><td>Corr.
Coeff.</td><td>Mode Description</td></tr><tr><td>1</td><td>7.3</td><td>0.46</td><td>37.8</td><td>.9992</td><td>Sting Bending-Yaw Plane</td></tr><tr><td>2</td><td>9.8</td><td>0.28</td><td>31.8</td><td>.9995</td><td>Sting Bending-Pitch Plane</td></tr><tr><td>3</td><td>12.1</td><td>0.51</td><td>8.71</td><td>.9995</td><td>Sting/Model Yaw</td></tr><tr><td>4</td><td>16.9</td><td>1.3</td><td>-0.93</td><td>-.9985</td><td>Model Pitch on Balance</td></tr><tr><td>5</td><td>17.2</td><td>1.0</td><td>-3.40</td><td>-.9998</td><td>Model Yaw on Balance</td></tr><tr><td>6</td><td>21.1</td><td>0.36</td><td>-9.54</td><td>-.9994</td><td>Model Yaw, 2nd Sting Bending</td></tr></table>

The results of sinusoidal excitation tests for the first mode (7.3 Hz) in the yaw plane are shown in Figure 5.17. This figure shows the angle of attack measured with the primary servo-accelerometer sensor and the corrected angle of attack after removal of the dynamically induced bias error. These tests were conducted with the model at a nominal angle of $6.01^{\circ}$ and the arc sector in a fixed position. After application of the modal correction method, the error is reduced from a maximum of $-0.087^{\circ}$ to $+0.003^{\circ}$ for the first mode in the yaw plane. As shown in Figure 5.17, the corrected AOA measurements are within the AOA accuracy requirement of $+/- 0.01^{\circ}$ . The higher frequency modes were not excited to high enough levels to produce significant shifts in the AOA measurements during the wind-off vibration tests.

In addition to the sinusoidal tests, the bias error was examined for modulated sine input. Figure 5.18 shows the angle of attack measured with the primary servo-accelerometer sensor and the corrected angle of attack after removal of the dynamically induced bias error. This data was obtained for excitation at the $7.3\mathrm{Hz}$ natural frequency with a $0.5\mathrm{Hz}$ modulation. The corresponding measured yaw moment is also shown in Figure 5.18 and has a maximum peak-to-peak value of 2400 in-lbs. Excellent correction is obtained using the modal correction method with errors as large as $-0.091^{\circ}$ being reduced to less than $+/-0.005^{\circ}$ from the nominal angle. Modulated sine tests were conducted for the first mode at several excitation amplitude levels and consistent results were obtained. For this type of model response, correction for the dynamically induced errors results in a shift in the mean value and a reduction in the variance of the signal.

图片摘要：该图主要展示 5.17. Measured and corrected angle of attack for sinusoidal 。
![](images/2a508ddd2d1eb9d4536af4c1599939116e97706489c08b792756c3dbc0e39931.jpg)  
Figure 5.17. Measured and corrected angle-of-attack for sinusoidal excitation at $7.3\mathrm{Hz}$ .

图片摘要：该图主要展示 5.17. Measured and corrected angle of attack for sinusoidal 。
![](images/d88db89a74316cd5ad5fbc06c48d52858c83d449ee57988b9027dbdeb510facb.jpg)  
Figure 5.18. (Top) Measured and corrected AOA for sinusoidal excitation at $7.3\mathrm{Hz}$ with $0.5\mathrm{Hz}$ modulation. (Bottom) Corresponding balance yaw moment.

# 5.3.3 Wind Tunnel Test Results

The data for the first 64 seconds of a test on the high speed transport model (Mach=0.95, Q=1800 pounds-per-square-foot, T=-254°F) were used to evaluate the dynamic response characteristics of the primary AOA sensor and the proposed modal correction method. The filtered output of the primary AOA is shown in Figure 5.19. Data analysis was restricted to the periods where the model pitch angle was paused to obtain "steady-state" aerodynamic data. The pitch acceleration was significantly lower than the yaw acceleration over the data analysis period. Analysis of the model yaw acceleration showed primarily 7.3 Hz response with additional energy at the 12.1 Hz natural frequency. Intermittent response at other frequencies was observed. Initial application of the modal correction method included the modes in Table 5.3. The AOA mean value and standard deviation over each pause period are listed in Table 5.4.

Table 5.4   
Summary of Wind Tunnel Results   

<table><tr><td>Time Period (Seconds)</td><td>Measured AOA Mean (Degrees)</td><td>Measured AOA Standard Deviation (Degrees)</td><td>Corrected AOA Mean (Degrees)</td><td>Corrected AOA Standard Deviation (Degrees)</td></tr><tr><td>0 to 9.25</td><td>-3.5664</td><td>0.0179</td><td>-3.5403</td><td>0.0121</td></tr><tr><td>12.5 to 32.5</td><td>-2.5094</td><td>0.0203</td><td>-2.4764</td><td>0.0082</td></tr><tr><td>40.75 to 52.5</td><td>-1.4803</td><td>0.0248</td><td>-1.4392</td><td>0.0088</td></tr><tr><td>56 to 64</td><td>-0.9308</td><td>0.0094</td><td>-0.9121</td><td>0.0057</td></tr></table>

图片摘要：该图主要展示 5.4。
![](images/9c71ce23a8e054e59e72c7bac4b27c3194d180bce303a0b1368b1fd147548679.jpg)  
Figure 5.19. Angle-of-Attack (AOA) for first sixty-four seconds of wind tunnel test on high speed transport model.

Figures 5.20 through 5.23 show the time domain response of the angle of attack measured with the primary servo-accelerometer sensor and the corrected angle of attack after removal of the dynamically induced bias error for each pause period. There were no optical measurements to confirm the corrected AOA measurements.

Since the response was primarily at the $7.3\mathrm{Hz}$ and $12.1\mathrm{Hz}$ natural frequencies, which have positive radii, trends consistent with the wind-off modulated sine test are expected. For a mode with a positive radius and fluctuating amplitude of motion, correction for dynamically induced errors will result in a positive shift in the mean value and a reduced variance for the corrected signal. The significant reduction in the variation observed in the corrected time domain AOA signal (Figures 5.20-5.23) as compared to the measured primary AOA and the corresponding reduction in the standard deviation for the corrected AOA measurement indicate successful application of the modal correction method. The periods from 12.5 to 32.5 seconds and 40.75 to 52.5 seconds (part of which are shown in Figures 5.21 and 5.22) are the best indicators of the amount of bias reduction possible. The inclusion of more natural frequencies in the modal correction method may aid in improving the bias correction. It is also important to note that the low frequency fluctuations in the corrected AOA signal may be due in part to oscillatory changes in the model pitch attitude.

图片摘要：该图主要展示 s 5.20 through 5.23 show the time domain response of the ang。
![](images/f83b7b64a1dc3dc1ba4e13779b2ec8e272650e8051dc89e61f3ed105210c0189.jpg)  
Aooaa (Oooss)

(s) t-1) 1000 Mx   
图片摘要：该图主要展示 s 5.20 through 5.23 show the time domain response of the ang。
![](images/02070fc951784bdf5babe8920cf2308426385fe1f220878df8e8adecf322e1f8.jpg)  
Figure 5.20. (Top) Time domain response of the AOA measured with the servo-accelerometer and the corrected AOA after removal   
of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment.

图片摘要：该图主要展示 5.20. (Top) Time domain response of the AOA measured with th。
![](images/1735501abbed78095cc5e081511817fd14ffe26ca63ec14ba9d3cee814313db4.jpg)  
Figure 5.21. (Top) Time domain response of the AOA measured with the servo-accelerometer and the corrected AOA after removal   
of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment.

图片摘要：该图主要展示 5.21. (Top) Time domain response of the AOA measured with th。
![](images/7a2b582df68ba7217320ff1ce35f28803f6b3f15fa60ecb39cddd15723f0ee8d.jpg)  
Figure 5.22. (Top) Time domain response of the AOA measured with the servo-accelerometer and the corrected AOA after removal   
of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment.

图片摘要：该图主要展示 5.22. (Top) Time domain response of the AOA measured with th。
![](images/0aed96b1456505622fb082ef69dbf6d60d78c3cea33dcf5d2e59d81786bbd10b.jpg)  
Figure 5.23. (Top) Time domain response of the AOA measured with the servo-accelerometer and the corrected AOA after removal of the dynamically induced bias error. (Bottom) Corresponding time domain measurement of yaw moment.

For this test, the data acquisition periods were longer than normal. The steady state data at NTF is typically taken over a 1 second period. Differences between the corrected and measured mean values over a given one second interval may be much larger than those shown in Table 5.4. The results for one second intervals from 16 to 22 seconds are listed in Table 5.5. Differences between the measured and corrected AOA mean value as large as $-0.64^{\circ}$ are observed over the selected one second intervals.

Table 5.5   
Summary of Wind Tunnel Results for One Second Data Acquisition Periods   

<table><tr><td>Time Period (Seconds)</td><td>Measured AOA Mean (Degrees)</td><td>Corrected AOA Mean (Degrees)</td><td>Difference Measured -Corrected (Degrees)</td></tr><tr><td>16 to 17</td><td>-2.531</td><td>-2.473</td><td>-0.058</td></tr><tr><td>17 to 18</td><td>-2.513</td><td>-2.483</td><td>-0.030</td></tr><tr><td>18 to 19</td><td>-2.508</td><td>-2.478</td><td>-0.030</td></tr><tr><td>19 to 20</td><td>-2.550</td><td>-2.486</td><td>-0.064</td></tr><tr><td>20 to 21</td><td>-2.540</td><td>-2.481</td><td>-0.059</td></tr><tr><td>21 to 22</td><td>-2.511</td><td>-2.487</td><td>-0.024</td></tr></table>

# Chapter 6

# CONCLUDING REMARKS

An original system dynamic analysis approach is presented to evaluate the effects of model vibrations on measured aerodynamic wind tunnel data. Analytical and experimental results show that centrifugal accelerations associated with model vibration cause bias errors in the inertial model attitude measurements. Wind-off dynamic response tests on two transport model systems found bias errors over an order of magnitude greater than the required device accuracy. An analysis is presented that shows these errors cannot be removed by filtering or averaging. Equations are developed to show the influence of the model attitude errors on the determination of the drag coefficient.

A new time domain technique is developed to correct for the dynamically induced errors in the inertial model attitude measurements using measured modal properties of the model system. This modal technique extends previous work to compensate for multiple modes in the pitch and yaw plane. Previously, the problem was associated with "sting whip" with no detailed analysis of the underlying system dynamics. Dynamic response tests on two transport models in a laboratory environment demonstrated the need to compensate for multiple modes. Theoretical and experimental modal analyses are presented to provide physical insight into the model system dynamics. Based on observed rigid body model motion for the low frequency modes of interest, the problem is simplified. For a planar rigid body model mode, analysis shows that the fuselage motion can be completely described by a translation and rotation degree of freedom. A mode

radius is defined to relate the translation and rotation degrees of freedom using analytical or experimental mode shapes. Analyses are presented that show the mode radii are not affected significantly by the aerodynamic loads experienced in a high dynamic pressure wind tunnel environment. A correlation coefficient is defined and used to validate the rigid body model assumption.

Due to short data acquisition periods and the multi-mode random response observed in wind tunnels, state of the art digital signal processing techniques are required to implement the modal correction method in the time domain. Bandpass filters are used to isolate the effects of individual modes and then the mode effects are combined using the principle of superposition. During the filtering processes, the phase relationship of the unfiltered model attitude signal and the model dynamic response must be maintained. To achieve zero-phase distortion, finite impulse response filters are applied in both the forward and reverse directions. The modal correction method compensates for the dynamically induced bias error and provides a corrected model attitude time signal that can be used to correlate with time varying changes in the balance forces

The modal correction method is verified through a series of wind-off dynamic response tests and actual wind tunnel test data. The wind-off dynamic response tests show the method has the ability to reduce the bias error in the inertial model attitude device by over an order of magnitude to achieve the required device accuracy.

Theoretical and experimental results are presented that demonstrate the need to correct for dynamically induced errors in inertial wind tunnel model attitude measurements. A correction method requiring four additional transducers was developed and implemented at the National Aerospace Laboratory in the Netherlands. A principal advantage of the modal correction technique is that it minimizes the number of required transducers (two) using the modal properties of the model system. This is especially critical for models with limited interior space and in wind tunnels that have extreme temperature conditions where heated instrumentation packages are required. Recently redesigned instrumentation packages for the National Transonic Facility (NTF) provide the two additional transducers required for the modal correction method. Currently, facilities in the United States have not implemented a correction.

Future research of wind tunnel model system dynamics and its effects on measured aerodynamic data is recommended in the following areas: (1) Perform a statistical analysis to evaluate the significance of the magnitude of the angle of attack correction with respect to the measured standard deviation, and small angle assumption for high angles of attack; (2) Perform a study of the cross axis sensitivity of the inertial attitude sensor, and the effects of model roll motions; (3) Perform a study of alternate signal processing methods, such as modulation techniques, for removing the dynamically induced errors in the inertial model attitude measurements; (4) Based on the observed rigid body model behavior, perform a parametric study to evaluate changes in dynamic response for variations in: mass or mass distribution of the model; balance stiffness and

damping; and sting material properties. This research would be aimed at developing design criteria for model systems that would minimize the model dynamic response and move closer to the desired steady-state wind tunnel test conditions. Further enhancements may be found in the use of active vibration control techniques to suppress the model vibrations.

# Chapter 7

# REFERENCES

[1] Young, C. P., Jr.: "Model Dynamics", AGARD Special Course on Cryogenic Wind Tunnels, 1996.   
[2] Fuller, D. E.: "Guide to Users of the National Transonic Facility", NASA TM-83124, July, 1981.   
[3] Strganac, T. W.: "A Study of the Aeroelastic Stability for the Model Support System of the National Transonic Facility", AIAA-88-2033, 1988.   
[4] Whitlow, W., Jr.; Bennet, R. M.; and Strganac, T. W.: "Analysis of Vibrations of the National Transonic Facility Model Support System Using a 3-D Aeroelastic Code", AIAA-89-2207, 1989.   
[5] Young, C. P., Jr.; Popernack, T. G., Jr.; Gloss, B. B.: "National Transonic Facility Model and Model Support Vibration Problems", AIAA-90-1416, 1990.   
[6] Buehrle, R. D.; Young, C. P., Jr.; Balakrishna, S.; and Kilgore, W. A.: "Experimental Study of Dynamic Interaction Between Model Support Structure and a High Speed Research Model in the National Transonic Facility", AIAA-94-1623, 1994.   
[7] Young, C. P., Jr.; Buehrle, R. D.; Balakrishna, S.; and Kilgore, W. A.: "Effects of Vibration on Inertial Wind-Tunnel Model Attitude Measurement Devices". NASA Technical Memorandum 109083, August, 1994.   
[8] Buehrle, R. D.; Young, C. P., Jr.; Burner, A. W.; Tripp, J. S.; Tcheng, P.; Finley, T. D.; and Popernack, T. G., Jr.: "Dynamic Response Tests of Inertial and Optical Wind-Tunnel Model Attitude Measurement Devices", NASA Technical Memorandum 109182, February, 1995.   
[9] Pope, A.; and Goin, K. L.: High Speed Wind Tunnel Testing, John Wiley & Sons, Inc., New York, 1965.   
[10] Muhlstein, L., Jr.; and Coe, C. F.: "Integration Time Required to Extract Accurate Data from Transonic Wind-Tunnel Tests", Journal of Aircraft, Volume 16, No. 9, pp 620-625, September 1979.   
[11] Mabey, D. G.: "Flow Unsteadiness and Model Vibration in Wind Tunnels at Subsonic and Transonic Speeds", Royal Aircraft Establishment Technical Report 70184, October, 1970.

[12] Steinle, F. and Stanewsky, E.: "Wind Tunnel Flow Quality and Data Accuracy Requirements", Advisory Group for Aerospace Research and Development (AGARD) Advisory Report No. 184, November, 1982.   
[13] Finley, T., and Tcheng, P.: "Model Attitude Measurements at NASA Langley Research Center", AIAA-92-0763, 1992.   
[14] Burt, G. E., and Uselton, J. C.: "Effect of Sting Oscillations on the Measurement of Dynamic Stability Derivatives in Pitch and Yaw", AIAA Paper No. 74-612, July, 1974.   
[15] Billingsley, J. P.: "Sting Dynamics of Wind Tunnel Models", Arnold Engineering Development Center Report Number: AEDC-TR-76-41, May, 1976.   
[16] Fuijkschot, P. H.: "Use of Servo-Accelerometers for the Measurement of Incidence of Windtunnel Models", National Aerospace Laboratory, The Netherlands, Memorandum AW-84-008, 1984.   
[17] Buehrle, R. D.; and Young, C. P., Jr.; "Modal Correction Method for Dynamically Induced Errors in Wind-Tunnel Model Attitude Measurements", Proceedings of the 13th International Modal Analysis Conference, pp. 1708-1714, Nashville, Tennessee, February 13-16, 1995.   
[18] Tcheng, P.; Tripp, J. S.; and Finley, T. D.; Effects of Yaw and Pitch Motion on Model Attitude Measurements, NASA Technical Memorandum 4641, February 1995.   
[19] Fuijkschot, P. H.: "A Correction Technique for Gravity Sensing Inclinometers", National Aerospace Laboratory, The Netherlands, Memorandum AF-95-004, 1995   
[20] Fuijkschot, P. H.: "A Correction Technique for Gravity Sensing Inclinometers-Phase 2: Proof of Concept", National Aerospace Laboratory, The Netherlands, CR 95458L, 1995.   
[21] Gloss, Blair, B.; "Future Experimental Needs To Support Applied Aerodynamics: A Transonic Perspective", AIAA Paper 92-0156, 1992.   
[22] Owen, F. K.; Orngard, G. M.; McDevitt, T. K.; and Ambur, T. A.; "A Dynamic Optical Model Attitude Measurement System", European Transonic Windtunnel GmbH and DFVLR, Cryogenic Technology Meeting, 2nd, Cologne, West Germany, June 28-30, 1988, Paper, 21 p.   
[23] Roberson, J. A.; and Crowe, C. T.: Engineering Fluid Mechanics, Houghton Mifflin Company, 1980.

[24] Meirovitch, Leonard: Elements of Vibration Analysis, McGraw-Hill, Inc., 1975, p 240-250.   
[25] Wells, D. A.: Schaum's Outline of Theory and Problems of Lagrangian Dynamics, Schaum Publishing Company, 1967.   
[26] Tse, F. S.; Morse, I. E.; and Hinkle, R. T.: Mechanical Vibrations Theory and Applications, Allyn and Bacon, Inc., 1978.   
[27] Fung, Y. C.: An Introduction to the Theory of Aeroelasticity, John Wiley & Sons, Inc., 1955.   
[28] Craig, R. R., Jr.: Structural Dynamics: An Introduction to Computer Methods, John Wiley & Sons, Inc., 1981.   
[29] Allemang, R. J.; and Brown, D. L.: Chapter 21: Experimental Modal Analysis, Shock and Vibration Handbook, 3rd Edition, McGraw Hill, Inc., 1988.   
[30] Ewins, D. J.: Modal Testing: Theory and Practice, Research Studies Press LTD., 1984   
[31] Ferris, A. T.: "Cryogenic Wind Tunnel Force Instrumentation", NASA Conference Publication No. 2122, Part II, 1982, pp 299-315.   
[32] Thomson, W. T.: Vibration Theory and Applications, Prentice-Hall, Inc., 1965, pp. 179-182.   
[33] Davenport, A. G.; and Novak, M.: Chapter 29 Part II: Vibration of Structures Induced by Wind, Shock and Vibration Handbook, 3rd Edition, McGraw Hill, Inc., 1988.   
[34] Alder, H. L.; and Roessler, E. B.: Introduction to Probability and Statistics, W. H. Freeman and Company, 1960.   
[35] MATLAB Reference Guide, The Math Works Inc., August, 1992.   
[36] Hornbeck, R. W.; Numerical Methods, Quantum Publishers, Inc., 1975.   
[37] The STAR System User Manual, Spectral Dynamics, Inc., 1996.   
[38] MSC/NASTRAN User's Manual, The MacNeal-Schwendler Corporation, 1989

# Appendix A

# EFFECT OF AERODYNAMIC FORCES ON MODAL CHARACTERISTICS

# Introduction

In this section, the effect of aerodynamic forces on the modal characteristics of a cantilevered wind tunnel model system are examined. The objective is to validate the assumption that the modal characteristics do not change significantly under the wind tunnel test conditions. This is a fundamental assumption of the modal correction method that enables wind-off estimates of the natural frequencies and mode effective radii to be used for correction of the model attitude measurement during wind tunnel testing. A finite element model (FEM) of a representative cantilevered transport model is used as the basis for evaluating the modal characteristics for several loading conditions including the most severe forces measured in a recent wind tunnel test on this model in the National Transonic Facility (NTF).

# Analytical Model

The finite element model of a representative cantilevered transport model system for the NTF was generated and analyzed using the MSC/NASTRAN® [38] structural analysis program. The FEM was developed with the goal of representing the low frequency (less than 50 Hertz) "rigid-fuselage" modes that contribute to the errors in the inertial model attitude measurements. Detailed modeling of the wings was not of interest for this study. The sting and model fuselage are constructed of beam elements with equivalent material

and cross-section specific geometric properties. The force balance which connects the sting to the fuselage was modeled using a concentrated mass equal to the balance mass and rigid bar elements. Springs were used at the connection between the rigid bar element and the fuselage to represent the balance stiffness corresponding to the three translation and three rotation degrees of freedom. The balance stiffness was determined from experimental measurements. The wings are modeled as concentrated masses attached to the fuselage using rigid bar elements. An additional lumped mass was used to represent instrumentation and associated hardware.

The primary generalized forces are the unsteady aerodynamic loads. The aerodynamic loads are modeled using a quasi-steady approximation [27]. The generalized aerodynamic forces are modeled as:

$$
Q _ {F} = q _ {\infty} \times S \times C _ {F} \tag {A.1}
$$

where, $q_{\infty}$ is the dynamic pressure and $S$ is the characteristic area. The coefficient $C_F$ will be assumed linear and is a function of the model attitude. Similarly, the generalized aerodynamic moments are modeled as:

$$
Q _ {M} = q _ {\infty} \times S \times d \times C _ {M} \tag {A.2}
$$

where $d$ is the characteristic length and the coefficient $C_M$ is assumed linear and is a function of the model attitude.

Data from a high-speed (Mach =0.9, $q_{\infty} = 1800$ pounds per square foot) wind tunnel test of this transport model in the NTF were used to determine the four most severe loading

conditions. To add additional conservatism, this data was scaled up to a dynamic pressure of 2700 pounds per square foot. The resulting loading conditions are listed in Table 1. These forces and moments were applied to the FEM at a point on the fuselage coincident with the balance moment center.

Table 1 Transport Model Worst Case Loading Conditions   

<table><tr><td>Load Case</td><td>Axial Force (Pounds)</td><td>Normal Force (Pounds)</td><td>Pitch Moment (Inch-Pounds)</td></tr><tr><td>1</td><td>69</td><td>-2271</td><td>4000</td></tr><tr><td>2</td><td>63</td><td>-491</td><td>3158</td></tr><tr><td>3</td><td>-53</td><td>2688</td><td>1474</td></tr><tr><td>4</td><td>-184</td><td>6035</td><td>632</td></tr></table>

For each of the four different aerodynamic load cases, a static analysis was run to generate a prestressed model and then the eigensolution was run for this prestressed loading condition. The eigensolution was also run for the no load case to provide a baseline set of natural frequencies and mode shapes.

# Results and Conclusions

The purpose of the analysis was to assess the effect of aerodynamic loading on the modal characteristics of a cantilevered wind tunnel model system. For the research presented in this dissertation, an important constant is the modal radius which is estimated from a linear regression fit of the fuselage mode shape coefficients. Therefore, the comparison

criteria are natural frequencies and mode radii. The mode radius for the first six analytical modes were estimated using the method described in Chapter 4. The natural frequencies and mode radii for the different loading conditions are listed in Tables 2 and 3, respectively. The natural frequency does not shift significantly for any of the loading conditions. For the largest aerodynamic forces measured on a representative transport model in the National Transonic Facility, the predicted shifts in the modal radius were less than $4\%$ , which is negligible.

Table 2 Transport Model Natural Frequency Comparison   

<table><tr><td></td><td>No Load</td><td>Load Case 1</td><td>Load Case 2</td><td>Load Case 3</td><td>Load Case 4</td><td></td></tr><tr><td>Mode</td><td>Frequency (Hz)</td><td>Frequency (Hz)</td><td>Frequency (Hz)</td><td>Frequency (Hz)</td><td>Frequency (Hz)</td><td>Maximum Difference (%)</td></tr><tr><td>1</td><td>9.19</td><td>9.19</td><td>9.19</td><td>9.20</td><td>9.22</td><td>0.3</td></tr><tr><td>2</td><td>9.23</td><td>9.23</td><td>9.23</td><td>9.25</td><td>9.30</td><td>0.8</td></tr><tr><td>3</td><td>17.2</td><td>17.2</td><td>17.2</td><td>17.2</td><td>17.3</td><td>0.6</td></tr><tr><td>4</td><td>17.3</td><td>17.4</td><td>17.4</td><td>17.4</td><td>17.4</td><td>0.6</td></tr><tr><td>5</td><td>29.5</td><td>29.5</td><td>29.5</td><td>29.6</td><td>29.7</td><td>0.7</td></tr><tr><td>6</td><td>30.4</td><td>30.4</td><td>30.4</td><td>30.5</td><td>30.6</td><td>0.7</td></tr></table>

Note: * Difference (%) = (fload-fnoload) / fno load *100

Table 3 Transport Model Mode Radius Comparison   

<table><tr><td></td><td>No Load</td><td>Load Case 1</td><td>Load Case 2</td><td>Load Case 3</td><td>Load Case 4</td><td></td></tr><tr><td>Mode</td><td>Radius (Inch)</td><td>Radius (Inch)</td><td>Radius (Inch)</td><td>Radius (Inch)</td><td>Radius (Inch)</td><td>Maximum Difference (%)*</td></tr><tr><td>1</td><td>39.4</td><td>39.5</td><td>39.4</td><td>39.6</td><td>40.2</td><td>1.8</td></tr><tr><td>2</td><td>39.7</td><td>39.8</td><td>39.7</td><td>40.0</td><td>41.1</td><td>3.5</td></tr><tr><td>3</td><td>7.68</td><td>7.68</td><td>7.67</td><td>7.72</td><td>7.87</td><td>2.5</td></tr><tr><td>4</td><td>8.21</td><td>8.24</td><td>8.20</td><td>8.28</td><td>8.54</td><td>4.0</td></tr><tr><td>5</td><td>-3.67</td><td>-3.66</td><td>-3.67</td><td>-3.67</td><td>-3.64</td><td>-0.8</td></tr><tr><td>6</td><td>-3.17</td><td>-3.18</td><td>-3.17</td><td>-3.15</td><td>-3.14</td><td>-0.9</td></tr></table>

Note: * Difference (%) = (Rload - Rnoload) / Rnoload *100
