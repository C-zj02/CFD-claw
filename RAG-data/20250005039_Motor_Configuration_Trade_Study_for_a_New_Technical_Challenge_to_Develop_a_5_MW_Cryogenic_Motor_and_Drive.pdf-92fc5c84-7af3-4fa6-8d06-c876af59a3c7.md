# Motor Configuration Trade Study for a New Technical Challenge to Develop a 5 MW Cryogenic Motor and Drive

Justin J. Scheidler

Thomas F. Tallerico

Aaron D. Anderson

Peter E. Kascak

图片摘要：该图片为文档封面或首页内容，主题与Motor Configuration Trade Study for a New Technical Challenge to Develop a 5 MW Cryogenic Motor and Drive相关。
![](images/1debdff74bfc985dad775a6780f922c45044c2526059ef61687e8572ec888487.jpg)

NASA Glenn Research Center, Cleveland, USA

This material is a work of the U.S. Government and is not subject to copyright protection in the United States.

• Motivation   
• Technical challenge & motor specifications   
• Description of motor configurations   
• Motor design codes   
• Motor trade study results

• Permanent magnet rotors   
• Superconducting rotors

• Conclusions

• Status quo won’t cut it – global ${ \mathsf { C O } } _ { 2 }$ emissions from aviation growing at increasing rate   
• US Aviation Climate Action Plan (2021) [2] set goal for net-zero carbon emissions by 2050   
• $C O _ { 2 }$ only accounts for 34% of total radiative forcing [1]   
• SAF (sustainable aviation fuels) alone cannot address environmental impact, and it has cost & significant scalability concerns

• Achieving significant impact necessitates focus on large transport aircraft   
• Aircraft-level studies demonstrate that higher power electrified propulsion systems enable larger reductions in energy consumption (fuel cost) [3-5]

图片摘要：该图片与Global aviation’s impact on CO2 [1]；Human Caused CO这部分内容相关。
![](images/b1a16fc6efe7a496678ca8ddd4898ec6edf2983ae2a9fb3432251c7c9b6cfabb.jpg)  
Global aviation’s impact on CO2 [1]

Human-Caused CO
2 Emissions Aviation’s Percentage of Total

1. https://doi.org/10.1016/j.atmosenv.2020.117834   
2. https://www.faa.gov/sustainability/aviation-climate-action-plan   
3. https://ntrs.nasa.gov/api/citations/20210016661/downloads/TM-20210016661.pdf

4. https://doi.org/10.2514/6.2024-1326   
5. https://ntrs.nasa.gov/api/citations/20240001480/downloads/NASA-TM-20240001480.pdf

# Develop a 5 MW superconducting motor system and demonstrate at subscale to enable new higher performance airplane architectures (TRL 3)

Design (2024 – 2028), build & test (2028 – 2030)

# Objectives

• Develop 5 MW Superconducting Machine Technologies (TRL-3)   
• Determine high power EAP aircraft and powertrain architectures

# Motor Specifications

<table><tr><td>Parameter</td><td>Requirement</td><td>Goal</td></tr><tr><td>Continuous power, MW</td><td>5</td><td>-</td></tr><tr><td>Rated speed, rpm</td><td>≥ 2,000</td><td>3,000</td></tr><tr><td>Rotor field source &amp; temperature</td><td>HTS (cryo) or PM (&gt; room temp.)</td><td>-</td></tr><tr><td>Stator conductor &amp; temperature</td><td>Metal (cryo)</td><td>Superconducting (cryo)</td></tr><tr><td>Efficiency at rated speed</td><td>≥ 99.5%</td><td>≥ 99.9%</td></tr><tr><td>Continuous specific power, kW/kg</td><td>≥ 20</td><td>≥ 40</td></tr><tr><td>Equivalent tip speed at outer radius, m/s</td><td>≤ 100</td><td>-</td></tr><tr><td>DC bus voltage (relative to neutral), V</td><td>≥ ±270</td><td>≤ ±1,000</td></tr><tr><td>Rated voltage of insulation, V</td><td>≥ 1,000</td><td>2,000</td></tr><tr><td>Local heat sink</td><td>Not fuel</td><td>-</td></tr><tr><td>Local heat sink temperature, K</td><td>&gt; 20</td><td>-</td></tr><tr><td>Time from off to operational, min</td><td>-</td><td>≤ 30</td></tr><tr><td>Thermal cycle life</td><td>-</td><td>≥ 10,000</td></tr><tr><td>Random vibration, Grms</td><td>-</td><td>TBD</td></tr><tr><td>Mechanical shock, G</td><td>-</td><td>6</td></tr></table>

