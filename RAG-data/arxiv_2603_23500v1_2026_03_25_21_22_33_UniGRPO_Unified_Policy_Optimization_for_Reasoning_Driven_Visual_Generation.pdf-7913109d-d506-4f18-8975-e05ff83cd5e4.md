# UniGRPO: Unified Policy Optimization for Reasoning-Driven Visual Generation

Jie Liu1,2∗ Zilyu $\forall \mathtt { e } ^ { 2 \ast }$ Linxiao Yuan2 Shenhan Zhu2 Yu Gao2 Jie $\boldsymbol { \mathsf { W } } \boldsymbol { \mathsf { U } } ^ { 2 \ddagger }$ Kunchang Li2 Xionghui Wang2 Xiaonan Nie2 Weilin Huang2§ Wanli Ouyang1

1The Chinese University of Hong Kong, 2ByteDance Seed

∗Equal contribution, ‡Project lead, §Corresponding author

# Abstract

Unified models capable of interleaved generation have emerged as a promising paradigm, with the community increasingly converging on autoregressive modeling for text and flow matching for image generation. To advance this direction, we propose a unified reinforcement learning framework tailored for interleaved generation. We validate our approach on its fundamental unit: a single round of reasoning-driven image generation, where the model first expands the user prompt through reasoning, followed by image synthesis. Formulating this multimodal generation process as a Markov Decision Process with sparse terminal rewards, we introduce UniGRPO to jointly optimize text and image generation policies using GRPO. Adopting a minimalist methodology to avoid over-design, we leverage established training recipes for both modalities by seamlessly integrating standard GRPO for reasoning and FlowGRPO for visual synthesis. To ensure scalability to multiround interleaved generation, we introduce two critical modifications to the original FlowGRPO: (1) eliminating classifier-free guidance to maintain linear, unbranched rollouts, which is essential for scaling to complex scenarios involving multi-turn interactions and multi-condition generation (e.g., editing); and (2) replacing the standard latent KL penalty with an MSE penalty directly on the velocity fields, providing a more robust and direct regularization signal to mitigate reward hacking effectively. Our experiments demonstrate that this unified training recipe significantly enhances image generation quality through reasoning, providing a robust and scalable baseline for the future post-training of fully interleaved models.

# 1 Introduction

The evolution of generative AI is rapidly progressing toward unified multimodal models [1–5] capable of interleaved generation [6]. A pivotal advantage of this emerging paradigm is the potential to effectively leverage test-time compute through iterative reasoning — refining prompts, generating images, and reflecting on outputs across multiple rounds to tackle complex image synthesis tasks [7]. As the boundaries between modalities blur, the community is increasingly gravitating toward a robust architectural synergy: Autoregressive (AR) [8] models for text generation paired with Flow Matching [9, 10] for visual synthesis [1, 4–6]. This combination harnesses the reasoning capabilities of Large Language Models (LLMs) alongside the high-fidelity generation strengths of Flow-based models.

In this work, we argue that advancing interleaved generation requires a unified Reinforcement Learning (RL) framework that jointly optimizes text and image generation policies. Rather than immediately scaling to long-horizon multi-turn generation, we validate our framework on its fundamental unit: a single round of

图片摘要：该图主要展示 1 Overview of UniGRPO. By formulating interleaved generation。
![](images/cef4a952a3930a9140fd95df100ab465a3379a03edaade0d1aae92c0594dc044.jpg)  
Figure 1 Overview of UniGRPO. By formulating interleaved generation as a joint MDP, this illustration demonstrates how UniGRPO jointly optimizes discrete language actions ( $_ { y k }$ ) in the LLM’s next-token prediction, and continuous visual actions $\left( \boldsymbol { x } _ { t _ { k } - \Delta t } \right)$ in flow matching. Both policies are updated using group-relative advantages derived from sparse terminal rewards.

reasoning-driven image generation. This setting already encompasses both text and image generation, covering the essential components of interleaved generation. In the absence of open-source base models natively capable of full interleaved generation, it serves as a meaningful and principled testbed for validating our unified RL framework.

To this end, we propose UniGRPO, a unified RL framework formulating the entire "Prompt Thinking → Image" sequence as a single Markov Decision Process (MDP) [11]. Adopting a minimalist methodology to avoid over-design, we integrate established training recipes for both modalities: standard GRPO [12] for the reasoning component and FlowGRPO [13] for visual synthesis. Under sparse terminal rewards, UniGRPO jointly optimizes both text and image generation policies, encouraging the model to produce more informative reasoning texts while simultaneously improving the visual synthesis process itself.

Crucially, our design choices are driven by the goal of scalability to future multi-round and multi-condition scenarios (e.g., complex editing tasks). We introduce two critical modifications to the standard Flow Matching RL training recipe within our framework. First, we eliminate Classifier-Free Guidance (CFG) [14] during training. While CFG is a standard inference technique, its removal ensures that the generation process remains a linear, unbranched rollout, which is essential for scaling to complex scenarios involving multi-turn interactions and multi-condition generation. Second, we replace the standard latent KL penalty with an MSE penalty directly on the velocity fields. This provides a more robust and direct regularization signal that effectively mitigates reward hacking, ensuring the optimization remains well-grounded. Our contributions can be summarized as follows:

• Unified RL Framework for Reasoning-Driven Image Generation: We propose UniGRPO, a minimalist framework that formulates the Prompt $\longrightarrow$ Thinking Image sequence as a single MDP, jointly optimizing AR text and flow-matching image policies. We validate this framework on the fundamental unit of interleaved generation, demonstrating that jointly optimizing reasoning and visual synthesis improves image generation quality.

# Prompts

A cloud in the shape of a teacup

图片摘要：该图片与UniGRPO；Mona Lisa, sketch这部分内容相关。
![](images/6117fef26657c9ce6de5cf6e0b5ac2e1db48ac03302d0cda99f0ffe3eeb917f4.jpg)

图片摘要：该图片与UniGRPO；Mona Lisa, sketch这部分内容相关。
![](images/00ebf9a286fa95c3db6df292db0c587cb158d0597bcb8741c40c89e3f8ce25ef.jpg)  
SFT

图片摘要：该图片与UniGRPO；Mona Lisa, sketch这部分内容相关。
![](images/1a9f0d3e169136aea6ab9e3094fc25a44a11bf3a1046a83c9a40c85d99006b32.jpg)  
UniGRPO

Mona Lisa, sketch

图片摘要：该图片与There are three podiums. On the surface of the tallest podium in the middle, the这部分内容相关。
![](images/384758530d0291d07233bb53b6dad2cb85d04369dda9e0c52f98c4ff8cedeaf8.jpg)

图片摘要：该图片与There are three podiums. On the surface of the tallest podium in the middle, the这部分内容相关。
![](images/36dfbd5f59edbf6d395b8d4b4c92575d135df90cc1cea14581232c453bab39f7.jpg)

图片摘要：该图片与There are three podiums. On the surface of the tallest podium in the middle, the这部分内容相关。
![](images/e4a4c8e14361f41530f70869c096ec6f3f1539b7a48daaed00a5c5509f15d840.jpg)

There are three podiums. On the surface of the tallest podium in the middle, the number "1" is written. Next is the podium on the right side with the number "2" written on it. The podium on the left side is the shortest, and the number "3" is written on its surface.

图片摘要：该图片与A Border Collie wearing a worker's helmet and holding a wrench in its mouth, and这部分内容相关。
![](images/be5db43ea3025f6fdbb7f090f1166bb138eca3cbe29b728c6defc33c555e4c8e.jpg)

图片摘要：该图片与A Border Collie wearing a worker's helmet and holding a wrench in its mouth, and这部分内容相关。
![](images/9ed4384e20981135fa6947cfd6585704096ea405ac1a19bbe9a913870488b357.jpg)

图片摘要：该图片与A Border Collie wearing a worker's helmet and holding a wrench in its mouth, and这部分内容相关。
![](images/75312fb8e7763dff67febe47a1c4f8afd2edbc2d0f5e61df566f3d7c59abb6ee.jpg)

A Border Collie wearing a worker's helmet and holding a wrench in its mouth, and a Corgi wearing a yellow-green checked sweater, are jumping and playing in the square.

图片摘要：该图片与A rabbit, a hedgehog, and a turtleA Border Collie wearing a worker's helmet and 这部分内容相关。
![](images/021cfc2824e67c211ca39314eabf7cc2b2d62959db77174525bf7667a950b307.jpg)

图片摘要：该图片与A rabbit, a hedgehog, and a turtleA Border Collie wearing a worker's helmet and 这部分内容相关。
![](images/1654a6d700a485cf7a00e208055ca079cc8b6343b2a145cf926d96bba4767aa8.jpg)

图片摘要：该图片与A rabbit, a hedgehog, and a turtleA Border Collie wearing a worker's helmet and 这部分内容相关。
![](images/35f31f8d7efa2fc4ebe6b11951eaacaa270156690a4239ee11d267b7e267c130.jpg)

A rabbit, a hedgehog, and a turtle.

