# Motor Configuration Trade Study for a New Technical Challenge to Develop a 5 MW Cryogenic Motor and Drive

Justin J. Scheidler NASA Glenn Research Center Cleveland, USA justin.j.scheidler@nasa.gov

Thomas F. Tallerico NASA Glenn Research Center Cleveland, USA thomas.tallerico@nasa.gov

Aaron D. Anderson NASA Glenn Research Center Cleveland, USA aaron.d.anderson-1@nasa.gov

Peter E. Kascak NASA Glenn Research Center Cleveland, USA peter.e.kascak@nasa.gov

Abstract— A 6-year technical challenge was started in Fall 2024 to develop and demonstrate a 5 MW cryogenic motor system (motor, power electronics, and motor controller) for large transport aircraft. This paper presents the motivation, objectives, and scope of this project along with the requirements for the motor and the results to date of a qualitative and quantitative trade study of motor configurations.

Keywords—electrified aircraft propulsion (EAP), superconducting electric machines

# I. INTRODUCTION

Aviation’s share of human-caused CO2 emissions has reached $2 . 5 \%$ and continues to grow. However, CO2 emissions only account for $3 4 \%$ of aviation's total effective radiative forcing [1]. Contrails actually dominate with a $5 7 \%$ contribution [1]. In addition to the climate change impacts, particulate emissions from aviation have negative impacts on human health [2]. Correspondingly, to truly mitigate aviation's environmental impact, the development of new aviation technologies must extend beyond net-zero carbon emission goals, such as [3]. SAF alone cannot address the full environmental impact of aviation [2], and it has cost and significant scalability concerns. New propulsion systems and/or energy carriers are needed.

Large transport aircraft with multi-MW powertrains produce the majority of aviation's emissions [4]. System level studies indicate that (a) electrified powertrains can reduce the energy consumption (thus fuel cost) and emissions of these aircraft and (b) increased electrification of the powertrain enables larger reductions in energy consumption [5]-[7]. Achieving these aircraft level benefits requires advancements in the efficiency and specific power of multi-MW electric motors and drives. Cryogenic electric motors and drives are an attractive approach to meet these requirements, especially the demand for very high

efficiency. However, only very limited practical demonstration of these technologies has occurred [8] and further development is needed to meet the performance and requirements demanded by these future aircraft. Accordingly, NASA has started a technical challenge to demonstrate a high performance cryogenic electric motor and drive for multi-MW class electric aircraft. This paper describes the objectives for that development and an initial exploration of the electric motor trade space.

# II. TECHNICAL CHALLENGE AND MOTOR SPECIFICATIONS

# A. Overview of the Technical Challenge

The technical challenge will focus on developing cryogenic electric propulsion technology and determining if it is ready to be a game-changing solution for large transport aircraft that can help meet 2050 aviation climate goals. The intent of the challenge is to look toward and beyond 2050 aviation climate goals by developing high power electrified propulsion systems to substantially reduce or eliminate the use of fossil fuels.

A 5 MW cryogenic motor and drive will be designed and demonstrated at TRL 3. The motor configurations that will be explored include both superconducting and cryogenic, normal conducting stators combined with superconducting or permanent magnet rotors. A priority will be placed on addressing the key technology barriers for high power superconducting machines, including cryogenic cooling of stators, non-contact rotor current supplies, measurement of AC loss in superconductors, low AC loss stator windings, cost, manufacturability, and aircraft requirements. The development is planned to be fuel agnostic. Thus, the motor will be designed to prioritize efficiency over specific power to enable the use of cryogenic machines on vehicles that don’t use liquid cryogen as a fuel. The motor drive development will focus on multi-level, cryogenic topologies that produce current waveforms compatible with the low rotor loss requirements of machines with superconducting rotors [9]. Studies on cryogenic electrical insulation, controls, fault management, and power quality will support the propulsion system development. System-level conceptual design of a high-power EAP vision vehicle and a vehicle-level assessment of the developed technology will guide the technology development and quantify its impact.

TABLE I. SPECIFICATIONS OF THE MOTOR.   

