# Hall Viscosity in the Quark-Gluon Plasma

S. Mondkar1, G. Torrieri2, M. Kaminski $^ 3$ , R. Meyer $^ { 4 , 5 }$ , ∗

1 Harish-Chandra Research Institute, A CI of Homi Bhabha National Institute, Chhatnag Road, Jhusi, Prayagraj (Allahabad) 211019, India

2 Department of Physics Gleb Watagin, University of Campinas, Campinas, Brazil

3 Department of Physics and Astronomy, University of Alabama, 514 University Boulevard, Tuscaloosa, AL 35487, USA

4 Institute for Theoretical Physics and Astrophysics, Julius-Maximilians Universität Würzburg, and Würzburg-Dresden Cluster of Excellence ctd.qmat, 97074 Würzburg, Germany

5 Shanghai Institute for Mathematics and Interdisciplinary Sciences (SIMIS), Shanghai, 200433, China * rene.meyer@physik.uni-wuerzburg.de

March 25, 2026

# Abstract

We study the Hall viscosity of the quark–gluon plasma (QGP) created in non-central heavy-ion collisions. In the presence of a strong magnetic field or vorticity, rotational symmetry is broken from $O ( 3 )$ to $O ( 2 )$ , allowing for two independent Hall viscosities associated with shear deformations transverse and parallel to the symmetry-breaking direction. We find the corresponding constitutive relations by extending the kinetic-theory mechanism to three spatial dimensions and provide parametric estimates of the Hall viscosities under realistic QGP conditions. Both kinetic-theory and holographic estimates indicate that Hall viscosities are comparable in magnitude to the shear viscosity at zero magnetic field. We further show that Hall viscous stresses at hydrodynamic initialization can be as large as standard viscous corrections and identify observable consequences in flow and event-plane correlations.

# Contents

1 Introduction 2   
2 Generating Hall viscosity in the QGP 4

2.1 Hall viscosities in three-dimensional non-relativistic hydrodynamics 4   
2.2 Estimated Hall viscosities from kinetic theory 6   
2.3 Estimated Hall viscosities from holography 9

3 Observables 10

3.1 Quantitative estimates of Hall viscosity effects on the QGP 11   
3.2 Observables and their quantitative estimates 14

4 Conclusions and Outlook 17

A Hall viscosities 19   
B The Alekseev mechanism in two-dimensional non-relativistic hydrodynamics 19   
C Derivation of early-time velocity gradients 21

References 23

# 1 Introduction

The quark-gluon plasma (QGP) created in ultra-relativistic heavy-ion collision (HIC) experiments behaves as a nearly perfect fluid with a small specific shear viscosity. Relativistic hydrodynamics has emerged as a remarkably successful framework for describing the spacetime evolution of the QGP at intermediate times. A broad set of collective observables, including anisotropic flow coefficients $v _ { n }$ , their event-by-event fluctuations and multiparticle cumulants, as well as long-range rapidity correlations, are quantitatively described by viscous relativistic hydrodynamics, initialled by Glauber or color glass initial conditions and converted into particle distributions using an isentropic Cooper-Frye ansatz. [1–3]. However, the exact parameters characterizing this fluid are subject to both theoretical and phenomenological studies [4,5], the latter employing state-of-the-art machine learning techniques [6].

This effort is justified by the fact that not all possible transport coefficients have yet been studied. There is growing evidence that strong and rapidly varying electromagnetic fields are present in noncentral HICs reaching peak values of $1 0 ^ { 1 8 } - 1 0 ^ { 1 9 }$ G at RHIC/LHC energies [7]. These are accompanied by sizable vorticity [8] associated with the initial angular momentum of the system. However, the full constitutive relations of hydrodynamic fields in the presence of magnetic fields and vorticity are still not fully available [4, 9]. The situation is both more complicated and interesting, as magnetic fields and vorticity break fundamental symmetries such as isotropy, allowing for a much greater variety of transport coefficients. Furthermore, we know that topological features of QCD [10] induce quantum anomalies and hence further transport coefficients [11], in the presence of both magnetic fields and vorticity. The effective theory of hydrodynamics, including all these effects, is likely to be much richer than that considered in [4, 9], and the sort of broad data analysed in [5] could well contain the effects of such hitherto undiscovered terms.

In this work, we concentrate on a particular transport coefficient, the Hall viscosity, which, remarkably, results from such a rotational symmetry breaking and, as we show, leads to a unique experimental signature, c.f. Fig.1 for an illustration. Hall viscosity [12–14] is a non-dissipative transport coefficient leading to novel hydrodynamic effects. From kinetic theory in two-dimensional Dirac semimetals like graphene, it is known that a magnetic field generates a Hall viscosity, $\ddot { \eta } _ { \perp }$ , in a plane perpendicular to it [15]. In three spatial dimensions, however, the structure of Hall viscous transport is richer and more subtle. Once rotational symmetry is broken from $O ( 3 )$ to $O ( 2 )$ by a background field such as the direction of a magnetic field or vorticity, two independent Hall viscosity coefficients are allowed, corresponding to shear deformations parallel and perpendicular to the symmetry-breaking direction [16–18]. This is illustrated in Fig. 2 for a magnetic field breaking the rotational symmetry. These two Hall viscosities are related through Kubo formulae [19] to the retarded correlator of the off-diagonal components of the stress-energy tensor $T ^ { \mu \nu }$ as [17, 18, 20, 21]

$$
\tilde {\eta} _ {| |} = \lim _ {\omega \to 0} \frac {\mathrm {I m} \langle T ^ {y z} T ^ {x y} \rangle (\omega)}{\omega}, \quad \tilde {\eta} _ {\perp} = \lim _ {\omega \to 0} \frac {\mathrm {I m} \langle T ^ {x z} (T ^ {x x} - T ^ {z z}) \rangle (\omega)}{\omega}, \qquad (1)
$$

evaluated at vanishing spatial momentum and in the limit of vanishing frequency $\omega  0$ . Despite being allowed by symmetry, such Hall viscous terms have received comparatively little attention in the context of QGP phenomenology.

The primary goal of this work is to systematically analyze Hall viscosity in the QGP and to assess its potential phenomenological relevance in HICs. We first discuss how in non-relativistic hydrodynamics with broken rotational symmetry, the stress tensor admits two distinct Hall viscosity coefficients, which we denote as $\tilde { \eta } _ { \perp }$ and $\tilde { \eta } _ { \parallel }$ . This is accomplished by extending a simple kinetic-theory mechanism originally proposed by Alekseev for two-dimensional charged fluids to three dimensions, demonstrating how Hall viscosity arises from Lorentz-force-induced distortions of the distribution function. We derive the corresponding constitutive relations from the kinetic theory mechanism of [15], and estimate the size of $\bar { \eta } _ { \parallel }$ and $\bar { \eta } _ { \perp }$ ”. Complementing this weak-coupling analysis, we also discuss estimates of Hall viscosity at strong coupling using holographic methods.

Finally, we focus on the implications of Hall viscosity for the early-time dynamics of the QGP. Rather than attempting a full magnetohydrodynamic simulation, we provide controlled order-ofmagnitude estimates of Hall viscous stress corrections at hydrodynamic initialization time, using realistic velocity gradients appropriate for HICs. We outline how Hall viscosity may influence the evolution of collective flow in HICs and identify an experimental observable sensitive to the Hall viscous effects.

图片摘要：该图主要展示 1: (a) A qualitative illustration of the effect of the trans。
![](images/9707d8fd6e91ad362952cf69c6fa311712d683207a77574ce7540713ead59362.jpg)  
(a)

图片摘要：该图主要展示 1: (a) A qualitative illustration of the effect of the trans。
![](images/d3499839079796a56e484c36e9ad18fbddacaf12da8e9d9e324c789c656f798f.jpg)

图片摘要：该图主要展示 1: (a) A qualitative illustration of the effect of the trans。
![](images/c978725fd51728a625099a784ee3b9668cd0c64e7f3129e8d73d3f8402d3cf9e.jpg)  
(b)   
Figure 1: (a) A qualitative illustration of the effect of the transverse Hall viscosity $\tilde { \eta } _ { \perp }$ on a QGP fireball with elliptic flow. This viscosity couples vorticity to azimuthal shear, $T _ { x x } \mathrm { ~ - ~ } T _ { z z }$ , hence causing an elongation of the fireball due to longitudinal polarization. (b) A qualitative illustration of the effect the longitudinal Hall viscosity $\tilde { \eta } _ { \parallel }$ on a QGP fireball with transverse polarization. This viscosity couples azimuthal to longitudinal shear, causing the fireball to spin, i.e. rotate perpendicular to the longitudinal vorticity.

Before we proceed, a comment on the convention of the coordinate axes is in order. In the heavy-ion literature, the most commonly adopted convention is as follows: The beam axis direction is along the $\mathbf { Z }$ -axis, and the impact parameter direction is along the $x$ -axis. Therefore, the $x , z$ -plane constitutes the reaction plane. The $y$ -axis direction is the out-of-plane direction. For off-central HICs, the overlap region of the two colliding nuclei at the point of closest approach is an almond-shaped region with the short axis of the almond along the impact parameter direction ( $x$ -axis) and the long axis of the almond along the out-of-plane direction ( $_ y$ -axis). This initial spatial anisotropy in the $x$ and $y$ directions gives rise to pressure anisotropy in these two directions, resulting in the rapid expansion of the fireball in the $x$ -direction compared to its expansion in the $y$ -direction. This pressure anisotropy gives rise to the flow coefficient $v _ { 2 }$ . The magnetic field generated in the collision of the two nuclei is initially oriented perpendicular to the reaction plane, that is, in the $y$ -direction [22–25]. Additionally, the axis of rotation of the fireball is also oriented perpendicular to the reaction plane, so also in the $y$ -direction [26–28].

Before proceeding, we emphasize the scope of the present work. Our analysis is not a full relativistic magneto-hydrodynamic simulation of the QGP, nor does it include the dynamical evolution of electromagnetic fields. Instead, our goal is to establish the existence, parametric magnitude, and phenomenological relevance of Hall viscous transport in the QGP through controlled analytic estimates. The results presented here should therefore be viewed as order-of-magnitude benchmarks that motivate future quantitative simulations incorporating Hall viscosity.

The main new results of this work are threefold: (i) a systematic derivation of the non-relativistic Hall viscous terms in the constitutive relations in three spatial dimensions with broken rotational symmetry from kinetic theory, (ii) the first quantitative estimates of Hall viscosities for QGP-relevant parameters using both kinetic theory and holography, and (iii) the identification of experimentally accessible signatures of Hall viscosity in heavy-ion collisions.

The paper is organized as follows. In Sec. 2.1, we derive the constitutive relations for threedimensional non-relativistic hydrodynamics in the presence of magnetic fields and derive the expressions for Hall viscosities. In Sec. 2.2 and 2.3, we present kinetic-theory and holographic estimates of the Hall viscosity coefficients, respectively. In Sec. 3, we evaluate the size of Hall viscous corrections

图片摘要：该图主要展示 2: Illustration of the distinct effect of the two Hall visco。
![](images/2d52eb1695328bf2c50536e16db82eb043df1717af483cea8fe467d8df28afec.jpg)  
transverse Hall viscosity

图片摘要：该图主要展示 2: Illustration of the distinct effect of the two Hall visco。
![](images/81fb915b76b92f04d3a08e3c51fbe74184969d6804a7ef4b25ecf28757feacb7.jpg)  
longitudinal Hall viscosity   
Figure 2: Illustration of the distinct effect of the two Hall viscosities on the stress-energy tensor components $T ^ { \mu \nu }$ in response to different shear flows. The magnetic field points along the $y$ -direction, the beamline is along $z$ , and the fluid flow has been chosen to have a shear in either the $x z$ -plane or the $x y$ -plane.

under QGP conditions and discuss their phenomenological implications. We conclude in Sec. 4 with a summary and outlook.

# 2 Generating Hall viscosity in the QGP

In this section, we will explain our mechanism of how Hall viscosity is generated in the magnetic fields present in HICs, and estimate the order of magnitude of the resulting Hall viscosities both in the perturbative regime as well as from holography.

# 2.1 Hall viscosities in three-dimensional non-relativistic hydrodynamics

In three spatial dimensions, Hall viscosity is a genuine tensor component of the viscosity tensor [14], and hence vanishes identically in the presence of rotational invariance even if time-reversal symmetry is broken [13]. However, the magnetic field breaks both time-reversal and rotational invariance, and therefore, non-zero Hall viscosity can be obtained in the presence of a magnetic field. In this subsection, we extend the mechanism proposed by Alekseev [15] for the generation of two-dimensional Hall viscosity, which we review in App. A, to non-relativistic kinetic theory in three dimensions. We will show that in three dimensions two Hall viscosities emerge in the presence of an external magnetic field, one parallel and one in the plane perpendicular to the magnetic field.

Alekseev’s mechanism [15] relies on kinetic theory, which itself relies on the existence of quasiparticles in the described medium. In the QGP, the relevant quasiparticles to which the magnetic field couples are in-medium quarks, and in the following we denote by $\tau _ { 2 }$ the relaxation time associated with the second moments of the quasiparticle distribution function.1 The reason that we can apply non-relativistic kinetic theory to the QGP is that the magnetic field induced Hall viscosity stems from the coupling of the magnetic field to the quarks. Since advective forces on a cell of size of the mean free path $\lambda$ are of order $\frac { \lambda } { e } \frac { d p } { d x }$ , these forces will not induce large comoving velocities. Hence, in a comoving cell frame, the quarks, with their thermally dressed masses being $\mathcal { O } ( 6 0 0 M e V )$ , can be

treated non-relativistically for a qualitative estimate of the Hall viscosities and the effects induced by them. The viscous stress tensor is given by $\Pi _ { i j } : = m \langle { v } _ { i } { v } _ { j } \rangle$ , where $\mathbf { v } = ( v _ { x } , v _ { y } , v _ { z } )$ is the threedimensional velocity of a single quasiparticle and the angular brackets stand for averaging over the quasiparticle velocity distribution at a given spatial location ${ \bf r } = ( x , y , z )$ . The equation of motion for the hydrodynamic velocity $V _ { i } = \langle v _ { i } \rangle$ in the absence of magnetic field is

$$
m \frac {\partial V _ {i}}{\partial t} = - \frac {\partial \Pi_ {i j}}{\partial x _ {j}} + e E _ {i}, \tag {2}
$$

where $E _ { i }$ is the external electric field, and we have assumed Einstein summation convention. In Müller-Israel-Stewart theory, $\tau _ { 2 }$ corresponds to the Müller-Israel-Stewart relaxation time [29–31]. At a time scale much greater than $\tau _ { 2 }$ , the expression for $\Pi _ { i j }$ is given by its steady-state value

$$
\Pi_ {i j} = \Pi_ {i j} ^ {(0)} = - \frac {m}{\varrho} \eta_ {0} V _ {i j}, \qquad V _ {i j} = \frac {\partial V _ {i}}{\partial x _ {j}} + \frac {\partial V _ {j}}{\partial x _ {i}}, \tag {3}
$$

where $m$ is the quasiparticle mass and $\varrho$ is the quasiparticle mass density. $\eta _ { 0 }$ is the dynamical viscosity with the same dimensions as the entropy density, $s$ , in the natural units. In the nonrelativistic literature, the kinematic viscosity, $\nu$ , is often used, but there is no meaningful relativistic generalization of it. Thus, in this work, we shall use the usual dynamical viscosity. The two are related by the expression

$$
\nu = \frac {\eta_ {0}}{s T + \varrho}, \tag {4}
$$

where $T$ denotes the temperature. In the non-relativistic limit $\varrho \gg s T$ , which implies $\nu \approx \eta _ { 0 } / \varrho$ . In the ultrarelativistic limit, (4) is still valid, with $s T + \varrho \approx s T$ .

$\Pi _ { i j }$ relaxes to its steady-state value $\Pi _ { i j } ^ { ( 0 ) }$ during the time $\tau _ { 2 }$ according to the Drude-like equation

$$
\frac {\partial \Pi_ {i j}}{\partial t} = - \frac {1}{\tau_ {2}} \left(\Pi_ {i j} - \Pi_ {i j} ^ {(0)}\right). \tag {5}
$$

Introducing an external constant magnetic field, $B _ { i }$ , shifts the steady-state value of $\Pi _ { i j }$ from $\Pi _ { i j } ^ { ( 0 ) }$ . Without loss of generality, we choose the magnetic field to point along the $\hat { \mathbf { y } }$ direction. This choice explicitly breaks the spatial $O ( 3 )$ rotational symmetry down to an $O ( 2 )$ symmetry in the plane transverse to $\mathbf { B } = B \hat { \mathbf { y } }$ . In the presence of a magnetic field, the time evolution of $V _ { i }$ and $\Pi _ { i j }$ is influenced not only by collisions and the electric field, but also by the magnetic component of the Lorentz force. Consequently, the evolution equations for $\partial V _ { i } / \partial t$ and $\partial \Pi _ { i j } / \partial t$ acquire additional magnetic-field–induced contributions. Explicitly, the magnetic terms entering the equations of motion (2) and (5) take the form [15]

