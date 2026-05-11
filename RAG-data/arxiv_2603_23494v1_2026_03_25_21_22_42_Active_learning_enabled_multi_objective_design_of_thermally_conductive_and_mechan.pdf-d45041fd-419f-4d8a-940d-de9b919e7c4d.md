# Active learning-enabled multi-objective design of thermally conductive and mechanically compliant polymers

Yuhan Liu 1 , Jiaxin Xu 2 , Renzheng Zhang 2 , Meng Jiang 3,4 , and Tengfei Luo 2,4,5 *

# AFFILIATIONS

1 Department of Chemistry and Biochemistry, University of Notre Dame, Notre Dame, IN 46556, USA   
2 Department of Aerospace and Mechanical Engineering, University of Notre Dame, Notre Dame, IN 46556, USA   
3 Department of Computer Science and Engineering, University of Notre Dame, Notre Dame, IN 46556, USA   
4 Lucy Family Institute for Data and Society, University of Notre Dame, Notre Dame, IN 46556, USA   
5 Department of Chemical and Biomolecular Engineering, University of Notre Dame, Notre Dame, IN 46556, USA   
*: Corresponding authors: tluo@nd.edu

# ABSTRACT

Polymers are widely used in applications like flexible electronic devices and thermal interface materials due to their mechanical compliance and processing versatility. However, conventional polymers intrinsically have low thermal conductivity (TC), limiting their heat transfer abilities. Moreover, polymer research often focuses on optimizing one specific property, leaving the cooptimization of multiple competing properties less explored. Therefore, identifying polymers that simultaneously achieve high intrinsic TC while maintaining mechanical flexibility (i.e., low modulus) remains a challenge. In this study, we develop an active learning (AL) framework based on multi-objective Bayesian optimization (MOBO) to efficiently discover polymers exhibiting both high TC and low bulk modulus. Initially, a high-throughput molecular dynamics (MD) pipeline was constructed to generate polymer property data, forming a small but informative initial dataset. Independent Deep Kernel Learning (DKL) surrogate models were then constructed for TC and bulk modulus, each integrating a multi-layer perceptron feature extractor with a Gaussian Process model to capture polymer structure-property relationships and quantify prediction

uncertainties. These surrogate models guide the ?NEHVI acquisition function through a larger unlabeled polymer database ${ \sim } 2 0 0 0$ polymers), systematically selecting new polymer candidates for MD simulations and validation. Newly evaluated polymers are iteratively integrated into the training dataset, continuously refining the DKL models to explore the chemical space. Ultimately, six high-performance candidates were identified on the Pareto front, achieving the trade-offs between TC and modulus. Additionally, we applied interpretability techniques to elucidate how molecular structure influences properties under multi-objective trade-offs and assessed the synthesizability of identified candidates. By combining MD simulations with AL-enabled MOBO, our workflow mitigates data scarcity, reduces development time, and provides actionable guidance for designing multifunctional polymers tailored for different applications.

# 1. Introduction

Polymers have become indispensable in industrial applications due to their mechanical flexibility, processing versatility, corrosion resistance, and light weight 1 . Many emerging applications, such as flexible electronics and thermal interface materials, specifically require high thermal conductivity (TC) along with mechanical compliance. However, conventional amorphous polymers exhibit low intrinsic TC, typically below $0 . 4 ~ \mathrm { W \cdot m ^ { - 1 } \cdot K ^ { - 1 } }$ , due to their highly disordered atomic arrangement 2 , 3 . This intrinsic limitation significantly constrains their performance in thermal management. Embedding thermally conductive fillers (e.g., ceramics or carbon) into polymer matrices can enhance TC, but the intrinsically low TC of the polymer matrix itself continues to be the primary bottleneck2,4. Meanwhile, flexible applications demand polymers with mechanical compliance (i.e., low bulk modulus) to facilitate conformal contact and mitigate mechanical stresses in flexible assemblies. In thermal interface materials, the mechanical compliance is also critical to fill the microscale gaps between two flat surfaces. Therefore, there is a compelling need to identify polymers that simultaneously possess high intrinsic TC while maintaining softness.

Traditionally, the discovery and design of new polymers have relied heavily on intuitiondriven experimentation and trial-and-error discovery. However, inconsistent synthesis processes and measurement methods often result in prolonged testing periods and significant costs, limiting

the efficiency and scalability of polymer screening. For example, PoLyInfo5, one of the largest publicly accessible polymer databases, provides sparse experimentally measured data for neat homopolymers, with only 91 polymers for TC and 36 for bulk modulus. For some polymers, significant variations persist even under comparable measurement temperatures. For instance, the reported TC for polypropylene ranges from 0.175 to $0 . 7 8 ~ \mathrm { W \cdot m ^ { - 1 } \cdot K ^ { - 1 } }$ , while the bulk modulus of polystyrene spans 3.55 to 11.1 GPa. Such substantial inter-source variability introduces large noise into data-driven modeling and analysis. Molecular dynamics (MD) simulations provide valuable computational insight into polymer structure-property relationships but are limited by their high computational cost when applied at scale6,7. Recent advancements in polymer informatics (PI) offer a promising route toward accelerating polymer discovery through data-driven methods8,9,10,11. However, typical machine learning (ML) pipelines depend heavily on large, high-fidelity datasets 12 and typically focus on optimizing single properties individually 13 , 14 . In contrast, practical polymer applications frequently necessitate the simultaneous optimization of multiple, sometimes competing attributes. Specifically, increasing intrinsic TC typically involves rigid, ordered, highly aligned polymer backbones to enhance phonon transport15,16,17, thereby increasing stiffness. Conversely, achieving a low modulus often requires flexible, less intermolecularly constrained molecular chains18,19,20, which can impede thermal transport. Thus, enhancing one property often comes at the expense of another, which requires explicitly balancing these intrinsic trade-offs through targeted multi-objective optimization strategies in polymer design.

Recently, significant research efforts have focused on employing active learning (AL) for data-efficient, single-objective polymer discovery 21 , 22 , 23 , as well as for multi-objective optimization across broader classes of materials24,25,26,27. AL, a ML approach that strategically selects the most informative data points from an unlabeled pool for labeling28, is particularly attractive when high-fidelity property evaluation is computationally or experimentally expensive. However, AL frameworks that explicitly target multifunctional polymer discovery remain scarce29,30. Among available data-driven optimization strategies, Bayesian optimization (BO), typically built on Gaussian process (GP)-based surrogate models, can efficiently guide the selection of promising candidates by balancing exploration and exploitation via designed acquisition functions22,23,31. Extending BO into multi-objective Bayesian optimization (MOBO) enables the identification of optimal trade-offs among conflicting properties, generating a set of non-dominated solutions known as the Pareto front (i.e., solutions where one property cannot be

improved without compromising the other). Integrating AL with MOBO can address data scarcity issues and further accelerate polymer screening by prioritizing candidates expected to maximally reduce model uncertainty, thereby improving surrogate accuracy with minimal additional highfidelity data, which is particularly valuable for multifunctional polymer design.

In this study, we develop an AL-enabled MOBO workflow for identifying amorphous polymers with simultaneously high TC $( k )$ and low bulk modulus $( B )$ , as illustrated in Fig. 1. First, a high-throughput MD pipeline is established to generate polymer property labels ( $k$ and $B$ ), constructing a small initial dataset. Next, separate Deep Kernel Learning (DKL) surrogate models for $k$ and $B$ are constructed to effectively capture polymer structure-property relationships, each consisting of a multi-layer perceptron (MLP) feature extractor coupled to a GP model for uncertainty-informed prediction. These surrogates then screen a large unlabeled polymer pool. Guided by predictive means and quantified uncertainties, an acquisition function selects polymer candidates expected to yield the greatest improvements in the Pareto front. The selected polymers are evaluated through MD simulations, and the resulting new data are integrated to continuously refine the surrogate models and inform the next selection, thus forming a closed optimization loop. By repeating this AL-MOBO loop, we systematically advance the Pareto front and ultimately identify six high-performance candidates with optimal high- $k$ and low- $B$ characteristics. Beyond performance evaluation, we integrate physical descriptors with interpretable analysis to uncover molecular-level structure-property relationships governing multi-objective trade-offs and further assess synthesizability of identified polymers. By integrating MD simulations, AL-enhanced MOBO, and uncertainty-aware surrogate models, our workflow offers a data-efficient pathway that provides guidance for the development of multifunctional polymers for target applications.

图片摘要：该图主要展示 1. Schematic of the active learning multi objective Bayesian。
![](images/17f6eda66158bf29a48257e2cf23573d18504fb4b98e690be823f2a86b75be5c.jpg)  
Figure 1. Schematic of the active learning multi-objective Bayesian optimization (AL-MOBO) workflow to discover amorphous polymers with high thermal conductivity (TC, $k$ ) and low bulk modulus (?). A highthroughput MD “oracle” (bottom left) provides $k$ and $B$ labels for an initial training set and for iteratively selected candidates; uncertainty-aware deep kernel learning (DKL) surrogates (top) map polymer structure to $k$ and $B$ , and a $q$ -Noisy Expected Hypervolume Improvement (?NEHVI)-based MOBO process (right) uses their predictions to choose new polymers from the unlabeled pool and advance the $k$ -? Pareto front.

