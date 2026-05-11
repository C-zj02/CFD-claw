# General Disclaimer

# One or more of the Following Statements may affect this Document

- This document has been reproduced from the best copy furnished by the organizational source. It is being released in the interest of making available as much information as possible.   
- This document may contain data, which exceeds the sheet parameters. It was furnished in this condition by the organizational source and is the best copy available.   
- This document may contain tone-on-tone or color graphs, charts and/or pictures, which have been reproduced in black and white.   
This document is paginated as submitted by the original source.   
- Portions of this document are not fully legible due to the historical nature of some of the material. However, it is the best reproduction available from the original submission.

# NASA TECHNICAL MEMORANDUM

NASA TM X-62,144

VZ9XW↓VSAN

(NASA-TM-X-62144) LONGITUDINAL HANDLING QUALITIES DURING APPROACH AND LANDING OF A POWERED LIFT STOL AIRCRAFT (NASA) 68 p HC A04/MF A01 CSCL O

图片摘要：该图片为文档封面或首页内容，主题与General Disclaimer相关。
![](images/3d5787a9306d8ac00b6885b866dcc74878272f65936511bf91f66837454495d3.jpg)

N77-33151

G3/05 51362

LONGITUDINAL HANDLING QUALITIES DURING APPROACH ANDLANDING OF A POWERED LIFT STOL AIRCRAFT

James A. Franklin and Robert C. Innis

Ames Research Center
Moffett Field, Calif. 94035

March 1972

图片摘要：该图片与LONGITUDINAL HANDLING QUALITIES；DURING APPROACH AND LANDING这部分内容相关。
![](images/fb7656f576d4e5173e105a4eaaa9e7c93517a9d3f3cd2a71b65ec2b7f99f0e58.jpg)

# LONGITUDINAL HANDLING QUALITIES

# DURING APPROACH AND LANDING

# OF A POWERED LIFT STOL AIRCRAFT

James A. Franklin and Robert C. Innis

SUMMARY

Longitudinal handling qualities evaluations were conducted on the Ames Research Center Flight Simulator for Advanced Aircraft (FSAA) for the approach and landing tasks of a powered lift STOL research aircraft. The test vehicle was a DeHavilland of Canada C-8A aircraft modified with a new wing incorporating internal blowing over an augmentor flap. The investigation included (1) use of various flight path and airspeed control techniques for the basic vehicle, (2) assessment of stability and command augmentation schemes for pitch attitude and airspeed control, (3) determination of the influence of longitudinal and vertical force coupling for the power control, (4) determination of the influence of pitch axis coupling with the thrust vector control, and (5) evaluations of the contribution of stability and command augmentation to recovery from a single engine failure. Three pilots, all having flight experience in powered lift aircraft participated in the simulator program. Results are presented in the form of pilot ratings and commentary substantiated by landing approach time histories.

# NOTATION

$\mathbf{C}_{\mathbb{L}}$ Lift coefficient

c Mean aerodynamic chord, ft

F s Longitudinal column control force, lbs.

Elevator hinge moment, ft. lbs

H $\delta_{\mathrm{e}}$ Dimensional elevator hinge moment derivative due to elevator deflection, $\frac{1}{I_{\mathrm{e}}}\frac{\partial H_{\mathrm{e}}}{\partial \delta_{\mathrm{e}}}$ , rad/sec²/rad

H $\dot{\mathbf{e}}$ Dimensional elevator hinge moment derivative due to elevator deflection rate, $\frac{l}{I_e}\frac{\partial H_e}{\partial \dot{\mathbf{e}}_e}$ , l/sec

h, h Course and fine altitude, ft.

Ie Elevator momen+ of inertia, slug-ft2

I y Aircraft moment of inertia, slug-rt²

Pitch attitude feedback gain to elevator or to nozzle, deg/deg

Pitch rate feedback gain to elevator, deg/deg/sec

K. Column feed forward gain, deg/deg

K Column rate feed forward gain, deg/sec/deg

K_u Airspeed feedback gain to nozzle, deg/ft/sec

K. Longitudinal acceleration gain to nozzle, deg/ft/sec²

M Pitching moment, ft. lbs

Pitching moment derivative due to throttle,

I M 1y 8sT, rad/sec2/1b

M

Pitching moment derivative due to nozzle,

1 M 1y dEv rad/sec2/

m

Aircraft mass, slugs

n z

Normal acceleration, g's

aB

Aircraft pitch rate, deg/sec

q

Dynamic pressure, lbs/ft²

S

Wing area, ft²

s

Laplace operator

THot

Hot thrust, lbs

1/Tsp1, 1/Tsp2

Roots of the longitudinal characteristic equation nominally associated with the short period mode

(which in this instance are real instead of complex), rad/sec

1/T'sp1, 1/T'sp2

Roots of the short period mode with pitch rate and attitude stabilization, rad/sec

1/T"1,1/T"2

Roots of the short period mode with pitch rate, pitch attitude and airspeed stabilization, rad/sec

1/T'p1, 1/T'p2

Low frequency roots of the longitudinal characteristic equation with pitch rate, pitch attitude, and airspeed stabilization (nominally associated with the phugoid mode), rad/sec

1/Tθ1, 1/Tθ2

Numerator roots of the elevator to pitch attitude transfer function, rad/sec.

iv

1/Th

Low frequency numerator root of the elevator to altitude transfer function, rad/sec

1/T'h1

Low frequency numerator root of the elevator to altitude transfer function in the presence of airspeed stabilization, rad/sec

V.

Airspeed, ft/sec, knots

W

Aircraft gross weight, lbs

X

Longitudinal force, lbs

x

Longitudinal force derivative due to thrust,

$$
\frac {1}{m} \quad \frac {\partial X}{\partial \delta_ {T}}, \quad f t / \sec^ {2} / 1 b
$$

x

Longitudinal force derivative due to nozzle deflection, $\frac{1}{m} \frac{\partial X}{\partial \delta v}, ft / \sec^2 / deg$

x, x e

Fuselage station location of the Pegasus nozzles, in. Vertical force, lbs

Z

Vertical force derivative due to thrust $\frac{1}{m} \frac{\partial Z}{\partial \delta_{T}}$ , ft/sec²/lb

ZsT

Z

Vertical force derivative due to nozzle deflection, $\frac{1}{m} \frac{\partial z}{\partial \delta v}, ft / \sec^2 \theta$

z, z e

Water line location of the Pegasus nozzles, in

$\alpha$

Angle of attack, deg

#

Flight path angle, deg

$\Delta$

Incremental value

8c

Longitudinal column deflection, in

#

Elevator deflection, deg

eA

Command to elevator surface actuator

$\delta_{\mathrm{e_c}}$

Commanded elevator deflection, deg

S SAS

Stability augmentation actuator input to the elevator

e sc

Stability augmentation actuator command

6H

Stabilizer position, deg

$\pmb{\delta}_{\mathrm{f}}$

Flap deflection, deg

$\pmb{\delta}_{\mathrm{T}}$

Hot thrust, lbs

Throttle position, deg

8,

Pegasus nozzle deflection, deg

8y

Pegasus nozzle command, deg.

SAS

Stability augmentation input to the nozzle

pi

Pilot's nozzle control deflection, deg

$\pmb{\epsilon}_{\mathrm{gs}}, \pmb{\epsilon}_{\mathrm{loc}}$

glide slope and localizer errors, deg

A,ωA

Damping ratio and natural frequency of the elevator

surface actuator

5p,ωp

Damping ratio and natural frequency of the phugoid mode

p

Damping ratio and natural frequency of the phugoid mode

as modified by pitch rate and attitude stabilization

s·ωs

Damping ratio and natural frequency of the elevator

SAS actuator

50, 0

Damping ratio and natural frequency of the numerator

roots of the elevator to pitch attitude transfer

function in the presence of airspeed stabilization

Air density, slugs/ft<sup>3</sup>

P

Standard deviation of atmospheric gust velocities, ft/sec

$\sigma_{\mathrm{gust}}$

Natural frequency of the elevator-spring tab system, rad/sec

W

vi