$$
\left(\frac {\partial V _ {i}}{\partial t}\right) _ {B} = \omega_ {c} \epsilon_ {y i k} V _ {k}, \tag {6}
$$

$$
\left(\frac {\partial \Pi_ {i j}}{\partial t}\right) _ {B} = \omega_ {c} \left(\epsilon_ {y i k} \Pi_ {k j} + \epsilon_ {y j k} \Pi_ {i k}\right), \tag {7}
$$

where $\omega _ { c } = q B / m$ is the cyclotron frequency and $q$ denotes the electric charge of quasiparticles. We have assumed that the electromagnetic fields, appearing implicitly in $\omega _ { c }$ , do not alter the particle mass significantly. If they would do so, the non-relativistic approximation would be not applicable in any case, and these effects would also show up in the resulting transport coefficients. The terms (6) and (7) are added to the right-hand side of equations (2) and (5), respectively.

We work in the hydrodynamic Navier–Stokes regime and focus on the steady state, $\partial _ { t } \Pi _ { i j } = 0$ appropriate for timescales long compared to the microscopic relaxation time $\tau _ { 2 }$ . Under these assumptions, the evolution equation (5) reduces to an algebraic relation between $\Pi _ { i j }$ and the symmetrized velocity gradients. Therefore, in the steady state, $\partial _ { t } \Pi _ { i j } = 0$ , from the modified equation (5) in the presence of a magnetic field, we get the following relation

$$
\Pi_ {i j} - \omega_ {c} \tau_ {2} \left(\epsilon_ {y i k} \Pi_ {k j} + \epsilon_ {y j k} \Pi_ {i k}\right) = \Pi_ {i j} ^ {(0)}. \tag {8}
$$

Note that $\Pi _ { i j }$ denotes the dissipative part of the stress-energy tensor, obtained after subtracting the isotropic equilibrium pressure contribution. For incompressible flow, $\mathrm { d i v } \mathbf { V } : = \partial V _ { i } / \partial x _ { i } = 0$ , and

Eq. (8) implies that the viscous correction is traceless, ${ { \mathrm { I I } } _ { i i } } = 0$ . Subsequently, only two of the three diagonal components of $\Pi _ { i j }$ are independent. Since $\Pi _ { i j }$ is a symmetric rank-2 tensor, there are three independent off-diagonal components. In total, $\Pi _ { i j }$ has five independent components: $\Pi _ { x x }$ , $1 \mathrm { I } _ { z z }$ , $\Pi _ { x z }$ , $\Pi _ { x y }$ , $\Pi _ { z y }$ . We can get five coupled algebraic equations for these five components from (8). Solving the resulting coupled algebraic equations for the components of $\Pi _ { i j }$ , we obtain the following constitutive relations between the stress tensor and the symmetrized velocity gradients, $V _ { i j } = \partial _ { i } V _ { j } + \partial _ { j } V _ { i }$ ,

$$
- \frac {\Pi_ {x x}}{(m / \varrho)} = \frac {\eta_ {0}}{2} \left(V _ {x x} + V _ {z z}\right) + \frac {\eta_ {\perp}}{2} \left(V _ {x x} - V _ {z z}\right) - \tilde {\eta} _ {\perp} V _ {x z}, \tag {9a}
$$

$$
- \frac {\Pi_ {z z}}{(m / \varrho)} = \frac {\eta_ {0}}{2} \left(V _ {x x} + V _ {z z}\right) - \frac {\eta_ {\perp}}{2} \left(V _ {x x} - V _ {z z}\right) + \tilde {\eta} _ {\perp} V _ {x z}, \tag {9b}
$$

$$
- \frac {\Pi_ {x z}}{(m / \varrho)} = \frac {\tilde {\eta} _ {\perp}}{2} \left(V _ {x x} - V _ {z z}\right) + \eta_ {\perp} V _ {x z}, \tag {9c}
$$

$$
- \frac {\Pi_ {x y}}{(m / \varrho)} = \eta_ {\parallel} V _ {x y} - \frac {\tilde {\eta} _ {\parallel}}{2} V _ {z y}, \tag {9d}
$$

$$
- \frac {\Pi_ {z y}}{(m / \varrho)} = \eta_ {\parallel} V _ {z y} + \frac {\tilde {\eta} _ {\parallel}}{2} V _ {x y}. \tag {9e}
$$

The residual $O ( 2 )$ symmetry about the magnetic-field direction allows two independent shear viscosities and two independent Hall viscosities. $\eta _ { \perp }$ and $\eta _ { \parallel }$ denote the anisotropic shear viscosities. Shear viscosities are time-reversal invariant and are dissipative transport coefficients that contribute to the irreversible entropy production. In contrast, $\tilde { \eta } _ { \perp }$ and $\tilde { \eta } _ { \parallel }$ are Hall viscosities, which are odd under timereversal and encode non-dissipative responses induced by the magnetic field. These four viscosities can be expressed in terms of zero magnetic field viscosity $\eta _ { 0 }$ as

$$
\eta_ {\perp} = \frac {\eta_ {0}}{1 + \varpi^ {2}}, \quad \eta_ {| |} = \frac {4}{4 + \varpi^ {2}} \eta_ {0}, \quad \tilde {\eta} _ {\perp} = \frac {\varpi}{1 + \varpi^ {2}} \eta_ {0}, \quad \tilde {\eta} _ {| |} = \frac {4 \varpi}{4 + \varpi^ {2}} \eta_ {0}, \tag {10}
$$

where $\varpi : = 2 \omega _ { c } \tau _ { 2 }$ . As a consistency check, in the zero-field limit $\varpi  0$ the Hall viscosities $\ddot { \eta } _ { \perp }$ and $\tilde { \eta } _ { \parallel }$ vanish, while the shear viscosities reduce to their isotropic value $\eta _ { 0 }$ as required by the restoration of full rotational symmetry.

The existence of two independent Hall viscosities follows purely from symmetry considerations once rotational invariance is broken from $O ( 3 )$ to $O ( 2 )$ and time-reversal symmetry is violated. This symmetry-breaking pattern is model-independent and applies equally to weakly and strongly coupled systems. The quantitative values of these transport coefficients, however, depend on microscopic dynamics and must be estimated using specific theoretical frameworks, which we will do in the next sections.

# 2.2 Estimated Hall viscosities from kinetic theory

We now turn to estimating the magnitude of the Hall viscosities for the QGP. In this subsection we obtain order-of-magnitude estimates for the Hall viscosities of the QGP by extrapolating the kinetic theory expressions derived in Sec. 2.1 to relativistic plasma conditions. These estimates are not meant to constitute a controlled relativistic kinetic-theory calculation, but rather to provide physical intuition and a benchmark scale for the potential size of Hall viscous effects.

In non-relativistic kinetic theory, the zero magnetic field shear viscosity is given by

$$
\eta_ {0} = \frac {1}{3} \sum_ {i} \rho_ {i} \langle p \rangle_ {i} \lambda_ {i}, \tag {11}
$$

where $\rho _ { i }$ is the number density of the quasiparticle species $i$ , $\langle p \rangle _ { i }$ is the average momentum, $\lambda _ { i }$ is the mean free path. However, for an ultrarelativistic gas, the prefactor changes from $\frac { 1 } { 3 }$ to $\frac { 4 } { 1 5 }$ [32, 33], yielding

$$
\eta_ {0} = \frac {4}{1 5} \sum_ {i} \rho_ {i} \langle p \rangle_ {i} \lambda_ {i}. \tag {12}
$$

The change of factor from 1/3 to 4/15 reflects the differences in momentum transfer and particle dynamics in a relativistic regime [32, 33]. The mean free path is related to the relaxation time $\tau _ { 2 }$ by

$$
\lambda_ {i} = v _ {i} \tau_ {2} \approx c \tau_ {2}, \tag {13}
$$

where $v _ { i } \approx c$ for ultrarelativistic particles. Thus we get

$$
\eta_ {0} \approx \frac {4}{1 5} \sum_ {i} \rho_ {i} \langle p \rangle_ {i} c \tau_ {2}. \tag {14}
$$

The energy density is given by

$$
\varepsilon = \sum_ {i} \rho_ {i} \langle E \rangle_ {i}. \tag {15}
$$

For an ultrarelativistic gas, the average energy is approximately equal to the average momentum $\langle E \rangle _ { i } \approx \langle p \rangle _ { i } c$ . This simplifies the energy density expression to

$$
\varepsilon \approx \sum_ {i} \rho_ {i} \langle p \rangle_ {i} c. \tag {16}
$$

Eq. (14) and (16) together yield

$$
\eta_ {0} \approx \frac {4}{1 5} \varepsilon \tau_ {2}. \tag {17}
$$

This relation reflects the fact that, in an ultrarelativistic gas, momentum transport is governed by the energy density and the relaxation time of the second moment of the distribution function, a result well known from relativistic kinetic theory. The energy density of the QGP in the high temperature limit is given by

$$
\varepsilon \approx \frac {\pi^ {2}}{3 0} g _ {\mathrm {e f f}} T ^ {4}, \tag {18}
$$

based on an estimate using the Stefan-Boltzmann law for an ideal gas of quarks and gluons [34–36]. $g _ { \mathrm { e f f } }$ is the effective number of degrees of freedom in QCD,

$$
g _ {\text {e f f}} = g _ {g} + \frac {7}{8} g _ {q} = 2 \left(N _ {c} ^ {2} - 1\right) + \frac {7}{8} 4 N _ {c} N _ {f} = 3 7, \tag {19}
$$

where $g _ { g } \ : = \ : 2 \left( N _ { c } ^ { 2 } - 1 \right)$ ( $N _ { c }$ colors, two polarizations) is the number of gluon degrees of freedom, whereas $g _ { q } = 4 N _ { c } N _ { f }$ ( $N _ { c }$ colors, $N _ { f }$ flavors, two spins, quarks and anti-quarks) is the number of quark degrees of freedom. The contribution from quark degrees of freedom is reduced by a factor of 7/8 due to fermionic statistics. We took $N _ { c } = 3$ and $N _ { f } = 2$ , i.e., considering only two active light quark flavors for simplicity; including the strange quark would modify numerical prefactors at the $1 0 { - } 2 0 \%$ level without qualitatively affecting the parametric estimates presented below. Thus, we get an approximate energy density of the QGP as [33]

$$
\varepsilon \approx 1 2. 1 7 T ^ {4}. \tag {20}
$$

The typical temperature of the QGP is $T \approx 3 0 0$ MeV at RHIC and LHC [37–39].

The holographic prediction of the relaxation time of the QGP is $\tau _ { 2 } \approx 0 . 2 - 0 . 3 ~ \mathrm { f m / c }$ with smooth initial conditions [40] (and $0 . 4 - 0 . 6 ~ \mathrm { f m / c }$ after incorporating initial state fluctuations [41]) for the temperatures $T \approx 3 0 0 - 4 0 0$ MeV. We take the relaxation time $\tau _ { 2 }$ to be $\tau _ { 2 } \approx 0 . 4 ~ \mathrm { f m / c }$ . Using the relation $1 \ \mathrm { M e V } ^ { - 1 } = 1 9 7 . 3 \ \mathrm { f m } / c$ , $\tau _ { 2 }$ can be expressed in terms of the QGP temperature $T$ as $\tau _ { 2 } \approx 0 . 6 / T$ (for $T \approx 3 0 0$ MeV). The estimates from holographic models are close to experimentally observed QGP thermalization times. In the present context $\tau _ { 2 }$ should be viewed as an effective phenomenological relaxation time characterizing the approach to local equilibrium, rather than a quantity derived selfconsistently within weakly coupled kinetic theory.

Finally, our estimate for the zero-magnetic field shear viscosity of the QGP (17) is

$$
\eta_ {0} \approx \frac {4}{1 5} 1 2. 1 7 T ^ {4} \frac {0 . 6}{T} = 1. 9 5 T ^ {3}. \tag {21}
$$

Next, we estimate the entropy density $s$ . We have the thermodynamic relation

$$
s = \frac {\varepsilon + P}{T}. \tag {22}
$$

Using the conformal equation of state (EoS), $P = \varepsilon / 3$ , whose validity we discuss below in our regime of parameters, and the expression for energy density (20), we get

$$
s \approx \frac {4}{3} \frac {1}{T} 1 2. 1 7 T ^ {4} = 1 6. 2 3 T ^ {3}. \tag {23}
$$

Combining (21) and (23), we get an estimate for the dimensionless ratio $\eta _ { 0 } / s \approx 0 . 1 2$ , which is of the same order of magnitude as the holographic value for very strongly interacting quantum field theories dual to Einstein Gravity $1 / ( 4 \pi )$ [42, 43].

Let us compare the $\eta _ { 0 } / s$ we obtained with the $\eta / s$ obtained by Bayesian parameter estimates. In particular, Ref. [44] has $\eta / s$ roughly in the range of $0 . 0 7 \lesssim \eta / s \lesssim 0 . 1 5$ . This is in the ballpark of our estimated value of $\eta _ { 0 } / s \approx 0 . 1 2$ . Note that our estimate of $\eta _ { 0 } / s$ is independent of temperature whereas the Bayesian estimate of Ref. [44] gives temperature dependent $\eta / s$ . Recall that in our estimate $\eta _ { 0 }$ came from using the conformal EoS of QCD with two active quark flavors and using phenomenological estimate for the relaxation time. So our estimate is only valid at high enough temperatures where QGP EoS can be approximated by the conformal EoS. Ref. [44] used a lattice QCD EoS [45] for the QGP. As another consistency check, we estimate the quantity $\frac { \tau _ { 2 } ( \varepsilon + P ) } { \eta _ { 0 } }$ by using the above estimates for $\begin{array} { r } { \tau _ { 2 } \approx \frac { 0 . 6 } { T } } \end{array}$ , $\eta _ { 0 } \approx 1 . 9 5 T ^ { 3 }$ , $\varepsilon \approx 1 2 . 1 7 \ T ^ { 4 }$ , and the conformal EoS $P = \varepsilon / 3$ . We get $\frac { \tau _ { 2 } ( \varepsilon + P ) } { \eta _ { 0 } } \approx 5$ which falls within the acceptable range of $5 - 7$ given in [46], albeit at the lower end of the range.

At $T \approx 3 0 0$ MeV, we get $\eta _ { 0 } \approx 1 . 9 5 T ^ { 3 } = 5 . 2 6 \times 1 0 ^ { 7 } \mathrm { M e V } ^ { 3 }$ . In order to obtain the estimates for the viscosities of Eq. (10) in the presence of external magnetic fields, we first estimate the quantity $\varpi = 2 \omega _ { c } \tau _ { 2 }$ . $\omega _ { c }$ is the cyclotron frequency and is related, in the non-relativistic limit, to the magnetic field $B$ as $\begin{array} { r } { \omega _ { c } = \frac { q B } { m } } \end{array}$ . $q B$ is estimated to be $1 0 ^ { 1 8 }$ Gauss at RHIC [22, 47] and $1 0 ^ { 1 9 } - 1 0 ^ { 2 0 }$ Gauss at m the LHC [48]. For our order-of-magnitude estimate, we take $q B \approx 1 0 ^ { 1 9 }$ − Gauss. This estimate applies to early times relevant for the onset of hydrodynamic evolution $\tau \approx 1 ~ \mathrm { f m / c }$ ), where the magnetic field, although already decaying from its initial peak, can still be sizable depending on the electrical conductivity of the medium and can therefore generate Hall viscous stress corrections at initialization.

The effecti[49,50], where e thermal mass of quarks is related to the dimensi $m$ that appears in thess strong coupling xpression fo of QCD by $\omega _ { c }$ $m \sim g T$ $g$ $\alpha _ { s }$ $\begin{array} { r } { \alpha _ { s } = \frac { g ^ { 2 } } { 4 \pi } } \end{array}$ $\alpha _ { s }$ $\alpha _ { s } ( 3 0 0 \mathrm { M e V } ) \approx 0 . 3$ . This gives $g ( 3 0 0 ~ \mathrm { M e V } ) \approx 1 . 9 4$ . Using the relations 1 $\mathrm { G a u s s } = 1 . 9 5 \times 1 0 ^ { - 2 0 } \mathrm { G e V } ^ { 2 }$ [54], $q B \approx 1 0 ^ { 1 9 }$ Gauss in units of GeV becomes $q B \approx ~ 0 . 1 9 5 ~ \mathrm { G e V } ^ { 2 } = 1 . 9 5 \times 1 0 ^ { 5 } ~ \mathrm { M e V } ^ { 2 }$ . We can express $q B$ in terms of temperature $T$ as $q B \approx 2 . 1 7 T ^ { 2 }$ at $T \approx 3 0 0$ MeV.

Therefore we get $\begin{array} { r } { \varpi = 2 \omega _ { c } \tau _ { 2 } \approx 2 \frac { q B } { g T } \frac { 0 . 6 } { T } \approx 2 \frac { 2 . 1 7 T ^ { 2 } } { 1 . 9 4 T } \frac { 0 . 6 } { T } \approx 1 . 3 4 } \end{array}$ 6 2 2.17 T 2 0.6 . By plugging this $\varpi$ estimate in Eq. (10), we obtain the following estimates for the viscosities at $T \approx 3 0 0$ MeV

