# OccAny: Generalized Unconstrained Urban 3D Occupancy

Anh-Quan Cao Tuan-Hung Vu

Valeo.ai, Paris, France

https://valeoai.github.io/OccAny

# Abstract

Relying on in-domain annotations and precise sensor-rig priors, existing 3D occupancy prediction methods are limited in both scalability and out-of-domain generalization. While recent visual geometry foundation models exhibit strong generalization capabilities, they were mainly designed for general purposes and lack one or more key ingredients required for urban occupancy prediction, namely metric prediction, geometry completion in cluttered scenes and adaptation to urban scenarios. We address this gap and present OccAny, the first unconstrained urban 3D occupancy model capable of operating on out-of-domain uncalibrated scenes to predict and complete metric occupancy coupled with segmentation features. OccAny is versatile and can predict occupancy from sequential, monocular, or surround-view images. Our contributions are three-fold: (i) we propose the first generalized 3D occupancy framework with (ii) Segmentation Forcing that improves occupancy quality while enabling mask-level prediction, and (iii) a Novel View Rendering pipeline that infers novel-view geometry to enable test-time view augmentation for geometry completion. Extensive experiments demonstrate that OccAny outperforms all visual geometry baselines on 3D occupancy prediction task, while remaining competitive with in-domain self-supervised methods across three input settings on two established urban occupancy prediction datasets. Our code is available at https://github.com/valeoai/OccAny .

# 1. Introduction

The innate ability to see and make sense of the world in three dimensions underpins how humans understand and navigate the space. Advancing 3D scene understanding is crucial for spatial intelligent systems such as autonomous driving, robotics, and augmented reality. A key task in this area is 3D occupancy prediction whose goal is to infer a voxelized map of the environment and, when required, provide the corresponding semantics. Despite advances in architecture design [12, 46, 58, 72], training algorithm [5, 27, 30, 44, 76]

图片摘要：该图主要展示 1. OccAny is a generalized 3D occupancy model that is traine。
![](images/f781a9578aa8c06ff61ecdae0c08b3dd51a24a719efd5238db35b3dc1138d7ee.jpg)  
Figure 1. OccAny is a generalized 3D occupancy model that is trained once and can operate on out-of-domain sequential, monocular, or surround-view urban images. It produces SAM2-like features, enabling promptable segmentation.

and dataset [4, 10, 13, 18], current state-of-the-art 3D models still lack the generalization of human perception, typically requiring constrained setup with precise sensor calibration. While humans can effortlessly infer complex 3D structures in any novel scenes, replicating this capability remains a demanding problem.

State-of-the-art supervised approaches for 3D occupancy prediction [23, 32, 34, 67, 69, 76, 82] achieve remarkable results when the training and test data are drawn from the same distribution, i.e. both are collected using the same or a similar sensor rig under comparable conditions. A core component of these methods is the lifting of 2D features into 3D space, performed either via learnable mechanisms [23, 34] or via explicit camera modeling [5, 79]. However, this lifting operation inherently embeds sensor- and domain-specific biases into the models, which limits their ability to generalize to new sensor suites or environments. Recent self-supervised works [6, 15, 24, 28, 70] remove the need for 3D supervision by formulating occupancy prediction as a differentiable volume-rendering problem, thereby leveraging advances in neural rendering [30, 44]. Despite this, self-supervised models still struggle to generalize, as they remain specialized to a particular training domain with strong biases in camera poses and intrinsic parameters. As we look toward a near future with millions of autonomous fleets equipped with different sensor configurations, advancing 3D occupancy prediction requires generalizable and efficient solutions capable of leveraging heterogeneous training data to overcome

current generalization barriers.

The advent of visual geometry foundation models [3, 63, 65, 66], built around the concept of direct pointmap prediction, has demonstrated the strong generalization potential of large-scale transformer networks for 3D scene understanding. However, their general-purpose design remains insufficient for urban occupancy prediction, which simultaneously requires metric-scale accuracy, cluttered geometry completion, and adaptation to the complex nature of urban environments.

We introduce a novel pipeline for urban 3D occupancy prediction that emphasizes scalability and generalization. Our approach follows the recipe of geometry foundation models that train visual transformers with straightforward point-level objectives on diverse, large-scale datasets. Unlike those prior works, we specialize in the task of occupancy prediction and focus exclusively on outdoor urban datasets, which we argue is essential for optimal adaptation to the unique characteristics of urban scene perception. A major challenge in outdoor urban scenarios is the sparsity of supervised LiDAR point clouds, which leads to irregular predictions in non-supervised regions and exacerbates the difficulty of geometry completion, particularly in highly cluttered areas. To address this, we introduce Segmentation Forcing, a distillation strategy that enriches geometry-focused features with segmentation awareness and thus helps regularize predictions with consistent segmentation cues of object instances and homogeneous regions. For geometry completion, we develop a Novel View Rendering pipeline that infers arbitrary novel-view geometry from a global scene memory. Our rendering pipeline enables Test-time View Augmentation, allowing us to densify and complete scenes at both the pointand voxel-levels. Fig. 1 illustrates our model. In summary, our contributions are three-fold:

• We propose a generalized 3D occupancy framework, OccAny, the first designed to infer dense 3D occupancy and segmentation features for out-of-domain unconstrained urban scenes. A unified OccAny model can operate on either sequential, monocular or surround-view images.   
• We introduce Segmentation Forcing, a novel regularization strategy to mitigate the sparsity of LiDAR supervision.   
• We develop a Novel View Rendering pipeline targeting geometry completion.

OccAny is trained on five urban datasets and evaluated on two out-of-distribution occupancy datasets: SemanticKITTI and Occ3D-NuScenes. OccAny significantly outperforms baseline visual geometry networks and performs on par with domain-specific SOTA self-supervised occupancy networks trained directly on SemanticKITTI and Occ3D-NuScenes.

# 2. Related works

Visual geometry foundation model. Dust3r [66] introduced the visual geometry foundation model, which uses large-scale pointmap prediction to solve diverse 3D tasks.

Research has rapidly expanded this paradigm beyond static, binocular inputs in several directions. One branch addresses dynamics by handling moving scenes [54, 84], dynamic video pose estimation [71], and camera rigs [33]. A major thrust has been multi-frame processing through feed-forward, sequential, and memory-based architectures [3, 62, 63, 65, 77]. Other works have explored downstream tasks such as indoor instance prediction [89] and image matching [31], or have leveraged known camera parameters [26]. While some methods explore novel view synthesis [29, 65], they often prioritize image synthesis over geometric fidelity [29] or exhibit limited applicability [65]. Unlike these approaches, we repurpose these models for occupancy prediction by introducing segmentation forcing to enhance geometric fidelity while enabling segmentation output. We further propose a novel pointmap rendering pipeline to enable complete geometry beyond visible scenery.

3D occupancy prediction . This task, which originates from 3D scene completion [53], aims to assign an occupancy state to each voxel in a 3D volume. Initially proposed for indoor depth scenes [53], it expanded to outdoor LiDAR [1, 7, 49, 73] and was later adapted for multi-view images [5]. Subsequent supervised research has focused on projection mechanisms [5, 34, 79], efficient representations [23, 25, 37, 51, 88], network architectures [34, 41, 85], and benchmark creation [35, 40, 59]. However, these methods’ reliance on dense, voxel-wise annotations limits their scalability.

Self-supervised methods mitigate this label dependency by training on posed images, often via volume rendering [6, 70]. Subsequent NeRF-based approaches have improved performance through better losses [21, 24, 83], optimized ray sampling [6, 75, 83], and enhanced representations by distilling foundation models [27, 52, 64]. More recently, 3D Gaussian Splatting has emerged as a more efficient alternative to NeRF [9, 15]. However, these approaches generally require precise camera information and in-domain training data. [15] is a partial exception, avoiding 6D poses via camera overlap, but still requires camera intrinsics and domain-specific information (i.e., adjacent camera overlap). Other works [28, 43, 80, 87] focus on pseudo-label generation, using open-vocabulary foundation models [28, 87] and sequence-level bundle adjustment [43]. While models trained on these pseudo-labels show promising cross-dataset generalization, they remain limited to specific settings.

# 3. Method

We build OccAny, a 3D occupancy framework that can generalize to arbitrary out-of-domain urban scenes. To this end, we adopt the transformer architecture from the Dust3r family and train the model on multiple urban datasets using standard point-level objectives commonly employed in prior works [3, 63, 66]. OccAny is supervised with metric-scale point-clouds enabling metric predictions at test time, a key

图片摘要：该图主要展示 2. OccAny Training is done in two stages: (i) 3D Reconstruct。
![](images/ce74e384bcba788a093171e654a1c75a5f9b232b5e6bfc91a00e86d99d074bf7.jpg)  
Figure 2. OccAny Training is done in two stages: (i) 3D Reconstruction infers 3D scene using $N _ { r e c }$ reconstruction frames and (ii) Novel-View Rendering renders geometry of $N _ { r n d }$ new views having camera poses $\{ \mathbf { T } _ { j } \} _ { j = 1 } ^ { N _ { r n d } }$ . Segmentation Forcing with SAM2 features helps regularize and improve geometry prediction. The scene memory M is dynamically updated during reconstruction, while during rendering, the final scene memory output from the reconstruction stage is used without updating

element in occupancy prediction. We propose two novel strategies Segmentation Forcing and Novel View Rendering to accommodate the unique characteristics of 3D occupancy prediction in urban environments.

Fig. 2 illustrates OccAny training process, which consists of two stages: 3D Reconstruction and Novel View Rendering. For each frame sequence, we randomly select $N$ frames for training. In the reconstruction stage, we set the number of reconstruction frames to $N _ { r e c } = N$ . In the rendering stage, we use non-overlapping sets of $N _ { r e c }$ reconstruction frames and $N _ { r n d }$ rendering frames, with $N = N _ { r e c } + N _ { r n d }$ .

# 3.1. 3D Reconstruction with Segmentation Forcing

The 3D Reconstruction stage aims to recover the scene geometry from a set of reconstruction frames, providing the geometry basis for the subsequent novel-view rendering stage. In this stage, OccAny extends MUSt3R [3], a multi-view geometry network, by adding a SAM2 feature prediction head. SAM2 [47] is a foundation model designed for promptable visual segmentation in images and videos; its features are thus rich in high-fidelity segmentation cues and are beneficial for resolving geometric ambiguity. The Segmentation Forcing loss compels OccAny to predict SAM2-like features. Our strategy regularizes geometry prediction by leveraging segmentation cues to enforce spatial and temporal feature consistency, thereby improving performance, especially in regions where LiDAR supervision is sparse.

OccAny processes $N _ { r e c }$ reconstruction frames $\{ \mathbf { I } _ { i } \} _ { i = 1 } ^ { N _ { r e c } } \quad \in \quad \mathbb { R } ^ { H \times W \times 3 }$ 1 as multi-view inputs to reconstruct the 3D scene. We feed $N _ { r e c }$ frames in chronological order through a shared reconstruction encoder $\mathcal { E }$ followed by a shared decoder $\mathcal { D }$ . The first frame is always designated as the reference frame; all non-reference frames are identified by a specialized token added at the beginning of the shared decoder. The two transformers produce, for each frame $\mathbf { I } _ { i }$ :

• SAM2-like feature maps $\mathbf { F } _ { i } \in \mathbb { R } ^ { H ^ { \prime } \times W ^ { \prime } \times C }$ ,   
• global pointmaps Pglobali,1 $\mathbf { P } _ { i , 1 } ^ { \mathrm { g l o b a l } } \in \mathbb { R } ^ { H \times W \times 3 }$ in the global camera coordinate of the reference frame 1,   
• local pointmap s Plocal $\mathbf { P } _ { i , i } ^ { \mathrm { l o c a l } } \in \mathbb { R } ^ { H \times W \times 3 }$ in the local camera coordinate of the current frame $i$ ,   
• confidence maps $\mathbf { C } _ { i } \in \mathbb { R } ^ { H \times W }$ ,   
• and camera poses $\mathbf { v } _ { i } \in \mathbb { R } ^ { 7 }$ inferred by registering the global and local pointmaps.

