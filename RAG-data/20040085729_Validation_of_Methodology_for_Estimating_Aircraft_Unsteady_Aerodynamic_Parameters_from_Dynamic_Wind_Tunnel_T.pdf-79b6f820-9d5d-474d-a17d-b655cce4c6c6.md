# VALIDATION OF METHODOLOGY FOR ESTIMATING AIRCRAFT UNSTEADYAERODYNAMIC PARAMETERS FROM DYNAMIC WIND TUNNEL TESTS

Patrick C. Murphy*

NASA Langley Research Center

Hampton, Virginia USA 23681 – 2199

Vladislav Klein†

The George Washington University

NASA Langley Research Center

Hampton, Virginia USA 23681 – 2199

# Abstract

A basic problem in flight dynamics is the mathematical formulation of the aerodynamic model for aircraft. This study is part of an ongoing effort at NASA Langley to develop a more general formulation of the aerodynamic model for aircraft that includes nonlinear unsteady aerodynamics and to develop appropriate test techniques that facilitate identification of these models. A methodology for modeling and testing using wide-band inputs to estimate the unsteady form of the aircraft aerodynamic model was developed previously but advanced test facilities were not available at that time to allow complete validation of the methodology. The new model formulation retained the conventional static and rotary dynamic terms but replaced conventional acceleration terms with more general indicial functions. In this study advanced testing techniques were utilized to validate the new methodology for modeling. Results of static, conventional forced oscillation, wide-band forced oscillation, oscillatory coning, and ramp tests are presented.

# Nomenclature

Only the main symbols are introduced here; other symbols are defined in the paper.

A, B, C numerator transfer function coefficients

b wing span, m

$a , \mathbf { b } _ { 1 }$ , c indicial function parameters

$\bar { c }$ mean aerodynamic chord, m

CL, CN lift and normal force coefficient

Cm pitching moment coefficient

IAR inclined-axis rolls or oscillatory coning

J cost function

k non-dimensional frequency, $\mathbf { k } { = } \infty l / \mathbf { V }$

l characteristic length, $l = \overline { { c } } \ / 2$

PSD power spectral density

q pitch rate, rad/sec

s Laplace transform variable

SF single frequency

t time, sec

V airspeed, m/sec

v measurement noise

WB wide band

Z vector of output measurements

$\alpha$ angle of attack, rad

$\beta$ sideslip angle, rad

η state variable in unsteady model

θ unknown parameter vector

$\sigma ^ { 2 }$ variance

τ dummy integration variable

$\tau _ { 1 }$ non-dimesional time constant

$\boldsymbol { \Phi }$ bank angle, rad

ω angular frequency, rad/sec

superscripts, subscripts

estimate (superscript)

A amplitude (subscript)

Aerodynamic derivatives

$$
C _ {A _ {a}} (\infty) \equiv C _ {A _ {a}} = \frac {\partial C _ {A}}{\partial a}
$$

$$
f o r A = L, m, o r N; a = \frac {q \overline {{c}}}{2 V}, \frac {\dot {q} \overline {{c}} ^ {2}}{4 V ^ {2}}, \alpha , \frac {\dot {\alpha} \overline {{c}}}{2 V}, \beta , o r \frac {\dot {\beta} b}{2 V}
$$

# Introduction

A basic problem in flight dynamics is the mathematical formulation of the aerodynamic model for aircraft. Aerodynamicists have investigated this problem and in turn the problem of how to test in wind tunnels to obtain model parameters since the early days of flight. Today the problem of predicting aerodynamic response for arbitrary aircraft motion has not been completely solved. The conventional formulation is to assume the aerodynamic forces and moments can be represented by a differentiable function and therefore expanded in Taylor series with only first order linear terms (stability and control derivatives) retained [1]. This formulation has only been effective in certain portions of the flight envelope where nonlinear or unsteady effects are either not present or relatively benign. As flight-maneuvering capability has expanded so have limitations of the conventional aerodynamic model to predict aircraft responses in flight. In addition, as efforts to develop new mathematical models have proceeded, the limitations of conventional test techniques have also been realized.

In reference [2] limitations of the conventional linear aerodynamic model for rigid-body aircraft and conventional forced-oscillation testing were noted. A methodology for modeling and testing to estimate an unsteady form of the model was presented. The new formulation retained the conventional static and rotary dynamic terms but replaced conventional acceleration terms (derivatives with respect to angle of attack rate or sideslip rate) with more general indicial functions. In addition, a frequency domain method for data analysis was presented to estimate all the terms in the new aerodynamic model at each test condition. The approach only required the use of a conventional forced-oscillation test rig, although the test rig was required to provide wide-band inputs. This approach substantially improved upon conventional onefrequency-at-a-time forced-oscillation tests by reducing the test matrix size and providing substantially more information content. The methodology was demonstrated on a longitudinal example using a $10 \%$ scale model of the F-16XL aircraft.

Ideally, validation of any methodology is accomplished by comparisons with independent identification methods and experimental tests showing the same results and by accurate prediction of aerodynamic response. In this study an effort is made to apply a variety of methods and tests that lead to an

effective validation of the new methodology. Previously, only conventional forced-oscillation testing results were available for comparison. A limitation of conventional modeling and forced-oscillation testing is that only in-phase and out-of-phase aerodynamic terms can be estimated. These terms are frequency and amplitude dependent and represent combinations of stability derivatives with acceleration terms.

Consequently, direct comparison of separate estimates of rotary damping and unsteady terms could not be made. More recently, a facility with an advanced dynamic test capability became available for validating the new methodology and for further investigation into nonlinear unsteady aerodynamic modeling.

