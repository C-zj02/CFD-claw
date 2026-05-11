图片摘要：该图片为文档封面或首页内容，主题与Estimation of Handling Qualities Parameters of the Tu 144 Supersonic Transport Aircraft From Flight Test Data相关。
![](images/0f0cd1253fd85457aa2af208097656ec5ecb3d0c07337f8ca072f2b360f49075.jpg)

# Estimation of Handling Qualities Parameters of the Tu-144 Supersonic Transport Aircraft From Flight Test Data

Timothy J. Curry  
George Washington University  
Joint Institute for the Advancement of Flight Sciences  
Hampton, Virginia

# The NASA STI Program Office ... in Profile

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA Scientific and Technical Information (STI) Program Office plays a key part in helping NASA maintain this important role.

The NASA STI Program Office is operated by Langley Research Center, the lead center for NASA's scientific and technical information. The NASA STI Program Office provides access to the NASA STI Database, the largest collection of aeronautical and space science STI in the world. The Program Office is also NASA's institutional mechanism for disseminating the results of its research and development activities. These results are published by NASA in the NASA STI Report Series, which includes the following report types:

- TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counterpart of peer-reviewed formal professional papers, but having less stringent limitations on manuscript length and extent of graphic presentations.   
- TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., quick release reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.   
- CONTRACTOR REPORT. Scientific and technical findings by NASA-sponsored contractors and grantees.

- CONFERENCE PUBLICATION. Collected papers from scientific and technical conferences, symposia, seminars, or other meetings sponsored or co-sponsored by NASA.   
- SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
- TECHNICAL TRANSLATION. English-language translations of foreign scientific and technical material pertinent to NASA's mission.

Specialized services that complement the STI Program Office's diverse offerings include creating custom thesauri, building customized databases, organizing and publishing research results ... even providing videos.

For more information about the NASA STI Program Office, see the following:

- Access the NASA STI Program Home Page at http://www.sti.nasa.gov   
E-mail your question via the Internet to help@sti.nasa.gov   
Fax your question to the NASA STI Help Desk at (301) 621-0134   
Phone the NASA STI Help Desk at (301) 621-0390   
Write to: NASA STI Help Desk NASA Center for AeroSpace Information 7121 Standard Drive Hanover, MD 21076-1320

图片摘要：该图片与Estimation of Handling Qualities Parameters of the Tu 144 Supersonic Transport A这部分内容相关。
![](images/e6b816e10a4e1d8d272a52ad04b94afbb75a6e54ff982478bd14a93f81484aa5.jpg)

# Estimation of Handling Qualities Parameters of the Tu-144 Supersonic Transport Aircraft From Flight Test Data

Timothy J. Curry  
George Washington University  
Joint Institute for the Advancement of Flight Sciences  
Hampton, Virginia

National Aeronautics and Space Administration

Langley Research Center Hampton, Virginia 23681-2199

Prepared for Langley Research Center under Cooperative Agreement NCC1-29

Available from the following:

NASA Center for AeroSpace Information (CASI)

7121 Standard Drive

Hanover, MD 21076-1320

(301)621-0390

National Technical Information Service (NTIS)

5285 Port Royal Road

Springfield, VA 22161-2171

(703) 487-4650

# ABSTRACT

Low order equivalent system (LOES) models for the Tu-144 supersonic transport aircraft were identified from flight test data. The mathematical models were given in terms of transfer functions with a time delay by the military standard MIL-STD-1797A, "Flying Qualities of Piloted Aircraft," and the handling qualities were predicted from the estimated transfer function coefficients. The coefficients and the time delay in the transfer functions were estimated using a nonlinear equation error formulation in the frequency domain. Flight test data from pitch, roll, and yaw frequency sweeps at various flight conditions were used for parameter estimation. Flight test results are presented in terms of the estimated parameter values, their standard errors, and output fits in the time domain. Data from doublet maneuvers at the same flight conditions were used to assess the predictive capabilities of the identified models. The identified transfer function models fit the measured data well and demonstrated good prediction capabilities. The Tu-144 was predicted to be between level 2 and 3 for all longitudinal maneuvers and level 1 for all lateral maneuvers. High estimates of the equivalent time delay in the transfer function model caused the poor longitudinal rating.

# ACKNOWLEDGMENTS

This research was conducted at the NASA Langley Research Center under the support of NASA Cooperative Agreement NCC1-29 and HSR Guidance and Control Element number 537-08-23-21. The element lead was Dave Hahne.

Additionally, guidance and advice from Dr. Vladislav Klein and Dr. Eugene Morelli greatly contributed to this work.

# TABLE OF CONTENTS

ABSTRACT.   
ACKNOWLEDGMENTS IV   
TABLE OF CONTENTS. V   
LIST OF TABLES vi   
LIST OF FIGURES ix   
LIST OF SYMBOLS Xii

1. INTRODUCTION   
2. AIRCRAFT AND FLIGHT DATA 5  
3. MATHEMATICAL MODELS AND MILITARY STANDARD REQUIREMENTS 9

3.1 Longitudinal Models 9   
3.2 Lateral Models 12

4. IDENTIFICATION METHODOLOGY 16

4.1 Time and Frequency Domain 16   
4.2 Equation Error Method 17

4.2.1 One Output Measurement 17   
4.2.2 Two Output Measurements 18

4.3 Output Error Method 20

4.3.1 One Output Measurement 20   
4.3.2 Two Output Measurements 21

4.4 Output Error Method for Frequency Response Data 22

5. ANALYSIS OF SIMULATED DATA 24

5.1 Longitudinal Simulation 24   
5.2 Lateral Simulation 27

6. FLIGHT TEST RESULTS AND DISCUSSION 29

6.1 Longitudinal Results 29   
6.2 Lateral Results 32

7. CONCLUSIONS AND SUGGESTIONS FOR FUTURE WORK 37

REFERENCES 39

APPENDIX A: MANEUVER DESCRIPTION 41

APPENDIX B: ERROR PROPAGATION 46

# LIST OF TABLES

TABLE 1 - Summary of geometric, mass, and inertia characteristics of the TU-144. 49   
TABLE 2 - Measured parameters used for data analysis. 50   
TABLE 3 - Coordinate location of instrumentation. 51   
TABLE 4 - Flight test maneuvers performed for handling qualities prediction. ....52   
TABLE 5 - Recommended short period requirements for Class III, (a) Category B and (b) Category C. 57   
TABLE 6 - Recommended roll-mode time constant for Class III, Category B and C. 57   
TABLE 7 - Recommended Dutch roll frequency and damping for Class III, (a) Category B and (b) Category C. 57   
TABLE 8 - Normalized pairwise parameter correlation matrices from simulated data for (a) EEM for one measurement, (b) EEM for two measurements, (c) OEM for one measurement, and (d) OEM for two measurements. 58   
TABLE 9 - Summary of longitudinal parameter estimates. 59   
TABLE 10 - Summary of longitudinal handling qualities predictions. 61   
TABLE 11 - Average parameter estimates for different flight conditions. Pitch rate to longitudinal stick transfer function coefficients. 63   
TABLE 12 - Summary of Dutch roll parameter estimates. 64   
TABLE 13 - Average parameter estimates for different flight conditions. Yaw rate to rudder pedal input transfer function coefficients.66   
TABLE 14 - Summary of roll-mode time constant estimates for first-order model. 67

TABLE 15 - Average parameter estimates for different flight conditions. Roll rate to lateral stick input transfer function coefficients. First-order model. 69   
TABLE 16 - Summary of roll-mode time constant estimates for third-order hybrid model. 70   
TABLE 17 - Average parameter estimates for different flight conditions. Roll rate to lateral stick input transfer function coefficients. Third-order hybrid model. 72   
TABLE 18 - Summary of lateral handling qualities predictions. Roll-mode time constant from first-order model shown. 73

# LIST OF FIGURES

FIGURE 1 - Three-view drawing of the Tu-144 aircraft. 75   
FIGURE 2 - Data compatibility results comparing measured and calculated (a) angle of attack, and (b) sideslip angle. 76   
FIGURE 3 - Time skew in response of aircraft to control surface deflection. Longitudinal doublet, test point number 2.4-15.4A. 77   
FIGURE 4 - (a) Simulated and model time histories for pitch rate for EEM, and (b) residuals from output fit. 78   
FIGURE 5 - Summary of parameter estimates with $2\sigma$ error bars for pitch rate to longitudinal stick transfer function. 79   
FIGURE 6 - Comparison of measured, estimated, and predicted time histories of pitch rate. Test point number (a) 2.4-16.1A for estimation, and (b) 2.4-16.4A for prediction. 82   
FIGURE 7 - Comparison of measured, estimated, and predicted time histories of pitch rate. Test point number (a) 2.4-15.1B for estimation, and (b) 2.4-15.4B for prediction. 83   
FIGURE 8 - Comparison of measured, estimated, and predicted time histories of pitch rate. Test point number (a) 2.4-12.1B for estimation, and (b) 2.4-12.4B for prediction. 84   
FIGURE 9 - Comparison of measured and predicted time histories of pitch rate. Test point number 2.4-16.1B predicted with 2.4-16.1A parameter estimates. 85   
FIGURE 10 - Summary of parameter estimates with $2\sigma$ error bars for yaw rate to rudder pedal transfer function. 86

FIGURE 11 - Comparison of measured, estimated, and predicted time histories of yaw rate. Test point number (a) 2.4-16.3A for estimation, and (b) 2.4-16.6A for prediction. 89   
FIGURE 12 - Comparison of measured, estimated, and predicted time histories of yaw rate. Test point number (a) 2.4-15.3A for estimation, and (b) 2.4-15.6A for prediction. 90   
FIGURE 13 - Comparison of measured, estimated, and predicted time histories of yaw rate. Test point number (a) 2.4-12.3A for estimation, and (b) 2.4-12.6A for prediction. 91   
FIGURE 14 - Summary of parameter estimates with $2\sigma$ error bars for roll rate to lateral stick transfer function. First-order model. 92   
FIGURE 15 - Comparison of measured, estimated, and predicted time histories of roll rate. First-order model. Test point number (a) 2.4-17.2A for estimation, and (b) 2.4-17.5A for prediction. 94   
FIGURE 16 - Comparison of measured, estimated, and predicted time histories of roll rate. First-order model. Test point number (a) 2.4-15.2A for estimation, and (b) 2.4-15.5A for prediction. 95   
FIGURE 17 - Comparison of measured, estimated, and predicted time histories of roll rate. First-order model. Test point number (a) 2.4-12.2B for estimation, and (b) 2.4-12.5B for prediction. 96   
FIGURE 18 - Summary of parameter estimates with $2\sigma$ error bars for roll rate to lateral stick transfer function. Third-order hybrid model. 97   
FIGURE 19 - Comparison of measured, estimated, and predicted time histories of roll rate. Third-order hybrid model. Test point number (a) 2.4-17.2A for estimation, and (b) 2.4-17.5A for prediction. 100

FIGURE 20 - Comparison of measured, estimated, and predicted time histories of roll rate. Third-order hybrid model. Test point number

(a) 2.4-15.2A for estimation, and (b) 2.4-15.5A for prediction. 101

FIGURE 21 - Comparison of measured, estimated, and predicted time histories of roll rate. Third-order hybrid model. Test point number

(a) 2.4-12.2B for estimation, and (b) 2.4-12.5B for prediction. 102

FIGURE 22 - Results of Monte Carlo simulation for longitudinal parameter

estimates. 103

# List of Symbols

# Variables

$\mathbf{A}_{\beta}$ sideslip angle static gain, fourth-order   
H frequency response   
J cost function   
$\mathbf{K}_{\mathrm{p}}$ roll rate static gain   
$\mathbf{K}_{\mathrm{r}}$ yaw rate static gain   
$\mathbf{K}_{\mathrm{z}}$ vertical acceleration static gain   
$\mathbf{K}_{\theta}$ pitch angle static gain   
$\mathbf{K}_{\phi}$ roll angle static gain   
$\mathbf{K}_{\beta}$ sideslip angle static gain, second-order   
S power spectral density   
$\mathbf{S}_{\mathbf{v}\mathbf{v}}$ power spectral density of measurement noise   
$\mathbf{T}_{\mathrm{S}}$ spiral mode time constant, sec   
$\mathbf{T}_{\mathbb{R}}$ roll mode time constant, sec   
$\mathbf{V}_0$ mean velocity, ft/s   
Y output vector   
$\mathbf{a}_{z}$ vertical acceleration, g units   
g acceleration due to gravity, ft/s2   
m number of frequencies   
j $\sqrt{-1}$   
p roll rate, rad/sec   
q pitch rate, rad/sec   
r yaw rate, rad/sec   
Laplace operator

time,sec

$1 / \mathrm{T}_{\mathrm{r}}$ yaw rate zero, 1/sec

1/Tθ1 low-frequency pitch attitude zero, 1/sec

$1 / \mathrm{T}_{\theta_2}$ high-frequency pitch attitude zero, 1/sec

1/Th1 low-frequency normal acceleration zero, 1/sec

$1 / \mathrm{T}_{\beta_1}$ sideslip angle zero, 1/sec

$1 / \mathrm{T}_{\beta_2}$ sideslip angle zero, 1/sec

$1 / \mathrm{T}_{\beta_3}$ sideslip angle zero, 1/sec

$\delta_{\mathrm{e}}$ elevator deflection, rad

$\eta_{\mathrm{a}}$ control wheel deflection, m

$\eta_{\mathrm{e}}$ control column deflection, m

$\eta_{\mathbf{r}}$ rudder pedal deflection, m

$\pmb{\lambda}$ vector of estimated parameters

v residual value in frequency domain

$\sigma$ standard error

$\tau_{p}$ time delay for roll transfer function, sec

$\tau_{\mathrm{r}}$ time delay for yaw transfer function, sec

$\tau_{\theta}$ time delay for longitudinal transfer function, sec

$\tau_{\beta}$ time delay for directional transfer function, sec

$\pmb{\omega}$ frequency vector, rad/sec

$\omega_{\mathrm{d}}$ undamped natural frequency of the Dutch roll oscillation, rad/sec

$\omega_{\mathrm{p}}$ undamped natural frequency of the phugoid oscillation, rad/sec

$\omega_{\phi}$ undamped natural frequency of the roll mode, rad/sec

$\omega_{\mathrm{sp}}$ undamped natural frequency of the short period oscillation, rad/sec

$\zeta_{\mathrm{d}}$ damping ratio of the Dutch roll oscillation

$\zeta_{\mathfrak{p}}$ damping ratio of the phugoid oscillation

$\zeta_{\phi}$ damping ratio of the roll mode

$\zeta_{\mathrm{sp}}$ damping ratio of the short period oscillation

# Superscripts

\~ Laplace transformed variable

time derivative

\* matrix conjugate transpose

$\wedge$ estimated value

T transpose

# Subscripts

E experimental value

i $i^{\mathrm{th}}$ component

$\theta$ pitch axis variable

# Abbreviations

HSR high-speed research program

TPN test point number

HOS high-order system

LOES low-orderequivalent system

FDAS flight data access system

EEM equation error method

OEM output error method

# 1. INTRODUCTION

Flying qualities, or handling qualities as they are also called, are defined as "qualities or characteristics that govern the ease and precision with which a pilot is able to perform the tasks required in support of an aircraft role" (ref. 1). The handling qualities can only be assessed from pilot opinions, but the governing military standards for flying qualities offer methods of predicting the handling qualities from estimated transfer function coefficients. The Military Specification for Flying Qualities of Piloted Aircraft, MIL-F-8785B (ref. 2), was written in the 1960's for unaugmented aircraft, or aircraft which did not have higher-order control systems (HOS). Predicting handling qualities from the open-loop transfer function coefficients was an acceptable method for unaugmented, or classical, aircraft but the use of complex augmentation systems on aircraft required a different mathematical model to describe the aircraft dynamics than the open-loop transfer function. Many aircraft built in the 1970's with high-order control systems were designed without the benefit of the specification since the guidelines were not considered to be applicable. A revision to the military specification, MIL-F-8785C (ref. 3), was developed in 1980 and was the first to recognize augmented aircraft and introduce the low order equivalent systems (LOES) concept:

"The contractor shall define equivalent classical systems which have responses most closely matching those of the actual aircraft. Then those numerical requirements...which are stated in terms of linear system parameters (such as frequency, damping ratio and modal phase angles) apply to the parameters of that equivalent system rather than to any particular modes of the actual higher-order system."

Thus, the military specification suggests that the equivalent system model should have parameters which are directly relatable to their classical counterparts. The LOES models are linearized, reduced-order models of the actual aircraft response and are used to allow the existing flying qualities requirements established for unaugmented, or classical, aircraft to be extended to higher order systems.

The most recent military standard for flying qualities of piloted aircraft, MIL-STD-1797A (ref. 4), was written in 1990 and suggests specific LOES models in the assessment of flying qualities. The LOES models have the same structure as the classical open-loop linear models, but use the pilot input with a pure time delay rather than control surface deflections as the model input.

Mitchell and Hoh (ref. 5) found encouraging results with a number of high-order system flight test results and showed in most cases the pitch short-period equivalent dynamics are relatable to their unaugmented counterparts. Additionally, a key finding was the significant role that the time delay played in the degradation of longitudinal flying qualities. Pure time lags produced by the control system directly impacted the pilots' opinions of the handling qualities.

In terms of the MIL-STD-1797A models, a substantial amount of research has been performed by Tischler (ref. 6-8) on their identification using frequency response matching. This method uses a least squares fit of the Bode plot (magnitude and phase) in the frequency domain using the LOES as the model. Though the results of this method have been very good, frequency response matching requires substantial data conditioning and computation time to estimate accurate parameters.

A more direct approach was sought by Manning and Gleason (ref. 9) who estimated the parameters of the LOES model in the time domain. Time response matching is an attractive option since the measured input and output data are all that are required; that is, no transformation to the frequency domain is required.

The flying qualities of a supersonic transport aircraft may be significantly different than current subsonic transports due to the vastly different configurations required for high-speed flight. Great concern is placed on the handling of the aircraft during landing approach where the aircraft is typically more difficult to control and greater precision is required. The NASA High Speed Research (HSR) program, in conjunction with Boeing and the Tupolev Design Bureau, performed 19 flight tests of a Russian Tu-144 supersonic transport to establish a new database of information for the development of a U.S. supersonic transport in the early 21st century. Data for flying quality and aircraft response evaluations were recorded from an array of aircraft configurations and flight conditions. From the recorded data, LOES models can be identified, and the flying qualities of the aircraft in several different flight regimes can be predicted. The primary objective of this research is to predict the flying qualities of the Tu-144 from flight test data.

This paper begins with a description of the Tu-144 aircraft and the flight test data used for flying qualities prediction, as well as a data compatibility check and description of all corrections made to the data before analysis. The mathematical models given by the military standard are given with all necessary assumptions and the important parameters for flying qualities prediction are illustrated.

Next, the reasoning for the selection of the equation error and output error method in the frequency domain for identification of the LOES models is presented. These methods are developed completely in reference 10, but a brief development is presented in this paper as well. Simulated data was used to validate the mathematical models and the identification methods.

Finally, the methodology was used to identify the model parameters from flight test data for twenty-one pitch frequency sweeps, nineteen roll frequency sweeps, and nineteen yaw frequency sweeps which were performed at various flight conditions and aircraft configurations. The parameters in the identified models were then used to predict the flying qualities of the Tu-144. The results are presented in terms of the estimated parameters and

their standard errors for each maneuver with the predicted handling qualities for each maneuver. If the aircraft was not rated level 1, the reason is also given. Suggestions for future research are also discussed. The appendices contain a detailed description of the flight test maneuver instructions given to the pilots as well as a derivation of the error analysis.

# 2. AIRCRAFT AND FLIGHT DATA

The Tu-144 supersonic transport aircraft is shown in figure 1 and the geometric, mass, and inertia characteristics of the aircraft are summarized in table 1. The Tu-144LL used for flight tests was a refurbished Tu-144D, tail number 77114, and re-equipped with Kuznetsov NK-321 turbofan engines like those operational on the Russian Air Force Tupolev Tu-160 Blackjack bomber. Pitch and roll are controlled with elevons which extend along the aft of the entire span of the wing. A rudder on the vertical tail is used for directional control. The aircraft is equipped with conventional cable-commanded hydraulic actuators which have a parallel electronic input. For stability augmentation, the cable input from the pilot is summed with the electronic command from the flight control system. Control inputs from the pilots go directly to the actuators via the control cables and do not go into the control laws.

The pitch augmentation system consists of a pitch damper which uses pitch rate feedback to provide improved pitch damping of the short period mode. Similarly, there is a yaw damper that uses yaw rate feedback. Autopilot and autothrottle were turned off during the testing. During takeoff and landing, the nose is drooped for increased visibility and a canard above the cockpit is extended for increased stability. The angle of droop for the nose for takeoff and landing is $11^{\circ}$ and $17^{\circ}$ , respectively. The canard is extended only for stability at lower speeds and is not a control surface.

For each flight test, the pilot input, control surface deflections, and aircraft responses were measured and stored as time histories. Additionally, other variables used to verify the flight condition and aircraft configuration were measured. The FDAS variables used for data analysis are listed in table 2. Table 3 indicates the coordinate locations of the instrumentation measuring aircraft response.

All flights of the Tu-144 were performed by Russian pilots at the Zhukovsky Air Development Center near Moscow, Russia. Flight tests were performed at speeds ranging from Mach 0.3-1.6 at altitudes of 5,000-50,000 feet and angles of attack ranging from $4^{\circ}-11^{\circ}$ . The test point number (TPN), test title, aircraft configuration, flight conditions and flight number for the maneuvers are listed in table 4.

For the handling qualities experiment, basic airworthiness sensors on board the TU-144LL were used. No additional instrumentation specific to this experiment was installed. The parameters were sampled into analog input channels in a DAMIEN pulse code modulation (PCM) data acquisition system. These channels were pre-sample filtered to prevent aliasing of data. The filters used were 2-pole low-pass passive RC filters with a 1 dB per octave rolloff. Attenuation was 3 dB at $200\mathrm{Hz}$ . Flight test data was taken by Tupolev and transferred to the NASA Dryden flight research center where it was made available on the flight data access system (FDAS). Further discussion of the instrumentation system can be found in reference 11.

The maneuvers used for handling qualities prediction were frequency sweeps performed along the pitch, roll and yaw axes at each flight condition or aircraft configuration of interest. A frequency sweep is a commanded oscillation of the controls about a trim condition which increases in frequency from the start to finish of the maneuver. Frequency sweeps along each axis were chosen since they would excite a wide range of frequencies. Additionally, these maneuvers are ideal for frequency response matching since they contain a rich spectral content. Doublets were performed along the same axes at each flight condition and these data were used to assess the predictive capabilities of the estimated models. A doublet is a combination of two pulses of equal amplitude and opposite sign in succession. Specifications given to the Russian pilots denoting how the frequency sweep and doublet maneuvers were to be flown are taken from reference 12 and included in appendix A.

