# Prediction of Aircraft Handling Qualities Using Analytical Models of the Human Pilot

Ronald A. Hess

April 1982

FOR REFERENCE

H

1

DAY 13 1982

LANGLEY RESEARCH

R

L1BRAry, NASA

HAMPTON, VIRGINIA

图片摘要：该图片与Prediction of Aircraft Handling Qualities Using Analytical Models of the Human P这部分内容相关。
![](images/c7ced619c504632971d57e17f4f48aeb63533f179c211c69c44fecf0f721eb5c.jpg)

# Prediction of Aircraft Handling Qualities Using Analytical Models of the Human Pilot

Ronald A. Hess, Ames Research Center, Moffett Field, California

图片摘要：该图片与PREDICTION OF AIRCRAFT HANDLING QUALITIES USING ANALYTICAL MODELS OF THE HUMAN P这部分内容相关。
![](images/06bfa7c7144ed122f2ecb915f852d103976b53e4f3f84afae396bed774722658.jpg)

# PREDICTION OF AIRCRAFT HANDLING QUALITIES USING ANALYTICAL MODELS OF THE HUMAN PILOT

by Ronald A. Hess Research Scientist NASA Ames Research Center, Moffett Field, California 94035

# SUMMARY

The optimal control model (OCM) of the human pilot is applied to the study of aircraft handling qualities. Attention is focused primarily on longitudinal tasks. The modeling technique differs from previous applications of the OCM in that considerable effort is expended in simplifying the pilot/vehicle analysis. After briefly reviewing the OCM, a technique for modeling the pilot controlling higher order systems is introduced. Following this, a simple criterion for determining the susceptibility of an aircraft to pilot-induced oscillations (PIO) is formulated. Finally, a model-based metric for pilot rating prediction is discussed. The resulting modeling procedure provides a relatively simple, yet unified approach to the study of a variety of handling qualities problems.

# 1. INTRODUCTION

The advent of modern digital stability and control augmentation systems has created a renewed interest in the study of aircraft longitudinal handling qualities. This renewed interest is attributable to two factors: First, the higher order nature of the dynamics typically associated with digital control systems makes analytical prediction of handling qualities difficult. Contemporary handling qualities specifications (Ref. 1) are written assuming "classical" aircraft characteristics, e.g., in the longitudinal mode, the existence of distinct and dominant short-period dynamics is assumed. With modern systems, the short-period characteristics may be dramatically altered by feedback and the higher order control system dynamics may dominate the vehicle handling qualities. Second, shortcomings in predictive techniques are made even more critical by the fact that severe handling qualities deficiencies often arise in practice which are directly attributable to the higher order nature of the digital control law implementation. An example of this is the ability of high frequency phase lags or time delays in the control system to sharply degrade aircraft handling qualities and to be a contributing factor to pilot-induced oscillations (Ref. 2).

In the research to be described, a pilot-modeling technique for handling qualities research, discussed in Ref. 3, is utilized and extended to cover higher order systems. The characteristics of over thirty aircraft configurations are analyzed, primarily in the longitudinal mode. Particular emphasis is placed upon those configurations where control system dynamics and time delays have been recognized as contributing factors to handling qualities deficiencies. The contribution of vehicle/control system dynamics to PIO tendencies is outlined, and a metric for pilot rating prediction is discussed.

# 2. BACKGROUND

The pilot-modeling technique as discussed in Ref. 3 forms the framework for the research described here. This technique utilizes the optimal control model of the human pilot and a novel method for the a priori selection of dominant OCM parameters (index of performance weighting coefficients and observation noise/signal ratios). A brief tutorial review of the procedure for selecting index of performance weighting coefficients is now presented. Consider the longitudinal tracking task of Fig. 1 in which the pilot is attempting to minimize pitch attitude deviations $\theta(t)$ in the presence of atmospheric disturbances. Ignore the dashed "internal attitude command" for the present. An acceptable index of performance for this task would be (Ref. 3)

$$
J = E \left\{\frac \lim  _ {X \rightarrow \infty} \frac {1}{2 X} \int_ {- X} ^ {X} \left[ \theta^ {2} (t) / \theta_ {M} ^ {2} + \dot {\delta} ^ {2} (t) / \dot {\delta} _ {M} ^ {2} \right] d t \right\}
$$

where $\delta(t)$ is control rate.

As discussed in Ref. 3, we assign an arbitrary maximum allowable deviation to the time rate of change of the error, $\dot{\theta}(t)$ , and denote it $\dot{\theta}_{\mathbf{M}}$ . Now an effective time constant $T$ can be introduced to define maximum allowable deviations of the integral and derivatives of $\dot{\theta}(t)$ as:

