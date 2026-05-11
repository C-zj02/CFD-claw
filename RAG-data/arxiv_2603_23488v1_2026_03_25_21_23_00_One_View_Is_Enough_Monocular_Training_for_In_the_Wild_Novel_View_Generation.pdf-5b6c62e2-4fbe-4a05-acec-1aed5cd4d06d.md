# One View Is Enough! Monocular Training for In-the-Wild Novel View Generation

Adrien Ramanana Rahary $^ { 1 , 2 } \oplus$ , Nicolas Dufour $^ 1 \oplus$ , Patrick Pére $^ 1 \oplus$ , and David Picard2

1 Kyutai, {adrienrr,nicolas.dufour, patrick}@kyutai.org   
2 LIGM, ENPC, IP Paris, CNRS, UGE, david.picard@enpc.fr

图片摘要：该图片为文档封面或首页内容，主题与One View Is Enough! Monocular Training for In the Wild Novel View Generation相关。
![](images/382a5e4babc666580d8414a3718476552f9c09efdce8738e285b4eecb2b83d13.jpg)  
Camera   
Indoor   
Outdoor   
Subjectcentric   
Nonnatural

图片摘要：该图片为文档封面或首页内容，主题与One View Is Enough! Monocular Training for In the Wild Novel View Generation相关。
![](images/209ff86a1e3f1413536413ad0b2d06507bcb8278c43432a8868bffe800c75c70.jpg)  
Source

图片摘要：该图主要展示 1: OVIE generates novel views from a single image across div。
![](images/18d657476ea394ce81a4f686954d6be1d4cbea343646f6307f3848bc6e870cfc.jpg)  
View 1

图片摘要：该图主要展示 1: OVIE generates novel views from a single image across div。
![](images/69b8ef016ecd5e51c10fb0044a1da9c028bef877013a2db90206d7ab1ac56e43.jpg)  
View 2

图片摘要：该图主要展示 1: OVIE generates novel views from a single image across div。
![](images/6a2bb3d878dbb41b806ba4ded0f2f931dc5773cb688811ad27193a017d9b0c64.jpg)  
View 3   
Fig. 1: OVIE generates novel views from a single image across diverse domains given a source image (gray) and target poses (colored), regardless of content or style.

Abstract. Monocular novel-view synthesis has long required multi-view image pairs for supervision, limiting training data scale and diversity. We argue it is not necessary: one view is enough. We present OVIE , trained entirely on unpaired internet images. We leverage a monocular depth estimator as a geometric scaffold at training time: we lift a source image into 3D, apply a sampled camera transformation, and project to obtain a pseudo-target view. To handle disocclusions, we introduce a masked training formulation that restricts geometric, perceptual, and textural losses to valid regions, enabling training on 30 million uncurated images. At inference, OVIE is geometry-free, requiring no depth estimator or 3D representation. Trained exclusively on in-the-wild images, OVIE outperforms prior methods in a zero-shot setting, while being $6 0 0 \times$ faster than the second-best baseline. Code and models are publicly available at https://github.com/AdrienRR/ovie.

Keywords: View synthesis $\cdot$ Unpaired training $\cdot$ Domain generalization

# 1 Introduction

A single photograph of a cathedral freezes a moment from one viewpoint, yet a human viewer effortlessly imagines how the scene looks from a dozen others. Replicating this capacity computationally to generate plausible views of a scene from previously unobserved camera positions is the problem of novel view synthesis. It is key in applications where a system must reason about three-dimensional space from two-dimensional observations: allowing a robot to plan around obstacles it has only glimpsed from one side, or letting a filmmaker explore virtual camera angles through a set that was only partially photographed. When the input is restricted to a single image, the problem becomes even more practical: a capable monocular novel view synthesis model would generalize across virtually any image ever captured, making immersive 3D understanding available at the scale of the internet. Despite significant recent progress, this level of generalization remains out of reach, and the reason is structural.

Current approaches to monocular novel view synthesis depend on multi-view supervision. They require training datasets of posed, static multi-view captures from which to extract geometric correspondences, and such datasets are rare. The community has converged on a small collection of purpose-built benchmarks, like RealEstate10K [78] or DL3DV [30], which cover only a narrow slice of the visual world. Synthetic datasets derived from 3D asset libraries such as Objaverse [14, 15] extend coverage somewhat, but introduce a domain gap that limits real-world performance. Video, despite its apparent abundance, does not fill this gap: video collections inevitably contain dynamic elements such as people and vehicles that violate the static-scene assumption and corrupt geometric supervision. Models trained on available data generalize within their training domains but fail elsewhere. This is a critical limitation for broad applicability.

The key observation driving this work is that monocular depth estimation has matured to the point where it can serve as a source of geometric supervision. A modern depth estimator applied to a single image produces a 3D point cloud that can be transformed and reprojected from a novel camera pose, yielding a partial rendering of the scene from a new viewpoint. This partial rendering is sparse where geometry is occluded or disoccluded, but faithful where it is not, and it constitutes what we call a pseudo-novel view: an imperfect but usable training target that requires no multi-view capture and no controlled recording conditions. As shown in Figure 1, this reframing transforms any single image into a source-target training pair, removing the dependency on multi-view data entirely and opening training to arbitrary image collections.

This insight directly shapes our method. At training time, we construct pseudo-pairs by lifting a source image into 3D using a pretrained depth estimator, sampling a novel camera pose, and reprojecting the pointcloud to obtain a partial target image. Our model takes as input only the source image and the target camera pose, and directly outputs a synthesized image in pixel space. It produces no intermediate 3D representation, requires no geometric input beyond the pose, and performs no per-scene optimization. To handle partial pseudotargets, the reconstruction loss is restricted to observed regions. For perceptual

supervision, both images are masked before the feature extractor, so the loss matches features only on available pixels. We further add a PatchGAN adversarial term between the source and the generated image to enforce realistic texture synthesis in unobserved regions. Incidentally, using a metric depth estimator endows the model with metric scale awareness, since pseudo-pair translations are expressed in metric units, in contrast to methods trained on SLAM-derived poses which are scale-ambiguous.

Trained on 30 million in-the-wild images from ImageNet-21K [49], Places [76], Open Images [28], and OpenStreetView5M [1], without any multi-view supervision, the model demonstrates strong generalization. On RealEstate10K [78] and DL3DV [30], two benchmarks unseen during training, performance is competitive across both settings. On RealEstate10K, the final model rivals or outperforms state-of-the-art geometry-free monocular methods, despite those baselines being trained in-domain. On DL3DV, an out-of-domain dataset for all compared methods i.e. a more balanced setting, the model surpasses all baselines.

Our contributions are as follows:

– A data-scalable, domain-agnostic, metric training paradigm: Pseudo-novel views from monocular depth estimation enable training entirely on singleimage collections, removing the need for multi-view data. Analysis shows data scale matters more than diversity, but that broader data coverage, even from distant domains, can yield marginal gains. Incorporating a metric depth estimator further grants metric scale awareness, removing the need for scale-calibrated supervision at test time.

– An efficient geometry-free model design: A feed-forward architecture maps a source image and target camera pose directly to a synthesized image in pixel space, optimized via pixel-level, input-masked perceptual, and adversarial losses. This streamlined design achieves inference at over 100 FPS, more than 600 $\times$ faster than the next fastest baseline. This throughput enables a real-time interactive navigation from a single image.

– Strong out-of-domain generalization: Training on large-scale in-the-wild images without multi-view supervision yields a model that is competitive with or superior to in-domain methods on established benchmarks. The model robustly generalizes to unseen domains where prior methods experience significant degradation.

# 2 Related Work

Problem setting. Novel view synthesis (NVS) encompasses tasks with significant differences in input, output and generalization scope. Per-scene optimization methods [27, 35] fit a scene representation to tens or hundreds of posed views and generalize only within that scene. Multi-view feed-forward methods [8,10,11, 24,62,77] generalize across scenes but require multiple source images at inference. Feed-forward reconstruction methods [34,58,59,68,70] predict 3D representations (Gaussians splattings or radiance fields) from a single image, yet remain largely object-centric. We address monocular scene-level novel view synthesis: given a

single image of an arbitrary scene and a target camera pose, synthesize the target view in one feed-forward pass with a model that generalizes across scenes and domains.

Monocular NVS with multi-view supervision. The dominant paradigm trains feed-forward models on posed multi-view collections, from which geometric correspondences can be extracted as supervision. SynSin [66] established this paireddata approach; NViST [23] scaled it to MVImgNet [73]. Geometry-free, poseconditioned image-to-image models—SRT [51], GeoGPT [50], PhotoNVS [71], and VIVID [17]—represent the family most related to ours, synthesizing the target view directly in pixel space without an explicit 3D representation. All share a structural bottleneck: they require posed, static multi-view datasets (e.g., RealEstate10K [78], DL3DV [30], ScanNet [13]), which as noted in Section 1 cover only a narrow visual domain. OVIE requires no multi-view data or posed images, training instead on 30 million unconstrained single images from domains these benchmarks do not reach.

Monocular novel view synthesis without multi-view supervision. Learning novel view synthesis without posed pairs has been explored primarily through 3Daware generative models trained on unposed image collections. HoloGAN [37], GRAF [54], $\pi$ -GAN [6], EG3D [7], GIRAFFE [38] and GET3D [20] learn implicit, tri-plane, or mesh-based 3D representations from such collections and render images from them; applying these unconditional generators to a real input image requires test-time GAN inversion [80], which is slow, per-image, and confined to the category distribution of the training data. [44] and G3DR [47] build NVS frameworks directly around this inversion paradigm but similarly remain restricted to object-centric, category-specific settings. The broader challenge of learning without paired views echoes CycleGAN [81], though cycle-consistency in 2D image space does not extend to 3D viewpoint change. Another line of work avoids pairs by supervising on single images with 3D bounding box annotations [33], achieving spatial but not detail consistency across viewpoints, and trading one scarce signal for another. OVIE escapes all these restrictions, training on 30 million unconstrained single images with no category prior, canonical pose distribution, or test-time optimization.

Large generative priors for novel view synthesis. An alternative strategy finetunes large pretrained generative models whose internet-scale training has absorbed implicit 3D knowledge: Zero-1-to-3 [31] adapts Stable Diffusion [18] on Objaverse [15] renders for object-level view synthesis; ViewCrafter [72] conditions DynamiCrafter [67] on DUSt3R [65] point-cloud renders for scene-level pose control; Stable Virtual Camera [77] fine-tunes a Stable Diffusion [18] backbone with 3D attention and Plücker ray conditioning for generalist multi-view synthesis; and PE-Field [2] replaces the 2D positional encodings of a pretrained Flux.1 Kontext [29] with depth-aware 3D encodings. These methods share two costs that OVIE avoids: iterative sampling through a large generative model makes inference expensive, and geometric consistency still requires fine-tuning on posed multi-view datasets, reintroducing the domain restriction the generative prior was meant to overcome.

Monocular depth estimation. Learning-based depth estimation splits into two branches. The relative branch (MiDaS [4, 46], DPT [45], Depth Anything [69], Marigold [25, 26], MoGe [63]) yields affine-invariant predictions. The metric branch (ZoeDepth [3], UniDepth [42, 43], MoGe-2 [64]) additionally recovers absolute scale. OVIE exploits this: metric depth lets us construct pseudo-pairs with true metric translations at training time, providing geometric supervision without any manual annotation.

Warping-based novel view synthesis. Warping-based methods unproject the source image into an explicit 3D representation and inpaint disoccluded regions, via layered depth inpainting [39, 56], soft point-cloud rendering [22, 66], MPI blending [60,79], or diffusion-based warp-then-inpaint pipelines such as GenWarp [55] and LucidDreamer [12]. MultiDiff [36] similarly conditions a video diffusion model on depth-warped reference images and warped noise at inference, tying its output quality to the accuracy of the depth estimate. Because the depth estimator is load-bearing at inference, its failures propagate directly to the output. OVIE is not warping-based: it requires no depth estimate at inference, and is therefore immune to the error accumulation that plagues methods which rely on depth at test time.