For this study, validation experiments were made possible by performing tests using an advanced dynamic test rig at Rolling Hills Research Company (RHRC), formerly Eidetics Corporation. This test rig was developed at RHRC through a Navy Phase II SBIR completed in June 2000 [3]. The new rig was designed to allow forced-oscillation, coning, oscillatory coning, and combined-axis rotation experiments in the RHRC water tunnel. With a Phase III SBIR, through NASA Langley Research Center, further enhancements to maximize dynamic testing accuracy and capability were added, including wideband input testing. As part of the effort under the Phase III SBIR, several advanced experiments have been performed to apply the new methodology proposed in [2] and to run validating experiments. In addition, flow visualization experiments, under static and dynamic conditions, have been performed to further support this effort.

In this paper one linear unsteady aerodynamic model is postulated for the experiments. However, different model structures are presented since each lends itself to a different method of identification. Two independent methods are used to identify the model and to validate the estimation techniques, themselves. Besides the first method under evaluation from [2], a second method called 2-Step regression [4] is used for comparison. Further validation of the estimated model is shown by testing the prediction capability of the model on data not used in the identification process. For these validation tests, predicted and measured responses are compared for two types of experiments: (1) ramp-up and hold tests at different rates and (2) small-amplitude forced oscillation tests at different frequencies.

Four different types of experimental data provide final validation of the methodology under evaluation.

First, wide-band (WB) forced-oscillation experiments are performed to allow application of the methodology. This results in a general unsteady model that can be validated against the remaining tests. Second, singlefrequency (SF) forced-oscillation data are analyzed using harmonic analysis to get conventional in-phase and out-of-phase coefficients. These coefficients can be compared with those determined directly from the unsteady model. Third, inclined-axis oscillatory coning experiments or inclined-axis rolls (IAR) allow estimation of frequency dependent acceleration terms [5]. Separation of these terms, normally combined in conventional models, allows for direct comparison with that predicted by the unsteady model. Fourth, static data are used to confirm the estimation process is working correctly by comparing, for example, lift curve slope from the model with that calculated directly from the static lift curve.

# Model Postulation

Results from wind tunnel forced-oscillation tests show that the resulting combinations of stability derivatives depend on the frequency of the oscillations, amplitude, and mean angle of attack. This dependency contradicts the basic assumption that stability derivatives are time invariant. The effect of frequency on the aerodynamic parameters is related to unsteady aerodynamics as explained in [6]. In this reference the aerodynamic model was expressed in the form of statespace equations. Later, in [7], the same problem was addressed by using indicial functions. In [7] the indicial function was postulated in models for aerodynamic coefficients as a simple exponential function

$$
a \left(1 - e ^ {b _ {1} t}\right) + c
$$

The unknown aerodynamic parameters in the complete aerodynamic model can be estimated in different ways. Two approaches have been established, namely, a 2- step linear regression [4] and a maximum likelihood (ML) method [2]. Both approaches are validated by this study.

As an example, lift is considered in the form

$$
\begin{array}{l} C _ {L} (t) = C _ {L} (0) + \int_ {0} ^ {t} C _ {L \alpha} (t - \tau) \dot {\alpha} (\tau) d \tau \tag {1} \\ + \frac {l}{V} \int_ {0} ^ {t} C _ {L q} (t - \tau) \dot {q} (\tau) d \tau \\ \end{array}
$$

where $C _ { L _ { \alpha } } ( t )$ and $C _ { L _ { q } } ( t )$ are the indicial functions, $C _ { L } ( 0 )$ is the initial value of $C _ { L }$ , l is the characteristic length, and V is the airspeed. Two assumptions were adopted to allow simplification of the model used in the analysis of measured data: a) the effect of ${ \dot { \boldsymbol { q } } } ( t )$ on the lift can be neglected and b) the indicial function $C _ { L _ { \alpha } } \left( t \right)$ can be expressed as

$$
C _ {L _ {\alpha}} (t) = C _ {L _ {\alpha}} (\infty) - a e ^ {- b _ {1} t}. \tag {2}
$$

The simplified model, which takes into account increments with respect to steady state conditions, has the form

$$
\begin{array}{l} C _ {L} (t) = C _ {L _ {\alpha}} (\infty) \alpha (t) + \frac {l}{V} C _ {L _ {q}} (\infty) q (t) \tag {3a} \\ - a \int_ {0} ^ {t} e ^ {- b _ {1} (t - \tau)} \dot {\alpha} (\tau) d \tau \\ \end{array}
$$

or in operator form

$$
\begin{array}{l} C _ {L} (t) = C _ {L \alpha} (\infty) \alpha (t) + \frac {l}{V} C _ {L q} (\infty) q (t) \tag {3b} \\ - \frac {a}{D + b _ {1}} D \alpha \\ \end{array}
$$

where $C _ { L _ { \alpha } } ( \infty )$ and $C _ { L _ { q } } ( \infty )$ are the rates of change with $\mathfrak { a }$ and q evaluated in steady flow. By introducing

$$
\eta (t) = \int_ {0} ^ {t} e ^ {- b _ {1} (t - \tau)} \dot {\alpha} (\tau) d \tau
$$

the state-space form of (3) is

$$
\begin{array}{l} \dot {\eta} (t) = - b _ {1} \eta + \dot {\alpha} \\ C _ {L} (t) = C _ {L \alpha} (\infty) \alpha (t) + \frac {l}{V} C _ {L q} (\infty) q (t) - a \eta (t) \end{array} \tag {4}
$$

Applying the Laplace transform to Eq. (4), the transfer function for the lift coefficient is obtained as

$$
\frac {C _ {L} (s)}{\alpha (s)} = \frac {A s ^ {2} + B s + C}{s + b _ {1}} \tag {5}
$$

where s is the Laplace transform parameter and

$$
A = \frac {\ell}{V} C _ {L q} (\infty)
$$

$$
B = C _ {L _ {\alpha}} (\infty) - a + b _ {1} \frac {\ell}{V} C _ {L q} (\infty) \tag {6}
$$

$$
C = b _ {1} C _ {L _ {\alpha}} (\infty)
$$

