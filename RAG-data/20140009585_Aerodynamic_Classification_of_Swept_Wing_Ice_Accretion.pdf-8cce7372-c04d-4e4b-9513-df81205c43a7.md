# Aerodynamic Classification of Swept-Wing Ice Accretion

Jeff M. Diebold

University of Illinois at Urbana-Champaign, Urbana, Illinois

Andy P. Broeren

Glenn Research Center, Cleveland, Ohio

Michael B. Bragg

University of Illinois at Urbana-Champaign, Urbana, Illinois

Since its founding, NASA has been dedicated to the advancement of aeronautics and space science. The NASA Scientific and Technical Information (STI) program plays a key part in helping NASA maintain this important role.

The NASA STI Program operates under the auspices of the Agency Chief Information Officer. It collects, organizes, provides for archiving, and disseminates NASA’s STI. The NASA STI program provides access to the NASA Aeronautics and Space Database and its public interface, the NASA Technical Reports Server, thus providing one of the largest collections of aeronautical and space science STI in the world. Results are published in both non-NASA channels and by NASA in the NASA STI Report Series, which includes the following report types:

TECHNICAL PUBLICATION. Reports of completed research or a major significant phase of research that present the results of NASA programs and include extensive data or theoretical analysis. Includes compilations of significant scientific and technical data and information deemed to be of continuing reference value. NASA counterpart of peer-reviewed formal professional papers but has less stringent limitations on manuscript length and extent of graphic presentations.   
TECHNICAL MEMORANDUM. Scientific and technical findings that are preliminary or of specialized interest, e.g., quick release reports, working papers, and bibliographies that contain minimal annotation. Does not contain extensive analysis.   
CONTRACTOR REPORT. Scientific and technical findings by NASA-sponsored contractors and grantees.

CONFERENCE PUBLICATION. Collected papers from scientific and technical conferences, symposia, seminars, or other meetings sponsored or cosponsored by NASA.   
SPECIAL PUBLICATION. Scientific, technical, or historical information from NASA programs, projects, and missions, often concerned with subjects having substantial public interest.   
TECHNICAL TRANSLATION. Englishlanguage translations of foreign scientific and technical material pertinent to NASA’s mission.

Specialized services also include creating custom thesauri, building customized databases, organizing and publishing research results.

For more information about the NASA STI program, see the following:

Access the NASA STI program home page at http://www.sti.nasa.gov   
• E-mail your question to help@sti.nasa.gov   
Fax your question to the NASA STI Information Desk at 443–757–5803   
Phone the NASA STI Information Desk at 443–757–5802   
Write to: STI Information Desk NASA Center for AeroSpace Information 7115 Standard Drive Hanover, MD 21076–1320

# Aerodynamic Classification of Swept-Wing Ice Accretion

Jeff M. Diebold

University of Illinois at Urbana-Champaign, Urbana, Illinois

Andy P. Broeren

Glenn Research Center, Cleveland, Ohio

Michael B. Bragg

University of Illinois at Urbana-Champaign, Urbana, Illinois

Prepared for the

5th Atmospheric and Space Environments Conference

sponsored by the American Institute of Aeronautics and Astronautics

San Diego, California, June 24–27, 2013

National Aeronautics and

Space Administration

Glenn Research Center

Cleveland, Ohio 44135

# Acknowledgments

The authors would like to thank Joe Botalla at the University of Illinois who wrote the first draft of the literature review of swept wings with ice accretion and thus help initiate this paper. Abdi Khodadoust provided hard to acquire references from his extensive collection of icing papers. Several colleagues shared their expertise by reading a draft of this document and providing helpful comments and suggestions. This includes: Frederic Moens at ONERA; Cris Bosetti, Don Cook, Abdi Khodadoust, Adam Malone and Ben Paul at Boeing; Jim Riley at FAA; Sam Lee, Mark Potapczuk, Mary Wadel and Eric Kreeger at NASA Glenn. The authors from the University of Illinois were supported in this effort by a grant from the FAA Technical Center, DOT_FAA 10-G-0004, with technical monitor Jim Riley. NASA’s Atmospheric Environment Safety Technologies Project of the Aviation Safety Program also supported this work.

Trade names and trademarks are used in this report for identification only. Their usage does not constitute an official endorsement, either expressed or implied, by the National Aeronautics and Space Administration.

Level of Review: This material has been technically reviewed by technical management.

Available from

NASA Center for Aerospace Information

7115 Standard Drive

Hanover, MD 21076–1320

National Technical Information Service

5301 Shawnee Road

Alexandria, VA 22312

# Aerodynamic Classification of Swept-Wing Ice Accretion

Jeff M. Diebold University of Illinois at Urbana-Champaign Urbana, Illinois 61801

Andy P. Broeren National Aeronautics and Space Administration Glenn Research Center Cleveland, Ohio 44135

Michael B. Bragg University of Illinois at Urbana-Champaign Urbana, Illinois 61801

# Abstract

The continued design, certification and safe operation of swept-wing airplanes in icing conditions rely on the advancement of computational and experimental simulation methods for higher fidelity results over an increasing range of aircraft configurations and performance, and icing conditions. The current state-of-the-art in icing aerodynamics is mainly built upon a comprehensive understanding of twodimensional geometries that does not currently exist for fundamentally three-dimensional geometries such as swept wings. The purpose of this report is to describe what is known of iced-swept-wing aerodynamics and to identify the type of research that is required to improve the current understanding. Following the method used in a previous review of iced-airfoil aerodynamics, this report proposes a classification of swept-wing ice accretion into four groups based upon unique flowfield attributes. These four groups are: ice roughness, horn ice, streamwise ice and spanwise-ridge ice. In the case of horn ice it is shown that a further subclassification of “nominally 3-D” or “highly 3-D” horn ice may be necessary. For all of the proposed ice-shape classifications, relatively little is known about the three-dimensional flowfield and even less about the effect of Reynolds number and Mach number on these flowfields. The classifications and supporting data presented in this report can serve as a starting point as new research explores sweptwing aerodynamics with ice shapes. As further results are available, it is expected that these classifications will need to be updated and revised.

# 1.0 Introduction

The formation of ice on lifting surfaces in flight presents a serious risk to aircraft safety as well as a multitude of scientific and engineering challenges. Investigations into the accretion of ice and the resulting aerodynamic penalties began as early as the 1940s, and the research conducted in the past several decades has led to a thorough, but far from complete, understanding of the effects of ice on airfoils. Lynch and Khodadoust (Ref. 1) provide a review of the performance effects of ice on airfoils and straight wings, while Bragg et al. (Ref. 2) reviewed the flowfield characteristics that lead to the observed performance effects. In addition to reviewing the flowfield of iced airfoils, Bragg et al. (Ref. 2) proposed an ice shape classification system that was based on the unique flowfield features generated by the ice. The classifications proved to be very useful when conducting parametric studies of the aerodynamic effects of ice on airfoils.

Our understanding of iced airfoil aerodynamics has reached a level of maturity where we can begin trying to understand the complex effects of ice on highly three-dimensional (3-D)swept wings. Swept wing icing presents significant challenges because the parameter space for the 3-D wing case is much larger and more complex than for airfoils. In addition to airfoil geometry, ice-shape geometry, size and

location, the 3-D wing geometry must be considered. Here the airfoil and ice accretion can vary along the span and wing sweep angle, twist, taper, dihedral and aspect ratio must also be considered. As a result of this complexity, there are relatively few studies investigating the effects of ice on swept wing aerodynamics.

NASA, FAA, ONERA, the University of Illinois, Boeing and others are embarking on a research program with goals to improve our understanding and ability to model ice accretion and the resulting aerodynamic effect on full-scale, 3-D swept wings. The purpose of this review is to provide the initial framework for improving our understanding of swept wing icing, by reviewing much of the previous aerodynamic research in the context of a proposed ice shape classification system, similar to that developed by Bragg et al. (Ref. 2) for airfoils, and identify areas where more research is required. The classification is based on the fundamental flow physics that are unique to the different ice geometries and are responsible for the measured aerodynamic effects. Similar to two-dimensional (2-D) case, the proposed classifications are: ice roughness, horn ice, streamwise ice and spanwise-ridge ice. On a swept wing, the horn ice accretion can be further classified as with scallops, incomplete scallops or no scallops. It will be shown that from an aerodynamic point of view it may be more appropriate to classify the horn ice as nominally 3-D and highly 3-D horn ice. This review will discuss each classification with a focus on the unique aerodynamic characteristics as they are currently understood. An effort will be made to interpret aerodynamic performance in terms of key flowfield features and where appropriate comparisons to the 2-D case will be made. It should be noted that experimental swept wing icing data are limited and the different ice shape classifications have not received equal attention in the literature. In addition, most of the swept wing icing experiments have been conducted at low Reynolds numbers, and Reynolds number and Mach number effects are unknown. When the ice-shape classifications for airfoils were developed there was a better understanding of the aerodynamics and flowfields than currently exists for 3- D iced wings. Therefore, as research is conducted and the knowledgebase increases, the classifications will undoubtedly change and improve. This report is a modified and updated version of the work of Broeren, Diebold and Bragg (Ref. 3).

# 2.0 Aerodynamic Classification of Swept Wing Ice Accretion