<table><tr><td>Parameter</td><td>Requirement</td><td>Goal</td></tr><tr><td>Continuous power, MW</td><td>5</td><td>-</td></tr><tr><td>Rated speed, rpm</td><td>≥2,000</td><td>3,000</td></tr><tr><td>Rotor field source &amp; temperature</td><td>HTS (cryogenic) or PM (&gt;room temp.)</td><td>-</td></tr><tr><td>Stator conductor &amp; temperature</td><td>Metal (cryogenic)</td><td>Supercond. (cryogenic)</td></tr><tr><td>Efficiency at rated speed &amp; power</td><td>≥99.5%</td><td>≥99.9%</td></tr><tr><td>Continuous specific power, kW/kg</td><td>≥20</td><td>≥40</td></tr><tr><td>Equivalent tip speed at outer radius, m/s</td><td>&lt;100</td><td>-</td></tr><tr><td>DC bus voltage (relative to neutral), V</td><td>≥±270</td><td>≤±1,000</td></tr><tr><td>Rated voltage of electrical insulation, V</td><td>≥1,000</td><td>2,000</td></tr><tr><td>Local heat sink</td><td>Not fuel</td><td>-</td></tr><tr><td>Local heat sink temperature, K</td><td>&gt;20</td><td>-</td></tr><tr><td>Time from off to operational, min</td><td>-</td><td>≤30</td></tr><tr><td>Thermal cycle life</td><td>-</td><td>≥10,000</td></tr><tr><td>Random vibration, Grms</td><td>-</td><td>TBD</td></tr><tr><td>Mechanical shock, G</td><td>-</td><td>6</td></tr></table>

# B. Motor Specifications

The requirements and goals of the motor are summarized in Table 1. The rated speed is defined to be appropriate for directly driving multi-MW fans or propellers. A range of rated speed is permitted because the motor is not designed for a specific aircraft and to provide design flexibility for different stator conductor topologies that may perform better at lower speeds and corresponding lower electrical frequencies due to AC losses. The stator is constrained to operate at cryogenic temperature but both fully and partially cryogenic motors are considered, using either a high temperature superconducting (HTS) or permanent magnet (PM) rotor. Relatively conservative requirements for efficiency and specific power are defined, because TRL advancement of cryogenic machine technology is emphasized over performance optimization. The outer radius of the motor is constrained through a limit on the equivalent rotor tip speed at the outer radius, to ensure the developed motor would have a limited impact on a propulsor’s air flow.

Regarding the DC bus voltage, the requirement defines a lower limit of $\pm 2 7 0 \mathrm { V }$ because it provides benefits and is feasible for a multi-MW system at a manageable weight if a superconducting bus is used. These benefits include keeping nominal voltages within existing aircraft regulations and at a level that prevents partial discharge (PD), reducing the importance of insulation defects, degradation, and material development, and increasing the availability of electronic components. However, higher voltages can increase the efficiency and specific power of both cryogenic and noncryogenic electrified powertrains [10]. The goal voltage is an upper limit of $\pm 1 { , } 0 0 0 \mathrm { V }$ to limit the need for insulation material development and partial discharge (PD) mitigation and to limit the difficultly of packaging the power electronics. This goal is

also high enough to approach peak performance for the powertrain architectures studied in [10]. The voltage specifications for the electrical insulation are kept high to help accommodate faults and to drive insulation technology development that benefits EAP more broadly.

Although the objective is to be fuel agnostic, the motor’s thermal management is constrained to be readily compatible with liquid hydrogen powered aircraft and anticipated safety restrictions. It is assumed that the local heat sink for the motor cannot be a cryogenic fuel. Specifications on operability, thermal cycle life, and operating environment are established as goals, in accordance with [8], to push toward flight readiness.

# III. MOTOR CONFIGURATION TRADE STUDY

This section presents the current status of a trade study of the motor configuration.

# A. Qualitative Assessment

An uncomprehensive list of 17 motor configurations was produced for evaluation. An initial down select was made after performing a qualitative assessment of each motor in terms of 9 criteria covering electromagnetic, thermal, structural, and rotordynamics attributes. Each criteria was graded 1 to 5 by each author. Each configuration was assigned a priority based on the average score, engineering judgement, and project objectives.

