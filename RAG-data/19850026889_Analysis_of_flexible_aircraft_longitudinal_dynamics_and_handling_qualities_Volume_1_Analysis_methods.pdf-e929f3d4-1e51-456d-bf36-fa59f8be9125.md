# NASA Contractor Report 177943, Volume I

ANALYSIS OF FLEXIBLE AIRCRAFT LONGITUDINAL

DYNAMICS AND HANDLING QUALITIES

VOLUME I - ANALYSIS METHODS

Martin R. Waszak and David S. Schmidt

PURDUE UNIVERSITY

West Lafayette, Indiana

Grant NAG1-254

June 1985

NASA

National Aeronautics and

Space Administration

Langley Research Center

Hampton, Virginia 23665

# ANALYSIS OF FLEXIBLE AIRCRAFT LONGITUDINAL DYNAMICS AND HANDLING QUALITIES

VOLUMEI - ANALYSIS METHODS

Martin R. Waszak

David K. Schmidt

School of Aeronautics and Astronautics

Purdue University

West Lafayette, IN

June 1985

# ACKNOWLEDGMENTS

This research was supported by the NASA Langley Research Center under grant number NAG-1-254. Thanks go to Mr. William Grantham and Mr. Jerry Elliot who have served as technical monitors.

Additional thanks go to J.B. Davidson and F.A. Leban for advice and assistance which aided this research.

# TABLE OF CONTENTS

Page

LIST OF TABLES.

LIST OF FIGURES. vi

LIST OF SYMBOLS ix

SUMMARY. xii

VOLUME I

CHAPTER I INTRODUCTION. 1

CHAPTER II BACKGROUND 3

CHAPTER III EXPERIMENTAL DATA BASE. 10

CHAPTER IV OPEN-LOOP MODAL ANALYSIS 19

Modal Analysis 19

Vehicle Model 24

Application to Data Base Configurations 28

Numerical Results 32

CHAPTER V CLOSED-LOOP ANALYSIS 52

Neal-Smith/Bacon Methodology. 52

Extension of Neal-Smith/Bacon Methodology 61

Application of the Neal-Smith/Bacon Analysis to the Data Base Configurations 68

Numerical Results 78

CHAPTER VI CONCLUSIONS 85

LIST OF REFERENCES 87

Page

# APPENDICES

Appendix A.1 Scaling Transformation for Mode Identification 89

Appendix A.2 $\mathfrak{n}_{\mathbf{z}}$ in Terms of Vehicle States 92

# VOLUME II

Appendix A.3 Vehicle Configurations and Modal Analysis Results 96

Configuration 1 100

Configuration 2 119

Configuration 3 137

Configuration 4 155

Configuration 5 173

Configuration 6 191

Configuration 7 209

Configuration 8 227

Appendix A.4 Aeroelastic-Structural Mode Shapes 245

Appendix A.5 OCM Frequency Responses 251

Appendix A.6 Listing of Source Code for Modal Analysis Program 284

# LIST OF TABLES

Table

3.1 Summary of Data Base Configurations 12   
3.2 Summary of Tracking Error, Pilot Rating and Pilot Comments 14   
4.1 Summary of Navion Longitudinal Dynamics 23   
5.1 Comparison of Resonance Peak and SP Values 67   
5.2 Summary of Closed-Loop Analysis Inputs 75   
5.3 Summary of Closcd-Loop Analysis of Data Base Configurations 82

# LIST OF FIGURES

# Figure

2.1 Pole-Zero Plot of Typical Flexible Aircraft 4   
2.2 Pole-Zero Plot of Simple Example 5   
3.1 Geometry of Data Base Configurations 11   
3.2 Rigid and Elastic Pitch Angles 13   
3.3 Simulation Visual Display 15   
3.4 Simulation Tracking Errors 16   
3.5 Simulation Pilot Ratings 17   
4.1 Rigid and Elastic Pitch Angles 30   
4.2 Pilot Impulse Residue Magnitudes - Config. 1 33   
4.3 Pilot Impulse Residue Magnitudes - Config. 2 34   
4.4 Pilot Impulse Residue Magnitudes - Config. 3. 35   
4.5 Pilot Impulse Residue Magnitudes - Config. 4. 36   
4.6 Pilot Impulse Residue Magnitudes - Config. 5. 37   
4.7 Pilot Impulse Residue Magnitudes - Config. 6. 38   
4.8 Pilot Impulse Residue Magnitudes - Config. 7 39   
4.9 Pilot Impulse Residue Magnitudes - Config. 8. 40

# Figure

1.10 Gust Impulse Residue Magnitudes - Config. 1 43   
4.11 Gust Impulse Residue Magnitudes - Config. 2 44   
4.12 Gust Impulse Residue Magnitudes - Config. 3 45   
4.13 Gust Impulse Residue Magnitudes - Config. 4 46   
1.11 Gust Impulse Residue Magnitudes - Config. 5 47   
4.15 Gust Impulse Residue Magnitudes - Config. 6 48   
4.16 Gust Impulse Residue Magnitudes - Config. 7 49   
4.17 Gust Impulse Residue Magnitudes - Config. 8 50   
5.1 Neal-Smith Model Structure 54   
5.2 Frequency Response Specifications 55   
5.3 Neal-Smith Criteria 57   
5.4 OCM Block Diagram 59   
5.5 Resonance Peak Adjustment 62   
5.6 Neal-Smith/Bacon Pilot Compensation 63   
5.7 Neal-Smith/Bacon Criteria 64   
5.8 Pilot Rating versus Bandwidth for Neal-Smith/Bacon Configurations 65   
5.9 SP versus PC for Neal-Smith Configurations 69   
5.10 Dynamics of Neal-Smith Configurations 70   
5.11 Dynamics of Flexible Configurations. 71   
5.12 Block Diagram of Tracking Analysis 74

# Figure

5.13 Example: OCM Frequency Response - Config. 8 77   
5.14 PR versus BW for Data Base Configurations 81   
5.15 SP versus PC for Data Base Configurations 83

# Appendix Figure

A.4.1 Mode Shape Sign Conventions 246   
A.4.2 Aeroelastic-Structural Mode Shape - Mode 1. 247   
A.4.3 Aeroelastic-Structural Mode Shape - Mode 2. 248   
A.4.4 Aeroelastic-Structural Mode Shape - Mode 3. 249   
A.4.5 Aeroelastic-Structural Mode Shape - Mode 4. 250   
A.5.1 OCM Frequency Responses - Config. 1. 252   
A.5.2 OCM Frequency Responses - Config. 2. 256   
A.5.3 OCM Frequency Responses - Config. 3. 260   
A.5.4 OCM Frequency Responses - Config. 4. 264   
A.5.5 OCM Frequency Responses - Config. 5. 268   
A.5.6 OCM Frequency Responses - Config. 6. 272   
A.5.7 OCM Frequency Responses - Config. 7 276   
A.5.8 OCM Frequency Responses - Config. 8. 280

# LIST OF SYMBOLS

# Symbol

# Meaning

A. plant matrices

$\mathbf{B}_{(1)}$ control matrices

B modal controllability matrix

BW. bandwidth frequency

C....output matrix (for states)

$\bar{\mathbf{C}}$ modal observability matrix

$\mathbf{D}_{()}$ .disturbance matrices

D modal disturbability matrix

E....output matrix (for controls)

F .output matrix (for disturbances)

$\mathbf{G}_{(\cdot)}$ control matrices

G(s) plant transfer functions

II(s) . pilot transfer function

Jp .pilot objective functional

$K_{p}$ . pilot gain (feedforward)

$\mathbf{K}_{x}$ optimal control gains

$\Delta K$ incremental change in pilot gain $\mathbf{K}_{\mathfrak{p}}$

OCM. Optimal Control Model of the pilot

P.C. pilot compensation

Q. weighting matrix for output vector

R(·) impulse residue

SP .sensitivity parameter

T...... modal matrix

$\overline{\mathbf{V}}_{(\cdot)}$ .. intensity of white noise $(\cdot)$

g....weighting on pilot input rate $(\dot{u}_p)$

$\mathbf{l}_{\mathbf{x}}$ distance from c.g. to pilot station

# Symbol

# Meaning

