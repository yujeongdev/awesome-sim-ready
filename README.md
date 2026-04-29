<div align="center">

# 🌉 Awesome Real2Sim Robotics

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Status](https://img.shields.io/badge/status-curated%20MVP-blue)
![Focus](https://img.shields.io/badge/focus-real2sim%20robotics-8A2BE2)
![License](https://img.shields.io/badge/license-CC--BY--4.0-green)

**Curated papers, projects, datasets, and engineering recipes for building simulator-executable assets, environments, and digital twins from real-world data.**

</div>

---

## 🔗 Sibling Project

- [Awesome Sim2Real Learning](https://github.com/yujeongdev/awesome-sim2real-learning) — policy-level transfer: RL/IL, domain randomization, curricula, policy evaluation, and deployment case studies.

## 🚩 News & Updates

- **2026-04** — Renamed from `awesome-sim-ready` and folded in the environment/digital-twin track from `awesome-sim2real-environments`.
- **2026-04** — Initial MVP structure: definition, reading path, resource taxonomy, and validation checklist.

## 📋 Contents

| | Section | What it answers |
| --- | --- | --- |
| 🎯 | [Aim of the Project](#aim) | Why Real2Sim is more than pretty reconstruction |
| 🧠 | [What is Real2Sim?](#definition) | How real observations become simulator-executable state |
| 🏷️ | [Legend](#legend) | How to read availability and capability tags |
| 🎚️ | [Selection Criteria](#selection-criteria) | What belongs here and what does not |
| 🔥 | [Must Read First](#must-read) | A practical reading order |
| 🧰 | [End-to-End Sim-Ready Asset Generation](#end-to-end) | Image/text/mesh → simulator-facing asset |
| 🦾 | [Articulated Object Generation and Reconstruction](#articulation) | Parts, joints, axes, limits, kinematic graphs |
| 🧪 | [Physics, Materials, and Dynamics Grounding](#physics) | Scale, materials, stability, dynamics, simulation feedback |
| 🌍 | [Environment Construction and Digital Twins](#environment-construction) | Real scenes/tasks → simulator-executable environments |
| 🎚️ | [Calibration, Domain Gap, and Validation](#calibration-validation) | How sim-real mismatch is measured and reduced |
| 👁️ | [Sensor Simulation and Synthetic Data](#sensor-simulation) | Cameras, tactile sensors, and observation pipelines |
| 📦 | [Datasets and Benchmarks](#datasets) | Where supervision and assets come from |
| ✅ | [Evaluating Real2Sim Outputs](#evaluation) | How to know whether output is actually useful |

<a id="aim"></a>

## 🎯 Aim of the Project

Real2Sim is the engineering problem of turning real-world evidence into simulation that robots can use.

This repo curates work around **simulator-executable representations**: objects, articulated assets, physical parameters, sensor models, task environments, digital twins, and validation methods that help close the loop from real data to simulation and back to real robots.

The goal is to be useful to engineers who own real pipelines: Isaac Sim / Isaac Lab, MuJoCo, SAPIEN, PyBullet, Genesis, Gazebo, Omniverse, synthetic data systems, digital twins, and real2sim2real workflows.

<a id="definition"></a>

## 🧠 What is Real2Sim?

In this repo, **Real2Sim** means constructing simulator-executable assets, scenes, environments, or digital twins from real-world observations, interactions, demonstrations, or task requirements.

```text
real2sim output
≈ geometry + articulation + physical properties + simulator format
  + scene/task/sensor context + validation evidence
```

Useful Real2Sim output can be small or large:

- **Object / asset Real2Sim** — image/video/scan/mesh → URDF/MJCF/USD, collision geometry, joints, materials, physics metadata.
- **Scene / environment Real2Sim** — real capture/task requirement → robot-scene-object-sensor simulation environment.
- **Digital twin Real2Sim** — synchronized or calibrated simulation that can replay, evaluate, or stress-test real robot behavior.
- **Real2Sim2Real loop** — real data → sim construction → synthetic rollouts / policy evaluation → real deployment → failure logs → sim update.

Importable is not the same as valid. A digital asset or scene that loads but explodes under gravity, lacks calibrated sensors, or fails to reproduce task behavior is only **format-ready**, not **simulation-valid**.

<a id="legend"></a>

## 🏷️ Legend

Availability:

- 🧪 paper-only
- 🌐 project page / demo
- 🛠️ code available
- 📦 data / checkpoints / assets
- 🤖 simulator-validated or simulator-facing evidence
- 🧾 license/provenance worth checking before company use
- ⭐ representative / must-read

Capability tags:

- `[G]` geometry
- `[A]` articulation
- `[P]` physical properties / contact / dynamics
- `[F]` simulator format
- `[E]` environment / scene
- `[R]` robot, actuator, embodiment model
- `[O]` object / asset / material model
- `[S]` sensor simulation
- `[DR]` domain randomization / adaptation
- `[ID]` system identification / calibration
- `[RT]` Real2Sim / digital twin
- `[L]` learning environment / RL / IL support
- `[V]` validation

Why bracket tags instead of emojis here? Availability is human-facing, so emojis work well. Capability tags are stable, grep-friendly, table-friendly, and easy to migrate into `resources.yml` later.

<a id="selection-criteria"></a>

## 🎚️ Selection Criteria

A strong entry should help construct or validate simulator-executable state from real data. It should contribute to at least one of:

- explicit geometry, part-level output, or collision representation;
- articulation / kinematic structure;
- physical/material/sensor grounding;
- simulator-facing formats such as URDF, MJCF, SDF, USD, or simulator-native assets;
- real2sim or digital twin construction;
- scene, robot, actuator, sensor, or contact calibration;
- domain randomization or sim-real gap reduction at the environment level;
- real-world validation, failure replay, or hardware-in-the-loop testing.

Usually out of scope:

- pure visual 3D reconstruction with no simulator-facing interaction;
- pure policy-transfer papers better placed in `awesome-sim2real-learning`;
- simulator demos with no task interface, real-world evidence, or reproducibility path.

<a id="must-read"></a>

## 🔥 Must Read First

1. **[SAPIEN / PartNet-Mobility](#sapien-partnet-mobility)** — understand articulated-object data and simulator substrate.
2. **[URDFormer](#urdformer)** — early real-image → URDF digital twin pipeline.
3. **[Real2Code](#real2code)** — articulation as executable code generation.
4. **[PhysX-Anything](#physx-anything)** — single-image simulation-ready physical asset pipeline.
5. **[Re³Sim / RoboGSim / RoboSimGS](#environment-construction)** — real-scene-to-simulation environments.
6. **[Scalable Real2Sim / Sim2Real²](#environment-construction)** — physics-aware asset and articulated-object real2sim.
7. **[ComSim / ReaDy-Go](#environment-construction)** — 2026 environment-construction directions.
8. **[TACTO / GelSight / FOTS](#sensor-simulation)** — sensor simulation as its own real2sim problem.

See also: [docs/reading-path.md](docs/reading-path.md) and [docs/environment-construction-methods.md](docs/environment-construction-methods.md).

<a id="end-to-end"></a>

## 🧰 End-to-End Sim-Ready Asset Generation

<a id="physx-anything"></a>

- ⭐ **[2025] PhysX-Anything — Simulation-Ready Physical 3D Assets from Single Image** `[G][A][P][F]` 🌐🛠️📦🤖
  Single image → part-aware physical asset with simulator-facing outputs.
  Links: [paper](https://arxiv.org/abs/2511.13648) · [code](https://github.com/ziangcao0312/PhysX-Anything)
  *Why engineers care:* anchor project for image-to-sim-ready asset generation; good case study for VLM reasoning + coarse geometry + decoder + URDF/XML lowering.
  *Caveat:* still needs per-asset physics QA; generated physical parameters should not be trusted blindly.

<a id="simart"></a>

- ⭐ **[2026] SIMART — Decomposing Monolithic Meshes into Sim-ready Articulated Assets via MLLM** `[G][A][F]` 🌐
  Static/generated monolithic mesh → segmented articulated asset with URDF-style metadata.
  Links: [project](https://simart-mllm.github.io/)
  *Why engineers care:* targets the practical bottleneck where many generated 3D meshes are visually good but mechanically dead.

- **[2025] EmbodiedGen — Towards a Generative 3D World Engine for Embodied Intelligence** `[G][F]` 🌐🛠️📦
  Broader embodied generation toolkit with image-to-3D/text-to-3D and simulator-ready asset framing.
  Links: [code](https://github.com/HorizonRobotics/EmbodiedGen) · [project](https://horizonrobotics.github.io/EmbodiedGen/)
  *Why engineers care:* useful reference for packaging generated assets across multiple simulators.

<a id="articulation"></a>

## 🦾 Articulated Object Generation and Reconstruction

<a id="articulate-anything"></a>

- ⭐ **[2025] Articulate-Anything — Automatic Generation of 3D Interactable Assets** `[G][A][F][V]` 🌐🛠️
  Text/image/video/PartNet asset → Python programs that compile to URDF.
  Links: [project](https://articulate-anything.github.io/) · [code](https://github.com/vlongle/articulate-anything)
  *Why engineers care:* frames asset generation as an agentic loop with code generation, compilation, and self-correction.

<a id="real2code"></a>

- ⭐ **[2025] Real2Code — Reconstruct Articulated Objects via Code Generation** `[G][A][F]` 🌐
  Visual observations → executable code descriptions for articulated objects.
  Links: [project](https://real2code.github.io/)
  *Why engineers care:* shows how LLM/code representations can carry articulation structure better than raw continuous predictions alone.

<a id="urdformer"></a>

- **[2023/2024] URDFormer — Constructing Articulated Simulation Environments from Real-World Images** `[G][A][F]` 🌐🛠️
  Real-world image → interactive digital twin in URDF.
  Links: [code](https://github.com/WEIRDLabUW/urdformer) · [project](https://urdformer.github.io/)
  *Why engineers care:* strong baseline for image-to-URDF pipelines and kitchen/cabinet-style articulated assets.

- **[2025] SINGAPO — Single Image Controlled Generation of Articulated Parts in Object** `[G][A]` 🌐
  Single image → articulated object with part-level geometry and kinematic structure.
  Links: [project](https://3dlg-hcvc.github.io/singapo/)
  *Why engineers care:* good contrast to URDF-first methods; emphasizes part graph generation.

- **[2025] DIPO — Dual-State Images Controlled Articulated Object Generation Powered by Diverse Data** `[G][A][F]` 🌐🛠️📦
  Dual-state image pair → articulated 3D object with part layouts and joint parameters; introduces PM-X with URDF annotations.
  Links: [project](https://rq-wu.github.io/projects/DIPO/) · [paper](https://arxiv.org/abs/2505.20460)
  *Why engineers care:* dual-state conditioning reduces articulation ambiguity compared with single-image-only pipelines.

- **[2025] ArtFormer — Controllable Generation of Diverse 3D Articulated Objects** `[G][A]` 🛠️
  Controllable articulated object generation with part-aware geometry representations.
  Links: [paper](https://openaccess.thecvf.com/content/CVPR2025/html/Su_ArtFormer_Controllable_Generation_of_Diverse_3D_Articulated_Objects_CVPR_2025_paper.html) · [code](https://github.com/ShuYuMo2003/ArtFormer)
  *Why engineers care:* useful reference for controllable part-level generation before simulator lowering.

- **[2025] DreamArt — Generating Interactable Articulated Objects from a Single Image** `[G][A][V]` 🧪
  Single image → high-fidelity interactable articulated object.
  Links: [paper](https://arxiv.org/abs/2507.05763)
  *Why engineers care:* combines single-view object generation with articulation priors and motion optimization.

- **[2026] AniGen — Unified S3 Fields for Animatable 3D Asset Generation** `[G][A][F]` 🌐🧪
  Single image → animatable 3D asset with co-generated geometry, skeleton, and skinning weights across animals, humanoids, and machinery.
  Links: [project](https://yihua7.github.io/AniGen_web/) · [paper](https://yihua7.github.io/AniGen_web/assets/pdf/AniGen.pdf)
  *Why engineers care:* unusually relevant for simulator-facing articulated assets because it predicts not just part structure but full animation scaffolding, which is a useful precursor to articulation-aware USD/URDF pipelines and embodied-agent-ready asset creation.
  *Caveat:* animation-ready rigging is not automatically simulator-valid articulation; joint semantics, limits, collision geometry, and dynamics metadata still need downstream Real2Sim lowering and QA.

- **[2026] PAct — Part-Decomposed Single-View Articulated Object Generation** `[G][A]` 🧪
  Single image → part-decomposed articulated 3D asset.
  Links: [paper](https://arxiv.org/abs/2602.14965)
  *Why engineers care:* feed-forward direction for faster controllable part assembly.

- **[2025] Particulate — Feed-Forward 3D Object Articulation** `[G][A]` 🧪
  Static mesh → parts, kinematic structure, and motion constraints.
  Links: [paper](https://arxiv.org/abs/2512.11798)
  *Why engineers care:* directly addresses static mesh → articulated asset conversion.

- **[2025] Articulate AnyMesh — Open-vocabulary 3D Articulated Objects Modeling** `[G][A][F][V]` 🌐
  Rigid 3D mesh → articulated object; includes real-to-sim-to-real examples.
  Links: [project](https://articulate-anymesh.github.io/)
  *Why engineers care:* useful for turning Objaverse/generated/reconstructed meshes into interactive objects.

<a id="physics"></a>

## 🧪 Physics, Materials, and Dynamics Grounding

<a id="physx-3d"></a>

- ⭐ **[2025] PhysX-3D — Physical-Grounded 3D Asset Generation** `[G][A][P][F]` 🌐
  3D asset generation and annotation with physical grounding: scale, material, affordance, kinematics, function.
  Links: [project](https://physx-3d.github.io/)
  *Why engineers care:* shifts asset generation from appearance toward physically meaningful metadata.

- ⭐ **[2025] Scalable Real2Sim — Physics-Aware Asset Generation via Robotic Pick-and-Place Setups** `[G][P][F][V]` 🌐🛠️📦🤖
  Robotic interaction pipeline → visual geometry, collision geometry, inertial parameters, and simulatable object descriptions for real-world objects.
  Links: [project](https://scalable-real2sim.github.io/) · [paper](https://arxiv.org/abs/2503.00370) · [code](https://github.com/nepfaff/scalable-real2sim) · [data](https://huggingface.co/datasets/nepfaff/scalable-real2sim)
  *Why engineers care:* demonstrates a scalable real-world data-collection loop for turning physical objects into simulation-ready assets with measured dynamics.

- **[2026] Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions** `[G][P][V]` 🌐🛠️📦🤖
  Real-world videos → Gaussian Splatting visual simulation and soft-body digital twins for closed-loop policy evaluation.
  Links: [project](https://real2sim-eval.github.io/) · [paper](https://arxiv.org/abs/2511.04665) · [code](https://github.com/kywind/real2sim-eval) · [data](https://huggingface.co/collections/shashuo0104/real-to-sim-policy-eval)
  *Why engineers care:* adds a validation-oriented Real2Sim example where reconstructed simulation correlates with real policy rollouts, especially for deformable interactions.

<a id="sophy"></a>

- **[2026] SOPHY — Generating Simulation-Ready Objects with Physical Materials** `[G][P]` 🧪
  Text/image-conditioned object generation with physical material properties.
  Links: [paper](https://openaccess.thecvf.com/content/WACV2026/html/Cao_SOPHY_Generating_Simulation-Ready_Objects_with_Physical_Materials_WACV_2026_paper.html)
  *Why engineers care:* material parameters are often invisible in images but crucial for contact-rich simulation.

<a id="physdreamer"></a>

- **[2024] PhysDreamer — Physics-Based Interaction with 3D Objects via Video Generation Priors** `[P][V]` 🌐
  Static 3D object → plausible dynamics under interaction using video priors.
  Links: [project](https://physdreamer.github.io/)
  *Why engineers care:* points toward dynamics-aware assets instead of static shape-only outputs.

- **[2024] PhyCAGE — Physically Plausible Compositional 3D Asset Generation** `[G][P][V]` 🌐
  Single image/compositional setup → physically plausible 3D Gaussian assets.
  Links: [project](https://wolfball.github.io/phycage/)
  *Why engineers care:* simulation-enhanced optimization can enforce physical plausibility during generation.

<a id="dso"></a>

- **[2025] DSO — Aligning 3D Generators with Simulation Feedback for Physical Soundness** `[G][P][V]` 🌐🛠️📦
  Aligns 3D generators so outputs are more stable/self-supporting under simulation feedback.
  Links: [code](https://github.com/RuiningLi/dso) · [project](https://ruiningli.com/dso/)
  *Why engineers care:* shows a path from “generate then hope” to simulator-in-the-loop alignment.

<a id="datasets"></a>

## 📦 Datasets and Benchmarks

<a id="sapien-partnet-mobility"></a>

- ⭐ **SAPIEN / PartNet-Mobility** `[G][A][F]` 🌐📦🤖
  Articulated objects, part hierarchy, and mobility annotations in a simulator ecosystem.
  Links: [project](https://www.fbxiang.com/portfolio/sapien.html) · [SAPIEN](https://sapien.ucsd.edu/)
  *Why engineers care:* common substrate for learning/evaluating articulated object perception and manipulation.

- **AKB-48 — Articulated Object Knowledge Base** `[G][A]` 🧪📦
  Real-world articulated object knowledge base.
  Links: [paper](https://arxiv.org/abs/2202.08432)
  *Why engineers care:* complements synthetic mobility datasets with real-world articulated categories.

- **GAPartNet — Generalizable and Actionable Parts** `[G][A][V]` 🧪📦
  Cross-category part semantics and actionable part annotations.
  Links: [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Geng_GAPartNet_Cross-Category_Domain-Generalizable_Object_Perception_and_Manipulation_via_Generalizable_and_CVPR_2023_paper.pdf)
  *Why engineers care:* bridges part perception and manipulation affordances.

- **Objaverse / Objaverse-XL** `[G]` 🌐📦🧾
  Large-scale raw 3D object corpora.
  Links: [Objaverse](https://objaverse.allenai.org/) · [Objaverse-XL](https://stability.ai/research/objaverse-xl-a-colossal-universe-of-3d-objects)
  *Why engineers care:* huge raw mesh source for mesh-to-sim-ready pipelines; licensing/provenance requires care.

- **Infinite Mobility — Scalable High-Fidelity Synthesis of Articulated Objects** `[G][A][F]` 🌐📦
  Procedural generation of large articulated object collections.
  Links: [project](https://infinite-mobility.github.io/)
  *Why engineers care:* data scaling path when handcrafted articulated assets are the bottleneck.

<a id="environment-construction"></a>

## 🌍 Environment Construction and Digital Twins

See [docs/environment-construction-methods.md](docs/environment-construction-methods.md) for the deeper landscape.

- ⭐ **[2025] Re³Sim — Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation** `[E][S][RT][L][V]` 🌐📦🤖
  Real scene capture → 3DGS + Isaac Sim/PhysX reconstruction → simulated expert demonstrations → zero-shot real manipulation transfer.
  Links: [project](https://xshenhan.github.io/Re3Sim/) · [paper](https://arxiv.org/abs/2502.08645) · [data](https://huggingface.co/datasets/RE3SIM/sim-resources)
  *Why engineers care:* directly targets the “build a useful sim environment from a real tabletop” problem, not just a new simulator backend.
  *Caveat:* visual similarity is not a full physics guarantee; scene/object alignment still matters.

- ⭐ **[2024] RoboGSim — Real2Sim2Real Robotic Gaussian Splatting Simulator** `[E][S][P][RT][L][V]` 🌐🤖
  Real captures → Gaussian reconstruction + digital twin builder + scene composer + interactive engine.
  Links: [project](https://robogsim.github.io/) · [paper](https://arxiv.org/abs/2411.11839)
  *Why engineers care:* strong reference for an end-to-end environment-making stack with novel views, objects, trajectories, scenes, and policy evaluation.
  *Caveat:* inspect where physics is explicit vs visually reconstructed.

- ⭐ **[2025] RoboSimGS — High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic Manipulation** `[E][S][RT][L][V]` 🌐🤖
  Multi-view real images → scalable photoreal and physically interactive manipulation environments.
  Links: [project](https://robosimgs.github.io/) · [paper](https://arxiv.org/abs/2510.10637)
  *Why engineers care:* representative of the real-scene-to-training-data pipeline for manipulation.
  *Caveat:* separate visual, geometric, and contact validation.

- **[2025] Scalable Real2Sim — Physics-Aware Asset Generation via Robotic Pick-and-Place Setups** `[O][P][ID][RT][V]` 🌐🤖
  Robot interaction + camera → visual geometry, collision geometry, mass and inertial parameters → simulatable object descriptions.
  Links: [project](https://scalable-real2sim.github.io/) · [paper](https://arxiv.org/abs/2503.00370)
  *Why engineers care:* adds physical parameter identification to reconstruction, essential for contact dynamics.
  *Caveat:* object-centric; best treated as a module in larger environment builders.

- **[2026] ReaDy-Go — Real-to-Sim Dynamic 3D Gaussian Splatting Simulation for Environment-Specific Visual Navigation** `[E][S][RT][L][V]` 🌐🤖
  Reconstructs target scenes with 3DGS and injects animatable human GS obstacles to generate dynamic navigation scenarios.
  Links: [project](https://syeon-yoo.github.io/ready-go-site/) · [paper](https://arxiv.org/abs/2602.11575)
  *Why engineers care:* extends real2sim construction from static scenes to dynamic, deployment-specific navigation worlds.
  *Caveat:* navigation-centered; physical contact fidelity is less central than dynamic-obstacle realism.

- **[2026] ComSim — Building Scalable Real-World Robot Data Generation via Compositional Simulation** `[E][O][S][L][V]` 🌐🤖
  Hybrid classical + neural simulation for scalable real-world robot data generation.
  Links: [project](https://faceong.github.io/ComSim/) · [paper](https://arxiv.org/abs/2604.11386)
  *Why engineers care:* combines simulator action consistency with neural realism rather than hand-authoring every environment.
  *Caveat:* verify whether neural translation improves behavior-relevant gaps or mainly appearance.

- **[2026] MATTERIX — Towards a Digital Twin for Robotics-Assisted Chemistry Lab Automation** `[E][S][P][RT][L][V]` 🧪
  Multi-scale GPU-accelerated chemistry-lab digital twin spanning robot manipulation, powder and liquid dynamics, device functionality, heat transfer, and basic reaction kinetics, with hierarchical workflow design and sim-to-real evidence.
  Links: [paper](https://arxiv.org/abs/2601.13232)
  *Why engineers care:* strong domain-specific example of Real2Sim as a usable digital-twin stack rather than just 3D reconstruction; especially relevant when environments must model process dynamics, instruments, and workflow semantics in addition to geometry.
  *Caveat:* chemistry-lab specificity is a strength and a limit; the key question is which semantics/physics layers transfer cleanly to general robot-manipulation environments.

- **[2026] RoboLab — A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies** `[E][R][O][S][L][V]` 🌐🛠️📦🤖🧾
  Scene/task descriptions → Isaac Lab task libraries and runnable robot-agnostic policy-evaluation environments.
  Links: [project](https://research.nvidia.com/labs/srl/projects/robolab/) · [paper](https://arxiv.org/abs/2604.09860) · [code](https://github.com/NVLabs/RoboLab)
  *Why engineers care:* packages scene generation, language-conditioned task generation, environment perturbations, and multi-policy evaluation into a reproducible manipulation benchmark.
  *Caveat:* benchmark/environment-generation substrate rather than real-scene reconstruction; use alongside the sibling sim2real list for policy-transfer interpretation.

<a id="calibration-validation"></a>

## 🎚️ Calibration, Domain Gap, and Validation

- ⭐ **[2019] SimOpt — Closing the Sim-to-Real Loop by Adapting Simulation Randomization** `[P][DR][ID][V]` 🧪🤖
  Adapts simulation parameter distributions using a few real-world rollouts interleaved with policy training.
  Links: [project](https://sites.google.com/view/simopt/home) · [paper](https://arxiv.org/abs/1810.05687)
  *Why engineers care:* turns randomization into a measured feedback loop instead of hand-tuned noise ranges.
  *Caveat:* task-specific real rollouts are still needed.

- **[2020] TuneNet — One-Shot Residual Tuning for System Identification and Sim-to-Real Robot Task Transfer** `[P][ID][V]` 🧪🤖
  Uses iterative residual tuning to adapt simulator/model parameters from limited real-world evidence.
  Links: [PMLR](https://proceedings.mlr.press/v100/allevato20a.html) · [paper](https://arxiv.org/abs/1907.11200)
  *Why engineers care:* representative of learning-based physics tuning when manual system identification is too slow.
  *Caveat:* tuning quality depends on whether chosen parameters can explain the real mismatch.

- ⭐ **[2017] OpenAI Dynamics Randomization — Sim-to-real transfer of robotic control** `[R][P][DR][V]` 🌐🤖
  Randomizes dynamics parameters during simulated policy training to improve transfer to a real robot.
  Links: [project](https://openai.com/index/sim-to-real-transfer-of-robotic-control-with-dynamics-randomization)
  *Why engineers care:* classic baseline for physics randomization as a practical alternative to perfect simulator fidelity.
  *Caveat:* randomization ranges are engineering decisions; overly broad ranges can hide root causes.

<a id="sensor-simulation"></a>

## 👁️ Sensor Simulation and Synthetic Data

- ⭐ **[2020] TACTO — Fast, Flexible, Open-source Simulator for High-Resolution Vision-based Tactile Sensors** `[S][P][V]` 🧪🛠️🤖
  Vision-based tactile sensor simulator with sim2real proof-of-concept.
  Links: [paper](https://arxiv.org/abs/2012.08456) · [code](https://github.com/facebookresearch/tacto)
  *Why engineers care:* tactile sensing has its own sim-real gap; RGB/depth simulation assumptions rarely transfer directly.
  *Caveat:* realism depends on contact, illumination, gel deformation, and sensor-specific calibration.

- **[2021] GelSight Simulation for Sim2Real Learning** `[S][DR][V]` 🌐🤖
  Gazebo-based simulation pipeline for generating GelSight tactile images and studying tactile sim2real transfer.
  Links: [project](https://danfergo.github.io/gelsight-simulation/) · [paper](https://arxiv.org/abs/2101.07169)
  *Why engineers care:* useful example of measuring sensor-domain mismatch and using augmentation to reduce it.
  *Caveat:* sensor morphology and fabrication artifacts matter.

<a id="evaluation"></a>

## ✅ Evaluating Real2Sim Outputs

See [docs/asset-qa-checklist.md](docs/asset-qa-checklist.md) and [docs/environment-qa-checklist.md](docs/environment-qa-checklist.md).

A practical validation ladder:

1. **Visual reconstruction** — looks plausible.
2. **Importable representation** — parses in the claimed simulator.
3. **Interactable representation** — joints, contacts, sensors, and controllers work under scripted actions.
4. **Physically stable representation** — mass/inertia/collision/materials do not explode under gravity/contact.
5. **Task-predictive representation** — simulation predicts real failures, rankings, or success rates.

Quick questions for every Real2Sim output:

- Does it import into the claimed simulator?
- Are mesh paths, scales, origins, and frames correct?
- Do joints and contacts behave without immediate interpenetration?
- Are collision meshes simpler and more stable than visual meshes?
- Is mass/inertia/friction/damping explicit, measured, or guessed?
- Are sensors calibrated or just rendered?
- Does validation compare behavior, or only rendered appearance?
- Is it useful for policy learning, evaluation, replay, or deployment?

## 🤝 Contributing

Contributions are welcome, but the bar is intentionally higher than “related to 3D” or “related to simulation.” See [CONTRIBUTING.md](CONTRIBUTING.md).

A good entry explains:

- what real-world input it consumes,
- what simulator-facing output it produces,
- which Real2Sim dimensions it covers,
- whether code/data/checkpoints are available,
- and what still needs validation.

## 🙏 Thanks

Format inspiration from [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models), [Awesome Embodied VLA / VA / VLN](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln), [Awesome Robotics Libraries](https://github.com/jslee02/awesome-robotics-libraries), and [Best of Robot Simulators](https://github.com/knmcguire/best-of-robot-simulators).

## 📝 Citation

If this list helps your work, cite the repository URL for now:

```bibtex
@misc{awesome_real2sim_robotics,
  title        = {Awesome Real2Sim Robotics},
  howpublished = {\url{https://github.com/yujeongdev/awesome-real2sim}},
  year         = {2026}
}
```

## 📜 License

This curated list and documentation are released under [CC BY 4.0](LICENSE), unless a linked project states otherwise. Linked papers, code, datasets, assets, and checkpoints retain their own licenses.