25-2

$$
\begin{array}{l} \theta_ {\mathrm {M}} = \dot {\theta} _ {\mathrm {M}} \mathrm {T}; \\ \dot {\theta} _ {M} = \text {s p e c i f i e d b u t a r b i t a r y}; \\ \ddot {\theta} _ {M} = \dot {\theta} _ {M} / T; \tag {1} \\ \end{array}
$$

and

$$
\ddot {\theta} _ {\mathrm {M}} = \ddot {\theta} _ {\mathrm {M}} / \mathrm {T} = \dot {\theta} _ {\mathrm {M}} / \mathrm {T} ^ {2}.
$$

The justification for using a single time constant to represent the ratio of the maximum value of a variable to that of its next highest derivative rests upon the system bandwidth implications which follow when Eq. (1) is used in implementing the OCM. We will also assign a maximum allowable deviation to the time rate of change of the pilot's control, $\delta(t)$ , and denote it $\delta_{\mathrm{M}}$ . Similar to Eq. (1) we write

$$
\begin{array}{l} \delta_ {\mathbf {M}} = \stackrel {\circ} {\delta} _ {\mathbf {M}} \mathbf {T}; \\ \delta_ {M} = \text {t o b e s e l e c t e d}; \\ \ddot {\delta} _ {M} = \dot {\delta} _ {M} / T; \\ \delta_ {\mathrm {M}} = \delta_ {\mathrm {M}} / \mathrm {T} = \delta_ {\mathrm {M}} / \mathrm {T} ^ {2}; \tag {2} \\ \end{array}
$$

The value of $\delta_{\mathbf{M}}$ is not arbitrary, however, but is found using Eqs. (1) and (2) and the vehicle dynamics as follows: Let the pitch attitude dynamics of the aircraft be given by

$$
\frac {\theta}{6} (s) = K \frac {s ^ {n - 1} + a _ {n - 2} s ^ {n - 2} + \dots + a _ {1} s + a _ {0}}{s ^ {n} + b _ {n - 1} s ^ {n - 1} + \dots + b _ {1} s + b _ {0}}. \tag {3}
$$

Then, as explained in Ref. 3, we write

$$
\dot {\delta} _ {M} = \frac {1 / T ^ {n - 1} + | b _ {n - 1} | / T ^ {n - 2} + . . . + | b _ {1} | + | b _ {0} | T}{K (1 / T ^ {n - 2} + | a _ {n - 2} | / T ^ {n - 3} + . . . + | a _ {1} | + | a _ {0} | T)} \dot {\theta} _ {M} \tag {4}
$$

Thus, once T is known, $\delta_{\mathbf{M}}$ and $\theta_{\mathbf{M}}$ (and, if needed, $\theta_{\mathbf{M}}$ , etc.) can be determined immediately. Choosing T involves selecting a domain of $1 / \mathrm{T}$ : $1 / 4\tau < 1 / \mathrm{T} < 4 / \tau$ and then plotting J, the value of the OCM index of performance, vs $1 / \mathrm{T}$ . The operating point or "knee" of this curve determines T. The knee is defined as the point where

$$
\frac {\partial J}{\partial \log (1 / T)} = n _ {\delta} \frac {J | _ {T = \tau / 4} - J | _ {T = 4 \tau}}{\log (4 / \tau) - \log (1 / 4 \tau)} \tag {5}
$$

Here $n_{\delta}$ is a constant, nominally unity, which can be used to reflect manipulator characteristics, much like an efficiency factor; $\tau$ is the pilot's time delay (nominally 0.2 sec). $J|_{T = \tau /4}$ is the value of the index of performance which results when $T = \tau /4$ .

The ability of the OCM parameter selection technique to provide a pilot model which matches measured pilot describing functions, remnant power spectral densities and root mean square (RMS) performance measures was demonstrated in Ref. 3. In addition, the

modeling technique was shown capable of providing qualitative and quantitative handling qualities assessments. The method for selecting observation noise/signal ratios for the OCM is discussed in Ref. 3 and will not be dealt with here.

Although Eq. (3) shows dynamics of arbitrary order, all the pitch attitude dynamics of Ref. 3 were of the form:

$$
\frac {\theta}{\delta} = \frac {K _ {\theta} \left(s + 1 / T _ {L}\right)}{s \left(s ^ {2} + 2 \zeta_ {n} \omega_ {n} s + \omega_ {n} ^ {2}\right)}. \tag {6}
$$