The purpose of this section is to review the existing body of technical literature on iced-swept wing aerodynamics in the context of a classification method based upon fundamental flowfield characteristics. The classifications include roughness, horn ice, streamwise ice and spanwise ridge ice. The focus of the following discussion will be on how the ice affects the flowfield and the performance, the physical characteristics and mechanisms through which the ice forms will only be discussed briefly. Vargas provides an excellent historical and technical summary of swept wing ice accretion (Ref. 4). As mentioned above, not all classifications have received an equal amount of attention. Currently, roughness and horn ice shapes have been the subject of the most investigations while streamwise and spanwise ridge ice have not been studied in as much detail.

# 2.1 Ice Roughness

Ice roughness refers to surface roughness associated with the initial stages of in-flight ice accretion. Anderson and Shin (Ref. 5) characterized roughness formation on airfoils and found that initially the leading-edge contains a smooth zone, a rough zone and a feather region. These same features are observed for swept wings, but for large sweep angles in both glaze and rime icing conditions it has been observed that the smooth zone may not form. Despite this difference, the characteristics of initial icing roughness on swept wings are fundamentally the same as for airfoils and straight wings. Icing roughness can be characterized by height, location, chordwise extent, concentration and shape (Ref. 2). It has been observed on airfoils (Ref. 6) and swept wings (Ref. 4) that the height of the ice roughness elements is generally greater than the local boundary layer thickness. Vargas (Ref. 4) points out that the effects of roughness of this size on the boundary layer instabilities and transition are unknown. It is reasonable to

assume that the local separated flowfield in the vicinity of the roughness elements is not fundamentally different than in the airfoil case. For this, Bragg et al. (Ref. 2) provide a detailed review of the roughness flowfield including the relevant phenomenological features, effects on transition and turbulence and impact on aerodynamic performance. For swept wings, the questions that arise have to do with the interaction of this flowfield with the spanwise and vortex flows.

Fortunately, in the case of roughness there is a fair amount of experimental data in the literature from studies unrelated to icing. The National Advisory Committee for Aeronautics (NACA) has conducted numerous experimental investigations into the aerodynamics of swept-wing configurations. Many of the studies explored Reynolds and Mach number effects and included cases with carborundum grains applied to leading edges. Neely and Conner (Ref. 7) investigated leading-edge roughness effects in the Langley 19-ft pressure tunnel on a full-span wing with aspect ratio 4, $4 2 ^ { \circ }$ leading-edge sweep, mean aerodynamic chord $= 3 4 . 7 1$ in., and taper ratio $= 0 . 6 2 5$ . Aerodynamic testing was conducted over a Reynolds number range of $1 . 7 \times 1 0 ^ { 6 }$ to $9 . 5 { \times } \dot { 1 } 0 ^ { 6 }$ with corresponding Mach number range of 0.10 to 0.22. Flow visualization showed that the stall of the clean wing began with separated flow near the trailing-edge of the outboard sections and progressed forward and inboard on the wing. In contrast, with $k / c _ { m a c } = 0 . 0 0 0 3 2$ diameter carborundum grains applied between $x / c = 0 . 0 8$ on the lower surface to $x / c = 0 . 0 8$ on the upper surface covering approximately 5 to 10 percent of the area, flow separation began at the leading-edge outboard sections. The effect of Reynolds number and surface roughness on the lift and drag is shown in Figure 1 and Figure 2, respectively. It can be seen that for all Reynolds numbers, the application of leading-edge roughness reduced $C _ { L \mathrm { m a x } } .$ , reduced the stalling angle of attack and increased the drag. In addition, the roughness reduced the effects of Reynolds number. All of these trends are typical of what has been observed in numerous airfoil studies with roughness.

Kind and Lawrysyn (Ref. 8) numerically investigated the effects of wing frost on a jet transport wing with an aspect ratio of 7.9, $3 0 ^ { \circ }$ sweep and taper ratio of 0.25. Figure 3 shows the effects of roughness with $k / c _ { m a c } = 0 . 0 0 0 0 6$ on lift and drag for various chordwise extents of the roughness. The numbers in the figure legend indicate the chordwise extent of the roughness on the wing upper surface: $^ { \mathfrak { c } \mathfrak { c } } 5 0 ^ { \mathfrak { s } }$ indicates the roughness extended from $x / c = 0 . 4 2$ to the trailing edge, $\boldsymbol { \mathfrak { s } } \mathfrak { s } ^ { \th }$ indicates $x / c = 0 . 2 0$ to the trailing edge, ${ } ^ { 6 6 } 9 5 ^ { , 3 }$ indicates $x / c = 0 . 0 0 9$ to the trailing edge and $^ { \mathfrak { c } \mathfrak { c } } 9 9 ^ { \mathfrak { d } } { } ^ { \mathfrak { d } }$ indicates $x / c = 0 . 0 0$ to the trailing edge. Their results indicate that the roughness reduced both the slope of the lift curve and $C _ { L \mathrm { m a x } }$ for all levels of coverage, but the wing was most sensitive to roughness located in the first 1 percent of the chord.

图片摘要：该图主要展示 1.—Effect of Reynolds number and leading edge roughness on t。
![](images/42a321847ecbddc4db3fc3b655e68c4514ad8b99116ab13f54f3368d321353ca.jpg)  
Figure 1.—Effect of Reynolds number and leading-edge roughness on the lift coefficient of a $4 2 ^ { \circ }$ leading-edge swept wing, after Neely and Conner (Ref. 7).

图片摘要：该图主要展示 1.—Effect of Reynolds number and leading edge roughness on t。
![](images/11dbd1a8c85a2f90428557720f28b77b7eca0e93f321a9794284ec730ebc6bbe.jpg)  
Figure 2.—Effect of Reynolds number and leading-edge roughness on the drag polar of a $4 2 ^ { \circ }$ leading-edge swept wing, after Neely and Conner (Ref. 7).

图片摘要：该图主要展示 2.—Effect of Reynolds number and leading edge roughness on t。
![](images/6cf8cd2ae9d0defeaed33613ccf1b855100cebff08bbed2a37eadb44ae515fd2.jpg)  
Figure 3.—Effect of simulated upper surface frost on a generic jet transport wing, after Kind and Lawrysyn (Ref. 8).

Papadakis et al. (Ref. 9) performed an investigation of roughness on the leading edge of a business jet T-tail configuration. Sandpaper was used for the roughness with grit sizes of 40, 80, 120 and 180 covering from approximately $x / c = 0 . 0 2 5$ on the lower surface to $x / c = 0 . 0 1 6$ on the upper surface. The chordwise extent was determined from a droplet trajectory analysis. The horizontal tail had a leadingedge sweep of $2 9 ^ { \circ }$ , aspect ratio 4.4 and taper ratio of 0.43. A full-scale model was tested in the NASA Ames 40- by 80-ft wind tunnel and a 25 percent scale model was tested in the Walter H. Beech Memorial 7- by 10-ft tunnel. The full-scale model had a mean aerodynamic chord of 49.2 in. and the 25 percent scale model had a mean aerodynamic chord of 12.3 in. The 25 percent scale model was tested at a maximum Reynolds number of $1 . 3 6 \times 1 0 ^ { 6 }$ , where it was found that the 40 and 80 grit roughness $( k / c _ { m a c } = 0 . 0 0 1 3 7 5$ and 0.000605) reduced $C _ { L \mathrm { m a x } }$ by 4.5 and 2.8 percent respectively; however, the 120 and 180 grit roughness $( k / c _ { m a c } = 0 . 0 0 0 3 6 5$ and 0.000259) increased $C _ { L \mathrm { m a x } }$ by 4.9 and 1.9 percent, respectively. Testing of the full-scale model at $\mathrm { R e } = 5 . 1 \times 1 0 ^ { 6 }$ showed that the 40 and 120 grit roughness $\mathrm { { \it k } } / c _ { m a c } =$ 0.000344 and 0.000091) decreased $C _ { L \mathrm { m a x } }$ by 18.5 and 15.9 percent respectively. Surface pressure measurements and boundary layer profile measurements at $x / c = 0 . 6$ and $2 y / b = 0 . 5 1$ showed that the leading-edge roughness led to significantly thicker boundary layers and trailing-edge separation.

These results demonstrate the possible large aerodynamic penalties of roughness but also a potential problem of testing at low Reynolds numbers. Low Reynolds number experiments can mask the true penalties of ice shapes because the clean wing performance generally suffers as a result of the low Reynolds number more than the iced wing. In the 2-D case, it has been shown that the Reynolds number typically has a substantially smaller effect on the iced airfoil aerodynamics than for the clean airfoil (Ref. 2). This is because the ice shape fixes the separation location thereby eliminating a potential mechanism through which the Reynolds number can affect performance. Therefore, while low Reynolds number experiments of iced airfoils are generally representative of higher Reynolds number, the low Reynolds number clean airfoil experiments may not and care must be taken when interpreting results. The low Reynolds number of the 25 percent scale experiments of Papadakis (Ref. 9) may explain the increase in $C _ { L \mathrm { m a x } }$ for the 120 and 180 grit roughness, because the classification of roughness does have the potential to depend more on the Reynolds number than other classifications (Ref. 2). It should be noted that due to the lack of high Reynolds number swept wing icing experiments, it is unknown how the Reynolds number effects iced swept wings.

While these roughness studies do provide some initial insights, more research is needed to understand the effect of size, location, concentration, Reynolds number and other factors important to the aerodynamics of iced-swept wings. There is very little or no flowfield information such as surface pressures, flow visualization and velocity profiles in these reports. An understanding of the roughness flowfield is important to accurate subscale simulation of roughness effects.

# 2.2 Horn Ice

