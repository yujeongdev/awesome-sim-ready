# Real2Sim Environment QA Checklist

This checklist is for deciding whether a robot simulation environment is merely attractive or actually useful for sim2real engineering.

## 1. Scope and Task Definition

- [ ] What real task is the environment meant to support?
- [ ] Is the target robot named and modeled?
- [ ] Is the expected real-world deployment setting clear?
- [ ] Are success/failure metrics defined before tuning the simulator?

## 2. Scene and Asset Integrity

- [ ] Are scene scale, gravity direction, and coordinate frames correct?
- [ ] Are object meshes, collision meshes, and materials separated?
- [ ] Are articulated objects represented with correct joint axes, limits, and frames?
- [ ] Are support surfaces, occluders, and contact geometry task-relevant?
- [ ] Are asset licenses/provenance acceptable for intended use?

## 3. Robot and Actuation

- [ ] Does the robot model match the real hardware revision?
- [ ] Are mass, inertia, center of mass, joint limits, and damping plausible?
- [ ] Is the real control mode represented: position, velocity, torque, impedance, or vendor API?
- [ ] Are actuator delay, saturation, rate limits, and command frequency modeled?
- [ ] Are controller and simulator timesteps documented?

## 4. Sensor Modeling

- [ ] Are camera intrinsics, extrinsics, distortion, resolution, and FoV calibrated?
- [ ] Are depth bias, missing data, quantization, and noise profiles modeled?
- [ ] Are tactile/LiDAR/IMU signals simulated at the right rate and coordinate frame?
- [ ] Are timestamps synchronized across sensors and robot state?
- [ ] Are rendering settings tied to real data, not just visual preference?

## 5. Physics and Contact

- [ ] Are friction, restitution, compliance, damping, and stiffness documented?
- [ ] Are mass/inertia values measured, identified, estimated, or defaulted?
- [ ] Are contact events stable under gravity and repeated scripted interaction?
- [ ] Are collision meshes simpler and more stable than visual meshes?
- [ ] Are failure cases such as tunneling, jitter, exploding contacts, and interpenetration checked?

## 6. Domain Gap Strategy

- [ ] Is the main mismatch named: perception, dynamics, contact, actuation, task distribution, or software stack?
- [ ] Is domain randomization tied to measured real-world variation?
- [ ] Are calibration and randomization separated conceptually?
- [ ] Are randomized variables logged and reproducible?
- [ ] Are stress tests designed around real failure modes?

## 7. Task Interface and Reproducibility

- [ ] Can the environment reset deterministically?
- [ ] Are observation/action spaces documented?
- [ ] Are rewards, termination conditions, and success metrics explicit?
- [ ] Are seeds, asset versions, simulator versions, and robot models pinned?
- [ ] Can logs be replayed from the same initial conditions?

## 8. Real-World Validation

- [ ] Is validation done on a real robot or real sensor data?
- [ ] Are visual metrics separated from behavior metrics?
- [ ] Are trajectory error, contact timing, force/torque residual, or sensor residual measured?
- [ ] Does the simulator reproduce known real failures?
- [ ] Does simulation predict policy ranking, task success, or safety constraints?

## Validation Ladder

1. **Renderable** — scene loads and looks plausible.
2. **Importable** — robot, objects, sensors, and task state parse correctly.
3. **Interactable** — scripted actions produce stable contacts, sensor outputs, and state transitions.
4. **Calibrated** — important residuals are measured against real data.
5. **Task-predictive** — simulation predicts real failures, rankings, or success rates.

## Red Flags

- “Photorealistic” is used as a substitute for contact or sensor validation.
- URDF/CAD values are treated as ground truth without measurement.
- Real robot control frequency is different from simulator frequency but not modeled.
- Domain randomization ranges are arbitrary and not tied to real variation.
- Evaluation only shows videos, not residuals or task metrics.
