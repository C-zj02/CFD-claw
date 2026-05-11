# AIAA-2002-0840

# Drag Prediction for the DLR-F4 Wing/Body

# Using OVERFLOW and CFL3D on an Overset Mesh

J. C. Vassberg

Phantom Works

The Boeing Company

Long Beach, CA 90807, USA

P. G. Buning

Configuration Aerodynamics

NASA Langley Research Center

Hampton, VA 23681, USA

C. L. Rumsey

Computational Modeling and Simulation

NASA Langley Research Center

Hampton, VA 23681, USA

# 40th AIAA Aerospace Sciences Meeting & Exhibit

14-17 January, 2002 / Reno, NV

# Drag Prediction for the DLR-F4 Wing/Body using OVERFLOW and CFL3D on an Overset Mesh

John C. Vassberg*

Phantom Works

The Boeing Company

Long Beach, CA 90807, USA

Pieter G. Buning†

Configuration Aerodynamics

NASA Langley Research Center

Hampton, VA 23681, USA

Christopher L. Rumsey

Comp. Modeling and Simulation

NASA Langley Research Center

Hampton, VA 23681, USA

14-17 January,2002

# Abstract

This paper reviews the importance of numerical drag prediction in an aircraft design environment. A chronicle of collaborations between the authors and colleagues is discussed. This retrospective provides a road-map which illustrates some of the actions taken in the past seven years in pursuit of accurate drag prediction. The advances made possible through these collaborations have changed the manner in which business is conducted during the design of all-new aircraft.

The subject of this study is the DLR-F4 wing/body transonic model. Specifically, the work conducted herein was in support of the $1^{st}$ CFD Drag Prediction Workshop, which was held in conjunction with the $19^{th}$ Applied Aerodynamics Conference in Anaheim, CA during June, 2001.

Comprehensive sets of OVERFLOW simulations were independently performed by several users on a variety of computational platforms. CFL3D was used on a limited basis for additional comparison on the same overset mesh. Drag polars based on this database were constructed with a CFD-to-Test correction applied and compared with test data from three facilities. These comparisons show that the predicted drag polars fall inside the scatter band of the test data, at least for pre-buffet conditions. This places the corrected drag levels within $1\%$ of the averaged experimental values. At the design point, the OVERFLOW and CFL3D drag predictions are within $1 - 2\%$ of each other. In addition, drag-rise characteristics and a boundary of drag-divergence Mach number are presented.

# Nomenclature

AR Wing Aspect Ratio $= \frac{b^2}{S_{ref}}$

$a$ Acoustic Speed

$b$ Wing Span

CD Drag Coefficient $= \frac{Drag}{q_{\infty}S_{ref}}$

$C_L$ Lift Coefficient $= \frac{\text{Lift}}{90 S_{ref}}$

$C_{ref}$ Wing Reference Chord

count Drag Coefficient Unit = 0.0001

$D$ Drag

DPW Drag Prediction Workshop

e Oswald's Efficiency Factor

L Lift

$M$ Mach Number

RANS Reynolds-Averaged Navier-Stokes

Ren Reynolds number $= \frac{\rho_{\infty}V_{\infty}C_{ref}}{4\pi r}$

$S_{ref}$ Wing Reference Area

SFC Specific Fuel Consumption

W Weight

$Y^{+}$ Wall Distance $= \frac{\rho_{W}u_{y}}{\mu_{w}}$

q Dynamic Pressure $= \frac{1}{2}\rho V^2$

$\alpha$ Angle of Attack

$\Lambda_{c / 4}$ Wing Quarter-Chord Sweep

$\infty$ Signifies Freestream Conditions

# 1 Introduction

In reflection, as the 100-year anniversary of flight draws near, it is truly amazing just how far the industry has progressed. This rapid advance in the science, technology, and business of flight was made possible through a blend of competition and cooperation between industry rivals, government agencies, and academic institutions around the world. It is in this spirit that the Drag Prediction Workshop (DPW) was conducted [1]-[2]. Participants from six nations came together for a common goal - to assess the state-of-the-art of drag prediction using Computational Fluid Dynamics (CFD) methods based on the Reynolds-Averaged Navier-Stokes (RANS) equations.

Copyright ©2002 by Vassberg, Buning & Rumsey.

Published by the AIAA with permission.

Why is drag prediction so important to the industry of flight? In short, drag represents the irrecoverable aerodynamic losses associated with a flight-based mission. For example, consider the generic task of delivering a payload between distant city pairs. The Breguet-Range equation, which aptly applies to long-range missions of jet aircraft, is:

$$
R a n g e = \frac {M L}{D} \frac {a}{S F C} \ln \left(\frac {W _ {0} + W _ {f}}{W _ {0}}\right). \tag {1}
$$

Here, $M$ is the cruise Mach number, $L \& D$ are the aerodynamic forces of lift and drag, respectively, $a$ is the acoustic speed, $SFC$ is the specific fuel consumption of the engines, $W_{0}$ is the aircraft landing weight, and $W_{f}$ is the weight of fuel burned during the flight. The Breguet-Range equation illustrates the importance of drag prediction as a function of lift and Mach number in the context of aerodynamic design; it also provides a glimpse into the interplay between the various disciplines.

Referring to Eqn (1), one might assume that the aerodynamic efficiency of an aircraft is represented by $\frac{ML}{D}$ , the propulsion efficiency is embedded in $SFC$ , and that the structural efficiency directly impacts $W_{0}$ . Interestingly, historical trends of in-service transport aircraft indicate that very little improvement in the $\frac{ML}{D}$ metric has been accomplished in the past 50 years. Yet it would be somewhat naive to state that no aerodynamic advances have been made during this period. In actuality, improvements in aerodynamics have better served aircraft designs by trading them for improvements in other disciplines. For example, the ability to increase the thickness-to-chord ratio of a wing while maintaining $\frac{ML}{D}$ not only reduces the structural weight of the wing, it also provides additional fuel volume. In terms of Eqn (1), an aerodynamic improvement of this nature would manifest itself as a decrease in $W_{0}$ and an increase in $W_{f}$ with the net result being an increase in range. Reducing the aircraft's empty weight has the added benefit of reducing the cost of the vehicle. Obviously, this aerodynamic improvement would not be apparent in the trend charts of $\frac{ML}{D}$ .

