# AgentRVOS: Reasoning Over Object Tracks for Zero-Shot Referring Video Object Segmentation

Woojeong Jin∗, Jaeho Lee∗, Heeseong Shin, Seungho Jang, Junhwan Heo, and Seungryong Kim†

# KAIST AI

Project page: https://cvlab-kaist.github.io/AgentRVOS

图片摘要：该图主要展示 1: Teaser. AgentRVOS is a training free agentic pipeline bui。
![](images/08469507ce89e5d3688dfff37addb38d3a791928d1f151a20c3ece68a624ab5f.jpg)  
Candidate Mask Track Generation

图片摘要：该图主要展示 1: Teaser. AgentRVOS is a training free agentic pipeline bui。
![](images/11bc9c9a79495c2cbdbe68c3133bcceb63f6bb71138a0ad11a73efa558ca1abd.jpg)  
Fig. 1: Teaser. AgentRVOS is a training-free agentic pipeline built on the complementary strengths of SAM3 [4] and an MLLM [1, 27]. The MLLM first uses SAM3 to generate candidate mask tracks, then iteratively prunes them through query-grounded reasoning over object-level evidence.

Abstract. Referring Video Object Segmentation (RVOS) aims to segment a target object throughout a video given a natural language query. Training-free methods for this task follow a common pipeline: an MLLM selects keyframes, grounds the referred object within those frames, and a video segmentation model propagates the results. While intuitive, this design asks the MLLM to make temporal decisions before any object-level evidence is available, limiting both reasoning quality and spatio-temporal coverage. To overcome this, we propose AgentRVOS, a training-free agentic pipeline built on the complementary strengths of SAM3 and an MLLM. Given a concept derived from the query, SAM3 provides reliable perception over the full spatio-temporal extent through generated mask tracks. The MLLM then identifies the target through query-grounded reasoning over this object-level evidence, iteratively pruning guided by SAM3’s temporal existence information. Extensive experiments show that AgentRVOS achieves state-of-the-art performance among trainingfree methods across multiple benchmarks, with consistent results across diverse MLLM backbones.

# 1 Introduction

Referring Video Object Segmentation (RVOS) requires generating the segmentation mask tracks of the target object throughout a video based on a given natural language query. Unlike image-level referring segmentation [15, 20, 25], RVOS involves queries that go beyond static appearance descriptions and possesses video-specific challenges such as temporal ordering, complex motions, and inter-object relations [7, 14, 38]. These challenges give rise to two intertwined requirements. First, the model must reason about complex temporal and relational queries that distinguish a specific object among many based on actions, state changes, or inter-object relations. Second, it must ensure dense spatio-temporal coverage, as target objects may be small, non-salient, or appear only briefly within a long sequence.

With the recent advances in multimodal large language models (MLLMs) [12, 21, 24, 31], the strong reasoning capabilities of these billion-scale models have shown significant promise for the RVOS task, particularly in comprehending the complex queries given in the task. Existing approaches adopt MLLMs either through task-specific fine-tuning [3,23,38,40], or more recently, in a training-free manner that directly leverages their native multi-modal reasoning capabilities over images and videos.

For the training-free methods [11,13,16], a common approach is to first identify a set of video frames that are relevant to a given query, and then perform object grounding on this set. Then, a video segmentation model, such as segment anything 2 (SAM2) [29], propagates the initial masks across the remaining frames to produce the full segmentation across the entire video. Consequently, these pipelines heavily rely on the MLLM for both temporal frame selection and spatial grounding. However, MLLMs often operate on sparsely sampled frames due to input token limits, resulting in limited temporal coverage. This makes it difficult to detect objects that appear only briefly or intermittently in long videos, suggesting that offloading precise spatio-temporal perception (i.e., temporal object detection) from the MLLM would allow the model to focus entirely on its primary strength such as complex reasoning.

In this paper, we present AgentRVOS, a training-free agentic pipeline for RVOS that leverages the reasoning capabilities of MLLMs to their fullest extent by incorporating SAM3 [4] as a complementary perceptual tool. Given a textual prompt, SAM3 can process all frames of a video and produce high quality mask tracks for every matching object instance, without the need for additional inputs such as points or bounding boxes. This allows us to reliably detect small, occluded objects, while also recognizing briefly appearing objects that MLLMs often overlook, as SAM3 can examine the entire video rather than sparse samples. Consequently, we can identify exactly which frames a given object appears in with frame-level precision, enabling us to leverage the MLLM to reason within this spatio-temporally constrained segment.

However, SAM3 alone is not sufficient for RVOS, as it is designed to accept concepts–often given as short noun phrases (e.g., “person”, “red car ”)–as inputs, and tends to struggle with complex queries including temporal or relational

图片摘要：该图主要展示 2: Complementary concept of SAM3 and MLLM. SAM3 [4] can prec。
![](images/6896440a531bc8802c81af71b1bdf4319e57f11f7bcfda42052879f14c31b3d7.jpg)  
“Sheep eating food from bowl then leaving”   
Fig. 2: Complementary concept of SAM3 and MLLM. SAM3 [4] can precisely identify objects without missing a single frame, but struggles with complex queries. MLLMs [1, 21, 27], on the other hand, offer strong reasoning capabilities, but operate on sparse frames and struggle with non-salient objects. AgentRVOS combines the advantages of both SAM3 and MLLM, by interleaving the two models in a complementary manner.

comprehension. For instance, given “the person who stands up after sitting”, SAM3 can easily locate each person in the video, but cannot determine which one exactly is exhibiting the described behavior. This is where the reasoning capability of MLLMs becomes essential. Given the candidate tracks produced by SAM3, the MLLM determines which one corresponds to the target by performing fine-grained temporal and relational reasoning over the full sentence query. In this way, SAM3 and MLLM complement each other: SAM3 provides reliable perception over the full spatio-temporal extent of the video, while the MLLM contributes comprehensive query-grounded reasoning over the resultant object-level evidence, as illustrated in Fig. 1.

Translating this complementary structure into practice requires addressing an additional challenge: SAM3’s concept-level candidate generation is intentionally exhaustive, producing a large and diverse candidate pool to ensure high recall. Presenting all candidates to the MLLM at once, however, is impractical, as overlapping mask visualizations may degrade reasoning quality and candidates may span different temporal intervals.

We therefore design AgentRVOS as an iterative agentic pipeline that progressively narrows both the candidate set and the temporal scope. At each iteration, MLLM progressively accepts or rejects candidates based on available evidence, while SAM3’s temporal existence information guides focused re-examination of

the remaining uncertain cases. Through this progressive narrowing–fewer candidates, tighter temporal windows, and simpler reasoning at each iteration–the pipeline converges on the target object without requiring an explicit frame selection module or exhaustive processing of the entire video.

Our contributions are summarized as follows:

– We propose AgentRVOS, a training-free agentic pipeline for RVOS that combines SAM3’s language-grounded perception with the MLLM’s reasoning capabilities. By delegating object detection and temporal localization to SAM3, our pipeline allows the MLLM to reason over structured, object-level evidence.   
– We introduce an iterative spatio-temporal pruning strategy in which the MLLM progressively eliminates candidates while SAM3’s temporal existence information narrows the relevant temporal scope, decomposing the complex selection problem into progressively simpler reasoning steps.   
– Extensive experiments demonstrate that AgentRVOS achieves state-of-theart performance across multiple benchmarks. Our pipeline consistently shows strong results with various open-source and closed-source MLLMs, demonstrating its generalizability.

# 2 Related Work

Referring Video Object Segmentation. RVOS aims to segment target objects in a video based on natural language expressions. Earlier RVOS datasets [8, 17, 30] mainly focused on appearance-based expressions, where objects could be identified through static visual attributes. Consequently, pioneering works [5,10, 26, 30, 36] demonstrated that query-based architectures–built upon DETR [5]– can effectively link appearance-based textual descriptions with visual representations of objects. However, more recent benchmarks introduce more challenging queries that go beyond appearance-based descriptions. For example, MeViS [7] introduces motion-centric expressions that require temporal reasoning and, ReVOS [38] requires strong reasoning capabilities and world knowledge. These emerging datasets highlight the need for reasoning capabilities beyond simple appearance matching.

MLLM-based Reasoning Video Object Segmentation. To enhance reasoning ability for more and more challenging RVOS datasets, recent methods incorporate multimodal large language models (MLLMs) [1, 2, 6, 21] with foundation segmentation models [18, 29] through large-scale supervised finetuning [3, 38, 40] or reinforcement learning based optimization [22, 37]. These approaches demonstrate strong performance and improved generalization to outof-distribution samples.

However, such training-based paradigms typically require substantial annotated data and computational resources. To address these issues, training-free agentic approaches that leverage the zero-shot reasoning capability of MLLMs

图片摘要：该图主要展示 3: Overall pipeline. Given a video and a natural language qu。
![](images/c325cbf8353b322c4b0ba330befdeefb938766df2580729bd93fd7117a35608d.jpg)

图片摘要：该图主要展示 3: Overall pipeline. Given a video and a natural language qu。
![](images/918943c87362ce3d7dea7ebccb435bcf795ba9d8a5a0cf4d155fd9fd5d5f1ac1.jpg)  
Fig. 3: Overall pipeline. Given a video and a natural language query, our pipeline operates in two phases. In Candidate Mask Track Generation (Sec. 3.2), the MLLM first analyzes the query to extract concepts, which SAM3 uses to produce temporally consistent candidate mask tracks; this process iterates to ensure sufficient coverage. In Iterative Spatio-temporal Pruning (Sec. 3.3), the MLLM reasons over the candidate pool, classifying each candidate as Accepted, Rejected, or Uncertain, while progressively narrowing the spatio-temporal scope until convergence.

have recently emerged. For example, CoT-RVS [16] exploits the zero-shot Chainof-Thought capability of MLLMs to select key frames, applies an image segmentation model to obtain masks for the target object on the selected frames, and propagates them across the video using a video processor. Similarly, Refer-Agent [13] leverages CLIP [28] and MLLMs for frame selection and utilizes MLLM-based grounding to prompt segmentation models. Although these methods achieve competitive results without additional training, they rely heavily on the reasoning and grounding capabilities of MLLMs. MLLMs possess strong reasoning capabilities, but they typically process only a limited subset of frames due to token limitations. As a result, the model may struggle to perform reasoning centered on the referred object, particularly when the target object appears only sparsely over time. Moreover, the zero-shot grounding capability of MLLMs remains limited when handling small, blurred, or visually ambiguous objects, which can propagate errors across the video.