# INTRODUCTION

The pilot's control of an aircraft capable of landing at the slow flight speeds associated with STOL operation is complicated by problems which are generally more severe than those of conventional aircraft landing at higher speeds. Longitudinal control of pitch attitude, flight path, and airspeed are all adversely affected by the low speed, high wing loading, and high inertias typical of the STOL transport class of vehicle. In addition, the availability of powered lift for the pilot's control and the associated influence on lift, drag, and pitching moment of engine power setting makes these aircraft respond to the application of power in a fashion considerably different (and not necessarily favorably so) from aircraft having conventional lift concepts. These problems are generally recognized (not necessarily in order of importance) as:

- poor longitudinal static stability so that attitude and speed tend to wander during unintended operation   
- unstable flight path-attitude relationship associated with operation on the "back side" of the thrust required curve   
- changes in speed and angle of attack with power setting where speed and angle of attack are not uniquely related as they are for aircraft using conventional lift concepts.   
- attitude changes required to hold speed while changing flight path with power which are opposite those of a conventional aircraft.

- sluggish flight path response to attitude changes   
- large variations in angle of attack with power   
- inability to use any single control to flare the airplane adequately for landing

Since these objectionable qualities tend to be inherent in the STOL category of vehicle, a simulator program was initiated to investigate what vehicle and control system characteristics or modifications are required to provide satisfactory longitudinal handling qualities for the approach and landing task. To enable early reporting the results are presented here largely in the form of time histories with limited discussion, in the form of brief observations of salient features of the responses, and pilot commentary.

# DESCRIPTION OF THE SIMULATION

As part of the program to develop a flight research vehicle for demonstration of the augmentor wing powered lift concept and for research on STOL performance, handling qualities, and operating problems, a real time digital simulation of the proposed vehicle was developed for the FSAA. The basic augmentor wing aircraft shown in Fig. 1 consists of a DeHavilland C-8A Buffalo airframe modified with a new wing incorporating internal blowing over an augmentor flap (1). The aircraft is powered by Rolls Royce Spey 80LSF engines with offtakes from the compressor section for wing blowing and with direct hot thrust which can be deflected through Pegasus nozzles for thrust vector control. Pitch control is accomplished through the Buffalo's existing manually actuated elevator - spring tab system. Roll control and stability augmentation utilize the modified aircraft's blown ailerons, spoilers, and augmentor flap choke which are integrated to give an essentially linear rolling moment relation to cockpit control deflection. Directional control and stability augmentation function through the Buffalo's existing power actuated two segment rudder. Lateral-directional stability augmentation provide roll damping, spiral mode stabilization, Dutch roll damping and turn coordination to compensate for the objectionable handling qualities of the basic aircraft for the STOL flight conditions of interest.

The vehicle simulation was built on the non-linear aerodynamic characteristics as derived from static tests of a powered model of the vehicle in the Ames 40x80 ft. low-speed wind tunnel. $^{(2,3)}$ A downwash model, based on finite span jet flapped wing theory and correlated with data from Ames 40x80 ft. wind tunnel tests was used to determine the contribution of the horizontal tail. Rotary derivatives were estimated, using jet flap theory where appropriate. Supporting data for the downwash model and rotary derivatives are unpublished. The models themselves appear in Refs. 2 and 3.

# TEST PROGRAM

This vehicle simulation, with modifications to the longitudinal control system for stability and command augmentation, was used to evaluate the influence of certain vehicle characteristics and control system configurations on handling qualities during approach and landing. Specific consideration was given to longitudinal handling qualities with emphasis on:

- studying the use of several techniques for the control of flight path and airspeed for the basic vehicle

1. flight path control with attitude; speed control with thrust vector   
2. flight path control with thrust vector; speed control with attitude   
3. flight path control with thrust; speed control with attitude

- assessing stability and command augmentation schemes for pitch attitude and airspeed control

1. pitch attitude command and stabilization   
2. pitch rate command - pitch attitude hold with varying degrees of control sensitivity   
3. airspeed stabilization

- determining the influence of longitudinal and vertical force coupling for the power control (variations implemented by using different trim thrust vector inclination)   
- determining the influence of pitch axis coupling with the power and thrust vector control (variations implemented by using different thrust line offsets)   
- evaluating the contribution of the pitch rate command - attitude hold and airspeed stabilization modes to recovery from a single engine failure

In the approach and landing, the pilot assumed control of the aircraft, trimmed for descent and aligned with the glide slope and localizer of a 1500 ft. STOL runway. The approach was initiated at 1300 feet along a 7.5 degree glide slope at an airspeed of 60 knots. Flaps were set at 65 degrees, Pegasus nozzles at 87.7 degrees and power corresponding to 7160 pounds of hot thrust. The pilots generally introduced their own disturbances, offsets and abuses to the task for evaluation. IFR conditions, random gust disturbances, wind shears, and crosswinds were also included as test variables. Time histories were obtained for the approach, and were supplemented by pilot commentary. Pilot ratings, based on the Cooper-Harper scale (4), were obtained for selected configurations.

# DISCUSSION OF RESULTS

Longitudinal Handling Qualities Of The Basic Augmentor Wing Aircraft

To provide a better description of the handling qualities problems associated with flight path and airspeed control of a powered lift STOL aircraft, the response of the basic augmentor wing aircraft to elevator, thrust, and thrust vectoring is presented in the first few figures. Fig. 2 illustrates the response to a step column input by the pilot. Somewhat sluggish pitch response associated with the low short period frequency may be noted. Strong phugoid excitation in the form of airspeed and attitude excursions is observed which will require attention by the pilot for precise attitude control. Furthermore, with the low level of static stability and the nonlinear pitching moment characteristics associated with this trim condition, nose up and nose down pitch disturbances produce considerably different responses. Unstable flight path response to attitude associated with operation on the back side of the thrust required curve is also typical of this flight condition. Performance data of Fig. 3 provide a more graphic description of the relationships between flight path and airspeed. The trimmed approach condition ( $\gamma = -7.5\deg$ , $V = 60$ kts) is well on the backside of the $\gamma$ -V curve (d $\delta$ /dV = 0.2 deg/kt), hence attempts to make flight path corrections at constant power through changes in attitude (and speed) will produce a result opposite to that which was sought. Use of thrust to change flight path, without any

corresponding control in the pitch axis will produce an unaccustomed change in speed; that is, increasing thrust reduces descent rate and decreases airspeed, whereas speed would typically remain constant or increase with increased thrust for a conventional aircraft (at least in the absence of a large nose down trim change with thrust). Furthermore, speed and angle of attack do not bear the same relationship as for conventionally configured aircraft, i.e., $V_{\text{trim}} = \sqrt{\frac{2W/S}{\rho C_L(\alpha)}}$

since a significant portion of the lift required for steady flight is contributed by power, not angle of attack. Consequently, changes in engine power setting can either result in steady state flight path and speed changes at constant angle of attack or flight path and angle of attack changes at constant speed. It may also be observed in Fig. 3 that the changes in pitch attitude required to hold speed while simultaneously changing flight path are opposite to those attitude changes normally associated with flight path corrections for conventional aircraft.

Responses to step increases or decreases in thrust level with no compensating longitudinal control are shown in Fig. 4. The changes in speed anticipated from the performance data are evident. Some variation in angle of attack caused by the thrust trim change is also present. Landing approaches where thrust was used to control flight

path are presented in Figs. 5 and 6 for high and low glideslope offsets as set up by the pilot. Attitude was maintained essentially constant up to the point of flare. Speed and angle of attack excursions with thrust appear as expected.

Performance characteristics associated with flight path control with thrust vectoring are illustrated in Fig. 7. Because the thrust vector is oriented nearly perpendicular to the flight path for the trim condition, changes in vector angle about this condition have effects similar to those of thrust control for a conventional aircraft in that speed and angle of attack are directly related and a change in vector angle simply causes a change in flight path. If there is no trim angle of attack change with thrust vectoring, speed remains constant. Responses to fore and aft thrust vectoring are shown in Fig. 8. No longitudinal control was used to compensate for trim changes. The vector aft and forward responses are considerably different due to the non-linear static angle of attack stability associated with the trim condition. For forward thrust inclination a stable nose down pitch response and an increase in airspeed may be observed due to the trim change associated with Pegasus nozzle location below the c.g. Conversely, aft thrust inclination produces a nose up pitch response which drives the aircraft into the region of longitudinal static instability. In either case, the need for the pilot to control