# 2. Results and discussions

# 2.1 Dataset

We curated an unlabeled screening pool of over 2000 homopolymer structures, sourced from the publicly accessible PoLyInfo5 and Membrane Society of Australasia (MSA)32 Polymer Membrane databases. This polymer dataset exhibits chemical diversity, covering a wide range of backbone families, including polyesters, polyamides, polyolefins, polyethers, polyketones, and other major classes represented in PoLyInfo6 . Polymer structures are encoded using polymer SMILES (p-SMILES)9, 33 , capturing monomer composition and polymerization connectivity, subsequently converted into numerical polymer embeddings $( \mathrm { P E } ) ^ { 9 }$ as model inputs. From the unlabeled set, we selected an initial subset of 93 polymers as training data for surrogate modeling. To ensure representative coverage and avoid bias toward specific chemistries, we utilized a Latin Hypercube Sampling (LHS) strategy with a maximin criterion for optimal space-filling34. TC and

bulk modulus values for these polymers were computed through MD simulations, which is detailed in the Method Section 4.1. As illustrated in Fig. 2a and 2b, the initial dataset spans a TC range of $0 . 0 4 7 \textrm { - } 0 . 5 5 1 \ \mathrm { W } { \cdot } \mathrm { m } ^ { - 1 } { \cdot } \mathrm { K } ^ { - 1 }$ and a bulk modulus range of 1.823 - 6.989 GPa. The high-dimensional polymer embedding space was qualitatively visualized using t-distributed Stochastic Neighbor Embedding (t-SNE) 35 (Fig. 2c). In addition, the polymer-family distribution of the initial set relative to the unlabeled pool is summarized in Supplementary Table S1 and Fig. S1. These results indicate that the initial training set exhibits broad coverage across the chemical space, avoiding early bias toward specific chemistry while leaving sparsely populated regions for adaptive exploration by the acquisition function during MOBO.

图片摘要：该图主要展示 2. Overview of the initial dataset. (a) TC and (b) bulk modu。
![](images/edac58aecf4ab8da298f80507ee304dfe705c8cb10becf0d956d60827a3fec6f.jpg)

图片摘要：该图主要展示 2. Overview of the initial dataset. (a) TC and (b) bulk modu。
![](images/4540ab260f40d5118abaca682a4f57de8a0ae64cb77b34cd20fddbe9aae80b1e.jpg)

图片摘要：该图主要展示 2. Overview of the initial dataset. (a) TC and (b) bulk modu。
![](images/b75e063f637d4e2efd62189ca1268db3d418e493919050e3498c9a12079908b7.jpg)  
Figure 2. Overview of the initial dataset. (a) TC and (b) bulk modulus distributions for the 93 amorphous polymers in the initial MD-labeled training set. (c) t-SNE visualization of the polymer embedding space, showing the initial set (red) relative to the unlabeled screening pool (gray).

# 2.2 Validation of polymer MD simulations

# 2.2.1 Comparison with experimental data

In this work, MD simulations were employed as the data-generation oracle within the AL framework to ensure all property labels were produced under consistent procedures. To validate the reliability of the MD simulations, polymers with experimentally reported property values were collected from the PoLyInfo database and other publicly available literature 36 , 37 . For fair comparison, only measurements obtained between $2 0 \ { } ^ { \circ } \mathrm { C }$ and $3 0 ^ { \circ } \mathrm { C }$ were considered, corresponding to room-temperature simulation conditions. The validation set comprised 28 TC and 18 bulk modulus data points. As shown in Fig. 3a and 3b, the MD-predicted values exhibit good agreement with experimental measurements, yielding coefficients of determination ( $\mathrm { R } ^ { 2 } = 0 . 7 5 1$ for TC and $\mathrm { R } ^ { 2 } = 0 . 6 4 1$ for bulk modulus). The observed deviations likely arise from variations in experimental conditions and measurement protocols, as well as residual uncertainty

in the MD simulations due to finite sampling, which together have been found to introduce substantial scatter in MD-experiment comparisons38.

图片摘要：该图主要展示 3. Experimental validation of the MD oracle. Parity plots co。
![](images/a69423326201551fdabced453698208a5f255568cad01a6e0904d2102c489328.jpg)

图片摘要：该图主要展示 3. Experimental validation of the MD oracle. Parity plots co。
![](images/12028e4d78ddfc28f40159e3cfba8e5dbceef8f3fefede7c450a8ba87b7f7cc7.jpg)  
Figure 3. Experimental validation of the MD oracle. Parity plots comparing MD-calculated values against experimental measurements for (a) TC and (b) bulk modulus.

# 2.2.2 Influence of polymer morphology

Previous studies have verified that randomness in polymer morphology during structure generation can introduce variations of $7 . 2 0 \%$ in the simulated TC of amorphous polymers38. To assess whether similar effects impact modulus evaluation, we examined the influence of initial structural configurations on the calculated bulk modulus. Three independent initial structures were generated for each of seven common polymers, and the resulting moduli were compared. As shown in Supplementary Fig. S2a, the coefficients of variation (defined as the ratio of standard deviation to the mean) within a single simulation were all $\leq 0 . 3 3 4$ , whereas the values across simulations with different initial structures remained below 0.041. These small deviations indicate that modulus calculations are largely insensitive to morphological randomness in the initial polymer configurations. However, to eliminate potential morphology-related biases for both TC and bulk modulus, all MD-calculated property values reported in this study were averaged from simulations conducted on three distinct initial structures for each polymer.

# 2.3 The AL-MOBO framework for multifunctional polymers

# 2.3.1 Polymer representation comparison

Prior to training the surrogate model, it is essential to establish a numerical representation for polymers to accurately quantify structure-property relationships. To identify the most informative representation, we benchmarked four commonly used methods: PE, Morgan Fingerprints (MF)39, MACCS Keys40, and RDKit Fingerprints41, on the initial dataset of 93 polymers using a unified 5-fold cross-validation (CV). Comparison was conducted under a fixed GP regressor, consistent with our subsequent DKL setup, as detailed in the Supplementary Information (SI). A GPR baseline was selected over DKL to attribute performance differences solely to the representation, avoiding confounding factors introduced by MLP, such as additional hyperparameters, neural architectures, and stochastic optimization, which may obscure the true representation effects, particularly on small datasets. As summarized in Supplementary Table S2, PE achieved the highest predictive accuracy for both TC $\mathrm { R } ^ { 2 } = 0 . 7 5 7$ , mean squared error, MSE $= 0 . 0 0 3 $ ) and bulk modulus $\mathrm { R } ^ { 2 } = 0 . 5 5 1$ , MSE = 0.459). PE, inspired by the word2vec concept9,42, represents p-SMILES into continuous-valued 300-dimensional vectors. This representation effectively captures subtle chemical differences influencing polymer properties, enabling more reliable property predictions43. Consequently, PE was adopted as the polymer representation for subsequent DKL surrogate modeling.

# 2.3.2 Construction of surrogate models

As PE are high-dimensional embeddings, Principal Component Analysis (PCA) was applied to reduce dimensionality before input into Gaussian Process (GP) regression, mitigating the curse of dimensionality23. However, as an unsupervised method, PCA discards responserelevant variance due to the lack of target-informed projections, adversely affecting predictions reliant on nonlinear features. While PCA was found effective for TC in our previous work23, the present study observed that PCA preprocessing significantly diminished critical information necessary for accurately predicting bulk modulus. Specifically, the 5-fold CV R2 for the GP model using PCA declined from approximately 0.6 initially to nearly 0.1 in subsequent iterations (Supplementary Fig. S3a), indicating severe degradation in predictive accuracy and generalization as optimization proceeded. Such feature loss decreases the signal-to-noise ratio, impairing the accurate capture of structure-modulus relationships, likely due to the strong dependence of bulk modulus on interchain interactions.

To address this, we employed DKL surrogate models, trained independently for TC $( k )$ and bulk modulus $( B )$ , incorporating MLP encoders prior to GP regression. These MLP encoders