Assume that an airline would like to provide a service between two cities with an aircraft that, when fully loaded with payload and fuel, is $1\%$ short on range. Since the aircraft is fuel-volume limited, the only recourse is to reduce the payload weight. In relative terms, a typical ratio of weights might have $W_{f} = \frac{2}{3} W_{0}$ and $W_{\text{payload}} = \frac{1}{6} W_{0}$ . In this scenario, Eqn (1) shows that the operator would have to reduce the payload (read revenue) by $7.6\%$ to recover the $1\%$ shortfall on range. Since most airlines operate on very small margins, this service most likely will no longer be a profit-generating venture. This

example illustrates that in the current business of flight, a $1\%$ delta in aircraft performance is a significant change. While improving an aircraft's performance by $1\%$ may not be a trivial task given the usual constraints, losing $5\%$ is easily done if attention is not paid to detail (e.g., juncture flows, external doublers, gaps, etc.).

Now consider a more typical case where the aircraft does not suffer from a shortfall on range. In round numbers, the Direct Operating Costs (DOC) of a transport aircraft can be itemized as: $50\%$ for the cost of ownership, $20\%$ for fuel burn, $20\%$ for crew salaries and maintenance, and $10\%$ for miscellaneous other items. From an airline's perspective, if the DOC of its fleet of aircraft could be reduced by $5\%$ with a new design (while providing the same set of services to its customers), the airline would most likely retire its entire fleet and replace it with the new aircraft [3].

So how can aerodynamics be leveraged to improve the economics associated with a flight-based mission? A simplified high-lift-system design that retains $\frac{L}{D}$ and $C_{Lmax}$ reduces manufacturing and maintenance costs as well as part count. Increasing the cruise Mach number without reducing $\frac{ML}{D}$ reduces the time-dependent costs such as crew and maintenance. And the classic, increasing $\frac{ML}{D}$ without penalizing the other disciplines reduces fuel burn. These are just a few examples of how aerodynamic advances can have an impact on DOC...and all of these require accurate drag predictions.

To push aerodynamic technologies forward, it is becoming more important that accurate drag prediction become a consistent product of the CFD community. Once this prerequisite is accomplished, the full benefits of automated aerodynamic shape optimization may begin to be realized.

With the various on-going design programs, these are exciting times for the aircraft industry. A prime example is the Blended-Wing-Body (BWB) which has established a renaissance in the design of a family of all-new aircraft [4]. This revolutionary concept is enabling aerodynamic advances in all of the above areas, and then some. It presents challenges, yet offers significant opportunities, and as a result, a $5\%$ reduction in DOC is within grasp. Suffice it to say that aerodynamics is not a sunset technology, but rather, it is as important today as it was a century ago; only the stakes have changed.

# 2 Background

The first and second authors embarked on a collaborative effort which began in late 1994. Specifically, this study was to determine what was required to

obtain accurate drag results from the OVERFLOW code [5]. At that time, a typical simulation for a commercial transport configuration yielded a drag error of about 100 counts, where the total drag of the aircraft was nominally 300 counts. Results for the High-Speed Research (HSR) platforms were even worse; computed drag values were occasionally negative. Clearly, that state-of-the-art was quite unacceptable. In fact, there were prominent members of the aerodynamics community at large who felt that accurate drag predictions from RANS-based CFD methods might never be accomplished. Nonetheless, a systematic study of gridding guidelines proved to be the key, and by mid 1995 the errors in computed absolute drag values for pre-buffet cruise conditions approached the $1 - 3\%$ level. This collaboration, along with the NASA Advanced Subsonic Transport (AST) Program cooperative work with (then) McDonnell Douglas Aerospace-West [6], was the catalyst for the development of the 7-zone grid system for wing/body configurations with the signature collar grid at the wing/body juncture. These gridding guidelines were used as the basis for the DPW baseline grids, and will be discussed later in the paper. However, the end result was that the size of a grid suitable for accurate drag prediction was nominally 4-5 times larger than that previously used. In addition, the number of iterations required for convergence on drag rather than pressures also jumped by a factor of 2-5, depending on the case. Hence, the cost of OVERFLOW simulations for drag prediction increased by more than an order-of-magnitude relative to those used for the calculation of pressure distributions.

In another collaborative effort which began in early 1995, the first two authors agreed that a parallel version of OVERFLOW for distributed processing was in order. The original parallel code was based on the Parallel Virtual Machine (PVM), and more recently, has been ported to use the MessagePassing Interface (MPI) [7]. For more than five years, the Aerodynamic Design group in Long Beach, CA has almost exclusively used a parallel version of OVERFLOW on distributed clusters for production overset-grid CFD simulations. A parallel-processing capability such as this was necessary for accurate CFD drag predictions to be economically feasible in an aircraft design environment [8]. Turn-around time was further improved with the addition of grid sequencing and full multigrid to accelerate solution convergence [9].

The combination of the above two collaborations had an immediate impact on the B717-200 design (previously called the MD-95). Here, several aerodynamic fairing designs for various juncture flows were evaluated using OVERFLOW. In all cases, the predicted drag increments were later confirmed to be

extremely accurate in wind-tunnel tests [10]. In one particular case, a pocket of separated flow was identified in the numerical simulations just prior to a wind-tunnel entry. This prompted a flow-visualization run that confirmed the separation. Before the test was over, a fillet for this troublesome region was designed, fabricated with stereolithography, shipped to the wind tunnel, and tested.

In 1996, the first author invited a team of NASA personnel from the Ames and Langley Research Centers to participate in the aerodynamic design of the MD-XX trijet aircraft. The NASA group worked on-site and fully integrated within the MD-XX team. Due to the successes of CFD drag prediction on the MD-95 program, the MD-XX Design Office elevated the role and importance of CFD in the design environment. They did so by scheduling the freeze of the final loft lines of the cruise geometry several months prior to the first wind-tunnel test entry which would verify the aircraft's aerodynamic performance. Although this program was later cancelled, it marked a dramatic change in the manner in which business is conducted in the design of an all-new aircraft. This philosophy lives on today in advanced programs such as the Blended-Wing-Body [4], [11].

The lessons learned in the above efforts have been augmented with subsequent studies on drag prediction conducted under various programs and extended to other CFD methods such as CFL3D [12], SYN107 [13]-[14], and TLNS3D [15]. Within Boeing Phantom Works Long Beach, OVERFLOW remains the work-horse for complex transport configurations, CFL3D is heavily used on the BWB and re-entry vehicle programs, while SYN107 and TLNS3D round out the tool chest by providing aerodynamic shape optimization capabilities.