The next model structure lends itself to the 2-step regression approach. For a one degree of freedom oscillatory motion with $\scriptstyle \beta = 0$ and

$$
\alpha = \alpha_ {A} \sin (\omega t) \tag {7}
$$

$$
q \equiv \dot {\alpha} = \alpha_ {A} \omega \cos (\omega t)
$$

The steady-state solution of (3) is

$$
C _ {L} (t) = \bar {C} _ {L _ {\alpha}} \sin (\omega t) + \bar {C} _ {L _ {q}} \cos (\omega t) \tag {8}
$$

where, as shown in [7], the in-phase and out-of-phase components of $C _ { L } ( t )$ are

$$
\bar {C} _ {L _ {\alpha}} = C _ {L _ {\alpha}} - a \frac {\tau_ {1} ^ {2} k ^ {2}}{1 + \tau_ {1} ^ {2} k ^ {2}} \tag {9}
$$

$$
\overline {{C}} _ {L q} = C _ {L q} - a \frac {\tau_ {1}}{1 + \tau_ {1} ^ {2} k ^ {2}}
$$

where $\tau _ { 1 } = \frac { V } { \ell } b _ { 1 } , k = \frac { \ell } { V } \omega$

An important element of the methodology is the general structure used for the aerodynamic model. It has a form that retains conventional static and rotary aerodynamic terms that have traditionally provided substantial engineering information to the flight dynamics community. Using lift as a representative example for any of the non-dimensional forces and moments, the general form can be written as equation (4). Similar equations can be written for the other force and moment equations. This structure allows easy interpretation of the model parameters by retaining conventional stability and control derivatives for static and dynamic terms. Unsteady terms are obtained by solving a first order differential equation with α- dependent coefficients. This approach offers a straightforward model for simulation.

# Model Identification

In model equations (3), (4), (5), and (9) there are four unknown parameters $( a , b _ { 1 } , C _ { L _ { \alpha } } , C _ { L _ { q } } )$ or

$( a , \tau _ { 1 } , C _ { L _ { \alpha } } , C _ { L _ { q } } )$ that can be estimated, in general,

from measured time histories of $\operatorname { \alpha } ( \operatorname { t } ) , \operatorname { \mathrm { q } } ( \operatorname { t } )$ , and $\mathrm { C _ { L } ( t ) }$ .

The first model equation, for 2-step linear regression, is obtained from (9) by expressing

$$
\frac {\tau_ {1} ^ {2} k ^ {2}}{1 + \tau_ {1} ^ {2} k ^ {2}} = 1 - \frac {1}{1 + \tau_ {1} ^ {2} k ^ {2}}
$$

then

$$
\bar {C} _ {L _ {\alpha}} = a _ {0} - \tau_ {1} \bar {C} _ {L _ {q}} \tag {10}
$$

where

$$
a _ {0} = C _ {L _ {q}} + (a - C _ {L _ {\alpha}}) \tau_ {1}
$$

As follows from the harmonic analysis of a linear system, the in-phase and out-of-phase components are obtained from the measurement as

$$
\bar {C} _ {L _ {\alpha}} = \frac {2}{\alpha_ {A} n _ {c} T} \int_ {o} ^ {n _ {c} T} \Delta C _ {L} (t) \sin \omega t d t \tag {11}
$$

$$
\bar {C} _ {L _ {q}} = \frac {2}{\alpha_ {A} k n _ {c} T} \int_ {o} ^ {n _ {c} T} \Delta C _ {L} (t) \cos \omega t d t
$$

where $T = \frac { 2 \pi } { \omega }$ and $n _ { c }$ is the number of cycles of

oscillation. Knowing the in-phase and out-of-phase components at various frequencies $\Theta _ { 1 }$ , ${ \mathfrak { O } } _ { 2 } .$ , …, ${ \mathfrak { O } } _ { \mathrm { n } } ,$ , where $\mathtt { n } > 2$ , the parameters $a _ { 0 }$ and $\tau _ { 1 }$ can be obtained by applying the least-squares principle to (10). In the second step $\tau _ { 1 }$ is assumed known and the least-squares estimates of $( a , C _ { L _ { \alpha } } , C _ { L _ { q } } )$ , L C follows from model equation (9).

The second estimation technique uses maximum likelihood in the frequency domain. The model equation is given by (5) after expressing s as jω. In this case, the model used in the estimation has the form

$$
C _ {L} (\omega) = \frac {- A \omega^ {2} + C + i B \omega}{b _ {1} + i \omega} \alpha (\omega) \tag {12}
$$

$$
z (j) = C _ {L} (j) + \mathrm {v} (j), \quad j = 1, 2, \dots , N \tag {13}
$$

where $C _ { L } ( \omega )$ and $\alpha ( \omega )$ are the Fourier transforms of $C _ { L } ( t )$ and $\alpha ( t ) , \ \mathbf { v } ( j )$ is the measurement noise

assumed to be a Gaussian random complex sequence with zero mean and variance $\sigma ^ { 2 }$ , N is the number of frequencies at which the transformed input output data are known, and ω is the angular frequency. The maximum likelihood estimator minimizes the negative logarithm of the likelihood function

$$
\hat {\theta} = \min  _ {\theta , \sigma^ {2}} \left\{- \ln L \left(Z _ {N}; \theta , \sigma^ {2}\right) \right\} \tag {14}
$$

where $Z _ { \mathrm { N } } = [ z ( 1 ) , z ( 2 ) , . . . , z ( \mathrm { N } ) ]$ is a vector of output measurements and $\boldsymbol { \theta } = [ \mathbf { A } , \mathbf { B } , \mathbf { C } , \mathbf { b } _ { 1 } ]$ is the vector of unknown parameters. Because (5) is nonlinear in the parameters, the estimation represents a nonlinear estimation problem. The initial values of parameters

