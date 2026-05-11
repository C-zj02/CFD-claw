HANDLING QUALITIES OF LARGE FLEXIBLE AIRCRAFT

NASA-CR-163593 19800023894

By

SUPAT POOPAKA

Bachelor of Science

Prince of Songkla University

Haadyai, Thailand

1972

Master of Science

University of Illinois

Urbana, Illinois

1977

LIBRARY COPY

JAN 27 1981

LANGLEY RESEARCH CENTER

LIBRARY, NASA

HAMPTON, VIRGIN

Submitted to the Faculty of the

Graduate College of the

Oklahoma State University

in partial fulfillment of

the requirements for

the Degree of

DOCTOR OF PHILOSOPHY

December 1980

图片摘要：该图片与NFO1979；Name: Supat Poopaka这部分内容相关。
![](images/2c47667c85f6e4168818c6f0c6f29613b47dbf94b637fa8fde70f0564165cfd8.jpg)

NFO1979

Name: Supat Poopaka

Date of Degree: December, 1980

Institution: Oklahoma State University Location: Stillwater, Oklahoma

Title of Study: HANDLING QUALITIES OF LARGE FLEXIBLE AIRCRAFT

Pages in Study: 61 Candidate for Degree of Doctor of Philosophy

Major Field: Mechanical Engineering

Scope and Method of Study: The effects on handling qualities of elastic modes interaction with the rigid body dynamics of a large flexible aircraft are studied by a mathematical computer simulation. An analytical method to predict the pilot ratings when there is a severe modes interaction is developed. This is done by extending the optimal control model of the human pilot response to include the mode decomposition mechanism into the model. The handling qualities are determined for a longitudinal tracking task using a large flexible aircraft with parametric variations in the undamped natural frequencies of the two lowest frequency, symmetric elastic modes made to induce varying amounts of mode interaction.

Findings and Conclusions: The modified model of the human pilot response developed in this study proved successful in discriminating when the pilot can or cannot separate rigid from elastic response in the tracking task. A comparison of the model predictions with the past experimental data shows that the modified pilot model is much better in predicting the elastic modes interaction effect on the handling qualities than the standard optimal control model of the human pilot. The techniques developed here make it easier to investigate the effects of elastic modes interaction with the rigid body dynamics of a large flexible aircraft on the handling qualities in a preliminary design stage.

HANDLING QUALITIES OF LARGE FLEXIBLE AIRCRAFT

Thesis Approved:

3eot

Thesis Advisor

Dean of the Graduate College

# ACKNOWLEDGMENTS

I would like to thank Dr. Robert L. Swaim, my thesis advisor, for his original idea on this research project, and for his technical guidance and suggestions throughout this study. I am also thankful to Dr. Karl N. Reid, my advisor and chairman of the advisory committee, for his guidance and encouragement throughout my studies at Oklahoma State University. Appreciation is also extended to my committee members, Dr. Lynn R. Ebbesen and Dr. Robert J. Mulholland who have always taken time to talk through problems and provide consultation as necessary. I am also grateful to Dr. Vijay K. Maddali whose advice contributed in developing the computer programs for the study. Special thanks are for Mrs. Teresa Tackett for her excellent job in typing the manuscript.

Parts of this research effort were supported by NASA under grant NSG 4018.

# TABLE OF CONTENTS

# Chapter

I. INTRODUCTION 1

General Background. 3

Objectives and Scope of Study 5

Plan of Presentation. 6

II. PAST RESULTS 7

III. EQUATIONS OF MOTION. 13

Small Perturbation Equations of Motion. 13

Turbulence Model. 15

Attitude Director Equations 17

B-1 Flight Condition. 19

IV. PILOT MODELING 20

Model Description 21

Internal Model. 23

Human Limitations 25

Task Definition 28

The Pilot Model 30

Pilot Opinion Rating Technique. 33

Computational Algorithms. 33

V. EFFECTS OF ELASTIC MODES INTERACTION ON HANDLING QUALITIES 35

The Illustrated Cases 36

The Separation Boundary 40

VI. CONCLUSIONS AND RECOMMENDATIONS 42

SELECTED BIBLIOGRAPHY. 44

APPENDIX A - NUMERICAL VALUES OF STABILITY DERIVATIVES AND EQUATIONS OF MOTION 47

APPENDIX B - DERIVATIONS RELATED TO SINGULAR PERTURBATION. 56

# LIST OF TABLES

# Table

I. Natural Frequencies and Damping Ratios of Eight Cases 10   
II. B-1 Flight Condition. 19   
III. Natural Frequencies and Damping Ratios of Ten Cases 37   
IV. Performance Prediction by the Standard OCM. 38   
V. Performance Prediction by the Modified OCM. 39   
VI. Dimensional Force and Moment Derivatives as a Function of Non-Dimensional Stability Derivatives 48   
VII. Dimensional Elastic Force Derivatives as a Function of Non-Dimensional Stability Derivatives. 49   
VIII. Stability Derivatives for B-1 Bomber in Mach 0.85 Flight Condition. 50   
IX. Gust Specifications 51   
X. A11 Matrix (8 x 8). 52   
XI. A12 Matrix (8 x 4). 53   
XII. $\mathsf{A}_{21} / \mu$ Matrix (4 x 8). 53   
XIII. A22/μ Matrix (4 x 4). 54   
XIV. $\mathbf{B}_1^*$ Matrix (1 x 8) 54   
XV. $\mathbf{B}_2^{\prime} / \mu$ Matrix (1 x 4) 54   
XVI. C1 Matrix (2 x 8) 54   
XVII. C2 Matrix (2 x 4) 55   
XVIII. $\mathbf{E}_1^{\prime}$ Matrix (2 x 8) 55

# LIST OF FIGURES

# Figure

Page

1. The Cooper-Harper Pilot Rating Scale 2   
2. Electronic Attitude Director Indicator (EADI). 9   
3. The Airplane Attitude Corresponding to the EADI. 9   
4. Sample Time History - Case 6 11   
5. Rigid and Elastic Pitch Angles 18   
6. Optimal Control Model of Human Pilot Response. 22   
7. Modified Optimal Control Model of Human Pilot Response 26

# NOMENCLATURE

$A_{a}$ - Matrix of physical state coefficients in the vehicle equations of motion   
$A_{g}$ -Gust matrix   
a - Half width of dead zone element   
$\mathbf{B}_{\mathbf{a}}$ - Matrix of control variable coefficients in the vehicle equations of motion   
$b_{\mathbf{W}}$ - Aircraft wing span   
$C_a$ - Matrix of output variable coefficients in the vehicle attitude director equations   
- Wing mean aerodynamic chord   
$\mathbf{D}_{\mathbf{a}}$ - Control distribution Matrix for observations   
$\mathbf{E}_{\mathbf{a}}$ - Matrix of disturbance variable coefficients   
$\mathbf{E}(\cdot)$ - Expected value of $\{\cdot\}$   
$\mathbf{f_{i}}$ - Fraction of attention allocated to $i^{\text{th}}$ display variable   
ft -Feet   
G - Scalar white noise coefficient vector in the vehicle equations of motion   
g - Local gravitational acceleration (32.17 ft/s²)   
$\mathbf{I}_{\mathbf{y}}$ - Mass moment of inertia about stability axis y   
J - Cost functional   
$\mathbf{L}_{\mathbf{u}}$ - Longitudinal gust scale factor   
$I_{w}$ - Vertical gust scale factor   
m -Airplane mass

N - Describing function gain for the threshold element  
P.O.R.- Pilot opinion rating in Cooper-Harper scale $Q_{\tau}$ - Weighting on control rate $Q_{y}$ - Weighting on display variables $Q_{\xi_i}$ - Generalized force of the $i^{\text{th}}$ elastic mode  
q - Perturbation pitch angle rate ( same as $\dot{\theta}$ ) $q_{g}$ - Perturbation of $q$ due to variations in vertical gust properties along the centerline of the vehicle  
r - $\tau$ -second delayed of the pilot control input $S_w$ - Wing area  
s - Second  
- Laplace transform variable $T_n$ - Neuromuscular constant matrix  
t - time (s) $U_o$ - Steady state vehicle velocity  
u - Perturbation forward speed $u_a$ - Control input vector $u_g$ - Perturbation of $u$ due to gust $u_m$ - "Commanded" control input $V_m$ - Motor noise covariance matrix $W_y$ - Observation noise covariance matrix $W_m$ - Motor noise $W_y$ - Observation noise $W_a$ - Random external disturbance $X_a$ - State vector associated with the physical output states of the aircraft $Y_a$ - Display information vector

$\gamma_{p}$ - Perceived display quantities $\alpha$ - Perturbation angle of attack $\alpha_{g}$ - Perturbation of $\alpha$ due to gust $\delta_{e}$ - Elevator deflection $\theta$ - Perturbation pitch angle $\theta_{g}$ - Perturbation of $\theta_{g}$ due to gust $\rho_{i}$ - Multiplicative noise/signal ratio $\sigma_{i}^{2}$ - Noise variance of i $\varepsilon$ - Error covariance matrix $\tau$ - Perceptual time delay $\mu$ - Small positive parameter which arises due to the presence of of high frequency elastic modes $\omega$ - Temporal frequency in turbulence model $\omega_{i}$ - In-vacuum elastic mode undamped natural frequency of $i^{\text{th}}$ mode $\omega_{ie}$ - Coupled undamped natural frequency of $i^{\text{th}}$ mode $\omega_{ph}$ - Natural frequency of phugoid mode $\omega_{sp}$ - Natural frequency of short-period mode $\zeta_{i}$ - Structural damping ratio of mode i $\zeta_{ie}$ - Coupled damping ratio of $i^{\text{th}}$ mode $\zeta_{ph}$ - Damping ratio of phugoid mode $\xi_{sp}$ - Damping ratio of short-period mode $\xi_{i}$ - Generalized coordinate of $i^{\text{th}}$ elastic mode $\phi_{i}^{\prime}$ - Slope of $i^{\text{th}}$ normalized mode shape

# CHAPTER 1

# INTRODUCTION

The handling or flying qualities of a piloted aircraft are the static and dynamic characteristics that influence the ease and precision with which a pilot is able to perform the control task required in support of the aircraft mission flight phase. Thus, the handling qualities depend not only on aircraft characteristics and a mission flight phase but also on the pilot's subjective opinion of the case with which he can perform the control task.

To accurately assess the pilot's opinion of the handling qualities of an aircraft prior to first flight of a prototype, a ground-based simulation is usually required. In the early stages of the design, it is more economical to use a mathematical pilot modeling simulation because the design parameters can be easily adjusted. The pilot's assessment is then related to some scale such as the widely accepted Cooper-Harper pilot rating scale (Figure 1).

Much research has been done to determine the relations between the parameters of the rigid body, small perturbation equations of motion and the pilot rating. The handling qualities requirements for a rigid airplane in Chalk et al. [1] are typical results of such research. Most of the airplanes in the past have been relatively rigid such that the elasticity of the airplanes do not contribute significantly to the pilot perceived handling qualities.

图片摘要：该图主要展示 1. The Cooper Harper Pilot Rating Scale [1]。
![](images/f76d315a3cd5a39c59d47eec2fa179680c9265a39e5a4683e1ac86f48a72811d.jpg)  
Figure 1. The Cooper-Harper Pilot Rating Scale [1]

Recent advances in control-configured vehicles design and active control technology makes it possible to increase aircraft size and the utilization of lighter structures in future designs. The elastic behavior of these vehicles is therefore becoming an appreciable influence in their handling qualities. Because of the potential adverse effects of mode interaction with the rigid body dynamics, there is a need for handling qualities assessment in the preliminary design phase of new airplanes.

# General Background

It is known that static aeroelastic deflections of an aircraft structure modify the aerodynamic pressure distributions which results in stability derivative changes associated with the rigid body, small perturbation equations of motion. Early attempts to account for aeroelastic effects on aircraft stability and control took the approach of making static aeroelastic corrections to the aerodynamic stability derivatives [2-4]. The drawbacks of this approach as pointed out by Milne [4] are that in calculating modified stability derivatives one is to imagine the major parts of the airplane to be kinematically constrained at various points which do not have any real physical meaning, and if the overall-motion frequencies are of the same order as the lower typical vibration natural frequencies of the structure then the approach is invalid.

For flying in high dynamic pressure environments, such as terrain following in turbulent air, the dynamic effects of flexibility are important enough that they must be included as additional degrees of freedom. A common approach has been to approximate the dynamics by a truncated set of superimposed orthogonal vibration modes. In this case