$$
\eta_ {\perp} = \frac {1}{(1 + \varpi^ {2})} \eta_ {0} \approx 0. 3 6 \eta_ {0}, \qquad \eta_ {\parallel} = \frac {4}{4 + \varpi^ {2}} \eta_ {0} \approx 0. 6 9 \eta_ {0},
$$

$$
\tilde {\eta} _ {\perp} = \frac {\varpi}{(1 + \varpi^ {2})} \eta_ {0} \approx 0. 4 8 \eta_ {0}, \quad \tilde {\eta} _ {\parallel} = \frac {4 \varpi}{4 + \varpi^ {2}} \eta_ {0} \approx 0. 9 3 \eta_ {0}. \tag {24}
$$

Recalling that the zero magnetic field viscosity is $\eta _ { 0 } \approx 5 . 2 6 \times 1 0 ^ { 7 } \ \mathrm { M e V ^ { 3 } }$ . From (24), we observe that the Hall viscosities are roughly the same order of magnitude as the anisotropic shear viscosities.

To assess the sensitivity of our estimates to the effective quasiparticle mass entering the cyclotron frequency, we consider an alternate route. Note that the masses of active u, d, and s quarks in the QGP are very small compared to the QGP temperature scale. Therefore, in the alternate approach we assume the quarks to be massless (instead of having thermal mass $\sim g T$ ). The $B$ dependence of the cyclotron frequency for ultra-relativistic massless charged Dirac fermions (electrons and holes) in graphene is given by $\omega _ { c } \propto \sqrt { B }$ [55–57]. We extrapolate this to the massless quarks in the QGP. So with $\omega _ { c } = \sqrt { q B }$ c ∝ instead of $\begin{array} { r } { \omega _ { c } = \frac { q B } { g T } } \end{array}$ , we get $\begin{array} { r } { \varpi = 2 \omega _ { c } \tau _ { 2 } = 2 \sqrt { q B } \tau _ { 2 } \approx 2 \sqrt { 2 . 1 7 T ^ { 2 } } \frac { 0 . 6 } { T } \approx 1 . 7 7 . } \end{array}$ , where we used $q B \approx 2 . 1 7 \ T ^ { 2 }$ and $\tau _ { 2 } \approx 0 . 6 / T$ . With this $\varpi \approx 1 . 7 7$ , we can provide alternate estimates for various viscosities in Eq. (10) as follows

$$
\eta_ {\perp} = \frac {1}{(1 + \varpi^ {2})} \eta_ {0} \approx 0. 2 4 \eta_ {0}, \qquad \eta_ {| |} = \frac {4}{4 + \varpi^ {2}} \eta_ {0} \approx 0. 5 6 \eta_ {0},
$$

$$
\tilde {\eta} _ {\perp} = \frac {\varpi}{\left(1 + \varpi^ {2}\right)} \eta_ {0} \approx 0. 4 3 \eta_ {0}, \quad \tilde {\eta} _ {\parallel} = \frac {4 \varpi}{4 + \varpi^ {2}} \eta_ {0} \approx 0. 9 9 \eta_ {0}. \tag {25}
$$

We notice that this estimate (25) with massless quarks does not differ much from the earlier estimate (24) with thermal mass quarks.

Taken together, these estimates indicate that both Hall viscosities, $\tilde { \eta } _ { \perp }$ and $\tilde { \eta } _ { \parallel }$ , are parametrically comparable to the anisotropic shear viscosities under realistic QGP conditions. This motivates treating Hall viscous contributions on equal footing with dissipative viscous terms when assessing their phenomenological impact.

# 2.3 Estimated Hall viscosities from holography

To complement the weak-coupling, kinetic-theory estimates presented in Sec. 2.2, we now turn to a strong-coupling estimate of Hall viscosities based on gauge–gravity duality, referring to [17, 20] and the later [18]. In particular, we compare to the field-theoretic analysis of chiral hydrodynamics in the presence of strong magnetic fields developed in Ref. [18], which derives the most general relativistic constitutive equations for a relativistic plasma containing chiral fermions in the presence of a strong external magnetic field carrying an anomalous $U ( 1 )$ charge. This field theoretic derivation yields relativistic Kubo formulae for the Hall viscosities. These are the relativistic counterparts to the non-relativistic Hall viscosities introduced in Sec. 2.1. Ref. [18] then provides a controlled computation of transport coefficients for a (3+1)-dimensional relativistic plasma within a holographic model, specifically both Hall viscosities are computed.

The holographic setup consists of a five-dimensional asymptotically AdS charged magnetic blackbrane geometry [58] within Einstein-Maxwell-Chern-Simons theory, i.e. Einstein gravity with a negative cosmological constant coupled to gauge fields through a Maxwell and a Chern–Simons term, the latter encoding the quantum anomaly of the dual field theory. The boundary theory describes a strongly coupled, charged relativistic fluid at finite temperature and chemical potential, subject to a constant external magnetic field. The magnetic field explicitly breaks spatial rotational symmetry from $O ( 3 )$ down to $O ( 2 )$ , thereby allowing for anisotropic transport and parity-odd response coefficients, including Hall viscosities.

As argued above, in (3+1) spacetime dimensions, once rotational symmetry is reduced to $O ( 2 )$ , the viscous stress tensor admits two independent non-dissipative, time-reversal-odd viscosity coefficients, corresponding to shear deformations perpendicular and parallel to the symmetry-breaking axis. Within the relativistic setup, these are the two Hall viscosities, $\tilde { \eta } _ { \perp }$ and $\bar { \eta } _ { \parallel }$ , introduced on general hydrodynamic grounds in Sec. 2.1. The holographic framework thus provides a natural arena to assess the magnitude and scaling behavior of these coefficients at strong coupling, and to contrast them with the kinetic-theory estimates discussed earlier.

In Ref. [18], the two Hall viscosities were computed for a strongly coupled ${ \mathcal N } = 4$ Super-Yang-Mills theory at a large number of colors, subject to a strong external magnetic field, at finite temperature and chemical potential. For small values of dimensionless magnetic field ${ \tilde { B } } : = B / T ^ { 2 }$ , the following behavior was found for $\bar { \eta } _ { \parallel }$

$$
\tilde {\eta} _ {\parallel} \propto \tilde {B} ^ {3} T ^ {3}, \tag {26}
$$

where $T$ is the temperature. Firstly, this differs from the corresponding behavior in kinetic theory (10). If we expand $\tilde { \eta } _ { \parallel }$ of (10) near $\varpi \to 0$ , we obtain $\tilde { \eta } _ { \parallel } = \eta _ { 0 } \left( \varpi - \varpi ^ { 3 } / 4 + \mathcal { O } ( \varpi ^ { 5 } ) \right)$ . So, at a small magnetic field, the leading behavior is $\tilde { \eta } _ { \parallel } \propto \tilde { B } T ^ { 3 }$ in kinetic theory, whereas in holography, it is $\tilde { \eta } _ { \parallel } \propto \tilde { B } ^ { 3 } T ^ { 3 }$ .

The results from kinetic theory and holography also differ at large magnetic fields. In particular, [18] obtained following expression for $\bar { \eta } _ { \parallel }$ in the presence of large magnetic fields

$$
\tilde {\eta} _ {| |} \approx 0. 3 0 5 \tilde {\mu} \bar {B} T ^ {3}, \tag {27}
$$

where ${ \tilde { \mu } } : = \mu / T$ is the dimensionless chemical potential. The kinetic theory expression for $\bar { \eta } _ { \parallel }$ (10), when expanded around $\varpi \ \to \ \infty$ gives $\tilde { \eta } _ { \parallel } ~ = ~ \eta _ { 0 } \left( 4 / \varpi - 1 6 / \varpi ^ { 3 } + \mathcal { O } ( \varpi ^ { - 5 } ) \right)$ . Thus, kinetic theory predicts $\tilde { \eta } _ { \parallel } \propto T ^ { 3 } / \tilde { B }$ at large magnetic fields in contrast to the behavior $\tilde { \eta } _ { \parallel } \propto \tilde { B } T ^ { 3 }$ obtained in ∥ holography.

We take $T \approx 3 0 0$ MeV and $B \approx 1 0 ^ { 1 9 } { \mathrm { ~ G a u s s } } = 0 . 1 9 5 { \mathrm { ~ G e V } } ^ { 2 }$ $B \approx 1 0 ^ { 1 9 }$ , i.e. $B \approx 2 . 1 7 \ T ^ { 2 }$ . From Fig. 3 of Ref. [59], for initial energy density of $\rho _ { 0 } = 1 f m ^ { - 3 }$ we can infer $\tilde { \mu } = \mu / T \approx 1$ assuming $\mu$ to be the

baryon chemical potential. Substituting these in Eq. 27, we get

$$
\frac {\tilde {\eta} _ {\parallel}}{T ^ {3}} \approx 0. 3 0 5 \tilde {\mu} \tilde {B} = 0. 3 0 5 \times \frac {\mu}{T} \times \frac {B}{T ^ {2}} \approx 0. 3 0 5 \times 1 \times \frac {2 . 1 7 T ^ {2}}{T ^ {2}} = 0. 6 6. \tag {28}
$$

Recalling that the zero magnetic field viscosity is $\eta _ { 0 } \approx 1 . 9 5 T ^ { 3 }$ , we finally obtain $\tilde { \eta } _ { \parallel } \approx 0 . 3 4 \eta _ { 0 }$ . This value is of the same order of magnitude as the corresponding kinetic-theory estimate for $\bar { \eta } _ { \parallel }$ , Eq. (24), suggesting qualitative consistency between weak- and strong-coupling approaches despite their differing functional dependence on the magnetic field.

For the transverse Hall viscosity, the holographic computation in [18] found that $\tilde { \eta } _ { \perp } = 0$ in this holographic model. This vanishing of $\tilde { \eta } _ { \perp }$ is not enforced by symmetry but is instead a feature of the specific Einstein-Maxwell-Chern-Simons model considered in Ref. [18]. This vanishing can be traced back to the fact that [18] does not consider Chern-Simons terms coupling curvature to gauge fields in the gravitational action, which would lead to a gauge-gravitational anomaly in the dual field theory [17, 20]. This gauge-gravitational anomaly is included in the holographic model of [17] and leads to a non-vanishing $\tilde { \eta } _ { \perp }$ . More specifically, for the transverse Hall viscosity not to vanish, the retarded correlator $\langle T ^ { x z } ( T ^ { x x } - T ^ { z z } ) \rangle$ needs to be non-zero, as seen from the Kubo formula (1).2 Non-vanishing of that correlator implies that the dual gravitational action couples the corresponding metric components to each other, i.e., the metric fluctuation is achieved by the terms coupling curvature to the gauge field $h _ { x z }$ $\left( h _ { x x } - h _ { z z } \right)$ . Thisemann $\epsilon ^ { \mu \nu \rho \sigma \gamma } A _ { \mu } R _ { \delta \nu \rho } ^ { \beta } R _ { \beta \sigma \gamma } ^ { \delta }$ tensor $R _ { \delta \nu \rho } ^ { \beta }$ and the five-dimensional gauge field $A _ { \mu }$ . As mentioned above, such terms are dual to the gauge-gravitational anomaly. For the holographic model [17], an analytic relation $\eta _ { \| } / \eta _ { \perp } = 2 \tilde { \eta } _ { \| } / \tilde { \eta } _ { \perp }$ holds between shear viscosities and Hall viscosities. Combining this relation with our holographic estimate $\tilde { \eta } _ { \parallel } \approx 0 . 3 4 \eta _ { 0 }$ yields $\tilde { \eta } _ { \perp } = 2 \tilde { \eta } _ { \parallel } \eta _ { \perp } / \eta _ { \parallel } \approx 0 . 6 8 \eta _ { 0 }$ , when using that approximately $\eta _ { \perp } / s \approx \eta _ { \parallel } / s$ at $\tilde { B } \approx 2 . 1 7$ and $\tilde { \mu } \approx 1$ , see figures 9 and 10 in [18].

In summary, taken together, the holographic models [17] and [18] imply that the axial $U ( 1 ) ^ { 3 }$ anomaly leads to a non-vanishing longitudinal Hall viscosity while the mixed gauge-gravitational anomaly leads to a non-vanishing of the transverse Hall viscosity. Both Hall viscosities at realistic QGP parameters are of the same order of magnitude as the standard shear viscosity $\eta _ { 0 }$ .

# 3 Observables

Since Hall viscosity is non-dissipative, it does not contribute to entropy production. Its effects, therefore, manifest not as damping but as systematic rotations and couplings between different shear components of the flow. We interpret the Kubo formulas, (67) and (68) for the two Hall viscosities $\ddot { \eta } _ { \perp }$ and $\bar { \eta } _ { \parallel }$ to understand how they influence the expanding (and rotating) QGP fireball. Let us begin with $\tilde { \eta } _ { \perp }$ . For this, consider equations (9a),(9b), and (9c). We observe that in the presence of non-zero $\ddot { \eta } _ { \perp }$ , shear in the reaction plane ( $x z$ -plane), $V _ { x z }$ , will source a pressure anisotropy $\left( P _ { x } - P _ { z } \right)$ in the reaction plane and vice versa. Since the axis of rotation of the fireball is the $y$ -axis, the rotation of the fireball induces shear in the $x z$ -plane. Therefore, the effect of $\tilde { \eta } _ { \perp }$ is to induce or enhance in-plane pressure anisotropy, $( P _ { x } - P _ { z } )$ . Let us understand why the rotation along the $y$ -axis induces shear in the $x z$ -plane. Note that the angular velocity can be expressed in terms of the velocity as $\omega = v / r$ , where $r$ is the distance from the center of the fireball. Assuming that the entire QGP fireball rotates with a constant angular velocity $\omega$ , the fluid layers farther from the center of the fireball move faster, i.e., have larger $v$ , than the layers nearer the center of the fireball. This is equivalent to having shear in the $x z$ -plane: the fluid elements moving along the $x$ -axis move at different velocities at different $z$ -values. Therefore, we observe that indeed the rotation of the fireball induces shear in the reaction plane.

Next, to understand the effect of $\tilde { \eta } _ { \parallel }$ , we examine equations (9d) and (9e). They state that shear in the $z y$ -plane induces shear in the $x y$ -plane, and vice versa. As we have understood that a rotation about an axis induces shear in the plane perpendicular to the axis of rotation, we can interpret the effect of $\tilde { \eta } _ { \parallel }$ as follows: rotations about the two axes in the reaction plane will source each other. In

图片摘要：该图主要展示 3: Illustration of the effect of : Rotation around the axis 。
![](images/63d367cc2f7fbb12f4752f1fc385b3fe086341f89850950ae048ba81c78485e7.jpg)

图片摘要：该图主要展示 3: Illustration of the effect of : Rotation around the axis 。
![](images/00c19a871f34cfe6e4bc9deb27e1b6dfcaf0c6881144fc434c2e2afec0b5aa4c.jpg)  
Figure 3: Illustration of the effect of $\tilde { \eta } _ { \parallel }$ : Rotation around the $z$ -axis induces a rotation around the $x$ -axis. Left: The shear flow in the $x y$ -plane generated by rotation around the $z$ -axis is schematically displayed by blue arrows. Longitudinal Hall viscosity induces a stress response in the $z y$ -plane, $T ^ { z y }$ indicated by the green arrows. Right: The stress response (shear flow), $T ^ { z y }$ , is displayed in the $z y$ -plane by green arrows, and the big arrow indicates the induced rotation around the $x$ -axis resulting from that shear flow.

other words, a rotation about the $x$ -axis will induce a rotation about the $z$ -axis and vice versa, c.f. the illustration in Fig. 3.

# 3.1 Quantitative estimates of Hall viscosity effects on the QGP

We aim to provide quantitative estimates for the terms in the constitutive relations (9) that involve Hall viscosities, thereby assessing their impact on the QGP stress-energy tensor. These terms are evaluated at the proper time $\tau _ { 0 } = 1 \mathrm { f m } / c$ , which corresponds to the typical initialization time for hydrodynamic simulations of the QGP. We will refer to $\tau _ { 0 }$ as the hydrodynamic initialization time. While the electromagnetic field produced by the spectator charges reaches its maximum strength at very early times, it subsequently decays due to both geometric dilution and the finite electrical conductivity of the medium. Our estimates correspond to early times relevant for the onset of hydrodynamic evolution $\tau \sim \tau _ { 0 }$ ), where the magnetic field, although already decaying from its initial peak, can still be sizable. In particular, several analyses that include the electromagnetic response of a conducting QGP indicate that the magnetic field can remain non-negligible up to times of order $\tau _ { 0 }$ , and in some scenarios even longer, depending on the assumed conductivity and medium evolution [7, 60, 61]. Anisotropic conductivities in the plasma subject to a strong magnetic field were recently discussed in [62–64].

Since we assumed that Hall viscosity is generated on the timescale $\tau _ { 2 } \approx 0 . 4 \mathrm { f m } / c$ given by holography [40, 41], its contribution to the viscous stress tensor does not require a long-lived magnetic field. Instead, we can assume that Hall viscous stresses are generated whenever sizable shear gradients coexist with a non-zero magnetic field, even if the latter is transient on a timescale longer than $\tau _ { 2 }$ . Consequently, the estimates presented here should be interpreted as capturing the Hall viscous stress corrections imprinted on the system at hydrodynamic initialization time $\tau _ { 0 } > \tau _ { 2 }$ . These early-time