图片摘要：该图片与Figure 2 T2I qualitative comparison；• Scalable Flow Matching RL Adaptations: We 这部分内容相关。
![](images/b240aba46e1b9d1997714fb3887b50ff364efa75667410fcf6b0a67445232835.jpg)

图片摘要：该图片与Figure 2 T2I qualitative comparison；• Scalable Flow Matching RL Adaptations: We 这部分内容相关。
![](images/da85cdc596384c11cb5683f19e4e6c40bb9d34737f423dfaa00f04b7e90339df.jpg)

图片摘要：该图片与Figure 2 T2I qualitative comparison；• Scalable Flow Matching RL Adaptations: We 这部分内容相关。
![](images/e3959dadcf6f7114e6acfb6f1bbf34807c188dcaa6027a32cba3f171583a6f93.jpg)  
Figure 2 T2I qualitative comparison.

• Scalable Flow Matching RL Adaptations: We introduce two critical modifications to FlowGRPO: eliminating CFG to ensure unbranched rollouts, and replacing the standard latent KL penalty with an MSE penalty directly on the velocity fields for more robust reward hacking mitigation. Together, these adaptations are essential for scaling to multi-turn and multi-condition generation scenarios.   
• We demonstrate that our unified training recipe effectively optimizes the model under sparse terminal rewards, establishing a robust and scalable baseline for future post-training of fully interleaved models.

# 2 Related Work

# 2.1 RL for LLMs

Recent LLM advancements rely on Reinforcement Learning (RL) for alignment and reasoning. While PPO [15] is a standard approach, the highly efficient Group Relative Policy Optimization (GRPO) [12] eliminates the value model by using group-relative baselines. This efficiency drives reasoning-intensive models using Chain-of-Thought (CoT) [16], such as DeepSeek-R1. Our work adapts GRPO to efficiently optimize the intermediate "thinking" tokens prior to visual synthesis.

# 2.2 RL for Diffusion and Flow Matching Models

Aligning text-to-image (T2I) models with human intent has been extensively explored, primarily through reward-driven optimization [17–20] and Reward Weighted Regression (RWR) [21–24]. Currently, Direct Preference Optimization (DPO) [25–34] and PPO-style policy gradients [15, 35–39] have become standard frameworks for fine-tuning diffusion models, alongside various training-free guidance methods [40–42]. However, adapting these established RL paradigms to the deterministic ODEs of modern flow matching architectures requires specific stochastic formulations. To address this, FlowGRPO [13] and DanceGRPO [43] introduce a method to apply policy gradients to flow models by reformulating the generation process into a stochastic SDE. Subsequently, several works [44–57] have further improved upon FlowGRPO by enhancing training stability, reward design, or sample efficiency. Building on this line of work, our work extends the RL framework to jointly optimize both language reasoning and visual synthesis.

# 2.3 Unified Multimodal Understanding and Generation Models

Multimodal understanding and image generation have long evolved independently, with autoregressive models dominating the former and diffusion models the latter. Recent work seeks to unify both capabilities within a single framework. One line of research applies vector quantization to visual signals so that image and text tokens share a unified autoregressive training space, as in Chameleon [58], Emu3 [59], and VILA-U [60]. Another line combines autoregressive and diffusion objectives: Show-o [4] and Transfusion [5] train a single transformer with mixed next-token prediction and diffusion losses, while Bagel [1] and Mogao [6] further scale this hybrid paradigm with large-scale interleaved multimodal data, demonstrating strong emerging capabilities in complex reasoning and coherent interleaved text-image generation. As surveyed by Zhang et al. [3], key challenges remain in tokenization strategy, cross-modal attention design, and training data construction.

# 2.4 Concurrent Work

Concurrent with our work, several studies independently apply RL to unified or joint multimodal generation. R3 [61] proposes a generate-understand-regenerate loop to mitigate the understanding-generation trade-off, but validates on benchmark-specific prompts rather than general-purpose training. DualGRPO [62] jointly optimizes a separate LLM model and diffusion backbone via a tree-structured rollout, yet this design is incompatible with true interleaved multimodal generation. PromptRL [63] similarly trains disjoint language and flow models in a joint RL loop, but on limited training datasets. SepGRPO [64] is also built on BAGEL and proposes alternating RL between the MLLM and DiT modules, but the two components are trained separately rather than jointly optimized end-to-end. In contrast, our method is built on a single unified model, trained with general-purpose prompts at 1024 resolution, with a scalable algorithm design built upon an improved FlowGRPO. We further provide comprehensive comparisons against a wide range of diffusion RL baselines, yielding broader and more robust performance gains across diverse benchmarks.

# 3 Preliminary

In this section, we establish the theoretical foundations for optimizing generative policies using Unified Group Relative Policy Optimization (UniGRPO), covering both discrete text generation and continuous flow-based visual generation.

# 3.1 Text GRPO

For the autoregressive text component, we adopt the standard GRPO [12] formulation. Given a prompt $c$ , the policy $\pi \theta$ generates a group of $G$ outputs $\{ y _ { i } \} _ { i = 1 } ^ { G }$ . The optimization objective maximizes the expected reward while constraining the policy update via importance sampling clipping.

The advantage for the $i$ -th sample is computed relatively within the group:

$$
\hat {A} _ {i} = \frac {R _ {i} - \operatorname {m e a n} \left(\left\{R _ {j} \right\} _ {j = 1} ^ {G}\right)}{\operatorname {s t d} \left(\left\{R _ {j} \right\} _ {j = 1} ^ {G}\right)}. \tag {1}
$$

The objective function is defined as:

$$
\mathcal {J} _ {\mathrm {T e x t}} (\theta) = \frac {1}{G} \sum_ {i = 1} ^ {G} \frac {1}{| y _ {i} |} \sum_ {k = 1} ^ {| y _ {i} |} \left(\min  \left(r _ {i, k} \hat {A} _ {i}, \operatorname {c l i p} \left(r _ {i, k}, 1 - \epsilon , 1 + \epsilon\right) \hat {A} _ {i}\right) - \beta_ {\mathrm {t x t}} D _ {\mathrm {K L}} \left(\pi_ {\theta} \| \pi_ {\mathrm {r e f}}\right)\right), \tag {2}
$$

where $\begin{array} { r } { r _ { i , k } = \frac { \pi _ { \theta } \left( y _ { i , k } | y _ { i , < k } \right) } { \pi _ { \theta _ { \mathrm { o l d } } } \left( y _ { i , k } | y _ { i , < k } \right) } } \end{array}$ πθ(yi,k|yi,<k) denotes the importance ratio at step $k$ .

# 3.2 Flow GRPO

For the visual component, we utilize FlowGRPO [13], which adapts reinforcement learning to flow matching models by converting the deterministic Ordinary Differential Equation (ODE) into a Stochastic Differential Equation (SDE) to enable exploration.

SDE Sampling. To introduce the necessary stochasticity for RL exploration, the sampling process is formulated as:

$$
\Delta x _ {t _ {k}} = \left[ v _ {\theta} \left(x _ {t _ {k}}, t _ {k}\right) + \frac {\sigma_ {t _ {k}} ^ {2}}{2 t _ {k}} \left(x _ {t _ {k}} + \left(1 - t _ {k}\right) v _ {\theta} \left(x _ {t _ {k}}, t _ {k}\right)\right) \right] \Delta t + \sigma_ {t _ {k}} \sqrt {\Delta t} \epsilon , \tag {3}
$$

where $\sigma _ { t _ { k } }$ controls the noise level and $\epsilon \sim \mathcal { N } ( 0 , I )$ . For training efficiency, we adopt the FlowGRPO-Fast variant [13], which employs a hybrid sampling strategy. Specifically, denoising steps within a continuous time window are performed via SDE and optimized with gradient tracking, while the remaining steps follow standard ODE sampling without gradient computation. This significantly reduces computational overhead while preserving optimization effectiveness.

Mitigating Reward Hacking via RatioNorm. Standard importance-ratio clipping often fails in diffusion models because the distribution of importance ratios

$$
r _ {t _ {k}} (\theta) = \frac {p _ {\theta} \left(x _ {t _ {k} - \Delta t} \mid c , y , x _ {t _ {k}} , t _ {k}\right)}{p _ {\theta_ {\text {o l d}}} \left(x _ {t _ {k} - \Delta t} \mid c , y , x _ {t _ {k}} , t _ {k}\right)}, \tag {4}
$$

is systematically left-shifted (mean $< 1$ ) and exhibits inconsistent variance across timesteps [65]. This prevents the clipping mechanism from constraining overconfident positive updates, leading to severe reward hacking. To address this, we adopt the Ratio Normalization (RatioNorm) proposed in GRPO-Guard [65]. This method standardizes the log-importance ratio to center its distribution around zero, thereby restoring the effectiveness of the clipping bounds:

$$
\log \tilde {r} _ {t _ {k}} (\theta) = \sigma_ {t _ {k}} \sqrt {\Delta t} \left(\log r _ {t _ {k}} (\theta) + \frac {\| \Delta \mu_ {\theta} (x _ {t _ {k}} , t _ {k}) \| ^ {2}}{2 \sigma_ {t _ {k}} ^ {2} \Delta t}\right), \tag {5}
$$