attitude is apparent if flight path corrections at a specified speed are to be accomplished. A time history of a landing approach for which vector angle was used to control flight path at constant thrust is shown in Fig. 9. In this case, attitude control was used to maintain a reasonably constant approach speed.

Pilot commentary relating to attitude, flight path, and airspeed control are summarized as follows for the basic aircraft:

# Pitch attitude control

- poor static stability; attitude wanders during unattended operation   
- sluggish response; difficulty in making rapid and precise changes in attitude

# Flight path control

- unstable flight path-attitude relationship (backside operation)   
- sluggish short-term flight path response to attitude changes   
- inability to flare precisely to low sink rate through a change in attitude   
- flight path and speed response to attitude changes occur with nearly the same time constant   
- changes in angle of attack with thrust which require the pilot's attention to insure adequate angle of attack margin from stall

- flight path control with thrust vector angle changes similar to effect of thrust change on conventional aircraft   
- pitch coupling with thrust vectoring requires pitch control during flight path corrections   
- thrust vectoring not sufficient to flare; thrust difficult to modulate precisely during flare   
- reductions in power to steepen flight path undesirable during final stage of approach - high sink rate, low power, longer-time lag if increased thrust is subsequently required

# Airspeed control

- changes in speed and trim with power setting not related as for conventional aircraft   
- attitude changes required to hold speed while changing flight path are large and opposite those of conventional aircraft

# Preferred control techniques

- flight path corrections with thrust vector, speed control with attitude   
- constant vector angle through flare, with thrust increase to augment flare with attitude change

Pilot ratings given the basic airplane for the task of a straight-in, constant speed approach under VFR conditions are tabulated below.

<table><tr><td rowspan="2">Control Task</td><td colspan="3">Pilot Rating</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td>Pitch attitude control</td><td>3.5</td><td>4-4.5</td><td>3.5-4</td></tr><tr><td>Flight path control</td><td></td><td></td><td></td></tr><tr><td>- with thrust</td><td>5</td><td></td><td>3.5</td></tr><tr><td>- with thrust vectoring</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Approach in turbulence (overall rating)</td><td></td><td></td><td>3.5</td></tr><tr><td>σg = 3 ft/s</td><td></td><td></td><td></td></tr></table>

The ratings reflect the pilots' objection to the work load associated with attitude control and their preference for thrust vector control of flight path. While only one pilot rating was obtained for an approach in turbulence, this rating reflects the general consensus among pilots that the level of turbulence used during the simulation did not sufficiently disturb the aircraft longitudinally to add materially to the pilot's work load.

# Pitch Attitude Stabilization and Command Augmentation

To improve control of pitch attitude and to provide attitude stabilization for unattended operation, an attitude stabilization and command augmentation system was incorporated in the longitudinal control system. To mechanize the attitude stabilization and command features, a power actuator was used to drive the elevator through the existing mechanical controls, including the spring tab. A block diagram of the system is shown in Fig. 10. Elevator-spring tab dynamics are described by the elevator hinge moment equation

$$
\ddot {\delta} _ {e} = - \dot {\varphi} _ {B} + H \dot {\varphi} _ {e} * \dot {\delta} _ {e} - \omega_ {e} ^ {2} * \delta_ {e} + A _ {e} * \delta_ {e _ {c}}
$$

where

$$
\mathrm {H} _ {\delta_ {\mathrm {e}}} = - 3 3 2 \bar {\mathrm {q}}
$$

$$
\overline {{q}} = 1 / 2 p v ^ {2}
$$

$$
\omega_ {e} ^ {2} = 2. 0 4 \bar {q} + A _ {e}
$$

$$
A _ {e} = \frac {1 3 . 3 5 + 1 7 . 4 4 \bar {q}}{1 + . 1 0 8 \bar {q}}
$$

The elevator and SAS actuators are represented by second order transfer functions where

$$
\frac {\delta_ {e _ {C}}}{\delta_ {e _ {A}}} = \frac {\omega_ {A} ^ {2}}{s ^ {2} + 2 5 \omega_ {A} s + \omega_ {A} ^ {2}}
$$

$$
\omega_ {A} = \omega_ {S} = 2 0 \mathrm {r a d / s}
$$

$$
\frac {\delta e _ {S A S}}{\delta e _ {S C}} = \frac {\omega_ {s} ^ {2}}{s ^ {2} + 2 5 \omega_ {s} s + \omega_ {s} ^ {2}}
$$

$$
\hat {S} _ {A} = \hat {S} _ {S} = . 6
$$

The system can be tailored to provide pitch rate command proportional to either column position or force with pitch attitude hold when the column is neutralized or the force relaxed. Besides permitting improvement in precision of attitude control, this system reduces the pilot's workload somewhat by trimming the airplane at the desired attitude. If the gain $K$ of the control input integrator is set to zero, the system reverts to an attitude command control in proportion to column input. By suitably adjusting the control input gains, control sensitivity can be tailored to the pilot's preference.

A comparison of the pitch control characteristics of the basic aircraft with a typical pitch rate command system is given in the following table.

TABLE 1. Comparison of Pitch Control Characteristics   

<table><tr><td colspan="2">Basic Aircraft</td><td>Typical Pitch Rate Command</td></tr><tr><td colspan="2">l/Tsp1= .62 rad/sec</td><td>l/T&#x27;sp1= .93 rad/sec</td></tr><tr><td colspan="2">l/Tsp2= 1.2 rad/sec</td><td>l/T&#x27;sp2= 2.99 rad/sec</td></tr></table>

$$
\omega_ {p} = . 2 2 \text {r a d / s e c} \quad \omega_ {p} = . 2 7 \text {r a d / s e c}
$$

$$
\mathbf {S} _ {\mathrm {p}} = . 1 5 \quad \mathbf {S} _ {\mathrm {p}} ^ {\prime} = . 9 4
$$

$$
1 / \mathbf {T} _ {\boldsymbol {\theta} _ {I}} = . 1 8 \text {r a d / s e c}
$$

$$
1 / \mathrm {T} _ {\mathbf {e} _ {2}} = . 3 7 \text {r a d / s e c}
$$

$$
0 / \delta_ {e} = . 0 4 2 5 r a n / s e c ^ {2} / i n
$$

$$
F _ {S} / n _ {z} = 5 7. 2 l u / g
$$

$$
\ddot {\theta} / \delta_ {c} = . 0 6 4 \mathrm {r a d} / \sec^ {2} / \mathrm {i n}
$$

$$
F _ {S} / n _ {Z} = 7 5 \mathrm {l b} / \mathrm {g}
$$

$$
K _ {\theta} = \sqrt {2} \cdot \deg / \deg
$$

$$
K _ {\bullet} = 2 \quad \text {d e g / d e g / s e c}
$$

$$
K _ {s} = . 5 \mathrm {d e g} / \mathrm {d e g}
$$

$$
K _ {3} = \perp . 5 \mathrm {d e g} / \sec / \mathrm {d e g}
$$

Response to a step column input is presented in Figs. 11 and 12 for the pitch rate command-attitude hold system the pilots found to be most acceptable. This particular configuration has the characteristics shown in Table 1. It provides the pilot with a steady pitch rate response for a column input and good attitude stabilization when the column is centered or when no force is applied. No attitude overshoot of any consequence exists and control sensitivity is favorably increased. Attitude stabilization against trim changes induced by thrust vectoring is apparent in Fig. 13, thereby reducing the pilot's workload when using this control for flight path corrections. In Figs. 14 and 15, the system was used in conjunction with flight path control with thrust. In Fig. 14, flight path corrections were made holding attitude constant, while in Fig.15, path corrections were made while attitude was changed to hold constant speed. In either case, the precise control of attitude required for the particular control technique is advantageous.