the phenomena of most interest are the effects of aerodynamic coupling between the various elastic modes and between elastic and rigid body modes, as well as elastic mode interaction with the feedback control system. Reference [5] was one of the earliest comprehensive studies of this problem. The most recent comprehensive work done under the AFFDL sponsorship is documented in reference [6].

The subject of handling qualities requirements and criteria for highly elastic airplanes in turbulent and high dynamic pressure environments has been largely ignored. Much of the research on handling qualities has been concerned with relatively rigid, tactical military aircraft. The handling qualities parameters, such as phugoid, short-period, dutch- roll frequencies and damping ratios, which have been determined pertinent for such airplanes, are mostly meaningless for a flexible airplane with elastic mode frequencies close to the rigid body frequencies. When multiple frequencies are in proximity to one another, the pilot cannot easily discern individual modes of motion; rather his opinion of the transient dynamics will likely be based on the time history of the total motion. No performance criteria suitable for handling qualities specification are presently available for such higher-order responses. This is all too evident in that no useful discussion of aeroelastic effects is included in the revision to the military aircraft handling qualities specification [1]. It contains only the following statement:

Since aeroelasticity, control equipment, and structural dynamics may exert an important influence on the airplane flying qualities, such effects should not be overlooked in calculations or analysis directed toward investigation of compliance with requirements of this specification (p. 497).

The specification is concerned only with desirable ranges of values on rigid body static and dynamic response parameters. There are methods available for estimating static aeroelastic corrections to rigid body aerodynamic stability derivatives [7]; however, the specification then requires the use of these in rigid aircraft equations of motion. It seems quite possible that the desirable ranges of parameter values could be significantly affected by elastic mode degrees of freedom, particularly when some of the modes have natural frequencies of the same order of magnitudes as the frequencies of the rigid body alone. It is not at all clear that the handling qualities should be specified by rigid body dynamic parameters when such mode interaction is present. In fact, the pilot could not tell, for example, how much of a given pitch angle response to command input is due to rigid body and how much to low frequency elastic modes.

The key in developing handling qualities criteria and eventually specifications for severe mode interaction situations is to establish when and under what conditions the pilot can visually separate the rigid body response from the total response. In conditions when he cannot, a structural mode suppression control system probably will be required.

# Objectives and Scope of Study

The primary objective was to develop an analytical method to determine the boundary between when the pilot can visually separate the rigid body motion from the total motion and when he cannot in terms of the small perturbation equations of motion parameters. This study is an extension of the experimental work done in reference [8], where a ground-based pilot-flown simulation was studied. The mathematical

pilot modeling simulation approach is used to assess the effects of mode interaction on the pilot opinion rating.

An extension of the optimal control model for the human pilot [9] is made so that the effects of mode interaction can be assessed. The extension is motivated by an observation of the experimental evidences of reference [8].

# Plan of Presentation

A summary of past results is presented in Chapter II. The longitudinal equations of motion for a flexible airplane are developed in Chapter III. The general description and flight condition of the flexible airplane under study are also described in that chapter. Numerical values of stability derivatives for the equations of motion are given in Appendix A. The pilot modeling and its extension is presented in Chapter IV. Derivations of some singular perturbation techniques needed in Chapter IV are summarized in Appendix B. The major results are presented in Chapter V. The conclusions and recommendations appear in Chapter VI.

# CHAPTER II

# PAST RESULTS

The only research of which we are aware that is directly relevant to the subject is documented in Crother [10] and Yen [8].

The results of North American Rockwell in Crother [10] were for an early version for the B-1 aircraft and included piloted simulator evaluations of tracking performance in turbulence. They concluded that the structural dynamics appeared as essentially a nuisance oscillation to the pilots and did not significantly effect tracking performance. However, the longitudinal dynamics of their configuration were very close to Case 1 of our results. Thus, it is not surprising that the elasticity did not significantly degrade pilot opinion; it was merely a ripple on the rigid body response.

In the work of Yen [8], the effects of parametric lowering of the undamped natural frequencies of the first two symmetric elastic modes of a flexible aircraft were investigated. A pitch tracking task, which included phugoid and short period dynamics, was programmed on a fixed-base simulator with a CRT attitude-director display of pitch command, total pitch angle and pitch error. The display and its variables are depicted in Figures 2 and 3.

The attitude-director equations are

$$
\theta_ {i} \left(x _ {p}, t\right) = \theta (t) - 0. 0 2 5 \xi_ {1} (t) - 0. 0 2 9 \xi_ {2} (t) \tag {3.1}
$$

$$
\text {p i t c h e r r o r} = \mathrm {e} _ {\theta} = \theta_ {\mathrm {i}} - \theta_ {\mathrm {c}} \tag {3.2}
$$

where 0.025 and 0.029 are the slopes of the two elastic modes at the pilot station. The flight condition is Mach 0.85 at sea level density,

Four pilots each flew eight cases which were combinations of elastic mode interaction. The cases are shown in Table I. Case 1 is the original dynamics. Case 6 was the most difficult, where the free-free elastic mode frequencies were set at 6.93 rad/s for both modes. This resulted in the phugoid mode splitting into positive and negative real roots. Sample time histories of one pilot's tracking difficulty on Case 6 are shown in Figure 4. Note the large amplitudes of the elastic modes' contributions to total pitch $\theta_{\mathrm{i}}$ relative to rigid pitch $\theta$ . This made it very difficult for the pilot to visually separate rigid from elastic pitch. The average of the four pilots' ratings of Case 6 was 6.7 on the Cooper-Harper scale. Contrast this with a 1.6 rating on Casel, the original dynamics. This work has clearly established the potential seriousness of elastic-rigid body low frequency mode interaction to handling qualities specifications and pilot rating.

图片摘要：该图主要展示 2. Electronic Attitude Director Indicator (FADI)。
![](images/b4d9e3dc4ab19da270cfbd3618217e43e9ff5db83cca247e76cb251caa516cba.jpg)  
Figure 2. Electronic Attitude Director Indicator (FADI)

图片摘要：该图主要展示 2. Electronic Attitude Director Indicator (FADI)。
![](images/eb07fa2d56823ce373c242966943244088ac9796d5bc4dc93edbc135220c0e6d.jpg)  
Figure 3. The Airplane Attitude Corresponding To Above EADI

TABLE I   
NATURAL FREQUENCIES AND DAMPING RATIOS OF EIGHT CASES  

<table><tr><td>Case #</td><td>ω1 rad/sec</td><td>ω2 rad/sec</td><td>ζsp rad/sec</td><td>ωsp rad/sec</td><td>ζph rad/sec</td><td>ωph rad/sec</td><td>ζle rad/sec</td><td>ω1e rad/sec</td><td>ζ2e rad/sec</td><td>ω2e P.O.R. rad/sec</td><td></td></tr><tr><td>1</td><td>13.59</td><td>21.18</td><td>0.5339</td><td>2.806</td><td>0.0197</td><td>0.0708</td><td>0.0494</td><td>13.312</td><td>0.0215</td><td>21.354</td><td>1.6</td></tr><tr><td>2</td><td>9.17</td><td>21.18</td><td>0.5235</td><td>2.5724</td><td>-0.00060267</td><td>0.0573</td><td>0.08769</td><td>8.7891</td><td>0.0213</td><td>21.356</td><td>2.0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Real Roots +0.090978 -0.076723</td><td>0.1999</td><td>5.8669</td><td>0.0213</td><td>21.357</td><td>5.9</td></tr><tr><td>3</td><td>6.16</td><td>21.18</td><td>0.5217</td><td>1.7691</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Real Roots +0.14654 -0.13167</td><td>0.05284</td><td>13.270</td><td>0.1137</td><td>5.9702</td><td>3.1</td></tr><tr><td>4</td><td>13.59</td><td>4.79</td><td>0.6872</td><td>1.5745</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Real Roots +0.17581 -0.15307</td><td>0.0773</td><td>11.801</td><td>0.0162</td><td>11.574</td><td>2.0</td></tr><tr><td>5</td><td>11.66</td><td>11.66</td><td>0.5436</td><td>2.5819</td><td>-0.0001122</td><td>0.0537</td><td>0.0773</td><td>7.3305</td><td>0.007599</td><td>6.9178</td><td>6.7</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>Real Roots +0.17581 -0.15307</td><td>0.1919</td><td>10.234</td><td>-0.0004277</td><td>9.8978</td><td>2.3</td></tr><tr><td>6</td><td>6.93</td><td>6.93</td><td>0.7028</td><td>1.3665</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>0.0282</td><td>0.1129</td><td>10.347</td><td>0.0005306</td><td>9.7781</td><td>1.9</td></tr><tr><td>7</td><td>10.25</td><td>9.75</td><td>0.5517</td><td>-0.0483</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>0.0256</td><td>0.11021</td><td>10.347</td><td>0.0005306</td><td>9.7781</td><td>1.9</td></tr><tr><td>8</td><td>10.68</td><td>9.27</td><td>2.3893</td><td>-0.0541</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

图片摘要：该图主要展示 I。
![](images/6c179e406a3e7dbffc8b1a3dbd70c0834206d34084b65f276b7b525045f12c58.jpg)  
Figure 4. Sample Time History-Case 6

图片摘要：该图主要展示 4. Sample Time History Case 6。
![](images/e7a5248edd95ea3d307403ba89adb3eb53b65db0da3b2bbff01a45bc267bcfbf.jpg)

图片摘要：该图主要展示 4. Sample Time History Case 6B Figure 4. (Continued) CHAPTER。
![](images/ad9b41a2613c3cc3f2db609775ba148f768f84cee23f4ba196e4be03205b29c9.jpg)

图片摘要：该图主要展示 4. Sample Time History Case 6B Figure 4. (Continued) CHAPTER。
![](images/52330ce9cc0c0da68b98b8e40073fbb11482156b8edbe5ac7fa3072551075394.jpg)  
-B-  
Figure 4. (Continued)

# CHAPTER III

# EQUATIONS OF MOTION

The equations of a flexible airplane consist of an overall spatial motion, that is, a rigid body motion, and a local deformation due to its inherent flexibility. The basic principles underlying the equations of motion are the conservation of the linear and angular momenta and an internal equilibrium due to elastic deformation. The equations are written in terms of the $x, y, z$ body-fixed axes frame of reference. The orthogonal axes are chosen such that the $x$ -axis passes through the center of gravity of the airplane and points forward parallel to the free stream steady-state (trim) velocity, the $y$ -axis points out to the right wing, and $z$ -axis points downward.

The deformation of the airplane is expressed in terms of natural mode shapes and generalized coordinates. The airplane is assumed to be a plate like structure in the normal mode (in-vacuum vibration modes) calculation.

In the next four sections the pertinent assumptions and the equations of motion are summarized. The detailed derivation and related discussions can be found in [11-14].

# Small Perturbation Equations of Motion

For a cruise, level flight condition at a trim speed $\mathsf{U}_0$ , the small perturbation longitudinal equations of motion are given by:

$$
\begin{array}{l} \dot {m u} = - m g \theta + X _ {u} (u + u _ {g}) + X _ {\alpha} (\alpha + \alpha_ {g}) + X _ {\delta_ {c}} \delta_ {c} \\ m U _ {0} (\dot {\alpha} - \dot {\theta}) = Z _ {u} (u + u _ {g}) + Z _ {\alpha} (\alpha + \alpha_ {g}) + Z _ {\dot {\alpha}} (\dot {\alpha} - q _ {g}) + Z _ {\dot {\theta}} (\dot {\theta} + q _ {g}) \\ + Z _ {\delta e} \delta e + \sum_ {i = 1} ^ {\infty} \left[ \frac {\partial Z}{\partial \xi} \xi_ {i} + \frac {\partial Z}{\partial \xi_ {i}} \xi_ {i} \right] \\ \end{array}
$$

$$
\begin{array}{l} I _ {y} \ddot {\theta} = M _ {u} (u + u _ {g}) + M _ {\alpha} (\alpha + \alpha_ {g}) + M _ {\dot {\alpha}} (\dot {\alpha} - q _ {g}) + M _ {\dot {\theta}} (\dot {\theta} + q _ {g}) \tag {3.1} \\ + M _ {\delta e} \delta e + _ {i = 1} ^ {\infty} \left[ \frac {\partial M}{\partial \xi_ {i}} \xi_ {i} + \frac {\partial M}{\partial \dot {\xi} _ {i}} \dot {\xi} _ {i} \right] \\ \end{array}
$$