Motor to direct drive multi-MW fans / propellers   
Considering fully cryogenic (HTS rotor) & partially cryogenic (permanent magnet rotor)   
• TRL advancement prioritized over performance   
Upper limit of ±1,000 V to limit material development & electronics packaging issues   
Desire to be fuel agnostic, but not allowing fuel to be local heat sink

# Motor Configurations

• Distributed winding in all but 1 configuration

<table><tr><td>#</td><td>Motor type (rotor field source)</td><td>Flux direction</td><td colspan="2">Construction</td></tr><tr><td>1</td><td rowspan="5">Partial cryo (permanent magnet)</td><td rowspan="3">Radial</td><td rowspan="2">Outer rotor</td><td>Stator is vacuum vessel</td></tr><tr><td>2</td><td>Rotor is vacuum vessel</td></tr><tr><td>3</td><td colspan="2">Helmholtz</td></tr><tr><td>4</td><td>Axial</td><td colspan="2">Rotor – stator – rotor</td></tr><tr><td>5</td><td>Radial + axial</td><td colspan="2">Tri-rotor, no iron</td></tr><tr><td>6</td><td rowspan="3">Fully cryo (supercond.)</td><td>Radial</td><td colspan="2">Inner rotor</td></tr><tr><td>7</td><td rowspan="2">Axial</td><td colspan="2">Stator – rotor – Stator</td></tr><tr><td>8</td><td colspan="2">Rotor – stator – rotor</td></tr></table>

图片摘要：该图片与Radial flux Helmholtz machine with permanent magnet rotors (patent pending)• Dis这部分内容相关。
![](images/d4660bb1423e21b383e24826ff714f5c11e762eead1a3c946b4579e7e496d0e1.jpg)

图片摘要：该图片与Radial flux Helmholtz machine with permanent magnet rotors (patent pending)• Dis这部分内容相关。
![](images/82cbe9363e678c9d6b55dcc7295bc9e5bc9c8a9bb1bb706a91999288f98d8ea0.jpg)

<table><tr><td>#</td><td>Motor type (rotor field source)</td><td>Flux direction</td><td colspan="2">Construction</td></tr><tr><td>1</td><td rowspan="5">Partial cryo (permanent magnet)</td><td rowspan="3">Radial</td><td rowspan="2">Outer rotor</td><td>Stator is vacuum vessel</td></tr><tr><td>2</td><td>Rotor is vacuum vessel</td></tr><tr><td>3</td><td colspan="2">Helmholtz</td></tr><tr><td>4</td><td>Axial</td><td colspan="2">Rotor – stator – rotor</td></tr><tr><td>5</td><td>Radial + axial</td><td colspan="2">Tri-rotor, no iron</td></tr><tr><td>6</td><td rowspan="3">Fully cryo (supercond.)</td><td>Radial</td><td colspan="2">Inner rotor</td></tr><tr><td>7</td><td rowspan="2">Axial</td><td colspan="2">Stator – rotor – Stator</td></tr><tr><td>8</td><td colspan="2">Rotor – stator – rotor</td></tr></table>

图片摘要：该图片与Radial flux Helmholtz machine with permanent magnet rotors (patent pending)这部分内容相关。
![](images/031e9bd54d148e2dfc5c09f931955b20ec8cd3e11b812b8c8444b2f7dde2f920.jpg)  
Radial flux Helmholtz machine with permanent magnet rotors (patent pending)