Geometry-free monocular novel view synthesis. Geometry-free methods map a source image and target pose directly to the new view, with no explicit 3D representation. They typically require posed multi-view data to learn geometric reasoning, as in Zero-1-to-3 [31], ZeroNVS [52], SRT [51], GeoGPT [50], PhotoNVS [71] and VIVID [17]. OVIE belongs to this family, but requires no posed multi-view data for training. Instead, it uses metric depth as an offline scaffold to construct pseudo-pairs with true metric translations for supervision, acquiring geometric understanding without any ground-truth pairs or poses.

# 3 Method

This section presents a framework for monocular novel view synthesis, trained entirely on unpaired image collections. A frozen monocular depth estimator constructs training pairs on the fly, enabling the pose-conditional image-to-image model to learn purely from pseudo-supervision.

More formally, given a source image $I _ { 0 } \in \mathbb { R } ^ { H \times W \times 3 }$ and a relative camera transformation $T _ { 0 \to 1 } \in S E ( 3 )$ specifying the target viewpoint, the objective is to synthesize a novel view $\hat { I } _ { 1 } \in \mathbb { R } ^ { H \times W \times 3 }$ that matches the true appearance $I _ { 1 }$ of the scene from this viewpoint.

# 3.1 Overview

To train exclusively on single-image collections, our framework relies on two core components: on-the-fly training-pair generation and partial supervision. First, a pretrained monocular depth network lifts each source image into 3D. The resulting point cloud is re-projected under sampled camera poses, yielding sparse novel views together with binary validity masks. Finally, a pose-conditional

图片摘要：该图主要展示 2: Method overview. Top: From web sourced images , a frozen 。
![](images/f5cde02967b6798232ba7d3feb01a401c7a3a52bcfd1288ab907817fb4ea1613.jpg)  
Pseudo Ground-Truth Generation

图片摘要：该图主要展示 2: Method overview. Top: From web sourced images , a frozen 。
![](images/2a253fe667d4e3a8aa6d7f4ee3ece23a24f3f856ec355e0d869471a6a7ba69c9.jpg)  
Fig. 2: Method overview. Top: From web-sourced images $I _ { 0 }$ , a frozen monocular depth estimator extracts per-image 3D point clouds $\mathcal { P }$ . We then sample camera transformations $T _ { 0 \to 1 } \in S E ( 3 )$ (rotation and translation), apply them to the point clouds, and reproject to generate pseudo-target views $I _ { 1 } ^ { * }$ . Bottom: Our model $f _ { \theta }$ takes a source image $I _ { 0 }$ and, conditioned on a camera transformation $T _ { 0  1 }$ , predicts the corresponding novel view $\hat { I } _ { 1 }$ . Training combines a masked reconstruction loss $\mathcal { L } _ { \mathrm { r e c o n } }$ and perceptual loss $\mathcal { L } _ { \mathrm { p e r c } }$ between $\hat { I } _ { 1 }$ and $I _ { 1 } ^ { * }$ , and an adversarial loss $\mathcal { L } _ { \mathrm { a d v } }$ where the discriminator $D _ { \phi }$ distinguishes source images $I _ { 0 }$ from predicted views $\hat { I } _ { 1 }$ .

image-to-image network uses these sparse views as pseudo-ground-truth to synthesize high-fidelity novel viewpoints. The full pipeline is shown in Fig. 2.

At inference, the depth estimator and projection pipeline are discarded entirely. The trained model requires only a source image and a target pose, reducing novel view synthesis to a single forward pass with no 3D data structures, point clouds, or warped inputs.

# 3.2 Annotation-Free Training Pair Construction

Depth-Based Scene Lifting. A pretrained monocular depth network processes the source image $I _ { 0 }$ , estimating a depth map $D \in \mathbb { R } ^ { H \times W }$ and surface normals $N \in \mathbb { R } ^ { H \times W \times 3 }$ . Together, these quantities define a point cloud $\mathcal { P } \in \mathbb { R } ^ { H W \times 3 }$ in the source camera coordinate system via standard unprojection.

Viewpoint Sampling and Reprojection. A transformation $T _ { 0 \to 1 } \in S E ( 3 )$ is then sampled from a distribution of plausible viewpoint changes derived from the scene geometry (see Supplementary for details). Rigidly transforming $\mathcal { P }$ by $T _ { 0  1 }$ and reprojecting onto the target image plane yields a pseudo-ground-truth target view $I _ { 1 } ^ { * }$ and a binary visibility mask $M \in \{ 0 , 1 \} ^ { H \times W }$ , where $M _ { i j } = 1$ denotes a

valid reprojected pixel and $M _ { i j } = 0$ marks disocclusions, occlusion boundaries, backface-culled regions (computed from $N$ ), and out-of-frame content.

Metric-Scale Supervision. When the depth model produces metric-scale estimates, MoGE-2 [64] in our case, the resulting pairs carry true metric changes, enabling real-world scale grounding, a class of supervision considerably scarcer than standard pose-annotated data and largely underexplored in the literature.

# 3.3 Training Objective

We propose to use a multi-term objective which enforces geometric accuracy, semantic consistency, and textural realism. Because the pseudo-target $I _ { 1 } ^ { * }$ contains missing content, every loss term accounts for unobserved regions via the mask $M$ .

Geometric Consistency. The primary supervision is a masked reconstruction loss. Pseudo-targets may contain residual errors where depth estimation fails; experiments comparing mean absolute error and the Charbonnier penalty [9] against mean squared error show that MSE yields more stable convergence and better preserves high-frequency detail. The reconstruction loss is:

$$
\mathcal {L} _ {\text {r e c o n}} = \frac {\left\| M \odot \hat {I} _ {1} - M \odot I _ {1} ^ {*} \right\| _ {2} ^ {2}}{\| M \| _ {1} + \epsilon}, \tag {1}
$$

where $\epsilon > 0$ prevents division by zero.

Semantic Preservation. To improve visual quality on top of accurate reconstruction, we apply perceptual losses to the prediction. Since the pseudo-target is sparse, we mask both the prediction and target prior to feature extraction, preventing spurious activations and restricting the loss to valid regions. Following [32], LPIPS [74] is combined with P-DINO, a patch-level loss derived from activations of a pretrained DINO model [5, 40, 57]:

$$
\mathcal {L} _ {\text {p e r c}} = \lambda_ {\text {L P I P S}} \mathcal {L} _ {\text {L P I P S}} \left(M \odot \hat {I} _ {1}, M \odot I _ {1} ^ {*}\right) + \lambda_ {\text {D I N O}} \mathcal {L} _ {\text {P - D I N O}} \left(M \odot \hat {I} _ {1}, M \odot I _ {1} ^ {*}\right), \tag {2}
$$

where $\mathcal { L } _ { \mathrm { P - D I N O } } ( \mathbf { x } , \mathbf { y } ) = 1 - \cos ( \mathrm { D I N O } ( \mathbf { x } ) , \mathrm { D I N O } ( \mathbf { y } ) )$ , and $\lambda _ { \mathrm { L P I P S } } , \lambda _ { \mathrm { D I N O } } > 0$ are scalar weights balancing the two perceptual terms. Pixel-wise masking deactivates unobserved regions in both images, suppressing invalid gradients while preserving the role of the extractor as a consistent feature matcher.

High-Frequency Realism. An adversarial objective sharpens high-frequency detail via a PatchGAN discriminator $D _ { \phi }$ [21]. Because the incomplete $I _ { 1 } ^ { * }$ cannot serve as a reliable real sample, the source image $I _ { 0 }$ represents the real distribution instead, a valid proxy under the assumption that local texture statistics are consistent across views:

$$
\mathcal {L} _ {\mathrm {a d v}} = \mathbb {E} _ {I _ {0}} [ \log D (I _ {0}) ] + \mathbb {E} _ {\hat {I} _ {1}} [ \log (1 - D (\hat {I} _ {1})) ]. \qquad (3)
$$

The discriminator follows the StyleGAN-T [53] design, using a pretrained representation backbone. The adaptive weight wadap from VQ-GAN [19] balances

reconstruction and adversarial terms automatically. More details are provided in the supplementary material.

Total Objective. The total loss combines all three terms:

$$
\mathcal {L} _ {\text {t o t a l}} = \mathcal {L} _ {\text {r e c o n}} + \mathcal {L} _ {\text {p e r c}} + \lambda_ {\mathrm {a}} \cdot w _ {\text {a d a p}} \cdot \mathcal {L} _ {\text {a d v}}, \tag {4}
$$

where $\lambda _ { \mathrm { a } } > 0$ controls the contribution of the adversarial term and $w _ { \mathrm { a d a p } }$ is the adaptive weight from VQ-GAN [19]. Together, these terms enforce geometric fidelity, semantic coherence, and perceptual realism, with all hyperparameters specified in the supplementary material.

# 3.4 Model Architecture

A convolutional encoder first downsamples the source image $I _ { 0 }$ into a dense feature map, which is then processed by a stack of pose-conditioned Transformer blocks. A mirrored convolutional decoder finally upsamples this representation back to the source resolution, producing $\hat { I } _ { 1 }$ .

Pose Conditioning. The relative transformation $T _ { 0  1 }$ is encoded as a 7D vector $\mathbf { p } \in \mathbb { R } ^ { 7 }$ (3D translation and unit quaternion), following VGGT [61] but omitting camera intrinsics, which are rarely available at deployment. A linear layer $W$ projects $\mathbf { p }$ into a conditioning token $\mathbf { c } = W \mathbf { p } \in \mathbb { R } ^ { d }$ , which modulates each Transformer block via Adaptive Layer Normalization (AdaLN) [41]. Further details appear in the supplementary material.

# 4 Experiments

We evaluate OVIE across five axes: qualitative generalization (Figure 3), a quantitative comparison on RealEstate10K where all baselines are in-domain while OVIE is not, a fair out-of-domain comparison on DL3DV (Table 1), ablations of loss design and training data (Table 2 and Figure 5), and a throughput analysis situating OVIE as a practical real-time navigation model (Figure 6).

# 4.1 Experimental Setup

Training Data. OVIE is trained on 30 million in-the-wild images drawn from four public collections: ImageNet-21K [49], Open Images [28], OSV5M [1], and Places [76]. No part of any training set overlaps with our evaluation benchmarks. No ground-truth multi-view pairs, depth annotations or camera poses are used at train time. Pseudo-pairs are generated on-the-fly using MoGe-2 [64]: it predicts metric depth, from which camera transformations are sampled in metric units.

Evaluation Benchmarks. We compare against baselines on both RealEstate10K [78] and DL3DV [30]. Ablation studies and data scaling experiments are conducted on both RealEstate10K and DL3DV. OVIE has never been trained on either dataset.

图片摘要：该图主要展示 3: Qualitative comparison with state of the art methods. Giv。
![](images/2a6877c96b01ed951e7eb9916fa9b5423a07683d5e922e7e3145c42f7b835e15.jpg)

图片摘要：该图主要展示 3: Qualitative comparison with state of the art methods. Giv。
![](images/8d41d0f7df440c15e30ac09bcf8bf8f1ee2c501f82cc13b93d0417204dead3af.jpg)

图片摘要：该图主要展示 3: Qualitative comparison with state of the art methods. Giv。
![](images/0d26c30ea9033e7c1b7590cccf4c375df61fc0e94794b3921bd635624f5b3f4a.jpg)  
Fig. 3: Qualitative comparison with state-of-the-art methods. Given a source image and a target camera pose, each method synthesizes a novel view. Despite never being trained on multi-view data, OVIE produces sharp novel views with consistent geometry and accurately follows camera pose changes. Concurrent methods can fail to enforce the target pose entirely, or produce geometrically inconsistent results.

Baselines. GeoGPT [50], PhotoNVS [71], and VIVID [17] are recent geometryfree pose-conditioned image-to-image methods that share our problem formulation: given a source image and a relative camera transformation, they synthesize the target view directly in pixel space without producing an explicit 3D representation. All three are trained on RealEstate10K, and evaluated using the pretrained models released by their authors. This creates a deliberate asymmetry: on RealEstate10K, all baselines are in-domain while OVIE is out-of-domain; on DL3DV, all methods are out-of-domain, making it a fair comparison for all.

Metrics. PSNR and SSIM measure pixel-level fidelity, LPIPS perceptual similarity, and FID distributional realism. The evaluation protocol follows prior work [2, 48]: (1) a starting frame is sampled from each of 750 scenes; (2) 14 novel views are generated independently from that frame, at a stride of 3 for