The results for the first half of the configurations are shown in Table 2. The results for the second half will be reported in future work after quantitative assessments of those configurations is completed. The configurations designated as partially cryogenic utilize a permanent magnet rotor, whereas those designated as fully cryogenic utilize a high temperature superconducting rotor. Three configurations were assigned a high priority: (a) the radial flux, inner rotor due to its maturity and relative ease of cooling and structurally supporting the stator and rotor and (b) two radial flux, outer rotor motors due to their low risk, simple rotor cooling, and insensitivity to rotor loss; the outer rotor motor with the stator containing the vacuum also doesn’t require a rotary vacuum seal. The number of rotary vacuum seals required by each configuration is important, because each seal adds a design challenge, leak source, failure mechanism, and maintenance concern. Two configurations were given a 2nd priority: (a) the radial+axial flux configuration without iron due to its simple rotor cooling, insensitivity to rotor loss, lack of rotary vacuum seals, and simpler stator construction and cooling compared to the ‘with iron’ variant and (b) the axial flux, fully cryogenic motor with rotor-stator-rotor construction due to an expectation that it is more feasible than the other two axial flux options. Despite scoring highly, the axial flux, partially cryogenic motor was given a low priority due to concerns about cooling and structurally supporting its stator.

This study evaluates every option in Table 2 except for the tri-rotor and fully cryogenic, outer rotor machines.

# B. Preliminary Quantitative Assessment – Methodology

The notable design assumptions are summarized in Table 3. The requirement in Table 1 for power was used along with the goal speed. This preliminary study only considers a ±270 V DC bus (540 V maximum line-to-line voltage). Higher voltage cases will be studied in future work. The outer radius of each radial

<table><tr><td rowspan="2" colspan="3">Configuration</td><td rowspan="2">Vol- ume</td><td rowspan="2">Rotor- dynamics</td><td colspan="2">Structure</td><td colspan="2">Cooling</td><td rowspan="2">Air gap size</td><td colspan="2">Loss</td><td rowspan="2">Score</td><td rowspan="2">Priority</td></tr><tr><td>Rotor</td><td>Stator</td><td>Rotor</td><td>Stator</td><td>Rotor</td><td>Stator</td></tr><tr><td rowspan="4">Radial flux</td><td rowspan="2">Fully Cryo</td><td>Inner rotor</td><td>2.3</td><td>4.7</td><td>3.7</td><td>4.0</td><td>4.0</td><td>4.0</td><td>2.7</td><td>3.3</td><td>3.3</td><td>32.0</td><td>A</td></tr><tr><td>Outer rotor</td><td>3.3</td><td>2.3</td><td>3.0</td><td>3.0</td><td>2.3</td><td>3.7</td><td>4.0</td><td>3.0</td><td>3.7</td><td>28.3</td><td>D</td></tr><tr><td rowspan="2">Partial Cryo</td><td>Outer rotor, stator vacuum</td><td>3.0</td><td>3.3</td><td>3.7</td><td>3.3</td><td>5.0</td><td>4.0</td><td>2.7</td><td>4.7</td><td>3.3</td><td>33.0</td><td>A</td></tr><tr><td>Outer rotor, rotor vacuum</td><td>3.0</td><td>4.0</td><td>3.7</td><td>4.0</td><td>4.7</td><td>2.3</td><td>4.3</td><td>4.3</td><td>3.0</td><td>33.3</td><td>A</td></tr><tr><td rowspan="2">Radial + axial flux</td><td rowspan="2">Partial Cryo</td><td>Tri-rotor without iron</td><td>4.3</td><td>3.3</td><td>2.7</td><td>3.3</td><td>5.0</td><td>4.0</td><td>1.7</td><td>4.3</td><td>3.3</td><td>32.0</td><td>B</td></tr><tr><td>Tri-rotor with iron</td><td>4.3</td><td>3.3</td><td>2.7</td><td>2.7</td><td>5.0</td><td>3.0</td><td>1.7</td><td>4.3</td><td>3.0</td><td>30.0</td><td>C</td></tr><tr><td rowspan="3">Axial flux</td><td rowspan="2">Fully Cryo</td><td>Stator-rotor-stator</td><td>3.3</td><td>4.0</td><td>3.7</td><td>3.0</td><td>3.3</td><td>3.7</td><td>3.3</td><td>3.3</td><td>3.0</td><td>30.7</td><td>C</td></tr><tr><td>Rotor-stator-rotor</td><td>3.3</td><td>4.0</td><td>4.0</td><td>2.7</td><td>2.3</td><td>3.3</td><td>2.7</td><td>3.3</td><td>4.0</td><td>29.7</td><td>B</td></tr><tr><td>Partial Cryo</td><td>Rotor-stator-rotor</td><td>3.3</td><td>4.0</td><td>4.3</td><td>2.3</td><td>5.0</td><td>2.0</td><td>4.3</td><td>4.3</td><td>3.7</td><td>33.3</td><td>D</td></tr></table>