corrections can subsequently influence the evolution of flow observables, even if the magnetic field decays rapidly at later times.

All terms on the RHS in the constitutive relations (9) are expressed in terms of viscosities and accompanying stresses $V _ { i j }$ . Here, $V _ { i j } : = \dot { o } _ { j } V _ { i } + \dot { o } _ { i } V _ { j }$ , where $V _ { i } = \langle v _ { i } \rangle$ is the hydrodynamic flow velocity. We have already performed quantitative estimates of various viscosities that appear in the constitutive relations (9) in the previous section. We now compute the values of $V _ { i j }$ . This can be readily done by adapting the ansatz of Ref. [65] for the flow-velocity $u ^ { \mu }$ at the hydrodynamic initialization time $\tau _ { 0 }$ given by

$$
u ^ {\mu} = \left(\cosh y _ {L} \cosh y _ {T}, \sinh y _ {T} \cos \phi , \sinh y _ {T} \sin \phi , \sinh y _ {L} \cosh y _ {T}\right), \tag {29}
$$

where $y _ { L } ( x , y )$ is the longitudinal momentum rapidity w.r.t. the beam (in polar coordinates

$$
\sinh y _ {L} = \sinh y _ {T} \sin \theta
$$

where $\theta$ is the longitudinal angle ) and $y _ { T } ( x , y , z )$ is the transverse momentum rapidity and $\phi =$ arctan $( y / x )$ . As given in Ref. [66],

$$
y _ {L} (x, y) = f y _ {C M} (x, y), \quad 0 \leq f \leq 1,
$$

$$
y _ {C M} (x, y) = \operatorname {a r c t a n h} \left[ \frac {T _ {A} - T _ {B}}{T _ {A} + T _ {B}} \right] \tanh (y _ {\mathrm {b e a m}}),
$$

$$
y _ {b e a m} = \operatorname {a r c c o s h} \left(\sqrt {s _ {N N}} / \left(2 m _ {N}\right)\right), \tag {30}
$$

where $y _ { C M } ( x , y )$ is the center-of-mass rapidity at the location $( x , y )$ in the transverse plane. $f \in [ 0 , 1 ]$ is a parameter that controls the fraction of longitudinal momentum attributed to the flow velocity. $T _ { A } ( x , y )$ , $T _ { B } ( x , y )$ are the participant thickness functions in the transverse plane, $m _ { N }$ is the mass of the nucleon, $\sqrt { s _ { N N } }$ is nucleon–nucleon center-of-mass energy, and $y _ { \mathrm { b e a m } }$ is the beam rapidity.

If the transverse flow is only associated with thermalization, we can set $y _ { T } = 0$ at hydrodynamic initialization time $\tau _ { 0 }$ . However, initial transverse flow has been advocated to solve the so-called HBT puzzle [67]. In order to obtain analytic expressions for $y _ { T }$ , we use the “universal flow” formula of Ref. [68], which is based on the free-streaming limit. Accordingly the expression for $y _ { T }$ is [68],

$$
\tanh  y _ {T} = - \frac {T ^ {t x}}{T ^ {t t}}. \tag {31}
$$

Note that $u ^ { \mu }$ defined in (29) is normalized $u ^ { \mu } u _ { \mu } = 1$ in Minkowski spacetime $g _ { \mu \nu } = ( 1 , - 1 , - 1 , - 1 )$ . Recall

$$
u ^ {\mu} = \gamma (c, v _ {x}, v _ {y}, v _ {z}), \quad \gamma = \frac {1}{\sqrt {1 - \frac {v _ {x} ^ {2} + v _ {y} ^ {2} + v _ {z} ^ {2}}{c ^ {2}}}},
$$

$$
u ^ {t} = \gamma c, \quad u ^ {i} = \gamma v _ {i}, (i = x, y, z),
$$

$$
v _ {i} = c \frac {u ^ {i}}{u ^ {t}}. \tag {32}
$$

Comparing this with $u ^ { \mu }$ ansatz Eq. (29), we get

$$
v _ {x} = c \tanh  y _ {T} \frac {\cos \phi}{\cosh y _ {L}}, \tag {33a}
$$

$$
v _ {y} = c \tanh  y _ {T} \frac {\sin \phi}{\cosh y _ {L}}, \tag {33b}
$$

$$
v _ {z} = c \tanh  y _ {L}. \tag {33c}
$$

To get tanh $y _ { T }$ , we need expressions for $T ^ { t t }$ and $T ^ { t x }$ . $T ^ { t t }$ can be expressed in terms of $T ^ { \tau \tau \tau }$ , $T ^ { \tau \eta }$ , and $T ^ { \prime \prime \prime \prime }$ using the Milne-to-Minkowski coordinate transformation as

$$
\begin{array}{l} T ^ {t t} = (\cosh \eta) ^ {2} T ^ {\tau \tau} + 2 \tau_ {0} \cosh \eta \sinh \eta T ^ {\tau \eta} + (\tau_ {0} \sinh \eta) ^ {2} T ^ {\eta \eta}, \\ = \left(1 + \mathcal {O} (\eta) ^ {2}\right) T ^ {\tau \tau} + 2 \tau_ {0} \left(\eta + \mathcal {O} (\eta) ^ {3}\right) T ^ {\tau \eta} + \tau_ {0} ^ {2} \mathcal {O} (\eta) ^ {2} T ^ {\eta \eta}, \quad \eta \ll 1, \\ = T ^ {\tau \tau} + 2 \tau_ {0} \eta T ^ {\tau \eta} + \mathcal {O} (\eta) ^ {2}, \quad \eta \ll 1. \tag {34} \\ \end{array}
$$

In the limit $\eta \ll 1$ , we neglected $\mathcal { O } ( \eta ) ^ { 2 }$ terms and kept terms up to linear order in $\eta$ . At the hydrodynamic initialization time $\tau _ { 0 }$ , $\eta \ll 1$ is a valid assumption. Expressions for $T ^ { \tau \tau \tau }$ and $T ^ { \tau \eta }$ at hydrodynamic initialization time $\tau _ { 0 }$ as given in Ref. [66] are

$$
T ^ {\tau \tau} (x, y, \eta) = e (x, y, \eta) \cosh (y _ {L}), \tag {35}
$$

$$
T ^ {\tau \eta} (x, y, \eta) = \frac {1}{\tau_ {0}} e (x, y, \eta) \sinh (y _ {L}). \tag {36}
$$

The expression for energy density $e ( x , y , \eta )$ is given by [66] ( $\Theta ( \ldots )$ is the Heavyside function)

$$
e (x, y, \eta ; y _ {C M} - y _ {L}) = \mathcal {N} _ {e} (x, y) \mathrm {e x p} \bigg [ - \frac {\left(| \eta - (y _ {C M} - y _ {L}) | - \eta_ {0}\right) ^ {2}}{2 \sigma_ {\eta} ^ {2}} \Theta (| \eta - (y _ {C M} - y _ {L}) | - \eta_ {0}) \bigg ],
$$

$$
\mathcal {N} _ {e} (x, y) = \frac {M (x , z)}{2 \sinh (\eta_ {0}) + \sqrt {\pi / 2} \sigma_ {\eta} e ^ {\sigma_ {\eta} ^ {2} / 2} C _ {\eta}},
$$

$$
C _ {\eta} = e ^ {\eta_ {0}} \operatorname {e r f c} \left(- \sqrt {\frac {1}{2}} \sigma_ {\eta}\right) + e ^ {- \eta_ {0}} \operatorname {e r f c} \left(\sqrt {\frac {1}{2}} \sigma_ {\eta}\right), \tag {37}
$$

where $\operatorname { e r f c } ( x )$ is the error function. The parameter $\eta _ { 0 }$ determines the width of the plateau and $\sigma _ { \eta }$ controls how fast the energy density falls off at the edge of the plateau. Ref. [66] and Ref. [69] set $\eta _ { 0 } = \mathrm { m i n } ( \eta _ { 0 } , y _ { \mathrm { b e a m } } - ( y _ { C M } - y _ { L } ) )$ .

The invariant mass $M ( x , y )$ can be expressed in terms of the participant thickness functions as follows,

$$
M (x, y) = m _ {N} \sqrt {T _ {A} ^ {2} + T _ {B} ^ {2} + 2 T _ {A} T _ {B} \cosh (2 y _ {\mathrm {b e a m}})}. \tag {38}
$$

Since we are only interested up to linear order in small $\eta$ , we fix a small bound $| \eta | \le \varepsilon$ with $\varepsilon \ll \eta _ { 0 }$ . Note that Table I in Ref. [69] gives $\eta _ { 0 } = 2 . 5$ , so this assumption is reasonable. If the transverse region satisfies

$$
\left| y _ {C M} (x, y) - y _ {L} (x, y) \right| = \left| (1 - f) y _ {C M} (x, y) \right| \leq \eta_ {0} - \varepsilon , \quad \forall x, y, \tag {39}
$$

then, by triangle inequality, one obtains

$$
\left| \eta - \left(y _ {C M} (x, y) - y _ {L} (x, y)\right) \right| = \left| \eta - (1 - f) y _ {C M} (x, y) \right| \leq \left| \eta \right| + \left| (1 - f) y _ {C M} (x, y) \right| \leq \varepsilon + \eta_ {0} - \varepsilon = \eta_ {0}. \tag {40}
$$

This implies

$$
\Theta \left(\left| \eta - \left(y _ {C M} (x, y) - y _ {L} (x, y)\right) \right| - \eta_ {0}\right) = 0. \tag {41}
$$

Therefore, we can drop the exponential term in the energy density expression and get

$$
e (x, y) = \mathcal {N} _ {e} (x, y). \tag {42}
$$

To obtain $T ^ { t x }$ , we use the universal flow formula of Ref. [68]

$$
\frac {T ^ {t x}}{T ^ {t t}} \approx \frac {t}{2} \frac {\partial_ {x} T ^ {t t}}{T ^ {t t}} = \frac {\tau_ {0} \cosh \eta}{2} \frac {\partial_ {x} T ^ {t t}}{T ^ {t t}}, \tag {43}
$$

where in the second equality we used $t = \tau _ { 0 } \cosh \eta$ ; $t$ is Minkowski time and $\tau _ { 0 }$ is the hydrodynamic initialization proper time.

The gradients of velocities $v _ { x }$ , $v _ { y }$ , and $v _ { z }$ are

$$
\partial_ {x} v _ {x} = c \frac {\cosh y _ {L} \cos \phi \partial_ {x} \tanh  y _ {T} - \cosh y _ {L} \tanh  y _ {T} \sin \phi \partial_ {x} \phi - \tanh  y _ {T} \cos \phi \sinh y _ {L} \partial_ {x} y _ {L}}{\cosh^ {2} y _ {L}}, \tag {44a}
$$

$$
\partial_ {y} v _ {x} = c \frac {\cosh y _ {L} \cos \phi \partial_ {y} \tanh  y _ {T} - \cosh y _ {L} \tanh  y _ {T} \sin \phi \partial_ {y} \phi - \tanh  y _ {T} \cos \phi \sinh y _ {L} \partial_ {y} y _ {L}}{\cosh^ {2} y _ {L}}, \tag {44b}
$$

$$
\partial_ {z} v _ {x} = c \frac {\cosh y _ {L} \cos \phi \partial_ {z} \tanh  y _ {T}}{\cosh^ {2} y _ {L}}, \tag {44c}
$$

$$
\partial_ {x} v _ {y} = c \frac {\cosh y _ {L} \sin \phi \partial_ {x} \tanh  y _ {T} + \cosh y _ {L} \tanh  y _ {T} \cos \phi \partial_ {x} \phi - \tanh  y _ {T} \sin \phi \sinh y _ {L} \partial_ {x} y _ {L}}{\cosh^ {2} y _ {L}}, \tag {44d}
$$

$$
\partial_ {y} v _ {y} = c \frac {\cosh y _ {L} \sin \phi \partial_ {y} \tanh  y _ {T} + \cosh y _ {L} \tanh  y _ {T} \cos \phi \partial_ {y} \phi - \tanh  y _ {T} \sin \phi \sinh y _ {L} \partial_ {y} y _ {L}}{\cosh^ {2} y _ {L}}, \tag {44e}
$$

$$
\partial_ {z} v _ {y} = c \frac {\cosh y _ {L} \sin \phi \partial_ {z} \tanh  y _ {T}}{\cosh^ {2} y _ {L}}, \tag {44f}
$$

$$
\partial_ {x} v _ {z} = c \operatorname {s e c h} ^ {2} y _ {L} \partial_ {x} y _ {L}, \tag {44g}
$$

$$
\partial_ {y} v _ {z} = c \operatorname {s e c h} ^ {2} y _ {L} \partial_ {y} y _ {L}, \tag {44h}
$$

$$
\partial_ {z} v _ {z} = 0. \tag {44i}
$$

We need gradients of $\phi$ , $y _ { L }$ , and tanh $_ { y T }$ to evaluate the velocity gradients above. The expressions for these gradients can be found in the Appendix C.

We need to choose some differentiable functional form of participant thickness functions $T _ { A } ( x , y )$ and $T _ { B } ( x , y )$ . The participant thickness functions are defined by

$$
T _ {A (B)} (x, y) = \int_ {- \infty} ^ {\infty} d z \rho \left(\sqrt {x ^ {2} + y ^ {2} + z ^ {2}}\right), \tag {45}
$$

where $\rho ( \mathfrak { r } )$ , ( $\mathfrak { r } = \sqrt { x ^ { 2 } + y ^ { 2 } + z ^ { 2 } } )$ is the nuclear density function. The most common choice for $\rho ( \mathfrak { r } )$ is the Wood-Saxon density given by

$$
\rho (\mathfrak {r}) = \frac {\rho_ {0}}{1 - \exp \left(\frac {\mathfrak {r} - R _ {0}}{a}\right)}. \tag {46}
$$

However the integral Eq. (45) cannot be computed analytically for Wood-Saxon density Eq. (46).

Since we are only interested in a back-of-the-envelope estimate, we choose the simplest ansatz for the nuclear density function - that of a “hard sphere” nucleus: uniform nuclear density with a sharp edge

$$
\rho (\mathfrak {r}) = \rho_ {0} \Theta (R - \mathfrak {r}), \tag {47}
$$

where $R$ is the nuclear radius and $\Theta$ is the Heavyside theta function. We choose values of parameters $\rho _ { 0 }$ and $R$ in the hard sphere nuclear density function $\rho ( \mathfrak { r } )$ of Eq. (47) as follows. For a given nucleus with mass number $A$ ,

$$
A = \int d ^ {3} \mathfrak {r} \rho (\mathfrak {r}) = \frac {4}{3} \pi R ^ {3} \rho_ {0}. \tag {48}
$$

We fix $\rho _ { 0 }$ to be the nuclear saturation density and solve for $R$ . The nuclear saturation density is 0.16 $\mathrm { f m } ^ { - 3 }$ [70–73]. We consider Au nuclei which have $A = 1 9 7$ . This gives $R = 6 . 6 5 f m$ .

By integrating $\rho ( \mathfrak { r } )$ over $z$ , we get