To address this limitation, we introduce AgentRVOS, a training-free agentic pipeline which incorporates SAM3 to provide dense spatio temporal object-level evidence across the entire video. This allows the MLLM to focus on querygrounded reasoning over reliable object-level cues.

# 3 Method

# 3.1 Problem Formulation and Overview

Given a video $\mathcal { V } = \{ I _ { t } \} _ { t = 1 } ^ { T }$ consisting of $T$ frames and a natural language query $Q$ , Referring Video Object Segmentation (RVOS) aims to predict a sequence

of $T$ binary masks $\mathcal { M } \in \{ 0 , 1 \} ^ { T \times H \times W }$ corresponding to the specified object, where $H$ and $W$ denote the spatial dimensions. To effectively tackle this, our approach leverages a synergistic integration of SAM3 [4] and an MLLM [1, 27]. The MLLM enhances SAM3’s capabilities by translating the complex query $Q$ into a more interpretable prompt, while SAM3 reciprocates by extracting precise spatio-temporal mask tracks. These generated tracks serve as focused visual priors, enabling the MLLM to perform targeted reasoning on specific object candidates rather than exhaustively processing the entire video at once.

Realizing this complementary pipeline, however, requires addressing two core challenges. First, the candidate mask tracks produced by SAM3 must actually contain the referred object; incomplete coverage at this stage cannot be recovered by later reasoning. Second, because SAM3 operates with limited semantic understanding of $Q$ , necessitating a subsequent reasoning phase that can reliably distinguish the exact target. Our method therefore proceeds in two phases: a candidate generation phase that prioritizes recall to ensure coverage, followed by a spatio-temporal pruning phase in which the MLLM leverages the objectlevel evidence provided by these tracks to identify and retain only the referred object.

In the first phase, Candidate Mask Track Generation (Sec. 3.2), the pipeline constructs a comprehensive pool of object candidates from the video. The MLLM first analyzes the query $Q$ to determine whether it can be resolved from language alone (i.e., referring) or requires visual context from the video (i.e., reasoning). Based on this, the MLLM extracts concept-level inputs, especially noun-phrase inputs, and SAM3 then generates temporally consistent candidate mask tracks for each concept. This process iterates to ensure sufficient candidate coverage, expanding to broader or alternative concepts when the initial set is insufficient. In the second phase, Iterative Spatio-temporal Pruning (Sec. 3.3), the MLLM performs query-grounded reasoning over the full candidate pool to identify the target. At each iteration, the MLLM classifies candidates as [Accepted, Rejected, Uncertain]. The temporal scope is then narrowed to focus on the frames where uncertain candidates exist, and the pruning repeats until no uncertain candidates remain. A detailed description of AgentRVOS is provided in Appendix A.2–A.4.

# 3.2 Candidate Mask Track Generation

While it would be straightforward to directly predict mask tracks with SAM3 with the given query $Q$ , SAM3 is trained to segment concepts - mainly referring to short noun phrases (e.g., “person”, “red car ”), and tends to struggle with complex queries in RVOS, which requires comprehensive temporal or relational understanding. This motivates us to break down the complex query into simpler and more understandable concepts for SAM3 to handle.

Concept Extraction. To this end, we first use the MLLM to pre-process the query $Q$ and extract a set of concepts $C$ that SAM3 can handle more reliably.

For referring queries, the target itself is self-contained in the query (e.g., “the cat sitting on the red couch”) and therefore can be identified from language alone without accessing the video. For reasoning queries, where the target is defined through temporal or contextual cues that require visual understanding (e.g., “the one that moves fastest”), the object itself cannot be inferable solely from the language query. Thus, the MLLM examines sampled video frames alongside the query to infer the relevant object categories.

For extraction, we define two levels of granularity to ensure robustness: core concepts and broader concepts. Core concepts directly correspond to the objects referred to in the query, and broader concepts, paired with the core concept, are aimed to capture more general categories that can help SAM3 detect instances missed by the core concept. For example, given “the person who stands up after sitting on the red couch”, the core concepts would be [person, couch] and the paired broader concepts [human, furniture], respectively.

Mask Track Generation via SAM3. With the extracted concepts, we can directly infer SAM3 with the concepts as textual prompts to obtain mask tracks. Between the core and broader concepts from a pair in $C$ , we select the one that yields more instances from SAM3 to prevent the pipeline from missing out objects, as illustrated in Fig. 3. We collect the mask tracks for each concept pair in $C$ , yielding a set of mask tracks $M \in \{ 0 , 1 \} ^ { I \times T \times H \times W }$ , which serve as a pool of candidate masks, where $I$ is the number of instances.

Nonetheless, even with core and broader concepts, SAM3 can still sometimes fail to detect an instance, i.e. $I = 0$ , even with the broader concepts from the extraction stage. In this case, we cascade the extraction process while revising the concepts. Specifically, the subsequent iteration would generate more broadly scoped concepts for referring queries, or exploring alternative object categories for reasoning queries until it is identified by SAM3 in the video.

Each candidate mask $m _ { i } \in M$ carries two types of information: i) spatial localization through the per-frame segmentation mask, and ii) temporal existence through the set of frames in which the object is present, denoted as $\mathcal { T } ( m _ { i } ) = \{ t \mid m _ { i } ^ { t } \neq \emptyset \}$ , where $m _ { i } ^ { t }$ denotes the binary mask for instance $i$ at frame $t$ . This temporal existence information, a natural byproduct of SAM3’s videolevel processing, plays a central role in the subsequent pruning phase (Sec. 3.3).

# 3.3 Iterative Spatio-temporal Pruning

Given the generated pool of candidate masks $M$ , we leverage the complex reasoning capabilities of MLLMs to obtain the query-grounded mask track $\mathcal { M }$ , which the ability SAM3 lacks. As we have the spatio-temporal masks, we can naturally apply visual prompting [4, 39] on the video to allow the MLLMs to further focus on the objects, as shown in Fig. 3. However, evaluating all candidates in a single pass can be impractical: the pool may contain numerous objects with overlapping masks that would clutter the MLLM, and different candidates may appear at different temporal locations, making a single round of frame sampling

insufficient to fairly assess all of them. We therefore adopt an iterative pruning strategy that progressively reduces both the candidate set and the temporal scope, to allow the MLLM to concentrate its reasoning on increasingly fewer, harder cases.

Candidate Pruning. At each iteration $r$ , the MLLM examines the current candidate set $M ^ { ( r ) }$ and classifies each candidate into one of three categories: Accepted (confidently matching the query), Rejected (confidently not matching), or Uncertain (requiring further evidence). Accepted candidates are collected and merged into the output set $\begin{array} { r } { \mathcal { M } = \bigcup _ { r } \{ m _ { i } \in M ^ { ( r ) } \ | \ \mathsf { A c c e p t e d } \} } \end{array}$ ; rejected candidates are permanently discarded. Only uncertain candidates carry forward to the next iteration:

$$
M ^ {(r + 1)} = \left\{m _ {i} \in M ^ {(r)} \mid \text {U n c e r t a i n} \right\}. \tag {1}
$$

By committing to confident decisions early, the MLLM avoids repeatedly reevaluating clear cases and concentrates its reasoning on genuinely ambiguous candidates.

Temporal Scope Pruning. As the candidate set shrinks, the relevant temporal scope naturally contracts as well. At iteration $r$ , the system restricts the temporal scope to the union of frames where the remaining uncertain candidates exist:

$$
\mathcal {T} ^ {(r + 1)} = \bigcup_ {m _ {i} \in M ^ {(r + 1)}} \mathcal {T} (m _ {i}). \tag {2}
$$

Frames are then sampled exclusively within $\mathcal { T } ^ { ( r + 1 ) }$ , ensuring that every sampled frame contains at least one uncertain candidate.

This achieves two effects simultaneously: it increases the density of informative content in the MLLM’s visual input, and it reduces the total temporal span under consideration. Notably, this mechanism requires no explicit frame selection module–the temporal narrowing emerges naturally from SAM3’s temporal existence information.

Convergence. The iterative process terminates when no uncertain candidates remain, i.e., $M ^ { ( r + 1 ) } = \varnothing$ , meaning all candidates have been either accepted or rejected. In practice, we also impose a maximum iteration count to bound computational cost. Since $| M ^ { ( r + 1 ) } | \le | M ^ { ( r ) } |$ at every non-trivial iteration, the process is guaranteed to terminate. We observe that most queries converge within a small number of iterations, as the progressive narrowing rapidly reduces ambiguity (see Sec. 4).

# 4 Experiments

Datasets and Metrics. We evaluate our method on three major benchmarks for language-guided video object segmentation: MeViS [7], ReVOS [38], and ReasonVOS [3]. These datasets pose distinct challenges. MeViS features complex

Table 1: Comparison with state-of-the-art methods on Referring and Reasoning VOS Benchmarks: MeViS [7], ReVOS [38] and ReasonVOS [3]. Qwen3-VL-8B-T and Qwen3-VL-32B-T indicate Qwen3-VL-8B-Thinking [1] and Qwen3-VL-32B-Thinking model, respectively. The best performing results are presented in bold, while the second-best results are underlined. † denotes our reproduced results.   