flux and axial flux motor was fixed at $0 . 2 5 \mathrm { m }$ and $0 . 3 0 \mathrm { m }$ , respectively, giving equivalent tip speeds of $7 9 \mathrm { m / s }$ and $9 4 \mathrm { m / s }$ . A flooded stator with direct coolant-to-winding contact on the winding’s inner and outer diameters was assumed. A nine-phase distributed wound stator matching the topology of NASA’s high efficiency megawatt motor (HEMM) [11] is assumed to give the machine a high winding factor, limit stator field harmonic content, and enable canceling of the 3rd, 5th, and 7th harmonics in the machine’s back emf.

This preliminary study explores single phase liquid neon (subcooled to $2 5 ~ \mathrm { K }$ at the inlet) as the stator coolant, because the results in [12] for some of the same motor configurations but alternative stator conductors (copper and aluminum Litz wire)

TABLE III. ASSUMED PARAMETERS FOR THE CONFIGURATION STUDY.   

<table><tr><td colspan="3">Parameter</td><td>Value</td></tr><tr><td rowspan="2">Motor</td><td colspan="2">Overall outer radius</td><td>0.25 m (radial flux)0.3 m (axial flux)</td></tr><tr><td colspan="2">Phases</td><td>9</td></tr><tr><td rowspan="7">Materials</td><td colspan="2">Structure - rotor</td><td>Titanium</td></tr><tr><td colspan="2">Structure - stator</td><td>G-10</td></tr><tr><td colspan="2">Shaft</td><td>17-4 stainless</td></tr><tr><td colspan="2">Back iron</td><td>Fe49.5Co48.5V1.9</td></tr><tr><td colspan="2">Conductor - rotor (fully cryo only)</td><td>2G HTS (REBCO)</td></tr><tr><td colspan="2">Rotor coil former (fully cryo only)</td><td>316 stainless</td></tr><tr><td colspan="2">Magnets (partial cryo only)</td><td>Neodymium N48SH</td></tr><tr><td rowspan="4">Thermal</td><td colspan="2">Cooling - stator</td><td>Flooded, ID &amp; OD contact</td></tr><tr><td colspan="2">Cooling - rotor</td><td>Rotating cryocooler</td></tr><tr><td rowspan="2">Thermal conductivity</td><td>Stator epoxy</td><td>1.1 W/m-K</td></tr><tr><td>Stator insulation</td><td>0.2 W/m-K</td></tr><tr><td rowspan="3">Magnetic</td><td colspan="2">Magnet Br (partial cryo only)</td><td>1.25 T</td></tr><tr><td colspan="2">Rotor conductor fill factor (fully cryo only)</td><td>90%</td></tr><tr><td colspan="2">Physical air gap</td><td>1 mm (radial, partial cryo)Variable (other)</td></tr></table>

show it provides a small to modest increase in specific power compared to gaseous helium at $2 1 \mathrm { ~ K ~ }$ and subcooled liquid nitrogen at $6 6 ~ \mathrm { K }$ . The coolant selection for the final motor will incorporate practical factors (e.g., cost, supply chain) and cryogen cooling factors that are not yet considered.

A detailed discussion of the design code used to assess the radial flux configurations is contained in [12]. The only geometric difference from that paper is that for the partially cryogenic motor with the rotor acting the vacuum containment , the vacuum tube in the air gap is eliminated. This study only considers a rotating cryocooler for cooling the superconducting rotor. Also, this study evaluates stator conductors not included in [12], as detailed below.

A detailed discussion of the design code used to assess the axial flux motors is included in [13]. The key differences here are the stator’s conductor, operating temperature, coolant, and structural material, as well as the assumed cryocooler performance (the cryocooler in [12] was assumed here). The geometry considered here for the fully cryogenic, axial flux motors has (a) a thermal bridge that extends radially through the middle of the superconducting rotor to the outer diameter of the HTS coils (i.e., the ‘mid-bridge’ design in [13]) and (b) a skewed stator winding to minimize the length and complexity of the end turns (i.e., the ‘zig-zag’ design in [13]), which enables a reasonable air gap in the rotor-stator-rotor configurations.