for this technique were obtained from a linear regression using the cost function

$$
J (\theta) = \sum_ {j = 1} ^ {N} \left| C _ {L} (j) \left(b _ {1} + i \omega_ {j}\right) + \left(A \omega_ {j} ^ {2} - C - i B \omega_ {j}\right) \alpha (j) \right| ^ {2} \tag {15}
$$

Oscillatory tests using a simple harmonic input are usually repeated at different frequencies. If the data are to be used to estimate (four) unsteady model parameters then six or more frequencies are recommended for better statistical results. In order to avoid the large number of runs, the use of a wide-band input was proposed in [2]. Specifically, the Schroeder sweep [8] was selected with specified amplitude to provide a flat power spectrum over a specified frequency range. Transforms of the time histories of the input and aerodynamic coefficients to the frequency domain were accomplished using a Discrete Fourier Transform (DFT) algorithm [9]. This algorithm utilizes a zoom transform and allows the transform to be performed over the frequency range corresponding to the wide-band input.

# Model Validation

Model validation is accomplished, in this study, by considering three kinds of validation tests. The first test uses two independent identification methods, applied to the same data. Obtaining the same model estimates confirms both the model and the estimation techniques. For this comparison, maximum likelihood estimation in the frequency domain, using model (12), is applied to the wide-band data. Then a comparison is made with results from the two-step regression method applied to the same data. For the two-step method, harmonic analysis is done first to produce the required in-phase and out-of-phase coefficients as inputs.

To ensure the methodology has produced an adequate model, validation data are required to test the predictive ability of the model. These data are additional measurements not used for identification of the model under test. For the second validation test, comparisons of measured and predicted responses are used. Test data are created using ramp inputs to drive the model at different maximum angular rates to excite unsteady behavior; inputs are applied at various angles of attack. Additional comparisons, to assess the predictive capability of the model, are made using sinusoidal SF forced-oscillation data at different frequencies.

The third set of validation tests use measurements from conventional SF forced-oscillation, inclined-axis

rolls, and static runs. Each data type facilitates an independent estimate of parameters that can be compared against that predicted by the general unsteady model. From tests based on conventional single-frequency forced-oscillation data, in-phase and out-of-phase components are obtained using (11). These components can be compared with those obtained from (12) realizing that

$$
\frac {C _ {L} (\omega)}{\alpha (\omega)} = U + i V \tag {16}
$$

where,

$$
U = \bar {C} _ {L _ {\alpha}} \tag {17}
$$

$$
\frac {1}{k} V = \bar {C} _ {L q} \tag {18}
$$

IAR experiments allow separate estimation of unsteady acceleration terms. In this case, the unsteady term in the more general model (last term in (3)) provides estimates that compare directly to those estimated from the IAR experiment. This experiment is a modification of the traditional rotary balance testing where the axis of rotation is inclined from the velocity vector by an angle λ. During the experiment the rotational velocity, $\Omega$ , remains constant, whereas the angle of attack and sideslip oscillate. For small inclination $\gimel$ , the changes in $\alpha$ and $\beta$ are defined as

$$
\alpha (t) = \alpha_ {0} + \lambda \cos \Omega t \tag {19}
$$

$$
\beta (t) = \lambda \sin \Omega t
$$

From the output data the frequency dependent parameters $C _ { A \dot { \alpha } }$ and $C _ { A { \dot { \beta } } }$ (where $\mathrm { C _ { A } }$ is one of the aerodynamic forces or moments) can be estimated. With a linear aerodynamic model assumed to be given as

$$
C _ {L} (t) = C _ {L} (\alpha , \beta , \dot {\alpha}, \dot {\beta}) \tag {20}
$$

and assuming small $\lambda$ , the response (using lift coefficient as an example) in terms of in-phase and out-of-phase harmonic components can be written as

$$
C _ {L} = \bar {C} _ {L \alpha} \lambda \cos \omega t + \bar {C} _ {L \beta} \lambda \sin \omega t \tag {21}
$$

where

$$
\bar {C} _ {L _ {\alpha}} = \left(C _ {L _ {\alpha}} + k C _ {L _ {\dot {\beta}}}\right) \tag {22}
$$

$$
\overline {{C}} _ {L \beta} = \left(C _ {L \beta} - k C _ {L \dot {\alpha}}\right)
$$

As described in reference [5], by performing oscillatory coning in both $\Omega ^ { + }$ and $\Omega ^ { - }$ directions, frequency dependent parameters can be estimated as

$$
\begin{array}{l} C _ {L _ {\dot {\alpha}}} = - \left[ \bar {C} _ {L \beta} ^ {+} - \bar {C} _ {L \beta} ^ {-} \right] / (2 | \Omega |) \tag {23} \\ C _ {L _ {\dot {\beta}}} = + [ \overline {{C}} _ {L _ {\alpha}} ^ {+} - \overline {{C}} _ {L _ {\alpha}} ^ {-} ] / (2 | \Omega |) \\ \end{array}
$$

With unsteady terms estimated from oscillatory coning, it is possible to separate steady-flow damping derivatives from the combined out-of-phase damping coefficients determined in conventional forcedoscillation experiments.

The last validation test checks the unsteady model estimates of force or moment derivatives with respect to $\mathfrak { a }$ or $\beta$ , $\mathrm { C } _ { \mathrm { A d } }$ or $\mathrm { C _ { A \beta } }$ respectively. This parameter (first term in (3)) can be directly compared to that obtained from static measurements. Comparable values from the two methods provide further validation that the identification process is working correctly.

Another test technique, requiring a test capability not available for this study, is an experiment with direct heave or sideslip motion. In oscillatory heave and sideslip testing

$$
\begin{array}{l} \begin{array}{l} \alpha (t) = \alpha_ {0} + \alpha_ {A} \sin \omega t \\ \alpha (t) = \alpha_ {0} - \alpha_ {A} \end{array} \tag {24} \\ \beta (t) = \beta_ {A} \sin \omega t \\ \end{array}
$$