Translation of the Russian coordinate system to the U.S. coordinate system and the calculation of true airspeed from indicated airspeed were both required for the Tu-144. These corrections are made at NASA Dryden and the corrected variables are available directly from the FDAS system. Corrections to the angle of attack and sideslip angles to account for vehicle rotation and corrections to accelerometer measurements due to center of gravity offset were not made at NASA Dryden but were completed before data analysis.

As a part of the data analysis, a data compatibility check was conducted. The purpose of this check is to identify and estimate constant offset and scale factor errors in the measured response variables due to instrumentation. The error parameters are added to the equations of motion and estimated using a maximum likelihood technique (ref. 13). If there was a consistent and significant effect of these parameters, the data were corrected prior to analysis.

For the longitudinal mode, the outputs were velocity, angle of attack, and Euler pitch angle. The lateral outputs were the sideslip angle, Euler roll angle, and Euler yaw angle. The main emphasis was on the agreement between the measured angle of attack and calculated angle of attack using integrated acceleration measurements for the longitudinal mode and the measured and calculated sideslip angle for the lateral mode. Even with the linear bias and scale factor error parameters, the data compatibility routine could not satisfactorily fit the angle of attack or sideslip angle for a longitudinal or directional maneuver, respectively. The resulting fits for angle of attack and sideslip angle, using flight data from test point numbers 2.4-15.1B and 2.4-15.3A, respectively, are shown in figure 2.

Different parameters, such as the first derivatives of the estimated angles and higher-order order terms, were added into the calculations of these two responses to improve the fit, but were unsuccessful. The most notable problem with the fit is that the measured data lags the estimation from the equations of motion. The cause of this lag is unknown. Additionally, the measurement of sideslip angle flattens out at the higher frequencies. This may complicate identification of the models for higher frequencies.

Another unexplained behavior in the data was the presence of time skews, or abnormal time shifts in the data. A time delay exists between the stick input and the control surface deflection due to the control system. Once the control surface deflects, however, we would expect the aircraft to respond almost immediately. This was not the case in for the Tu-144. An example of this type of time skew is shown in figure 3. The elevator deflection lags the stick by approximately 0.13 seconds. This lag can be attributed to the control system and actuator delays and is normal for a large transport aircraft. The pitch rate then lags the elevator deflection by an additional 0.25 seconds. Initially, the time skews were believed to be caused by time intervals between sampling different parameters on the multiplexed data system; however, this time delay can be at most one time frame long, or 0.03125 seconds. This accounts for very little of the 0.25 second lag. Another theory is that this time delay is real and the aircraft actually responds in this manner. Both Boeing and Tupolev have been made aware of the problem, but the cause for the delay is still unknown. Similar time skews are apparent with the lateral maneuvers as well. Whatever the cause, these time skews are not accounted for in the equations of motion used for data compatibility and may be the cause of the poor agreement with the angle of attack and sideslip angle estimates. Since there was no information on the magnitude (if any) of the time skews, the data was analyzed as recorded and stored on FDAS.

# 3. MATHEMATICAL MODELS AND MILITARY STANDARD REQUIREMENTS

The LOES models given by the military standard are introduced in this section and the parameters required for handling qualities prediction are highlighted. In some cases, the mathematical models deviate from those suggested by the military standard, but the assumptions which lead to the different models are explained. The estimated coefficients are directly correlated to the handling qualities criteria, and these criteria for the longitudinal and lateral modes for a Class III, Category B or C aircraft are summarized in tables 5-7. In every case, the primary goal is to formulate mathematical models which not only describe the approximate dynamics of the aircraft, but will also yield the specific parameter estimates which lead directly to the handling qualities prediction.

# 3.1 Longitudinal Models

For handling qualities prediction, the military standard places requirements on the short period damping ratio $(\zeta_{\mathrm{sp}})$ , time delay $(\tau_{\theta})$ , and the product of the short period natural frequency and inverse of the high frequency pitch attitude zero $(\omega_{\mathrm{sp}}T_{\theta_2})$ .

The pitch rate and normal acceleration LOES models are given in reference 4 as

$$
\frac {\tilde {q}}{\tilde {\eta} _ {\mathrm {c}}} = \frac {\mathrm {K} _ {\theta} \mathrm {s} \left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\theta_ {1}}}\right) \left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\theta_ {2}}}\right) \mathrm {e} ^ {- \tau_ {\theta} \mathrm {s}}}{\left[ \mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {p}} \omega_ {\mathrm {p}} \mathrm {s} + \omega_ {\mathrm {p}} ^ {2} \right] \left[ \mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {s p}} \omega_ {\mathrm {s p}} \mathrm {s} + \omega_ {\mathrm {s p}} ^ {2} \right]} \tag {1}
$$

and

$$
\frac {\tilde {a} _ {z}}{\tilde {\eta} _ {e}} = \frac {\mathrm {K} _ {z} \mathrm {s} \left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\mathrm {h} _ {1}}}\right) \mathrm {e} ^ {- \tau_ {\theta} \mathrm {s}}}{\left[ \mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {p}} \omega_ {\mathrm {p}} \mathrm {s} + \omega_ {\mathrm {p}} ^ {2} \right] \left[ \mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {s p}} \omega_ {\mathrm {s p}} \mathrm {s} + \omega_ {\mathrm {s p}} ^ {2} \right]}. \tag {2}
$$

Note all of the required parameters are found in these models. For a maneuver where the velocity is approximately constant, a short period approximation may be made.

Additionally, when the effect of elevon deflection on the lift is neglected, the normal acceleration to stick transfer function may be rearranged to be a function of only parameters which appear in the pitch rate to stick transfer function. This is advantageous for parameter estimation since it allows the use of another measurement without any additional parameters. The new LOES models may be rewritten and expressed with generic parameters as

$$
\frac {\tilde {q}}{\tilde {\eta} _ {\mathrm {e}}} = \frac {\mathrm {K} _ {\theta} \left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\theta_ {2}}}\right) \mathrm {e} ^ {- \tau_ {\theta} \mathrm {s}}}{\mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {s p}} \omega_ {\mathrm {s p}} \mathrm {s} + \omega_ {\mathrm {s p}} ^ {2}} = \frac {(\mathrm {A s} + \mathrm {B}) \mathrm {e} ^ {- \tau_ {\theta} \mathrm {s}}}{\mathrm {s} ^ {2} + \mathrm {k} _ {1} \mathrm {s} + \mathrm {k} _ {0}} \tag {3}
$$

and

$$
\frac {\tilde {a} _ {z}}{\tilde {\eta} _ {e}} = \frac {- \left(\frac {V _ {o}}{g} \frac {K _ {\theta}}{T _ {\theta_ {2}}}\right) e ^ {- \tau_ {\theta} s}}{s ^ {2} + 2 \zeta_ {s p} \omega_ {s p} s + \omega_ {s p} ^ {2}} = \frac {- \frac {V _ {o}}{g} B e ^ {- \tau_ {\theta} s}}{s ^ {2} + k _ {1} s + k _ {0}}, \tag {4}
$$

where

$$
\mathbf {A} = \mathbf {K} _ {\boldsymbol {\theta}},
$$

$$
\mathbf {B} = \mathbf {K} _ {\boldsymbol {\theta}} / \mathbf {T} _ {\boldsymbol {\theta} _ {2}},
$$

$$
\mathrm {k} _ {\mathrm {l}} = 2 \zeta_ {\mathrm {s p}} \omega_ {\mathrm {s p}},
$$

and

$$
\mathbf {k} _ {0} = \boldsymbol {\omega} _ {\mathrm {s p}} ^ {2}.
$$

All of the required parameters for handling qualities prediction are present in these equations even though the models have been greatly simplified. Equations (3) and (4) without the exponential term are identical to the open loop transfer function models with elevator deflection, $\delta_{\mathrm{e}}$ , as the input. The parameter $\tau_{\theta}$ accounts for the time delay between $\eta_{\mathrm{e}}$ and $\delta_{\mathrm{e}}$ as well as other possible nonlinearities and added dynamics associated with the control system and aircraft augmentation. However, it is important to note that although the primary function of $\tau_{\theta}$ is to account for the time delay between stick and control surface, the equivalent system will actually estimate the time delay as the time between stick deflection and aircraft response (input to output), or $\eta_{\mathrm{e}}$ to $q$ , for the longitudinal mode.

Table 5, given by the military standard, relates the parameter values estimated from equations (3) and (4) to the handling qualities of the aircraft. Note the requirement on the time delay is 0.10 for a level 1 aircraft. There has been significant data to suggest that this figure is too stringent for large transport aircraft and values of $\tau_{\theta}$ of up to 0.4 have still resulted in a level 1 pilot rating (ref. 14-16). Nevertheless, the current military standard values were used in this report.

The generic parameters, $[\mathbf{k}_1\mathbf{k}_0\mathrm{A}\mathrm{B}\tau_0]^{\mathrm{T}}$ , are introduced to simplify the model and ease the workload of the optimizer. Obtaining the military standard transfer function coefficients from the generic parameters is a simple algebra problem, but determining the errors from the generic parameters required a little more computation. The derivation of the error propagation from the generic parameters to the military standard transfer function coefficients is given in appendix B. Thus, we can estimate all the necessary parameters for handling qualities prediction and their standard errors using equations (3) and (4).

# 3.2 Lateral Models

For the lateral modes, the military standard requires only 3 parameters to be estimated: the roll-mode time constant $(\mathrm{T}_{\mathrm{R}})$ , the Dutch roll damping ratio $(\zeta_{\mathrm{d}})$ , and the Dutch roll natural frequency $(\omega_{\mathrm{d}})$ . The requirements imposed on the values of these parameters are indicated in tables 6-7.

The military standard gives two options for obtaining the Dutch roll damping and natural frequency. First, if the ratio of amplitudes of bank angle and sideslip angle envelopes in the Dutch roll mode, $|\phi / \beta|_{\mathrm{d}}$ , is large, reference 4 suggests estimating the parameters in

$$
\frac {\tilde {p}}{\tilde {\eta} _ {a}} = \frac {K _ {\phi} s \left[ s ^ {2} + 2 \zeta_ {\phi} \omega_ {\phi} s + \omega_ {\phi} {} ^ {2} \right] e ^ {- \tau_ {p} s}}{\left(s + \frac {1}{T _ {s}}\right) \left(s + \frac {1}{T _ {R}}\right) \left[ s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} {} ^ {2} \right]} \tag {5}
$$

and

$$
\frac {\tilde {\beta}}{\tilde {\eta} _ {a}} = \frac {A _ {\beta} \left(s + \frac {1}{T _ {\beta_ {1}}}\right) \left(s + \frac {1}{T _ {\beta_ {2}}}\right) \left(s + \frac {1}{T _ {\beta_ {3}}}\right) e ^ {- \tau_ {\beta} s}}{\left(s + \frac {1}{T _ {s}}\right) \left(s + \frac {1}{T _ {R}}\right) \left[ s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} ^ {2} \right]} \tag {6}
$$

simultaneously. Though this would yield all of the parameters required for handling qualities prediction, the models contain a substantial number of parameters which would be difficult to estimate accurately.

If $\left|\phi / \beta\right|_{\mathrm{d}}$ is small, the military standard then suggests the use of a second-order transfer function relating sideslip angle to rudder pedal deflection:

$$
\frac {\tilde {\beta}}{\tilde {\eta} _ {r}} = \frac {K _ {\beta} e ^ {- \tau_ {\beta} s}}{s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} ^ {2}}. \tag {7}
$$

This transfer function is obtained from the Dutch roll approximation and assumes the side force due to rudder input is negligible. An alternative transfer function utilizing only the Dutch roll approximation relates yaw rate response to yaw control input:

$$
\frac {\tilde {\mathrm {r}}}{\tilde {\eta} _ {\mathrm {r}}} = \frac {\mathrm {K} _ {\mathrm {r}} \left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\mathrm {r}}}\right) \mathrm {e} ^ {- \tau_ {\mathrm {r}} \mathrm {s}}}{\mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {d}} \omega_ {\mathrm {d}} \mathrm {s} + \omega_ {\mathrm {d}} ^ {2}}. \tag {8}
$$

Equation (8) adds an additional parameter to the estimation; however, it does offer the ability to use the rate measurement instead of the sideslip angle measurement. The estimation of the parameters in either (7) or (8) would give the required Dutch roll parameters for handling qualities prediction.

To obtain the maximum roll-mode time constant, reference 4 defines the equivalent roll and sideslip transfer functions, respectively, as

$$
\frac {\tilde {\phi}}{\tilde {\eta} _ {\mathrm {a}}} = \frac {\mathrm {K} _ {\phi} \left[ \mathrm {s} ^ {2} + 2 \zeta_ {\phi} \omega_ {\phi} \mathrm {s} + \omega_ {\phi} ^ {2} \right] \mathrm {e} ^ {- \tau_ {\mathrm {p}} \mathrm {s}}}{\left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\mathrm {s}}}\right) \left(\mathrm {s} + \frac {1}{\mathrm {T} _ {\mathrm {R}}}\right) \left[ \mathrm {s} ^ {2} + 2 \zeta_ {\mathrm {d}} \omega_ {\mathrm {d}} \mathrm {s} + \omega_ {\mathrm {d}} ^ {2} \right]} \tag {9}
$$

and

$$
\frac {\tilde {\beta}}{\tilde {\eta} _ {r}} = \frac {\left(A _ {3} s ^ {3} + A _ {2} s ^ {2} + A _ {1} s + A _ {0}\right) e ^ {- \tau_ {\beta} s}}{\left(s + \frac {1}{T _ {s}}\right) \left(s + \frac {1}{T _ {R}}\right) \left[ s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} ^ {2} \right]}. \tag {10}
$$

The military standard does not suggest these two transfer functions be estimated simultaneously, but in either (9) or (10), there is still a substantial number of parameters to be estimated. If we look only at (9) and assume

$$
\mathbf {p} \approx \dot {\boldsymbol {\phi}} \quad \text {o r} \quad \tilde {\mathbf {p}} \approx \mathbf {s} \tilde {\boldsymbol {\phi}},
$$

then we can rewrite the transfer function as

$$
\frac {\tilde {p}}{\tilde {\eta} _ {a}} = \frac {K _ {\phi} s \left[ s ^ {2} + 2 \zeta_ {\phi} \omega_ {\phi} s + \omega_ {\phi} ^ {2} \right] e ^ {- \tau_ {p} s}}{\left(s + \frac {1}{T _ {s}}\right) \left(s + \frac {1}{T _ {R}}\right) \left[ s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} ^ {2} \right]}. \tag {11}
$$

Additionally, if we assume that the spiral mode time constant, $T_{s}$ , is large, then we can simplify (11) to

$$
\frac {\tilde {p}}{\tilde {\eta} _ {a}} = \frac {K _ {\phi} \left[ s ^ {2} + 2 \zeta_ {\phi} \omega_ {\phi} s + \omega_ {\phi} {} ^ {2} \right] e ^ {- \tau_ {p} s}}{\left(s + \frac {1}{T _ {R}}\right) \left[ s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} {} ^ {2} \right]} = \frac {\left[ K _ {\phi} s ^ {2} + C s + D \right] e ^ {- \tau_ {p} s}}{\left(s + \frac {1}{T _ {R}}\right) \left[ s ^ {2} + 2 \zeta_ {d} \omega_ {d} s + \omega_ {d} {} ^ {2} \right]}, \tag {12}
$$

where

$$
\mathbf {C} = 2 \mathbf {K} _ {\phi} \zeta_ {\phi} \omega_ {\phi},
$$

and

$$
\mathbf {D} = \mathbf {K} _ {\boldsymbol {\phi}} \boldsymbol {\omega} _ {\boldsymbol {\phi}} ^ {2}.
$$

This simplification not only reduces the order of the transfer function, but also eliminates one parameter from the estimation. Once again the model is stated in terms of generic

parameters as in (3); however, there are still a large number of parameters to be estimated in the transfer function. One option to reduce the number of parameters in the estimation is to fix the values of those which have already been estimated. For example, if a yaw frequency sweep was used to estimate the Dutch roll parameters in equation (7) or (8), then those can be fixed in the estimation of (12) when using a roll frequency sweep.

Another alternative which reduces the number of parameters significantly is to assume the numerator and denominator quadratics are nearly equal, which assumes the aircraft behaves as a first-order system:

$$
\frac {\tilde {p}}{\tilde {\eta} _ {a}} = \frac {K _ {p} e ^ {- \tau_ {p} s}}{s + \frac {1}{T _ {R}}}. \tag {13}
$$

This transfer function allows only one degree of freedom, and a large modeling error will be introduced if this model is used and the assumption of pole-zero cancellation of the quadratics is not valid.

# 4. IDENTIFICATION METHODOLOGY

The selected identification techniques were the equation error and output error methods in the frequency domain. In the following sections, the reasoning for this choice is explained and the selected methods are developed for one and two measurements for the longitudinal mode. This development is based on reference 17. The lateral and directional modes are easily developed in the same manner.

# 4.1 Time and Frequency Domain

The time domain method used in reference 9 minimized the squared error between the measured data and model output for the parameter estimation. Time domain matching was an attractive option since the measured output and input data were all that were required. However, the optimization technique, when applied to (3) and (4), can have serious convergence problems. This can be illustrated by rearranging the transfer function (3) and expressing it in the time domain:

$$
\ddot {\mathbf {q}} + \mathrm {k} _ {1} \dot {\mathbf {q}} + \mathrm {k} _ {0} \mathbf {q} = \mathrm {A} \dot {\eta} _ {\mathrm {e}} (\mathrm {t} - \tau_ {\theta}) + \mathrm {B} \eta_ {\mathrm {e}} (\mathrm {t} - \tau_ {\theta}). \tag {14}
$$

The time delay, $\tau_{\theta}$ , is a parameter to be estimated; however, any perturbation in $\tau_{\theta}$ would change the input form. If the optimization algorithm can actually converge to a solution, the estimates would likely have high errors.

On the other hand, rearranging (3) in the frequency domain gives

$$
- \omega^ {2} \tilde {q} + j \omega k _ {1} \tilde {q} + k _ {0} \tilde {q} = j \omega A \tilde {\eta} _ {\mathrm {e}} e ^ {- j \omega \tau_ {\theta}} + B \tilde {\eta} _ {\mathrm {e}} e ^ {- j \omega \tau_ {\theta}}. \tag {15}
$$

The most notable benefit to frequency domain analysis is the time delay is an ordinary parameter and will not alter the input form during the estimation procedure. Additionally, the integration of the state equations is not required for the estimation procedure; the mathematics are reduced to algebraic manipulations. The primary disadvantage to frequency domain analysis is the data must be transformed for analysis. Frequency domain techniques were selected to reduce convergence problems and eliminate numerical integration.

# 4.2 Equation Error Method

In the equation error method (EEM), the measured time histories are Fourier transformed and the transfer function model is used to match the complex data in the frequency domain. Translation to the frequency domain was performed with a high accuracy Fourier transform (ref. 18) to eliminate translation errors. The typical formulation for the equation error method is for only one output measurement. However, the formulation can also be extended to two or more output measurements. Both of these formulations are briefly presented below, and a full development of the equation error method for one output measurement is presented in reference 10.

# 4.2.1 One Output Measurement

In EEM, the sum of squared errors satisfying the equation is minimized. Recall equation (15):

$$
- \omega^ {2} \tilde {\mathrm {q}} + \mathrm {j} \omega \mathrm {k} _ {1} \tilde {\mathrm {q}} + \mathrm {k} _ {0} \tilde {\mathrm {q}} = \mathrm {j} \omega \mathrm {A} \tilde {\eta} _ {\mathrm {e}} \mathrm {e} ^ {- \mathrm {j} \omega \tau_ {\theta}} + \mathrm {B} \tilde {\eta} _ {\mathrm {e}} \mathrm {e} ^ {- \mathrm {j} \omega \tau_ {\theta}}.
$$

When all terms containing unknown parameters are moved to the right-hand side, the estimation for the single measurement of pitch rate then becomes:

$$
- \omega^ {2} \tilde {\mathrm {q}} = \left[ \begin{array}{l l l l} - \mathrm {j} \omega \tilde {\mathrm {q}} & - \tilde {\mathrm {q}} & \mathrm {j} \omega \tilde {\eta} _ {\mathrm {e}} e ^ {- \mathrm {j} \omega \tau_ {\theta}} & \tilde {\eta} _ {\mathrm {e}} e ^ {- \mathrm {j} \omega \tau_ {\theta}} \end{array} \right] \left[ \begin{array}{l} k _ {1} \\ k _ {0} \\ A \\ B \end{array} \right]. \tag {16}
$$

The parameters can then be perturbed until the right-hand side of (16) is equal to the left-hand side within an acceptable stopping criterion. Specifically, the cost function to be minimized for (16) is

$$
\mathrm {J} (\lambda) = \frac {1}{2} \sum_ {\mathrm {i} = 1} ^ {\mathrm {m}} \left[ - \omega_ {\mathrm {i}} ^ {2} \tilde {\mathrm {q}} _ {\mathrm {i}} + \left(\mathrm {j} \omega_ {\mathrm {i}} \mathrm {k} _ {\mathrm {l}} + \mathrm {k} _ {\mathrm {0}}\right) \tilde {\mathrm {q}} _ {\mathrm {i}} - \left(\mathrm {j} \omega_ {\mathrm {i}} \mathrm {A e} ^ {- \mathrm {j} \omega_ {\mathrm {i}} \tau_ {\theta}} + \mathrm {B e} ^ {- \mathrm {j} \omega_ {\mathrm {i}} \tau_ {\theta}}\right) \tilde {\mathfrak {n}} _ {\mathrm {e} _ {\mathrm {i}}} \right] ^ {2}, \quad (1 7)
$$

where $\lambda$ represents the vector of estimated parameters, $\lambda = [\mathbf{k}_1\mathbf{k}_0\mathbf{A}\mathbf{B}\tau ]'$ and $m$ represents the number of frequencies. A tilde ( $\sim$ ) over the variable represents the Fourier transform of that variable. Since equation (17) is nonlinear in the parameters, the parameter estimation constitutes a nonlinear estimation problem and will require the use of an iterative technique. The modified Newton-Raphson technique (ref. 19) was employed for the estimation of the parameters.

# 4.2.2 Two Output Measurements

The formulation for two measurements is identical in theory to that for one measurement with a few exceptions. If the second measurement of normal acceleration is rearranged in the same way as pitch rate, an equation analogous to (16) is formed:

$$
- \omega^ {2} \tilde {\mathrm {a}} _ {z} = \left[ \begin{array}{l l l} - \mathrm {j} \omega \tilde {\mathrm {a}} _ {z} & - \tilde {\mathrm {a}} _ {z} & - \frac {\mathrm {V} _ {0}}{\mathrm {g}} \tilde {\eta} _ {\mathrm {e}} \mathrm {e} ^ {- \mathrm {j} \omega \tau_ {\theta}} \end{array} \right] \left[ \begin{array}{l} \mathrm {k} _ {1} \\ \mathrm {k} _ {0} \\ \mathrm {B} \end{array} \right]. \tag {18}
$$

The optimization scheme will now have to estimate parameters that satisfy equations (16) and (18) simultaneously. The cost function for this method can be written as