On airfoils, glaze icing conditions often lead to leading-edge ice accretion known as horn ice. There are several geometric features that are important to the horn-ice shape, including height, the angle it makes with respect to the flow and its surface location (Ref. 2). For a swept wing in glaze or mixed icing conditions, ice accretion can be divided into three subcategories known as complete scallops, incomplete scallops and no scallops. An illustration (Ref. 4) of each shape is shown in Figure 4, and photographs (Ref. 10) of a complete and incomplete scallop ice accretion are shown in Figure 5. The type that forms has been found to be dependent on sweep angle and icing conditions (Ref. 4). Based on the aerodynamic classification system proposed here, the ice accretions in Figure 4 can be classified as horn ice. It will be shown in this section that on swept wings a further subclassification of “nominally 3-D” or “highly 3-D” horn ice is necessary. These subclassifications are based on the fundamental aerodynamics of the particular ice shape which will be explained in this section. Based on available data, ice accretions with no scallops or incomplete scallops can be considered nominally 3-D horn ice while accretions with full scallops can be considered highly 3-D horn ice.

图片摘要：该图主要展示 4.—Ice accretion on a swept wing in glaze icing conditions. 。
![](images/064f2cbfe4023eaf97dc883ca58b4e86d40f1671776e3fa76632022cddeb9dd9.jpg)  
(（a）

图片摘要：该图主要展示 4.—Ice accretion on a swept wing in glaze icing conditions. 。
![](images/7b81df55819398b7730055c0715ce4578648a5aaebb1c70e0e282a8f96b5c6b0.jpg)

图片摘要：该图主要展示 4.—Ice accretion on a swept wing in glaze icing conditions. 。
![](images/92ebba73544ee285142d16d25f7f6c9aef895bdfcc9c0c241eded2ea64b6e8fa.jpg)  
（C）  
Figure 4.—Ice accretion on a swept wing in glaze icing conditions. Arrows indicate direction of flow. (a) Complete scallops, (b) Incomplete scallops, and (c) No scallops (Ref. 4).

图片摘要：该图主要展示 4.—Ice accretion on a swept wing in glaze icing conditions. 。
![](images/2d69b84101797bf317b766e064d952d006e7cad6f35824fc3c1536b2e47fe6a6.jpg)

图片摘要：该图主要展示 4.—Ice accretion on a swept wing in glaze icing conditions. 。
![](images/948844b81cfca6ab3fa53da1f6cb573452f755edb806b880070a8b3ccd9fc3c7.jpg)  
Figure 5.—Photographs of complete and incomplete scallop glaze ice accreted on a wing having $2 8 ^ { \circ }$ leading-edge sweep in the NASA Glenn Icing Research Tunnel (Ref. 10).

In contrast to ice roughness on swept wings, there is some fundamental research regarding the flowfield about a 3-D wing with horn ice. An early experimental study by Khodadoust and Bragg (Ref. 11) and an accompanying CFD study by Kwon and Sankar (Ref. 12) investigated the performance and flowfield of a semispan wing with a chord of 15-in., sweep angle of $3 0 ^ { \circ }$ and an aspect ratio of approximately 2.3. A NACA 0012 airfoil section was used. The ice shape used for the experiment and the CFD study was a simulation of a horn ice shape that was formed on a NACA 0012 airfoil in NASA’s IRT. Figure 6 shows the cross sections of the IRT generated ice shape and the simulated shape used for the experiment and the CFD study. The 2-D cross section was extruded along the span and in the framework of the proposed aerodynamic classification system this ice shape is nominally 3-D horn ice.

Figure 7 shows experimental pressure distributions at several spanwise locations with and without the horn ice at ${ \mathfrak { a } } = 8 ^ { \circ }$ and $\mathrm { R e } = 1 . 5 { \times } 1 0 ^ { 6 }$ . The pressure distributions show that when the horn ice is present the leading-edge suction peaks are replaced by regions of nearly constant pressure covering approximately 20 to 40 percent of the chord. This is very similar to the pressure distribution on an airfoil with a horn shape

where the pressure plateau indicates a separation bubble. In the case of a swept wing however, the separated flow and spanwise pressure gradient result in a 3-D leading-edge vortex. This vortex can clearly be seen in Figure 8 which shows surface oil flow and a particle trajectory simulation from the CFD results for the iced wing at the same conditions as Figure 7. The vortex grew in diameter moving outboard along the wing, and was lifted off the wing surface and shed into the wake near the tip. The effect of the increasing diameter of the vortex is seen in the broadening and reduction of the pressure peaks in Figure 7. The simulated surface-oil flow showed regions of purely spanwise flow near the trailing edge and regions of almost completely reversed flow near the leading edge. These flowfield characteristics are analogous to the fundamental studies of swept wing stall conducted by Poll (Ref. 13).

图片摘要：该图主要展示 7 shows experimental pressure distributions at several spanw。
![](images/615beb45d3a0eb1af71b2eab1eb5426b345fa6ad1a87145125dfb4b71b29d6d1.jpg)  
Figure 6.—Measured and simulated glaze ice shape (Refs. 11 and 12).

图片摘要：该图主要展示 6.—Measured and simulated glaze ice shape (Refs. 11 and 12)。
![](images/78399e02c8929547c7d0d387ea4a5de24ad9a1402c9b146a42bc948f5f56e8fc.jpg)  
(a) Clean Wing

图片摘要：该图主要展示 6.—Measured and simulated glaze ice shape (Refs. 11 and 12)。
![](images/bea775c32d8d34c2b10e3953d89d00139c0e2043235808e29e65bd9b8e0f2dab.jpg)  
(b) Wing with horn ice   
Figure 7.—Pressure distributions for the NACA 0012 swept wing with and without the horn ice shape, $\mathtt { q } = 8 ^ { \circ }$ $\mathsf { \Pi } _ { \mathsf { R e } } ^ { \mathsf { \Theta } } = 1 . 5 { \times } 1 0 ^ { 6 }$ , after Bragg and Khodadoust (Ref. 11).

Bragg et al. (Ref. 14) used LDV to study the flowfield of the same swept NACA 0012 wing used by Khodadoust (Ref. 11) and Kwon (Ref. 12). The LDV was used to measure all three components of velocity at several spanwise locations for ${ \mathfrak { a } } = 8 ^ { \circ }$ and $\mathrm { R e } = 1 . 0 { \times } 1 0 ^ { 6 }$ . Streamwise velocity measurements showed the inviscid flow accelerating over the ice shape leading to maximum values of $u / U _ { \infty }$ of 1.53 and 1.39 located at $y / b = 0 . 4$ and $y / b = 0 . 7$ respectively. Just downstream of the separation point, spanwise velocities of nearly twice the freestream velocity were measured. In general the velocities within vortex decreased as the tip was approached due to the increasing size of the vortex; however, near the tip large spanwise velocities due to the tip vortex were observed. Due to limitations of the experimental setup the only turbulence quantity obtained was $\overline { { { u ^ { \prime } } ^ { 2 } } }$ . Maximum turbulence intensities of nearly 35 percent were measured in the shear layer.

A more recent low-Reynolds number study by Diebold et al. (Ref. 15) investigated the performance and flowfield of a semispan wing with $3 5 ^ { \circ }$ leading-edge sweep, an aspect ratio of 8.3, taper ratio of 0.296 and a mean aerodynamic chord of 6.9-in. A nominally 3-D horn ice shape was used. The ice shape simulation was formed by lofting several 2-D ice shape cross sections along the span. The model was based on the CRM, designed by Vassberg (Ref. 16), and was representative of a modern wide body commercial airliner. Experiments included force balance measurements, pressure sensitive paint, surface oil flow visualization and 5-hole probe wake surveys. Figure 9 shows oil flow images for the iced wing at several angles of attack for a Reynolds number of $3 { \times } 1 0 ^ { 5 }$ . The oil flow clearly indicates the presence of a leading-edge vortex. In Figure 9, the reattachment line of the leading-edge vortex, which indicates where the separated shear layer has reattached to the surface, is highlighted. It can be seen that as the angle of attack increased, the reattachment line moved downstream indicating that the size of the leading-edge vortex grew. This is very similar to flowfield of an airfoil with a horn ice shape. As the angle of attack increases the separation bubble on the airfoil grows in the chordwise direction (Ref. 2). Pressure sensitive paint results on the swept wing indicated reduced pressure peaks and broad regions of nearly constant pressure under the vortex similar to Figure 7(b).

When an airfoil with horn ice reaches the stalling angle of attack, the separated flow fails to reattach. When a swept wing with horn ice stalls the flowfield is far more complex than for an airfoil. Figure 10 shows the oil flow of the stalled swept wing with ice. On the inboard sections of the wing the separated shear layer was able to reattach to the surface and the flow is qualitatively similar to the flow at lower angles of attack. Over the outboard sections of the wing however, the separated shear layer was unable to reattach and this section of the wing was stalled. The leading-edge vortex began near the root and quickly turned downstream and was shed into the wake creating a similar flowfield to that of the swept NACA 0012 shown in Figure 8.

图片摘要：该图主要展示 7.—Pressure distributions for the NACA 0012 swept wing with 。
![](images/18d82e59eadb283ffa04a0abfabb728b29975e1c43dfd8369428b56000ff176b.jpg)

图片摘要：该图主要展示 8.—Flowfield over the NACA 0012 swept wing with horn ice sha。
![](images/9320503e738a515d06a38e2d8c27b56a1e3eca0fc16d283651c4b3a222f0f0d7.jpg)  
Figure 8.—Flowfield over the NACA 0012 swept wing with horn ice shape: (a) CFD surface oil simulation and (b) CFD Particle trajectory simulation, ${ \mathfrak { a } } = 8 ^ { \circ }$ , $\mathsf { R e } = \mathsf { 1 } . 5 \mathsf { \times } 1 0 ^ { 6 }$ , after Kwon and Sankar (Ref. 12).

图片摘要：该图主要展示 8.—Flowfield over the NACA 0012 swept wing with horn ice sha。
![](images/c4369ed7524db886b2f3d9602fd9391f608d11f40f8b85b4f940a2ec343bec01.jpg)

图片摘要：该图主要展示 8.—Flowfield over the NACA 0012 swept wing with horn ice sha。
![](images/42ae3ffa49823b9ebc3c04b90c09b7bc444ec20206ed9dafce9c1c5c7b01391a.jpg)  
Figure 9.—Reattachment line of the separated flow on the iced wing for a range of angles. $\mathsf { \bar { R e } } = 3 \mathsf { x } 1 0 ^ { 5 }$ . Adapted from Diebold et al. (Ref. 15).   
Figure 10.—Stalled iced wing with reattachment line highlighted. $\mathtt { q } = 6 . 5 ^ { \circ }$ , $\check { \mathsf { R e } } = 3 \times 1 0 ^ { 5 }$ . Adapted from Diebold et al. (Ref. 15).

Diebold and Bragg (Ref. 17) studied the performance of the same swept wing model as Diebold et al. (Ref. 15) using a 5-hole probe wake survey analysis. Using methods described by Brune (Ref. 18), measurements of velocity and pressure in the wake were used to determine the lift and drag on the model, decompose drag into profile and induced drag components and measure the spanwise distribution of lift and drag. Figure 11 shows $C _ { L }$ of the clean and iced wing plotted against the profile and induced drag components. The wake survey results show that the increase in drag due to the ice shape is exclusively the result of an increase in the profile drag. For the same $C _ { L } ,$ the ice shape does not affect the induced drag. The increase in profile drag due to the ice shape is a result of the large separated region behind the horn ice and the resulting pressure drag. In addition, the profile drag of the iced wing increased at much faster rate on the iced wing due to the increasing size of the leading-edge vortex which was seen in Figure 9. The wake survey results of Diebold and Bragg (Ref. 17) were also used to determine the spanwise distribution of lift and drag. Their results showed that for the particular ice shape and wing studied, the ice had a larger impact on the local aerodynamics of the outboard sections of the wing. This was explained as a result of a combination of the size of the ice shape relative to the local chord which increased as the tip was approached and the fundamental aerodynamics of swept wings. The spanwise flow on a swept wing acts as a form of boundary layer suction (Ref. 19) which may have helped promote reattachment of the separated flow. Diebold and Bragg (Ref. 17) were also able to relate features seen in the surface oil flow to features in the lift and drag distributions. It should be noted that the experiments of Diebold et al. and Diebold and Bragg were conducted at very low Reynolds numbers $( \mathrm { R e } < 1 \times 1 0 ^ { 6 } )$ ) and it is unknown if the observations discussed here will hold at higher Reynolds number.