When higher order dynamics are encountered, the method for selecting the operating point needs to be modified slightly. The large phase lags typically associated with the dynamics of vehicles with higher order dynamics need to be reflected in choosing the domain of $\frac{1}{\tau}$ to be used in Eq. (5). To accomplish this, a delay $\tau_{D}$ is defined as the delay which accrues when the vehicle dynamics of Eq. (3) are represented as

$$
\frac {\theta}{\delta} = \frac {K _ {\theta} (s + 1 / T _ {L}) e ^ {- \tau_ {D} s}}{s \left(s ^ {2} + 2 \tau_ {n} \omega_ {n} s + \omega_ {n} ^ {2}\right)} \tag {7}
$$

The parameters on the right hand side of Eq. (7) are found using a program to fit a linar transfer function model to the actual vehicle dynamics (Ref. 4). Equation (5) is modified by simply replacing $\tau$ with $\tau + \tau_{D}$ . The resulting equation is interpreted graphically in Fig. 2. Calculating $\tau_{D}$ and including it in Eq. (5) constitutes the extension of the methods of Ref. 3 to higher order systems. It is important to emphasize that the actual higher order vehicle dynamics are used in the modeling procedure; Eq. (7) is employed only to select $\tau_{D}$ which, in turn, determines the domain of $l / T$ used in finding the index of performance weighting coefficients.

# 3. APPLICATION TO AIRCRAFT HANDLING QUALITIES

# 3.1 Pilot-Induced Oscillations

Table I lists the aircraft configurations which have been analyzed in this study. The designations in the column labeled "Configuration" use notation found in the corresponding references. The first sixteen deal with high performance fighter-type aircraft in tracking or landing approach conditions and are taken from Refs. 2, 5, and 6. These configurations constitute the test cases for the majority of the assessments. The next four configurations are taken from Ref. 7 and represent pilot-in-the-loop simulations of a hovering helicopter. Configurations 21-25 are flight test results from Ref. 9 in which the Princeton University Variable Response Aircraft (VRA) was used to determine the effect of digital sampling rates and time delays on longitudinal handling qualities. The vehicle dynamics appropriate for 105 kts airspeed were used in the modeling procedure. The pilot ratings used were average values obtained from altitude tracking and approach and landing tasks (Fig. 3 of Ref. 9). Finally, configurations 26-32 are taken from Ref. 10 where a moving-base simulator experiment on the NASA Ames Flight Simulator for Advanced Aircraft (FSAA) was described which investigated a wings level-turn control mode for air-to-ground weapons delivery. Note that unlike the previous twenty-five configurations, these involve lateral-directional aircraft handling qualities. The effective vehicle dynamics for the lateral gunsight aiming task were parameterized by a damping ratio $\zeta_{\mathrm{n}}$ , an undamped natural frequency $\omega_{\mathrm{n}}$ and a pure time delay $\tau_{\mathrm{D}}$ (Ref. 10). The data for the so-called "fine" task were used. This task is explained in Ref. 10.

As an example of the modeling results, Fig. 3 shows the longitudinal open-loop pilot/vehicle characteristics $(\mathrm{Y_pY_c})$ for three of the configurations used in Ref. 2. Here, the NASA Dryden F-8 digital fly-by-wire aircraft is considered with a rudimentary augmentation system ("Pitch Direct") and three transport time delays of 0.13 sec, 0.23 sec, and 0.33 sec, respectively. The predicted effect of the time delays is apparent in the reduced open-loop crossover frequencies $\omega_{c}$ . This open-loop characteristic obviously has a deleterious effect on the closed loop $\theta / \theta_{c}$ transfer functions as shown in Fig. 4 $[\theta / \theta_{c} = \mathrm{Y}_{p} \mathrm{Y}_{c} / (1 + \mathrm{Y}_{p} \mathrm{Y}_{c})]$ . This transfer function is important in assessing PIO susceptibility. Although the task has been defined as pitch-attitude disturbance regulation, attitude commands $\theta_{c}$ internally generated by the pilot would be employed in precise altitude regulation (dashed line in Fig. 1). Note in Fig. 4, that as $\tau_{D}$ increases, $|\theta / \theta_{c}|$ and $\angle \theta / \theta_{c}$ decrease at all frequencies. Perfect command following, of course, implies $\theta / \theta_{c} = 1.0$ at all frequencies. In Fig. 4, $|\theta / \theta_{c}| < 1.0$ for all configurations when $\omega < 3.0$ rad/sec, and is particularly poor for the configuration with $\tau_{D} = 0.33$ sec. It can be readily shown that open-loop crossover frequencies less than 3-4 rad/sec will invariably result in poor closed-loop attitude command-following characteristics. The simplest and most direct way for the pilot to attempt to improve this closed loop command-following performance is to increase $\omega_{c}$ by increasing his