图片摘要：该图主要展示 3: Qualitative comparison with state of the art methods. Giv。
![](images/84b39b977da04f4afe43d47daf881b7b23bd5c608950ee4bd2306bc4c40f2cf2.jpg)

图片摘要：该图主要展示 3: Qualitative comparison with state of the art methods. Giv。
![](images/ac7e02c2b6ca5eef6e76ad7acaba34194adad1572c2404d3aa3f1c9472d983a8.jpg)  
Fig. 4: Metric scale understanding. The same 20 cm camera translation is applied to two scenes of different physical scales. The close-up banana (left, 50 cm away) undergoes a large apparent displacement, while the room-scale scene (right, 3 m away) shows a proportionally smaller shift consistent with metrically correct parallax.

RealEstate10K and 1 for DL3DV; (3) metrics are averaged over all scenes, with FID computed over all generated and source images. Since benchmark poses are derived from SLAM and are therefore scale-ambiguous, a per-scene scale sweep is performed independently for each method, selecting the value that maximizes its own performance. Optimizing scale per method rather than using a shared value ensures that no method is disadvantaged by a systematic scale mismatch, making the comparison fair across all approaches.

Implementation Details. The encoder spatially downsamples the source image by 8 $\times$ via convolutions, with a channel dimension matching the Transformer hidden size. The bottleneck follows a ViT-B architecture with 768 hidden dimensions [16], and a convolutional decoder upsamples back to the original resolution. The full model is trained for 2M steps with a batch size of 512 on a mix of 30M images from ImageNet21K, Places, and OpenImages, while ablations and data influence experiments use models trained for 250K steps at the same batch size. Full architectural details and hyperparameters are provided in the supplementary material.

# 4.2 Qualitative Results

Figure 1 illustrates four facets of OVIE ’s generalization capability. For indoor (1st row) and outdoor (2nd row) scenes, OVIE produces geometrically consistent novel views with well-preserved structure and texture. For object-centric images (3rd row), the model generalizes cleanly on a distribution that differs substantially from typical novel view synthesis data. For non-photographic content such as paintings (fourth row), OVIE synthesizes plausible viewpoint changes on imagery that would be impossible to supervise with true multi-view data.

Figure 3 compares novel views generated by OVIE against concurrent methods. Despite not being trained on the evaluation dataset used by these methods,

OVIE produces novel views of comparable or superior quality. It exhibits strong geometric consistency (house details, first row), more accurate parallax rendering (table perspective, 2nd row), more faithful adherence to input camera target positions while other methods can ignore or incorrectly enforce them (3rd row), and convincing inpainting of unobserved regions (half-open door, last row).

Finally, Figure 4 illustrates the metric scale awareness that OVIE inherits from MoGE-2, the frozen depth estimator used to build pseudo-targets. When the same camera transformation is applied to images captured at different distances from the subject, OVIE produces correctly scaled parallax: objects that are physically closer undergo larger apparent displacement than those in expansive scenes under the same translation. This behavior emerges naturally from training on metric pseudo-pairs and requires no scale calibration at test time.

# 4.3 Comparison with State of the Art

RealEstate10K: competing at a disadvantage. Despite no RealEstate10K training, OVIE outperforms 2 of the 3 in-domain baselines (Table 1), and remains competitive with VIVID, the strongest in-domain baseline. The remaining gap between OVIE and VIVID is consistent with the domain disadvantage rather than a limitation of the approach, as the DL3DV results confirm.

DL3DV: a fair out-of-domain comparison. When all methods face the same domain shift on DL3DV, OVIE outperforms all baselines on all metrics. This observation is consistent with the hypothesis that the diversity of OVIE ’s largescale training data confers a robustness to distribution shifts that in-domain specialization does not provide.

# 4.4 Ablation Studies

Loss terms. Each loss term in our objective serves a distinct role, as Table 2 shows. Removing all learned losses yields the highest PSNR and SSIM on both benchmarks (19.6 dB / 0.627 on RealEstate10K, 15.7 dB / 0.441 on DL3DV), yet LPIPS degrades to 0.416 / 0.627 and FID collapses to 62.1 / 111.0, demonstrating that pixel-level metrics reward blurry, regression-to-the-mean predictions and should not serve as the sole evaluation criterion for generative models.

Table 1: Quantitative comparison on RealEstate10K and DL3DV. ↑ higher is better; $\downarrow$ lower is better. Bold: best; underline: second best. OOD: method was not trained on the evaluated benchmark.   

<table><tr><td rowspan="2">Method</td><td colspan="5">RealEstate10K [78]</td><td colspan="5">DL3DV [30]</td></tr><tr><td>OOD</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>FID↓</td><td>OOD</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>FID↓</td></tr><tr><td>GeoGPT [50]</td><td>X</td><td>15.25</td><td>0.480</td><td>0.446</td><td>18.0</td><td>✓</td><td>13.1</td><td>0.339</td><td>0.560</td><td>35.9</td></tr><tr><td>PhotoNVS [71]</td><td>X</td><td>18.9</td><td>0.601</td><td>0.314</td><td>10.6</td><td>✓</td><td>13.8</td><td>0.349</td><td>0.525</td><td>37.6</td></tr><tr><td>VIVID [17]</td><td>X</td><td>20.5</td><td>0.661</td><td>0.241</td><td>4.26</td><td>✓</td><td>14.5</td><td>0.362</td><td>0.471</td><td>18.0</td></tr><tr><td>OVIE (ours)</td><td>✓</td><td>18.8</td><td>0.602</td><td>0.279</td><td>6.74</td><td>✓</td><td>14.8</td><td>0.369</td><td>0.464</td><td>13.6</td></tr></table>

Table 2: Loss ablation studies on RealEstate10K and DL3DV. Each group varies one design axis while keeping all others at the default configuration (bold).   

<table><tr><td rowspan="2">P-DINO</td><td rowspan="2">LPIPS</td><td rowspan="2">GAN</td><td colspan="4">RealEstate10K [78]</td><td colspan="4">DL3DV [30]</td></tr><tr><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>FID↓</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>FID↓</td></tr><tr><td colspan="11">Loss component ablation</td></tr><tr><td>✓</td><td>✓</td><td>✓</td><td>18.9</td><td>0.596</td><td>0.284</td><td>7.12</td><td>15.0</td><td>0.373</td><td>0.468</td><td>14.3</td></tr><tr><td></td><td>✓</td><td>✓</td><td>19.0+0.1</td><td>0.599+0.03</td><td>0.288+0.04</td><td>8.34+1.22</td><td>15.1+0.1</td><td>0.377+0.04</td><td>0.472+0.04</td><td>15.7+1.4</td></tr><tr><td>✓</td><td></td><td>✓</td><td>18.7-0.2</td><td>0.592-.004</td><td>0.297+.013</td><td>8.43+1.31</td><td>14.9-0.1</td><td>0.371-.002</td><td>0.478+.010</td><td>15.3+1.0</td></tr><tr><td></td><td></td><td>✓</td><td>18.7-0.2</td><td>0.584-.012</td><td>0.367+.083</td><td>18.7+11.6</td><td>14.9-0.1</td><td>0.368-.005</td><td>0.540+.072</td><td>27.0+12.7</td></tr><tr><td>✓</td><td>✓</td><td></td><td>19.2+0.3</td><td>0.598+.002</td><td>0.301+.017</td><td>13.4+6.28</td><td>15.4+0.4</td><td>0.375+.002</td><td>0.496+.028</td><td>48.5+34.2</td></tr><tr><td></td><td></td><td></td><td>19.6+0.7</td><td>0.627+.031</td><td>0.416+.132</td><td>62.1+55.0</td><td>15.7+0.7</td><td>0.441+.068</td><td>0.627+.159</td><td>111.0+96.7</td></tr><tr><td colspan="11">Reconstruction loss</td></tr><tr><td>L2</td><td></td><td></td><td>18.9</td><td>0.596</td><td>0.284</td><td>7.12</td><td>15.0</td><td>0.373</td><td>0.468</td><td>14.3</td></tr><tr><td>L1</td><td></td><td></td><td>18.5-0.4</td><td>0.594-.002</td><td>0.297+.013</td><td>8.57+1.45</td><td>14.5-0.5</td><td>0.367-.006</td><td>0.477+.009</td><td>14.3-0.0</td></tr><tr><td>Charbonnier</td><td></td><td></td><td>18.5-0.4</td><td>0.592-.004</td><td>0.296+.012</td><td>8.35+1.23</td><td>14.5-0.5</td><td>0.367-.006</td><td>0.476+.008</td><td>14.1-0.2</td></tr></table>

Removing P-DINO while retaining LPIPS raises FID from 7.12 to 8.34 on RealEstate10K and from 14.3 to 15.7 on DL3DV, indicating that P-DINO provides complementary perceptual supervision beyond what LPIPS captures. Removing LPIPS while retaining P-DINO similarly degrades FID to 8.43 / 15.3 and LPIPS to 0.297 / 0.478 on RealEstate10K / DL3DV respectively, confirming that the two losses address distinct aspects of perceptual quality. Removing both perceptual losses together sharply worsens FID to 18.7 on RealEstate10K and 27.0 on DL3DV, consistent with their additive contribution. Removing the adversarial loss degrades FID to 13.4 on RealEstate10K and 48.5 on DL3DV while slightly improving PSNR to 19.2 dB / 15.4 dB, suggesting the GAN term contributes to recovering high-frequency detail at a modest cost to pixel-level accuracy. The GAN loss impact is particularly pronounced on DL3DV, where FID increases by 34.2 points compared to 6.28 on RealEstate10K, suggesting that adversarial training is especially important for out-of-domain generalization.

Reconstruction loss. One might expect that robust losses such as L1 or the Charbonnier penalty [9] would outperform L2 by suppressing the influence of erroneous depth estimates in the pseudo-targets. As Table 2 shows, the opposite is true: L2 outperforms both alternatives across all metrics on RealEstate10K and on most metrics on DL3DV (Charbonnier edges out L2 only on DL3DV FID by 0.2 points).

# 4.5 Data Scaling and Diversity

Training at internet scale on unpaired images is central to OVIE ’s design. Two controlled experiments isolate the contributions of scale and diversity: scale is the primary driver of performance, with diversity providing an additional gain at fixed budget.

Effect of data scale. Training on more data consistently improves performance. Figure 5 reports PSNR and FID for models trained on subsampled versions of our full dataset at 3K, 30K, 300K, 3M, and 30M images, with source proportions

图片摘要：该图主要展示 5: Scaling with dataset size. PSNR and FID on RealEstate10K 。
![](images/539475f5787a76b75175197f60b04826d61a83eef99a4c292cbe8a78ff751888.jpg)

图片摘要：该图主要展示 5: Scaling with dataset size. PSNR and FID on RealEstate10K 。
![](images/f57bfab5e947f2d2536957b5f98a0cc8f952669fecfd8c3c445748ee86315e46.jpg)  
Fig. 5: Scaling with dataset size. PSNR and FID on RealEstate10K as a function of training set size. Both metrics improve consistently as data volume increases. SSIM and LPIPS curves, which follow the same trend, are reported in the Supplementary.

preserved across scales (SSIM and LPIPS curves, which follow the same trend, are in the supplementary material). For context, dedicated multi-view datasets such as RealEstate10K and DL3DV contain on the order of 10K scenes.

Effect of data diversity. To isolate diversity from scale, we train four models each on a single data source subsampled to 2M images (the size of our smallest source, Places), covering ImageNet-21K, OSV5M, Places, and Open Images. We also train a mixed model on a combination of all four sources at the same total budget, preserving their original proportions. Results are reported in Table 3.

Single-source models perform broadly comparably across both benchmarks. On RealEstate10K, OSV5M underperforms the others (FID 8.59 vs. 7.20–7.42) due to domain shift. On DL3DV, OpenImages is the strongest single source (FID 14.8), while Places shows the largest gap (FID 20.3). The mixed model consistently improves over or matches the best single-source baseline (FID 7.08 on RE10K, 14.2 on DL3DV), showing that incorporating diverse domains yields a modest but reliable gain.

Relative contributions. Comparing the two data-focused experiments, scaling the training set yields larger gains than changing dataset composition at fixed scale. Data scale is therefore the more important axis, while diverse mixing provides a complementary and essentially free benefit when assembling large training sets.