图片摘要：该图主要展示 10.—Stalled iced wing with reattachment line highlighted. , 。
![](images/58289f3e79515d8df5889e2f81b21973d84cdf803e2c8b3b753959ecf000bac6.jpg)  
Figure 11.— $\scriptstyle \cdot C _ { L }$ versus components of drag for clean and iced wing measured from wake survey. $\mathsf { R e } = 6 \times 1 0 ^ { 5 }$ (Ref. 17).

The studies discussed above provided valuable insight into the flowfield of a swept wing with a horn ice shape. To better understand the performance effects of horn ice on swept wings it is necessary to utilize different and more realistic ice shapes. Papadakis et al. (Ref. 20) investigated the effect of horn ice shapes on the T-Tail used in the roughness study (Ref. 9) discussed in Section 2.1. The model was a 25 percent scale business jet T-Tail with a $2 9 ^ { \circ }$ leading-edge sweep, a mean aerodynamic chord of 12.31 in. and an aspect ratio of 4.4. The ice shapes tested were generated using LEWICE (LEWICE (Ref. 21) is a computational tool that simulates ice growth on surfaces exposed to icing conditions.), and in addition two spoilers consisting of a spanwise flat plate protruding normal to the airfoil surface were also tested. Cross-sectional views of the ice shapes and spoilers are shown in Figure 12. The ice-shape simulations were generated using the same atmospheric conditions but different simulation times, 9 and $2 2 \mathrm { { m i n } }$ . The spoilers were used to represent only the height of the horn on the suction surface. Two types of spoilers were used, for one type the height matched the LEWICE shape along the span while the other type of spoiler had a constant height equal to the maximum height of the ice shape. Note, the suction surface is the lower surface. In addition, the LEWICE ice shapes were tested with and without 24-grit $( k / c _ { m a c } = 0 . 0 0 2 4 )$ roughness was added.

At a Reynolds number of $1 . 3 6 \times 1 0 ^ { 6 }$ the ice shapes had a significant effect on performance. The 9 and 22 min LEWICE shapes reduced $C _ { L \mathrm { m a x } } 1 0 . 8$ and 24.5 percent respectively. The addition of 24 grit roughness reduced $C _ { L \mathrm { m a x } }$ by approximately 10 percent more than the corresponding smooth shapes. The addition of the roughness also increased the drag relative to the smooth shape. The large effect of added roughness, not typically seen in past airfoil studies, may be due to the aerodynamics of a swept wing; however, another potential explanation could be the geometry of the LEWICE simulations. The horns of LEWICE shapes are significantly more rounded than those of typical ice accretion. Because the horns are fairly rounded the point of separation may not be fixed to a specific location on the horn. Therefore, the addition of roughness may affect the separation location, whereas on a sharper horn this point would be fixed regardless of the surface condition. Surface pressure distributions showed that the roughness generally resulted in a reduced suction peak and a flatter broader $C _ { p }$ distribution, and boundary layer measurements near midspan at $x / c = 0 . 6$ showed the application of roughness generally resulted in thicker boundary layers. Both of these observations support the idea that the roughness led to earlier separation on the ice shape.

图片摘要：该图主要展示 11.— versus components of drag for clean and iced wing measu。
![](images/81806f0700be981645509f4efedc92b9c553f76a02ec8a8d7e038ebf7611e047.jpg)

图片摘要：该图主要展示 11.— versus components of drag for clean and iced wing measu。
![](images/d736d40640d5286bed6e0433f6c9ea6944e0ead451dc8d6c0c0b96c3675d0dbf.jpg)  
Figure 12.—Ice-shape simulations for 25 percent scale business jet T-Tail used by Papadakis et al. (Ref. 20).

图片摘要：该图主要展示 12.—Ice shape simulations for 25 percent scale business jet 。
![](images/f356fc5c64c1cc85a29b0990666528a4b147d3c6c97cd73925712ea072c86388.jpg)  
(a) 9-min ice shape

图片摘要：该图主要展示 12.—Ice shape simulations for 25 percent scale business jet 。
![](images/16dff184a434f5fa7459c3f394bd3744098d50f09cf6527dbdaf87e82e5f5c5d.jpg)  
(b) 22-min ice shape   
Figure 13.—Comparison of smooth and rough LEWICE shapes with constant and variable height flat plate spoilers for a) the 9-min ice shape and b) the 22-min ice shape. $\mathsf { R e } \overset { \cdot } { = } 1 . 3 6 \times 1 0 ^ { 6 }$ . Adapted from Papadakis et al. (Ref. 20).

When investigating the effects of ice on aerodynamic performance it is advantageous to use simple simulations for the ice shape. Several studies (Refs. 22 and 23), have shown that very simple geometries, such as a leading-edge “spoiler,” can reproduce the performance characteristics of a horn-ice shape over a large angle of attack range. A simple geometry representing the height, angle, and location of the ice horn, essentially generates an equivalent separation bubble on the airfoil and, hence, very similar performance results. Figure 13 compares the lift of the smooth and rough LEWICE shapes, discussed above, with the constant and variable height flat plate spoilers. The designations L9 and L22 refer to the small and large smooth LEWICE shapes, and L9B and L22B refer to the same shapes with the 24 grit roughness added. The designations SP47C, SP47V, SP94C and SP94V refer to the spoilers. SP47 corresponds to the L9 ice shape and SP49 corresponds to the L22 ice shape. The C and V refer to constant height and variable height respectively. Not unsurprisingly the spoiler with constant height, SP47C and SP94C had the largest effect because its height was equal to the maximum height of the ice shape and was constant along the span. Interestingly, the variable height spoilers, which matched the ice shapes height along the span, agreed well with the rough LEWICE shapes. It is perhaps surprising that the variable height spoiler matched the rough LEWICE shape as opposed to the smooth. This could possibly be because the location of the plate corresponds more closely to the separation point on the rough ice shape as opposed to the smooth shape; however, looking at surface pressure distributions and boundary layer measurements there are a few substantial differences between the rough LEWICE shape and the spoiler indicating the close match in performance may have been fortuitous. For example, pressure measurements at an angle of attack of $- 5 ^ { \circ }$ showed poor agreement in both the magnitude of the suction peak and width of the separated region on the root and midspan sections.

The studies discussed above utilized ice shape simulations without any scallop features which can all be classified as nominally 3-D horn ice. Studies by Papadakis et al. (Refs. 24 and 25) investigated the effects of several different ice shapes on a swept wing that included high-fidelity, 3-D ice-casting simulations incorporating various levels of incomplete and complete scallops. The swept-wing model had a GLC-305 airfoil section aligned in the streamwise direction with a $2 8 ^ { \circ }$ leading-edge sweep, 18.72-in. mean aerodynamic chord, 60-in. semispan and an aspect ratio of 6.8. The ice shapes used for this study