This paper considers the following stator conductors: copper and aluminum Litz cables and three multi-filamentary wires (high purity aluminum (HPAL) [14], $\mathbf { M g B } _ { 2 }$ [15], and Bi-2212 [16]). The construction of the Litz cables and the AC loss in them was modeled as in [12]. The AC loss components in the superconducting windings, namely the hysteresis, eddy current, and coupling losses, were calculated according to the method in [17] that captures the effect of a rotating and oscillating magnetic field as well as higher harmonics. Note that transport current losses in the superconductors was neglected at this stage of the analysis. Hysteresis loss does not occur in HPAL but conventional Ohmic loss does [14]. The total resistivity of the HPAL was quantified by curve fitting the zero-field resistivity data in [18] and using the magnetoresistance contribution from [19]-[20]. The assumed residual resistance ratio (RRR) of the

HPAL filaments is 1000. The coupling loss and eddy current loss in the HPAL wire’s sheath are calculated in the same manner as the superconductors. The eddy current loss in the HPAL filaments was calculated using the equation in [17] but with the conductivity and wire diameter replaced by the HPAL resistivity and filament diameter. The assumed construction and properties of the multifilamentary wires is given in Table 4. The diameter of each wire was defined as an optimization variable. For the Litz cables, a 30 to 50 AWG wire was permitted (wire diameter of $0 . 2 5 5 \mathrm { m m }$ to $0 . 0 2 5 \mathrm { m m } ,$ ). For HPAL and the superconductors, a wire diameter of $0 . 1 6 \mathrm { m m }$ to $2 . 1 6 \mathrm { m m }$ was specified, although the diameter was increased to the thickness of the stator winding if less than 2 wires would fit radially. Thus, diameters up to $4 . 3 \mathrm { m m }$ could occur. The large majority of optimized MgB2 and HPAL designs were found to use wire diameters of about 1 mm or smaller. However, the Bi-2212 designs optimized to wire diameters of 1 mm to $4 . 3 \mathrm { m m }$ , in order to reduce coupling losses by decreasing the critical frequency for skin effect [21]. Consequently, results are also shown for the case where the diameter of the Bi-2212 wire is limited to 1 mm.

The optimization variables used in this study are: the number of pole pairs; stack length; stator wire gauge/diameter; thickness of the stator winding and stator coolant channel; shaft diameter at the bearings; pressure and flow rate of the coolant; and distance between the cryogenic stator winding and noncryogenic stator back iron. The fully cryogenic machines also included the following optimization variables: width and operating temperature of the HTS; mechanical air gap; and thickness of the thermal bridge that connects the cryocooler to the HTS rotor winding. For the partially cryogenic machines, the thickness of the magnets was optimized. The skew of the stator windings in the axial flux machines was optimized.

# C. Preliminary Assessment – Partially Cryogenic Machines

Figs. 1 and 2 show the optimization results for the radial flux, partially cryogenic motors with an outer rotor and the vacuum contained, respectively, by the rotor and stator. Note that the results for Bi-2212 wires less than 1 mm in diameter and $\mathbf { M g B } _ { 2 }$ do not appear because the optimization algorithm did not find valid designs within the depicted performance range. When the stator provides containment, no rotary vacuum seals are needed but the vacuum vessel is in the air gap. This necessitates

TABLE IV. ASSUMED CONSTRUCTION AND PROPERTIES OF THE MULTIFILAMENTARY STATOR CONDUCTORS.   

<table><tr><td rowspan="2">Parameter</td><td colspan="3">Conductor</td></tr><tr><td>HPAL</td><td>MgB2</td><td>Bi-2212</td></tr><tr><td>Diameter - filament</td><td colspan="3">10 μm</td></tr><tr><td>Diameter - wire</td><td colspan="3">Variable</td></tr><tr><td>Diameter - core</td><td colspan="3">100 μm</td></tr><tr><td>Thickness - wire sheath</td><td colspan="3">50 μm</td></tr><tr><td>Thickness - filament chemical barrier</td><td colspan="2">10 μm</td><td>5 μm</td></tr><tr><td>Thickness - wire insulation</td><td colspan="3">30 μm</td></tr><tr><td>Resistivity - wire sheath &amp; matrix</td><td colspan="2">36.5 μΩ-cm [22]</td><td>1.5 μΩ-cm [16]</td></tr><tr><td>Twist pitch</td><td colspan="3">30x wire diameter</td></tr></table>