For each frame $i \in [ 3 , N _ { r e c } ]$ , a scene memory $\mathbf { M } _ { i - 1 }$ of all historical reconstruction frames $1 . . i - 1$ is used in the decoding process to infer the geometry of the current frame $i$ via cross-attention between tokens of frame $i$ and memory tokens in $\mathbf { M } _ { i - 1 }$ . The scene memory $\mathbf { M } _ { i }$ is then constructed by concatenating $\mathbf { M } _ { i - 1 }$ with the decoder tokens of the current frame i. To initialize, $\mathbf { M } _ { 2 }$ is formed by concatenating the decoder tokens of the first two frames. With a slight abuse of notation, we use M without a subscript to denote the final global scene memory, which aggregates information from the entire sequence; that is, M ≡ MNrec ∈ RH′×W ′×(C·Nrec). $\mathbf { M } \equiv \mathbf { \bar { M } } _ { N _ { r e c } } ^ { - } \in \mathbb { R } ^ { H ^ { \prime } \times W ^ { \prime } \times ( C \cdot N _ { r e c } ) }$

The decoder is followed by linear heads for pointmap and confidence prediction, and an MLP head for SAM2-like feature prediction. Because the geometry and segmentation tasks differ in nature, we introduce two learnable task tokens: $t _ { \mathrm { g } }$ for the pointmap heads and $t _ { \mathrm { s } }$ for the SAM2 head. These tokens are added to all decoder tokens before the corresponding head is applied. For clarity, we omit task tokens in the equations and only visualize them in Fig. 2.

The SAM2 head consists of an MLP with two linear layers followed by two upsampling layers. Each upsampling layer uses bilinear interpolation to resize the features, followed by a convolution, layer norm, and GELU.

In summary, the output of this stage is:

$$
\mathcal {D} \left(\mathcal {E} \left(\left\{\mathbf {I} _ {i} \right\} _ {i = 1} ^ {N _ {r e c}}\right)\right) = \left(\mathbf {M}, \left\{\mathbf {F} _ {i}, \mathbf {P} _ {i, 1} ^ {\text {g l o b a l}}, \mathbf {P} _ {i, i} ^ {\text {l o c a l}}, \mathbf {C} _ {i}, \mathbf {v} _ {i} \right\} _ {i = 1} ^ {N _ {r e c}}\right). \tag {1}
$$

# 3.2. Novel-View Rendering

We train a rendering encoder $\widetilde { \mathcal E }$ and decoder $\widetilde { \mathcal { D } }$ to predict pointmaps and SAM2-like features for arbitrary novel views along the reconstruction camera trajectories $\{ \bar { \bf v } _ { i } \} _ { i = 1 } ^ { N _ { r e c } }$ (cf . Eq. (1)). The reconstruction modules $\mathcal { E }$ , $\mathcal { D }$ are frozen, and their outputs serve as inputs to the rendering stage.

During training, we sample $N _ { r e c }$ reconstruction frames and $N _ { r n d }$ rendering frames from the same sequence; the $\{ \mathbf { T } _ { j } \} _ { j = 1 } ^ { N _ { r n d } }$ e always belongs to the reconstruction be the camera poses of rendering frames $\widetilde { \mathbf { I } } _ { j }$ Let. Our each $\mathbf { T } _ { j }$ , conditioned on reconstruction outputs. Rendering frames are used only for loss computation.

{Pglobali,1 }Nreci=1 Tokenization. $\{ \mathbf { P } _ { i , 1 } ^ { \mathrm { g l o b a l } } \} _ { i = 1 } ^ { N _ { r e c } }$ into a single point cloud We merge the global pointmaps $\mathbf { P } ^ { \mathrm { g l o b a l } }$ in the reference-frame coordinate system. Projecting $\mathbf { P } ^ { \mathrm { g l o b a l } }$ into {Tj}Nrndj=1 $\{ \mathbf { T } _ { j } \} _ { j = 1 } ^ { N _ { r n d } }$ }Nrnd yields $N _ { r n d }$ xyz-images and point-to-pixel correspondences, enabling 2D projection of SAM2-like features and confidence maps into each novel view. Each modality image is processed by an MLP; the results are coand linearly projected to form novel-view tokens $\{ \mathbf { X } _ { j } \} _ { j = 1 } ^ { N _ { r n d } }$

Rendering. Because reconstruction frames cover the scene only partially, projected novel views contain missing areas and projection artifacts. The rendering transformers learn to complete missing geometry and correct projection errors, producing denser pointmaps.

The rendering encoder $\widetilde { \varepsilon }$ contains 6 transformer blocks, processing novel-view token representations X to predict encoder tokens. During training, we distill knowledge from the large reconstruction encoder $\mathcal { E }$ (24 transformer blocks) to the small rendering encoder $\widetilde { \mathcal E }$ through the ${ \mathcal { L } } _ { \mathrm { e n c } }$ loss (defined in Sec. 3.4). This helps facilitate the optimization process by providing an auxiliary supervision signal, encouraging the rendering encoder to mimic the tokens produced by the larger teacher reconstruction encoder.

The rendering decoder $\widetilde { \mathcal { D } }$ has the same architecture as the reconstruction decoder $\mathcal { D }$ and is initialized from its weights. We also introduce two learnable task tokens $\widetilde { t _ { \mathrm { g } } }$ and $\widetilde { t _ { \mathrm { s } } }$ , initialized from $t _ { \mathrm { g } }$ and $t _ { \mathrm { s } }$ . The scene memory M obtained from the reconstruction stage remained fixed (cf . Eq. (1)) and is used by $\widetilde { \mathcal { D } }$ to render the final set of outputs. During decoding, $\tilde { \mathcal { D } }$ applies cross-attention between decoder tokens and the memory tokens in M, making possible reference to the whole reconstructed scene. Intuitively, the explicit reconstruction outputs from the previous stage guides the rendering, while the implicit memory provides supporting information to correct and complete the scene. Segmentation Forcing is also applied to regularize novel-view predictions.

In summary, output of the rendering stage is written:

$$
\widetilde {\mathcal {D}} (\mathbf {M}, \widetilde {\mathcal {E}} (\{\mathbf {X} \} _ {j = 1} ^ {N _ {r n d}})) = \left\{\widetilde {\mathbf {F}} _ {j}, \widetilde {\mathbf {P}} _ {j, 1} ^ {\text {g l o b a l}}, \widetilde {\mathbf {P}} _ {j, j} ^ {\text {l o c a l}}, \widetilde {\mathbf {C}} _ {j} \right\} _ {j = 1} ^ {N _ {r n d}}. \tag {2}
$$

图片摘要：该图主要展示 3. OccAny inference undergoes two stages: (i) 3D reconstruct。
![](images/2be1bc96465b117f48b7b759db6845a20577f9e34dc26825e175a9fa679c3faa.jpg)  
Figure 3. OccAny inference undergoes two stages: (i) 3D reconstruction to retrieve $N _ { r e c }$ pointmaps with predicted camera poses $\{ \mathbf { v } _ { i } \} _ { i = 1 } ^ { N _ { r e c } }$ , and (ii) novel-view rendering with TTVA sampled along the trajectory of $\{ \mathbf { v } _ { i } \} _ { i = 1 } ^ { N _ { r e c } }$ . 3D occupancy is obtained by aggregating all pointmaps and voxelizing them with trilinear interpolation.

# 3.3. OccAny Inference

We first retrieve the reconstructed pointmaps, SAM2-like features and the registered camera poses of all $N _ { r e c }$ input frames from the 3D Reconstruction stage. We then randomly sample novel views around the predicted camera trajectory $\{ \mathbf { v } _ { i } \} _ { i = 1 } ^ { N _ { r e c } }$ (cf . Eq. (1)) and pass them through the Novel View Rendering (NVR) stage to infer the novel-view pointmaps and segmentation features (cf . Eq. (2)). The final 3D occupancy is obtained by aggregating all pointmaps from both stages and voxelizing them into a dense grid via trilinear interpolation. The inference protocol is visualized in Fig. 3. OccAny is versatile and can predict 3D occupancy for either sequential, monocular, or surround-view inputs. Predicted SAM2-like features can be directly used for segmentation.

NVR Inference. Thanks to NVR, we can use arbitrary views at test-time to help infer occlusion; this strategy is coined Test-time View Augmentation (TTVA). We first position novel camera views uniformly every straight path along the trajectory of predi $\rho _ { \mathrm { f w d } }$ meteoses $\{ \mathbf { v } _ { i } \} _ { i = 1 } ^ { N _ { r e c } }$ At each of those $N _ { \mathrm { f w d } }$ sampled positions, we vary horizontal viewing angles $\Phi { = } \{ 0 , \pm \phi \}$ and shift the camera by a lateral amount of $\pm \rho _ { \mathrm { l a t } }$ . Fig. 6 illustrates the NVR setups.

Segmentation w/ SAM2-like features. We apply Grounded SAM2 [48] pipeline by feeding the first frame to GroundingDINO [38] and obtain candidate bounding boxes of all semantic classes of interest. We then use the pretrained prompt decoder of SAM2 to prompt OccAny’s predicted SAM2-like features with the obtained bounding boxes, resulting in dense semantic masks for the first frame. Semantic masks are then propagated through the entire scene with SAM2 video tracking. Finally we assign the predicted occupancy voxels with predicted semantic classes.

# 3.4. Training Losses

Both stages are trained using the same set of losses, i.e. global- and local- pointmap loss $\mathcal { L } _ { \mathrm { g l o } }$ , $\mathcal { L } _ { \mathrm { l o c } }$ , and Segmentation Forcing loss $\mathcal { L } _ { \mathrm { f o r c i n g } }$ , with the exception of the rendering encoder distillation loss ${ \mathcal { L } } _ { \mathrm { e n c } }$ , which is applied only in the rendering stage. We only describe common losses in the reconstruction stage for brevity.

Pointmap Losses $\mathcal { L } _ { \mathrm { g l o } }$ , $\mathcal { L } _ { \mathrm { l o c } }$ . The loss weights the difference between the predicted pointma p Pglobal $\mathbf { P } _ { i , 1 } ^ { \mathrm { g l o b a l } }$ and ground truth $\mathbf { P } _ { i , 1 } ^ { * }$ using the predicted confidence map $\mathbf { C } _ { i }$ [3]:

$$
\mathcal {L} _ {\mathrm {g l o}} = \frac {1}{| s |} \sum_ {i = 1} ^ {N _ {r e c}} \left\| \mathbf {C} _ {i} \odot (\mathbf {P} _ {i, 1} ^ {\mathrm {g l o b a l}} - \mathbf {P} _ {i, 1} ^ {*}) \right\| _ {1} - \alpha \log (\mathbf {C} _ {i}),
$$

where $\odot$ denotes element-wise multiplication with channelwise broadcasting, and $\alpha$ controls the regularization strength, and $s$ is the normalization scale [3, 65]. The local pointmap loss $\mathcal { L } _ { \mathrm { l o c } }$ is formulated identically.

Geometry-aware Segmentation Forcing Loss Lforcing. We employ a Mean Squared Error (MSE) loss. We use the same confidence map C in pointmap losses above to weight the MSE error:

$$
\mathcal {L} _ {\text {f o r c i n g}} = \frac {1}{H ^ {\prime} W ^ {\prime}} \sum_ {i = 1} ^ {N _ {r e c}} \left\| \mathbf {C} _ {i} \odot \left(\mathbf {F} _ {i} - \mathbf {F} _ {i} ^ {*}\right) \right\| _ {2} ^ {2}, \tag {3}
$$