$$
\begin{array}{l} m _ {i} \left[ \ddot {\xi_ {i}} + 2 \zeta_ {i} \omega_ {i} \dot {\xi_ {i}} + \omega_ {i} ^ {2} \xi_ {i} \right] = \left(\frac {\partial Q _ {\xi_ {i}}}{\partial a}\right) (\alpha + \alpha_ {g}) + \frac {\partial Q _ {\xi_ {i}}}{\partial q} (\dot {\theta} + q _ {g}) \\ + \left(\frac {\partial Q _ {\xi_ {i}}}{\partial \delta_ {e}}\right) \delta_ {e} + \left(\frac {\partial Q _ {\xi_ {i}}}{\partial \dot {\alpha}}\right) (\dot {\alpha} - q _ {g}) + k = 1 ^ {\infty} \left[ \frac {\partial Q _ {\xi_ {i}}}{\partial \xi_ {k}} \xi_ {k} + \frac {\partial Q _ {\xi_ {i}}}{\partial \dot {\xi} _ {k}} \dot {\xi} _ {k} \right], i = 1, 2,.. \\ \end{array}
$$

where:

$$
(\cdot) \equiv d (\cdot) / d t
$$

u Perturbation forward speed

$\mathbf{u}_{\mathbf{g}}$ Perturbation of $\mathbf{u}$ due to gust

$\theta$ Perturbation pitch angle (rad)

q Perturbation pitch angle rate (rad/s), $(q = \dot{0})$

qg Perturbation of q due to gust

$\alpha$ Perturbation of angle of attack (rad)

$\alpha_{g}$ Perturbation of $\alpha$ due to gust

$\delta_{e}$ Perturbation of elevator deflection (rad)

$\xi_{i}$ Generalized coordinate of the $i^{\text{th}}$ elastic model

m i Generalized mass of the $i^{\text{th}}$ elastic mode

$Q_{\xi_i}$ Generalized force of the $i^{th}$ elastic mode

$\omega_{i}$ in-vacuum elastic mode undamped natural frequency of $i^{\text{th}}$ mode

The equations (3.1) are rewritten in a state-variable formulation as:

$$
\dot {x} _ {a} (t) = A _ {a} x _ {a} (t) + B _ {a} u _ {a} (t) + E _ {a} w _ {a} (t) \tag {3.2}
$$

where

$$
x _ {a} (t) = \operatorname {c o l}. [ u g, a g _ {1}, a g, q g, u, a, 0, \dot {\theta}, \xi_ {1}, \xi_ {2}, \dots , \dot {\xi} _ {1}, \dot {\xi} _ {2}, \dots ]
$$

$$
u _ {a} (t) = \delta_ {e}
$$

The state $\alpha_{\mathbf{g}_1}$ and the input vector $\mathbf{w}_a(t)$ are to be discussed in the next section on the turbulence model.

# Turbulence Model

The turbulence model is derived from the Dryden gust power spectra which have the forms [1].

$$
\phi_ {U _ {g}} (\omega) = \sigma_ {u} ^ {2} \frac {2 L _ {u}}{U _ {o}} \frac {1}{1 + \left(\frac {L _ {u}}{U _ {o}} \omega\right) ^ {2}}
$$

$$
\phi_ {w} g (\omega) = \sigma_ {w} ^ {2} \frac {L _ {w}}{U _ {o}} \frac {1 - 3 \left(\frac {L _ {u}}{U _ {o}} \omega\right) ^ {2}}{\left[ 1 + \left(\frac {L _ {w}}{U _ {o}} \omega\right) ^ {2} \right] ^ {2}}
$$

$$
\phi_ {\alpha} g (\omega) = \frac {1}{U _ {0} ^ {2}} \phi_ {W} g (\omega)
$$

$$
\phi_ {q _ {g}} (\omega) = \frac {\left(\frac {\omega}{U _ {0}}\right) ^ {2}}{1 + \left(\frac {4 b _ {w}}{\pi} \frac {\omega}{U _ {0}}\right) ^ {2}} \phi_ {w g} (\omega)
$$

where

$$
\sigma_ {i} ^ {2} = \frac {1}{2 \pi} \int_ {\infty} ^ {\infty} \phi_ {i} (\omega) d \omega , i = u _ {g}, w _ {g}, a _ {g}, a n d q _ {g}
$$

$\omega$ temporal frequency (rad/s)

$\mathbf{U}_{0}$ true air speed

$b_{\mathbb{W}}$ wing span

L u, L w gust scale factors which depend on the altitude

The time domain representation of the turbulence as a shaping filter with zero mean, gaussian, white noise processes $\mathbf{1}$ , and $\mathbf{2}$ as inputs is:

$$
\left[ \begin{array}{l} \dot {u} _ {g} \\ \dot {\alpha}  \\ \dot {\alpha} _ {g} \\ \dot {q} _ {g} \end{array} \right] = [ A _ {g} ] \left[ \begin{array}{l} u _ {g} \\ \alpha \\ \alpha_ {g} \\ q _ {g} \end{array} \right] + [ G ] \left[ \begin{array}{l} n _ {1} \\ n \\ 2 \end{array} \right]
$$

where

$$
\left[ A _ {g} \right] = \left[ \begin{array}{c c c c} - \frac {U _ {o}}{L _ {u}} & 0 & 0 & 0 \\ 0 & - \frac {U _ {o}}{L _ {w}} & 0 & 0 \\ 0 & - (\sqrt {3} - 1) \frac {\sigma_ {w}}{L _ {w}} \sqrt {\frac {U _ {o}}{L _ {w}}} & - \frac {U _ {o}}{L _ {w}} & 0 \\ 0 & - (\sqrt {3} - 1) \frac {\pi \sigma_ {w}}{4 b _ {w}} \frac {U _ {o}}{L _ {w}} \sqrt {\frac {U _ {o}}{L _ {w}}} & - \frac {\pi U _ {o} ^ {2}}{4 b _ {w} L _ {w}} & - \frac {\pi U _ {o}}{4 b} \end{array} \right]
$$

$$
[ G ] = \left[ \begin{array}{c c} u \sqrt {\frac {2 U _ {o}}{L _ {u}}} & 0 \\ 0 & 1 \\ 0 & \frac {\sigma_ {w} \sqrt {3}}{\sqrt {U _ {o} L _ {w}}} \\ 0 & \frac {\pi \sigma_ {w} \sqrt {3}}{4 b _ {w}} \sqrt {\frac {U _ {o}}{L _ {w}}} \end{array} \right]
$$

and

$$
\operatorname {E} \left\{\left[ \begin{array}{l} n _ {1} \\ n _ {2} \end{array} \right] \quad [ n _ {1} \quad n _ {2} ] \right\} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right]
$$

# Attitude Director Equations

The total pitch angle time history that the pilot feels and sees, either on the outside horizontal or the attitude indicator display, is given by [10]:

$$
\begin{array}{l} y _ {a} \left(x _ {p}, t\right) = \theta (t) - \sum_ {i = 1} ^ {n} \phi_ {j} ^ {\prime} \left(x _ {p}\right) \xi_ {j} (t) \tag {3.5} \\ = \theta (t) - \theta_ {e} \left(x _ {p}, t\right) \\ \end{array}
$$

where $x_p$ indicates pilot fuselage station, $\phi_j(x_p)$ the slope of the $j^{\text{th}}$ symmetric elastic mode at that station, $\theta(t)$ the rigid body pitch angle, and $\theta_e(t)$ the elastic contribution to the total pitch angle (Figure 5).

The equation (3.5) can be written in terms of the state variables defined in equation (3.2) as follows:

$$
y _ {a} (t) = C _ {a} x _ {a} (t)
$$

where

$$
C _ {a} = \operatorname {c o l}. [ 0, 0, 0, 0, 0, 0, 1, 0, - \phi_ {1} ^ {\prime} - \phi_ {2} ^ {\prime}, \dots , 0, 0, \dots ]
$$

图片摘要：该图主要展示 5. Rigid And Elastic Pitch Angles。
![](images/bd7ceff2a4af9b6115eedbdc2be7f21a8c4ddb0ecf5264be444a1da05d5db497.jpg)

图片摘要：该图主要展示 5. Rigid And Elastic Pitch Angles。
![](images/b8c163ae203facdf8367bb43b2d73e03ad0b933bac7ff1abfcc8dc355e857587.jpg)  
Figure 5. Rigid And Elastic Pitch Angles

# B-1 Flight Condition

The B-1 bomber was chosen for this study because it exemplifies the trend toward more elastic structures for future large aircraft. The total length of the B-1 is $46\mathrm{m}$ (151 ft.). The reference wing span utilized at the flight condition in Table II is $41.7\mathrm{m}$ (136.67 ft.). The values of the stability derivatives and the necessary data for the equations of motion are given in Appendix A.

# TABLE II

# B-1 FLIGHT CONDITION

$$
\text {M a s s} = 1 0 3, 3 7 0. 1 5 \mathrm {k g} (7 0 8 5. 0 \text {s l u g s})
$$

$$
\text {M a c h N o .} = 0. 8 5
$$

$$
\text {V e l o c i t y} = 2 8 9. 4 \mathrm {m} / \mathrm {s} (9 4 9. 0 \mathrm {f p s})
$$

$$
\operatorname {c g} \text {a t f u s e l a g e s t a t i o n} = 4 0. 6 7 \mathrm {m} (1 0 6 1. 2 \mathrm {i n})
$$

$$
I _ {y} = 8. 0 \times 1 0 ^ {6} k g - m ^ {2} (5. 9 \times 1 0 ^ {6} s l u g - f t ^ {2})
$$

$$
S _ {w} = 1 8 0. 8 m ^ {2} (1 9 4 6. 0 f t ^ {2})
$$

$$
\bar {c} _ {w} = 4. 6 7 \mathrm {m} (1 5. 3 3 \mathrm {f t})
$$

$$
b _ {W} = 4 1. 7 \mathrm {m} (1 3 6. 6 7 \mathrm {f t})
$$

# CHAPTER IV

# PILOT MODELING

The human pilot in a manual control task can be modeled as an active feedback element in the aircraft control system. The quasi-linear model and the optimal control model (OCM) are the two models widely used in this way. The quasi-linear model has the analytical description in terms of the frequency-domain control system design technique, while the optimal control model is based on the time-domain or optimal control theory. Since the analysis in this study is mostly in the time-domain, the optimal control model is employed through out. There are other reasons for employing the optimal control model which will be discussed later.

The optimal control model of the human pilot was originally developed by Kleinman, Baron and Levison [9]. The fundamental assumption underlying the OCM is that the well-motivated, well-trained human pilot will act in a near optimal manner subject to the pilot's internal limitations and understanding of the task. By specifying human limitations, the optimality assumption gives a model that adapts to task specifications and requirements automatically and not through a subsidiary set of adjustment rules as has been done in the quasi-linear model. Thus, for a new situation, the optimal control model can be modified by just determining the operative limitations and the

new control task. The review of the past applications of the model can be found in reference [15].

# Model Description

The structure of the optimal control model of human pilot response is shown in Figure 6. The aircraft dynamics, which also include noise shaping filters of the turbulence, are described by the linear, time invariant equations.

$$
\dot {x} _ {a} (t) = A _ {a} x _ {a} (t) + B _ {a} u _ {a} (t) + E _ {a} w _ {a} (t) \tag {4.1}
$$

$$
x _ {a} (0) = \text {g i v e n}
$$

where

$x_{a}(t) =$ aircraft and shaping filters state vector of dimension Na

$\mathbf{u}_a(t) =$ pilot's control input vector of dimension $\mathbf{Nu}$

$w_{a}(t) =$ disturbance vector of dimension Nw, each of which is an independent zero mean, Gaussian white noise process with covariance

$$
E \left\{w _ {a _ {i}} (t) w _ {a _ {i}} (\sigma) \right\} = W _ {i} \delta (t - \sigma), i = 1, 2, \dots , N w \tag {4.2}
$$

The display variables are given by a linear combination of state variables.

$$
y _ {a} (t) = C _ {a} x _ {a} (t) \tag {4.3}
$$

where

$y_{a}(t) =$ displayed vector of dimension $N_{y}$

图片摘要：该图主要展示 6. Optimal Control Model of Human Pilot Response。
![](images/8b8b15a1d97473185dccc5f129bc911cf4a8f7f8355495e3138c129aa8283d11.jpg)  
Figure 6. Optimal Control Model of Human Pilot Response

The usual assumption in the model is that if a quantity $y_{i}$ is explicitly displayed to the pilot, he also derives the rate of change $\dot{y}_{i}$ . Thus, $y_{a}(t)$ contains both position and velocity information of a displayed signal, but no higher derivative information.

# Internal Model