compressed the original 300-dimensional PE into compact latent spaces (16-dimensional for $k$ and 12-dimensional for $B$ ), effectively preserving essential nonlinear information (hyperparameter optimization details provided in the Method Section 4.2). This approach effectively circumvented both the curse of dimensionality and loss of predictive features. The latent representations were subsequently input to GP regressors, providing predictive means and uncertainties. As illustrated in Supplementary Fig. S3b, DKL models demonstrated consistently robust performance throughout the AL campaign. Specifically, TC surrogate maintained stable predictive accuracy with $\mathrm { R } ^ { 2 } \sim 0 . 8$ and consistently low MSE, while the bulk modulus surrogate displayed steady performance with CV R2 around 0.58, without any noticeable deterioration. The initial surrogate accuracy, presented in Fig. 4, exhibited good agreement in trend between predictions and MD ground truth labels: TC predictions achieved CV $\mathrm { R } ^ { 2 } = 0 . 8 0 4$ and $\mathrm { M S E } = 0 . 0 0 2$ (Fig. 4a), and bulk modulus predictions yielded CV $\mathrm { R } ^ { 2 } = 0 . 6 5 9$ and $\mathrm { M S E } = 0 . 3 4 8$ (Fig. 4c). These results demonstrate the efficacy of DKL surrogates in capturing the structure-property relations of both target properties even with limited initial data.

Subsequently, these DKL models were utilized to predict properties for the entire unlabeled polymer pool. Fig. 4b and 4d visualize predicted means with posterior uncertainties $( \sigma )$ , represented as vertical bars. Moreover, initial uncertainty was quantified using 5-fold out-of-fold predictions via Spearman rank correlation and empirical coverage to evaluate uncertainty discrimination and calibration, as reported in Supplementary Table S3. These diagnostics motivate the subsequent assessment of uncertainty calibration. These posterior estimates guide the exploration-exploitation strategies during candidate selection, where high predictive means drive exploitation of promising candidates, and large posterior variances indicate under-characterized regions for exploration. The $q$ -Noisy Expected Hypervolume Improvement (?NEHVI) acquisition function balances exploration and exploitation by maximizing the expected hypervolume improvement under the joint posterior, yielding the selection of informative candidates for subsequent iterations.

图片摘要：该图主要展示 4. Performance of the DKL surrogates and their initial predi。
![](images/d6cc533d66d45f72e8406ab2fda6df3a5cb38148011bffc89ab5e6f31f7a9654.jpg)

图片摘要：该图主要展示 4. Performance of the DKL surrogates and their initial predi。
![](images/48a1b65f9f33c6705f37b9400eb0e2e0f50daef0c12027353a8aa493a6f44a18.jpg)

图片摘要：该图主要展示 4. Performance of the DKL surrogates and their initial predi。
![](images/6d2356d68912d73ca70b7de19567c7ea12d63bead08d4098bee1d9fa9376fc70.jpg)

图片摘要：该图片与Figure 4. Performance of the DKL surrogates and their initial predictions at ite这部分内容相关。
![](images/edaf76d4d1d48c09e80c8ce3047d1eff1c12123266665b022c268f52dbcb38fc.jpg)  
Figure 4. Performance of the DKL surrogates and their initial predictions at iteration 0. 5-fold crossvalidated parity plots comparing DKL-predicted and MD-labeled values for (a) TC and (c) bulk modulus. (b) and (d) show the DKL-predicted means (points) with predictive uncertainties (vertical bars) over the unlabeled polymer pool for TC and bulk modulus, respectively.

# 2.3.3 Performance assessment of the AL-MOBO framework

To effectively balance exploration and exploitation under noise during optimization loop, we employed the ? NEHVI algorithm 44 as our acquisition function. At each iteration, we concurrently selected four polymer candidates ( $q = 4$ ) to maximize the joint expected hypervolume gain while accounting for observation noise (see Method Section 4.3 for details). This promotes diverse and complementary candidate selections, optimizing guidance while managing computational costs. Throughout the 60 iterations performed (240 evaluated polymers), the AL-MOBO performance was quantified using hypervolume (HV) and incremental improvements per iteration (∆HV). Additionally, surrogate reliability and uncertainty calibration were monitored via negative log likelihood (NLL) and expected normalized calibration error (ENCE). We detail below the Pareto front development, optimization trajectory, sample efficiency via HV metrics, as well as model reliability and calibration.

Fig. 5a-c summarizes the optimization progress, showing rapid early improvements followed by diminishing gains and practical convergence around iteration 31. To verify convergence within the candidate pool, we continued optimization until iteration 60. Fig. 5a illustrates the evolution of the Pareto set through three representative snapshots, highlighting an expand-then-contract pattern: the number of non-dominated polymers peaked at 11 by iteration 8, then contracted to 6 by iteration 31 as superior candidates replaced earlier suboptimal ones. Fig. 5b depicts the sampling trajectory across all 60 iterations, chronologically color-coded, illustrating a shift from the initial broad exploration, driven by higher uncertainty, to targeted exploitation near the evolving Pareto front. Because the candidate pool is discrete, the trade-off region is not uniformly populated. Later iterations (lighter points in Fig. 5b) further sampled near the Pareto front, particularly the mid-range region, to densify local coverage and confirming convergence. The final Pareto set (red stars) consists of six polymers identified at iterations 6, 13, 19, 29, and 31, covering TC from 0.127 to $0 . 6 3 7 \mathrm { W } \mathrm { m } ^ { - 1 } \mathrm { K } ^ { - 1 }$ and bulk modulus from 1.09 to 4.654 GPa. These selections effectively represent diverse and complementary trade-offs, identifying the global extremes (lowest modulus and highest TC) among all MD-labeled polymers.

Fig. 5c evaluates sample efficiency through HV and its per-iteration increment (∆HV). HV measures the volume of space dominated by the current Pareto front relative to a fixed reference point (in two objectives, this corresponds to the dominated area)45. The HV progression reveals three distinct phases: rapid early gains (iterations 1-6), a subsequent plateau with minimal improvements (iterations 7-28), and a notable surge around iterations 29-31 followed by stabilization. HV increases only when newly evaluated polymers expand the non-dominated region (discrete, stepwise jumps rather than smooth changes). This behavior aligns with ?NEHVI, which jointly selects each batch to maximize the expected HV gain. Consequently, ∆HV is episodic rather than continuous. Sparse peaks in ∆HV indicate iterations where the Pareto front shifts outward, producing the observed HV improvements; moreover, it serves as a practical stopping criterion, signaling convergence around iteration 31. Early HV gains primarily arise from identifying polymers with notably low moduli, while later enhancements result from discovering polymers with the highest TC and strategically filling intermediate gaps. The best-so-far TC increased substantially from 0.482 W m⁻¹ K⁻¹ at iteration 1 to 0.637 W m⁻¹ K⁻¹ by iteration 29 (a $32 \%$ improvement), while the best bulk modulus decreased notably from 1.892 GPa to 1.09 GPa by

iteration 6 (a $42 \%$ reduction). Both metrics subsequently remained stable (Supplementary Fig. S4a), consistent with the observed convergence of the Pareto front.

图片摘要：该图主要展示 5c evaluates sample efficiency through HV and its per iterat。
![](images/714367ef4fa86f1da5358228166b6adf31d352f79d93b72e534d308a03ebbccb.jpg)

图片摘要：该图主要展示 5c evaluates sample efficiency through HV and its per iterat。
![](images/558349eb3a0a2c40728ced5e12b8514af7c2e25b8017834fab4c95818a3a0717.jpg)

图片摘要：该图主要展示 5c evaluates sample efficiency through HV and its per iterat。
![](images/5e7c6498de4fb7b7e4f1d31d0b86347992046b152936403643d7e768ba45f695.jpg)

图片摘要：该图片与Figure 5. Optimization trajectory and surrogate reliability of the AL MOBO strat这部分内容相关。
![](images/c3b9ffda01d8d3170be12eee8a2f55e9a6fea35c1d284e22c0d0d6460604868d.jpg)  
Figure 5. Optimization trajectory and surrogate reliability of the AL-MOBO strategy. (a) Snapshots of the non-dominated (Pareto) set at iterations 2, 8, and 31 (red stars) overlaid on all polymers evaluated up to that iteration (gray). The fixed reference point (blue cross) is set to be dominated by all evaluated polymers. (b) Sampling trajectory over 60 iterations, with AL-selected polymers color-coded by iteration index (1- 60); the final Pareto set is marked by red stars. (c) Observed hypervolume rescaled to $0 . 1 0 0 \%$ (line) and the corresponding per-iteration increment (∆HV) reported in percentage-point (pp) (bars). (d) EWMAsmoothed negative log-likelihood (NLL) for $k$ and $B$ surrogates across iterations.

Surrogate model reliability was primarily assessed using the negative log likelihood (NLL), which penalizes both inaccurate predictions and miscalibrations (over- and under-confidence). As displayed in Fig. 5d, NLL decreased for both surrogates and plateaued around iteration 30, coinciding with the observed HV and Pareto front stabilization. Across 60 iterations, the bulk modulus surrogate initially exhibited high NLL values due to its inherently noisier and more challenging prediction compared to TC. Nevertheless, its NLL sharply decreased from an initial average of 9.51 (iterations 1-5) to 1.03 over the final ten iterations, representing an approximately