Since 1995, while the errors in predicted absolute drag have stabilized, the complexity of the configurations being analyzed has consistently increased. Today, the size of an overset grid system for a complete B747-400 configuration (comprised of a cruise wing, fuselage, pylons, flow-through bifurcated fan and core cowls, winglets, vertical and horizontal tail components) is approximately 20 million nodes. Furthermore, these simulations are being performed with the aircraft trimmed to specified center-of-gravity locations. After correcting for excrescences, internal cowl drags, etc., comparisons with flight test data have confirmed that the numerically predicted absolute drag values are within the band of uncertainties.

The next challenge for drag prediction is to improve the level of accuracy for post-buffet cruise conditions as well as for high-lift configurations. Improved high-lift drag prediction may become critical to achieve the pending more-stringent environmental requirements on take-off and landing noise.

Unfortunately, current state-of-the-art RANS-based CFD methods cannot consistently predict accurate pressures for these flows. Until this is accomplished, there is little hope that accurate drag values will be attained here as well. An accomplishment of this magnitude will likely be possible only through the cumulative work of many collaborative efforts such as those aforementioned.

The works noted above were conducted by a multitude of individuals, including the authors, under numerous collaborations between Boeing Phantom Works Long Beach and the NASA Ames and Langley Research Centers. A subset of those who were involved are: Dan Bencze, Bob Biedron, Dick Campbell, William Chan, Roger Clark, Susan Cliff, Mark DeHaan, Lie-Mine Gea, Robb Gregg, James Hager, Ray Hicks, Rick Hooker, Dennis Jespersen, Steve Krist, Steve Mysko, Bob Narducci, Mike Olsen, Rick Potter, Stuart Rogers, Dino Roman, Tony Sclafani, Jeff Slotnick, Richard Wahls, and Mark Whitlock.

# 3 DLR-F4 Geometry

The case chosen for the DPW is the DLR-F4 wing/body configuration [16]. Several factors were considered in the decision to use this geometry as the test-bed for the workshop. One factor was the availability of test data from multiple wind-tunnel facilities. Another was that this configuration is representative of current transonic transport aircraft.

The general layout of the DLR-F4 is provided in Figure 1. This configuration is typical of a transonic aircraft designed to cruise at $M = 0.75$ . The wing quarter-chord is swept $25^{\circ}$ with a leading-edge sweep of $27.1^{\circ}$ and an outboard trailing-edge sweep of $18.9^{\circ}$ . The 9.5 aspect-ratio wing is rigged with a dihedral angle of $4.8^{\circ}$ . Its planform is void of a leading-edge glove, yet includes a yehudi which extends to $40\%$ semispan, completely unsweeping the trailing edge of the inboard wing. This planform is representative of wings that accommodate retractable main landing gear. The airfoil sections are supercritical with thickness-to-chord ratios of $14.9\%$ at the side-of-body, reducing to $12.2\%$ outboard. The wing trailing edge has a blunt base of $0.5\%$ local chord. Figures 2-3 provide the thickness and camber distributions, as well as the geometry, for the root and outboard airfoil sections, respectively. The wind-tunnel model has a wing semispan of $585.7mm$ , a mean aerodynamic chord of $141.2mm$ , a reference area of $145,400mm^2$ , and reference center at $x = 504.9mm$ . The fuselage length is $1,192mm$ . Its constant barrel section has a diameter of $148.42mm$ , which begins at $x = 250mm$ and extends to $x = 626mm$ . No special fillets are incorporated at the wing-body

juncture, yielding a sharp corner everywhere on the intersection line. The DPW geometry also includes the aeroelastic twist of the wind-tunnel model under a loading which corresponds to the nominal cruise condition of $M = 0.75$ and $C_L = 0.5$ , with a dynamic pressure of $q = 43,434Pa$ .

# 4 DPW Overset Grid

The overset mesh generated for the DPW was based on the original process developed in 1995. The grid is comprised of 7 zones, 4 of which conform to the geometry and three box grids that transition the system to the farfield boundary. The 4 conforming grids define the volumes next to the fuselage, the wing-body juncture, the wing, and the wingtip. Two intermediate boxes surround the fuselage and wing geometries, while the remaining farfield box extends outward about 150 reference-chord lengths.

For this exercise, the surface grids were constructed using Gridgen-V13 [17] and are depicted in Figure 4. These surface grids were then extruded outward using HYPGEN [18] to generate the 4 surface-abutting volume grids. Figure 5 shows a close-up of the wingtip grid. Figures 6-7 illustrate the collar grid at the wing-body juncture.

The hole-cutting and fringe-point coupling steps were performed manually using GMAN [19]. The overlap and blanking of the meshes near the wing's mid-chord are shown in Figure 8.

On the wing surface, the chordwise spacing at both the leading and trailing edges is approximately $0.1\%$ local chord. The trailing-edge base is defined with 5 evenly-spaced points. The wake is represented with 65 points in the streamwise direction. The spanwise spacing is about $1\%$ semispan at the root and $0.1\%$ at the tip. On the fuselage nose and after-body, the maximum grid spacing is nominally $5mm$ . In the direction normal to the viscous surfaces, the first-layer spacing is about $0.001mm$ , which corresponds to $Y^{+} \simeq 1$ . Also in this direction, the maximum growth rate of the grid spacing is 1.24. Figure 9 provides an itemization of the individual grid dimensions, surface points, total grid points, and non-blanked real points. The complete grid system is comprised of 3,231,377 real points, with 54,445 residing on the viscous surfaces.

The guidelines used to generate the DPW overset mesh purposely omitted two gridding rules; these will be discussed now for completeness. The first is related to the manner in which OVERFLOW computes skin-friction drag. For this calculation to be second-order accurate, the first two layers of the grid normal to viscous walls must be evenly spaced. While this rule was not strictly enforced, the spacing ra

tios of the first two layers were fairly close to unity. The second rule is related to the grid resolution at a blunt trailing-edge base. Here, it is the first author's standard practice to include a trailing-edge cap grid that wraps around the blunt base in a C-clamp fashion. This grid normally has half of the cells on the base and the remaining cells evenly split between the upper and lower surfaces. It normally extends about $5 - 10\%$ upstream of the trailing edge. However, in the case of the DLR-F4 wing where the gradients near the trailing edge are relatively benign, inclusion of a high-resolution cap grid is probably not required for accurate drag prediction.