The information processor in the pilot model operates on a noisy, delayed version of the displayed variables to obtain a "best" estimate of the aircraft state vector. This is accomplished by a Kalman filter and a least-mean-square predictor and makes use of an internal model. The internal model of the pilot may be considered to consist of [16].

1. Knowledge about the overall behavior of the aircraft under control and about the possibilities to control it.   
2. Knowledge about the disturbances acting on the aircraft and the way they will influence it. This knowledge will be of a statistical nature.   
3. Knowledge about the task to be performed.

In many instances, the assumption that the internal model is an exact replica of the system model, i.e., perfect internal model, appears to be a satisfactory one [17]. There are situations in which the assumption of a perfect internal model does not appear tenable. In a highly complex system, i.e., one with a large number of state variables, with a single display it is unlikely to be modeled perfectly by the pilot.

It is of interest in this study to determine the effects of high frequency oscillation, contributed mainly by the elastic modes, on the handling qualities and pilot rating. From a past experiment with ground based simulation of the elastic airplane [8], the pilot action

in a pitch tracking task closely resembles that of the rigid body pitch error rather than the total error displayed to him. This shows the pilot's ability to filter out the high frequency oscillation in the total pitch response and leads to a hypothesis that the pilot uses the slowly varying dynamics subsystem as the internal model.

The decomposition of the slowly varying dynamics from the aircraft/disturbance dynamics, Eqns. (4.1) and (4.3), is accomplished by the singular perturbation technique (Appendix B). The aircraft/disturbance dynamics can be written in the form:

$$
\begin{array}{l} \dot {x} _ {1} (t) = A _ {1 1} x _ {1} (t) + A _ {1 2} x _ {2} (t) + B _ {1} u _ {a} (t) + l _ {1} w _ {a} (t) \tag {4.4} \\ \mu \dot {x} _ {2} (t) = A _ {2 1} x _ {1} (t) + A _ {2 2} x _ {2} (t) + B _ {2} u _ {a} (t) + l _ {2} w _ {a} (t) \\ y _ {a} (t) = C _ {1} x _ {1} (t) + C _ {2} x _ {2} (t) \\ \end{array}
$$

where

$\mathbf{x}_1(t) =$ rigid body and noise shaping filters state vector

$x_{2}(t) =$ elastic modes state vector

$\mu =$ a small positive parameter which arises due to the presence of high frequency elastic modes and can be an unknown in this analysis.

Then, by letting $\mu \to 0^{+}$ we get

$$
\begin{array}{l} \dot {x} _ {d} (t) = A _ {d} x _ {d} (t) + B _ {d} u _ {a} (t) + E _ {d} w _ {d} (t) \tag {4.5} \\ y _ {d} (t) = C _ {d} x _ {d} (t) + D _ {d} u _ {a} (t) \\ \end{array}
$$

where

$$
\begin{array}{l} A _ {d} = A _ {1 1} - A _ {1 2} A _ {2 2} ^ {- 1} A _ {2 1} \\ B _ {d} = B _ {1} - A _ {1 2} A _ {2 2} ^ {- 1} B _ {2} \\ C _ {d} = C _ {1} - C _ {2} A _ {2 2} ^ {- 1} A _ {2} \\ D _ {d} = D - C _ {2} A _ {2 2} ^ {- 1} B _ {2} \\ E _ {d} = E _ {1} - A _ {1 2} A _ {2 2} ^ {- 1} E _ {2} \quad \text {T h i s i s p r o v i d e d} A _ {2 2} ^ {- 1} \text {e x i s t s}. \\ \end{array}
$$

By using an imperfect internal model, the computational task becomes formidable since it involves the solution of the matrix delay differential equation [17]. The structure of the original optimal control model can be modified from Figure 6 to that of Figure 7. This modification does not affect the prediction capability of the model very much as has been shown in references [17-19]. In this modified model, the pure time delay $\tau$ is approximated by a first-order Pade polynomial. Thus, the relation between $u_{a}(t)$ and $r(t)$ in Figure 7, which was originally expressed by

$$
u _ {a} (t) = r (t - \tau) \tag {4.6}
$$

or in the Laplace transform operator s,

$$
u _ {a} (s) = e ^ {- \tau s} r (s) \tag {4.7}
$$

is now approximated by

$$
u _ {a} (s) = \frac {- s + 2 / \tau}{s + 2 / \tau} r (s) \tag {4.8}
$$

which can be expressed in the state variable form as

$$
u _ {a} (t) = z (t) - r (t) \tag {4.9}
$$

where

$$
\dot {z} (t) = - \frac {2}{\tau} I z (t) + \frac {4}{\tau} I r (t) \tag {4.10}
$$

I is an identity matrix of appropriate dimension. The time delay $\tau$ is normally 0.1 to 0.2 sec.

# Human Limitations

Other than the time delay, the pilot has inherent limitations of perceptual noise and perceptual indifference thresholds on displayed information. The time delay has been compensated for in the control action as shown in Eqns. (4.9) and (4.10). The other quantities are associated with the observation process in the pilot model, so the

图片摘要：该图主要展示 7. Modified Optimal Control Model of Human Pilot Response。
![](images/f79a34702d68abe537216b20ced29aa1c538747f0ea42f33b8d9135e6eaeba4b.jpg)  
Figure 7. Modified Optimal Control Model of Human Pilot Response

pilot is assumed to perceive $y_{\mathfrak{p}}(t)$ which is a noisy version of $y_{a}(t)$ , i.e.,

$$
y _ {p} (t) = y _ {a} (t) + v _ {y} (t) \tag {4.11}
$$

where the observation threshold is replaced by the Random Input Describing Function $N(\sigma)$ and incorporated in the observation noise, $v_{y}(t)$ is a zero-mean, gaussian, white noise process with autocovariance,

$$
E \left\{v _ {y _ {a _ {i}}} (t) v _ {y _ {a _ {i}}} (\sigma) \right\} = V _ {y _ {i}} (t - \sigma), i = 1, 2, \dots , N _ {y} \tag {4.12}
$$

When directly viewing $y_{a_i}(t)$ , the associated covariance $V_{y_i}$ is:

$$
V _ {y _ {i}} = \frac {e _ {y _ {i}} ^ {\circ}}{f _ {i}} \hat {\sigma} _ {i} ^ {2} \tag {4.13}
$$

where

$$
\hat {\sigma} _ {i} = \sigma_ {y _ {i}} N (\sigma_ {y _ {i}}) ^ {- 1}
$$

$$
\sigma_ {y _ {i}} = \sqrt {E \left\{y _ {a _ {i}} ^ {2} (t) \right\}}
$$

$$
N \left(\sigma_ {y _ {i}}\right) = \operatorname {e r f c} \left(\frac {a _ {i}}{y _ {i} \sqrt {2}}\right), \text {d e s c r i b i n g}
$$

$$
\text {e r f c} = \text {e r r o r}
$$

$$
a _ {i} = \text {h a l f w i d t h o f d e a d z o n e e l e m e n t}
$$

$$
\begin{array}{l} \mathrm {o} _ {\mathrm {y} _ {\mathrm {i}}} = \text {n o i s e / s i g n a l r a t i o} \\ = 0. 0 1 \pi \text {o r} - 2 0 \mathrm {d B} \\ \end{array}
$$

$$
f _ {i} = \text {a t t e n t i o n a l l o c a t i o n t o d i s p l a y i n d i c a t o r i}
$$

For the total of $k$ indicators, neglecting the time spent in interinstrument scanning, we have

$$
\underset {i = 1} {\overset {k} {\sum}} f _ {i} = 1, 0 <   f _ {i} <   1 \tag {4.14}
$$

The value of $f_{i}$ is chosen such that the cost functional of the pilot model is minimized.

# Task Definition

The important assumption about the optimal control pilot model is that the pilot's control task is adequately reflected in the choice of a control $\mathbf{r}(\cdot)$ that minimizes the cost functional of the form

$$
J (\mathbf {r}) = \lim  _ {\mathrm {T} \rightarrow \infty} \mathrm {E} \left\{\frac {1}{\mathrm {T}} \int_ {0} ^ {\mathrm {T}} \left[ y _ {\mathrm {a}} ^ {\prime} (t) Q _ {\mathrm {y}} y _ {\mathrm {a}} (t) + \dot {r} ^ {\prime} (t) Q _ {\mathrm {R}} \dot {r} (t) \right] d t \right\} \tag {4.15}
$$

conditioned on the perceived information $y_{p}(\cdot)$ . $Q_{y}$ is a specified constant, symmetric, nonnegative definite matrix which depends on the task specification. The control rate term is used to account for the pilot's limitation on the rate of control motion and introduces first-order neuromuscular dynamics in the pilot model.

The selection of the weighting $Q_{y} = \text{diag}$ . $[q_{y_i}]$ is such that

$$
\mathrm {q} _ {\mathrm {y} _ {\mathrm {i}}} = \left| \frac {1}{\mathrm {y} _ {\mathrm {p i}} , \max } \right| ^ {2} \tag {4.16}
$$

where

$y_{\mathbf{p_i}, \mathbf{max}}$ is the maximum desired or allowable value of $y_{\mathbf{p_i}}$ . Unlike $Q_y$ , the weighting $Q_R = \text{diag.} [q_{r_i}]$ , a positive definite matrix, is not specified before the pilot model equations are solved. It can be shown that the pilot control law which minimizes (4.15) takes the following form:

$$
\mathrm {T} _ {\mathrm {n}} \dot {\boldsymbol {r}} (\mathrm {t}) = - \boldsymbol {r} (\mathrm {t}) + \mathrm {u} _ {\mathrm {m}} (\mathrm {t}) + \mathrm {v} _ {\mathrm {m}} (\mathrm {t}) \tag {4.17}
$$

The matrix $\mathbf{T}_{\mathbf{n}}$ is assumed to be in the form $\mathbf{T}_{\mathbf{n}} = \mathrm{diag}$ . $[\mathbf{t}_{\mathbf{n_i}}]$ , $i = 1,2,\ldots, \mathbf{Nu}$ . The scalars $\mathbf{t}_{\mathbf{n_i}}$ are a neuromuscular time constant of human limbs, which has a typical value of 0.1 sec., independent of the system to be controlled. Thus, the weighting $\mathbf{q}_{\mathbf{r_i}}$ are adjusted iteratively until each $\mathbf{t}_{\mathbf{n_i}} = 0.1$ sec. If the resulting $\mathbf{q}_{\mathbf{r_i}}$ weighting is such that $1 / \sqrt{\mathbf{q}_{\mathbf{r_i}}}$ is much greater than the physical rate at which one can move

control $r_i$ , then $q_{r_i} = |1 / f_i(t), \max|^2$ must be used. Though, this rarely happens except for highly unstable aircraft dynamics or an aircraft flying through very severe turbulence.

The motor noise $\nu_{\mathfrak{m}}(t)$ is a zero-mean, gaussian, white noise process, with autocovariance

$$
E \left\{v _ {m} (t) v _ {m} (\sigma) \right\} = V _ {m} \delta (t - \sigma) \tag {4.18}
$$

and $V_{\mathfrak{m}}$ is known to scale with $E\{\mathfrak{m}_{\mathbf{i}}^{2}(\mathfrak{t})\}$ , i.e.,

$$
V _ {m _ {i}} = \rho_ {m _ {i}} E \left\{m _ {i} ^ {2} (t) \right\} \tag {4.19}
$$

where the typical value of the motor noise/signal ratio

$$
m _ {i} = 0. 0 0 3 \pi .
$$

Equations (4.9) and (4.10) may now be augmented to Eqn.

(4.1) to define an augmented system of equations

$$
\dot {x} _ {c} (t) = A _ {c} x _ {c} (t) + B _ {c} u _ {m} (t) + E _ {c} w _ {c} (t) \tag {4.20}
$$

$$
y _ {a} (t) = C _ {c} x _ {c} (t)
$$

where

$$
x _ {c} = \left[ x _ {a}, z, r \right] ^ {\prime}
$$

$$
A _ {C} = \left[ \begin{array}{l l l} A _ {a} & B _ {a} & - B _ {a} \\ 0 & - 2 / \tau & 4 / \tau \\ 0 & 0 & - T _ {n} \end{array} \right]
$$

$$
B _ {C} = \left[ 0, 0, T _ {n} ^ {- 1} \right]
$$

$$
C _ {c} = \left[ C _ {a}, 0, 0 \right]
$$

$$
E _ {C} = \left[ \begin{array}{l l} E _ {a} & 0 \\ 0 & 0 \\ 0 & T _ {n} ^ {- 1} \end{array} \right]
$$

$$
w _ {c} = [ w, v _ {m} ] ^ {\prime}
$$

Equation (4.20) is the "actual" dynamics to be controlled by the pilot.