In the process of tailoring the rate command - attitude hold system to the various pilot's preferences, various degrees of stiffness for attitude stabilization and various control sensitivities were evaluated. The system configurations encompassed ranges shown in Table 2.

TABLE 2 - Pitch Attitude Stabilization and Command Augmentation Characteristics   

<table><tr><td>Kθ</td><td>Kθ</td><td>Kθ/Kθ</td><td>Kθ</td><td>Kθ</td><td>Kθ/1+Kθ</td></tr><tr><td>deg/deg</td><td>deg/deg/sec</td><td>sec.</td><td>deg/deg</td><td>deg/sec/deg</td><td>1/sec</td></tr><tr><td>1.0 to 3.0</td><td>1.0 to 3.0</td><td>.5 to 1.0</td><td>.0 to 1.0</td><td>1.0 to 2.0</td><td>1.0</td></tr></table>

While pilot ratings were not given for every one of the combinations shown in Table 2, commentary of the four pilots participating in the program showed a definite preference for the system characteristics described in Table 1. The preference was based on control sensitivity and initial response and attitude stabilization stiffness. Ratings given for the VFR approach for the preferred attitude control system were PR 2.0 to 3.0 for operation either in smooth air or in turbulence (gust = 3 ft/s).

# Airspeed Command and Stabilization

In light of the stringent airspeed control requirements which typify STOL operations, it was also of interest to explore the influence of airspeed stabilization on speed and flight path control and its ability to reduce pilot workload during the approach and flare. With these objectives, the speed stabilization system shown in Fig. 16 was incorporated in the simulation.

The system functioned through feedback of airspeed, longitudinal acceleration and pitch attitude to the Pegasus nozzles. Because of the nozzle location below the aircraft's center of gravity attitude stabilization was activated when the speed stabilization mode was operating in order to stabilize the otherwise divergent pitch response of the speed stabilization system.

TABLE 3. Longitudinal Control Characteristics Comparison - Effects of Speed Stabilization   

<table><tr><td colspan="2">Basic Aircraft</td><td colspan="2">Speed Stabilization</td></tr><tr><td colspan="2">l/Tsp1= .62 rad/sec</td><td colspan="2">l/T&#x27;&#x27;sp1= 1.10 rad/sec</td></tr><tr><td colspan="2">l/Tsp2= 1.2 rad/sec</td><td colspan="2">l/T&#x27;&#x27;sp2= 2.94 rad/sec</td></tr><tr><td colspan="2">ωp= .22 rad/sec</td><td colspan="2">l/T&#x27;p1= .39 rad/sec</td></tr><tr><td colspan="2">sp= .15</td><td colspan="2">l/T&#x27;p2= .81 rad/sec</td></tr><tr><td colspan="2">l/Th1= .06 rad/sec</td><td colspan="2">l/T&#x27;h1= .76 rad/sec</td></tr><tr><td colspan="2">l/Th1= .18 rad/sec</td><td colspan="2">ωθ= .68 rad/sec</td></tr><tr><td colspan="2"></td><td colspan="2">Sθ&#x27; = .99</td></tr><tr><td colspan="2"></td><td colspan="2">Ku= 9 deg/ft/sec</td></tr><tr><td colspan="2"></td><td colspan="2">Ku= 0</td></tr><tr><td colspan="2"></td><td colspan="2">Kθ= 0</td></tr><tr><td colspan="2">γ/θ= -.43 deg/deg</td><td colspan="2">γ/θ= .8 deg/deg</td></tr><tr><td colspan="2">γ/V= .18 deg/kt</td><td colspan="2">δ/V= -2.1 deg/kt</td></tr><tr><td colspan="2">V/θ= 2.5 kt/deg</td><td colspan="2">V/θ= -.38 kt/deg</td></tr></table>

The speed control system functions to stabilize flight path response to changes in attitude as well as to reduce speed excursion associated with path and attitude changes. Short term flight path response to attitude changes is also more rapid when speed is stabilized. These characteristics are apparent in Fig. 17 and 18. Flight path corrections were made with the longitudinal control in Fig. 17, while in Fig. 18, path corrections were made with thrust. Note that the adverse speed changes with thrust associated with the basic aircraft are no longer present. However, the changes in flight path made at constant attitude still involve significant changes in angle of attack, and hence the concerns regarding operating margin from the stall associated with power management for the basic aircraft continue to exist.

A typical landing approach time history with the attitude and speed stabilization systems operating is shown in Fig. 19. For this approach, the longitudinal control was used exclusively for flight path control and flare.

Pilot ratings given for the preferred attitude and speed control configurations on the VFR approach were PR 2.0 in smooth air and 2.5 to 3.5 in 3 ft/s rms turbulence. The applicable control technique for these ratings was path control with attitude.

# Longitudinal-Vertical Force-Pitching Moment Coupling

# Effects of coupling on thrust control

A number of configurations were evaluated which possessed various degrees of coupling between the longitudinal and vertical forces and pitching moment associated with thrust control. Since the dominant influence of thrust, so far as powered lift is concerned, is in vertical force, the test configurations are defined in terms of the incremental amounts of longitudinal force and pitching moment produced for an increment in vertical force. These configurations are listed in Table 4 and are displayed in Fig. 20 along with the characteristics associated with various ranges of configurations. Variations in the ratio of longitudinal to vertical force produced by a given change in thrust were obtained by inclining the thrust vector for the trim flight condition. The ratio of pitching moment to vertical force was altered by changing the longitudinal thrust line offset.

Thrust vector inclination - Some effective forward inclination of the thrust vector $(X_{\delta_r} / Z_{\delta_r}$ negative) was found to be desirable for use of thrust to control flight path. This favorable coupling served to reduce the speed excursions to which the pilot objected for the basic aircraft. Fig. 2l shows the response to a step thrust increase for thrust inclination $X_{\delta_r} / Z_{\delta_r} = -.064$ ( $\delta_v = 76.4$ deg).

TABLE 4 - Thrust Control Coupling Configurations   

<table><tr><td rowspan="2">Config.</td><td>δv</td><td>δT</td><td>δf</td><td>xv/ε</td><td>πv/ε</td><td>xδT/εδT</td><td>MδT/εδT</td><td>zδT</td></tr><tr><td>deg.</td><td>1bs.</td><td>deg.</td><td></td><td></td><td></td><td>rad/ft.</td><td>ft/sec2/1b</td></tr><tr><td>Basic Aircraft</td><td>87.7</td><td>7160</td><td>65.</td><td>-.024</td><td>.23</td><td>.0164</td><td>.0008</td><td>-.0018</td></tr><tr><td>⊥</td><td>90.</td><td>7520</td><td></td><td>0.</td><td>0.</td><td>.0333</td><td>.00096</td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td>.08</td><td></td><td></td><td>.00143</td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td>-.08</td><td></td><td></td><td>.00335</td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td>-.16</td><td></td><td></td><td>.00572</td><td></td></tr><tr><td>5</td><td></td><td></td><td></td><td>-.24</td><td></td><td></td><td>.0081</td><td></td></tr><tr><td>6</td><td>76.4</td><td>6440</td><td>75</td><td>-.16</td><td></td><td>-.064</td><td>.00558</td><td></td></tr><tr><td>7</td><td></td><td></td><td></td><td>-.08</td><td></td><td></td><td>.00333</td><td></td></tr><tr><td>8</td><td></td><td></td><td></td><td>0</td><td></td><td></td><td>.00105</td><td></td></tr><tr><td>9</td><td>60.</td><td>5190</td><td></td><td>.08</td><td></td><td></td><td>-.0012</td><td></td></tr><tr><td>10</td><td></td><td></td><td></td><td>-.024</td><td>.23</td><td>-.15</td><td>-.0023</td><td>-.002</td></tr></table>