where $N _ { r e c }$ is the number of reconstruction frames. Since C represents the geometry confidence learned by the pointmap head, our weighting forces the network to focus on highconfidence areas and ignore low-confidence ones like sky. We note that $\mathcal { L } _ { \mathrm { f o r c i n g } }$ does not update the confidence head.

Encoder Distillation Loss ${ \mathcal { L } } _ { \mathrm { e n c } }$ . This loss distills knowledge from the larger teacher reconstruction encoder $\mathcal { E }$ (24 layers) to the smaller student rendering encoder $\widetilde { \varepsilon }$ (6 layers). It minimizes the squared L2 distance between the output tokens from both encoders. Given the output tokens from the rendering encoder $\widetilde { \mathcal { E } } ( \{ \mathbf { X } _ { j } \} _ { j = 1 } ^ { N _ { r n d } } )$ and the reconstruction encoder $\mathcal { E } ( \{ \widetilde { \mathbf { I } } _ { j } \} _ { j = 1 } ^ { N _ { r n d } } )$ e , the loss is written as:

$$
\mathcal {L} _ {\mathrm {e n c}} = \sum_ {j = 1} ^ {N _ {r e c}} \left\| \mathcal {E} (\widetilde {\mathbf {I}} _ {j}) - \widetilde {\mathcal {E}} (\mathbf {X} _ {j}) \right\| _ {2} ^ {2},
$$

where $\{ \widetilde { \mathbf { I } } _ { j } \} _ { j = 1 } ^ { N _ { r e c } }$ are the novel-view images.

# 4. Experiments

Training. OccAny is trained on a mixture of five urban datasets, using images from all cameras and projected Li-DAR pointmap as ground truth: Waymo [55], DDAD [19], PandaSet [74], VKITTI2 [2], and ONCE [42].

In the reconstruction stage, we initialize with MUSt3R [3], freeze the encoder $\mathcal { E }$ and only train the

decoder $\mathcal { D }$ for 3D reconstruction. Input frames are resized to 512-width with varying aspect ratios. We sample training sequences with minimum length $N { = } 6$ and maximum length $N { = } 1 0$ . Frames are sampled at $2 \mathrm { H z }$ in all datasets.

In the rendering stage, we initialize $\widetilde { \mathcal { D } }$ with the pretrained weights of $\mathcal { D }$ . We keep the same sequence length $N \in$ [6, 10], and randomly select among those $N _ { r n d }$ frames as rendering views; the remaining $N _ { r e c } = N - N _ { r n d }$ are used for reconstruction. The first frame serves as reference and it is always part of the reconstruction set.

Evaluation. We evaluate the generalization of OccAny on two out-of-domain benchmarks: SemanticKITTI [1] and Occ3D-NuScenes [59], detailed in Sec. A.

We use three evaluation settings:

• Sequence: a sequence of 5 frames coming from a single camera on SemanticKITTI and Occ3D-NuScenes,   
• Monocular: a single input frame on SemanticKITTI,   
• Surround-view: all surrounding frames at a single timestep on Occ3D-NuScenes.

NVR inference. In the Sequence and Surround-view settings, we use the augmentation strategy TTVA with $N _ { \mathrm { f w d } } ~ = ~ 1 0$ , forward shift $\rho _ { \mathrm { f w d } }$ of $3 \mathrm { m }$ , and lateral shift $\rho _ { \mathrm { l a t } }$ of $2 \mathrm { m }$ . In the Monocular setting, we sample denser and use $N _ { \mathrm { f w d } } = 5 0$ , forward shift $\rho _ { \mathrm { f w d } }$ of $1 \mathrm { m }$ , lateral shift $\rho _ { \mathrm { l a t } }$ of $2 \mathrm { m }$ . All settings use horizontal angle $\phi$ of $\{ 0 ^ { \circ } , \pm 6 0 ^ { \circ } \}$ .

Baselines. We compare OccAny against four strong baselines: MUSt3R [3], CUT3R [65], VGGT [63], AnySplat [29], and Depth Anything 3 (DA3) [36]. Among them, CUT3R is trained only in the online setting. AnySplat is an VGGT extension with Gaussian Splatting [30] for novel view synthesis and for improving geometric consistency. MUSt3R and CUT3R output metric-scale pointmaps, whereas VGGT and AnySplat produce scale-invariant pointmaps. To resolve the scale ambiguity of VGGT and AnySplat, we calibrate their depth predictions with Metric3Dv2 [22] using their predicted camera intrinsics; those two variants are presented as VGGT† and AnySplat†. For DA3, we use DA3-LARGE to estimate global point map and DA3METRIC-LARGE for metric scaling. Since AnySplat and CUT3R support novelview synthesis, we also apply our proposed TTVA strategy to improve those, referred to as CUT3R* and AnySplat*†. All models are tested on the same input resolution, with a very slight difference depending on the patch-size.

For reference, we also report published results from vision-based self-supervised occupancy models trained indomain, which are heavily biased to dataset-specific characteristics especially camera intrinsics and extrinsics. We compare against self-supervised methods as both do not require in-domain 3D ground-truth for training. However, OccAny is completely zero-shot while self-supervised methods are trained on in-domain calibrated data.

Metrics. Similar to [5, 24], we use the standard 3D occupancy metrics Precision, Recall, and Intersection over Union

图片摘要：该图主要展示 4. Occupancy predictions of OccAny and baselines on a sequen。
![](images/4bbd95026a54535b6e8eb0f37fc904ba4ddca9b2caac499be24430b0f870c89c.jpg)  
Figure 4. Occupancy predictions of OccAny and baselines on a sequence and a surround view. We visualize here predicted voxels. For qualitative analysis, we overlay the semantic ground-truth colors on predicted voxels to better highlight class-wise gains. False positive voxels are painted in gray without any overlayed color. Compared to baselines, our occupancy predictions are denser and more accurate.

Table 1. Sequence setting. Occupancy prediction on SemanticKITTI and Occ3D-NuScenes.   

<table><tr><td rowspan="2">Method</td><td rowspan="2">Venue</td><td colspan="4">Semantic KITTI</td><td colspan="3">Occ3D-NuScenes</td></tr><tr><td>Res.</td><td>Prec.</td><td>Rec.</td><td>IoU</td><td>Res.</td><td>Prec.</td><td>Rec.</td></tr><tr><td>MUST3R [3]</td><td>CVPR&#x27;25</td><td>512x160</td><td>18.38</td><td>25.58</td><td>11.97</td><td>512x288</td><td>19.27</td><td>28.60</td></tr><tr><td>CUT3R [65]</td><td>CVPR&#x27;25</td><td>512x160</td><td>25.72</td><td>21.11</td><td>13.11</td><td>512x288</td><td>24.69</td><td>16.57</td></tr><tr><td>CUT3R* [65]</td><td>CVPR&#x27;25</td><td>512x160</td><td>27.05</td><td>27.92</td><td>15.93</td><td>512x288</td><td>29.44</td><td>30.50</td></tr><tr><td>VGGT† [63]</td><td>CVPR&#x27;25</td><td>518x168</td><td>36.35</td><td>22.62</td><td>15.20</td><td>518x294</td><td>38.34</td><td>26.23</td></tr><tr><td>AnySplat† [29]</td><td>TOG&#x27;25</td><td>518x168</td><td>18.22</td><td>35.62</td><td>11.67</td><td>518x294</td><td>26.67</td><td>36.93</td></tr><tr><td>AnySplat*† [29]</td><td>TOG&#x27;25</td><td>518x168</td><td>14.53</td><td>47.48</td><td>12.39</td><td>518x294</td><td>24.42</td><td>42.48</td></tr><tr><td>DA3 [36]</td><td>ICLR&#x27;26</td><td>518x168</td><td>26.37</td><td>28.13</td><td>15.76</td><td>518x294</td><td>51.25</td><td>23.64</td></tr><tr><td>OccAnybase</td><td>-</td><td>512x160</td><td>43.38</td><td>20.37</td><td>16.09</td><td>512x288</td><td>48.09</td><td>20.97</td></tr><tr><td>OccAny</td><td>-</td><td>512x160</td><td>36.79</td><td>46.70</td><td>25.91</td><td>512x288</td><td>36.09</td><td>40.39</td></tr></table>

*: use TTVA †: scaled with Metric3Dv2 [22].   
OccAnybase: w/o Segmentation Forcing & Novel-view Rendering.

(IoU) to assess geometry quality; mean IoU (mIoU) is used for semantic segmentation. Following open-vocabulary Li-DAR semantic segmentation works [17, 45, 50], we also report performance on super classes, denoted as mIoUsc. This helps evaluate results at a coarser semantic level, alleviating the impact of “prompting and text-to-image alignment” limitations [45] especially on semantically confusing classes, e.g., “car” vs. “other-vehicle”.

# 4.1. Main results

Sequence. In the Sequence setting ( Tab. 1), OccAny surpasses all other zero-shot baselines. On SemanticKITTI, it reaches $2 5 . 9 1 \%$ IoU, surpassing the nearest baseline

Table 2. Monocular setting. Occupancy results with Monocular input on SemanticKITTI following [6, 24]. Results for MonoScene and Splatter Image are taken from [6, 75].   

<table><tr><td>Test</td><td>Method</td><td>Venue</td><td>Res.</td><td>Prec.</td><td>Rec.</td><td>IoU</td></tr><tr><td rowspan="6">in-domain</td><td>MonoScene [5]</td><td>CVPR&#x27;22</td><td>1220x370</td><td>13.15</td><td>40.22</td><td>11.18</td></tr><tr><td>SceneRF [6]</td><td>ICCV&#x27;23</td><td>1220x370</td><td>17.28</td><td>40.96</td><td>13.84</td></tr><tr><td>SelfOcc [24]</td><td>CVPR&#x27;24</td><td>1220x370</td><td>34.83</td><td>37.31</td><td>21.97</td></tr><tr><td>Splatter Image [56]</td><td>CVPR&#x27;24</td><td>1220x370</td><td>11.30</td><td>53.93</td><td>10.30</td></tr><tr><td>Hi-Gaussian [75]</td><td>ICCV&#x27;25</td><td>1220x370</td><td>17.39</td><td>59.72</td><td>15.56</td></tr><tr><td>OccNeRF [83]</td><td>TIP&#x27;25</td><td>1220x370</td><td>35.25</td><td>39.27</td><td>22.81</td></tr><tr><td rowspan="9">out-of-domain</td><td>MUST3R [3]</td><td>CVPR&#x27;25</td><td>512x160</td><td>15.29</td><td>12.24</td><td>7.29</td></tr><tr><td>CUT3R [65]</td><td>CVPR&#x27;25</td><td>512x160</td><td>33.32</td><td>8.64</td><td>7.37</td></tr><tr><td>CUT3R* [65]</td><td>CVPR&#x27;25</td><td>512x160</td><td>33.47</td><td>17.59</td><td>13.03</td></tr><tr><td>VGGT† [63]</td><td>CVPR&#x27;25</td><td>518x168</td><td>25.59</td><td>14.49</td><td>10.19</td></tr><tr><td>AnySplat† [29]</td><td>TOG&#x27;25</td><td>518x168</td><td>17.97</td><td>20.39</td><td>10.56</td></tr><tr><td>AnySplat*† [29]</td><td>TOG&#x27;25</td><td>518x168</td><td>14.61</td><td>35.21</td><td>11.52</td></tr><tr><td>DA3 [36]</td><td>ICLR&#x27;26</td><td>518x168</td><td>23.98</td><td>14.54</td><td>9.95</td></tr><tr><td>OccAnybase</td><td>-</td><td>512x160</td><td>41.24</td><td>14.49</td><td>12.01</td></tr><tr><td>OccAny</td><td>-</td><td>512x160</td><td>45.64</td><td>33.66</td><td>24.03</td></tr></table>