图片摘要：该图主要展示 IV. ASSUMED CONSTRUCTION AND PROPERTIES OF THE MULTIFILAMENT。
![](images/9b035bec584192177a6e6d5c60af3e98d25726d068e1c5f51bb51399a2673645.jpg)  
Cu (RRR 97)   
. HPAL   
Al (RRR 100)   
·Bi-2212   
·MgB2   
Bi-2212<1 mm

Fig. 1. Optimization results for the radial flux, partially cryogenic motor with an outer rotor and vacuum contained by the rotor for different stator conductors. Stator cooled by subcooled liquid neon at $2 5 ~ \mathrm { K }$ . The requirement and goal are shown by the black square and black diamond, respectively.

Fig. 2. Optimization results for the radial flux, partially cryogenic motor with an outer rotor and vacuum contained by the stator for different stator conductors. Stator cooled by subcooled liquid neon at $2 5 ~ \mathrm { K }$ . The requirement and goal are shown by the black square and black diamond, respectively.   
图片摘要：该图主要展示 2. Optimization results for the radial flux, partially cryog。
![](images/d059c582c1a45dcc03c6f6a26c496b8b5f527d4d53720d1dd669cb75e3f883a7.jpg)  
·Cu (RRR 97) .   
. HPAL   
Al (RRR 100)   
Bi-2212   
·MgB2   
Bi-2212<lmm

heavier permanent magnets to maintain the magnetic field in the stator and/or higher total current in the stator. This tradeoff is found to significantly reduce the achievable specific power regardless of stator conductor. The relative performance of the stator conductors is independent of the vacuum containment. No conductor enables either motor configuration to achieve the requirements in Table 1, although copper and aluminum Litz with rotor vacuum containment are close enough to warrant consideration due to the benefits of a magnet rotor (simplicity, cost, and reduced inverter output filtering).

The optimization algorithm was unable to find any valid designs for the axial flux, partially cryogenic motor with either concentrated or distributed stator windings. The root cause is the

large thickness of vacuum and fluid containment vessels, which in this configuration exist on each side of the stator. Stiffening the vessel via a material or geometry change or changing the cooling approach may lead to valid designs.

# D. Preliminary Assessment – Fully Cryogenic Machines

Figs. 3 and 4 present the results for the two axial flux, fully cryogenic motors. $\mathbf { M g B } _ { 2 }$ designs did not close and the smaller diameter Bi-2212 designs either didn’t close or didn’t meet requirements. The machines with two rotors perform worse because the rotor’s mass and heat load are larger and the rotor field directed away from the stator is not used. Compared to the radial flux, inner rotor motor, the axial flux configurations make HPAL more attractive, and with two stators they achieve a higher efficiency but reduced specific power; these trends are due to the axial flux motors’ better compatibility with a smaller number of pole pairs, a lack of iron loss, and more freedom in rotor iron placement.

The results for optimizing the radial flux, fully cryogenic motor with inner rotor are depicted in Fig. 5. Viable designs were found for all conductors, and only HPAL does not meet the required performance. The MgB2 machines achieve almost half the loss of the Bi-2212 and Litz conductors, although MgB2 designs are limited to $2 2 \mathrm { k W / k g }$ due to thermal constraints. An improved cooling design could extend that limit.

# E. Effect of Wire Gauge on Machines Employing Litz Cables

Figs. 1 to 5 show Litz cables to be very competitive with superconductors. A key reason for their high efficiency is an assumption that 50 AWG Litz is feasible. Fig. 6 shows the impact of restricting Litz strand gauge on a radial flux, inner rotor machine. For the Litz cable construction assumed, limiting the wire gauge to 40 to 45 AWG has little to no effect, whereas loss significantly increases for 35 and 30 AWG.

图片摘要：该图主要展示 5. Optimization results for the axial flux, fully cryogenic 。
![](images/21bd579216cf99498673d89800a81769a11e80074214acccf3cf90c5cb23f5e6.jpg)  
Fig. 5. Optimization results for the axial flux, fully cryogenic motor with a distributed stator winding and a rotor-stator-rotor construction. Stator cooled by subcooled liquid neon at $2 5 ~ \mathrm { K }$ . The requirement and goal are shown by the black square and black diamond, respectively.