Using the model structure in (20) and application of harmonic analysis (11), estimates in-phase and out-ofphase coefficients can be obtained. From these results $C _ { A \dot { \alpha } }$ and $C _ { A { \dot { \beta } } }$ can be determined.

# Experiments

Advanced dynamic tests were conducted in the Rolling Hills Research Company Water Tunnel in order to apply and validate the methodology presented in [2]. For these tests a $2 . 5 \%$ scale model of the F-16XL (figure 1) was mounted on a dynamic test rig through a five-component strain-gauge balance (axial force was not measured). The dynamic test rig is a computer-controlled system with a sting-mounted double C-strut support system [3]. The mounting arrangement rotated the model about the reference center of gravity location of 0.558 c . The tests were conducted at a dynamic pressure of 0.81 psf resulting in the flow velocity of 11 inches/sec and a Reynolds number of $5 2 \mathrm { x } 1 0 ^ { 3 }$ based on the mean aerodynamic chord. Reynolds number values different from that found in flight or wind tunnels are acceptable for this study since the methodology is both applied and

validated using the same water tunnel conditions. With this relaxed requirement, hydrodynamic flow at the inlet was improved by adding an inlet fairing to block flow into the inlet. Flow visualization and measurement equipment inside the model did not allow enough space for smooth flow through the body.

Application of the methodology under test required wide-band forced oscillation experiments. Wide-band oscillatory data were created using Schroeder sweeps in $\alpha$ as an input. Tests were conducted at 17 mean values of angle of attack, $\mathrm { { \mathbf { { a } } _ { 0 } , } }$ using an amplitude $\alpha _ { \mathrm { { A } } } = 5$ degrees. The range of $\alpha$ - mean values was from ${ \sf a } _ { 0 } = 0$ to 75 degrees. Data were sampled at $1 0 \ : \mathrm { H z }$ with a lowpass analog filter at $5 \mathrm { H z }$ . Tests were repeated eleven times at each angle of attack and then an average signal was formed using the ensemble data to minimize measurement noise. The ensemble-averaged data was used for data analysis.

