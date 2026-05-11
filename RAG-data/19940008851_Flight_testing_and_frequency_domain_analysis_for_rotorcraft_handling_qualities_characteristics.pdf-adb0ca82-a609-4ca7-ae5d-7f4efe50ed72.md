# FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS

MAJ Johnnie A. Ham

Charles K. Gardner

Airworthiness Qualification Test Directorate (Edwards AFB, CA)

US Army Aviation Technical Test Center

Ft Rucker, Alabama

Mark B. Tischler

Aeroflightdynamics Directorate

U.S. Army ATCOM

Ames Research Center

Moffett Field, California

# Abstract

A demonstration of frequency domain flight testing techniques and analyses was performed on a U.S. Army OH-58D helicopter in support of the OH-58D Airworthiness and Flight Characteristics Evaluation and the Army's development and ongoing review of Aeronautical Design Standard 33C, Handling Qualities Requirements for Military Rotorcraft. Hover and forward flight (60 knots) tests were conducted in 1 flight hour by Army experimental test pilots. Further processing of the hover data generated a complete database of velocity, angular rate, and acceleration frequency responses to control inputs. A joint effort was then undertaken by the Airworthiness Qualification Test Directorate (AQTD) and the US Army Aeroflightdynamics Directorate (AFDD) to derive handling qualities information from the frequency response database. A significant amount of information could be extracted from the frequency domain database using a variety of approaches. This report documents numerous results that have been obtained from the simple frequency domain tests; in many areas, these results provide more insight into the aircraft dynamics that affect handling qualities than do traditional flight tests. The handling qualities results include ADS-33C bandwidth and phase delay calculations, vibration spectral determinations, transfer function models to examine single axis results, and a six degree of freedom fully coupled state space model. The ability of this model to accurately predict aircraft responses was verified using data from pulse inputs. This report also documents the frequency-sweep flight test technique and data analysis used to support the tests.

# Introduction

# Background

Quantifying the "handling qualities" of rotorcraft has been a difficult task for the flight test community to accomplish. In its truest form, an aircraft's handling qualities are comprised of a set of metrics that measure objectively, the ease with which a pilot can perform a specified task. In the past, one method used by the testing community has been to measure specified static and dynamic characteristics, such as trim control positions and forces, stick characteristics, and aircraft responses to disturbances. There has been an attempt to measure selected stability and control derivatives individually through separate tests (in essence, a rough method of system identification). As an example, the character of speed stability $(\mathbf{M}_{\mathbf{u}})$ , the pitching moment generated due to longitudinal velocity perturbations), has been measured by relating the longitudinal cyclic position to changes in airspeed from a trim condition, as shown in the following quasi-static equation:

$$
\mathbf {M} _ {\mathbf {u}} = - \mathbf {M} \delta_ {\text {l o n g}} (\mathrm {d} \delta_ {\text {l o n g}} / \mathrm {d u})
$$

If forward cyclic is required for increasing velocity from trim, there is positive longitudinal static stability, which is considered "good." This provides information on the character of the speed stability, but not its magnitude, since there is no direct measurement of pitching moment due to longitudinal cyclic. It also becomes an invalid test for sophisticated modern control systems, such as a sidearm controller that commands acceleration, but holds velocity. A plot of stick position versus airspeed for this system would show neutral static stability, when in fact the aircraft may possess strong speed stability.

The demands of the next generation of rotorcraft require a closer than ever link between flight control

system design and aircraft handling qualities. This requirement, coupled with the presence of powerful computing systems and sophisticated software and tools, allows us to carefully characterize the aircraft dynamics that affect its handling qualities. The analysis tools presented in this paper allow for the accurate determination of the aircraft frequency responses, which can then be approximated with transfer function and stability and control derivative models to yield quantitative descriptions of the aircraft behavior. The analyses for this paper were conducted using a frequency domain based approach, which first requires generation of the flight test frequency domain database. Once the database has been generated, numerous applications can be derived from the data, as shown in figure 1.

图片摘要：该图主要展示 1 Diagram of the applications。
![](images/56e308227e64803ad6702901e3ef01f767f898610e664d603b4dc3a65d7fb2c8.jpg)  
Fig. 1 Diagram of the applications

# Coverage of the Paper

This paper presents a detailed flight test example of the application of these methods to the OH-58D. The goal of the system identification was to characterize the aircraft handling qualities with simple models rather than to create very high fidelity models that may be needed for detailed simulation validation. The simple models provide significant insight into the aircraft's dynamic behavior in the piloted frequency range, using significantly less flight test time than traditional tests. The paper discusses testing requirements, instrumentation, data processing, and interpretation, and shows its usefulness as a tool in testing new and modified aircraft.

# Description of the Test Aircraft

The test aircraft was a production OH-58D helicopter. This aircraft is a two-place, single-main-rotor helicopter powered by an Allison 250-C30R engine rated at 650 shaft horsepower. The engine drives a 4-bladed, soft in-plane composite main rotor and a two-bladed teetering tail rotor. The main rotor is outfitted with elastomeric lead-lag dampers and pitch-change bearings; flapping occurs through bending of the blade and the yoke to which the blades are attached, as well as through movement allowed by the elastomeric fittings which

attach the blade to the yoke. Control inputs to the rotors are provided through an irreversible hydraulic system with a limited-authority stability and control augmentation system. The helicopter can be armed with a .50 caliber machine gun, 2.75" folding-fin aerial rockets, heat-seeking air-to-air Stinger missiles, and laser-guided HELLFIIRE missiles. A sight mounted above the rotor hub houses a laser rangefinder and target designator, and both infrared and television sensors that provide images to the crew. The helicopter has a maximum gross weight of 5500 pounds in the armed configuration and 4500 pounds in the unarmed configuration. A sideview of the OH-58D helicopter is shown in Figure 2, and additional physical characteristics of the helicopter are listed in Table 1.

图片摘要：该图主要展示 2. OH 58D Sideview。
![](images/2c004af27d049fd19e17aad90faab4f97561e8894e8818411c88831755166d80.jpg)  
Figure 2. OH-58D Sideview

<table><tr><td colspan="2">Table 1 OH-58D Physical Characteristics</td></tr><tr><td>Maximum gross weights:</td><td></td></tr><tr><td>unarmed</td><td>4500 lb</td></tr><tr><td>armed</td><td>5500 lb</td></tr><tr><td>Main rotor:</td><td></td></tr><tr><td>number of blades</td><td>4</td></tr><tr><td>diameter</td><td>35.0 ft</td></tr><tr><td>chord</td><td>13.0 in</td></tr><tr><td>tip speed</td><td>725 ft/s</td></tr><tr><td>effective hinge offset</td><td>2.9%</td></tr><tr><td>Tail rotor:</td><td></td></tr><tr><td>number of blades</td><td>2</td></tr><tr><td>diameter</td><td>5.42 ft</td></tr><tr><td>chord</td><td>5.3 in</td></tr></table>

The OH-58D helicopter is used primarily in the scout mission, where it acquires, tracks and designates targets for AH-64A attack helicopters. The mission includes battlefield management, which entails a range of battle coordination tasks including artillery, air defense, and Air Force ground attack integration, as well as maneuver unit control. In an armed configuration, the helicopter can perform light attack missions by providing air-to-air and air-to-ground fire.

Tests for this paper were conducted at approximately 4800 pounds with weapon pylons and empty ejector racks on the helicopter. The aircraft had a pulse-codemodulation instrumentation system onboard which recorded measurements on magnetic tape and also transmitted these measurements to a ground monitoring station. The instrumentation system included an extensive array of sensors, although measurements for this paper were all provided by angular attitude and rate gyros, linear accelerometers, and potentiometers that indicated cockpit control positions. Further details of the test aircraft are provided in reference 1.

# Flight Test Technique

# Instrumentation

The results of frequency domain analyses are strongly influenced by the characteristics of the aircraft instrumentation system. And although useful data can be gathered with an instrumentation set-up not intended for frequency domain tests (as were the data for this paper), a properly designed instrumentation package can greatly improve results. This section describes innstrumentation considerations for frequency domain testing.

Measurements typically required for handling qualities analyses consist of angular rates and attitudes, linear velocities and accelerations, and control positions. The accelerometers should be located as close to the center of gravity as possible, and their positions with respect to the cg should be accurately known. This information is used to correct the acceleration measurements to the cg--a step that is necessary to determine meaningful aircraft accelerations. Control positions can be measured at the pilot's stick or at the actuator outputs. Frequency responses derived from pilot stick measurements represent the closed-loop aircraft dynamics (aircraft dynamics as modified by the stability and control augmentation system), whereas frequency responses derived from actuator output measurements represent the open-loop or bare-airframe dynamics.