$$
T _ {A (B)} (x, y) = \left\{ \begin{array}{l l} 2 \rho_ {0} \sqrt {R ^ {2} - \left(\mathfrak {r} _ {\perp} ^ {A (B)}\right) ^ {2}}, & \mathfrak {r} _ {\perp} ^ {A (B)} \leq R \\ 0, & \mathfrak {r} _ {\perp} ^ {A (B)} > R \end{array} , \right. \tag {49}
$$

where

$$
\mathfrak {r} _ {\perp} ^ {A} (x, y; b) = \sqrt {\left(x - \frac {b}{2}\right) ^ {2} + y ^ {2}}, \tag {50}
$$

$$
\mathfrak {r} _ {\perp} ^ {B} (x, y; b) = \sqrt {\left(x + \frac {b}{2}\right) ^ {2} + y ^ {2}}, \tag {51}
$$

with the impact parameter is $b$ , and we choose centers of nucleus A and nucleus B at transverse positions $\left( x , y \right) = \left( { \textstyle { \frac { b } { 2 } } } , 0 \right)$ and $( x , y ) = ( - \textstyle { \frac { b } { 2 } } , 0 )$ , respectively. The values of velocity gradients of Eq. (44) are provided in Table 1. The values of various terms appearing in constitutive relations Eq. (9) are provided in Tables 2 and 3. From Tables 2 and 3, we observe that the terms with Hall viscosities are comparable to the terms with anisotropic shear viscosities.

# 3.2 Observables and their quantitative estimates

Hydrodynamics is a deterministic theory. Once initial conditions are known, the dynamics, given by conservation laws

$$
\partial_ {\mu} T ^ {\mu \nu} = \partial_ {\mu} J ^ {\nu} = 0 \tag {52}
$$

<table><tr><td>(x,y,z)</td><td>∂x vx</td><td>∂y vx</td><td>∂z vx</td><td>∂x vy</td><td>∂y vy</td><td>∂z vy</td><td>∂x uz</td><td>∂y uz</td><td>∂z uz</td></tr><tr><td>(0.001,0,0)</td><td>0.05569</td><td>0</td><td>-0.02815</td><td>0</td><td>0.05569</td><td>0</td><td>0.02815</td><td>0</td><td>0</td></tr><tr><td>(0.5,0.5,0.1)</td><td>0.02759</td><td>-0.017653</td><td>-0.01953</td><td>0.06578</td><td>0.020543</td><td>-0.019537</td><td>0.03048</td><td>0.0006358</td><td>0</td></tr><tr><td>(1,1,0.1)</td><td>0.05902</td><td>-0.01613</td><td>-0.02292</td><td>0.11093</td><td>0.035781</td><td>-0.022925</td><td>0.04023</td><td>0.00335</td><td>0</td></tr></table>

Table 1: Note that $\eta = \arcsin ( z / \tau _ { 0 } )$ . For $z = 0 . 1 f m$ , we get $\eta = 0 . 0 9 9 8$ for $\tau _ { 0 } = 1 f m / c$ . Since our expressions for velocity gradients are valid only up to linear order in $\eta$ around $\eta = 0$ , we do estimates for $z \le 0 . 1 f m$ . The values of parameters $f$ , $\eta _ { 0 }$ , $\sigma _ { \eta }$ , $\tau _ { 0 }$ are taken from table I of Ref. [69], namely $f = 0 . 1 5$ , $\eta _ { 0 } ~ = ~ 2 . 5$ , $\sigma _ { \eta } ~ = ~ 0 . 5$ , $\tau _ { 0 } = 1 f m / c$ . $\sqrt { s _ { N N } } = 2 0 0$ GeV, $m _ { N } = 0 . 9 4 ~ \mathrm { G e V } / c ^ { 2 }$ . $\rho _ { 0 }$ is taken as nuclear saturation density, $0 . 1 6 f m ^ { - 3 }$ and $A = 1 9 7$ (Au mass number). From $\rho _ { 0 }$ and $A$ , the nuclear radius $R$ is determined by using $\begin{array} { r } { A = \rho _ { 0 } \frac { 4 } { 3 } \pi R ^ { 3 } } \end{array}$ to be $R = 6 . 6 5 f m$ . The value of the impact parameter, $b$ , is taken as $b = 9 f m$ $4 0 – 5 0 \ \%$ centrality class ). Note that in the table, the positions $( x , y , z )$ are in units of $f m$ and velocity gradients are in units of $f m ^ { - 1 }$ . We have used natural units, i.e., $\hbar = c = k _ { B } = 1$ .   

<table><tr><td>(x,y,z)</td><td>η0/2(Vxx+Vzz)</td><td>η⊥/2(Vxx-Vzz)</td><td>η⊥Vxz</td></tr><tr><td>(0.001,0,0)</td><td>0.000577</td><td>0.000208</td><td>0</td></tr><tr><td>(0.5,0.5,0.1)</td><td>0.000286</td><td>0.000103</td><td>0.0000545</td></tr><tr><td>(1,1,0.1)</td><td>0.000612</td><td>0.000220</td><td>0.0000862</td></tr></table>

Table 2: In this table and in Table 3, we estimate values of various terms appearing in constitutive relations, Eq. (9), at various spacetime locations $( x , y , z )$ . We have used the velocity gradients of Table 1. Note that the values of velocity gradients in Table 1 are in units of $f m ^ { - 1 }$ (in natural units $\hbar = c = 1$ ). We used the relation $1 f m ^ { - 1 } = 0 . 1 9 7 3 \ \mathrm { G e V }$ to convert them in units of GeV. Furthermore we used the zero-magnetic field viscosity $\eta _ { 0 }$ values from our earlier estimate, namely, $\eta _ { 0 } = 0 . 0 5 2 6 \ G e V ^ { 3 }$ . Values of the other four viscosities were also used from our earlier estimate of Eq. (24), namely $\eta _ { \perp } = 0 . 3 6 \eta _ { 0 }$ , $\eta _ { \parallel } = 0 . 6 9 \eta _ { 0 }$ , $\tilde { \eta } _ { \perp } = 0 . 4 8 \eta _ { 0 }$ , $\tilde { \eta } _ { \parallel } = 0 . 9 3 \eta _ { 0 }$ . All values in this table are in the units of $G e V ^ { 4 }$ . Estimates of three of the terms from constitutive relations, Eq. (9), are in this table, whereas the estimates of the remaining six terms from constitutive relations, Eq. (9), are in Table 3.   
Table 3: Together in this table and in Table 2, we estimate the values of the various terms appearing in constitutive relations, Eq. (9), at various spacetime locations $( x , y , z )$ . See caption of Table 2.   

<table><tr><td>(x,y,z)</td><td>η⊥Vxz</td><td>η⊥/2(Vxx - Vzz)</td><td>η∥Vxy</td><td>η∥/2Vzy</td><td>η∥Vzy</td><td>η∥/2Vxy</td></tr><tr><td>(0.001,0,0)</td><td>0</td><td>0.000277</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>(0.5,0.5,0.1)</td><td>0.0000409</td><td>0.000137</td><td>0.000344</td><td>-0.0000912</td><td>-0.000135</td><td>0.000232</td></tr><tr><td>(1,1,0.1)</td><td>0.0000646</td><td>0.000294</td><td>0.000678</td><td>-0.0000944</td><td>-0.000140</td><td>0.000457</td></tr></table>

as well as the EoS and transport coefficients (determining the form of $T _ { \mu \nu } , J _ { \mu } )$ uniquely determines subsequent evolution up to initial state fluctuations (described by geometric models or approaches like the Color Glass) and final state fluctuations (assumed to be thermal as well as given by resonance decays).

In heavy-ion collisions (HIC) it is convenient to parametrize the details of the evolution in terms of a harmonic analysis w.r.t. the azimuthal angle, which is given by the impact parameter. In other words, the anisotropy $\epsilon _ { u }$ of the collective flow3

$$
u _ {r, \theta} = u _ {0} (r) \left(1 + \sum_ {n} \epsilon_ {u n} \cos \left(n \left(\phi - \phi_ {u n}\right)\right)\right), \tag {53}
$$

which freezes out into particles, via a Cooper-Frye type ansatz, in terms of , temperature $T$ , and a $u _ { \mu }$

freeze-out hypersurface $\Sigma _ { \mu }$

$$
E \frac {d N}{d ^ {3} p} = \int d \Sigma_ {\mu} p ^ {\mu} \exp \left[ \frac {p _ {\mu} u ^ {\mu} (x)}{T (x)} \right]. \tag {54}
$$

Obvious observables to consider in this regard are the anisotropic flow coefficients $v _ { n }$ . At midrapidity these coefficients are defined by

$$
\frac {d N}{p _ {T} d p _ {T} d \phi} = 1 + \sum_ {n} 2 v _ {n} \left(p _ {T}\right) \cos \left(n \left(\phi - \phi_ {0 n}\right)\right), \quad v _ {n} \equiv \left\langle \cos \left(n \left(\phi - \phi_ {0 n}\right)\right) \right\rangle , \tag {55}
$$

and $v _ { n }$ can be measured with a variety of techniques, including numerical Fourier decomposition, cumulants of $\phi$ distributions and Lee-Young zeroes (see references in [74]).

In hydrodynamics, the $v _ { n }$ are uniquely determined by $\epsilon _ { x }$ , the initial position space anisotropy of energy density $e$ (given by azimuthal gradients),

$$
e (r, \theta , t = 0) = e _ {0} (r) \left(1 + \sum_ {n} \epsilon_ {x n} \cos \left(n \left(\phi - \phi_ {e n}\right)\right)\right), \tag {56}
$$

as well as intensive parameters such as pressure and viscosity (which in turn depend on energy density).

Of course hydrodynamic equations are highly non-linear, so mixings between different phases $\phi _ { 0 }$ , and flow and freeze-out Fourier coefficients $\epsilon _ { u n }$ , and correlations between $\epsilon _ { x n }$ and $v _ { n \neq m }$ are nonnegligible. However, unless one is in a turbulent regime, a good control over initial conditions and a stable enough hydrodynamic code should lead to deterministic $v _ { n }$ once initial geometry was precisely enough accounted for.

Additional dynamical fluctuations can be constrained by $v _ { 2 }$ fluctuation and correlations, in other words event-by-event [75–78]

$$
\langle (\delta v _ {n} \delta v _ {m}) \rangle \equiv \langle \cos [ n (\phi - \phi_ {0 n}) ] \cos [ m (\phi - \phi_ {0 m}) ] \rangle - \langle \cos [ n (\phi - \phi_ {0 n}) ] \rangle \langle \cos [ m (\phi - \phi_ {0 m}) ] \rangle . \tag {57}
$$

Considering the odd components, correlations between $\phi _ { n }$ and $\phi _ { m }$ can also be isolated. Events can even be binned by $\cos [ n ( \phi - \phi _ { 0 n } ) ]$ leading to “event engineering” [79] (geometry selection) techniques. So far no evidence of fluctuations due to dynamics have been found, see [80] and references therein.

From the previous sections, it is straightforward to see that Hall viscosity appears in this latter category. In particular, the longitudinal component of vorticity is directly connected to the welldeveloped program of the study of fluctuations of anisotropic flow/event eccentricity.4 For both longitudinal and transverse Hall viscosity, a distinctive signature is the correlation between

$$
\theta_ {Q} = \operatorname {A r g} [ Q ], \qquad Q = p _ {x} + i p _ {y}
$$

and the global geometry (impact parameter distribution).

While a quantitative estimate of the effects sketched in Figs. 1a and 1b would need a numerical hydrodynamic calculation, it is possible to give an order-of-magnitude estimate of the effect from available experimental data and parameters characterizing the collision. The previous section makes it clear that the effect we are looking for is a torque density, a torque divided by the relevant crosssectional area. Thus looking at Figs. 1a and 1b we get

$$
\frac {\mathcal {T} _ {\theta}}{\left(t _ {f} - t _ {0}\right) S _ {x z}} \sim \tilde {\eta} _ {\perp} \left(\Pi_ {x x} - \Pi_ {y y}\right), \quad \frac {\mathcal {T} _ {\phi}}{\left(t _ {f} - t _ {0}\right) S _ {y z}} \sim \tilde {\eta} _ {| |} \left(\Pi_ {z z} - \Pi_ {x x}\right), \tag {58}
$$

where $\tau$ is the torque, $S$ a cross-sectional area and $\theta , \phi$ are, respectively, the angle between $x - z , x - y$ . It is important to emphasize that the Hall viscous effects discussed here are cumulative over the lifetime of the fireball. While the instantaneous Hall viscous stresses are small, their integrated effect over several fm/c can lead to observable phase shifts (i.e. shifts of the angles $\theta$ and $\phi$ inferrred from data w.r.t. the event geometry definitions of Eq. (29)) The resulting observable angles will then simply be the torque multiplied by the lifetime of the fireball squared, i.e., the square of the difference between freezeout time $t _ { f }$ and thermalization time $t _ { 0 }$ .

$$
\Delta \theta \sim \frac {1}{2} \left(t _ {f} - t _ {0}\right) ^ {2} \mathcal {T} _ {\theta}, \quad \Delta \phi \sim \frac {1}{2} \left(t _ {f} - t _ {0}\right) ^ {2} \mathcal {T} _ {\phi}. \tag {59}
$$

For an order of magnitude estimate, we note that the measured anisotropic flow coefficients directly track the shear,

$$
v _ {2} \sim \frac {\Pi_ {x x} - \Pi_ {y y}}{\Pi_ {x x} + \Pi_ {y y}}, \quad \Delta y \frac {d v _ {1}}{d y} \sim \frac {\Pi_ {z z} - \Pi_ {x x}}{\Pi_ {z z} + \Pi_ {x x}}, \tag {60}
$$

while the sum of the shears can be related to the average transverse momentum $\langle p _ { T } \rangle$ together with the relevant volume of the fireball

$$
\Pi_ {x x} + \Pi_ {y y} \sim \frac {1}{t _ {0} \Delta y} \frac {d \left\langle p _ {T} \right\rangle}{d y}, \quad \Pi_ {x x} + \Pi_ {z z} \sim \frac {1}{t _ {0} \Delta y} \frac {d \left\langle p \right\rangle}{d y} \tag {61}
$$

where we assume that the longitudinal component dominates over any transverse gradient.

Finally, the transverse areas are related to the eccentricity $\epsilon$ and the nuclear radius $R$ via elementary geometry

$$
S _ {x y} \sim \epsilon R ^ {2}, \quad S _ {x z} \sim R t _ {0} \Delta y, \tag {62}
$$

Thus, the observable phase shifts are given as a function of $\begin{array} { r } { v _ { 1 } , v _ { 2 } , \epsilon , R , \frac { d \langle p _ { T } \rangle } { d y } \Delta y , t _ { 0 } , t _ { f } } \end{array}$ , d⟨pT ⟩ ∆y, t0, tf as

$$
\Delta \theta \sim \frac {\left(t _ {f} - t _ {0}\right)}{2 \Delta y t _ {0}} v _ {2} R t _ {0} \left(\Delta y \frac {d \langle p \rangle}{d y}\right) ^ {- 1} \tilde {\eta} _ {\perp}. \tag {63}
$$

$$
\Delta \phi \sim \frac {\left(t _ {f} - t _ {0}\right)}{2 \Delta y t _ {0}} \frac {d v _ {1}}{d y} \Delta y \in R ^ {2} \left(\frac {d \langle p _ {T} \rangle}{d y}\right) ^ {- 1} \tilde {\eta} _ {\parallel}. \tag {64}
$$

This is essentially a back-of-the-envelope dimensional analysis estimate, but it gives a physical indication of what Hall viscosity actually does, as also summarized in the figures: It causes an interplay between the transverse and longitudinal Fourier components and the longitudinal and transverse mean “phase” ( $\phi _ { 0 n }$ in Eq. (55)) .

For the numerical estimate, we took $\langle p _ { T } \rangle$ from [81] to be $\simeq 0 . 6$ GeV, $p = p _ { T } \sinh y$ , $t _ { 0 } = 1$ and $t _ { f } = 5$ fm, $R = 6$ fm [82], $\epsilon = 0 . 2 - 0 . 8$ [82], $\Delta v _ { 1 } / \Delta y = 0 . 5 - 1$ [83, 84] and $v _ { 2 } = 0 . 0 1 - 0 . 0 5$ [85]. the numerical values for $\Delta \theta , \Delta \phi$ would be

$$
\Delta \theta = \alpha_ {\perp} \sim G e V ^ {- 3} (0. 0 3 \tilde {\eta} _ {\perp}), \quad \Delta \phi = \alpha_ {| |} \sim G e V ^ {- 3} (9 \tilde {\eta} _ {| |}) \tag {65}
$$

where

$$
\alpha_ {i} = \frac {\tilde {\eta} _ {i}}{s}, \quad s \sim \frac {4}{N _ {\text {p a r t}} f m ^ {3}} \frac {d N}{d y} \sim s _ {0} s _ {c m} ^ {0. 1 5 5} \ln s _ {c m}. \tag {66}
$$

Entropy is estimated by assigning each particle 4 units of entropy [86], and by estimating the multiplicity per participant according to an empirical formula in terms of the center of mass energy $s _ { c m }$ [87].

$\Delta \theta$ and $\Delta \phi$ are in principle observable, as they appear as differences between the phase $\phi _ { n }$ in Eq. (56) and Eq. (53). Eq. (56) is related to the spectator recoil angle, which is observable with a zero degree calorimeter. Eq. (53) relates to $\theta _ { 0 }$ and $\phi _ { 0 }$ phase angles that maximize $\displaystyle \langle \cos ( 2 ( \phi - \phi _ { 0 } ) ) \rangle$ and $\left. \cos ( \theta - \theta _ { 0 } ) \right.$ once non-flow has been taken out. A systematic shift between them, related to $v _ { 1 , 2 }$ , and global event characteristics such as the nuclear radius and $\langle p _ { T } \rangle$ , would give an experimental indication of the presence of Hall viscosity. Experimentally, these effects can be accessed through event-plane correlations and directed-flow rapidity slopes, all of which are currently measured by experiments such as STAR and ALICE. Event-engineering techniques provide a particularly promising avenue for isolating Hall viscous signatures.

# 4 Conclusions and Outlook

In this work we have provided the first quantitative estimate of the Hall viscosity in the quarkgluon plasma (QGP), demonstrating that non-dissipative parity-odd transport can appear naturally once rotational symmetry is broken by the strong magnetic field in off-central heavy-ion collisions.

By extending the Alekseev mechanism from two-dimensional kinetic theory [15] to three spatial dimensions, we have shown that two independent Hall viscosities emerge: a transverse $( \tilde { \eta } _ { \perp } )$ and a longitudinal (η˜ ) component. These enter the viscous stress tensor through well-defined constitutive

relations, Eq. (9), and modify the hydrodynamic response of the plasma in distinct ways: As illustrated in Fig. 2, $\tilde { \eta } _ { \perp }$ couples in-reaction plane shear to pressure anisotropy in the reaction plane, while $\tilde { \eta } _ { \parallel }$ couples mixed in- and out-of-reaction plane shears with each other.