$\mathbf{n}_{2}$ . plunge acceleration (g's)

$\mathbf{P}(\cdot)$ . pole of a transfer function

q.........modal state vector

weighting on pilot input $(\mathfrak{u}_{\mathfrak{p}})$

u............perturbed forward velocity (ft/sec)

u.......input vector

$\mathbf{v}_{\mathfrak{m}}$ . motor noise

$\mathbf{v}_{\mathbf{y}}$ . observation ncise

w. Gaussian white noise

w............disturbance vector

X..state vector

$\dot{\mathbf{x}}$ ..state estimate vector

y....output vector

$\mathbf{z}_{(\cdot)}$ zero of a transfer function

$\Phi_{(\cdot)}$ phase of impulse residue, $\mathbf{R}_{(\cdot)}$

$\pmb{\alpha}$ angle of attack, (rad)

$\gamma$ flight path angle, (rad)

$\delta_{(\cdot)}$ control surface deflection

$\epsilon$ ...attitudetrackingerror $(\theta -\theta_{\mathrm{C}})$

damping ratio

$\pmb{\eta}$ …generalizeddeflection,(dimensionless)

$\theta_{(\cdot)}$ ... attitude angle, (rad)

$\lambda_{(1)}$ . eigenvalue

$\nu_{(\cdot)}$ . eigenvector

$\xi$ damping ratio

real part of eigenvalue, $\pmb{\lambda}$

$\pmb{\tau}$ time delay, (sec)

$\pmb{\tau}_{\mathfrak{n}}$ .neuro-motor lag, (sec)

$\phi_{(\cdot)}$ mode shape, (ft)

$\phi^{\prime}(\cdot)$ mode slope, (ft/ft)

$\omega$ .imaginary part of eigenvalue, $\lambda$

xi

Symbol

Meaning

operations

$\mathbf{E}\{\cdot \}$ ...expected value operator

$\mid \cdot \mid$ ..magnitude of (·)

[7] .complex conjugate of (·)

$\angle (\cdot)$ . phase angle of $(\cdot)$

(·) time derivative of (·)

subscripts

C.......commanded

R. rigid-body

T. total (rigid-body + elastic)

g... .gust

p... .pilot

v.......vehicle

y....output or measurement

# SUMMARY

As aircraft become larger and lighter due to design requirements for increased payload and improved fuel efficiency, they may also become much more flexible. For highly flexible vehicles, the handling qualities may not be accurately predicted by conventional methods. This study applies two analysis methods to a family of flexible aircraft in order to investigate how and when structural (especially dynamic aeroplastic) effects affect the dynamic characteristics of aircraft. The first type of analysis is an open-loop modal analysis technique. This method considers the effect of modal residue magnitudes on determining vehicle handling qualities. The second method is a pilot-in-the-loop analysis procedure that considers several closed-loop system characteristics. Both analyses indicated how dynamic aeroplastic effects can cause a degradation in vehicle tracking performance, based on the evaluation of some simulation results.

This report is divided into two volumes. Volume I consists of the development and application of the two analysis methods described above. Volume II consists of the presentation of the state variable models of the flexible aircraft configurations used in the analysis applications, mode shape plots for the structural modes, numerical results from the modal analysis, frequency response plots from the pilot-in-the-loop analysis and a listing of the modal analysis computer program.

# CHAPTER I INTRODUCTION

Usually, the attitude dynamics and handling qualities of aircraft are defined in terms of rigid-body modal characteristics. For example, the frequency and damping of the short-period and phugoid modes are used for handling qualities specifications of the longitudinal dynamics of aircraft [1]. This is possible, not because the aircraft are actually rigid, but because they are "rigid enough" so that structural effects can be ignored. It has been shown, however, that this approach may not be very accurate for aircraft with significant amounts of structural flexibility [2]. Since, in the future, aircraft will become larger and lighter due to design requirements of increased payload and improved fuel efficiency, they may also become much more flexible. In addition to the rigid-body modes, flexible aircraft have aeroelastic-structural modes which may significantly affect their dynamic characteristics. Analysis of the dynamics of these aircraft, without considering the contribution of the structural modes, would be inaccurate. Any use of such an analysis, in flight control designs for example, could produce poor, if not disastrous results [3].

At present there is no universally accepted way to predict the handling characteristics of an aircraft in which structural flexibility is significant. Further, there is a need to describe qualitatively, the significance of structural effects. The goal of this research, then, is to address the questions of when and how do structural effects (especially dynamic aeroelastic effects) significantly affect the dynamic characteristics of aircraft? Answering these questions is the first step in developing a systematic approach to analyzing flexible aircraft handling qualities and synthesizing appropriate flight control laws.

This report is divided into the following chapters that present the development and application of the analysis "tools". Chapter 2 uses pole-zero plots and transfer functions of flexible aircraft to provide background on why structural effects can be significant and therefore explains why they need consideration. Chapter 3 presents the family of vehicle configurations which will be used throughout the analysis. In Chapter 4, an open-loop analysis

technique is developed and applied to the vehicle configurations which are presented in Chapter 3. Chapter 5 presents the application of a closed-loop pilot/vehicle analysis method to the vehicle configurations from Chapter 3. In conclusion, Chapter 6 presents a summary of the results and conclusions based on those results.

# CHAPTER II BACKGROUND

When the vibrational frequencies of an aircraft structure are large compared to the frequencies of the rigid-body modes, the effect of the flexible modes on the overall dynamic response of the aircraft is small. This is the situation for most aircraft and, as will be seen, allows the dynamics to be accurately modeled by the rigid-body modes only. However, as the frequencies of the structural modes become lower, the effect of these modes on the dynamics can become significant.

For example, consider the attitude response of an hypothetical aircraft due to elevator deflection by studying the transfer function $\left(\frac{\theta(s)}{\delta_E(s)}\right)$ , or the pole-zero plot corresponding to this transfer function. Figure 2.1 shows a typical pole-zero plot of the longitudinal attitude response transfer function where the poles and zeros of the phugoid and short-period modes and the first few structural modes are included. Four poles and two zeros may be considered to be associated with the phugoid and short-period modes. Typically, the poles are complex conjugates and the zeros are real. Note also that there is a pole-zero "dipole" associated with each of the structural modes. The poles and the zeros are complex for these modes.

Although a real aircraft, like any structure, has an infinity of vibrational modes, for ease of discussion the example used here will consider only one of the structural modes. To further simplify the discussion, the phugoid mode will also be omitted, that is, the "short-period approximation" is invoked.

The pole-zero plot simplifies to Figure 2.2 when the above simplifications are applied. The transfer function associated with this simplified case appears in Equation (2.1).

图片摘要：该图主要展示 2.1。
![](images/f6f7a92a62d521c03dd991b3eef089d18da675d7c4274cff18342e9ba79e3764.jpg)  
Figure 2.1   
Pole-Zero Plot of Typical Flexible Aircraft

图片摘要：该图主要展示 2.1。
![](images/f1245c171d42036698d2d8a5d0dbd106c1a5b01d361f6133659bfcb2d5b895d0.jpg)  
Figure 2.2   
Poie-Zero Plot of Simple Example

$$
\frac {\theta (s)}{\delta_ {E} (s)} = \frac {\left(s - z _ {s p}\right) \left(s - z _ {1}\right) \left(s - \bar {z} _ {1}\right)}{s \left(s - p _ {s p}\right) \left(s - \bar {p} _ {s p}\right) \left(s - p _ {1}\right) \left(s - \bar {p} _ {1}\right)} \tag {2.1}
$$

- where $(\neg)$ denotes the conjugate of $(\cdot)$ . Equivalently, the transfer function for pitch rate due to elevator input is,

$$
\frac {\dot {\theta} (s)}{\delta_ {E} (s)} = \frac {(s - z _ {s p}) (s - z _ {1}) (s - \bar {z} _ {1})}{(s - p _ {s p}) (s - \bar {p} _ {s p}) (s - p _ {1}) (s - \bar {p} _ {1})} \tag {2.2}
$$

The pitch-attitude-rate response of the aircraft due to an impulsive input is therefore,

$$
\dot {\theta} (s) = \frac {\left(s - z _ {s p}\right) \left(s - z _ {1}\right) \left(s - \bar {z} _ {1}\right)}{\left(s - p _ {s p}\right) \left(s - \bar {p} _ {s p}\right) \left(s - p _ {1}\right) \left(s - \bar {p} _ {1}\right)}. \tag {2.3}
$$

The following form of the attitude-rate response results from the partial fraction expansion of Equation (2.3) and transformation into the time domain.

$$
\dot {\theta} (t) = R _ {s p} e ^ {p _ {s p} t} + \bar {R} _ {s p} e ^ {\bar {p} _ {s p} t} + R _ {1} e ^ {p _ {1} t} + \bar {R} _ {1} e ^ {\bar {p} _ {1} t} \tag {2.4}
$$

Here $\mathbf{R}_i$ is the residue associated with pole $p_i$ , and $\overline{\mathbf{R}}_i$ is its conjugate. For complex poles, the residues are complex numbers with magnitudes that determine the degree to which each mode contributes to the overall response. Therefore, the significance of an individual mode in the dynamics of the aircraft is represented by the residue magnitude of that mode. This can be illustrated by writing Equation (2.4) in the form,

$$
\begin{array}{l} \dot {\theta} (t) = 2 \left| R _ {s p} \right| e ^ {\sigma_ {s p} t} \cos \left(\omega_ {s p} t + \Phi_ {s p}\right) \\ + 2 \left| R _ {1} \right| e ^ {\sigma_ {1} t} \cos \left(\omega_ {1} t + \Phi_ {1}\right). \tag {2.5} \\ \end{array}
$$

$$
- w h e r e p _ {i} = \sigma_ {i} + j \omega_ {i},
$$

$$
\begin{array}{l} \Phi_ {i} = \tan^ {- 1} \left\{\frac {\operatorname {I m} \left(R _ {i}\right)}{\operatorname {R e} \left(R _ {i}\right)} \right\}, \\ \left| R _ {i} \right| = \left\{\left[ R e \left(R _ {i}\right) \right] ^ {2} + \left[ I m \left(R _ {i}\right) \right] ^ {2} \right\} ^ {1 / 2}. \\ \end{array}
$$

The residue magnitudes can be interpreted geometrically in terms of the poles and zeros of Figure 2.2 by considering the following relations [4],

$$
\left| R _ {s p} \right| = \frac {\left| z _ {s p} - p _ {s p} \right| \cdot \left| z _ {1} - p _ {s p} \right| \cdot \left| \bar {z} _ {1} - p _ {s p} \right|}{\left| \bar {p} _ {s p} - p _ {s p} \right| \cdot \left| p _ {1} - p _ {s p} \right| \cdot \left| \bar {p} _ {1} - p _ {s p} \right|}, \tag {2.6}
$$

and,

$$
\left| R _ {s p} \right| = \frac {\left| z _ {1} - p _ {1} \right| \cdot \left| z _ {1} - p _ {1} \right| \cdot \left| \bar {z} _ {1} - p _ {1} \right|}{\left| p _ {s p} - p _ {1} \right| \cdot \left| \bar {p} _ {s p} - p _ {1} \right| \cdot \left| \bar {p} _ {1} - p _ {1} \right|}. \tag {2.7}
$$

and from symmetry of the pole-zero plot, $|\mathbf{R}_i| = |\overline{\mathbf{R}}_i|$ . Here $|\cdot|$ denotes the magnitude of a complex number and so $|z_1 - p_1|$ is the distance from the point $z_1$ to the point $p_1$ .

If the hypothetical aircraft was fairly rigid, the poles and zeros associated with the structural mode would be far from the origin when compared to the poles and zero associated with the short-period mode. This implies that,

$$
\left| z _ {1} - p _ {s p} \right| \simeq \left| p _ {1} - p _ {s p} \right| \tag {2.8}
$$

and,

$$
\left| \bar {z} _ {1} - p _ {s p} \right| \simeq \left| \bar {p} _ {1} - p _ {s p} \right|. \tag {2.9}
$$

In this case, the expression for the residue magnitudes associated with the short-period mode can be simplified by the effective cancellation of terms involving $\mathbf{z}_1$ and $\mathbf{p}_1$ from the numerator and the denominator so that the short-period residue magnitudes are relatively independent of the structural mode, or,

$$
\left| \mathrm {R} _ {\mathrm {s p}} \right| \simeq \frac {\left| z _ {\mathrm {s p}} - \mathrm {p} _ {\mathrm {s p}} \right|}{\left| \bar {\mathrm {p}} _ {\mathrm {s p}} - \mathrm {p} _ {\mathrm {s p}} \right|}. \tag {2.10}
$$

Similarly, for a fairly rigid aircraft, the zero near a pole associated with the structural mode is much closer to that pole than any other pole or zero of the system. Also, the distance from that pole to its complex conjugate is approximately equal to the distance to the zero associated with that conjugate pole (i.e. the zero of the pole-zero dipole). These two statements imply that,

$$
\left| z _ {1} - p _ {1} \right| \ll \left| p _ {s p} - p _ {1} \right|, \tag {2.11}
$$

$$
\left| z _ {1} - p _ {1} \right| \ll \left| \bar {p} _ {\mathrm {s p}} - p _ {1} \right|, \tag {2.12}
$$

and,

$$
\left| \bar {z} _ {1} - p _ {1} \right| \simeq \left| \bar {p} _ {1} - p _ {1} \right|. \tag {2.13}
$$

Here, the residue magnitudes associated with the structural mode can be simplified, using Equation (2.13), to obtain the following expression.

$$
\left| R _ {1} \right| \simeq \frac {\left| z _ {s p} - p _ {1} \right| \cdot \left| z _ {1} - p _ {1} \right|}{\left| p _ {s p} - p _ {1} \right| \cdot \left| \bar {p} _ {s p} - p _ {1} \right|} <   <   1. \tag {2.14}
$$

It is clear, by applying Equations (2.11) and (2.12), that the structural mode residue magnitude is much less than unity. Since the short-period mode residue magnitude is on the order of unity, it is obvious that

$$
\left| \lambda_ {1} \right| \ll \left| R _ {\text {s p}} \right|. \tag {2.15}
$$

As a result of this discussion, two conclusions can be drawn concerning fairly rigid aircraft. First, the structural modes have little affect on the degree to which the rigid-body modes contribute to the dynamic response of the vehicle. And second, the contribution of the structural modes to the dynamic response of the vehicle is insignificant compared to the affect of the rigid-body modes. Therefore, the longitudinal attitude-rate impulse response of the aircraft can be accurately approximated by the following expression.

$$
\dot {\theta} (t) \simeq 2 \left| R _ {s p} \right| e ^ {\sigma_ {s p} t} \cos \left(\omega_ {s p} t + \Phi_ {s p}\right) \tag {2.16}
$$

The implication of this expression is that, when it is valid, the dynamics of the aircraft are determined almost entirely by the values of the rigid-body poles and zeros.

However, if the amount of flexibility is significant enough so that Equations (2.8), (2.9), (2.11) and (2.12) are no longer valid, the conclusions above will no longer apply. In this case, the degree to which the rigid-body modes contribute to the overall response will depend somewhat on the characteristics of the structural modes. In addition, the contribution of the structural modes to the response may be significant.

# CHAPTER III EXPERIMENTAL DATA BASE

A set of aircraft dynamic models, one of which is similar to the B-1 bomber, were available from a previous study [2]. The B-1 is a large aircraft with a reasonable amount of structural flexibility. Figure 3.1 is a sketch that depicts the geometry of the aircraft that corresponds to all the vehicle models to be considered. The models represent a family of aircraft similar to the B-1 that differ only in their amount of structural rigidity, quantified in terms of the invacio-structural vibration frequencies. The configurations can be described physically as vehicles with identical geometries but made of different materials so that the vibration frequencies are changed while the vibration mode shapes remain unchanged.

The mathematical models of the aircraft include two structural modes which correspond to the first fuselage bending mode and the second fuselage bending mode. The mode shapes which correspond to these aeroelastic-structural modes can be found in Appendix A.4. The family of configurations were generated by parametrically varying the invacuo-structural frequencies of the two structural modes. Table 3.1 summarizes the eight configurations, listing their eigenvalues and the invacuo-vibration frequencies of the two structural modes.

Notice that for configurations 6, 7 and 8 the second acroelastic mode is slightly unstable due to negative aerodynamic damping. The original simulation study [2] involved considering the effect of neutrally stable modes on vehicle dynamics. To study this effect, the very slightly unstable (i.e. effectively neutrally stable) configurations 6, 7 and 8 were developed.

The complete mathematical model of the eight configurations in state variable form corresponding to Equation (3.1) can be found in Appendix A.3.

图片摘要：该图主要展示 3.1。
![](images/463327fe3700aa66a9a589cd7dbadbee5d43a62f9f137c09b62b4b155598e0b5.jpg)  
Figure 3.1   
Geometry of Data Base Configurations

$$
\dot {\mathbf {x}} _ {\mathbf {v}} = \mathbf {A} _ {\mathbf {v}} \mathbf {x} _ {\mathbf {v}} + \mathbf {B} _ {\mathbf {v}} \mathbf {u} + \mathbf {D} _ {\mathbf {v}} \mathbf {w} \tag {3.1}
$$

- where $\mathbf{x}_{\mathbf{v}}$ is the vector of vehicle states and $\mathbf{A}_{\mathbf{v}}, \mathbf{B}_{\mathbf{v}}$ and $\mathbf{D}_{\mathbf{v}}$ are system matrices, $\mathbf{u}$ is the vector of control inputs and $\mathbf{w}$ is the vector of disturbances.

Table 3.1 Summary of Data Base Configurations   

<table><tr><td></td><td colspan="2">INVACUO
MODE FREQ&#x27;S (Hz)</td><td colspan="4">AEROELASTIC VEHICLE
MODE EIGENVALUES</td></tr><tr><td>CONFIG</td><td>MODE
1</td><td>MODE
2</td><td>PHUGOID</td><td>SHORT
PERIOD</td><td>MODE
1</td><td>MODE
2</td></tr><tr><td>1</td><td>2.18</td><td>3.37</td><td>-0.0015
±j0.067</td><td>-1.5
±j2.37</td><td>-0.66
±j13.3</td><td>-0.46
±j21.3</td></tr><tr><td>2</td><td>1.46</td><td>3.37</td><td>0.001
±j0.053</td><td>-1.35
±j2.2</td><td>-0.73
±j8.76</td><td>-0.46
±j21.3</td></tr><tr><td>3</td><td>0.97</td><td>3.37</td><td>-0.08;
0.095</td><td>-0.9
±j1.5</td><td>-1.11
±j5.7</td><td>-0.46
±j21.3</td></tr><tr><td>4</td><td>2.18</td><td>0.76</td><td>-0.13;
0.15</td><td>-1.06
±j1.1</td><td>-0.7
±j13.3</td><td>-0.53
±j5.9</td></tr><tr><td>5</td><td>1.86</td><td>1.86</td><td>-0.001
±j0.049</td><td>-1.4
±j2.17</td><td>-0.86
±j11.7</td><td>-0.12
±j11.6</td></tr><tr><td>6</td><td>1.10</td><td>1.10</td><td>-0.15;
0.18</td><td>-0.95
±j0.97</td><td>-1.31
±j7.16</td><td>0.057
±j7.0</td></tr><tr><td>7</td><td>1.63</td><td>1.55</td><td>0.001
±j0.017</td><td>-1.32
±j2.0</td><td>-1.1
±j10.2</td><td>0.085
±j9.9</td></tr><tr><td>8</td><td>1.70</td><td>1.48</td><td>0.0013
±j0.012</td><td>-1.3
±j2.0</td><td>-1.08
±j10.3</td><td>0.085
±j9.8</td></tr></table>

In the previous study [2], the above vehicle configurations were used in a fixed based, laboratory simulation involving longitudinal tracking of a low frequency command signal. A cathode ray tube was used to display the following variables; commanded attitude angle, $\theta_{\mathbf{C}}$ , and vehicle attitude angle, $\theta_{\mathbf{T}}$ , measured at the cockpit location. The vehicle attitude angle is the pitch attitude measured, for example, by a gyro located at the cockpit and differs from the rigid vehicle pitch angle, $\theta_{\mathbf{R}}$ , by the contribution of the local structural deflections. This effect is illustrated in Figure 3.2 and defined by Equation (3.2).

图片摘要：该图主要展示 3.2 Rigid and Elastic Pitch Angles。
![](images/1987742223e69e0450dbbb82736865f362bb889120b959d5c1011dc34f170af5.jpg)  
Figure 3.2 Rigid and Elastic Pitch Angles

$$
\theta_ {1} (t) = \theta_ {R} (t) - \sum_ {i = 1} ^ {\prime \prime} \phi_ {i} ^ {\prime} \left(l _ {x}\right) \eta_ {i} (t) \tag {3.2}
$$

- where $l_{x}$ is the cockpit location measured from the center of gravity, $\phi_{i}'$ is the mode slope of the ith elastic mode and $\eta_{i}$ is the generalized coordinate of the ith elastic mode [5].

The above information was displayed to the pilot by means of a visual display similar to the one depicted in Figure 3.3. His task was simply to minimize the error between the commanded and the indicated attitudes angles.

Three types of data were collected from the simulations: 1) rms tracking error (taken over a 120 second run for each case); 2) Cooper-Harper [6] pilot rating in the tracking task $^{+}$ ; and 3) pilot comments. A summary of these results can be found in Table 3.2. These results indicate that flexible aeroelastic effects significantly affected pitch attitude tracking performance.

Table 3.2 Summary of Tracking Error, Pilot Rating and Pilot Comments   

<table><tr><td>CONFIG</td><td>RMS Tracking Error (d·g)</td><td>RMS Pilot Rating</td><td>Pilot Comments</td></tr><tr><td>1</td><td>1.15</td><td>1.6</td><td>Good; no problem</td></tr><tr><td>2</td><td>1.05</td><td>2.0</td><td>little oscillation; slight control response lag</td></tr><tr><td>3</td><td>5.67</td><td>5.9</td><td>difficult; PIO problem; extreme response lag</td></tr><tr><td>4</td><td>1.90</td><td>3.1</td><td>little more difficult than C1; sluggish attitude response</td></tr><tr><td>5</td><td>1.51</td><td>2.0</td><td>pretty good; same as C2</td></tr><tr><td>6</td><td>7.57</td><td>6.7</td><td>severe oscillation; virtually uncontrollable</td></tr><tr><td>7</td><td>1.48</td><td>2.3</td><td>not difficult; annoying oscillation</td></tr><tr><td>8</td><td>1.16</td><td>1.9</td><td>not difficult; little oscillation but could ignore it and fly rigid body</td></tr></table>

note: These results are for 4 pilots with 2 runs per pilot.

Before introducing the analysis methods, the simulation results, which are summarized in Figures 3.4 and 3.5, will be reviewed. It is clear that aeroelastic

图片摘要：该图主要展示 3.2 Summary of Tracking Error, Pilot Rating and Pilot Commen。
![](images/4c1da994d0e36d8c41ac7b74450930a317d33cade2bf635b2b0134584f2a998e.jpg)  
Figure 3.3   
Simulation Visual Display

图片摘要：该图主要展示 3.3。
![](images/c96e7f93d7a9ac666a1c8aebbe34453a5daaa2dd1e1720f6acfafc0723a67fa6.jpg)  
Figure 3.4   
Simulation Tracking Errors

level 1 - good

level 2 - fair

level 3 - poor

图片摘要：该图主要展示 3.5。
![](images/6a9db2dc7e1774bfb3e45e1fd91ebac76b72594bc49539288bf49c16965333cc.jpg)  
Figure 3.5   
Simulation Pilot Ratings

effects significantly affected vehicle dynamics. By merely varying invacuo-structural frequencies, the dynamics changed so drastically that two configurations (3 and 6) received Level 3 ratings while the others received Level 1 ratings. Once again the question to be answered is, "when and how do these aeroelastic effects affect aircraft dynamics?"

Note that the "rigid-body" phugoid and short-period eigenvalues alone give little insight into the effect of reducing the invacio-structural frequencies (see Table 3.1). For example, Configuration 3 has a much higher (worse) Cooper-Harper rating and larger tracking errors than Configuration 4 despite the fact that Configuration 3 has a more stable phugoid mode and only a slightly higher frequency associated with the short-period mode. In addition, Configurations 3 and 4 have similar lowest-frequency aeroelastic mode eigenvalues. Based on this, one might predict that Configuration 4 should be worse than Configuration 3, which is contrary to the simulation results. Thus, the eigenvalues alone do not completely capture the actual dynamics of a vehicle.

# CHAPTER IV OPEN-LOOP MODAL ANALYSIS

A modal analysis of the family of aircraft presented in Chapter 3 will be presented. The results of this analysis will be used to help explain some of the findings which were obtained in the simulation of those dynamic configurations. These results will also be used to answer the questions posed earlier - namely, when and how do structural effects significantly affect the dynamics of aircraft?

# Modal Analysis

Consider the vehicle modeled in the state variable form,

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} + \mathbf {D} \mathbf {w}
$$

(4.1)

$$
\mathbf {y} = \mathbf {C} _ {\mathbf {x}} + \mathbf {E} _ {\mathbf {u}} + \mathbf {F} _ {\mathbf {w}}
$$

Here $\mathbf{x}$ is a vector of vehicle states, $\mathbf{y}$ is a vector of outputs and $\mathbf{u}$ and $\mathbf{w}$ are vectors of control inputs and disturbances, respectively.

One may diagonalize the system using the modal transformation [4,5], where the modal matrix, $\mathbf{T}$ , is formed from the eigenvectors of $\mathbf{A}$ (assuming distinct eigenvalues), so that

$\mathbf{T}\triangleq \{\varkappa_1,\varkappa_2,\dots ,\varkappa_n\} .$ (4.2)

Here $\pmb{\nu}_{\mathbf{i}}$ is the eigenvector associated with the ith eigenvalue of $\pmb{A}$ . In terms of the modal states, the system dynamics are,

$$
\dot {\mathbf {q}} = \mathbf {A} \mathbf {q} + \bar {\mathbf {B}} \underline {{\mathbf {u}}} + \bar {\mathbf {D}} \underline {{\mathbf {w}}},
$$

(4.3)

$$
\mathbf {y} = \tilde {\mathbf {C}} \mathbf {q} + \mathbf {E} \mathbf {u} + \mathbf {F} \mathbf {w}.
$$

Here $\mathbf{q}$ is the vector of modal coordinates, $\mathbf{A} \triangleq \mathbf{T}^{-1}\mathbf{A}\mathbf{T}$ (diagonal), $\tilde{\mathbf{B}} \triangleq \mathbf{T}^{-1}\mathbf{B}$ , $\tilde{\mathbf{D}} \triangleq \mathbf{T}^{-1}\mathbf{D}$ and $\tilde{\mathbf{C}} \triangleq \mathbf{C}\mathbf{T}$ . The matrices $\tilde{\mathbf{B}}, \tilde{\mathbf{C}}$ and $\tilde{\mathbf{D}}$ are called the modal controllability, turbidity and observability matrices, respectively. With proper vehicle state definitions, elements of these matrices indicate how controllable, combustible and observable each mode is, with respect to the inputs and outputs. Each element of the modal controllability matrix, for example, is a relative measure of how much the associated control input contributes to the response of the corresponding mode. If the magnitude of one element of the modal controllability matrix is small compared to the magnitudes of the other elements of the controllability matrix then the mode in question is "relatively uncontrollable" from that input.

At this point, to simplify the development, one may redefine the input vector as,

$$
\bar {u} \triangleq \left[ \begin{array}{l} u \\ w \end{array} \right]. \tag {4.4}
$$

Substituting this into Equation (4.3) results in,

$$
\dot {\mathbf {q}} = \boldsymbol {\Lambda} \mathbf {q} + \tilde {\mathbf {B}} \bar {\mathbf {u}}
$$

(4.5)

