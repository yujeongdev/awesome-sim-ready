# Environment Construction Method Landscape

This note tracks methods that **construct robot simulation environments**, not
simulators themselves. The emphasis is on pipelines that turn real scenes,
images, videos, language, demonstrations, or robot interactions into usable
simulation worlds, tasks, or synthetic rollouts.

## Why this track matters

Simulator choice answers: “What engine do we run?”

Environment construction answers:

> How do we build, calibrate, populate, and validate the world that the robot
> actually trains or tests in?

For this repository, a strong environment-construction paper should contribute
at least one of:

- real-world scene or object capture into simulator state;
- robot/task-aware scene composition;
- automatic task or environment generation;
- physics/contact/sensor calibration during construction;
- scalable synthetic rollouts from real or generated worlds;
- real robot validation that the generated environment is useful.

## Taxonomy

| Method family | Core input | Output | Main risk |
| --- | --- | --- | --- |
| Real2Sim2Real reconstruction | images/video/scans/logs | photoreal + physical sim environment | visual fidelity mistaken for physics fidelity |
| Physics-aware real2sim | robot interaction/logs | calibrated objects/scenes/parameters | narrow task or object scope |
| Task generation | language/images/LLMs/VLMs | simulator tasks, rewards, demos | generated tasks may be unrealistic or invalid |
| Demonstration-to-synthetic-data | human/robot demos + scans | many synthetic rollouts | bypassed dynamics may miss contact failures |
| Sensor-realistic environments | real sensor data/reconstruction | sensor-matched simulation | observation realism without action realism |
| Validation/debugging tools | real rollouts/failure logs | gap metrics or replay environment | metrics may not predict policy success |

## 2026 snapshot

The 2026 cluster is useful because it shifts the question from “which simulator
should I use?” to “how do I construct the environment instance?” Current themes:

- **Dynamic real2sim worlds**: ReaDy-Go adds moving human obstacles to
  target-environment GS navigation scenes.
- **Intent-driven active real2sim**: VLM-generated behavior trees acquire only
  task-relevant physical parameters.
- **Physics-consistent clutter**: contact graphs and differentiable simulation
  make single-view reconstructed scenes stable under gravity/contact.
- **Compositional simulation**: classical simulators provide action consistency
  while neural simulators reduce visual/domain gaps.
- **Digital twin-guided policy loops**: reconstructed twins guide exploration,
  failure sampling, and human-in-the-loop real rollouts.

## High-priority papers / systems

### Real2Sim2Real reconstruction pipelines