<table><tr><td rowspan="3">Method</td><td rowspan="3">MLLM</td><td colspan="3">MeViS</td><td colspan="9">ReVOS</td><td colspan="3">ReasonVOS</td></tr><tr><td rowspan="2">J</td><td rowspan="2">F</td><td rowspan="2">J&amp;F</td><td colspan="3">Referring</td><td colspan="3">Reasoning</td><td colspan="3">Overall</td><td rowspan="2">J</td><td rowspan="2">F</td><td rowspan="2">J&amp;F</td></tr><tr><td>J</td><td>F</td><td>J&amp;F</td><td>J</td><td>F</td><td>J&amp;F</td><td>J</td><td>F</td><td>J&amp;F</td></tr><tr><td colspan="17">Training-based Methods</td></tr><tr><td>VideoLISA [3]</td><td>LLaVA-3.8B</td><td>41.3</td><td>47.6</td><td>44.4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>45.1</td><td>49.9</td><td>47.5</td></tr><tr><td>VISA [38]</td><td>Chat-UniVi-13B</td><td>41.8</td><td>47.1</td><td>44.5</td><td>55.6</td><td>59.1</td><td>57.4</td><td>42.0</td><td>46.7</td><td>44.3</td><td>48.8</td><td>52.9</td><td>50.9</td><td>-</td><td>-</td><td>-</td></tr><tr><td>HyperSeg [34]</td><td>Mipha-3B</td><td>-</td><td>-</td><td>-</td><td>56.0</td><td>60.9</td><td>58.5</td><td>50.2</td><td>55.8</td><td>53.0</td><td>53.1</td><td>58.4</td><td>55.7</td><td>-</td><td>-</td><td>-</td></tr><tr><td>InstructSeg [35]</td><td>Mipha-3B</td><td>-</td><td>-</td><td>-</td><td>54.8</td><td>59.2</td><td>57.0</td><td>49.2</td><td>54.7</td><td>51.9</td><td>52.0</td><td>56.9</td><td>54.5</td><td>-</td><td>-</td><td>-</td></tr><tr><td>GLUS [23]</td><td>LISA-7B</td><td>48.5</td><td>54.2</td><td>51.3</td><td>56.0</td><td>60.7</td><td>58.3</td><td>48.8</td><td>53.9</td><td>51.4</td><td>52.4</td><td>57.3</td><td>54.9</td><td>47.5</td><td>52.4</td><td>49.9</td></tr><tr><td>ViLLA [32]</td><td>InternVideo2-6B</td><td>46.5</td><td>52.3</td><td>49.4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>54.9</td><td>59.1</td><td>57.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Sa2VA [40]</td><td>InternVL2-8B</td><td>-</td><td>-</td><td>46.9</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>57.6</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Sa2VA [40]</td><td>InternVL3-14B</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>60.7</td><td>-</td><td>-</td><td>-</td></tr><tr><td>RGA3 [33]</td><td>Qwen2.5-VL-7B</td><td>47.4</td><td>52.8</td><td>50.1</td><td>58.7</td><td>62.3</td><td>60.5</td><td>53.1</td><td>57.7</td><td>55.4</td><td>55.9</td><td>60.0</td><td>58.0</td><td>51.3</td><td>56.0</td><td>53.6</td></tr><tr><td>VRS-HQ [9]</td><td>Chat-UniVi-13B</td><td>48.0</td><td>53.7</td><td>50.9</td><td>61.1</td><td>65.5</td><td>63.3</td><td>54.1</td><td>59.4</td><td>56.8</td><td>57.6</td><td>62.5</td><td>60.0</td><td>-</td><td>-</td><td>-</td></tr><tr><td>VideoSeg-R1 [37]</td><td>Qwen2.5-VL-7B</td><td>52.7</td><td>57.8</td><td>55.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>58.2</td><td>64.0</td><td>61.1</td><td>-</td><td>-</td><td>-</td></tr><tr><td colspan="17">Training-free Methods</td></tr><tr><td>AL-Ref-SAM2 [11]</td><td>GPT-4</td><td>39.5</td><td>46.2</td><td>42.8</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CoT-RVS [16]</td><td>Gemma3-12B</td><td>40.3</td><td>48.1</td><td>44.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>43.4</td><td>50.9</td><td>47.1</td><td>47.5</td><td>54.0</td><td>50.7</td></tr><tr><td>CoT-RVS&#x27; [16]</td><td>Qwen3-VL-8B-T</td><td>37.7</td><td>43.9</td><td>40.8</td><td>56.1</td><td>61.5</td><td>58.8</td><td>46.6</td><td>53.0</td><td>49.8</td><td>51.4</td><td>57.3</td><td>54.3</td><td>52.5</td><td>58.9</td><td>55.7</td></tr><tr><td>CoT-RVS [16]</td><td>GPT-4o</td><td>48.7</td><td>55.7</td><td>52.2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>52.8</td><td>59.0</td><td>55.9</td><td>62.4</td><td>68.7</td><td>65.5</td></tr><tr><td rowspan="3">AgentRVOS (Ours)</td><td>Qwen3-VL-8B-T</td><td>59.2</td><td>64.5</td><td>61.9</td><td>58.7</td><td>62.5</td><td>60.6</td><td>56.8</td><td>61.3</td><td>59.0</td><td>57.7</td><td>61.9</td><td>59.8</td><td>65.5</td><td>71.8</td><td>68.6</td></tr><tr><td>Qwen3-VL-32B-T</td><td>65.3</td><td>70.0</td><td>67.7</td><td>62.8</td><td>66.8</td><td>64.8</td><td>58.0</td><td>62.6</td><td>60.3</td><td>60.4</td><td>64.7</td><td>62.5</td><td>67.3</td><td>73.4</td><td>70.4</td></tr><tr><td>GPT-5</td><td>70.4</td><td>75.7</td><td>73.1</td><td>66.8</td><td>70.8</td><td>68.8</td><td>61.4</td><td>66.0</td><td>63.7</td><td>64.1</td><td>68.4</td><td>66.3</td><td>73.1</td><td>78.0</td><td>75.5</td></tr></table>

scenes involving multiple visually similar objects and demands strong motion understanding. ReVOS and ReasonVOS, on the other hand, emphasize reasoningcentric scenarios that require deeper semantic reasoning and world knowledge. Following prior works [3,16], we report region similarity $\mathcal { I }$ (average IoU), contour accuracy $\mathcal { F }$ (mean boundary similarity), and their average $\mathcal { I } \& \mathcal { F }$ .

Implementation Details. We adopt various models as our baseline MLLMs: Qwen3-VL-8B-Thinking [1] and Qwen3-VL-32B-Thinking for open-sourced models, and GPT-5 [27] for closed-source model. As mentioned above, we use additional SAM3 [4] to generate candidate mask tracks. For each video, 16 frames are used by default. The maximum number of iterations is 3 for both concept extraction and iterative spatio-temporal pruning. All experiments are conducted with 4 RTX PRO 5000 Blackwell GPUs. Additional implementation details, including the prompts used in our pipeline, are provided in Appendix B.1.

# 4.1 Quantitative Results

Tab. 1 presents quantitative comparisons with state-of-the-art methods on three challenging RVOS benchmarks: MeViS, ReVOS, and ReasonVOS. As shown in the table, AgentRVOS significantly outperforms existing training-free methods achieving up to 40.0%, 18.6%, 15.3% improvements on MeViS, ReVOS, and ReasonVOS respectively. Even when using the same backbone model, AgentR-VOS significantly outperforms prior approaches. For instance, with Qwen3-VL-

图片摘要：该图主要展示 4: Qualitative results. AgentRVOS effectively resolves chall。
![](images/7e0537672bbc9a691f390a5ba5ba70a58f8d3e38e8d1f31b80ee9d67d44c1162.jpg)

图片摘要：该图主要展示 4: Qualitative results. AgentRVOS effectively resolves chall。
![](images/60519bf1e5919c74e0119f16389a5562fe403016a30dc24ccc9fd9ba143acb3a.jpg)

图片摘要：该图主要展示 4: Qualitative results. AgentRVOS effectively resolves chall。
![](images/346ec79d6532d95d5b81e079e89b853616773debfc2e7453ba99e03e23361a0c.jpg)  
Fig. 4: Qualitative results. AgentRVOS effectively resolves challenging scenarios such as multi-instance ambiguity and temporal reasoning, accurately segmenting the referred objects.

8B-Thinking, AgentRVOS surpasses CoT-RVS [16] using the same model. Moreover, even when compared with pipelines that integrate powerful closed-source models, such as AL-Ref-SAM2 [11] and CoT-RVS with GPT-4o [12], our method still achieves substantially better performance, highlighting the effectiveness of our pipeline design. These results suggest that the spatio-temporal information provided by SAM3 effectively supports MLLMs in both temporal understanding and reasoning over complex video queries.

Furthermore, when stronger MLLMs are integrated into our framework, the performance consistently improves. Using Qwen3-VL-32B-Thinking, AgentR-VOS achieves state-of-the-art performance across all benchmarks, even compared with training based approaches. Replacing the backbone with strong closedsource models like GPT-5 further improves the results, demonstrating the scalability of our pipeline leveraging stronger MLLM reasoning capabilities.

Table 2: Component analysis. We provide ablation study for our core components– (a) retry for the concept extraction in the Candidate Mask Track Generation phase, and (b) the iterative process and (c) temporal scope pruning in the Iterative Spatiotemporal Pruning phase.   

<table><tr><td>Component</td><td>J</td><td>F</td><td>J&amp;F</td></tr><tr><td>(a) w/o Retry in Concept Extraction</td><td>65.6</td><td>71.8</td><td>68.7</td></tr><tr><td>(b) w/o Iteration in Iterative Spatio-temporal Pruning</td><td>63.0</td><td>68.1</td><td>65.6</td></tr><tr><td>(c) w/o Temporal Scope Pruning</td><td>64.2</td><td>70.4</td><td>67.3</td></tr><tr><td>AgentRVOS (Full Pipeline)</td><td>67.1</td><td>73.6</td><td>70.3</td></tr></table>

# 4.2 Qualitative Results

Fig. 4 presents qualitative comparisons between AgentRVOS and CoT-RVS on several challenging referring expressions. In the first example, where multiple instances of the same category appear, AgentRVOS correctly identifies the target by reasoning over inter-object relations, while CoT-RVS fails to distinguish between similar objects. In the second example, our method successfully resolves temporal motion reasoning by identifying the vehicle moving to the left among multiple vehicles. In the third example, AgentRVOS accurately performs instance-level reasoning, distinguishing the correct lamb among the same instances. These results demonstrate the effectiveness of AgentRVOS in accurately segmenting the correct objects under challenging scenarios by enabling stronger query-grounded reasoning. Additional overall reasoning process and qualitative results are provided in the Appendices A.5 and A.6, respectively.

# 4.3 Analysis

Component analysis. In Tab. 2, we provide ablation studies for our core components–(a) retry for the concept extraction in Candidate Mask Track Generation, (b) iteration and (c) temporal scope pruning in Iterative Spatio-temporal Pruning. For concept extraction, we can clearly observe that the (a) retry strategy, play a significant role for preventing the framework from falling into failure cases where SAM3 is not able to detect any objects. We provide detailed analysis of concept extraction in Tab. 5 and in Fig. 6 below.

For the Iterative Spatio-temporal Pruning phase, we can also observe that both the (b) iteration and (c) temporal scope pruning play a significant role, evident from the gains for our full pipeline. This verifies the effectiveness of the core motivation for our framework - MLLMs can perform better reasoning when the model is able to spatio-temporally focus in a video, as opposed to existing approaches that naïvely employ the MLLMs to reason the entire video at once, with sampled frames. Additional analysis on the effect of MLLM reasoning is provided in Appendix A.1.

Ablation on maximum number of iterations for spatio-temporal pruning. In Tab. 3, we provide quantitative results for varying number of max iterations we apply for Iterative Spatio-temporal Pruning. As shown, we can clearly observe that the iterations show steady improvements, with significant gains up to 3 iterations. As discussed in Sec. 3.3, we observe that most queries converge in small