$89 \%$ reduction. The TC surrogate exhibited lower and less variable NLL, decreasing from 1.77 initially to 0.74 over the same interval ( $58 \%$ reduction) and reaching 0.21 by the end of the campaign. Uncertainty calibration was further assessed using the expected normalized calibration error (ENCE), which measures the alignment between predicted uncertainties and actual errors. As shown in Supplementary Fig. S4b, rolling-pooled ENCE (5-round window) decreased from 1.05 to 0.63 for TC ( $40 \%$ reduction) and from 3.29 to 0.24 for bulk modulus ( $9 3 \%$ reduction), highlighting progressive calibration improvements.

Collectively, these results indicate enhanced posterior predictive distributions characterized by improved predictive accuracy (lower NLL) and better-calibrated uncertainties (lower ENCE). This continuous surrogate refinement underpinned the transition from initial exploration to reliable convergence. Together with steadily increasing HV, these findings validate the effectiveness of the AL-MOBO framework in efficiently exploring the polymer design space.

# 2.4 Post-optimization interpretability and analyses

# 2.4.1 t-SNE visualization of polymer space

To qualitatively show how AL-MOBO expanded coverage and converged near Pareto‑relevant regions, we visualized the chemical embedding space using t‑SNE (Fig. 6a). Specifically, we projected the 300-dimensional PE into two dimensions using t-SNE, overlaying four cohorts: the unlabeled polymer pool (gray), the initial dataset (red), all MOBO-selected candidates (color-coded by iteration from 1 to 60), and the final Pareto candidates (blue stars). The resulting t-SNE map shows a progressive optimization trajectory. Early iterations primarily sample neighborhoods close to the initial dataset, reflecting cautious exploration around known structures. As iterations advance, candidates gradually extend into previously under-sampled regions of the chemical embedding space, indicative of broader exploratory behavior. In later iterations, the sampled polymers increasingly concentrate in several distinct neighborhoods that coincide with the Pareto-optimal solutions. Notably, these Pareto solutions are not confined to a single region but instead span multiple disconnected clusters, some of which were not covered by the initial set. This distribution highlights the capability of MOBO to uncover diverse and complementary polymer chemotypes. Moreover, many late-iteration selections appear near the boundaries of densely populated regions of the unlabeled pool, implying strategic exploitation at the frontiers rather than solely within densely sampled areas.

Since t-SNE preserves local neighborhood relationships without faithfully representing global cluster sizes or inter-cluster distances, we interpret the spatial patterns qualitatively: the proximity of late-iteration points to Pareto candidates signifies neighborhood-level enrichment, whereas absolute distances are not over-interpreted. Thus, the t-SNE visualization complements quantitative assessments (such as hypervolume trajectory) by qualitatively demonstrating where the transition from exploration to exploitation occurs. Overall, the visualization confirms that MOBO expanded beyond initial regions, identified multiple structurally diverse high-value clusters, and effectively exploited previously under-explored areas, thereby providing spatial context consistent with observed improvements in optimization performance.

图片摘要：该图主要展示 6. Exploration of polymer chemical space and synthesizabilit。
![](images/b265774b4ccbddb4d60c4ce517c0407f3c1e0e1e3daf65ed84de105c5420df3b.jpg)

图片摘要：该图主要展示 6. Exploration of polymer chemical space and synthesizabilit。
![](images/c56d3843ca7b9b765018d8fd1306a42f28b0f42de969d6dd69a162c27698a151.jpg)  
Figure 6. Exploration of polymer chemical space and synthesizability assessment. (a) t-SNE projection of the polymer embedding space showing the unlabeled pool (gray), initial set (red), all MOBO-selected candidates (colored by iteration), with Pareto polymers highlighted as blue stars. (b) Distributions of SA score for the unlabeled pool (blue), all selected candidates (orange), and Pareto polymers (red), where all three are concentrated in the easy-to-moderate range.

# 2.4.2 Synthesizability evaluation

Schuffenhauer’s synthetic accessibility (SA) score46 is widely used to quantify molecular synthesizability on a scale from 1 (easy) to 10 (difficult), with scores above 6 generally considered challenging. Here, we analyzed SA score distributions for three datasets: the unlabeled pool, all MOBO-selected candidates, and the final Pareto set (Fig. 6b). Both the unlabeled pool and all selected candidates exhibit unimodal distributions centered around the easy-to-moderate region ( $\mathrm { S A } \approx 2 – 4$ ), with very few high-difficulty cases $\mathrm { ( S A > 6 ) }$ ). Compared to the unlabeled pool, the selected candidates show a slight shift toward higher complexity, reflected by a modest increase

in median (2.42 to 2.49) and mean (2.61 to 2.79). However, the proportion of difficult-tosynthesize polymers remains low $( P _ { \mathrm { S A } > 6 } = 0 . 0 2 1 )$ . Moreover, while the final Pareto candidates exhibited higher structural complexity (median 4.16), all remained within a reasonable synthesis range, with SA scores spanning 1.21 to 5.13. These results indicate that the MOBO framework effectively explored a more complex chemical space without exceeding the threshold of synthetic accessibility, supporting the practical feasibility of the identified Pareto optimal polymers for future experimental validation.

# 2.4.3 Structure-property interpretability analysis

In our MOBO workflow, opaque embeddings inherently restrict direct insight into how specific structural features influence polymer properties. To obtain mechanistic insights beyond the “black-box” nature of candidate selections47, we utilized physically interpretable descriptors to train explainable tree-based models (performance details provided in the SI), thereby explicitly attributing property variance to specific structural features. Specifically, we employed hierarchical descriptors from PolyMetriX48, minimally complemented by first-order RDKit physicochemical descriptors, which distinguish contributions from polymer backbone and sidechain attributes. These descriptors explicitly represent chemical and topological characteristics, such as backbone rigidity and $\pi$ -conjugation, chain flexibility and saturation, polarity and hydrogen bonding, charge, and proxies for packing or polarizability49.

To establish interpretable structure-property relationships, we quantitatively mapped descriptors to property contributions using SHapley Additive exPlanations (SHAP) 50 . For improved readability, SHAP values are reported using a consistent sign convention (i.e., positive SHAP values indicate an increase in the predicted TC or bulk modulus). Furthermore, SHAP plots consistently differentiate Backbone (B) and Sidechain (S) attributes (Fig. 7), directly linking structural hierarchies to property findings.

Global beeswarm plots (Fig. 7a and 7b), derived from all MD-labeled polymers (306 polymers), highlight the most influential B/S descriptors and their directional influences on polymer properties (descriptor definitions are provided in the Supplementary Table S4). Overall, backbone rigidity and $\pi$ -conjugation metrics (e.g., AromaticFrac, AroRings, Balaban J) contribute positively to the SHAP values for both TC and bulk modulus. This finding agrees with previous studies showing that rigid, ordered backbones enhance phonon transport, especially along the

backbone17, 51 , thereby improving TC at the cost of mechanical flexibility. Conversely, the descriptor FracCSP3 (fraction of $\mathsf { s p } ^ { 3 }$ carbons) represents saturated carbon content. Within our amorphous polymer dataset, higher FracCSP3 (B) corresponds to increased rotatable dihedrals, causing segmental disorder and phonon scattering, which reduces TC, consistent with MD observations that chain rotation lowers the TC of single-chain polymers 52 , 53 . Additionally, sidechain flexibility (captured by higher FracCSP3 (S)) decreases the modulus by enhancing segmental mobility and loosening packing, aligning with studies indicating longer, more flexible alkyl side chains soften polymers54,55. Collectively, these insights confirm the anticipated tradeoff between polymer rigidity and mechanical compliance.

Polarity-related descriptors further differentiate the mechanisms governing bulk modulus and TC. TPSA (B/S), representing polar surface area56, exhibits positive contributions to bulk modulus, consistent with stronger noncovalent interactions (e.g., dipolar and hydrogen-bonding) enhancing interchain electrostatic cohesion and thereby increasing modulus57. For TC, although thermal transport is often reported to improve when intermolecular coupling (e.g., H‑bonds) is strengthened in polymers 58 , our amorphous dataset shows a negative net effect of polarity: depending on chain conformation and packing state, electrostatic interactions among polar groups can promote self-association and more compact conformations59 (e.g., smaller radius of gyration), which may impede effective backbone-mediated thermal transport, leading to lower TC17. This interpretation aligns with the observed negative SHAP contribution of MaxAbsQ (S) to TC. Notably, nO (B) acts as a composite proxy: beyond reflecting polymer polarity, it also correlates with oxygen-containing linkage types and associated conformational flexibility (e.g., softer torsional potentials), which likewise contributes negatively to TC in this dataset. Overall, lowering polarity density emerges as a feasible lever for increasing TC while decreasing bulk modulus.

Additional descriptors for TC and bulk modulus further refine these mechanistic interpretations. Regarding TC (Fig. 7a), sidechain complexity indices, such as SidechainDiv (S) and NumSidechains (S), negatively correlate with TC. This is likely related to the vibrational interaction between the side chain and the backbone: the diverse sidechains can have diverse vibrational frequency spectra, which scatter different phonon modes transporting along the backbone, thus reducing TC 60 . Additionally, high HalogenFrac (S) aligns with lower TC, consistent with increased mass-disorder and phonon scattering as well as reduced phonon group velocities in heavy-atom-containing polymers61. For modulus descriptors (Fig. 7b), features that