One final note. After the DPW was held, the Long Beach Aerodynamic Design group has finally transitioned from GMAN to PEGASUS-V5 [20] to provide semi-automatic hole-cutting and fringe-point coupling capabilities. There were several reasons for this lag, most were related to drag prediction. With that being said, the current parallel version of PEGASUS-V5 has proved to be a very useful tool, and one now appropriate for drag prediction. Further, it will continue to improve through the on-going collaborations within the PEGASUS community.

# 5 Wind-Tunnel Test Data

The DLR-F4 model was tested in three European facilities: NLR-HST, ONERA-S2MA, and DRA-8x8. The repeatability of these facilities was on the order of $\pm 5$ counts. While the AGARD AR-303 report [16] presented this data, an unfortunate element of this documentation was that the drag coefficients were only tabulated to three decimal places. Hence, the archived public-domain data has an effective scatter band of $\pm 10$ counts.

In an attempt to alleviate the uncertainty introduced by the truncation, the first author postprocessed the public-domain data with two filters. The first data enhancement augmented the drag coefficients with the coefficients of axial and normal forces. This process reduced the uncertainty of the tabulated values from the original 5 counts, down to as small as 0.8 counts, depending on the case. The second data enhancement was a careful digitization of the drag polar figure in the AGARD report. This digitization was also checked to be consistent with the reduced uncertainty bands derived by the first enhancement process. The resulting wind-tunnel drag polars are provided in Figure 10. A more detailed explanation of these filters can be found in the Data Enhancement presentation on the DPW website [1].

The enhanced wind-tunnel test data for $M = 0.75$ has been collapsed to a curve, by fitting a limited

range of the data to an equation of the following form.

$$
C _ {D} = C _ {D 0} + \frac {C _ {L} ^ {2}}{\pi * e * A R}. \tag {2}
$$

Here, $C_{D0}$ and $e$ are the free coefficients of the curve fit and the aspect ratio of the DLR-F4 wing is $AR = 9.437262$ . Including data from all three tests, but limited to the lifting range of

$$
0. 2 \leq C _ {L} \leq 0. 5 5, \tag {3}
$$

a least-squares curve fit yields $C_{D0} = 0.018388$ and $e = 0.829146$ . Eqn (2) now becomes:

$$
C _ {D} = 0. 0 1 8 3 8 8 + \frac {C _ {L} ^ {2}}{2 4 . 5 8 2 5 5}, \tag {4}
$$

and is applicable for the $C_L$ range given in Eqn (3). The curve fit given by Eqn (4) and associated test data are provided in Figure 11.

Since Case 1 of the DPW exercise is to compute the drag at $M = 0.75$ , $Ren = 3M$ , and $C_L = 0.5$ , it might be of interest to apply Eqn (4) to this condition, which yields:

$$
C _ {D} = 0. 0 1 8 3 8 8 + \frac {0 . 5 ^ {2}}{2 4 . 5 8 2 5 5} = 0. 0 2 8 5 6. \tag {5}
$$

The drag polars presented in the next section use the enhanced wind-tunnel data, rather than data taken directly from the AGARD AR-303 report.

# 6 Results

Included in this section are comprehensive sets of OVERFLOW solutions which were performed on the DPW baseline overset mesh. Also included is a limited set of data generated by CFL3D on the same overset mesh for additional comparison. A more complete set of CFL3D solutions for the DPW baseline 1-to-1 multiblock mesh is documented by the third author in Reference [21].

For the DPW exercise, the authors purposely did not coordinate with each other in an attempt to obtain independent results on the DLR-F4 configuration. In spite of this, the first two authors ran OVERFLOW with essentially the same set of critical input parameters. Both used central difference scalar dissipation with the Spalart-Allmaras (SA) turbulence model. However, slightly different versions of OVERFLOW were run, different computer platforms were utilized at different levels of precision, and different methods to converge on lift were employed. It is good to report that these differences yielded no noticeable variations in the computed forces, moments or pressures.

The first author ran full convergence on all solutions, starting each solution from a uniform flow

at freestream conditions. Full multigrid acceleration was used with 150 iterations in both the coarse and intermediate meshes, and 3,000 iterations in the fine mesh. All solutions were run by specifying an angle-of-attack, even when a specific lifting condition was desired. All computations were performed using 64-bit precision. Version $1.8\mathrm{m}$ was run in parallel using MPI on a cluster of 6 Hewlett-Packard C3610 workstations, each with 2 GB of RAM, and connected with a switched 100BaseT ethernet. Each solution required about 13 hours of wall-clock time. Alpha sweeps were conducted at 10 Mach numbers, then these data were interpolated on $C_L$ to derive the required alphas for $C_Ls$ of 0.3, 0.4, 0.5, and 0.6. In all, a total of 53 OVERFLOW solutions were performed to obtain drag polars at the 10 Mach numbers. To define the drag-rise curves, the drag polars were interpolated on $C_L^2$ to obtain the corresponding $C_D$ values.

The second author and colleagues ran some cases with a fixed angle-of-attack and some with a specified lift-coefficient. All computations were performed using 32-bit precision. Version 1.8s was run in parallel on three different computer platforms, an SGI Octane with 2 processors, an SGI Origin using 8 processors, and a cluster of 6 Compaq XP-1000 machines. Wall-clock timings for these systems were 18.5 hours, 7.5 hours, and 6 hours per 1,000 fine-mesh iterations, respectively.

For a limited set of conditions on the overset mesh, the third author ran CFL3D with $3^{rd}$ -order upwind differencing with Roe flux difference splitting and using the SA model. These solutions were converged 4,800 multigrid iterations on the fine grid only, and were run by specifying an angle-of-attack. A non-dedicated SGI Origin was used with one processor, requiring approximately 270 hours of wall-clock time per solution.

Figures 12-13 illustrate the OVERFLOW convergence histories of lift and drag, respectively, for a freestream condition of $M = 0.75$ , $Ren = 3M$ , and $\alpha = -1^{\circ}$ , which yields $C_L = 0.409$ and $C_D = 263.3$ counts. These forces have essentially converged by 2,000 iterations on the fine mesh. Note the scale on these figures; lift increments are 0.002 and drag increments are a count.

Figures 14-15 provide a similar set of OVERFLOW convergence histories, however, these correspond to the cruise lifting condition of $C_L = 0.5$ with corresponding $C_D = 295.6$ counts. Unlike the previous condition, these forces continue to oscillate through all 3,000 iterations, albeit at very small amplitudes. The cause of these fluctuations is a small pocket of separated flow that appears near the trailing edge of the wing-body intersection; see Figure 16.