were formed on the same model in the NASA Glenn Icing Research Tunnel (Ref. 10). The icing conditions were chosen to produce a wide range of ice shapes including complete and incomplete scallops of various sizes and a rime ice formation. Moldings of the IRT ice accretions were subsequently used to produce the ice castings that were used for the aerodynamic tests. The ice-casting simulations captured the fully 3-D variation of the ice accretion.

The ice accretions tested and the corresponding tunnel conditions are shown in Table I. Ice1 (IRT-CS10) is an example of a complete scallop glaze ice accretion. This shape can be compared with Ice2 (IRT-IS10) which is an example of an incomplete scallop. While the cross-sectional tracings look similar, the photographs reveal the large differences in the 3-D geometry. Ice3 (IRT-SC5) is a rime ice accretion and will be discussed in Section 2.3. Ice4 (IRT-CS2) was formed at identical conditions to Ice1(IRT-CS10), but with a much shorter exposure time of 2 min. Therefore, this is a relatively small glaze ice accretion and it is unclear if true scallop features formed due to the short exposure time. Ice5 (IRT-CS22) was also formed at identical conditions to Ice1 (IRT-CS10), but with a longer exposure time of 22.5 min. This longer duration led to the very larger complete scallop accretion shown in Table I. Finally, Ice6 (IRT-IPSF22) had some characteristics of complete scallops that were not as fully developed as in Ice1(IRT-CS10) and Ice5 (IRT-CS22).

TABLE I.—ICE ACCRETIONS AND CORRESPONDING ICING CONDITIONS USED BY PAPADAKIS ET AL. (REF. 24)   

<table><tr><td>Ice1 or IRT-CS10
A
B
C
Complete scallops
V = 250 mph
AOA = 4°
Ttotal = 25 °F
LWC = 0.68 g/m3
MVD = 20 μm
Time = 10 min</td><td>Ice2 or IRT-IS10
AOA = 4°
Incomplete scallops
V = 150 mph
Ttotal = 25 °F
LWC = 0.65 g/m3
MVD = 20 μm
Time = 10 min</td><td>Ice3 or IRT-SC5
AOA = 6°
No scallops
V = 201 mph
Ttotal = 11.7 °F
LWC = 0.51 g/m3
MVD = 14.5 μm
Time = 5 min</td><td>A = Normal to LE
B = Normal to LE
C = Streamwise
18 in.
B
25 in.
C
25 in.*</td></tr><tr><td>Ice4 or IRT-CS2
A
B
C
Initial formation of scallops
V = 250 mph
AOA = 4°
Ttotal = 25 °F
LWC = 0.68 g/m3
MVD = 20 μm
Time = 2 min</td><td>Ice5 or IRT-CS22
AOA = 4°
Complete scallops
V = 250 mph
Ttotal = 25 °F
LWC = 0.68 g/m3
MVD = 20 μm
Time = 22.5 min</td><td>Ice6 or IRT-IPSF22
AOA = 4°
IPS failure case
V = 150 mph
Ttotal = 27 °F
LWC = 0.46 g/m3
MVD = 20 μm
Time = 22.5 min</td><td>Ice4
Ice5
Ice6</td></tr></table>

*Distances are measured along wing leading edge,section C is at wing root,section Bis 25-in.from wing root, section Ais 50 in.from wing root or 18 in. from wing tip.

In addition to the IRT ice accretion in Table I, seven additional ice shapes were generated using the ice accretion code LEWICE 2.0. Since LEWICE 2.0 is a 2-D ice accretion code, the 3-D simulations used for the aerodynamic testing were composed of 2-D slices at several spanwise sections of the wing blended

together. The detailed procedure is discussed in the original reference (Ref. 24). The LEWICE shapes were formed at the same conditions shown in Table I, but the velocity and airfoil geometry used in the computations was the velocity normal to the leading edge. The LEWICE shapes did not contain any scallop features and as will be shown below can be classified as nominally 3-D horn ice. These are designated with the prefix “LS” in the following figures. The geometry did vary in the spanwise direction but only according to the number of slices used to loft the 3-D geometry. The effect of ice-shape roughness was also investigated by adding 36-grit size roughness $k / c _ { m a c } = 0 . 0 0 1 1 )$ to the smooth LEWICE shapes.

Because the Papadakis et al. (Refs. 24 and 25) study utilized high-fidelity ice-casting simulations of the 3-D ice accretions, it is possible to make some observations about the attendant aerodynamic effects relative to nominally 3-D horn ice with minimal 3-D features. Figure 14 shows a comparison of the ice accretion cross-section and the corresponding LEWICE shape for Ice2 (IRT-IS10) both of which can be classified as nominally 3-D horn ice. Overall, there is reasonable agreement in the tracings, particularly for station A. Figure 15 compares the lift and $C _ { P }$ distributions for the IRT generated shape and the smooth and rough LEWICE shapes. The results here are very similar to what has been reported for horn ice simulations on airfoils (Ref. 22). The effect on lift coefficient is very similar for all three configurations up to the stall region where the 3-D ice casting configuration has slightly lower maximum lift and stalling angle. For horn ice shapes on airfoils, small differences in the horn height, location or angle can significantly affect $C _ { L , \mathrm { { m a x } } }$ and may explain the differences given the obvious differences in the cross sections shown in Figure 14. The smooth LEWICE (LS-IS10) shape had slightly higher $C _ { L , \mathrm { { m a x } } }$ than the LEWICE shape with roughness (LS-IS10), which is consistent with the observations for the business jet T-tail (Ref. 20) discussed above and for past research on airfoils.

Also included in Figure 15 is a comparison of surface pressure at the 50 percent semispan stations at ${ \mathfrak { a } } = 4 ^ { \circ }$ For all three configurations, there are fairly well defined regions of approximately constant pressure from $x / c \approx 0 . 0$ to $x / c \approx 0 . 2$ on the upper surface. This pressure signature is similar to that shown previously in Figure 7 due to the leading-edge vortex induced by the horn geometry. In their report, Papadakis et al. (Ref. 25) provide more pressure comparisons at several angles of attack and for two additional spanwise locations. In most of these plots, the general shape of the distributions for the Ice2 (IRT-IS10) casting is similar to that for the LEWICE simulations. Thus indicating that for incomplete scallops, the large flowfield features (such as the leading-edge vortex) are similar to ice shape with no scallops described earlier in this section. Therefore, from an aerodynamic perspective, shapes with no scallops and incomplete scallops fall under the same classification of nominally 3-D horn ice.

图片摘要：该图主要展示 14.—Comparison of IRT Ice2 (IRT IS10) and LEWICE ice shape c。
![](images/9ffa1644fa45b082b3f111d28ce1a19d2759833d5fd93cc17b7332bfadd521ec.jpg)

图片摘要：该图主要展示 14.—Comparison of IRT Ice2 (IRT IS10) and LEWICE ice shape c。
![](images/be2601e7115b717e62597972f214d3297ec8ea4f74f263a32f978daf2de67f2f.jpg)  
Figure 14.—Comparison of IRT Ice2 (IRT-IS10) and LEWICE ice-shape cross sections on GLC-305 swept wing, after Papadakis et al. (Ref. 24)

图片摘要：该图主要展示 14.—Comparison of IRT Ice2 (IRT IS10) and LEWICE ice shape c。
![](images/369f8ff25551fb183e03b928b321a916005c0fa2c2c64556a14a3bf62004efda.jpg)

图片摘要：该图主要展示 14.—Comparison of IRT Ice2 (IRT IS10) and LEWICE ice shape c。
![](images/df982a340df33ac6ce488972c53966399d7ea34035dd0118bdcebbfb3919bb9a.jpg)  
Figure 15.—Aerodynamic effect of IRT Ice2 (IRT-IS10) and LEWICE ice-shape simulations on GLC-305 swept wing at $\mathsf { R e } = 1 . 8 \times 1 0 ^ { 6 }$ , after Papadakis et al. (Ref. 24)

图片摘要：该图主要展示 15.—Aerodynamic effect of IRT Ice2 (IRT IS10) and LEWICE ice。
![](images/cdb23a2c4ba5a833f9564092091529d6c9dc3927a79319b3e6d530036fcf5929.jpg)

图片摘要：该图主要展示 15.—Aerodynamic effect of IRT Ice2 (IRT IS10) and LEWICE ice。
![](images/cbe0179702dbeed01625ede310ffa15e186bd6e3bf321cb2fb4a346871db5e26.jpg)  
Figure 16.—Comparison of IRT Ice1 (IRT-CS10) and LEWICE ice-shape cross sections on GLC-305 swept wing, after Papadakis et al. (Ref. 24).

The data presented in Figure 14 and Figure 15 for the incomplete scallop configuration of Ice2 (IRT-IS10) are contrasted with the data for the complete scallop configuration of Ice1 (IRT-CS10). The crosssection geometry and LEWICE results are depicted in Figure 16 where there are much larger differences in the two geometries relative to that shown in Figure 14. This is most likely a result of the much higher degree of three-dimensionality associated with the complete scallop condition. It is not expected that the LEWICE cross sections in Figure 16 should match since LEWICE does not generate 3-D results. Even the most sophisticated ice accretion simulation codes do not predict the level of three dimensionality associated with a compete scallop ice accretion. It is also very difficult to compare a 2-D tracing of a highly 3-D ice accretion as small changes in spanwise location can have a very large effect on the crosssectional tracing.