number of iterations, being 3 in particular, and show minimal improvements with additional iterations further on. Therefore, we set our maximum number of iterations as 3, further iterating the process would increase the inference time with marginal improvements.

Table 3: Results for varying maximum number of iterations.   

<table><tr><td>Max Iteration</td><td>J</td><td>F</td><td>J&amp;F</td></tr><tr><td>1 (No Retry)</td><td>63.0</td><td>68.1</td><td>65.6</td></tr><tr><td>2</td><td>64.4</td><td>70.6</td><td>67.5</td></tr><tr><td>3</td><td>67.1</td><td>73.6</td><td>70.3</td></tr><tr><td>4</td><td>67.4</td><td>73.7</td><td>70.6</td></tr></table>

Ablation on number of sampled frames. Our empirical results show that sampling 16 frames yields the best performance of 70.3 $\mathcal { I } \& \mathcal { F } .$ . Using fewer frames (8 in this table) limits temporal coverage, while increasing beyond 16 introduces redundancy that may hinder the reasoning ability of the MLLM, with diminishing returns in both accuracy and computational cost. We use 16 frames as the default for all other experiments.

Table 4: Effect of the number of sampled frames.   

<table><tr><td># of Frames</td><td>J</td><td>F</td><td>J&amp;F</td></tr><tr><td>8</td><td>64.6</td><td>70.7</td><td>67.6</td></tr><tr><td>16</td><td>67.1</td><td>73.6</td><td>70.3</td></tr><tr><td>32</td><td>65.6</td><td>72.1</td><td>68.8</td></tr><tr><td>64</td><td>64.9</td><td>71.5</td><td>68.2</td></tr></table>

Effectiveness of iteration for Iterative Spatio-temporal Pruning. In Fig. 5, we provide detailed visual analysis of the effects of iteration for our Iterative Spatio-temporal Pruning phase. For simple cases, as shown on the top, we can observe that the MLLM is able to confidently classify objects into Accepted or Rejected, thus not resulting in redundant iterations. In more challenging examples, we can observe that the MLLM is capable of identifying objects that the model is uncertain at first glance. As for the example shown in the middle bottom row, we can observe the framework iteratively rejecting objects and focusing on more confusing objects.

Effectiveness of iteration for concept extraction. In Tab. 5, we report the ratio of empty masks generated from the Candidate Mask Track Generation phase for different number of iterations applied for the concept extraction process. As a comparison, we also report the ratio of empty masks from CoT-RVS [16], where CoT-RVS leverages CLIP to identify query-relevant frames to reason with

Table 5: Effects of iterations on the ratio of empty mask prediction $( \% )$ .   

<table><tr><td>Iterations</td><td>Empty Mask Ratio (%)</td></tr><tr><td>CoT-RVS [16]</td><td>12.0</td></tr><tr><td>1</td><td>4.9</td></tr><tr><td>2</td><td>4.1 (-0.8)</td></tr><tr><td>3</td><td>3.8 (-1.1)</td></tr></table>

图片摘要：该图主要展示 5: Effects of iterations on the ratio of empty mask predicti。
![](images/2728f5590a53711cb1916574abd7d2bb9c7844885732ea88a8dbdfce8a7007ce.jpg)  
Fig. 5: Qualitative results of iteration in Iterative Spatio-temporal Pruning. We illustrate how our iterative spatio-temporal pruning progressively narrows the relevant temporal window and eliminates irrelevant track candidates. Across iterations, the remaining candidates become fewer but more query-consistent, leading to the final selected track set.

the MLLM. We can clearly observe that even without additional iterations, we show significantly lower ratio for having empty masks, demonstrating the effectiveness of our approach with MLLM and SAM3. Further adding iterations to the concept extraction stage minimizes the ratio for having empty masks generated from SAM3.

We further provide detailed visual analysis in Fig. 6, where in Fig. 6(a) the framework is able to identify objects that were not previously identified for the reasoning queries (e.g. folded paper). Furthermore, we can also observe cases where the subsequent retry processes revise the concept as a more general (Fig. 6(b)) or more specific (Fig. 6(c)) concept for the referring queries, allowing SAM3 to correctly identify objects that it was previously not able to segment.

# 5 Conclusion

In this paper, we present AgentRVOS, a training-free agentic pipeline that combines SAM3’s language-grounded perception with the MLLM’s reasoning capability for Referring Video Object Segmentation tasks. By leveraging SAM3 for object detection and temporal localization, our pipeline enables the MLLM to perform query-grounded reasoning over structured object-level evidence rather than the entire video directly. To effectively utilize this complementary design, we introduce an iterative spatio-temporal pruning strategy that progressively narrows the candidate set and temporal scope, allowing the MLLM to focus on ambiguous objects and refine its reasoning iteratively. Extensive experiments

# Iteration #1