Table 3: Comparison of data coverage on model performance on RealEstate10K and DL3DV. All datasets are scaled to 2M samples. Bold: best; underline: second best. Differences are relative to the Mix baseline.   

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Domain</td><td colspan="4">RealEstate10K [78]</td><td colspan="4">DL3DV [30]</td></tr><tr><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>FID↓</td><td>PSNR↑</td><td>SSIM↑</td><td>LPIPS↓</td><td>FID↓</td></tr><tr><td>Mix</td><td>Mixed</td><td>18.8</td><td>0.595</td><td>0.284</td><td>7.08</td><td>15.0</td><td>0.372</td><td>0.467</td><td>14.2</td></tr><tr><td>OSV5M [1]</td><td>Street View</td><td>18.2-0.6</td><td>0.566-.029</td><td>0.318+.034</td><td>8.59+1.51</td><td>15.0</td><td>0.369-.003</td><td>0.481+.014</td><td>18.9+4.7</td></tr><tr><td>ImageNet21K [49]</td><td>Objects</td><td>18.8</td><td>0.593-.002</td><td>0.289+.005</td><td>7.32+0.24</td><td>14.9-0.1</td><td>0.370-.003</td><td>0.472+.005</td><td>15.9+1.7</td></tr><tr><td>Places [76]</td><td>Scenes</td><td>18.8</td><td>0.596+.001</td><td>0.286+.002</td><td>7.41+0.33</td><td>14.8-0.2</td><td>0.367-.006</td><td>0.477+.010</td><td>20.3+6.1</td></tr><tr><td>OpenImages [28]</td><td>General</td><td>18.8</td><td>0.593-.002</td><td>0.287+.003</td><td>7.20+0.12</td><td>14.9-0.1</td><td>0.370-.003</td><td>0.469+.002</td><td>14.8+0.6</td></tr></table>

图片摘要：该图主要展示 3: Comparison of data coverage on model performance on RealE。
![](images/8092631e4fa1cc4da876ed767d3e1fa4b745c3a35a3d0ba864ebd27567bde15e.jpg)  
(a) PSNR vs. FPS (upper-right is better)

Fig. 6: Quality vs. Inference tradeoff on DL3DV. Bubble size indicates parameter count. Our single-step model achieves improved quality at drastically higher FPS than its competitors. SSIM and LPIPS plots are in the supplementary material.   
图片摘要：该图主要展示 6: Quality vs. Inference tradeoff on DL3DV. Bubble size indi。
![](images/0e50b29e177f33b590a0f5c950e0493e4c3a2e502f66ee18a13cb72ba8d72a49.jpg)  
# params: 100M 250M 500M

(b) FID vs. FPS (lower-right is better)

# 4.6 Towards an Interactive Navigation Model

Figure 6 plots inference throughput against generation quality for all methods on a single H100 GPU, evaluated on the DL3DV dataset. OVIE achieves throughputs of 116 FPS (8.6 ms), compared to 0.19 FPS for VIVID (50 diffusion steps), 0.17 FPS for GeoGPT (autoregressive), and 0.024 FPS for PhotoNVS (2000 diffusion steps). By performing a single forward pass per image, OVIE is over 600 $\times$ faster than the next best approach, while exceeding its perceptual quality.

This high throughput unlocks real-time use cases. Given a single input image and keyboard-driven camera controls, OVIE can be used as a practical navigation model, allowing a user to freely explore a scene at interactive rates.

# 5 Conclusion

Monocular novel view synthesis has long been limited by the scarcity of multiview training data. This paper overcomes this bottleneck by using monocular depth estimation as a scalable, domain-agnostic source of geometric supervision. By generating pseudo-pairs from 30 million unlabeled images, OVIE achieves generalization that matches or exceeds models trained on specialized multi-view benchmarks. Our results show that data scale, rather than architectural complexity, is the primary driver of performance in view synthesis. This framework enables 3D-aware applications in domains where multi-view capture is impossible, such as historical archives and artwork, while supporting real-time inference. Ultimately, we demonstrate that 3D capabilities can be acquired from internetscale 2D data, providing a path toward universal geometric priors learned from any image collection.

Acknowledgments. We thank Robin Courant for proof-reading, and Eloi Alonso, Mathieu Aubry, Antoine Guédon, Anthony Hu, Loïc Landrieu, Vincent Lepetit, Vincent Micheli, Manu Orsini, Amélie Royer, and Václav Volhejn for interesting discussions.

# References

1. Astruc, G., Dufour, N., Siglidis, I., Aronssohn, C., Bouia, N., Fu, S., Loiseau, R., Nguyen, V.N., Raude, C., Vincent, E., Xu, L., Zhou, H., Landrieu, L.: OpenStreetView-5M: The many roads to global visual geolocation. CVPR (2024) 3, 8, 13   
2. Bai, Y., Li, H., Huang, Q.: Positional encoding field. arXiv (2025) 4, 9   
3. Bhat, S.F., Birkl, R., Wofk, D., Wonka, P., Müller, M.: Zoedepth: Zero-shot transfer by combining relative and metric depth. arXiv (2023) 5   
4. Birkl, R., Wofk, D., Müller, M.: Midas v3.1 – a model zoo for robust monocular relative depth estimation. arXiv (2023) 5   
5. Caron, M., Touvron, H., Misra, I., Jégou, H., Mairal, J., Bojanowski, P., Joulin, A.: Emerging properties in self-supervised vision transformers. In: ICCV (2021) 7   
6. Chan, E., Monteiro, M., Kellnhofer, P., Wu, J., Wetzstein, G.: pi-gan: Periodic implicit generative adversarial networks for 3d-aware image synthesis. In: CVPR (2021) 4   
7. Chan, E.R., Lin, C.Z., Chan, M.A., Nagano, K., Pan, B., De Mello, S., Gallo, O., Guibas, L.J., Tremblay, J., Khamis, S., Karras, T., Wetzstein, G.: Efficient geometry-aware 3d generative adversarial networks. In: CVPR (2022) 4   
8. Charatan, D., Li, S., Tagliasacchi, A., Sitzmann, V.: pixelsplat: 3d gaussian splats from image pairs for scalable generalizable 3d reconstruction. In: CVPR (2024) 3   
9. Charbonnier, P., Blanc-Feraud, L., Aubert, G., Barlaud, M.: Deterministic edgepreserving regularization in computed imaging. IEEE Transactions on Image Processing (1997) 7, 12   
10. Chen, Y., Xu, H., Zheng, C., Zhuang, B., Pollefeys, M., Geiger, A., Cham, T.J., Cai, J.: Mvsplat: Efficient 3d gaussian splatting from sparse multi-view images. arXiv (2024) 3   
11. Chen, Y., Zheng, C., Xu, H., Zhuang, B., Vedaldi, A., Cham, T.J., Cai, J.: Mvsplat360: Feed-forward 360 scene synthesis from sparse views. In: NeurIPS (2024) 3   
12. Chung, J., Lee, S., Nam, H., Lee, J., Lee, K.M.: Luciddreamer: Domain-free generation of 3d gaussian splatting scenes. arXiv (2023) 5   
13. Dai, A., Chang, A.X., Savva, M., Halber, M., Funkhouser, T., Nießner, M.: Scannet: Richly-annotated 3d reconstructions of indoor scenes. In: CVPR (2017) 4   
14. Deitke, M., Liu, R., Wallingford, M., Ngo, H., Michel, O., Kusupati, A., Fan, A., Laforte, C., Voleti, V., Gadre, S.Y., VanderBilt, E., Kembhavi, A., Vondrick, C., Gkioxari, G., Ehsani, K., Schmidt, L., Farhadi, A.: Objaverse-xl: A universe of 10m+ 3d objects. NeurIPS (2023) 2   
15. Deitke, M., Schwenk, D., Salvador, J., Weihs, L., Michel, O., VanderBilt, E., Schmidt, L., Ehsani, K., Kembhavi, A., Farhadi, A.: Objaverse: A universe of annotated 3d objects. CVPR (2023) 2, 4   
16. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., Houlsby, N.: An image is worth 16x16 words: Transformers for image recognition at scale. ICLR (2021) 10

17. Elata, N., Kawar, B., Ostrovsky-Berman, Y., Farber, M., Sokolovsky, R.: Novel view synthesis with pixel-space diffusion models. CVPR (2025) 4, 5, 9, 11, 26   
18. Esser, P., Kulal, S., Blattmann, A., Entezari, R., Müller, J., Saini, H., Levi, Y., Lorenz, D., Sauer, A., Boesel, F., Podell, D., Dockhorn, T., English, Z., Rombach, R.: Scaling rectified flow transformers for high-resolution image synthesis. In: Proc. ICML (2024) 4   
19. Esser, P., Rombach, R., Ommer, B.: Taming transformers for high-resolution image synthesis. In: CVPR (2021) 7, 8, 25   
20. Gao, J., Shen, T., Wang, Z., Chen, W., Yin, K., Li, D., Litany, O., Gojcic, Z., Fidler, S.: Get3d: a generative model of high quality 3d textured shapes learned from images. In: NeurIPS (2022) 4   
21. Isola, P., Zhu, J.Y., Zhou, T., Efros, A.A.: Image-to-image translation with conditional adversarial networks. CVPR (2017) 7, 25   
22. Jampani, V., Chang, H., Sargent, K., Kar, A., Tucker, R., Krainin, M., Kaeser, D., Freeman, W.T., Salesin, D., Curless, B., et al.: Slide: Single image 3d photography with soft layering and depth-aware inpainting. In: ICCV (2021) 5   
23. Jang, W., Agapito, L.: Nvist: In the wild new view synthesis from a single image with transformers. In: CVPR (2024) 4   
24. Jin, H., Jiang, H., Tan, H., Zhang, K., Bi, S., Zhang, T., Luan, F., Snavely, N., Xu, Z.: Lvsm: A large view synthesis model with minimal 3d inductive bias. In: ICLR (2025) 3   
25. Ke, B., Obukhov, A., Huang, S., Metzger, N., Daudt, R.C., Schindler, K.: Repurposing diffusion-based image generators for monocular depth estimation. In: CVPR (2024) 5   
26. Ke, B., Qu, K., Wang, T., Metzger, N., Huang, S., Li, B., Obukhov, A., Schindler, K.: Marigold: Affordable adaptation of diffusion-based image generators for image analysis. IEEE TPAMI (2025) 5   
27. Kerbl, B., Kopanas, G., Leimkühler, T., Drettakis, G.: 3d gaussian splatting for real-time radiance field rendering. SIGGRAPH (2023) 3   
28. Kuznetsova, A., Rom, H., Alldrin, N., Uijlings, J., Krasin, I., Pont-Tuset, J., Kamali, S., Popov, S., Malloci, M., Kolesnikov, A., Duerig, T., Ferrari, V.: The open images dataset v4: Unified image classification, object detection, and visual relationship detection at scale. IJCV (2020) 3, 8, 13   
29. Labs, B.F., Batifol, S., Blattmann, A., Boesel, F., Consul, S., Diagne, C., Dockhorn, T., English, J., English, Z., Esser, P., Kulal, S., Lacey, K., Levi, Y., Li, C., Lorenz, D., Müller, J., Podell, D., Rombach, R., Saini, H., Sauer, A., Smith, L.: Flux.1 kontext: Flow matching for in-context image generation and editing in latent space. arXiv (2025) 4   
30. Ling, L., Sheng, Y., Tu, Z., Zhao, W., Xin, C., Wan, K., Yu, L., Guo, Q., Yu, Z., Lu, Y., et al.: Dl3dv-10k: A large-scale scene dataset for deep learning-based 3d vision. In: CVPR (2024) 2, 3, 4, 8, 11, 12, 13, 20   
31. Liu, R., Wu, R., Van Hoorick, B., Tokmakov, P., Zakharov, S., Vondrick, C.: Zero-1-to-3: Zero-shot one image to 3d object. In: ICCV (2023) 4, 5   
32. Ma, Z., Xu, R., Zhang, S.: Pixelgen: Pixel diffusion beats latent diffusion with perceptual loss. arXiv (2026) 7   
33. Maillard, L., Durand, T., Rahary, A.R., Ovsjanikov, M.: Laconic: A 3d layout adapter for controllable image creation. In: ICCV (2025) 4   
34. Mescheder, L., Dong, W., Li, S., Bai, X., Santos, M., Hu, P., Lecouat, B., Zhen, M., Delaunoy, A., Fang, T., Tsin, Y., Richter, S.R., Koltun, V.: Sharp monocular view synthesis in less than a second. In: ICLR (2026) 3

