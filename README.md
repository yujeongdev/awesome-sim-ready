<div align="center">

# 🧰 Awesome Sim-Ready 3D Asset Generation

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Status](https://img.shields.io/badge/status-curated%20MVP-blue)
![Focus](https://img.shields.io/badge/focus-physical%203D%20assets-8A2BE2)
![License](https://img.shields.io/badge/license-CC--BY--4.0-green)

**Curated papers, projects, datasets, and engineering recipes for generating physics-executable 3D assets.**

</div>

---

## 🚩 News & Updates

- **2026-04** — Initial MVP structure: definition, reading path, resource taxonomy, and validation checklist.

## 📋 Contents

| | Section | What it answers |
|---|---|---|
| 🎯 | [Aim of the Project](#aim) | Why this is not another visual 3D paper dump |
| 🧠 | [What is a Sim-Ready Asset?](#definition) | What must exist beyond a pretty mesh |
| 🏷️ | [Legend](#legend) | How to read availability and capability tags |
| 🎚️ | [Selection Criteria](#selection-criteria) | What belongs here and what does not |
| 🔥 | [Must Read First](#must-read) | A practical reading order |
| 🧰 | [End-to-End Sim-Ready Asset Generation](#end-to-end) | Image/text/mesh → simulator-facing asset |
| 🦾 | [Articulated Object Generation and Reconstruction](#articulation) | Parts, joints, axes, limits, kinematic graphs |
| 🧪 | [Physics, Materials, and Dynamics Grounding](#physics) | Scale, materials, stability, dynamics, simulation feedback |
| 📦 | [Datasets and Benchmarks](#datasets) | Where supervision and assets come from |
| ✅ | [Evaluating Sim-Ready Assets](#evaluation) | How to know whether an asset is actually useful |

<a id="aim"></a>

## 🎯 Aim of the Project

Most 3D generation lists focus on visual quality. Robotics and embodied AI teams need a sharper question:

> Can this asset be imported, articulated, simulated, validated, and reused in a robot-learning pipeline?

This repo curates work around **simulation-ready physical 3D assets**: papers, projects, datasets, and tooling that help convert images, text, videos, point clouds, or static meshes into assets with enough structure to run inside physics simulators.

The goal is to be useful to engineers who own real pipelines: Isaac Sim / Isaac Lab, MuJoCo, SAPIEN, PyBullet, Genesis, Gazebo, Omniverse, synthetic data systems, and real2sim workflows.

<a id="definition"></a>

## 🧠 What is a Sim-Ready Asset?

A visual 3D asset is mostly geometry and appearance:

```text
visual 3D asset ≈ geometry + texture
```

A sim-ready physical asset needs more:

```text
sim-ready asset ≈ geometry + articulation + physical properties + simulator format + validation
```

In this repo we use the following dimensions:

- **[G] Geometry** — mesh, part meshes, Gaussian/implicit geometry, collision geometry.
- **[A] Articulation** — part hierarchy, joint type, joint axis, limits, kinematic graph.
- **[P] Physical properties** — scale, mass, inertia, friction, material, damping, stiffness, stability.
- **[F] Simulator format** — URDF, MJCF/XML, SDF, USD, simulator-specific assets.
- **[V] Validation** — evidence that the asset imports, remains stable, moves correctly, and supports tasks.

Importable is not the same as valid. A URDF that loads but explodes under gravity is only **format-ready**, not **simulation-valid**.

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
- `[P]` physical properties
- `[F]` simulator format
- `[V]` validation

Why bracket tags instead of emojis here? Availability is human-facing, so emojis work well. Capability tags are intended to be stable, grep-friendly, table-friendly, and easy to migrate into `resources.yml` later. They also avoid ambiguity across platforms where emoji rendering/search can be inconsistent.

Ordering policy: representative and runnable work appears first within a section; newer additions can be added chronologically after the core items.

<a id="selection-criteria"></a>

## 🎚️ Selection Criteria

This list prioritizes resources that move 3D assets closer to actual simulator use. A strong entry should cover at least one of:

- explicit geometry or part-level output,
- articulation / kinematic structure,
- physical or material grounding,
- simulator-facing formats,
- validation evidence beyond a rendered demo.

Pure visual 3D generation is usually out of scope unless it is a useful building block for sim-ready asset generation.

Real2Sim work is included only when it produces reusable object-level assets, physical parameters, simulator-facing descriptions, or direct sim-vs-real validation evidence. Scene reconstruction or policy-transfer-only work is out of scope.

<a id="must-read"></a>

## 🔥 Must Read First

1. **[SAPIEN / PartNet-Mobility](#sapien-partnet-mobility)** — understand the articulated-object dataset and simulator substrate.
2. **[URDFormer](#urdformer)** — early real-image → URDF digital twin pipeline.
3. **[Real2Code](#real2code)** — articulation as executable code generation.
4. **[Articulate-Anything](#articulate-anything)** — VLM agent loop for generating articulated URDF assets.
5. **[PhysX-3D](#physx-3d)** — physics-grounded asset properties and annotations.
6. **[PhysX-Anything](#physx-anything)** — single-image simulation-ready physical asset pipeline.
7. **[SIMART](#simart)** — sparse 3D-token MLLM for decomposing monolithic meshes into sim-ready articulated assets.
8. **[DSO](#dso) / [SOPHY](#sophy) / [PhysDreamer](#physdreamer)** — physical plausibility, material, and dynamics directions.

See also: [docs/reading-path.md](docs/reading-path.md).

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

<a id="evaluation"></a>

## ✅ Evaluating Sim-Ready Assets

See [docs/asset-qa-checklist.md](docs/asset-qa-checklist.md).

A practical validation ladder:

1. **Visual asset** — looks plausible.
2. **Importable asset** — parses in the claimed simulator.
3. **Kinematically usable asset** — joints, axes, limits, and frames work.
4. **Physically stable asset** — mass/inertia/collision/materials do not explode under gravity/contact.
5. **Task-useful asset** — planners or policies can interact with it repeatably.

Quick questions for every generated asset:

- Does it import into the claimed simulator?
- Are mesh paths, scales, origins, and frames correct?
- Do joints move without immediate interpenetration?
- Are collision meshes simpler than visual meshes?
- Is mass/inertia/friction/damping explicit or guessed?
- Was stability tested under gravity and contact?
- Is it useful for policy learning, or only a demo render?

## 🤝 Contributing

Contributions are welcome, but the bar is intentionally higher than “related to 3D.” See [CONTRIBUTING.md](CONTRIBUTING.md).

A good entry explains:

- what input it consumes,
- what simulator-facing output it produces,
- which sim-ready dimensions it covers,
- whether code/data/checkpoints are available,
- and what still needs validation.

## 🙏 Thanks

Format inspiration from [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models), [Awesome Embodied VLA / VA / VLN](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln), [Awesome Robotics Libraries](https://github.com/jslee02/awesome-robotics-libraries), and [Best of Robot Simulators](https://github.com/knmcguire/best-of-robot-simulators).

## 📝 Citation

If this list helps your work, cite the repository URL for now:

```bibtex
@misc{awesome_sim_ready_asset_generation,
  title        = {Awesome Sim-Ready 3D Asset Generation},
  howpublished = {\url{https://github.com/techhouse-looper/awesome-sim-ready}},
  year         = {2026}
}
```

## 📜 License

This curated list and documentation are released under [CC BY 4.0](LICENSE), unless a linked project states otherwise. Linked papers, code, datasets, assets, and checkpoints retain their own licenses.