Figure 17 provides a comparison of pressure distri

butions between OVERFLOW and test data at the cruise design point of $M = 0.75$ and $C_L = 0.5$ . Note that the leading-edge peaks are missed because of the difference in alphas between the numerical simulation and the tests. Also, the isobars in this figure hint to the small pocket of flow separation on the upper-surface near the root trailing edge.

An important aspect of comparing results from OVERFLOW and CFL3D on the overset mesh is to estimate variation due to choice of CFD code. Figure 18 shows a comparison of pressure distributions at $M = 0.75$ and $\alpha = 0^\circ$ . At this $\alpha$ -matched condition, results are very close and computed leading-edge peaks better match the test data. The lift, drag and moment comparisons are provided in Table 1. Additional documentation on variations due to CFD method can be found in Reference [22].

Table 1: OVERFLOW and CFL3D Comparison at $M = 0.75$ , $Ren = 3M$ , and $\alpha = 0^\circ$ .   

<table><tr><td></td><td>CL</td><td>CD(counts)</td><td>CM</td></tr><tr><td>OVERFLOW</td><td>0.532</td><td>309.6</td><td>-0.1614</td></tr><tr><td>CFL3D</td><td>0.535</td><td>313.0</td><td>-0.1653</td></tr></table>

Case 1 of the DPW asked that all participants compute a solution for the cruise design point of $M = 0.75$ , $Ren = 3M$ , and $C_L = 0.5$ . The second author and two colleagues independently ran this case and included solutions with 3rd-order Roe upwind as well. Combined with the first author's data, these results are provided in Table 2.

Table 2: DPW Case 1 OVERFLOW Results.   

<table><tr><td>Alpha (deg)</td><td>CD(counts)</td><td>Type</td></tr><tr><td>-0.260</td><td>295.6</td><td>Central</td></tr><tr><td>-0.258</td><td>295.8</td><td>Central</td></tr><tr><td>-0.257</td><td>295.9</td><td>Central</td></tr><tr><td>-0.254</td><td>296.0</td><td>Central</td></tr><tr><td>-0.241</td><td>292.6</td><td>Roe</td></tr><tr><td>-0.238</td><td>292.9</td><td>Roe</td></tr></table>

This table shows that the independent assessments of drag using a consistent differencing scheme were within $\pm 0.2$ counts of the average. Correcting for the variation of $C_L$ (which occurs in the $4^{th}$ decimal place) collapses the variations in drag to an insignificant number. The variation between central differencing and Roe upwinding is $\simeq 3$ counts, with Roe yielding the lower drag.

While a CFL3D solution for $C_L = 0.5$ was not computed on the overset mesh, Table 3 contains data which stradle this condition, and include interpolated values for $\alpha$ (based on $C_L$ ) and $C_D$ (based on $C_L^2$ ). This table shows that the interpolated CFL3D result yields a drag level approximately 2-5 counts higher than OVERFLOW at the design point.

Table 3: CFL3D Results.   

<table><tr><td>Alpha (deg)</td><td>CD(counts)</td><td>CL</td></tr><tr><td>-1.000</td><td>266.0</td><td>0.416</td></tr><tr><td>-0.294</td><td>298.0</td><td>0.500</td></tr><tr><td>0.000</td><td>313.0</td><td>0.535</td></tr></table>

Figure 19 provides the OVERFLOW computed drag polar for $M = 0.75$ and includes the wind-tunnel data for reference. The data in this figure are inconsistent in that the numerical simulations were performed assuming fully-turbulent flow, while the tests allowed laminar runs of $5 - 15\%$ chord on the wing's upper surface and $25\%$ chord on the wing's lower surface. Figure 20 shows the transitions pattern used in the tests.

To assess the impact on drag caused by this difference, FLO22 [23]-[24] was used to generate drag polars of fully-turbulent flows and flows tripped with the pattern of Figure 20. These results are shown in Figure 21. Also shown in this figure are least-squares curve fits of the polars. When differenced, these curve fits yield a shift in drag of

$$
C _ {D s h i f t} = 1 3. 7 - 2. 3 * C _ {L} ^ {2} \text {c o u n t s}. \tag {6}
$$

Hence at $C_L = 0.5$

$$
\begin{array}{l} C _ {D s h i f t} (0. 5) = 1 3. 7 - 2. 3 * 0. 5 ^ {2} \\ = 1 3. 1 \text {c o u n t s}. \tag {7} \\ \end{array}
$$

Applying the correction of Eqn (6) to the fully-turbulent OVERFLOW and CFL3D results yields the drag polars depicted in Figure 22. Once the effect of transition is taken into consideration, the numerically predicted results lie within the scatter of the experimental data.

If the cruise point is reviewed, the drag predictions with the correction of Eqn (7) become:

$$
\begin{array}{l} C _ {D o v e r f l o w c o r r e c t e d} = 0. 0 2 8 2 5, \\ C _ {D c f l 3 d - v 6 c o r r e c t e d} = 0. 0 2 8 4 9. \tag {8} \\ \end{array}
$$

Comparing Eqns (8) with Eqn (5) shows only a $1\%$ difference in drag levels between CFD and experiment.

During the DPW, Schwamborn and Sutcliffe presented a result using the DLR-TAU code which also addressed this CFD-to-Test difference. Their presentation is available on the DPW website [1]. On page 5, the data labeled Case 3 and Transition indicate that at $C_L = 0.5$ , the correction is:

$$
C _ {D \text {s h i f t}} (0. 5) \simeq 1 2 \text {c o u n t s}. \tag {9}
$$

Eqns (7) & (9) are very consistent with each other and are independent estimates of the effects on drag of the laminar runs vs. fully-turbulent flows.

Figure 23 illustrates the drag-rise curves as predicted by the OVERFLOW solutions. From bottom-to-top, the four curves of this figure correspond to $C_L = 0.3$ , 0.4, 0.5, and 0.6, respectively. Also included in this figure is a cross-plot curve, depicted by the dotted line, which illustrates the drag-divergence Mach number for the DLR-F4. The definition of $M_{dd}$ is taken to occur when the drag-rise slope is $dC_D / dM = 0.05$ . Using these results, the drag-divergence boundary is determined and is shown in Figure 24.