35. Mildenhall, B., Srinivasan, P.P., Tancik, M., Barron, J.T., Ramamoorthi, R., Ng, R.: Nerf: Representing scenes as neural radiance fields for view synthesis. In: ECCV (2020) 3   
36. Müller, N., Schwarz, K., Rössle, B., Porzi, L., Bulò, S.R., Nießner, M., Kontschieder, P.: Multidiff: Consistent novel view synthesis from a single image. In: CVPR (2024) 5   
37. Nguyen-Phuoc, T., Li, C., Theis, L., Richardt, C., Yang, Y.L.: Hologan: Unsupervised learning of 3d representations from natural images. In: ICCV (2019) 4   
38. Niemeyer, M., Geiger, A.: Giraffe: Representing scenes as compositional generative neural feature fields. In: CVPR (2021) 4   
39. Niklaus, S., Mai, L., Yang, J., Liu, F.: 3d ken burns effect from a single image. ACM Transactions on Graphics (2019) 5   
40. Oquab, M., Darcet, T., Moutakanni, T., Vo, H.V., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., Howes, R., Huang, P.Y., Xu, H., Sharma, V., Li, S.W., Galuba, W., Rabbat, M., Assran, M., Ballas, N., Synnaeve, G., Misra, I., Jegou, H., Mairal, J., Labatut, P., Joulin, A., Bojanowski, P.: Dinov2: Learning robust visual features without supervision. arXiv (2023) 7   
41. Peebles, W., Xie, S.: Scalable Diffusion Models with Transformers . In: ICCV (2023) 8, 23   
42. Piccinelli, L., Sakaridis, C., Yang, Y.H., Segu, M., Li, S., Abbeloos, W., Gool, L.V.: UniDepthV2: Universal monocular metric depth estimation made simpler. arXiv (2025) 5   
43. Piccinelli, L., Yang, Y.H., Sakaridis, C., Segu, M., Li, S., Van Gool, L., Yu, F.: UniDepth: Universal monocular metric depth estimation. In: CVPR (2024) 5   
44. Ramirez, P.Z., Tonioni, A., Tombari, F.: Unsupervised novel view synthesis from a single image. arXiv (2021) 4   
45. Ranftl, R., Bochkovskiy, A., Koltun, V.: Vision transformers for dense prediction. In: ICCV (2021) 5   
46. Ranftl, R., Lasinger, K., Hafner, D., Schindler, K., Koltun, V.: Towards robust monocular depth estimation: Mixing datasets for zero-shot cross-dataset transfer. IEEE TPAMI (2022) 5   
47. Reddy, P., Elezi, I., Deng, J.: G3dr: Generative 3d reconstruction in imagenet. CVPR (2024) 4   
48. Ren, X., Shen, T., Huang, J., Ling, H., Lu, Y., Nimier-David, M., Müller, T., Keller, A., Fidler, S., Gao, J.: Gen3c: 3d-informed world-consistent video generation with precise camera control. In: CVPR (2025) 9   
49. Ridnik, T., Ben-Baruch, E., Noy, A., Zelnik-Manor, L.: Imagenet-21k pretraining for the masses. arXiv (2021) 3, 8, 13   
50. Rombach, R., Esser, P., Ommer, B.: Geometry-free view synthesis: Transformers and no 3d priors. In: ICCV. pp. 14356–14366 (2021) 4, 5, 9, 11, 26   
51. Sajjadi, M.S.M., Meyer, H., Pot, E., Bergmann, U., Greff, K., Radwan, N., Vora, S., Lucic, M., Duckworth, D., Dosovitskiy, A., Uszkoreit, J., Funkhouser, T., Tagliasacchi, A.: Scene Representation Transformer: Geometry-Free Novel View Synthesis Through Set-Latent Scene Representations. In: CVPR (2022) 4, 5   
52. Sargent, K., Li, Z., Shah, T., Herrmann, C., Yu, H.X., Zhang, Y., Chan, E.R., Lagun, D., Fei-Fei, L., Sun, D., Wu, J.: ZeroNVS: Zero-shot 360-degree view synthesis from a single real image. arXiv (2023) 5   
53. Sauer, A., Karras, T., Laine, S., Geiger, A., Aila, T.: Stylegan-t: unlocking the power of gans for fast large-scale text-to-image synthesis. In: Proc. ICML (2023) 7

54. Schwarz, K., Liao, Y., Niemeyer, M., Geiger, A.: Graf: Generative radiance fields for 3d-aware image synthesis. In: Advances in Neural Information Processing Systems (NeurIPS) (2020) 4   
55. Seo, J., Fukuda, K., Shibuya, T., Narihira, T., Murata, N., Hu, S., Lai, C.H., Kim, S., Mitsufuji, Y.: Genwarp: Single image to novel views with semantic-preserving generative warping. arXiv (2024) 5   
56. Shih, M.L., Su, S.Y., Kopf, J., Huang, J.B.: 3d photography using context-aware layered depth inpainting. In: CVPR (2020) 5   
57. Siméoni, O., Vo, H.V., Seitzer, M., Baldassarre, F., Oquab, M., Jose, C., Khalidov, V., Szafraniec, M., Yi, S., Ramamonjisoa, M., Massa, F., Haziza, D., Wehrstedt, L., Wang, J., Darcet, T., Moutakanni, T., Sentana, L., Roberts, C., Vedaldi, A., Tolan, J., Brandt, J., Couprie, C., Mairal, J., Jégou, H., Labatut, P., Bojanowski, P.: Dinov3. arXiv (2025) 7, 24   
58. Szymanowicz, S., Insafutdinov, E., Zheng, C., Campbell, D., Henriques, J., Rupprecht, C., Vedaldi, A.: Flash3d: Feed-forward generalisable 3d scene reconstruction from a single image. 3DV (2025) 3   
59. Szymanowicz, S., Rupprecht, C., Vedaldi, A.: Splatter image: Ultra-fast single-view 3d reconstruction. In: CVPR (2024) 3   
60. Tucker, R., Snavely, N.: Single-view view synthesis with multiplane images. In: CVPR (2020) 5   
61. Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., Novotny, D.: Vggt: Visual geometry grounded transformer. In: CVPR (2025) 8   
62. Wang, Q., Wang, Z., Genova, K., Srinivasan, P., Zhou, H., Barron, J.T., Martin-Brualla, R., Snavely, N., Funkhouser, T.: Ibrnet: Learning multi-view image-based rendering. In: CVPR (2021) 3   
63. Wang, R., Xu, S., Dai, C., Xiang, J., Deng, Y., Tong, X., Yang, J.: Moge: Unlocking accurate monocular geometry estimation for open-domain images with optimal training supervision. In: CVPR (2025) 5   
64. Wang, R., Xu, S., Dong, Y., Deng, Y., Xiang, J., Lv, Z., Sun, G., Tong, X., Yang, J.: Moge-2: Accurate monocular geometry with metric scale and sharp details. In: NeurIPS (2025) 5, 7, 8, 24   
65. Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., Revaud, J.: Dust3r: Geometric 3d vision made easy. In: CVPR (2024) 4   
66. Wiles, O., Gkioxari, G., Szeliski, R., Johnson, J.: SynSin: End-to-end view synthesis from a single image. In: CVPR (2020) 4, 5   
67. Xing, J., Xia, M., Zhang, Y., Chen, H., Yu, W., Liu, H., Liu, G., Wang, X., Shan, Y., Wong, T.T.: Dynamicrafter: Animating open-domain images with video diffusion priors. In: ECCV (2025) 4   
68. Xu, H., Peng, S., Wang, F., Blum, H., Barath, D., Geiger, A., Pollefeys, M.: Depthsplat: Connecting gaussian splatting and depth. In: CVPR (2025) 3   
69. Yang, L., Kang, B., Huang, Z., Xu, X., Feng, J., Zhao, H.: Depth anything: Unleashing the power of large-scale unlabeled data. In: CVPR (2024) 5   
70. Yu, A., Ye, V., Tancik, M., Kanazawa, A.: pixelNeRF: Neural radiance fields from one or few images. In: CVPR (2021) 3   
71. Yu, J.J., Forghani, F., Derpanis, K.G., Brubaker, M.A.: Long-term photometric consistent novel view synthesis with diffusion models. In: ICCV (2023) 4, 5, 9, 11, 26   
72. Yu, W., Xing, J., Yuan, L., Hu, W., Li, X., Huang, Z., Gao, X., Wong, T.T., Shan, Y., Tian, Y.: Viewcrafter: Taming video diffusion models for high-fidelity novel view synthesis. IEEE TPAMI (2024) 4

73. Yu, X., Xu, M., Zhang, Y., Liu, H., Ye, C., Wu, Y., Yan, Z., Liang, T., Chen, G., Cui, S., Han, X.: Mvimgnet: A large-scale dataset of multi-view images. In: CVPR (2023) 4   
74. Zhang, R., Isola, P., Efros, A.A., Shechtman, E., Wang, O.: The unreasonable effectiveness of deep features as a perceptual metric. In: CVPR (2018) 7   
75. Zheng, B., Ma, N., Tong, S., Xie, S.: Diffusion transformers with representation autoencoders. In: ICLR (2026) 25   
76. Zhou, B., Khosla, A., Lapedriza, À., Torralba, A., Oliva, A.: Places: An image database for deep scene understanding. arXiv (2016) 3, 8, 13   
77. Zhou, J.J., Gao, H., Voleti, V., Vasishta, A., Yao, C.H., Boss, M., Torr, P., Rupprecht, C., Jampani, V.: Stable virtual camera: Generative view synthesis with diffusion models. arXiv (2025) 3, 4   
78. Zhou, T., Tucker, R., Flynn, J., Fyffe, G., Snavely, N.: Stereo magnification: Learning view synthesis using multiplane images. SIGGRAPH (2018) 2, 3, 4, 8, 11, 12, 13, 20, 21, 26   
79. Zhou, T., Tucker, R., Flynn, J., Fyffe, G., Snavely, N.: Stereo magnification: learning view synthesis using multiplane images. ACM Trans. Graph. (2018) 5   
80. Zhu, J.Y., Krähenbühl, P., Shechtman, E., Efros, A.: Generative visual manipulation on the natural image manifold. In: ECCV (2016) 4   
81. Zhu, J.Y., Park, T., Isola, P., Efros, A.A.: Unpaired image-to-image translation using cycle-consistent adversarial networkss. In: ICCV (2017) 4

# A Summary of Supplementary Material

This supplementary document provides additional details and results that complement the main paper. It is organized as follows:

– Section B – Additional Quantitative Results. We report supplementary SSIM and LPIPS curves for the data-scaling (B.1) and throughput analyses (B.2).   
– Section C – Camera Sampling Details. We describe the distribution from which relative camera transformations are sampled during training, including the parameterization (C.1, C.2), the geometry-aware reprojection (C.3) and pseudo-views sampling hyperparameters (C.4).   
– Section D – Additional Implementation Details. We provide extended details on architecture (D.1), pose-conditioning (D.2), and training details and hyperparameters (D.3).   
– Section E – Additional Qualitative Results. We illustrate OVIE’s robust generalization by synthesizing additional novel views from diverse outof-distribution images, including non-realistic source inputs such as paintings (E.1). We compare OVIE-generated views against their corresponding pseudo-ground-truth supervision targets (E.2). We present more qualitative comparisons on RealEstate10K [78], contrasting OVIE’s outputs with the source, the ground-truth novel view, and baseline methods (E.3). To highlight generation consistency and responsiveness, we provide animated sideby-side navigations (E.4) and real-time interactive screen recordings, driven by mouse and keyboard inputs, all generated continuously from a single initial frame (E.5).

# B Additional Quantitative Results

# B.1 Effect of Dataset Size on SSIM and LPIPS

Figure 7 shows SSIM and LPIPS as functions of dataset size, confirming the trends observed for PSNR and FID in Figure 5 of the main paper: both metrics improve consistently with more training data.

# B.2 Throughput analysis