static gain. If the pilot attempts this for the F-8 configuration with $\tau_{\mathrm{D}} = 0.33$ sec, a very lightly damped closed-loop oscillation occurs at $\omega = 3.3$ rad/sec (see Fig. 4). This is identical to the PIO frequency shown in Ref. 2 for this configuration.

Similar results are also obtained for configurations from Ref. 5. Figure 5 compares a pair of open-loop transfer functions obtained using configurations "11" and "12" from Ref. 5 and applying the pilot-modeling technique discussed above. Once again, the dramatic difference in the crossover frequencies $\omega_{C}$ is apparent. The effects of the pilot's attempting to improve the performance of configuration "12" by increasing his static gain by 10 dB are shown in Fig. 6. Once again, a lightly damped oscillatory mode is seen to appear. The simulations of Ref. 5 were intended to provide performance comparisons for configurations which were flight tested and discussed in Ref. 8. The latter report included Pilot-Induced-Oscillation-Ratings (PIOR) obtained using the scale of Fig. 7. It is interesting to note that configuration "11" received an average PIOR of 1 indicating a very satisfactory vehicle whereas configuration "12" received a marginal average rating of 2.7 indicating a vehicle with definite PIO tendencies. These experimental results are seen to corroborate the analytical findings just discussed.

Next, consider two configurations from Ref. 6 denoted as "4-1" and "6-1." Figure 8 shows the $\mathrm{Y_pY_c}$ plots for these configurations. Configuration "4-1" received a very satisfactory PIOR of 1 whereas configuration "6-1" received a very poor PIOR of 4. Indeed, configuration "6-1" produced a PIO in flight test with a frequency of approximately 3.75 rad/sec. Analytically increasing the pilot's static gain by 4.75 dB (the limit for closed-loop stability) in the modeling-results for this configuration produced a closed-loop oscillation at approximately 3.5 rad/sec. This 4.75 dB increase would increase $\omega_{\mathrm{c}}$ from around 1.5 rad/sec to only around 2.5 rad/sec as compared to a value of 4.5 rad/sec for configuration "4-1."

Figure 9 shows the predicted $\mathrm{Y_pY_c}$ 's for a pair of configurations from Ref. 9. The task was longitudinal control in approach and landing using the Princeton VRA. The variable of interest here was the amount of effective delay in the control system. In the first, an effective delay of 0.055 sec was employed, while in the second, 0.355 sec was used. Again, note the striking difference in crossover frequencies in the predicted pilot/vehicle dynamics. In the first case, $\omega_{\mathrm{c}} = 3.4$ rad/sec, while in the latter, $\omega_{\mathrm{c}} = 0.55$ rad/sec. Flight test of the first configuration showed no PIO tendencies, while those for the latter produced PIO's (Ref. 9).

Finally, Fig. 10 shows the predicted $\mathrm{Y_pY_c}$ 's for a pair of configurations from Ref. 10. In the first, the control system parameters were $\zeta_{\mathrm{n}} = 1.4$ , $\omega_{\mathrm{n}} = 2.0$ rad/sec and $\tau_{\mathrm{D}} = 0.0$ sec, while in the second, $\zeta_{\mathrm{n}} = 1.4$ , $\omega_{\mathrm{n}} = 15.0$ rad/sec and $\tau_{\mathrm{D}} = 0.49$ sec. The $\omega_{\mathrm{c}}$ difference is again evident. Simulation results indicated that the configuration with delay was definitely PIO prone and the one without delay was not. It is interesting to point out that the configuration without delay still received an average Cooper-Harper pilot rating of 6.5, even though it was not PIO prone. Thus, poor pilot ratings, per se, are not a necessary condition for PIO susceptibility.

In each of the cases above, we have made direct comparisons of vehicles which were found to be PIO prone with those which were not. This was done to emphasize the fact that the method proposed here is clearly discriminatory in predicting PIO susceptibility. The simple criterion for exonerating a vehicle from PIO tendencies requires that the predicted pilot/vehicle crossover frequencies associated with inner attitude-loops be greater than 3-4 rad/sec.

# 3.2 Cooper-Harper Ratings