One consideration with all the measurements is that the range of the measurement is not so large that the resolution is unacceptably large. With an 8-bit data system, for example, the resolution of a roll attitude gyro with a range of $\pm 180$ degrees is 1.4 degrees--probably not acceptable for analyses of small-amplitude aircraft motions.

Aircraft instrumentation systems usually employ analog anti-aliasing filters. Because their properties are often not well-defined, these filters can unacceptably distort the data. To minimize such effects, similar filters should be used on all the measurements. This ensures, most importantly, that time delays introduced by the filters affect all measurements alike (time delays greatly

influence the frequency response phase curves derived from the data). The cutoff frequency of the filters should not be less than about five times the highest frequency of interest. This guarantees that the data is modified only by the low-frequency end of the filter pass band, where filter phase distortions are small. Additional filtering with well-defined digital filters can be performed after the data is recorded. The data sample rate must be at least twice the filter cutoff frequency; a sample rate five times the filter cutoff frequency is preferable to avoid aliasing effects. Obviously, a common sample rate among all measurements is desirable, although not necessary.

A final issue is the time skew between measurements inherent in a data system that samples measurements sequentially. These time skews are usually small (10 ms is typical). Nevertheless, a data system structured to sample handling qualities measurements in the shortest time interval possible minimizes time skews between channels.

Measurements taken on the OH-58D and used for this paper consisted of aircraft attitudes, angular rates, linear accelerations, and control positions. Longitudinal, lateral, and vertical accelerometers were located under the pilot's seat, and an additional vertical accelerometer was positioned near the center of gravity. Control positions were measured at the pilot's stick.

The aircraft instrumentation system was not intended to gather data for frequency response analyses. For example, the accelerometers were not located at the cg, and the position of the cg was not accurately known. Different analog filters and sample rates (from 75 to 450 Hz) were used on different measurements. And linear velocities were not measured. Data processing to account for some of the shortcomings of the data required considerable effort: data were filtered and decimated or expanded to create a common sample rate, linear accelerations were referred to the estimated cg position, and linear velocity time derivatives were reconstructed from the other measurements. And although these corrections ultimately yielded a useful database, better results could have been obtained with less effort if the instrumentation setup had followed the simple rules-of-thumb described above.

# Test Inputs

The set of test inputs needed for this type of analysis consists of pilot induced frequency sweeps, and doublets or pulses. The sweeps are used to generate the frequency response database, and the doublets and pulses are used for time domain verification of resulting models. The basic pilot technique used in the frequency sweep is to produce a sinusoidal input about a reference trim condition, beginning at very low frequency and progressively increasing the frequency of inputs.

Generally, a frequency range of $0.1\mathrm{Hz}$ (10 sec period) to $2\mathrm{Hz}$ is adequate for handling qualities analyses. The frequency sweeps in these tests were conducted using small amplitude inputs starting with a period of about 16 seconds and progressing to a desired frequency of $2 - 3\mathrm{Hz}$ . Input and response data should be recorded over at least a 90-second period (minimum to maximum frequency). A minimum of two (ideally three) frequency sweeps per axis should be recorded for data reduction. Maintaining the trim condition for each axis throughout each maneuver is essential to eliminate errors. Control input size should be as small as possible with the pilot perceiving continuous control movement, but large enough to get an airframe response at low and mid frequencies (generally +/- 1/2 inch control deflection is a maximum). Intermittent, uncorrelated off-axis inputs are allowable as required to counter large excursions due to control coupling effects. An example of a lateral axis frequency sweep is presented in Figure 3.

图片摘要：该图主要展示 3 Lateral stick frequency sweep, hover。
![](images/5acef48c862d05a618822f64f266fda4f1dcc3a9523dd4f3110ca3a033468e43.jpg)

图片摘要：该图主要展示 3 Lateral stick frequency sweep, hover。
![](images/e5e24279fcaf1980159f5496aa6c5a7cd161067597e6364917fe7f502606e796.jpg)  
Fig. 3 Lateral stick frequency sweep, hover

# Safety Considerations

Although the technique is straightforward, experience with frequency response testing during the AH-64A and OH-58D tests emphasizes the need to carefully plan the frequency sweep tests. Tests conducted with frequency sweeps revealed the potential for damage caused by structural resonances. Some of these are documented by AQTD in reference 2. Unexpected structural resonances which were not identified during structural demonstrations or during operational flying have been

encountered during frequency sweep tests. The lesson is frequency response testing should be approached cautiously.

There are some methods that can be used to minimize the risks from frequency response testing. One is to limit the range of the frequency sweep to a pre-determined value. Guidance from Tischler (Ref. 3) suggests testing a frequency range from $1/2$ the bandwidth frequency to $2\omega_{180}$ . Unfortunately, no bandwidth data is available prior to conducting testing. Therefore, the tester must make an educated guess at the neutral stability frequency. Ideally, one would like to start at a very low frequency, and build up to a frequency high enough to make the bandwidth and phase delay computations. The low frequency range is the most difficult to acquire data with adequate coherence, due to the small control inputs required to minimize translation during the low frequency portion of the sweep. To reduce the risk of damage and save flight test time, it is suggested that one sweep be performed in each axis to more closely identify the range of frequencies actually required to accurately determine the bandwidth. An initial limit of $1.5\mathrm{Hz}$ should be used. Once a more accurate estimation of the bandwidth has been attained, the frequency sweep can be repeated over a more restricted (or expanded, if needed) frequency range. The object of this method is to avoid the higher frequencies, thus reducing the likelihood of driving other aircraft components into a damaging resonance. The technique will also reduce the number of asymmetrical and off-axis inputs required by the pilot to restrict translations started during the low frequency portions. Another method that will help minimize risk is to restrict the input magnitude. The size of the input should be kept to a minimum, which will reduce cyclic loads imposed upon the airframe.

Training the pilot and the engineer is another important ingredient to a successful frequency sweep test. The input magnitude and frequency ranges must be thoroughly understood prior to flight. The pilot has a tendency to increase the magnitude of the inputs at higher frequencies, to compensate for a reduction in aircraft response. Using a fixture may help to relieve this tendency, but so will adequate ground training. The pilot should be coached by the engineer both for input timing and input magnitude. This pilot-engineer interface should be practiced on the ground. Realtime monitoring of the stick inputs is valuable for this task. Once the engineer determines that the inputs have met this frequency, he should make the "knock-it-off" call to the pilot. At frequencies above $1\mathrm{Hz}$ , it is difficult for the pilot to accurately estimate the input frequency. Experience has shown that pilots are capable of generating input frequencies in the range of $5 - 6\mathrm{Hz}$ (30-40 rad/sec) which may excite rotor modes. As a general rule, it appears that handling qualities frequency tests can be terminated at $2\mathrm{Hz}$ , and sufficient information will be available for

handling qualities analyses. A combination of establishing a pre-determined cutoff frequency, realtime input monitoring, limiting the magnitude of the inputs, and pilot-engineer ground training makes the test technique safe and efficient.

# Generation of the Frequency Response Database

# General

Generation of the frequency response database is the starting point for any of the analyses shown in figure 1. The overall goal is to extract a complete set of nonparametric input-to-output (pilot control-to-vehicle response) frequency responses that fully characterize the behavior of the helicopter.

# CIFER Overview

The US Army/NASA and Sterling Software have jointly developed an integrated software facility (CIFER) for system identification based on a comprehensive frequency-response approach that is uniquely suited to the difficult rotorcraft problem. This program provides a set of utilities that reduce the frequency sweep time histories into high quality multi-input/multi-output frequency responses. A full description of the CIFER software is provided in reference 4. Essentially, three steps are used to generate the frequency response database. The first step is to produce the single-input/single-output (SISO) frequency response from the time histories using an advanced Fast Fourier Transform. An example of the autospectrum and Bode plots generated from this step are presented in Figure 4 for the roll axis. The input autospectrum shows good excitation up to 21 rad/sec (3.3 Hz).

The second step is to condition the responses to account for the effect of secondary inputs. These conditioned multi-input/single-output (MISO) responses are the same as the SISO frequency responses that would have been obtained had no correlated controls been present during the frequency sweep of a single control. A further detailed description of this conditioning process is presented in reference 6. Figure 5 shows how results are affected by the presence of secondary inputs, especially for off-axis identification.

