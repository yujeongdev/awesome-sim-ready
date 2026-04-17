# 📚 Reading Path

This path is for engineers and researchers who want to understand Real2Sim robotics without drowning in generic 3D generation, rendering, simulator, or policy-learning papers.

## 0. Start with the Boundary

Real2Sim asks:

```text
real-world evidence → simulator-executable representation
```

This repo focuses on constructing assets, scenes, environments, sensors, physics models, and digital twins. Pure behavior transfer belongs in `awesome-sim2real-learning` unless the paper also contributes a reusable Real2Sim substrate.

## 1. Learn Object / Asset Real2Sim

Start with object-level outputs because environments are built from executable assets.

- SAPIEN / PartNet-Mobility
- URDFormer
- Real2Code
- Articulate-Anything
- PhysX-Anything
- SIMART

Questions to ask:

- Does the method output an executable representation?
- Are geometry, articulation, physics, and format handled separately?
- Can the output become URDF/MJCF/USD, or is it only a visual demo?
- Is simulator validation shown?

## 2. Add Physics and Materials

Then study physical grounding:

- PhysX-3D
- SOPHY
- PhysDreamer
- PhyCAGE
- DSO
- Scalable Real2Sim

Questions to ask:

- Which physical properties are measured, predicted, defaulted, or optimized?
- Is a simulator in the loop?
- Are contact, friction, and stability validated against real data?

## 3. Study Scene / Environment Real2Sim

Move from objects to worlds:

- Re³Sim
- RoboGSim
- RoboSimGS
- DISCOVERSE
- ReaDy-Go
- ComSim

Questions to ask:

- What is reconstructed from real data: appearance, geometry, collision, articulation, physics, sensor model, or task state?
- Is the output a pretty scene, an executable environment, or a calibrated digital twin?
- Which mismatch is measured: visual, geometric, dynamic, sensor, or task-level?

## 4. Study Active and Physics-Aware Real2Sim

Interaction often reveals physical parameters that passive scanning cannot.

- Sim2Real²
- Real2Sim with VLM-generated behavior trees
- Physics-consistent cluttered Real2Sim
- TwinTrack-style vision + contact physics systems

Questions to ask:

- Does the robot actively acquire task-relevant parameters?
- Are support relations and contact graphs modeled?
- Is differentiable or repeated simulation used to make the scene physically stable?

## 5. Study Sensor Real2Sim

Sensor realism is often its own problem.

- TACTO
- GelSight Simulation
- FOTS
- Taccel
- UniVTAC

Questions to ask:

- What signal is simulated: RGB, depth, tactile image, force, deformation, shear, or taxel values?
- Are intrinsics, extrinsics, noise, latency, and synchronization modeled?
- Is sensor realism validated with real data?

## 6. Evaluate with Behavior, Not Just Appearance

Use this ladder:

```text
load → interact → calibrate → stress-test → predict real behavior
```

The strongest Real2Sim systems can answer:

- Does this real-world failure replay in simulation?
- Does simulated policy ranking match real policy ranking?
- Do contact timings and trajectories match real logs?
- Does synthetic data improve real-world performance?

## 7. When Adding a New Resource

Place it by the missing piece it strengthens:

- object reconstruction → asset Real2Sim
- scene construction → environment Real2Sim
- physics/contact parameter inference → physics-aware Real2Sim
- camera/tactile/LiDAR rendering → sensor Real2Sim
- behavior correlation / failure replay → validation