Validation data were created using the same test rig and instrumentation as that used for the wide-band data. For this paper, only small amplitude ramps and oscillatory motions are considered. In both cases $\mathrm { \Delta \mathrm { a } _ { A } = }$ 5 degrees. Ramp inputs were generated for three different non-dimensional pitch rates, (0.01, 0.02, 0.03), starting at five different $\mathtt { Q } _ { 0 }$ ranging from 30 to 50 degrees. Sinusoidal, single-frequency, forcedoscillation data were created at five different nondimensional frequencies, (0.05, 0.10, 0.15, 0.20, 0.25), and at five mean $\mathrm { \bf q } _ { 0 } ,$ ranging from 20 to 60 degrees. Inclined-axis oscillatory coning experiments were run for $\gimel$ equal to 5 degrees. These tests were completed for four non-dimensional rotation rates, $\Omega { \bf b } / 2 \mathrm { V } = ( 0 . 0 5 $ , 0.10, 0.15,0.20), and ${ \bf { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm \mathrm { { \alpha } } \mathrm { { \alpha } } \mathrm \mathrm { { \alpha } } \mathrm \mathrm { { \alpha } } \mathrm \mathrm { { \alpha } } \mathrm \mathrm { { \alpha } } \mathrm \mathrm { \mathrm { \alpha } } \mathrm \mathrm { { \alpha } } \mathrm \mathrm { \mathrm { \alpha } } \mathrm \mathrm { \mathrm { \alpha } } \mathrm \mathrm  \mathrm { \alpha } \mathrm \mathrm { \alpha } \mathrm \mathrm { } \mathrm \mathrm { \alpha } \mathrm \mathrm \mathrm { \alpha } \mathrm \mathrm { \mathrm \mathrm { \alpha } \mathrm \mathrm } \mathrm \mathrm  \mathrm \mathrm { \alpha } \mathrm \mathrm \mathrm { \alpha \alpha } \mathrm \mathrm \mathrm \mathrm { \mathrm \alpha } \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm { \alpha \alpha \alpha } \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm \mathrm  \alpha \alpha \alpha \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \alpha \alpha \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm  \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm \mathrm $ up to 35 degrees.

Example time histories of input/output data for application of the methodology are shown in figure 2. Angle of attack, normal force and pitching moment coefficients, α, $\mathrm { C _ { N } } ,$ , and $\mathrm { { C } _ { \mathrm { { m } } } , }$ at $\mathbf { \alpha } \mathbf { a } _ { 0 } = 3 0$ degrees are presented. These plots show displacements relative to starting values at ${ \bf { \cal Q } } _ { 0 }$ . The harmonic content of the angle of attack is shown in figure 3 as a function of frequency. Figure 3 indicates a flat spectrum for a frequencies up to $0 . 2 \ : \mathrm { H z }$ which corresponds to reduced frequencies up to ${ \mathrm { k } } = 0 . 4 2$ . For the analysis, time histories of inputs and aerodynamic coefficients were transformed to the frequency domain using a DFT algorithm over the frequency range of 0.003 to $0 . 2 \ : \mathrm { H z }$ .

Example time histories of input/output data for validation are shown in figures 4 and 5. Figure 4 provides example measurements α, $\mathrm { C _ { N } } ,$ and $\mathrm { C } _ { \mathrm { m } }$ for conventional forced oscillation (FO) data. This

example is for oscillations about $\mathrm { \Delta a } _ { 0 } = 3 0$ degrees and at frequencies of ${ \mathrm { k } } = 0 . 2 5$ $\mathrm { f } = 0 . 1 1 8 \mathrm { H z }$ ). For these experiments 30 cycles of data were recorded for each run. An average over all cycles, forming one cycle, is shown in the figure. Figure 5 shows $\boldsymbol { \Phi }$ , α, β, $\mathrm { C } _ { \mathrm { N } } ,$ and $C _ { \mathrm { m } }$ time histories for IAR runs at $\mathbf { \Delta } \mathbf { Q } _ { 0 } = 3 5$ degrees. Bank angle, $\boldsymbol { \Phi }$ , indicates that the model undergoes rotations in the positive direction followed by the same steady rotations in the negative direction. In this example, rotation rate is $2 5 . 9 \deg / \sec$ producing oscillation periods for $\mathfrak { a }$ and $\beta$ of approximately 13.9 seconds and $\Omega \mathrm { b } / 2 \mathrm { V } = 0 . 2$ . Similar results were obtained for side force, rolling and yawing moments. For IAR tests ensemble averages were formed using 15 repetitions of the experiment.

# Results and Discussion

For this paper, methodology validation was limited to longitudinal low-amplitude forcedoscillation data and only test cases for angle of attack between 30 and 70 degrees were considered. Unsteady effects, for this water-tunnel model, primarily occur for $3 0 { < } \alpha { < } 5 0$ degrees, as will be shown by considering the in-phase and out-of-phase coefficients (figure 10).

Both identification methods used in the first validation test require transformation of the data to a frequency domain representation. The method in [2], based on Maximum Likelihood (ML), uses input and output measurements of the experiments almost directly except for the DFT applied to the data. The 2- Step Regression approach [4] requires estimates of the in-phase and out-of-phase coefficients as inputs, thus some data processing is also required before application of the method. In order to minimize data processing a simple method was chosen to obtain these coefficients. Forming transfer function (16) directly by dividing outputs $\mathrm { C _ { N } ( \omega ) }$ by inputs $\alpha ( \omega )$ in the frequency domain, the coefficients could be obtained using (17) and (18). This method produces a relatively noisy frequency response function; however, sufficient information content and signal-to-noise ratio are present for the analysis. Because of this approach the 2-Step Regression method produced relatively larger standard errors, reflecting more on the quality of the inputs rather than the identification method, itself.

Figure 6 shows the estimates of the four unsteady model parameters obtained by ML and 2-Step methods. Circles indicate ML estimates and solid lines are used to show the trends between points. The 2σ error bounds are also plotted as solid vertical lines. 2-Step estimates are marked by $\mathbf { \Delta } ^ { \mathfrak { c } \mathfrak { c } } \mathbf { \Delta } _ { \mathbf { X } } ^ { \mathbf { , 3 } \mathbf { , } }$ with dotted lines showing

both trends between points and $2 \sigma$ bounds. In the top graph for $\mathfrak { a }$ between 30 and 50 degrees, mean values for $\mathrm { C } _ { \mathrm { N a } }$ are in good agreement between the two methods. The differences at higher alphas reflect the limited unsteady information content in the data. The model structure, used in both approaches, assumes the presence of unsteady dynamics. This problem is reflected in the tendency for larger error bounds above $\alpha = 5 0$ degrees for all the estimated parameters. For the $\mathrm { C _ { N q } }$ term similar results occurred, except the 2-Step method produced unrealistic negative values above 50 degrees angle of attack. This is likely the result of limited unsteady dynamics further aggravated by the poor signal-to-noise ratio. A similar plot is obtained for the model parameter “a” except the ML method is also producing larger error bounds for the higher alphas. Mean values from the ML method are consistent with expectations that the parameter “a” will become small as unsteady behavior reduces for $\alpha > 5 0$ degrees. In water tunnel facilities motions have much longer time constants than wind tunnels. Consequently the transfer function parameter, $\mathsf { b } _ { 1 } ,$ , for the unsteady model is very small. Mean values agree very well between the two methods and the larger error bounds for the 2-Step method reflect the less desirable input data. Mean value of $\mathbf { b } _ { 1 }$ over the range $3 0 { < } \alpha { < } 5 0$ is approximately 0.168.

An indication that an adequate model has been determined is shown by the ability to predict responses using data that was not used for identification. Figures 8 and 9 provide this type of validation data. In addition, these figures show inputs $\alpha ( \mathrm { t } )$ and q(t), as well as transient behavior of state, η(t), defined in (4). Figure 8 shows a representative example of measured and predicted responses of $\mathrm { C _ { N } }$ to ramp-and-hold inputs performed at different pitch rates. For the example in figure 8, the unsteady model estimated at $\mathrm { a } _ { 0 } = 4 2 . 5$ degrees is used to model a ramp from $\alpha = 4 0$ to 45 degrees. The maximum pitch rate achieved during the ramp was $q \overline { { c } } / 2 V = 0 . 0 3$ or approximately 5 deg/sec (model scale). Figure 9 shows a representative example of the unsteady model (at $\mathrm { \Delta } \mathrm { a } _ { 0 } = 4 0$ degrees) predicting harmonic response of $\mathrm { C _ { N } }$ during conventional forced oscillation. For this comparison, the third cycle of oscillation is compared with the measured data to allow start-up transients to die out. For this example the harmonic input has a reduced frequency of ${ \mathrm { k } } = 0 . 2$ and an amplitude of 5 degrees.

The third set of validation tests allow various parameters to be estimated and compared with the general unsteady model. In-phase and out-of-phase

coefficients (Fourier coefficients) defined by (11) can be obtained from conventional, single-frequency (SF), forced-oscillation data. The same parameters can be estimated from the general model by using (17-18). This comparison is shown in figure 10 for three reduced frequencies. The general unsteady model results are provided over the $\alpha$ range shown, however the coefficients from SF forced-oscillation data are only computed at $\alpha = ( 2 0 , 3 0 , 4 0 , 5 0 , 6 0 )$ degrees and are shown as triangles. This figure shows the strong frequency dependence or unsteady behavior of the aerodynamics for $\alpha$ greater than 30 degrees and less than 50 degrees. The agreement between the two modeling methods is very good within the range of $\mathfrak { a }$ where unsteady behavior occurs. At $\mathbf { \alpha } \mathbf { a } _ { 0 } = 3 0$ degrees, where little unsteady behavior occurs, only a small difference is apparent.

Oscillatory coning or IAR experiments produced data shown in figure 5. The advantage of harmonic IAR experiments is that unsteady acceleration terms can be readily extracted from this type of data. The dynamic rig in this example is capable of approximately 406 degrees of rotation before the wires leading to the balance reach their limits. Consequently, the motion begins at a minimum $\Phi ^ { = } \mathrm { - } 4 0 6$ degrees and continues until a maximum of $\phi = + 4 0 6 $ degrees. At this point the rig must stop and reverse direction. It appears that the measured responses may not be in steady harmonic motion since the lower peaks of $C _ { \mathrm { N } }$ are changing with each cycle. This implies that the initial transient has not decayed sufficiently to reach steady harmonic oscillation where each peak would have approximately the same amplitude. The analysis defined in (23) assumes steady harmonic data and therefore is not appropriate for this type of data. A transient analysis of this data will be part of the next phase of this study and comparisons can then be made with results using the ML methodology in [2]. Figure 11shows estimates of $C _ { N _ { \dot { \alpha } } } ( k , \alpha )$ from the WB experiment using the ML approach. This can be considered as the unsteady equivalent to the conventional derivative, ${ \partial C _ { N } } / { \partial ( \dot { \alpha } \overline { { c } } / 2 V ) }$ .

To demonstrate the harmonic analysis proposed in [5] for IAR experiments, representative model parameters were chosen and simulated data were prepared as shown in figure 12. Time histories of α, β, and $C _ { \mathrm { N } }$ are shown for steady harmonic motion in both the positive and negative roll directions. Oscillations occur at a reduced frequency of $\mathrm { k } = \mathrm { \omega _ { o b } } / 2 \mathrm { V } = 0 . 0 5$ . A moderate amount of noise was added to the

measurements of $\mathrm { C _ { N } }$ to simulate realistic tunnel data. Parameter true values, $\theta$ , for the IAR model (20) and estimates, $\hat { \theta }$ , of the acceleration terms are given in the table below.

<table><tr><td></td><td>CNα</td><td>CNβ</td><td>CNβ</td><td>CNα</td></tr><tr><td>θ</td><td>1.0</td><td>-0.3</td><td>5.0</td><td>18.0</td></tr><tr><td>θ̂</td><td>---</td><td>---</td><td>4.98</td><td>17.87</td></tr></table>

The top half of figure 13 shows mean values for 5 repeated measurements of static $C _ { \mathrm { N } }$ with $2 \sigma$ error bounds. The second graph shows the corresponding mean values and $2 \sigma$ bounds for $\mathrm { C } _ { \mathrm { N a } }$ estimated by the general unsteady model and by a simple gradient method using the static data above. The two methods generally agree well and have reasonable error bounds. Although some difference in mean values occur at ${ \mathfrak { a } } =$ 40 degrees where a steep gradient occurs in $\mathrm { C _ { N } }$ . This is not surprising since the gradient can vary sharply in this region and this is a region of peak unsteady behavior. Some unsteady behavior was observed during static measurements as well.

# Concluding Remarks

This study is part of an ongoing effort at NASA Langley to develop a more general formulation of the aerodynamic model for aircraft that includes nonlinear unsteady aerodynamics. In this study independent identification methods and a series of different dynamic tests were used to show the validity of a methodology for modeling and testing to estimate linear unsteady models for aircraft. Independent identification methods applied to the same wide-band data produced the same model parameter values indicating legitimacy of the two approaches. The unsteady model successfully predicted transient dynamics that occurred in ramp and hold as well as harmonic experiments providing validation that the methodology produces an adequate model. Static derivatives and Fourier coefficients were well predicted by the model further validating the methodology for modeling unsteady aircraft behavior. Simulated inclined-axis results demonstrated a technique for estimating unsteady acceleration terms.

# References

1. Etkin, B.: Dynamics of Atmospheric Flight, John Wiley & Sons, Inc., New York, 1972.   
2. Murphy, P. C., Klein, V.: Estimation of Aircraft Unsteady Aerodynamic Parameters From

Dynamic Wind Tunnel Testing, AIAA Paper 2001-4016, August 2001.

3. Eidetics Corporation: Final Report; Determination of Nonlinear Dynamic Aerodynamic Coefficients for Aircraft, SBIR Phase II Final Report, Naval Air Warfare Center Aircraft Division, TR00-002, June 11, 2000.   
4. Abramov, N. B, Goman, M. G., Greenwell, D. I., and Khrabrov, A. N.: Two-Step Linear Regression Method for Identification of High Incidence Unsteady Aerodynamic Model. AIAA Paper 2001-4080, August 2001.   
5. Khrabrov, A., Kolinko, K., Miatov, O., Vinogradov, J., Zhuk, A.: Using of Oscillatory Conning Experimental Rig for Separation of Rotary and Unsteady Aerodynamic Dervivatives, $1 8 ^ { \mathrm { t h } }$ ICIASF, Toulouse, France, June 14-17, 1999.   
6. Goman, M. and Khrabrov, A.: State-Space Representation of Aerodynamic Characteristics at High Angles of Attack. Journal of Aircraft, Vol. 31, No. 5, Sept.–Oct. 1994, pp. 1109–1115.   
7. Klein, Vladislav and Noderer, Keith D.: Modeling of Aircraft Unsteady Aerodynamic Characteristics. Part 2-Parameters Estimated from Wind Tunnel Data. NASA TM 110161, 1995.   
8. Schroeder, M.R.: Synthesis of Low-Peak-Factor Signals and Binary Sequences with Low Autocorrelation, IEEE Transactions on Information Theory, January 1970, pp. 85-89.   
9. Morelli, Eugene A.: High Accuracy Evaluation of the Finite Fourier Transform Using Sampled Data, NASA TM 110340, June 1997.

图片摘要：该图主要展示 1. Three view drawing of F 16XL model。
![](images/c96fced2c4d9fecefb944524e8bd8f0950ad2ee76373775fc42956652e5cd338.jpg)  
Figure 1. Three-view drawing of $2 . 5 \%$ F-16XL model.

图片摘要：该图主要展示 1. Three view drawing of F 16XL model。
![](images/f3ed74a6e440a6629749ded135a9a8438b4e076f79ba6b19f863feb5bc4e78d3.jpg)

图片摘要：该图主要展示 1. Three view drawing of F 16XL model。
![](images/bad572b01b6bc6a8dbc1e565e449e566edba7d432387e57de7d194b10a142dbb.jpg)

图片摘要：该图主要展示 1. Three view drawing of F 16XL modelFigure 2. Time historie。
![](images/b17c9dfaae3b09b4f3f25fd494bd8d4c2d2e75c42a04beec15b5e27cc64fc3a1.jpg)  
Figure 2. Time histories of angle of attack, lift, and pitch-moment coefficients for $\scriptstyle { \mathfrak { a } } _ { 0 } = 3 0$ degrees during wide-band input exeperiment in water tunnel.

图片摘要：该图主要展示 2. Time histories of angle of attack, lift, and pitch moment。
![](images/58527f38c89e327b3ec70c368c5f9f7341e72f366c66b79624b5d48c108a66a3.jpg)  
Figure 3. Harmonic content of transformed $\alpha$ wideband input for $\mathbf { \alpha } \mathbf { a } _ { 0 } = 3 0$ degrees in water tunnel.

图片摘要：该图主要展示 3. Harmonic content of transformed wideband input for degree。
![](images/b490a4e063ee71dee41a5649bae786eb8774851bacbef27638c96a7bd2acd005.jpg)  
Figure 4. Conventional FO experiment measurements at ${ \bf k } = 0 . 2 5$ and $\mathrm { \Delta Q } _ { 0 } = 3 0$ degrees.

图片摘要：该图主要展示 4. Conventional FO experiment measurements at and degrees。
![](images/00ca35b7996f7fc49fce199a3ddff7e0a70f9f36efa2c289aa499fb35c00d33b.jpg)  
Figure 5. Input and output measurements for IAR experiments at ${ \mathrm { k } } { = } 0 . 2$ and $\mathbf { \Delta } \mathbf { Q } _ { 0 } = 3 5$ degrees.

图片摘要：该图主要展示 5. Input and output measurements for IAR experiments at and 。
![](images/fa02a53268775eea7533c2484086fe4795d35e9e3cd77d0c537e692a517c8389.jpg)

图片摘要：该图主要展示 5. Input and output measurements for IAR experiments at and 。
![](images/49ef07e26ab329a6673a4a61e9c305ef73563f181338c0b00e0ff3584772ea89.jpg)

图片摘要：该图主要展示 5. Input and output measurements for IAR experiments at and 。
![](images/25888a45c4bae70ec1b8f66dcaa9e2a4c15692638e9177396be30af62f15fc16.jpg)

图片摘要：该图主要展示 5. Input and output measurements for IAR experiments at and 。
![](images/c50efa4e66af91fa4bdfe6353b1ab65adca050e4d588393bfe698602dcad0e0f.jpg)  
Figure 6. Estimated parameters and their $2 \sigma$ confidence bounds for Normal force coefficient.

图片摘要：该图主要展示 6. Estimated parameters and their confidence bounds for Norm。
![](images/f65c94969c0ae2642ca6ac4a246dee718a84d4b5d4f34020778ea593dcfd350a.jpg)  
Figure 8. Measured and predicted $\mathrm { C _ { N } ( t ) }$ for ramp input at non-dimensional maximum pitch rate $= 0 . 0 3$ .

图片摘要：该图主要展示 8. Measured and predicted for ramp input at non dimensional 。
![](images/70130fbe3856a9efb046df0f5b18583fceda42370a1970fe4d2768239ceab400.jpg)  
Figure 9. Measured and predicted $\mathrm { C _ { N } ( t ) }$ for harmonic input at ${ \mathrm { k } } = 0 . 2$ , and $\alpha _ { \mathrm { { A } } } = 5$ deg.

图片摘要：该图主要展示 9. Measured and predicted for harmonic input at , and deg。
![](images/c944bea1a661c64f8c3d04d5eec6c32079ae63470c4d519cbedcdc7f3eb93c1b.jpg)  
Figure 10. In-phase and out-of-phase coefficients estimated from wide-band and single harmonic data.

图片摘要：该图主要展示 10. In phase and out of phase coefficients estimated from wi。
![](images/2d2518b56d7ab1613b33925d69572c248d3d505292b6da7fc9a331b5bc1c6640.jpg)  
Figure 11. Variation of $C _ { N \dot { \alpha } }$ with $\alpha$ and $\mathrm { k }$ .

图片摘要：该图主要展示 11. Variation of with and。
![](images/814d41021a43346177069484cf5df60bdf9665e2fc19999dc3e6103be0675240.jpg)  
Figure 12. Input and output measurements for IAR simulated experiment at $_ { \mathrm { k = 0 . 0 4 } }$ and $\mathbf { \Delta } \mathbf { Q } _ { 0 } = 3 5$ degrees.

图片摘要：该图主要展示 12. Input and output measurements for IAR simulated experime。
![](images/aa68e852ccdba4850c5fdb5217baf9514e000fd611997bf8adcec1787bf875dc.jpg)  
Figure 13. $\mathrm { C } _ { \mathrm { N a } }$ estimated from wide-band data and static data.