Step three is to combine multiple window lengths into a composite response. A further detailed description of this composite process is presented in reference 4. The overall result of these three steps (CIFER programs -FRESPID, MISOSA, and COMPOSITE) is the rapid identification of a set of broadband frequency responses for all input/output pairs for which there is dynamic excitation. This set of composite conditioned frequency responses and associated coherence functions forms the

core of the frequency response database. An example of the final response is shown in Figure 6.

图片摘要：该图主要展示 4 Roll axis SISO frequency response。
![](images/75423c1880c9c56f00d9b3ab22a35fcfeb1039f92f4f736eb14e122cb154e17b.jpg)

图片摘要：该图主要展示 4 Roll axis SISO frequency response。
![](images/777e4ebd28de8a0fe18afc7cd10e29f223cec90aa6a2d9ca569d043412456509.jpg)

图片摘要：该图主要展示 4 Roll axis SISO frequency response。
![](images/e6f91b97952eba7f411a5e477eeefea4366476ddb78417347429bdd2eb97f04e.jpg)

图片摘要：该图片与Fig. 4 Roll axis SISO frequency response；Original unconditioned response Conditi这部分内容相关。
![](images/69458394fe21bb5275cf8d853043c4f45dc36407601aeab10627d37178b65338.jpg)  
Fig. 4 Roll axis SISO frequency response

图片摘要：该图主要展示 4 Roll axis SISO frequency responseOriginal unconditioned re。
![](images/2304577d8db9b5fd490cbb26b288ec076613d0a9674d2544a3907f74d4ffd7c8.jpg)

图片摘要：该图主要展示 4 Roll axis SISO frequency responseOriginal unconditioned re。
![](images/6690e9a90cf8b10ed54fc2633df10192516c560ab2b7610fd4716cb558828877.jpg)  
Original unconditioned response Conditioned response

图片摘要：该图主要展示 4 Roll axis SISO frequency response。
![](images/0a667e822f3f294c380e39eec7337ff227908695b277830ab5a6926e153d264d.jpg)

图片摘要：该图片与Fig. 5 Conditioned response, q/δlat；Fig. 6 Final composite response,这部分内容相关。
![](images/38714cf8340379f65dcef8531f4c0ff8b2232d43076fa34a0c87ae63f2488cbd.jpg)

图片摘要：该图片与Fig. 5 Conditioned response, q/δlat；Fig. 6 Final composite response,这部分内容相关。
![](images/d96a127f4e4b63c817d13f76e149773c753f34ed8046266d39ba9ed6738ce1ae.jpg)  
Fig. 5 Conditioned response, q/δlat   
Fig. 6 Final composite response, $\mathbf{p} / \delta \mathrm{lat}$

# Applications

# ADS33C Specification Compliance

The requirements for response to small amplitude inputs are specified in ADS-33C (Ref. 8) using two frequency domain parameters, bandwidth and phase delay. The bandwidth parameter is the end to end, pilot control input to airframe angular response closed loop frequency that assures at least a 6 db gain margin, and a 45 degree phase margin from the neutral stability frequency. Essentially, it is a measure of the "quickness" with which the aircraft can respond to an input. Since any input can be modeled as a series of sine (or cosine) waves of differing frequencies and magnitudes, using Fourier analysis, the bandwidth defines the highest input frequency that results in a usable response both in magnitude and phase. The criterion in ADS-33C is based on the premise that ... the maximum frequency that a pure

gain pilot can achieve, without threatening stability, is a valid figure-of-merit ... (Ref. 9). An aircraft with a high bandwidth would nearly mirror the input, and would be described as sharp, quick, crisp, or agile. A low bandwidth aircraft would be more sluggish, with a smooth response. Typical high gain tasks that would be most affected by bandwidth include slope landings, precision hover over a moving platform, air-to-air and air-to-ground target tracking, and running landings.

The phase delay parameter is effectively a measure of the steepness of the slope of the phase plot at the point where the output lags the input by 180 degrees (neutral stability). As the pilot increases his gain in a task, he approaches the frequency where the aircraft responds out of phase with the input. The natural pilot reaction is to apply a "mental lead filter" to compensate for this phase

shift. The success of this technique depends in large part on the predictability of the response. If the phase slope near the -180 degrees point is shallow, minor control deviations in the vicinity of this frequency will not change the phase shift significantly resulting in predictability. However, if the slope is too steep, minor changes in frequency will cause major changes in the phase shift, causing the "mental lead filter" to be less effective, or less predictable. An aircraft with a large phase delay is prone to Pilot Induced Oscillations, or PIOs. Phase delay is calculated based on either a two point fit, or a least-squares fit of the phase data between the neutral stability frequency and the phase at twice the neutral stability frequency. This assumes of course, that reliable data is available in this region, which may be a source of potential problems.

The bandwidth and phase delay are measured from a frequency response plot of the angular attitude response to cockpit controller deflection or force. CIFER applies the simple 1/s correction to the angular rate frequency responses to obtain the attitude to stick deflection frequency response. Phase margin and gain margin bandwidths are directly calculated, and the phase delay is calculated using either a two point fit, or a least squares fit algorithm, as shown in Figure 7. The least squares fit in CIFER uses an exponential coherence weighting function to place more emphasis on the higher quality spectral data present in the frequency response.