$$
J (\lambda) = \frac {1}{2} \sum_ {i = 1} ^ {m} \left(\tilde {\mathrm {Y}} _ {\mathrm {E} _ {i}} - \tilde {\mathrm {Y}} _ {i} (\lambda)\right) ^ {*} S _ {\mathrm {v v}} ^ {- 1} \left(\tilde {\mathrm {Y}} _ {\mathrm {E} _ {i}} - \tilde {\mathrm {Y}} _ {i} (\lambda)\right), \tag {19}
$$

where the E subscript denotes experimental, or measured value; that is,

$$
\tilde {\mathrm {Y}} _ {\mathrm {E}} = \left[ \begin{array}{l l} - \omega^ {2} \tilde {\mathrm {q}} & - \omega^ {2} \tilde {\mathrm {a}} _ {z} \end{array} \right] ^ {\mathrm {T}}. \tag {20}
$$

Then,

$$
\mathbf {\tilde {Y}} (\lambda) = \left[ \begin{array}{l l} \mathbf {\tilde {Y}} _ {\mathrm {q}} & \mathbf {\tilde {Y}} _ {\mathrm {a} _ {z}} \end{array} \right] ^ {\mathrm {T}} \tag {21}
$$

is formulated where $\tilde{\mathrm{Y}}_{\mathrm{q}}$ and $\tilde{\mathrm{Y}}_{\mathrm{a}_z}$ are equivalent to the right-hand sides of equations (16) and (18), respectively. $S_{\mathrm{vv}}$ is the spectral density of the measurement noise estimated from the residuals:

$$
S _ {v v} = \frac {1}{m} \tilde {v} \tilde {v} ^ {*}, \tag {22}
$$

where

$$
\tilde {\nu} = \tilde {\mathrm {Y}} _ {\mathrm {E}} - \tilde {\mathrm {Y}} (\lambda). \tag {23}
$$

This weighting matrix is required to account for the different physical values of the pitch rate and normal acceleration.

# 4.3 Output Error Method

An alternative approach also developed in reference 10 is the output error method (OEM). In this approach, the sum of squared differences between the measured and model outputs is minimized. Aside from this difference the development is identical to the equation error method.

# 4.3.1 One Output Measurement

The development begins with the transfer function relating pitch rate to stick, equation (3):

$$
\frac {\tilde {q}}{\tilde {\eta} _ {\mathrm {e}}} = \frac {(\mathrm {A s} + \mathrm {B}) e ^ {- \tau_ {\theta} s}}{s ^ {2} + k _ {1} s + k _ {0}}.
$$

Now the equation is rearranged and converted to the frequency domain leaving the measured output, $\tilde{\mathbf{q}}$ , segregated on the left-hand side and the remaining terms on the right-hand side:

$$
\tilde {q} = \frac {\left(j \omega A + B\right) e ^ {- j \omega \tau_ {\theta}}}{- \omega^ {2} + j \omega k _ {1} + k _ {0}} \tilde {\eta} _ {e}. \tag {24}
$$

Note that the optimization theory is the same; that is, vary the parameter values until the right-hand side of (24) becomes acceptably close to the left-hand side. The cost function is written as

$$
J (\lambda) = \frac {1}{2} \sum_ {i = 1} ^ {m} \left[ \tilde {q} _ {\mathrm {E} i} - \tilde {q} _ {i} (\lambda) \right] ^ {2}, \tag {25}
$$

where the subscript $\mathrm{E}$ once again denotes the experimental value and $\tilde{\mathbf{q}}_{\mathrm{i}}(\lambda)$ denotes that value of pitch rate obtained from the right hand side of (24).

# 4.3.2 Two Output Measurements

If desired, the measurement of normal acceleration can also be used in OEM. The individual equation for normal acceleration analogous to (24) is

$$
\tilde {a} _ {z} = \frac {- \frac {V _ {0}}{g} B e ^ {- j \omega \tau_ {\theta}}}{- \omega^ {2} + j \omega k _ {1} + k _ {0}} \tilde {\eta} _ {e}. \tag {26}
$$

The cost function looks identical to that for EEM:

$$
J (\lambda) = \frac {1}{2} \sum_ {i = 1} ^ {m} \left(\tilde {\mathrm {Y}} _ {\mathrm {E} _ {i}} - \tilde {\mathrm {Y}} _ {i} (\lambda)\right) ^ {*} S _ {\mathrm {v v}} ^ {- 1} \left(\tilde {\mathrm {Y}} _ {\mathrm {E} _ {i}} - \tilde {\mathrm {Y}} _ {i} (\lambda)\right), \tag {27}
$$

but now $\tilde{\mathbf{Y}}_{\mathrm{E}}$ is given by

$$
\tilde {\mathrm {Y}} _ {\mathrm {E}} = \left[ \begin{array}{l l} \tilde {\mathrm {q}} & \tilde {\mathrm {a}} _ {z} \end{array} \right] ^ {\mathrm {T}}, \tag {28}
$$

and

$$
\tilde {\mathrm {Y}} (\lambda) = \left[ \begin{array}{l l} \tilde {\mathrm {Y}} _ {\mathrm {q}} & \tilde {\mathrm {Y}} _ {\mathrm {a} _ {z}} \end{array} \right] ^ {\mathrm {T}} \tag {29}
$$

is formulated from the right hand sides of equations (24) and (26), respectively. The $S_{\mathrm{vw}}$ matrix is formed in the same way as in EEM. If desired, the estimates obtained from EEM can be used as initial estimates in OEM to decrease convergence time.

# 4.4 Output Error Method for Frequency Response Data

One of the most popular estimation techniques in the frequency domain involves frequency response matching (ref. 6-8). This entails a least squares fit of the Bode plot (magnitude and phase) in the frequency domain using the transfer function as the model. The frequency response from the measured time histories is found from a ratio of the cross-spectral density of the input and output to the auto-spectral density of the input. For the longitudinal case, this can be written as

$$
\mathrm {H} (\omega) = \frac {\mathrm {S} _ {\eta_ {\mathrm {e}} \mathrm {q}} (\omega)}{\mathrm {S} _ {\eta_ {\mathrm {e}} \eta_ {\mathrm {e}}} (\omega)}. \tag {30}
$$

The accuracy of the model identification depends on the accurate computation of frequency response data points from the measured data; subsequently, this requires accurate spectral estimates. In order to obtain accurate spectral estimates, reference 7 suggests the use of four different data conditioning techniques: digital prefiltering, overlapped/tapered windowing, the chirp z-transform, and composite window averaging. These methods not only require a significant amount of computation time and effort, but the accuracy of the spectral estimates is also a function of the amount of data available.

Though frequency response matching is a very common estimation technique in parameter estimation, it would be advantageous to use a method which does not require such enormous amounts of computational work.

# 5. ANALYSIS OF SIMULATED DATA

Having the model structure predetermined as a LOES by the military standard is advantageous since a major step in the system identification process, i.e. model structure determination, can be eliminated; however, it can be a great disadvantage if the model is inadequate in representing the higher-order system (HOS). As a check on the model structure and the estimation algorithms, a simulation case was developed for the longitudinal mode which could judge the performance of the LOES model using outputs generated by a higher order system which emulated actual Tu-144 flight dynamics. For the lateral modes, simulation cases were developed which checked only the identifiability of the models. Both types of simulations and the conclusions drawn from them are discussed in this section.

# 5.1 Longitudinal Simulation

The Tu-144 HOS model for the longitudinal mode was created by adding first order control system dynamics to the short period mode. The dynamics of the model were chosen to approximate the Tu-144 during a maneuver performed at a Mach number of 0.9 at 32,000 feet and angle of attack of $6^{\circ}$ . Only approximate coefficient values were required since the order of the system was of greater importance than the exact model. The HOS models were determined to be:

$$
\frac {\tilde {q}}{\tilde {\eta} _ {e}} = \frac {1 2 . 4 s + 8 . 1}{(s + 0 . 9 8) (s ^ {2} + 2 (0 . 6) (4 . 3) s + (4 . 3) ^ {2})} \tag {31}
$$

and

$$
\frac {\tilde {a} _ {z}}{\tilde {\eta} _ {c}} = \frac {- 2 1 9 . 6}{(s + 0 . 9 8) (s ^ {2} + 2 (0 . 6) (4 . 3) s + (4 . 3) ^ {2})}. \tag {32}
$$

By including the first order control system, an additional pole was added to those of the short period mode.

These models along with a frequency sweep input from measured Tu-144 data were used to create simulated time histories of pitch rate and normal acceleration. Gaussian noise was added to the simulated outputs to represent random measurement variations. The noise level had a standard deviation of $10\%$ of the root mean square value of the simulated output. These noisy outputs were then used as "measured" time histories to estimate parameters in the LOES models to see how well the LOES estimation of the output could match the simulated time histories. Parameters in (3) and (4) were estimated using EEM and OEM for both a single output (pitch rate, q) and for two outputs (pitch rate, q, and normal acceleration, $\mathbf{a}_{z}$ ). The frequency range of interest was 0.1 rad/sec to $2\pi$ rad/sec in 0.01 rad/sec increments. A wider frequency range of 0.1 rad/sec to 10 rad/sec is suggested by the military standard; however, upon spectral analysis of the input signal for all maneuvers on the Tu-144, it was found that the signal had little frequency content at frequencies greater than $2\pi$ rad/sec. Thus, the narrower band was selected. Though the estimation is carried out in the frequency domain, it is more physically meaningful to compare the estimated model in the time domain with the measured output. The time histories of the simulated output from (31) and the estimation of the LOES model output from EEM for one output are shown in figure 4a. Figure 4b shows the residuals, the difference between simulated and model output, for this fit. Even in the presence of measurement and modeling errors,

the fit in the time domain is excellent. The application of the other three methods on the same data produced similar fits for all outputs. The parameter estimates for the single output EEM were

$$
\left[ \begin{array}{l} \mathrm {K} _ {\theta} \\ 1 / \mathrm {T} _ {\theta_ {2}} \\ \zeta_ {\mathrm {s p}} \\ \omega_ {\mathrm {s p}} \\ \tau_ {\theta} \end{array} \right] = \left[ \begin{array}{l} 1. 9 7 2 (0. 0 5 4) \\ 2. 0 4 8 (0. 1 1 6) \\ 0. 6 0 7 (0. 0 1 8) \\ 2. 9 2 2 (0. 0 6 1) \\ 0. 1 2 0 (0. 0 0 4) \end{array} \right].
$$

The standard errors of the parameters, noted parenthetically next to the estimates, were $6\%$ or less. The short period damping ratio, $\zeta_{\mathrm{sp}}$ , remained approximately the same as in the higher-order model, but the natural frequency, $\omega_{\mathrm{sp}}$ , decreased by roughly $30\%$ . The estimates of the static gain, $\mathbf{K}_{\theta}$ , and pitch attitude zero, $1 / \mathrm{T}_{\theta_2}$ , also differed significantly from the higher-order system. This indicates some of the effects the addition of the time delay and the use of the LOES may have on the parameter estimates.

Upon analysis of the normalized pairwise parameter correlation matrices, it was discovered that there was a high correlation between $\mathbf{k}_0$ and B for all of the cases except EEM for two outputs. The OEM model with one output also had a high correlation between $\mathbf{k}_1$ and A, and the OEM model with two outputs had additional high correlations between $\mathbf{k}_1$ and $\mathbf{k}_0$ , A and B and between $\mathbf{k}_0$ and A. The correlation matrices for all four cases are presented in table 8. A 'high' correlation is defined in this paper as one whose absolute value is greater than 0.90. Since the correlation matrix is symmetrical, the upper triangle is blacked out for clarity.

Insight into the differences between estimation techniques may be evident in the correlation matrices. Correlated variables in an estimation are mathematically analogous to having more unknowns than equations. There is simply not enough information to find a unique solution. Thus, high correlations may reduce the accuracy of the parameter

estimates. In three of the methods, a high correlation occurs between the parameters $\mathbf{k}_0$ and B. Together, these two terms represent the static gain of the transfer function, and the model is not structured in a way to prevent this correlation. In the single measurement OEM, an additional high correlation is present. Finally, for the two measurement OEM, a total of five high correlations exist. The data and model structure were held constant for all methods. This indicates that the source of the differences between the correlation matrices was the estimation technique itself.

Looking only at the number of high correlations in the estimation, the simulation cases illustrated that for the given models and data sets that in this application, the output error method was not an appropriate choice for this purpose. Eliminating errors in the methodology was critical to the overall quality of the results; thus, the output error method was abandoned at this point. EEM for both one and two outputs were still to be used.

# 5.2 Lateral Simulation

The purpose of the lateral simulations was a check on the identifiability of the models. A model is said to be identifiable if all of the model parameters can be estimated with the identification method and given data. The applicability of a LOES to a high-order system was not of primary importance. In these simulations, models given in section 3.2 were used along with frequency sweep inputs to generate simulated outputs. Noise was added as in the longitudinal simulations to the outputs and an attempt was made to estimate the parameters in the same model using either EEM or OEM. Attempting to estimate all of the parameters at once, using a roll frequency sweep with either (5) and (6) simultaneously or (9) individually, or using a yaw frequency sweep with (10), was not successful. The parameters were highly dependent on the starting values, especially if the numerator and denominator quadratic terms were approximately equal. When these values were not close to one another, the model could be estimated, but with substantial computation time and

several high pairwise parameter correlations. Another option was to estimate the Dutch roll and roll-mode time constant separately using different models. Both (7) and (8) were used to estimate the Dutch roll parameters. Each of these models were easily identifiable and the parameters all had low standard errors and approximated the known values in the simulation within $1\%$ . For the roll-mode time constant, equations (12) and (13) were used. Again, the numerator and denominator quadratic terms were important in the estimation, as (12) was very difficult to estimate when the quadratics were approximately equal, but the model was well-suited when these terms were not nearly equal. Equation (13) was estimated quite easily when the simulated data was created with the same model structure, but if a higher-order system was used to create the simulated data and the numerator and denominator quadratics were not equal, the estimated model had high errors in the fit between simulated and estimated output. Thus, (13) is appropriate only if the numerator and denominator quadratics are approximately equal. Once again, EEM had fewer high correlations and lower standard errors than OEM in all cases. This reiterates the reasons for abandoning OEM for this application.

In short for the lateral modes, the Dutch roll parameters are estimated using either (7) or (8) with a yaw frequency sweep. The roll-mode time constant is then estimated using a roll frequency sweep and either (12) or (13). If (12) is used, the Dutch roll parameters in the model are fixed to those estimated from the yaw frequency sweep at the same flight condition.

# 6. FLIGHT TEST RESULTS AND DISCUSSION

This section includes the application of the mathematical models and identification methodology to the flight test data. All maneuvers were analyzed using Matlab v5.1 on a 200 MHz Ultra Sparc 2 Unix system. Average time to analyze a single maneuver from raw data to final estimate was under two minutes.

# 6.1 Longitudinal Results

Twenty-one longitudinal frequency sweeps were analyzed for the Tu-144. The Mach number for these flights ranged from 0.3-1.6. Parameters of equation (3) and (4) were to be estimated using EEM for both one and two outputs (q alone or q and $\mathbf{a}_{\tau}$ , respectively) over the same frequency range as the simulations.

However, EEM for two outputs did not converge for the flight test data. This was an indication that there was something inconsistent in the flight test data between the measurements of pitch rate and normal acceleration that was not present in the simulations. Hence, transfer function coefficients for all 21 sweeps were estimated using the equation error method in the frequency domain with one output (q). The estimated transfer function coefficients were tabulated along with their standard errors in table 9. Flying qualities were then predicted using the estimated transfer function coefficients and MIL-STD-1797A. The flying quality predictions are shown in table 10. The longitudinal flying qualities of the Tu-144 were predicted to be level 2 or 3 for all maneuvers. The poor ratings were caused by high estimates of the time delay in the transfer function. Note that even with the modification to relax the time delay mentioned in section 3.1, the Tu-144 would still be a level 2 aircraft in all cases.

Figure 5 contains plots of the values and standard errors of each parameter for every test point number. This figure best illustrates the proximity of the results for the repeated

maneuvers. For roughly $90\%$ of the estimations, the repeat cases were within $2\sigma$ of each other. One notable exception is test point number 2.4-15.1A. Though the fit of the estimation and prediction were acceptable, the values for all of the estimated parameters are quite different from the other two repeated maneuvers at the same flight conditions. The aircraft configuration and flight conditions were identical in the repeat cases. Since there are two cases which contradict the parameter estimates of 2.4-15.1A, this maneuver would likely be discarded. Figures 6-8 summarize the results obtained for a maneuver at Mach 0.3, 0.9, and 1.6, respectively. Each of these figures includes a plot of the measured and estimated frequency sweep, a plot of the measured and predicted doublet, the flight conditions for the sweep and doublet, the parameter values and standard errors, and the flying qualities prediction. The predicted doublet was at similar flight conditions and the same aircraft configuration. The comparisons are shown in the time domain, although the modeling was done in the frequency domain.

Looking again at figure 5, it can be seen that the estimated parameters for test point numbers 2.4-3.1A,B and 2.4-16.1A,B-2.4-21.1A,B were all comparable. For the first parameter value in figure 5, $\mathrm{K}_{\theta}$ , the parameter estimates for similar flight conditions are grouped together. These maneuvers were all flown at similar flight conditions and aircraft configurations. The extension of the landing gear in test point numbers 2.4-19.1A,B had little effect on the parameter estimates. The most notable differences in parameter values occurred in the high subsonic and supersonic maneuvers, but both the flight conditions and aircraft configurations were different in these cases so parameter variations can be expected. Neither the Mach number nor the angle of attack varied while the other remained fixed; therefore, it cannot be determined how either of these variables individually affect the parameter estimates. However, average values can be given over a range of similar flight conditions where there was no significant change in the estimated parameters. Table 11 lists three different ranges of Mach numbers and angles of attack: low subsonic, high subsonic, and supersonic with their corresponding range of $\alpha$ and average value of each parameter at

that flight condition. Test point number 2.4-15.1A was discarded for the calculation of the averages for the reasons mentioned above. With the exception of $\mathbf{K}_{\theta}$ which had extremely small errors, the average values fell within the $2\sigma$ bounds of nearly every estimate in the particular range of flight conditions. The parameter estimates had very low standard errors, almost always less than $10\%$ , for all maneuvers.

In general for all for all of the maneuvers, the estimate of the output for the high frequency data fit the measured output better than the estimate at lower frequencies in many of the frequency sweep estimations. This was due to the formulation of the equation error method which has a weighting on the higher frequencies caused by the $\omega^2$ term in the equation. The low frequency data was typically in the range of 0.3-0.7 rad/sec, and the average estimated short period natural frequency was 1.33 rad/sec, so this was not considered a major issue in the accuracy of the estimates.

However, the inaccuracy of the estimates at lower frequencies did affect the doublet predictions. The doublets mostly excited only one low frequency; there was very little excitation of the higher frequencies. If the low frequencies are not matched well for the frequency sweep, the estimated parameters will not be good predictors for the doublets. Conversely, if the sweep matched the low frequencies just as well as the high, then the estimated parameters would have good prediction capabilities for any frequency.

An alternative way of looking at the prediction capabilities is not to use the doublets at all, but rather employ the estimated model to predict another frequency sweep at similar flight conditions. Figure 9 illustrates the prediction of the frequency sweep from test point number 2.4-16.1B where the model has been identified from test point number 2.4-16.1A. The sweep is well predicted over a wide range of frequencies. Note that the best prediction occurs in the higher frequencies; this reiterates the high frequency weighting mentioned above. In general, the larger band of frequencies, the more difficult it will be to estimate a model which is good at every frequency. If some a priori knowledge of which frequencies

were of interest was given, it would be possible to limit the estimation to a more narrow band of frequencies to increase the accuracy in this band.

The normalized pairwise correlation matrices are not presented for each test maneuver, but high correlations appeared with the same parameters as in the simulation: $\mathbf{k}_0$ and B. Additional high correlations with $\mathbf{k}_1$ and B were present in the takeoff maneuvers (TPN 2.4-3.1A,B) and the landing gear extended approach maneuvers (TPN 2.4-19.1A,B). As mentioned in a previous section, the takeoff configuration differed from the approach configuration in the nose position. The flap positions are approximately equal for each of these maneuvers. For test point number 2.4-19.1A,B, the landing gear was extended, and even though the parameter estimates were approximately the same as for maneuvers at similar flight conditions with the landing gear retracted, the correlations were higher. The added high correlations for each of these different maneuvers may be due to the unusual configurations at these conditions.

At all supersonic maneuvers, the standard errors of the parameters were the lowest and there were no high correlations. This may not be a function of the airspeed, however, but rather the canard, which was extended for all low-speed maneuvers. The canard may introduce a nonlinear effect which cannot be accounted for in the linearized model. One test of this would be to fly a low speed approach maneuver with the canard retracted and investigate whether the errors are present in that estimation. These data were not available.

# 6.2 Lateral Results

For the lateral handling qualities, 19 yaw frequency sweeps and 19 roll frequency sweeps were analyzed on the Tu-144. The flight conditions and aircraft configurations were identical to those for the longitudinal maneuvers. Once again, EEM for a single output was employed. Which output was used depended on the model being identified. For the yaw frequency sweeps, equation (7) and (8) were identified over the same frequency range as the

simulations; however, the agreement between the measured and estimated time histories of the sideslip angle, $\beta$ , attained from the identification of equation (7) was very poor. This was likely due to the poor measurement of $\beta$ at higher frequencies. The time history of $\beta$ showed no oscillatory motion, and therefore had no frequency content, beyond a rudder pedal input frequency greater than roughly $\pi$ rad/sec. Therefore, the model could not be identified at these frequencies and this greatly impacted the parameter estimates. Thus, equation (7) was discarded in favor of (8) for the yaw frequency sweeps. Identifying the model in equation (8) gave the Dutch roll handling qualities parameters and standard errors shown in table 12.

Figure 10 contains plots of the values and $2\sigma$ error bars for each parameter at every test point number to once again show the proximity of the parameter estimates to one another. Though many of the repeat cases were within $2\sigma$ of one another, it can be seen that, in general, there was considerably more scatter in these results. However, the two parameters of concern for handling qualities prediction, $\zeta_{\mathrm{d}}$ and $\omega_{\mathrm{d}}$ , are fairly consistent for similar flight conditions. Test point number 2.4-15.3A deviated greatly in relation to the other two repeated maneuvers and was therefore discarded. The average parameter values for the same ranges of flight conditions used in table 11 are shown for the Dutch roll parameters in table 13. A greater number of the average values fall outside of the $2\sigma$ ranges of the parameters in the Dutch roll estimation than in the longitudinal estimation. This is consistent with the scatter and larger errors associated with the Dutch roll estimation. Possible explanations for this scatter are addressed below. Figures 11-13 summarize the results obtained for a maneuver obtained at Mach 0.3, 0.9, and 1.6, respectively. Each of these figures contains the same information found in figures 6-8 for the longitudinal maneuvers. Note that the agreement between measured and estimated time histories is better at higher frequencies. This is once again due to the weighting imposed by EEM to the larger values of $\omega$ .