improve packability tend to increase bulk modulus (reducing polymer flexibility), whereas packing-disruptive features decrease bulk modulus and thus promote flexibility. Specifically, Kappa2 (S) reveals that more rod-like, less-branched side chains pack more efficiently, which can elevate modulus54. Most visibly, LabuteASA (B), a 2D proxy for backbone accessible surface, illustrates that larger contactable backbone area is associated with a higher modulus, consistent with the classical view that greater inter-chain packing corresponds to higher stiffness 62 . Conversely, the descriptor AliphRings (B) reflects a softening trend in this dataset, consistent with cycloaliphatic (contorted) units disrupting backbone planarity and inter-chain packing63,64.

Overall, SHAP analysis indicates that TC is governed primarily by intrachain vibrational transport along the covalently connected backbone, favored by straighter and more rigid backbones, whereas the bulk modulus is dominated by interchain cohesion and packing, reflected by polarity and accessible-surface descriptors. These insights offer actionable guidance for multi-objective polymer design: maintaining rigid, $\pi$ -rich backbones to enhance TC, while reducing modulus primarily through non-polar flexibility (e.g., rotatable segments at side chains) and backbone contortions that impede dense packing. Simultaneously, strongly polar side chains should be avoided, as these negatively impact TC in our models.

Within these structure-property trends, the six polymer candidates ultimately identified on the Pareto front (Fig. 7c) exemplify distinct structural strategies to balance TC and bulk modulus. PF5 (polyethylene) anchors the high-TC boundary: its chemically simple, fully saturated hydrocarbon backbone facilitates efficient packing, yielding the highest TC in our dataset (0.637 $\mathrm { W } \mathrm { m } ^ { - 1 } \mathrm { K } ^ { - 1 } .$ ), though at the expense of a high bulk modulus, highlighting the stiffness penalty at this extreme. Conversely, PF1 [poly(1,2,2-trifluorovinyl 1,1,2,2,3,4,4-heptafluorobut-3-enyl ether)] occupies the opposite end of the Pareto front with extensive fluorination and a small ether linkage. The strong C-F bonds combined with low polarizability lead to low interaction energy between chains and thus the lowest modulus observed (1.09 GPa).

Positioned between these extremes, PF3 [poly(3,3′-bi(11H-5-thia-6,12- diazananaphthacene)- $\cdot 8 , 8 ^ { \prime }$ -diyl] features a $\pi$ -conjugated backbone containing N/S heteroatoms. Its rigid $\pi$ -framework leads to relatively high TC, while potential hydrogen-bonding N–H/amine sites tend to enhance interchain cohesion, placing its modulus towards the higher end of the Pareto front. PF2 (PIM-PI-1)65 and PF4 (PIM-PI-4)65, recognized as polyimides of intrinsic microporosity (PIM-PIs), incorporate locally rigid $\pi$ -rich segments combined with spiro-center-induced

geometric contortion. Consistent with classical PIM topologies, these “rigid yet contorted” structures inhibit dense packing and produce high free volume66,67. Additionally, many of the O/N sites appear sterically shielded within their bulky fused frameworks, limiting the formation of extended inter-chain hydrogen-bonding networks, reflected in our simulations as relatively low moduli paired with moderate TC values. Lastly, PF6 (PBO-PI 0/100) is a rigid, aromatic polymer belonging to the PBO-PI family, characterized by multiple aryl-O-aryl ether linkages. Its $\pi$ -rich but kinked fused aromatic backbone packs less efficiently than PF5, resulting in intermediate modulus values between the softer PIM-PIs and the tightly packed hydrocarbon (PF5). Collectively, these examples support our established design principles, demonstrating structurally diverse, chemically complementary polymers capable of achieving a range of property trade-offs.

图片摘要：该图主要展示 7. SHAP based interpretability and structures of Pareto opti。
![](images/2b93ec7e5d3bb5dc7fc61ffa54e3d0ccfd0fbcfa570d1d4951ac7850eed32cb2.jpg)

图片摘要：该图主要展示 7. SHAP based interpretability and structures of Pareto opti。
![](images/4f9de407de6fce1e43938512e2a47035d139823f7c5fba185f7f35d8b764307b.jpg)

图片摘要：该图主要展示 7. SHAP based interpretability and structures of Pareto opti。
![](images/02ff3df8e7d851ef5b9ad22e251ec0d9820b8da7b585daa973e12ec94e1f41db.jpg)  
Figure 7. SHAP-based interpretability and structures of Pareto-optimal polymers. (a, b) SHAP beeswarm plots ranking the top-15 backbone (B) and sidechain (S) descriptors governing (a) TC and (b) bulk modulus. Positive values indicate an increase in the target property. Points are colored by standardized feature value $( { \mathrm { r e d } } = { \mathrm { h i g h } }$ , blue $=$ low). (c) Chemical structures and MD-predicted TC $( \mathrm { W } { \cdot } \mathrm { m } ^ { - 1 } { \cdot } \mathrm { K } ^ { - 1 } )$ ) and bulk modulus

(GPa) of the six Pareto-optimal polymers identified by AL-MOBO, illustrating diverse motifs governing the optimal trade-offs.

# 3. Conclusion

This study presents an AL-enabled MOBO framework designed to discover amorphous polymers that simultaneously achieve high TC and low bulk modulus. By integrating a highthroughput molecular dynamics pipeline, deep-kernel learning surrogates, and the ? NEHVI acquisition strategy, the framework efficiently explored the polymer space and identified six nondominated candidates, which span the performance extremes (lowest modulus and highest TC) and capture the trade-off between mechanical compliance and heat transport efficiency. Structureproperty interpretability analyses further elucidated the molecular mechanisms underlying this trade-off, revealing how intrachain backbone rigidity and interchain cohesive interactions jointly influence the balance between thermal transport and elastic stiffness. The synthetic accessibility assessment indicated that the identified Pareto polymers are both chemically diverse and practically attainable. Looking forward, this scalable workflow offers a pathway to explore additional properties and material classes. Future efforts will involve applying this framework to larger polymer libraries (e.g., entire PoLyInfo, PI1M databases) and enhancing molecular dynamics accuracy to further expand discovery potential and predictive reliability. Overall, this study establishes a data-efficient and interpretable paradigm for the systematic design of multifunctional polymers, offering guidance for targeted materials design in applications such as flexible electronics and thermal interface materials.

# 4. Methods

# 4.1 MD simulation

TC $( \kappa )$ and bulk modulus $( B )$ were obtained via a two-step MD simulation comprising amorphous structure generation and optimization, followed by property evaluation, which are Non-Equilibrium MD (NEMD) for $\kappa$ and finite-strain elasticity for $B$ .

Amorphous Polymer Structure Generation and Optimization. Our methodology involves the polymerization of monomers, chain replication, and fully structural relaxation. Polymer monomers are represented in SMILES (Simplified Molecular Input Line Entry System) strings and serve as inputs to PYSIMM68 (a Python-based automated pipeline). As shown in Fig.

1, we use this pipeline to automate the polymerization of monomers into polymer chains with approximately 600 atoms each69 . The General AMBER Force Field 2 (GAFF2) 70 forcefield parameters are assigned simultaneously to each polymer by PYSIMM. Each polymer chain is then replicated six times and put in a simulation box with periodic boundary conditions. Subsequently, the structures will be optimized using the large-scale atomic-molecular massively parallel simulator (LAMMPS)71. The initialization process involves simulating the system under the NVT ensemble at 100 K for 2 ps, followed by a gradual heating up to $1 0 0 0 \mathrm { K }$ in 1 ns, and then simulated in the NPT ensemble for an additional 50 ps at 0.1 atm, achieving further relax the structure and eliminate close contacts between atoms. Following this, the system experiences a 1 ns NPT simulation at $1 0 0 0 \mathrm { K }$ , allowing the pressure to rise from 0.1 atm to 500 atm. Subsequently, the obtained polymer system was annealed from $1 0 0 0 \mathrm { K }$ to $3 0 0 \mathrm { K }$ with a cooling rate of $1 4 0 ~ \mathrm { K / n s }$ in an NPT ensemble at 1 atm, followed by another NPT run at $3 0 0 ~ \mathrm { K }$ and 1 atm for 8 ns as the relaxation process to achieve the final equilibration state. This procedure is designed to simulate realistic polymer behaviors under diverse conditions.