图片摘要：该图片与Motor ConfigurationsRadial flux Helmholtz machine with permanent magnet rotors (这部分内容相关。
![](images/98224cf23702c0ca8c53dae837d389bbbfcdd5666c03ffa3655dba3c386c07b4.jpg)

图片摘要：该图片与Motor ConfigurationsRadial flux Helmholtz machine with permanent magnet rotors (这部分内容相关。
![](images/7022715750c81d25f1cedb5c8f05841647985a5a4c3e6c5c0a9ce7619d2d3beb.jpg)

图片摘要：该图片与Motor ConfigurationsRadial flux Helmholtz machine with permanent magnet rotors (这部分内容相关。
![](images/e252d814e16871c42b553f7cd236d272ad8dfdc3609261adb0b8d052bc25f973.jpg)

# Motor Configurations

<table><tr><td>#</td><td>Motor type (rotor field source)</td><td>Flux direction</td><td colspan="2">Construction</td></tr><tr><td>1</td><td rowspan="5">Partial cryo (permanent magnet)</td><td rowspan="3">Radial</td><td rowspan="2">Outer rotor</td><td>Stator is vacuum vessel</td></tr><tr><td>2</td><td>Rotor is vacuum vessel</td></tr><tr><td>3</td><td colspan="2">Helmholtz</td></tr><tr><td>4</td><td>Axial</td><td colspan="2">Rotor – stator – rotor</td></tr><tr><td>5</td><td>Radial + axial</td><td colspan="2">Tri-rotor, no iron</td></tr><tr><td>6</td><td rowspan="3">Fully cryo (supercond.)</td><td>Radial</td><td colspan="2">Inner rotor</td></tr><tr><td>7</td><td rowspan="2">Axial</td><td colspan="2">Stator – rotor – Stator</td></tr><tr><td>8</td><td colspan="2">Rotor – stator – rotor</td></tr></table>

图片摘要：该图片与Motor Configurations；Motor Design Codes这部分内容相关。
![](images/96880c4f5886722879be30c7d5e7ffdbd673e90625031ddebe91aa99f9c90356.jpg)

图片摘要：该图片与Motor Configurations；Motor Design Codes这部分内容相关。
![](images/d5c9c5857aede367ac0c726c7ed4f30b329211977b8dac24d0b3ad70e708a193.jpg)

# Motor Configurations

图片摘要：该图片与Motor Design Codes；• Analytical equations to calculate rotor & stator magnetic f这部分内容相关。
![](images/84d32f04789375bc49e1c85bd4fcec3ac7e7a7043b288b23365a0ea9eb9a764c.jpg)

# Motor Design Codes

图片摘要：该图片与• Analytical equations to calculate rotor & stator magnetic fields over a half p这部分内容相关。
![](images/4532e187fc48b9b8ad31ab9663eacbf970705222c3bd12422a3d2aa0c457fcdd.jpg)

• Analytical equations to calculate rotor & stator magnetic fields over a half period, heat transfer, & AC loss   
• Winding surface directly cooled: on one active face (tri-rotor & axial flux) or inner & outer diameters (radial flux)   
• Vacuum & coolant vessels sized based on buckling (external pressure) or hoop stress (internal pressure)   
• Shafts & bearings sized to direct drive propeller subjected to aircraft maneuvers with $290 \%$ bearing reliability   
• For superconducting rotors:

• Rotating cryocooler used with Carnot efficiency from [6] & mass based on commercial Stirling coolers [7]

• Heat load $=$ radiation + 10 W

<table><tr><td>Losses considered</td><td>Masses considered</td></tr><tr><td>• In Litz wires: AC resistive &amp; proximity eddy current losses
• In superconductors: hysteresis, eddy current, coupling, (also transport in HTS)
• Bearing
• Windage (Helmholtz motor only)
• Pumping fluid through motor
• Cryocooler (fully cryo motors)
• Iron (where required)
• 1.5 kW for rotary vacuum seals (where required)</td><td>• Electromagnetic
• Shafts &amp; bearings
• Vacuum vessels, fluid containment, fluid, &amp; rotors
• Cryocooler &amp; thermal connection to it
• 10 kg for miscellaneous components</td></tr></table>

• 10% margin on torque   
• Assumed 1 inverter for Helmholtz motor, but 1 inverter per pole pair for others   
• Results shown for 3,000 rpm, ±1,000 V DC bus, & 100 m/s equivalent tip speed

• Coolant: mostly subcooled LNe but also GHe

<table><tr><td rowspan="2" colspan="2">Parameter</td><td colspan="2">Conductor</td></tr><tr><td>HPAL</td><td>MgB2 Bi-2212</td></tr><tr><td rowspan="3">Diameter</td><td>Filament</td><td colspan="2">10 μm</td></tr><tr><td>Wire</td><td colspan="2">Optimized</td></tr><tr><td>Core</td><td colspan="2">100 μm</td></tr><tr><td rowspan="3">Thickness</td><td>Wire sheath</td><td colspan="2">50 μm</td></tr><tr><td>Chemical barrier</td><td>10 μm</td><td>5 μm</td></tr><tr><td>Wire insulation</td><td colspan="2">30 μm</td></tr><tr><td colspan="2">Resistivity of wire sheath &amp; matrix</td><td>36.5 μΩ-cm</td><td>1.5 μΩ-cm</td></tr><tr><td colspan="2">Twist pitch</td><td colspan="2">30x wire diameter</td></tr></table>

<table><tr><td colspan="2">Parameter</td><td>Value</td></tr><tr><td>Motor</td><td>Phases</td><td>9 (distributed) or 3-9 (concentrated)</td></tr><tr><td rowspan="2">Structural</td><td>Rotor materials</td><td>316 SS (coil former), 17-4 SS (shaft), titanium (other)</td></tr><tr><td>Stator materials</td><td>G-10 (in field), titanium (other)</td></tr><tr><td rowspan="4">Magnetic</td><td>Back iron</td><td>Fe49.5Co48.5V1.9</td></tr><tr><td>Rotor conductor (fully cryo only)</td><td>REBCO, 90% fill</td></tr><tr><td>Magnets (partial cryo only)</td><td>NdFeB, Br = 1.3 T, 90% fill</td></tr><tr><td>Physical air gap</td><td>1 mm (radial, partial cryo) variable (other)</td></tr></table>

• Subcooled LNe (25 K at inlet)   
• Bi-2212 did not close, HPAL & MgB2 closed outside range shown for stator vacuum case   
• Eliminating vacuum vessel from air gap provides ~7 kW/kg benefit but at expense of rotary vacuum seal

# Subcooled LNe

25 K inlet, 6-40 m3/hr, 1 bar

图片摘要：该图片与Config. 1；Subcooled LNe这部分内容相关。
![](images/cea96901bd6bfaf40d5589cec175e8e174dca8dedd2f32c3705a6fd1a5bdadd2.jpg)  
Config. 1

图片摘要：该图片与Subcooled LNe；25 K inlet, 6 40 m3/hr, 1 bar这部分内容相关。
![](images/c335b1c7529206377b69afd87c93cf87e278bec0ccad408aa84e6b41fb5fbedc.jpg)

# Subcooled LNe

25 K inlet, 6-40 m3/hr, 1 bar

图片摘要：该图片与Config. 2；Results – Permanent Magnet Rotors这部分内容相关。
![](images/3c1e170fbe092f8578c5aa254d31d9fe10330910c2043a633311dc342a48ce27.jpg)  
Config. 2

图片摘要：该图片与Results – Permanent Magnet Rotors；• Helmholtz configuration ( 3)这部分内容相关。
![](images/86faeb6f06f03dc3716e8e0f65b692b5d2803ef98a76b5a9d1372a099ef813cd.jpg)

# Results – Permanent Magnet Rotors

• Helmholtz configuration (#3)

• Primary limitation: tradeoff between (a) keeping phase voltage < ±1 kV (using more HTS tapes in parallel to compose a turn) and (b) reducing circulating current in paralleled tapes (using fewer HTS tapes in parallel to reduce circulating currents)   
• High performance possible by limiting circulating currents

# GHe

allowed: 35-65 K inlet, 60-600 m3/hr, 5-40 bar

图片摘要：该图片与Config. 3；no mitigation of circulating currents这部分内容相关。
![](images/864a049784db53f5d5dde538922361266cd9a7dc9f19340b3115b7e981067042.jpg)  
Config. 3

no mitigation of circulating currents

Did not close with original assumptions & model of a stator coil

Ideal (circulating currents $= 0$   
图片摘要：该图片与SerieHTS；2 mitigations implemented这部分内容相关。
![](images/0eb65a4fb37522c9a3442c9085146fed96ea97232326c6be46183924b6509b35.jpg)  
. SerieHTS

2 mitigations implemented   
图片摘要：该图片与Specific Power (kW/kg)；SerieHTS这部分内容相关。
![](images/5908eba4d109a0ec1b047e5e2d2735dbac91fc5ca515d6422da6055dc21ff197.jpg)  
Specific Power (kW/kg)

. SerieHTS

# Results – Permanent Magnet Rotors

• Tri-rotor (#5) can attain very high efficiency but requires considerable improvement to thermal management to meet specific power requirement   
• Disc-shaped G-10 vacuum & coolant vessels too thick magnetic field in stator too low

# Subcooled LNe

图片摘要：该图片与25 K inlet, 5 31 m3/hr, 1 bar；Subcooled LNe这部分内容相关。
![](images/0f9bf6dd763e321214f1c229089b2ad611006905e47be4514eff5005e739813f.jpg)  
25 K inlet, 5-31 m3/hr, 1 bar

图片摘要：该图片与Subcooled LNe；25 K inlet, 1 bar这部分内容相关。
![](images/dcf1a396f582bf9ed6105a599edda57ea7d4b48c1cfbd46dc9dd8ef44dec8250.jpg)

Subcooled LNe

25 K inlet, 1 bar

图片摘要：该图片与Config. 4；Did not close这部分内容相关。
![](images/628c5e11a2350f7918fdad46b1e81bed58c4d08b8b409cd36edc02085cb0fdf0.jpg)  
Config. 4

Did not close

• Rotor-stator-rotor (#8) performs much worse due to (a) thicker stator winding [larger impact of one-sided cooling] & (b) larger rotor heat load & mass

# Subcooled LNe

25 K inlet, 1 bar

图片摘要：该图片与Config. 7；Subcooled LNe这部分内容相关。
![](images/bff7a8230aa5456e29ec6aba76e969cb523e5a1aa7bc9f8e4d90623fdb116cdc.jpg)  
Config. 7

图片摘要：该图片与Subcooled LNe；25 K inlet, 1 bar这部分内容相关。
![](images/c53a3cba607183865af690720fd2e3dd28b26dd51d560ee73d1155058d07358b.jpg)

# Subcooled LNe

25 K inlet, 1 bar

图片摘要：该图片与Config. 8；• High performance with Litz wire这部分内容相关。
![](images/224e0e0cacd94a206010e20253ea3484961541fd48244da4a0aa8ff87265f2ca.jpg)  
Config. 8

图片摘要：该图片与• High performance with Litz wire；• Large drop in efficiency if Litz wire gauge 这部分内容相关。
![](images/86cc85b7e76718de13504e43f58d56efb5b032601b0a6f5b8af5b2dae76c0f14.jpg)

• High performance with Litz wire   
• Large drop in efficiency if Litz wire gauge reduced from 50 AWG to 40 AWG   
• Only modest (~3 kW/kg) drop in specific power if GHe used instead of LNe

图片摘要：该图片与Config. 6；Subcooled LNe这部分内容相关。
![](images/fd3082ddba185f8e0d4bbbcbeb3ef12593f834d1b1a6b37800c7a6f5690bec13.jpg)  
Config. 6

图片摘要：该图片与Subcooled LNe；25 K inlet, 5 32 m3/hr, 1 bar这部分内容相关。
![](images/ca560dc150772638d3a772ce88bdc7d6dfafb1b9e7247cfd39ee718e26965108.jpg)  
Subcooled LNe   
25 K inlet, 5-32 m3/hr, 1 bar

RRR97 Copper   
. 2212   
2212 Low Speed

图片摘要：该图片与Sensitivity to stator wire gauge (AWG)；for Cu (RRR 97) Litz这部分内容相关。
![](images/6294fdc804dd5dd4a6e563f277562a46fd798a200d3048d8cd5932b95f8c091a.jpg)  
Sensitivity to stator wire gauge (AWG)   
for Cu (RRR 97) Litz

图片摘要：该图片与Sensitivity to coolant for Cu (RRR 250) Litz；Conclusions这部分内容相关。
![](images/7b026db52ad7258ef2539a79392f512cd14e1702564f2b8e3ec5f103da2e21fa.jpg)  
Sensitivity to coolant for Cu (RRR 250) Litz

# Conclusions

• Most permanent magnet motors cannot meet requirement of 99.5% at 20 kW/kg due to low magnetic field & subsequent thermal challenge of cooling more heavily-excited stator winding

• New Helmholtz motor can overcome this & enable HTS stators

• Performance of axial flux motors can be improved if vacuum & coolant vessels can be stiffened

• Litz wire benefits from very fine strand diameters (Ø80 to Ø25 μm) & high slot fill factor $( \sim 5 0 \% )$

• Refined comparison of conductors will be completed after motor configuration down selected

• Results suggest …

• modest reductions in specific power occur if GHe used instead of LNe   
• Large reductions in efficiency occur if Litz wire gauge reduced from 50 AWG to 40 AWG

• Points of uncertainty

• AC loss in thick stacks of HTS   
• Rotary vacuum seals: power loss, constraints on leak rate & life

# Partially cryogenic motors with permanent magnet rotor

Highest performing:

# Helmholtz motor with HTS stator

(99.78% at 20 kW/kg • 99. $5 \%$ at 28.5 kW/kg)

<table><tr><td>Pros</td><td>Cons</td></tr><tr><td>• Simple rotor cooling
• No rotary vacuum seals
• Lighter / more efficient inverter (likely tolerates higher current distortion)</td><td>• Structural support of outer rotor &amp; stator more difficult
• Reliant on reducing emf for circulating currents (phase voltage constraint)</td></tr></table>

# Fully cryogenic motors with HTS rotor

Highest performing:

radial flux inner rotor with Cu Litz stator

(99.66% to ~99.75% at 20 kW/kg • 99.5% at

30 to ~40 kW/kg)

<table><tr><td>Pros</td><td>Cons</td></tr><tr><td>• Relatively easy rotor structure &amp; rotordynamics</td><td>• Requires 2 rotary vacuum seals (heat &amp; reliability concern)</td></tr><tr><td>• Lower cryogenic heat load</td><td>• Cryogenic rotor (cooling &amp; heat load concerns)</td></tr><tr><td></td><td>• Requires current supply with very low distortion</td></tr></table>

This work was funded by the Aircraft Electrification Subproject

Aeronautics Research Mission Directorate

Advanced Air Vehicles Program

Advanced Air Transport Technology Project

Aircraft Electrification Subproject

# Contact Info

{justin.j.scheidler, thomas.Tallerico, aaron.d.anderson-1, peter.e.kascak}@nasa.gov

# THANK YOU

图片摘要：该图片与• Develop a 5 MW superconducting motor system and demonstrate at subscale to ena这部分内容相关。
![](images/9d5c115f63b1cbedd8ba506dd720d9d2f8c35cc68215185d13861b2d11612a23.jpg)

• Develop a 5 MW superconducting motor system and demonstrate at subscale to enable new higher performance airplane architectures (TRL 3)   
• Design (2024 – 2028), build & test (2028 – 2030)

# Objectives

• Develop 5 MW Superconducting Machine Technologies (TRL-3)   
• Determine high power EAP aircraft and powertrain architectures

# Approach

• Explore fully superconducting and fully cryogenic machines to increase percentage electrification and meet weight targets at the airplane level   
• Design a 5 MW machine and drive   
• Demonstrate key tall poles for high power superconducting (stator cooling, noncontact rotor current supply, low AC loss, cost, flight-like requirements, etc.)   
• Support component-level work with system studies at all levels (power quality, thermal management, airplane performance)   
• Focus on solutions that support SAF and Hydrogen

Configuration 7 →

图片摘要：该图主要展示 3 "Distributed" stator topology. Windings have no skew in th。
![](images/6925ee381ce4984c807275fecac0a01923c77c20e652b5d81941f2e1c27bd0cb.jpg)  
Fig.3 "Distributed" stator topology. Windings have no skew in the active region of the machine and correspondingly complex end turn geometry.

Configuration 8 →

图片摘要：该图主要展示 3 "Distributed" stator topology. Windings have no skew in th。
![](images/012955f1eef347ec5b78486f14ed6a54a774cb8f084f80e83973c76bb2e14b57.jpg)  
Fig.4 "Zig-Zag" stator topology.Windings are skewed by approximately one pole arc in the active region of the machine in order to minimize end winding complexity and massat the cost of reduced torque production due to the winding skew.