where $\Delta \mu _ { \boldsymbol { \theta } } ( x _ { t _ { k } } , t _ { k } ) \triangleq \mu _ { \boldsymbol { \theta } _ { \mathrm { o l d } } } ( x _ { t _ { k } } , t _ { k } ) - \mu _ { \boldsymbol { \theta } } ( x _ { t _ { k } } , t _ { k } )$ is the mean drift between the current and reference policies.

Combining the hybrid SDE sampling strategy with the RatioNorm mechanism, the final FlowGRPO objective is computed exclusively over the SDE timestep subset $\tau _ { \mathrm { S D E } }$ :

$$
\mathcal {J} _ {\mathrm {F l o w}} (\theta) = \frac {1}{G} \sum_ {i = 1} ^ {G} \frac {1}{| \mathcal {T} _ {\mathrm {S D E}} |} \sum_ {t _ {k} \in \mathcal {T} _ {\mathrm {S D E}}} \left(\min  \left(\tilde {r} _ {i, t _ {k}} \hat {A} _ {i}, \operatorname {c l i p} \left(\tilde {r} _ {i, t _ {k}}, 1 - \epsilon , 1 + \epsilon\right) \hat {A} _ {i}\right) - \beta_ {\mathrm {i m g}} D _ {\mathrm {K L}} \left(\pi_ {\theta} \| \pi_ {\mathrm {r e f}}\right)\right), \tag {6}
$$

where $| \mathcal { T } _ { \mathrm { S D E } } |$ denotes the number of denoising steps within the continuous SDE window.

# 4 Method

Building upon these foundations, we propose UniGRPO, a unified framework that jointly optimizes multimodal generation policies within a single reinforcement learning loop.

# 4.1 Multimodal Generation as a Markov Decision Process

We formulate interleaved generation as a sequential MDP $( \cal { S } , \cal { A } , \cal { P } , \cal { R } )$ , where each MDP step $k$ corresponds to a single token prediction during the text phase and a single denoising step during the image phase.

• State Space $s$ : The state evolves through two phases. In the text phase, $s _ { k } ^ { \mathrm { t x t } } = ( c , ~ y _ { < k } )$ comprises the input prompt $c$ and all previously generated reasoning tokens $y _ { < k }$ . In the image phase, $s _ { k } ^ { \mathrm { i m g } } =$ $( c , \ y , \ x _ { t _ { k } } , \ t _ { k } )$ includes the prompt, the completed reasoning trace $y$ , the noisy image latent $x _ { t _ { k } }$ , and the current flow time $t _ { k }$ .   
• Action Space $\mathcal { A } \colon$ In the text phase, $a _ { k } ^ { \mathrm { t x t } } \in \mathcal { V }$ is a single token drawn from the vocabulary. In the image phase, aimgk = xtk−∆t ∈ Rd is the denoised latent at the next flow step. $a _ { k } ^ { \mathrm { i m g } } = x _ { t _ { k } - \Delta t } \in \mathbb { R } ^ { d }$   
• Transition $P$ : Both phases are deterministic given the action: the text transition appends $a _ { k } ^ { \mathrm { t x t } }$ to the token sequence, while the image transition advances the latent from $x _ { t _ { k } }$ to $x _ { t _ { k } - \Delta t }$ .   
• Reward R: A sparse terminal reward $R ( x _ { 0 } , c )$ is assigned only after the image latent has been fully denoised to $x _ { 0 }$ ; all intermediate steps receive zero reward.

# 4.2 UniGRPO Framework

Given a unified model $\pi _ { \theta }$ that performs interleaved generation, UniGRPO models the entire generation process as a MDP and optimizes it through group relative policy optimization. Specifically, for a given prompt $c$ , we first sample i=1 kmodel to generate a corresponding image trajectory $G$ reasoning chains $\{ y _ { i } \} _ { i = 1 } ^ { G }$ via $\pi _ { \boldsymbol { \theta } } \big ( a _ { k } ^ { \mathrm { t x t } } \ \big | \ s _ { k } ^ { \mathrm { t x t } } \big )$ $\{ x _ { i } \} _ { i = 1 } ^ { G }$ . Each reasoning chain then conditions the same via $\pi _ { \boldsymbol { \theta } } ( a _ { k } ^ { \mathrm { i m g } } \mid s _ { k } ^ { \mathrm { i m g } } )$ with a hybrid SDE-ODE integrator. We compute group-relative advantages ${ \hat { A } } _ { i }$ based on the terminal rewards of the completed multimodal trajectories. These advantages are used to update $\pi \theta$ through a unified objective:

$$
\mathcal {J} = \mathcal {J} _ {\text {T e x t}} + \lambda \mathcal {J} _ {\text {F l o w}}, \tag {7}
$$

where $\lambda$ is a hyperparameter controlling the relative weight of the image generation objective. To equally balance the reasoning and synthesis tasks, we simply set $\lambda = 1$ across all our experiments. To ensure scalability to multi-round interleaved generation, we introduce two critical modifications to the training recipe.

Eliminating Classifier-Free Guidance. Standard flow matching inference typically relies on CFG to enhance prompt adherence, requiring two model evaluations per step (conditional and unconditional). Crucially, this computational burden scales with the number of conditions; for multi-condition generation such as image editing, CFG demands at least three evaluations per step. Furthermore, this complexity compounds in multi-round interleaved generation, where the system must continuously manage and branch multiple conditional contexts across alternating text and image phases. In an RL setting, this multiplication of function evaluations and context branches drastically inflates computational and memory costs, while creating a branched computation graph that severely complicates gradient estimation. We therefore train UniGRPO entirely without CFG, enforcing a linear, unbranched rollout. While removing CFG typically degrades prompt adherence, our framework compensates for this during training. By explicitly maximizing the expected reward—which evaluates text-image alignment and visual quality—we internalize the alignment capabilities directly into the policy weights. This establishes a highly efficient pipeline that naturally scales to complex multi-condition, multi-round interaction generation.

Velocity-Based Regularization. Preventing reward hacking is a primary challenge in RL for visual generation. In the above SDE formulation, the step-wise transition probabilities are Gaussian, meaning the exact local KL divergence in the latent space can be analytically computed. Specifically, this exact KL evaluates to

the squared difference in predicted velocities, weighted by the inverse noise variance $( 1 / \sigma _ { t _ { k } } ^ { 2 } )$ ). However, this inherent weighting applies an uneven penalty across the generative trajectory. For instance, at timesteps with high noise variance, the KL penalty becomes excessively small. This inconsistency creates temporal vulnerabilities that the RL optimizer can easily exploit. To achieve a more robust and consistent constraint, we drop this timestep-dependent weighting and apply a Mean Squared Error (MSE) penalty directly on the unweighted velocity fields:

$$
\mathcal {L} _ {\mathrm {M S E}} (\theta) = \left\| v _ {\theta} \left(x _ {t _ {k}}, t _ {k}, y\right) - v _ {\text {r e f}} \left(x _ {t _ {k}}, t _ {k}, y\right) \right\| ^ {2}. \tag {8}
$$

This unweighted formulation explicitly forces the RL-tuned vector field to remain close to the pre-trained reference model uniformly across all noise levels. Empirically, we find that this uniform regularization leaves fewer loopholes for policy exploitation, proving significantly more effective at mitigating reward hacking while safely preserving the base model’s generative priors.

# 5 Experiments

This section presents the empirical validation of the proposed UniGRPO framework. We begin by outlining the experimental setup—including the pretrained model, reward formulation, baselines, and evaluation protocols. Detailed hyperparameter settings are deferred to Appendix 3. Following this, we compare UniGRPO against strong baselines and conclude with ablation studies to evaluate critical design choices.

# 5.1 Experimental Settings

The Pretrained Model. As a preliminary exploration into reinforcement learning for interleaved generation, we require a backbone capable of handling mixed-modal outputs. We adopt Bagel [1], a model architecture with inherent interleaved generation potential. However, we observed that the vanilla Bagel exhibits limited instruction-following capabilities and suboptimal image generation quality. To establish a strong baseline, we performed Supervised Fine-Tuning (SFT) on Bagel using a curated internal dataset. This process significantly boosted performance (see Table 1). Unless otherwise stated, all subsequent baselines and experiments utilize this finetuned Bagel as the starting checkpoint.

Reward Model. A key advantage of the GRPO algorithm is its flexibility; it does not require differentiable reward functions, allowing the integration of black-box verifiers or VLM-based feedback. However, to ensure a fair comparison with gradient-based baselines like ReFL [19] (which necessitates differentiable rewards), we utilize a differentiable reward formulation for the main experiments. Specifically, we employ the exact same reward model as utilized in RewardDance [66]. This model is fine-tuned based on InternVL [67] using collected user preference data, explicitly designed to measure the consistency between generated images and user prompts. It is important to note that while ReFL is restricted to such differentiable objectives, UniGRPO is compatible with a broader range of verifier-based rewards.