TC Calculation. Each relaxed amorphous polymer structure, which was in a cubic box, is then duplicated in three copies to form a cuboid for TC calculation. Their sizes are around $9 . 9 \times$ $3 . 3 \times 3 . 3 \mathrm { n m } ^ { 3 }$ , with slight variations due to density differences of specific polymers. The cuboid is then employed for calculating TC via Non-Equilibrium MD (NEMD) simulations. The system is run in an NVE ensemble for 5 ns with a 0.25 fs timestep to capture the vibrational dynamics of light hydrogen atoms. In NEMD, we establish thermal gradients using Langevin thermostats at opposite ends of the system, setting a heat source at $3 2 0 \mathrm { K }$ and a sink at 280 K. Finally, the heat flux and temperature profiles over the last 5 ns of the simulation are recorded to calculate TC using Fourier’s law72, $\begin{array} { r } { \kappa = - \frac { J } { \nabla \mathrm { T } } . } \end{array}$ where $J$ is the heat flux and ∇? is the temperature gradient along the heat flux direction.

Modulus Calculation. The bulk modulus of amorphous polymers was computed using a finite‑deformation stress-strain method implemented in LAMMPS. Each equilibrated polymer cell was first converted from a cubic to a triclinic box to allow for shear deformation. Symmetric $\pm 2 \%$ finite strains were then applied along the six independent strain modes (three normal and three shear) with atom remapping. After each $\pm$ deformation, the system was run at fixed volume at 300 K using NVE integration coupled with a Langevin thermostat, consisting of a 250-fs brief equilibration followed by a 75-fs sampling segment (0.25 fs timestep), and the time-averaged stress

tensor was recorded. The elastic stiffness constants73 $C _ { i j }$ were derived from the linear relation between stress $( \sigma _ { i } )$ and strain $\left( \varepsilon _ { j } \right)$ within the elastic regime, yielding the complete $6 \times 6$ stiffness matrix via central finite differences. The bulk modulus was computed from the symmetrized stiffness constants using the Voigt expression $B = ( C _ { 1 1 } + 2 C _ { 1 2 } ) / 3$ , which is equivalent to the Voigt-Reuss-Hill value under isotropic symmetry. To ensure statistical reliability, for each simulation, the final mean bulk modulus was averaged from 100 snapshot evaluations evenly sampled over an 8 ns production trajectory. A representative polyacrylic acid example illustrating the snapshot-averaging stability is provided in Supplementary Fig. S2b. This workflow adheres to standard finite‑temperature elasticity protocols in LAMMPS.

# 4.2 Polymer representation and DKL surrogate model

We constructed separate DKL surrogate models to predict TC $( k )$ and bulk modulus $( B )$ . The DKL framework combines a neural feature extractor $\phi _ { \theta } ( \cdot )$ with a GP prior in the latent feature space:

$$
\mathbf {z} = \phi_ {\boldsymbol {\theta}} (\mathbf {x}), \qquad f (\mathbf {z}) \sim \mathcal {G P} (m (\mathbf {z}), k _ {\psi} (\mathbf {z}, \mathbf {z} ^ {\prime})), \qquad y _ {i} = f (\mathbf {z} _ {i}) + \varepsilon_ {i}, \qquad \varepsilon_ {i} \sim \mathcal {N} (0, \sigma_ {n} ^ {2})
$$

where $\phi _ { \theta }$ is an MLP-based FeatureNet and $k _ { \psi }$ represents the GP kernel (Rational Quadratic kernel for TC and Matern kernel with $\nu = 1 . 5$ for modulus).

Input features derived from p-SMILES were converted into PE, the approximately 300- dimensional embeddings using mol2vec, and subsequently standardized based on the initial set for numerical stability. Target properties (TC in $\textrm { W } \textrm { m } ^ { - 1 } \textrm { K } ^ { - 1 }$ and bulk modulus in GPa) were standardized separately (z-score space) to remove bias from differing scales. The feature extractor is an MLP with ReLU $^ +$ dropout feeding an Exact GP: for TC - hidden (192, 128), dropout 0.1, latent 16; for Modulus - hidden (224, 192, 128, 32), dropout 0.05, latent 12. Model architectures were selected based on Optuna74 tuning and then fixed for all subsequent experiments. The GP models used a ConstantMean function and ScaleKernel applied over an Automatic Relevance Determination (ARD) kernel matching the latent dimension. The TC surrogate utilized a Rational Quadratic kernel (with an alpha prior set as Gamma (1.5, 1.0)), while the modulus surrogate employed a Matern kernel with $\nu = 1 . 5$ . Both GPs used a Gaussian likelihood function.

Training proceeded in two optimization phases under double-precision computation: an initial Adam pre-optimization phase (learning rate $3 \times 1 0 ^ { - 4 }$ for 200 epochs) followed by L-BFGS fine-tuning (TC surrogate: learning rate 0.8 for 40 iterations; modulus surrogate: learning rate 0.8

for 50 iterations), with maximizing the exact marginal log likelihood in GPyTorch with joint endto-end updates of the MLP weights/biases, GP kernel parameters, the constant mean, and the likelihood noise $\sigma _ { n } ^ { 2 }$ . We evaluated the models through 5-fold CV. All predictions were made using the observation-noise posterior, and uncertainties were back-transformed to physical units via their respective scalers. Reported CV metrics and parity plots are also shown in physical units. A consistent random seed (42) was applied throughout the entire process.

# 4.3 Multi-objective optimization and active learning

All multi-objective optimization was conducted in the z-score space used to train the DKL surrogates, with the bulk modulus sign-flipped $( - B )$ so both objectives were maximized. We construct a two-objective surrogate by combining the independently trained DKL models for $k$ and $- B$ into a ModelListGP. Candidate selection is driven by the ? -Noisy Expected Hypervolume Improvement (?NEHVI) acquisition function, defined as

$$
\alpha_ {q \mathrm {N E H V I}} (\mathbf {X} _ {q}) = \mathbb {E} _ {F _ {n}, f (\mathbf {X} _ {q})} [ \mathrm {H V} (\mathrm {N D} (F _ {n} \cup f (\mathbf {X} _ {q}))) - \mathrm {H V} (\mathrm {N D} (F _ {n})) ],
$$

where $F _ { n }$ denotes a posterior sample of the previously evaluated objectives, ND(⋅) the non-dominated set, $\mathbf { X } _ { q }$ the batch of $q$ candidates, and HV(⋅) the hypervolume with respect to a reference point. Monte Carlo sampling approximation was used to estimate the joint posterior expectation for candidate selection (batch size $q = 4$ ) over the unlabeled polymer pool. Featurewise min-max normalization bounds ( $10 \%$ padding) were computed from the labeled embeddings and used to normalize both the baseline set and the unlabeled pool for acquisition optimization, and the reference point was initialized 6 units $\scriptstyle ( { \varepsilon } = 6 )$ below the initial objective minima and kept fixed for hypervolume (HV) computation (validated each iteration to remain below the current minima). Newly selected polymers were evaluated via MD to obtain ground-truth property labels, appended to the training set, and removed from the unlabeled pool to prevent duplication. Both DKL surrogates were retrained each iteration using the same configuration as in surrogate model construction. After every update, the updated HV was computed and 5-fold CV performed to monitor R² and MSE in real units. The AL‑MOBO loop proceeded for 60 iterations, with the iteration achieving the highest HV designated as the final optimum $( S _ { \mathrm { b e s t } } )$ .

We evaluated each MOBO iteration in terms of probabilistic performance using the Gaussian negative log‑likelihood (NLL) and uncertainty calibration using the expected normalized calibration error (ENCE). At each iteration $t$ , we prospectively evaluated performance on the

newly acquired batch using surrogate models trained up to iteration ? − 1. Specifically, predictive means $\mu _ { i }$ and standard deviations $\sigma _ { i }$ were obtained from the posterior predictive distribution including observation noise. The NLL was computed as

$$
\mathrm {N L L} = \frac {1}{N} \sum_ {i = 1} ^ {N} \left(\frac {1}{2} \log (2 \pi \sigma_ {i} ^ {2}) + \frac {(y _ {i} - \mu_ {i}) ^ {2}}{2 \sigma_ {i} ^ {2}}\right),
$$

where $N$ is the number of newly evaluated polymers at iteration $t$ .

For calibration assessment, predictions were sorted by $\sigma$ , partitioned into $B$ equal-sized bins (per iteration $B = 4$ , matching $q = 4$ ). In each bin $b$ , we calculated

$$
\mathrm {R M S E} _ {b} = \sqrt {\frac {1}{| b |} \sum_ {i \in b} (y _ {i} - \mu_ {i}) ^ {2}}, \quad \mathrm {R M S} _ {\sigma , b} = \sqrt {\frac {1}{| b |} \sum_ {i \in b} \sigma_ {i} ^ {2}},
$$

and defined ENCE as

$$
\mathrm {E N C E} = \frac {| b |}{N} \sum_ {b = 1} ^ {B} \frac {| \mathrm {R M S E} _ {b} - \mathrm {R M S} _ {\sigma , b} |}{\mathrm {R M S} _ {\sigma , b}},
$$