*: use TTVA †: scaled with Metric3Dv2 [22].   
OccAnybase: w/o Segmentation Forcing & Novel-view Rendering.

(CUT3R*) by roughly 10 points. A similar trend is observed on Occ3D-NuScenes, where OccAny achieves $2 3 . 5 5 \%$ IoU, significantly outperforming baselines; of note, some baselines are already enhanced with post-hoc metric scaling and, if applicable, TTVA. This demonstrates OccAny’s ability to effectively complete geometry from limited-view sequence without in-domain training, thanks to Segmentation Forcing

图片摘要：该图主要展示 5. Qualitative ablation shows the gains from Segmentation Fo。
![](images/1f0204447bb0e7b3b593aab0a8c7c887274f908a9877e6f0efe42d280a8df4d1.jpg)

图片摘要：该图主要展示 5. Qualitative ablation shows the gains from Segmentation Fo。
![](images/a2b137c1d4f742643b4f616fa8f840691bd345cff50c9caa0f62abcc073f8278.jpg)  
Figure 5. Qualitative ablation shows the gains from Segmentation Forcing and Novel-View Rendering. Voxel colorization follows Fig. 4. The two proposed strategies significantly improve the density and the accuracy of occupancy predictions.

Table 3. Surround-view setting. More results are in Tab. 8.   

<table><tr><td>Test</td><td>Method</td><td>Venue</td><td>Res.</td><td>Prec.</td><td>Rec.</td><td>IoU</td></tr><tr><td rowspan="5">in-domain</td><td>SelfOcc [24]</td><td>CVPR&#x27;24</td><td>800x450</td><td>-</td><td>-</td><td>45.01</td></tr><tr><td>OccNeRF [83]</td><td>TIP&#x27;25</td><td>672x336</td><td>57.20</td><td>55.47</td><td>39.20</td></tr><tr><td>DistillNeRF [64]</td><td>NeuRIPS&#x27;24</td><td>400x228</td><td>-</td><td>-</td><td>29.11</td></tr><tr><td>SimpleOcc [14]</td><td>TIV&#x27;24</td><td>672x336</td><td>41.91</td><td>64.02</td><td>33.92</td></tr><tr><td>GaussTR [28]</td><td>CVPR&#x27;25</td><td>896x504</td><td>-</td><td>-</td><td>45.19</td></tr><tr><td rowspan="9">out-of-domain</td><td>MUSt3R [3]</td><td>CVPR&#x27;25</td><td>512x288</td><td>20.79</td><td>28.29</td><td>13.61</td></tr><tr><td>CUT3R [65]</td><td>CVPR&#x27;25</td><td>512x288</td><td>32.19</td><td>7.93</td><td>6.79</td></tr><tr><td>CUT3R* [65]</td><td>CVPR&#x27;25</td><td>512x288</td><td>40.60</td><td>26.73</td><td>19.21</td></tr><tr><td>VGGT† [63]</td><td>CVPR&#x27;25</td><td>518x294</td><td>41.56</td><td>28.64</td><td>20.42</td></tr><tr><td>AnySplat† [29]</td><td>TOG&#x27;25</td><td>518x294</td><td>29.35</td><td>40.80</td><td>20.59</td></tr><tr><td>AnySplat*† [29]</td><td>TOG&#x27;25</td><td>518x294</td><td>24.52</td><td>57.65</td><td>20.78</td></tr><tr><td>DA3 [36]</td><td>ICLR&#x27;26</td><td>518x294</td><td>53.26</td><td>23.75</td><td>19.65</td></tr><tr><td>OccAnybase</td><td>-</td><td>512x288</td><td>59.58</td><td>21.19</td><td>18.53</td></tr><tr><td>OccAny</td><td>-</td><td>512x288</td><td>45.04</td><td>58.54</td><td>34.15</td></tr></table>

*: use TTVA †: scaled with Metric3Dv2 [22].   
OccAnybase: w/o Segmentation Forcing & Novel-view Rendering.

and Novel-View Rendering. The ${ \mathrm { O c c A n y } } _ { \mathrm { b a s e } }$ variant, which is equivalent to fine-tuning MUSt3R on our datasets, was trained without the two proposed strategies and obtained only marginal improvements over baselines.

Wrong metric reasoning leads to voxels predicted outside of the scene, significantly degrading the performance. The scale-invariant design of VGGT and AnySplat is not wellsuited for the occupancy task, unlike OccAny with metric prediction by design. The Gaussian Splatting of AnySplat, while favorable for synthesizing compelling images, produces lots of geometric artifacts, thereby hallucinating lots of noises and harming geometry prediction. Fig. 4 visualizes the occupancy results.

Monocular. In the more challenging Monocular set-

Table 4. Semantic Occupancy Prediction with GSAM2 [48].   

<table><tr><td rowspan="2">Method</td><td rowspan="2">Venue</td><td colspan="3">Semantic KITTI sequence</td><td colspan="3">Occ3D-NuScenes surround-view</td></tr><tr><td>Res.</td><td>mIoU</td><td>mIoU\( ^{1\text{sc}} \)</td><td>Res.</td><td>mIoU</td><td>mIoU\( ^{1\text{sc}} \)</td></tr><tr><td>MUSi3R [3] + SAM2 [47]</td><td>CVPR&#x27;25</td><td>512x160</td><td>3.22</td><td>5.96</td><td>512x288</td><td>2.43</td><td>3.84</td></tr><tr><td>CUT3R [65] + SAM2 [47]</td><td>CVPR&#x27;25</td><td>512x160</td><td>4.15</td><td>6.72</td><td>512x288</td><td>2.40</td><td>2.75</td></tr><tr><td>CUT3R* [65] + SAM2 [47]</td><td>CVPR&#x27;25</td><td>512x160</td><td>4.53</td><td>8.18</td><td>512x288</td><td>3.06</td><td>3.99</td></tr><tr><td>VGGT†[63] + SAM2 [47]</td><td>CVPR&#x27;25</td><td>518x294</td><td>3.47</td><td>6.76</td><td>518x294</td><td>4.39</td><td>6.49</td></tr><tr><td>AnySpat†[29] + SAM2 [47]</td><td>TOG&#x27;25</td><td>518x168</td><td>3.37</td><td>6.83</td><td>518x294</td><td>3.96</td><td>5.97</td></tr><tr><td>AnySpat*†[29] + SAM2 [47]</td><td>TOG&#x27;25</td><td>518x168</td><td>3.86</td><td>7.51</td><td>518x294</td><td>4.44</td><td>6.51</td></tr><tr><td>DA3 [36] + SAM2 [47]</td><td>ICLR&#x27;26</td><td>518x168</td><td>4.92</td><td>9.56</td><td>518x294</td><td>4.55</td><td>6.29</td></tr><tr><td>OccAny w/o forcing + SAM2 [47]</td><td>-</td><td>512x160</td><td>6.83</td><td>12.01</td><td>512x288</td><td>6.17</td><td>8.96</td></tr><tr><td>OccAny</td><td>-</td><td>512x160</td><td>7.28</td><td>13.53</td><td>512x288</td><td>6.66</td><td>10.32</td></tr></table>

*: use TTVA † : scaled with Metric3Dv2 [22].

ting on SemanticKITTI (Tab. 2), OccAny demonstrates remarkable generalization. It achieves $2 4 . 0 3 \%$ IoU, outperforming all other zero-shot baselines by significant margins (e.g., $+ 1 1 . 0 0 \%$ IoU over ${ \mathrm { C U T } } 3 { \mathrm { R } } ^ { * }$ w/ TTVA). Notably, it significantly surpasses several in-domain self-supervised methods like SceneRF $( + 1 0 . 1 9 \% )$ ; OccAny even surpasses self-supervised SOTAs SelfOcc $( + 2 . 0 6 \% )$ and OccNeRF $( + 1 . 2 2 \% )$ , despite never been trained on SemanticKITTI.

Surround-view. In the Surround-view setting on Occ3D-NuScenes Tab. 3, OccAny maintains its lead among zeroshot methods with $3 4 . 1 5 \%$ IoU, and achieves better performance than some in-domain approaches like Distill-NeRF/SimpleOcc, yet remains behind more recent methods.

Semantic Occupancy. We further evaluate 3D semantic occupancy (Tab. 4) by applying Grounded SAM2 pipeline directly on OccAny’s segmentation features. OccAny achieves the highest mIoU and mIoUsc across both datasets, compared to baselines using a separated SAM2 model to produce segmentation features. The comparison with the variant “OccAny w/o forcing $^ +$ SAM2” confirms that our Segmentation Forcing strategy leads to a unified and simpler solution to

Table 5. Changing the base foundation models used in OccAny to DA3 [36] and SAM3 [8] results in the OccAny+ variant.   

<table><tr><td rowspan="2">Method</td><td colspan="6">Semantic KITTI sequence</td><td colspan="6">Occ3D-NuScenes surround-view</td></tr><tr><td>Res.</td><td>Pre.</td><td>Rec.</td><td>IoU</td><td>mIoU</td><td>mIoU\( ^{SC} \)</td><td>Res.</td><td>Pre.</td><td>Rec.</td><td>IoU</td><td>mIoU</td><td>mIoU\( ^{SC} \)</td></tr><tr><td>OccAny</td><td>512x160</td><td>36.79</td><td>46.70</td><td>25.91</td><td>7.28</td><td>13.53</td><td>512x288</td><td>45.04</td><td>58.54</td><td>34.15</td><td>6.66</td><td>10.32</td></tr><tr><td>OccAny+</td><td>512x160</td><td>38.12</td><td>49.14</td><td>27.33</td><td>6.48</td><td>13.30</td><td>512x288</td><td>46.38</td><td>54.66</td><td>33.49</td><td>7.20</td><td>11.50</td></tr></table>

Table 6. Ablation results on SemanticKitti. The “geo-aware” stands for applying geometry confidence maps $\mathbf { C }$ in the segmentation forcing loss (cf . Eq. (3)).   

<table><tr><td rowspan="2">NVR
Σflowing
geo-share + Σtge</td><td colspan="2">SemKITTI seq.</td><td colspan="2">SemKITTI single</td></tr><tr><td>IoU</td><td>Δ IoU</td><td>IoU</td><td>Δ IoU</td></tr><tr><td>X</td><td>19.64</td><td>-6.27</td><td>11.55</td><td>-12.48</td></tr><tr><td>X</td><td>24.23</td><td>-1.68</td><td>21.73</td><td>-2.30</td></tr><tr><td>X</td><td>24.88</td><td>-1.03</td><td>23.02</td><td>-1.01</td></tr><tr><td>X</td><td>25.04</td><td>-0.87</td><td>22.67</td><td>-1.36</td></tr><tr><td>X</td><td>24.99</td><td>-0.92</td><td>23.46</td><td>-0.57</td></tr><tr><td>OccAny</td><td>25.91</td><td>—</td><td>24.03</td><td>—</td></tr></table>

图片摘要：该图主要展示 6. Ablation results on SemanticKitti. The “geo aware” stands。
![](images/99a4920c4da67bcde92e9c3d5ae8538ed7db79d22ba7a3d9ebe5b1a40a32afb1.jpg)  
Figure 6. Ablating NVR inference on SemanticKITTI

better predict geometry and segmentation.

Impact of base foundation models. We change the foundation models used in OccAny to DA3 [36] and SAM3 [8], resulting in the OccAny+ variant, detailed in Sec. A.3. Tab. 5 and Sec. B show that OccAny benefits from advances in generic foundation models, while being independently and orthogonally effective for occupancy prediction.

# 4.2. Analysis