The roll-mode time constant was estimated in two ways. Initially, the first-order roll rate to lateral stick transfer function in equation (13) was identified. The estimated parameters and standard errors are shown in table 14. Plots of these values with $2\sigma$ error bars are given in figure 14. Average values of the parameter estimates over the aforementioned ranges of flight conditions are listed in table 15. In these estimates, there seems to be considerable difference between the parameters at Mach 1.2 and 1.6. It is unknown why this difference occurs in these parameters. Other than these, the average values all fall fairly close to being within the $2\sigma$ error bounds of the parameter estimates.

Figures 15-17 summarize the results obtained for a maneuver obtained at Mach 0.3, 0.9, and 1.6, respectively. Each of these figures contains the same information found in figures 6-8 for the longitudinal maneuvers. Note that for the predicted time histories, the model fits the data as well as can be expected from a first-order model, but misses some of the higher-order dynamics in the measured data. These dynamics may be caused by either the rigid body motion of the aircraft or twisting and bending of the wing and body. This gives some indication that the assumption of pole-zero cancellation of the quadratic terms mentioned in section 3.2 may not be valid. The agreement between the measured and estimated time histories are quite good, but do have a slight mismatch in amplitude at higher frequencies ( $\omega > \pi$ rad/sec). The measured and estimated data are in phase with one another, so the mismatch can likely be attributed to a problem in the estimation of the static gain. Note that the formulation of equation (13) in EEM would not have the same $\omega^2$ weighting on the frequencies that was present in previous two estimations.

The roll-mode time constant was also estimated using a hybrid of equation (12). The term 'hybrid' is used because, although using the form of equation (12) is used, the values of the Dutch roll parameters, $\zeta_{\mathrm{d}}$ and $\omega_{\mathrm{d}}$ , are fixed during the estimation to values obtained from the yaw frequency sweep analysis. This allows a higher-order model to be used for the identification, but eliminates two of the parameters to be estimated. The estimated parameters and standard errors are shown in table 16. Plots of these values with

2σ error bars are given in figure 18. Average values of the parameter estimates over the aforementioned ranges of flight conditions are listed in table 17. There was some scatter in the parameter estimates once again, especially between the Mach 1.2 and 1.6 maneuvers again, but the most interesting results were in the estimation of the roll-mode time constant. For all three flight condition ranges, the roll-mode time constant was fairly consistent with the first-order estimation. For a Mach number of 0.3 to 0.4 and angle of attack of $8.2^{\circ}$ to $11^{\circ}$ , the value of the $\mathrm{T}_{\mathrm{R}}$ varied by only 0.017 seconds. The differences for the second and third flight condition ranges were 0.04 seconds and 0.12 seconds, respectively. Figures 19-21 summarize the results obtained for a maneuver obtained at Mach 0.3, 0.9, and 1.6, respectively. Each of these figures show the fit, parameter estimates, and handling qualities prediction for a lateral/directional maneuver in a format similar to that of figures 6-8 for the longitudinal maneuvers. Note that for the predicted time histories, the model tries to fit some of the higher-order dynamics in the measured data and fits the measured data slightly better than the first-order model. However, the agreement between the measured and estimated time histories is not as good as the first-order model in terms of the root-mean-square of the difference between the measured and estimated output. In this estimation, similar mismatches occurred at higher frequencies ( $\omega > \pi$ rad/sec), but now the estimated amplitude was much higher than the measured.

Note once again that equation (12) was formulated in EEM without a weighting on the higher frequencies. The Dutch roll parameters used as fixed values in the model, however, were estimated from a model which did weight the higher frequencies. This dichotomy may be the cause for the poor agreement at higher frequencies in these estimates. Nevertheless, the phase at higher frequencies was still identical for the measured and estimated time histories, and the amplitude mismatch at high frequencies would not likely affect the estimate of the roll-mode time constant.

With the Dutch roll and roll-mode time constant parameters estimated, a flying qualities prediction was made. These parameters are tabulated along with the predicted

flying qualities in table 18. Note that the values listed in the table for the roll-mode time constant are from the first-order model estimates, but using the third-order hybrid model estimates would not affect the handling qualities prediction. The Tu-144 was predicted to be level 1 for all lateral maneuvers. Another important note, however, is that the military standard places no requirements on the time delay for the lateral handling qualities.

Additional sources of error are present in the lateral estimations that were not seen in the longitudinal mode. The largest probable source of error and the likely cause of the scatter in the estimates is due to the coupling of the roll and yaw motion in the aircraft. This is attributed not only to the aerodynamic cross-derivatives, but also to the control system. For example, when the pilot deflects the rudder pedal, the aileron moves along with the rudder. This introduces roll dynamics to the aircraft which may not be accounted for in the assumptions made for the yaw rate to rudder pedal transfer function. Though a source of error, this coupling will not likely affect the handling qualities prediction.

The pairwise correlation matrices for the yaw frequency sweep analysis showed no high correlations between any of the parameters. For the first-order roll frequency sweep transfer functions, there was a high correlation between $\mathrm{K_p}$ and $1 / \mathrm{T}_{\mathrm{R}}$ . The third-order hybrid transfer function had high correlations between $\mathbf{K}_{\phi}$ and D. Recall that the mismatch at the higher frequencies for the first-order roll model output time histories was disregarded. This was because the cause was likely a problem with the static gain; however, it is now seen that the static gain is correlated with $1 / \mathrm{T}_{\mathrm{R}}$ , the parameter of interest. Though normally this would be of concern, the third-order hybrid model did not have a high correlation associated with the estimation of $1 / \mathrm{T}_{\mathrm{R}}$ ; the parameters $\mathbf{K}_{\phi}$ and D are both numerator terms.

Additionally, the time constants were approximately equal for either the first or third-order hybrid model; thus, performing both estimations gives more confidence in the handling qualities prediction. This also indicates that even if the assumption of pole-zero cancellation in the quadratic terms of the roll transfer function was incorrect, it had little effect on the estimate of $\mathrm{T}_{\mathrm{R}}$ .

# 7. CONCLUSIONS AND SUGGESTIONS FOR FUTURE WORK

The equation error method was applied in the frequency domain for the estimation of parameters in the specified transfer functions. These transfer functions were low-order equivalent system (LOES) models of the aircraft for pitching, rolling, and yawing motion. Some of the transfer functions were altered from those specified in the governing military standard to create models that could be more accurately estimated. The change in the models did not sacrifice the physical meaning of the estimated handling qualities parameters. Simulation cases were developed which emulated the Tu-144 supersonic transport and the LOES models were identified using the specified estimation technique. The agreement of the simulated data with the identified model response was very good. The same estimation procedure was applied to 21 pitch frequency sweeps, 19 yaw frequency sweeps, and 19 roll frequency sweeps from flight tests of the Tu-144. Parameter estimates and their standard errors were typically comparable between maneuvers repeated at the same flight conditions, and the agreement between measured and estimated output in the time domain was excellent for all maneuvers. The Tu-144 was predicted to have level 2 or 3 handling qualities in the longitudinal mode and level 1 in the lateral modes. The reason for the poor longitudinal rating was high estimates of the time delay in the transfer function.

In general, the new formulation of the military standard transfer functions and the use of the equation error method in the frequency domain provided an excellent method of estimating the handling qualities parameters. The parameter values were estimated with standard errors typically less than $10\%$ and could be estimated from the raw data in less than two minutes of computer time. Additionally, the first-order approximation of the roll rate to lateral stick transfer function yielded nearly identical estimates of the roll-mode time constant as the higher-order model which required a priori knowledge of the Dutch roll parameters.

In the future, the most obvious next step would be to compare the predictions to actual pilot ratings of the Tu-144. One major question would be how the pilots rate the aircraft in longitudinal motion, and if the results support the notion that the military standard requirement for time delay on large transport aircraft is too stringent.

There are no requirements on the types of maneuvers that must be flown, but only that the maneuvers properly excite the modes to be analyzed. Different maneuver forms (such as 3-2-1-1 or 2-1-1 pulses) can be designed which minimize flight time required to perform the maneuver while still offering enough information in the data. Another maneuver would be to perform step inputs along the roll axis, estimate the roll-mode time constant directly from the time history, and compare the results to those obtained from the frequency sweep. Maneuvers could also be performed which segregated the parameter variations with either Mach number or angle of attack.

Additionally, frequency response matching is one of the more popular methods of parameter estimation when the input form is a frequency sweep. A comparison of the results obtained in this paper and those obtained from frequency response matching would contribute to the field of parameter identification.

# REFERENCES

1.) Cooper, G. E., and Harper, R. P., Jr., "The Use of Pilot Rating in the Evaluation of Aircraft Handling Qualities", NASA TN-D-5153, 1969.   
2.) "Military Specification, Flying Qualities of Piloted Airplanes", MIL-F-8785B, August, 1969.   
3.) "Military Specification, Flying Qualities of Piloted Airplanes", MIL-F-8785C, November, 1980.   
4.) "Military Standard, Flying Qualities of Piloted Aircraft", MIL-STD-1797A, January, 1990.   
5.) Hoh, R., and Mitchell, R., "Low-Order Approaches to High-Order Systems: Problems and Promises", AIAA Paper 82-4250, 1982.   
6.) Tischler, M. B., "Frequency Response Identification of the XV-15 Tilt-Rotor Aircraft Dynamics", NASA TM-89428, May, 1987.   
7.) Tischler, M. B., "Identification Techniques - Frequency Domain Methods", AGARD Paper 92N17158, 1991.   
8.) Tischler, M. B., "System Identification Methods for Handling-Qualities Evaluation", AGARD Paper 92N17165, 1991.   
9.) Manning, C., and Gleason, D., "Flight Test Results Using a Low Order Equivalent Systems Technique to Estimate Flying Qualities", AIAA Paper 92-4425-CP, Atmospheric and Flight Mechanics Conference, Hilton Head Island, SC, August, 1992.   
10.) Klein, V., "Aircraft Parameter Estimation in the Frequency Domain", AIAA Paper 78-1344, Atmospheric Flight Mechanics Conference, Palo Alto, CA, August, 1978.   
11.) "Flight Research Using Modified Tu-144 Aircraft", Final Report Submitted by the Boeing Company, HSR-AT Contract No. NAS1-20220, May 1998, Volume 1.   
12.) "Flight Research Using Modified Tu-144 Aircraft", Final Report Submitted by the Boeing Company, HSR-AT Contract No. NAS1-20220, May 1998, Volume 6.   
13.) Klein, V., and Morgan, D. R., "Estimation of Bias Errors in Measured Airplane Responses Using the Maximum Likelihood Method", NASA TM-89059, January, 1987.   
14.) Rossitto, K., Hodgkinson, J., and Williams, T., "Initial Results of an In-Flight Investigation of Longitudinal Flying Qualities for Augmented, Large Transports in Approach and Landing", AIAA Paper 93-3816, 1993.   
15.) Weingarten, N., and Rynaski, E., “Flared Landing Approach Flying Qualities”, NASA CR-178188, Vol. I and II, December, 1986.

16.) Meyer, R., Knox, J., Tingas, S., "Suggested Revisions to the Mil-F-8785C for Large (Class III) Aircraft", Lockheed Georgia Company, February, 1983.   
17.) Morelli, E. A., "Identification of Low Order Equivalent System Models from Flight Test Data", NASA TM-2000-210117, August 2000.   
18.) Morelli, E. A., "High Accuracy Evaluation of the Finite Fourier Transform Using Sampled Data", NASA TM-110340, June 1997.   
19.) Iliff, K. W., Taylor, L. W., Jr., and Powers, B., “A Comparison of Newton-Raphson and Other Methods for Determining Stability Derivatives from Flight Data”, AIAA Paper 69-0315, 1969.   
20.) Coleman, H., and Steele, W.G, Jr., Experimentation and Uncertainty Analysis for Engineers, John Wiley and Sons, New York, 1989.

# APPENDIX A - MANEUVER DESCRIPTION

The pilots and test engineers were briefed before the flight test program and the experiment objectives and test procedures were explained. Descriptions of the individual test procedures for each of the maneuvers used in the handling qualities prediction are taken from reference 10 and given below:

# Pitch Frequency Sweep

Conditions: Minimal Turbulence, Autopilot Off, Autothrottle Off, No Throttle Position Changes

1. A test engineer in the back of the airplane should carefully monitor the control column position, load factor, and pitch attitude time history responses plotted on a computer screen in real time during this maneuver. The time scale should be expanded so that a frequency limit of TBD cycles per second for the input can be easily judged. Once this frequency limit is reached, the engineer should tell the pilot to stop making inputs to prevent excitation of the 2.5 cycle per second first bending mode of the airplane.   
2. Trim airplane for hands off level flight. Do not retrim during the remainder of this maneuver.   
3. Begin data recording and record 5 seconds of hands off level flight data.   
4. Slowly cycle the control column back and forth with an amplitude large enough to obtain $+ / - 0.2\mathrm{g}$ load factor and/or $+ / - 5$ to 15 degree pitch attitude excursions. Make two complete 20 second cycles of the control for a total of 40 seconds of input. The cycling of the control should be centered around a position that produces airplane oscillations that center around the trim pitch attitude. Control wheel and rudder pedals should be used to minimize roll and yaw response.

5. Slowly increase the frequency of the input. Adjust input amplitude so that the amplitude of airplane motion remains about the same as in step 4. It is important to increase frequency slowly, so that there is enough middle frequency content in the data. When the amplitude of airplane motion drops off sharply or the input frequency reaches TBD cycles per second, stop the input. Should a structural mode become excited, terminate input immediately. The combined inputs for steps 4. and 5. should last about 80 - 100 seconds.   
6. Record 5 seconds of hands off data at the end of the maneuver.

# Roll Frequency Sweep

Conditions: Minimal Turbulence, Autopilot Off, Autothrottle Off, No Throttle Position Changes

1. A test engineer in the back of the airplane should carefully monitor the control wheel position, roll rate, and roll angle time history responses of the airplane plotted on a computer screen in real time during this test. The time scale should be expanded so that a frequency limit of TBD cycles per second for the input can be easily judged. Once this frequency limit is reached, the engineer should tell the pilot to stop making inputs to prevent excitation of the 2.5 cycle per second first bending mode of the airplane.   
2. Trim airplane for hands off level flight. Do not retrim during the remainder of this maneuver.   
3. Begin data recording and record 5 seconds of hands off level flight data.   
4. Slowly cycle the control wheel back and forth with amplitude large enough to obtain $+ / - 5$ to 15 degree roll angle excursions. Make two complete 20 second cycles of the control for a total of 40 seconds of input. The cycling of the control should be centered around a position that produces airplane oscillations that center around a wings level roll angle. Rudder pedals should only be used if the airplane

oscillations do not remain centered about the initial heading angle. Control columns should be used to minimize pitch response.

5. Slowly increase the frequency of the input. Adjust input amplitude so that the amplitude of airplane motion remains about the same as in step 4. It is important to increase frequency slowly, so that there is enough middle frequency content in the data. When the amplitude of airplane motion drops off sharply or the input frequency reaches TBD cycles per second, stop the input. Should a structural mode become excited, terminate input immediately. The combined inputs for steps 4. and 5. should last about 80 - 100 seconds.   
6. Record 5 seconds of hands off data at the end of the maneuver.

# Yaw Frequency Sweep

Conditions: Minimal Turbulence, Autopilot Off, Autothrottle Off, No Throttle Position Changes

1. A test engineer in the back of the airplane should carefully monitor the rudder pedal position, yaw rate, and heading angle time history responses of the airplane plotted on a computer screen in real time during this test. The time scale should be expanded so that a frequency limit of TBD cycles per second for the input can be easily judged. Once this frequency limit is reached, the engineer should tell the pilot to stop making inputs to prevent excitation the 2.5 cycle per second first bending mode of the airplane.   
2. Trim airplane for hands off level flight. Do not retrim during the remainder of this maneuver.   
3. Begin data recording and record 5 seconds of hands off level flight data.   
4. Slowly cycle the rudder pedals back and forth with an amplitude large enough to obtain $+ / - 5$ to 15 degree heading angle excursions. Make two complete 20 second cycles of the control for a total of 40 seconds of input. The cycling of the control

should be centered around a position that produces airplane oscillations that center around the initial heading angle. Control wheel should only be used if the airplane oscillations do not remain centered about a wings level roll angle. Control column should be used to minimize pitch response.

5. Slowly increase the frequency of the input. Adjust input amplitude so that the amplitude of airplane motion remains about the same as in step 4. It is important to increase frequency slowly, so that there is enough middle frequency content in the data. When the amplitude of airplane motion drops off sharply or the input frequency reaches TBD cycles per second, stop the input. Should a structural mode become excited, terminate input immediately. The combined inputs for steps 4. and 5. should last about 80 - 100 seconds.   
6. Record 5 seconds of hands off data at the end of the maneuver.

# Pitch Doublet

Conditions: Minimal Turbulence, Autopilot Off, Autothrottle Off, No Throttle Position Changes

1. Trim airplane for hands off level flight. Do not retrim during the remainder of this maneuver.   
2. Begin data recording and record 5 seconds of hands off level flight data.   
3. Pull back on control column sharply and hold input for 5 seconds, push forward on control column sharply and hold input for 5 seconds, and then release the control column to neutral position. Inputs should be large enough to produce $+/-0.2\mathrm{g}$ load factor and/or $+/-5$ to 15 degree pitch attitude excursions. Control wheel and rudder pedals should be used to minimize roll and yaw response.   
4. Record 60 seconds of hands off data at the end of the maneuver.

# Roll Doublet

Conditions: Minimal Turbulence, Autopilot Off, Autothrottle Off, No Throttle Position Changes

1. Trim airplane for hands off level flight. Do not retrim during the remainder of this maneuver.   
2. Begin data recording and record 5 seconds of hands off level flight data.   
3. Rotate control wheel sharply one direction and hold input for 5 seconds, rotate control wheel sharply the other direction and hold input for 5 seconds, and then release the control wheel to neutral position. Inputs should be large enough to produce $+ / - 5$ to 15 degree roll angle excursions. Control column should be used to minimize pitch response.   
4. Record 60 seconds of hands off data at the end of the maneuver.

# Yaw Doublet

Conditions: Minimal Turbulence, Autopilot Off, Autothrottle Off, No Throttle Position Changes

1. Trim airplane for hands off level flight. Do not retrim during the remainder of this maneuver.   
2. Begin data recording and record 5 seconds of hands off level flight data.   
3. Push one rudder pedal sharply and hold input for 5 seconds, push the other rudder pedal sharply and hold input for 5 seconds, and then release the rudder pedals to neutral position. Inputs should be large enough to produce $+ / - 5$ to 15 degree heading angle excursions. Control column should be used to minimize pitch response.   
4. Record 60 seconds of hands off data at the end of the maneuver.

# APPENDIX B - ERROR PROPAGATION

The standard errors of the generic parameters introduced in (3) and (4) are not equivalent to those of the transfer function coefficients of the models from the military standard; however, the estimated standard errors can be used to estimate the errors of the desired coefficients through a linearized error propagation formula. Reference 20 explains uncertainty analysis in detail, but a short development of the theory and application to an example on the longitudinal mode is presented below.

Consider a general case in which an experimental result, $\mathbf{x}$ , is a function of $\mathbf{N}$ variables, $\mathbf{y}_i$ :

$$
\mathrm {x} = \mathrm {x} \left(\mathrm {y} _ {1}, \mathrm {y} _ {2}, \dots , \mathrm {y} _ {\mathrm {N}}\right). \tag {33}
$$

Equation (33) defines how to determine $\mathbf{x}$ from the known value of the variables $\mathbf{y}_i$ . The uncertainty in the result is given as

$$
\mathrm {U} _ {\mathrm {x}} = \left[ \left(\frac {\partial \mathrm {x}}{\partial \mathrm {y} _ {1}} \mathrm {U} _ {\mathrm {x} _ {1}}\right) ^ {2} + \left(\frac {\partial \mathrm {x}}{\partial \mathrm {y} _ {2}} \mathrm {U} _ {\mathrm {x} _ {2}}\right) ^ {2} + \dots + \left(\frac {\partial \mathrm {x}}{\partial \mathrm {y} _ {\mathrm {N}}} \mathrm {U} _ {\mathrm {x} _ {\mathrm {N}}}\right) ^ {2} \right] ^ {1 / 2}, \tag {34}
$$

where the $\mathrm{U}_{\mathrm{x},\mathrm{i}}$ represent the uncertainties in the dependent variables $\mathbf{y}_i$ .

The uncertainties of the estimated parameters and their functional dependence on the military standard coefficients are known; thus, equation (34) can be used to determine the desired standard errors. For example, the short period damping ratio is given in terms of the estimated generic parameters as

$$
\zeta_ {\mathrm {s p}} = \frac {\mathrm {k} _ {1}}{2 \mathrm {k} _ {0} ^ {1 / 2}}. \tag {35}
$$

Applying (34) to (35) yields

$$
\begin{array}{l} \sigma_ {\zeta_ {s p}} = \left[ \left(\frac {\partial \zeta_ {s p}}{\partial k _ {1}} \sigma_ {k _ {1}}\right) ^ {2} + \left(\frac {\partial \zeta_ {s p}}{\partial k _ {0}} \sigma_ {k _ {0}}\right) ^ {2} \right] ^ {1 / 2} \tag {36} \\ = \left[ \left(\frac {1}{2 \mathrm {k} _ {0} ^ {1 / 2}} \sigma_ {\mathrm {k} _ {1}}\right) ^ {2} + \left(- \frac {\mathrm {k} _ {1}}{4 \mathrm {k} _ {0} ^ {3 / 2}} \sigma_ {\mathrm {k} _ {0}}\right) ^ {2} \right] ^ {1 / 2}. \\ \end{array}
$$

Similarly, for the remaining coefficients,

$$
\sigma_ {\omega_ {\mathrm {s p}}} = \frac {1}{2 k _ {0} ^ {1 / 2}} \sigma_ {k _ {0}}, \tag {37}
$$

and

$$
\sigma_ {1 / T _ {\theta_ {2}}} = \left[ \left(\frac {1}{A} \sigma_ {B}\right) ^ {2} + \left(- \frac {B}{A ^ {2}} \cdot \sigma_ {A}\right) ^ {2} \right] ^ {1 / 2}. \tag {38}
$$

The errors of the final two parameters, $\mathbf{K}_{\theta}$ and $\tau$ , are estimated directly.

These error propagation formulae were used for all of the estimated parameters; however, they are only linear approximations of the errors. The first-order analytical functions were validated using a Monte Carlo simulation which multiplied a random variable with a mean of zero and variance of one by the standard error of each estimated parameter.

The product was then scaled by adding the estimated parameter value. For example, for the parameter $\mathbf{k}_0$ , a new parameter, $\mathbf{k}_0'$ , was created as

$$
\mathrm {k} _ {0} ^ {\prime} = \mathrm {k} _ {0} + \sigma (\mathrm {k} _ {0}) * \mathrm {r}, \tag {39}
$$

where $r$ represents a Gaussian distributed random variable. The Monte Carlo estimate of the short period natural frequency is then

