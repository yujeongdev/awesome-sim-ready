# Contributing to Awesome Real2Sim Robotics

Thanks for helping make this list useful.

The goal is not to collect every 3D, simulator, or sim2real paper. The goal is to help engineers find work that improves the **Real2Sim substrate** for robot training, testing, debugging, calibration, or deployment.

## Inclusion Criteria

A resource should contribute to at least one Real2Sim dimension:

- `[G]` **Geometry** — mesh, part meshes, Gaussian/implicit geometry, collision geometry.
- `[A]` **Articulation** — part hierarchy, joint type, joint axis, limits, kinematic graph.
- `[P]` **Physics / contact / dynamics** — mass, inertia, friction, compliance, damping, stability.
- `[F]` **Simulator format** — URDF, MJCF/XML, SDF, USD, simulator-native assets.
- `[E]` **Environment / scene** — world layout, dynamic scenes, procedural scenarios, task state.
- `[R]` **Robot / actuator model** — robot bodies, controllers, actuators, latency, deployment interfaces.
- `[O]` **Object / material model** — usable objects inside environments, especially when tied to interaction.
- `[S]` **Sensor simulation** — RGB-D, tactile, LiDAR, IMU, event camera, synthetic annotations.
- `[DR]` **Domain randomization / adaptation** — environment-level variation and gap reduction.
- `[ID]` **System identification / calibration** — real-data alignment of physics, sensors, actuators, or tasks.
- `[RT]` **Real2Sim / digital twin** — real-world capture into executable simulator state.
- `[L]` **Learning environment support** — RL/IL/task APIs when they define reusable environments.
- `[V]` **Validation** — real robot/data evidence, failure replay, behavior correlation, hardware-in-the-loop.

Good additions include:

- simulator-ready asset generation or reconstruction;
- articulated object reconstruction and URDF/MJCF/USD export;
- real2sim / digital twin systems;
- scene generation and synthetic data pipelines;
- sensor simulators and calibration tools;
- environment-level domain randomization tools;
- validation methods for sim-real gaps.

Usually out of scope:

- pure visual 3D reconstruction with no simulator-facing interaction;
- pure policy learning papers with no reusable Real2Sim contribution;
- generic robot-policy papers where simulation is incidental;
- rendering-only demos with no task interface or validation;
- links with no paper, project, code, dataset, or documentation context.

## Entry Format

Use this compact format in `README.md`:

```markdown
- ⭐ **[YEAR] Resource Name — Short Title** `[G][A][P][F][E][S][RT][V]` 🌐🛠️📦🤖
  One-line summary focused on the Real2Sim contribution. Links: paper · project · code · data
  *Why engineers care:* concrete utility for building, calibrating, evaluating, or deploying simulator-executable outputs.
  *Caveat:* known limitation, missing real validation, simulator lock-in, license concern, or fragile setup.
```

Availability labels:

- 🧪 paper-only
- 🌐 project page / demo
- 🛠️ code available
- 📦 data / checkpoints / assets
- 🤖 simulator-validated or simulator-facing evidence
- 🧾 license/provenance worth checking before company use
- ⭐ representative / must-read

Keep capability tags as bracket tokens such as `[G][A][P][F][V]` or `[E][S][RT][V]`. They are easier to grep, sort, lint, and migrate into structured metadata later.

## Quality Bar

Before opening a PR, check:

- Does the entry identify the Real2Sim contribution?
- Does it explain what simulator-facing output is produced?
- Does it identify the robot, task, sensor, object, or physics substrate if relevant?
- Does it avoid overstating simulation readiness?
- Are caveats included when validation is weak?
- Are links stable and official when possible?
- Is the item placed in the most useful section, not just the newest section?

## Style

- Prefer concise, engineer-facing summaries.
- Avoid hype words unless backed by evidence.
- Use official project/code/paper links when available.
- Do not copy abstracts wholesale.
- Keep the README navigable; move long explanations into `docs/`.