Baselines. ReFL directly fine-tunes diffusion models by viewing reward model scores as human preference losses and back-propagating gradients to a randomly-picked late timestep t. ReFL w/ Thinking generates thinking prompts during training and optimizing only the image generation part using the ReFL objective. ReFL $^ +$ TextGRPO follows a two-stage paradigm: initializing from the trained ReFL w/ Thinking checkpoint and subsequently optimizing the text generation module using TextGRPO. FPO / AWR [68, 69] serves as an alternative to FlowGRPO. Unlike FlowGRPO which introduces SDE perturbations for exploration, FPO utilizes the forward process to obtain $x _ { t }$ and uses the Evidence Lower Bound (ELBO) of the denoising process as a surrogate for $\log p _ { \theta } ( x _ { 0 } | c )$ to compute importance sampling weights. UniFPO denotes a unified framework analogous to UniGRPO, where the text component is optimized via TextGRPO and the image synthesis component is trained using the FPO objective.

Evaluation Metrics. We employ two benchmarks to evaluate generation quality and prompt alignment:

• Text Alignment (TA) Benchmark: Our internal evaluation set consisting of 150 diverse prompts. For each prompt, we generate 4 images. Evaluation is performed by a VLM, which assesses the outputs against multiple specific exam points defined for each prompt. Each exam point receives a binary score

Table 1 Main results on TA and GenEval. All RL methods start from the Bagel checkpoint after SFT. “Thinking” denotes whether the method explicitly generates intermediate reasoning tokens. − indicates training collapse.   

<table><tr><td>Model / Method</td><td>Thinking</td><td>TA Score</td><td>GenEval</td></tr><tr><td>Bagel</td><td>×</td><td>0.6810</td><td>0.78</td></tr><tr><td>Bagel</td><td>✓</td><td>0.7132</td><td>0.79</td></tr><tr><td>SFT</td><td>×</td><td>0.7486</td><td>0.83</td></tr><tr><td>SFT</td><td>✓</td><td>0.7769</td><td>0.82</td></tr><tr><td>ReFL</td><td>×</td><td>0.7786</td><td>0.85</td></tr><tr><td>ReFL</td><td>✓</td><td>0.8120</td><td>0.84</td></tr><tr><td>FPO</td><td>×</td><td>0.7893</td><td>0.87</td></tr><tr><td>FPO</td><td>✓</td><td>0.8159</td><td>0.85</td></tr><tr><td>FlowGRPO</td><td>×</td><td>0.8112</td><td>0.88</td></tr><tr><td>FlowGRPO</td><td>✓</td><td>0.8208</td><td>0.86</td></tr><tr><td>TextGRPO</td><td>✓</td><td>0.8078</td><td>0.88</td></tr><tr><td>ReFL (w/ Thinking)</td><td>✓</td><td>0.7804</td><td>0.83</td></tr><tr><td>ReFL (w/ Thinking) + TextGRPO</td><td>✓</td><td>0.7987</td><td>0.87</td></tr><tr><td>UniFPO</td><td>✓</td><td>-</td><td>-</td></tr><tr><td>UniGRPO (Ours)</td><td>✓</td><td>0.8381</td><td>0.90</td></tr></table>

(1 for correct, 0 for incorrect), and the score for a single image is calculated as the average score across all its associated exam points. The final reported metric is the overall average score across all evaluated images. We refer to RewardDance [66] for further details on this scoring mechanism.

• GenEval [70]: A standard benchmark assessing Text-to-Image models on complex compositional capabilities, including object counting, spatial relations, and attribute binding.

# 5.2 Main Results

We begin by analyzing the learning dynamics of UniGRPO, presenting the training and validation reward curves in Figure 3 alongside qualitative generation examples in Figure 2. Next, we benchmark our framework against several established baselines: ReFL, FPO, FlowGRPO, TextGRPO, and hybrid approaches. The quantitative comparisons are summarized in Table 1.

Benchmark Performance. The results in Table 1 indicate that SFT significantly improves the base capabilities of Bagel. Among the RL methods, UniGRPO achieves state-of-the-art performance, scoring 0.8381 on TA and 0.90 on GenEval. Notably, UniFPO failed to converge, underscoring the stability advantages of our GRPObased formulation. The comparison between UniGRPO, FlowGRPO, and TextGRPO confirms that jointly optimizing both the reasoning and synthesis policies yields gains superior to optimizing either component in isolation. Furthermore, we observe that enabling the explicit reasoning chain ("Thinking") on the Bagel model does not consistently improve GenEval scores. As noted by the Bagel authors, their reasoning module is primarily trained for knowledge-based reasoning and may not be ideally suited for short prompt rewriting tasks found in benchmarks like GenEval 1. However, our UniGRPO framework successfully leverages the reasoning chain to achieve SOTA performance. Please see Appendix A.1 for the detailed metrics of GenEval.

Qualitative Analysis. As illustrated in Figure 2, the original Bagel tends to generate images with oversaturated colors and noticeable synthetic artifacts. While SFT helps mitigate these synthetic artifacts, it compromises image sharpness, resulting in noticeable blurriness upon close inspection. Overcoming this limitation, our proposed UniGRPO significantly enhances both aesthetic quality and text-image alignment, yielding photorealistic, finely detailed images that faithfully reflect complex user prompts. Beyond visual quality, we analyze the models’ internal reasoning processes in Figures 6, 7 & 8. Note that during SFT, we standardized Bagel’s original <think> format to align with prevalent LLM conventions. While the base Bagel and SFT

图片摘要：该图主要展示 3 Training and Validation reward curves of UniGRPO on the Fi。
![](images/4792b5cc0e7693c4bdd498f66a2a8e765cfa3012243dc7e3fbd82133b05cdf4b.jpg)  
Figure 3 Training and Validation reward curves of UniGRPO on the Finetuned Bagel base model at a resolution of 1024. The x-axis represents the gradient update steps.

models generate detailed reasoning texts, these traces can sometimes lose focus or become disconnected from the core visual generation task. In contrast, UniGRPO optimizes the reasoning phase to be highly purposeful and task-oriented. By explicitly aligning the thought process with the final visual reward, UniGRPO produces reasoning traces that tightly couple with and effectively guide the subsequent image synthesis.

# 5.3 Ablation Study

We conduct ablation studies to validate our specific architectural and training decisions, including the removal of CFG and the choice of KL regularization.

Impact of CFG-Free Training. We compared training UniGRPO with and without CFG. As shown in Figure 4, although CFG during training yields images with higher rewards, removing CFG results in comparable or better final performance when evaluated with CFG. This confirms that CFG is unnecessary for RL-based alignment, rendering the computationally expensive branched CFG rollouts unnecessary during training.

图片摘要：该图主要展示 4 Ablation Study on CFG. Removing CFG during training yields。
![](images/017faab1cc6c3ebf8cb21ba6888812b56a641ea16705b98e1eb3a6b6f44bcc45.jpg)  
Figure 4 Ablation Study on CFG. Removing CFG during training yields comparable or superior performance, showing that CFG is unnecessary for RL-based training. Note that CFG is applied at evaluation for all settings. Furthermore, these results are not directly comparable to the curves in Figure 3, as this ablation uses the original Bagel as the base model at a resolution of 512.

图片摘要：该图主要展示 4 Ablation Study on CFG. Removing CFG during training yields。
![](images/e36a46f98d00ddd02ea5c8e266e50dd9dd9acb2197dd109c45cbeba27289658c.jpg)

图片摘要：该图主要展示 4 Ablation Study on CFG. Removing CFG during training yields。
![](images/9ac07de6e7313fa4d5c6f36f3d5d072bf1d460a76e7dd2490a70865fe0eb430b.jpg)

图片摘要：该图主要展示 4 Ablation Study on CFG. Removing CFG during training yields。
![](images/25daf61ca121a0d4a31f30783ec90eddd1258df3c35e6a1902b086886a768d30.jpg)  
Figure 5 Ablation Study on Regularization Strategies. From left to right: training reward, validation reward, and images generated under three different regularization strategies. Without regularization, the validation reward drops after an initial increase, leading to unnatural, oversaturated textures in the generated images. For KL divergence on the latents, the significant drop in training reward indicates that a sufficiently large KL coefficient has been used, yet grid-like artifacts still emerge as early as step 250, prompting us to terminate this run early. In contrast, directly applying MSE regularization on the velocity field ensures stable training dynamics and produces high-fidelity images with realistic textures.

Regularization Strategies. Preventing reward hacking is critical in RL. We compared three strategies: (1) No KL, (2) Latent KL (standard practice), and (3) Velocity MSE (Ours). As shown in Figure 5, removing KL leads to reward hacking where metrics are high but quality degrades. Velocity MSE achieves the best balance, constraining the vector field to the reference model while maintaining strong generation performance.

# 6 Conclusion and Future Work

In this work, we presented UniGRPO, a unified reinforcement learning framework designed to align interleaved text-and-image generation models. By formulating the multimodal generation process as an MDP, we successfully integrated autoregressive reasoning and flow-based visual synthesis into a single optimization loop. Our minimalist approach establishes a scalable training recipe by eliminating CFG to enforce linear rollouts and employing velocity-based regularization to mitigate reward hacking. Empirically, we demonstrated that UniGRPO effectively enhances image generation quality through chain-of-thought reasoning, providing a scalable baseline for future post-training of fully interleaved models. We identify two promising directions to extend this framework:

Scaling to Multi-Round Interleaved Generation. While this work validates UniGRPO on single-round generation (Prompt Reasoning Image), the unified MDP formulation naturally extends to multi-turn interactions. Future work will apply UniGRPO to complex scenarios such as interactive image editing, visual storytelling, and multi-turn dialogue. In these settings, the model must maintain context consistency across long horizons, where our CFG-free, linear rollout strategy is expected to offer significant computational advantages and training stability.

Multimodal Process Reward Modeling. Currently, UniGRPO relies on sparse terminal rewards evaluated solely on the final generated image. This can lead to inefficient credit assignment, where the model may generate high-quality images despite flawed reasoning. A critical future direction is to introduce Multimodal Process Reward Models (PRMs) that provide dense feedback on the intermediate reasoning steps. By verifying whether the generated "thoughts" are logically sound and aligned with the visual intent before the image is generated, we can further improve the sample efficiency of RL training and ensure better interpretability of the model’s decision-making process.

Six cups are arranged in two rows, with three in each row, viewed from above.

<think> The goal is to depict six cups neatly spaced in two horizontal rows of three when seen overhead. Proper alignment and perspective matching are all that change here; no alterations to objects or scene. </think>A neatly arranged overhead view shows exactly six identical cups evenly spaced in two clear horizontal rows, each containing three cups directlyaligned side by side under uniform lighting for accurate overhead perspective. render each cup as simple ceramic or similar with no clutter nearby to fulfill the specified arrangement from above as described.

图片摘要：该图片与A boy is holding a piece of wood, and a girl is drawing on it with a pen；The mod这部分内容相关。
![](images/d732092c467c4ea4759c0fa860c36aac92ee2bb75b16f5230787f82291c3ea00.jpg)

A boy is holding a piece of wood, and a girl is drawing on it with a pen.

<think> The model appropriately shows the boy gripping wood while the girl writing on it with a pen; accurate; no alterations are necessary.

</think>A young boy gently holds a flat piece of wood horizontally with both hands while a girl skillfully draws designs on the wood’s surface using a pen. render scene softly lit indoors with both subjects centered, accurately depicting their actions as described without changing details.

图片摘要：该图片与A large cat climbing frame has three platforms. On the three platforms, there is这部分内容相关。
![](images/24baa589ad087b98945c0967cef9a5c42019d2752f72ab72cad5d524f372ef52.jpg)

A large cat climbing frame has three platforms. On the three platforms, there is a cat, a dog and a mouse lying respectively.

<think> The goal is to depict a cat on one platform, a dog on another, and a mouse on the third with no changes; accurate positioning of each animal on their spots correctly matches the scene described.

</think>A sleek large house cat comfortably lying on its stomach on the middle platform of a spacious pet climbing frame with three distinct circular platforms. Directly to the left on the top platform rests a calm medium-sized fluffy dog, also lying down. On the right of the middle platform, a tiny mouse with smooth fur gently lies on the bottom platform, spaced appropriately. render all three animals peacefully posed facing outward, evenly lit and realistically scaled relative to the climbing structure without altering their positions per the original scene’s intent.

图片摘要：该图主要展示 6 Reasoning and visual outputs of UniGRPO. Our joint RL opti。
![](images/e6d2146e1a680b194b1302802e185a26cc443550c87bd7e7b3c52b17b0135943.jpg)

On the grassland, a tiger is chasing two sheep, one big and one small.

<think> The goal is to depict a tiger chasing the two sheep (large and small) on grassland as described. No alterations; render scene accurately with specified subjects and setting. </think>A vibrant orange tiger with dark stripes is sprinting to chase a large fluffy white sheep and a smaller white sheep, both calmly running ahead on green grass under clear sky; ensure all accurately portrayed per prompt. render warm realistic textures suitable for scene accuracy without changing intent.

图片摘要：该图主要展示 6 Reasoning and visual outputs of UniGRPO. Our joint RL opti。
![](images/9ed02860944783a71995894893b964d7501bf562360bc4eb2d703a0bfa521035.jpg)  
Figure 6 Reasoning and visual outputs of UniGRPO. Our joint RL optimization produces task-oriented reasoning that guides the synthesis policy toward faithful, photorealistic image generation.

# References

[1] Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu, Xiaonan Nie, Ziang Song, et al. Emerging properties in unified multimodal pretraining. arXiv preprint arXiv:2505.14683, 2025.   
[2] Hongyang Wei, Baixin Xu, Hongbo Liu, Size Wu, Jie Liu, Yi Peng, Peiyu Wang, Zexiang Liu, Jingwen He, Yidan Xietian, et al. Skywork unipic 2.0: Building kontext model with online rl for unified multimodal model. arXiv preprint arXiv:2509.04548, 2025.   
[3] Shanshan Zhao, Xinjie Zhang, Jintao Guo, Jiakui Hu, Lunhao Duan, Minghao Fu, Yong Xien Chng, Guo-Hua Wang, Qing-Guo Chen, Zhao Xu, et al. Unified multimodal understanding and generation models: Advances, challenges, and opportunities. arXiv preprint arXiv:2505.02567, 2025.   
[4] Jinheng Xie, Weijia Mao, Zechen Bai, David Junhao Zhang, Weihao Wang, Kevin Qinghong Lin, Yuchao Gu, Zhijie Chen, Zhenheng Yang, and Mike Zheng Shou. Show-o: One single transformer to unify multimodal understanding and generation. arXiv preprint arXiv:2408.12528, 2024.   
[5] Chunting Zhou, Lili Yu, Arun Babu, Kushal Tirumala, Michihiro Yasunaga, Leonid Shamis, Jacob Kahn, Xuezhe Ma, Luke Zettlemoyer, and Omer Levy. Transfusion: Predict the next token and diffuse images with one multi-modal model. arXiv preprint arXiv:2408.11039, 2024.   
[6] Chao Liao, Liyang Liu, Xun Wang, Zhengxiong Luo, Xinyu Zhang, Wenliang Zhao, Jie Wu, Liang Li, Zhi Tian, and Weilin Huang. Mogao: An omni foundation model for interleaved multi-modal generation. arXiv preprint arXiv:2505.05472, 2025.   
[7] Wenxuan Huang, Shuang Chen, Zheyong Xie, Shaosheng Cao, Shixiang Tang, Yufan Shen, Qingyu Yin, Wenbo Hu, Xiaoman Wang, Yuntian Tang, et al. Interleaving reasoning for better text-to-image generation. arXiv preprint arXiv:2509.06945, 2025.   
[8] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners.   
[9] Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling. arXiv preprint arXiv:2210.02747, 2022.   
[10] Xingchao Liu, Chengyue Gong, and Qiang Liu. Flow straight and fast: Learning to generate and transfer data with rectified flow. arXiv preprint arXiv:2209.03003, 2022.   
[11] Martin L Puterman. Markov decision processes. Handbooks in operations research and management science, 2: 331–434, 1990.   
[12] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.   
[13] Jie Liu, Gongye Liu, Jiajun Liang, Yangguang Li, Jiaheng Liu, Xintao Wang, Pengfei Wan, Di Zhang, and Wanli Ouyang. Flow-grpo: Training flow matching models via online rl. arXiv preprint arXiv:2505.05470, 2025.   
[14] Jonathan Ho and Tim Salimans. Classifier-free diffusion guidance. arXiv preprint arXiv:2207.12598, 2022.   
[15] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.   
[16] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems, 35:24824–24837, 2022.   
[17] Mihir Prabhudesai, Anirudh Goyal, Deepak Pathak, and Katerina Fragkiadaki. Aligning text-to-image diffusion models with reward backpropagation. arXiv preprint arXiv:2310.03739, 2023.   
[18] Kevin Clark, Paul Vicol, Kevin Swersky, and David J Fleet. Directly fine-tuning diffusion models on differentiable rewards. arXiv preprint arXiv:2309.17400, 2023.   
[19] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation. Advances in Neural Information Processing Systems, 36, 2024.