Figure 11 is a plot of the Cooper-Harper ratings which the thirty-one configurations from Table I received in simulation or flight test vs the value of a proposed handling qualities metric defined as $\mathrm{K_i}[(\tau + \tau_D) / \tau]^{*} \cdot J$ . No ratings were reported in Ref. 10 for configuration 32 of Table I. Hence, only thirty-one data points are shown in Fig. 11. The $\mathrm{K_i}$ can be interpreted as a "calibration parameter" which, when multiplied by $[(1 + \tau_D) / \tau]^{*} \cdot J$ , allows the reported pilot ratings from different tasks and data sources to coalesce as shown in Fig. 11. Note that we do not allow $\mathrm{K_i}$ to vary within the analysis of any particular task, regardless of configuration changes. Thus, the analysis of the six configurations from Ref. 2 used a single value of $\mathrm{K_i}$ (call it $\mathrm{K_1}$ ). The analysis of the seven configurations from Refs. 5 and 8 used a single value of $\mathrm{K_i}$ (call it $\mathrm{K_2}$ ), etc. In all, six different $\mathrm{K_i}$ values (each one corresponding to the six different symbols in Fig. 11) were used to generate Fig. 11. With the exception of $\mathrm{K_i}$ , all the parameters of the metric are an intrinsic part of the modeling procedure, and, as such, involve no guesswork on the part of the analyst. In order to determine $\mathrm{K_i}$ , the analyst must have an actual pilot rating for one of the configurations tested for the task under study. If the analyst does not have such a rating available, Fig. 11 is still useful, since the curve is nearly linear from a pilot rating of about 2.0 to 10.0, a range which covers 80% of the Cooper-Harper scale. Thus, relative rating changes may be able to be predicted using the linear portion of the curve. Note that, with the exception of one data point (Config. 19 from Ref. 7), the scatter in the ratings in Fig. 11 is only about ±½ a pilot rating.

The inclusion of the factor $\left[\left(\tau + \tau_{\mathrm{D}}\right) / \tau\right]^{4}$ in the metric deserves a brief discussion. In previous research with the OCM, the value of $J$ , alone, has been found to correlate well with pilot opinion rating (Ref. 11). In many of the configurations studied here, however (those with $\tau_{\mathrm{D}} > 0$ ), the value of $J$ was not acceptable as a metric. In

general, the "predicted" opinion rating increments were smaller than those reported in experiment. There appears to be a reason for this based upon pilot tracking performance. Namely, when the task is disturbance regulation involving relatively low-bandwidth turbulence, large time delays are not necessarily a harbinger of dramatic deterioration in tracking performance. This is analytically verified by considering the RMS tracking scores for configurations 1 and 3 from Table I. Here, a $154\%$ increase in time delay between configurations 1 and 3 involves a log wc regression of nearly a decade. However, the predicted RMS pitch attitude score increases by only $36\%$ and the predicted RMS control-rate score actually decreases. As we have attempted to point out here, however, the same cannot be said for discrete command following or abrupt maneuvers. In this case, $\omega_{C}$ regression can have a significant impact on the ability of the closed-loop pilot/vehicle system to follow abrupt, internally generated commands. It certainly is not unreasonable to postulate that such short-term response characteristics (in addition to RMS characteristics) are reflected in pilot opinion rating. Indeed, recorded pilot comments support this notion (e.g., Refs. 2 and 6). The inclusion of $\left[\tau + \tau_{D}\right] / \tau$ " in the metric appears to account for the influence of these delays on pilot opinion in a straightforward manner, employing an easily identifiable parameter ( $\tau_{D}$ ).

# 4. CONCLUSIONS

The research summarized in this paper provides a unified approach to pilot/vehicle analysis, and in particular for:

1) Modeling the pilot controlling higher order systems.   
2) Predicting the susceptibility of aircraft to longitudinal PIO's.   
3) Predicting pilot ratings for tasks when one configuration rating is known, or predicting relative rating changes between configurations.

Although the majority of tasks studied dealt with longitudinal control, five lateral-directional configurations were successfully analyzed with no changes in the modeling technique.

# 5. REFERENCES