# The Pilot Model

The pilot's control input $\mathbf{r}(t)$ that minimizes $J(\mathbf{r})$ is generated based on the augmented system of the internal model (4.5) and the delay compensation (4.9) and (4.10), i.e.,

$$
\dot {x} _ {s} (t) = A _ {s} x _ {s} (t) + B _ {s} r (t) + E _ {s} w (t) \tag {4.21}
$$

$$
y _ {s} (t) = C _ {s} x _ {s} (t) + D _ {s} r (t)
$$

where

$$
\begin{array}{l} \mathrm {x} _ {\mathrm {s}} = \left[ \begin{array}{l} \mathrm {x} _ {\mathrm {d}} \\ \mathrm {z} \end{array} \right] \\ \mathrm {A} _ {\mathrm {s}} = \left[ \begin{array}{l l} \mathrm {A} _ {\mathrm {d}} & \mathrm {B} _ {\mathrm {d}} \\ 0 & - 2 / \tau \end{array} \right] \end{array}
$$

$$
B _ {S} = \left[ \begin{array}{l} - B _ {d} \\ 4 / \tau \end{array} \right]
$$

$$
C _ {s} = \left[ C _ {d}, D _ {d} \right]
$$

$$
D _ {s} = \left[ - D _ {d} \right]
$$

$$
E _ {S} = \left[ \begin{array}{l} E _ {d} \\ 0 \end{array} \right]
$$

The command control of the pilot is given by

$$
\begin{array}{l} u _ {m} (t) = - L _ {\text {o p t}} x _ {s} (t) \tag {4.22} \\ = - L ^ {*} x _ {t} (t) \\ \end{array}
$$

where

$$
\begin{array}{l} L ^ {*} = \left[ L _ {\text {o p t}} 0 \right] \\ x _ {t} = \left[ \begin{array}{l} x _ {s} \\ r \end{array} \right] \\ \mathrm {L} _ {\text {o p t}} = \mathrm {P} _ {2 2} ^ {- 1} \mathrm {Q} _ {\mathrm {R}} \\ \end{array}
$$

$$
T _ {n} = P _ {2 2} ^ {- 1} P _ {1 2}
$$

$$
P = \left[ \begin{array}{l l} P _ {1 1} & P _ {1 2} \\ P _ {1 2} & P _ {2 2} \end{array} \right]
$$

satisfies the equation

$$
\Lambda_ {o} ^ {\prime} P + P A _ {o} + C _ {o} ^ {\prime} Q _ {y} C _ {o} - P B _ {o} Q _ {R} ^ {- 1} B _ {o} ^ {\prime} P = 0 \tag {4.23}
$$

where

$$
A _ {0} = \left[ \begin{array}{l l} A _ {s} & B _ {s} \\ 0 & 0 \end{array} \right]
$$

$$
B _ {o} = \left[ \begin{array}{c} 0 \\ I \end{array} \right]
$$

$$
C _ {o} = \left[ \begin{array}{c c} C _ {s} & D _ {s} \end{array} \right]
$$

The state $x_{t}(t)$ is the best estimate of $x_{t}(t)$ generated by a Kalman filter

$$
\dot {\hat {x}} _ {t} (t) = A _ {t} \hat {x} _ {t} (t) + B _ {t} u _ {m} (t) + K \left[ y _ {p} - C _ {0} \dot {\hat {x}} _ {t} (t) \right] \tag {4.24}
$$

where

$$
K = \sum C _ {o} ^ {-} V _ {y} ^ {- 1} \tag {4.25}
$$

and $\Sigma$ satisfies the equation

$$
A _ {t} \Sigma + \Sigma A _ {t} ^ {\prime} + E _ {o} W _ {t} E _ {o} ^ {\prime} + \Sigma C _ {o y} ^ {- 1} C _ {o} \Sigma = 0 \tag {4.26}
$$

where

$$
A _ {t} = \left[ \begin{array}{l l} A _ {s} & B _ {s} \\ 0 & - T _ {n} ^ {- 1} \end{array} \right]
$$

$$
B _ {t} = \left[ \begin{array}{l} 0 \\ T _ {n} ^ {- 1} \end{array} \right]
$$

$$
E _ {0} = \left[ \begin{array}{l l} E _ {s} & 0 \\ 0 & T _ {n} ^ {- 1} \end{array} \right]
$$

$$
W _ {t} = \left[ \begin{array}{l l} W & 0 \\ 0 & V _ {m} \end{array} \right]
$$

Combining equations (4.11) with (4.20), (4.22) and (4.24) yields the closed loop system

$$
\begin{array}{l} \dot {x} _ {c} (t) = A _ {c} x _ {c} (t) - B _ {c} L \hat {x} _ {t} (t) + E _ {c} w _ {c} (t) \\ \dot {\hat {x}} _ {t} (t) = \left(A _ {1} - B _ {1} L\right) \hat {x} _ {t} + K \left[ C _ {c} x _ {c} - C _ {o} \hat {x} _ {t} + v _ {y} (t) \right] \tag {4.27} \\ \end{array}
$$

or

$$
\dot {\psi} = F \psi + G w \tag {4.28}
$$

where

$$
\begin{array}{l} \psi = \left[ \begin{array}{l} x _ {c} \\ x _ {t} \end{array} \right] \\ F = \left[ \begin{array}{c c c c} A _ {c} & - B _ {c} L ^ {*} & & \\ K C _ {c} & A _ {1} & - B _ {1} L ^ {*} & - K C _ {O} \end{array} \right] \\ G = \left[ \begin{array}{l l} E _ {C} & 0 \\ 0 & K \end{array} \right] \\ w = \left[ \begin{array}{l} w _ {c} \\ v _ {y} \end{array} \right] \\ \end{array}
$$

Thus,

$$
\operatorname {c o v} \psi = \left[ \begin{array}{l l} \operatorname {c o v} x _ {c} x _ {c} ^ {\prime} & \operatorname {c o v} x _ {c} x _ {t} ^ {\prime} \\ \operatorname {c o v} x _ {t} x _ {c} ^ {\prime} & \operatorname {c o v} x _ {t} x _ {t} ^ {\prime} \end{array} \right] \equiv \Psi \tag {4.29}
$$

is the solution of

$$
\dot {\Psi} = F \Psi + \Psi F ^ {\prime} + G \Omega G ^ {\prime} \tag {4.30}
$$

where

$$
\Omega = \left[ \begin{array}{l l} W _ {C} & 0 \\ 0 & V _ {y} \end{array} \right]
$$

# Pilot Opinion Rating Technique

Hess [18] has formulated a pilot rating technique for the optimal control pilot modeling procedure. The technique has been successfully validated in a variety of tasks [18, 20]. The rating technique can be stated as follows:

If

(1) the indices of performance and model parameters in the optimal control pilot modeling procedure yield a dynamically representative model of the human pilot,

(2) the variables selected for inclusion in the index of performance are directly observable by the pilot,

(3) the weighting coefficients in the index of performance are chosen as the squares of the reciprocals of maximum "allowable" deviations of the respective variables, and these deviations are consonent withthe task as perceived by the pilot. Then

the numerical value of the index of performance resulting from the modeling procedure can be related to the numerical pilot rating which the pilot assigns to the vehicle and task by

P.O.R. = 2.51 ln (10 J) + 0.3 where

P.O.R. = pilot opinion rating on Cooper-Harper scale
J = value of the performance index

# Computational Algorithms

There are two major computer programs developed in this work for predictions of pilot rating and standard deviations of the response variables

for a piloted-aircraft manual control task. A digital computer program STDOCM is a modification and extension of the program PIREP [21] written for operation on CDC-6600 at Wright Patterson Air Force Base to implement the standard optimal control model of the human pilot. A program MODOCM is developed to implement the modified optimal control model of the human pilot which is presented in this chapter. Both programs are written in Fortran IV for operation on IBM system 370/168 at Oklahoma State University and are available from Professor R. L. Swaim, School of Mechanical and Aerospace Engineering, Oklahoma State University.

# CHAPTER V

# EFFECTS OF ELASTIC MODES INTERACTION ON HANDLING QUALITIES

The elastic modes interaction with the rigid body dynamics is introduced to the large flexible aircraft model by parametric lowering of the undamped natural frequencies of the two elastic modes. This will cause controlling the rigid pitch angle by observing the total pitch error to become more difficult as indicated in the past experimental results [8]. The standard optimal control model for the human pilot and modified model presented in Chapter IV are applied to the illustrated cases of varying elastic modes interaction. It will be shown that the standard optimal control model gives the misleading results when there is a severe modes interaction between the elastic modes and the rigid body dynamics. The modified model gives more consistent results with the experimental data on the effects of elastic modes and the rigid body dynamics. The modified model gives more consistent results with the experimental data on the effects of elastic modes interaction on handling qualities and pilot ratings than that of the standard optimal control model. In this chapter the illustrated cases used in the computer simulation study are described. Then the simulation results are presented. Finally, the separation boundary which can be used as an indicator of when the pilot can or cannot visually separate the rigid body motion from the total motion is presented.

# The Illustrated Cases

The ten illustrated cases are obtained from the equations of motion (3.1) in which the natural frequencies of the two elastic modes are parametrically reduced. Dynamic characteristics of each case are specified by four modes: phugoid mode, short period mode, elastic mode 1, and elastic mode 2 as shown in Table III. These ten cases will exemplify most of the situations in which the handling qualities and pilot ratings would be affected differently by the two elastic modes included in the model.

The lowering of the elastic mode natural frequencies resulted in mode interaction which lowered the coupled short-period and phugoid frequencies or made one of them split into positive and negative real roots. A full state feedback control law is used to place the roots of the characteristic equation at precise values for each case. The rigid body dynamics are maintained to be the same as Case 1 and the elastic mode coupled frequencies placed at original values before the state feedback control law was applied. This will ensure that the pilot ratings are based on the relative amplitudes of rigid and elastic pitch angle responses and not on poor rigid body dynamics.

The simulation results on the ten cases by using the standard optimal control model (OCM) for the human pilot and the modified model are shown in Tables IV and V, respectively. These results clearly indicate that when there are severe modes interaction, such as Cases #3, 6 and 9, the standard OCM gave very low pilot ratings predictions which are inconsistent with the experimental results [8]. In contrast the modified OCM gave more consistent results since it includes the visual separation process of the rigid body response from the elastic modes response which the pilot has to accomplish when the amplitude of the high frequency

TABLE III   
NATURAL FREQUENCIES AND DAMPING RATIOS OF TEN CASES   

<table><tr><td>Case #</td><td>ω1 rad/s</td><td>ω2 rad/s</td><td>ωph rad/s</td><td>ζph</td><td>ωsp rad/s</td><td>ζsp</td><td>ω1e rad/s</td><td>ζle</td><td>ω1e rad/s</td><td>ζ2e</td></tr><tr><td>1</td><td>13.59</td><td>21.18</td><td>.0665</td><td>.0312</td><td>2.9334</td><td>.5209</td><td>13.236</td><td>.0497</td><td>21.395</td><td>.02112</td></tr><tr><td>2-</td><td>8</td><td>21.18</td><td>.04614</td><td>.001376</td><td>2.581</td><td>.4992</td><td>7.508</td><td>.1127</td><td>21.390</td><td>.02104</td></tr><tr><td>3</td><td>4</td><td>21.18</td><td>.1412</td><td>.1336</td><td colspan="2">+ 1.652 - 2.266</td><td>4.544</td><td>.3892</td><td>21.380</td><td>.02102</td></tr><tr><td>4</td><td>13.59</td><td>15.00</td><td>.06345</td><td>.02899</td><td>2.889</td><td>.5247</td><td>13.04</td><td>.04508</td><td>15.480</td><td>.03052</td></tr><tr><td>5</td><td>8</td><td>15.00</td><td>.04489</td><td>.001946</td><td>2.586</td><td>.5031</td><td>7.400</td><td>.1073</td><td>15.340</td><td>.02787</td></tr><tr><td>6</td><td>4</td><td>15.00</td><td>.1411</td><td>.134</td><td colspan="2">+ 1.568 - 2.172</td><td>4.356</td><td>.3990</td><td>15.320</td><td>.02761</td></tr><tr><td>7</td><td>13.59</td><td>13.59</td><td>.06203</td><td>.02797</td><td>2.87</td><td>.5262</td><td>12.76</td><td>.03821</td><td>14.380</td><td>.02923</td></tr><tr><td>8</td><td>8</td><td>13.59</td><td>.04433</td><td>.002208</td><td>2.588</td><td>.5048</td><td>7.345</td><td>.1042</td><td>13.990</td><td>.03117</td></tr><tr><td>9</td><td>4</td><td>13.59</td><td>.1411</td><td>.1350</td><td colspan="2">+ 1.527 - 2.126</td><td>4.269</td><td>.4035</td><td>13.970</td><td>.03062</td></tr><tr><td>10</td><td>8</td><td>8</td><td>.03801</td><td>.005574</td><td>2.608</td><td>.5245</td><td>6.403</td><td>.04999</td><td>9.390</td><td>.08138</td></tr></table>