- ⭐ **[2025] Re³Sim — Generating High-Fidelity Simulation Data via
  3D-Photorealistic Real-to-Sim for Robotic Manipulation** `[E][S][RT][L][V]`
  🧰 📦 🧪
  Real scene capture → 3DGS + Isaac Sim/PhysX reconstruction → simulated expert
  demonstrations → zero-shot real manipulation transfer. Links:
  [project](https://xshenhan.github.io/Re3Sim/) ·
  [paper](https://arxiv.org/abs/2502.08645) ·
  [data](https://huggingface.co/datasets/RE3SIM/sim-resources)
  *Why engineers care:* directly targets the “build a useful sim environment
  from a real tabletop” problem, not just a new simulator backend.
  *Caveat:* still requires careful scene/object alignment and task-specific
  validation; visual similarity is not a full physics guarantee.

- ⭐ **[2024] RoboGSim — Real2Sim2Real Robotic Gaussian Splatting Simulator**
  `[E][S][P][RT][L][V]` 🧪
  Real captures → Gaussian reconstruction + digital twin builder + scene
  composer + interactive engine. Links: [project](https://robogsim.github.io/)
  · [paper](https://arxiv.org/abs/2411.11839)
  *Why engineers care:* strong reference for an end-to-end environment-making
  stack with novel views, objects, trajectories, scenes, and policy evaluation.
  *Caveat:* inspect where physics is explicit vs visually reconstructed.

- ⭐ **[2025] RoboSimGS — High-Fidelity Simulated Data Generation for Real-World
  Zero-Shot Robotic Manipulation Learning with Gaussian Splatting**
  `[E][S][RT][L][V]` 🧪
  Multi-view real images → scalable photoreal and physically interactive
  manipulation environments. Links: [project](https://robosimgs.github.io/)
  *Why engineers care:* representative of the real-scene-to-training-data
  pipeline for manipulation.
  *Caveat:* needs careful separation between visual, geometric, and contact
  validation.

- **[2025] DISCOVERSE — Efficient Robot Simulation in Complex High-Fidelity
  Environments** `[E][S][P][RT][L]` 🧰
  3DGS rendering + MuJoCo physics + ROS interfaces for Real2Sim2Real robot
  learning. Links: [project](https://air-discoverse.github.io/) ·
  [paper](https://arxiv.org/abs/2507.21981)
  *Why engineers care:* useful architecture example for hybrid neural-rendering
  plus explicit physics environment construction.
  *Caveat:* newer ecosystem; verify reproducibility and supported task set.

- **[2024] SplatSim — Zero-Shot Sim2Real Transfer of RGB Manipulation Policies Using
  Gaussian Splatting** `[E][S][RT][L][V]`
  Gaussian-splat visual layer inside simulation to reduce RGB sim-real gap.
  Links: [project](https://splatsim.github.io/) ·
  [paper](https://arxiv.org/abs/2409.10161)
  *Why engineers care:* clean example of replacing the visual layer while
  preserving simulator scalability.
  *Caveat:* mostly visual-gap focused; pair with physics/contact checks.

- **[2025] GSWorld — Closed-Loop Photo-Realistic Simulation Suite for Robotic
  Manipulation** `[E][S][P][RT][L]`
  3DGS + physics-engine suite for manipulation policy benchmarking, DAgger-style
  data collection, and virtual teleoperation. Links:
  [project](https://3dgsworld.github.io/) ·
  [paper](https://arxiv.org/abs/2510.20813)
  *Why engineers care:* moves from static reconstruction toward closed-loop
  benchmarking and data generation.
  *Caveat:* new; code/data availability and real-world validation need tracking.

- **[2026] Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions** `[E][S][P][RT][V]` 🧰
  Real videos → soft-body digital twin and photoreal robot/object/environment
  rendering for policy evaluation. Links:
  [project](https://real2sim-eval.github.io/) ·
  [code](https://github.com/kywind/real2sim-eval)
  *Why engineers care:* important because soft-body/contact-rich interactions
  expose failures that rigid-body-only environments can miss.
  *Caveat:* task scope and soft-body model assumptions matter.

- **[2026] ReaDy-Go — Real-to-Sim Dynamic 3D Gaussian Splatting Simulation
  for Environment-Specific Visual Navigation with Moving Obstacles**
  `[E][S][RT][L][V]` 🧪
  Static scene GS + animatable human GS avatars → photorealistic dynamic
  navigation scenarios and datasets for target environments. Links:
  [project](https://syeon-yoo.github.io/ready-go-site/) ·
  [paper](https://arxiv.org/abs/2602.11575)
  *Why engineers care:* expands real2sim construction beyond static tabletop
  manipulation into dynamic navigation environments with moving obstacles.
  *Caveat:* navigation-focused; contact/interaction physics are less central
  than visual/dynamic-obstacle realism.

### Physics-aware and interaction-driven real2sim

- ⭐ **[2025] Scalable Real2Sim — Physics-Aware Asset Generation via Robotic
  Pick-and-Place Setups** `[O][P][ID][RT][V]` 🧪
  Robot interaction + camera → visual geometry, collision geometry, mass and
  inertial parameters → simulatable object descriptions. Links:
  [project](https://scalable-real2sim.github.io/) ·
  [paper](https://arxiv.org/abs/2503.00370)
  *Why engineers care:* adds physical parameter identification to reconstruction,
  which is essential for environments that need contact dynamics.
  *Caveat:* object-centric rather than full-scene; best treated as a module in a
  larger environment builder.

- ⭐ **[2023] Sim2Real² — Actively Building Explicit Physics Model for Precise
  Articulated Object Manipulation** `[O][P][ID][RT][V]` 🧪
  Robot actively interacts with an articulated object to build an explicit
  physics model for planning/manipulation. Links:
  [project](https://ttimelord.github.io/Sim2Real2-site/)
  *Why engineers care:* shows why “environment construction” sometimes requires
  task-directed interaction, not passive scanning.
  *Caveat:* focused on articulated objects and precise manipulation.

- **[2026] Real2Sim based on Active Perception with automatically
  VLM-generated Behavior Trees** `[E][O][P][ID][RT]`
  User request + incomplete sim + RGB observation → VLM-generated behavior tree
  for physical parameter acquisition with a real robot. Links:
  [paper](https://arxiv.org/abs/2601.08454)
  *Why engineers care:* makes environment construction intent-driven: acquire
  only the parameters needed for the current simulation objective.
  *Caveat:* early work; implementation and generality need tracking.

- **[2026] Real-to-Sim for Highly Cluttered Environments via
  Physics-Consistent Inter-Object Reasoning** `[E][O][P][RT][V]`
  Single-view RGB-D → physically consistent cluttered 3D scenes for
  contact-rich manipulation. Links: [project](https://physics-constrained-real2sim.github.io/) ·
  [paper](https://arxiv.org/abs/2602.12633)
  *Why engineers care:* addresses the gap between geometric reconstruction and
  physically stable clutter.
  *Caveat:* very recent; verify code/data and simulator integration when public.

- **[2026] MATTERIX — Towards a Digital Twin for Robotics-Assisted Chemistry
  Lab Automation** `[E][S][P][RT][L][V]`
  Multi-scale chemistry-lab digital twin covering robot manipulation, powder
  and liquid dynamics, device functionality, heat transfer, and basic reaction
  kinetics, with hierarchical workflow definitions and sim-to-real evidence.
  Links: [paper](https://arxiv.org/abs/2601.13232)
  *Why engineers care:* a good reminder that environment construction is not
  only geometry plus rendering; some domains require explicit process semantics,
  instrument logic, and non-rigid material dynamics for the twin to be useful.
  *Caveat:* highly domain-specific; useful as a digital-twin systems reference
  even when its chemistry abstractions do not transfer directly.

### Upstream perception and reconstruction precursors

- **[2026] Reconstruction by Generation — 3D Multi-Object Scene Reconstruction
  from Sparse Observations** `[E][O]`
  Sparse RGB-D observations → probabilistic joint estimation of object/part
  shape and pose in cluttered, occluded scenes. Links:
  [project](https://reconstruction-by-generation.github.io/) ·
  [paper](https://reconstruction-by-generation.github.io/recgen.pdf)
  *Why engineers care:* relevant upstream to environment construction because
  occlusion-robust object/part recovery is often the bottleneck before any
  simulator lowering, calibration, or task composition can happen.
  *Caveat:* keep it out of the main curated list unless/until the pipeline shows
  clearer simulator-facing outputs, physical grounding, or direct interactive
  digital-twin validation.

### Task and environment generation

- ⭐ **[2024] GenSim — Generating Robotic Simulation Tasks via Large Language Models**
  `[E][O][L]` 🧰 📦
  LLM-generated simulation tasks, curricula, and demonstrations. Links:
  [paper](https://arxiv.org/abs/2310.01361) ·
  [code](https://github.com/liruiw/GenSim)
  *Why engineers care:* foundational example of using code-generating LLMs to
  create task environments rather than hand-author every scenario.
  *Caveat:* generated task validity and physics realism require automated checks.

- ⭐ **[2025] GenSim2 — Scaling Robot Data Generation with Multi-modal and Reasoning
  LLMs** `[E][O][L][V]`
  Multimodal/reasoning LLMs generate articulated, 6-DoF robotic tasks in
  simulation for pretraining multitask policies. Links:
  [project](https://gensim2.github.io/)
  *Why engineers care:* pushes beyond text-only task generation toward more
  realistic articulated-object task generation.
  *Caveat:* belongs partly to learning; environment validity criteria should be
  inspected separately from policy results.

- **[2025] GRS — Generating Robotic Simulation Tasks from Real-World Images**
  `[E][O][RT][L]`
  Real-world images → object correspondence and task simulation environments.
  Links: [paper](https://arxiv.org/abs/2410.15536) ·
  [NVIDIA research](https://research.nvidia.com/publication/2025-06_grs-generating-robotic-simulation-tasks-real-world-images-0)
  *Why engineers care:* directly targets generating task environments from real
  visual context.
  *Caveat:* task feasibility and physical validity need explicit validation.

- **[2024] RoboGen — Generative Simulation for Automated Robot Learning** `[E][O][L]`
  Foundation/generative models propose tasks, populate scenes/assets, generate
  supervision, and learn skills in a propose-generate-learn loop. Links:
  [paper](https://arxiv.org/abs/2311.01455) ·
  [code](https://github.com/Genesis-Embodied-AI/RoboGen) ·
  [PMLR](https://proceedings.mlr.press/v235/wang24cc.html)
  *Why engineers care:* early high-level blueprint for automated environment and
  task generation at scale.
  *Caveat:* not necessarily real-scene faithful; more generative than calibrated.

- **[2025] RoboTwin 2.0 — Scalable Data Generator and Benchmark with Strong Domain
  Randomization for Bimanual Manipulation** `[E][R][O][DR][L][V]` 🧰 📦
  MLLM task generation + annotated object library + trajectory automation +
  domain randomization for bimanual manipulation data. Links:
  [project](https://robotwin-platform.github.io/) ·
  [paper](https://arxiv.org/abs/2506.18088)
  *Why engineers care:* environment generation for cross-embodiment, bimanual,
  cluttered manipulation.
  *Caveat:* benchmark/data-generator style; check real-world validation coverage.

- **[2026] RoboLab — A High-Fidelity Simulation Benchmark for Analysis of Task
  Generalist Policies** `[E][R][O][S][L][V]` 🧰 📦
  Manually or agentically arranged scenes + language instructions → Isaac Lab
  task libraries and robot-agnostic runnable environments. Links:
  [project](https://research.nvidia.com/labs/srl/projects/robolab/) ·
  [paper](https://arxiv.org/abs/2604.09860) ·
  [code](https://github.com/NVLabs/RoboLab)
  *Why engineers care:* provides a reproducible environment-generation and
  evaluation substrate for 120 manipulation tasks, controlled perturbations, and
  policy-server benchmarking.
  *Caveat:* not real-scene reconstruction; include it here for task/environment
  generation and in `awesome-sim2real-learning` for policy-evaluation use.

### Demonstration-to-synthetic-rollout pipelines

- ⭐ **[2026] ComSim — Building Scalable Real-World Robot Data Generation via
  Compositional Simulation** `[E][O][S][L][V]` 🧪
  Classical simulation + neural simulation → closed-loop real-sim-real data
  augmentation for scalable action-video pairs. Links:
  [project](https://faceong.github.io/ComSim/) ·
  [paper](https://arxiv.org/abs/2604.11386)
  *Why engineers care:* a useful 2026 formulation of environment construction
  as composition: keep simulator action consistency while using neural rendering
  to reduce appearance/domain gaps.
  *Caveat:* watch for whether physical/contact dynamics are truly improved or
  mainly visually translated by the neural simulator.

- **[2025] Real2Render2Real — Scaling Robot Data Without Dynamics Simulation or Robot Hardware** `[E][O][S][L][V]` 🧰
  Smartphone scan + monocular human demonstration → object motion and thousands
  of photoreal synthetic demonstrations without dynamics simulation. Links:
  [project](https://real2render2real.com/) ·
  [paper](https://arxiv.org/abs/2505.09601)
  *Why engineers care:* important counterpoint: sometimes useful synthetic data
  can come from rendering and trajectory retargeting without full physics.
  *Caveat:* bypassing dynamics is powerful but can miss contact/force failures.

- **[2025] ROSE — Reconstructing Objects, Scenes, and Trajectories from Casual Videos for Robotic Manipulation** `[E][O][RT][L][V]`
  Casual videos → objects, scenes, trajectories → simulation training and
  Real2Sim2Real deployment. Links: [project](https://rose-project-2025.github.io/)
  *Why engineers care:* turns casual video into a richer environment/data source,
  which is a promising route for scalable environment construction.
  *Caveat:* inspect how physical execution constraints are recovered from video.

- **[2023] MimicGen — Data Generation System for Scalable Robot Learning using Human Demonstrations** `[E][L][V]` 🧰 📦
  Few human demonstrations → many simulation demonstrations across tasks. Links:
  [project](https://mimicgen.github.io/) ·
  [paper](https://arxiv.org/abs/2310.17596)
  *Why engineers care:* not a scene reconstructor, but a key environment-data
  generator once a task environment exists.
  *Caveat:* depends on an already valid environment and task decomposition.

### Digital twin-guided policy improvement loops

- **[2026] TwinRL-VLA — Digital Twin-Driven Reinforcement Learning for
  Real-World Robotic Manipulation** `[E][RT][L][V]` 🧪
  Smartphone-captured scenes → high-fidelity digital twins that expand VLA
  exploration support and guide real-world human-in-the-loop rollouts. Links:
  [paper](https://arxiv.org/abs/2602.09023)
  *Why engineers care:* shows digital twins as active exploration and failure
  sampling tools, not only offline evaluation environments.
  *Caveat:* strongly overlaps with `awesome-sim2real-learning`; include here only
  for the digital-twin construction and environment-guided exploration loop.

### Video/world-model-assisted construction

- **[2026] V-Dreamer — Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors** `[E][S][L][V]`
  Video-generation priors → executable trajectories through visual-kinematic
  alignment. Links: [paper](https://arxiv.org/abs/2603.18811)
  *Why engineers care:* points toward generative video as a prior for simulation
  and trajectory synthesis.
  *Caveat:* early direction; physical consistency and long-horizon stability need
  careful validation.

- **[2025] IRASim — Fine-Grained World Model for Robot Manipulation** `[E][S][L][V]`
  Action-conditioned robot-world video model for policy evaluation and planning.
  Links: [project](https://gen-irasim.github.io/)
  *Why engineers care:* expands “environment” beyond physics engines toward
  learned controllable world models that can evaluate policies.
  *Caveat:* belongs at the boundary with `awesome-sim2real-learning`; include only
  when used as an environment/evaluation substrate.

## Suggested next README changes

After review, add a new README section:

```markdown
## Environment Construction Methods
```

Recommended first representatives:

1. Re³Sim
2. RoboGSim
3. RoboSimGS
4. DISCOVERSE
5. ReaDy-Go
6. Scalable Real2Sim
7. Physics-consistent cluttered Real2Sim
8. ComSim
9. GenSim / GenSim2
10. GRS
11. Real2Render2Real / ROSE
12. TwinRL-VLA

## Open questions for deeper curation

- Which systems produce **executable physics state** versus only photoreal
  observations?
- Which systems expose a reproducible task API?
- Which systems validate sim-real **behavior correlation** rather than only image
  similarity?
- Which systems support closed-loop robot policy evaluation?
- Which methods are environment construction papers, and which belong more in
  `awesome-sim2real-learning`?