["aircraft", "vehicle”]

# Iteration #2

["folded paper", "object"]

图片摘要：该图片与“will probably turn out to be a handmade aircraft.”；Iteration 1这部分内容相关。
![](images/8e03c1b4f5e99b4529867a6455c073dc3b8e2baaad7878f6df671124b4b9d136.jpg)  
“will probably turn out to be a handmade aircraft.”

# Iteration #1

["creature", "animal”]

# Iteration #2

["hand", "body part"]

图片摘要：该图片与“the creature(s) that picks up and puts down the waist bag.”；(a) Class changing这部分内容相关。
![](images/0d821dac812369eab934bbd0a50e0be8fbd60932df1667740beed427efe97415.jpg)  
“the creature(s) that picks up and puts down the waist bag.”

# (a) Class changing

# Iteration #1

[”basin", "container"]

# Iteration #2

["bowl", "tableware"]

图片摘要：该图片与“Which pot(s) is/are placed at the top of the screen?"；Iteration 1这部分内容相关。
![](images/90d85286de666adb2428f531f9873cb5485827dc83b302715de6ca809b6d748c.jpg)  
“Which pot(s) is/are placed at the top of the screen?"

# Iteration #1

["tray", "container"]

# Iteration #2

["box", "object"]

图片摘要：该图片与“square object(s) with blue border on the table.”；(b) Specific to General Concep这部分内容相关。
![](images/aa53e344875c48007b41ab50af73960b03b12a6b950c1202f0ffb14682c8ce8a.jpg)  
“square object(s) with blue border on the table.”

# (b) Specific to General Concept

# Iteration #1

["utensil", "tool"]

# Iteration #2

[” plate", "tableware"]

图片摘要：该图片与“utensil(s) for holding food with a shallow bottom.”；Iteration 1这部分内容相关。
![](images/305e938158567ed315a1fd1e6a5422ee5cb24405b7727e07182b564b5123257a.jpg)  
“utensil(s) for holding food with a shallow bottom.”

# Iteration #1

["ship", "vehicle"]

# Iteration #2

["boat", "None"]

图片摘要：该图主要展示 6: Qualitative results of iteration in Concept Extraction. W。
![](images/f04e45d59468d97845250572866bef98a6bc07dc5663e3069c46e2e1f31bba0a.jpg)  
Fig. 6: Qualitative results of iteration in Concept Extraction. We visualize how our iterative concept extraction progressively refines object concepts from the query. From top to bottom, the iterative process refines concepts through three distinct patterns: (a) the extracted concept class changes entirely to better match the query, (b) a specific concept is broadened to a more general one, and (c) a vague concept is narrowed to a more precise one, each converging to concepts better aligned with the query’s intent.

“the white ship(s) that is/are moving rapidly on the water surface."

# (c) General to Specific Concept

across multiple RVOS benchmarks and various MLLM backbones demonstrate the effectiveness of AgentRVOS, highlighting the complementary strengths of SAM3’s spatio-temporal perception and MLLM-based reasoning.

# Appendix Overview

The appendix is organized as follows.

– Sec. A presents additional experiments and analyses:

- Ablation on the effect of MLLM reasoning (Sec. A.1)   
- Robustness of Concept Extraction (Sec. A.2)   
- Details of Visual Prompting (Sec. A.3)   
- Detailed Algorithm of AgentRVOS (Sec. A.4)   
- Visualization of Overall Reasoning Process of AgentRVOS (Sec. A.5)   
- Additional Qualitative Results (Sec. A.6)

– Sec. B provides implementation details of AgentRVOS:

- Ablation study configurations (Sec. B.1)   
- Detailed prompts used in AgentRVOS (Sec. B.2)

– Sec. C discusses future directions.

# A Additional Results and Analyses

# A.1 Ablation on the Effect of MLLM reasoning

Table A1: Ablation on MLLM reasoning. Replacing our MLLM-based reasoning pipeline with direct input of the referring expression into SAM3 leads to a substantial drop in segmentation accuracy and a sharp increase in empty mask ratio, demonstrating that MLLM reasoning is essential for handling the complexity of referring expressions.   

<table><tr><td>Methods</td><td>Empty Mask Ratio (%)</td><td>J</td><td>F</td><td>J&amp;F</td></tr><tr><td>SAM3 [4]</td><td>38.9</td><td>36.8</td><td>44.7</td><td>40.8</td></tr><tr><td>AgentRVOS</td><td>3.8 (-35.1)</td><td>67.1 (+30.3)</td><td>73.6 (+28.9)</td><td>70.3 (+29.5)</td></tr></table>

We evaluate the necessity of MLLM-based reasoning in our agentic pipeline by replacing it with direct input of the referring expression into SAM3 [4]. Since SAM3 is designed to process simple noun phrases rather than complex linguistic queries, this baseline bypasses query-grounded reasoning entirely. As shown in Tab. A1, removing MLLM reasoning leads to a substantial performance drop of 29.5 points in $\mathcal { I } \& \mathcal { F }$ (40.8 vs. 70.3), alongside a sharp increase in the empty mask ratio from 3.8% to $3 8 . 9 \%$ , confirming that SAM3 alone cannot adequately handle the semantic complexity of referring expressions. These results demonstrate that the complementary roles of SAM3 and the MLLM are both necessary, where SAM3 provides reliable perceptual grounding while MLLM reasoning is essential for interpreting the query and resolving ambiguity among candidate tracks.

图片摘要：该图主要展示 A1: Ablation on MLLM reasoning. Replacing our MLLM based rea。
![](images/62134403088a789ece35adb4d2828f17144b3f6ed1164a72023c77075d206658.jpg)  
(a) Referring

图片摘要：该图主要展示 A1: Concept extraction for referring and reasoning queries. 。
![](images/0d118e020b0f6ac850a56c1c45873921373c384c6a6d50afcb7889c0f88c4132.jpg)  
(b) Reasoning   
Fig. A1: Concept extraction for referring and reasoning queries. For referring queries (a), the target is identifiable from the expression alone, so SAM3 is applied directly using the extracted concept. For reasoning queries (b), resolving the referent requires visual evidence, so the video is provided alongside the expression. Notably, SAM3 is applied across all frames rather than a sampled subset, enabling reliable detection even when the target object appears in only a small fraction of the video, as illustrated by the “hand ” visible in just two frames.

# A.2 Robustness of Concept Extraction

We provide further detail on the concept extraction step introduced in Sec. 3, focusing on how it handles diverse query types and why it reliably satisfies the coverage requirement of the candidate generation phase. The behavior of concept extraction is driven by the type of the given language query $Q$ . Although this step may appear fragile–particularly for queries that resist direct noun extraction (e.g. “what made the dogs move”)–our pipeline explicitly accounts for the query type before invoking SAM3.

Specifically, we distinguish between two cases. For referring queries, the target object is identifiable from $Q$ alone without visual evidence (Fig. A1 (a)). In this case, concept extraction proceeds from text only, and the resulting concepts reliably anchor SAM3 to the correct object category. For reasoning queries, the target object cannot be determined without observing the video (Fig. A1 (b)). Here, the MLLM examines uniformly sampled frames alongside $Q$ to infer plausible candidate concepts. In most cases, this is sufficient to identify the target object. However, in extreme cases the referred object may not be clearly visible in the sampled subset–a hand appearing in only two frames, for instance, could be entirely absent from a uniform sample. Even so, the MLLM can still propose plausible candidates such as “person” or “hand” by reasoning about the expression and the available visual context. Because SAM3 processes all frames rather than only the sampled subset, it can verify whether these candidates actually exist anywhere in the video, reliably capturing objects that uniform sampling alone would miss.

图片摘要：该图主要展示 A1: Concept extraction for referring and reasoning queries. 。
![](images/7b422bd1069d3487e5f3cdf37d4329c3a713d99866141b3dd5801b5abac1d391.jpg)  
Fig. A2: Details of appearance tool. Between candidate mask track generation and iterative spatio-temporal pruning, the appearance tool can be optionally invoked to obtain appearance information that may be obscured by visual prompting. When the agent determines that appearance-level evidence is needed for reasoning, it generates a brief phrase describing each candidate object’s appearance.

This design directly addresses the coverage requirement identified in Sec. 3: candidate tracks that do not contain the referred object cannot be recovered by subsequent reasoning. By converting the language query into SAM3-compatible noun phrases according to the query type, concept extraction ensures that the candidate pool is sufficiently complete before the spatio-temporal pruning phase begins.

# A.3 Details of Visual Prompting

In the iterative spatio-temporal pruning stage, the MLLM reasons over maskoverlaid videos where each candidate mask track is visualized with a distinct color [4, 39]. While this visual prompting strategy is essential for grounding the MLLM’s focus to specific object regions, it inevitably obscures the original appearance of each instance, including color, texture, and other fine-grained visual details. This can be problematic when the referring expression hinges on such appearance cues (e.g., “Parking white car”).

To mitigate this, we introduce a simple appearance tool that can be optionally invoked before pruning begins. A brief illustration is provided in Fig. A2. When the MLLM determines that appearance-level evidence is needed, the tool constructs a two-panel image (which we refer to as a reference image) for each candidate following a similar visualization strategy to SAM3 Agent [4]: a loosely cropped view with the bounding box for spatial context, and a tightly cropped view for fine-grained appearance. Notably, for each candidate object, we select the single frame index where the object has the largest visible area, which is obtained from the mask track information produced by SAM3. The MLLM then generates a brief natural language description of each candidate’s appearance,

Table A2: Ablation for appearance tool call.   

<table><tr><td>Component</td><td>J</td><td>F</td><td>J&amp;F</td></tr><tr><td>w/o Appearance Tool</td><td>64.6</td><td>70.9</td><td>67.7</td></tr><tr><td>AgentRVOS</td><td>67.1</td><td>73.6</td><td>70.3</td></tr></table>

which is carried forward into the pruning stage as supplementary evidence. Additionally, as shown in Tab. A2 (the results were obtained under the same setting as the ablation studies), incorporating the appearance tool yields some improvement, confirming that it effectively recovers appearance information lost under the visual overlay.

# A.4 Detailed Algorithm

We provide a detailed description of the AgentRVOS pipeline through three algorithms. Algorithm 1 (Candidate Mask Track Generation) generates candidate mask tracks by extracting concept pairs from the query using an MLLM and prompting SAM3 with these concepts. Algorithm 2 (Appearance Tool) introduces an appearance tool that determines whether additional appearance information is required by the query and extracts it when necessary. Algorithm 3 (Iterative Spatio-temporal Pruning) performs iterative spatio-temporal pruning, where candidate mask tracks are progressively verified and filtered through reasoning over the video and the query.

Candidate Mask Track Generation. Algorithm 1 describes the procedure for generating mask tracks from a natural language query. Given a video $\mathcal { V } = \{ I _ { t } \} _ { t = 1 } ^ { T }$ and a language query $Q$ , the algorithm iteratively extracts concept pairs using an MLLM and uses them to prompt SAM3 for mask track generation.

At the first iteration ( $k = 0$ ), the MLLM receives $Q$ with $\mathtt { p r o m p t } _ { r e f e r r i n g } ( \ S \mathrm { A 9 } )$ The model first determines the query type. If the query corresponds to a referring case, where the referred object can be identified from the textual expression alone, the model directly extracts a set of concept pairs from the query. Otherwise, if the query is classified as reasoning and requires visual information from the video, the model does not extract concept pairs at this stage and instead proceeds to perform video conditioned concept extraction using $\mathtt { p r o m p t } _ { r e a s o n i n g } ( \ S \mathrm { \ A 1 0 } )$ . Each extracted concept pair, indexed by $_ i$ , consists of a core concept $c _ { i } ^ { c o r e }$ that closely corresponds to the referred object and a broader concept $c _ { i } ^ { b r o a d }$ that represents a more general category, increasing the likelihood iof retrieving candidate tracks. For each concept pair $( c _ { i } ^ { c o r e } , c _ { i } ^ { b r o a d } )$ , SAM3 is applied to the video separately using the core concept and the broader concept, producing two candidate mask tracks. Among the concepts, we retain the track with the larger number of the sum of the total detected instances across frames, and denote this number as Count(·). If no instances are detected, a retry step is performed. Previously failed concept pairs are accumulated in a failure set and

provided to the MLLM in the next iteration to prevent the model from generating similar concepts again. This process continues until a mask track containing at least one detected instance is obtained or the maximum retry limit $k _ { m a x }$ , which is set to 3, is reached. The result of this stage is a set of candidate mask tracks $M$ together with the final selected concepts $C ^ { * }$ which provides class-level information about the target object for the subsequent selection stage.

Appearance Tool. Since mask overlays used during candidate visualization may obscure appearance cues such as color, an additional appearance tool is introduced to explicitly extract appearance information when needed. Algorithm 2 introduces an appearance tool that extracts additional appearance information when required by the query (e.g. “a white dog with black dots”). The MLLM first analyzes the query using promptappearance_requirement(§ A11 (top)) to determine whether appearance attributes are necessary for identifying the target object. If appearance information is required, the MLLM extracts appearance cues using promptappearance_retrieval(§ A11 (bottom)). The MLLM then receives reference images $I$ for all candidate objects as described in Sec. A.3, and extracts an appearance description $\mathcal { A }$ for all candidate objects.

Iterative Spatio-temporal Pruning. Algorithm 3 performs the final selection of the referred object through iterative spatio-temporal pruning of candidate mask tracks. The procedure begins with the candidate mask tracks $M$ obtained from Algorithm 1. The initial temporal scope $\mathcal { T } ^ { ( 0 ) }$ is defined as the union of frame indices where at least one instance is detected in the candidate mask tracks.

To proceed with the selection process, the candidate mask tracks are first visualized on the video frames, producing a masked overlaid video $V ^ { * }$ . At each iteration $r$ , frames are uniformly sampled from the current temporal scope $\mathcal { T } ^ { ( r ) }$ . Each candidate mask track $m _ { i } \in M ^ { ( r ) }$ is then evaluated by the MLLM using $\mathrm { p r o m p t } _ { s e l e c t } ( \ S \qquad )$ , conditioned on the mask overlaid video $V ^ { * }$ , the query $Q$ , the concept for each object $C ^ { * }$ , and the appearance information $\mathcal { A }$ .

Based on this evaluation, each mask track is classified into one of three categories: Accepted, Rejected, or Uncertain. Tracks classified as Accepted are added to the final mask set $\mathcal { M }$ , while tracks labeled Rejected are removed from further consideration. Tracks labeled Uncertain are retained for further evaluation in the next iteration.

As the pruning process progresses, the temporal scope is updated using the temporal spans associated with the uncertain tracks. Specifically, the next temporal set $\mathcal { T } ^ { ( r + 1 ) }$ is defined as the union of the temporal intervals $\tau ( m _ { i } )$ of the uncertain tracks. At the same time, visualization is also restricted to these uncertain candidates, which further reduces the spatial region under consideration. Together, these updates progressively narrow both the temporal and spatial search space to regions where ambiguous candidates remain.

The iterative pruning continues until no uncertain tracks remain or the maximum iteration limit $r _ { m a x }$ , which is set to 3, is reached. The final output of this stage is the set of predicted masks $\mathcal { M }$ .

Algorithm 1 Candidate Mask Track Generation   
Require: Video $\mathcal{V} = \{I_t\}_{t=1}^T$ , Language Query $Q$ , MLLM $\mathcal{L}$ , SAM3 $\mathcal{S}$ Ensure: Candidate Mask Tracks $M \in \{0,1\}^{T \times H \times W}$ , Final selected concepts $C^*$ 1: $k \gets 0$ 2: $M \gets \emptyset$ 3: Fail $\gets \emptyset$ 4: $C^* \gets \emptyset$ 5: while $M = \emptyset \land k \leq k_{\max}$ do  
6: if $k = 0$ then  
7: $A^{(k)} \gets \mathcal{L}(Q, \text{prompt}_{\text{referring}})$ 8: if $A^{(k)}[\text{query type}] = \text{referring}$ then  
9: $C^{(k)} \gets A^{(k)}[\text{concept pairs}]$ 10: else  
11: $A^{(k)} \gets \mathcal{L}(\mathcal{V}, Q, \text{prompt}_{\text{reasoning}})$ 12: $C^{(k)} \gets A^{(k)}[\text{concept pairs}]$ 13: end if  
14: else  
15: $A^{(k)} \gets \mathcal{L}(\mathcal{V}, Q, \text{prompt}_{\text{reasoning}}, \text{Fail})$ 16: $C^{(k)} \gets A^{(k)}[\text{concept pairs}]$ 17: end if  
18: for each ( $c_i^{\text{core}}, c_i^{\text{broad}}$ ) in $C^{(k)}$ do  
19: $M_i^{\text{core}} \gets S(\mathcal{V}, c_i^{\text{core}})$ 20: $M_i^{\text{broad}} \gets S(\mathcal{V}, c_i^{\text{broad}})$ 21: $c_i^{\text{selected}} \gets \text{argmax}_{c \in \{c_i^{\text{core}}, c_i^{\text{broad}}\}} \text{COUNT}(M_i^c)$ 22: $M_i^{\text{selected}} \gets S(\mathcal{V}, c_i^{\text{selected}})$ 23: $C^* \gets C^* \cup c_i^{\text{selected}}$ 24: $M \gets M \cup M_i^{\text{selected}}$ 25: end for  
26: if $M = \emptyset$ then  
27: Fail $\gets \text{Fail} \cup C^{(k)}$ 28: end if  
29: $k \gets k + 1$ 30: end while

<table><tr><td colspan="2">Algorithm 2 Appearance Tool</td></tr><tr><td colspan="2">Require: Language Query Q, MLLM L, Reference images I</td></tr><tr><td colspan="2">Ensure: Appearance information A</td></tr><tr><td>1: B ← L(Q, promptappearance Requirement)</td><td>▷ Check appearance requirement</td></tr><tr><td>2: if B then</td><td></td></tr><tr><td>3: A ← L(I, Q, promptappearance_retrieval)</td><td>▷ Extract appearance descriptions</td></tr><tr><td>4: else</td><td></td></tr><tr><td>5: A ← ∅</td><td></td></tr><tr><td>6: end if</td><td></td></tr></table>

Algorithm 3 Iterative Spatio-Temporal Pruning   
Require: Video $\mathcal{V} = \{I_t\}_{t=1}^T$ , Language Query $Q$ , MLLM $\mathcal{L}$ , Candidate Mask Tracks $M \in \{0,1\}^{T \times H \times W}$ , Appearance information $\mathcal{A}$ , Selected Concepts $C^*$ Ensure: Predicted masks $\mathcal{M} \in \{0,1\}^{T \times H \times W}$ 1: $M^{(0)} \gets M$ , $\mathcal{T}^{(0)} \gets \bigcup_{m_i \in M^{(0)}} \mathcal{T}(m_i)$ , $\mathcal{M} \gets \emptyset$ 2: for $r = 0,1,\ldots,r_{\max}$ do  
3: Uniform sampled frames from $\mathcal{T}^{(r)}$ 4: $V^* \gets \text{visualize}(\mathcal{V}, M^{(r)})$ 5: Classify each $m_i \in M^{(r)}$ as Acc., Rej., or Unc. via $\mathcal{L}(V^*, Q, \text{prompt}_{select}, C^*, \mathcal{A})$ 6: $\mathcal{M} \gets \mathcal{M} \cup \{m_i | \text{Accepted}\}$ 7: $M^{(r+1)} \gets \{m_i \in M^{(r)} | \text{Uncertain}\}$ 8: $\mathcal{T}^{(r+1)} \gets \bigcup_{m_i \in M^{(r+1)}} \mathcal{T}(m_i)$ 9: if $M^{(r+1)} = \emptyset$ then break  
10: end if  
11: end for  
12: return $\mathcal{M}$

# A.5 Visualization of Overall Reasoning Process

We provide end-to-end qualitative visualizations of AgentRVOS in Figs. A3 and A4, illustrating how the pipeline processes a referring expression from concept extraction through iterative spatio-temporal pruning to the final mask track output.

In Fig. A3, the referring expression is “Which car disappears from the scene first? ” The MLLM extracts the core concept “car ” and the broader concept “vehicle.” Since SAM3 detects only 2 objects with the core concept, the pipeline falls back to the broader concept, yielding 4 candidate mask tracks. During iterative spatio-temporal pruning, the MLLM first rejects objects 2 and 3 as bicycles while classifying objects 0 and 1 as uncertain, since both cars remain visible in the sampled frames. In the subsequent iteration, with only the two cars remaining, the MLLM examines their temporal presence more carefully and determines that object 1 disappears first, accepting it as the final output. This example demonstrates a case where candidate pruning alone suffices to resolve the expression.

Fig. A4 presents a more complex case with the expression “Which creature has the minimum energy loss? ” Again, the core concept “monkey” retrieves only

2 objects, so the pipeline falls back to “animal,” yielding 4 candidates. The first pruning iteration rejects the clearly active zebras (objects 2 and 3) while marking objects 4 and 5 as uncertain. In the next iteration, the MLLM observes that object 5 moves more noticeably and rejects it, but remains uncertain about object 4. At this point, temporal scope pruning is triggered: since object 4 mostly does not span the full temporal range of the video, the pipeline restricts reasoning to the temporal scope where only object 4 exists. With this pruned context, the MLLM confirms that object 4 moves less actively compared to the zebras and accepts it as the final answer. This example shows how temporal scope pruning complements candidate pruning when spatial reasoning alone cannot fully resolve the expression.

# A.6 Additional Qualitative Results

We present additional qualitative results of AgentRVOS on MeViS [7] (Figs. A5, A6), ReVOS [38] (Fig. A7), and ReasonVOS [3] (Fig. A8). These examples span a diverse range of expression types, from motion-based descriptions and spatial relationships in MeViS, to causal and comparative reasoning in ReVOS, to commonsense and hypothetical reasoning in ReasonVOS. Across all benchmarks, AgentRVOS consistently produces accurate mask tracks, demonstrating its effectiveness.

# B Additional Implementation Details

# B.1 Ablation study configurations

All experiments are conducted via MLLM served through vLLM [19], with temperature set to 0.2 and a maximum of 8192 output tokens. Ablation experiments use Qwen3-VL-8B-Instruct [1] as the MLLM backbone and are evaluated on the MeViS valid u set.

# B.2 Detailed prompts

We provide the prompts used in the AgentRVOS pipeline in Figs. A9, A10 (Concept Extraction), Fig. A11 (Appearance Tool), and Fig. A12 (Iterative Spatiotemporal Pruning).

# C Future Works

As stronger MLLMs such as Gemini-3-Pro [31] continue to emerge, a promising direction is to substitute them into the pipeline, which requires no architectural modification due to the training-free and modular nature of AgentRVOS. To fully leverage their improved reasoning capabilities, exploring more sophisticated prompting strategies such as few-shot examples or structured chain-of-thought is another promising avenue for future work.

# “Which car disappears from the scene first?”

Concept Extraction $^ +$ Mask Track Generation

图片摘要：该图主要展示 A3: Visualization of the overall pipeline of AgentRVOS. This。
![](images/08b6bfb83ec00df667054e71dfc48a759891793aebf1dfa1ebc813f5b54f8a0c.jpg)  
Fig. A3: Visualization of the overall pipeline of AgentRVOS. This example illustrates a case where candidate pruning is applied. AgentRVOS progressively rejects irrelevant objects across iterations and identifies the correct target through proper iterative reasoning.

# “Which creature has the minimum energy loss?”

图片摘要：该图主要展示 A3: Visualization of the overall pipeline of AgentRVOS. This。
![](images/24319eccdb011d65b03fd21040e1b468f62bcf593a197a5d58ca5a534aa92743.jpg)  
Fig. A4: Visualization of the overall pipeline of AgentRVOS. This example illustrates a case requiring both candidate pruning and temporal scope pruning. After spatially narrowing the candidates, the pipeline further restricts the temporal scope to resolve the remaining ambiguity.

图片摘要：该图主要展示 A4: Visualization of the overall pipeline of AgentRVOS. This。
![](images/b614899fe54028988ad411a0b0da878e24bab9505b8834ccd0f51ff85375fdd6.jpg)  
“The distant parked motorcycle.”

图片摘要：该图主要展示 A4: Visualization of the overall pipeline of AgentRVOS. This。
![](images/7fae0a9923618a8a3e7dab4b79a4bacefadb8d8552635c3f6bc03b239cec24cf.jpg)

图片摘要：该图主要展示 A4: Visualization of the overall pipeline of AgentRVOS. This。
![](images/a02219be0799657f21d3fd78b0aafebcff9f1f0df79f9393b46d48763d34c08d.jpg)  
“the little walks back and away”   
“The rabbit that started off in the middle and later moved to the left”

图片摘要：该图主要展示 A5: Qualitative results in MeViS. MeViS [7] expressions requ。
![](images/795f0083e45515db58200b911cbb7c0e754ff02d8b41b03f0e9cbe6c4f42a376.jpg)  
“The white pigeon that has moved a little from the left to the right.”   
Fig. A5: Qualitative results in MeViS. MeViS [7] expressions require understanding object motion and spatial relationships. AgentRVOS successfully identifies targets based on motion descriptions such as walking direction and relative displacement.

图片摘要：该图主要展示 A5: Qualitative results in MeViS. MeViS [7] expressions requ。
![](images/7c8ec4dcce98cb1ebf6d35821f52a82490b16dd1ca73334a1b53a49e3b1279d0.jpg)  
“The pigeon that walked a few steps to the left.”

图片摘要：该图主要展示 A5: Qualitative results in MeViS. MeViS [7] expressions requ。
![](images/ab45aa0548b8d65de6bcbbc0951df7946fa945bccfd059113d95291701134da8.jpg)  
“The zebra remaining stationary without any movement.”

图片摘要：该图主要展示 A5: Qualitative results in MeViS. MeViS [7] expressions requ。
![](images/e1e778dc34d851b0f7ccf867bec2279f990920595e0fd5e1344e877fdbe0f259.jpg)  
“A monkey squatting in the distant right without moving.”

图片摘要：该图主要展示 A6: Qualitative results in MeViS. These examples involve dis。
![](images/8d208ffb5e10d85d92c7ae75848f6da2293d6568e52b128f469f81c56bd40ed0.jpg)  
“The elephant that drank water first.”   
Fig. A6: Qualitative results in MeViS. These examples involve distinguishing among multiple similar objects by their motion patterns, such as remaining stationary or performing a specific action first.

图片摘要：该图主要展示 A6: Qualitative results in MeViS. These examples involve dis。
![](images/fbe60d3cd96727b8cdb07d097ea10b27b464cea83936852f5eb99c6df20e400a.jpg)  
"Which object(s) was/were put into the dustpan and finally fell into the pit?"

图片摘要：该图主要展示 A6: Qualitative results in MeViS. These examples involve dis。
![](images/2800065264e94a1fd38a9475d0850a8ccaa540238088030e9fef669130ab70c2.jpg)  
"Which object has the largest displacement?"

图片摘要：该图主要展示 A6: Qualitative results in MeViS. These examples involve dis。
![](images/4c2f11ab080102d8ed7fb9476607096f43ffef638c50f5f4d41784f882d6a751.jpg)  
“the dog that is not easily found in the dark.”

图片摘要：该图主要展示 A7: Qualitative results in ReVOS. ReVOS [38] expressions oft。
![](images/1c211abf033b8206a4673983e559ef0e3074817eb6feb4c90a4e5188d5dd5377.jpg)  
"Which object(s) might be picked up by the man in black?"   
Fig. A7: Qualitative results in ReVOS. ReVOS [38] expressions often involve complex reasoning about object interactions and scene context. AgentRVOS correctly segments targets described through causal relationships, relative comparisons, and challenging visual conditions.

图片摘要：该图主要展示 A7: Qualitative results in ReVOS. ReVOS [38] expressions oft。
![](images/d9297d0398a6204eb53db8204b8e75fd2b933f66a59dee5a8f4f423fe64bee98.jpg)  
“The vehicle that overtakes from the left and heads in a different direction at the intersection.”

图片摘要：该图主要展示 A7: Qualitative results in ReVOS. ReVOS [38] expressions oft。
![](images/7655f5209793aae45077e905c8be4e67a9df857111d300bf956e38f89e7ecb4a.jpg)  
“When your hands are wet from washing, which tool can help soak up the excess water?”

图片摘要：该图主要展示 A7: Qualitative results in ReVOS. ReVOS [38] expressions oft。
![](images/9f2409d3563cece894a27eece4133d795feb4bd8661901497bf966b75ddbd778.jpg)  
“The object that was temporarily in the girl’s left hand grasp.”

图片摘要：该图主要展示 A8: Qualitative results in ReasonVOS. ReasonVOS [3] requires。
![](images/de36dbad09268cc0225a490a257ddae427884b13ec4eca4b2d2aa33f68061399.jpg)  
"In case of a flat tire, which vehicle would have a spare tire on board?"   
Fig. A8: Qualitative results in ReasonVOS. ReasonVOS [3] requires commonsense and world knowledge beyond direct visual cues. AgentRVOS handles expressions involving functional reasoning, hypothetical scenarios, and temporal event understanding.

# Candidate Mask Track Generation – Referring

You are a linguistic specialist for Referring Video Object Segmentation (RVOS).

Your Primary Objective:

Analyze the user's expression and determine if the **Target Object Class** can be identified explicitly from the text alone.

# ### Classification Logic:

# 1. EXPLICIT (Specific Class Known)

* The identified target is a **specific physical noun** (e.g., "dog", "car", "plate", "man").   
* Even with typos ("yhe") or broken grammar ("bear fight"), if the specific class is clear, output EXPLICIT.

# 2. REASONING (Visual Context Required)

* **Questions / Interrogatives:** The expression is a question asking about the identity of the target.   
* **Generic Placeholders:** The target is identified grammatically, but the noun itself is too vague to determine the class without video.   
* *Logic:* In "The **object** that is scared by the monkey", the target is "**object**". Since "object" is generic, you must look at the video to know what it is. $- >$ Output **REASONING**.

* *Keywords:* "object", "thing", "item", "stuff", "entity", "one".   
* **Non-Physical / Intangible:** The identified target is an **abstract concept, phenomenon, or intangible entity**, NOT a physical object class.   
* *Keywords:* "sound", "voice", "speed", "shadow", "reflection", "air", "time", "moment".   
* **Ambiguous:** The target is a pronoun (it, they) or interrogative (what, who).

### Output Format (JSON Only):

```txt
{ "expression_type": "EXPLICIT" or "REASONING", "nouns": ["base_noun", "hypernym"] or null, "reasoning": "Brief explanation. Format: 'Target is [Noun] ([Reason])'.} 
```

* base_noun: Singular form (e.g., "monkeys" -> "monkey").   
* SAM-Optimized Hypernym Mapping (CRITICAL)

Map the extracted noun to a Common Visual Superclass optimized for AI segmentation models (like SAM).

# Rule A: Rare Species $\vartriangleleft$ Visual Proxy (Shape Match)

* If the noun is a rare species or specific type, map it to the **most common visual equivalent** that shares the same shape.

* Examples: "Yak" -> "**Cow**", "Baboon" -> "**Monkey**".

# Rule B: Common Objects $\vartriangleleft$ Broad Category

* If the noun is a common object, map it to its standard superclass.   
* Examples: "Car" -> "**Vehicle**", "Truck" -> "**Vehicle**".

* Identity Rule: If the base noun is already a top-level generic category, set to `null`.   
* Reasoning: concise justification focusing ONLY on the identified target and its specificity. Do NOT list ignored context words.

Fig. A9: Prompts used in AgentRVOS $( \mathtt { p r o m p t } _ { r e f e r r i n g } )$ . The prompt for concept extraction, where the model receives a referring expression and extracts a core concept and a broader concept to guide SAM3 mask track generation.

# Candidate Mask Track Generation – Reasoning

You are a Video Reasoning Expert for Referring Video Object Segmentation (RVOS).

Your task is to identify the specific Physical Object(s) corresponding to the provided text expression by analyzing the video frames.

### Input Parameters:

1. Expression Type: 'EXPLICIT' (Text names the object) or 'REASONING' (Text is ambiguous/question).   
2. Iteration: Current attempt number (1, 2, ...).   
3. Failed Nouns: List of nouns that failed in previous attempts. **DO NOT output these again.**

### Workflow by Expression Type:

#### CASE A: Expression Type $= =$ 'REASONING' (Ambiguous / Questions)

* **Goal:** Visually infer the missing target.

Step 1: Analyze Ambiguity Type

Identify why the text was insufficient and what to look for in the video:

* **Pronouns ("It", "Ones"):** Find the specific object the pronoun refers to.   
* **Interrogatives ("Who", "What"):** Visually answer the question.   
* **Abstract/Intangible ("Pressure", "Force", "Wind"):** Find the **Visible Source/Agent** causing the effect.   
* *Example:* "Invisible pressure making the dog move" $- >$ Look for *what* scares the dog (e.g., a vacuum cleaner).   
* **Missing Subject ("Moving fast"):** Find the actor performing the action.

# Step 2: Visual Inference & Extraction (Best Effort)

* **Visible:** If the target object is clearly visible in the frames, extract its **Singular Base Noun** directly.   
* *Rule:* Convert plural to singular (e.g., "cars" -> "**car**", "children" -> "**child**").   
* **Not Visible / Ambiguous:** If the exact target is not visible or clear, **infer the most plausible visible object** based on the visual context.   
* *Strategy:* Identify the object being looked at, the surface receiving an action, or the visible proxy causing the effect. Just make the best logical guess from what is shown and output the **Singular Form**.

# #### CASE B: Expression Type $= =$ 'EXPLICIT' (Specific Naming)

* **Goal:** Translate the specific name into a **SAM-Friendly Visual Descriptor**.   
* **Logic:**

1. **Avoid Specifics:** SAM models struggle with proper nouns (e.g., "Mario", "Pororo") or highly specific sub-types.   
2. **Visual Translation:** Convert the specific name into a description of its **visual appearance** or **material**.   
3. **Generalization:** If `iteration` $>$ 1, broaden the category significantly.

### Output Format (JSON Only):

```json
{
    "nouns": ["base_noun", "hypernym)];
    "reasoning_logic": "Brief text explaining the visual inference (e.g., 'Text says 'pressure', video shows a vacuum cleaner scaring the dog, so the target is the vacuum cleaner.)"
} 
```

Fig. A10: Prompts used in AgentRVOS $( \mathtt { p r o m p t } _ { r e a s o n i n g } )$ ). The prompt for concept extraction, where the model receives the referring expression and extracts a core concept and a broader concept to guide SAM3 mask track generation.

# Appearance Tool Verification

You are an intelligent assistant analyzing referring expressions for video object segmentation.

Your task is to determine whether the given referring expression requires color or appearance information to identify the target object.

referring expression: {expression_string}

Analyze whether identifying this object requires color-related or appearance-related information. This includes:

- Direct color mentions (e.g., "red car", "blue shirt", "white dog")   
- Texture or pattern descriptions (e.g., "striped", "polka-dotted")   
- Material appearances that imply color (e.g., "golden", "silver", "wooden")   
- Relative color comparisons (e.g., "darker one", "lighter colored")   
- Any visual appearance that could be obscured by a mask overlay

Return True if color/appearance information is needed, False otherwise.

Return the result in the following format enclosed within <answer> tags:

<answer>

True or False

</answer>

# Appearance Tool

You are an intelligent assistant extracting color and appearance information from an image.

The image shows an object in two views:

- Left: The object is highlighted with a red bounding box in context (with surrounding area visible)   
- Right: A tightly cropped view of the object for detailed observation

Object class: {class_name}

Your task is to extract concise color-related appearance information for this object.

Focus on extracting:

- Primary color(s) of the object   
- Notable color patterns if visible   
- Any distinctive color features

Keep the description concise (1-2 short phrases). Do NOT describe shape, size, position, or actions.

Only describe color and visual appearance.

Return the result in the following format enclosed within <answer> tags:

<answer>

[concise color/appearance description]

</answer>

Fig. A11: Prompts used in AgentRVOS (promptappearance_requirement and promptappearance_retrieval). The prompt for Appearance Tool Verification (top) determines whether the referring expression requires appearance-level evidence, and the prompt for Appearance Tool (bottom) extracts concise color and appearance descriptions from each candidate.

# Iterative Spatio-temporal Pruning

You are an intelligent assistant for generalized referring expression segmentation and reasoning segmentation.

User has provided a referring expression and uniformly sampled frames from video.

The frames are visually prompted with object masks and object IDs.

Your task is to partition object IDs into true, false, and unknown object IDs according to referring expression.

referring expression: {expression_string}

object IDs: {unknown_obj_ids}

Please analyze the visually prompted frames and partition the object IDs into:

1. true_obj_ids: The object IDs that definitely DO match the referring expression with high confidence.   
2. false_obj_ids: The object IDs that definitely DO NOT match the referring expression with high confidence.   
3. unknown_obj_ids: The object IDs for which it cannot be clearly determined whether they match the referring expression.

IMPORTANT: Your response MUST include ALL object IDs from the input list: {unknown_obj_ids}

Each ID must appear in exactly ONE of the three lists. Missing any ID is an error.

Return the result in the following JSON format enclosed within <answer> tags:

```txt
<answer>   
{ "true_obj_ids": [list of true object IDs], "false_obj_ids": [list of false object IDs], "unknown_obj_ids": [list of unknown object IDs]   
}   
</answer> 
```

Fig. A12: Prompts used in AgentRVOS $( \mathtt { p r o m p t } _ { s e l e c t } )$ $s e l e c t$ ). The prompt for Iterative Spatio-temporal Pruning, where the model receives a candidate mask track and a language query and classifies each candidate as Accept, Reject, or Uncertain, progressively narrowing the candidate pool.

# References

1. Bai, S., Cai, Y., Chen, R., Chen, K., Chen, X., Cheng, Z., Deng, L., Ding, W., Gao, C., Ge, C., et al.: Qwen3-vl technical report. arXiv preprint arXiv:2511.21631 (2025) 1, 3, 4, 6, 9, 22   
2. Bai, S., Chen, K., Liu, X., Wang, J., Ge, W., Song, S., Dang, K., Wang, P., Wang, S., Tang, J., Zhong, H., Zhu, Y., Yang, M., Li, Z., Wan, J., Wang, P., Ding, W., Fu, Z., Xu, Y., Ye, J., Zhang, X., Xie, T., Cheng, Z., Zhang, H., Yang, Z., Xu, H., Lin, J.: Qwen2.5-vl technical report (2025), https://arxiv.org/abs/2502.13923 4   
3. Bai, Z., He, T., Mei, H., Wang, P., Gao, Z., Chen, J., Liu, L., Zhang, Z., Shou, M.Z.: One token to seg them all: Language instructed reasoning segmentation in videos. Advances in Neural Information Processing Systems 37, 6833–6859 (2024) 2, 4, 8, 9, 22, 28   
4. Carion, N., Gustafson, L., Hu, Y.T., Debnath, S., Hu, R., Suris, D., Ryali, C., Alwala, K.V., Khedr, H., Huang, A., et al.: Sam 3: Segment anything with concepts. arXiv preprint arXiv:2511.16719 (2025) 1, 2, 3, 6, 7, 9, 15, 17   
5. Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., Zagoruyko, S.: Endto-end object detection with transformers. In: European conference on computer vision. pp. 213–229. Springer (2020) 4   
6. Chen, Z., Wang, W., Cao, Y., Liu, Y., Gao, Z., Cui, E., Zhu, J., Ye, S., Tian, H., Liu, Z., et al.: Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. arXiv preprint arXiv:2412.05271 (2024) 4   
7. Ding, H., Liu, C., He, S., Jiang, X., Loy, C.C.: Mevis: A large-scale benchmark for video segmentation with motion expressions. In: Proceedings of the IEEE/CVF international conference on computer vision. pp. 2694–2703 (2023) 2, 4, 8, 9, 22, 25   
8. Gavrilyuk, K., Ghodrati, A., Li, Z., Snoek, C.G.: Actor and action video segmentation from a sentence. In: Proceedings of the IEEE conference on computer vision and pattern recognition. pp. 5958–5966 (2018) 4   
9. Gong, S., Zhuge, Y., Zhang, L., Yang, Z., Zhang, P., Lu, H.: The devil is in temporal token: High quality video reasoning segmentation. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 29183– 29192 (2025) 9   
10. He, S., Ding, H.: Decoupling static and hierarchical motion perception for referring video segmentation (2024), https://arxiv.org/abs/2404.03645 4   
11. Huang, S., Ling, R., Li, H., Hui, T., Tang, Z., Wei, X., Han, J., Liu, S.: Unleashing the temporal-spatial reasoning capacity of gpt for training-free audio and language referenced video object segmentation. In: Proceedings of the AAAI Conference on Artificial Intelligence. vol. 39, pp. 3715–3723 (2025) 2, 9, 10   
12. Hurst, A., Lerer, A., Goucher, A.P., Perelman, A., Ramesh, A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A., Radford, A., et al.: Gpt-4o system card. arXiv preprint arXiv:2410.21276 (2024) 2, 10   
13. Jiang, H., Liang, T., Zheng, W.S., Hu, J.F.: Refer-agent: A collaborative multiagent system with reasoning and reflection for referring video object segmentation. arXiv preprint arXiv:2602.03595 (2026) 2, 5   
14. Jin, W., Kim, S., Lee, J., Kim, S.: Interrvos: Interaction-aware referring video object segmentation. arXiv preprint arXiv:2506.02356 (2025) 2

15. hong Kao, S., Huang, C.H., Liu, H., Tai, Y.W., Tang, C.K.: Cot-seg: Rethinking segmentation with chain-of-thought reasoning and self-correction (2026), https: //arxiv.org/abs/2601.17420 2   
16. Kao, S.h., Tai, Y.W., Tang, C.K.: Cot-rvs: Zero-shot chain-of-thought reasoning segmentation for videos. arXiv preprint arXiv:2505.18561 (2025) 2, 5, 9, 10, 12   
17. Khoreva, A., Rohrbach, A., Schiele, B.: Video object segmentation with referring expressions. In: Proceedings of the European Conference on Computer Vision (ECCV) Workshops. pp. 0–0 (2018) 4   
18. Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A.C., Lo, W.Y., et al.: Segment anything. In: Proceedings of the IEEE/CVF international conference on computer vision. pp. 4015–4026 (2023)   
19. Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C.H., Gonzalez, J., Zhang, H., Stoica, I.: Efficient memory management for large language model serving with pagedattention. In: Proceedings of the 29th symposium on operating systems principles. pp. 611–626 (2023) 22   
20. Lai, X., Tian, Z., Chen, Y., Li, Y., Yuan, Y., Liu, S., Jia, J.: Lisa: Reasoning segmentation via large language model. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. pp. 9579–9589 (2024) 2   
21. Li, B., Zhang, Y., Guo, D., Zhang, R., Li, F., Zhang, H., Zhang, K., Zhang, P., Li, Y., Liu, Z., et al.: Llava-onevision: Easy visual task transfer. arXiv preprint arXiv:2408.03326 (2024) 2, 3, 4   
22. Li, Y., Yin, Y., Zhu, L., Chen, W., Qian, S., Wang, X., Fu, Y.: Revseg: Incentivizing the reasoning chain for video segmentation with reinforcement learning (2025), https://arxiv.org/abs/2512.02835 4   
23. Lin, L., Yu, X., Pang, Z., Wang, Y.X.: Glus: Global-local reasoning unified into a single large language model for video segmentation. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 8658–8667 (2025) 2, 9   
24. Liu, H., Li, C., Wu, Q., Lee, Y.J.: Visual instruction tuning. Advances in neural information processing systems 36, 34892–34916 (2023) 2   
25. Liu, Y., Peng, B., Zhong, Z., Yue, Z., Lu, F., Yu, B., Jia, J.: Seg-zero: Reasoningchain guided segmentation via cognitive reinforcement (2025), https://arxiv. org/abs/2503.06520 2   
26. Miao, B., Bennamoun, M., Gao, Y., Shah, M., Mian, A.: Temporally consistent referring video object segmentation with hybrid memory. IEEE Transactions on Circuits and Systems for Video Technology (2024) 4   
27. OpenAI: Introducing gpt-5 (Aug 2025), august 7 2025 1, 3, 6, 9   
28. Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., et al.: Learning transferable visual models from natural language supervision. In: International conference on machine learning. pp. 8748–8763. PmLR (2021) 5   
29. Ravi, N., Gabeur, V., Hu, Y.T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rädle, R., Rolland, C., Gustafson, L., et al.: Sam 2: Segment anything in images and videos. In: The Thirteenth International Conference on Learning Representations (2024) 2, 4   
30. Seo, S., Lee, J.Y., Han, B.: Urvos: Unified referring video object segmentation network with a large-scale benchmark. In: European conference on computer vision. pp. 208–223. Springer (2020) 4   
31. Team, G., Anil, R., Borgeaud, S., Alayrac, J.B., Yu, J., Soricut, R., Schalkwyk, J., Dai, A.M., Hauth, A., Millican, K., et al.: Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805 (2023) 2, 22

32. Varma, M., Delbrouck, J.B., Hooper, S., Chaudhari, A., Langlotz, C.: Villa: Finegrained vision-language representation learning from real-world data. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 22225– 22235 (2023) 9   
33. Wang, H., Chen, Q., Yan, C., Cai, J., Jiang, X., Hu, Y., Xie, W., Gavves, S.: Object-centric video question answering with visual grounding and referring. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 22274–22284 (2025) 9   
34. Wei, C., Zhong, Y., Tan, H., Liu, Y., Zhao, Z., Hu, J., Yang, Y.: Hyperseg: Towards universal visual segmentation with large language model. arXiv preprint arXiv:2411.17606 (2024) 9   
35. Wei, C., Zhong, Y., Tan, H., Zeng, Y., Liu, Y., Wang, H., Yang, Y.: Instructseg: Unifying instructed visual segmentation with multi-modal large language models. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 20193–20203 (2025) 9   
36. Wu, J., Jiang, Y., Sun, P., Yuan, Z., Luo, P.: Language as queries for referring video object segmentation. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 4974–4984 (2022) 4   
37. Xu, Z., Guo, Y., Lu, Y., Yang, F., Li, J., Cai, L.: Videoseg-r1: reasoning video object segmentation via reinforcement learning. In: Proceedings of the AAAI Conference on Artificial Intelligence. pp. 11496–11504. No. 14 (2026) 4, 9   
38. Yan, C., Wang, H., Yan, S., Jiang, X., Hu, Y., Kang, G., Xie, W., Gavves, E.: Visa: Reasoning video object segmentation via large language models. In: European Conference on Computer Vision. pp. 98–115. Springer (2024) 2, 4, 8, 9, 22, 27   
39. Yang, J., Zhang, H., Li, F., Zou, X., Li, C., Gao, J.: Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v. arXiv preprint arXiv:2310.11441 (2023) 7, 17   
40. Yuan, H., Li, X., Zhang, T., Sun, Y., Huang, Z., Xu, S., Ji, S., Tong, Y., Qi, L., Feng, J., et al.: Sa2va: Marrying sam2 with llava for dense grounded understanding of images and videos. arXiv preprint arXiv:2501.04001 (2025) 2, 4, 9