Order-of-magnitude estimates based on kinetic theory yield Hall viscosities of the same order as the zero field shear viscosity $\eta _ { 0 }$ , $\tilde { \eta } _ { \perp } \approx ( 0 . 4 - 0 . 5 ) \eta _ { 0 }$ and $\tilde { \eta } _ { \parallel } \approx ( 0 . 9 - 1 ) \eta _ { 0 }$ for magnetic fields $B \approx 1 0 ^ { 1 9 } G$ and $T \approx 3 0 0$ MeV at initialization time. The estimates based on holographic models [17, 18] predict $\tilde { \eta } _ { \parallel } \approx 0 . 3 4 \eta _ { 0 }$ and $\tilde { \eta } _ { \perp } \approx 0 . 6 8 \eta _ { 0 }$ , which is of the same order as the kinetic theory estimates. Our estimates based on kinetic theory and holography both yield similar values for the Hall viscosities, which are in turn comparable to the values of the zero field shear viscosity $\eta _ { 0 }$ . This quantitative agreement between weak- and strong-coupling estimates suggests that Hall viscosity is a robust, largely couplinginsensitive feature of QCD matter under broken time reversal and rotational symmetry.

An important feature of Hall viscosity is that its phenomenological impact is primarily controlled by the magnetic fields at early times in the collision, i.e., on the time scale when the anisotropic flow is generated. We quantified how the Hall viscous terms enter the stress tensor at hydrodynamic initialization time $\tau _ { 0 } \sim 1 f m / c$ using velocity gradients derived from analytic models of pre-equilibrium flow [65–69]. The Hall viscous corrections are comparable in magnitude to the anisotropic viscous stresses and can therefore influence early-time pressure anisotropies, potentially altering the build-up of elliptic ( $v _ { 2 }$ ) and directed flow ( $v _ { 1 }$ ).

Phenomenologically, Hall viscosity induces torque-like couplings between longitudinal and transverse flow harmonics (c.f. Figs. 1a and 1b), leading to rotations of the event-plane phases $( \Delta \theta , \Delta \phi )$ that could manifest as correlations between global polarization, directed-flow rapidity slopes, and the participant-plane angle [23, 28, 83, 84]. These signatures are experimentally accessible via modern event-engineering and polarization-flow correlators.

Several directions for future theoretical studies are: First of all, we would like to quantify the effect of strong vorticity on the Hall transport in the heavy-ion collision (HIC) which we expect to be of the same order-of-magnitude as the strong magnetic field effect. Another important future direction on the theoretical front is to compute magnetovortical transport coefficients in Veneziano-QCD (V-QCD) at finite temperature and baryon density, in this way testing more realistically the mechanisms for generating Hall viscosity at strong coupling. V-QCD provides a very realistic holographic model of QCD at finite temperature and baryon density. Since the magnetic field only couples to the quark sector, the naive semiclassical limit in AdS/CFT of large number of colors misses its effect. V-QCD, on the other hand, works in the Veneziano limit, which is a limit of large number of both flavors and colors while maintaining their ratio finite, and thus accounts for backreaction from the quark onto the gluon sector, thereby capturing magnetic-field effects.

Incorporating $\tilde { \eta } _ { \perp }$ and $\tilde { \eta } _ { \parallel }$ into relativistic magneto-hydrodynamic codes will allow a quantitative study of how Hall viscous terms modify freeze-out observables.5 The predicted phase-angle shifts $( \Delta \theta , \Delta \phi )$ could be compared to event-plane correlations and $\Lambda -$ hyperon global polarization data. The coupling of shear to spin polarization [95–97] suggests a direct relation between Hall viscosity and spin hydrodynamics that warrants investigation. Future global fits could include $\tilde { \eta } _ { \perp }$ and $\tilde { \eta } _ { \parallel }$ as additional transport parameters in Bayesian analyses [44,98–100]. Sensitivity studies using observables such as elliptic flow $v _ { 2 }$ , directed flow $v _ { 1 }$ , polarization correlations, or event-plane tilts would constrain the magnitude and sign of Hall viscosities in the QGP.

# Acknowledgements

We thank Dmitri Kharzeev for valuable comments and Aleksi Kurkela for discussions in the early stage of this project. R.M. acknowledges the support of the German Research Foundation (DFG) through the Collaborative Research Center ToCoTronics, Project-ID 258499086 — SFB 1170, as well as Germany’s Excellence Strategy through the Würzburg-Dresden Cluster of Excellence on Complexity and Topology in Quantum Matter - ctd.qmat (EXC 2147, Project-ID 390858490). He furthermore acknowledges hospitality from the Shanghai Institute for Mathematics and Interdisciplinary Sciences

(SIMIS) during the final stages of this work, and associated travel support under STCSM Grant 25HB2701900. G.T. thanks Bolsa de produtividade CNPQ 305731/2023-8 and FAPESP 2023/06278- 2, as well as participation in the tematico 2023/13749-1 for support. M.K. was supported, in part, by the U.S. Department of Energy grant DE-SC0012447. M.K. thanks the Galileo Galilei Institute for Theoretical Physics for the hospitality and the INFN for partial support during the completion of this work. S.M. thanks the Theoretical Physics III Group at the University of Würzburg for their hospitality and support during the early stages of this work.

# A Hall viscosities

In 3+1-dimensional fluids described by hydrodynamics the breaking of rotation invariance from $\mathcal { O } ( 3 )$ down to $\mathcal { O } ( 2 )$ is crucial. This can be achieved by introducing a large anisotropy in the plasma, for example a strong magnetic field or global rotation. This leads to different behavior within the plane perpendicular to the anisotropy (e.g. perpendicular to the axis of global rotation) and the planes including the anisotropy direction (e.g. including the axis of rotation).

In general, the QGP will be subject to at least three anisotropies: magnetic field generated by colliding ions, rotation due to non-zero impact parameter/off-central collision, and anisotropic energy densities as well as pressures due to Bjorken-like expansion of the plasma along the beam line, which we take to be the $z$ -direction. The magnetic field and global rotation axis are aligned with each other, let’s assume along the $y$ -direction. For Hall viscosity it does not matter what type of anisotropy breaks the rotation symmetry, any anisotropy will lead to two distinct Hall viscosities: $\tilde { \eta } _ { \lvert { \lvert { \ l } } \rvert }$ within the plane containing the anisotropy, and $\tilde { \eta } _ { \perp }$ perpendicular to that plane.

Also the shear viscosity will split into $\eta _ { \parallel }$ and $\eta _ { \perp }$ . In holographic systems, only $\eta _ { \perp }$ is required to satisfy $\eta / s = 1 / ( 4 \pi )$ , while $\eta _ { | | } / s$ generically decreases towards zero when the anisotropy is increased. The only known cases in which $\eta _ { | | } / s$ increases with increasing anisotropy are a holographic p-wave superfluid [101] and the charged $\mathcal { N } \ : = \ : 4$ Super-Yang-Mills plasma subject to a moderately strong external magnetic field [18]. Anisotropic shear viscosities along with other anisotropic transport coefficients or anisotropic dispersion relations have been computed holographically in [88–94].

Kubo relations in the case of only one anisotropy, computed for a magnetic field along the $z$ - direction, give the transverse Hall viscosity (this is like the one known from condensed matter physics in 2+1-dimensional materials [12–14, 102])

$$
\tilde {\eta} _ {\perp} = \lim  _ {\omega \rightarrow 0} \lim  _ {k \rightarrow 0} \frac {1}{\omega} \left\langle T _ {x z} \left(T _ {x x} - T _ {z z}\right)\right\rangle \tag {67}
$$

and the longitudinal Hall viscosity (which is not known or discussed in condensed matter literature )

$$
\tilde {\eta} _ {| |} = \lim  _ {\omega \rightarrow 0} \lim  _ {k \rightarrow 0} \frac {1}{\omega} \left\langle T _ {x y} T _ {z y} \right\rangle \tag {68}
$$

In addition to Hall viscosities, there are anisotropic shear viscosities in 3D, denoted by $\eta _ { \perp }$ and $\eta _ { \parallel }$ Their Kubo formulas are

$$
\eta_ {\perp} = \lim  _ {\omega \rightarrow 0} \lim  _ {k \rightarrow 0} \frac {1}{\omega} \left\langle T _ {x z} T _ {x z} \right\rangle , \tag {69}
$$

and

$$
\eta_ {\parallel} = \lim  _ {\omega \rightarrow 0} \lim  _ {k \rightarrow 0} \frac {1}{\omega} \left\langle T _ {x y} T _ {x y} \right\rangle = \lim  _ {\omega \rightarrow 0} \lim  _ {k \rightarrow 0} \frac {1}{\omega} \left\langle T _ {z y} T _ {z y} \right\rangle , \tag {70}
$$

respectively.

# B The Alekseev mechanism in two-dimensional non-relativistic hydrodynamics

In Ref. [15], it was shown in non-relativistic kinetic theory for 2D electron systems that a Hall viscosity can be induced in a charged plasma by an out-of-plane external magnetic field. The mechanism relies

on the Lorentz force exerted by the magnetic field onto the charged particles as they get exchanged between different fluid layers. Consider a electrically charged fluid at zero magnetic field, with kinematic shear viscosity $\nu _ { 0 }$ given by the relaxation time $\tau _ { 2 }$ of the second moment of the quasiparticle (in [15] electron) distribution function via

$$
\nu_ {0} = \frac {1}{4} v _ {F} ^ {2} \tau_ {2}, \quad \frac {1}{\tau_ {2}} = \frac {1}{\tau_ {2 , e e}} + \frac {1}{\tau_ {2 , 0}}. \tag {71}
$$

Here $\tau _ { 2 , e e }$ is the relaxation time due to electron-electron interactions, and $\tau _ { 2 } , 0$ due to other effects such as impurities. The latter part will be absent in the quark-gluon plasma. We include subscript 0 in $\nu _ { 0 }$ to emphasize that this is shear viscosity in the absence of magnetic field. Ref. [15] showed that when switching on a finite but still non-quantizing6 magnetic field, both kinematic shear and kinematic Hall viscosities get a correction of form

$$
\nu_ {\perp} (B) = \nu_ {x x} (B) = \frac {\nu_ {0}}{1 + (2 \omega \tau_ {2}) ^ {2}}, \quad \tilde {\nu} _ {\perp} (B) = \nu_ {x y} (B) = \frac {2 \omega_ {c} \tau_ {2} \nu_ {0}}{1 + (2 \omega \tau_ {2}) ^ {2}}. \tag {72}
$$

The non-relativistic derivation of Ref. [15] technically goes as follows. Let $\vec { v } ( \vec { r } , t )$ be the velocity field of the fluid flow, and $\tau _ { 2 }$ the intrinsic relaxation time for the relaxation to equilibrium (related to interactions between the fluid constituents). In kinetic theory, the viscous stress tensor of the fluid per particle and the associated Navier-Stokes equations are given by

$$
m \frac {\partial v _ {i}}{\partial t} = - \frac {\partial \Pi_ {i j}}{\partial x _ {j}} - m \frac {v _ {i}}{\tau} + e E _ {i}, \quad \Pi_ {i j} = m \langle v _ {i} v _ {j} \rangle . \tag {73}
$$

Here $\tau$ is a momentum relaxation timescale, to be included for condensed matter applications but set to zero in the QGP, $E _ { i }$ is an external electric field, and $\langle \rangle$ denotes a statistical average. The Einstein summation convention is assumed. The idea of Ref. [15] is now to include, on top of an already thermalized fluid, the effect of the external magnetic field. Since including the magnetic field will change the equilibrium value of $\Pi _ { i j } { } ^ { 7 }$ , Ref. [15] considers the relaxation equation

$$
\frac {\partial \Pi_ {i j}}{\partial t} = - \frac {1}{\tau_ {2}} \left(\Pi_ {i j} - \Pi_ {i j} ^ {0}\right), \tag {74}
$$

In the absence of the magnetic field, the equilibrium solution to (74) in the presence of kinematic shear viscosity $\nu _ { 0 }$ only is

$$
\Pi_ {i j} ^ {0} = - m \nu_ {0} V _ {i j}, \quad V _ {i j} = \frac {\partial V _ {i}}{\partial x _ {j}} + \frac {\partial V _ {j}}{\partial x _ {i}}, \tag {75}
$$

where the average drift velocity $V : = \langle v _ { i } \rangle$ . We emphasize that $\nu _ { 0 }$ here is kinematic shear viscosity and not dynamical shear viscosity $\eta _ { 0 }$ unlike in the main text. The two are related by the relation $\nu \approx \eta _ { 0 } / \varrho$ in the non-relativistic limit, where $\varrho$ is the mass density of the quasiparticles. The Lorentz force due to the magnetic field will now induce additional first and second moments in the velocity distribution,

$$
\frac {\partial \left\langle v _ {i} \right\rangle}{\partial t} = \omega_ {c} \epsilon_ {z i k} \left\langle v _ {k} \right\rangle , \tag {76}
$$

$$
\frac {\left\langle v _ {i} v _ {j} \right\rangle}{\partial t} = \omega_ {c} \left(\epsilon_ {z i k} \left\langle v _ {k} v _ {j} \right\rangle + \epsilon_ {z j k} \left\langle v _ {i} v _ {k} \right\rangle\right), \tag {77}
$$

with of (74), $\begin{array} { r } { \omega _ { c } = \frac { e B } { m } } \end{array}$ m the non-relativistic cyclotron frequency. Only (77) will show up on the right hand side

$$
\frac {\partial \Pi_ {i j}}{\partial t} = - \frac {1}{\tau_ {2}} \left(\Pi_ {i j} - \Pi_ {i j} ^ {0}\right) + \omega_ {c} \left(\epsilon_ {z i k} \langle v _ {k} v _ {j} \rangle + \epsilon_ {z j k} \langle v _ {i} v _ {k} \rangle\right), \tag {78}
$$

leading to a shift in the equilibrium stress tensor

$$
\Pi_ {i j} = \Pi_ {i j} ^ {0} + \tau_ {2} \omega_ {c} \left(\epsilon_ {z i k} \langle v _ {k} v _ {j} \rangle + \epsilon_ {z j k} \langle v _ {i} v _ {k} \rangle\right). \tag {79}
$$

Comparing this to the hydrodynamic form of the viscous stress tensor in the presence of Hall viscosity $\nu _ { H }$ and shear viscosity $\nu$ , $\Pi _ { i j } = m ( \nu v _ { i j } + \nu _ { H } \epsilon _ { z i k } v _ { k j } )$ yields (72).

The derivation of Ref. [15] is strictly only true in the Fermi liquid regime $\mu / T \gg 1$ , where $\mu$ is the chemical potential for the electromagnetic $U ( 1 )$ symmetry. For electron fluids, the corrections to the result (72) are not very big, of the order of 20% at most.

# C Derivation of early-time velocity gradients

In this appendix, we evaluate various terms appearing in the expressions for velocity gradients of Eq. 44. Recall from Eq. (34), we have,

$$
T ^ {t t} = T ^ {\tau \tau} + 2 \tau_ {0} \eta T ^ {\tau \eta} \tag {80}
$$

up to linear order in $\eta$ . Differentiating and using Eq. (35) and Eq. (36), we get,

$$
\begin{array}{l} \partial_ {x} T ^ {t t} = \left(\cosh y _ {L} (x, y) + 2 \eta \sinh y _ {L} (x, y)\right) \partial_ {x} e (x, y) \\ + e (x, y) (\sinh y _ {L} (x, y) + 2 \eta \cosh y _ {L} (x, y)) \partial_ {x} y _ {L} (x, y) \tag {81} \\ \end{array}
$$

Substituting this in the universal flow formula, Eq. (43), we get

$$
\begin{array}{l} \frac {T ^ {t x}}{T ^ {t t}} \approx \frac {\tau_ {0} \cosh \eta}{2} \frac {\partial_ {x} T ^ {t t}}{T ^ {t t}}, \\ = \frac {\tau_ {0} \cosh \eta}{2} \Big (\frac {\partial_ {x} e (x , y)}{e (x , y)} + \frac {2 \eta + \tanh  y _ {L} (x , y)}{1 + 2 \eta \tanh  y _ {L} (x , y)} \partial_ {x} y _ {L} (x, y) \Big), \\ = \frac {\tau_ {0} \cosh \left(\operatorname {a r c s i n h} \left(\frac {z}{\tau_ {0}}\right)\right)}{2} \left(\frac {\partial_ {x} e (x , y)}{e (x , y)} + \frac {2 (\operatorname {a r c s i n h} \left(\frac {z}{\tau_ {0}}\right)) + \tanh  y _ {L} (x , y)}{1 + 2 (\operatorname {a r c s i n h} \left(\frac {z}{\tau_ {0}}\right)) \tanh  y _ {L} (x , y)} \partial_ {x} y _ {L} (x, y)\right), \tag {82} \\ \end{array}
$$

where we used $\begin{array} { r } { \eta = ( \mathrm { a r c s i n h } \left( \frac { z } { \tau _ { 0 } } \right) ) } \end{array}$ . $\partial _ { x } y _ { L } ( x , y )$ and $\partial _ { x } e ( x , y )$ appearing in Eq. (82) are given by the following expressions