图片摘要：该图主要展示 5. Optimization results for the axial flux, fully cryogenic 。
![](images/c4df1cd2d7f3e3d75ef9810bf82012544a887953beec276d3be5268539ff85c9.jpg)  
Fig. 3. Optimization results for the axial flux, fully cryogenic motor with a distributed stator winding and a stator-rotor-stator construction. Stator cooled by subcooled liquid neon at $2 5 ~ \mathrm { K }$ . The requirement and goal are shown by the black square and black diamond, respectively.

图片摘要：该图主要展示 3. Optimization results for the axial flux, fully cryogenic 。
![](images/ee96b057e4f92fd32583439f41fe41b5978aa346d00a97bbb23dd1af003c164f.jpg)  
Fig. 4. Optimization results for the radial flux, fully cryogenic motor with an inner rotor and a distributed stator winding. Stator cooled by subcooled liquid neon at $2 5 ~ \mathrm { K }$ . The requirement and goal are shown by the black square and black diamond, respectively.

# IV. CONCLUSIONS

This paper presented an overview of a new project to develop a 5 MW motor and drive that uses a cryogenic stator. The specifications of the motor were described. The preliminary results of a motor configuration trade study were then presented. A qualitative assessment of 9 configurations was discussed, and the performance of 6 was evaluated using motor design codes that predict the motor’s efficiency and total specific power based on electromagnetic, thermal, and mechanical calculations. The preliminary results in this paper will be refined in future work to gain more confidence in the relative performance of the motor configurations and conductors.

图片摘要：该图主要展示 4. Optimization results for the radial flux, fully cryogenic。
![](images/035d3e9cd5de9c00aadbfe3e8d4063908d9723459f9a35220f0f004815a7208a.jpg)  
Fig. 6. Optimization results for a radial flux, fully cryogenic motor with an inner rotor and stator composed of copper (RRR 97) with different limits on the wire gauge. Stator cooled by subcooled liquid neon at $2 5 ~ \mathrm { K }$ . The requirement and goal are shown by the black square and black diamond, respectively.

These preliminary results indicate that the radial flux, fully cryogenic machine is the most promising of the topologies considered here for achieving the project’s goals. Despite having a $2 0 \%$ larger diameter, axial flux machines generally perform worse than radial machines primarily due to their thicker fluid and vacuum vessels in the air gap with the materials and cooling schemes assumed in this paper. Radial flux permanent magnet machines have promising performance without the use of superconductors but don’t meet performance requirements.

The results herein are subject to the conductor construction, voltage, and cooling assumptions made in this paper. These assumptions will be refined and varied in future work before definitive conclusions are drawn on the relative merit of each conductor. These preliminary results suggest that copper and aluminum Litz cables can outperform HPAL and compete with superconductors even if Litz strands are limited to 40 AWG. MgB2 is shown to enable very high efficiency when it does close thermally. Bi-2212 is predicted to have very high performance when operated above its first critical frequency, but that result warrants more scrutiny and refined modeling. In this paper, a somewhat conservative definition of the wire and turn/cable construction is assumed for HPAL and the superconductors. In general, MgB2 and HPAL do not perform well due to their low fill factor of conductor in the stator slot $( < 1 0 \% )$ , particularly when compared to the Litz cables. Increasing this fill factor will make them more competitive. It should also be noted that the manufacturability of the stator windings has not been accounted for. For example, the performance of MgB2 and Bi-2212 may decrease if the designs herein are found to be incompatible with a ‘react then wind’ manufacture, because the structural material assumed for the stator cannot survive the reaction heat treatment.

The electrical frequency of machines reported in this paper varies since the number of pole pairs is an optimization variable. MgB2 optimized to lower frequencies, whereas the large diameter Bi-2212 optimized to higher frequencies. Most designs fall within the range of 250 to $4 0 0 \mathrm { H z }$ .

# REFERENCES