TABLE IV   
PERFORMANCE PREDICTION BY THE STANDARD OCM   

<table><tr><td>CASE #</td><td>θ rms (deg)</td><td>δ rms (deg/s)</td><td>δ rms (rad x 103)</td><td>P. O. R.</td></tr><tr><td>1</td><td>.3895</td><td>1.650</td><td>1.143</td><td>1.0</td></tr><tr><td>2</td><td>.5422</td><td>2.343</td><td>2.475</td><td>2.6</td></tr><tr><td>3</td><td>.5042</td><td>1.573</td><td>2.234</td><td>1.0</td></tr><tr><td>4</td><td>.3612</td><td>0.917</td><td>0.910</td><td>1.0</td></tr><tr><td>5</td><td>.5096</td><td>2.335</td><td>2.266</td><td>2.5</td></tr><tr><td>6</td><td>.4604</td><td>1.721</td><td>2.061</td><td>1.2</td></tr><tr><td>7</td><td>.3437</td><td>1.127</td><td>1.392</td><td>1.0</td></tr><tr><td>8</td><td>.4955</td><td>2.288</td><td>2.142</td><td>2.4</td></tr><tr><td>9</td><td>.4445</td><td>1.750</td><td>2.000</td><td>1.2</td></tr><tr><td>10</td><td>.3833</td><td>1.591</td><td>2.810</td><td>1.0</td></tr></table>

TABLE V   
PERFORMANCE PREDICTION BY THE MODIFIED OCM   

<table><tr><td>CASE #</td><td>θ rms(deg)</td><td>δ rms(deg/s)</td><td>δ rms(rad x 103)</td><td>P.O.R.</td></tr><tr><td>1</td><td>.3663</td><td>1.848</td><td>0.829</td><td>1.2</td></tr><tr><td>2</td><td>.5724</td><td>2.832</td><td>1.199</td><td>3.3</td></tr><tr><td>3</td><td>.8123</td><td>3.721</td><td>1.014</td><td>4.7</td></tr><tr><td>4</td><td>.3157</td><td>0.999</td><td>1.024</td><td>1.0</td></tr><tr><td>5</td><td>.5345</td><td>2.746</td><td>1.195</td><td>3.2</td></tr><tr><td>6</td><td>.7374</td><td>3.470</td><td>0.872</td><td>4.3</td></tr><tr><td>7</td><td>.3228</td><td>1.428</td><td>0.869</td><td>1.0</td></tr><tr><td>8</td><td>.5172</td><td>2.657</td><td>1.181</td><td>3.0</td></tr><tr><td>9</td><td>.7043</td><td>3.360</td><td>0.833</td><td>4.1</td></tr><tr><td>10</td><td>.4187</td><td>2.091</td><td>1.167</td><td>1.8</td></tr></table>

elastic modes is getting larger. On the other hand, when the modes interaction are small, both pilot modeling techniques gave almost the same predictions.

# The Separation Boundary

The separation boundary is defined as the limit of when the pilot can or cannot visually separate the rigid body motion from the total motion. The visual separation is essential in controlling the rigid pitch angle or other rigid body parameter of the elastic airplane when only the total pitch angle response or a corresponding parameter is available to the pilot.

From Chapter IV, two kinds of pilot modeling techniques are discussed. The standard OCM is the pilot model that assumed that the pilot has the perfect internal model of the aircraft/disturbance dynamics. This model will give the best possible pilot opinion rating (P.O.R.) in any tracking task. The other model, the modified OCM, is the one with a slowly varying internal model. In this model, the pilot is assumed to be able to completely separate the slowly varying or the rigid body motion from the total motion. The difference between the P.O.R.'s, i.e., $\Delta P.O.R.$ , of 2 is chosen to be a separation boundary. That is if $\Delta P.O.R.$ is greater than or equal to 2, the pilot cannot visually separate the rigid body motion from the elastic motion in the display.

It is known that the pilot opinion rating depends on many factors such as the intensity of turbulence and the level of difficulty of the task. To study the modes interaction effect all other effects should be kept at their nominal values. That is without severe modes interaction effect the other parameters should be set such that P.O.R. is equal to 1. Once the P.O.R. has been initialized for some specific task, the separation

boundary can be found from the P.O.R. prediction of the modified OCM alone. This is because the standard OCM will give almost unity P.O.R. in the severe modes interaction cases, if the rigid body dynamics have been maintained at the known good handling qualities specifications. So, instead of using $\Delta P.O.R. = 2$ as the separation boundary, the modified OCM's P.O.R. of 3 can be equally well used as the separation boundary provided the proper initialization mentioned above has been done.

# CHAPTER VI

# CONCLUSIONS AND RECOMMENDATIONS

A model for the human pilot in a manual control task using the optimal control techniques has been developed for predicting the handling qualities or the pilot ratings of a large flexible aircraft where the elastic modes interaction with the rigid body dynamics is significant. The separation boundary concept, which will tell when the pilot can or cannot visually separate the rigid body motion from the elastic one, has been introduced. The techniques developed here make it easier to investigate the modes interaction effect on the handling qualities in a preliminary design stage before the first prototype has been built. If the handling qualities are severely affected by the elastic modes interaction with the rigid body dynamics, the elastic modes suppression control system should be designed and implemented along with the stability augmentation system of the rigid body dynamics.

A comparison of the model predictions with the past experimental data shows that the modified optimal control model for the human pilot developed here is much better in predicting the elastic modes effect on the handling qualities than the standard optimal control model. This is due to the fact that the mode decomposition mechanism has been incorporated into the modified model.

However, only one longitudinal trim flight condition was investigated, its validity for different flight conditions can only be confirmed by conducting more investigations.

Future work should also include the computational aspect of the model. In the pilot model parameters identification, it is required to solve an $(\eta_{a} + \eta_{s} + 4) \times (\eta_{a} + \eta_{s} + 4)$ matrix equation (4.30) for the modified model instead of solving an $(\eta_{a} + 1) \times (\eta_{a} + 1)$ matrix equation in the standard OCM, where $\eta_{a}$ , dimension of an aircraft/disturbance dynamics, is 12; $\eta_{s}$ , dimension of a slowly varying part of the aircraft/disturbance dynamics, is 8. This will risk the numerical instability when one has to include more elastic modes in the aircraft/disturbance dynamics. An alternative structure of the pilot model should be explored to ease the computational burden of the high order aircraft/disturbance system.

# SELECTED BIBLIOGRAPHY

(1) Chalk, C.R. et al. Background Information and User Guide for Mil-8785B (ASG), Military Specification-Flying Qualities of Piloted Airplanes. AFFDL-TR-69-72, Air Force Flight Dynamics Laboratory, Wright-Patterson AFB, Ohio, 1969.   
(2) Lyon, H. M. A Method for Estimation the Effect of Aeroelastic Distortion of a Sweptback Wing on Stability and Control Derivatives. Aeronautical Research Council, Report and Memoranda No. 2331, London, 1946.   
(3) McCarthy, J.F., and Kirsch, A.A. Effect of Structural Flexibility on Aircraft Loading. WADC TR 6385, Wright Air Development Center, Wright-Patterson AFB, Ohio, 1953.   
(4) Milne, R.D. Dynamics of Deformable Airplane. Aeronautical Research Council Report and Memoranda No. 3345, London, 1964.   
(5) Howard, V.W. The Effects of Structural Elasticity on Aircraft Control Systems. WADC TR 56-166, Wright Air Development Center, Wright-Patterson AFB, Ohio, 1956.   
(6) Dornfeld, G.M. et al. A Method for Predicting the Stability Characteristics of an Elastic Airplane, Vol. 1, 2, 3, Flexstab 3.01.00, AFFDL-TR-77-55, Air Force Flight Dynamics Laboratory Wright-Patterson AFB, Ohio, 1977.   
(7) Roskam, J. Flight Dynamics of Rigid and Elastic Airplanes. Roskam Aviation and Engineering Corporation, Lawrence, Kansas, 1979.   
(8) Yen, W.Y. "Effects of Dynamic Aeroelasticity on Handling Qualities and Pilot Rating." (Unpublished Ph.D. Thesis, Purdue University, 1977.)   
(9) Kleinman, D.L., Baron, S., and Levison, W.H. "Acontrol Theoretic Approach to Manned Vehicle Systems Analysis." IEEE Trans. on Automatic Control, Vol. AC-16, No. 6 (Dec., 1971), pp. 824-832.   
(10) Crother, C.A., Gabelman, B., and Langton D. Structural Mode Effects on Flying Qualities in Turbulence. AFFDL-TR-73-88, Air Force Flight Dynamics Laboratory, Wright-Patterson AFB, Ohio, 1973.

(11) Wykes, J.H. B-1 Flexible Vehicle Equations of Motion for Ride Quality, Terrain Following, and Handling Qualities Studies. Internal Document TFD-71-430-1, North American Rockwell, Los Angeles, CA, 1973.   
(12) Roberts, P.A. "Effects of Control Laws and Relaxed Static Stability on Vertical Ride Quality of Flexible Aircraft." (Unpublished Ph.D. Thesis, Purdue University, 1976.)   
(13) Taylor, A.S., and Woodcock, D.L. The Dynamics of Deformable Aircraft. Aeronautical Research Council, Report and Memoranda No. 3776, London, 1976.   
(14) Swaim, R.L., and Fullman, D.G. "Prediction of Elastic Airplane Longitudinal Dynamics from Rigid-body Aerodynamics." Journal of Aircraft, Vol. 14, No. 9 (1977), pp. 868-873.   
(15) Baron, S. "A Brief Overview of the Theory and Application of the Optimal Control Model of the Human Operator." Edited by M.C. Waller: Models of Human Operators in Vision Dependent Tasks. NASA Conference Publication 2103, 1979.   
(16) Velduyzen, W., and Stassen, H.G. "The Internal Model Concept: An Application to Modeling Human Control of Large Ships." Human Factors, Vol. 19, No. 4 (1977), pp. 367-380.   
(17) Baron, S., and Berliner, J. MANMOD 1975: Human Internal Models and Scene-Perception Models. Army Missile Research, Development and Engineering, Redstone Arsenal, Alabama, 1975.   
(18) Hess, R.A. "Prediction of Pilot Ratings Using an Optimal Pilot Model." Human Factors, Vol. 19, No. 5 (1977), pp. 459-475.   
(19) Stengel, R.F., Taylor, J.H., Broussard, J.R., and Berry, P.W. High Angle of Attack Stability and Control. ONE-CR215-273-1, The Office of Naval Research, 1976.   
(20) Schmidt, D.K. Unified Synthesis of Manual and Automatic Control. Applied to Integrated Fire and Flight Control. AFFDL-TM-78-105-FGC, Wright-Patterson Air Force Base, Ohio, 1978.   
(21) Curry, R.E., Hoffman, W.C., and Young, L.R. Pilot Modeling for Manned Simulation. AFFDL-TR-76-124, Air Force Flight Dynamics Laboratory, Wright-Patterson AFB, Ohio, 1976.   
(22) Chow, J.H., Allemong, J.J., and Kokotovic, P.V. "Singular Perturbation Analysis of Systmes with Sustained High Frequency Oscillation." Automatica, Vol. 14 (1978), pp. 271-279.   
(23) Haddad, A.H. "Linear Filtering of Singularity Perturbed Systems." IEEE Trans, Automat. Control, Vol. AC-21 (1976), pp. 515-519.

(24) Chow, J.H., and Kokotovic, P.V. "A Decomposition of Near-Optimum Regulators for Systems with Slow and Fast Modes." IEE Trans, Automat. Control, Vol. AC-21 (1976), pp. 701-705.

# APPENDIX A

# NUMERICAL VALUES OF STABILITY DERIVATIVES

# AND EQUATIONS OF MOTION