[20] Mihir Prabhudesai, Russell Mendonca, Zheyang Qin, Katerina Fragkiadaki, and Deepak Pathak. Video diffusion alignment via reward gradients. arXiv preprint arXiv:2407.08737, 2024.   
[21] Xue Bin Peng, Aviral Kumar, Grace Zhang, and Sergey Levine. Advantage-weighted regression: Simple and scalable off-policy reinforcement learning. arXiv preprint arXiv:1910.00177, 2019.   
[22] Jiajun Fan, Shuaike Shen, Chaoran Cheng, Yuxin Chen, Chumeng Liang, and Ge Liu. Online reward-weighted fine-tuning of flow matching with wasserstein regularization. In The Thirteenth International Conference on Learning Representations, 2025.   
[23] Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, and Shixiang Shane Gu. Aligning text-to-image models using human feedback. arXiv preprint arXiv:2302.12192, 2023.   
[24] Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative foundation model alignment. arXiv preprint arXiv:2304.06767, 2023.   
[25] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in Neural Information Processing Systems, 36, 2024.   
[26] Bram Wallace, Meihua Dang, Rafael Rafailov, Linqi Zhou, Aaron Lou, Senthil Purushwalkam, Stefano Ermon, Caiming Xiong, Shafiq Joty, and Nikhil Naik. Diffusion model alignment using direct preference optimization. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 8228–8238, 2024.   
[27] Jie Liu, Gongye Liu, Jiajun Liang, Ziyang Yuan, Xiaokun Liu, Mingwu Zheng, Xiele Wu, Qiulin Wang, Wenyu Qin, Menghan Xia, et al. Improving video generation with human feedback. arXiv preprint arXiv:2501.13918, 2025.   
[28] Kai Yang, Jian Tao, Jiafei Lyu, Chunjiang Ge, Jiaxin Chen, Weihan Shen, Xiaolong Zhu, and Xiu Li. Using human feedback to fine-tune diffusion models without any reward model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 8941–8951, 2024.   
[29] Zhanhao Liang, Yuhui Yuan, Shuyang Gu, Bohan Chen, Tiankai Hang, Ji Li, and Liang Zheng. Step-aware preference optimization: Aligning preference with denoising performance at each step. arXiv preprint arXiv:2406.04314, 2024.   
[30] Huizhuo Yuan, Zixiang Chen, Kaixuan Ji, and Quanquan Gu. Self-play fine-tuning of diffusion models for text-to-image generation. arXiv preprint arXiv:2402.10210, 2024.   
[31] Runtao Liu, Haoyu Wu, Zheng Ziqiang, Chen Wei, Yingqing He, Renjie Pi, and Qifeng Chen. Videodpo: Omni-preference alignment for video diffusion generation. arXiv preprint arXiv:2412.14167, 2024.   
[32] Jiacheng Zhang, Jie Wu, Weifeng Chen, Yatai Ji, Xuefeng Xiao, Weilin Huang, and Kai Han. Onlinevpo: Align video diffusion model with online video-centric preference optimization. arXiv preprint arXiv:2412.15159, 2024.   
[33] Hiroki Furuta, Heiga Zen, Dale Schuurmans, Aleksandra Faust, Yutaka Matsuo, Percy Liang, and Sherry Yang. Improving dynamic object interactions in text-to-video generation with ai feedback. arXiv preprint arXiv:2412.02617, 2024.   
[34] Zhanhao Liang, Yuhui Yuan, Shuyang Gu, Bohan Chen, Tiankai Hang, Mingxi Cheng, Ji Li, and Liang Zheng. Aesthetic post-training diffusion models from generic preferences with step-by-step preference optimization. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 13199–13208, 2025.   
[35] Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, and Sergey Levine. Training diffusion models with reinforcement learning. arXiv preprint arXiv:2305.13301, 2023.   
[36] Ying Fan, Olivia Watkins, Yuqing Du, Hao Liu, Moonkyung Ryu, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, Kangwook Lee, and Kimin Lee. Reinforcement learning for fine-tuning text-to-image diffusion models. Advances in Neural Information Processing Systems, 36, 2024.   
[37] Shashank Gupta, Chaitanya Ahuja, Tsung-Yu Lin, Sreya Dutta Roy, Harrie Oosterhuis, Maarten de Rijke, and Satya Narayan Shukla. A simple and effective reinforcement learning method for text-to-image diffusion fine-tuning. arXiv preprint arXiv:2503.00897, 2025.

[38] Zichen Miao, Jiang Wang, Ze Wang, Zhengyuan Yang, Lijuan Wang, Qiang Qiu, and Zicheng Liu. Training diffusion models towards diverse image generation with reinforcement learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10844–10853, 2024.   
[39] Hanyang Zhao, Haoxian Chen, Ji Zhang, David D Yao, and Wenpin Tang. Score as action: Fine-tuning diffusion generative models by continuous-time reinforcement learning. arXiv preprint arXiv:2502.01819, 2025.   
[40] Po-Hung Yeh, Kuang-Huei Lee, and Jun-Cheng Chen. Training-free diffusion model alignment with sampling demons. arXiv preprint arXiv:2410.05760, 2024.   
[41] Zhiwei Tang, Jiangweizhi Peng, Jiasheng Tang, Mingyi Hong, Fan Wang, and Tsung-Hui Chang. Tuning-free alignment of diffusion models with direct noise optimization. arXiv preprint arXiv:2405.18881, 2024.   
[42] Jiaming Song, Qinsheng Zhang, Hongxu Yin, Morteza Mardani, Ming-Yu Liu, Jan Kautz, Yongxin Chen, and Arash Vahdat. Loss-guided diffusion models for plug-and-play controllable generation. In International Conference on Machine Learning, pages 32483–32498. PMLR, 2023.   
[43] Zeyue Xue, Jie Wu, Yu Gao, Fangyuan Kong, Lingting Zhu, Mengzhao Chen, Zhiheng Liu, Wei Liu, Qiushan Guo, Weilin Huang, et al. Dancegrpo: Unleashing grpo on visual generation. arXiv preprint arXiv:2505.07818, 2025.   
[44] Haoyou Deng, Keyu Yan, Chaojie Mao, Xiang Wang, Yu Liu, Changxin Gao, and Nong Sang. Densegrpo: From sparse to dense reward for flow matching model alignment, Wed Jan 28 2026 03:39:05 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2601.20218.   
[45] Kaiwen Zheng, Huayu Chen, Haotian Ye, Haoxiang Wang, Qinsheng Zhang, Kai Jiang, Hang Su, Stefano Ermon, Jun Zhu, and Ming-Yu Liu. Diffusionnft: Online diffusion reinforcement with forward process, 2025. URL https://arxiv.org/abs/2509.16117.   
[46] Tao Huang, Zhao Zhong, Yutao Cui, Chun Fan, Junzhe Li, Yinping Ma, and Miles Yang. Mixgrpo: Unlocking flow-based grpo efficiency with mixed ode-sde, 2025. URL https://arxiv.org/abs/2507.21802.   
[47] Yiyang Wang, Xi Chen, Xiaogang Xu, Yu Liu, and Hengshuang Zhao. Gdro: Group-level reward post-training suitable for diffusion models, Mon Jan 05 2026 11:47:18 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2601.02036.   
[48] Shengjun Zhang, Zhang Zhang, Chensheng Dai, and Yueqi Duan. E-grpo: High entropy steps drive effective reinforcement learning for flow models, Thu Jan 01 2026 18:27:32 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2601.00423.   
[49] Haoran He, Yuxiao Ye, Jie Liu, Jiajun Liang, Zhiyong Wang, Ziyang Yuan, Xintao Wang, Hangyu Mao, Pengfei Wan, and Ling Pan. Gardo: Reinforcing diffusion models without reward hacking, Tue Dec 30 2025 10:55:45 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2512.24138.   
[50] Feng Wang and Zihao Yu. Coefficients-preserving sampling for reinforcement learning with flow matching, Thu Oct 09 2025 09:42:33 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2509.05952.   
[51] Yujie Zhou, Pengyang Ling, Jiazi Bu, Yibin Wang, Yuhang Zang, Jiaqi Wang, Li Niu, and Guangtao Zhai. G2rpo: Granular grpo for precise reward in flow models, Fri Oct 10 2025 08:40:51 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2510.01982.   
[52] Dailan He, Guanlin Feng, Xingtong Ge, Yazhe Niu, Yi Zhang, Bingqi Ma, Guanglu Song, Yu Liu, and Hongsheng Li. Neighbor grpo: Contrastive ode policy optimization aligns flow models, Fri Nov 21 2025 05:02:47 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2511.16955.   
[53] Jiajun Fan, Chaoran Cheng, Shuaike Shen, Xiangxin Zhou, and Ge Liu. Fine-tuning flow matching generative models with intermediate feedback, Mon Oct 20 2025 20:08:03 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2510.18072.   
[54] Jian Yang, Bo Zhang, Siming Fu, Dacheng Yin, Fengyun Rao, Yuke Zhao, Xiaoxuan He, and Wanli Li. Tempflowgrpo: When timing matters for grpo in flow models, 2025. URL https://arxiv.org/abs/2508.04324.   
[55] Yihong Luo, Tianyang Hu, and Jing Tang. Reinforcing diffusion models by direct group preference optimization, Thu Oct 09 2025 16:40:43 GMT+0000 (Coordinated Universal Time). URL https://arxiv.org/abs/2510.08425.   
[56] Benjamin Yu, Jackie Liu, and Justin Cui. Smart-grpo: Smartly sampling noise for efficient rl of flow-matching models, 2025. URL https://arxiv.org/abs/2510.02654.