Method ablation. Tab. 6 analyzes the contribution of each proposed component. Removing Test-Time View Augmentation (TTVA) causes the most significant drop $( - 6 . 2 7 \%$ in sequence- and $- 1 2 . 4 7 \%$ in monocular setting), highlighting its critical role in geometry completion. The renderingspecific losses $\mathcal { L } _ { \mathrm { E n c } }$ , geometry-aware $\mathcal { L } _ { \mathrm { f o r c i n g } }$ , and the task tokens also consistently contribute to the final performance, proving their effectiveness. Fig. 5 shows gains brought by Segmentation Forcing and Novel-view Rendering (TTVA).

NVR inference. We ablate NVR inference in Fig. 6. Starting from the baseline without TTVA, adding simple forward movement helps complete distant geometry $\left( + 1 . 8 3 \% \right)$ . Introducing rotations and lateral shifts further helps complete the geometry by resolving occlusions from diverse views, improving IoU by $+ 4 . 1 5 \%$ and resulting in the final $2 5 . 9 1 \%$

Promptable segmentation feature. We visualize the seg-

图片摘要：该图主要展示 7. PCA visualization of our segmentation features of multi v。
![](images/48549b3a5f15d395559c50cae187dc0bb5bd17bb60e7cb205c880a8e53bc463e.jpg)  
Figure 7. PCA visualization of our segmentation features of multi-view sequences. Low-resolution features capture high-level semantics (e.g., separating cars, buildings, and roads), while highresolution features capture low-level details such as boundaries and textures. Features remain consistent across different views.

图片摘要：该图主要展示 7. PCA visualization of our segmentation features of multi v。
![](images/186dbb5f5e561c67861b8b63c4380dee81d677c62a178106323be9880233a878.jpg)  
Figure 8. Instance segmentation of cars with OccAny’s features.

mentation features of OccAny using PCA, as shown in Fig. 7. Low-resolution features appear to cluster semantically similar regions, while high-resolution features seem to capture fine details like boundaries and textures, both helping regularize and improve occupancy prediction (cf . Fig. 5 & Tab. 6).

Similar to SAM2, our segmentation features remain spatially and temporally consistent. This consistency enables instance segmentation via prompting with object instances detected by Grounding DINO. In Fig. 8, we show some qualitative results when performing instance segmentation directly on our segmentation features.

# 5. Conclusion

We propose for the first time a generalized 3D occupancy network, called OccAny, that is trained once and perform zeroshot inference on arbitrary out-of-domain sequential, monocular and surround-view unposed data. With the proposed Segmentation Forcing and Novel-View Rendering strategies, OccAny outperforms generic visual-geometry foundation models on occupancy prediction. OccAny surpasses several in-domain self-supervised models, while remaining behind more recent ones. Our work introduces a novel framework for occupancy prediction prioritizing scalability and generalization, paving the way toward the next generation of versatile and generalized occupancy networks. The gap to fully-supervised in-domain performance remains substantial, leaving room for future improvements in this direction.

Acknowledgment. This work was granted access to the HPC resources of IDRIS under the allocations AD011014102R2, AD011013540R1 made by GENCI. We acknowledge EuroHPC Joint Undertaking for awarding the project ID EHPC-REG-2025R01-032 access to Karolina, Czech Republic.

# References

[1] Jens Behley, Martin Garbade, Andres Milioto, Jan Quenzel, Sven Behnke, Cyrill Stachniss, and Juergen Gall. Semantickitti: A dataset for semantic scene understanding of lidar sequences. In ICCV, 2019. 2, 5, 13   
[2] Yohann Cabon, Naila Murray, and Martin Humenberger. Virtual kitti 2. In arXiv, 2020. 5   
[3] Yohann Cabon, Lucas Stoffl, Leonid Antsfeld, Gabriela Csurka, Boris Chidlovskii, Jerome Revaud, and Vincent Leroy. Must3r: Multi-view network for stereo 3d reconstruction. In CVPR, 2025. 2, 3, 5, 6, 7   
[4] Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Giancarlo Baldan, and Oscar Beijbom. nuscenes: A multimodal dataset for autonomous driving. In CVPR, 2020. 1, 13   
[5] Anh-Quan Cao and Raoul de Charette. Monoscene: Monocular 3d semantic scene completion. In CVPR, 2022. 1, 2, 5, 6   
[6] Anh-Quan Cao and Raoul de Charette. Scenerf: Selfsupervised monocular 3d scene reconstruction with radiance fields. In ICCV, 2023. 1, 2, 6, 13   
[7] Anh-Quan Cao, Angela Dai, and Raoul de Charette. Pasco: Urban 3d panoptic scene completion with uncertainty awareness. In CVPR, 2024. 2   
[8] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, Jie Lei, Tengyu Ma, Baishan Guo, Arpit Kalla, Markus Marks, Joseph Greer, Meng Wang, Peize Sun, Roman Rä- dle, Triantafyllos Afouras, Effrosyni Mavroudi, Katherine Xu, Tsung-Han Wu, Yu Zhou, Liliane Momeni, Rishi Hazra, Shuangrui Ding, Sagar Vaze, Francois Porcher, Feng Li, Siyuan Li, Aishwarya Kamath, Ho Kei Cheng, Piotr Dollár, Nikhila Ravi, Kate Saenko, Pengchuan Zhang, and Christoph Feichtenhofer. Sam 3: Segment anything with concepts. In ICLR, 2026. 8   
[9] Loick Chambon, Eloi Zablocki, Alexandre Boulch, Mickael Chen, and Matthieu Cord. Gaussrender: Learning 3d occupancy with gaussian rendering. In CVPR, 2025. 2   
[10] Angel X Chang, Thomas Funkhouser, Leonidas Guibas, Pat Hanrahan, Qixing Huang, Zimo Li, Silvio Savarese, Manolis Savva, Shuran Song, Hao Su, et al. Shapenet: An informationrich 3d model repository. arXiv, 2015. 1   
[11] Dubing Chen, Jin Fang, Wencheng Han, Xinjing Cheng, Junbo Yin, Chenzhong Xu, Fahad Shahbaz Khan, and Jianbing Shen. Alocc: adaptive lifting-based 3d semantic occupancy and cost volume-based flow prediction. In ICCV, 2025. 14, 15   
[12] Christopher Choy, JunYoung Gwak, and Silvio Savarese. 4d spatio-temporal convnets: Minkowski convolutional neural networks. In CVPR, 2019. 1

[13] Angela Dai, Angel X Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser, and Matthias Nießner. Scannet: Richlyannotated 3d reconstructions of indoor scenes. In CVPR, 2017. 1   
[14] Wanshui Gan, Ningkai Mo, Hongbin Xu, and Naoto Yokoya. A comprehensive framework for 3d occupancy estimation in autonomous driving. IEEE TIV, 2024. 7   
[15] Wanshui Gan, Fang Liu, Hongbin Xu, Ningkai Mo, and Naoto Yokoya. Gaussianocc: Fully self-supervised and efficient 3d occupancy estimation with gaussian splatting. In ICCV, 2025. 1, 2, 14   
[16] Shenyuan Gao, Jiazhi Yang, Li Chen, Kashyap Chitta, Yihang Qiu, Andreas Geiger, Jun Zhang, and Hongyang Li. Vista: A generalizable driving world model with high fidelity and versatile controllability. In NeurIPS, 2024. 15   
[17] Simon Gebraad, Andras Palffy, and Holger Caesar. Leap: Consistent multi-domain 3d labeling using foundation models. In ICRA, 2025. 6   
[18] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we ready for autonomous driving? the kitti vision benchmark suite. In CVPR, 2012. 1   
[19] Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raventos, and Adrien Gaidon. 3d packing for self-supervised monocular depth estimation. In CVPR, 2020. 5   
[20] Mariam Hassan, Sebastian Stapf, Ahmad Rahimi, Pedro M. B. Rezende, Yasaman Haghighi, David Brüggemann, Isinsu Katircioglu, Lin Zhang, Xiaoran Chen, Suman Saha, Marco Cannici, Elie Aljalbout, Botao Ye, Xi Wang, Aram Davtyan, Mathieu Salzmann, Davide Scaramuzza, Marc Pollefeys, Paolo Favaro, and Alexandre Alahi. Gem: A generalizable ego-vision multimodal world model for fine-grained ego-motion, object dynamics, and scene composition control. In CVPR, 2025. 15   
[21] Adrian Hayler, Felix Wimbauer, Dominik Muhle, Christian Rupprecht, and Daniel Cremers. S4c: Self-supervised semantic scene completion with neural fields. In 3DV, 2024. 2   
[22] Mu Hu, Wei Yin, Chi Zhang, Zhipeng Cai, Xiaoxiao Long, Hao Chen, Kaixuan Wang, Gang Yu, Chunhua Shen, and Shaojie Shen. Metric3d v2: A versatile monocular geometric foundation model for zero-shot metric depth and surface normal estimation. IEEE TPAMI, 2024. 5, 6, 7, 13   
[23] Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Jie Zhou, and Jiwen Lu. Tri-perspective view for vision-based 3d semantic occupancy prediction. In CVPR, 2023. 1, 2   
[24] Yuanhui Huang, Wenzhao Zheng, Borui Zhang, Jie Zhou, and Jiwen Lu. Selfocc: Self-supervised vision-based 3d occupancy prediction. In CVPR, 2024. 1, 2, 5, 6, 7, 13   
[25] Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Jie Zhou, and Jiwen Lu. Gaussianformer: Scene as gaussians for visionbased 3d semantic occupancy prediction. In ECCV, 2024. 2   
[26] Wonbong Jang, Philippe Weinzaepfel, Vincent Leroy, Lourdes Agapito, and Jerome Revaud. Pow3r: Empowering unconstrained 3d reconstruction with camera and scene priors. In CVPR, 2025. 2

[27] Aleksandar Jevtic, Christoph Reich, Felix Wimbauer, Oliver ´ Hahn, Christian Rupprecht, Stefan Roth, and Daniel Cremers. Feed-forward scenedino for unsupervised semantic scene completion. In ECCV, 2025. 1, 2   
[28] Haoyi Jiang, Liu Liu, Tianheng Cheng, Xinjie Wang, Tianwei Lin, Zhizhong Su, Wenyu Liu, and Xinggang Wang. Gausstr: Foundation model-aligned gaussian transformer for self-supervised 3d spatial understanding. In CVPR, 2025. 1, 2, 7   
[29] Lihan Jiang, Yucheng Mao, Linning Xu, Tao Lu, Kerui Ren, Yichen Jin, Xudong Xu, Mulin Yu, Jiangmiao Pang, Feng Zhao, Dahua Lin, and Bo Dai. Anysplat: Feed-forward 3d gaussian splatting from unconstrained views. ACM TOG, 2025. 2, 5, 6, 7, 14   
[30] Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, and George Drettakis. 3d gaussian splatting for real-time radiance field rendering. ACM TOG, 2023. 1, 5   
[31] Vincent Leroy, Yohann Cabon, and Jerome Revaud. Grounding image matching in 3d with mast3r. In ECCV, 2024. 2   
[32] Bohan Li, Yasheng Sun, Xin Jin, Wenjun Zeng, Zheng Zhu, Xiaoefeng Wang, Yunpeng Zhang, James Okae, Hang Xiao, and Dalong Du. Stereoscene: Bev-assisted stereo matching empowers 3d semantic scene completion. In IJCAI, 2024. 1   
[33] Samuel Li, Pujith Kachana, Prajwal Chidananda, Saurabh Nair, Yasutaka Furukawa, and Matthew Brown. Rig3r: Rigaware conditioning for learned 3d reconstruction. In NeurIPS, 2025. 2   
[34] Yiming Li, Zhiding Yu, Christopher Choy, Chaowei Xiao, Jose M Alvarez, Sanja Fidler, Chen Feng, and Anima Anandkumar. Voxformer: Sparse voxel transformer for camerabased 3d semantic scene completion. In CVPR, 2023. 1, 2   
[35] Yiming Li, Sihang Li, Xinhao Liu, Moonjun Gong, Kenan Li, Nuo Chen, Zijun Wang, Zhiheng Li, Tao Jiang, Fisher Yu, Yue Wang, Hang Zhao, Zhiding Yu, and Chen Feng. Sscbench: A large-scale 3d semantic scene completion benchmark for autonomous driving. In IROS, 2024. 2   
[36] Haotong Lin, Sili Chen, Jun Hao Liew, Donny Y. Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. Depth anything 3: Recovering the visual space from any views. arXiv, 2025. 5, 6, 7, 8   
[37] Haisong Liu, Haiguang Wang, Yang Chen, Zetong Yang, Jia Zeng, Li Chen, and Limin Wang. Fully sparse 3d panoptic occupancy prediction. In ECCV, 2024. 2   
[38] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Qing Jiang, Chunyuan Li, Jianwei Yang, Hang Su, et al. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. In ECCV, 2024. 4   
[39] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In ICLR, 2019. 13   
[40] Junyi Ma, Xieyuanli Chen, Jiawei Huang, Jingyi Xu, Zhen Luo, Jintao Xu, Weihao Gu, Rui Ai, and Hesheng Wang. Cam4docc: Benchmark for camera-only 4d occupancy forecasting in autonomous driving applications. In CVPR, 2024. 2   
[41] Qihang Ma, Xin Tan, Yanyun Qu, Lizhuang Ma, Zhizhong Zhang, and Yuan Xie. Cotr: Compact occupancy transformer for vision-based 3d occupancy prediction. In CVPR, 2024. 2