$$
\mathbf {y} = \tilde {\mathbf {C}} \mathbf {q} + \mathbf {E} \bar {\mathbf {u}},
$$

where $\tilde{\mathbf{B}}\triangleq \begin{bmatrix} \tilde{\mathbf{B}}\\ \tilde{\mathbf{D}} \end{bmatrix}$ and $\mathbf{E}\triangleq \begin{bmatrix} \mathbf{E}\\ \mathbf{F} \end{bmatrix}$

The diagonal property of $\pmb{\Lambda}$ is especially useful when considering the system in the frequency domain, or,

$$
[ s \mathbf {I} - \boldsymbol {\Lambda} ] q (c) = \tilde {\mathbf {B}} \bar {\mathbf {u}} (s),
$$

(4.6)

$$
\mathbf {x} (s) = \tilde {\mathbf {C}} \mathbf {q} (s) + \mathbf {E} \bar {\mathbf {u}} (s).
$$

Since the identity matrix, $\mathbf{I}$ , and $\pmb{\Lambda}$ are diagonal and square, the inverse of $[\mathbf{sI} - \mathbf{A}]$ is diagonal as well. By multiplying the first of Equations (4.6) by $[\mathbf{sI} - \mathbf{A}]^{\dagger}$ and substituting into the second of Equations (4.6), the following matrix equation for the outputs $\pmb{\nu}$ results.

$$
\mathbf {y} (\mathrm {s}) = \tilde {\mathbf {C}} [ \mathrm {s I} - \boldsymbol {\Lambda} ] ^ {1} \tilde {\mathbf {B}} \bar {\mathbf {u}} (\mathrm {s}) + \mathbf {E} \bar {\mathbf {u}} (\mathrm {s}) \tag {4.7}
$$

By writing the elements of $\tilde{\mathbf{C}}$ as $c_{ij}$ (i the row and j the column), the elements of $\tilde{\mathbf{B}}$ and $\mathbf{E}$ as $b_{ij}$ and $e_{ij}$ , respectively, and by using the fact that $[\mathbf{sI} - \mathbf{A}]^{\dagger}$ is diagonal, the transfer function for the ith output due to the jth input, $\left(\frac{y_j(s)}{u_j(s)}\right)$ , can be written as,

$$
\frac {y _ {i} (s)}{u _ {j} (s)} = \sum_ {k = 1} ^ {n} \frac {c _ {i k} \cdot b _ {k j}}{s - \lambda_ {k}} + c _ {i j}. \tag {4.8}
$$

Here $n$ is the number of system states and $\lambda_{k}$ is the $k$ th eigenvalue of the system.

From Equation (4.8) the impulse response of $\mathbf{y}_i$ can be obtained by assuming $u_j$ to be an impulse and taking the inverse Laplace transform. The impulse response of $\mathbf{y}_i$ becomes,

$$
y _ {i} (t) = \sum_ {k = 1} ^ {n} c _ {i k} \cdot b _ {k j} \exp (\lambda_ {k} t) + c _ {i j}. \tag {1.0}
$$

Note that the values of $c_{ik} \cdot b_{kj}$ are the values of the residues associated with mode $k$ ( $k = 1,2,\ldots,n$ ) for the $i$ th output ( $y_i$ ), when the system is excited by the $j$ th input ( $u_j$ ). This relationship results from the definition of a "residue" [4] and Equations (4.8) and (4.9) so that,

$$
\left. \mathrm {R} _ {\mathbf {k}} \right| _ {\left(\mathrm {y}, \mathrm {u},\right)} = \mathrm {c} _ {\mathrm {i k}} \cdot \mathrm {b} _ {\mathrm {k j}}. \tag {4.10}
$$

Therefore, the information reflected in the controllability, disturbance and observability of a mode is also completely contained in the modal residues. Equation (4.9) can therefore be written as,

$$
y _ {i} (t) = \sum_ {k = 1} ^ {n} R _ {k} \exp \left(\lambda_ {k} t\right) + e _ {i j}. \tag {4.11}
$$

- where $n$ is the number of system poles. By representing the residue in terms of its magnitude and phase and combining terms involving complex conjugates, Equation (4.11) can be written as,

$$
y _ {i} (t) = \sum_ {k = 1} ^ {m} 2 | R _ {k} | e ^ {- \sigma_ {k} t} \cos \left(\omega_ {k} t + \Phi_ {k}\right) + e _ {i j}. \tag {4.12}
$$

- where $\mathfrak{m}$ is the number of modes of the system (i.e. $\mathfrak{m} = \mathfrak{n}/2$ ) and all eigenvalues are assumed to be complex for ease of discussion. As discussed in Chapter 2 and clearly from the above equation, the magnitude of the residue of a mode is a direct measure of the contribution of that mode to the dynamic response of the vehicle. From Equation (4.12), the relative importance of each mode to a given response can be determined by inspection. By numerically implementing this analysis, it is possible to investigate how higher order modes directly affect the dynamic response of an aircraft by comparing impulse residue magnitudes.

The results of the modal analysis as developed above include the eigenvalues and eigenvectors of the system. The eigenvectors are used to determine which mode of the dynamics is associated with each generalized coordinate of the system. It should be noted that when the term "rigid-body mode" is used it means the system mode whose eigenvector reflects significant participation of the rigid-body states (e.g. attitude, attitude rate and angle of attack). Similarly, the term "elastic mode" is used to mean a system mode whose eigenvector reflects significant participation of the elastic states (i.e. $\eta_{\mathrm{i}}$ , $\dot{\eta}_{\mathrm{i}}$ ). In the application to flexible aircraft, there are no truly rigid-body modes or purely structural modes due to aeroelastic coupling.

The manner in which the modes of the dynamics associated with the generalized coordinates are identified can best be explained through example.

Consider the data presented in Table 4.1 which represents the two rigid-body modes of the Navion aircraft [7]. The magnitude of the element associated with attitude rate, $\dot{\theta}$ , in the first eigenvector is larger than the elements associated with the other states. This indicates that the mode associated with the first eigenvector primarily contains attitude rate and therefore, corresponds to the short-period mode. Similarly, for the second eigenvector, the magnitude of the element associated with forward velocity perturbation, u, is larger than the other elements and so, that mode corresponds to the phugoid mode. This technique was used to identify the vehicle modes for the configurations used in this study.

Table 4.1 Summary of Navion Longitudinal Dynamics   

<table><tr><td colspan="4">Flight Condition: Sea Level
U = 176.0 ft/sec
W = 1.84 ft/sec
State Vector: xT △ [u, w, ð, θ]</td></tr><tr><td colspan="3"></td><td>units</td></tr><tr><td>eigenvalues</td><td>-2.51
± j2.59</td><td>-0.017
± j0.213</td><td>sec-1</td></tr><tr><td rowspan="4">eigenvectors</td><td>-0.003
± j0.019</td><td>1.0</td><td>ft·sec-1</td></tr><tr><td>-0.120
± j0.656</td><td>-0.059
± j0.001</td><td>ft·sec-1</td></tr><tr><td>1.0</td><td>0.143
± j0.009</td><td>10-2 rad/sec</td></tr><tr><td>-0.193
± j0.199</td><td>-0.094
± j0.662</td><td>10-2 rad</td></tr></table>

Notice that, in the example, the units of the elements of the eigenvector are not the same. Two of the elements have units of feet per second and the other two have units of $10^{-2}$ radians per second and $10^{-2}$ radians, respectively. This set of units enable the modes of the system to be readily identified. Since the magnitude of an element of an eigenvector is dependent on the units selected for the system states, proper choice of the units can aid in identifying the modes of the system. In general, the states of a system (and therefore the elements of the eigenvectors) do not have the same physical units. The units can be changed, however, by applying a similarity transformation to the state variable representation of the system. It can be easily shown that a similarity

transformation does not affect the eigenvalues or residues of a system. As a result, a similarity transformation can be applied to the system without altering the modal analysis results. Appendix A.1 presents the development of the transformation used in this study to change the units of the states and eigenvectors to aid in identifying the system modes.

In addition to the eigenvalues and eigenvectors, the modal controllability, turbidity and observability matrices are available from the modal analysis. With proper selection of units (using a similarity transformation), these can be used to gain further information concerning dynamic relationships between the control and disturbance inputs and the system modes, and between the outputs and the system modes as described previously.

The last and most useful of the analysis results are the modal impulse residues, $\mathbf{R}_{\mathrm{i}}$ . The impulse residues are useful since, as noted previously, they are a direct combination of the observability and controllability (or disturbability) of a particular mode. The magnitude of the impulse residues will be used extensively in this study.

# Vehicle Model

The vehicle models considered were those used by Yen [2]. They consist of linear equations of the form -

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} _ {R} \\ \dot {\mathbf {x}} _ {E} \end{array} \right] = \left[ \begin{array}{l l} \mathbf {A} _ {R} & \mathbf {A} _ {C} \\ \mathbf {A} _ {C} ^ {\prime} & \mathbf {A} _ {E} \end{array} \right] \cdot \left[ \begin{array}{l} \mathbf {x} _ {R} \\ \mathbf {x} _ {E} \end{array} \right] + \left[ \begin{array}{l} \mathbf {B} _ {R} \\ \mathbf {B} _ {E} \end{array} \right] \cdot \underline {{\mathbf {u}}} + \left[ \begin{array}{l} \mathbf {D} _ {R} \\ \mathbf {D} _ {E} \end{array} \right] \cdot \underline {{\mathbf {w}}}. \tag {4.13}
$$

The vehicle states include some states which are rigid-body degrees of freedom, $\mathbf{x}_{\mathbb{R}}$ , and others which are the structural degrees of freedom, $\mathbf{x}_{\mathbb{E}}$ . Together these form the partitioned state vector. The system matrices are also partitioned to be consistent with the state vector partition. The sub-matrices with the subscript $\mathbb{R}$ are those associated with the rigid states and the sub-matrices with the subscript $\mathbb{E}$ are those associated with the elastic states. The sub-matrices $\mathbf{A}_{\mathbb{C}}$ and $\mathbf{A}_{\mathbb{C}'}$ relate the cross-coupling between the rigid states and the elastic states.

The modal analysis procedure could be accomplished with the flexible vehicle model described in Equation (4.13) but the results would not be the

most meaningful. This is due to the fact that interpretation of the modal analysis requires extensive use of characteristic parameters that influence the impulse response of the system (i.e. modal controllability, modal observability, residues, etc.) and since an impulse input is unrealistic, these characteristic parameters are unrealistic. Since an impulse is physically unrealizable, impulse responses of an aircraft are unrealistic and do not reflect the dynamics of a vehicle in actual flight. In order to obtain meaningful results from the analysis, inputs should represent important aspects of the actual pilot commands and atmospheric turbulence.

An impulse has infinite bandwidth and cannot be produced by any physical system. A pilot may try to produce an impulse but, due to his limited bandwidth, cannot achieve it. What results is a type of "realistic pulse" input that can be approximated by treating the pilot as a low pass filter (i.e. a first order lag). The input to the filter is an impulse and the resulting output is a finite bandwidth pulse which approximates what a pilot is capable of producing. Equation (4.14) is the state space representation of a low pass filter.

$$
\dot {x} _ {p ^ {-}} = A _ {p} x _ {p} + G _ {p} \eta_ {p} \tag {4.14}
$$

The scalar $\mathbf{x}_{\mathfrak{p}}$ is the "realistic pulse", $\eta_{\mathfrak{p}}$ is the impulsive input, $\mathbf{A}_{\mathfrak{p}} = -\frac{1}{\tau_{\mathfrak{p}}}$ , where $\tau_{\mathfrak{p}}$ is the time constant of the filter, and $\mathbf{G}_{\mathfrak{p}}$ is $\frac{1}{\tau_{\mathfrak{p}}}$ so that the Bode gain of the filter is unity. By using $\mathbf{x}_{\mathfrak{p}}$ as the input to the vehicle model and an impulse as the input to the filter, a realistic response is obtained for the pilot/vehicle system.

The importance of using the low pass filter to obtain meaningful results can be clearly shown by a simple example. Consider a system with two states in modal coordinates -

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} - 1 & 0 \\ 0 & - 1 0 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 1 \\ 1 \end{array} \right] \mathbf {u}, \tag {4.15}
$$

$$
\mathbf {y} = \left[ \begin{array}{l l} 1 & 1 \end{array} \right] \mathbf {x}.
$$

The response of this system to an impulse input, $\mathbf{u} = \delta(t)$ , is,

$$
\left. \mathbf {y} (t) \right| _ {\mathrm {u} = \delta (t)} = e ^ {- t} + e ^ {- 1 0 0 t}. \tag {4.16}
$$

Now consider the same system and let the input, $\mathbf{u}$ , be represented as,

$$
\dot {\mathbf {u}} = - 1 0 \mathbf {u} + 1 0 \eta . \tag {4.17}
$$

That is, u is the output of a low pass filter with a time constant, $\tau_{\mathfrak{p}} = 0.10\mathrm{sec}^{\dagger}$ The system can be reorganized as,

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} \\ \dot {\mathbf {u}} \end{array} \right] = \left[ \begin{array}{c c c} - 1 & 0 & 1 \\ 0 & - 1 0 0 & 1 \\ 0 & 0 & - 1 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} \\ \mathbf {u} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 0 \\ 1 0 \end{array} \right] \eta , \tag {4.18}
$$

$$
\mathbf {y} = \left[ \begin{array}{l l l} 1 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} \\ \mathbf {u} \end{array} \right].
$$

The response of this system to an impulse input, $\pmb{\eta} = \delta(t)$ , is,

$$
\begin{array}{l} \left. \mathbf {y} (t) \right| _ {\eta = \delta (t)} = (1. 1 1) e ^ {- t} \\ + (1. 0 0) e ^ {- 1 0 t} + (0. 1 1) e ^ {- 1 0 0 t}. \tag {4.19} \\ \end{array}
$$

Note the difference between the two responses, Equations (4.16) and (4.19). The unrealizable response (Equation (4.16)) indicates that both modes contribute equally to the overall response, in terms of residue magnitude. The realizable, filtered response (Equation (4.19)) indicates that the fast system mode $(\lambda = -100)$ has a much less significant contribution to the overall response than does the other original system mode $(\lambda = -1)$ . The obvious conclusion is that an impulse input to the system excites the fast mode, but cannot be excited as much by the limited bandwidth filtered impulse. Therefore, the modal analysis

should be performed on the system which includes the low pass filter that more accurately reflects the true inputs that are expected. If the filter is not used, the modal analysis may indicate that certain high frequency modes significantly contribute to the vehicle response when they actually may have insignificant effects.

An argument similar to that used for the pilot commands can be used to justify describing the disturbances produced by the atmosphere in a similar way. Since atmospheric turbulence is an important aircraft disturbance and turbulence is random in nature, these disturbances are modeled stochastically. One commonly used disturbance model is the Dryden Gust Model [7]. The Dryden Model may be expressed in matrix form as,

$$
\lambda_ {g} ^ {T} \triangleq [ \alpha_ {g _ {1}}, \alpha_ {g} ],
$$

(4.20)

$$
\dot {\mathbf {x}} _ {g} = \mathbf {A} _ {g} \mathbf {x} _ {g} + \mathbf {G} _ {g} \eta_ {g}.
$$

The gust state $\alpha_{g}$ is the angle of attack induced by a vertical gust and $\alpha_{g}$ is an additional gust state which is necessary to obtain the proper frequency character of the gust model. The system matrices $\mathbf{A}_{g}$ and $\mathbf{G}_{g}$ (given later) provide the proper characteristics of the random gust response when the "white" noise, $\eta_{g}$ , is the input.

By combining the "pilot equation" and the Dryden Gust Model equation, (Equations (4.14) and (4.20)), with the aircraft, (Equation (4.3)), an augmented flexible aircraft mathematical model is formed. The resulting flexible aircraft model is then composed of a combination of the system matrices from the pilot equation, the gust equation and the flexible vehicle equation, (Equation (4.22)).

$$
\mathbf {x} ^ {T} = \left[ \begin{array}{l l l} \mathbf {x} _ {p} ^ {T}, \mathbf {x} _ {q} ^ {T}, \mathbf {x} _ {v} ^ {T} \end{array} \right] \tag {4.21}
$$

$$
\dot {\boldsymbol {\lambda}} = \left[ \begin{array}{l l l} \boldsymbol {A} _ {p} & 0 & 0 \\ 0 & \boldsymbol {A} _ {g} & 0 \\ \boldsymbol {B} _ {v} & \boldsymbol {D} _ {v} & \boldsymbol {A} _ {v} \end{array} \right] \boldsymbol {\lambda} + \left[ \begin{array}{l} \boldsymbol {G} _ {p} \\ 0 \\ 0 \end{array} \right] \eta_ {p} + \left[ \begin{array}{l} 0 \\ \boldsymbol {G} _ {g} \\ 0 \end{array} \right] \eta_ {g} \tag {4.22}
$$

Finally, the proper choice of aircraft responses, $\mathbf{y}$ , is critical for obtaining meaningful results from the analysis. If the wrong outputs are selected, erroneous conclusions may be drawn. This point is emphasized so that the reader is aware that a great deal of engineering judgement must be used in choosing the proper outputs. Understanding the physics of the problem is necessary to obtain meaningful results.

Once the outputs of interest are chosen, linear matrix output equations are formed so that,

$$
\mathbf {y} = \mathbf {C} _ {\mathbf {X}} + \mathbf {E} \eta_ {\mathrm {p}} + \mathbf {F} \eta_ {\mathrm {g}} \tag {4.23}
$$

- where $\mathbf{y}$ is a vector of outputs. The modal analysis may now be performed, using Equations (4.21), (4.22) and (4.23) as the complete system.

# Application To Data Base Configurations

The modal analysis method was implemented in a computer program. A listing of this program appears in Appendix A.6. As a result of the modal analysis, several quantities of interest are readily available. In addition to the modal impulse residues, the modal eigenvalues, the modal eigenvectors, and the modal controllability, disturbance and observability matrices are all easily obtained.