Figure 8 demonstrates that OVIE is 600 $\times$ faster than the next fastest method while also achieving improved SSIM and LPIPS scores on DL3DV [30]. This complements the improved PSNR and FID results discussed in Figure 6 of the main paper.

# C Camera Sampling Details

During training, we generate novel views of the input image to serve as pseudoground-truth targets by reprojecting the scene’s 3D point cloud into newly sampled camera viewpoints. To achieve this, a monocular depth estimator first predicts both the absolute depth and the camera’s horizontal field of view $\left( \Theta _ { \mathrm { h } } \right)$ ,

图片摘要：该图主要展示 8 demonstrates that OVIE is 600 faster than the next fastest。
![](images/3fa245a149d831637275e2851584d7c741c15b8b03e4cb6ffcc34b231e0f9a8f.jpg)

图片摘要：该图主要展示 8 demonstrates that OVIE is 600 faster than the next fastest。
![](images/fccb68a679dbc480a340d379a8f64b487a342c2b10dd7fe6fa654d4855acfc85.jpg)  
Fig. 7: Scaling with dataset size – SSIM and LPIPS. Complementary to Figure 5 in the main paper, SSIM and LPIPS on RealEstate10K [78] follow the same monotonic improvement as data volume increases.

图片摘要：该图主要展示 7: Scaling with dataset size – SSIM and LPIPS. Complementary。
![](images/6a1c24e419e502fc69d0fffb4918dde1116a5449f04d08fd9c0f90ae8343070f.jpg)  
(a) SSIM vs. FPS (upper-right is better)

图片摘要：该图主要展示 7: Scaling with dataset size – SSIM and LPIPS. Complementary。
![](images/ea8cc4971699a507c4c301ee2d81bff79cdb52fe49d7cac613416601061f1c60.jpg)  
(b) LPIPS vs. FPS (lower-right is better)   
Fig. 8: Quality vs. Inference tradeoff on DL3DV – SSIM and LPIPS. Complementary to Figure 6 in the main paper. Bubble size indicates parameter count. The same trend holds: OVIE is faster and better-performing than concurrent methods

together enabling reconstruction of the point cloud in a true metric, real-world scale. Because this geometry possesses accurate physical dimensions, the distributions used to sample new camera poses can be defined directly in actual scene units (e.g., meters) rather than an arbitrary coordinate space. This ensures that camera displacements and distances scale consistently with the specific geometry of each scene. Next, a routing module stochastically assigns each batch element to one of six sampling methods based on fixed prior weights. All methods ultimately produce a world-to-camera extrinsic matrix $[ \mathbf { R } \mid \mathbf { t } ] \in \mathbb { R } ^ { 3 \times 4 }$ .

Throughout this section, we denote continuous uniform and normal distributions as $\boldsymbol { u }$ and $\mathcal { N }$ , respectively, and let $\hat { y } = [ 0 , 1 , 0 ] ^ { \top }$ and $\hat { z } = [ 0 , 0 , 1 ] ^ { \top }$ represent the canonical up and forward directional unit vectors.

# C.1 Sampling methods.

The six strategies span a range of transformation types, from trivial (identity) to geometry-grounded (normal-derived, frontal hemisphere), ensuring the model is trained on diverse yet plausible viewpoint changes.

– Identity. No transformation is applied. The extrinsic is set to [I | 0].   
– Pure translation. The camera is shifted relative to the scene without any rotation, with the shift magnitude tied to the spatial extent of the point cloud. The rotation is fixed to $\mathbf { R } = \mathbf { I }$ . The translation is sampled as $\textbf { t } \sim$ $\mathcal { U } [ - \alpha _ { \mathrm { t } } \pmb { \sigma } , + \alpha _ { \mathrm { t } } \pmb { \sigma } ]$ , where $\alpha _ { \mathrm { t } } \in \mathbb { R } ^ { + }$ is a scaling hyperparameter and $\pmb { \sigma } \in \mathbb { R } ^ { 3 }$ is the per-axis standard deviation of the point cloud. To prevent points from passing behind the camera, the z-component of the translation is clamped to $t _ { z } \le \operatorname* { m i n } _ { i } z _ { i }$ , where $z _ { i }$ is the depth (z-coordinate) of the $i$ -th point.   
– Pure rotation. The camera rotates in place, with the maximum rotation angle bounded by the field of view. The translation is fixed to $\mathbf { t } \ = \ \mathbf { 0 }$ . A forward direction is sampled by rotating the canonical forward axis $\hat { z }$ by polar angle $\theta \sim \mathcal { U } [ 0 , \alpha _ { \mathrm { r } } \Theta _ { \mathrm { h } } ]$ (where $\alpha _ { \mathrm { r } } \in \mathbb { R } ^ { + }$ is a rotation scaling factor and $\Theta _ { \mathrm { h } }$ is the horizontal field of view estimated by the monocular depth estimator) and azimuth $\phi \sim \mathcal { U } [ 0 , 2 \pi )$ . This direction is then orthonormalized against the canonical up vector $\hat { y }$ to form $\mathbf { R }$ .   
– Combined rotation and translation. The camera is both shifted and rotated, combining the two previous strategies. A translation $\mathbf { t } _ { \mathrm { t } }$ and rotation $\mathbf { R } _ { \mathrm { r } }$ are sampled independently as above and composed as $\mathbf { R } _ { \mathrm { h y b r i d } } \ = \ \mathbf { R } _ { \mathrm { r } }$ , $\mathbf { t } _ { \mathrm { h y b r i d } } = \mathbf { R } _ { \mathrm { r } } \mathbf { t } _ { \mathrm { t } }$ .   
– Normal-derived. The camera is placed above a randomly selected surface point, looking at it from along its normal direction, as estimated by the monocular depth estimator. An anchor point $\mathbf { p } \in \mathbb { R } ^ { 3 }$ is sampled with probability $\propto \lVert \mathbf { p } \rVert ^ { - 1 }$ , restricted to points whose surface normal $\hat { \mathbf { n } } \in \mathbb { R } ^ { 3 }$ satisfies $| n _ { y } | < \tau$ , where $n _ { y }$ is the y-component of the normal and $\tau$ is a filtering threshold. The camera is placed at $\mathbf { c } = \mathbf { p } + s \hat { \mathbf { n } }$ , where the distance multiplier $s$ is drawn from a log-uniform distribution $s \sim \log \mathcal { U } ( d _ { \operatorname* { m i n } } \| \mathbf { p } \| , d _ { \operatorname* { m a x } } \| \mathbf { p } \| )$ $d _ { \operatorname* { m a x } } \| \mathbf { p } \|$ ), with $d _ { \mathrm { m i n } }$ and $d _ { \mathrm { m a x } }$ representing the minimum and maximum distance bounds. Log-uniform sampling is used here to ensure that exponentially large distances are not overrepresented. Finally, $\mathbf { R }$ is set by a look-at from $\mathbf { c }$ to $\mathbf { p }$ . Batches for which no valid normal survives filtering fall back to identity.   
– Frontal hemisphere. The camera orbits around a randomly selected scene point, staying roughly frontal with a limited angular deviation. An anchor $\mathbf { p }$ is sampled with probability $\propto ~ \left\| \mathbf { p } \right\| ^ { - 1 }$ and jittered as $\tilde { \textbf { p } } = \textbf { p } + \epsilon$ , $\mathbf { \epsilon } \gets \mathcal { N } ( \mathbf { 0 } , ( \sigma _ { \mathrm { a n c h o r } } \| \mathbf { p } \| ) ^ { 2 } \mathbf { I } )$ , where $\sigma _ { \mathrm { a n c h o r } }$ is a hyperparameter controlling the variance of the jitter. The reference direction $\hat { \mathbf { r } } = - \tilde { \mathbf { p } } / \| \tilde { \mathbf { p } } \|$ is perturbed by azimuth and elevation each drawn from $\mathcal { U } [ - \delta , \delta ]$ , where $\delta$ bounds the maximum angular deviation, to obtain a new viewing direction $\hat { \mathbf { d } }$ . The camera is placed at $\mathbf { c } = \tilde { \mathbf { p } } + z \hat { \mathbf { d } }$ , where $z = \| \mathbf { p } \| \cdot s$ and $s \sim \log \mathcal { U } ( d _ { \operatorname* { m i n } } , d _ { \operatorname* { m a x } } )$ . As previously mentioned, the log sampling of the distance multiplier $s$ ensures that large distances are not overrepresented. Finally, $\mathbf { R }$ is set by a look-at from $\mathbf { c }$ to $\bar { \bf p }$ .

# C.2 Look-at construction.

Given camera position c and target $\mathbf { p }$ , we compute the forward vector $\hat { f } ~ =$ $( \mathbf { p } - \mathbf { c } ) / \lVert \mathbf { p } - \mathbf { c } \rVert$ , the right vector $\hat { r } ~ = ~ ( \hat { y } \times \hat { f } ) / \| \hat { y } \times \hat { f } \|$ , the true up vector $\hat { u } = \hat { f } \times \hat { r }$ , and set $\mathbf { R } = [ \hat { r } \mid \hat { u } \mid \hat { f } ]$ .

# C.3 Geometry-aware reprojection.

Given a target viewpoint, source colors are reprojected by mapping each 3D point into the new camera’s image plane. Formally, each source point $\mathbf { p } _ { i } \in \mathbb { R } ^ { 3 }$ , derived from the monocular depth estimator, with normal $\hat { \mathbf { n } } _ { i }$ is projected to 2D pixel coordinates ${ \bf q } _ { i }$ . This is expressed in homogeneous coordinates as ${ \bf q } _ { i } \sim$ $\mathbf { K } \left( \mathbf { R } \mathbf { p } _ { i } + \mathbf { t } \right)$ , where $\mathbf { K } \in \mathbb { R } ^ { 3 \times 3 }$ is the known camera intrinsic matrix.

To handle occlusions, we apply a strategy akin to backface culling in computer graphics, discarding points that face away from the camera, i.e., those satisfying $\hat { \mathbf { n } } _ { i } ^ { \top } ( \mathbf { c } - \mathbf { p } _ { i } ) \leq 0$ , where $\mathbf { c } = - \mathbf { R } ^ { \top } \mathbf { t }$ is the target camera center in world coordinates. When multiple valid points project onto the exact same discrete pixel, a z-buffer resolves the collision by assigning the pixel the color of the point with the minimum projected depth. If no points project onto a given pixel, it remains black.

Finally, a visibility mask is computed to indicate these valid, populated pixels; this mask is later applied during the computation of perceptual losses as discussed in the main paper.

# C.4 Hyperparameters.

All sampling hyperparameters and model settings are summarized in Table 4.

# D Implementation Details

# D.1 Architecture

OVIE consists of a convolutional encoder (8 $\times$ spatial downsampling), a ViT-B bottleneck, and a symmetric convolutional decoder. Input images (256 $\times$ 256) are compressed to a 32 $\times$ 32 $\times$ 512 feature map via three ResNet stages (GroupNorm, SiLU), then patchified into 1024 tokens (1 $\times$ 1 patches) and linearly projected to D=768 dimensions. A 12-layer ViT-B ( $D$ =768, 12 heads, RMSNorm, SwiGLU) processes the tokens, after which they are unpatchified and decoded symmetrically, concluding with a 1 $\times$ 1 convolution and Sigmoid activation.

# D.2 Camera Conditioning via AdaLN

Camera extrinsics $\mathbf { p } \in \mathbb { R } ^ { 7 }$ (translation and a quaternion for rotation) are projected to a conditioning embedding $\mathbf { c } \in \mathbb { R } ^ { D }$ via a single linear layer. This embedding modulates the ViT-B bottleneck via adaLN-Zero [41]: for each transformer

Table 4: Camera sampling hyperparameters and model settings used during training.   