[42] Jiageng Mao, Minzhe Niu, Chenhan Jiang, Hanxue Liang, Jingheng Chen, Xiaodan Liang, Yamin Li, Chaoqiang Ye, Wei Zhang, Zhenguo Li, et al. One million scenes for autonomous driving: Once dataset. In NeurIPS, 2021. 5   
[43] R. Marcuzzi, L. Nunes, E.A. Marks, L. Wiesmann, T. Läbe, J. Behley, and C. Stachniss. SfmOcc: Vision-Based 3D Semantic Occupancy Prediction in Urban Environments. RA-L, 2025. 2   
[44] Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, and Ren Ng. Nerf: representing scenes as neural radiance fields for view synthesis. Commun. ACM, 2021. 1   
[45] Aljoša Ošep, Tim Meinhardt, Francesco Ferroni, Neehar Peri, Deva Ramanan, and Laura Leal-Taixé. Better call sal: Towards learning to segment anything in lidar. In ECCV, 2024. 6   
[46] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point sets for 3d classification and segmentation. In CVPR, 2017. 1   
[47] Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, and Christoph Feichtenhofer. Sam 2: Segment anything in images and videos. In ICLR, 2025. 3, 7   
[48] Tianhe Ren, Shilong Liu, Ailing Zeng, Jing Lin, Kunchang Li, He Cao, Jiayu Chen, Xinyu Huang, Yukang Chen, Feng Yan, et al. Grounded sam: Assembling open-world models for diverse visual tasks. In arXiv, 2024. 4, 7   
[49] Luis Roldão, Raoul de Charette, and Anne Verroust-Blondet. Lmscnet: Lightweight multiscale 3d semantic completion. In 3DV, 2020. 2   
[50] Nermin Samet, Gilles Puy, and Renaud Marlet. Losc: Lidar open-voc segmentation consolidator. In 3DV, 2026. 6   
[51] Yiang Shi, Tianheng Cheng, Qian Zhang, Wenyu Liu, and Xinggang Wang. Occupancy as set of points. In ECCV, 2024. 2   
[52] Sophia Sirko-Galouchenko, Alexandre Boulch, Spyros Gidaris, Andrei Bursuc, Antonin Vobecky, Patrick Pérez, and Renaud Marlet. Occfeat: Self-supervised occupancy feature prediction for pretraining bev segmentation networks. In CVPR, 2024. 2   
[53] Shuran Song, Fisher Yu, Andy Zeng, Angel X Chang, Manolis Savva, and Thomas Funkhouser. Semantic scene completion from a single depth image. In CVPR, pages 1746–1754, 2017. 2   
[54] Edgar Sucar, Zihang Lai, Eldar Insafutdinov, and Andrea Vedaldi. Dynamic point maps: A versatile representation for dynamic 3d reconstruction. In ICCV, 2025. 2   
[55] Pei Sun, Henrik Kretzschmar, Xerxes Dotiwalla, Aurelien Chouard, Vijaysai Patnaik, Paul Tsui, James Guo, Yin Zhou, Yuning Chai, Benjamin Caine, et al. Scalability in perception for autonomous driving: Waymo open dataset. In CVPR, 2020. 5   
[56] Stanislaw Szymanowicz, Chrisitian Rupprecht, and Andrea Vedaldi. Splatter image: Ultra-fast single-view 3d reconstruction. In CVPR, 2024. 6

[57] Zachary Teed and Jia Deng. DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras. In NeurIPS, 2021. 15   
[58] Hugues Thomas, Charles R Qi, Jean-Emmanuel Deschaud, Beatriz Marcotegui, François Goulette, and Leonidas J Guibas. Kpconv: Flexible and deformable convolution for point clouds. In ICCV, 2019. 1   
[59] Xiaoyu Tian, Tao Jiang, Longfei Yun, Yucheng Mao, Huitong Yang, Yue Wang, Yilun Wang, and Hang Zhao. Occ3d: A large-scale 3d occupancy prediction benchmark for autonomous driving. In NeurIPS, 2023. 2, 5, 13   
[60] Alexander Veicht, Paul-Edouard Sarlin, Philipp Lindenberger, and Marc Pollefeys. GeoCalib: Single-image Calibration with Geometric Optimization. In ECCV, 2024. 15   
[61] Antonin Vobecky, Oriane Siméoni, David Hurych, Spyros Gidaris, Andrei Bursuc, Patrick Pérez, and Josef Sivic. Pop-3d: Open-vocabulary 3d occupancy prediction from images. In NeurIPS, 2023. 14   
[62] Hengyi Wang and Lourdes Agapito. 3d reconstruction with spatial memory. In 3DV, 2025. 2   
[63] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. Vggt: Visual geometry grounded transformer. In CVPR, 2025. 2, 5, 6, 7, 15   
[64] Letian Wang, Seung Wook Kim, Jiawei Yang, Cunjun Yu, Boris Ivanovic, Steven L. Waslander, Yue Wang, Sanja Fidler, Marco Pavone, and Peter Karkus. Distillnerf: Perceiving 3d scenes from single-glance images by distilling neural fields and foundation model features. In NeurIPS, 2024. 2, 7   
[65] Qianqian Wang, Yifei Zhang, Aleksander Holynski, Alexei A Efros, and Angjoo Kanazawa. Continuous 3d perception model with persistent state. In CVPR, 2025. 2, 5, 6, 7   
[66] Shuzhe Wang, Vincent Leroy, Yohann Cabon, Boris Chidlovskii, and Jerome Revaud. Dust3r: Geometric 3d vision made easy. In CVPR, 2024. 2   
[67] Yu Wang and Chao Tong. H2gformer: Horizontal-to-global voxel transformer for 3d semantic scene completion. In AAAI, 2024. 1   
[68] Zehan Wang, Siyu Chen, Lihe Yang, Jialei Wang, Ziang Zhang, Hengshuang Zhao, and Zhou Zhao. Depth anything with any prior. In arXiv, 2025. 14   
[69] Yi Wei, Linqing Zhao, Wenzhao Zheng, Zheng Zhu, Jie Zhou, and Jiwen Lu. Surroundocc: Multi-camera 3d occupancy prediction for autonomous driving. In ICCV, 2023. 1   
[70] Felix Wimbauer, Nan Yang, Christian Rupprecht, and Daniel Cremers. Behind the scenes: Density fields for single view reconstruction. In CVPR, 2023. 1, 2   
[71] Felix Wimbauer, Weirong Chen, Dominik Muhle, Christian Rupprecht, and Daniel Cremers. Anycam: Learning to recover camera poses and intrinsics from casual videos. In CVPR, 2025. 2   
[72] Xiaoyang Wu, Li Jiang, Peng-Shuai Wang, Zhijian Liu, Xihui Liu, Yu Qiao, Wanli Ouyang, Tong He, and Hengshuang Zhao. Point transformer v3: Simpler faster stronger. In CVPR, 2024. 1   
[73] Zhaoyang Xia, Youquan Liu, Xin Li, Xinge Zhu, Yuexin Ma, Yikang Li, Yuenan Hou, and Yu Qiao. Scpnet: Semantic scene completion on point cloud. In CVPR, 2023. 2

[74] Pengchuan Xiao, Zhenlei Shao, Steven Hao, Zishuo Zhang, Xiaolin Chai, Judy Jiao, Zesong Li, Jian Wu, Kai Sun, Kun Jiang, et al. Pandaset: Advanced sensor suite dataset for autonomous driving. In ITSC, 2021. 5   
[75] Binjian Xie, Pengju Zhang, Hao Wei, and Yihong Wu. Higaussian: Hierarchical gaussians under normalized spherical projection for single-view 3d reconstruction. In ICCV, 2025. 2, 6   
[76] Yujie Xue, Huilong Pi, Jiapeng Zhang, Yunchuan Qin, Zhuo Tang, Kenli Li, and Ruihui Li. Sdformer: Vision-based 3d semantic scene completion via sam-assisted dual-channel voxel transformer. In ICCV, 2025. 1   
[77] Jianing Yang, Alexander Sax, Kevin J. Liang, Mikael Henaff, Hao Tang, Ang Cao, Joyce Chai, Franziska Meier, and Matt Feiszli. Fast3r: Towards 3d reconstruction of $1 0 0 0 +$ images in one forward pass. In CVPR, 2025. 2   
[78] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, and Hengshuang Zhao. Depth anything v2. In NeurIPS, 2024. 15   
[79] Jiawei Yao, Chuming Li, Keqiang Sun, Yingjie Cai, Hao Li, Wanli Ouyang, and Hongsheng Li. Ndc-scene: Boost monocular 3d semantic scene completion in normalized device coordinates space. In ICCV, 2023. 1, 2   
[80] Baijun Ye, Minghui Qin, Saining Zhang, Moonjun Gong, Shaoting Zhu, Hao Zhao, and Hang Zhao. Gs-occ3d: Scaling vision-only occupancy reconstruction with gaussian splatting. In ICCV, 2025. 2   
[81] Zhangchen Ye, Tao Jiang, Chenfeng Xu, Yiming Li, and Hang Zhao. Cvt-occ: Cost volume temporal fusion for 3d occupancy prediction. In ECCV, 2024. 14, 15   
[82] Zhu Yu, Runmin Zhang, Jiacheng Ying, Junchen Yu, Xiaohai Hu, Lun Luo, Si-Yuan Cao, and Hui-liang Shen. Context and geometry aware voxel transformer for semantic scene completion. In NeurIPS, 2024. 1   
[83] Chubin Zhang, Juncheng Yan, Yi Wei, Jiaxin Li, Li Liu, Yansong Tang, Yueqi Duan, and Jiwen Lu. Occnerf: Advancing 3d occupancy prediction in lidar-free environments. IEEE TIP, 2025. 2, 6, 7   
[84] Junyi Zhang, Charles Herrmann, Junhwa Hur, Varun Jampani, Trevor Darrell, Forrester Cole, Deqing Sun, and Ming-Hsuan Yang. Monst3r: A simple approach for estimating geometry in the presence of motion. In ICLR, 2025. 2   
[85] Yunpeng Zhang, Zheng Zhu, and Dalong Du. Occformer: Dual-path transformer for vision-based 3d semantic occupancy prediction. In ICCV, 2023. 2   
[86] Jilai Zheng, Pin Tang, Zhongdao Wang, Guoqing Wang, Xiangxuan Ren, Bailan Feng, and Chao Ma. Veon: Vocabularyenhanced occupancy prediction. In ECCV, 2024. 14   
[87] Xiaoyu Zhou, Jingqi Wang, Yongtao Wang, Yufei Wei, Nan Dong, and Ming-Hsuan Yang. Autoocc: Automatic openended semantic occupancy annotation via vision-language guided gaussian splatting. In ICCV, 2025. 2   
[88] Sicheng Zuo, Wenzhao Zheng, Xiaoyong Han, Longchao Yang, Yong Pan, and Jiwen Lu. Quadricformer: Scene as superquadrics for 3d semantic occupancy prediction. NeurIPS, 2025. 2