The above definition of $M_{dd}$ is motivated partially by the Breguet-Range Eqn (1), and by economic forces (related to block times) that push the operating Mach number upward towards the 99% Long-Range-Cruise (LRC) point. From Figure 24, it appears that the DLR-F4 wing is capable of cruising in excess of $M = 0.775$ at the lifting condition of $C_L = 0.5$ . However, these estimates have all been made at a wind-tunnel Reynolds number, rather than at flight.

# 7 Conclusions

The importance of drag prediction within an aircraft design environment is reviewed. A seven-year retrospective of collaborations is given which illustrates some of the steps taken by the authors and colleagues in pursuit of accurate drag predictions. The successes of this body of work have had a significant impact on the manner in which all-new aircraft designs are approached.

The DLR-F4 wing/body configuration has been analyzed by OVERFLOW and CFL3D using an over-set mesh. This study focused on the prediction of drag as a function of lift and Mach number for a wind-tunnel Reynolds number of $3M$ based on reference chord. For pre-buffet conditions, results presented herein show that the numerical drag predictions are within $1\%$ of the averaged wind-tunnel data, and the OVERFLOW and CFL3D drag predictions are within $1 - 2\%$ of each other. This level of uncertainty is comparable to that of the wind-tunnel data itself.

Comprehensive sets of OVERFLOW simulations were independently performed by several users, on a variety of computational platforms. These solutions spanned 10 Mach numbers from 0.5 to 0.82. By coincidence, most of these solutions used central differencing, scalar dissipation and the Spalart-Allmaras turbulence model. However, a variety of parallel computational platforms were used, a mixture of single and double precision simulations were performed, and slightly different versions of OVERFLOW were applied. It is good to say that the vari

ation of these results are negligible. In addition, a few computations were performed with Roe upwind ing. The difference in drag levels between the two differencing stencils is on the order of $1\%$ .

The Drag Prediction Workshop called for the CFD calculations to be performed fully turbulent. The available wind-tunnel data, however, was tripped at $5 - 15\%$ on the wing upper surface and $25\%$ on the lower surface. Corrections for the CFD-to-Test differences were estimated using FLO22, running semicomplete polars for both flows. The study derived a correction of about 13 counts at the design point. This is comparable to a similar and independent study based on the DLR-TAU code. Drag polars based on OVERFLOW were constructed with the CFD-to-Test corrections and compared with wind-tunnel test data. These comparisons show that the predicted polars fall within the scatter band of the test data, at least for pre-buffet conditions.

Four drag-rise curves were constructed from the OVERFLOW solutions. Using a slope definition for drag-divergence Mach number, the $M_{dd}$ boundary for the DLR-F4 wing/body was constructed.

In future workshops, a grid-resolution study should be included by providing a series of parametrically-consistent meshes of varying resolution. Post-processing the results from such a sequence using Richardson extrapolation will provide further insight into the resolution required for a desired level of accuracy, at least for the case being investigated.

# Acknowledgment

The authors acknowledge The Boeing Company and The National Aeronautics and Space Administration for their support in the Drag Prediction Workshop, and for providing a working environment that not only allows, but encourages the numerous collaborative studies that have and will continue to occur between the two institutions.

The second and third authors would like to acknowledge S. Melissa Rivers, Joseph H. Morrison, and Robert T. Biedron of the NASA Langley Research Center, for their contributions to the authors' respective Drag Prediction Workshop presentations.

# References

[1] AIAA CFD Drag Prediction Workshop Website. http://www.iaaa.org/te/apa/dragpredworkshop/dpw.html, June 2001.   
[2] D. W. Levy, J. C. Vassberg, R. A. Wahls, T. Zickuhr, S. Agrawal, S. Pirzadeh, and M. J.