Given these differences in geometry, it is interesting to compare the aerodynamic results in Figure 17. For example, the main effect on lift coefficient is not observed until the stall region where the differences in $C _ { L , \mathrm { { m a x } } }$ among the three configurations is larger than for the incomplete scallop case in Figure 15. The selected pressure distribution shown in Figure 17 is typical of the others plotted by Papadakis et al. (Refs. 24 and 25). In this case, there is a sharp contrast between the pressure signatures of the Ice1 (IRT-CS10) casting and the LEWICE ice-shape simulations. The upper-surface pressure distribution of the LEWICE configurations are very similar to what has been shown previously in Figure 7 and Figure 15. This is particularly true for the case with roughness, LR-CS10. But for the Ice1 (IRT-CS10) casting, there is a gradual pressure recovery region with peak values of suction pressure much less than for the LEWICE shapes. A similar trend was observed for Ice6 (IRT-IPSF22) which also had a highly 3-D ice accretion geometry typical of complete scallops. Since there are significant differences in cross-section geometries between the ice castings and the LEWICE simulations for Ice1 and Ice6 (not shown), better matching of the surface pressure distributions is not expected. What is of interest here is that the shape of the pressure distributions is different in the area immediately downstream of the ice shape. For the nominally 3-D LEWICE shapes, there is a fairly distinct region of approximately constant pressure that has been shown to correspond to the leading-edge vortex. For the highly 3-D geometry of the complete scallop ice casting simulation, this pressure region was not observed and the peak suction pressures were much lower. To the authors’ knowledge, the flowfield immediately downstream of the highly 3-D geometry has not been characterized or reported in the technical literature. These pressure data suggest that there exists a significantly different flowfield than for the nominally 3-D horn ice shapes reported in other swept-wing icing studies. Papadakis et al. (Ref. 24) suggest that the gaps between the scallop peaks allow high pressure air from the front face of the ice shape to leak through to the low pressure region behind the ice shape and alter the pressure distribution. Since current state-of-the-art ice accretion simulation codes are unable to predict highly 3-D features such as complete scallops, it is important to understand their impact on the aerodynamics. More research is needed to understand the flowfield associated with highly 3-D horn ice on swept wings so that the resulting impacts on wing performance may be better explained.

图片摘要：该图主要展示 16.—Comparison of IRT Ice1 (IRT CS10) and LEWICE ice shape c。
![](images/4e35e01114bab51c0c78289ccc5741a4e6fb2adfcf0006575c2977ae38adacb4.jpg)

图片摘要：该图主要展示 16.—Comparison of IRT Ice1 (IRT CS10) and LEWICE ice shape c。
![](images/11f75be1c4505bc3c3e527db4daf0536d173537dac46a98a00196d5d01b485cf.jpg)  
Figure 17.—Aerodynamic effect of IRT Ice1 (IRT-CS10) and LEWICE ice-shape simulations on GLC-305 swept wing at $\bar { R e } = 1 . 8 \times 1 0 ^ { 6 }$ , after Papadakis et al. (Ref. 24).

Unlike the situation for other ice accretion on swept wings, there are currently both experimental performance measurements as well as flowfield studies for horn ice; although these studies offer valuable insights into the effect of horn ice accretions on swept wings there is still a substantial lack of information relative to the airfoil case. For example, a shortcoming of the studies discussed in this section is that no attempt was made to ensure that the IRT generated ice shapes were accurate representations of full-scale ice accretion. Other areas where experimental data are needed include more flowfield studies for detailed ice shapes with and without scallops and different wing geometries, parametric studies investigating geometrical features of the ice such as height, shape (e.g., tip radius, roughness level), location and the influence of wing geometry.

The data presented in this section for horn ice on swept wings suggest an aerodynamic subclassification that distinguishes between “nominally 3-D” horn ice and “highly 3-D” horn ice. Nominally 3-D horn ice is associated with glaze ice accretion having either no scallops or incomplete scallops. This is only nominally 3-D since the gross shape does not vary significantly over small spanwise distances. Highly 3-D horn ice is associated with glaze ice accretion having complete scallops. In this case, the ice geometry changes significantly over small spanwise distances. From the perspective of aerodynamic classification, the difference between nominally 3-D and highly 3-D horn ice is defined in terms of the flowfield characteristics. The results discussed in this section for Figure 7 to Figure 15 were all associated with nominally 3-D horn ice as there was very little change in the simulated ice geometry in the spanwise direction. The flowfield was described in terms of the leading-edge vortex and the resulting region of approximately constant surface pressure aft of the ice shape. This was contrasted against some results for highly 3-D horn ice in Figure 16 and Figure 17 where the pressure signatures exhibited more gradual pressure recovery in place of the constant pressure regions aft of the ice shape. Due to a lack of data for highly 3-D horn ice on a swept wing, the key flowfield characteristics in this case are unknown. To further distinguish between nominally 3-D and highly 3-D horn ice flowfield characteristics is yet another area where further research is required.

# 2.3 Streamwise Ice

This section will briefly discuss the classification of streamwise ice which is most often associated with rime icing conditions (Ref. 2). They typically follow the wing leading edge contour or form a hornlike shape, or protuberance, oriented into the flow direction. The available literature on this classification is very sparse. Papadakis et al. (Ref. 24) tested one ice shape that could be classified as streamwise, Ice3 in Table I. Figure 18 shows the effect of the IRT generated streamwise ice (IRT-SC5) as well as the smooth and rough LEWICE shapes. Although not shown here, for this particular case LEWICE predicted the ice shape very well. It can be seen that the IRT shape as well as both LEWICE shapes increased $C _ { L \mathrm { m a x } }$ An increase in the maximum lift due to a streamwise ice shape has been observed on airfoils (Ref. 26) and has been attributed to the ice shape effectively forming a leading-edge flap with the increase in chord length and wing area relative to the reference area. Another potential factor may be the low Reynolds number at which the experiments were performed.

There is clearly a need for more aerodynamic data for streamwise ice on swept wings. It is expected that streamwise ice will not improve maximum lift performance in most cases. More information about the flowfield is required to understand the effects of roughness on streamwise ice that are thought to be important to the aerodynamics. For streamwise ice on airfoils, the aerodynamic effects were chiefly made manifest through trailing-edge separations. While small leading-edge separation bubbles were often observed at the ice/airfoil juncture this flowfield feature did not play a decisive role in the resulting aerodynamics. For swept wings, it is expected that this separation, if present, may lead to leading-edge vortex formation. It remains to be determined which of these effects, or perhaps both, contribute to the observed performance changes on the iced swept wing.

图片摘要：该图主要展示 18.—Effect of streamwise ice on lift. . Adapted from Papadak。
![](images/08a5682d823f33ea1ca545db26bfea188b1c76c43826a913527a9fb7b38ca2e5.jpg)  
Figure 18.—Effect of streamwise ice on lift. $\mathsf { \Pi } \mathsf { \check { R } e } = 1 . 8 \mathsf { x } 1 0 ^ { 6 }$ . Adapted from Papadakis et al. (Ref. 24).

# 2.4 2.4 Spanwise Ridge Ice

Spanwise-ridge ice can be associated with a number of icing conditions where the wing leading edge is free of ice with sometimes large ice formations located farther downstream. Typical examples are SLD icing conditions coupled with ice-protection system operation. Large drops can impinge on the wing aft of the protected areas sometimes forming an ice accretion best described as a ridge. Spanwise-ridge ice can also form when a heated leading-edge, ice-protected surface is not evaporating all of the impinging water. The liquid water flows downstream from the ice-protection system where it freezes forming a ridge oriented in the spanwise direction.

Like streamwise ice, there is very little available data on spanwise ridge ice. Papadakis et al. (Ref. 27) performed a parametric study of spanwise-ridge ice on the same, swept GLC-305 model used by Papadakis et al. (Ref. 24). Ice shapes were simulated by uniformly extending the simple geometries, shown in Table II, across the span of the wing. The method of simulating spanwise-ridge ice with simple geometries is common practice for airfoils (Ref. 28). It is unknown if any effort was made to use simulations that accurately represented any documented full-scale ice accretion. The ridge heights ranged from 0.2 to 0.5-in. corresponding to 1 to 2.7 percent of the 18.72-in. mean aerodynamic chord. Each iceshape simulation was tested at 2.5, 5, 10, 15, 20 and 30 percent chord measured in the streamwise direction. The effect of ridge size could be assessed by comparing performance measurements for the ice simulation RB-2 and RB-6 which showed that for a given chordwise location the larger ridge had a more significant impact. The importance of ridge shape could be observed by comparing results for RB-4 and RB-5 which showed that RB-4, with the flat surface facing forward, resulted in lower $C _ { L \mathrm { m a x } }$ and higher drag than RB-5, with the round surface facing forward. Similar results were observed in parametric studies of spanwise ridge ice on airfoils (Ref. 29) These parametric studies with airfoils showed that the chordwise location of the ridge was very important, and that the most severe penalties occurred when the ridge was located in a region of strong adverse pressure gradient (Ref. 2 and 29). In their test, Papadakis et al. (Ref. 27) observed that a given spanwise ridge simulation had the largest effect when it was located at 2.5 percent of the chord. Figure 19 shows the effect of all six simulated spanwise ridge shapes on the pressure distribution at 15 percent semispan of the wing for two different locations of the ice shapes, 2.5 and 15 percent. The angle of attack was $4 ^ { \circ }$ and the Reynolds number $1 . 8 \times 1 0 ^ { 6 }$ . It can be seen that the suction peak of the clean wing was located at approximately 1 percent of the chord and therefore the spanwise ridge at 2.5 percent was located in a region of severe adverse pressure gradient. Figure 19(a) shows that when the ice shape was located at 2.5 percent it prevented the formation of the initial suction