[89] Lojze Zust, Yohann Cabon, Juliette Marrie, Leonid Antsfeld, Boris Chidlovskii, Jerome Revaud, and Gabriela Csurka. Panst3r: Multi-view consistent panoptic segmentation. In ICCV, 2025. 2

Table 7. Using pretrained segmentation features to boost semantic performance. OccAny+ is the variant using DA3 and SAM3 base models. Parameter counts reflect the forward path from the input to the predicted pointmaps and segmentation features. Note that using "pretrained" semantic features incurs a higher parameter cost due to the use of pretrained encoder.   

<table><tr><td rowspan="2">Method</td><td rowspan="2">Sem. feat. Params</td><td colspan="3">Semantic KITTI sequence</td><td colspan="3">Occ3D-NuScenes surround-view</td></tr><tr><td>Res.</td><td>mIoU</td><td>mIoUsc</td><td>Res.</td><td>mIoU</td><td>mIoUsc</td></tr><tr><td>OccAny</td><td>Distilled</td><td>623M</td><td>512x160</td><td>7.28</td><td>13.53</td><td>512x288</td><td>6.66</td></tr><tr><td>OccAny+</td><td>Distilled</td><td>651M</td><td>512x160</td><td>6.48</td><td>13.30</td><td>512x288</td><td>7.20</td></tr><tr><td>OccAny</td><td>Pretrained</td><td>864M</td><td>512x160</td><td>7.67</td><td>13.75</td><td>512x288</td><td>7.42</td></tr><tr><td>OccAny+</td><td>Pretrained</td><td>1.08B</td><td>512x160</td><td>8.03</td><td>13.17</td><td>512x288</td><td>9.45</td></tr></table>

# A. Additional Details

# A.1. Datasets

Occ3D-NuScenes was built upon nuScenes [4]. It contains 1, 000 20-sec sequences captured by one LiDAR and six surrounding cameras. The dataset provides 3D occupancy annotations of 18 semantic classes, with $0 . 4 \mathrm { m }$ voxels covering $8 0 \times 8 0 \times 6 . 4 \mathrm { m }$ areas at the resolution of $2 0 0 \times 2 0 0 \times 1 6$ voxels. Evaluation is done on the official val split [59] of 150 sequences.

SemanticKITTI, based on KITTI [1], consists of 22 sequences. Each sequence is annotated at the resolution of $2 5 6 \times 2 5 6 \times 3 2$ with $_ { 0 . 2 \mathrm { m } }$ voxels and 21 semantic classes (19 semantics, 1 free, 1 unknown). In our experiments, we only use images from the cam2 camera. Following [6, 24], we evaluate on the val set, i.e. sequence 8.

# A.2. Training

The 3D Reconstruction stage (cf . Sec. 3.1) is trained in two consecutive steps:

• Sequence-only training. We only use mono-view sequences from all cameras across the five datasets. Training samples are drawn from frames within the same monoview sequences.   
• Mixed training. This step continues Sequence-only training while mixing surround-view data with sequential data (from the previous step) at a $1 : 1$ ratio. For surround-view data, we use frames from different cameras captured at the same timestep.

The Novel-View Rendering stage (cf . Sec. 3.2) is trained exclusively on sequential data. Empirically, we observed no gains when incorporating surround-view data in this stage.

Each stage is trained for 100 epochs using the AdamW optimizer [39] with a learning rate of $7 \times 1 0 ^ { - 5 }$ . We utilize a cosine scheduler with a minimum learning rate of $1 \times 1 0 ^ { - 6 }$ and a 3-epoch warmup. The training set consists of 50, 000 samples (sequences or sets of surrounding images), with 10, 000 drawn from each dataset. Experiments are conducted on 16 NVIDIA A100 40GB GPUs with an effective batch size of 64. The 3D Reconstruction and Novel-View

Table 8. Detailed surround-view results. OccAny+ is the variant using DA3 and SAM3 base models.   

<table><tr><td></td><td>Method</td><td>Extr.</td><td>Intr.</td><td>Fixed Ratio</td><td>Fixed Rig</td><td>GT LiDAR</td><td>Sem. Adapt.</td><td>GT Occ.</td><td>IoU</td><td>mIoU</td></tr><tr><td rowspan="8">Occ3D-NumScenes (ext. Tab. 3)</td><td>SimpleOcc</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>33.92</td><td>7.05</td></tr><tr><td>DistillNeRF</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>-</td><td>29.11</td><td>8.93</td></tr><tr><td>SelfOcc</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>Req.</td><td>-</td><td>45.01</td><td>9.30</td></tr><tr><td>POP-3D</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>28.17</td><td>9.31</td></tr><tr><td>OccNeRF</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>Req.</td><td>-</td><td>39.20</td><td>9.53</td></tr><tr><td>GaussianOcc</td><td>-</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>Req.</td><td>-</td><td>51.22</td><td>9.94</td></tr><tr><td>VEON</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>57.92</td><td>12.38</td></tr><tr><td>GaussTR</td><td>Req.</td><td>Req.</td><td>Req.</td><td>Req.</td><td>-</td><td>Req.</td><td>-</td><td>45.19</td><td>12.27</td></tr><tr><td rowspan="7">out-of-domain</td><td>MUSt3R</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>13.61</td><td>2.43</td></tr><tr><td>CUT3R*</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>19.21</td><td>3.06</td></tr><tr><td>VGGT†</td><td>Rescale</td><td>Rescale</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>20.42</td><td>4.39</td></tr><tr><td>AnySplat*†</td><td>Rescale</td><td>Rescale</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>20.78</td><td>4.44</td></tr><tr><td>DA3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>19.65</td><td>4.55</td></tr><tr><td>OccAny</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>34.10</td><td>6.62</td></tr><tr><td>OccAny+ (Pretrained)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>33.49</td><td>9.45</td></tr></table>

*: use TTVA † : scaled with Metric3Dv2 [22]. Req.: required in-domain data/priors. Rescale: metric scaling needed

Rendering stages required approximately 40 and 30 training hours, respectively.

# A.3. OccAny+ using DA3 and SAM3

For the 3D Reconstruction phase, we substitute the reconstruction encoder $\mathcal { E }$ and decoder $\mathcal { D }$ from MUSt3R with DA3 backbone, fine-tuning the final eight transformer layers and the dual DPT head. For novel view rendering, we utilize the same projection and tokenization layers but replace both the rendering encoder $\widetilde { \mathcal E }$ and decoder $\tilde { \mathcal { D } }$ with DA3 backbone.

To leverage the strong initialization of the pretrained DA3 model, we introduce a self-distillation branch that duplicates the last eight transformer layers. These duplicated layers serve as a "teacher", supervising the eight trainable transformer layers via a scale-invariant loss, matching the scale-invariant output of the pretrained DA3.

In the Novel View Rendering phase, DA3 is initialized with the weights from the reconstruction phase. We train the first eight transformer layers while freezing the rest. Because DA3 lacks a memory mechanism, we tokenize the reconstruction outputs (pointmap, confidence, RGB, and segmentation features) from all reconstructed views using the same toview tokens $\{ \mathbf { X } _ { j } \} _ { j = 1 } ^ { N _ { r n d } }$ ese are passed alongside the novel-. To facilitate cross-view information between global and local attention starting from the first layer, rather than the eighth layer as in the original DA3.

Regarding Segmentation Forcing, we replaced the SAM2 encoder with a SAM3 encoder. Our findings indicate that performance improves significantly when the linear head is replaced with a DPTHead, particularly when trained using a $1 0 \times$ higher learning rate. In all experiments, we use the DA3-LARGE variant.

# B. Supplementary Studies

We present here the supplementary studies not presented in the main text due to the lack of space.

# B.1. Boosting semantic performance.

While the unified OccAny model conveniently uses distilled segmentation features, it can also be combined with the original features from segmentation foundation models at inference. Although this introduces additional overhead, it enables the use of higher-resolution segmentation features and improves semantic performance, as shown in Tab. 7.

# B.2. More surround-view results

Tab. 8 details results and method constraints in the surround-view setting, further including POP-3D [61], GaussianOcc [15], and VEON [86]. Existing in-domain approaches, including self-supervised ones, rely heavily on domain-specific priors, and VEON further depends on binary occupancy ground truth for training. In contrast, OccAny promotes a paradigm shift toward generalized and unconstrained occupancy prediction, enabling deployment of a unified model across out-of-domain and heterogeneous sensor setups. Beyond being unconstrained, OccAny can benefit from continual advances in foundation models, and is therefore expected to progressively narrow the remaining performance gap.

As preliminary evidence, upgrading MUSt3R to DA3 and replacing SAM2 with the more recent SAM3 yields an mIoU improvement of approximately 3 points, reaching performance comparable to recent self-supervised methods such as GaussianOcc [15].

# B.3. Novel-View Rendering vs. Depth Completion

In this experiment, we compare the effectiveness of our Novel-View Rendering stage (cf . Sec. 3.2) with a baseline that performs depth completion on the projected pointmaps of the novel views. To this end, we replace Novel-View Rendering by using Prior Depth Anything [68], which takes as input the sparse projected pointmaps and the rendered RGB images produced by the state-of-the-art novel-view synthesis method AnySplat [29]. The Prior Depth Anything model outputs dense, completed depth maps for the novel views. We name this baseline OccAnydepth completion and present comparison results in Tab. 9. Both models start from the first-stageonly OccAny and both adopt the TTVA strategy. OccAny significantly outperforms the OccAnydepth completion baseline, validating the effectiveness of our second stage.

# B.4. Generalization of State-of-the-art (SOTA) 3D Supervised Occupancy Models

We assess the generalization capability of SOTA 3D fullysupervised models by evaluating models trained on a source

dataset directly on a different target dataset. We evaluate two settings:

• Occ3D-Waymo Occ3D-NuScenes (surround-view surround-view).   
• Occ3D-NuScenes/Occ3D-Waymo SemanticKITTI (surround-view monocular).

As shown in Table 10, despite careful alignment of sensor configurations, inference areas, and voxel resolutions, these supervised methods exhibit limited generalization capabilities compared to OccAny. Notably, OccAny’s inference is straightforward and does not require any prior knowledge of the sensor configurations (number of cameras, intrinsics/extrinsics and camera poses), adapting effortlessly to any inference areas and any voxel resolutions.

Occ3D-Waymo Occ3D-NuScenes. In this setting, we evaluate CVT-Occ [81] using weights trained on Occ3D-Waymo to perform inference on Occ3D-NuScenes. While the voxel resolutions and voxel sizes are consistent between these datasets, significant differences remain in sensor configurations. To enable inference, we align the sensor setups by mapping the five Occ3D-Waymo cameras to the six Occ3D-NuScenes cameras. Specifically, we map the Occ3D-Waymo Front, Front-Right, and Front-Left to their Occ3D-NuScenes counterparts, while the Occ3D-Waymo Side-Left is mapped to both Back and Back-Left, and Side-Right to Back-Right. Regarding image resolution, we follow the official implementation to scale Occ3D-NuScenes input images to the Occ3D-Waymo training resolution of $9 6 0 ~ \times ~ 6 4 0$ . We also report inference performance at $1 6 0 0 \times 9 0 0$ , which yields slightly better results. However, as detailed in Table 10, even with these manual adaptations, the model struggles to generalize to the new domain, achieving a peak IoU of only $1 7 . 5 6 \%$ , significantly lower than the $3 4 . 1 5 \%$ achieved by our method.