[57] Jie Liu, Xipeng Qiu, Ning Ding, Alex Lamb, Lifeng Qiao, Luozhijie Jin, Zijie Qiu, and Zijie Diao. Inference-time alignment control for diffusion models with reinforcement learning guidance, 2025. URL https://arxiv.org/ abs/2508.21016.   
[58] Chameleon Team. Chameleon: Mixed-modal early-fusion foundation models. arXiv preprint arXiv:2405.09818, 2024.   
[59] Xinlong Wang, Xiaosong Zhang, Zhengxiong Luo, Quan Sun, Yufeng Cui, Jinsheng Wang, Fan Zhang, Yueze Wang, Zhen Li, Qiying Yu, et al. Emu3: Next-token prediction is all you need. arXiv preprint arXiv:2409.18869, 2024.   
[60] Yecheng Wu, Zhuoyang Zhang, Junyu Chen, Haotian Tang, Dacheng Li, Yunhao Fang, Ligeng Zhu, Enze Xie, Hongxu Yin, Li Yi, et al. Vila-u: a unified foundation model integrating visual understanding and generation. arXiv preprint arXiv:2409.04429, 2024.   
[61] Sen Ye, Mengde Xu, Shuyang Gu, Di He, Liwei Wang, and Han Hu. Understanding vs. generation: Navigating optimization dilemma in multimodal models. arXiv preprint arXiv:2602.15772, 2026.   
[62] Siqi Kou, Jiachun Jin, Zetong Zhou, Ye Ma, Yugang Wang, Quan Chen, Peng Jiang, Xiao Yang, Jun Zhu, Kai Yu, et al. Think-then-generate: Reasoning-aware text-to-image diffusion with llm encoders. arXiv preprint arXiv:2601.10332, 2026.   
[63] Fu-Yun Wang, Han Zhang, Michael Gharbi, Hongsheng Li, and Taesung Park. Promptrl: Prompt matters in rl for flow-based image generation. arXiv preprint arXiv:2602.01382, 2026.   
[64] Siyu Jiao, Yiheng Lin, Yujie Zhong, Qi She, Wei Zhou, Xiaohan Lan, Zilong Huang, Fei Yu, Yingchen Yu, Yunqing Zhao, et al. Thinkgen: Generalized thinking for visual generation. arXiv preprint arXiv:2512.23568, 2025.   
[65] Jing Wang, Jiajun Liang, Jie Liu, Henglin Liu, Gongye Liu, Jun Zheng, Wanyuan Pang, Ao Ma, Zhenyu Xie, Xintao Wang, et al. Grpo-guard: Mitigating implicit over-optimization in flow matching via regulated clipping. arXiv preprint arXiv:2510.22319, 2025.   
[66] Jie Wu, Yu Gao, Zilyu Ye, Ming Li, Liang Li, Hanzhong Guo, Jie Liu, Zeyue Xue, Xiaoxia Hou, Wei Liu, et al. Rewarddance: Reward scaling in visual generation. arXiv preprint arXiv:2509.08826, 2025.   
[67] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 24185–24198, 2024.   
[68] David McAllister, Songwei Ge, Brent Yi, Chung Min Kim, Ethan Weber, Hongsuk Choi, Haiwen Feng, and Angjoo Kanazawa. Flow matching policy gradients. arXiv preprint arXiv:2507.21053, 2025.   
[69] Shuchen Xue, Chongjian Ge, Shilong Zhang, Yichen Li, and Zhi-Ming Ma. Advantage weighted matching: Aligning rl with pretraining in diffusion models. arXiv preprint arXiv:2509.25050, 2025.   
[70] Dhruba Ghosh, Hannaneh Hajishirzi, and Ludwig Schmidt. Geneval: An object-focused framework for evaluating text-to-image alignment. Advances in Neural Information Processing Systems, 36:52132–52152, 2023.

# A Extended Experimental Results

# A.1 Detailed GenEval Results

Table 2 provides the comprehensive category-level breakdown of the GenEval benchmark. We present the fine-grained metrics across all six sub-categories (Single Object, Two Objects, Counting, Colors, Position, and Attribute Binding) for all evaluated models and baselines.

Table 2 Main quantitative results on the GenEval benchmark. All RL methods use the Bagel checkpoint after SFT. “Thinking” denotes whether the method explicitly generates intermediate reasoning tokens. $\times$ indicates training collapse.   

<table><tr><td>Model / Method</td><td>Thinking</td><td>Overall</td><td>Single Obj.</td><td>Two Obj.</td><td>Counting</td><td>Colors</td><td>Position</td><td>Attr. Binding</td></tr><tr><td>Bagel</td><td>×</td><td>0.78</td><td>0.98</td><td>0.96</td><td>0.78</td><td>0.84</td><td>0.52</td><td>0.58</td></tr><tr><td>Bagel</td><td>✓</td><td>0.79</td><td>0.99</td><td>0.92</td><td>0.77</td><td>0.88</td><td>0.56</td><td>0.62</td></tr><tr><td>SFT</td><td>×</td><td>0.83</td><td>0.99</td><td>0.95</td><td>0.83</td><td>0.89</td><td>0.58</td><td>0.75</td></tr><tr><td>SFT</td><td>✓</td><td>0.82</td><td>0.98</td><td>0.93</td><td>0.63</td><td>0.91</td><td>0.68</td><td>0.79</td></tr><tr><td>ReFL</td><td>×</td><td>0.85</td><td>1.00</td><td>0.97</td><td>0.86</td><td>0.92</td><td>0.57</td><td>0.81</td></tr><tr><td>ReFL</td><td>✓</td><td>0.84</td><td>0.99</td><td>0.96</td><td>0.63</td><td>0.94</td><td>0.70</td><td>0.82</td></tr><tr><td>FPO</td><td>×</td><td>0.87</td><td>0.99</td><td>0.99</td><td>0.90</td><td>0.93</td><td>0.59</td><td>0.86</td></tr><tr><td>FPO</td><td>✓</td><td>0.85</td><td>0.99</td><td>0.97</td><td>0.69</td><td>0.91</td><td>0.69</td><td>0.81</td></tr><tr><td>FlowGRPO</td><td>×</td><td>0.88</td><td>0.99</td><td>0.98</td><td>0.93</td><td>0.94</td><td>0.60</td><td>0.86</td></tr><tr><td>FlowGRPO</td><td>✓</td><td>0.86</td><td>0.99</td><td>0.96</td><td>0.76</td><td>0.90</td><td>0.71</td><td>0.84</td></tr><tr><td>TextGRPO</td><td>✓</td><td>0.88</td><td>0.99</td><td>0.96</td><td>0.87</td><td>0.91</td><td>0.76</td><td>0.84</td></tr><tr><td>ReFL (w/ Thinking)</td><td>✓</td><td>0.83</td><td>0.99</td><td>0.94</td><td>0.64</td><td>0.92</td><td>0.70</td><td>0.81</td></tr><tr><td>ReFL (w/ Thinking) + TextGRPO</td><td>✓</td><td>0.87</td><td>0.98</td><td>0.97</td><td>0.84</td><td>0.91</td><td>0.75</td><td>0.80</td></tr><tr><td>UniFPO</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>UniGRPO (Ours)</td><td>✓</td><td>0.90</td><td>0.99</td><td>0.99</td><td>0.91</td><td>0.91</td><td>0.73</td><td>0.86</td></tr></table>

# A.2 Qualitative Results Across Training Stages

We present qualitative comparisons of reasoning traces and generated images across different training stages. Figure 7 shows the reasoning trace and generated image of the baseline Bagel model. Figure 8 illustrates the result after SFT, during which we standardized the original <think> format to match prevalent LLM conventions. Although the SFT model produces extensive reasoning steps, the translation from textual thoughts to fine-grained visual details remains suboptimal. Figure 6 demonstrates that the subsequent RLbased training stage effectively addresses this gap, yielding more coherent reasoning traces and higher-quality image generation.

# B Implementation Details and Hyperparameters

Table 3 details the comprehensive hyperparameter settings used for the joint training of our Mixture of Experts (MoT) architecture. This includes the specific optimization configurations for both the text reasoning expert (TextGRPO) and the image denoising expert (FlowGRPO), alongside the joint objective weight $\lambda$ .

Six cups are arranged in two rows, with three in each row, viewed from above.

<think> The model should generate an image showing the cups from a top-down perspective, with the arrangement clearly visible as two rows of three cups each.

The expanded prompt follows: Six ceramic cups arranged in two neat rows of three, viewed from a top-down perspective, showcasing their symmetrical arrangement and clean, minimalist design. The cups are evenly spaced, with a neutral background that emphasizes their form and arrangement. The lighting is soft and diffused, creating subtle shadows and a calm, balanced atmosphere. The image is ultra-realistic, with fine details visible in the texture of the ceramic and the smooth surfaces of the cups. </think>

图片摘要：该图主要展示 3 details the comprehensive hyperparameter settings used for。
![](images/7fea55892ce9aaa2ea4431241caee3df1942a60ad86b2437e8afada2eac21472.jpg)

A boy is holding a piece of wood, and a girl is drawing on it with a pen.

<think> The model should generate an image where the girl is actively drawing on the wood held by the boy, showing interaction between them and the object.

Here’s the full, detailed prompt: A young boy stands holding a piece of wood horizontally, while a girl, seated nearby, actively draws on the wood with a pen. The scene is set in a bright, cozy workshop filled with natural light streaming through large windows, casting soft shadows. The wood has visible grain patterns, and the girl‘s hand is steady as she sketches intricate designs. The boy appears curious and supportive, watching her work with a gentle smile. The atmosphere is warm and creative, with subtle hints of wood shavings and tools scattered around the workspace. The image is highly detailed, ultra-realistic, with vibrant colors and a sense of realism, capturing the interaction between the two characters and the wooden surface. </think>