$$
\omega_ {\mathrm {s p}} ^ {\prime} = \sqrt {\mathrm {k} _ {0} ^ {\prime}}. \tag {40}
$$

A random number generator was used to create 1000 values for $r$ and thus 1000 Gaussian distributed values for $\omega_{\mathrm{sp}}$ . The mean and standard deviation of the Monte Carlo simulation should be very close to that estimated by the analytical functions. The other variables were checked in the same fashion. Figure 22 illustrates the distribution of each of the checked variables for the parameters estimated from test point number 2.4-16.1A. A small table on each plot indicates the mean value and standard deviation for both the analytic function and the Monte Carlo simulation. These values indicate that the simulation validated the analytical functions.

TABLE 1: Summary of geometric, mass, and inertia characteristics of the Tu-144.   

<table><tr><td>Length</td><td>196 ft 10 in (60.0 m)</td></tr><tr><td>Span</td><td>88 ft 7 in (27.0 m)</td></tr><tr><td>Nose Tip to Leading Edge of MAC</td><td>98 ft 8 in (30.1 m)</td></tr><tr><td>Length of MAC</td><td>76 ft 5 in (23.3 m)</td></tr><tr><td>Wing Area</td><td>4716 ft2(438 m2)</td></tr><tr><td>Wing Aspect Ratio</td><td>1.66</td></tr><tr><td>Wing Sweep, Inboard Portions</td><td>76 deg</td></tr><tr><td>Wing Sweep, Main Panels</td><td>57 deg</td></tr><tr><td>Weight*</td><td>303,000 lb (138,000 kg)</td></tr><tr><td>Roll Axis Moment of Inertia, Ixx*</td><td>38,805,000 lbf-ft2(1,635,000 kg·m2)</td></tr><tr><td>Pitch Axis Moment of Inertia, Iyy*</td><td>417,797,000 lbf-ft2(17,606,000 kg·m2)</td></tr><tr><td>Yaw Axis Moment of Inertia, Izz*</td><td>450,222,000 lbf-ft2(18,973,000 kg·m2)</td></tr><tr><td>Roll-Yaw Product of Inertia, Ixyz*</td><td>-6,486,000 lbf-ft2(-273,000 kg·m2)</td></tr></table>

* Average values over all yaw frequency sweeps.

TABLE 2: Measured parameters used for data analysis.   

<table><tr><td>Parameter</td><td>Parameter Description</td><td>Units</td><td>+ Sign Convention</td><td>Range</td><td>Accuracy</td><td>Rate</td></tr><tr><td>PCOL</td><td>Control Column Position</td><td>mm</td><td>Pull</td><td>-100 - +250 mm</td><td>±1.5%</td><td>32 Hz</td></tr><tr><td>PWHL</td><td>Control Wheel Position</td><td>deg</td><td>Clockwise</td><td>±80 deg</td><td>±1.5%</td><td>32 Hz</td></tr><tr><td>PPED</td><td>Rudder Pedal Position</td><td>mm</td><td>Right Pedal</td><td>±125 mm</td><td>±1.5%</td><td>64 Hz</td></tr><tr><td>ERL</td><td>Left Elevon 1 Position</td><td>deg</td><td>Trailing Edge Down</td><td>±25 deg</td><td>±1.5%</td><td>64 Hz</td></tr><tr><td>ERP</td><td>Right Elevon 1 Position</td><td>deg</td><td>Trailing Edge Down</td><td>±25 deg</td><td>±1.5%</td><td>32 Hz</td></tr><tr><td>RUDDER</td><td>Upper Rudder Position</td><td>deg</td><td>Trailing Edge Left</td><td>±25 deg</td><td>±1.5%</td><td>64 Hz</td></tr><tr><td>PHI</td><td>Roll Euler Angle</td><td>deg</td><td>Right Wing Down</td><td>±90 deg</td><td>±1.2%</td><td>32 Hz</td></tr><tr><td>THETA</td><td>Pitch Euler Angle</td><td>deg</td><td>Nose Up</td><td>±90 deg</td><td>±1.2%</td><td>32 Hz</td></tr><tr><td>HEADING</td><td>Heading Angle</td><td>deg</td><td>Clockwise from North</td><td>±180 deg</td><td>±1.2%</td><td>16 Hz</td></tr><tr><td>P</td><td>Body Axis Roll Rate</td><td>deg/sec</td><td>Right Wing Down</td><td>±18 deg/sec</td><td>±2.0%</td><td>32 Hz</td></tr><tr><td>Q</td><td>Body Axis Pitch Rate</td><td>deg/sec</td><td>Nose Up</td><td>±6 deg/sec</td><td>±2.0%</td><td>32 Hz</td></tr><tr><td>R</td><td>Body Axis Yaw Rate</td><td>deg/sec</td><td>Clockwise</td><td>±6 deg/sec</td><td>±2.0%</td><td>32 Hz</td></tr><tr><td>NX</td><td>Longitudinal Acceleration</td><td>g&#x27;s</td><td>Forward</td><td>±0.5 g&#x27;s</td><td>±2.5%</td><td>32 Hz</td></tr><tr><td>NY</td><td>Lateral Acceleration</td><td>g&#x27;s</td><td>Right</td><td>±0.5 g&#x27;s</td><td>±2.5%</td><td>64 Hz</td></tr><tr><td>NZ</td><td>Vertical Acceleration</td><td>g&#x27;s</td><td>Up</td><td>-1.0 - +3.0 g&#x27;s</td><td>±2.5%</td><td>64 Hz</td></tr><tr><td>KTAS</td><td>True Airspeed</td><td>knots</td><td>Always +</td><td></td><td></td><td>16 Hz</td></tr><tr><td>HPC</td><td>Geopotential Pressure Altitude</td><td>feet</td><td>Up</td><td>0 - 22000 m</td><td>±0.6%</td><td>16 Hz</td></tr><tr><td>MACHC</td><td>Mach Number</td><td>No Units</td><td>Always +</td><td>0.0 - 2.5</td><td></td><td>16 Hz</td></tr><tr><td>ALPHA</td><td>Angle of Attack</td><td>deg</td><td>Nose Up Relative to Flight Path</td><td>±25 deg</td><td>±0.5%</td><td>32 Hz</td></tr><tr><td>BETA</td><td>Sideslip Angle</td><td>deg</td><td>Nose Left Relative to Flight Path</td><td>±15 deg</td><td>±0.5%</td><td>32 Hz</td></tr><tr><td>GW</td><td>Post Flight Computed Gross Weight</td><td>kg</td><td>Always +</td><td></td><td></td><td>Sparse</td></tr><tr><td>GTOCT</td><td>Total Fuel Quantity Remaining</td><td>metric tons</td><td>Always +</td><td>0 - 100 metric tons</td><td>±4.0%</td><td>8 Hz</td></tr><tr><td>CGX</td><td>Post Flight Computed Long. CG</td><td>% MAC</td><td>Always +</td><td></td><td></td><td>Sparse</td></tr><tr><td>CGV</td><td>Post Flight Computed Vertical CG</td><td>m</td><td>Up</td><td></td><td></td><td>Sparse</td></tr><tr><td>IXX</td><td>Roll Axis Moment of Inertia</td><td>kg-m²</td><td>Always +</td><td></td><td></td><td>Sparse</td></tr><tr><td>IYY</td><td>Pitch Axis Moment of Inertia</td><td>kg-m²</td><td>Always +</td><td></td><td></td><td>Sparse</td></tr><tr><td>IZZ</td><td>Yaw Axis Moment of Inertia</td><td>kg-m²</td><td>Always +</td><td></td><td></td><td>Sparse</td></tr><tr><td>IXZ</td><td>Roll - Yaw Product of Inertia</td><td>kg-m²</td><td>-</td><td></td><td></td><td>Sparse</td></tr></table>

TABLE 3: Coordinate location of instrumentation.   

<table><tr><td>Parameters</td><td>X (ft)</td><td>Y (ft)</td><td>Z (ft)</td></tr><tr><td>Airspeeds &amp; Pressures</td><td>-4.4</td><td>-2.7</td><td>0</td></tr><tr><td>Angle of Attack</td><td>+15.7</td><td>-1.4</td><td>-2.4</td></tr><tr><td>Sideslip</td><td>+15.7</td><td>+1.0</td><td>0</td></tr><tr><td>Rate Gyros &amp; Accelerometers</td><td>+106.6</td><td>-1.3</td><td>+2.46</td></tr></table>

Notes:

- The origin of the coordinate system is at the base of the nose boom/tip of nose cone.   
- Axis System:

$+\mathrm{X}$ is measured longitudinally from nose to tail   
$+\mathbf{Y}$ is measured vertically up   
+Z is measured laterally out the right wingtip

Note that this is a left-handed coordinate system.

KEY:

TPN

CG

LG

CND

NOSE

Alt.

Mach

Time

TABLE 4: Flight Test Maneuvers Performed for Handling Qualities Prediction.   

<table><tr><td rowspan="2">TPN</td><td rowspan="2">Test Title</td><td colspan="4">Aircraft Configuration</td><td colspan="2">Flight Conditions</td><td rowspan="2">Flight</td><td rowspan="2">Start Time</td><td rowspan="2">Stop Time</td></tr><tr><td>CG</td><td>LG</td><td>CND</td><td>NOSE</td><td>Alt. feet</td><td>Mach Number</td></tr><tr><td>2.4-3.1A</td><td>Takeoff Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>5900</td><td>0.33</td><td>14</td><td>9:34:00</td><td>9:36:00</td></tr><tr><td>2.4-3.1B</td><td>Takeoff Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6000</td><td>0.31</td><td>14</td><td>9:36:50</td><td>9:38:50</td></tr><tr><td>2.4-3.2A</td><td>Takeoff Roll Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6000</td><td>0.34</td><td>14</td><td>9:40:50</td><td>9:42:50</td></tr><tr><td>2.4-3.2B</td><td>Takeoff Roll Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>11°</td><td>5900</td><td>0.33</td><td>14</td><td>9:42:50</td><td>9:44:50</td></tr><tr><td>2.4-3.3A</td><td>Takeoff Yaw Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>11°</td><td>5900</td><td>0.33</td><td>14</td><td>9:45:50</td><td>9:47:50</td></tr><tr><td>2.4-3.3B</td><td>Takeoff Yaw Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6200</td><td>0.32</td><td>14</td><td>9:47:50</td><td>9:49:50</td></tr><tr><td>2.4-3.4A</td><td>Takeoff Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6300</td><td>0.32</td><td>14</td><td>9:22:00</td><td>9:23:00</td></tr><tr><td>2.4-3.4B</td><td>Takeoff Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6400</td><td>0.31</td><td>14</td><td>9:24:00</td><td>9:25:00</td></tr><tr><td>2.4-3.5A</td><td>Takeoff Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6300</td><td>0.33</td><td>14</td><td>9:26:00</td><td>9:27:00</td></tr><tr><td>2.4-3.5B</td><td>Takeoff Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6600</td><td>0.34</td><td>14</td><td>9:28:15</td><td>9:29:15</td></tr><tr><td>2.4-3.6A</td><td>Takeoff Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6600</td><td>0.33</td><td>14</td><td>9:30:00</td><td>9:31:00</td></tr><tr><td>2.4-3.6B</td><td>Takeoff Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>11°</td><td>6200</td><td>0.33</td><td>14</td><td>9:31:40</td><td>9:32:40</td></tr></table>

TABLE 4:Continued.   

<table><tr><td rowspan="2">TPN</td><td rowspan="2">Test Title</td><td colspan="4">Aircraft Configuration</td><td colspan="2">Flight Conditions</td><td rowspan="2">Flight</td><td rowspan="2">Start Time</td><td rowspan="2">Stop Time</td></tr><tr><td>CG</td><td>LG</td><td>CND</td><td>NOSE</td><td>Alt. feet</td><td>Mach Number</td></tr><tr><td>2.4-12.1A</td><td>Descent Pitch Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>49000</td><td>1.61</td><td>18</td><td>11:05:00</td><td>11:07:00</td></tr><tr><td>2.4-12.1B</td><td>Descent Pitch Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>49000</td><td>1.60</td><td>18</td><td>11:09:00</td><td>11:11:00</td></tr><tr><td>2.4-12.2A</td><td>Descent Roll Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>49000</td><td>1.57</td><td>18</td><td>11:11:00</td><td>11:13:00</td></tr><tr><td>2.4-12.2B</td><td>Descent Roll Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>48000</td><td>1.59</td><td>18</td><td>11:16:00</td><td>11:18:00</td></tr><tr><td>2.4-12.3A</td><td>Descent Yaw Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>48000</td><td>1.61</td><td>18</td><td>11:18:00</td><td>11:20:00</td></tr><tr><td>2.4-12.3B</td><td>Descent Yaw Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>48000</td><td>1.62</td><td>18</td><td>11:20:00</td><td>11:22:00</td></tr><tr><td>2.4-12.4A</td><td>Descent Pitch Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>47000</td><td>1.57</td><td>18</td><td>10:57:20</td><td>10:58:20</td></tr><tr><td>2.4-12.4B</td><td>Descent Pitch Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>49000</td><td>1.60</td><td>18</td><td>10:59:00</td><td>11:00:00</td></tr><tr><td>2.4-12.5A</td><td>Descent Roll Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>50000</td><td>1.60</td><td>18</td><td>11:00:50</td><td>11:01:50</td></tr><tr><td>2.4-12.5B</td><td>Descent Roll Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>48000</td><td>1.61</td><td>18</td><td>11:01:50</td><td>11:02:50</td></tr><tr><td>2.4-12.6A</td><td>Descent Yaw Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>48000</td><td>1.62</td><td>18</td><td>11:02:45</td><td>11:03:45</td></tr><tr><td>2.4-12.6B</td><td>Descent Yaw Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>48000</td><td>1.57</td><td>18</td><td>11:03:45</td><td>11:04:45</td></tr><tr><td>2.4-13.1A</td><td>Descent Pitch Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>43000</td><td>1.25</td><td>18</td><td>10:28:00</td><td>10:30:00</td></tr><tr><td>2.4-13.1B</td><td>Descent Pitch Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.24</td><td>18</td><td>10:30:00</td><td>10:32:00</td></tr><tr><td>2.4-13.2A</td><td>Descent Roll Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.22</td><td>18</td><td>10:32:00</td><td>10:34:15</td></tr><tr><td>2.4-13.2B</td><td>Descent Roll Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.21</td><td>18</td><td>10:34:15</td><td>10:36:15</td></tr><tr><td>2.4-13.3A</td><td>Descent Yaw Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>43000</td><td>1.19</td><td>18</td><td>10:37:00</td><td>10:39:00</td></tr><tr><td>2.4-13.3B</td><td>Descent Yaw Frequency Sweep</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.20</td><td>18</td><td>10:39:15</td><td>10:41:15</td></tr><tr><td>2.4-13.4A</td><td>Descent Pitch Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.21</td><td>18</td><td>10:18:00</td><td>10:19:00</td></tr><tr><td>2.4-13.4B</td><td>Descent Pitch Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>43000</td><td>1.22</td><td>18</td><td>10:19:10</td><td>10:20:10</td></tr><tr><td>2.4-13.5A</td><td>Descent Roll Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.18</td><td>18</td><td>10:21:45</td><td>10:22:45</td></tr><tr><td>2.4-13.5B</td><td>Descent Roll Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.19</td><td>18</td><td>10:22:45</td><td>10:23:45</td></tr><tr><td>2.4-13.6A</td><td>Descent Yaw Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>43000</td><td>1.22</td><td>18</td><td>10:24:10</td><td>10:25:10</td></tr><tr><td>2.4-13.6B</td><td>Descent Yaw Doublet</td><td>47%</td><td>Ret</td><td>Ret</td><td>0°</td><td>42000</td><td>1.21</td><td>18</td><td>10:25:30</td><td>10:26:30</td></tr></table>

TABLE 4:Continued.   

<table><tr><td rowspan="2">TPN</td><td rowspan="2">Test Title</td><td colspan="4">Aircraft Configuration</td><td colspan="2">Flight Conditions</td><td rowspan="2">Flight</td><td rowspan="2">Start Time</td><td rowspan="2">Stop Time</td></tr><tr><td>CG</td><td>LG</td><td>CND</td><td>NOSE</td><td>Alt. feet</td><td>Mach Number</td></tr><tr><td>2.4-15.1A</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>32000</td><td>0.89</td><td>12</td><td>9:38:50</td><td>9:41:00</td></tr><tr><td>2.4-15.1B</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>33000</td><td>0.89</td><td>12</td><td>9:44:50</td><td>9:47:30</td></tr><tr><td>2.4-15.1C</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>31000</td><td>0.83</td><td>16</td><td>10:46:50</td><td>10:48:50</td></tr><tr><td>2.4-15.2A</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>32000</td><td>0.88</td><td>12</td><td>9:50:00</td><td>9:52:00</td></tr><tr><td>2.4-15.2B</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>32000</td><td>0.87</td><td>12</td><td>9:54:50</td><td>9:57:00</td></tr><tr><td>2.4-15.2C</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>29000</td><td>0.89</td><td>16</td><td>10:49:50</td><td>10:51:50</td></tr><tr><td>2.4-15.3A</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>31000</td><td>0.92</td><td>12</td><td>9:58:00</td><td>10:00:00</td></tr><tr><td>2.4-15.3B</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>32000</td><td>0.86</td><td>12</td><td>10:04:00</td><td>10:06:00</td></tr><tr><td>2.4-15.3C</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>30000</td><td>0.88</td><td>16</td><td>10:51:50</td><td>10:53:50</td></tr><tr><td>2.4-15.4A</td><td>Subsonic Cruise Pitch Doublet</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>30000</td><td>0.88</td><td>16</td><td>10:16:45</td><td>10:17:45</td></tr><tr><td>2.4-15.4B</td><td>Subsonic Cruise Pitch Doublet</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>31000</td><td>0.87</td><td>12</td><td>9:04:00</td><td>9:05:10</td></tr><tr><td>2.4-15.5A</td><td>Subsonic Cruise Roll Doublet</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>30000</td><td>0.90</td><td>16</td><td>10:18:40</td><td>10:19:40</td></tr><tr><td>2.4-15.5B</td><td>Subsonic Cruise Roll Doublet</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>31000</td><td>0.88</td><td>12</td><td>9:08:00</td><td>9:10:00</td></tr><tr><td>2.4-15.6A</td><td>Subsonic Cruise Yaw Doublet</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>30000</td><td>0.86</td><td>16</td><td>10:21:15</td><td>10:22:15</td></tr><tr><td>2.4-15.6B</td><td>Subsonic Cruise Yaw Doublet</td><td>46%</td><td>Ret</td><td>Ret</td><td>0°</td><td>31000</td><td>0.87</td><td>12</td><td>9:10:30</td><td>9:11:10</td></tr><tr><td>2.4-16.1A</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7200</td><td>0.36</td><td>12</td><td>10:30:50</td><td>10:33:00</td></tr><tr><td>2.4-16.1B</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7600</td><td>0.36</td><td>12</td><td>10:33:00</td><td>10:35:00</td></tr><tr><td>2.4-16.2A</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7100</td><td>0.36</td><td>12</td><td>10:36:00</td><td>10:38:00</td></tr><tr><td>2.4-16.2B</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7600</td><td>0.37</td><td>12</td><td>10:39:00</td><td>10:41:00</td></tr><tr><td>2.4-16.3A</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7000</td><td>0.36</td><td>12</td><td>10:43:00</td><td>10:45:00</td></tr><tr><td>2.4-16.3B</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7200</td><td>0.35</td><td>12</td><td>10:46:00</td><td>10:48:00</td></tr><tr><td>2.4-16.4A</td><td>Canard Ext. Effect Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7000</td><td>0.35</td><td>12</td><td>10:20:00</td><td>10:21:30</td></tr><tr><td>2.4-16.4B</td><td>Canard Ext. Effect Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7000</td><td>0.35</td><td>12</td><td>10:21:30</td><td>10:22:40</td></tr><tr><td>2.4-16.5A</td><td>Canard Ext. Effect Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6900</td><td>0.36</td><td>12</td><td>10:22:40</td><td>10:23:50</td></tr><tr><td>2.4-16.5B</td><td>Canard Ext. Effect Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6900</td><td>0.35</td><td>12</td><td>10:23:50</td><td>10:25:00</td></tr><tr><td>2.4-16.6A</td><td>Canard Ext. Effect Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6800</td><td>0.35</td><td>12</td><td>10:25:00</td><td>10:26:40</td></tr><tr><td>2.4-16.6B</td><td>Canard Ext. Effect Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6900</td><td>0.35</td><td>12</td><td>10:26:40</td><td>10:28:30</td></tr></table>

TABLE 4:Continued.   