# Occ3D-NuScenes/Occ3D-Waymo SemanticKITTI.

Regarding the transfer from surround-view to monocular, we evaluate two SOTA 3D supervised methods: CVT-Occ [81] and ALOcc [11]. We use checkpoints trained on Occ3D-NuScenes (for both ALOcc and CVT-Occ) and Occ3D-Waymo (for CVT-Occ) to perform inference on SemanticKITTI. This scenario presents a significantly greater challenge than the previous setting: in addition to domain shifts and sensor discrepancies (using only the source front camera to align with the target setup), there are substantial divergences in voxel grid extents and resolutions.

For CVT-Occ [81], we use two provided models, one trained on Occ3D-NuScenes $( 1 6 0 0 ~ \times ~ 9 0 0 )$ ) and another trained on Occ3D-Waymo $( 9 6 0 \times 6 4 0 )$ ). We evaluate the Occ3D-NuScenes-trained model on SemanticKITTI at full image resolution $( 1 2 2 0 \times 3 7 0 )$ , as it is closely aligned with the training resolution. For the Occ3D-Waymo-trained model, we conduct evaluations at both the full resolution and a resized resolution of $9 6 0 \times 5 4 0$ , which preserves the

Table 9. Novel-View Rendering vs. Depth Completion. Occupancy prediction results on SemanticKITTI and Occ3D-NuScenes show the effectiveness of Novel-View Rendering.   

<table><tr><td rowspan="3">Method</td><td colspan="6">Semantic KITTI</td><td colspan="6">Occ3D-NuScenes</td></tr><tr><td rowspan="2">Res.</td><td colspan="2">sequence</td><td colspan="3">monocular</td><td>Res.</td><td rowspan="2" colspan="2">sequence</td><td colspan="3">surround-view</td></tr><tr><td>Prec.</td><td>Rec.</td><td>IoU</td><td>Prec.</td><td>Rec.</td><td>IoU</td><td>Prec.</td><td>Rec.</td><td>IoU</td></tr><tr><td>OccAnydepth completion</td><td>512 × 160</td><td>24.59</td><td>44.55</td><td>18.82</td><td>21.59</td><td>37.55</td><td>15.89</td><td>512 × 288</td><td>29.80,</td><td>36.09</td><td>19.51</td><td>30.57</td></tr><tr><td>OccAny</td><td>512 × 160</td><td>36.79</td><td>46.79</td><td>25.91</td><td>45.64</td><td>33.66</td><td>24.03</td><td>512 × 288</td><td>36.09</td><td>40.39</td><td>23.55</td><td>45.04</td></tr></table>

Table 10. Generalization results of fully-supervised methods. Occ label is denser through temporal accumulation of LiDAR point-clouds and subsequent post-processing, whereas the LiDAR label remains sparser at each timestep. OccAny works out of the box in any evaluation settings with different inference areas, voxel resolutions and sensor configurations. In contrast, other methods require manual code modifications to align testing and training conditions. Beyond being more versatile, OccAny clearly demonstrates superior generalization.   

<table><tr><td rowspan="2">Label</td><td rowspan="2">Method</td><td rowspan="2">Venue</td><td colspan="4">Occ3D-NuScenes surround-view</td><td colspan="4">SemanticKITTI monocular</td></tr><tr><td>Res.</td><td>Prec.</td><td>Rec.</td><td>IoU</td><td>Res.</td><td>Prec.</td><td>Rec.</td><td>IoU</td></tr><tr><td rowspan="4">Occ</td><td>CVT-Occ [81] (Trained on Occ3D-Waymo)</td><td>ECCV&#x27;24</td><td>1600 × 900</td><td>35.38</td><td>25.86</td><td>17.56</td><td>1220 × 370</td><td>8.97</td><td>34.92</td><td>7.69</td></tr><tr><td>CVT-Occ [81] (Trained on Occ3D-Waymo)</td><td>ECCV&#x27;24</td><td>960 × 540</td><td>29.15</td><td>28.33</td><td>16.78</td><td>960 × 292</td><td>8.92</td><td>36.84</td><td>7.73</td></tr><tr><td>CVT-Occ [81] (Trained on Occ3D-NuScenes)</td><td>ECCV&#x27;24</td><td>in-domain</td><td>-</td><td>-</td><td>-</td><td>1220 × 370</td><td>11.73</td><td>59.97</td><td>9.43</td></tr><tr><td>ALOcc [11] (Trained on Occ3D-NuScenes)</td><td>ICCV&#x27;25</td><td>in-domain</td><td>-</td><td>-</td><td>-</td><td>704 × 256</td><td>16.34</td><td>53.06</td><td>14.28</td></tr><tr><td>LiDAR</td><td>OccAny</td><td>-</td><td>512 × 288</td><td>45.04</td><td>58.54</td><td>34.15</td><td>512 × 160</td><td>45.64</td><td>33.66</td><td>24.03</td></tr></table>

SemanticKITTI aspect ratio while approximating the source training resolution.

For ALOcc [11], only the model trained on Occ3D-NuScenes is available. Since ALOcc encodes the stereo cost volume’s frustum grid within its parameters, the network is constrained to a fixed input resolution of $7 0 4 \times 2 5 6$ . Consequently, we evaluate ALOcc on SemanticKITTI at this exact resolution, adhering to the official implementation by using 16 history frames and pairs of consecutive timesteps as stereo input.

The results in Table 10 highlight a significant drop in performance when these models are inferred on the unseen SemanticKITTI dataset. CVT-Occ and ALOcc achieve IoUs of only $9 . 4 3 \%$ and $1 4 . 2 8 \%$ , respectively, whereas our proposed method demonstrates superior robustness with an IoU of $2 4 . 0 3 \%$ .

# B.5. Ego Vehicle Trajectory Prediction

We assess the quality of ego-trajectory prediction using OccAny on the nuScenes validation set, following the evaluation protocol of [16, 20]. OccAny+ outperforms the base DA3-LARGE model in terms of Average Displacement Error (ADE), demonstrating clear advantages in urban scenes. Furthermore, it approaches the accuracy of optimization-based RGB-D SLAM methods while remaining fully feed-forward and significantly simpler.

Table 11. Ego Vehicle Trajectory Prediction.   

<table><tr><td>Method</td><td>ADE (m)</td></tr><tr><td>GeoCalib [60] + DroidSLAM [57] + DA2 [78]</td><td>1.63</td></tr><tr><td>DA3 large + DA3 metric large</td><td>2.44</td></tr><tr><td>OccAny+</td><td>1.86</td></tr></table>

Table 12. NVR inference complexity, measured on one A100 GPU.   

<table><tr><td>#Aug. Frames</td><td>1</td><td>2</td><td>4</td><td>8</td><td>10</td><td>20</td><td>50</td><td>100</td><td>200</td></tr><tr><td>Time (s)</td><td>0.052</td><td>0.057</td><td>0.085</td><td>0.172</td><td>0.227</td><td>0.542</td><td>1.406</td><td>2.786</td><td>5.572</td></tr><tr><td>Mem. (GB)</td><td>1.175</td><td>1.920</td><td>3.422</td><td>6.471</td><td>8.005</td><td>9.936</td><td>14.314</td><td>17.013</td><td>22.418</td></tr></table>

Table 13. Model size and speed. Train times are from the original papers. Inference times are measured in the surround setting with 6 input views and 6 render views.   

<table><tr><td>Method</td><td>Train. GPUs</td><td>Train. time</td><td>Recon. time (ms)</td><td>Render time (ms)</td><td>Params (M)</td></tr><tr><td>CUT3R</td><td>8×A100</td><td>≈30 days</td><td>240.0</td><td>259.8</td><td>793.3</td></tr><tr><td>VGGT</td><td>64×A100</td><td>&gt;9 days</td><td>222.2</td><td>-</td><td>1157.9</td></tr><tr><td>AnySplat</td><td>16×A800</td><td>≈2 days</td><td>251.7</td><td>17.2</td><td>1190.7</td></tr><tr><td>OccAny</td><td>16×A100</td><td>≈1.5 days</td><td>93.8</td><td>123.2</td><td>651.1</td></tr></table>

# B.6. NVR complexity.

We report in Tab. 12 the memory consumption and running time of NVR inference using one A100 GPU in the surround-view setting. Similar to VGGT (cf . Tab. 9 in [63]), both memory & time scale much slower w.r.t. number of augmentation frames.

# B.7. Model sizes and speeds

We are report the model sizes and speeds of OccAny and baselines in Tab. 13. OccAny has the fewest parameters $\mathrm { \sim } 6 5 1 \mathrm { M } )$ vs. CUT3R $( \sim 7 9 3 \mathbf { M } )$ and VGGT/AnySplat $( \sim 1 . 2 \mathrm { B } )$ , and is the most runtime efficient in training/inference. OccAny’s rendering is about $2 \times$ faster than CUT3R, while AnySplat’s is the fastest thanks to 3DGS.

# C. Qualitative Examples

We show additional qualitative results in Fig. 9, Fig. 10, Fig. 11, Fig. 12, and Fig. 13.

图片摘要：该图主要展示 9. Occupancy predictions of OccAny and baselines on sequenti。
![](images/a17d7146de0a5395627e536d28e1d171916da24bdf90c2fb0ca32efe30c98af1.jpg)  
Figure 9. Occupancy predictions of OccAny and baselines on sequential data. We visualize here predicted voxels. For qualitative analysis, we overlay the semantic ground-truth colors on predicted voxels to better highlight class-wise gains. False positive voxels are painted in gray without any overlayed color. Compared to baselines, our occupancy predictions are denser and more accurate.

图片摘要：该图主要展示 9. Occupancy predictions of OccAny and baselines on sequenti。
![](images/41d10a42e09dd33742d4b00199c402262c758af569dc9feaf97a07d7804af776.jpg)  
Figure 10. Occupancy predictions of OccAny and baselines on surround-view data. Voxel colorization follows Fig. 9. Compared to baselines, our occupancy predictions are denser and more accurate.

图片摘要：该图主要展示 10. Occupancy predictions of OccAny and baselines on surroun。
![](images/849f1bf34626742c4da1b3fcfc797ac1439cf1c544d00c55569b070dfef884e5.jpg)  
Figure 11. Qualitative ablation on Semantic KITTI shows the gains from Segmentation Forcing and Novel-View Rendering. Voxel colorization follows Fig. 9. The two proposed strategies significantly improve the density and the accuracy of occupancy predictions.

图片摘要：该图主要展示 11. Qualitative ablation on Semantic KITTI shows the gains f。
![](images/034bb9d2cd73589a76c05fabd7f94a18928bbe2800df8d4d357566213218d7ae.jpg)  
Figure 12. Qualitative ablation on Occ3D-NuScenes shows the gains from Segmentation Forcing and Novel-View Rendering. Voxel colorization follows Fig. 9. The two proposed strategies significantly improve the density and the accuracy of occupancy predictions.

图片摘要：该图主要展示 12. Qualitative ablation on Occ3D NuScenes shows the gains f。
![](images/24e7e20b127aae510bb70e406ef8b4f6999cda2f3ae13cdaa90477a25e030f0f.jpg)  
Figure 13. PCA visualization of predicted feature maps. Low-resolution features capture high-level semantics (e.g., separating cars, buildings, and roads), while high-resolution features capture low-level details such as boundaries and textures. Features remain consistent across different views.