图片摘要：该图主要展示 7 ADS 33C phase delay calculation with least squares fit (p/。
![](images/b695ba78c20d8f6fecf741659508d41b9e48b531b1f0ab5113dab14d3e09061f.jpg)  
Fig. 7 ADS-33C phase delay calculation with least squares fit (p/dlat)

The resulting bandwidth and phase delay are then plotted against specification boundaries detailed in ADS-33C for Levels 1, 2, and 3. As an example, the roll axis results plotted in Figure 8 predict Level 2 handling qualities in the hover roll axis using the ADS-33C small amplitude criteria for the Target Acquisition and Tracking Mission Task Elements (MTEs). A review of earlier evaluations indicate that the aircraft possesses generally Level 2 handling qualities (Ref. 10). Right and left slope landings, a very high gain task, were rated HQRS 4 and 5 (Level 2) in the lateral axis. A pilot induced oscillation (PIO) in roll was documented at a hover in these two evaluations. The PIO disappeared when the pilot gained experience in the aircraft. A PIO significantly degrades handling qualities, and has been related to gain margin limited systems. Target Acquisition and Tracking MTEs were not performed during these tests. As can be seen, the predicted handling qualities trends from the frequency response criteria do compare with the actual handling qualities obtained in flight test.

图片摘要：该图主要展示 7 ADS 33C phase delay calculation with least squares fit (p/。
![](images/14f4ae1414b2027dfc30600f80b5b17f4be850c50f5bc002e43dc317729391d6.jpg)  
Target Acquisition and Tracking and Air Combat MTEs   
Fig. 8 ADS-33C Small amplitude roll criteria

# Spectral Analysis of Helicopter Vibration

Helicopter vibration levels are routinely measured in flight test programs to determine compliance with specifications and to document in-flight vibration characteristics. The analysis associated with determining vibration levels is virtually identical to that of generating frequency responses; the CIFER software is therefore capable of performing all the functions required for a

vibration analysis. This section presents the results of such a vibration analysis for the OH-58D helicopter.

A vertical accelerometer was mounted under the pilot's seat on the test aircraft to measure vibration levels experienced by the pilot. The distribution of vertical vibration level with frequency is indicated by the power spectral density of the vertical acceleration time history. Between two frequencies, the area under this curve is proportional to the mean square value of vertical acceleration in this frequency range. Figure 9 shows the power spectral density of the pilot's seat vertical acceleration for the OH-58D in a hover. The data used to generate this plot was taken from the trim portions of several maneuvers. Vibration peaks are evident at frequencies corresponding to 1/rev, 2/rev, 4/rev, and 8/rev. Vertical vibration levels at each of these frequencies were determined by the CIFER software by calculating the area under each peak. The total vibration level was also calculated by integrating under the curve from 5 to $60\mathrm{Hz}$ . The results are presented in Table 2.

图片摘要：该图主要展示 9 Power spectral density, vertical vibration。
![](images/c26de57c4350f2a14f090df8861b8cd76536d1f34bc7cddab99085f57e529b4e.jpg)  
Fig. 9 Power spectral density, vertical vibration

Table 2. OH-58D Vertical Vibration Levels in a Hover   

<table><tr><td>Vibration Mode</td><td>Frequency (Hz)</td><td>RMS of Vertical Acceleration (g&#x27;s)</td></tr><tr><td>1/rev</td><td>6.5</td><td>.006</td></tr><tr><td>2/rev</td><td>13.1</td><td>.003</td></tr><tr><td>4/rev</td><td>26.1</td><td>.018</td></tr><tr><td>8/rev</td><td>52.2</td><td>.006</td></tr><tr><td>Total</td><td>5 to 60</td><td>.032</td></tr></table>

The peak amplitude of the acceleration is typically two to three times the root-mean-square value of the vertical acceleration. The maximum vibratory acceleration the pilot feels at the 4/rev frequency, for example, is therefore

about 0.045 g's. The military handling qualities specification MIL-H-8501A requires vibrations levels lower than .15 g's for frequencies less than $32\mathrm{Hz}$ .

# Transfer Function Modeling

Transfer-function modeling is a rapid and useful tool for characterizing the helicopter responses when the overall input-to-output behavior is of concern, rather than a complete physical representation based on the force and moment equations. In CIFER, transfer-functions are extracted directly by minimizing the magnitude and phase errors between the identified frequency-responses and the model. CIFER adjusts the transfer-function model parameters until a best fit is achieved. These transfer-function models are often referred to as "equivalent system" representations since they characterize the dominant dynamics in terms of simple "equivalent" first and second order responses. Examples of the applicability of transfer-function models are:

- flight mechanics studies - determination of key rotor parameters, and coupled rotor/fuselage modes   
- handling-qualities analysis - comparison of equivalent system parameters such as short period damping and frequency, and time delay with the handling-qualities data base   
- flight control system design model - classical design and analysis techniques such as Bode and Root Locus are based on the transfer-function descriptions of the on-axis angular responses to control inputs   
- structural and rotor elasticity - damping and frequency of rotor lead-lag and airframe structure modes

Detailed examples of these applications are found in reference 11 for the BO-105, Puma, and AH-64A helicopters. In the following sections, the OH-58D data base is exercised to yield transfer-function models for the flight mechanics and handling-qualities applications.

# Roll Response Modeling

An equivalent system model of the roll rate response to lateral stick input of Figure 6 was desired for flight mechanics analysis purposes. The frequency range of interest was selected as 1-16 rad/sec, which encompasses the dominant coupled fuselage/rotor flapping response. At present we choose to cut off the fit at 16 rad/sec to exclude the lead-lag dynamics prominent for higher frequencies as seen in Figure 6.

Two models of the roll-response were evaluated. In the simplest model, the response dynamics are characterized as first-order leading to the "quasi-steady" formulation in which the rotor and residual (mechanical and other higher-order) dynamics are represented by a pure time delay $(\tau_{\mathrm{lat}})$ , and the coupled fuselage/rotor

dynamics are represented by the roll gain $(\mathbf{L}_{\delta \mathrm{lat}})$ , and the first order roll damping $(\mathbf{L}_{\mathbf{p}})$ :

$$
\frac {p}{\delta_ {\mathrm {l a t}}} = \frac {L _ {\delta_ {\mathrm {l a t}}} e ^ {- \tau_ {\mathrm {l a t}} s}}{s - L _ {p}} \tag {1}
$$

The parameters obtained for this model are listed in Table 3 and result in the rather poor frequency-response fit shown in Figure 10. The large cost function (CF=126) indicates that the model does not satisfactorily characterize the response. Also, the parameters in the table are very sensitive to the exact fitting range of the fit, a further indication of the inadequacy of the quasi-steady formulation for this helicopter. The same limitations for the quasi-steady model were found for the BO-105

图片摘要：该图主要展示 10 Equivalent system model of。
![](images/ea09e983efba10ff40629346c62b528e569da6aab2aecd5d9f871b359fe27718.jpg)

图片摘要：该图主要展示 10 Equivalent system model of。
![](images/d5e2f43cb01e7f25f857f676c724fb0cb38790d7aa18112f9e46e361cd1cc0fb.jpg)

图片摘要：该图片与Fig. 10 Equivalent system model of；As discussed by Heffley (Ref. 12), the roll r这部分内容相关。
![](images/afcbfd191e1583e3a50fce54b51367de4ebc443dfe648c2952657bebbb604113.jpg)

图片摘要：该图片与Fig. 10 Equivalent system model of；As discussed by Heffley (Ref. 12), the roll r这部分内容相关。
![](images/db282597b1c666e4aa64c7eef2db481fbb1cd34d197cd3e3dcf376049bb0611a.jpg)  
Fig. 10 Equivalent system model of $\mathbf{p} / \delta \mathrm{lat}$

As discussed by Heffley (Ref. 12), the roll response in the frequency range of interest is essentially second-order, owing to the coupling of the rotor regressive flapping and fuselage roll modes. A simple model involving the rotor flap inverse time-constant $(1 / \tau_{\mathrm{f}})$ , the total flapping stiffness $(\mathsf{L}_{\mathsf{b1s}})$ , the lateral stick gearing $(\mathsf{K}_{\mathsf{slat}})$ , and the residual time delay $(\tau_{\mathrm{lat}})$ :

$$
\frac {p}{\delta_ {\mathrm {l a t}}} = \frac {K _ {\delta_ {\mathrm {l a t}}} e ^ {- \tau_ {\mathrm {l a t}} s}}{s ^ {2} + (1 / \tau_ {\mathrm {f}}) s + L _ {\mathrm {b l s}}} \tag {2}
$$

The resulting model listed in Table 3 matches the frequency-response data quite well (cost function $=21$ ) as seen in Figure 10. Also the model parameters are not sensitive to the exact fitting range. The high level of rotor fuselage coupling is evident from reference to the second order poles $[\zeta=0.42$ and $\omega_{\mathrm{n}}=7.4]$ , clearly showing why the quasi-steady approximation is not appropriate for this response.

Heffley (Ref. 12) tabulates the rotor parameters of eqn 2 for a broad range of helicopters. The report lists an OH-58 "D" model which includes the mast mounted sight (MMS), but the data of reference 13 used in Heffley's analysis excludes the MMS. The main differences are do the change in inertias and center of gravity (cg) associated with the MMS for the "D" model. In hover, the inflow effects on the flapping time constant are significant, and can be accounted for by making a correction to the Lock number $\gamma$ as described by Harding (Ref. 14). Applying this correction to the OH-58D reduces the Lock number from the theoretical value of $\gamma = 7.06$ to an effective value of $\gamma_{\mathrm{eff}} = 5.33$ . The resulting rotor flap time constant prediction based on Heffley's analysis is $\tau_{\mathrm{f}} = 0.131$ sec, which is quite close to the identified value of $\tau_{\mathrm{f}} = 0.155$ sec. The flapping stiffness for the OH-58D is determined by Heffley from simulation data as $L_{b1s} = 47.7$ , which is also quite close to the identified value. The small identified residual time delay ( $\tau_{\mathrm{lat}} = 0.051$ sec) reflects the sensor filtering, hydraulic actuator and linkage dynamics between the stick measurement and the swashplate motion, and additional unmodeled rotor dynamics (e.g., lead-lag motion).

The maximum achievable roll rate can be assessed from the steady state response per unit input and the full throw control authority by noting from reference 12 that the roll rate response is to stick inputs is highly linear:

$$
p _ {\max } = \left(\frac {p}{\delta_ {\text {l a t}}}\right) _ {s s} \left(\delta_ {\text {l a t}}\right) _ {\max } \tag {3}
$$

$$
\begin{array}{l} = \frac {K _ {\delta_ {\mathrm {l a t}}}}{L _ {\mathrm {b l s}}} \left(\delta_ {\mathrm {l a t}}\right) _ {\max } \\ = (0.01785 \mathrm{rad} / \mathrm{sec} / \%) (\pm 50 \%) \\ = 0. 8 7 5 \mathrm {r a d} / \sec \\ = \pm 5 0 \mathrm {d e g} / \sec \\ \end{array}
$$

which meets ADS-33 Level 1 roll rate requirements for limited and aggressive maneuvering.

A final parameter of interest is the effective first-order inverse time-constant $1 / \mathrm{T_{eff}}$ , where:

$$
T _ {\text {e f f}} = \frac {2 \zeta}{\omega_ {n}} = 0. 1 1 6 3 \sec \tag {4}
$$

so

$$
1 / T _ {\text {e f f}} = 8. 6 \text {r a d} / \sec \tag {5}
$$

As expected, this value is comparable with the first-order quasi-steady model parameter $(\mathbf{L_p})$ shown in Table 3, and indicates a rather rapid roll rate command response for the OH-58D. A somewhat lower simulation value of $1 / T_{\mathrm{eff}} = 6.25$ rad/sec is obtained based on Heffley's rotor parameters.

Table 3 Transfer Function Models for $p/\delta$ lat   

<table><tr><td>Model Structure</td><td>Transfer Function</td><td>Cost</td></tr><tr><td>Quasi-steady</td><td>p/δlat=0.184 e-0.155s/s+9.27</td><td>125.6</td></tr><tr><td>Coupled body/rotor flapping</td><td>p/δlat=0.988 e-0.051s/s2+(1/0.155)s+55.35</td><td>21.4</td></tr></table>

# Heave Axis Modeling

Transfer function modeling was also used to investigate the helicopter vertical speed response due to collective control inputs. Previous work has shown that inflow dynamics significantly affect the vertical response in hovering flight, and are primarily responsible for determining the pilot's perception of the aircraft's "crispness" during vertical maneuvers (Ref. 15). Figure 11 (solid line) shows the frequency response of the vertical acceleration due to collective control; the increasing magnitude with frequency is caused by inflow effects. The physical mechanism that creates this peak in the magnitude plot is the dynamic response of the inflow velocity. Because the air has mass, the inflow velocity does not assume a new steady value instantaneously after an abrupt collective pitch change. This dynamic lag of the inflow velocity influences the angle of attack of the

rotor blades such that the blades experience their largest angle of attack immediately after an abrupt collective pitch increase, and a decreasing angle of attack as the inflow velocity increases. The result is a large rotor thrust spike after a rapid collective pitch change, which causes the high-frequency peak in the magnitude plot. This phenomenon is also responsible for much of the vertical acceleration cues the pilot feels while making abrupt collective inputs in a hover, and is therefore necessary to include in simulation models to capture the "crispness" of the actual helicopter.

图片摘要：该图主要展示 11 Heave Axis Response。
![](images/7910e6c021a32810b2e8ab9d6b4db45431ec048b81c8a7d0e35cbdbf0935cd8e.jpg)  
Fig. 11 Heave Axis Response

Two transfer function models were used to approximate the vertical axis response to collective stick.

The first model is a first-order description of vertical velocity to collective which neglects inflow dynamics:

$$
\frac {a _ {z}}{\delta_ {\mathrm {c o l l}}} = \mathrm {s} \frac {Z _ {\delta_ {\mathrm {c o l l}}}}{(s - Z _ {w})} \tag {6}
$$

Figure 11 (dashed line) illustrates that this model fits the vertical frequency response poorly. In particular, the model cannot follow the increasing magnitude with frequency that the frequency response exhibits.

The second model includes terms to model the inflow. The influence of dynamic inflow is approximated in the transfer function through the addition of a zero and a time delay to the first-order model of vertical velocity to collective stick:

$$
\frac {a _ {z}}{\delta_ {\mathrm {c o l l}}} = s \frac {Z _ {\delta_ {\mathrm {c o l l}}} (s - Z _ {\mathrm {L}}) e ^ {- \tau_ {\mathrm {c o l l}} s}}{(s - Z _ {\mathrm {w}})} \tag {7}
$$

where the coefficient values are $Z_{\mathbf{w}} = -.413$ , $Z_{\mathbf{coll}} = -0.071$ , $Z_{\mathbf{L}} = -9.25$ , and $\tau_{\mathbf{coll}} = .0785$ . Figure 11 compares this transfer function to the actual frequency response and to the first model. The match is significantly better than that of the model which neglects inflow dynamics, illustrating the importance of including these effects in handling qualities models.

Single-input-single-output transfer function modeling, as illustrated in the preceding two examples, can reveal a great deal about the behavior of the helicopter. Quite often the physical mechanisms influencing the helicopter behavior are evident in this simple analysis--a benefit more complicated modeling approaches usually cannot offer. This makes transfer function modeling ideal for many common flight test and handling qualities analyses not considered here. For example, the effects of changing the external configuration of an aircraft, either by the addition of new components (antennae, wing stores, etc.) or modification of existing parts, are often assessed in flight test. Low-order transfer function models can quickly reveal and quantify aircraft behavior changes, most simply in terms of damping ratios and natural frequencies obtained from the transfer function coefficients.

# Handling Qualities Model Identification

State-space modeling provides a comprehensive characterization of the coupled helicopter dynamics in terms of linear differential equations of motion. The coefficients of these equations are the fundamental force and moment perturbation (stability and control) derivatives of classical aircraft flight mechanics. Statespace models are useful for control system design, simulation model fidelity assessment and improvement,

comparison of wind tunnel and flight characteristics, and multi-input/multi-output (MIMO) handling-qualities analysis. CIFER identifies state-space models of general structure and of high-order by simultaneously fitting the entire frequency-frequency data base.

The goal of the state-space modeling effort in this paper is to characterize the MIMO rotor-flapping/body dynamics of the OH-58D helicopter. The frequency range of concern is for pilot-in-the-loop handling qualities (0.5-15 rad/sec), as assumed by Heffley (Ref. 12). The larger goal is to develop a general approach for identification of rotorcraft handling-qualities models that can be routinely applied to future test programs. Such a model must be sufficient to capture the important dynamic modes and key coupling, without being overly complex and thus requiring an unacceptable level of labor or computer effort for the analysis.

# Model Structure

A key aspect in the identification of a state-space model is the choice of model structure. Model structure refers to the form and order of the differential equations to be identified by CIFER. The earlier transfer-function modeling results described earlier show the angular responses of the OH-58D helicopter are dominated by the 2nd-order coupled fuselage/regressive-rotor dynamics. This modeling approach is generalized in the state-space formulation by expressing the lateral and longitudinal regressive flapping responses as first order differential equations. This approach follows Heffley's "primary analysis model" for handling-qualities analysis (Ref. 12) and is developed further into the "hybrid model" formulation of reference 4. The decoupled lateral regressive-flapping response $(\mathbf{b}_{1S})$ is expressed as:

$$
\tau_ {f} \dot {b} _ {1 s} = - b _ {1 s} - \tau_ {f} p + K _ {b 1 s} \delta_ {l a t} (t - \tau_ {\delta_ {l a t}}) \tag {8}
$$

where $\tau_{\mathbf{f}}$ is the rotor flap time constant as in eqn (2) and $\mathbf{K}_{\mathbf{b1s}}$ is the stick gain.

The rotor is coupled to the fuselage through rotor flapping springs $\mathbf{L}_{\mathbf{b}_{1s}}$ and $\mathbf{Y}_{\mathbf{b}_{1s}}$

$$
\begin{array}{l} \dot {\mathbf {p}} = \mathrm {L} _ {\mathrm {b l s}} \mathbf {b} _ {\mathrm {l s}} + \mathrm {L} _ {\mathrm {q}} \mathbf {q} + \mathrm {L} _ {\mathrm {r}} \mathbf {r} + \mathrm {L} _ {\mathrm {u}} \mathbf {u} + \dots \\ + \mathrm {L} _ {\delta_ {\text {i o n}}} \delta_ {\text {i o n}} + \mathrm {L} _ {\delta_ {\text {p e d}}} \delta_ {\text {p e d}} + \mathrm {L} _ {\delta_ {\text {c o l}}} \delta_ {\text {c o l}} \tag {9} \\ \end{array}
$$

$$
\begin{array}{l} \dot {\mathbf {v}} = \mathbf {Y} _ {\mathrm {b l s}} \mathbf {b} _ {\mathrm {l s}} + \mathbf {Y} _ {\mathrm {p}} \mathbf {p} + \mathbf {Y} _ {\mathrm {q}} \mathbf {q} + \mathbf {Y} _ {\mathrm {r}} \mathbf {r} + \mathbf {Y} _ {\mathrm {u}} \mathbf {u} + \\ \dots + \mathrm {Y} _ {\delta_ {\text {i o n}}} \delta_ {\text {i o n}} + \mathrm {Y} _ {\delta_ {\text {p e d}}} \delta_ {\text {p e d}} + \mathrm {Y} _ {\delta_ {\text {c o l}}} \delta_ {\text {c o l}} \tag {10} \\ \end{array}
$$

where it is important to remember that $\mathbf{L}_{\mathfrak{p}}$ $\mathbf{M_q}$ Lslat, Mlon, Yslat, and Xslon are omitted since their effects are associated with the steady-state rotor flapping response. The $\Upsilon_{\mathfrak{p}}$ term is retained to correct for errors in

the assumption of the vertical cg location. The same form of the equations is used for the decoupled longitudinal regressive flapping (a1s), pitch rate (q), and axial velocity (u) responses. The rotor flapping time constant $(\tau_{f})$ is constrained to be equal in the pitch and roll equations, as predicted by theory for hovering flight. Harding (Ref. 14) adopts a coupled rotor flapping formulation and eliminates the quasi-steady coupling derivatives, which was found to produce a slightly less accurate model in the current study.

The model was further simplified by assuming a diagonal form of the force-speed derivatives and force-control derivatives; i.e.,

$$
X _ {v} = X _ {w} = Y _ {u} = Y _ {w} = Z _ {u} = Z _ {v} = 0 \tag {11}
$$

$$
X _ {\delta \text {l a t}} = X _ {\delta \text {p e d}} = X _ {\delta \text {c o l}} = Y _ {\delta \text {l o n}} =
$$

$$
Y _ {\delta \text {c o l}} = Z _ {\delta \text {l a t}} = Z _ {\delta \text {l o n}} = Z _ {\delta \text {p e d}} = 0 \tag {12}
$$

The low frequency speed derivatives $\mathbf{X}\mathbf{u}$ and Yv were fixed at their OH-58D simulation values (Ref. 13), because their effects are not significant to the dynamic response in the frequency range of interest and could therefore not be identified. The vertical response is essentially decoupled from the other degrees-of-freedom and is modeled as in eqn (7) to include the heave damping Zw, the inflow lead $Z_{\mathrm{L}}$ , the control derivative Zδcol and a time delay τc1. Finally, time delays were included as a time shift on each of the angular controls. In the vertical axis, a second time delay τc2 was applied to the angular response to collective (r/δcol) which accounts for the torque response time constant (about 0.25 sec). More sophisticated models can be developed that include the complete engine/rpm engine dynamics (Ref. 15), and the coupled flap-inflow dynamics (Ref. 14).

# Model Identification Using CIFER

The hybrid model structure discussed above was identified using CIFER. After convergence was achieved with the initial fully populated model, an accuracy analysis was completed to determine which parameters are insensitive or highly correlated and should be removed from the model (Ref. 4). These unimportant derivatives are sequentially eliminated and the model is reconverted and re-analyzed for accuracy at each step. The final model parameters are listed in Table 4 together with their Insensitivities and Cramer-Rao bounds. Target Insensitivities and Cramer-Rao bounds are for the most part within their target limits (10% and 20% respectively), indicating that a good final model structure has now been achieved. A comparison of the frequency domain model results with selected flight test results is presented in Figure 12, which shows excellent agreement, including the off-axes responses.

The entire system identification and analysis procedure using CIFER required about 3 man-weeks of effort. All calculations were completed on a VAX 8650 computer.

The model parameters of Table 4 convey important flight mechanics characteristics of the OH-58D helicopter. The rotor flapping spring $(\mathbf{L}_{\mathbf{b1s}})$ is within $4\%$ of the simple roll-response transfer function result of eqn (2). The rotor flapping time constant $(\tau_{f})$ , which for the state-space model is based on both pitch and roll responses, is $15\%$ larger than the previous roll-response transfer-function result. These results show overall that the addition of the coupling effects and lower-frequency quasi-steady parameters do not substantially alter the dominant 2nd order roll/flapping behavior predicted by simple transfer function methods.

The identified pitch and roll spring constants should be (physically) related to the inertia ratios:

$$
\mathrm {L b} _ {1 \mathrm {s}} / \mathrm {M a} _ {1 \mathrm {s}} = 5 3. 0 6 / 2 2. 0 5 = 2. 4 0 6 = \mathrm {I} _ {\mathrm {y y}} / \mathrm {I} _ {\mathrm {x x}} \tag {13}
$$

Bivens (Ref. 13) provides inertias for the OH-58D simulation model: $\mathrm{Iyy} / \mathrm{Ixx} = 2939.9 / 1208.4 = 2.43$ which is amazingly close to the identified value. The identified yaw damping is also quite close to the simulation value. The identified heave damping value $(Z_{\mathbf{W}})$ is nearly the same as the earlier transfer-function fit result of eqn (7), and very close to the simulation value of $Z_{\mathbf{W}} = -0.32$ . The inflow zero is identified as $Z_{\mathbf{L}} = -8.6$ rad/sec, which is also very close to the transfer function results in eqn (7).

The level of pitch-roll coupling is appreciated by comparison of the control and response coupling derivatives with the on-axis derivatives. The roll due-to-pitch response ratio is:

$$
\frac {\left| \mathrm {L} _ {\mathrm {q}} \right|}{\left| \left(\mathrm {L} _ {\mathrm {p}}\right) _ {\text {e f f}} \right|} = \frac {\left| \mathrm {L} _ {\mathrm {q}} \right|}{\left| 1 / \left(\tau_ {\mathrm {f}} \mathrm {L} _ {\mathrm {b 1 s}}\right) \right|} = \frac {2 . 1 6}{9 . 6 1} = 0. 2 3 \tag {14}
$$

while the pitch due-to-roll response coupling ratio is 0.26.

The coupling ratio for longitudinal control input is:

$$
\frac {\left| L _ {\delta_ {l o n}} \right|}{\left| \left(L _ {\delta_ {l a}}\right) _ {e f f} \right|} = \frac {\left| L _ {\delta_ {l o n}} \right|}{\left| \left(L _ {b 1 s} K _ {b 1 s}\right) \right|} = \frac {0 . 0 3 0}{0 . 1 6 6} = 0. 1 8 \tag {15}
$$

and 0.26 similarly for the lateral control input. These results indicate a pitch-roll interaxis coupling of about $25\%$ , which is about half of that of the BO-105 (Ref. 4),

图片摘要：该图片与and 0.26 similarly for the lateral control input. These results indicate a pitch这部分内容相关。
![](images/30e515e829992e288ab1acd2f6ff4f47aa23d6efed5fce2eb9d331e95cdc17f1.jpg)

图片摘要：该图片与and 0.26 similarly for the lateral control input. These results indicate a pitch这部分内容相关。
![](images/571682c69b9cffc15c74776e522bf7d26482001e0cd5aa062404b4d2aa559ccf.jpg)

图片摘要：该图片与and 0.26 similarly for the lateral control input. These results indicate a pitch这部分内容相关。
![](images/883ed89cbcdecfe7b24d438572091a8bafe9f429dceddd61342960297da1969b.jpg)

图片摘要：该图片与and 0.26 similarly for the lateral control input. These results indicate a pitch这部分内容相关。
![](images/d9cecb5a8af2bb8d79f5203d30f436d7bd47cb4179b8da8d47d5166e478348aa.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/9d62db0f1dd6cdb3dacc4fc1b041c9dffe2d83da649983e3c33902bcdb2d0b4d.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/547e6c962ef0424f32f887b0688efdf1e79487fdaf9d94cb57f22014c67693dc.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/0f7fe19eead61295f1ef857ce64ee1ce812167f63d10bc39b92bf041c64e0865.jpg)

图片摘要：该图主要展示 12 Model Results。
![](images/fd69a3f45b8453b8df8b63f3dd0aa902895ee81e57b2aa7bbabd4407d4fe763f.jpg)

图片摘要：该图主要展示 12 Model Results。
![](images/e8feca6c249539d5788392d52ad2611da4d8abde3c56f09d472c94951604ed8a.jpg)

图片摘要：该图主要展示 12 Model Results。
![](images/de60ea0ba6d2d33a55286580aa7e206f4d8047c22f06fdcff8e3a5ef428689e4.jpg)

图片摘要：该图主要展示 12 Model Results。
![](images/44f6c5f2fc2354bcb7592c125ae5551d4e81dc94d4836aa1748898bd4995981b.jpg)

Figure 12 Model Results   
图片摘要：该图主要展示 12 Model ResultsFlight data Identified model including flapp。
![](images/31bf0042dc207c980cab21bb65691d07a58000106e9175b6fb479266e6974d13.jpg)  
Flight data   
-Identified model including flapping and vertical inflow

<table><tr><td></td><td colspan="3">Identified model</td></tr><tr><td>Derivative</td><td>Param Value</td><td>C.R. (%)</td><td>Insens.(%)</td></tr><tr><td>Xu</td><td>-0.0140 †</td><td>......</td><td>......</td></tr><tr><td>Xv</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Xw</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Xp</td><td>4.751</td><td>13.03</td><td>4.149</td></tr><tr><td>Xq</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Xr</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>G</td><td>32.17 †</td><td>......</td><td>......</td></tr><tr><td>Xa1s</td><td>-55.53</td><td>6.696</td><td>1.984</td></tr><tr><td>Yu</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Yt</td><td>-0.03300 †</td><td>......</td><td>......</td></tr><tr><td>Yw</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Yp</td><td>1.569</td><td>18.03</td><td>6.575</td></tr><tr><td>Yq</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Yr</td><td>3.535</td><td>10.58</td><td>0.7944</td></tr><tr><td>G</td><td>32.17 †</td><td>......</td><td>......</td></tr><tr><td>Yb1s</td><td>127.8</td><td>4.412</td><td>0.7742</td></tr><tr><td>Zu</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zt</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zw</td><td>-0.3980</td><td>34.04</td><td>13.98</td></tr><tr><td>Zp</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zq</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zr</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Lu</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Lt</td><td>0.01636</td><td>20.75</td><td>3.744</td></tr><tr><td>Lw</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Lp</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Lq</td><td>-2.159</td><td>11.37</td><td>1.687</td></tr><tr><td>Lr</td><td>1.049</td><td>11.24</td><td>0.9681</td></tr><tr><td>Lb1s</td><td>53.06</td><td>4.350</td><td>0.6191</td></tr><tr><td>Mu</td><td>-9.662E-03</td><td>20.66</td><td>5.398</td></tr><tr><td>Mr</td><td>0.03279</td><td>11.86</td><td>2.498</td></tr><tr><td>Mw</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Mp</td><td>-1.032</td><td>9.622</td><td>1.604</td></tr><tr><td>Mq</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Mr</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Mals</td><td>22.05</td><td>5.208</td><td>1.185</td></tr><tr><td>Nu</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Nv</td><td>0.03547</td><td>15.89</td><td>3.144</td></tr><tr><td>Nw</td><td>-0.3780</td><td>32.45</td><td>11.60</td></tr><tr><td>Np</td><td>-0.6021</td><td>16.10</td><td>4.212</td></tr><tr><td>Nq</td><td>1.906</td><td>10.31</td><td>3.087</td></tr><tr><td>Nr</td><td>-0.5644</td><td>13.51</td><td>3.394</td></tr><tr><td>Kin1</td><td>1.000 †</td><td>......</td><td>......</td></tr><tr><td>Kin2</td><td>1.000 †</td><td>......</td><td>......</td></tr><tr><td>T1</td><td>-0.1806 *</td><td>......</td><td>......</td></tr><tr><td>T3</td><td>-0.1806 *</td><td>......</td><td>......</td></tr><tr><td>ZL</td><td>-8.60</td><td>14.6</td><td>2.3</td></tr></table>

<table><tr><td></td><td colspan="3">Identified Model</td></tr><tr><td>Derivative</td><td>Param Value</td><td>C.R. (%)</td><td>Insens.(%)</td></tr><tr><td>Xlon</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Xlat</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Xped</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Xcol</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Ylon</td><td>-0.1480</td><td>4.248</td><td>0.9466</td></tr><tr><td>Ylat</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Yped</td><td>-0.1191</td><td>5.096</td><td>2.073</td></tr><tr><td>Ycol</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zlon</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zlat</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zped</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Zcol</td><td>-0.07450</td><td>10.72</td><td>1.868</td></tr><tr><td>Lion</td><td>-0.03062</td><td>5.902</td><td>1.463</td></tr><tr><td>Lat</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Lped</td><td>0.01420</td><td>6.542</td><td>2.928</td></tr><tr><td>Lcol</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Mlon</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Mlat</td><td>0.01290</td><td>15.32</td><td>2.648</td></tr><tr><td>Mped</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Mcol</td><td>0.000 +</td><td>......</td><td>......</td></tr><tr><td>Nlon</td><td>-7.613E-03</td><td>21.71</td><td>8.117</td></tr><tr><td>Nlat</td><td>0.01823</td><td>9.564</td><td>2.754</td></tr><tr><td>Nped</td><td>0.05702</td><td>5.314</td><td>2.004</td></tr><tr><td>Ncol</td><td>0.03830</td><td>5.080</td><td>2.376</td></tr><tr><td>Kals</td><td>2.227E-03</td><td>6.157</td><td>1.059</td></tr><tr><td>Kb1s</td><td>3.123E-03</td><td>5.023</td><td>0.8559</td></tr><tr><td>τc1</td><td>0.08110</td><td>10.53</td><td>3.661</td></tr><tr><td>τc2</td><td>0.2660</td><td>4.191</td><td>1.729</td></tr><tr><td>τlong</td><td>0.03646</td><td>15.67</td><td>6.197</td></tr><tr><td>Tats</td><td>0.05956</td><td>9.163</td><td>3.632</td></tr><tr><td>τped</td><td>0.09027</td><td>5.346</td><td>2.518</td></tr></table>

Table 4 Model Results - OH58D Stability and Control Derivatives   

<table><tr><td></td><td colspan="3">Identified Model</td></tr><tr><td>Derivative</td><td>Param Value</td><td>C.R. (%)</td><td>Insens.(%)</td></tr><tr><td>Taur</td><td>0.1806</td><td>4.228</td><td>0.5924</td></tr><tr><td>T2</td><td>0.1806*</td><td>……</td><td>……</td></tr></table>

+ Eliminated during model structure determination   
Fixed value in model   
* Fixed derivative tied to a free derivative

but which is still quite significant from a handling-qualities point of view.

The longitudinal and lateral moment derivatives $(\mathbf{M}_{\mathbf{u}}$ and $\mathbf{L}_{\mathbf{v}})$ have small values, but are negative in sign -- opposite from first principles result. This problem reflects poor low frequency identification (e.g., for frequencies less than 0.5 rad/sec in the roll response of Figure 6) and suggests that these parameters may better be determined from the static calculation, given in the introduction, using the identified effective control moment derivatives of equations 14 and 15.

Finally, the eigenvalues of the model listed in Table 5 give the coupled natural modes of the OH-58D. The roll/flapping response $[\zeta = 0.407, \omega_{\mathrm{n}} = 7.17]$ matches the transfer-function result of eqn (2) as expected. The pitch/rotor-flap response is also coupled but at a lower frequency $[\zeta = 0.550, \omega_{\mathrm{n}} = 4.64]$ , but at a lower frequency due to the higher pitch inertia.

Table 5 OH-58D Hover Eigenvalues   

<table><tr><td>Mode</td><td>Real</td><td>Imag</td><td>ω rad/sec</td><td>ζ</td></tr><tr><td>Long Phugoid</td><td>0.242</td><td>0.0</td><td></td><td></td></tr><tr><td>Long Phugoid</td><td>-0.269</td><td>0.0</td><td></td><td></td></tr><tr><td>Lat velocity</td><td>0.433</td><td>0.0</td><td></td><td></td></tr><tr><td>Yaw/sway</td><td>-0.578</td><td>0.349</td><td>0.675</td><td>0.856</td></tr><tr><td>Heave Mode</td><td>-0.398</td><td>0.0</td><td></td><td></td></tr><tr><td>Roll/flapping</td><td>-2.916</td><td>6.550</td><td>7.17</td><td>0.407</td></tr><tr><td>Pitch/flapping</td><td>-2.554</td><td>3.877</td><td>4.64</td><td>0.550</td></tr></table>

# Model Verification in the Time-Domain

Comparison of the pulse responses for the identified hybrid model and the flight data are shown in Figure 13 for lateral stick and pedal inputs. Similar accuracy is achieved for longitudinal and collective inputs. The results show that key characteristics of the on- and off-axis responses are very well predicted, and the model is quite acceptable for handling-qualities characterization purposes.

# Full Simulation Quality Identification

The last, most complex application of the frequency domain database is the identification of a state space model that could be used for detailed analyses, with fidelity equivalent to a complete nonlinear model. The utility of such an identification includes simulation validation, piloted simulation, and detailed flight control design. Several researchers have documented the effectiveness of the frequency domain identification approach on the BO-105 (Ref. 4), the AH-64A (Refs. 14 and 15), and the UH-60A helicopters (Ref. 16). The data required from flight test is essentially the same, except

that more attention is placed on the test inputs to maximize data quality. An extended frequency range is usually needed to obtain information at higher frequencies where rotor dynamic effects become more prominent. Detailed angular and kinematic consistency analysis, measurement error modeling, state reconstruction, detection of bad data, calibration of control rigging, all need to be examined to ensure high quality frequency response data that has a high degree of confidence (Ref. 11). Further data that would improve results could include rotor measurements such as flapping and lead/lag angles. Additional states are usually added to account for higher order rotor and inflow dynamics, as well as engine and stick dynamics. Obviously, the level of effort increases from 3-4 manweeks to 3-4 manmonths, as well as the amount of time necessary to plan and conduct the flight test program needed to obtain the data. The payoffs, however can be significant, resulting from the high fidelity simulation quality models that are generated from this process.

# CONCLUSIONS

This paper has described the variety of handling qualities related information that can be derived from the frequency domain database generated from the relatively simple frequency sweep flight test technique. In many cases, substantially more information is available than the results produced from classical flight test techniques, which demonstrates the unique power of the frequency based approach over the classical time domain approaches. Research needs to continue in this area to determine further applications of the information available from the frequency doamin database. Some particular conclusions from this study are:

Non-parametric models are easily obtained from frequency sweep flight tests, and provide useful handling qualities information.

Simple parametric models are useful for characterizing the dominant vehicle characteristics using a few number of parameters.

An example of a simple parametric model of the OH-58D illustrates that frequency domain identification can reliably be used to support handling qualities studies.

Simple 1st order rigid body models are inadequate for even simple handling qualities models. A coupled fuselage/regressive flapping model must be used to characterize the vehicle response.

# RECOMMENDATIONS:

A technical note should be written for H-Q frequency domain testing.

图片摘要：该图片与A technical note should be written for H Q frequency domain testing；RECOMMENDATI这部分内容相关。
![](images/71cd7107f046935f916a7b2d350589521122481b07a1742184f90829432f19a5.jpg)

图片摘要：该图片与A technical note should be written for H Q frequency domain testing；RECOMMENDATI这部分内容相关。
![](images/d8f831ce7469777379c40d803b3b68d81323a75b1be2fa3b8622aa8e0a692c13.jpg)

图片摘要：该图片与A technical note should be written for H Q frequency domain testing；RECOMMENDATI这部分内容相关。
![](images/9b610d988137b6756993e0826bd0b6c8a57ef4e697c7de4ab6bedfa5afaea616.jpg)

图片摘要：该图片与A technical note should be written for H Q frequency domain testing这部分内容相关。
![](images/608cc73d955f8896584ac2c414351400dc07f0ed4cb3fc1685cff77f82851cb0.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/9e3077a0511d1c413a64c2ef571c86035edde8fdca685fc6724f74b228d326ee.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/9b5b984ef8149be943fb895a01b0286400782ddf7aa04f53e6fd175bad66c71e.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/ae33cf4907275ece3ae9ea2119ae6323ffae2eab5a3fdc65b8ebfa6c72f82b54.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/c288482132216338c686aee3d35b800f68be5d60a053d1f78703a292e3f4c0db.jpg)

图片摘要：该图片展示了FLIGHT TESTING AND FREQUENCY DOMAIN ANALYSIS FOR ROTORCRAFT HANDLING QUALITIES CHARACTERISTICS相关内容。
![](images/339b3f978377e0dcbbeec95e043472374a64628cee013674799ea4044a84b502.jpg)

图片摘要：该图主要展示 13 Time domain verification of model。
![](images/1b3e111a2d7536ca22806aed8457b4b270e8b57c28fc8658b883febc1d1242d5.jpg)

图片摘要：该图主要展示 13 Time domain verification of model。
![](images/2d3e23bcdf1854f28205b8e87bf24dd2b64ef0ccd7f976ad05c06db3c91ee544.jpg)

图片摘要：该图主要展示 13 Time domain verification of model。
![](images/66bdcaf28acb08466c859ca9d93791d17821cb4571d9618230bdf437f8ff433e.jpg)

图片摘要：该图主要展示 13 Time domain verification of model。
![](images/a5eb0dc6eaa4807041564dee44c469f7d84ca593549509bb241871887a20b7e8.jpg)

Fig. 13 Time-domain verification of model   
图片摘要：该图主要展示 13 Time domain verification of modelFlight data Identified m。
![](images/153c97afbf59ca82c97522e57dbe9ec0eb9b779bd6e2a77ed119bd16ad6a827d.jpg)  
Flight data   
Identified model including flapping and vertical inflow

Incorporate procedure in future airworthiness testing of new and modified aircraft.

Store FR database for future use and make available a compatible format for wide dissemination and further research.

# ACKNOWLEDGMENTS

The authors gratefully acknowledge the support, comments and contributions of David Key, AFDD; and Mavis Cauffman, Sterling Federal Systems.

# REFERENCES

1Brown, J.D., Stormer. W.H., Hopkins, G.J., and Nagata, J.L., "Airworthiness and Flight Characteristics Evaluation of the OH-58D Helicopter," USAAEFA Project No. 83-27-1, October 1990.   
2Ham, J.A., and Butler, C.P., "Flight Testing the Handling Qualities requirements of ADS-33C - Lessons Learned at ATTC," American Helicopter Society 47th Annual Forum, May 1991.   
3Tischler, M.B., et al., "Demonstration of Frequency-Sweep Testing Technique Using a Bell 214-ST Helicopter," NASA TM 89422, April 1987.   
4Tischler, M.B., Cauffman, M.G., "Frequency-Response Method for Rotorcraft System Identification: Flight Applications to BO-105 Coupled Rotor/Fuselage Dynamics," Journal of the American Helicopter Society, Vol 37, No 3, pgs 3-17, July 1992.   
5Tischler, M.B., Leung, J.G.M., and Dugan, D.C., "Frequency Domain Identification of XV-15 Tilt Rotor Aircraft Dynamics in Hovering Flight," AHS J. Vol.30(2), pp 38-48, April 1985.   
6Otnes, R.K., and Enochsen, L., Applied Time Series Analysis, John Wiley and Sons, Inc., New York, 1978, pp. 363-412.   
7Carter, C.G., et al., "Estimation of the Magnitude-Squared Coherence Function Via Overlapped Fast Fourier Transform Processing," IEEE Transaction on Audio and Electroacoustics, Vol. AU-21, (4), Aug 1973, pp. 337-344   
8Aeronautical Design Standard, "Handling Qualities Requirements for Military Rotorcraft," AVSCOM, ADS-33C, August 1989.   
9Hoh, R.H., et al., "Background Information and User's Guide for Handling Qualities Requirements for Military Rotorcraft," Technical Report No. 89-A-008, AVSCOM, December 1989.

10Ham, J.A., "Frequency Domain Flight Testing and Analysis of an OH-58D Helicopter," AHS J. Vol.37(4), pp 16-24, October 1992.   
11"Rotorcraft System Identification," AGARD AR 280, Sept. 1991.   
12Heffley, R.K., Bourne, S.M., Curtiss, H.C., Jr., Hindson, W.S., Hess, R.A., "Study of Helicopter Roll Control Effectiveness Criteria, NASA CR 177404, April 1986.   
13 Bivens, C.C., Guercio, J.G., "A Simulation Investigation of Scout/Attack helicopter Directional Control Requirements for Hover and Low-Speed Tasks, NASA TM 86755, March 1987.   
14 Harding, J.W., "Frequency-Domain Identification of Coupled Rotor/Body Models of an Advanced Attack Helicopter," AHS 48th Annual Forum, Washington, D.C., June 1992.   
15 Schroeder, Tischler, Watson, Eshow, "Identification and Simulation Evaluation of an AH-64 Helicopter Hover Math Model", AIAA Atmospheric Flight Mechanics Conference, Aug 12-14, 1991, New Orleans, Louisiana.   
16Ballin, M.G., Dalang-Sectretan, M.A., "Validation of the Dynamic Response of a Blade-Element UH-60 Simulation Model in Hovering Flight," American Helicopter Society 46th Annual Forum, May 1990.

图片摘要：该图片与16Ballin, M.G., Dalang Sectretan, M.A., "Validation of the Dynamic Response of a这部分内容相关。
![](images/5051a9c9828394c8eaae604e8625f199dea4425821dd2dee9fea9080cce08a35.jpg)