$$
\partial_ {x} y _ {L} (x, y) = \frac {f}{2} \tanh  \left(y _ {\text {b e a m}}\right) \left(\frac {\partial_ {x} T _ {A} (x , y)}{T _ {A} (x , y)} - \frac {\partial_ {x} T _ {B} (x , y)}{T _ {B} (x , y)}\right) \tag {83}
$$

and

$$
\partial_ {x} e (x, y) = \frac {m _ {N} ^ {2} \left((T _ {A} (x , y) \cosh (2 y _ {b e a m}) T _ {B} (x , y)) \partial_ {x} T _ {A} (x , y) + (T _ {B} (x , y) + \cosh (2 y _ {b e a m}) T _ {A} (x , y)) \partial_ {x} T _ {B} (x , y)\right)}{M (x , y) \left(2 \sinh (\eta_ {0}) + \sqrt {\pi / 2} \sigma_ {\eta} e ^ {\sigma_ {\eta} ^ {2} / 2} C _ {\eta}\right)} \tag {84}
$$

We now derive expressions for the gradients of $\theta$ , $y _ { L }$ , and $\operatorname { t a n h } y _ { T }$ to evaluate velocity gradients of Eq. 44. We have,

$$
\partial_ {x} \phi = - \frac {y}{x ^ {2} + y ^ {2}} \tag {85}
$$

$$
\partial_ {y} \phi = - \frac {x}{x ^ {2} + y ^ {2}} \tag {86}
$$

$$
\partial_ {x} (\tanh  y _ {T}) = - \frac {\tau_ {0} \cosh \eta}{2} \left(\frac {T ^ {t t} \partial_ {x} ^ {2} T ^ {t t} - \left(\partial_ {x} T ^ {t t}\right) ^ {2}}{\left(T ^ {t t}\right) ^ {2}}\right) \tag {87}
$$

$$
\partial_ {y} (\tanh  y _ {T}) = - \frac {\tau_ {0} \cosh \eta}{2} \left(\frac {T ^ {t t} \partial_ {y} \partial_ {x} T ^ {t t} - \left(\partial_ {x} T ^ {t t}\right) \left(\partial_ {y} T ^ {t t}\right)}{\left(T ^ {t t}\right) ^ {2}}\right) \tag {88}
$$

$$
\partial_ {z} (\tanh  y _ {T}) = - \frac {\tau_ {0}}{2} \cosh \eta \Big (\frac {T ^ {t t} \partial_ {z} \partial_ {x} T ^ {t t} - (\partial_ {x} T ^ {t t}) (\partial_ {z} T ^ {t t})}{(T ^ {t t}) ^ {2}} \Big) - \frac {\tau_ {0}}{2} \sinh \eta (\partial_ {z} \eta) \frac {\partial_ {x} T ^ {t t}}{T ^ {t t}} \tag {89}
$$

Recall $\eta = \mathrm { a r c s i n h } \left( z / \tau _ { 0 } \right)$ , which gives

$$
\partial_ {z} \eta = \frac {1}{\sqrt {z ^ {2} + \tau_ {0} ^ {2}}} \tag {90}
$$

We obtain following expressions for the gradients of $\operatorname { t a n h } y _ { T }$

$$
\tanh  y _ {T} = \frac {\tau_ {0}}{2} \cosh \eta \left(\frac {\partial_ {x} e}{e} + \frac {(\sinh y _ {L} + 2 \eta \cosh y _ {L}) \partial_ {x} y _ {L}}{(\cosh y _ {L} + 2 \eta \sinh y _ {L})}\right) \tag {91}
$$

$$
\partial_ {x} (\tanh  y _ {T}) = - \frac {\tau_ {0} \cosh \eta}{2} \left(\frac {- (\partial_ {x} e) ^ {2} + e \partial_ {x} ^ {2} e}{e ^ {2}} + \right.
$$

$$
\left. \frac {\left(2 - 8 \eta^ {2}\right) \left(\partial_ {x} y _ {L}\right) ^ {2} + \left(4 \eta \cosh 2 y _ {L} + \left(1 + 4 \eta^ {2}\right) \sinh 2 y _ {L}\right) \partial_ {x} ^ {2} y _ {L}}{2 \left(\cosh y _ {L} + 2 \eta \sinh y _ {L}\right) ^ {2}}\right) \tag {92}
$$

$$
\partial_ {y} (\tanh y _ {T}) = - \frac {\tau_ {0} \cosh \eta}{2} \bigg (\frac {- \partial_ {y} e \partial_ {x} e + e \partial_ {y} \partial_ {x} e}{e ^ {2}} +
$$

$$
\left. \frac {2 \left(1 - 4 \eta^ {2}\right) \partial_ {x} y _ {L} \partial_ {y} y _ {L} + \left(4 \eta \cosh 2 y _ {L} + \left(1 + 4 \eta^ {2}\right) \sinh 2 y _ {L}\right) \partial_ {y} \partial_ {x} y _ {L}}{2 (\cosh y _ {L} + 2 \eta \sinh y _ {L}) ^ {2}}\right) \tag {93}
$$

$$
\partial_ {z} (\tanh  y _ {T}) = \frac {\tau_ {0}}{2} \partial_ {z} \eta \left(- \frac {\sinh \eta \partial_ {x} e}{e} - \right.
$$

$$
\left. \frac {\left(2 \cosh \eta + 2 \eta \cosh 2 y _ {L} \sinh \eta + \left(1 + 4 \eta^ {2}\right) \cosh y _ {L} \sinh y _ {L} \sinh \eta\right) \partial_ {x} y _ {L}}{\left(\cosh y _ {L} + 2 \eta \sinh y _ {L}\right) ^ {2}}\right) \tag {94}
$$

Whereas, using the expression for $y _ { L }$ in Eq. (30), the gradients of $y _ { L }$ come out to be,

$$
\partial_ {x} y _ {L} = f \frac {\tanh  (y _ {\text {b e a m}})}{2} \left(\frac {\partial_ {x} T _ {A}}{T _ {A}} - \frac {\partial_ {x} T _ {B}}{T _ {B}}\right) \tag {95}
$$

$$
\partial_ {y} y _ {L} = f \frac {\tanh  (y _ {\text {b e a m}})}{2} \left(\frac {\partial_ {y} T _ {A}}{T _ {A}} - \frac {\partial_ {y} T _ {B}}{T _ {B}}\right) \tag {96}
$$

$$
\partial_ {x} ^ {2} y _ {L} = f \frac {\tanh  \left(y _ {\text {b e a m}}\right)}{2} \left(\frac {- \left(\partial_ {x} T _ {A}\right) ^ {2} + T _ {A} \partial_ {x} ^ {2} T _ {A}}{T _ {A} ^ {2}} + \frac {\left(\partial_ {x} T _ {B}\right) ^ {2} - T _ {B} \partial_ {x} ^ {2} T _ {B}}{T _ {B} ^ {2}}\right) \tag {97}
$$

$$
\partial_ {y} \partial_ {x} y _ {L} = f \frac {\tanh  (y _ {\mathrm {b e a m}})}{2} \left(\frac {- (\partial_ {x} T _ {A}) (\partial_ {y} T _ {A}) + T _ {A} (\partial_ {y} \partial_ {x} T _ {A})}{T _ {A} ^ {2}} + \frac {(\partial_ {x} T _ {B}) (\partial_ {y} T _ {B}) - T _ {B} (\partial_ {y} \partial_ {x} T _ {B})}{T _ {B} ^ {2}}\right) \tag {98}
$$

Finally we evaluate gradients of $e$ . Recall from Eq. (42),

$$
e (x, y) = \mathcal {N} _ {e} (x, y) = \frac {M (x , y)}{\kappa},
$$

$$
\kappa = 2 \sinh (\eta_ {0}) + \sqrt {\pi / 2} \sigma_ {\eta} e ^ {\sigma_ {\eta} ^ {2} / 2} C _ {\eta},
$$

$$
C _ {\eta} = e ^ {\eta_ {0}} \operatorname {e r f c} \left(- \sqrt {\frac {1}{2}} \sigma_ {\eta}\right) + e ^ {- \eta_ {0}} \operatorname {e r f c} \left(\sqrt {\frac {1}{2}} \sigma_ {\eta}\right) \tag {99}
$$

The expression for $M ( x , y )$ is given in Eq. (38). We get the following expressions for the gradients,

$$
\partial_ {x} e (x, y) = \frac {\partial_ {x} M (x , y)}{\kappa} \tag {100}
$$

$$
\partial_ {y} e (x, y) = \frac {\partial_ {y} M (x , y)}{\kappa} \tag {101}
$$

$$
\partial_ {x} ^ {2} e (x, y) = \frac {\partial_ {x} ^ {2} M (x , y)}{\kappa} \tag {102}
$$

$$
\partial_ {y} \partial_ {x} e (x, y) = \frac {\partial_ {y} \partial_ {x} M (x , y)}{\kappa} \tag {103}
$$

# References

[1] U. Heinz and R. Snellings, Collective flow and viscosity in relativistic heavy-ion collisions, Ann. Rev. Nucl. Part. Sci. 63, 123 (2013), doi:10.1146/annurev-nucl-102212-170540, 1301.2826.   
[2] C. Gale, S. Jeon and B. Schenke, Hydrodynamic Modeling of Heavy-Ion Collisions, Int. J. Mod. Phys. A 28, 1340011 (2013), doi:10.1142/S0217751X13400113, 1301.5893.   
[3] J. E. Bernhard, P. W. Marcy, C. E. Coleman-Smith, S. Huzurbazar, R. L. Wolpert and S. A. Bass, Quantifying properties of hot and dense QCD matter through systematic model-to-data comparison, Phys. Rev. C 91(5), 054910 (2015), doi:10.1103/PhysRevC.91.054910, 1502.00339.   
[4] G. S. Rocha, D. Wagner, G. S. Denicol, J. Noronha and D. H. Rischke, Theories of Relativistic Dissipative Fluid Dynamics, Entropy 26(3), 189 (2024), doi:10.3390/e26030189, 2311.15063.   
[5] J. E. Bernhard, J. S. Moreland and S. A. Bass, Bayesian estimation of the specific shear and bulk viscosity of quark–gluon plasma, Nature Phys. 15(11), 1113 (2019), doi:10.1038/s41567- 019-0611-8.   
[6] K. Zhou, L. Wang, L.-G. Pang and S. Shi, Exploring QCD matter in extreme conditions with Machine Learning, Prog. Part. Nucl. Phys. 135, 104084 (2024), doi:10.1016/j.ppnp.2023.104084, 2303.15136.   
[7] D. Shen, J. Chen, X.-G. Huang, Y.-G. Ma, A. Tang and G. Wang, A Review of Intense Electromagnetic Fields in Heavy-Ion Collisions: Theoretical Predictions and Experimental Results, Research 8, 0726 (2025), doi:10.34133/research.0726.   
[8] L. Adamczyk et al., Global Λ hyperon polarization in nuclear collisions: evidence for the most vortical fluid, Nature 548, 62 (2017), doi:10.1038/nature23004, 1701.06657.   
[9] G. Inghirami, M. Mace, Y. Hirono, L. Del Zanna, D. E. Kharzeev and M. Bleicher, Magnetic fields in heavy ion collisions: flow and charge transport, Eur. Phys. J. C 80(3), 293 (2020), doi:10.1140/epjc/s10052-020-7847-4, 1908.07605.   
[10] D. E. Kharzeev, J. Liao, S. A. Voloshin and G. Wang, Chiral magnetic and vortical effects in high-energy nuclear collisions—A status report, Prog. Part. Nucl. Phys. 88, 1 (2016), doi:10.1016/j.ppnp.2016.01.001, 1511.04050.   
[11] D. T. Son and P. Surowka, Hydrodynamics with Triangle Anomalies, Phys. Rev. Lett. 103, 191601 (2009), doi:10.1103/PhysRevLett.103.191601, 0906.5044.   
[12] J. E. Avron, R. Seiler and P. G. Zograf, Viscosity of quantum hall fluids, Physical Review Letters 75(4), 697–700 (1995), doi:10.1103/physrevlett.75.697.   
[13] J. E. Avron, Odd viscosity (1998), physics/9712050.   
[14] C. Hoyos, Hall viscosity, topological states and effective theories, Int. J. Mod. Phys. B 28, 1430007 (2014), doi:10.1142/S0217979214300072, 1403.4739.   
[15] P. Alekseev, Negative magnetoresistance in viscous flow of two-dimensional electrons, Physical review letters 117(16), 166601 (2016).   
[16] E. M. Lifshitz and L. P. Pitaevskii, Physical Kinetics, Pergamon Press, Oxford (1981).   
[17] K. Landsteiner, Y. Liu and Y.-W. Sun, Odd viscosity in the quantum critical region of a holographic Weyl semimetal, Phys. Rev. Lett. 117(8), 081604 (2016), doi:10.1103/PhysRevLett.117.081604, 1604.01346.

[18] M. Ammon, S. Grieninger, J. Hernandez, M. Kaminski, R. Koirala, J. Leiber and J. Wu, Chiral hydrodynamics in strong external magnetic fields, JHEP 04, 078 (2021), doi:10.1007/JHEP04(2021)078, 2012.09183.   
[19] R. Kubo, Statistical mechanical theory of irreversible processes. 1. General theory and simple applications in magnetic and conduction problems, J. Phys. Soc. Jap. 12, 570 (1957), doi:10.1143/JPSJ.12.570.   
[20] K. Landsteiner, Notes on Anomaly Induced Transport, Acta Phys. Polon. B 47, 2617 (2016), doi:10.5506/APhysPolB.47.2617, 1610.04413.   
[21] J. Hernandez and P. Kovtun, Relativistic magnetohydrodynamics, JHEP 05, 001 (2017), doi:10.1007/JHEP05(2017)001, 1703.08757.   
[22] V. Skokov, A. Y. Illarionov and V. Toneev, Estimate of the magnetic field strength in heavy-ion collisions, Int. J. Mod. Phys. A 24, 5925 (2009), doi:10.1142/S0217751X09047570, 0907.1396.   
[23] W.-T. Deng and X.-G. Huang, Event-by-event generation of electromagnetic fields in heavy-ion collisions, Phys. Rev. C 85, 044907 (2012), doi:10.1103/PhysRevC.85.044907.   
[24] A. Bzdak and V. Skokov, Event-by-event fluctuations of magnetic and electric fields in heavy ion collisions, Phys. Lett. B 710, 171 (2012), doi:10.1016/j.physletb.2012.02.065, 1111.1949.   
[25] V. Voronyuk, V. D. Toneev, W. Cassing, E. L. Bratkovskaya, V. P. Konchakovski and S. A. Voloshin, Electromagnetic field evolution in relativistic heavy-ion collisions, Phys. Rev. C 83, 054911 (2011), doi:10.1103/PhysRevC.83.054911.   
[26] Y. Jiang, Z.-W. Lin and J. Liao, Rotating quark-gluon plasma in relativistic heavy ion collisions, Phys. Rev. C 94(4), 044910 (2016), doi:10.1103/PhysRevC.94.044910, [Erratum: Phys.Rev.C 95, 049904 (2017)], 1602.06580.   
[27] F. Becattini and M. A. Lisa, Polarization and Vorticity in the Quark–Gluon Plasma, Ann. Rev. Nucl. Part. Sci. 70, 395 (2020), doi:10.1146/annurev-nucl-021920-095245, 2003.03640.   
[28] S. Rath and S. Dash, Analyzing the transport coefficients and observables of a rotating QGP medium in kinetic theory framework with a novel approach to the collision integral (2024), 2403.01240.   
[29] I. Muller, Zum Paradoxon der Warmeleitungstheorie, Z. Phys. 198, 329 (1967), doi:10.1007/BF01326412.   
[30] W. Israel, Nonstationary irreversible thermodynamics: A Causal relativistic theory, Annals Phys. 100, 310 (1976), doi:10.1016/0003-4916(76)90064-6.   
[31] W. Israel and J. M. Stewart, Transient relativistic thermodynamics and kinetic theory, Annals Phys. 118, 341 (1979), doi:10.1016/0003-4916(79)90130-1.   
[32] S. Mattiello and W. Cassing, Shear viscosity of the Quark-Gluon Plasma from a virial expansion, Eur. Phys. J. C 70, 243 (2010), doi:10.1140/epjc/s10052-010-1459-3, 0911.4647.   
[33] P. Danielewicz and M. Gyulassy, Dissipative phenomena in quark-gluon plasmas, Phys. Rev. D 31, 53 (1985), doi:10.1103/PhysRevD.31.53.   
[34] J. P. Blaizot, Theory of the quark gluon plasma, Lect. Notes Phys. 583, 117 (2002), doi:10.1007/3-540-45792-5_4, hep-ph/0107131.   
[35] L. I. AbouSalem, N. M. El Naggar and I. Elmashad, The Quark-Gluon Plasma Equation of State and The Generalized Uncertainty Principle (2015), 1507.03533.   
[36] P. Castorina and M. Mannarelli, Effective degrees of freedom of the quark-gluon plasma, Phys. Lett. B 644, 336 (2007), doi:10.1016/j.physletb.2006.11.058, hep-ph/0510349.   
[37] M. Sas, Temperature of the QGP: a brief overview, Rev. Mex. Fis. Suppl. 3(4), 040915 (2022), doi:10.31349/SuplRevMexFis.3.040915.   
[38] J. Adam et al., Direct photon production in Pb-Pb collisions at $\sqrt { s _ { N N } } = 2 . 7 6$ TeV, Phys. Lett. B 754, 235 (2016), doi:10.1016/j.physletb.2016.01.020, 1509.07324.   
[39] Temperature Measurement of Quark-Gluon Plasma at Different Stages (2024), 2402.01998.   
[40] V. Balasubramanian, A. Bernamonti, J. de Boer, N. Copland, B. Craps, E. Keski-Vakkuri, B. Muller, A. Schafer, M. Shigemori and W. Staessens, Thermalization of Strongly Coupled Field Theories, Phys. Rev. Lett. 106, 191601 (2011), doi:10.1103/PhysRevLett.106.191601, 1012.4753.