peak. The suction peak observed in the figure is due to the flow accelerating over the ice shape rather than around the leading edge. In contrast, Figure 19(b) shows that when the ice shape was located at 15 percent the leading-edge suction peak was able to form which resulted in increased lift. Very similar results were observed by Lee and Bragg (Ref. 29) during their experiments with spanwise ridges on airfoils.

TABLE II.—SIMULATIONS OF SPANWISE RIDGE ICE USED BY PAPADAKIS ET AL. (REF. 27)   

<table><tr><td>Ice shape configurations</td><td>Dimensions</td><td>Flow direction</td></tr><tr><td>RB-1</td><td>0.2 in. (5 mm) 0.28 in. (7 mm)</td><td>→</td></tr><tr><td>RB-2</td><td>0.25 in. (6.35 mm) 0.25 in. (6.35 mm)</td><td>→</td></tr><tr><td>RB-3</td><td>0.2 in. (5 mm) 0.2 in. (5 mm)</td><td>→</td></tr><tr><td>RB-4</td><td>0.25 in. (6.35 mm) 0.25 in. (6.35 mm)</td><td>→</td></tr><tr><td>RB-5</td><td>0.25 in. (6.35 mm) 0.25 in. (6.35 mm)</td><td>→</td></tr><tr><td>RB-6</td><td>0.5 in. (12.7 mm) 0.5 in. (12.7 mm)</td><td>→</td></tr></table>

图片摘要：该图主要展示 II.—SIMULATIONS OF SPANWISE RIDGE ICE USED BY PAPADAKIS ET A。
![](images/7427bb30ed01bb9c0e408f35d6168bd27f57a8605af41b8672d1d0fb7afc7784.jpg)  
(a) Ice shape at $\mathsf { x } / \mathsf { c } = 0 . 0 2 5$

图片摘要：该图主要展示 II.—SIMULATIONS OF SPANWISE RIDGE ICE USED BY PAPADAKIS ET A。
![](images/5a5f43579b7fe59c9735336e74bba8cf713244df88fbf9fa3a59c41ef81993b8.jpg)  
(b) Ice shape at $\mathsf { x } / \mathsf { c } = 0 . 1 5$   
Figure 19.—Effect of different spanwise ridge ice simulations on pressure distribution at 15 percent span of GLC-305 swept wing at ${ \mathfrak { a } } = 4 ^ { \circ }$ and $\mathsf { R e } \overset { \cdot } { = } 1 . 8 \times 1 0 ^ { 6 }$ . Ice shape located at (a) 2.5 percent and (b) 15 percent chord. Adapted from Papadakis et al. (Ref. 27).

All of the ice shapes tested by Papadakis et al. (Ref. 27) resulted in reduced lift curve slopes and increased drag regardless of the chordwise location; however, for most of the ice shapes and locations tested the maximum lift coefficient increased relative to the clean wing. The effects of the simulated ice shapes, located at 15 percent chord, on lift are shown in Figure 20. It can be seen that although the lift curve slope was reduced for the iced cases, the stalling angle of attack and maximum lift coefficient increased.

Increases in lift coefficient at high angles of attack have been observed for spanwise-ridge ice accretions on airfoils. Whalen (Ref. 30) and Papadakis et al. (Ref. 31) investigated the effects of simulated spanwise-ridge ice accretions on airfoils at Reynolds numbers of $1 . { \bar { 8 } } \times 1 0 ^ { 6 }$ and $2 . 0 \times 1 0 ^ { 6 }$ , respectively. They both observed that when the clean airfoil exhibited trailing-edge stall and the height of the ice simulation was comparable to the local boundary-layer thickness, the iced airfoil performed better at angles of attack near and above clean wing stall. This performance enhancement was attributed to the mixing layer generated by the ice shape entraining higher-momentum fluid into the boundary layer. This explanation may not suffice for the case of the ice simulations shown in Table II. The size of these simulations ranged from 0.2-to 0.5-in., likely making them significantly larger than the local boundary layer. It is also important to note that Broeren et al. (Ref. 32) showed that this lift enhancing effect on airfoils can be an artifact of low-Reynolds number testing of the clean airfoil. Their results showed that it is possible for the iced airfoil to have better high angle of attack performance characteristics than the clean airfoil at a Reynolds number of $1 . 8 \times 1 0 ^ { 6 }$ , but when compared to the clean airfoil at a Reynolds number of $1 5 . 9 \times 1 0 ^ { 6 }$ the iced airfoil performance degraded substantially. Due to these results it is difficult to determine the exact cause of the performance enhancement seen by Papadakis et al. (Ref. 27). This also emphasizes the importance of investigating Reynolds number effects where such data are lacking.

Future research on spanwise ridge ice should explore Reynolds number effects. The authors are unaware of any swept-wing studies that used high-fidelity spanwise ridge ice shapes formed from castings of actual ice accretions. As a result, there are no data that can be used to validate the method of simulating ice shapes with simple geometries on swept wings. It is well known that real spanwise-ridge type ice accretion can be highly 3-D with significant spanwise variation in the gross shape. Any future work must be supplemented with extensive flowfield studies in order to improve our understanding of how the ice accretions affect the aerodynamics of swept wings. Of particular interest is the spanwise vortex interaction with the spanwise ridge in determining the attendant aerodynamic effects.

图片摘要：该图主要展示 19.—Effect of different spanwise ridge ice simulations on pr。
![](images/da2fcd178811b554e77efd6ae54c0c212d3b1747a3937b97f7200ca2659737ce.jpg)  
Figure 20.—Effect of simulated spanwise-ridge ice shapes located at 15 percent chord on GLC-305 swept wing, $\mathsf { R e } = 1 . 8 \dot { \times } 1 0 ^ { 6 }$ , after Papadakis et al. (Ref. 27).

# 3.0 Summary

The continued design, certification and safe operation of swept-wing airplanes in icing conditions rely on the advancement of computational and experimental simulation methods for higher fidelity results over an increasing range of aircraft configurations and performance, and icing conditions. There is increasing demand to balance trades-offs in aircraft efficiency, cost and noise that tend to compete directly with allowable performance degradations over an increasing range of icing conditions. Aircraft icing research has now reached the level of maturity that computational methods and experimental tools are currently being used to address many of these challenges. However, knowledge gaps do remain for swept-wing geometries and larger droplet icing conditions. The current state-of-the-art in icing aerodynamics is mainly built upon a comprehensive understanding of 2-D geometries developed from myriads of research efforts described in the technical literature. Such an understanding for fundamentally 3-D geometries such as swept wings does not currently exist. The purpose of this report is to describe what is known of iced-swept-wing aerodynamics; to identify the type of research that is required to improve the current understanding; and to develop an aerodynamically based classification of swept-wing ice accretion. This report focuses on the fundamental aerodynamics of iced swept wings. The existing data tend to be: (1) mostly at low-Reynolds number and (2) applicable to simple swept-wing geometries that do not have high-lift systems, wing-mounted engines, fuselages and other features of actual airplane wings. These factors can significantly alter the iced aerodynamics for particular configurations and so extreme caution must be exercised in terms of making general conclusions based upon the current, limited database.

Ice accretion formations on swept wings can have unique characteristics. Depending upon specific icing conditions and sweep angle, the region of the attachment line may not be smooth as is often the case for airfoils. While initial roughness and rime ice accretion on swept wings tend to look very similar to that on airfoils, there can be significant differences for glaze ice accretion. For glaze icing, certain combinations of icing conditions and sweep angle can lead to the formation of highly 3-D features called scallops that do not exist for ice accretions on airfoils. It is also possible to have glaze ice accretion with no scallops or even incomplete scallop formations on swept wings.

Following the method used in a previous review of iced-airfoil aerodynamics, this report classifies swept-wing ice accretion into four groups that are based upon unique flowfield features. Instead of relying upon ice accretion terminology such as rime and glaze, the four aerodynamic groups have names associated with ice-shape geometry. These four groups are: ice roughness, horn ice, streamwise ice and spanwise-ridge ice. This report attempts to describe the unique flowfield features of each group that determines the iced-wing aerodynamics:

Ice roughness represents initial leading-edge ice accretion and a key aerodynamic characteristic is that the scale of the boundary-layer separation is of the same order as the size of the roughness. While there are many studies that have looked at roughness effects on swept-wing performance, including Reynolds number effects, there is a lack of flowfield data from which to interpret these results. More data are needed to understand the effects of roughness size, location and concentration on swept-wing aerodynamics.   
Horn ice is large, leading-edge ice accretion that can be associated with glaze icing conditions. The flowfield is characterized by large-scale, boundary-layer separation originating at the horn. This separation leads to the formation of a spanwise-running, leading-edge vortex that is similar to that found on clean swept wings with leading-edge separation. There are a number of low-Reynolds number studies that have characterized the horn-ice flowfield for swept wings and documented the behavior of the leading-edge vortex preceding wing stall. This presents an excellent starting point, especially for nominally 3-D horn shapes such as those with no scallops or even incomplete scallops. However, there are no flowfield data known to the authors for highly