When compared to the basic aircraft response to a similar input in Fig. 4 the reduced speed excursion is apparent. A side effect of the forward vector inclination which adversely influenced path control was the reduced thrust level required to stabilize the aircraft on the -7.5 deg. 60 kt flight path. Particularly for the configuration with $\delta_{\nu} = 60$ deg. $(X_{\delta_{T}} / Z_{\delta_{T}} = -.15)$ the increase in thrust response time lags associated with the low thrust setting made precise flight path corrections more difficult. In addition, not enough incremental thrust was available to satisfactorily correct for offsets above glide slope. Furthermore, at the lower power settings, this bileron blowing coefficients were reduced sufficiently to seriously degrade lateral control.

In conclusion, considering the favorable and adverse characteristics of thrust inclination, its net effect on flight path control with thrust was negligible. It may be noted, however, that if longitudinal-vertical force coupling were accomplished by interconnecting the thrust and thrust vector controls, the undesirable consequences of thrust inclination could be avoided and a more favorable tailoring of the thrust control for flight path could be achieved.

Thrust line offset - Coupling of thrust and pitching moment can be expected to affect the speed response associated with flight path corrections due to the changes in trim contributed by the path control. A range of pitch coupling configurations were explored for two levels of thrust vector inclination (Table 4 and Fig. 20). In general, forward offset of the thrust line from the c.g. tended to exaggerate speed excursions accompanying changes in thrust. Some aft thrust line effect was found to improve speed control. Too much offset forced the pilot to control excessive attitude excursions and thereby again increased the pilot's control workload. Figs. 22 to 24 present responses to thrust inputs for a range of configurations tested at $\delta_{\nu} = 90$ deg. ( $x_{\delta_{\tau}} / z_{\delta_{\tau}} = .033$ ). Fig. 22 corresponds closely to the basic aircraft. Fig. 23 represents the extreme forward offset condition, and Fig. 24 represents a large aft offset condition. No longitudinal control was applied by the pilot in any of these cases. Fig. 25 and 26 show landing approach time histories for the forward and aft offset configurations respectively. Thrust was used to control flight path in both instances while attitude was used for speed control as the situation required. Smaller speed excursions and less longitudinal control activity are apparent in the aft offset configuration of Fig. 26 as compared to the forward offset configuration of Fig. 25.

Figure 27 shows an approach for a forward offset configuration in combination with forward tilt of the thrust vector. In comparison of Fig. 21, speed and attitude excursions are again observed to be greater for the forward thrust line offset condition.

Effects of coupling on thrust vector control

The dominant effect of thrust vectoring appears as a change in longitudinal force, hence the test configurations in this sequence are defined in terms of the incremental vertical force and pitching moment produced for an increment in longitudinal force. These configurations are listed in Table 5 and are displayed in Fig. 28 along with comments descriptive of the characteristics of the various ranges of configuration.