[41] B. Müller, A. Rabenstein, A. Schäfer, S. Waeber and L. G. Yaffe, Phenomenological implications of asymmetric AdS5 shock wave collision studies for heavy ion physics, Phys. Rev. D 101(7), 076008 (2020), doi:10.1103/PhysRevD.101.076008, 2001.07161.   
[42] P. Kovtun, D. T. Son and A. O. Starinets, Viscosity in strongly interacting quantum field theories from black hole physics, Phys. Rev. Lett. 94, 111601 (2005), doi:10.1103/PhysRevLett.94.111601, hep-th/0405231.   
[43] S. Cremonini, The Shear Viscosity to Entropy Ratio: A Status Report, Mod. Phys. Lett. B 25, 1867 (2011), doi:10.1142/S0217984911027315, 1108.0677.   
[44] J. E. Bernhard, J. S. Moreland and S. A. Bass, Bayesian estimation of the specific shear and bulk viscosity of quark–gluon plasma, Nature Phys. 15(11), 1113 (2019), doi:10.1038/s41567- 019-0611-8.   
[45] A. Bazavov, T. Bhattacharya, C. DeTar, H.-T. Ding, S. Gottlieb, R. Gupta, P. Hegde, U. M. Heller, F. Karsch, E. Laermann, L. Levkova, S. Mukherjee et al., Equation of state in $( 2 + 1 )$ - flavor qcd, Phys. Rev. D 90, 094503 (2014), doi:10.1103/PhysRevD.90.094503.   
[46] A. Czajka and S. Jeon, Kubo formulas for the shear and bulk viscosity relaxation times and the scalar field theory shear $\boldsymbol { \mathscr { n } } _ { \pi }$ calculation, Phys. Rev. C 95(6), 064906 (2017), doi:10.1103/PhysRevC.95.064906, 1701.07580.   
[47] A. Huang, D. She, S. Shi, M. Huang and J. Liao, Dynamical magnetic fields in heavy-ion collisions, Phys. Rev. C 107, 034901 (2023), doi:10.1103/PhysRevC.107.034901.   
[48] Z.-F. Jiang, Z.-H. Zhang, X.-F. Yuan and B.-W. Zhang, External-magnetic-field-induced paramagnetic squeezing effect in heavy-ion collisions at energies available at the CERN Large Hadron Collider, Phys. Rev. C 110(1), 014902 (2024), doi:10.1103/PhysRevC.110.014902, 2405.02610.   
[49] D. Seipt, M. Bluhm and B. Kampfer, Quark mass dependence of thermal excitations in QCD in one-loop approximation, J. Phys. G 36, 045003 (2009), doi:10.1088/0954-3899/36/4/045003, 0810.3803.   
[50] Y. Hidaka and M. Kitazawa, Chiral transition and mesonic excitations for quarks with thermal masses, Phys. Rev. D 75, 011901 (2007), doi:10.1103/PhysRevD.75.099901, [Erratum: Phys.Rev.D 75, 099901 (2007)], hep-ph/0610374.   
[51] A. G. Shalaby, A study on the deconfined degree of freedom $g _ { 1 }$ and the running coupling constant $\alpha _ { s } ( T )$ , Int. J. Phys. Sci. 7, 1741 (2012), doi:10.5897/IJPS11.1717, 1309.6220.   
[52] A. C. Mattingly and P. M. Stevenson, Optimization of R(e+ e-) and ’freezing’ of the QCD couplant at low-energies, Phys. Rev. D 49, 437 (1994), doi:10.1103/PhysRevD.49.437, hep-p h/9307266.   
[53] T. Dai, J.-F. Paquet, D. Teaney and S. A. Bass, Parton energy loss in a hard-soft factorized approach, Phys. Rev. C 105(3), 034905 (2022), doi:10.1103/PhysRevC.105.034905, 2012.03441.   
[54] P. Pal, Conversion table, https://www.saha.ac.in/theory/palashbaran.pal/conv.html, Accessed: 2025-05-11 (n.d.).   
[55] Z. Jiang, E. A. Henriksen, L. C. Tung, Y.-J. Wang, M. E. Schwartz, M. Y. Han, P. Kim and H. L. Stormer, Infrared spectroscopy of landau levels of graphene, Phys. Rev. Lett. 98, 197403 (2007), doi:10.1103/PhysRevLett.98.197403.   
[56] S. A. Mikhailov, Nonlinear cyclotron resonance of a massless quasiparticle in graphene, Phys. Rev. B 79, 241309 (2009), doi:10.1103/PhysRevB.79.241309.   
[57] A. A. Sokolik, A. D. Zabolotskiy and Y. E. Lozovik, Many-body effects of coulomb interaction on landau levels in graphene, Phys. Rev. B 95, 125402 (2017), doi:10.1103/PhysRevB.95.125402.   
[58] E. D’Hoker and P. Kraus, Charged Magnetic Brane Solutions in AdS (5) and the fate of the third law of thermodynamics, JHEP 03, 095 (2010), doi:10.1007/JHEP03(2010)095, 0911.4518.   
[59] T. Dore, J. Noronha-Hostler and E. McLaughlin, Far-from-equilibrium search for the QCD critical point, Phys. Rev. D 102(7), 074017 (2020), doi:10.1103/PhysRevD.102.074017, 2007.1 5083.   
[60] K. Tuchin, Initial value problem for magnetic fields in heavy ion collisions, Phys. Rev. C 93(1), 014905 (2016), doi:10.1103/PhysRevC.93.014905, 1508.06925.

[61] E. Stewart and K. Tuchin, Continuous evolution of electromagnetic field in heavy-ion collisions, Nucl. Phys. A 1016, 122308 (2021), doi:10.1016/j.nuclphysa.2021.122308, 2106.09124.   
[62] R. Ghosh and I. A. Shovkovy, Electrical conductivity of hot relativistic plasma in a strong magnetic field, Phys. Rev. D 110(9), 096009 (2024), doi:10.1103/PhysRevD.110.096009, 2404 .01388.   
[63] R. Ghosh and I. A. Shovkovy, Anisotropic charge transport in strongly magnetized relativistic matter, Eur. Phys. J. C 84(11), 1179 (2024), doi:10.1140/epjc/s10052-024-13570-3, 2407.13828.   
[64] I. A. Shovkovy and R. Ghosh, Review of heat and charge transport in strongly magnetized relativistic plasmas, AAPPS Bull. 35, 34 (2025), doi:10.1007/s43673-025-00174-6, 2506.14956.   
[65] G. Torrieri and J. Rafelski, Statistical hadronization probed by resonances, Phys. Rev. C 68, 034912 (2003), doi:10.1103/PhysRevC.68.034912, nucl-th/0212091.   
[66] S. Ryu, V. Jupic and C. Shen, Probing early-time longitudinal dynamics with the Λ hyperon’s spin polarization in relativistic heavy-ion collisions, Phys. Rev. C 104(5), 054908 (2021), doi:10.1103/PhysRevC.104.054908, 2106.08125.   
[67] S. Pratt, The Long Slow Death of the HBT Puzzle, Acta Phys. Polon. B 40, 1249 (2009), 0812.4714.   
[68] J. Vredevoogd and S. Pratt, Universal Flow in the First Stage of Relativistic Heavy Ion Collisions, Phys. Rev. C 79, 044915 (2009), doi:10.1103/PhysRevC.79.044915, 0810.4325.   
[69] S. Alzhrani, S. Ryu and C. Shen, Λ spin polarization in event-by-event relativistic heavy-ion collisions, Phys. Rev. C 106(1), 014905 (2022), doi:10.1103/PhysRevC.106.014905, 2203.15718.   
[70] C. J. Horowitz, J. Piekarewicz and B. Reed, Insights into nuclear saturation density from parity-violating electron scattering, Phys. Rev. C 102, 044321 (2020), doi:10.1103/PhysRevC.102.044321.   
[71] C. Drischler, P. G. Giuliani, S. Bezoui, J. Piekarewicz and F. Viens, Bayesian mixture model approach to quantifying the empirical nuclear saturation point, Phys. Rev. C 110(4), 044320 (2024), doi:10.1103/PhysRevC.110.044320, 2405.02748.   
[72] Queena, M. Kumar, R. Kumar and S. K. Dhiman, Symmetry energy and its impact on the characteristics of asymmetric nuclear dense matter, Phys. Rev. C 112, 025802 (2025), doi:10.1103/hjn1-24xg.   
[73] W.-J. Zou, J.-X. Lu, P.-W. Zhao, L.-S. Geng and J. Meng, Saturation of nuclear matter in the relativistic Brueckner-Hatree-Fock approach with a leading order covariant chiral nuclear force, Phys. Lett. B 854, 138732 (2024), doi:10.1016/j.physletb.2024.138732, 2312.15672.   
[74] V. Khachatryan et al., Evidence for collectivity in pp collisions at the LHC, Phys. Lett. B 765, 193 (2017), doi:10.1016/j.physletb.2016.12.009, 1606.06198.   
[75] M. Aaboud et al., Measurement of longitudinal flow decorrelations in Pb+Pb collisions at $\sqrt { s _ { N N } } = 2 . 7 6$ and 5.02 TeV with the ATLAS detector, Eur. Phys. J. C 78(2), 142 (2018), doi:10.1140/epjc/s10052-018-5605-7, 1709.02301.   
[76] G. Aad et al., Measurement of the correlation between flow harmonics of different order in lead-lead collisions at √s =2.76 TeV with the ATLAS detector, Phys. Rev. C 92(3), 034903 (2015), doi:10.1103/PhysRevC.92.034903, 1504.01289.   
[77] J. Adam et al., Correlation Measurements Between Flow Harmonics in Au+Au Collisions at RHIC, Phys. Lett. B 783, 459 (2018), doi:10.1016/j.physletb.2018.05.076, 1803.03876.   
[78] S. Acharya et al., Systematic studies of correlations between different order flow harmonics in Pb-Pb collisions at $\sqrt { s _ { \mathrm { N N } } } ~ = ~ 2 . 7 6 ~ $ eV, Phys. Rev. C 97(2), 024906 (2018), doi:10.1103/PhysRevC.97.024906, 1709.01127.   
[79] J. Schukraft, A. Timmins and S. A. Voloshin, Ultra-relativistic nuclear collisions: event shape engineering, Phys. Lett. B 719, 394 (2013), doi:10.1016/j.physletb.2013.01.045, 1208.4563.   
[80] S. Vogel, G. Torrieri and M. Bleicher, Elliptic flow fluctuations in heavy ion collisions at RHIC and the perfect fluid hypothesis, Phys. Rev. C 82, 024908 (2010), doi:10.1103/PhysRevC.82.024908, nucl-th/0703031.

[81] B. B. Abelev et al., Multiplicity dependence of the average transverse momentum in pp, p-Pb, and Pb-Pb collisions at the LHC, Phys. Lett. B 727, 371 (2013), doi:10.1016/j.physletb.2013.10.054, 1307.1094.   
[82] C. Loizides, J. Kamin and D. d’Enterria, Improved Monte Carlo Glauber predictions at present and future nuclear colliders, Phys. Rev. C 97(5), 054910 (2018), doi:10.1103/PhysRevC.97.054910, [Erratum: Phys.Rev.C 99, 019901 (2019)], 1710.07098.   
[83] B. I. Abelev et al., System-size independence of directed flow at the Relativistic Heavy-Ion Collider, Phys. Rev. Lett. 101, 252301 (2008), doi:10.1103/PhysRevLett.101.252301, 0807.1518.   
[84] L. Adamczyk et al., Beam-Energy Dependence of the Directed Flow of Protons, Antiprotons, and Pions in Au+Au Collisions, Phys. Rev. Lett. 112(16), 162301 (2014), doi:10.1103/PhysRevLett.112.162301, 1401.3043.   
[85] R. Snellings, Elliptic Flow: A Brief Review, New J. Phys. 13, 055008 (2011), doi:10.1088/1367- 2630/13/5/055008, 1102.3010.   
[86] E. Fermi, High Energy Nuclear Events, Prog. Theor. Phys. 5(4), 570 (1950), doi:10.1143/ptp/5.4.570.   
[87] S. Acharya et al., Centrality and pseudorapidity dependence of the charged-particle multiplicity density in Xe–Xe collisions at √sNN =5.44TeV, Phys. Lett. B 790, 35 (2019), doi:10.1016/j.physletb.2018.12.048, 1805.04432.   
[88] M. Garbiso and M. Kaminski, Hydrodynamics of simply spinning black holes & hydrodynamics for spinning quantum fluids, JHEP 12, 112 (2020), doi:10.1007/JHEP12(2020)112, 2007.04345.   
[89] C. Cartwright, M. G. Amano, M. Kaminski, J. Noronha and E. Speranza, Convergence of hydrodynamics in rapidly spinning strongly coupled plasma (2021), 2112.10781.   
[90] C. Cartwright, M. Kaminski and M. Knipfer, Hydrodynamic attractors for the speed of sound in holographic Bjorken flow, Phys. Rev. D 107(10), 106016 (2023), doi:10.1103/PhysRevD.107.106016, 2207.02875.   
[91] M. A. G. Amano, M. Blake, C. Cartwright, M. Kaminski and A. P. Thompson, Chaos and poleskipping in a simply spinning plasma, JHEP 02, 253 (2023), doi:10.1007/JHEP02(2023)253, 2211.00016.   
[92] M. A. G. Amano, C. Cartwright, M. Kaminski and J. Wu, Relativistic hydrodynamics under rotation: Prospects and limitations from a holographic perspective, Prog. Part. Nucl. Phys. 139, 104135 (2024), doi:10.1016/j.ppnp.2024.104135, 2308.11686.   
[93] C. Cartwright, R. Chudasama, S. Gleyzer, D. Ilyas, M. Kaminski, M. Knipfer and J. Zhang, Anisotropic time evolution of sound modes in Bjorken expanding holographic plasma (2026), 2602.02687.   
[94] M. Kaminski, Non-Equilibrium Dynamics in QCD and Holography (2025), 2512.24909.   
[95] B. Fu, S. Y. F. Liu, L. Pang, H. Song and Y. Yin, Shear-Induced Spin Polarization in Heavy-Ion Collisions, Phys. Rev. Lett. 127(14), 142301 (2021), doi:10.1103/PhysRevLett.127.142301, 2103.10403.   
[96] F. Becattini, M. Buzzegoli, G. Inghirami, I. Karpenko and A. Palermo, Local Polarization and Isothermal Local Equilibrium in Relativistic Heavy Ion Collisions, Phys. Rev. Lett. 127(27), 272302 (2021), doi:10.1103/PhysRevLett.127.272302, 2103.14621.   
[97] F. Becattini, M. Buzzegoli and A. Palermo, Spin-thermal shear coupling in a relativistic fluid, Phys. Lett. B 820, 136519 (2021), doi:10.1016/j.physletb.2021.136519, 2103.10917.   
[98] D. Everett et al., Multisystem Bayesian constraints on the transport coefficients of QCD matter, Phys. Rev. C 103(5), 054904 (2021), doi:10.1103/PhysRevC.103.054904, 2011.01430.   
[99] D. Everett et al., Phenomenological constraints on the transport properties of QCD matter with data-driven model averaging, Phys. Rev. Lett. 126(24), 242301 (2021), doi:10.1103/PhysRevLett.126.242301, 2010.03928.   
[100] A. Mankolli et al., Longitudinal Dynamics of Large and Small Systems from a 3D Bayesian Calibration of RHIC Top-energy Collision Data (2026), 2601.17234.

[101] J. Erdmenger, P. Kerner and H. Zeller, Non-universal shear viscosity from Einstein gravity, Phys. Lett. B 699, 301 (2011), doi:10.1016/j.physletb.2011.04.009, 1011.5912.   
[102] K. Jensen, M. Kaminski, P. Kovtun, R. Meyer, A. Ritz and A. Yarom, Parity-Violating Hydrodynamics in 2+1 Dimensions, JHEP 05, 102 (2012), doi:10.1007/JHEP05(2012)102, 1112.4498.   
[103] J. Liao and V. Koch, On the Fluidity and Super-Criticality of the QCD matter at RHIC, Phys. Rev. C 81, 014902 (2010), doi:10.1103/PhysRevC.81.014902, 0909.3105.