1. Anon.: Military Specification, Flying Qualities of Piloted Airplanes: MIL-F-8785B(ASG), August 1969.   
2. Berry, D.T., Powers, Bruce G., Szalai, K.J., and Wilson, R.J.: A Summary of an In-Flight Evaluation of Control System Pure Time Delays During Landing Using the F-8 DFBW Airplane, AIAA Paper No. 80-1626. 1980 AIAA Atmospheric Flight Mechanics Conference, Danvers, Mass.   
3. Hess, R.A.: A Pilot Modeling Technique for Handling Qualities Research, AIAA Paper No. 80-1624. 1980 AIAA Atmospheric Flight Mechanics Conference, Danvers, Mass.   
4. Seidel, R.C.: Transfer-Function-Parameter Estimation From Frequency Response Data--A FORTRAN Program. NASA TM X-3286, 1975.   
5. Arnold, J.D.: An Improved Method of Predicting Aircraft Longitudinal Handling Qualities Based on the Minimum Pilot Rating Concept. Air Force Institute of Technology, GGC/MA/73-122, 1973.   
6. Smith, Rogers, E.: Effects of Control System Dynamics on Fighter Approach and Landing Longitudinal Flying Qualities, Vol. 1. Air Force Flight Dynamics Laboratory, AFFDL-TR-73-122, 1978.   
7. Miller, D.P.; and Vinje, E.W.: Fixed-Base Flight Simulator Studies of VTOL Aircraft Handling Qualities in Hovering and Low-Speed Flight. Air Force Flight Dynamics Laboratory, AFFDL-TR-67-152, 1968.   
8. Neal, Peter T.; and Smith, Rogers E.: An In-Flight Investigation to Develop Control System Design Criteria for Fighter Airplanes. Air Force Flight Dynamics Laboratory, AFFDL-TR-70-74, 1970.   
9. Stengel, R.F.; and Miller, G.E.: Flight Tests of a Microprocessor Control System. Journal of Guidance and Control, Vol. 3, No. 6, Nov.-Dec. 1980, pp. 494-500.   
10. Sammonds, R.I.; and Bunnell, J.W., Jr.: Flying Qualities Criteria for Wings-Level-Turn Maneuvering During an Air-to-Ground Weapon Delivery Task. AIAA Paper No. 80-1628. 1980 AIAA Atmospheric Flight Mechanics Conference, Aug. 11-13, 1980.   
11. Hess, R.A.: Prediction of Pilot Opinion Ratings Using an Optimal Pilot Model. Human Factors, Vol. 19, No. 5, Oct. 1977, pp. 459-475.

Table I. Aircraft Configurations Analyzed   

<table><tr><td>No.</td><td colspan="4">Configuration</td><td>Reference</td></tr><tr><td>1</td><td>F-8 &quot;Pitch Direct&quot;</td><td colspan="3">0.13 sec delay</td><td>2</td></tr><tr><td>2</td><td></td><td colspan="3">.23</td><td>2</td></tr><tr><td>3</td><td></td><td colspan="3">.33</td><td>2</td></tr><tr><td>4</td><td>&quot;ISAS&quot;</td><td colspan="3">0.13 sec delay</td><td>2</td></tr><tr><td>5</td><td></td><td colspan="3">.23</td><td>2</td></tr><tr><td>6</td><td></td><td colspan="3">.33</td><td>2</td></tr><tr><td>7</td><td>&quot;2D&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>8</td><td>&quot;5A&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>9</td><td>&quot;8A&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>10</td><td>&quot;9&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>11</td><td>&quot;10&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>12</td><td>&quot;11&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>13</td><td>&quot;12&quot;</td><td colspan="3"></td><td>5,8</td></tr><tr><td>14</td><td>&quot;3-1&quot;</td><td colspan="3"></td><td>6</td></tr><tr><td>15</td><td>&quot;4-1&quot;</td><td colspan="3"></td><td>6</td></tr><tr><td>16</td><td>&quot;6-1&quot;</td><td colspan="3"></td><td>6</td></tr><tr><td>17</td><td>&quot;PH-28&quot;</td><td colspan="3"></td><td>7</td></tr><tr><td>18</td><td>&quot;PH-29&quot;</td><td colspan="3"></td><td>7</td></tr><tr><td>19</td><td>&quot;PH-32&quot;</td><td colspan="3"></td><td>7</td></tr><tr><td>20</td><td>&quot;PH-35&quot;</td><td colspan="3"></td><td>7</td></tr><tr><td>21</td><td>Princeton VRA</td><td colspan="3">0.055 sec delay</td><td>9</td></tr><tr><td>22</td><td></td><td colspan="3">.135</td><td>9</td></tr><tr><td>23</td><td></td><td colspan="3">.255</td><td>9</td></tr><tr><td>24</td><td></td><td colspan="3">.355</td><td>9</td></tr><tr><td>25</td><td></td><td colspan="3">.455</td><td>9</td></tr><tr><td></td><td>FSAA Wings-Level Turn (lateral-directional)</td><td>\( \zeta_n \)</td><td>\( \omega_n \) (rad/sec)</td><td>\( \tau_D \) (sec)</td><td>10</td></tr><tr><td>26</td><td></td><td>1.4</td><td>15.0</td><td>0</td><td>10</td></tr><tr><td>27</td><td></td><td>1.4</td><td>2.0</td><td>0</td><td>10</td></tr><tr><td>28</td><td></td><td>2.0</td><td>8.0</td><td>0</td><td>10</td></tr><tr><td>29</td><td></td><td>0.7</td><td>6.0</td><td>0</td><td>10</td></tr><tr><td>30</td><td></td><td>0.5</td><td>4.5</td><td>0</td><td>10</td></tr><tr><td>31</td><td></td><td>0.3</td><td>4.5</td><td>0</td><td>10</td></tr><tr><td>32</td><td></td><td>1.4</td><td>4.5</td><td>0.49</td><td>10</td></tr></table>