The "vehicle models used in Yen's simulation were extended to include two additional structural modes. The additional modes were t.e second and fourth lowest frequency modes of the baseline vehicle (i.e. Configuration 1), thus increasing the model to include the four lowest frequency structural modes. The mode shapes of the additional modes indicate that they are primarily symmetric wing bending modes. The shapes of these modes can be seem in Appendix A.4. These modes could be important in the gust responses and will be considered later in the analysis.

The total state vector includes the standard rigid-body degree of freedom (i.e. perturbed forward velocity, $\mathbf{u}$ ; angle of attack, $\alpha$ ; rigid-body pitch attitude and attitude rate, $\theta_{\mathbb{R}}$ and $\dot{\theta}_{\mathbb{R}}$ ) and the generalized coordinates of the four structural modes, (i.e. the generalized deflections, $\eta_{i}$ ; and the generalized rates

$\dot{\eta}_{\mathrm{i}}\}$ . The total state vector is defined as,

$$
\mathbf {x} _ {\mathbf {v}} ^ {\mathbf {T}} \triangleq \left[ \begin{array}{l l} \mathbf {x} _ {\mathbf {R}} ^ {\mathbf {T}} & \mathbf {x} _ {\mathbf {E}} ^ {\mathbf {T}} \end{array} \right]
$$

(4.24)

$$
\triangleq \left\{\alpha , \dot {\theta} _ {R}, u, \theta_ {R} \mid \eta_ {1}, \dots , \eta_ {4} \mid \dot {\eta} _ {1}, \dots , \dot {\eta} _ {4} \right\}.
$$

The system matrices of the vehicle configurations using this state vector can be found in Appendix A.3.

The output parameters were chosen to include rigid-body flight path angle $(\gamma)$ . (Equation (4.25)), total-elastic $(\theta_{\mathbf{T}})$ and rigid-body $(\theta_{\mathbf{R}})$ pitch attitude angles, (Equation (4.26), Figure 4.1), total-elastic $(\dot{\theta}_{\mathbf{T}})$ and rigid-body $(\dot{\theta}_{\mathbf{R}})$ pitch attitude rates, (Equation (4.27)), and normal acceleration at the cockpit $(n_z)$ , (Equation (4.28)).

$$
\gamma_ {R} = \theta_ {R} - \alpha_ {R}, (\text {r a d}) \tag {4.25}
$$

$$
\theta_ {\mathrm {T}} = \theta_ {\mathrm {R}} - \sum_ {\mathrm {i} = 1} ^ {\mathrm {n}} \eta_ {\mathrm {i}} (\mathrm {t}) \phi^ {\prime} _ {\mathrm {i}} \left(\mathrm {l} _ {\mathrm {x}}\right) \quad , (\text {r a d}) \tag {4.26}
$$

$$
\dot {\theta} _ {T} = \dot {\theta} _ {R} - \sum_ {i = 1} ^ {n} \dot {\eta} _ {i} (t) \phi^ {\prime} _ {i} \left(l _ {x}\right), (\text {r a d / s e c}) \tag {4.27}
$$

$$
n _ {z} = \frac {1}{g} \left[ U _ {o} \dot {\gamma} + I _ {x} \ddot {\theta} _ {R} - \sum_ {i = 1} ^ {n} i j _ {i} (t) \phi_ {i} \left(I _ {x}\right) \right], \quad \left(g ^ {\prime} s\right) \tag {4.28}
$$

$$
- w h e r e g = \text {g r a v i t a t i o n a l} (f t / \sec^ {2})
$$

$$
U _ {o} = \text {c r u i s e v e l o c i t y , 9 4 9 (f t / s e c)}
$$

$$
l _ {x} = \text {d i s t a n c e b e t w e e n c . g . a n d c o c k p i t , (f t)}
$$

图片摘要：该图主要展示 4.1。
![](images/d1c0193faed518f93d79ae8d46e70e349fa0a6fa9ab0c5044f4f755270041ae5.jpg)  
Figure 4.1   
Rigid and Elastic Pitch Angles

The above parameters constitute what was judged to be the significant responses in longitudinal attitude dynamics. Total-elastic and rigid-body pitch attitude angle and pitch rate are used extensively by the pilot to control the vehicle and evaluate its performance. In fact, in the simulation study, the pilot's task was to minimize the error between a commanded attitude, $\theta_{\mathrm{C}}$ , and the vehicle attitude, $\theta_{\mathrm{T}}$ . This implies that $\theta_{\mathrm{T}}$ and $\dot{\theta}_{\mathrm{T}}$ as well as $\theta_{\mathrm{R}}$ and $\dot{\theta}_{\mathrm{R}}$ are of extreme importance in pitch attitude tracking. Normal (or plunge) acceleration is another significant response of the vehicle from the aspect of ride quality, but of course was not a factor in the fixed-base simulation.

Note that the equation for $\mathbf{n}_{\mathbf{z}}$ , (Equation (4.28)), is not an explicit function of the states in Equation (4.24), but is a function of the state derivatives. It is, therefore, an implicit function of the system states and control deflections. By using the state equations (Equation 4.1), $\mathbf{n}_{\mathbf{z}}$ can be written as an explicit function of the system states, as presented in Appendix A.2.

The algebraic equations for the chosen output parameters were combined to obtain a matrix output equation in the form of Equation (4.23) using the output vector,

$$
\mathbf {y} ^ {\mathbf {T}} \triangleq \left[ \gamma , \mathbf {n} _ {\mathbf {z}}, \theta_ {\mathbf {R}}, \theta_ {\mathbf {T}}, \dot {\theta} _ {\mathbf {R}}, \dot {\theta} _ {\mathbf {T}} \right]. \tag {4.29}
$$

The numerical values of matrices $\mathbf{C}$ , $\mathbf{E}$ and $\mathbf{F}$ for each configuration appear in Appendix A.3.

The pilot parameters, the time constants and D.C. gains were chosen to accurately describe the bandwidth limitation of the human pilot. A characteristic lag of 0.15 seconds was chosen to be consistent with other studies [8]. The resulting pilot filter equation used in the analysis is,

$$
\dot {x} _ {p} = - \frac {1}{r _ {p}} x _ {p} + \frac {1}{r _ {p}} \eta_ {p} \tag {4.30}
$$

$$
- \text {w h e r e} \tau_ {p} = 0. 1 5 \text {s e c s}.
$$

The gust parameters were chosen to be consistent with a previous study using the B-1 vehicle and the Dryden Gust Model [9]. The gust equation used in the analysis is,

$$
\mathbf {x} _ {\mathbf {g}} \triangleq \left[ \alpha_ {\mathbf {g} _ {1}}, \alpha_ {\mathbf {g}} \right],
$$

(4.31)

$$
\dot {x} _ {\mathbf {g}} = \left[ \begin{array}{l l} - 9. 4 & 0. 0 \\ - 0. 0 2 2 5 & - 9. 5 \end{array} \right] x _ {\mathbf {g}} + \left[ \begin{array}{l} 1. 0 \\ 0. 0 0 5 6 \end{array} \right] \eta_ {\mathbf {g}}.
$$

- for $\alpha_{\mathbf{g}}$ in radians and $\eta_{\mathbf{g}}$ of unit intensity.

# Numerical Results

The modal analysis method was applied to the eight configurations of the data base described in Chapter 3. The complete numerical results can be found in Appendix A.3.

Consider the graphical results on Figures 4.2 - 4.9 which are the normalized relative magnitudes of the modal impulse residues for each mode of the vehicle due to pilot inputs. The normalization was done so that the residue magnitudes of the vehicle modes (not including pilot lag, i.e. phugoid, short-period and aeroelastic) sum to unity for each output. The equation used to accomplish this is Equation (4.32).

$$
\left| \mathrm {R} _ {\mathrm {i}} \right| _ {\text {n o r m}} = \frac {\left| \mathrm {R} _ {\mathrm {i}} \right|}{\sum_ {\mathrm {j} = 1} ^ {\mathrm {m}} \left| \mathrm {R} _ {\mathrm {j}} \right|}, (\mathrm {i} = 1, \dots , \mathrm {m}) \tag {4.32}
$$

- where $m$ is the number of vehicle modes.

The absolute magnitudes for each mode can be obtained from the numerical results in Appendix A.3. Since pitch attitude and pitch attitude rate are outputs of primary concern in a pitch tracking task, the residue magnitudes associated with the rigid-body and total-elastic pitch attitude angles, $(\theta_{\mathbf{R}}$ and $\theta_{\mathrm{T}})$ , and rates, $(\dot{\theta}_{\mathbf{R}}$ and $\dot{\theta}_{\mathbf{T}})$ , will be considered first. Clearly, $\theta_{\mathbf{T}}$ and $\dot{\theta}_{\mathbf{T}}$ have more aeroclastic mode contribution than do $\theta_{\mathbf{R}}$ and $\dot{\theta}_{\mathbf{R}}$ , which is as expected since $\theta_{\mathbf{R}}$ is the rigid-body attitude angle and $\theta_{\mathbf{T}}$ is the total attitude angle including elastic deformation at the cockpit.

# CASE 1 -

图片摘要：该图片与GAMMA；THETA R这部分内容相关。
![](images/2e8daccc9f58e73b5cf164ff7f1f1f310fbbf6e2b09770acce18e4d7c825006e.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/9ac0ccea4d8ca7aa4e3d69244204314da2a7c75f019c1f47bda5d365c46b0fa3.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/f68621db5f42764392f7a112debc8b445a8e68a885957af50dd08ed9c8280ad8.jpg)  
THETA-R

图片摘要：该图主要展示 4.2。
![](images/dc6fbdcf27a01ea291047f21716576872db58a3437aa067e3966e94d5707e9a2.jpg)  
THETA - T

图片摘要：该图主要展示 4.2。
![](images/3b13bbb92c59315080c504f63422094f992c2fde09de248e268a1bc1adb0a908.jpg)  
THETA DOT - R

THETA DOT - T