3-D horn ice such as complete scallop formations. Therefore, the fundamental aerodynamics are essentially unknown in this case. This is an important factor since the associated performance penalties may be large. The small amount of existing data indicate that there are fundamental flowfield differences between nominally 3-D horn ice characterized by no scallop formations versus highly 3-D horn ice characterized by fully developed scallop formations. Flowfield data, such as mean and fluctuating velocity profiles and surface shear stress are needed to further understand the important differences observed between these two cases of horn ice on swept wings.

• Streamwise ice can be associated with rime icing conditions and is generally conformal to the wing leading edge, or may form a horn-like feature (or protuberance) oriented into the flow direction. The only example of this group cited in this report showed an increase in wing maximum lift coefficient with the streamwise ice. While this effect may be possible, it is not expected to hold for most cases and illustrates the need for further wing performance data and flowfield information with realistic streamwise ice simulations.   
• Spanwise-ridge ice can be associated with ice protection system operation in SLD icing conditions or incomplete evaporation of impinging water. The leading edge is free of ice with an ice ridge located downstream often in the range of 10 to 15 percent chord. This report describes data from only one low-Reynolds number study for very simple geometric representations of spanwise-ridge ice on a swept wing. More aerodynamic performance data and flowfield information are needed for realistic spanwise-ridge ice simulations.

For all of the proposed ice-shape classifications, relatively little is known about the 3-D flowfield and even less about the effect of Reynolds number and Mach number on these flowfields. Both of these deficiencies are important and limit the ability to classify swept-wing ice accretion. Most of the data found in the literature pertain only to aerodynamic performance. Except for nominally 3-D horn ice, flowfield information is limited to some pressure distributions, all at low-Reynolds number. Variations in Reynolds number found for iced-swept wings are all for relatively low-Reynolds number and provide no guidance as to the appropriateness of these data at Reynolds numbers approaching flight. In the 2-D case, Reynolds and Mach number effects have been shown to be small in most cases and low-Reynolds number data have been used extensively to classify ice shapes and improve our understanding of iced-airfoil flowfields and aerodynamics. The very limited data available on swept wings to date suggest a similar result, but much more data are needed, particularly for realistic ice-shape simulations at higher Reynolds numbers.

The classifications and supporting data presented in this report can serve as a starting point as new research explores swept-wing aerodynamics with ice shapes. As further results become available, it is expected that these classifications will need to be revised just as has occurred in the airfoil case.

# References

1. Lynch, F.T., and Khodadoust, A., “Effects of Ice Accretions on Aircraft Aerodynamics,” Progress in Aerospace Sciences, Vol. 37, No. 8, Nov. 2001, pp. 669-767.   
2. Bragg, M.B., Broeren, A.P., and Blumenthal, L.A., “Iced-Airfoil Aerodynamics,” Progress in Aerospace Sciences, Vol. 41, No. 5, Jul. 2005, pp. 323-362.   
3. Broeren, A.P., Diebold, J.M. and Bragg, M.B., “Aerodynamic Classification of Swept-Wing Ice Accretion,” NASA/TM—2013-216381, 2013   
4. Vargas, M., “Current Experimental Basis for Modeling Ice Accretions on Swept Wings,” Journal of Aircraft, Vol. 44, No. 1, Jan.-Feb. 2007, pp. 274-290.   
5. Anderson D. N. and Shin J., “Characterization of Ice Roughness from Simulated Icing Encounters,” AIAA Paper 1997-0052.   
6. Shin, J., “Characteristics of Surface Roughness Associated with Leading-Edge Ice Accretion,” AIAA Paper 1994-0799.

7. Neely, R.H, and Connor, D.W., “Aerodynamic Characteristics of a $4 2 ^ { \circ }$ Swept-Back Wing With Aspect Ratio 4 and NACA 641-112 Airfoil Sections at Reynolds Numbers From 1,700,000 to 9,500,000,” NACA RM L7D14, 1947.   
8. Kind, R.J., and Lawrysyn, M.A., “Effects of Frost on Wing Aerodynamics and Take-Off Performance,” Paper 8 in “Effects of Adverse Weather on Aerodynamics,” AGARD-CP-496, Dec. 1991.   
9. Papadakis, M., Yeong, H.W., Chandrasekharan, R., Hinson, M., and Ratvasky, T.P., “Effects of Roughness on the Aerodynamic Performance of a Business Jet Tail,” AIAA Paper 2002-0242, Jan. 2002.   
10. Vargas, M., Papadakis, M., Potapczuk, M.G., Addy, H.E. Jr., Sheldon, D., and Giriunas, J., “Ice Accretions on a Swept GLC-305 Airfoil.” SAE 02GAA-43, SAE General Aviation Technology Conference and Exhibition, Wichita, KS, Apr. 2002, Also NASA/TM—2002-211557, Apr. 2002.   
11. Khodadoust, A. and Bragg, M.B., “Measured Aerodynamic Performance of a Swept Wing with a Simulated Ice Accretion,” AIAA Paper 1990-0490.   
12. Kwon, O.J., and Sankar, L.N., “Numerical Study of the Effects of Icing on Fixed and Rotary Wing Performance,” AIAA Paper 91-0662, Jan. 1990.   
13. Poll, D.I.A., “Spiral Vortex Flow Over a Swept-Back Wing,” Aeronautical Journal, May 1986.   
14. Bragg, M.B., Kerho, M.F., and Khodadoust, A., “LDV Flowfield Measurements on a Straight and Swept Wing with a Simulated Ice Accretion,” AIAA Paper 93-0300, Jan. 1993.   
15. Diebold, J.M, Monastero, M.C. and Bragg, M.B., “Aerodynamic of a Swept Wing with Ice Accretion at Low Reynolds Number,” AIAA 2012-2795   
16. Vassberg, J.C., DeHaan, M.A., Rivers, S.M. and Wahls, R.A., “Development of a Common Research Model for Applied CFD Validation Studies,” AIAA 2008-6929   
17. Diebold J.M. and Bragg, M.B., “Study of a Swept Wing with Leading-Edge Ice Using A Wake Survey Technique,” To be presented at the 51st AIAA Aerospace Sciences Meeting, January 2013.   
18. Brune, G. W., “Quantitative Low Speed Wake Surveys,” Journal of Aircraft Vol. 31, No. 2, 1994.   
19. Hoerner, S.F., Fluid-Dynamic Lift, Hoerner Fluid Dynamics, Brick Town, NJ, 1975.   
20. Papadakis, M., Alansatan, S., and Yeong, H.W., “Aerodynamic Performance of a T-Tail with Simulated Ice Accretions,” AIAA Paper 2000-0363, Jan. 2003.   
21. Wright, W.B., “User’s Manual for LEWICE Version 3.2,” NASA/CR—2008-214255, Jan. 2008.   
22. Busch, G.T., Broeren, A.P., and Bragg, M.B., “Aerodynamic Simulation of a Horn-Ice Accretion on a Subscale Model,” AIAA Paper 2007-0087, Jan. 2007.   
23. Papadakis, M., Gile-Laflin, B.E., Youssef, G.M., Ratvasky, T.P., “Aerodynamic Scaling Experiments With Simulated Ice Accretions,” AIAA Paper 2001-0833, Jan. 2001.   
24. Papadakis, M., Yeong, H.W., Wong, S.C., Vargas, M., and Potapczuk, M.G., “Aerodynamic Performance of a Swept Wing with Ice Accretions,” AIAA Paper 2003-0731, Jan. 2003.   
25. Papadakis, M., Yeong, H.W., Wong, S, Vargas, M and Potapczuk, M., “Experimental Investigation of Ice Accretion Effects on a Swept Wing,” DOT/FAA/AR-05/39, Aug. 2005.   
26. Bragg, M.B., and Gregorek, G.M., “Wind Tunnel Investigation of Airfoil Performance Degradation Due to Icing,” AIAA Paper 82-0582, Jan. 1982.   
27. Papadakis, M., Yeong, H.W., and Wong, S.C., “Aerodynamic Performance of a Swept Wing with Simulated Ice Shapes,” AIAA Paper 2004-0734, Jan. 2004.   
28. Busch, G.T, “Experimental Study of Full-Scale Iced-Airfoil Aerodynamic Performance Using Sub-Scale Simulations,” Ph.D. Dissertation, Dept. of Aeronautical and Astronautical Engineering, Univ. of Illinois Urbana-Champaign, Urbana, IL, 2009.   
29. Lee, S. and Bragg, M.B., “Effects of Simulated-Spanwise Ice Shapes on Airfoils: Experimental Investigation,” AIAA Paper 99-0092, 1999   
30. Whalen, E.A. “Aerodynamics of Runback Ice Accretions,” Ph.D. Dissertation, Dept. of Aeronautical and Astronautical Engineering, Univ. of Illinois Urbana-Champaign, Urbana, IL, 2007.   
31. Papadakis, M., and Gile-Laflin, B.E., “Aerodynamic Performance of a Tail Section with Simulated Ice Shapes and Roughness,” AIAA Paper 2001-0539, Jan. 2001.

32. Broeren, A.P., Whalen, E. A., Busch, G.T., and Bragg, M.B., “Aerodynamic Simulation of Runback Ice Accretion,” AIAA Paper 2009-4261, Jun. 2009.

图片摘要：该图片与32. Broeren, A.P., Whalen, E. A., Busch, G.T., and Bragg, M.B., “Aerodynamic Sim这部分内容相关。
![](images/568d451a4a8180761dad50bc8763cb691031ca3c47d78124e420944b71284bf5.jpg)