<table><tr><td rowspan="2">TPN</td><td rowspan="2">Test Title</td><td colspan="4">Aircraft Configuration</td><td colspan="2">Flight Conditions</td><td rowspan="2">Flight</td><td rowspan="2">Start Time</td><td rowspan="2">Stop Time</td></tr><tr><td>CG</td><td>LG</td><td>CND</td><td>NOSE</td><td>Alt. feet</td><td>Mach Number</td></tr><tr><td>2.4-17.1A</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6200</td><td>0.33</td><td>14</td><td>10:27:50</td><td>10:29:50</td></tr><tr><td>2.4-17.1B</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6200</td><td>0.34</td><td>14</td><td>10:30:50</td><td>10:32:50</td></tr><tr><td>2.4-17.1C</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6000</td><td>0.33</td><td>15</td><td>11:52:45</td><td>11:54:45</td></tr><tr><td>2.4-17.1D</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5500</td><td>0.33</td><td>15</td><td>11:54:45</td><td>11:56:45</td></tr><tr><td>2.4-17.2A</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6100</td><td>0.34</td><td>14</td><td>10:32:50</td><td>10:34:50</td></tr><tr><td>2.4-17.2B</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6300</td><td>0.34</td><td>14</td><td>10:35:50</td><td>10:37:50</td></tr><tr><td>2.4-17.3A</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6100</td><td>0.34</td><td>14</td><td>10:40:50</td><td>10:42:50</td></tr><tr><td>2.4-17.3B</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6400</td><td>0.34</td><td>14</td><td>10:42:50</td><td>10:44:50</td></tr><tr><td>2.4-17.4A</td><td>Canard Ext. Effect Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6200</td><td>0.33</td><td>14</td><td>10:16:20</td><td>10:17:20</td></tr><tr><td>2.4-17.4B</td><td>Canard Ext. Effect Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6200</td><td>0.32</td><td>14</td><td>10:18:10</td><td>10:19:10</td></tr><tr><td>2.4-17.4C</td><td>Canard Ext. Effect Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>7000</td><td>0.33</td><td>15</td><td>11:49:00</td><td>11:50:00</td></tr><tr><td>2.4-17.4D</td><td>Canard Ext. Effect Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6600</td><td>0.33</td><td>15</td><td>11:50:45</td><td>11:51:45</td></tr><tr><td>2.4-17.5A</td><td>Canard Ext. Effect Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6000</td><td>0.35</td><td>14</td><td>10:19:40</td><td>10:20:40</td></tr><tr><td>2.4-17.5B</td><td>Canard Ext. Effect Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6500</td><td>0.34</td><td>14</td><td>10:21:10</td><td>10:22:10</td></tr><tr><td>2.4-17.6A</td><td>Canard Ext. Effect Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5600</td><td>0.33</td><td>14</td><td>10:25:00</td><td>10:25:30</td></tr><tr><td>2.4-17.6B</td><td>Canard Ext. Effect Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6000</td><td>0.34</td><td>14</td><td>10:26:30</td><td>10:27:00</td></tr><tr><td>2.4-18.1A</td><td>Gear Ret. Approach Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5700</td><td>0.30</td><td>13</td><td>12:30:30</td><td>12:32:30</td></tr><tr><td>2.4-18.1B</td><td>Gear Ret. Approach Pitch Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6300</td><td>0.33</td><td>13</td><td>12:32:30</td><td>12:34:20</td></tr><tr><td>2.4-18.2A</td><td>Gear Ret. Approach Roll Frequency Sweep</td><td>40%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5500</td><td>0.31</td><td>13</td><td>12:36:00</td><td>12:37:40</td></tr><tr><td>2.4-18.2B</td><td>Gear Ret. Approach Roll Frequency Sweep</td><td>40%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5400</td><td>0.31</td><td>13</td><td>12:39:40</td><td>12:41:40</td></tr><tr><td>2.4-18.3A</td><td>Gear Ret. Approach Yaw Frequency Sweep</td><td>40%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5100</td><td>0.31</td><td>13</td><td>12:41:40</td><td>12:43:40</td></tr><tr><td>2.4-18.3B</td><td>Gear Ret. Approach Yaw Frequency Sweep</td><td>40%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5000</td><td>0.31</td><td>13</td><td>12:44:40</td><td>12:46:40</td></tr><tr><td>2.4-18.4A</td><td>Gear Ret. Approach Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5500</td><td>0.32</td><td>13</td><td>12:15:30</td><td>12:16:40</td></tr><tr><td>2.4-18.4B</td><td>Gear Ret. Approach Pitch Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5800</td><td>0.32</td><td>13</td><td>12:17:20</td><td>12:18:50</td></tr><tr><td>2.4-18.5A</td><td>Gear Ret. Approach Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>6000</td><td>0.31</td><td>13</td><td>12:22:10</td><td>12:23:20</td></tr><tr><td>2.4-18.5B</td><td>Gear Ret. Approach Roll Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5800</td><td>0.32</td><td>13</td><td>12:23:40</td><td>12:24:50</td></tr><tr><td>2.4-18.6A</td><td>Gear Ret. Approach Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5900</td><td>0.32</td><td>13</td><td>12:25:50</td><td>12:26:40</td></tr><tr><td>2.4-18.6B</td><td>Gear Ret. Approach Yaw Doublet</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5900</td><td>0.31</td><td>13</td><td>12:27:30</td><td>12:28:40</td></tr></table>

TABLE 4: Concluded.   

<table><tr><td rowspan="2">TPN</td><td rowspan="2">Test Title</td><td colspan="4">Aircraft Configuration</td><td colspan="2">Flight Conditions</td><td rowspan="2">Flight</td><td rowspan="2">Start Time</td><td rowspan="2">Stop Time</td></tr><tr><td>CG</td><td>LG</td><td>CND</td><td>NOSE</td><td>Alt. feet</td><td>Mach Number</td></tr><tr><td>2.4-19.1A</td><td>Approach Pitch Frequency Sweep</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6700</td><td>0.31</td><td>16</td><td>11:28:50</td><td>11:30:50</td></tr><tr><td>2.4-19.1B</td><td>Approach Pitch Frequency Sweep</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6800</td><td>0.32</td><td>16</td><td>11:30:50</td><td>11:32:50</td></tr><tr><td>2.4-19.2A</td><td>Approach Roll Frequency Sweep</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>7000</td><td>0.31</td><td>16</td><td>11:32:50</td><td>11:34:50</td></tr><tr><td>2.4-19.2B</td><td>Approach Roll Frequency Sweep</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>7100</td><td>0.31</td><td>16</td><td>11:34:50</td><td>11:36:50</td></tr><tr><td>2.4-19.3A</td><td>Approach Yaw Frequency Sweep</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6900</td><td>0.31</td><td>16</td><td>11:38:50</td><td>11:40:50</td></tr><tr><td>2.4-19.3B</td><td>Approach Yaw Frequency Sweep</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6800</td><td>0.31</td><td>16</td><td>11:40:50</td><td>11:42:50</td></tr><tr><td>2.4-19.4A</td><td>Approach Pitch Doublet</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6300</td><td>0.31</td><td>16</td><td>11:18:40</td><td>11:19:40</td></tr><tr><td>2.4-19.4B</td><td>Approach Pitch Doublet</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6700</td><td>0.31</td><td>16</td><td>11:20:30</td><td>11:21:30</td></tr><tr><td>2.4-19.5A</td><td>Approach Roll Doublet</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>7000</td><td>0.31</td><td>16</td><td>11:22:20</td><td>11:23:20</td></tr><tr><td>2.4-19.5B</td><td>Approach Roll Doublet</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>6700</td><td>0.31</td><td>16</td><td>11:23:30</td><td>11:24:30</td></tr><tr><td>2.4-19.6A</td><td>Approach Yaw Doublet</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>7100</td><td>0.31</td><td>16</td><td>11:25:10</td><td>11:26:10</td></tr><tr><td>2.4-19.6B</td><td>Approach Yaw Doublet</td><td>41%</td><td>Ext</td><td>Ext</td><td>17°</td><td>7000</td><td>0.31</td><td>16</td><td>11:27:00</td><td>11:28:00</td></tr><tr><td>2.4-21.1A</td><td>Approach Pitch Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5500</td><td>0.31</td><td>13</td><td>11:30:40</td><td>11:32:30</td></tr><tr><td>2.4-21.1B</td><td>Approach Pitch Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5800</td><td>0.32</td><td>13</td><td>11:36:30</td><td>11:38:40</td></tr><tr><td>2.4-21.2A</td><td>Approach Roll Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5900</td><td>0.30</td><td>13</td><td>11:39:40</td><td>11:41:40</td></tr><tr><td>2.4-21.2B</td><td>Approach Roll Frequency Sweep</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5500</td><td>0.31</td><td>13</td><td>11:41:40</td><td>11:43:40</td></tr><tr><td>2.4-21.3A</td><td>Approach Yaw Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5700</td><td>0.31</td><td>13</td><td>11:47:40</td><td>11:49:40</td></tr><tr><td>2.4-21.3B</td><td>Approach Yaw Frequency Sweep</td><td>41%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5300</td><td>0.31</td><td>13</td><td>11:49:40</td><td>11:51:40</td></tr><tr><td>2.4-21.4A</td><td>Approach Pitch Doublet</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5300</td><td>0.31</td><td>13</td><td>11:20:30</td><td>11:21:50</td></tr><tr><td>2.4-21.4B</td><td>Approach Pitch Doublet</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5300</td><td>0.30</td><td>13</td><td>11:21:50</td><td>11:23:00</td></tr><tr><td>2.4-21.5A</td><td>Approach Roll Doublet</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5300</td><td>0.31</td><td>13</td><td>11:23:00</td><td>11:23:50</td></tr><tr><td>2.4-21.5B</td><td>Approach Roll Doublet</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5500</td><td>0.32</td><td>13</td><td>11:25:00</td><td>11:26:00</td></tr><tr><td>2.4-21.6A</td><td>Approach Yaw Doublet</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5600</td><td>0.32</td><td>13</td><td>11:26:40</td><td>11:27:40</td></tr><tr><td>2.4-21.6B</td><td>Approach Yaw Doublet</td><td>42%</td><td>Ret</td><td>Ext</td><td>17°</td><td>5400</td><td>0.32</td><td>13</td><td>11:28:40</td><td>11:30:00</td></tr></table>

TABLE 5: Recommended Short Period Requirements for Class III, (a) Category B and (b) Category C   
(a) Category B   

<table><tr><td>Level</td><td>Min ζsp</td><td>Max ζsp</td><td>τ, sec</td><td>Min ωspTθ2</td></tr><tr><td>1</td><td>0.30</td><td>2.00</td><td>0.10</td><td>1.00</td></tr><tr><td>2</td><td>0.20</td><td>2.00</td><td>0.20</td><td>0.60</td></tr><tr><td>3</td><td>-</td><td>-</td><td>0.25</td><td>-</td></tr></table>

(b) Category C   

<table><tr><td>Level</td><td>Min ζsp</td><td>Max ζsp</td><td>τ, sec</td><td>Min ωspTθ2</td></tr><tr><td>1</td><td>0.35</td><td>1.30</td><td>0.10</td><td>1.40</td></tr><tr><td>2</td><td>0.25</td><td>2.00</td><td>0.20</td><td>0.70</td></tr><tr><td>3</td><td>-</td><td>-</td><td>0.25</td><td>-</td></tr></table>

TABLE 6:Recommended Roll-Mode Time Constant for Class III, Category B and C   

<table><tr><td>Level</td><td>Max TR, sec</td></tr><tr><td>1</td><td>1.4</td></tr><tr><td>2</td><td>3.0</td></tr><tr><td>3</td><td>10.0</td></tr></table>

TABLE 7: Recommended Dutch Roll Frequency and Damping for Class III, (a) Category B and (b) Category C   
(a) Category B   

<table><tr><td>Level</td><td>Min ζd</td><td>Min ζdωd</td><td>Min ωd</td></tr><tr><td>1</td><td>0.08</td><td>0.15</td><td>0.4</td></tr><tr><td>2</td><td>0.02</td><td>0.05</td><td>0.4</td></tr><tr><td>3</td><td>0</td><td>--</td><td>0.4</td></tr></table>

(b) Category C   

<table><tr><td>Level</td><td>Min ζd</td><td>Min ζdωd</td><td>Min ωd</td></tr><tr><td>1</td><td>0.08</td><td>0.10</td><td>0.4</td></tr><tr><td>2</td><td>0.02</td><td>0.05</td><td>0.4</td></tr><tr><td>3</td><td>0</td><td>--</td><td>0.4</td></tr></table>

TABLE 8: Normalized pairwise parameter correlation matrices from simulated data for (a) EEM for one measurement, (b) EEM for two measurements, (c) OEM for one measurement, and (d) OEM for two measurements. Shaded values indicate those defined as having a high correlation.   
(a)   

<table><tr><td></td><td>k1</td><td>k0</td><td>A</td><td>B</td><td>τθ</td></tr><tr><td>k1</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>k0</td><td>0.027</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.673</td><td>-0.658</td><td>1.000</td><td></td><td></td></tr><tr><td>B</td><td>0.030</td><td>0.973</td><td>-0.655</td><td>1.000</td><td></td></tr><tr><td>τθ</td><td>0.768</td><td>-0.439</td><td>0.889</td><td>-0.481</td><td>1.000</td></tr></table>

(b)   

<table><tr><td></td><td>k1</td><td>k0</td><td>A</td><td>B</td><td>τθ</td></tr><tr><td>k1</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>k0</td><td>0.735</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.790</td><td>0.434</td><td>1.000</td><td></td><td></td></tr><tr><td>B</td><td>0.807</td><td>0.844</td><td>0.464</td><td>1.000</td><td></td></tr><tr><td>τθ</td><td>0.875</td><td>0.751</td><td>0.672</td><td>0.751</td><td>1.000</td></tr></table>

(c)   

<table><tr><td></td><td>k1</td><td>k0</td><td>A</td><td>B</td><td>τθ</td></tr><tr><td>k1</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>k0</td><td>-0.085</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.956</td><td>-0.242</td><td>1.000</td><td></td><td></td></tr><tr><td>B</td><td>-0.136</td><td>0.980</td><td>-0.292</td><td>1.000</td><td></td></tr><tr><td>τθ</td><td>0.888</td><td>-0.126</td><td>0.896</td><td>-0.201</td><td>1.000</td></tr></table>

(d)   

<table><tr><td></td><td>k1</td><td>k0</td><td>A</td><td>B</td><td>τθ</td></tr><tr><td>k1</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>k0</td><td>0.968</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.943</td><td>0.907</td><td>1.000</td><td></td><td></td></tr><tr><td>B</td><td>0.971</td><td>0.990</td><td>0.896</td><td>1.000</td><td></td></tr><tr><td>τθ</td><td>0.862</td><td>0.890</td><td>0.822</td><td>0.878</td><td>1.000</td></tr></table>

TABLE 9: Summary of longitudinal parameter estimates.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="5">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kθ</td><td>l/Tθ2</td><td>ζsp</td><td>ωsp</td><td>τθ</td></tr><tr><td>2.4-3.1A</td><td>Takeoff Pitch Frequency Sweep</td><td>0.33</td><td>9.8</td><td>1.390 (0.012)</td><td>0.602 (0.115)</td><td>0.830 (0.084)</td><td>1.021 (0.087)</td><td>0.210 (0.002)</td></tr><tr><td>2.4-3.1B</td><td>Takeoff Pitch Frequency Sweep</td><td>0.31</td><td>11.0</td><td>1.194 (0.013)</td><td>0.467 (0.125)</td><td>0.837 (0.113)</td><td>0.828 (0.093)</td><td>0.210 (0.003)</td></tr><tr><td>2.4-12.1A</td><td>Descent Pitch Frequency Sweep</td><td>1.61</td><td>4.8</td><td>0.614 (0.004)</td><td>0.391 (0.015)</td><td>0.354 (0.007)</td><td>1.500 (0.011)</td><td>0.182 (0.001)</td></tr><tr><td>2.4-12.1B</td><td>Descent Pitch Frequency Sweep</td><td>1.60</td><td>4.8</td><td>0.649 (0.005)</td><td>0.362 (0.015)</td><td>0.348 (0.008)</td><td>1.541 (0.012)</td><td>0.183 (0.002)</td></tr><tr><td>2.4-13.1A</td><td>Descent Pitch Frequency Sweep</td><td>1.25</td><td>6.4</td><td>0.870 (0.010)</td><td>0.378 (0.023)</td><td>0.387 (0.012)</td><td>1.581 (0.019)</td><td>0.192 (0.003)</td></tr><tr><td>2.4-13.1B</td><td>Descent Pitch Frequency Sweep</td><td>1.24</td><td>6.4</td><td>0.872 (0.008)</td><td>0.418 (0.019)</td><td>0.369 (0.009)</td><td>1.574 (0.015)</td><td>0.181 (0.002)</td></tr><tr><td>2.4-15.1A</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>0.89</td><td>6.0</td><td>2.524 (0.048)</td><td>1.538 (0.061)</td><td>0.586 (0.014)</td><td>2.922 (0.039)</td><td>0.261 (0.003)</td></tr><tr><td>2.4-15.1B</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>0.89</td><td>6.2</td><td>1.972 (0.031)</td><td>1.137 (0.057)</td><td>0.607 (0.017)</td><td>2.261 (0.042)</td><td>0.217 (0.003)</td></tr><tr><td>2.4-15.1C</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>0.83</td><td>6.1</td><td>1.833 (0.033)</td><td>1.297 (0.089)</td><td>0.678 (0.025)</td><td>2.071 (0.061)</td><td>0.214 (0.003)</td></tr><tr><td>2.4-16.1A</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.36</td><td>9.5</td><td>0.995 (0.009)</td><td>0.633 (0.071)</td><td>0.796 (0.047)</td><td>1.139 (0.056)</td><td>0.200 (0.002)</td></tr><tr><td>2.4-16.1B</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.36</td><td>9.5</td><td>1.034 (0.006)</td><td>0.791 (0.072)</td><td>0.774 (0.039)</td><td>1.275 (0.052)</td><td>0.200 (0.001)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 9: Concluded.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="5">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kθ</td><td>l/Tθ2</td><td>ζsp</td><td>ωsp</td><td>τθ</td></tr><tr><td>2.4-17.1A</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.33</td><td>8.5</td><td>1.416 (0.011)</td><td>0.605 (0.092)</td><td>0.803 (0.064)</td><td>1.101 (0.074)</td><td>0.210 (0.002)</td></tr><tr><td>2.4-17.1B</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.34</td><td>8.3</td><td>1.366 (0.019)</td><td>0.803 (0.116)</td><td>0.682 (0.057)</td><td>1.248 (0.080)</td><td>0.196 (0.003)</td></tr><tr><td>2.4-17.1C</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.33</td><td>8.6</td><td>1.290 (0.013)</td><td>0.960 (0.105)</td><td>0.755 (0.047)</td><td>1.367 (0.067)</td><td>0.201 (0.002)</td></tr><tr><td>2.4-17.1D</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.33</td><td>8.3</td><td>1.460 (0.012)</td><td>0.757 (0.089)</td><td>0.790 (0.050)</td><td>1.295 (0.068)</td><td>0.201 (0.002)</td></tr><tr><td>2.4-18.1A</td><td>Gear Ret. Approach Pitch Frequency Sweep</td><td>0.30</td><td>9.1</td><td>1.042 (0.017)</td><td>1.030 (0.141)</td><td>0.628 (0.052)</td><td>1.325 (0.077)</td><td>0.202 (0.004)</td></tr><tr><td>2.4-18.1B</td><td>Gear Ret. Approach Pitch Frequency Sweep</td><td>0.33</td><td>8.2</td><td>1.301 (0.020)</td><td>1.020 (0.129)</td><td>0.669 (0.048)</td><td>1.472 (0.080)</td><td>0.201 (0.004)</td></tr><tr><td>2.4-19.1A</td><td>Approach Pitch Frequency Sweep</td><td>0.31</td><td>9.7</td><td>0.904 (0.010)</td><td>0.890 (0.138)</td><td>0.709 (0.066)</td><td>1.133 (0.078)</td><td>0.194 (0.003)</td></tr><tr><td>2.4-19.1B</td><td>Approach Pitch Frequency Sweep</td><td>0.32</td><td>9.4</td><td>1.062 (0.012)</td><td>0.849 (0.127)</td><td>0.768 (0.065)</td><td>1.196 (0.078)</td><td>0.193 (0.003)</td></tr><tr><td>2.4-21.1A</td><td>Approach Pitch Frequency Sweep</td><td>0.31</td><td>10.2</td><td>1.160 (0.019)</td><td>0.303 (0.130)</td><td>0.842 (0.172)</td><td>0.683 (0.121)</td><td>0.196 (0.004)</td></tr><tr><td>2.4-21.1B</td><td>Approach Pitch Frequency Sweep</td><td>0.32</td><td>9.4</td><td>1.101 (0.017)</td><td>0.656 (0.158)</td><td>0.622 (0.087)</td><td>1.001 (0.099)</td><td>0.179 (0.004)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 10: Summary of longitudinal handling qualities predictions.   

<table><tr><td>TPN</td><td>Test Title</td><td>ζsp</td><td>τθ</td><td>ωspTθ2</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>2.4-3.1A</td><td>Takeoff Pitch Frequency Sweep</td><td>0.830</td><td>0.210</td><td>1.696</td><td>C</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-3.1B</td><td>Takeoff Pitch Frequency Sweep</td><td>0.837</td><td>0.210</td><td>1.773</td><td>C</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-12.1A</td><td>Descent Pitch Frequency Sweep</td><td>0.354</td><td>0.182</td><td>3.836</td><td>B</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-12.1B</td><td>Descent Pitch Frequency Sweep</td><td>0.348</td><td>0.183</td><td>4.257</td><td>B</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-13.1A</td><td>Descent Pitch Frequency Sweep</td><td>0.387</td><td>0.192</td><td>4.183</td><td>B</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-13.1B</td><td>Descent Pitch Frequency Sweep</td><td>0.369</td><td>0.181</td><td>3.766</td><td>B</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-15.1A</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>0.586</td><td>0.261</td><td>1.900</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-15.1B</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>0.607</td><td>0.217</td><td>1.989</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-15.1C</td><td>Subsonic Cruise Pitch Frequency Sweep</td><td>0.678</td><td>0.214</td><td>1.597</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-16.1A</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.796</td><td>0.200</td><td>1.799</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-16.1B</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.774</td><td>0.200</td><td>1.612</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 10: Concluded.   

<table><tr><td>TPN</td><td>Test Title</td><td>ζsp</td><td>τθ</td><td>ωspTθ2</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>2.4-17.1A</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.803</td><td>0.210</td><td>1.820</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-17.1B</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.682</td><td>0.196</td><td>1.554</td><td>B</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-17.1C</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.755</td><td>0.201</td><td>1.424</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-17.1D</td><td>Canard Ext. Effect Pitch Frequency Sweep</td><td>0.790</td><td>0.201</td><td>1.711</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-18.1A</td><td>Gear Ret. Approach Pitch Frequency Sweep</td><td>0.628</td><td>0.202</td><td>1.286</td><td>C</td><td>3</td><td>τθ&gt;0.20 ωspTθ2&lt;1.4</td></tr><tr><td>2.4-18.1B</td><td>Gear Ret. Approach Pitch Frequency Sweep</td><td>0.669</td><td>0.201</td><td>1.443</td><td>C</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>2.4-19.1A</td><td>Approach Pitch Frequency Sweep</td><td>0.709</td><td>0.194</td><td>1.273</td><td>C</td><td>2</td><td>τθ&gt;0.10 ωspTθ2&lt;1.4</td></tr><tr><td>2.4-19.1B</td><td>Approach Pitch Frequency Sweep</td><td>0.768</td><td>0.193</td><td>1.409</td><td>C</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-21.1A</td><td>Approach Pitch Frequency Sweep</td><td>0.842</td><td>0.196</td><td>2.254</td><td>C</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>2.4-21.1B</td><td>Approach Pitch Frequency Sweep</td><td>0.622</td><td>0.179</td><td>1.526</td><td>C</td><td>2</td><td>τθ&gt;0.10</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 11: Average parameter estimates for different flight conditions. Pitch rate to longitudinal stick transfer function coefficients.   

<table><tr><td>Flight Condition</td><td>Kθ</td><td>l/Tθ2</td><td>ζsp</td><td>ωsp</td><td>τθ</td></tr><tr><td>0.3 &lt; M &lt; 0.4</td><td rowspan="2">1.2</td><td rowspan="2">0.74</td><td rowspan="2">0.76</td><td rowspan="2">1.15</td><td rowspan="2">0.20</td></tr><tr><td>8.2 &lt; α &lt; 11.0</td></tr><tr><td>0.8 &lt; M &lt; 0.9</td><td rowspan="2">1.9</td><td rowspan="2">1.2</td><td rowspan="2">0.64</td><td rowspan="2">2.2</td><td rowspan="2">0.22</td></tr><tr><td>6.0 &lt; α &lt; 6.2</td></tr><tr><td>1.2 &lt; M &lt; 1.6</td><td rowspan="2">0.75</td><td rowspan="2">0.39</td><td rowspan="2">0.36</td><td rowspan="2">1.55</td><td rowspan="2">0.19</td></tr><tr><td>4.8 &lt; α &lt; 6.4</td></tr></table>