Figure 4.2   
Pilot Impulse Residue Magnitudes -Config. 1   
图片摘要：该图主要展示 4.2。
![](images/0607abc5f8de0091863a5c5c78b28466d79e831e39be22cc02722cb73a3d8cd8.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 2 -

图片摘要：该图主要展示 4.2。
![](images/5f1f4b78bf7934e72c69e8000b6aaf2f9be9444bfc4bb228afe6a43cd86efa48.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/4776e4c72faccaf0a8d6abadd34742cd39fd23176874aa0a53741677ec0b3a82.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/967daf63d0edee7632b9d06fc9d0aabbda61ff5847b6d77e6d37bd1cda472b44.jpg)  
THETA- R

图片摘要：该图主要展示 4.3。
![](images/a136982aebaf35ff0480f0b8800f03738ea2d64fae18fd4a6cf0e56b5fe30070.jpg)  
THETA - T

图片摘要：该图主要展示 4.3。
![](images/bac00eb4332e93025538d8f1a145063190b55530cd45d39dce3a17d37e801896.jpg)  
THETA DOT- R

THETA DOT - T

Figure 4.3   
Pilot Impulse Residue Magnitudes -Config. 2   
图片摘要：该图主要展示 4.3。
![](images/7715a551ca25497369a11d989c6b790fe8505c621da40c4decfe2d8737055396.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

图片摘要：该图主要展示 4.3。
![](images/1c8c82961d6b744905f534707ed4c82da3f24e5f9dfcbcd071ea3ae76faf05a3.jpg)  
CASE 3 -

图片摘要：该图主要展示 4.3。
![](images/de685eeb4f613f6651687fc823fafb91632f8d25833dbf7bea24b2bc64c79496.jpg)

图片摘要：该图主要展示 4.4。
![](images/ad7a13b07606e17eebc064011dbfaf0ded346dc8b62ad5f8ce67251db863671b.jpg)

图片摘要：该图片与RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0；Figure 4.4这部分内容相关。
![](images/f02c34596dee3ff7a20ef66198c75f926dd353c1e7c9a66c46f84a0004a85088.jpg)

图片摘要：该图片与RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0；Figure 4.4这部分内容相关。
![](images/95232a2882982db2150be916a04cf5affb572daa99a9616532ff29b1c8d6b909.jpg)

图片摘要：该图主要展示 4.4。
![](images/7513135b4ef42161ad949f476f5f1002ae32a25373e164998a7b9e342589ebab.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0   
Figure 4.4   
Pilot Impulse Residue Magnitudes -Config. 3

# CASE 4 -

图片摘要：该图主要展示 4.4。
![](images/34748b91581adddcc0c68374127f14e8001a803cd4170257d45f196b93df81c8.jpg)  
GAMMA

图片摘要：该图主要展示 4.4。
![](images/cccc9a0e6b76ecb2c73ee536a3e53d443c30e0a28d1e5a7604ba8e6bd37c65e6.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/71a9a47ddd6a72b8439dea76d1b92b9672d1987754c367b103f261c8ef53456c.jpg)  
THETA - R

图片摘要：该图主要展示 4.5。
![](images/12a7b72a9529d1d21f3f100fd9c5845cb6273e4f25d084a087b4f8ab93ef97df.jpg)  
THETA - T

图片摘要：该图主要展示 4.5。
![](images/56f6b80760eff936b87fd33858257ae92ed4c99459ff21bf3ee10c73804db01d.jpg)  
THETA DOT- R

THETA DOT- T

Figure 4.5   
Pilot Impulse Residue Magnitudes -Config. 4   
图片摘要：该图主要展示 4.5。
![](images/0e3466c8f1bee72d332acbedfaea4cdff06cbcd492fd0f48edc32bf15e3399fe.jpg)  
RES:JES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 5 -

图片摘要：该图主要展示 4.5。
![](images/26de99eddc344022563b75cd701757171baaab140875d241c4579eb4aa168701.jpg)  
GAMMA

图片摘要：该图片与THEIA R；THETA T这部分内容相关。
![](images/9cf77f27d306dc48ad6e34b64ca77e7493100ce3b2e24989832326d51f1352e2.jpg)  
NZ

图片摘要：该图片与THEIA R；THETA T这部分内容相关。
![](images/53286eeefc4ddbf8369ac516607e381d6db00babd1bd082e81fa2f1e0a07d20d.jpg)  
THEIA-R

图片摘要：该图主要展示 4.6。
![](images/56606d41472d6b17ef43a5705c058317c812043463e11a858195f144fadc5fe6.jpg)  
THETA-T

图片摘要：该图主要展示 4.6。
![](images/7aede74d52fb452140148137b4348f366b45a0f2dc0e08759e477f1389929d7e.jpg)  
THETA DOT - R

THETA DOT - T

Figure 4.6   
Pilot Impulse Residue Magnitudes -Config. 5   
图片摘要：该图主要展示 4.6。
![](images/69580c5b9817e036a1bb8d5c187b3ddd0bc8bb681e1cea1008ee320ebf2b3dbc.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 6 -

图片摘要：该图主要展示 4.6。
![](images/fb892b3c63ce8a66d455c8da1dffba5ffcdf21c05a0db9a6d85ab61e2488bd2c.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/7e79beaf16a462eb3c6911ecb8713e77db72fa0df84a20f98cd1d080bf4826ec.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/42678b2a9e930b2587f22613e572b75f89ce177fb6600e2de3720420c363ee7b.jpg)  
THETA- R

图片摘要：该图主要展示 4.7。
![](images/c8ca4c9a17a212f758a97b803c98439224ee41e76c35adb18cc7b76b880adc73.jpg)  
THETA - T

图片摘要：该图主要展示 4.7。
![](images/ce713ced8ab0b78eaa45656573b5e6f5c2df66ab4429bd94f1e3b5ff69f509e9.jpg)  
THETA DOT- R

THETA DOT - T

Figure 4.7   
Pilot Impulse Residue Magnitudes -Config. 6   
图片摘要：该图主要展示 4.7。
![](images/7d7bd8b26305dfaca33a5859a3868417aec0f6342adb509ffba381742073b010.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SD THAT THEIR SUN IS 1.0

# CASE 7 -

图片摘要：该图主要展示 4.7。
![](images/df94b35d97ffcaf0059235972c0607473b14e435ac6001486d8fc203f4021092.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/1b9e97fceb0e62d26b944f0ff8b8864eb718fe0dc941a5b209270c9b947f37e4.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/218035d152bd45a48f4fa03a83c3bd569a6167e0df47e2e744369993b6e78349.jpg)  
THETA-R

图片摘要：该图片与THETA T；THETA DDT R这部分内容相关。
![](images/ba5ac79cd4cf75785e470679ca39ab75c067bb768c79f01da2546c57e9ff3d71.jpg)  
THETA - T

图片摘要：该图主要展示 4.8。
![](images/857739eca9764aec71ba0e1e8a25e1b00791d468101f36ca502adc9aa112db92.jpg)  
THETA DDT- R

图片摘要：该图主要展示 4.8。
![](images/dbdc4c4ef754022a6b75dc830c1166b49ca2882c022a859dc5c98477a8e4c4b2.jpg)  
THETA DOT - T   
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0   
Figure 4.8   
Pilot Impulse Residue Magnitudes -Config. 7

# CASE 8 -

图片摘要：该图主要展示 4.8。
![](images/0308f74256421ec79d270711ccb57d4891e1f1cbe3e34ab1c192ba29b767600c.jpg)  
GAMMA

图片摘要：该图主要展示 4.8。
![](images/fa85138e8c2197baa623b575591aa0b5a95bfb785b00d3c14af8b0db4d189462.jpg)  
NZ

图片摘要：该图片与THEIA R；THETA T这部分内容相关。
![](images/2100969a00ea684a2f4ac4b172c2ce18f666d506ab268f007d6460191ddbe0d4.jpg)  
THEIA-R

图片摘要：该图主要展示 4.9。
![](images/007429d7005a3de070477530e99c0d6c14feff896ca4f6bebfb82f07f69cfe14.jpg)  
THETA-T

图片摘要：该图主要展示 4.9。
![](images/4e7dcc015b89f3e089b2d7b352ea5b2182d9691280efbded78145f6fade6ddcb.jpg)  
THETA DOT- R

THETA DOT - T

Figure 4.9   
Pilot Impulse Residue Magnitudes -Config. 8   
图片摘要：该图主要展示 4.9。
![](images/04030a33a701a8c5f789afd4934e9405171f1ad740b0ee48d08fa89486161552.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

Now consider the results for $\theta_{\mathbb{R}}$ and $\dot{\theta}_{\mathbb{R}}$ as the frequency of the first elastic mode is reduced as in configurations 1 through 3 (see Table 3.1 for reference). The residue magnitudes of the first aeroelastic mode (E1) monotonically increases until, in Configuration 3, it is larger than the short-period modal residue! This indicates that, for Configuration 3, the rigid-body attitude response is dominated by the first aeroelastic mode! It is obvious that the use of a pure rigid-body analysis would be wrong and any model not including the effects of elastic modes would be inappropriate.

The results also explain why Configurations 3 and 4, while having similar eigenvalue characteristics, have very different simulation results, (see Table 3.2). The aerolestatic modes in Configuration 4 do not dominate the attitude response (as they do in Configuration 3). The residue magnitude for the lowest frequency aeroelastic mode (E3 in this case) is not larger than the short-period residue. In other words, Configuration 4 has attitude dynamics which are dominated by a rigid-body mode and Configuration 3 has dynamics which are dominated by an aeroelastic mode. Since Configuration 4 acts more like a "rigid vehicle" than Configuration 3, the tracking performance for Configuration 4 is better than Configuration 3. However, the aeroelastic mode residue in Configuration 4 still contributes to some degradation in tracking performance.

This approach can also be used to relate the rest of the tracking simulation results to the effects of the aeroelastic modes. The tracking errors (Figure 3.4) and the Cooper-Harper ratings (Figure 3.5) of the simulations agree especially well with the trends in the magnitudes of the impulse residues for total pitch attitude angle $(\theta_{\mathbf{T}})$ . The configurations with large tracking errors and poor pilot ratings have aeroelastic residue magnitudes which are larger than the rigid-body residue magnitudes in the $\theta_{\mathbf{T}}$ response. The converse is also true; the configurations with large aeroelastic residue magnitudes tend to have large tracking errors and poor pilot ratings.

The graphical results can be used to bring attention to other aspects of the vehicle dynamics as well. Take, for instance, the plunge acceleration at the pilot station $(\mathbf{n}_2)$ . This parameter was, of course, of no importance in the fixed-based simulation, but would be of particular interest if the configurations were to be studied using a moving-base or in-flight simulator. The graphical results of the $\mathbf{n}_2$ modal impulse residue magnitudes in Figures 4.2 - 4.9 indicate that ignoring aeroelastic affects when considering, for example, ride quality would be improper. The contribution of the aeroelastic modes is very important in the $\mathbf{n}_2$ response of the vehicle for all configurations.

Consider also, the flight path angle $(\gamma)$ response for Configuration 3. Ignoring aeroelastic affects in this case would give erroneous results since the aeroelastic residue magnitudes are significant compared to those of the rigid-body modes.

Finally, the insignificance of the second and fourth aeroelastic modes (E2 and E4) in the pilot impulse response is clearly evident from the graphical results. The exclusion of these two modes in Yen's [2] simulation study was therefore valid.

The same type of trends i. residue magnitude occur in the gust-disturbance impulse residue magnitudes, Figures 4.10 - 4.17. These results indicate that the aeroelastic modes contribute, in varying degrees, to the various vehicle responses due to an impulse input to the Dryden gust model, where an impulse input is the deterministic counterpart to "white" noise. Of particular interest are the results for rigid-body pitch-attitude-rate $(\dot{\theta}_{\mathbb{R}})$ . For Configurations 3, 4 and 6, the contribution of the aeroelastic modes is very significant. One of the wing bendings modes, E2, has significant residue magnitudes compared to those of the rigid-body modes. This indicates that attitude tracking in turbulence would be similar for each cf these configurations in that the $\dot{\theta}_{\mathbb{R}}$ responses would be dominated by aeroelastic-structural modes. This implies that even though Configuration 4 had a satisfactory pitch attitude response in the simulation, added turbulence may result in significantly different and degraded performance.

The modal analysis paints a different picture than the eigenvalue analysis presented in Chapter 3. Recalling the discussion in Chapter 2, one can see that as the frequencies of the structural modes are reduced, the interaction between the rigid-body modes and the aeroclastic modes increases. The result is that the residues associated with the structural modes and those associated with the rigid-body modes are modified and, as a result, alter the vehicle dynamics. If the residues of the aeroclastic modes become large enough to dominate the vehicle response, the aircraft no longer acts like a "rigid aircraft". In other words, the vehicle attitude response is not dominated by the characteristic short-period attitude dynamics.

Since the residue magnitudes are a measure of the modal participation, the above argument indicates that when the impulse residue magnitudes associated with acroelastic modes dominate those of the short-period mode, the vehicle performance degrades. The modal analysis results support this argument.

# CASE 1 -

图片摘要：该图片与CASE 1；Since the residue magnitudes are a measure of the modal participation, th这部分内容相关。
![](images/4ab8cb180b5086808981b2bd9ec9ecab9ddcd4f1c8c837019848d7d7d3e5bfa5.jpg)

图片摘要：该图片与CASE 1；Since the residue magnitudes are a measure of the modal participation, th这部分内容相关。
![](images/6fc71ebb999413956d8092aa280e2bd7f7c1dc2e07e409b12c015713ad2a2cb6.jpg)

图片摘要：该图主要展示 4.10。
![](images/517f98a6f8448de5d0bd2f58342cb79d590753cfedd4735873049a8e2b37c39a.jpg)

图片摘要：该图片与RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0；Figure 4.10这部分内容相关。
![](images/289e7a06d17d455f07eabfa4398c09c416d41b21063e329106f4fc433f29477b.jpg)

图片摘要：该图主要展示 4.10。
![](images/ca7e271e9c09b7298f54d9547a4703d7ac5c72970b5a53078f79892f1644717a.jpg)

图片摘要：该图主要展示 4.10。
![](images/f42df5d3ae940cd17ebcbe93f2a4f889c71609c1625e0e65c2a1d8c127792ac0.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0   
Figure 4.10   
Gust Impulse Residue Magnitudes - Config. 1

# CASE 2 -

图片摘要：该图主要展示 4.10。
![](images/198df1f923bc3c7ed818645adaf7aee7518588cff468d68e6deee34da172ee7e.jpg)  
GAMMA

图片摘要：该图主要展示 4.10。
![](images/542f55d0d0b170d869a3084b76dfde554634ae06006cc24276cf6fc1de05807b.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/6724e29c08b4c30cbd7efe66e8b5dadc453171f81df4517e532b2f53d74cd7ec.jpg)  
THETA- R

图片摘要：该图主要展示 4.11。
![](images/c50d9e31dc90fbdce81c4ec0a9cd284d4738bd4cd54e51cd9ac3d9ea2bd249e4.jpg)  
THETA-T

图片摘要：该图主要展示 4.11。
![](images/6f7dec5782baee9f397dc8b16a9ac705a3dfa0222c2ae78042f4370c60009db9.jpg)  
THETA DOT-?

THETA DOT - T

Figure 4.11   
Gust Impulse Residue Magnitudes - Config. 2   
图片摘要：该图主要展示 4.11。
![](images/f4611dd41e609ca9e8f43d6faf2d135d6388bec56e31fc90b57ca94c96438e67.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 3 -

图片摘要：该图主要展示 4.11。
![](images/6453696cfd519263db30a47f7b2f852ccde44da380ac8b5f1772202f73e6834f.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/4c37cec0c69a04fdde9ccbb38c5e65d833112167bc04377f1a1c99fa044078d0.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/e996a5ebd24987e5e8a57cff6664ab0f562562e9f457ce301ddae332c7e4a483.jpg)  
THETA- R

图片摘要：该图主要展示 4.12。
![](images/17ab1e96436a1a54935295f2a62793ae22b9e4c42a941a6d2e47df6ca24f0287.jpg)  
THETA-T

图片摘要：该图主要展示 4.12。
![](images/f79afdee183e16a6a62e40c2816f8986b28eb1428550375c4d9dfa27b8d65893.jpg)  
THETA DOT-P.

THETA DOT- T

Figure 4.12   
Gust Impulse Residue Magnitudes - Config. 3   
图片摘要：该图主要展示 4.12。
![](images/63082f7541a7a774a8be7b93a8ccff61c5e955dcae4ee6e87215a560ebe51caa.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 4 -

图片摘要：该图主要展示 4.12。
![](images/1db751cfa25677e65ab303e586771d124d36ad9b07f486cf542ab1b599706f0d.jpg)  
GAMMA

图片摘要：该图片与THETA P；THETA T这部分内容相关。
![](images/39d19a40fc661d234c837f9c7555093838fb3ebd0ca9bc92ed10e5a47b35100c.jpg)  
NZ

图片摘要：该图片与THETA P；THETA T这部分内容相关。
![](images/7e471c7986b4ff26413f52e5ec961dcc55d3ab14d140cb78eb4add229922a13f.jpg)  
THETA-P

图片摘要：该图主要展示 4.13。
![](images/57c41e1be055e917008e837b58ef9dcf88d89ddc28af3e2922c0f2ec3ccf5658.jpg)  
THETA-T

图片摘要：该图主要展示 4.13。
![](images/e2206dc4723774f79c9385b1578efb76d5a43fb26bfaf2b21ba5ce43dfcab843.jpg)  
THETA DOT - R

THETA DOT - T

Figure 4.13   
Gust Impulse Residue Magnitudes - Config. 4   
图片摘要：该图主要展示 4.13。
![](images/a2b1b970a4bf921907a35f36897a7c15eb2b872869547ccaf9a7600584903b1d.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 5 -

图片摘要：该图主要展示 4.13。
![](images/fda77ccdc421f881167c750d4173706baec29876a69cf54cd1ade37d38651561.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/ea172bd23e0d856487e1578ef59808dd1a395770dd36097ae4feee38acbb63b4.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/e44f28b395a711d3f6fe5e23db1829ea3e6f38deb483987ed0fb425c67fe3d98.jpg)  
THETA- R

图片摘要：该图主要展示 4.14。
![](images/af67ef5ad6e54bfb579be348c6c541593461aabe29d5ccce2ef047a47e64546a.jpg)  
THETA-T

图片摘要：该图主要展示 4.14。
![](images/3b1b11fcba2e1e3f73680f41cdbc9cbe8c3a104886c3575347775ccb15083503.jpg)  
THETA DOT - R

THETA DOT- T

Figure 4.14   
Gust Impulse Residue Magnitudes - Config. 5   
图片摘要：该图主要展示 4.14。
![](images/b6d02318140c7ed7a6f4688e2fd52b2ffaed451ec0e5d935ff06d3ea59a844b3.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO   
THAT THEIR SUM IS 1.0

# CASE 6 -

图片摘要：该图主要展示 4.14。
![](images/172bd67223a37581f06929a59a62bfc55604753603448a9ba2c24213698faafb.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/1c11cc81e85bda3e0a80e4e86439c7044476ebda09e235a7ea20465eab483720.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/22f1d7b8abf64773fb3cdb85f025dd0710dfe61de8bb291cff18ca48a9a15e10.jpg)  
THETA- R

图片摘要：该图主要展示 4.15。
![](images/7fcfd68aed88c81fd04ab6871aa7ca27a6b008f5a24cf288483ebf2879002b7e.jpg)  
THETA-T

图片摘要：该图主要展示 4.15。
![](images/5c1e8a36416c405a300d2b90f73f3526692c3097fdee323f5bb3a411cd71c6d4.jpg)  
THETA DOT- R

THETA DOT - T

Figure 4.15   
Gust Impulse Residue Magnitudes - Config. 6   
图片摘要：该图主要展示 4.15。
![](images/6b893030514f8d9913cdee350aa555ad96b262a7de8c3737c64027088438c363.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

图片摘要：该图主要展示 4.15。
![](images/2711d2b6b7562412b8316d7874cb4876ded53fd61d77caa8e574981e6c776041.jpg)  
CASE 7 -

图片摘要：该图主要展示 4.15。
![](images/dfdfe2b5ef6240c2f91fefa967b30b97348867d0c3f03998fce0d9537184df84.jpg)

图片摘要：该图主要展示 4.16。
![](images/617b04db7f38c6f777452594b406416bf28634952fca7ee3b8f7e7e52c3971e6.jpg)

图片摘要：该图片与Figure 4.16；Gust Impulse Residue Magnitudes Config. 7这部分内容相关。
![](images/f4378860f13a0874192014990da00db171464e8bb7a580523894673859f5de85.jpg)

图片摘要：该图片与Figure 4.16；Gust Impulse Residue Magnitudes Config. 7这部分内容相关。
![](images/89591bb3223793a8e8f38b4cf738eb747968de56ae215df0626c86ca7c9b846f.jpg)

Figure 4.16   
Gust Impulse Residue Magnitudes - Config. 7   
图片摘要：该图主要展示 4.16。
![](images/b4bb47e4a5fd3b41161fcefa303a6383d0d1237cd75797e5bd8801e351231d74.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

# CASE 8 -

图片摘要：该图主要展示 4.16。
![](images/452acb99b1409dce3821c5cb954129bf9bf6b0a9cba18adc3c2e938b03febe3c.jpg)  
GAMMA

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/68eeb69da4106470bbb87ff94fcb28a9f1af2da04fd1a9d150ec4aa9e5c6ce0b.jpg)  
NZ

图片摘要：该图片与THETA R；THETA T这部分内容相关。
![](images/b308f64ce38e014dded6b337a17dc695b876c95d65aead132c930b773a588fd4.jpg)  
THETA- R

图片摘要：该图主要展示 4.17。
![](images/a4150b84a80a6e8ae98c758bcc238e93ed376d65482e606449bc277a247fbd1b.jpg)  
THETA-T

图片摘要：该图主要展示 4.17。
![](images/0e66c096df5c7b4e42529848001c49943543f4f025d3dc36693081f0ef2c4c4b.jpg)  
THETA DOT-R

THETA DOT - T

Figure 4.17   
Gust Impulse Residue Magnitudes - Config 8   
图片摘要：该图主要展示 4.17。
![](images/6cb6fa6a0d24c59685aefa8001b034218aa5a547b9d940c63f82a2f8cee9ef10.jpg)  
RESIDUES FOR EACH OUTPUT ARE NORMALIZED SO THAT THEIR SUM IS 1.0

In summary, the modal analysis method described in this chapter has been used to attack the question of, "how and when do aeroelastic effects significantly affect aircraft dynamics?" The analysis indicates that when the magnitudes of the modal impulse residues of the "aeroelastic modes" become the dominant residue magnitudes of the vehicle system for important outputs, the vehicle dynamics change significantly and may change in such a way as to result in "un-aircraft like" characteristics. In addition, the trends in the relative residue magnitude values for some outputs are closely related to the pilot ratings and tracking errors of the simulations.

A drawback of using this modal analysis approach is that it is essentially open-loop in nature. Even though the modal analysis procedure considers some aspects of the pilot, specifically his limited bandwidth, it is still an open-loop analysis method. Since the pilot/vehicle system performance is really determined by the dynamics of the vehicle when the pilot closes the loop, a "closed-loop" or "pilot-in-the-loop" analysis may give more insight into the effects of the aeroclastic modes. The next chapter considers such an approach.

# CHAPTER V CLOSED-LOOP ANALYSIS

Complete flight vehicle system dynamics are dependent, not only on the aircraft dynamics, but also on the dynamics of the pilot and on how he interacts with the aircraft dynamics. Though the modal analysis method did consider the bandwidth limitations of the pilot, the method was still open-loop in nature. This chapter will apply a closed-loop analysis procedure to the configurations in the data base to study the effect of aeroelastic modes on closed-loop dynamics.

The closed-loop analysis procedure that will be used here is an extension of the Neal-Smith procedure [10] which uses an optimal control model (OCM) of the pilot [11] in a pitch tracking task. This approach has, in the past, been applied to study the effect of flight control system dynamics on pitch tracking performance of fighter-type aircraft [12,13]. Since flight-control system dynamics and aeroelastic modes are both examples of higher order dynamics, there is reason to believe that this procedure may be useful in evaluating the effects of aeroelastic modes on the pitch tracking performance of the data base configurations.

Before using this procedure to study the data base configurations, the procedure must be extended for application to flexible aircraft. This entails understanding the Neal-Smith methodology and applying the OCM to the Neal-Smith approach. This will be accomplished by briefly reviewing the work done by Neal and Smith [10] and by Bacon and Schmidt [12].

# Neal-Smith/Bacon Methodology

The investigation performed by Neal and Smith in the early 1970's resulted in a criteria developed to expose problem areas in aircraft where the pilot was to perform a given task. Their criteria utilize a closed-loop or "pilot-in-the-loop" analysis procedure. This pilot-in-the-loop approach was

used because of difficulties encountered in using existing open-loop handling qualities criteria and because of the truly closed-loop nature of piloted vehicles.

The analysis method was based on the fact that the subjective pilot rating of a pitch-attitude task is primarily determined by how well the pilot can control the pitch attitude and how difficult it is to do so. Specifically, the analysis was performed using a compensatory tracking task model (i.e. the pilot only perceives the difference between the attitude of the aircraft and the commanded attitude), and by representing the pilot by a describing function consisting of a time delay and a lead-lag compensator (see Figure 5.1). The time delay accounts for perceptual delays and neuromuscular lags and the lead-lag compensation is used as a first order approximation of the pilot's dynamic compensation in the task.

By considering the closed-loop frequency response of the modeled pilot/aircraft system, Neal and Smith were able to relate the pilot's objective ratings to frequency response characteristics depicted in Figure 5.2. The resulting specifications also relate to the stated goals of actual pilots.

For good performance, a pilot wants to be able to acquire the target quickly and predictably and with a minimum of overshoot and oscillation. "Quick acquisition of the target" implies that the pilot wants to achieve a high bandwidth. Neal and Smith also related minimizing overshoot to minimizing the closed-loop resonance peak, $\left( \left| \frac{\theta}{\theta_{\mathrm{c}}} \right|_{\max} \right)$ . This inference comes from the relationship between system damping and the magnitude of the resonance peak in a second order system. By combining the two objectives, Neal and Smith concluded that, "pilot rating is a function of the compensation required to achieve good low frequency performance and the oscillatory tendencies that result." [10,12,13]

These objectives were related to the closed-loop analysis by defining the system bandwidth to be the frequency at which the closed-loop system phase lag reaches -90 degrees as illustrated in Figure 5.2. The pilot compensation was defined as the phase of the resulting pilot describing function at the bandwidth frequency, excluding the effect of the pure time delay, as shown in Equation (5.1).

图片摘要：该图主要展示 5.1。
![](images/e38e1f24a8d441fb28bb327e058b018cd390a1a2901fd1714c7b163cbcd205a3.jpg)  
Figure 5.1   
Neal-Smith Model Structure

图片摘要：该图主要展示 5.1。
![](images/00f2a09891a32e849da767cbd0ad826c6f99d2a53aff8e868cd2f4545bdb579b.jpg)  
Figure 5.2   
Frequency Response Specifications

$$
\mathrm {P C} \triangleq \angle \left(\frac {\mathrm {j} \omega_ {\mathrm {B W}} \mathrm {T} _ {\mathrm {p} _ {1}} + 1}{\mathrm {j} \omega_ {\mathrm {B W}} \mathrm {T} _ {\mathrm {p} _ {2}} + 1}\right) \tag {5.1}
$$

- where $\mathbf{PC}$ is the pilot compensation. The closed-loop resonance peak is defined to be the maximum value of the magnitude of the closed-loop frequency response. (see Figure 5.2)

The choice of parameters in the pilot describing function $(\mathbf{K}_p, \tau, \mathbf{\Sigma}_{p_1}, \mathbf{T}_{p_2})$ were made to best satisfy a set of performance requirements. The requirements consist of

1) a specified time delay $(\tau)$ ,   
2) a specified bandwidth characteristic of the task,   
3) a maximum allowable "low frequency droop",   
4) compensation (i.e. the value of $\frac{T_{p_1}}{T_{p_2}}$ ) required for a minimum value of resonance peak.

Neal and Smith found that the parameters which satisfied these requirements resulted in a pilot phase compensation and closed-loop resonant peak that correlated with pilot rating.

By plotting the value of resonance peak against PC (i.e. pilot compensation), Neal and Smith found regions in which aircraft with similar pilot rating were grouped. Figure 5.3 shows the Neal-Smith result and the regions which correspond to the three levels of handlings qualities described in MIL-F-8785C [1]. Level 1 includes aircraft having pilot ratings (Cooper-Harper) of 1.0 - 3.5, level 2 includes pilot ratings of 3.5 - 6.5 and level 3 ratings of 6.5 - 10.0.

There are problems associated with the Neal-Smith method however. These problems lie in the difficulties associated with choosing appropriate frequency response specifications. For instance, it may be very difficult to determine the proper bandwidth frequency for an aircraft in a particular task without experimental data. Another problem lies in the choice of a maximum low frequency droop. Since the droop is only a relative measure of low frequency tracking performance, the choice of a maximum allowable value is rather arbitrary. Still further, the Neal-Smith method uses a compensatory task that was not representative of the actual task used in their flight tests. Bacon [13] extended the work of Neal and Smith to try to address these

图片摘要：该图主要展示 5.3。
![](images/c2c77e98bf3969b1dd786420f64a135d7faf04254741b2517ac4b7586a581934.jpg)  
Figure 5.3   
Ncal-Smith Criteria

problems. He applied an optimal control model of the pilot (OCM, [11]) to the closed-loop analysis method. The use of the OCM provides more flexibility in conducting the analysis by allowing the Neal-Smith criterion to be applied to other, more general, piloting tasks. It also eliminates the requirement of choosing the arbitrary frequency response specifications which are required to determine the pilot describing function.

The optimal control model (OCM) of the pilot is based on the assumption that a well trained, highly motivated pilot chooses his control input $(\mathfrak{u}_p)$ , subject to physiological limitations, in such a way that a quadratic cost function,

$$
J _ {\mathrm {p}} = \mathrm {E} \left\{\lim  _ {\mathrm {T} \rightarrow \infty} \frac {1}{\mathrm {T}} \int_ {0} ^ {\mathrm {T}} \left(\dot {\mathbf {x}} ^ {\mathrm {T}} \mathbf {Q} \mathbf {y} + \mathrm {r u} _ {\mathrm {p}} ^ {2} + \mathrm {g} \dot {\mathbf {u}} _ {\mathrm {p}} ^ {2}\right) \mathrm {d t} \right\}, \tag {5.2}
$$

is minimized. Here, $\mathbf{Q}$ and $\mathbf{r}$ are weightings chosen to reflect the task objectives and $\mathbf{g}$ is usually chosen to reflect physiological limits.

Although details concerning the OCM can be found in [11], a brief description will be included here. Consider the block diagram of the OCM in Figure 5.4. The human perception characteristics that are modeled involve the pilot observations $(\mathbf{y}_p)$ , passed through a pure time delay and contaminated by white noise of intensity $\overline{\mathbf{V}}_y$ . (see Equation 5.3)

$$
\underline {{y}} _ {p} (t) = \underline {{y}} (t - r) + \underline {{v}} _ {y} (t - r)
$$

(5.3)

$$
\mathbf {y} (t) = \mathbf {C} _ {\mathbf {p}} \mathbf {x} (t)
$$

The solution to the stated optimal control problem yields a Kalman filter to estimate the delayed states and a least-mean-square predictor to obtain a current estimate of the states, $(\dot{\mathbf{x}}(t))$ . The control law, obtained from minimization of the cost function $J_{p}$ , for a scalar $\mathbf{u}_{p}$ , can be expressed as,

$$
\tau_ {n} \dot {u} _ {p} = - K _ {x} \dot {x} - u _ {p} \tag {5.4}
$$

图片摘要：该图主要展示 5.4。
![](images/c92393c5ae4cd76b97e892f82ec42da0aadab9cc62dae14b25713356c4dddaa8.jpg)  
Figure 5.4   
OCM Block Diagram

- where $\mathbf{K}_{\mathbf{x}}$ is the optimal control gain matrix. The neuro-motor lag $(\tau_{\mathfrak{n}})$ results from including control rate $(\dot{\mathbf{u}}_{\mathfrak{p}})$ in the cost function $J_{\mathrm{p}}$ and by weighting it so as to obtain a physically achievable value of $\tau_{\mathfrak{n}}$ , based on machine experiments.

As discussed in [12,13], when to OCM cost function is used to minimize tracking error, $(\theta - \theta_{\mathrm{C}})$ , the resulting controller automatically minimizes low-frequency droop and resonance peak of the closed-loop system frequency response. This is an alternative to specifying maximum droop and determining the compensation required to minimize resonance peak in the Neal-Smith approach. In addition, the OCM will automatically determine the achievable bandwidth of the closed-loop system. Therefore, the Neal-Smith requirements are compatible with the OCM. The task for the analyst is now to properly apply the OCM.

The proper application of the OCM involves,

1) selecting a realistic pilot observation vector for the task $(\underline{y}_p)$ ,   
2) defining the cost function to be minimized $(J_{\mathfrak{p}})$ in the task,   
3) defining the command signal to be tracked $(\theta_{c})$   
4) specifying the noise variances, observational thresholds and delays consistent with the human operator.

By proper choice of pilot observations, cost function and command signal, the analysis using the OCM closely reflects the inflight tracking task used by Neal and Smith.

A subtlety discussed by Bacon [13] was associated with the almost-guaranteed stability of the OCM solution. We the cost function reflects minimizing tracking error, the resulting control tries to make the closed-loop system act like a perfect tracker, that is, a system with a response-to-command transfer function of unity. As a result there is a trade-off between the low frequency droop and resonance peak. That is, an aircraft that would actually lead to oscillatory tendencies and a significant resonance peak in the Neal-Smith analysis, would yield an OCM solution that would sacrifice low frequency performance for stability. This is analogous to the pilot being less aggressive and tracking the target so that the oscillations would not occur. This piloting strategy tends not to expose the tendency of the aircraft to oscillate.

Bacon argued that, since oscillation occurs from "suboptimal" piloting strategy, the OCM controller would do a better job of tracking than a real

pilot. He further argued that by increasing the forward path gain, one could approximate an aggressive pilot. An aggressive pilot would try to obtain better low frequency performance at the expense of high frequency oscillations. This type of piloting strategy would therefore expose the oscillatory nature of an aircraft. Hence, in Bacon's approach, the forward path gain (i.e. $\mathbf{K}_{\mathfrak{p}}$ in Figure 5.5) was adjusted so that each vehicle configuration led to a maximum low frequency droop, similar to the Neal-Smith method. The adjustment exposed the oscillatory aircraft by increasing the resonance peak of such aircraft. Figure 5.5 illustrates this effect.

By plotting the gain-adjusted resonance peak against the pilot phase compensation (obtained from the OCM) at the bandwidth frequency (as illustrated if Figure 5.6), Bacon obtained a plot analogous to the one obtained by Neal and Smith. Figure 5.7 presents Bacon's results for the Neal-Smith Configurations which can be compared with Neal-Smith's original results shown in Figure 5.3. Just as in the Neal-Smith criterion, aircraft with similar pilot ratings group together on Bacon's plot.

The choice of proper bandwidth is not necessary in the Bacon method and is replaced by choosing a weighting in the cost function which results in a reasonable neuro-motor lag $(\tau_{\mathfrak{n}})$ , which is a natural physiological limit. Bacon's [13] results also indicate that the closed-loop system bandwidth, a result from the OCM analysis, correlates with subjective pilot rating. In fact, this relationship has been suggested as an additional criterion for measuring the quality of the vehicle dynamics.[12,13] Figure 5.8 illustrates the relationship between closed-loop bandwidth and pilot rating for the Neal-Smith Configurations.

A disadvantage of both methods is the need to choose au arbitrary maximum low frequency droop. As an extension of the Neal-Smith/Bacon method, an alternate way of considering oscillatory tendencies will be presented. This new variation of the Neal-Smith/Bacon method will be used to consider how aeroelastic modes affect the closed-loop characteristics of aircraft.

# Extension Of Neal-Smith/Bacon Methodology

In an attempt to make the analysis procedure independent of an arbitrary choice of the maximum low-frequency droop, an alternate method is proposed. Pilot induced oscillations (PIO's) usually occur with aggressive pilot behavior. If the pilot "backs-off" (i.e. reduces his aggressiveness), the oscillations

图片摘要：该图主要展示 5.5。
![](images/c8b4fcfea07314a57dfff5b15a9a8ca30a8072d2c31738ef7f646c68cf44f66e.jpg)

图片摘要：该图主要展示 5.5。
![](images/4815393da34d564e790b56b0cca5ee1cb0387c748f11f37ceda26165ed12c763.jpg)  
Figure 5.5   
Resonance Peak Adjustment

图片摘要：该图主要展示 5.5。
![](images/eb75b6d8f98c558fcbc5365d1c6530d4033837fde16097799fb754b6d84fbe32.jpg)

图片摘要：该图主要展示 5.5。
![](images/49f44d4e90d77f1061c63539b14234e514fb9f6aa29c9e940bc3a33f5abc2152.jpg)  
Figure 5.6   
Neal-Smith/Dacon Pilot Compensation

图片摘要：该图主要展示 5.6。
![](images/5782a9ae022c6641843316c69b6ead73d91d8ef494decc55dff0c96aae8c371a.jpg)  
EQUIVALENT PILOT PHASE COMPENSATION (occ.)   
Figure 5.7   
Neal-Smith/Bacon Criteria

图片摘要：该图主要展示 5.7。
![](images/33cfff3ad110f15d462ac526692fd922d64968863e9c5c44e3b1c507f14d9292.jpg)  
Figure 5.8   
Pilot Rating versus Bandwidth for Neal-Smith/Bacon Configurations

disappear. A poor aircraft may have characteristics which produce PIO's, with just slight increases in aggressiveness. It is this characteristic which Bacon's gain adjustment exposes.

A first order approximation to pilot aggressiveness is the DC gain of the pilot describing function. A slight increase in this gain from the OCM approximates an increase in pilot aggressiveness. If the increase in closed-loop resonance peak which results from the increased pilot gain is relatively large, one could conclude that the aircraft is sensitive to pilot aggressiveness or, in other words, has oscillatory tendencies.

This argument implies that a gain sensitivity procedure can be used to expose aircraft with oscillatory tendencies. Since the OCM optimizes the controller design in such a way that low frequency droop is sacrificed for resonance peak, excessive droop results for configurations with oscillatory tendencies. Using these ideas, a gain sensitivity parameter is defined to be,

$$
\mathrm {S P} \triangleq \mathrm {D R O O P} \times \frac {\Delta \left| \frac {\theta_ {\mathrm {R}}}{\theta_ {\mathrm {c}}} \right| _ {\max }}{\Delta \mathrm {K}} (\mathrm {d B}). \tag {5.5}
$$

The term, DROOP, is the magnitude of the "droop" for the case in question, obtained directly from the closed-loop OCM analysis (see Figure 5.2). The other term on the right hand side is the relative gain sensitivity which is determined by calculating the change in resonance peaks obtained using the basic pilot (model) gain and that obtained using a perturbed gain, $\delta K$ . The sensitivity is the ratio of the change in resonance peaks, $\left|\Delta \left|\frac{\theta_{\mathrm{R}}}{\theta_{\mathrm{C}}}\right|_{\max}\right|$ , to the gain difference ( $\Delta K$ ).

To justify the validity of using SP as a measure of oscillatory tendency, consider Table 5.1. This table presents the resonance peaks of the configurations from the Neal-Smith study and the Bacon study and the values of the SP calculated for the same configurations.

Table 5.1 Comparison of Resonance Peak and SP Values   

<table><tr><td rowspan="2">Config.</td><td colspan="2">Resonance Peak (dB)</td><td rowspan="2">SP (dB)</td></tr><tr><td>Neal-Smith</td><td>Bacon</td></tr><tr><td>1A</td><td>7.0</td><td>7.19</td><td>1.33</td></tr><tr><td>1B</td><td>0.5</td><td>1.86</td><td>0.49</td></tr><tr><td>1C</td><td>2.0</td><td>4.84</td><td>1.13</td></tr><tr><td>1D</td><td>0.0</td><td>1.83</td><td>0.39</td></tr><tr><td>1E</td><td>9.0</td><td>3.59</td><td>0.73</td></tr><tr><td>2A</td><td>3.0</td><td>4.97</td><td>1.50</td></tr><tr><td>2B</td><td>7.0</td><td>11.37</td><td>2.44</td></tr><tr><td>2C</td><td>2.0</td><td>1.20</td><td>0.93</td></tr><tr><td>2D</td><td>2.0</td><td>1.24</td><td>0.84</td></tr><tr><td>2E</td><td>3.5</td><td>3.28</td><td>1.40</td></tr><tr><td>2F</td><td>2.5</td><td>3.90</td><td>1.20</td></tr><tr><td>2G</td><td>6.0</td><td>9.25</td><td>2.09</td></tr><tr><td>2H</td><td>3.0</td><td>2.50</td><td>0.81</td></tr><tr><td>2I</td><td>7.0</td><td>6.36</td><td>1.60</td></tr><tr><td>3A</td><td>-1.0</td><td>0.68</td><td>0.28</td></tr><tr><td>4A</td><td>10.0</td><td>10.17</td><td>2.26</td></tr><tr><td>5A</td><td>&gt;12</td><td>18.21</td><td>3.71</td></tr><tr><td>6C</td><td>1.5</td><td>1.25</td><td>0.35</td></tr><tr><td>7C</td><td>0.0</td><td>0.77</td><td>0.17</td></tr><tr><td>8A</td><td>0.0</td><td>0.646</td><td>0.11</td></tr></table>

The trends between the three parameters, for the most part, agree well with each other. Furthermore, Figure 5.9, when compared with Figure 5.7, indicates that SP is an analogous measure of oscillatory tendencies and can therefore be used instead of resonance peak in the analysis.

# Application Of The Neal-Smith/Bacon Analysis To The Data Base Configurations

In order to apply the Neal-Smith/Bacon analysis method, a clear understanding $c^{\prime}$ the similarities and differences between the type of configurations studied by Bacon and the flexible aircraft of the data base of Chapter 3 is necessary. The aircraft used in Bacon's study were some of the configurations used in the Neal-Smith study, and represent basic airframe dynamics with control system dynamics added. The basic aircraft dynamics that were analyzed included only the short-period mode. The added high order modes representing control system dynamics included a real pole, a real zero and a second-order, oscillatory mode. Figure 5.10 shows the basic airframe plus flight control system (FCS) dynamics in the pitch-attitude-rate-to-stick-deflection transfer function. The short period dynamics are determined by $T_{\theta_2}$ and by $\omega_{sp}$ and $\varsigma_{sp}$ and the rCS dynamics are determined by $\tau_1$ , $\tau_2$ , $\omega_3$ and $\varsigma_3$ .

The flexible aircraft of this study also have higher order modes but they correspond to aeroelastic effects and not FCS effects. The dynamics of the flexible aircraft have already been discussed in Chapters 2 and 4 and it will suffice to summarize them with Figure 5.11. Here the rigid-body dynamic parameter: are $T_{\theta_1}, T_{\theta_2}, \omega_{ph}, \varsigma_{ph}, \omega_{sp}$ and $\varsigma_{sp}$ , and the aeroelastic effects lead to $\sigma_i, \xi_i (i = 1, \dots, m)$ and $\omega_i, \varsigma_i (i = 1, \dots, m)$ where $m$ equals the number of structural modes included in the vehicle model.

An important step in the analysis is to decide on an appropriate cost function $(J_{\mathfrak{p}})$ . In the case of flexible aircraft the pilot sees or senses total

(8p) dS   
图片摘要：该图主要展示 5.9。
![](images/6957c921bdf3c79bcb0dbdc111b31bb62a4bdbde55f76b0465a22f9878b72e3b.jpg)  
Figure 5.9   
SP versus PC for Neal-Smith Configurations

Dynamics of Neal-Smith Configurations   
图片摘要：该图主要展示 5.9。
![](images/ad48db0ee65c61ba3ffc1a41e94be9df84a4a99f1f0585203b2fc0a7c52def83.jpg)  
Figure 5.10

图片摘要：该图主要展示 5.10。
![](images/b3339b811bf5b3257d5c977de0a2b04127ea4da94274d5ea163cdcee4151c95d.jpg)  
Figure 5.11   
Dynamics of Flexible Configurations

tracking error $(\epsilon_{\mathbf{T}} \triangleq \theta_{\mathbf{T}} - \theta_{\mathbf{C}})$ , with structural effects included. Choosing total error as the minimized parameter, however, may not correctly reflect the pilot's objectives. The pilot comments from the simulation of the data base configurations suggest that the pilot tried to track rigid-body error.

The following quotes are typical of the pilot comments that resulted from the simulation study [2].

For Configuration 8, the pilot comments included -

"more oscillation involved due to elasticity apparently, but it was high enough frequency that it was easy to ignore that and simply to fly the rigid body ..." [2]

For Configuration 7 the pilot comments included -

“it was not too difficult to ignore (the oscillation) and to fly the rigid (body) ...” [2]

These comments indicate that the pilot places more emphasis on keeping the rigid tracking error low than on minimizing total (displayed) tracking error. (Also see [12,14].) Therefore, the appropriate cost function for the flexible aircraft is,

$$
J _ {\mathrm {p}} \left(\theta_ {\mathrm {R}}\right) = \mathrm {E} \left\{\lim  _ {\mathrm {T} \rightarrow \infty} \frac {1}{\mathrm {T}} \int_ {0} ^ {\mathrm {T}} \left(\iota_ {\mathrm {R}} ^ {2} + \mathrm {g} \dot {\mathrm {u}} _ {\mathrm {p}} ^ {2}\right) \mathrm {d t} \right\} \tag {5.6}
$$

- where $\epsilon_{\mathbb{R}} \triangleq (\theta_{\mathbb{R}} - \theta_{\mathbb{C}})$ and $\mathbf{g}$ is chosen to obtain the desired $\tau_{\mathfrak{n}}$ .

Bacon has shown [12,13] that the choice of $\tau_{\mathfrak{n}}$ takes the place of bandwidth in the Neal-Smith method. The value of $\tau_{\mathfrak{n}}$ is chosen to reflect pilot aggressiveness in the tracking task and determines the bandwidth of the closed-loop system. As $\tau_{\mathfrak{n}}$ increases, by increasing $\mathbf{g}$ , the bandwidth decreases. Low $\tau_{\mathfrak{n}}$ , which represents "aggressive behavior", results in a fast closed-loop system and so a high bandwidth. Therefore, to obtain the maximum possible bandwidth, $\tau_{\mathfrak{n}}$ should be set at the lowest physically possible value, which is usually considered to be 0.1 seconds. [8] The value of $\mathbf{g}$ used in this study to obtain a $\tau_{\mathfrak{n}}$ of approximately 0.1 seconds was,

$$
\mathbf {g} = 0. 0 0 4 0.
$$

The analysis includes the v.hicle dynamics, the pilot observations and the command signal dynamics. These factors must be chosen to be consistent with the task. The complete pilot observation vector therefore includes $\epsilon_{\mathbf{T}}$ and $\dot{\iota}_{\mathbf{T}}$ , $\theta_{\mathbf{T}}$ and $\theta_{\mathbf{T}}$ . These four parameters are naturally displayed to the pilot in the tracking task.

The intermediate output of the analysis consists of the controller gains, closed-loop eigenvalues, rms values of the inputs, states and output parameters, cost function values, optimal estimator gains and, most importantly for this application, frequency responses for selected transfer functions. By combining the transfer functions properly, the desired closed-loop transfer function frequency response, similar to that of Neal and Smith, can be formed.

Consider the block diagram of the tracking task in Figure 5.12. The closed-loop transfer function of interest in this study is $\frac{\theta_{\mathbf{R}}(\mathbf{s})}{\theta_{\mathbf{C}}(\mathbf{s})}$ , since rigid-body attitude, $\theta_{\mathbf{R}}$ , is what the pilot "cares about" in rating the performance of the aircraft. This transfer function can be written as,

$$
\begin{array}{l} \frac {\theta_ {R} (s)}{\theta_ {C} (s)} = \frac {H (s) \cdot G _ {1} (s)}{1 + H (s) \cdot G _ {1} (s) \cdot G _ {2} (s)} \tag {5.7} \\ = \frac {\frac {\theta_ {R} (s)}{\epsilon_ {T} (s)}}{1 + \frac {\theta_ {T} (s)}{\epsilon_ {T} (s)}} \\ \end{array}
$$

The transfer functions of interest are therefore $\frac{\theta_{\mathbf{R}}(\mathbf{s})}{\epsilon_{\mathbf{T}}(\mathbf{s})}$ and $\frac{\theta_{\mathbf{C}}(\mathbf{s})}{\epsilon_{\mathbf{T}}(\mathbf{s})}$ . Table 5.2 summarizes the numerical values used to obtain the desired results from the analysis.

The vehicle dynamics (Equations 4.21-4.23) are the same as those used in the open-loop irrodal analysis. These consist of the $\mathbf{A}_{\nu}$ and $\mathbf{B}$ matrices of the data base configurations. The $\mathbf{D}$ matrix is zero however since gust disturbance dynamics is not considered in this analysis.

Block Diagram of Tracking Analysis   
图片摘要：该图主要展示 5.12。
![](images/04cb839af8567e1745ed04c6499e77a82b82dcbcf5780f6189f5b323de7443e4.jpg)  
Figure 5.12

Table 5.2 Summary of Closed-Loop Analysis Inputs   

<table><tr><td rowspan="2">Observational Thresholds</td><td>θR, θT, εT</td><td>8.7 x 10-4rad °</td></tr><tr><td>θR, θT, iT</td><td>3.1 x 10-3rad °/sec °</td></tr><tr><td rowspan="2">Variance of Sensor Noise</td><td>εT, iT, θT, θT</td><td>-20 dB °</td></tr><tr><td>θR, θR</td><td>-6 dB</td></tr><tr><td rowspan="2">Attention Allocation (ΣA.A. i = 1.0)</td><td>εT, iT, θT, θT</td><td>0.245 °</td></tr><tr><td>θR, θR</td><td>0.01</td></tr></table>

consistent with previous work [13]

The remaining requirement is the command signal dynamics. A command signal $(\theta_{\mathbf{C}})$ , which accurately represents a challenging pitch tracking task and approximates the tracking task used by Neal and Smith, is defined by Equation 5.8.

$$
\ddot {\theta} _ {C} + 0. 5 \dot {\theta} _ {C} + 0. 2 5 \theta_ {C} = w (t) \tag {5.8}
$$

Here, $\theta_{\mathbf{C}}$ is the commanded attitude and $\mathbf{w}(\mathbf{t})$ is zero mean Gaussian white noise of intensity $\overline{\mathbf{V}}_{\mathbf{w}}$ . The intensity of the white noise was chosen to result in an rms value for $\theta_{\mathbf{C}}$ of approximately three (3) degrees.

The resulting, model-compatible, state variable representation has the form,

$$
\dot {\mathbf {x}} _ {\mathrm {O C M}} = \left[ \begin{array}{l l} \mathbf {A} _ {c} & 0 \\ 0 & \mathbf {A} _ {v} \end{array} \right] \cdot \mathbf {x} _ {\mathrm {O C M}} + \left[ \begin{array}{l} 0 \\ \mathbf {B} _ {v} \end{array} \right] \cdot \underline {{\mathbf {u}}} + \left[ \begin{array}{l} \mathbf {E} _ {c} \\ 0 \end{array} \right] \cdot \mathbf {w} \tag {5.9}
$$

where,

$$
\mathbf {x} _ {\mathrm {O C M}} ^ {\mathbf {T}} = \left[ \begin{array}{l l l} \theta_ {\mathrm {C}}, \dot {\theta} _ {\mathrm {C}} & | \mathbf {x} _ {\mathrm {v}} ^ {\mathbf {T}} \end{array} \right]. \tag {5.10}
$$

Here, $\mathbf{A}_{\mathbf{C}}$ and $\mathbf{E}_{\mathbf{C}}$ are the matrices resulting from the state variable representation of the command signal.

Closed-loop evaluation of the model yields the desired frequency responses and the pilot describing function frequency response. The desired closed-loop frequency response, namely $\frac{\theta_{\mathbb{R}}(\mathbf{s})}{\theta_{\mathbb{C}}(\mathbf{s})}$ , is obtained by manipulating the frequency responses according to Equation 5.7 at selected frequencies. That is,

$$
\frac {\theta_ {\mathrm {R}} (\mathrm {j} \omega)}{\theta_ {\mathrm {C}} (\mathrm {j} \omega)} = \left. \frac {\frac {\theta_ {\mathrm {R}} (\mathrm {s})}{\epsilon_ {\mathrm {T}} (\mathrm {s})}}{1 + \frac {\theta_ {\mathrm {T}} (\mathrm {s})}{\epsilon_ {\mathrm {T}} (\mathrm {s})}} \right| _ {\mathrm {s} = \mathrm {j} \omega}. \tag {5.11}
$$

The frequency responses that result from the closed-loop analysis of the eight data base configurations, can be found in Appendix A.5. An example of the frequency responses is shown in Figure 5.13. The "Purdue Pilot" frequency response corresponds to $\mathbf{H}(\mathbf{s})$ or $\frac{\delta(s)}{\epsilon_{\mathrm{T}}(s)}$ and the "Aircraft (O.L.)" frequency response corresponds to $\mathbf{G}_{\mathbf{l}}(\mathbf{s})$ or $\frac{\theta_{\mathrm{R}}(\mathbf{s})}{\delta(\mathbf{s})}$ as depicted in Figure 5.12. The "Aircraft Plus Pilot (O.L.)" frequency response corresponds to $\mathbf{H}(\mathbf{s})\mathbf{G}_{\mathbf{l}}(\mathbf{s})$ or $\frac{\theta_{\mathrm{R}}(\mathbf{s})}{c_{\mathrm{T}}(\mathbf{s})}$ and "Aircraft Plus Pilot (C.L.)" corresponds to the frequency response for $\frac{\theta_{\mathrm{R}}(\mathbf{s})}{\theta_{\mathrm{C}}(\mathbf{s})}$ .

# Numerical Results

The closed-loop system frequency response properties; bandwidth, droop, resonance peak and sensitivity parameter; pilot phase compensation at the bandwidth frequency and pilot rating are summarized in Table 5.3 for each of the data base configurations.

First examine the trends in pilot rating with closed-loop bandwidth. Figure 5.14 is a plot of pilot rating (PR) versus bandwidth frequency $(\omega_{\mathrm{BW}})$ for the eight data base configurations. Though the number of data points is

图片摘要：该图主要展示 5.13。
![](images/b22ba861738c5c6bb1abd74764091b0b7a4e73d2b3fd5a4af230ce6a37719098.jpg)  
B-1 CASE 8:

图片摘要：该图主要展示 5.13。
![](images/167ccd47ae25a6e556d5743c76807d7a9f278edcfdbfaed12742e2854974a3e9.jpg)  
Figure 5.13   
Example: OCM Frequency Responses - Config. 8

图片摘要：该图主要展示 5.13。
![](images/434e1058f66599723cab70e86466f4e082e325896696978fad5de1f204fc635f.jpg)  
B-1 CASE 8:   
Figure 5.13 (con't)   
Example: OCM Frequency Responses - Config. 8

图片摘要：该图主要展示 5.13 (con't)。
![](images/7bc07bb9e64060324685e66ec856c88437f11986a19e234863bdef30b0691276.jpg)  
B-1 C:SE 8:   
Figure 5.13 (con't)   
Example: OCM Frequency Responses - Config. 8

图片摘要：该图主要展示 5.13 (con't)。
![](images/58bb6faf6bf9e1526a9c8ed4188b365b60db148b1831592eb5e9681c0d243415.jpg)  
B-1 CASE 8:

Figure 5.13 (conn)   
Example: OCM Frequency Responses - Config. 8   
图片摘要：该图主要展示 5.13 (conn)。
![](images/0857b678d0311b3a9df8e388b674ee03f23d8086c5b32b223d2b4d0fb5f40ebf.jpg)  
BANOWIDTHS 2.00 R&D/SEC   
PILOT COMPENSATION: -53.30 DEG   
RESONANCE PEAK 1.65 DB   
DROOP -1.23 D   
SENSITIVITY .53 02

# APPENDICES

图片摘要：该图主要展示 5.14。
![](images/1cd4b9698216b20b3a72f4980d6ffa0c99a729fb7cd6a9b5c86a00e2a4ee4d30.jpg)  
Figure 5.14   
PR versus BW for Data Base Configurations

Table 5.3 Summary of Closed-I nop analysis of Data Base Configurations   

<table><tr><td>Case</td><td>ωBW rad/sec</td><td>DROOP dI</td><td>θR/θC</td><td>max dB</td><td>SP dB</td><td>PC deg</td><td>PR</td></tr><tr><td>1</td><td>2.29</td><td>1.0</td><td colspan="2">2.17</td><td>0.67</td><td>-58.9</td><td>1.6</td></tr><tr><td>2</td><td>1.80</td><td>1.51</td><td colspan="2">1.12</td><td>0.40</td><td>-66.6</td><td>2.0</td></tr><tr><td>3</td><td>0.07</td><td>8.45</td><td colspan="2">6.99</td><td>7.59</td><td>-96.02</td><td>5.9</td></tr><tr><td>4</td><td>1.77</td><td>1.93</td><td colspan="2">-0.11</td><td>0.78</td><td>-16.08</td><td>3.1</td></tr><tr><td>5</td><td>1.53</td><td>2.14</td><td colspan="2">0.10</td><td>0.49</td><td>-68.9</td><td>2.0</td></tr><tr><td>6</td><td>0.10</td><td>6.94</td><td colspan="2">9.59</td><td>5.7</td><td>-72.3</td><td>6.7</td></tr><tr><td>7</td><td>1.76</td><td>1.56</td><td colspan="2">1.02</td><td>0.48</td><td>-60.55</td><td>2.3</td></tr><tr><td>8</td><td>2.00</td><td>1.23</td><td colspan="2">1.69</td><td>0.56</td><td>-53.3</td><td>1.9</td></tr></table>

limited, the trend is consistent with that of [12,13]. The configurations with low closed-loop bandwidth have poor pilot ratings and the configurations with relatively high bandwidth have better pilot ratings.

Next, consider the closed-loop system parameters of Neal and Smith. Figure 5.15 is a plot of "Neal-Smith like" criteria for the eight data base configurations. However, in place of resonance peak, the sensitivity parameter (SP) is used as a measure of oscillatory tendencies. Note that the configurations with similar pilot ratings (PR) are grouped together and the configurations with poorer ratings (i.e. configurations 3,4 and 6) are distinctly separated from the better aircraft. Also, two of the configurations (i.e. 3 and 6) have relatively large values of SP, indicating oscillatory tendencies. This oscillatory nature is also noted in the pilot comments from the simulations (see Table 3.2). Notice that the value of SP for Configuration 4 indicates that its poorer performance is not due to oscillatory tendencies. The pilot compensation (PC), though, indicates that the pilot has to supply more lead for the best performance, or in other words, the aircraft response is sluggish. This sluggish nature is also noted in the pilot comments from the simulations (see Table 3.2).

Therefore, the analysis not only grouped aircraft with similar pilot ratings, but it also exposed response characteristics that contribute to degraded performance. Though there is not enough data to determine boundaries defining the three handling qualities levels, the trends tend to imply their existence. The implication is that this closed-loop analysis might be able to identify when actoelastic effects significantly affect the dynamics of flexible aircraft. That is, the Neal-Smith/Bea analysis, appropriately utilized, may

图片摘要：该图主要展示 5.15。
![](images/3982aa35eb52e3b242a1b54c3e18b63f7a92ccafd04e52dad7194d9f21744db6.jpg)  
SP (dB)   
Figure 5.15   
SP versus PC for Data Base Configurations

appl: to large flexible aircraft as well as small aircraft with added control system dynamics. More specifically, the results indicate that the data base configurations with poor tracking performance received the poor results because of sensitivity to forward path gain (used to approximate pilot aggressiveness) and indicates oscillatory tendencies.

# CHAPTER VI CONCLUSIONS

The objective of this study was to investigate when and how structural effects (especially dynamic aeroelastic effects) affect the dynamics of aircraft. Two analysis methods, an open-loop modal technique and a pilot-in-the-loop method, were used to see how aeroelastic modes affect the dynamics of aircraft in the longitudinal axis. Both procedures were applied to a family of aircraft which exhibit considerable aeroelastic effects.

The results of the modal analysis indicate that when the magnitudes of the modal impulse residues of the aeroelastic modes become large compared to the residue magnitudes of the rigid-body modes for important outputs, the dynamics can change significantly and in such a way that the handling qualities of the vehicle may be degraded. In addition, the trends in impulse residue magnitudes for some inputs are closely related to the trends in pilot ratings of the configurations from the fixed based simulation.

The pilot-in-the-loop analysis verifies that as the frequencies of the aeroelastic modes decrease, the performance of the vehicle tends to degrade. More specifically, as the structural vibration frequencies were decreased, the sensitivity of the closed-loop system to perturbations in forward path gain increased. This effect was demonstrated by plotting feed-forward gain sensitivity (SP) versus pilot compensation (PC) in a tracking task. It was also shown that the bandwidth of the closed-loop system correlates with the subjective pilot ratings and those configurations with lower structural frequencies tend to have lower closed-loop bandwidths. These results indicate that reduced aeroelastic mode frequencies can cause degraded handling qualities which may appear in the form of oscillatory tendencies and sluggish response.

In conclusion, dynamic aeroelastic effects can definitely contribute to degraded performance of aircraft in the longitudinal axis. The aeroelastic modes contribute to poor performance primarily by, 1) introducing dynamic effects of their own in the form of high frequency oscillations, and 2) modal interaction which alters the dynamics of the rigid-body modes. In addition,

these effects can occur when the aeroelastic mode frequencies are still several times higher than the frequencies of the rigid-body modes! As a consequence of these effects, aeroelastic modes should be taken into account for vehicles that exhibit these dynamic aeroelastic effects.

Future work in this area should include expanding the data base. With a larger set of configurations to study, the analysis methods developed here can be applied to obtain more conclusive results which may lead to quantitative rules for specifying handling qualities for flexible aircraft. For example, it may be possible to define handling qualities boundaries in the SP versus PC (i.e. sensitivity parameter versus pilot compensation) plot from the pilot-in-the-loop analysis. The boundaries would divide the plot into three regions which correspond to the three handling qualities levels. Also, the analysis methods developed here should be extended to study lateral-directional dynamics in order to understand the problem more completely. Finally, since it has been shown that aeroelastic modes can be important, future work should be aimed at developing control synthesis techniques that utilize the modal techniques, either directly or indirectly, to gain insight into the consequences of aeroelastic effects. Such techniques might address restoring excellent handling qualities to vehicles with poor handling due to dynamic aeroelastic effects.

LIST OF REFERENCES

# LIST OF REFERENCES

[1] Military Specification - Flying Qualities of Piloted Aircraft, MIL-F8785C (ASG), 1980.   
[2] Yen, W.Y., "Effects of Dynamic Aeroelasticity on Handling Qualities and Pilot Rating." PhD Thesis, Department of Aeronautical and Astronautical Engineering, Purdue University, 1977.   
[3] Gilbert, M.G., Schmidt, D.K., and Weisshaar, T.A., "Quadratic Synthesis of Active Controls for an Aeroelastic Forward-Swept-Wing Aircraft," Journal of Guidance, Control and Dynamics, March-April, 1984, pg. 190.   
[4] D'Azzo, J., and Houpi, C., Linear Control System Analysis and Design: Conventional and Modern. New York: McGraw-Hill, 1975.   
[5] Meirovitch, L., Elements of Vibration Analysis. New York: McGraw-Hill, 1975.   
[6] Cooper, G.E., and Harper, R.P., "The Use of a Pilot Rating Scale in the Evaluation of Aircraft Handling Qualities," NASA TND-5153, April, 1969.   
[7] Teper, G.L., “Aircraft Stability and Control Data,” Systems Technology Inc. Technical Report 176-1, April, 1979.   
[8] McRuer, D.T., and Krendel, E.S., “Mathematical Models of Human Pilot Behavior,” North Atlantic Treaty Organization Advisory Group for Aerospace Research and Development, AGARDograph No. 188, Jan., 1974.   
[9] Roberts, D.A. et. al., "Effects of Control Laws and Relaxed Stability on Vertical Ride Quality of Flexible Aircraft," NASA-CR-143843, April, 1977.

[10] Neal, T.P., and Smith, R.E., "An Inflight Investigation to Develop System Design Criteria for Fighter Airplanes," Flight Dynamics Laboratory, WPAFB, Ohio, AFFDL-TR-70-74, Vol. I, Dec., 1970.   
[11] Kleimman, D.L., Baron, S., and Levison, W.H., "An Optimal Control Model of Human Response, Parts I and II," Automatica, Vol. 6, May, 1970, pp. 357-383.   
[12] Bacon, B.J., and Schmidt, D.K., "An Optimal Control Approach to Pilot/Vehicle Analysis and the Neal-Smith Criteria," Journal of Guidance and Control, Vol. 6, No. 5, Sept.-Oct., 1983, pp. 339-347.   
[13] Bacon, B.J., “A Modern Approach to Pilot/Vehicle Analysis and the Neal-Smith Criteria,” Master Thesis, Department of Aeronautics and Astronautics, Purdue University, 1982.   
[14] Schmidt, D.K., "Pilot Modeling and Closed-Loop Analysis of Flexible Aircraft in the Pitch Tracking Task," AIAA Paper No. 83-2231, Guidance and Control Conference, Gatlinburg TN, Aug., 1983.

# Appendix A.1 Scaling Transformation for Mode Identification

The aircraft states are scaled so that the elements of the eigenvectors have comparable units. This is done so that the eigenvectors can be used to simplify the task of identifying the modes of the system. That is, aid in determining which eigenvalues are associated with, for example, the short-period mode or one of the aeroelastic modes.

The scaling of the system states is accomplished by means of a similarity transformation applied to the vehicle state variable model of the form,

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
$$

(A.1.1)

$$
\mathbf {y} = \mathbf {C x} + \mathbf {D u}.
$$

Consider a flexible aircraft in the longitudinal axis. The following state vector definition is representative of such an aircraft.

$$
\mathbf {x} ^ {T} \triangleq [ u, \alpha , \theta , \dot {\theta}, \eta , \dot {\eta} ] \tag {A.1.2}
$$

In the longitudinal axis, pitch angle and pitch rate are two pertinent dimensions. The vehicle states can be scaled so that all of them are nondimensional or can be physically interpreted as angles and angular rates, (i.e. units of radians and radians per second). The forward velocity perturbation, $\mathbf{u}$ , can be divided by the cruise velocity, $\mathbf{U_0}$ . The generalized elastic deflection, $\eta$ , can be multiplied by the mode slope, $\phi'$ , which makes the state physically analogous to elastic pitch angle with units of radians. This is evident when considering the equation for total-elastic pitch angle,

$$
\theta_ {\mathrm {T}} = \theta_ {\mathrm {R}} - \sum_ {\mathrm {i} = 1} ^ {\mathrm {n}} \eta_ {\mathrm {i}} (\mathrm {t}) \phi^ {\prime} _ {\mathrm {i}} \left(\mathrm {l} _ {\mathrm {x}}\right) \tag {A.1.3}
$$

Similarly, the generalized rate, $\dot{\eta}$ , can be multiplied by the mode slope. The result is that the state becomes analogous to elastic pitch rate with units of radians per second. The rigid-body pitch attitude, $\theta$ , pitch rate, $\dot{\theta}$ , and angle of attack, $\alpha$ , are expressed in radians and so do not need to be scaled.

For the model and the scaling factors described above, the similarity transformation can be defined to be,

$$
\mathbf {T} = \left[ \begin{array}{c c c c c c} \frac {1}{U _ {0}} & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & \phi^ {\prime} & 0 \\ 0 & 0 & 0 & 0 & 0 & \phi^ {\prime} \end{array} \right]. \tag {A.1.4}
$$

The transformed state vector is defined by,

$$
\tilde {\mathbf {x}} = \mathbf {T} _ {\mathbf {X}}. \tag {A.1.5}
$$

Applying the transformation to the vehicle model in Equation (A.1.1) results in the scaled system,

$$
\dot {\tilde {\mathbf {x}}} = \mathbf {T} \mathbf {A} \mathbf {T} ^ {- 1} \tilde {\mathbf {x}} + \mathbf {T} \mathbf {B} \mathbf {u}, \tag {A.1.6}
$$

$$
\mathbf {x} = \mathbf {C T} ^ {- 1} \tilde {\mathbf {x}} + \mathbf {D} \mathbf {u}.
$$

An important property of a similarity transformation is that it has no affect on the eigenvalues or residues of the original system. This property allows the scaling transformation to be applied to the vehicle model without altering the results of the modal analysis.

Therefore, by applying the scaling transformation described above, the units of the eigenvectors can be adjusted to make identifying the modes of the system easier. In addition, this can be done without affecting the results of the modal analysis procedure.

# Appendix A.2 $\mathbf{n}_{\pm}$ as a Function of the Vehicle States

Consider the longitudinal state variable model of an aircraft, Equation (A.2.2), with the following state variable definition.

$$
\mathbf {x} ^ {T} \triangleq [ u, \alpha , \theta , \dot {\theta}, \eta , \dot {\eta} ] \tag {A.2.1}
$$

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
$$

(A.2.2)

$$
\mathbf {y} = \mathbf {C x} + \mathbf {D u}
$$

The plunge acceleration of an aircraft $(\mathfrak{n}_{\mathbf{z}})$ is described by the following expression,

$$
n _ {z} (t) = \frac {1}{g} \left[ U _ {0} \dot {\gamma} (t) + I _ {x} \ddot {\theta} (t) - \sum_ {i = 1} ^ {m} \phi_ {i} \left(I _ {x}\right) \ddot {\eta} _ {i} (t) \right], \left(g ^ {\prime} s\right) \tag {A.2.3}
$$

where $\mathbf{g} =$ gravitational acceleration, (ft/sec²)

$$
\mathbf {U} _ {\mathbf {0}} = \text {c r u i s e v c l o c i t y}, (f t / \sec)
$$

$$
l _ {x} = \text {d i s t a n c e f r o m c . g . t o c o o k p i t , (f t)}
$$

$$
\phi_ {i} = \text {m o d e s h a p e o f i t h a c r o e l a s t i c m o d e , (f t)}
$$

$$
m = \text {n u m b e r o f a c r o c l i s t i c m o d e s}
$$

The other parameters in Equation (A.2.3) can be expressed in terms of the states of the aircraft.

The flight path angle is defined as,

$$
\gamma (t) \triangleq \theta (t) - a (t). \tag {A.1.1}
$$

Therefore,

$$
\dot {\gamma} (t) = \dot {\theta} (t) - \dot {\alpha} (t). \tag {A.2.5}
$$

Note that $\dot{\theta} (t)$ is a state of the vehicle but $\dot{\alpha} (t)$ is the time derivative of the vehicle state $\alpha (t)$ . Note also that the derivative of the angle of attack with respect to time can be written as,

$$
\dot {\alpha} (t) = \mathbf {A} _ {\dot {\alpha}} \mathbf {x} + \mathbf {B} _ {\dot {\alpha}} \mathbf {u} \tag {A.2.6}
$$

- where $\mathbf{A}_{\dot{\alpha}}$ and $\mathbf{B}_{\dot{\alpha}}$ are the rows of the matrices $\mathbf{A}$ and $\mathbf{B}$ , respectively, associated with the scalar equation for $\dot{\alpha}(t)$ .

Similarly, $\ddot{\theta}(t)$ and $\ddot{\eta}(t)$ are the time derivatives of the states $\dot{\theta}(t)$ and $\dot{\eta}(t)$ . Therefore,

$$
\ddot {\theta} (t) = \mathbf {A} _ {i j} \mathbf {x} + \mathbf {B} _ {j i} \mathbf {u} \tag {A.2.7}
$$

and,

$$
\ddot {\eta} (t) = \mathbf {A} _ {\ddot {\eta}} \mathbf {x} + \mathbf {B} _ {\dot {\eta}} \mathbf {u} \tag {A.2.8}
$$

- where $\mathbf{A}_{ij}$ and $\mathbf{B}_{ij}$ , and $\mathbf{A}_{\ddot{\eta}}$ and $\mathbf{B}_{\dot{\eta}}$ are the rows of $\mathbf{A}$ and $\mathbf{B}$ associated with the scalar equations for $\dot{\theta} (t)$ and $\dot{\eta} (t)$ , respectively.

Using Equations (A.2.5), (A.2.6), (A.2.7) and (A.2.8), the expression for the plunge acceleration can be written as,

$$
n _ {z} (t) = \frac {1}{g} \left\{U _ {0} \left(\dot {\theta} (t) - A _ {\dot {o}} x + B _ {\dot {o}} y\right) + I, \left(A _ {\ddot {i}} x + \bar {r} _ {\ddot {i}} y\right) \right.
$$

$$
\left. - \sum_ {i = 1} ^ {m} \phi_ {i} \left(\mathbf {A} _ {\ddot {\eta}} \mathbf {x} + \mathbf {B} _ {\dot {\eta}} \mathbf {u}\right) \right\}. \tag {A.2.9}
$$

Note also that $\theta(t)$ can be written as,

$$
\theta (t) = \mathbf {A} _ {j} \mathbf {x} + \mathbf {B} _ {j} \mathbf {u} \tag {A.2.10}
$$

- where $\mathbf{A}_j$ and $\mathbf{B}_j$ are the rows of $\mathbf{A}$ and $\mathbf{B}$ associated with the scalar equation for $\dot{\theta}(t)$ .

Therefore,

$$
\begin{array}{l} n _ {2} (t) = \frac {1}{g} \left\{U _ {0} \left(\mathbf {A} _ {i} - \mathbf {A} _ {\dot {o}}\right) x + u _ {0} \left(\mathbf {B} _ {j} - \mathbf {B} _ {\dot {o}}\right) u \right. \\ + \left. I _ {x} \left(\mathbf {A} _ {\ddot {j}} x + \mathbf {B} _ {\dot {j}} u\right) - \sum_ {i = 1} ^ {n} \phi_ {i} \left(\mathbf {A} _ {\ddot {j}} x + \mathbf {B} _ {\dot {j}} u\right) \right\}. \tag {A.2.11} \\ \end{array}
$$

By grouping the terms multiplying $\mathbf{x}$ and $\mathbf{y}$ , simple expressions for the rows of $\mathbf{C}$ and $\mathbf{D}$ associated with the scalar $\mathbf{n}_z$ output equation can be formed.

$$
\mathbf {C} _ {n _ {s}} = \frac {1}{8} \left\{\mathrm {U} _ {0} \left(\mathbf {A} _ {i j} - \mathbf {A} _ {i j}\right) + \mathrm {I} _ {x} \mathbf {A} _ {i j} - \sum_ {i = 1} ^ {n} \phi_ {i} \mathbf {A} _ {i j} \right\} \tag {A.2.12}
$$

$$
\boldsymbol {D} _ {n _ {0}} = \frac {1}{g} \left\{U _ {0} \left(\boldsymbol {B} _ {i} - \boldsymbol {B} _ {o}\right) + I _ {x} \boldsymbol {B} _ {i} - \sum_ {i = 1} ^ {n} \phi_ {i} \boldsymbol {B} _ {i j} \right\} \tag {A.2.13}
$$

- where $\mathbf{C}_{n_s}$ and $\mathbf{D}_{n_s}$ are the row of $\mathbf{C}$ and $\mathbf{D}$ associated with the scalar $n_s$ equation.

This method of determining the proper coefficients for the $\mathbf{C}$ and $\mathbf{D}$ matrices associated with $\mathbf{n}_{\mathbf{s}}$ can be implemented numerically very easily by using a transformation row vector, $\mathbf{x}$ . The definition of the transformation depends on the state vector for the system. For the state definition in Equation (A.2.1), the transformation vector has the following form,

$$
\mathbf {X} \triangleq [ 0, - \frac {\mathrm {U} _ {0}}{\mathrm {g}}, \frac {\mathrm {U} _ {0}}{\mathrm {g}}, \frac {\mathrm {l} _ {\mathrm {x}}}{\mathrm {g}}, 0, - \frac {\phi}{\mathrm {g}} ]. \tag {A.2.14}
$$

Thus,

$$
\mathbf {C} _ {\mathrm {n} _ {\mathrm {a}}} = \mathbf {X} \cdot \mathbf {A} \tag {A.2.15}
$$

and,

$$
\mathbf {D} _ {n _ {1}} = \mathbf {X} \cdot \mathbf {B}. \tag {A.2.16}
$$

<table><tr><td>1. Report No.
NASA CR-177943</td><td colspan="2">2. Government Accession No.</td><td colspan="2">3. Recipient&#x27;s Catalog No.</td></tr><tr><td rowspan="2" colspan="3">4. Title and Subtitle
Analysis of Flexible Aircraft Longitudinal Dynamics and handling Qualities - Volume I - Analysis Methods</td><td colspan="2">5. Report Date
June 1985</td></tr><tr><td colspan="2">6. Performing Organization Code</td></tr><tr><td rowspan="2" colspan="3">7. Author(s)
Martin R. Waszak and David K. Schmidt</td><td colspan="2">8. Performing Organization Report No.</td></tr><tr><td colspan="2">10. Work Unit No.</td></tr><tr><td rowspan="2" colspan="3">9. Performing Organization Name and Address
Purdue University
School of Aeronautics and Astronautics
West Lafayette, IN 47907</td><td colspan="2">11. Contract or Grant No.
NAG-1-254</td></tr><tr><td colspan="2">13. Type of Report and Period Covered
Contractor Report</td></tr><tr><td colspan="3">12. Sponsoring Agency Name and Address
National Aeronautics and Space Administration
Washington, D.C. 20546</td><td colspan="2">14. Sponsoring Agency Code
505-34-03-03</td></tr><tr><td colspan="5">15. Supplementary Notes
NASA Technical Monitors: William D. Grantham and Jarrell R. Elliott
Langley Research Center</td></tr><tr><td colspan="5">16 Abstract
As aircraft become larger and lighter due to design requirements for increased payload and improved fuel efficiency, they will also become more flexible. For highly flexible vehicles, the handling qualities may not be accurately predicted by conventional methods. This study applies two analysis methods to a family of flexible aircraft in order to investigate how and when structural (especially dynamic aeroelastic) effects affect the dynamic characteristics of aircraft.
The first type of analysis is an open-loop modal analysis technique. This method considers the effect of modal residue magnitudes on determining vehicle handling qualities. The second method is a pilot-in-the-loop analysis procedure that considers several closed-loop system characteristics. Both analyses indicated that dynamic aeroelastic effects caused a degradation in vehicle tracking performance, based on the evaluation of some simulation results.</td></tr><tr><td colspan="2">17. Key Words (Suggested by Author(s))
Flexible Aircraft
Flight Dynamics
Handling Qualities
Modal Analysis</td><td colspan="3">18. Distribution Statement
Unclassified - Unlimited
Subject Category 08</td></tr><tr><td>19 Security Classif. (of this report)
Unclassified</td><td>20. Security Classif. (of this page)
Unclassified</td><td>21. No. of Pages
108</td><td colspan="2">22. Price
A06</td></tr></table>