The low level penetration flight condition for the B-1 was supplied by the B-1 System Program Office at Wright-Patterson AFB from Rockwell International unclassified documents. The stability derivatives used in equations (3.1) were based on preliminary aerodynamic analyses, but closely representative of the vehicle that has been flying. The relations between dimensional force and moment and elastic force derivatives as a function of nondimensional stability derivatives are given in Table VI and VII, respectively. The non-dimensional stability derivative values for the unaugmented vehicle are given in Table VIII. The gust specifications for the study vehicle are given in Table IX. Finally, the $A_{11}, A_{12}, A_{21} / \mu, A_{22} / \mu, B_1, B_2 / \mu, C_1, C_2$ and $E_1$ matrices for the unaugmented airplane are given in Tables X to XVIII, respectively. The matrices $E_2$ and D are zero matrices and the matrices $A_a, B_a, C_a$ and $E_a$ are defined as follows:

$$
A _ {a} \equiv \left[ \begin{array}{l l} A _ {1 1} & A _ {1 2} \\ A _ {2 1 / \mu} & A _ {2 2 / \mu} \end{array} \right]
$$

$$
B _ {a} \equiv \left[ \begin{array}{l} B _ {1} \\ B _ {2 / \mu} \end{array} \right]
$$

$$
\mathrm {C} _ {\mathbf {a}} \equiv [ \mathrm {C} _ {1} \quad \mathrm {C} _ {2} ]
$$

$$
\mathrm {E _ {a}} \equiv \left[ \begin{array}{c} \mathrm {F _ {1}} \\ \mathrm {E _ {2 / u}} \end{array} \right]
$$

# TABLE VI

# DIMENSIONAL FORCE AND MOMENT DERIVATIVES AS A FUNCTION OF NON-DIMENSIONAL STABILITY DERIVATIVES

<table><tr><td>a1= ρU02S/2</td><td colspan="2">a2=a1c/2U0</td></tr><tr><td>Xu=a1Cx/u</td><td>Zu=a1Cz/u</td><td>Mu=a1Cm/u</td></tr><tr><td>Xα=a1Cxα</td><td>Zα=a1Czα</td><td>Ma=a1Cmα</td></tr><tr><td>Xα=a2Cxα</td><td>Zα=a2Czα</td><td>Ma=a2Cmα</td></tr><tr><td>Xθ=a2Cxθ</td><td>Zθ=a2Czθ</td><td>Mθ=a2Cmθ</td></tr><tr><td>Xδe=a1Cxδe</td><td>Zδe=a1Czδe</td><td>Mδe=a1Cmδe</td></tr><tr><td>Xδe=1</td><td>Zδe=a1Czδe</td><td>Mδe=a1Cmδe</td></tr><tr><td>Xδt=1</td><td>Zδt=0</td><td>Mδt=0</td></tr><tr><td>Xξ1=a1Cxξ1</td><td>Zξ1=a1Czξ1</td><td>Mξ1=a1Cmξ1</td></tr><tr><td>Xξ1=a1Cxξ1/u</td><td>Zξ1=a1Czξ1/u</td><td>Mξ1=a1Cmξ1/u</td></tr><tr><td>Xξ2=a1Cxξ2</td><td>Zξ2=a1Czξ2</td><td>Mξ2=a1Cmξ2</td></tr><tr><td>Xξ2=a1Cxξ2/u</td><td>Zξ2=a1Czξ2/u</td><td>Mξ2=a1Cmξ2/u</td></tr></table>

# TABLE VII

# DIMENSIONAL ELASTIC FORCE DERIVATIVES

# AS A FUNCTION OF NON-DIMENSIONAL

# STABILITY DERIVATIVES

$$
a _ {1} = \rho U _ {0} ^ {2} S / 2 \quad a _ {2} = a _ {1} c / 2 U _ {0}
$$

$$
Q _ {\xi_ {1 \alpha}} = a _ {1} C _ {\xi_ {1 \alpha}} \quad Q _ {\xi_ {2 \alpha}} = a _ {1} C _ {\xi_ {2 \alpha}}
$$

$$
\mathrm {Q} _ {\xi_ {1 \dot {\alpha}}} = \mathrm {a} _ {2} \mathrm {C} _ {\xi_ {1 \dot {\alpha}}} \quad \mathrm {Q} _ {\xi_ {2 \dot {\alpha}}} = \mathrm {a} _ {2} \mathrm {C} _ {\xi_ {2 \dot {\alpha}}}
$$

$$
\mathrm {Q} _ {\xi_ {1 \dot {\theta}}} = \mathrm {a} _ {2} \mathrm {C} _ {\xi_ {1 \dot {\theta}}} \quad \mathrm {Q} _ {\xi_ {2 \dot {\theta}}} = \mathrm {a} _ {2} \mathrm {C} _ {\xi_ {2 \dot {\theta}}}
$$

$$
\begin{array}{l} Q _ {\xi_ {1}} = a _ {1} C _ {\xi_ {1}} \\ \hline \xi_ {1} & \end{array} \qquad \qquad \qquad \begin{array}{l} Q _ {\xi_ {2}} = a _ {1} C _ {\xi_ {2}} \\ \hline \xi_ {1} & \end{array}
$$

$$
Q _ {\xi_ {1} \dot {\xi} _ {2}} = a _ {1} C _ {\xi_ {1} \dot {\xi} _ {2}} / U _ {0} \quad Q _ {\xi_ {2} \dot {\xi} _ {2}} = a _ {1} C _ {\xi_ {2} \dot {\xi} _ {2}} / U _ {0}
$$

$$
Q _ {\xi_ {1} \xi_ {2}} = a _ {1} C _ {\xi_ {1} \xi_ {2}} \quad Q _ {\xi_ {2} \xi_ {2}} = a _ {1} C _ {\xi_ {2} \xi_ {2}}
$$

$$
\begin{array}{l} Q _ {\xi_ {1 \xi_ {2}}} = a _ {1} C _ {\xi_ {1 \xi_ {2}}} / U _ {0} \\ Q _ {\xi_ {2 \xi_ {2}}} = a _ {1} C _ {\xi_ {2 \xi_ {2}}} / U _ {0} \end{array}
$$

$$
\begin{array}{c} Q _ {\xi_ {1 \delta} = a _ {1} C _ {\xi_ {1 \delta}}} \\ e \end{array} Q _ {\xi_ {2 \delta} = a _ {1} C _ {\xi_ {2 \delta}}}
$$

TABLE VIII   
STABILITY DERIVATIVES FOR B-1 BOMBER  
IN MAC10.85 FLIGHT CONDITION  

<table><tr><td>Cxu = -0.08066</td><td>Czu = -1.9659</td><td>Cmu = -0.4546</td></tr><tr><td>Cxα = -0.08500</td><td>Czα = -3.9367</td><td>Cma = -1.41052</td></tr><tr><td>Cxα = 0</td><td>Czα = -5.0</td><td>Cmα = -11.005</td></tr><tr><td>Cxθ = 0</td><td>Czθ = 17.8558</td><td>Cmθ = -35.7556</td></tr><tr><td>Cxδe = 0</td><td>Czδe = -0.9426</td><td>Cmδe = -2.799</td></tr><tr><td>Cxξ1 = 0</td><td>Czξ1 = -0.02922</td><td>Cmξ1 = -0.0348</td></tr><tr><td>Cxξ1 = 0</td><td>Czξ1 = -0.6592</td><td>Cmξ1 = -1.32169</td></tr><tr><td>Cxξ2 = 0</td><td>Czξ2 = 0.015</td><td>Cmξ2 = 0.03787</td></tr><tr><td>Cxξ2 = 0</td><td>Czξ2 = 0.4733</td><td>Cmξ2 = 1.233</td></tr><tr><td>Cξ1α = -0.06478</td><td>Cξ1α = 0.48975</td><td></td></tr><tr><td>Cξ1α = 0.02469</td><td>Cξ1α = 0.48779</td><td></td></tr><tr><td>Cξ1θ = -1.47658</td><td>Cξ1θ = 3.97547</td><td></td></tr><tr><td>Cξ1ξ1 = 0.00064</td><td>Cξ2ξ1 = 0.00451</td><td></td></tr></table>

TABLE VIII (Continued)   
TABLE IX   

<table><tr><td>Cξ1ξ1= -0.07243</td><td>Cξ2ξ1= -0.07333</td></tr><tr><td>Cξ1ξ2= -0.0014</td><td>Cξ2ξ2= -0.0051</td></tr><tr><td>Cξ1ξ2= 0.0765</td><td>Cξ2ξ2= -0.2588</td></tr><tr><td>Cξ1δe= -0.19635</td><td>Cξ2δe= 0.3939</td></tr></table>

GUST SPECIFICATIONS   

<table><tr><td>Parameters</td><td>Value</td></tr><tr><td>σw</td><td>6 fps</td></tr><tr><td>σu</td><td>10.8 fps</td></tr><tr><td>Lw</td><td>300 ft</td></tr><tr><td>Lu</td><td>970 ft</td></tr><tr><td>Uo</td><td>979 fps</td></tr><tr><td>bw</td><td>136.68 ft</td></tr></table>

TABLE X   
A11 MATRIX   

<table><tr><td>-.9777</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>-3.1633</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>-.02604</td><td>-3.1633</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>-.142</td><td>-17.25028</td><td>-5.4532</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-.025</td><td>0</td><td>-25.0000</td><td>0</td><td>-.025</td><td>-25.0</td><td>-32.2</td><td>0</td></tr><tr><td>-6.3408 x 10-4</td><td>0</td><td>-1.205</td><td>5.6506 x 10-2</td><td>-.63408 x 10-4</td><td>-1.205</td><td>0</td><td>1.03178</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1.0</td></tr><tr><td>-2.292 x 10-3</td><td>0</td><td>-7.0672</td><td>-1.1112</td><td>-2.292 x 10-3</td><td>-7.0672</td><td>0</td><td>-2.06314</td></tr></table>

TABLE XI   
A12 MATRIX   

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-8.944 x 10-3</td><td>4.591 x 10-3</td><td>-2.1262 x 10-4</td><td>1.5266 x 10-4</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-.1844</td><td>.20762</td><td>-70449 x 10-3</td><td>6.9711 x 10-3</td></tr></table>

TABLE XII   
A21/MATRIX   

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>-1.4343x10-3</td><td>0</td><td>-737.04</td><td>-137.51</td><td>-1.4353x10-3</td><td>-738.04</td><td>0</td><td>-133.038</td></tr><tr><td>-3.9012x10-3</td><td>0</td><td>752.39</td><td>44.3375</td><td>-3.9017x10-3</td><td>757.39</td><td>0</td><td>56.4903</td></tr></table>

TABLEXIII   
A22/MATRIX   

<table><tr><td>0</td><td>0</td><td>1.0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>1.0</td></tr><tr><td>-177.444</td><td>61.8964</td><td>-1.139</td><td>.91536</td></tr><tr><td>6.98597</td><td>-456.528</td><td>-.121926</td><td>-.849</td></tr></table>

TABLE XIV   
B1 MATRIX   

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>-.28852</td><td>0</td><td>-15.465</td></tr></table>

TABLE: XV   
B. $\mu$ MATRIX   

<table><tr><td>0</td><td>0</td><td>-2229.4</td><td>613.343</td></tr></table>

TABLE XVI   
C1 MATRIX   

<table><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>57.2958</td><td>0</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>57.2958</td></tr></table>

TABLE XVII   
CMATRIX   

<table><tr><td>-1.4324</td><td>-1.66158</td><td>0</td><td>0</td></tr><tr><td>0</td><td>0</td><td>-1.4324</td><td>-1.66158</td></tr></table>

TABLE XVIII   
$\mathbf{E}_1^{\prime}$ MATRIX   

<table><tr><td>5.088</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>.01948</td><td>.10621</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

# APPENDIX B

# DERIVATIONS RELATED TO SINGULAR PERTURBATION

Consider a singularly perturbed linear time-invariant system

$$
\dot {x} _ {1} = A _ {1 1} x _ {1} + A _ {1 2} x _ {2} + B _ {1} u + E _ {1} w, x _ {1} (0) = x _ {1 0} \tag {A.1a}
$$

$$
\mu \dot {x} _ {2} = A _ {2 1} x _ {1} + A _ {2 2} x _ {2} + B _ {2} u + E _ {2} w, x _ {2} (o) = x _ {2 0} \tag {A.1b}
$$

$$
y = C _ {1} x _ {1} + C _ {2} x _ {2} + v \tag {A.1c}
$$

where $x_1, x_2$ , and $y$ are $n_1, n_2$ and $m$ dimensional vectors respectively, the control $u$ is an $r$ vector, and $\mu > 0$ is a small scalar parameter which arises due to the presence of high frequency elastic modes. The covariances of the $p$ and $q$ dimensional white noise vectors $w$ and $v$ are

$$
E \{w (t) w ^ {\prime} (\tau) \} = W \delta (t - \tau)
$$