TABLE 12: Summary of Dutch roll parameter estimates.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="5">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kr</td><td>1/Tr</td><td>ζd</td><td>ωd</td><td>τr</td></tr><tr><td>2.4-3.3A</td><td>Takeoff Yaw Frequency Sweep</td><td>0.33</td><td>9.7</td><td>0.238 (0.010)</td><td>1.035 (0.167)</td><td>0.183 (0.038)</td><td>0.902 (0.039)</td><td>0.120 (0.009)</td></tr><tr><td>2.4-3.3B</td><td>Takeoff Yaw Frequency Sweep</td><td>0.32</td><td>10.1</td><td>0.292 (0.007)</td><td>0.476 (0.102)</td><td>0.286 (0.048)</td><td>0.803 (0.046)</td><td>0.145 (0.006)</td></tr><tr><td>2.4-12.3A</td><td>Descent Yaw Frequency Sweep</td><td>1.61</td><td>4.3</td><td>0.550 (0.008)</td><td>0.275 (0.024)</td><td>0.191 (0.012)</td><td>1.453 (0.017)</td><td>0.115 (0.004)</td></tr><tr><td>2.4-12.3B</td><td>Descent Yaw Frequency Sweep</td><td>1.62</td><td>4.3</td><td>0.510 (0.007)</td><td>0.257 (0.024)</td><td>0.179 (0.010)</td><td>1.391 (0.014)</td><td>0.111 (0.004)</td></tr><tr><td>2.4-13.3A</td><td>Descent Yaw Frequency Sweep</td><td>1.19</td><td>6.5</td><td>0.606 (0.008)</td><td>0.392 (0.025)</td><td>0.286 (0.012)</td><td>1.455 (0.018)</td><td>0.158 (0.003)</td></tr><tr><td>2.4-13.3B</td><td>Descent Yaw Frequency Sweep</td><td>1.20</td><td>6.3</td><td>0.569 (0.011)</td><td>0.456 (0.033)</td><td>0.269 (0.015)</td><td>1.512 (0.023)</td><td>0.183 (0.005)</td></tr><tr><td>2.4-15.3A</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>0.92</td><td>5.4</td><td>1.558 (0.016)</td><td>0.238 (0.027)</td><td>0.725 (0.024)</td><td>1.216 (0.029)</td><td>0.158 (0.003)</td></tr><tr><td>2.4-15.3B</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>0.86</td><td>6.2</td><td>1.018 (0.008)</td><td>0.246 (0.020)</td><td>0.433 (0.014)</td><td>0.997 (0.016)</td><td>0.130 (0.002)</td></tr><tr><td>2.4-15.3C</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>0.88</td><td>5.4</td><td>1.216 (0.011)</td><td>0.210 (0.019)</td><td>0.565 (0.017)</td><td>1.050 (0.018)</td><td>0.124 (0.003)</td></tr><tr><td>2.4-16.3A</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.36</td><td>9.1</td><td>0.467 (0.007)</td><td>0.486 (0.088)</td><td>0.505 (0.052)</td><td>0.804 (0.051)</td><td>0.170 (0.004)</td></tr><tr><td>2.4-16.3B</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.35</td><td>9.6</td><td>0.439 (0.006)</td><td>0.518 (0.098)</td><td>0.505 (0.059)</td><td>0.789 (0.054)</td><td>0.161 (0.004)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 12: Concluded.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="5">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kr</td><td>l/Tr</td><td>ζd</td><td>ωd</td><td>τr</td></tr><tr><td>2.4-17.3A</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.34</td><td>8.2</td><td>0.433 (0.009)</td><td>0.361 (0.071)</td><td>0.299 (0.036)</td><td>0.879 (0.040)</td><td>0.162 (0.005)</td></tr><tr><td>2.4-17.3B</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.34</td><td>8.2</td><td>0.435 (0.008)</td><td>0.283 (0.054)</td><td>0.319 (0.033)</td><td>0.821 (0.034)</td><td>0.154 (0.005)</td></tr><tr><td>2.4-18.3A</td><td>Gear Ret. Approach Yaw Frequency Sweep</td><td>0.31</td><td>8.4</td><td>0.432 (0.006)</td><td>0.291 (0.059)</td><td>0.282 (0.030)</td><td>0.848 (0.031)</td><td>0.144 (0.003)</td></tr><tr><td>2.4-18.3B</td><td>Gear Ret. Approach Yaw Frequency Sweep</td><td>0.31</td><td>8.4</td><td>0.350 (0.006)</td><td>0.414 (0.081)</td><td>0.240 (0.034)</td><td>0.880 (0.037)</td><td>0.166 (0.004)</td></tr><tr><td>2.4-19.3A</td><td>Approach Yaw Frequency Sweep</td><td>0.31</td><td>9.7</td><td>0.306 (0.007)</td><td>0.354 (0.072)</td><td>0.323 (0.040)</td><td>0.737 (0.037)</td><td>0.148 (0.005)</td></tr><tr><td>2.4-19.3B</td><td>Approach Yaw Frequency Sweep</td><td>0.31</td><td>9.6</td><td>0.282 (0.005)</td><td>0.565 (0.087)</td><td>0.302 (0.037)</td><td>0.836 (0.037)</td><td>0.150 (0.004)</td></tr><tr><td>2.4-21.3A</td><td>Approach Yaw Frequency Sweep</td><td>0.31</td><td>9.3</td><td>0.282 (0.010)</td><td>0.828 (0.122)</td><td>0.165 (0.036)</td><td>0.927 (0.038)</td><td>0.120 (0.009)</td></tr><tr><td>2.4-21.3B</td><td>Approach Yaw Frequency Sweep</td><td>0.31</td><td>9.5</td><td>0.357 (0.006)</td><td>0.324 (0.078)</td><td>0.273 (0.047)</td><td>0.755 (0.044)</td><td>0.127 (0.004)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 13: Average parameter estimates for different flight conditions. Yaw rate to rudder pedal input transfer function coefficients.   

<table><tr><td>Flight Condition</td><td>Kr</td><td>1/Tr</td><td>ζd</td><td>ωd</td><td>τr</td></tr><tr><td>0.3 &lt; M &lt; 0.4</td><td rowspan="2">0.36</td><td rowspan="2">0.47</td><td rowspan="2">0.31</td><td rowspan="2">0.83</td><td rowspan="2">0.15</td></tr><tr><td>8.2 &lt; α &lt; 11.0</td></tr><tr><td>0.8 &lt; M &lt; 0.9</td><td rowspan="2">1.1</td><td rowspan="2">0.23</td><td rowspan="2">0.50</td><td rowspan="2">1.0</td><td rowspan="2">0.13</td></tr><tr><td>6.0 &lt; α &lt; 6.2</td></tr><tr><td>1.2 &lt; M &lt; 1.6</td><td rowspan="2">0.56</td><td rowspan="2">0.35</td><td rowspan="2">0.23</td><td rowspan="2">1.5</td><td rowspan="2">0.15</td></tr><tr><td>4.8 &lt; α &lt; 6.4</td></tr></table>

TABLE 14: Summary of roll-mode time constant estimates. First-order model.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="3">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kp</td><td>1/TR</td><td>τp</td></tr><tr><td>2.4-3.2A</td><td>Takeoff Roll Frequency Sweep</td><td>0.34</td><td>9.4</td><td>7.043 (0.443)</td><td>2.101 (0.159)</td><td>0.090 (0.019)</td></tr><tr><td>2.4-3.2B</td><td>Takeoff Roll Frequency Sweep</td><td>0.33</td><td>9.9</td><td>7.893 (0.425)</td><td>2.391 (0.161)</td><td>0.103 (0.015)</td></tr><tr><td>2.4-12.2A</td><td>Descent Roll Frequency Sweep</td><td>1.57</td><td>4.8</td><td>8.412 (0.275)</td><td>2.746 (0.102)</td><td>0.154 (0.007)</td></tr><tr><td>2.4-12.2B</td><td>Descent Roll Frequency Sweep</td><td>1.59</td><td>4.4</td><td>7.546 (0.337)</td><td>2.392 (0.127)</td><td>0.137 (0.011)</td></tr><tr><td>2.4-13.2A</td><td>Descent Roll Frequency Sweep</td><td>1.22</td><td>6.5</td><td>5.455 (0.075)</td><td>1.487 (0.025)</td><td>0.135 (0.004)</td></tr><tr><td>2.4-13.2B</td><td>Descent Roll Frequency Sweep</td><td>1.21</td><td>6.4</td><td>5.312 (0.088)</td><td>1.456 (0.029)</td><td>0.130 (0.005)</td></tr><tr><td>2.4-15.2A</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>0.88</td><td>6.1</td><td>17.598 (0.982)</td><td>3.392 (0.259)</td><td>0.132 (0.012)</td></tr><tr><td>2.4-15.2B</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>0.87</td><td>6.3</td><td>16.219 (0.964)</td><td>3.063 (0.259)</td><td>0.100 (0.014)</td></tr><tr><td>2.4-15.2C</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>0.89</td><td>5.2</td><td>15.862 (1.607)</td><td>3.054 (0.049)</td><td>0.048 (0.028)</td></tr><tr><td>2.4-16.2A</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.36</td><td>9.2</td><td>9.711 (0.570)</td><td>2.905 (0.229)</td><td>0.108 (0.014)</td></tr><tr><td>2.4-16.2B</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.37</td><td>9.1</td><td>10.308 (0.592)</td><td>3.034 (0.225)</td><td>0.112 (0.013)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 14: Concluded.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="3">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kp</td><td>l/TR</td><td>τp</td></tr><tr><td>2.4-17.2A</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.34</td><td>8.2</td><td>10.077 (0.636)</td><td>2.801 (0.211)</td><td>0.101 (0.015)</td></tr><tr><td>2.4-17.2B</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.34</td><td>8.4</td><td>9.201 (0.562)</td><td>2.462 (0.195)</td><td>0.075 (0.017)</td></tr><tr><td>2.4-18.2A</td><td>Gear Ret. Approach Roll Frequency Sweep</td><td>0.31</td><td>8.6</td><td>9.857 (0.491)</td><td>2.752 (0.173)</td><td>0.110 (0.012)</td></tr><tr><td>2.4-18.2B</td><td>Gear Ret. Approach Roll Frequency Sweep</td><td>0.31</td><td>9.0</td><td>8.614 (0.440)</td><td>2.457 (0.159)</td><td>0.087 (0.013)</td></tr><tr><td>2.4-19.2A</td><td>Approach Roll Frequency Sweep</td><td>0.31</td><td>9.6</td><td>8.714 (0.366)</td><td>2.875 (0.137)</td><td>0.158 (0.009)</td></tr><tr><td>2.4-19.2B</td><td>Approach Roll Frequency Sweep</td><td>0.31</td><td>9.7</td><td>8.083 (0.423)</td><td>2.677 (0.158)</td><td>0.083 (0.014)</td></tr><tr><td>2.4-21.2A</td><td>Approach Roll Frequency Sweep</td><td>0.30</td><td>10.4</td><td>4.875 (0.342)</td><td>1.092 (0.120)</td><td>0.050 (0.025)</td></tr><tr><td>2.4-21.2B</td><td>Approach Roll Frequency Sweep</td><td>0.31</td><td>9.5</td><td>6.638 (0.405)</td><td>1.771 (0.154)</td><td>0.067 (0.019)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 15: Average parameter estimates for different flight conditions. Roll rate to lateral stick input transfer function coefficients. First-order model.   

<table><tr><td>Flight Condition</td><td>Kp</td><td>1/TR</td><td>τp</td></tr><tr><td>0.3 &lt; M &lt; 0.4</td><td></td><td></td><td></td></tr><tr><td>8.2 &lt; α &lt; 11.0</td><td>8.4</td><td>2.4</td><td>0.10</td></tr><tr><td>0.8 &lt; M &lt; 0.9</td><td></td><td></td><td></td></tr><tr><td>6.0 &lt; α &lt; 6.2</td><td>16.6</td><td>3.2</td><td>0.09</td></tr><tr><td>1.2 &lt; M &lt; 1.6</td><td></td><td></td><td></td></tr><tr><td>4.8 &lt; α &lt; 6.4</td><td>6.7</td><td>2.0</td><td>0.14</td></tr></table>

TABLE 16: Summary of roll-mode time constant estimates. Third-order hybrid model.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="5">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kφ</td><td>ζφ</td><td>ωφ</td><td>l/TR</td><td>τp</td></tr><tr><td>2.4-3.2A</td><td>Takeoff Roll Frequency Sweep</td><td>0.34</td><td>9.4</td><td>8.392 (0.431)</td><td>0.109 (0.015)</td><td>0.815 (0.055)</td><td>1.975 (0.152)</td><td>0.098 (0.015)</td></tr><tr><td>2.4-3.2B</td><td>Takeoff Roll Frequency Sweep</td><td>0.33</td><td>9.9</td><td>10.621 (0.393)</td><td>0.149 (0.014)</td><td>0.721 (0.031)</td><td>2.421 (0.142)</td><td>0.122 (0.009)</td></tr><tr><td>2.4-12.2A</td><td>Descent Roll Frequency Sweep</td><td>1.57</td><td>4.8</td><td>10.337 (0.224)</td><td>0.091 (0.007)</td><td>1.334 (0.063)</td><td>2.822 (0.086)</td><td>0.175 (0.004)</td></tr><tr><td>2.4-12.2B</td><td>Descent Roll Frequency Sweep</td><td>1.59</td><td>4.4</td><td>11.886 (0.252)</td><td>0.054 (0.006)</td><td>1.201 (0.049)</td><td>2.874 (0.087)</td><td>0.179 (0.004)</td></tr><tr><td>2.4-13.2A</td><td>Descent Roll Frequency Sweep</td><td>1.22</td><td>6.5</td><td>6.267 (0.100)</td><td>0.265 (0.013)</td><td>1.652 (0.073)</td><td>2.355 (0.055)</td><td>0.162 (0.003)</td></tr><tr><td>2.4-13.2B</td><td>Descent Roll Frequency Sweep</td><td>1.21</td><td>6.4</td><td>6.134 (0.119)</td><td>0.249 (0.015)</td><td>1.705 (0.094)</td><td>2.247 (0.063)</td><td>0.153 (0.004)</td></tr><tr><td>2.4-15.2A</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>0.88</td><td>6.1</td><td>23.999 (0.693)</td><td>0.355 (0.039)</td><td>0.898 (0.054)</td><td>2.662 (0.186)</td><td>0.170 (0.006)</td></tr><tr><td>2.4-15.2B</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>0.87</td><td>6.3</td><td>22.630 (0.814)</td><td>0.235 (0.026)</td><td>0.795 (0.041)</td><td>3.094 (0.206)</td><td>0.133 (0.008)</td></tr><tr><td>2.4-15.2C</td><td>Subsonic Cruise Roll Frequency Sweep</td><td>0.89</td><td>5.2</td><td>24.690 (1.452)</td><td>0.300 (0.051)</td><td>0.807 (0.076)</td><td>2.708 (0.355)</td><td>0.076 (0.015)</td></tr><tr><td>2.4-16.2A</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.36</td><td>9.2</td><td>15.515 (0.483)</td><td>0.402 (0.031)</td><td>0.611 (0.021)</td><td>3.324 (0.188)</td><td>0.145 (0.006)</td></tr><tr><td>2.4-16.2B</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.37</td><td>9.1</td><td>16.690 (0.558)</td><td>0.405 (0.030)</td><td>0.627 (0.021)</td><td>3.929 (0.200)</td><td>0.163 (0.006)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 16: Concluded.   

<table><tr><td></td><td></td><td colspan="2">Flight Conditions</td><td colspan="5">Parameter Values and Standard Errors*</td></tr><tr><td>TPN</td><td>Test Title</td><td>Mach</td><td>α, deg</td><td>Kφ</td><td>ζφ</td><td>ωφ</td><td>I/TR</td><td>τp</td></tr><tr><td>2.4-17.2A</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.34</td><td>8.2</td><td>13.456 (0.627)</td><td>0.163 (0.019)</td><td>0.782 (0.047)</td><td>2.791 (0.203)</td><td>0.115 (0.010)</td></tr><tr><td>2.4-17.2B</td><td>Canard Ext. Effect Roll Frequency Sweep</td><td>0.34</td><td>8.4</td><td>11.087 (0.527)</td><td>0.173 (0.023)</td><td>0.725 (0.044)</td><td>2.118 (0.192)</td><td>0.079 (0.013)</td></tr><tr><td>2.4-18.2A</td><td>Gear Ret. Approach Roll Frequency Sweep</td><td>0.31</td><td>8.6</td><td>11.736 (0.436)</td><td>0.150 (0.017)</td><td>0.752 (0.036)</td><td>2.479 (0.157)</td><td>0.116 (0.009)</td></tr><tr><td>2.4-18.2B</td><td>Gear Ret. Approach Roll Frequency Sweep</td><td>0.31</td><td>9.0</td><td>12.043 (0.405)</td><td>0.099 (0.011)</td><td>0.783 (0.033)</td><td>2.692 (0.139)</td><td>0.113 (0.008)</td></tr><tr><td>2.4-19.2A</td><td>Approach Roll Frequency Sweep</td><td>0.31</td><td>9.6</td><td>10.258 (0.330)</td><td>0.216 (0.015)</td><td>0.690 (0.024)</td><td>2.751 (0.124)</td><td>0.169 (0.006)</td></tr><tr><td>2.4-19.2B</td><td>Approach Roll Frequency Sweep</td><td>0.31</td><td>9.7</td><td>11.366 (0.406)</td><td>0.203 (0.015)</td><td>0.769 (0.033)</td><td>3.003 (0.140)</td><td>0.123 (0.008)</td></tr><tr><td>2.4-21.2A</td><td>Approach Roll Frequency Sweep</td><td>0.30</td><td>10.4</td><td>8.241 (0.348)</td><td>0.029 (0.018)</td><td>0.714 (0.038)</td><td>1.197 (0.101)</td><td>0.071 (0.012)</td></tr><tr><td>2.4-21.2B</td><td>Approach Roll Frequency Sweep</td><td>0.31</td><td>9.5</td><td>8.968 (0.389)</td><td>0.116 (0.018)</td><td>0.648 (0.013)</td><td>1.567 (0.141)</td><td>0.074 (0.013)</td></tr></table>

* Parentheses Denote Standard Errors

TABLE 17: Average parameter estimates for different flight conditions. Roll rate to lateral stick input transfer function coefficients. Third-order hybrid model.   

<table><tr><td>Flight Condition</td><td>Kφ</td><td>ζφ</td><td>ωφ</td><td>1/TR</td><td>τp</td></tr><tr><td>0.3 &lt; M &lt; 0.4</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8.2 &lt; α &lt; 11.0</td><td>11.6</td><td>0.18</td><td>0.72</td><td>2.5</td><td>0.12</td></tr><tr><td>0.8 &lt; M &lt; 0.9</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6.0 &lt; α &lt; 6.2</td><td>23.8</td><td>0.30</td><td>0.83</td><td>2.8</td><td>0.13</td></tr><tr><td>1.2 &lt; M &lt; 1.6</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.8 &lt; α &lt; 6.4</td><td>8.7</td><td>0.16·</td><td>1.5</td><td>2.6</td><td>0.17</td></tr></table>

TABLE 18: Summary of lateral handling qualities predictions. Roll-mode time constant from first-order model shown.   

<table><tr><td>TPN</td><td>Test Title</td><td>\( \zeta_{\mathrm {d}} \)</td><td>\( \omega_{\mathrm {d}} \)</td><td>\( \zeta_{\mathrm {d}}\omega_{\mathrm {d}} \)</td><td>\( 1/ \mathrm {T}_{\mathrm {R}} \)</td><td>\( T_{\mathrm {R}} \)</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>2.4-3.2/3A</td><td>Takeoff Yaw Frequency Sweep</td><td>0.183</td><td>0.902</td><td>0.165</td><td>2.101</td><td>0.476</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-3.2/3B</td><td>Takeoff Yaw Frequency Sweep</td><td>0.286</td><td>0.803</td><td>0.230</td><td>2.391</td><td>0.418</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-12.2/3A</td><td>Descent Yaw Frequency Sweep</td><td>0.191</td><td>1.453</td><td>0.278</td><td>2.746</td><td>0.364</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-12.2/3B</td><td>Descent Yaw Frequency Sweep</td><td>0.179</td><td>1.391</td><td>0.249</td><td>2.392</td><td>0.418</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-13.2/3A</td><td>Descent Yaw Frequency Sweep</td><td>0.286</td><td>1.455</td><td>0.416</td><td>1.487</td><td>0.672</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-13.2/3B</td><td>Descent Yaw Frequency Sweep</td><td>0.269</td><td>1.512</td><td>0.407</td><td>1.456</td><td>0.687</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-15.2/3A</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>0.725</td><td>1.216</td><td>0.882</td><td>3.392</td><td>0.295</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-15.2/3B</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>0.433</td><td>0.997</td><td>0.432</td><td>3.063</td><td>0.326</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-15.2/3C</td><td>Subsonic Cruise Yaw Frequency Sweep</td><td>0.565</td><td>1.050</td><td>0.593</td><td>3.054</td><td>0.327</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-16.2/3A</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.505</td><td>0.804</td><td>0.406</td><td>2.905</td><td>0.344</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-16.2/3B</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.505</td><td>0.789</td><td>0.398</td><td>3.034</td><td>0.330</td><td>B</td><td>1</td><td>None</td></tr></table>

* Parentheses Denote Standard Errors   
Note that "2/3" in TPN indicates the use of both a yaw and a roll frequency sweep.

TABLE 18: Concluded.   

<table><tr><td>TPN</td><td>Test Title</td><td>\( \zeta_d \)</td><td>\( \omega_d \)</td><td>\( \zeta_d\omega_d \)</td><td>\( 1/TR \)</td><td>\( T_R \)</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>2.4-17.2/3A</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.299</td><td>0.879</td><td>0.263</td><td>2.801</td><td>0.357</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-17.2/3B</td><td>Canard Ext. Effect Yaw Frequency Sweep</td><td>0.319</td><td>0.821</td><td>0.262</td><td>2.462</td><td>0.406</td><td>B</td><td>1</td><td>None</td></tr><tr><td>2.4-18.2/3A</td><td>Gear Ret. Approach Yaw Frequency Sweep</td><td>0.282</td><td>0.848</td><td>0.239</td><td>2.752</td><td>0.363</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-18.2/3B</td><td>Gear Ret. Approach Yaw Frequency Sweep</td><td>0.240</td><td>0.880</td><td>0.211</td><td>2.457</td><td>0.407</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-19.2/3A</td><td>Approach Yaw Frequency Sweep</td><td>0.323</td><td>0.737</td><td>0.238</td><td>2.875</td><td>0.348</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-19.2/3B</td><td>Approach Yaw Frequency Sweep</td><td>0.302</td><td>0.836</td><td>0.252</td><td>2.677</td><td>0.374</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-21.2/3A</td><td>Approach Yaw Frequency Sweep</td><td>0.165</td><td>0.927</td><td>0.153</td><td>1.092</td><td>0.916</td><td>C</td><td>1</td><td>None</td></tr><tr><td>2.4-21.2/3B</td><td>Approach Yaw Frequency Sweep</td><td>0.273</td><td>0.755</td><td>0.206</td><td>1.771</td><td>0.565</td><td>C</td><td>1</td><td>None</td></tr></table>