Hemsch. Summary of data from the first AIAA CFD Drag Prediction Workshop. AIAA paper 2002-0841, Reno, NV, January 2002.   
[3] J. C. Vassberg and R. D. Gregg. Overview of aerodynamic design for transport aircraft. Presentation, First M.I.T. Conference on Computational Fluid and Solid Mechanics, Cambridge, MA, June 2001.   
[4] R. H. Liebeck. Design of the Blended-Wing-Body subsonic transport. Wright Brothers Lecture, AIAA paper 2002-0002, Reno, NV, January 2002.   
[5] P. G. Buning, D. C. Jespersen, T. H. Pulliam, G. H. Klopfer, W. M. Chan, J. P. Slotnick, S. E. Krist, and K. J. Renze. OVERFLOW User's Manual, Version 1.8L. Technical report, NASA, July 1999.   
[6] L. M. Gea, N. D. Halsey, G. A. Intemann, and P. G. Buning. Applications of the 3-D Navier-Stokes code OVERFLOW for analyzing propulsion-airframe integration related issues on subsonic transports. In Proceedings of 19th Congress of the International Council of the Aeronautical Sciences (ICAS '94), number ICAS-94-3.7.4, pages 2420-2435, Anaheim, CA, September 1994.   
[7] D. C. Jespersen. Parallelism and OVERFLOW. NAS Technical Report NAS-98-013, NASA Ames Research Center, October 1998. http://www.nas.nasa.gov/Research/Reports /Techreports/1998/PDF/nas-98-013.pdf.   
[8] J. Conlon. OVERFLOW code empowers Computational Fluid Dynamics. InSights Issue 5, NASA High-Performance Computing and Communications Program, Moffett Field, CA, April 1998.   
[9] D. C. Jespersen, T. H. Pulliam, and P. G. Bunning. Recent enhancements to OVERFLOW. AIAA paper 97-0644, AIAA 35th Aerospace Sciences Meeting, Reno, NV, January 1997.   
[10] J. C. Vassberg. CFD-Based Design. Presentation, Stanford University, Palo Alto, CA, February 2000. Graduate Seminar Series.   
[11] D. L. Roman, J. B. Allen, and R. H. Liebeck. Aerodynamic design challenges of the Blended-Wing-Body subsonic transport. AIAA paper 2000-4335, Denver, CO, August 2000.   
[12] S. L. Krist, R. T. Biedron, and C. L. Rumsey. CFL3D User's Manual. NASA-TM 1998-208444, NASA, June 1998. Version 5.0.

[13] A. Jameson and J. C. Vassberg. Computational fluid dynamics for aerodynamic design: Its current and future impact. AIAA paper 2001-0538, Reno, NV, January 2001.   
[14] J. C. Vassberg and A. Jameson. Aerodynamic shape optimization of a Reno race plane. *Int'l Journal of Vehicle Design*, 28(4):318-338, 2002. Special Issue on: Design Sensitivity and Optimization.   
[15] G. Kuruvilla, R. P. Narducci, and S. Agrawal. Development and application of TLNS3D-Adjoint: A practical tool for aerodynamic shape optimization. AIAA paper 2001-2400, Anaheim, CA, June 2001.   
[16] G. Redeker. DLR-F4 wing-body configuration. In A Selection of Experimental Test Cases for the Validation of CFD Codes, number AR-303, pages B4.1-B4.21. AGARD, August 1994.   
[17] Gridgen user manual version 13. Technical report, Pointwise, 1998.   
[18] W. M. Chan, I. T. Chiu, and P. G. Buning. User's manual for the HYPGEN hyperbolic grid generator and the HGUI graphical user interface. NASA-TM 108791, NASA, October 1993.   
[19] T. D. Gatzke, W. F. LaBozzetta, G. P. Frin-frock, J. A. Johnson, and W. W. Romer. MACGS: A zonal grid generation system for complex aero-propulsion configurations. *AIAA Paper* 91-2156, June 1991.   
[20] N. E. Shus, W. E. Dietz, S. M. Nash, M. D. Baker, and S. E. Rogers. PEGASUS user's manual version 5.1c. Technical report, MICRO CRAFT, July 2000.   
[21] C. L. Rumsey and R. T. Biedron. Computation of flow over a drag prediction workshop wing/body transport configuration using CFL3D. NASA-TM 2001-211262, NASA, December 2001.   
[22] C. L. Rumsey, D. O. Allison, R. T. Biedron, P. G. Buning, T. G. Gainer, J. H. Morrison, S. M. Rivers, S. J. Mysko, and D. P. Witkowski. CFD sensitivity analysis of a modern civil transport near buffet-onset conditions. NASA-TM 2001-211263, NASA, December 2001.   
[23] A. Jameson. Transonic potential flow calculations using conservative form. In Proceedings of AIAA 2nd Computational Fluid Dynamics Conference, pages 148-161, June 1975.

[24] P. A. Henne and R. M. Hicks. Wing analysis using a transonic potential flow computational method. NASA-TM 78464, July 1978.

图片摘要：该图主要展示 1: General Layout of the DLR F4 Model。
![](images/f64d0444678e063dfdc5e8b6ce7d3818138d0ce0c9d9765692358ebe93c13533.jpg)  
Figure 1: General Layout of the DLR-F4 Model.

# DLR-F4 Airfoils

图片摘要：该图主要展示 1: General Layout of the DLR F4 Model。
![](images/4153fd2a2f787452b96bd6d079f42534548fbf68b762e1b92abc5be79cb22fdd.jpg)  
Airfoil Geometry -- Camber & Thickness Distributions   
Figure 2: Root Airfoil Section of the DLR-F4 Model.

# DLR-F4 Airfoils

图片摘要：该图主要展示 2: Root Airfoil Section of the DLR F4 Model。
![](images/f11d19c876fb299c19543f7339575a9668174f83ef235a9c7661fbe46f973220.jpg)  
Airfoil Geometry -- Camber & Thickness Distributions   
Figure 3: Outboard Airfoil Section of the DLR-F4 Model.

图片摘要：该图主要展示 3: Outboard Airfoil Section of the DLR F4 Model。
![](images/cc701be2abe7118573b62174a8af733b287eee7d24bc9cc963f71b2493c07cde.jpg)  
Figure 4: Four Grids Defining the Wing/Body/Wake Surfaces

图片摘要：该图主要展示 4: Four Grids Defining the Wing/Body/Wake Surfaces。
![](images/0ae95fd69bc578a3e3a37453f90c1ee7332d5c65a54a2766845e9b0e620bdb90.jpg)  
Figure 5: Wing-Tip Grid

图片摘要：该图主要展示 5: Wing Tip Grid。
![](images/e6e82ed6f2ac5ee0297423298495ed9bf51813c5c4976596ac2b0f418fdc8b9d.jpg)  
Figure 6: Collar Grid Volume

图片摘要：该图主要展示 6: Collar Grid Volume。
![](images/95fa5d9f7439f9a400eddc4f9936692eaff0acd06cc0fe0c26535d4ef978ad29.jpg)  
Figure 7: Collar Grid on Fuselage Near Wing Trailing Edge

图片摘要：该图主要展示 7: Collar Grid on Fuselage Near Wing Trailing Edge。
![](images/221d9e798cdc78f30e5dd6bb69f5bb08479d245eb207dd2f161bbf0fbb876af9.jpg)  
Figure 9: Statistics of the DPW Baseline Overset Grid.

Figure 8: Field Grids Near Wing Mid-Chord Location

Total viscous-surface points: 54445  
Total grid points: 3727462  
Total non-blanked grid points: 3231377  
Grid points across the TE base 5  
Farfield boundary is a box $\sim 150$ chord lengths away.

```batch
grid id jd kd surfpts gridpts %pts realpts %real description 1 49 273 49 13377 655473 17.6 562499 17.4 fuselage 2 385 65 49 22209 1226225 32.9 1092327 33.8 collar 3 385 62 49 15934 1169630 31.4 1038606 32.1 wing 4 25 141 49 2925 172725 4.6 135219 4.2 wingtip 5 121 22 43 0 114466 3.1 76840 2.4 fuse_box 6 67 74 46 0 228068 6.1 168408 5.2 wing_box 7 75 39 55 0 160875 4.3 157468 4.9 global_box Totals: ---- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
```

图片摘要：该图主要展示 10: Enhanced Test Data Drag Polar for the DLR F4。
![](images/1503b4b1bf9fe543654e6d46d1d3448be7297ff1ee38244e8aa852f49aebe0ae.jpg)  
DLR-F4 WING /BODY GEOMETRY AGARD Report 303 - Figure 12   
Figure 10: Enhanced Test Data $M = 0.75$ Drag Polar for the DLR-F4.

图片摘要：该图主要展示 10: Enhanced Test Data Drag Polar for the DLR F4。
![](images/ca5d41e025e2590b0789fb0f770bf7216bbd02175cda0406723050b86a30500a.jpg)  
DLR-F4 WING / BODY GEOMETRY AGARD Report 303 Data   
Figure 11: Least-Squares Fit of the DLR-F4 Enhanced Test Data.

图片摘要：该图主要展示 11: Least Squares Fit of the DLR F4 Enhanced Test Data。
![](images/0a8e6c11d21f997142f90e961478714ed4be7e4d5f6825d82987bd8a9e73788f.jpg)  
DLR-F4 WING/BODY CONFIGURATION   
Baseline Over-Set Grid   
M = 0.75, REN = 3M, Alpha = -1.00, CL = 0.40864, CD = 0.026332   
LIFT COEFFICIENT   
Figure 12: Convergence History of Lift at $\mathrm{CL} = 0.409$ .

图片摘要：该图主要展示 12: Convergence History of Lift at。
![](images/d6dd2334ae945bc259d4b8d21617f008f298d779d6b8eff873991a6a30e955de.jpg)  
DLR-F4 WING/BODY CONFIGURATION   
Baseline Over-Set Grid   
Figure 13: Convergence History of Drag at $\mathrm{CL} = 0.409$ .

图片摘要：该图主要展示 13: Convergence History of Drag at。
![](images/5d37f531008a755506a6382a7e32014fcf0796149e0cc170391560ef2df44421.jpg)  
DLR-F4 WING/BODY CONFIGURATION   
Baseline Over-Set Grid   
Figure 14: Convergence History of Lift at $\mathrm{CL} = 0.500$ .

图片摘要：该图主要展示 14: Convergence History of Lift at。
![](images/26ff845d158668d700e00c3b19a072248ea44ffe138eae94c43e745a5510501c.jpg)  
Figure 15: Convergence History of Drag at $\mathbf{CL} = 0.500$ .

图片摘要：该图主要展示 15: Convergence History of Drag at。
![](images/e1d9494a3a916138ab458a6633dcfb266e061fe08b66431cda9077424ab4f671.jpg)  
Figure 16: Juncture-Flow Separation at Design Point.

图片摘要：该图主要展示 16: Juncture Flow Separation at Design Point。
![](images/e9a96bd206b30cef99630de5047d321b5eba14a8a329217f2cc267686b347391.jpg)  
COMPARISON OF CHORDWISE PRESSURE DISTRIBUTIONS DLR-F4 WING/BODY CONFIGURATION   
Figure 17: OVERFLOW Pressure Comparisons at Design Point.

Ren=3.e6, M=0.75, α=0 deg.

图片摘要：该图主要展示 17: OVERFLOW Pressure Comparisons at Design Point。
![](images/e521b7dafcf0a4cce71f6fd7e1c031c183c2719ed7a6e1409ae3a432ae90b51b.jpg)

图片摘要：该图主要展示 17: OVERFLOW Pressure Comparisons at Design Point。
![](images/63b154c9d48760d79b1ca118d6f72a61914411185e760f18502c8b5cc20acaac.jpg)

图片摘要：该图主要展示 17: OVERFLOW Pressure Comparisons at Design Point。
![](images/eec021106f2d092254923cf6c094630f33fd564fd8c9918c202f0e4c8a1ff4f6.jpg)

图片摘要：该图片与Figure 18: OVERFLOW and CFL3D Pressure Comparisons atRen=3.e6, M=0.75, α=0 deg这部分内容相关。
![](images/726c82d7a896efaac3fa14c15a3b2afd1743a0c6de8815dd7d5e85fa3bfe6e6a.jpg)

图片摘要：该图主要展示 18: OVERFLOW and CFL3D Pressure Comparisons at。
![](images/9bac96f652a2073a3b736c84760e7ccc1da4dd73e19618ba0e652828cb340080.jpg)

图片摘要：该图主要展示 18: OVERFLOW and CFL3D Pressure Comparisons at。
![](images/97ac96dd0258fdf18f681772ce522f102455db4dce5dcc9a3cdbe4a8f8db0f20.jpg)

图片摘要：该图主要展示 18: OVERFLOW and CFL3D Pressure Comparisons at。
![](images/c02d026b48e0e76bbc20a9b9d62b3fcb933853ea75e14afb4b24afbf871287da.jpg)  
Figure 18: OVERFLOW and CFL3D Pressure Comparisons at $\alpha = 0^{\circ}$ .

图片摘要：该图主要展示 18: OVERFLOW and CFL3D Pressure Comparisons atDLR F4 WING/BO。
![](images/4c540c65213dc75946a532f69d992dacecf471c2ca722ee59392b67f541a5905.jpg)  
DLR-F4 WING/BODY CONFIGURATION   
Baseline Over-Set Grid   
LIFT COEFFICIENT SQUARED   
Figure 19: Drag Polars of the DLR-F4 Wing/Body.

图片摘要：该图主要展示 19: Drag Polars of the DLR F4 Wing/Body。
![](images/3a6ede63c2dd8cfe2ce07dba072a18cc3e69dad7e7fa64c458da2b41ef567661.jpg)  
Figure 20: Transition Strips on DLR-F4 Wing/Body Model.

图片摘要：该图主要展示 20: Transition Strips on DLR F4 Wing/Body Model。
![](images/100638041d9eeee36f2a63ca700daa9f620adbef832bcbc357ad80469642f3f2.jpg)  
DLR-F4 WING/BODY CONFIGURATION CFD-TO-TEST CORRECTIONS   
Figure 21: FLO22 Drag Polars with and without Transition Trips.

图片摘要：该图主要展示 21: FLO22 Drag Polars with and without Transition Trips。
![](images/b6ad57c5672266b4fe1a901622936de7d1880ef28e17b9bdee00f29743631ef5.jpg)  
Figure 22: OVERFLOW Drag Polars with and without Transition Corrections.

图片摘要：该图主要展示 22: OVERFLOW Drag Polars with and without Transition Correct。
![](images/0271f88bfa776399bba86f63b32a23da88a8211b8e504516eba32c261253b7c9.jpg)  
DLR-F4 WING/BODY CONFIGURATION   
Baseline Over-Set Grid   
Figure 23: Predicted Drag Rise for the DLR-F4 Wing/Body.

图片摘要：该图主要展示 23: Predicted Drag Rise for the DLR F4 Wing/Body。
![](images/57ed60f451044bc8d71b0235bf73aba4c1c9e9b7d1af3a989814968c57f17abc.jpg)  
DLR-F4 WING/BODY   
DRAG DIVERGENCE BOUNDARY   
Figure 24: Predicted Drag Divergence Boundary for the DLR-F4 Wing/Body.