To stabilize small-batch variation, a rolling pooled ENCE was computed by pooling samples over a sliding window of $W = 5$ iterations prior to binning. As ENCE depends on the employed binning strategy, we report it as an internal calibration diagnostic rather than an absolute benchmark. Learning‑curve trends for NLL were smoothed for visualization using an exponentially weighted moving average (EWMA, $\alpha = 0 . 3 5$ ), while reported statistics were computed from raw periteration metrics. All uncertainty metrics were computed in the standardized z-score space used during optimization.

# 4.4 Post-optimization interpretability and analyses

t-SNE visualization. We visualized the polymer feature space using t-SNE to examine how the initial set, unlabeled pool, and MOBO-selected candidates were distributed in the polymer embedding space. PEs were standardized using a scaler fitted on the combined initial and unlabeled datasets, and the same scaler was applied to all subsets. Dimensionality was reduced with PCA ( $\leq 5 0$ components) before computing a single unified 2D t-SNE embedding. Perplexity was set adaptively based on the total sample size. All subsets were embedded jointly to ensure comparability and prevent drift between maps. Following standard practice, the resulting t-SNE map is interpreted qualitatively to reveal local chemical neighborhoods rather than global distances.

Feature importance analysis. For structure-property interpretation, we trained treeensemble regressors on the MD-labeled polymer set (all selected candidates combined with the

initial set, totaling 306 polymers) and computed SHAP values to quantify feature importance. Input features were built from a hierarchical descriptor set using PolyMetriX at full-polymer, backbone, and sidechain levels, and were minimally supplemented with RDKit physicochemical descriptors computed at the same hierarchy, span size and shape, $\pi$ -conjugation and rigidity, flexibility, polarity and hydrogen-bonding, polarizability, composition, and packing-related proxies. All descriptors were standardized (z-score). Highly correlated features were removed using a correlation threshold of $| \mathbf { r } | > 0 . 9 2$ , yielding a non-redundant subset of 82 features used for downstream analysis. For each target property ( $k$ and $B$ ), we performed a small grid search over RandomForestRegressor and ExtraTreesRegressor hyperparameters and selected the bestperforming model via 10-fold CV. Out‑of‑fold SHAP values were then computed with TreeExplainer (interventional mode) to quantify each descriptor’s contribution to TC and bulk modulus. SHAP values are reported using a consistent sign convention: positive values indicate higher model-predicted $k$ or $B$ . The interpretations are visualized through top K feature bar charts $( \mathrm { K } { = } 1 5$ ), value-colored SHAP beeswarm plots, and SHAP-feature dependence plots for key descriptors. For interpretability, Fig. 7a and 7b focuses on backbone/sidechain descriptors that directly map attributions to structural hierarchies. Descriptor stability was further assessed via bootstrap resampling (500 iterations) and y‑scramble controls (20 permutations), by monitoring the overlap and Jaccard similarity of the Top-15 descriptor sets across resamples.

# Acknowledgements

This work was supported in part by the Notre Dame Center for Research Computing and National Science Foundation grants (2332270 and 2102592).

# Author contributions

Y.L. and T.L. conceived the project. Y.L. developed the methodology, implemented the model, and carried out the investigation. Y.L., J.X. and R.Z. curated the data. Y.L., T.L. and M.J. performed the formal analysis. Y.L. prepared the visualizations and wrote the original draft. T.L. supervised the work and acquired funding. All authors reviewed and edited the manuscript and approved the final version.

# Data availability

The authors declare that the data supporting the findings of this study are available within the article and its supplementary information files or will be available for download from https://github.com/yuhanliu57/Polymer-ALMOBO upon publication.

# Code availability

The code for this study will be available for download from https://github.com/yuhanliu57/Polymer-ALMOBO upon publication. Other codes can be available upon reasonable request from the authors.

# Conflict of interest

The authors declare no competing financial interest.

# Additional information

Supplementary information is available for this paper.

# References

1 Shen, S., Henry, A., Tong, J., Zheng, R. & Chen, G. Polyethylene nanofibres with very high thermal conductivities. Nat. Nanotechnol. 5, 251-255 (2010).   
2 Wei, X., Wang, Z., Tian, Z. & Luo, T. Thermal transport in polymers: a review. J. Heat Transf. 143, 072101 (2021).   
3 Henry, A. Thermal transport in polymers. Annu. Rev. Heat Transf. 17, 485–520 (2014).   
4 Xu, X., Chen, J., Zhou, J. & Li, B. Thermal conductivity of polymers and their nanocomposites. Adv. Mater. 30, 1705544 (2018).   
5 Otsuka, S., Kuwajima, I., Hosoya, J., Xu, Y. & Yamazaki, M. PoLyInfo: Polymer database for polymeric materials design. Proc. Int. Conf. Emerg. Intell. Data Web Technol. 22-29 (2011).   
6 Hayashi, Y., Shiomi, J., Morikawa, J. & Yoshida, R. RadonPy: automated physical property calculation using all-atom classical molecular dynamics simulations for polymer informatics. npj Comput. Mater. 8, 222 (2022).   
7 Kim, J., Liu, Y., Luo, T. & Tian, Z. Molecular Dynamics Simulations in Nanoscale Heat Transfer: A Mini Review. ASME J. Heat Mass Transf. 147, 030801 (2025).   
8 Kim, C. et al. Polymer genome: a data-powered polymer informatics platform for property predictions. J. Phys. Chem. C 122, 17575–17585 (2018).   
9 Ma, R. & Luo, T. PI1M: a benchmark database for polymer informatics. J. Chem. Inf. Model. 60, 4684- 4690 (2020).   
10 Chen, L. et al. Polymer informatics: current status and critical next steps. Mater. Sci. Eng. R Rep. 144, 100595 (2021).   
11 Liu, Y., Alosious, S., Zhou, J., Jiang, M. & Luo, T. Machine Learning in Nanoscale Thermal Transport. Annu. Rev. Heat Transf. 28, 173–214 (2025).   
12 Tao, L., Varshney, V. & Li, Y. Benchmarking machine learning models for polymer informatics: an example of glass transition temperature. J. Chem. Inf. Model. 61, 5395–5413 (2021).   
13 Wu, S. et al. Machine-learning-assisted discovery of polymers with high thermal conductivity using a molecular design algorithm. npj Comput. Mater. 5, 66 (2019).   
14 Ma, R., Zhang, H. & Luo, T. Exploring high thermal conductivity amorphous polymers using reinforcement learning. ACS Appl. Mater. Interfaces 14, 15587-15598 (2022).   
15 Zhang, T. & Luo, T. Morphology-influenced thermal conductivity of polyethylene single chains and crystalline fibers. J. Appl. Phys. 112, 093502 (2012).   
16 Zhang, T., Wu, X. & Luo, T. Polymer nanofibers with outstanding thermal conductivity and thermal stability: fundamental linkage between molecular characteristics and macroscopic thermal properties. J. Phys. Chem. C 118, 21148–21159 (2014).   
17 Zhang, T. & Luo, T. Role of chain morphology and stiffness in thermal conductivity of amorphous polymers. J. Phys. Chem. B 120, 803–812 (2016).   
18 Holliday, L. The stiffness of polymers in relation to their structure. In Structure and Properties of Oriented Polymers, 242–263 (Springer, 1975).   
19 Stafford, C. M. et al. Elastic moduli of ultrathin amorphous polymer films. Macromolecules 39, 5095– 5099 (2006).