<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td></tr><tr><td colspan="3">Sampling probabilities</td></tr><tr><td>Identity</td><td>-</td><td>0.15</td></tr><tr><td>Pure translation</td><td>-</td><td>0.10</td></tr><tr><td>Pure rotation</td><td>-</td><td>0.10</td></tr><tr><td>Combined rotation &amp; translation</td><td>-</td><td>0.35</td></tr><tr><td>Normal-derived</td><td>-</td><td>0.05</td></tr><tr><td>Frontal hemisphere</td><td>-</td><td>0.25</td></tr><tr><td colspan="3">Translation &amp; rotation</td></tr><tr><td>Translation scaling factor</td><td>\( \alpha_t \)</td><td>1.0</td></tr><tr><td>Rotation scaling factor</td><td>\( \alpha_r \)</td><td>1.0</td></tr><tr><td colspan="3">Normal-derived &amp; frontal hemisphere</td></tr><tr><td>Distance range</td><td>\( [d_{\text{min}}, d_{\text{max}}] \)</td><td>[0.75, 1.5]</td></tr><tr><td>Max perturbation angle</td><td>\( \delta \)</td><td>25°</td></tr><tr><td>Anchor jitter scale</td><td>\( \sigma_{anchor} \)</td><td>0.02</td></tr><tr><td colspan="3">Model settings</td></tr><tr><td>Depth estimator</td><td>-</td><td>moge-2-vitl-normal [64]</td></tr></table>

block, a two-layer MLP regresses, from c, dimension-wise scale $\gamma$ , shift $\beta$ , and residual gate $\alpha$ for both the MSA and SwiGLU sub-layers:

$$
\mathbf {x} ^ {\prime} = \mathbf {x} + \alpha_ {\mathrm {m s a}} \odot \operatorname {M S A} \left(\gamma_ {\mathrm {m s a}} \odot \operatorname {R M S N o r m} (\mathbf {x}) + \beta_ {\mathrm {m s a}}\right), \tag {5}
$$

$$
\mathbf {x} ^ {\prime \prime} = \mathbf {x} ^ {\prime} + \alpha_ {\mathrm {m l p}} \odot \operatorname {S w i G L U} \left(\gamma_ {\mathrm {m l p}} \odot \operatorname {R M S N o r m} \left(\mathbf {x} ^ {\prime}\right) + \beta_ {\mathrm {m l p}}\right). \tag {6}
$$

Following adaLN-Zero, the MLP’s final linear layer is zero-initialized so the conditioning path contributes nothing at the start of training.

# D.3 Optimization and Training

OVIE is trained for 2,000,000 steps with a global batch size of 512 using the AdamW optimizer ( $\beta _ { 1 } ~ = ~ 0 . 9$ , $\beta _ { 2 } ~ = ~ 0 . 9 9 9$ , weight decay of 0.05). We apply gradient clipping with a maximum norm of 1.0. The learning rate follows a cosine decay schedule, annealing from a peak of $2 \times 1 0 ^ { - 4 }$ down to a minimum of $2 \times 1 0 ^ { - 5 }$ , which is preceded by a linear warmup phase over the first $0 . 6 2 5 \%$ of training (∼12.5k steps). Finally, we maintain an exponential moving average (EMA) of the generator weights with a decay rate of 0.999 for inference.

Loss. The training objective combines $L _ { 2 }$ reconstruction loss, LPIPS (λLPIPS=1.0), and a P-DINO perceptual loss (λP-DINO=0.5) extracted from a pretrained DINOv3- ViT-B/16 model [57].

Adversarial Training. A PatchGAN discriminator [21] sharpens high-frequency detail. Following Representation Autoencoders (RAE) [75], we adopt a frozen DINO-S/8 backbone (inputs resized to 224 $\times$ 224) over the standard DINO-S/16, which reduces adversarial patch artifacts. The discriminator uses standard batch normalization, a convolutional head (kernel size 9) with Spectral Normalization, a hinge loss for discriminator updates, and a non-saturating loss for the generator. To balance the scale of the reconstruction and adversarial gradients, we employ a dynamic adaptive weighting scheme originally introduced in VQGAN [19]. At each training step, the adaptive weight $\lambda$ is computed as:

$$
\lambda = \mathrm {c l a m p} \left(\frac {\| \nabla_ {\mathbf {W} _ {L}} \mathcal {L} _ {\mathrm {r e c o n}} \| _ {2}}{\| \nabla_ {\mathbf {W} _ {L}} \mathcal {L} _ {\mathrm {G A N}} \| _ {2} + \epsilon}, 0, \lambda_ {\mathrm {m a x}}\right),
$$

where $\nabla _ { \mathbf { W } _ { L } }$ denotes the gradient with respect to the weights of the last convolutional layer of the decoder, $\mathcal { L } _ { \mathrm { r e c o n } }$ is the $L _ { 2 }$ reconstruction loss, $\mathcal { L } _ { \mathrm { G A N } }$ is the generator’s adversarial loss, and $\epsilon = 1 0 ^ { - 6 }$ ensures numerical stability. The weight is clamped to a maximum limit of $\lambda _ { \operatorname* { m a x } } = 1 0 , 0 0 0$ to prevent gradient explosion. The final adversarial penalty added to the total training objective is scaled by $\lambda _ { \mathrm { a d v } } \lambda L _ { \mathrm { G A N } }$ , where $\lambda _ { \mathrm { a d v } } = 0 . 7 5$ is a fixed scalar. Finally, discriminator updates and adversarial penalties are delayed until 37.5% and 40% of total steps, respectively, to prevent early collapse.

Hyperparameters. All hyperparameters are reported in Table 5. For all ablation studies and supplementary experiments, we use the identical hyperparameter configuration but reduce the total training duration to 250,000 steps, keeping the absolute number of warmup steps constant.

# E Additional Qualitative Results

# E.1 Out-of-distribution novel views

Figure 9 illustrates novel views synthesized from out-of-domain, non-realistic source images (e.g., paintings). Notably, training on such artistic domains would be unfeasible using standard monocular novel-view synthesis methods reliant on multi-view datasets.

# E.2 Comparison between training pseudo-targets and generated views

Figures 10–13 show examples of pseudo-targets used for supervision during training, along with the views generated from the source image and the target camera pose.

The grid-like patterns in the pseudo-target images (middle) stem from the point cloud’s regular spatial structure. Because each 3D point is a back-projected source pixel, the points inherit the original image’s grid layout. When rendered from a novel viewpoint, the spacing between these points becomes visible as a grid that varies with depth and angle.

Table 5: Architecture, optimization, and loss hyperparameters.   

<table><tr><td>Hyperparameter</td><td>Value</td><td>Hyperparameter</td><td>Value</td></tr><tr><td>Generator Architecture</td><td></td><td>Losses</td><td></td></tr><tr><td>Resolution</td><td>256 × 256</td><td>Reconstruction loss</td><td>L2(MSE)</td></tr><tr><td>Base channels</td><td>128</td><td>LPIPS weight λLPIPS</td><td>1.0</td></tr><tr><td>Channel multipliers</td><td>[1, 2, 4]</td><td>P-DINO model</td><td>DINOv3-ViT-B/16</td></tr><tr><td>Downsampling factor</td><td>8×</td><td>P-DINO weight λDINO</td><td>0.5</td></tr><tr><td>ViT bottleneck</td><td></td><td>Adversarial weight λadv</td><td>0.75</td></tr><tr><td># Layers</td><td>12</td><td>Max adaptive weight limit</td><td>10,000</td></tr><tr><td># Heads</td><td>12</td><td></td><td></td></tr><tr><td>Hidden dimension</td><td>768</td><td colspan="2">Discriminator &amp; Adversarial Training</td></tr><tr><td>Normalization</td><td>RMSNorm</td><td>Backbone</td><td>Frozen DINO-S/8, 224×224</td></tr><tr><td>Activation</td><td>SwiGLU</td><td>Head</td><td>Conv 9×9, BN, SN</td></tr><tr><td>Camera embedder</td><td>Linear(R7→RD)</td><td>Augmentation probability</td><td>1.0</td></tr><tr><td>Generator Optimisation</td><td></td><td>Discriminator loss</td><td>Hinge</td></tr><tr><td>Batch size</td><td>512</td><td>Generator loss</td><td>Non-saturating (Vanilla)</td></tr><tr><td>Training steps</td><td>2,000,000</td><td>Optimizer</td><td>AdamW</td></tr><tr><td>Optimizer</td><td>AdamW</td><td>Optimizer betas (β1, β2)</td><td>(0.9, 0.95)</td></tr><tr><td>Optimizer betas (β1, β2)</td><td>(0.9, 0.999)</td><td>Peak learning rate</td><td>2×10-4</td></tr><tr><td>Peak learning rate</td><td>2×10-4</td><td>Minimum learning rate</td><td>2×10-5</td></tr><tr><td>Minimum learning rate</td><td>2×10-5</td><td>Learning rate scheduler</td><td>Cosine with warmup</td></tr><tr><td>Learning rate scheduler</td><td>Cosine with warmup</td><td>Warmup ratio</td><td>5%</td></tr><tr><td>Warmup ratio</td><td>0.625% (~12.5k steps)</td><td>Weight decay</td><td>0.0</td></tr><tr><td>Weight decay</td><td>0.05</td><td>Dφupdate start</td><td>37.5% (~750k steps)</td></tr><tr><td>Gradient clip (max norm)</td><td>1.0</td><td>Ladvstart</td><td>40.0% (~800k steps)</td></tr><tr><td>EMA decay</td><td>0.999</td><td></td><td></td></tr></table>

# E.3 Comparison to baseline methods

Figure 14–16 show qualitative comparisons between GeoGPT [50], PhotoNVS [71], VIVID [17], and OVIE on the RealEstate10K [78] dataset.

# E.4 Side-by-side navigation clips

Please refer to the accompanying supplementary .zip archive for .gif files demonstrating OVIE’s performance on continuous trajectories. These animations utilize sequences from the RealEstate10K [78] dataset. In each .gif, the left panel displays the ground-truth sequence, while the right panel shows the corresponding novel views generated by our approach. The generated sequence is synthesized by conditioning solely on the first image of the sequence, without utilizing any subsequent ground-truth frames.

# E.5 Real-time interactive navigation clips

Please refer to the accompanying supplementary .zip archive for mp4 screen recordings showcasing the real-time interactive navigation capabilities of OVIE. To achieve this, we map standard mouse and keyboard actions to small, incremental changes in the camera’s position and rotation, similar to the control mechanics found in first-person video games. Based on these inputs, we continuously update the camera extrinsics to generate a new image on the fly, conditioned strictly on the initial source image.

图片摘要：该图主要展示 9: Qualitative results on out of distribution images. Each p。
![](images/625b6b97af627db598afb5afbdf195e89426d63e1b9528c561f9fee37700678e.jpg)  
Fig. 9: Qualitative results on out-of-distribution images. Each pair shows the input source image followed by the generated novel view. Source views are, from left to right and top to bottom: Gas by Edward Hopper, Untitled by Ralambo, A Sunday on La Grande Jatte by Georges Seurat, Nighthawks by Edward Hopper, Portrait of an Artist (Pool with Two Figures) by David Hockney, and The Sea of Ice by Caspar David Friedrich.

图片摘要：该图主要展示 9: Qualitative results on out of distribution images. Each p。
![](images/fca9cf2ec9a6d065f4ae6a9f52a7fb715250b56bcd05f957dbdbb2dbfeb0a185.jpg)  
Source   
Pseudo-Target   
Generated View

图片摘要：该图主要展示 9: Qualitative results on out of distribution images. Each p。
![](images/aa11157049544ee668011712c748adcb0c151c2a5c7198796390846d889f3ced.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/3895064220d51865e3162005d2986d3738f7b6fe9bc85ec5f524e623948f0f84.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/b7cbb2c639d00ceab79e298609e4ad21e0d265548c7bc8511de1bd2b62f9e423.jpg)

图片摘要：该图片与Generated View这部分内容相关。
![](images/fb3733a54591bf44a8b2aeee2eb373c7397eb0c1a8063fd67a699b2c21912dd1.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/e0094f3f5870df0ab1933d132b5bb9ee7cbb30f6d96f1188bef7824bf1275b86.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/97ee84d3b420e562d3a9444ad6bbbd9e5fe7ecbf3758d8d8b6c691822e279c4d.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/070392779d63e67a40584627bcbbb0c13f55424875c79161a993a506669d9d3e.jpg)

图片摘要：该图主要展示 10: Comparison of source inputs, training pseudo targets, an。
![](images/3af19b6fbd42ebb0a915414e1d0d941f41e60f097f4cfbec502b7ac630ac4f93.jpg)

图片摘要：该图主要展示 10: Comparison of source inputs, training pseudo targets, an。
![](images/73e094a5d933ff10886910605e50f182d814e9b084f22674fe3fe3fa2c65ad69.jpg)