* Parentheses Denote Standard Errors   
Note that "2/3" in TPN indicates the use of both a yaw and a roll frequency sweep.

图片摘要：该图主要展示 18: Concluded。
![](images/1c3582010412cf06d22a773171d1ed66e5bd9d185421bcf93b7dd335dd228a96.jpg)  
FIGURE 1: Three-view drawing of the Tu-144 aircraft.

图片摘要：该图主要展示 1: Three view drawing of the Tu 144 aircraft。
![](images/5b225871e27714ab2238814b73248ff3374cbdf8f5d22626cfc987b8e1622d2e.jpg)  
(a)

图片摘要：该图主要展示 1: Three view drawing of the Tu 144 aircraft。
![](images/ac6465c628e32f55db5c28b740c96d6bb1ba8b8339093c13a47e6b9bb6aef6b8.jpg)  
(b)   
FIGURE 2: Data compatibility results comparing measured and calculated (a) angle of attack, and (b) sideslip angle.

图片摘要：该图主要展示 2: Data compatibility results comparing measured and calcula。
![](images/9ec1428b3b2a15d19fc4b51d99ba65b194ebb21a7d317776d38bd9265d495d94.jpg)  
FIGURE 3: Time skew in response of aircraft to control surface deflection. Longitudinal doublet, test point number 2.4-15.4A.

图片摘要：该图主要展示 3: Time skew in response of aircraft to control surface defl。
![](images/5b3b282e72525af80f1472074552f19c7856bd6a0c819e89ae63454ef0b65f95.jpg)  
(a)

图片摘要：该图主要展示 3: Time skew in response of aircraft to control surface defl。
![](images/dc50722f5039549e2bc86fd8d3eb3600d50daa3d8e3bc0dd3c43a6ad6e8a2d73.jpg)  
(b)   
FIGURE 4: (a) Simulated and model time histories for pitch rate for EEM, and (b) residuals from output fit.

图片摘要：该图主要展示 4: (a) Simulated and model time histories for pitch rate for。
![](images/e48dac9c7a0ec4110591022ecac854eed9715a6f485d0c4cabb4d80f81672d3a.jpg)

图片摘要：该图主要展示 4: (a) Simulated and model time histories for pitch rate for。
![](images/c695855f5e9c69e7b2c6a0944f547a6001df9494db989c2dbeb6fe87122b015b.jpg)  
FIGURE 5: Summary of parameter estimates with $2\sigma$ error bars for pitch rate to longitudinal stick transfer function.

图片摘要：该图主要展示 5: Summary of parameter estimates with error bars for pitch 。
![](images/e61c2145d55e217567ca38730ae4216f8456b9165cb64b5ec40de15b96c4e764.jpg)

图片摘要：该图主要展示 5: Summary of parameter estimates with error bars for pitch 。
![](images/99849306a425259421cf1721b94de5c739305f3c9d7dbd209490901755db5531.jpg)  
FIGURE 5: Continued.

图片摘要：该图主要展示 5: Continued。
![](images/38fca2cd6162b47fa5f7f0d1cf089a9bf509b6e35684c4b4bc6a4db1432ffbda.jpg)  
FIGURE 5: Concluded.

图片摘要：该图主要展示 5: Concluded。
![](images/e80f95e7bd71a69a6b294a936587e698fee5f069af4a078d8610e57b67e24dd6.jpg)  
(a)

图片摘要：该图主要展示 5: Concluded。
![](images/12ee92ca31065d0b68fef60873c3eaaab923e2e3ecc8a53f784c79501d6a4c8a.jpg)  
(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kθ</td><td>1/Tθ2</td><td>ζsp</td><td>ωsp</td><td>τθ</td><td>ωspTθ2</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>0.995</td><td>0.633</td><td>0.796</td><td>1.139</td><td>0.200</td><td>1.799</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>(0.009)</td><td>(0.071)</td><td>(0.047)</td><td>(0.056)</td><td>(0.002)</td><td></td><td></td><td></td><td></td></tr></table>

FIGURE 6: Comparison of measured, estimated, and predicted time histories of pitch rate.

Test point number (a) 2.4-16.1A for estimation, and (b) 2.4-16.4A for prediction.

图片摘要：该图主要展示 6: Comparison of measured, estimated, and predicted time his。
![](images/792817da2a9a511664f336f09dfa6cc9ad64d9aac37b013a0db886f8cc4f2bf7.jpg)  
(a)

图片摘要：该图主要展示 6: Comparison of measured, estimated, and predicted time his。
![](images/8a8cb19bd9664a8bde186548c413c71690dd81ad3d87853b558d63de379ae226.jpg)  
FIGURE 7: Comparison of measured, estimated, and predicted time histories of pitch rate. Test point number (a) 2.4-15.1B for estimation, and (b) 2.4-15.4B for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kθ</td><td>1/Tθ2</td><td>ζsp</td><td>ωsp</td><td>τθ</td><td>ωspTθ2</td><td>Category</td><td>Level</td><td>Reason for Not Level I</td></tr><tr><td>1.972</td><td>1.137</td><td>0.607</td><td>2.261</td><td>0.217</td><td>1.989</td><td>B</td><td>3</td><td>τθ&gt;0.20</td></tr><tr><td>(0.031)</td><td>(0.057)</td><td>(0.017)</td><td>(0.042)</td><td>(0.003)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 7: Comparison of measured, estimated, and predicted time his。
![](images/f0efd3e07bffd07c1ea70c9e60043d169657f19d7907f34df3c27e9c2e24ca98.jpg)  
(a)

图片摘要：该图主要展示 8: Comparison of measured, estimated, and predicted time his。
![](images/7690fe1fdeb8ac2c6f2ed574e12cf90890a60a72e7fe5e35b665c4c20cba3f68.jpg)  
FIGURE 8: Comparison of measured, estimated, and predicted time histories of pitch rate. Test point number (a) 2.4-12.1B for estimation, and (b) 2.4-12.4B for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kθ</td><td>l/Tθ2</td><td>ζsp</td><td>ωsp</td><td>τθ</td><td>ωspTθ2</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>0.649</td><td>0.362</td><td>0.348</td><td>1.541</td><td>0.183</td><td>4.257</td><td>B</td><td>2</td><td>τθ&gt;0.10</td></tr><tr><td>(0.005)</td><td>(0.015)</td><td>(0.008)</td><td>(0.012)</td><td>(0.002)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 8: Comparison of measured, estimated, and predicted time his。
![](images/f93334b7c7f9349b9eb101d2c38a28cf61eef4abba555fa9f33c352470cf9b33.jpg)  
Figure 9: Comparison of measured and predicted time histories of pitch rate. Test point number 2.4-16.1B predicted with 2.4-16.1A parameter estimates.

图片摘要：该图主要展示 9: Comparison of measured and predicted time histories of pi。
![](images/c0fbce7c34f129bd896d50653da8e300bf431849c42e189eb57f727075a9ae37.jpg)

图片摘要：该图主要展示 9: Comparison of measured and predicted time histories of pi。
![](images/2b104e31df89236ed4cf16719041e3f52a1a0af1d234a7515e58bbc76fc641df.jpg)  
FIGURE 10: Summary of parameter estimates with $2\sigma$ error bars for yaw rate to rudder pedal transfer function.

图片摘要：该图主要展示 10: Summary of parameter estimates with error bars for yaw r。
![](images/9ac3a90612bb28a09afd74eaacd52f917c13327b51b0ff81f01c5ff65a5253a4.jpg)

图片摘要：该图主要展示 10: Summary of parameter estimates with error bars for yaw r。
![](images/6d2ce26bbb1ba044e4e3f81fc9adf25037ef309fdb07bb01fd34d5fc9beb67e0.jpg)  
FIGURE 10:Continued.

图片摘要：该图主要展示 10:Continued。
![](images/27904fc920946c7b413e40f49f2d30a032d9d2a8a1245c3fb55596bd2195f2cb.jpg)  
FIGURE 10: Concluded.

图片摘要：该图主要展示 10: Concluded。
![](images/3ea041c65289586c5fde63709a2660c2ef73d03c3299a25c715becb38dbeaf7a.jpg)  
(a)

图片摘要：该图主要展示 10: Concluded。
![](images/fb2e73b14d9984ed0f7d7a504fa63454303ce2a7ccbfeae6f49fe90b8c82c50a.jpg)  
FIGURE 11: Comparison of measured, estimated, and predicted time histories of yaw rate. Test point number (a) 2.4-16.3A for estimation, and (b) 2.4-16.6A for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kr</td><td>1/Tr</td><td>ζd</td><td>ωd</td><td>τr</td><td>ζdωd</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>0.467</td><td>0.486</td><td>0.505</td><td>0.804</td><td>0.170</td><td>0.406</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.007)</td><td>(0.088)</td><td>(0.052)</td><td>(0.051)</td><td>(0.004)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 11: Comparison of measured, estimated, and predicted time hi。
![](images/ec8c8a5f75e30c6224790a8a2f9013d054c6d20256f715f678a111c6b6e11e9b.jpg)  
(a)

图片摘要：该图主要展示 12: Comparison of measured, estimated, and predicted time hi。
![](images/85bbc7e5bb2ab49cdc61b40d2fef8b85aac139c30724c8fba5d16e63cfa5e814.jpg)  
FIGURE 12: Comparison of measured, estimated, and predicted time histories of yaw rate. Test point number (a) 2.4-15.3A for estimation, and (b) 2.4-15.6B for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kr</td><td>1/Tr</td><td>ζd</td><td>ωd</td><td>τr</td><td>ζdωd</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>1.558</td><td>0.238</td><td>0.725</td><td>1.216</td><td>0.158</td><td>0.882</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.016)</td><td>(0.027)</td><td>(0.024)</td><td>(0.029)</td><td>(0.003)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 12: Comparison of measured, estimated, and predicted time hi。
![](images/dfa4dc442d3279bf92f25080ab423c596778393c38e231241455739948a27908.jpg)  
(a)

图片摘要：该图主要展示 13: Comparison of measured, estimated, and predicted time hi。
![](images/4e94516391c551d4652a7a9ff9208874329af215022c31db649b62919705a0b2.jpg)  
FIGURE 13: Comparison of measured, estimated, and predicted time histories of yaw rate. Test point number (a) 2.4-12.3A for estimation, and (b) 2.4-12.6A for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kt</td><td>l/Tt</td><td>ζd</td><td>ωd</td><td>τr</td><td>ζdωd</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>0.550</td><td>0.275</td><td>0.191</td><td>1.453</td><td>0.115</td><td>0.278</td><td>B</td><td>I</td><td>None</td></tr><tr><td>(0.008)</td><td>(0.024)</td><td>(0.012)</td><td>(0.017)</td><td>(0.004)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 13: Comparison of measured, estimated, and predicted time hi。
![](images/bdd4a1e471acd94c222f417bb6e6e44bde1764d90e185f044c30876c6ff776d9.jpg)

图片摘要：该图主要展示 14: Summary of parameter estimates with error bars for roll 。
![](images/274f3b7630b2efe97da6defd789eb541217388f26f8280491b5817a33ec38df6.jpg)  
FIGURE 14: Summary of parameter estimates with $2\sigma$ error bars for roll rate to lateral stick transfer function. First-order model.

图片摘要：该图主要展示 14: Summary of parameter estimates with error bars for roll 。
![](images/f6dae2b4de8f037bfa31e964308ac48fc5f043caa10d5da9be865f5e4721801f.jpg)  
FIGURE 14: Concluded.

图片摘要：该图主要展示 14: Concluded。
![](images/776bcd4782e152a43c0b1e928966f73ddfacba6423ad144aa98d319c5ca58a68.jpg)  
(a)

图片摘要：该图主要展示 14: Concluded。
![](images/5e9410724b5bbfaf1ea2e64996b7353d7e80efacfe6faad1e6bb4b1861f568a3.jpg)  
FIGURE 15: Comparison of measured, estimated, and predicted time histories of roll rate. First-order model. Test point number (a) 2.4-17.2A for estimation, and (b) 2.4-17.5A for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kp</td><td>I/Tk</td><td>τp</td><td>TK</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>10.077</td><td>2.801</td><td>0.101</td><td>0.357</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.636)</td><td>(0.211)</td><td>(0.015)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 15: Comparison of measured, estimated, and predicted time hi。
![](images/91a25cde1a4deeae47caad71124985f452ce9810d65dd8256cd1f2edfbba421a.jpg)  
(a)

图片摘要：该图主要展示 16: Comparison of measured, estimated, and predicted time hi。
![](images/229c54779b9b64b23e7915b7ccb7b289a7cb5fb4b6d9e72740ed0a03a1fcdb96.jpg)  
FIGURE 16: Comparison of measured, estimated, and predicted time histories of roll rate. First-order model. Test point number (a) 2.4-15.2A for estimation, and (b) 2.4-15.5B for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kp</td><td>1/TR</td><td>τp</td><td>TR</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>17.598</td><td>3.392</td><td>0.132</td><td>0.295</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.982)</td><td>(0.259)</td><td>(0.012)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 16: Comparison of measured, estimated, and predicted time hi。
![](images/bdc7022a7dc99c89dec29bf9317c52d997ffab43d65d017344ab6a3a27ad8529.jpg)

图片摘要：该图主要展示 17: Comparison of measured, estimated, and predicted time hi。
![](images/199b1b53dc35eb93123400581446ff0486914c764c49fdab371ee0e97c2cfec5.jpg)  
FIGURE 17: Comparison of measured, estimated, and predicted time histories of roll rate. First-order model. Test point number (a) 2.4-12.2B for estimation, and (b) 2.4-12.5B for prediction.

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kp</td><td>1/TR</td><td>τp</td><td>TR</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>7.546</td><td>2.392</td><td>0.137</td><td>0.418</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.337)</td><td>(0.127)</td><td>(0.011)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 17: Comparison of measured, estimated, and predicted time hi。
![](images/96dba38d6f2123f06c1e2e1a3dee5cd2c264ed2a12207edadc8d9efe0e0965ce.jpg)

图片摘要：该图主要展示 17: Comparison of measured, estimated, and predicted time hi。
![](images/ea699da22afb1e7eeab947247a56829b58910328966c651f8372dc3b13349318.jpg)  
FIGURE 18: Summary of parameter estimates with $2\sigma$ error bars for roll rate to lateral stick transfer function. Third-order hybrid model.

图片摘要：该图主要展示 18: Summary of parameter estimates with error bars for roll 。
![](images/42b0f32a98ea7523cdd36c768794ebd94e5011d7c324fe7a7d1e633443929061.jpg)

图片摘要：该图主要展示 18: Summary of parameter estimates with error bars for roll 。
![](images/61f6a6fbd44649e310bb4dd55e9980cfc9a8c2dd8e29e9d587e1b55f298800d9.jpg)  
FIGURE 18: Continued.

图片摘要：该图主要展示 18: Continued。
![](images/26a9180cf7347c6a54b536e8ccc9883b51a93335ba217dcdafb9243dbf23601a.jpg)  
FIGURE 18: Concluded.

图片摘要：该图主要展示 18: Concluded。
![](images/7ae82895c47988f5bb13fd8dbb24a7b75b8d226386f980427f087db5ade7a50e.jpg)  
(a)

图片摘要：该图主要展示 18: Concluded。
![](images/57ef6dbab7c604f17229d2cb0b3341954cd17896d9de435aebfa4760329fa388.jpg)  
(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kφ</td><td>ζφ</td><td>ωφ</td><td>1/TR</td><td>τp</td><td>TR</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>13.456</td><td>0.163</td><td>0.782</td><td>2.791</td><td>0.115</td><td>0.358</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.627)</td><td>(0.019)</td><td>(0.047)</td><td>(0.203)</td><td>(0.010)</td><td></td><td></td><td></td><td></td></tr></table>

FIGURE 19: Comparison of measured, estimated, and predicted time histories of roll rate. Third-order hybrid model. Test point number (a) 2.4-17.2A for estimation, and (b) 2.4-17.5A for prediction.

图片摘要：该图主要展示 19: Comparison of measured, estimated, and predicted time hi。
![](images/130817e814af7c4dc43a1cd8f145d78542b6f3d07b09aa8acf8f1c67c6f5020d.jpg)  
(a)

图片摘要：该图主要展示 19: Comparison of measured, estimated, and predicted time hi。
![](images/a37abd45331e09802cda9c9f7f6068b8063166676098e798fbabaffdc591d210.jpg)  
FIGURE 20: Comparison of measured, estimated, and predicted time histories of roll rate. Third-order hybrid model. Test point number (a) 2.4-15.2A for estimation, and (b) 2.4-15.5B for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kφ</td><td>ζφ</td><td>ωφ</td><td>l/TR</td><td>τp</td><td>TR</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>23.999</td><td>0.355</td><td>0.898</td><td>2.662</td><td>0.170</td><td>0.376</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.693)</td><td>(0.039)</td><td>(0.054)</td><td>(0.186)</td><td>(0.006)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 20: Comparison of measured, estimated, and predicted time hi。
![](images/38ae14b9e522bd67df08fa53a64e72f7c18e612148b5c08a56ce0f289a7f9dcf.jpg)  
(a)

图片摘要：该图主要展示 21: Comparison of measured, estimated, and predicted time hi。
![](images/c6dab7e325e6ea656fefe49dccea83fbbd982e16b62857a6ca86dfcc507b0e8c.jpg)  
FIGURE 21: Comparison of measured, estimated, and predicted time histories of roll rate. Third-order hybrid model. Test point number (a) 2.4-12.2B for estimation, and (b) 2.4-12.5B for prediction.

(b)

Parameter Values, Standard Errors (in parentheses), and Flying Qualities Prediction   

<table><tr><td>Kφ</td><td>ζφ</td><td>ωφ</td><td>1/TR</td><td>τp</td><td>TR</td><td>Category</td><td>Level</td><td>Reason for Not Level 1</td></tr><tr><td>11.886</td><td>0.054</td><td>1.201</td><td>2.874</td><td>0.179</td><td>0.348</td><td>B</td><td>1</td><td>None</td></tr><tr><td>(0.252)</td><td>(0.006)</td><td>(0.049)</td><td>(0.087)</td><td>(0.004)</td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 21: Comparison of measured, estimated, and predicted time hi。
![](images/2cb59a483d64dec281299fc955ad7a67e0bc817379d5f240ed3525540e2acc63.jpg)

图片摘要：该图主要展示 22: Results of Monte Carlo simulation for longitudinal param。
![](images/f3b0d77bebb50fa31f0f171bdf730a508094fed2f01651415ec2640fc38c92a3.jpg)

图片摘要：该图片与FIGURE 22: Results of Monte Carlo simulation for longitudinal parameter estimate这部分内容相关。
![](images/c2811d497dc4fe344be16f0d528765adbf988e294b48aae8dddf0cc77f944667.jpg)  
FIGURE 22: Results of Monte Carlo simulation for longitudinal parameter estimates.

<table><tr><td colspan="3">REPORT DOCUMENTATION PAGE</td><td>Form Approved
OMB No 0704-0188</td></tr><tr><td colspan="4">Public reporting burden for this collection of information is estimated to average 1 hour per response, including the time for reviewing instructions, searching existing data sources, gathering and maintaining the data needed, and completing and reviewing the collection of information. Send comments regarding this burden estimate or any other aspect of this collection of information, including suggestions for reducing this burden, to Washington Headquarters Services, Directorate for Information Operations and Reports, 1215 Jefferson Davis Highway, Suite 1204, Arlington, VA 22202-4302, and to the Office of Management and Budget, Paperwork Reduction Project (0704-0188), Washington, DC 20503.</td></tr><tr><td>1. AGENCY USE ONLY (Leave blank)</td><td>2. REPORT DATE
August 2000</td><td colspan="2">3. REPORT TYPE AND DATES COVERED
Contractor Report</td></tr><tr><td colspan="2">4. TITLE AND SUBTITLE
Estimation of Handling Qualities Parameters of the Tu-144 Supersonic Transport Aircraft From Flight Test Data</td><td rowspan="2" colspan="2">5. FUNDING NUMBERS
NCC1-29
537-08-23-21</td></tr><tr><td colspan="2">6. AUTHOR(S)
Timothy J. Curry</td></tr><tr><td colspan="2">7. PERFORMING ORGANIZATION NAME(S) AND ADDRESS(ES)
George Washington University
Joint Institute for the Advancement of Flight Sciences
Langley Research Center
Hampton, VA 23681-2199</td><td colspan="2">8. PERFORMING ORGANIZATION
REPORT NUMBER</td></tr><tr><td colspan="2">9. SPONSORING/MONITORING AGENCY NAME(S) AND ADDRESS(ES)
National Aeronautics and Space Administration
Langley Research Center
Hampton, VA 23681-2199</td><td colspan="2">10. SPONSORING/MONITORING
AGENCY REPORT NUMBER
NASA/CR-2000-210290</td></tr><tr><td colspan="4">11. SUPPLEMENTARY NOTES
Langley Technical Monitor: James G. Batterson</td></tr><tr><td colspan="2">12a. DISTRIBUTION/AVAILABILITY STATEMENT
Unclassified-Unlimited
Subject Category 08 Distribution: Nonstandard
Availability: NASA CASI (301) 621-0390</td><td colspan="2">12b. DISTRIBUTION CODE</td></tr><tr><td colspan="4">13. ABSTRACT (Maximum 200 words)
Low order equivalent system (LOES) models for the Tu-144 supersonic transport aircraft were identified from flight test data. The mathematical models were given in terms of transfer functions with a time delay by the military standard MIL-STD-1797A, “Flying Qualities of Piloted Aircraft,” and the handling qualities were predicted from the estimated transfer function coefficients. The coefficients and the time delay in the transfer functions were estimated using a nonlinear equation error formulation in the frequency domain. Flight test data from pitch, roll, and yaw frequency sweeps at various flight conditions were used for parameter estimation. Flight test results are presented in terms of the estimated parameter values, their standard errors, and output fits in the time domain. Data from doublet maneuvers at the same flight conditions were used to assess the predictive capabilities of the identified models. The identified transfer function models fit the measured data well and demonstrated good prediction capabilities. The Tu-144 was predicted to be between level 2 and 3 for all longitudinal maneuvers and level 1 for all lateral maneuvers. High estimates of the equivalent time delay in the transfer function model caused the poor longitudinal rating.</td></tr><tr><td rowspan="2" colspan="3">14. SUBJECT TERMS
System Identification; Flight Test Data Analysis; Closed Loop Modeling;
Handling Qualities; TU-144 Supersonic Transport</td><td>15. NUMBER OF PAGES
120</td></tr><tr><td>16. PRICE CODE
A06</td></tr><tr><td>17. SECURITY CLASSIFICATION
OF REPORT
Unclassified</td><td>18. SECURITY CLASSIFICATION
OF THIS PAGE
Unclassified</td><td>19. SECURITY CLASSIFICATION
OF ABSTRACT
Unclassified</td><td>20. LIMITATION
OF ABSTRACT
UL</td></tr></table>