图片摘要：该图片与A large cat climbing frame has three platforms. On the three platforms, there is这部分内容相关。
![](images/420f7088018c646bc3b12a578240351f037bb613ee3a0dc183cf7d123df4d320.jpg)

A large cat climbing frame has three platforms. On the three platforms, there is a cat, a dog and a mouse lying respectively.

<think> The model should generate an image of a cat climbing frame with three platforms, each occupied by a cat, a dog, and a mouse, demonstrating a playful interaction among different animals.

Here’s the finished detailed prompt: A large, detailed cat climbing frame made of sturdy wood and metal, featuring three distinct platforms of varying heights. On the lowest platform, a relaxed cat lies sprawled out, its fur soft and fluffy, embodying comfort. On the middle platform, a playful dog sits upright, its ears perked and tail wagging slightly, exuding energy and curiosity. On the highest platform, a tiny mouse lies curled up, its tiny whiskers twitching softly, appearing calm and secure. The scene is set in a bright, airy environment with natural light streaming through large windows, casting soft shadows and creating a warm, inviting atmosphere. The image is ultra-realistic with fine details, showcasing textures like the rough wood grain, the smooth fur of the animals, and the intricate design of the climbing frame. </think>

图片摘要：该图片与On the grassland, a tiger is chasing two sheep, one big and one small；The model 这部分内容相关。
![](images/7e9016ac5801ee767c16f827a4d116f4d248e44e18cf3f5f387d03fa8b040a01.jpg)

On the grassland, a tiger is chasing two sheep, one big and one small.

<think> The model should generate an image where the tiger is depicted as a predator and the sheep are prey, emphasizing the chase dynamic.

Here’s the expanded prompt: A dynamic and vivid scene set on a vast, sunlit grassland under a clear blue sky, featuring a powerful tiger in midchase, its muscles tense and focused, as it pursues two sheep—one large and one small—scrambling away in panic. The tiger is depicted as a formidable predator with realistic fur texture and lifelike detail, while the sheep appear vulnerable and agile, their woolly coats catching the light. The composition emphasizes the chase, with the tiger positioned slightly ahead and the sheep trailing behind, creating a sense of motion and urgency. The grassland is lush and green, with scattered wildflowers and a warm, golden glow from the sunlight, enhancing the natural and dramatic atmosphere. Ultra-realistic style, cinematic lighting, and sharp focus bring the scene to life. </think>

图片摘要：该图主要展示 7 Reasoning trace and generated image of the baseline Bagel 。
![](images/7ba216d5997a7c38daa51852b6b463cfb05c8658b9d5828909b6c51d43f87687.jpg)  
Figure 7 Reasoning trace and generated image of the baseline Bagel model.

# Prompts

# Thinking Texts

# Images

<table><tr><td>Six cups are arranged in two rows, with three in each row, viewed from above.</td><td>&lt;think&gt; Okay, let&#x27;s tackle this user prompt. The user wants a prompt for an image of six cups arranged in two rows with three in each row, viewed from above. First, I need to determine the text intention. The user didn&#x27;t mention any specific text to visualize, so it&#x27;s &quot;no intention for visualized text.&quot; Next, I need to structure the prompt with style, content, and aesthetics. The style here is likely &quot;flat design&quot; or &quot;minimalist&quot; since it&#x27;s a simple arrangement. The content is the six cups in two rows of three, viewed from above. Aesthetics would include color, composition, and atmosphere. I should start with the style. &quot;Flat design&quot; is good for simplicity. Then describe the content: six cups arranged in two rows of three, viewed from above. Aesthetics could include color (maybe pastel or neutral), composition (balanced, centered), and atmosphere (clean, modern). Check if all elements are included: six cups, two rows of three, viewed from above. No text needed, so no quotes. Ensure the language is concise, no literary fluff. Let me put it all together. &lt;/think&gt; Flat design style, six cups arranged in two rows, three cups in each row, viewed from above. The cups are of different colors: light blue, light green, and light pink, with simple geometric patterns. The composition is centered, the arrangement is neat and orderly, and the color scheme is soft and harmonious, creating a clean and modern atmosphere.</td></tr><tr><td>A boy is holding a piece of wood, and a girl is drawing on it with a pen.</td><td>&lt;think&gt; The model should generate an image where the boy is holding the wood steady, and the girl is actively drawing on it with a pen, emphasizing their collaborative activity. &lt;/think&gt;A highly detailed and realistic scene of a boy and girl working together on a wooden surface, with the boy holding the wood steady with both hands, his posture relaxed yet focused, while the girl sits beside him, actively drawing on the wood with a pen in her right hand. The setting is indoors, with soft, natural lighting illuminating the scene, creating a warm and inviting atmosphere. The wooden surface is smooth and polished, with faint pencil marks visible as the girl draws intricate designs or patterns. The girl appears concentrated, her expression thoughtful, while the boy looks supportive and engaged. The background is minimalistic, featuring a simple wooden table and a few subtle decorative elements, ensuring the focus remains on their collaboration. The image captures a sense of creativity and teamwork, with a slightly artistic and intimate mood.</td></tr><tr><td>A large cat climbing frame has three platforms. On the three platforms, there is a cat, a dog and a mouse lying respectively.</td><td>&lt;think&gt; Okay, let&#x27;s tackle this user prompt. First, I need to determine if there&#x27;s a need for visual text. The user didn&#x27;t mention any specific text to display, so it&#x27;s &quot;no intention for visualized text.&quot; Next, I need to rewrite the prompt. The main elements are: a large cat climbing frame with three platforms. On each platform, there&#x27;s a cat, a dog, and a mouse lying respectively. Style: Since it&#x27;s a scene description, maybe &quot;flat design&quot; or &quot;cartoon illustration&quot; to keep it simple and clear. Content: The climbing frame, three platforms, each with a different animal. Aesthetic: Colors should be bright and playful, maybe pastel tones. Composition should be centered to show all elements clearly. Check if all elements are included: large cat climbing frame, three platforms, cat, dog, mouse on each. No text needed, so no quotes. Putting it all together: &quot;Flat design, a large cat climbing frame with three platforms. On the first platform, a cat lies; on the second, a dog lies; on the third, a mouse lies. Pastel color scheme, centered composition, simple and clear illustration style, playful and cute atmosphere.&quot; &lt;/think&gt; Flat design, a large cat climbing frame with three platforms. On the first platform, a cat lies; on the second, a dog lies; on the third, a mouse lies. Pastel color scheme, centered composition, simple and clear illustration style, playful and cute atmosphere.</td></tr><tr><td>On the grassland, a tiger is chasing two sheep, one big and one small.</td><td>&lt;think&gt; The model should generate an image of a grassland with a tiger in pursuit of two sheep, one larger and one smaller, emphasizing the predator-prey dynamic. &lt;/think&gt;A vast, vibrant grassland under a clear blue sky, featuring a majestic tiger in mid-stride, its powerful muscles taut as it chases two sheep—one large and one small—across the terrain. The scene captures the raw tension of the predator-prey dynamic, with the tiger focused intently on its prey, and the sheep appearing vulnerable yet determined. The grassland is lush and green, with scattered wildflowers and rolling hills in the background, bathed in warm, golden sunlight. The image should feel dynamic and lifelike, with realistic textures and detailed fur patterns on the tiger and sheep, emphasizing the natural beauty and intensity of the moment.</td></tr></table>

Figure 8 Reasoning trace and generation result after SFT. During SFT, we standardized the original <think> format to match prevalent LLM conventions. Although the model produces extensive reasoning steps, the translation from textual thoughts to fine-grained visual details remains suboptimal.

Table 3 Hyperparameters for UniGRPO.   

<table><tr><td colspan="2">Model Configuration</td></tr><tr><td>Training Timesteps</td><td>25</td></tr><tr><td>CFG Scale</td><td>1</td></tr><tr><td>Timestep Shift</td><td>3</td></tr><tr><td>Image Resolution</td><td>1024</td></tr><tr><td>Evaluation Timesteps</td><td>50</td></tr><tr><td colspan="2">Training</td></tr><tr><td>Group Size</td><td>24</td></tr><tr><td>Batch Size</td><td>32</td></tr><tr><td>Reasoning Expert Learning Rate</td><td>1e-6</td></tr><tr><td>Denoising Expert Learning Rate</td><td>3e-5</td></tr><tr><td>PPO Epochs</td><td>2</td></tr><tr><td>Flow Objective Weight (λ)</td><td>1</td></tr><tr><td colspan="2">TextGRPO</td></tr><tr><td>KL Divergence Loss Weight</td><td>0</td></tr><tr><td>Temperature</td><td>1</td></tr><tr><td colspan="2">FlowGRPO</td></tr><tr><td>MSE Loss Weight</td><td>1.5e-5</td></tr><tr><td>Loss Clip Range</td><td>1e-6</td></tr><tr><td>SDE Window</td><td>[0, 5]</td></tr><tr><td>SDE Window Size</td><td>3</td></tr><tr><td>Noise Level</td><td>0.8</td></tr></table>