[1] D.S. Lee et al., “The contribution of global aviation to anthropo-genic climate forcing for 2000 to 2018,” Atmos. Environ. 244, 117834, 2021.   
[2] P. Prashanth et al., "Near-zero environmental impact aircraft," Sustainable Energy & Fuels, vol. 20, 2024.   
[3] Federal Aviation Administration, “United States 2021 Aviation Climate Action Plan,” 2021.   
[4] B. Graver et al., “CO2 emissions from commercial aviation, 2018,” Intl. Council on Clean Transport., 2019.   
[5] J.L. Felder et al., “Updated assessment of turboelectric boundary layer ingestion propulsion applied to a single-aisle commercial transport,” NASA/TM-20210016661, 2022.   
[6] T. Chau and J. Duensing, “Conceptual design of the hybrid-electric subsonic single aft engine (SUSAN) electrofan transport aircraft,” AIAA SCITECH 2024 Forum, AIAA 2024-1326, Orlando, FL, 2024.   
[7] N.J. Blaesser, “Mission and vehicle-level updates for the parallel electricgas architecture with synergistic utilization scheme (PEGASUS) Concept Aircraft,” NASA/TM–20240001480, 2024.   
[8] E. Nilsson, “Cryogenic and superconductivity development for future electric aircraft propulsion at Airbus,” 4th Intl. Workshop on Emissions Free Air Transport through Supercond., Enschede, Netherlands, 2024.   
[9] M. G. Granger, T. F. Tallerico, A. D. Anderson, J. J. Scheidler, P. Kascak, and A. Leary, “Concept design of a 1.4 MW drive for rotor loss minimization in a partially superconducting motor,” IEEE Transp. Electrif. Conf., Aanaheim, CA, 2022.   
[10] P. Kshirsagar et al., “Anatomy of a 20 MW electrified aircraft: metrics and technology drivers,” AIAA/IEEE Elec. Aircr. Technol. Symp., New Orleans, LA, 2020.   
[11] T. T. Tallerico, J. J. Scheidler, D. Lee, and K. Haran, “Electromagnetic redesign of NASA’s high efficiency megawatt motor,” AIAA/IEEE Elec. Aircr. Technol. Symp., New Orleans, LA, 2020.   
[12] T. F. Tallerico, J. J. Scheidler, and A. D. Anderson, “Cryogenic copper and aluminum litz wire motors for electric aircraft,” IEEE Transp. Electrif. Conf., in press.   
[13] T. Tallerico, A. D. Anderson, and J. J. Scheidler, "Concept design of a 5 MW axial flux partially superconducting electric machine," AIAA Aviation Forum & ASCEND, AIAA 2024-4092, Las Vegas, NV, 2024.   
[14] J. Kwon et al., “Comparison of the AC loss of MgB2 superconductors and HPAL cryogenic composites for rotating machine applications,” IEEE Trans. Appl. Supercond., vol. 35, no. 5, 2025.   
[15] Y. Sogabe et al., “AC loss evaluations of twisted multifilament magnesium diboride (MgB2) wires under practical operating conditions based on experiments,” Supercond. Sci. Tech., vol. 38, no. 3, 2025.   
[16] M. Sumption, J. Rochester, and A. Otto, “Low loss Bi:2212 superconductors for electric aircraft,” IEEE Transp. Electrif. Conf., Aanaheim, CA, 2022.   
[17] T. Balachandran and K. S. Haran, “Instantaneous loss integration method to estimate AC losses in superconductors with spatial and time harmonics,” IEEE Trans. Appl. Supercond., vol. 33, no. 5, 2023.   
[18] J. E. Campbell, E. A. Eldridge, and J. K. Thompson, "Handbook on materials for superconducting machinery," Battelle Columbus Labs, 1974.   
[19] F. R. Fickett, “Aluminum; 1. a review of resistive mechanisms in aluminum,” Cryogenics, vol. 11, pp. 349–367, 1972.   
[20] R. J. Corruccini, “The Electrical Properties of Aluminum for Cryogenic Electromagnets,” NBS Technical Note 218, 1964.   
[21] M. D. Sumption, M. Majoros, and E. W. Collings, “AC losses in superconducting materials, wires, and tapes,” in Handbook of Superconductivity: Characterization and Applications, vol. III, D. A. Cardwell and D. C. Larbalestier, Eds. CRC Press, 2023, pp. 243–244.   
[22] M. D. Sumption, J. Murphy, M. Susner, and T. Haugan, “Performance metrics of electrical conductors for aerospace cryogenic motors, generators, and transmission cables,” Cryogenics, vol. 111, 103171, 2020.