Thrust vector inclination - Inclination of the thrust vector over a range corresponding to trim Pegasus nozzle deflections from $\pmb{\nu} = 60$ to 90 deg. had no apparent effect on control coupling so far as the pilots were concerned. For nozzle deflections of $\pm 20$ deg. the increment in vertical acceleration was low enough to have an insignificant influence on flight path or speed ( $\Delta n_{\mathrm{g}} = .028$ g's for $\Delta \nu = -20$ deg at the $\pmb{\nu} = 60$ deg. condition). However, the reduced level of thrust at the more forward vector inclinations made the vector control less effective and hence not as useful to the pilot as a path controller.

TABLE 5. Thrust Vector Control Coupling Configurations   

<table><tr><td>Config.</td><td>δv</td><td>δT</td><td>δf</td><td>xv/c</td><td>γv/c</td><td>Zδv/Xδv</td><td>Mδv/Xδv</td><td>Xδv</td></tr><tr><td></td><td>deg</td><td>1bs</td><td>deg</td><td></td><td></td><td></td><td>deg/ft</td><td>ft/sec2/deg</td></tr><tr><td>Basic Aircraft</td><td>87.7</td><td>7160.</td><td>65.</td><td>-.024</td><td>.23</td><td>.0424</td><td>.0153</td><td>-.094</td></tr><tr><td>11</td><td>90.</td><td>7520.</td><td rowspan="3">75.</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>-.101</td></tr><tr><td>12</td><td>↓</td><td>6440.</td><td>↓</td><td>.24</td><td>.24</td><td>.016</td><td>↓</td></tr><tr><td>13</td><td>↑</td><td rowspan="4">5190.</td><td>↓</td><td>.48</td><td>.48</td><td>.032</td><td>↓</td></tr><tr><td>14</td><td>76.4</td><td>75.</td><td>↓</td><td>.00</td><td>.257</td><td>0.0</td><td>-.083</td></tr><tr><td>15</td><td>↓</td><td>↓</td><td>-.024</td><td>.23</td><td>.23</td><td>.0157</td><td>↓</td></tr><tr><td>16</td><td>60.</td><td>↓</td><td>-.024</td><td>.23</td><td>.615</td><td>.0167</td><td>-.059</td></tr></table>

Thrust line offset - Again, due to the changes in speed accompanying trim changes associated with pitch coupling, the vertical offset of the Pegasus nozzles from the c.g. influenced the pilot's ability to use thrust vectoring as a path control. The series of configurations only encompassed nozzle locations below the c.g. $(\mathbf{M}_{\delta \nu} / \mathbf{X}_{\delta \nu}$ positive as indicated in Fig. 28). The pilots found some positive pitch coupling to be desirable in that the aircraft's attitude led in the direction of the intended path correction. Although some longitudinal control was required to counter the trim change in order to hold speed, the control force levels were innocuous to the pilots for the level of pitch coupling associated with the basic aircraft $(\mathbf{F}_{\mathrm{s}} / \delta \nu = .21\mathrm{lb / deg})$ . At the highest level of pitch coupling tested $(\mathbf{M}_{\delta \nu} / \mathbf{X}_{\delta \nu} = .032)$ the longitudinal control necessary to trim became objectionable. In Fig. 29, an example of response to a step change in thrust vector for an uncoupled control configuration is shown. Essentially no change in speed with the change in flight path is apparent. By contrast, an approach for the configuration having the greatest pitch coupling is shown in Fig. 30. In this case, some longitudinal control was required to maintain the desired approach speed. Sustained column forces did not exceed 5 lbs during the approach prior to flare.

# Recovery from Engine Failure

Considerable evaluation of the behavior of the basic aircraft following a single engine failure and development of suitable control techniques for recovery has been accomplished during previous simulator investigations at Ames. Results of these tests are anticipated to be published shortly. It was of interest during the current phase of testing to determine the effects, favorable and unfavorable, of the selected attitude and speed stabilization systems on engine out recovery.

In summary, the basic aircraft's initial response to the loss of one engine consists of:

- an immediate increase in sink rate   
- an increase in airspeed   
- some roll and very little yaw prior to configuration change

If the landing is to be continued, the pilot increases thrust on the remaining engine and vectors the nozzle aft to re-establish the glide slope. Speed is maintained at or slightly above 60 knots. Lateral and directional controls are used to counter rolling and yawing moments due to nozzle deflection and due to increased thrust on the remaining engine. Acceptable landings can be made if sufficient altitude is available to arrest the increased sink rate. A typical single out landing is shown in Fig. 31. Engine out waveoffs are performed by increasing thrust, vectoring the nozzle full aft,

and raising the flaps to 30 deg. Speed is allowed to increase to 75-80 kts for best climb performance. Typical altitude losses during recovery are 100-150 ft. in excess of those experienced during a normal two engine waveoff. A time history of an engine-out landing with the attitude and speed stabilization systems engaged is shown in Fig. 32. Whatever improvement exists over the basic aircraft lies in part with the precise attitude control and the ability of the pilot to have the airplane in more precise control on the approach prior to the engine failure. Speed stabilization has the unfavorable characteristic upon failure of an engine of rotating the nozzles forward (vectoring the remaining hot thrust aft) to counter the increase in airspeed which follows the loss of powered lift. Sink rate increases even more as a result of the nozzle response until the pilot can counter with increased thrust. If the landing is to be continued, the speed hold at 60 kts can ultimately aid the pilot as soon as sufficient thrust is applied to regain the glide slope. If a wave off is to be made, the pilot must have either the capability to override the nozzle command from the speed control system or the ability to quickly and precisely select the desired climb speed of 75-80 kts. Given this capability, the speed hold system can assist the pilot in establishing his climb condition and thereby relieve some of his work load.

# CONCLUSIONS

Considering the difficulty in obtaining satisfactory control of pitch attitude, flight path, and airspeed typical of powered lift STOL aircraft, this simulator investigation has provided an indication of improvements which can be made in the aircraft's attitude, thrust, and thrust vector controls to make the aircraft more acceptable to the pilot for the STOL approach and landing. The results relate to:

- stability and command augmentation for attitude and airspeed control   
- longitudinal and vertical force and pitching moment coupling associated with the thrust and thrust vector controls   
- impact of stability and command augmentation on recovery from a single engine failure

Specific conclusions regarding each of these categories are:

Attitude Stabilization and Command Augmentation

- improves precision and speed of response for attitude changes   
- improves control sensitivity   
- stabilizes against trim changes and external disturbances   
- pitch rate command preferred over attitude command to relieve pilot's trimming workload

Airspeed Stabilization

- stabilizes flight path response to attitude changes   
- provides more rapid flight path response to attitude changes   
- reduces speed excursions associated with path and attitude changes   
- reduces speed changes with thrust

# Thrust Control Coupling

- forward thrust vector inclination (negative $x_{\delta \tau} / z_{\delta \tau}$ ) preferred in order to reduce speed changes when controlling flight path with thrust   
- adverse effects of forward vector inclination associated with lower trim thrust can be avoided by interconnecting thrust and thrust vectoring controls to achieve desired coupling   
- thrust line aft of c.g. preferred in order to provide pitch coupling (positive $M_{\mathrm{sr}} / Z_{\mathrm{sr}}$ ) to reduce speed excursions when controlling path with thrust

# Thrust Vector Control Coupling

- thrust vector inclination with respect to the vertical of 30 degrees has only minor influence on flight path control with thrust vectoring (reduced thrust reduces effectiveness of vectoring for flight corrections)   
- some nozzle offset below the c.g. (positive $M_{\delta_2} / X_{\delta_2}$ ) preferred for vector control of path

# Engine Out Recovery - Stability and Command Augmentation On

- attitude and speed stabilization effective in permitting precise control of attitude and speed prior to engine failure and helpful in recovery to a satisfactory flight condition following the initial transients.   
- response of speed control to transients following engine failure adversely affect flight path control by increasing rate of descent   
- pilot must be provided with the capability to override nozzle commands from the speed stabilization system and the ability to select a new commanded airspeed quickly and precisely

# REFERENCES

1. Quigley, H. C., Sinclair, Nark, and O'Keefe, A Progress Report on the Development of an Augmentor Wing Jet STOL Research Aircraft, SAE Paper 710757, National Aeronautics and Space Engineering and Manufacturing Meeting, Los Angeles, Calif. Sept. 28-30, 1971   
2. Rumsey, P. C. and Spitzer, R. E., Simulator Model Specification for the Augmentor Wing Jet STOL Research Aircraft, NASA CR-114434, December 1971   
3. Cleveland, William B., Augmentor Wing Jet STOL Research Aircraft Digital Simulation, NASA TM X-62,149, March 1972.   
4. Cooper, G. E. and Harper, R. P., The Use of Pilot Rating in the Evaluation of Aircraft Handling Qualities, NASA TN D-5153, April 1969

图片摘要：该图主要展示 la Augmentor Wing Jet STOL Research Aircraft。
![](images/086b890441eebe6e9f1183292f3767fea883c03967a5705abe44216199226e3c.jpg)

图片摘要：该图主要展示 la Augmentor Wing Jet STOL Research Aircraft。
![](images/e3c7564c67dbbd785b5d043b801f958b370b58dc46899fd097379d3719dd2e88.jpg)  
Fig. la Augmentor Wing Jet STOL Research Aircraft

图片摘要：该图主要展示 la Augmentor Wing Jet STOL Research Aircraft。
![](images/1988c567b58cfa1faa3c1ddaa0e7d2c2883d08cbca71aff450db0c0b1cb016b0.jpg)  
Fig.1b Rolls Royce Spey 801 SF Engine and Pegasus Nozzle Arrangement

图片摘要：该图主要展示 1b Rolls Royce Spey 801 SF Engine and Pegasus Nozzle Arrange。
![](images/5f3784558b506ef04423b0c94677ee1d5de7c78929fa97129a14260ed226c5c5.jpg)  
Fig.1c Augmentor Flap

# Weights

Maximum Gross 45,000 lbs.

Maximum Landing 43,000 lbs.

Operational Empty 32,600 lbs.

Inertias (Maximum Gross Weight)

$\mathbf{l}_{\mathbf{x}}$ 380,000 slug ft²

$\mathbf{l}_{\mathbf{y}}$ 207,160 slug ft²

$\mathbf{I}_{\mathbf{Z}}$ 552,610 slug ft²

Center of Gravity Limits (Horizontal tail incidence of $0^{\circ}$ , 40,000 lbs.)

Forward 24.0% MAC

Rear 33.0% MAC

# Areas

Wing area, total including ailerons flaps and 111 square feet 865 square feet of fuselage

Wing flap area, projected, including ailerons aft of wing line 187.10 square feet

Total aileron area aft of hinge line, including trim tab 46.30 square feet

Horizontal tail area, total 233 square feet

Elevator aft of hinge line 81.5 square feet

Vertical tail area, total 152 square feet

Rudder aft of hinge line:

Fore 30 square feet

Trailing 30 square feet

# Dimensions and General Data

Wings:

Span 78.75 feet

Root Chord 12.58 feet

Tip Chord 7.74 feet

Mean aerodynamic chord 12.1 feet

Aerofoil section

Root NACA 643A417.5 (MOD)

Tip NACA 632A615 (MOD)

Sweep back at 40 percent chord zero degrees

Dihedral, outer wing only 5.0 degrees

(Note: Leading edge sweep back and dihedral each

start 17.6 feet from plane of symmetry.)

Aspect ratio 7.2

Fig. 1d. Aircraft Characteristics

Control Surface Deflections and Rates   

<table><tr><td colspan="3">Ailerons:</td></tr><tr><td>Span</td><td></td><td>11.50 feet</td></tr><tr><td>Chord aft of hinge line</td><td></td><td>2.01 feet</td></tr><tr><td>Distance from plane of symmetry to centroid of aileron</td><td></td><td>33.70 feet</td></tr><tr><td>Aerodynamic balance</td><td></td><td>20.0 percent</td></tr><tr><td colspan="3">Spoilers:</td></tr><tr><td>Span</td><td></td><td>11.30 feet</td></tr><tr><td>Chord</td><td></td><td>1.18 feet</td></tr><tr><td>Position of hinge line percent wing chord (average)</td><td></td><td>62.4 percent</td></tr><tr><td colspan="3">Flaps:</td></tr><tr><td>Span</td><td></td><td>55.70 feet</td></tr><tr><td>Chord aft of hinge line</td><td></td><td>3.2 feet</td></tr><tr><td colspan="3">Horizontal tail:</td></tr><tr><td>Span</td><td></td><td>32.0 feet</td></tr><tr><td>Root chord</td><td></td><td>8.33 feet</td></tr><tr><td>Mean Aerodynamic Chord</td><td></td><td>6.25 feet</td></tr><tr><td colspan="3">Aerofoil Section:</td></tr><tr><td>Root</td><td>NACA</td><td>63 A 214 (MOD) (inverted)</td></tr><tr><td>Tip</td><td>NACA</td><td>63-212 (MOD) (inverted)</td></tr><tr><td>Sweep of leading edge</td><td></td><td>4.8 degrees</td></tr><tr><td>Dihedral</td><td></td><td>zero degrees</td></tr><tr><td>Aspect ratio</td><td></td><td>4.4</td></tr><tr><td colspan="3">Vertical tail:</td></tr><tr><td>Span</td><td></td><td>13.60 feet</td></tr><tr><td>Root chord</td><td></td><td>14.00 feet</td></tr><tr><td>Tip chord</td><td></td><td>8.33 feet</td></tr><tr><td>Mean aerodynamic chord</td><td></td><td>11.41 feet</td></tr><tr><td>Airfoil section</td><td>NACA</td><td>63 (215)014 (MOD)</td></tr><tr><td>Sweep of leading edge</td><td></td><td>22.6 degrees</td></tr><tr><td>Aspect ratio</td><td></td><td>1.2</td></tr><tr><td>Overall height</td><td></td><td>28.7 feet</td></tr><tr><td>Overall length (with probe of 16 feet)</td><td></td><td>93.32 feet</td></tr><tr><td>Distance, wing MAC, 1/4C, to horizontal tail MAC, 1/4C</td><td></td><td>46.3 feet</td></tr><tr><td>Distance, wing MAC, 1/4C, to vertical tail MAC, 1/4C</td><td></td><td>43.4 feet</td></tr><tr><td>Wing incidence angle</td><td></td><td>+2.5 degrees</td></tr><tr><td>Horizontal tail incidence angle (adjustable)</td><td></td><td>+1.0 degrees</td></tr></table>

<table><tr><td>Flaps</td><td>6 5° down to 75° down
4°/sec extension and retraction</td></tr><tr><td>Pegasus nozzles</td><td>18.5° to 116.0° (down from aft of aircraft)
90°/sec</td></tr><tr><td>Ailerons</td><td>±17° about +30° max droop angle
30°/sec</td></tr><tr><td>Spoilers</td><td>-50°
100°/sec</td></tr><tr><td>Augmentor Choke</td><td>65% choke gap area closure at 75° flap
deflection
30°/sec</td></tr><tr><td>Rudder</td><td>±25° forward segment
±25° trailing segment
-50°/sec</td></tr><tr><td>Elevator</td><td>+25°
-15°</td></tr></table>

图片摘要：该图主要展示 2. Longitudinal Response to a。
![](images/b1863d7d9ae2755847edeedae06fe983569bee6ca8bdae90eea3b9c185fee789.jpg)  
Figure 2. Longitudinal Response to a   
Step Column Input - Basic   
Augmentor Wing Aircraft

图片摘要：该图主要展示 2. Longitudinal Response to a。
![](images/c477f80103a79b06bd0345168038f15b1a932b08a642bbb8886eba734c366b99.jpg)  
Figure 3. Augmentor Wing Aircraft Landing Approach Performance - Thrust Control

图片摘要：该图主要展示 3. Augmentor Wing Aircraft Landing Approach Performance Thru。
![](images/591223067d4b59a12cd434cbab1f3c06d19bbe99ceb8a7227843998f22479dcf.jpg)  
Figure 4. Longitudinal Response to a Step Thrust Change - Basic Augmentor Wing Aircraft

图片摘要：该图主要展示 4. Longitudinal Response to a Step Thrust Change Basic Augme。
![](images/3b375888f215637ed2d5983bc4961ff254ded29ca41834b8ee372b59792fa0a3.jpg)  
Figure 5. Landing Approach Time History for Flight Path Control with Thrust - Basic Augmentor Wing Aircraft

图片摘要：该图主要展示 5. Landing Approach Time History for Flight Path Control wit。
![](images/68ccdef36e066707bffc9ad420092482a26558a15cb3ffd3b03ba51e69838ffc.jpg)  
Figure 6. Landing Approach Time History for Flight Path Control with Thrust - Basic Augmentor Wing Aircraft

# Trim Condition

$= {40},{000} \times  {10}^{7}$   
${V}_{0} = {60}\mathrm{{kts}}\;{\delta }_{\mathrm{f}} = {1160}\mathrm{{lbs}}$   
[{r}_{0} =  - {7.5}{\mathrm{\;{dec}}}_{4}\;{8}_{4} = {65}\;\mathrm{{deg}}]

图片摘要：该图主要展示 6. Landing Approach Time History for Flight Path Control wit。
![](images/a0913bcf8b54d4c84efecb3f34fbd9b2ffc4efb24f2f282012105dfd7e2c0c63.jpg)  
Figure 7. Augmentor Wing Landing Approach Performance - Thrust Vector Control

图片摘要：该图主要展示 7. Augmentor Wing Landing Approach Performance Thrust Vector。
![](images/437f69c5505f6ee667f3898c3080dd56c9aa4190ac977f68c8236c6ba958e989.jpg)  
Figure 8. Longitudinal Response to a Step Thrust Vector Change - Basic Augmentor Wing Aircraft

图片摘要：该图主要展示 8. Longitudinal Response to a Step Thrust Vector Change Basi。
![](images/5f3452724ec81465d05ec6d238f59eceff08831b42019413aac0eaedea701344.jpg)  
Figure 9. Landing Approach Time History for Flight Path Control with Thrust Vector - Basic Augmentor Wing Aircraft

图片摘要：该图主要展示 9. Landing Approach Time History for Flight Path Control wit。
![](images/ba60f0571263217601d2778ab88bb8123f8cd18ff42efdd7daa34f0e7ff73597.jpg)  
Figure 10. Block Diagram of Pitch Attitude Stabilization and Command System

图片摘要：该图主要展示 10. Block Diagram of Pitch Attitude Stabilization and Comman。
![](images/cde5bf51b334c35ebe972bd0438843441bc6df586402ac9a247b07fcec4077ca.jpg)  
Figure 11. Longitudinal Response to a Step Column Input - Pitch Rate Command/Attitude Hold System

Trim Condition   

<table><tr><td>GH</td><td>40,000 lbs.</td><td>δv= 87.7 deg</td></tr><tr><td>Vo</td><td>60 kts</td><td>δr= 7100 lbs</td></tr><tr><td>r0</td><td>-7.5 deg</td><td>δf= 65 deg</td></tr></table>

Attitude Stabilization   

<table><tr><td>Kθ=2.0 deg/deg K8=50 dcr/dec</td></tr><tr><td>Kθ=2.0 deg/dec K8=1.5 dcr/dec</td></tr></table>

图片摘要：该图主要展示 12. Attitude Changes by Pilot Using Pitch Rate Command/Attit。
![](images/f0c1ba3cf2b805aebe0699849fd343c282c0a453f65bce7667fb9b9433970c47.jpg)  
Figure 12. Attitude Changes by Pilot Using Pitch Rate Command/Attitude Hold System

Trim Condition

$$
\begin{array}{l} G W = 4 0, 0 0 0 \mathrm {l b s}. \quad \delta_ {V} = 8 7. 7 \mathrm {d e g} \\ V _ {0} = 6 0 k \mathrm {t s} \quad \delta_ {T} = 7 1 6 0 1 3 \\ r _ {0} = - 7. 5 \mathrm {d e g} S _ {f} = 6 5 \mathrm {d e g} \\ \end{array}
$$

Attitude Stabilization

$$
\begin{array}{l} \mathrm {K} _ {\theta} = 2. 0 \frac {\mathrm {d e g}}{\mathrm {d e g}} \quad \mathrm {K} _ {\delta} = - 3 0 \frac {\mathrm {d e g}}{\mathrm {d e g}} \\ \mathrm {K} _ {\dot {\theta}} = 2. 0 \frac {\mathrm {d e g}}{\mathrm {d e g / s e c}} \quad \mathrm {K} _ {\dot {\delta}} = 1. 5 \frac {\mathrm {d e g / s e c}}{\mathrm {d e g}} \end{array}
$$

图片摘要：该图主要展示 13. Longitudinal Response to a Step Thrust Vector Change Pit。
![](images/1b575b2706112992259977c9dcf4c773c81c6d15a469d4cadc94ae3278a03e2f.jpg)  
Figure 13. Longitudinal Response to a Step Thrust Vector Change - Pitch Rate Command/Attitude Hold System

图片摘要：该图主要展示 13. Longitudinal Response to a Step Thrust Vector Change Pit。
![](images/de34888fa41da8bd9ad651763ed70d68d8a3160fcd6db56c089e6f3d6406d70b.jpg)  
Figure 14. Flight Path Control with Thrust Pitch Rate Command/Attitude Hold System

图片摘要：该图主要展示 14. Flight Path Control with Thrust Pitch Rate Command/Attit。
![](images/7c3a87e0a149e63bd25d271488205946ff95c8b81f0731810c01ff01923d8473.jpg)  
Figure 15. Flight Path Control with Thrust, Airspeed Control with Attitude - Pitch Rate Command/Attitude Hold System

图片摘要：该图主要展示 15. Flight Path Control with Thrust, Airspeed Control with A。
![](images/2abb76d0aebe5612fc7473b410aaff1f4874f39ef037a447fbe26548a7d2fa77.jpg)  
Figure 16. Block Diagram of Airspeed Stabilization System

图片摘要：该图主要展示 16. Block Diagram of Airspeed Stabilization System。
![](images/0e9fd0f772f929e3bf710a3c755b254bba8e77275425c1cad6ff0431edf4780c.jpg)  
Figure 17. Longitudinal Response to a Step Column Input - Pitch Rate Command and Airspeed Stabilization Systems

图片摘要：该图主要展示 17. Longitudinal Response to a Step Column Input Pitch Rate 。
![](images/8305e0b658b6daffefa57ca0f758997bec0d2cf9167169c552d2435c22f81f86.jpg)  
Figure 18. Longitudinal Response to a Step   
Thrust Change - Pitch Rate   
Command and Airspeed   
Stabilization Systems

图片摘要：该图主要展示 18. Longitudinal Response to a Step。
![](images/285e676aee9e6a46ccedc87ea5128efadfbf38d1a6ee439ed22023b32b67599b.jpg)  
Figure 19. Landing Approach Time History - Pitch Rate Command and Airspeed Stabilization Systems

图片摘要：该图主要展示 19. Landing Approach Time History Pitch Rate Command and Air。
![](images/9ccbce6058438434a5a2856d49bf66445c7bbc070dc4c00df4b2d51c4611880a.jpg)

图片摘要：该图主要展示 19. Landing Approach Time History Pitch Rate Command and Air。
![](images/b662431a45967d24ac82cc5c851fce9fad7a7d45b21109b1b67a4ae6ca59fe88.jpg)  
Figure 20. Axial-Vertical Force-Pitching Moment Test Configurations for Thrust Control

图片摘要：该图主要展示 20. Axial Vertical Force Pitching Moment Test Configurations。
![](images/9fad62f793ec672c8ba73f2dc061511129d4ed89c4277ccd8e72885a8c528385.jpg)  
Figure 21. Longitudinal Response to   
Thrust Change - Configuration 8

图片摘要：该图主要展示 21. Longitudinal Response to。
![](images/9512cc436186671352148d35a76c4e8e69f73a2df225700375e8b4b98998ee79.jpg)  
Figure 22. Longitudinal Response to   
Thrust Change - Configuration 1

图片摘要：该图主要展示 22. Longitudinal Response to。
![](images/a4c381b769f1b3423fd8050bb5becb5b34e350f8e7b3edf518fb9424f558bd82.jpg)  
Figure 23. Longitudinal Response   
Thrust Change - Configuration 2

图片摘要：该图主要展示 23. Longitudinal Response。
![](images/d5d8fb1ade6b732b29beb27634ea8b84545bc52c7e0f030ee0b5a84773606f8f.jpg)  
Figure 2. Longitudinal Response to   
Thrust Change - Configuration 4

图片摘要：该图主要展示 2. Longitudinal Response to。
![](images/ff3f61cacc55c5e3a2c773ddc84ba99857fa58bc2baddafadece435471b9c883.jpg)  
Figure 25. Landing Approach Time History - Configuration 2

Trim Condition

$$
G W = 4 0, 0 0 0 2 b. S V = 4 0 a c g
$$

$$
V _ {0} = 6 0 k i s \quad \delta_ {T} = 7 5 2 0 k s
$$

$$
\gamma_ {0} = - 7. 5 \mathrm {d e g} \quad \delta_ {f} = 6 5 \mathrm {d e g}
$$

Thrust Control 3

$$
\frac {x _ {\delta_ {T}}}{z _ {\delta_ {T}}} \quad . 0 3 3 \quad \frac {M _ {\delta_ {T}}}{v} = - 0. 0 1 4 \frac {r a d}{f t}
$$

$$
\begin{array}{c c} \stackrel {{x}} {{-}} & . 0 8 \\ \stackrel {{c}} {{-}} & \end{array}
$$

图片摘要：该图主要展示 26. Landing Approach Time History Configuration 4。
![](images/5e7490aa4f88e62aba06a055ed4aa30faf37019d50d994e2b8455b639ad53b62.jpg)  
Figure 26. Landing Approach Time History - Configuration 4

# Trim Condition

$$
\begin{array}{l} G W = 4 0, 0 0 0 \mathrm {l b s}. \quad \delta v = 4 0 \mathrm {d e g} \\ v _ {0} = 6 0 k t \quad \delta_ {T} = 7 5 2 0 k s \\ r _ {0} = - 7. 5 \mathrm {d e g} \quad \delta_ {4} = 6 5 \mathrm {d e g} \\ \end{array}
$$

# Thrust Control Coupling

$$
\begin{array}{l} \frac {x _ {6 _ {T}}}{z _ {6 _ {T}}} = . 0 3 3 \quad \frac {M _ {8 _ {T}}}{z _ {6 _ {T}}} = . 0 0 5 7 \frac {\text {r a d}}{\text {f t}} \\ \frac {x}{c} = - 1 0 \\ \end{array}
$$

图片摘要：该图主要展示 27. Landing Approach Time History Configuration 9。
![](images/47150656fc3d47cf3c1ee59a283876dce4ba288c315f77b007caa02bb889a4ae.jpg)  
Figure 27. Landing Approach Time History - Configuration 9

图片摘要：该图主要展示 27. Landing Approach Time History Configuration 9。
![](images/36b6dd928c1c055d73618bf254202dbe1842767ca60187b7c88f2edd82ce9cae.jpg)

图片摘要：该图主要展示 27. Landing Approach Time History Configuration 9。
![](images/61498a40f07d76654a1ee41ee8af32471f630b902dcc42a863ef3f8df3f1b6d0.jpg)  
Figure 28. Axial-Vertical Force - Pitching Moment Test Configurations for Thrust Vector Control

图片摘要：该图主要展示 28. Axial Vertical Force Pitching Moment Test Configurations。
![](images/86f155a4562d7da5314efdd5b4b3127223c183e1d5f401bc9c3a5fc1d44253e3.jpg)  
Figure 29. Longitudinal Response to a Step   
Thrust Vector Change -   
Configuration ll

# Trim Condition

<table><tr><td>GW = 40,000 lbs.</td><td>δv= 40 deg</td></tr><tr><td>Vo = 60 kts</td><td>δr= 1520 lbs</td></tr><tr><td>r0=-7.5 deg</td><td>δf= 65 deg</td></tr></table>

# Thrust Vector Control Coupling

<table><tr><td>z
δv/χδv</td><td>0.0</td><td>M
δv/χδv</td><td>0.0</td><td>rad
ft</td></tr><tr><td></td><td>z0/c</td><td>0.0</td><td></td><td></td></tr></table>

图片摘要：该图主要展示 30. Landing Approach Time History Configuration 13。
![](images/4854446c6d9fc687a29f6bba742838b4374d736d008030812dcd35ae87bd5cb0.jpg)  
Figure 30. Landing Approach Time History Configuration 13

图片摘要：该图主要展示 30. Landing Approach Time History Configuration 13。
![](images/a9656cba33e5f3ca9566c0371d605224b0d79a57651ce184c7d86a43789b01b4.jpg)  
Figure 31. Time History of an Engine   
Failure During Landing Approach   
Basic Augmentor Wing Aircraft

图片摘要：该图主要展示 31. Time History of an Engine。
![](images/d5fa2a2f0a9229656a52c8efb92f7b9084305bd466527dd69df4c8fc47fe3534.jpg)  
Figure 32. Time History of an Engine Failure During Landing Approach-Attitude and Speed Stabilization Systems Engaged