图片摘要：该图主要展示 I. Aircraft Configurations Analyzed。
![](images/0abc03a9ea8821f523ac53d7b22e5e2ad4ec744890b01dff191e2efdbd7af574.jpg)  
Figure 1. A pitch attitude regulation task.

图片摘要：该图主要展示 1. A pitch attitude regulation task。
![](images/ce712ed3436d432fd1d10848363ff2110d3a27a1186e96c3b4cd2f48da7574b6.jpg)  
Figure 2. Selecting an "effective time constant" T.

图片摘要：该图主要展示 2. Selecting an "effective time constant" T。
![](images/7f46c77e1e471cef8720d63d0fb00413e7b01b97ec814c9864a45c28caa79b59.jpg)  
Figure 3. Pilot/vehicle dynamics for three configurations from Ref. 2.

$$
- - - - \frac {\Theta}{\Theta_ {c}} F O R r _ {D} = 0. 3 3 \mathrm {s e c} A N D 5 \mathrm {d B I N C R E M E N T I N Y} _ {p}
$$

图片摘要：该图主要展示 3. Pilot/vehicle dynamics for three configurations from Ref.。
![](images/ab83b41063de6d6a9c6aba2fbe2e6c93dcf0cb7a115c5bd24b268686928de413.jpg)  
Figure 4. Closed-loop characteristics for three configurations from Ref. 2.

图片摘要：该图主要展示 4. Closed loop characteristics for three configurations from。
![](images/8e723e4aa139eb46ec05571cac9d5e971cc352e4708e43b48a734b119ebef40d.jpg)  
Figure 5. Pilot/vehicle dynamics for two configurations from Ref. 5.

图片摘要：该图主要展示 5. Pilot/vehicle dynamics for two configurations from Ref. 5。
![](images/2685db39a837ce4c8b4c4b0c19885964157329a1e595eff9150ffe6cb8631d23.jpg)  
Figure 6. Closed-loop characteristics for a configuration from Ref. 5.

PIO TENDENCY RATING SCALE   
Figure 7. The pilot-induced-oscillation rating scale.   

<table><tr><td>DESCRIPTION</td><td>NUMERICALRATING</td></tr><tr><td>NO TENDENCY FOR PILOT TO INDUCE UNDESIRABLE MOTIONS.</td><td>1</td></tr><tr><td>UNDESIRED MOTIONS TEND TO OCCUR WHEN PILOT INITIATES ABRUPT MANEUVERS OR ATTEMPTS TIGHT CONTROL. THESE MOTIONS CAN BE PREVENTED OR ELIMINATED BY PILOT TECHNIQUE.</td><td>2</td></tr><tr><td>UNDESIRED MOTIONS EASILY INDUCED WHEN PILOT INITIATES ABRUPT MANEUVERS OR ATTEMPTS TIGHT CONTROL. THESE MOTIONS CAN BE PREVENTED OR ELIMINATED BUT ONLY AT SACRIFICE TO TASK PERFORMANCE OR THROUGH CONSIDERABLE PILOT ATTENTION AND EFFORT.</td><td>3</td></tr><tr><td>OSCILLATIONS TEND TO DEVELOP WHEN PILOT INITIATES ABRUPT MANEUVERS OR ATTEMPTS TIGHT CONTROL. PILOT MUST REDUCE GAIN OR ABANDON TASK TO RECOVER.</td><td>4</td></tr><tr><td>DIVERGENT OSCILLATIONS TEND TO DEVELOP WHEN PILOT INITIATES ABRUPT MANEUVERS OR ATTEMPTS TIGHT CONTROL. PILOT MUST OPEN LOOP BY RELEASING OR FREEZING THE STICK.</td><td>5</td></tr><tr><td>DISTURBANCE OR NORMAL PILOT CONTROL MAY CAUSE DIVERGENT OSCILLATION. PILOT MUST OPEN CONTROL LOOP BY RELEASING OR FREEZING THE STICK.</td><td>6</td></tr></table>