20 Torres, J. M., Stafford, C. M. & Vogt, B. D. Elastic modulus of amorphous polymer thin films: relationship to the glass transition temperature. ACS Nano 3, 2677–2685 (2009).   
21 Xu, J. & Luo, T. Unlocking enhanced thermal conductivity in polymer blends through active learning. npj Comput. Mater. 10, 74 (2024).   
22 Kim, C., Chandrasekaran, A., Jha, A. & Ramprasad, R. Active-learning and materials design: the example of high glass transition temperature polymers. MRS Commun. 9, 860-866 (2019).   
23 Zhang, R., Xu, J., Zhang, H., Xu, G. & Luo, T. Active learning-guided exploration of thermally conductive polymers under strain. Digit. Discov. 4, 812-823 (2025).   
24 Jablonka, K. M., Jothiappan, G. M., Wang, S., Smit, B. & Yoo, B. Bias free multiobjective active learning for materials design and discovery. Nat. Commun. 12, 2312 (2021).   
25 MacLeod, B. P. et al. A self-driving laboratory advances the Pareto front for material properties. Nat. Commun. 13, 995 (2022).   
26 Torres, J. A. G., Lau, S. H., Anchuri, P., Stevens, J. M. & Tabora, J. E. et al. A multi-objective active learning platform and web app for reaction optimization. J. Am. Chem. Soc. 144, 19999-20007 (2022).   
27 Huang, X., Zhao, C. Y., Wang, H. & Ju, S. AI-assisted inverse design of sequence-ordered high intrinsic thermal conductivity polymers. Mater. Today Phys. 44, 101438 (2024).   
28 Settles, B. Active Learning Literature Survey. Technical Report 1648, Univ. Wisconsin–Madison, Dept. Computer Sciences (2009).   
29 Martin, T. B. & Audus, D. J. Emerging trends in machine learning: a polymer perspective. ACS Polym. Au 3, 239–258 (2023).   
30 Knox, S. T. et al. Autonomous polymer synthesis delivered by multi-objective closed-loop optimisation. Polym. Chem. 13, 1576–1585 (2022).   
31 Batra, R., Song, L. & Ramprasad, R. Emerging materials intelligence ecosystems propelled by machine learning. Nat. Rev. Mater. 6, 655–678 (2021).   
32 Membrane Society of Australasia (MSA). Membrane Society of Australasia MSA. Available at: www.membrane-australasia.org (accessed 2025).   
33 Weininger, D. SMILES, a chemical language and information system. 1. Introduction to methodology and encoding rules. J. Chem. Inf. Comput. Sci. 28, 31-36 (1988).   
34 Morris, M. D. & Mitchell, T. J. Exploratory designs for computational experiments. J. Stat. Plan. Inference 43, 381-402 (1995).   
35 Van der Maaten, L. & Hinton, G. Visualizing data using t-SNE. J. Mach. Learn. Res. 9, 2579-2605 (2008).   
36 Wypych, G. Handbook of Polymers. (Elsevier, 2022).   
37 Mark, J. E. Polymer Data Handbook. 2nd edn. (Oxford University Press, 2009).   
38 Ma, R., Zhang, H., Xu, J., Sun, L. & Hayashi, Y. et al. Machine learning-assisted exploration of thermally conductive polymers based on high-throughput molecular dynamics simulations. Mater. Today Phys. 28, 100850 (2022).   
39 Rogers, D. & Hahn, M. Extended-connectivity fingerprints. J. Chem. Inf. Model. 50, 742-754 (2010).   
40 Durant, J. L., Leland, B. A., Henry, D. R. & Nourse, J. G. Reoptimization of MDL keys for use in drug discovery. J. Chem. Inf. Comput. Sci. 42, 1273-1280 (2002).

41 Landrum, G. RDKit Documentation. Release 1.4. Available at: https://www.rdkit.org/ (2013).   
42 Jaeger, S., Fülle, S. & Turk, S. Mol2vec: unsupervised machine learning approach with chemical intuition. J. Chem. Inf. Model. 58, 27-35 (2018).   
43 Ma, R., Liu, Z., Zhang, Q., Liu, Z. & Luo, T. Evaluating polymer representations via quantifying structure–property relationships. J. Chem. Inf. Model. 59, 3110-3119 (2019).   
44 Daulton, S., Balandat, M. & Bakshy, E. Parallel Bayesian optimization of multiple noisy objectives with expected hypervolume improvement. Adv. Neural Inf. Process. Syst. 34, 2187-2200 (2021).   
45 Zitzler, E. et al. Performance assessment of multiobjective optimizers: an analysis and review. IEEE Trans. Evol. Comput. 7, 117–132 (2003).   
46 Ertl, P. & Schuffenhauer, A. Estimation of synthetic accessibility score of drug-like molecules based on molecular complexity and fragment contributions. J. Cheminform. 1, 8 (2009).   
47 Oviedo, F., Ferres, J. L., Buonassisi, T. & Butler, K. T. Interpretable and explainable machine learning for materials science and chemistry. Acc. Mater. Res. 3, 597-607 (2022).   
48 Kunchapu, S. & Jablonka, K. M. PolyMetriX: an ecosystem for digital polymer chemistry. npj Comput. Mater. 11, 312 (2025).   
49 Huang, X., Ma, S., Zhao, C. Y., Wang, H. & Ju, S. Exploring high thermal conductivity polymers via interpretable machine learning with physical descriptors. npj Comput. Mater. 9, 191 (2023).   
50 Lundberg, S. M. & Lee, S.-I. A unified approach to interpreting model predictions. Adv. Neural Inf. Process. Syst. 30 (2017).   
51 Xu, Y., Wang, X., Zhou, J., Song, B. & Jiang, Z. et al. Molecular engineered conjugated polymer with high thermal conductivity. Sci. Adv. 4, eaar3031 (2018).   
52 Luo, T. et al. Molecular dynamics simulation of thermal energy transport in polydimethylsiloxane. J. Appl. Phys. 109, 073501 (2011).   
53 Ma, H. & Tian, Z. Chain rotation significantly reduces thermal conductivity of single-chain polymers. J. Mater. Res. 34, 126-133 (2019).   
54 Sugiyama, F., Kleinschmidt, A. T., Kayser, L. V., Rodriquez, D. & Finn, M. et al. Effects of flexibility and branching of side chains on the mechanical properties of low-bandgap conjugated polymers. Polym. Chem. 9, 4354-4363 (2018).   
55 Wang, Y., Li, Z., Niu, K., Xia, W. & Giuntoli, A. A molecular dynamics study of mechanical and conformational properties of conjugated polymer thin films. Macromolecules 57, 5130-5142 (2024).   
56 Ertl, P., Rohde, B. & Selzer, P. Fast calculation of molecular polar surface area as a sum of fragmentbased contributions and its application to the prediction of drug transport properties. J. Med. Chem. 43, 3714-3717 (2000).   
57 Wang, H., Liu, H., Cao, Z., Li, W. & Huang, X. et al. Room-temperature autonomous self-healing glassy polymers with hyperbranched structure. Proc. Natl Acad. Sci. USA 117, 11299-11305 (2020).   
58 Xie, X. et al. Thermal conductivity, heat capacity, and elastic constants of water-soluble polymers and polymer blends. Macromolecules 49, 972–978 (2016).   
59 Dobrynin, A. V. & Rubinstein, M. Theory of polyelectrolytes in solutions and at surfaces. Prog. Polym. Sci. 30, 1049–1118 (2005).   
60 Xu, C., Wang, D., Zhu, Z. et al. Understanding thermal transport in polymer semiconductors via two-

channel mechanism. Nat Commun 16, 11545 (2025).   
61 Zhou, Jingyi, et al. "Reduction of the Thermal Conductivity of Polyurethanes by Fluorination: Impact of Crystallinity, Atomic Density, and Sound Velocity." Angewandte Chemie (2025): e202503497.   
62 Ward, I. M. & Sweeney, J. Mechanical Properties of Solid Polymers. Vol. 313 (Wiley, 1971).   
63 Chen, T., Jiang, G., Li, G., Wu, Z. & Zhang, J. Poly(ethylene glycol-co-1,4-cyclohexanedimethanol terephthalate) random copolymers: Effect of copolymer composition and microstructure on the thermal properties and crystallization behavior. RSC Adv. 5, 60570-60580 (2015).   
64 Foster, A. B., Tamaddondar, M., Luque-Alled, J. M., Harrison, W. J. & Li, Z. et al. Understanding the topology of the polymer of intrinsic microporosity PIM-1: cyclics, tadpoles, and network structures and their impact on membrane performance. Macromolecules 53, 569-583 (2020).   
65 Ghanem, B. S., McKeown, N. B., Budd, P. M., Al-Harbi, N. M. & Fritsch, D. et al. Synthesis, characterization, and gas permeation properties of a novel group of polymers with intrinsic microporosity: PIM-polyimides. Macromolecules 42, 7881-7888 (2009).   
66 Budd, Peter M., et al. "Polymers of intrinsic microporosity (PIMs): robust, solution-processable, organic nanoporous materials." Chemical communications 2 (2004): 230-231.   
67 Budd, Peter M., Neil B. McKeown, and Detlev Fritsch. "Free volume and intrinsic microporosity in polymers." Journal of Materials Chemistry 15.20 (2005): 1977-1986.   
68 Fortunato, M. E. & Colina, C. M. pysimm: A python package for simulation of molecular systems. SoftwareX 6, 7-12 (2017).   
69 Wei, X. & Luo, T. Chain length effect on thermal transport in amorphous polymers and a structure– thermal conductivity relation. Phys. Chem. Chem. Phys. 21, 15523-15530 (2019).   
70 Vassetti, D., Pagliai, M. & Procacci, P. Assessment of GAFF2 and OPLS-AA general force fields in combination with the water models TIP3P, SPCE, and OPC3 for the solvation free energy of druglike organic molecules. J. Chem. Theory Comput. 15, 1983-1995 (2019).   
71 Plimpton, S. Fast parallel algorithms for short-range molecular dynamics. J. Comput. Phys. 117, 1-19 (1995).   
72 Kaviany, M. Heat Transfer Physics. (Cambridge University Press, 2014).   
73 Clavier, G., Desbiens, N., Bourasseau, E., Lachet, V. & Brusselle-Dupend, N. et al. Computation of elastic constants of solids using molecular simulation: comparison of constant volume and constant pressure ensemble methods. Mol. Simul. 43, 1413-1422 (2017).   
74 Akiba, T., Sano, S., Yanase, T., Ohta, T. & Koyama, M. Optuna: A next-generation hyperparameter optimization framework. Proc. 25th ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. 2623–2631 (2019).