$$
E \left\{\mathbf {w} (t) \quad \mathbf {v} ^ {\prime} (\tau) \right\} = 0
$$

$$
E \left\{v (t) v ^ {\prime} (\tau) \right\} = V \delta (t - \tau)
$$

Given the observation $y(\tau)$ for $0 < \tau < \infty$ , it is desired to estimate $x_1(t)$ which is a slowly varying dynamics vector of the system (A.1).

The conditions that guarantee that high frequency oscillations will occur are $\mathfrak{n}_2$ is even and $\Lambda_{22}$ has the form [22]

$$
A _ {2 2} = \left[ \begin{array}{l l} \mu D _ {1} & D _ {2} \\ D _ {3} & \mu D _ {4} \end{array} \right]
$$

where $D_2, D_3$ are $n_2/2 \times n_2/2$ nonsingular matrices and the matrix $D_2D_3$ has simple and negative eigenvalues $-\omega_i^2$ , $i = 1, 2, \ldots, n_2/2$ .

By using the techniques presented in [22-24] it will be shown that in the limit $(\mu + 0^{+})x_{2}$ can be approximated as a white noise process which can be used as an input to the slow mode $x_{1}$ . Then the estimation of $x_{1}(t)$ by ignoring the high frequency oscillations can be analytically represented by the filtering of a reduced order system.

If $\mu$ in (A.1b) is neglected and (A.1b) is replaced by

$$
0 = A _ {2 1} \bar {x} _ {1} + A _ {2 2} \bar {x} _ {2} + B _ {2} \bar {u} + E _ {2} w
$$

then, if $\mathsf{A}_{22}^{-1}$ exists,

$$
\bar {x} _ {2} = - A _ {2 2} ^ {- 1} \left(A _ {2 1} \bar {x} _ {1} + B _ {2} \bar {u} + E _ {2} w\right)
$$

and the substitution of $\bar{\mathbf{x}}_2$ in (A.1a) results in the reduced order system

$$
\dot {\bar {x}} _ {1} = A _ {o} \bar {x} _ {1} + B _ {o} \bar {u} + E _ {o} w \tag {A.3a}
$$

$$
\bar {y} = C _ {o} \bar {x} _ {1} + D _ {o} \bar {u} + F _ {o} w + v \tag {A.3b}
$$

where

$$
A _ {0} = A _ {1 1} - A _ {1 2} A _ {2 2} ^ {- 1} A _ {2 1}
$$

$$
B _ {O} = B _ {1} - A _ {1 2} A _ {2 2} ^ {- 1} B _ {2}
$$

$$
E _ {0} = E _ {1} - A _ {1 2} A _ {2 2} ^ {- 1} E _ {2}
$$

$$
C _ {o} = C _ {1} - C _ {2} A _ {2 2} ^ {- 1} A _ {2 1}
$$

$$
D _ {o} = - C _ {2} A _ {2 2} ^ {- 1} B _ {2}
$$

$$
F _ {o} = - C _ {2} A _ {2 2} ^ {- 1} E _ {2}
$$

without any input, the slowly varying part of $x_2$ is $\bar{x}_2 = -A_{22}^{-1} A_{21} \bar{x}_1$ . To separate $\bar{x}_2$ from the highly oscillatory part of $x_2$ , a change of variable is used.

$$
n = x _ {2} + A _ {2 2} ^ {- 1} A _ {2 1} x _ {1} + \mu G x _ {1} = x _ {2} + L x _ {1} \tag {A.4}
$$

transforming (A.1) into

$$
\dot {x} _ {1} = \left(A _ {0} - \mu A _ {1 2} G\right) x _ {1} + A _ {1 2} n + B _ {1} u + E _ {1} w
$$

$$
\mu \dot {n} = F x _ {1} + (A _ {2 2} + \mu L A _ {1 2}) n + (B _ {2} + \mu L B _ {1}) \mu + (E _ {2} + \mu L E _ {1}) w
$$

where

$$
F = \mu \left(A _ {2 2} ^ {- 1} A _ {2 1} + \mu G\right) \left(A _ {0} - \mu A _ {1 2} G\right) - \mu A _ {2 2} G
$$

The solution of $\mathbf{F} = 0$ is

$$
G = A _ {2 2} ^ {- 2} A _ {2 1} A _ {0} + 0 (\mu)
$$

To separate the slow modes, introduce

$$
\zeta = x _ {1} - \mu \left(A _ {1 2} A _ {2 2} ^ {- 1} + \mu M\right) n \equiv x _ {1} - \mu H n \tag {A.5}
$$

and choose M such that

$$
A _ {1 2} + \mu (A _ {0} - \mu A _ {1 2} G) H - H (A _ {2 2} + \mu L A _ {1 2}) = 0
$$

so

$$
M = A _ {0} A _ {1 2} A _ {2 2} ^ {- 2} - A _ {1 2} A _ {2 2} ^ {- 2} A _ {2 1} A _ {1 2} A _ {2 2} ^ {- 1} + O (\mu)
$$

The transformation (A.4) and (A.5) can be written as

$$
\left[ \begin{array}{l} \zeta \\ n \end{array} \right] = \left[ \begin{array}{c c c} I _ {n} & - & \mu H L \\ & L & \\ & & I _ {m} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \tag {A.6}
$$

The original system (A.1) is finally transformed into

$$
\dot {\zeta} = A _ {0} \zeta + B _ {0} u + E _ {0} w \tag {A.7a}
$$

$$
\mu \dot {\eta} = A _ {2} \eta + B _ {2} u + E _ {2} w \tag {A.7b}
$$

$$
y = C _ {0} \zeta + C _ {2} n + v \tag {A.7c}
$$

where

$$
A _ {o} = A _ {o} - \mu A _ {1 2} G \simeq A _ {o} + O (\mu)
$$

$$
B _ {0} = B _ {0} - \mu \left(H L B _ {1} = M B _ {2}\right) \approx B _ {0} - 0 (\mu)
$$

$$
E _ {0} = E _ {0} - \mu \left(H L B _ {1} + M E _ {2}\right) \approx E _ {0} - 0 (\mu)
$$

$$
A _ {2} = A _ {2 2} + \mu L A _ {1 2} = A _ {2 2} + 0 (\mu)
$$

$$
B _ {2} = B _ {2} + \mu L B _ {1} \simeq B _ {2} + 0 (\mu)
$$

$$
E _ {2} = E _ {2} + \mu L E _ {1} \simeq E _ {2} + 0 (\mu)
$$

$$
C _ {0} = C _ {1} - C _ {2} L \approx C _ {0} + 0 (\mu)
$$

$$
C _ {2} = C _ {2} + \mu \left(C _ {1} - C _ {2}\right) H = C _ {2} + O (\mu)
$$

To investigate the behavior of $\mathfrak{n}(t)$ , we assume that (A.7b) can be written as

$$
\mu \dot {\eta} = A _ {2} \eta + E _ {2} w \tag {A.8}
$$

That is, $\mathfrak{u}$ has been replaced by the feedback control before applying the transformation to get (A.7)

Let $\tau = \frac{t - t_0}{\mu}$ , then (A.8) becomes

$$
\frac {d}{d \tau} n = A _ {2} n + E _ {2} w
$$

where $w$ in the $\tau$ -scale has covariance $W / \mu$ instead of $W$ in the $t$ -scale. Consequently the covariance of the process $n(\tau)$ would also have the form $V / \mu$ where $V$ satisfies the eqn.

$$
\frac {\mathrm {d}}{\mathrm {d} \tau} V = A _ {2} V + V A _ {2} ^ {-} + E _ {2} W E _ {2} ^ {-}
$$

with steady state value $V$ satisfying

$$
0 = A _ {2} V _ {\infty} + V _ {\infty} A _ {2} ^ {\prime} + E _ {2} W E _ {2} ^ {\prime}
$$

If $A_{2}$ is stable and given an arbitrary $\epsilon > 0$ , then there exists $\mu^{\star} > 0$ and $t_{1} > 0$ such that $||V(t) - V_{\infty}|| < \epsilon$ for all $t \geqslant t_{1}$ and $0 < \mu < \mu^{\star}$ . Therefore, for $t > t_{1}$ , $\eta(t)$ may be approximated by a stationary stochastic process with the autocorrelation function

$$
R _ {\eta} (t ^ {\prime}; t ^ {\prime \prime}) = E \left\{\left(t ^ {\prime}\right) \left(t ^ {\prime \prime}\right) \right\} = \frac {V _ {\infty}}{\mu} \exp \left[ A _ {2} \frac {\left(t ^ {\prime} - t ^ {\prime \prime}\right)}{\mu} \right], t <   t ^ {\prime}
$$

However, $R_{n}(t^{\prime}, t^{\prime \prime}) \to 0$ as $\mu \to 0$ for $t^{\prime} \neq t^{\prime \prime}$ , and

$$
\lim  _ {\mu \rightarrow 0} f _ {t - E} ^ {t - E} R _ {\eta} \left(t ^ {\prime} - t ^ {\prime \prime}\right) d t ^ {\prime \prime} = - A _ {2} ^ {- 1} \bar {V} - \bar {M} _ {2} ^ {- 1}
$$

where

$$
V _ {\infty} = \bar {V} + 0 (\mu)
$$

so that $\bar{\mathbf{V}}$ satisfies

$$
A _ {2 2} \bar {V} + \bar {V} A _ {2 2} ^ {\prime} + E _ {2} W E _ {2} ^ {\prime} = 0
$$

It follows that in the limit $\mathfrak{n}$ becomes a white noise process with covariance

$$
\begin{array}{l} \lim  _ {\mu \rightarrow 0} R _ {n} (t ^ {\prime}, t ^ {\prime \prime}) = - (\Lambda_ {2 2} ^ {- 1} \bar {V} + \bar {V} \Lambda_ {2 2} ^ {- 1}) \delta (t ^ {\prime} - t ^ {\prime \prime}) \\ = \left(A _ {2 2} ^ {- 1} E _ {2} W F _ {2} ^ {\prime} A _ {2 2} ^ {- 1}\right) \delta \left(t ^ {\prime} - t ^ {\prime \prime}\right) \\ \end{array}
$$

which is the covariance of the process

$$
\bar {n} = A _ {2 2} ^ {- 1} E _ {2} W \simeq A _ {2} ^ {- 1} E _ {2} W
$$

obtained by the formal substitution of $\mu = 0$ in (A.8).

The estimation equation for the slow mode is

$$
\dot {\hat {\zeta}} = A _ {0} \hat {\zeta} + K _ {0} [ \bar {y} - C _ {0} \hat {\zeta} ]
$$

Since the inverse of (A.6) is

$$
\left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] = \left[ \begin{array}{c c c} I _ {n} & & \mu H \\ - L & & I _ {m} - \mu L H \end{array} \right] \left[ \begin{array}{l} \zeta \\ n \end{array} \right]
$$

So the filtered estimate of $\mathbf{x}_1$ and $\mathbf{x}_2$ are given as

$$
\hat {x} _ {1} = \hat {\zeta} - \mu H \hat {\eta} = \hat {\zeta}
$$

$$
\hat {x} _ {2} = - L \hat {\zeta} + (I - \mu I H) \hat {n}
$$

Since $A_0 = A_0 + 0(\mu)$ , $B_0 = B_0 + 0(\mu), \ldots,$ so

$$
\hat {\mathbf {x}} _ {1} = \hat {\mathbf {x}} _ {1} + 0 (\mu)
$$

where $\hat{\mathbf{x}}$ are the estimates obtained by solving the filtering problem for the reduced system (A.3).

VITA

Supat Poopaka

Candidate for the Degree of

Doctor of Philosophy

Thesis: HANDLING QUALITIES OF LARGE FLEXIBLE AIRCRAFT

Major Field: Mechanical Engineering

Biographical:

Personal Data: Born in

the son of Mr. Somboon and Mrs. Pannee Poopaka.

Education: Graduated from Benjamaborpit High School, Bangkok, Thailand, in 1968; received Bachelor of Science degree in Mechanical Engineering from Prince of Songkla University, Haadyai, Thailand, in 1972; received Master of Science degree in Mechanical Engineering from University of Illinois, Urbana, Illinois, in 1977; completed the requirements for the Doctor of Philosophy degree at Oklahoma State University in December, 1980.

Professional Experience: Teaching assistant, Mechanical Engineering Department, Prince of Songkla University, 1972-1975; graduate research assistant, School of Mechanical and Aerospace Engineering, Oklahoma State University, 1979 to July 1980; King Mongkut Institute of Technology, Bangkok, Thailand, from 1975 to date (on leave).

End of Document