图片摘要：该图主要展示 10: Comparison of source inputs, training pseudo targets, an。
![](images/b3181baca0c373c3c415189e789b819438e18683bc33490a1e839e958363ca11.jpg)

图片摘要：该图主要展示 10: Comparison of source inputs, training pseudo targets, an。
![](images/fc4e87a8ef42eb8342eed52e04645132ef55e52825db18bb9d14557611971ff1.jpg)  
Fig. 10: Comparison of source inputs, training pseudo-targets, and generated views. During training, OVIE is supervised on pseudo-targets (middle) created by depth-lifting the source image (left) to a sampled pose. At inference, it generates novel views (right) from a source image and target pose. Here, the generated views are rendered at the same poses as their corresponding pseudo-targets.

图片摘要：该图主要展示 10: Comparison of source inputs, training pseudo targets, an。
![](images/9cb17d6410f889946ae4a52a531f9f01bf3bde1d7413f78bcb64851a66ce9cae.jpg)  
Source   
Pseudo-Target   
Generated View

图片摘要：该图主要展示 10: Comparison of source inputs, training pseudo targets, an。
![](images/10cdf44c56778cdcc70a1530c9cd8613ac14c675da562e71c767b9f45f59abc1.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/fd21ec59de107acb59f9957a7bea1ec8d04a7ded45d555c5adc007447bbcb919.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/a1f754af475afab5ac9cc4b358b335b0fa7a21f6e13ae2804194f7d898955d71.jpg)

图片摘要：该图片与Generated View这部分内容相关。
![](images/ed786f2638ae5333bf74dac5002f25b90a5e94ac02f5ff19cbe8937dd59ec0cf.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/fe4d9d694f8280a0e82e149524eaa4bf6acd441389224d4ab79f4699b773bb2b.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/cd6493c341513daefc088b2ce6f143384c82b25b5f27f1706497b8d2e3d7a60d.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/13555ebc326e87cc25eee7e66f14b305e5013b2b1b9a7988298ffa70a30325b6.jpg)

图片摘要：该图主要展示 11: Comparison of source inputs, training pseudo targets, an。
![](images/5062200f69f84292bce56fe169ddab3a4f3166b1e7e7bbb11bb7417c580aef18.jpg)

图片摘要：该图主要展示 11: Comparison of source inputs, training pseudo targets, an。
![](images/ed7d9afdf9f7812d2cebcd9336552a2d97be54caa80ec0eb7e656a0a2f8abe0e.jpg)

图片摘要：该图主要展示 11: Comparison of source inputs, training pseudo targets, an。
![](images/a1919775d7e8ea470245d9226d52fa78db457605d1d3c965fb482638b625f4bc.jpg)

图片摘要：该图主要展示 11: Comparison of source inputs, training pseudo targets, an。
![](images/bd2b7adba226c0f87c06d49afef2dba34841bb7fe5b1960f43da2c0c32c08a14.jpg)  
Fig. 11: Comparison of source inputs, training pseudo-targets, and generated views. During training, OVIE is supervised on pseudo-targets (middle) created by depth-lifting the source image (left) to a sampled pose. At inference, it generates novel views (right) from a source image and target pose. Here, the generated views are rendered at the same poses as their corresponding pseudo-targets.

图片摘要：该图主要展示 11: Comparison of source inputs, training pseudo targets, an。
![](images/fdbca59fa3f962ba3be1f479dbc5e3e0d448006829a0b1dec0e4d5f4ebb2b8f9.jpg)  
Source   
Pseudo-Target   
Generated View

图片摘要：该图主要展示 11: Comparison of source inputs, training pseudo targets, an。
![](images/5ba34c8df31df22130006b900d8559cf689bddc3803d040b5990191e06078774.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/2209c3b187d61f66e667b78a6511f6ab234f9c21dc23ea60dd4a0af1f467b72b.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/b41470b0058c5ee7914f59ce9a4ad1cc1cc0c5a29ac30edd1300c0a1428adb35.jpg)

图片摘要：该图片与Generated View这部分内容相关。
![](images/0e4b3010085296f2ba40d2589ea6df63f7648eb4c18cf25086425b56a2e571cb.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/b9c3d6581cbbcf7da881c524a3ceb7f2e59597c249fa43a88a6da47865161270.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/68b3d8f87f600036317ff6a4a4cd97ae62c9f09b385ced665f4b19a9b77b6cce.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/a0a149094f7735b1000b4b7e7c390b417fb20f4797e97aa667eb52309e5f2cf4.jpg)

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/ccc579612a70e13d03c4c830c098aee8ed75bfb93badca215b6cfbd03d9b6a76.jpg)

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/942cdaf07c88685f62f078fd890b937b7d120806ebb62370b8da0dbcce721772.jpg)

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/591021c8c6dfd6dc7a2e081a58c1e481eacbfe7fd547a2a520caaeffc17c3257.jpg)

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/a36f02b83824936719d9e733cacd6b46bbd726e75777efd4b4a7e3f90c7b79d6.jpg)  
Fig. 12: Comparison of source inputs, training pseudo-targets, and generated views. During training, OVIE is supervised on pseudo-targets (middle) created by depth-lifting the source image (left) to a sampled pose. At inference, it generates novel views (right) from a source image and target pose. Here, the generated views are rendered at the same poses as their corresponding pseudo-targets.

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/70e88ed4ae20ee75a3881227d62dc7bd374d776ff46315ad6b38b70cde85924a.jpg)  
Source

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/1fd868f0d06f0db937c727fe3f429c82ad57a7238305c246ed9d303a02c60698.jpg)  
Pseudo-Target

图片摘要：该图主要展示 12: Comparison of source inputs, training pseudo targets, an。
![](images/70def5bc061886b177e3f35de522d801f562160719d28a709400e42cba021ea5.jpg)  
Generated View

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/db04b5ba3c908df082b49a7e335dbce5208fbe8859c7e560d9583caccfc20652.jpg)

图片摘要：该图片与Generated View；Pseudo Target这部分内容相关。
![](images/e66837be0268845c95840907845d5280fbd19dd5cc297e10eef67bae23ed8537.jpg)

图片摘要：该图片与Generated View这部分内容相关。
![](images/ff5151dd841189c28f371b18e69e839d73abda5c14705831481d828b3dcb825a.jpg)

图片摘要：该图片与Generated View这部分内容相关。
![](images/5839a0affda60be8df7ab84717edd78dbb4f3782f891ef8d57a2eb1abd1d92e2.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/66fe1e63056d4cff0f5b2153e68238c6c72a037b57f5a4b64971b46bca41a3b8.jpg)

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/31afe26323fca23e60bd1d1377a47922e10c9613f4e4c373cfe4abcab8e080ef.jpg)

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/3e6c28bae963367b1a3211dc6f4c50344bdc8814634a3239f2e5c7993181fd2f.jpg)

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/f3cadee0d726f3c4e229a9f4c965c655b044f749dc956c5bc352a3b6b32371ff.jpg)

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/f0e26e8dff24a0f29e7bbde44c04d1b9322182a2f881ca0981548fb5bbbd6ec3.jpg)  
Fig. 13: Comparison of source inputs, training pseudo-targets, and generated views. During training, OVIE is supervised on pseudo-targets (middle) created by depth-lifting the source image (left) to a sampled pose. At inference, it generates novel views (right) from a source image and target pose. Here, the generated views are rendered at the same poses as their corresponding pseudo-targets.

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/ad5f12d5aaa7367294fe3240d5b7168bd24c7d10d9f5a56a12286c0618bf4ad7.jpg)

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/84e89b047fbc882da6ab74c76e1cdaeb90b61b01d469d60e7ceb20de29503fb6.jpg)

图片摘要：该图主要展示 13: Comparison of source inputs, training pseudo targets, an。
![](images/eaaf70eaada3a5ab834b0893923928be5bc55836d9c785e4bddce8002aa383db.jpg)  
OVIE (Ours)

图片摘要：该图片与OVIE (Ours)这部分内容相关。
![](images/e7ed683b7b0918e3ae13082a0e67efffb062562f1e6c517d2d613938b007b72d.jpg)

图片摘要：该图片与OVIE (Ours)这部分内容相关。
![](images/8e0540b31c8bfd27f4a497262c7ee0d47a69027e9fe23e0bce1dcf805d731735.jpg)

图片摘要：该图片与OVIE (Ours)这部分内容相关。
![](images/6a68fe9959f0485ae85a776bdc1b010e6aa10671c459c553df6da6340fd142db.jpg)

图片摘要：该图片与OVIE (Ours)这部分内容相关。
![](images/f56d3bb59ea24b977db1aaf5c653f2da672447dc0bd4bcc1b7aa7628d5fea955.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/2068c1cff625cecdc1c1976d9e553861e28d00fd2b40b647fb0ef59ddc5dc31d.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/9c073d4c27a5a8436258bb893b44d5241e7cfafd575ee64f399f83f1609bd018.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/ee7436659038e3f41030e2b913f03fdce386eee8d788aeecf3de9bc3d917530a.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/11f5c35eb10d57dcfe7f5e4793e1b8f5b0c278534d52fb820eb48395bab743f6.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/8c9035246084e89d3c95682e8cdd1e50d8ea24481c72f50d2b4e57ff9a5445f8.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/923b1ddfba8372dbbe4cdfb987a0e34208476dc6b22e5fe8cd33d9bae1bb894f.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/d123832166434307eecf66e119b139482cd4f6d06833daca7e53fca589c07659.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/c0975f9635888b170f3ba0334f6ced95b85dc80edcdfc63a679dba715a8d8cdd.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/7e6e5d7c5a2f278439b2d0707123b24000a1eec7ef7544f88461e7474e843445.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/c06d4ecf04bd83509762c4ad476663d942ba60b55fb8dc2f52813fcefa1c3a12.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/b3fbecf44b5691ee1f68f01cc8be74ed9c28691c4fd8f3363d9f236092bad337.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/d8ce14763e4a0c30414a5ae3e7a5683f690de47748a1096d2fb73e2450ad03ea.jpg)

图片摘要：该图片展示了One View Is Enough! Monocular Training for In the Wild Novel View Generation相关内容。
![](images/00526e7908c7b6c82c3d2809aafe311e9e3e62d6a1f229206c8c2f35d696947c.jpg)

图片摘要：该图主要展示 14: Qualitative comparison with state of the art methods. Gi。
![](images/6a6b2ffaad974e9f14f1cd727a822f9dccdfc574789c201a31781c4dda44dbac.jpg)

图片摘要：该图主要展示 14: Qualitative comparison with state of the art methods. Gi。
![](images/5b55b215d5fac4fc460be33e2b48b3db4c06f1d20902eed8467fb1cabc9bb408.jpg)

图片摘要：该图主要展示 14: Qualitative comparison with state of the art methods. Gi。
![](images/745133bb47b9fc19e067fa9e45a8e4e5c3aed6e319bad5f7b034e033bde24330.jpg)

图片摘要：该图主要展示 14: Qualitative comparison with state of the art methods. Gi。
![](images/e8efb725e9deb0265dd9fab72c610ed6e4515d322856700c8f76910b1df2c127.jpg)  
Fig. 14: Qualitative comparison with state-of-the-art methods. Given a source image and target camera pose, each method synthesizes a novel view. Despite training on no multi-view data, OVIE generates novel views that match or exceed the quality of concurrent methods.

图片摘要：该图主要展示 14: Qualitative comparison with state of the art methods. Gi。
![](images/73afa0719530aa595158e1049d7538819a8c411f3651d0c67ffc995ee5240b55.jpg)  
Fig. 15: Qualitative comparison with state-of-the-art methods. Given a source image and target camera pose, each method synthesizes a novel view. Despite training on no multi-view data, OVIE generates novel views that match or exceed the quality of concurrent methods.

图片摘要：该图主要展示 15: Qualitative comparison with state of the art methods. Gi。
![](images/319da21a2337cd4354cbc9b5702c6dcde133258c789a2a5b5bad1985b477596f.jpg)  
Fig. 16: Qualitative comparison with state-of-the-art methods. Given a source image and target camera pose, each method synthesizes a novel view. Despite training on no multi-view data, OVIE generates novel views that match or exceed the quality of concurrent methods.