图片摘要：该图主要展示 7. The pilot induced oscillation rating scale。
![](images/dc7297cd130a5c622f83f5bc794e7b0d86fba23725bc82a456c481b5251500aa.jpg)  
Figure 8. Pilot/vehicle dynamics for two configurations from Ref. 6.

图片摘要：该图主要展示 8. Pilot/vehicle dynamics for two configurations from Ref. 6。
![](images/98b96f4589c56e8fba260bb5a294633114c1fccda48ff3fe499be949e35e7b84.jpg)  
Figure 9. Pilot/vehicle dynamics for two configurations from Ref. 9.

图片摘要：该图主要展示 9. Pilot/vehicle dynamics for two configurations from Ref. 9。
![](images/1e1000840fb45eb5e61023fc9dca0165ce054773856a8e1926f7d22a7954399c.jpg)  
Figure 10. Pilot/vehicle dynamics for two configurations from Ref. 10.

图片摘要：该图主要展示 10. Pilot/vehicle dynamics for two configurations from Ref. 。
![](images/8b29c467ab789ac9c7b1c5612ef0ea94b08cb9225546a6fdf8d4998a6eab53fa.jpg)  
Figure 11. Cooper-Harper pilot ratings vs a proposed model-based metric.

<table><tr><td>1. Report No.
NASA TM-84233</td><td colspan="2">2. Government Accession No.</td><td colspan="2">3. Recipient&#x27;s Catalog No.</td></tr><tr><td rowspan="2" colspan="3">4. Title and Subtitle
PREDICTION OF AIRCRAFT HANDLING QUALITIES USING
ANALYTICAL MODELS OF THE HUMAN PILOT</td><td colspan="2">5. Report Date
April 1982</td></tr><tr><td colspan="2">6. Performing Organization Code</td></tr><tr><td rowspan="2" colspan="3">7. Author(s)
Ronald A. Hess</td><td colspan="2">8. Performing Organization Report No.
A-8884</td></tr><tr><td colspan="2">10. Work Unit No.
T-3608Y</td></tr><tr><td rowspan="2" colspan="3">9. Performing Organization Name and Address
Ames Research Center, Moffett Field, CA 94035</td><td colspan="2">11. Contract or Grant No.</td></tr><tr><td colspan="2">13. Type of Report and Period Covered
Technical Memorandum</td></tr><tr><td colspan="3">12. Sponsoring Agency Name and Address
National Aeronautics and Space Administration
Washington, DC 20546</td><td colspan="2">14. Sponsoring Agency Code
505-44-21</td></tr><tr><td colspan="5">15. Supplementary Notes
Point of contact: Ronald A. Hess. Ames Research Center, MS 210-9, Moffett
Field, CA 94035. (415)965-5443 or FTS 448-5443.</td></tr><tr><td colspan="5">16. Abstract
The optimal control model (OCM) of the human pilot is applied to the
study of aircraft handling qualities. Attention is focused primarily on
longitudinal tasks. The modeling technique differs from previous appli-
cations of the OCM in that considerable effort is expended in simplifying
the pilot/vehicle analysis. After briefly reviewing the OCM, a technique
for modeling the pilot controlling higher order systems is introduced. Fol-
lowing this, a simple criterion for determining the susceptibility of an
aircraft to pilot-induced oscillations (PIO) is formulated. Finally, a
model-based metric for pilot rating prediction is discussed. The resulting
modeling procedure provides a relatively simple, yet unified approach to the
study of a variety of handling qualities problems.</td></tr><tr><td colspan="2">17. Key Words (Suggested by Author(s))
Pilot Models
Handling Qualities
Pilot-Induced-Oscillations</td><td colspan="3">18. Distribution Statement
Unlimited
Subject Category-08</td></tr><tr><td>19. Security Classif. (of this report)
Unclassified</td><td colspan="2">20. Security Classif. (of this page)
Unclassified</td><td>21. No. of Pages
11</td><td>22. Price*
A02</td></tr></table>

图片摘要：该图片与11 22. Price；Unclassified 21. No. of Pages这部分内容相关。
![](images/c4c9612fb9985e9d7e468c7fabe2444ba081dfdaeffbee81436b5ce0ce3090ef.jpg)
