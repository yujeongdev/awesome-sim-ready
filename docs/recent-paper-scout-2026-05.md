# Recent Paper Scout (2026-05-07)

다음은 `awesome-real2sim`에 **추가 검토할 만한 최신 후보 논문**들입니다.
선정 기준은 (1) Real2Sim/디지털트윈 직접성, (2) 시뮬레이터 실행가능성(geometry+articulation+physics/format), (3) 최근성(2026 중심)입니다.

## 추천 우선순위

1. **URDF-Anything+ (arXiv:2603.14010, 2026-03)**
   - 링크: https://arxiv.org/abs/2603.14010
   - 핵심: 자동회귀 방식으로 articulated object의 geometry+kinematics를 생성하고, 물리 시뮬레이션 실행 가능성까지 전면에 둔 접근.
   - 왜 추가할 만한가: 현재 리포의 `Articulated Object Generation` 축(URDFormer, Real2Code, Articulate-Anything)과 직접 연결되며, **최신 세대의 executable articulation 생성** 흐름을 보강함.

2. **A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting (arXiv:2601.03200, 2026-01-06)**
   - 링크: https://arxiv.org/abs/2601.03200
   - 핵심: 조작(manipulation) 용도의 고충실도 디지털 트윈 구축.
   - 왜 추가할 만한가: 리포의 `Environment Construction and Digital Twins`/`Calibration & Validation` 구간에 적합하며, **3DGS 기반 실시간/고충실도 twin** 트랙을 명확히 보강함.

3. **Real2Sim based on Active Perception with automatically VLM-generated Behavior Trees (arXiv:2601.08454, 2026-01)**
   - 링크: https://arxiv.org/abs/2601.08454
   - 핵심: VLM이 behavior tree를 자동 생성해, 과업 관련 물리 파라미터(질량/마찰 등)를 능동적으로 수집.
   - 왜 추가할 만한가: 단순 재구성이 아니라 **task-driven system identification** 성격이 강해, Real2Sim의 실사용 측면(파라미터 추정, 불완전 모델 보정)을 강화함.

4. **SyncTwin: Fast Digital Twin Construction and Synchronization for Safe Robotic Grasping (arXiv:2601.09920, 2026-01-14)**
   - 링크: https://arxiv.org/abs/2601.09920
   - 핵심: 동적/가려짐(occlusion) 환경에서 twin 동기화를 통해 안전한 grasping 계획-실행 루프를 구성.
   - 왜 추가할 만한가: `real→sim→real` 폐루프 관점에서 **동기화(synchronization)**를 명시적으로 다뤄, 디지털 트윈 운용성 측면을 보완함.

## 예비 후보 (선별 후 추가)

- **GaussTwin (arXiv:2603.05108, 2026-03)** — GS + 물리 보정 결합 관점에서 흥미롭지만, 구현/재현성 정보 확인 후 본문 반영 권장.
  - https://arxiv.org/abs/2603.05108
- **Asset Harvester (arXiv:2604.18468, 2026-04)** — AV 중심이지만 real logs→reusable assets 파이프라인이 분명해 도메인 확장 참고 가치가 큼.
  - https://arxiv.org/abs/2604.18468

## 경계선이지만 추적할 후보

- **ManiDreams (arXiv:2603.18336, 2026-03-24)** — 직접적인 real-scene/object reconstruction 논문은 아니지만, perceptual/parametric/structural uncertainty를 한 번에 다루는 조작용 intuitive physics 레이어라는 점에서 `Calibration, Domain Gap, and Validation` 섹션 보강 가치가 큼.
  - https://arxiv.org/abs/2603.18336
  - 왜 중요하나: Real2Sim 결과물이 보기 좋게 재구성되었는지보다, 불확실성을 안고도 **행동 시점에 얼마나 robust하게 쓸 수 있는지**를 평가/활용하는 관점을 제공함.
  - 주의할 점: 자산/환경을 직접 생성하는 pipeline은 아니므로, README에서는 보조적인 validation/planning layer로 한정해 설명하는 편이 맞음.

## 리포 반영 제안

- `README.md`
  - `🦾 Articulated Object Generation and Reconstruction`에 **URDF-Anything+** 추가.
  - `🌍 Environment Construction and Digital Twins`에 **High-Fidelity DT (3DGS), SyncTwin** 추가.
  - `🎚️ Calibration, Domain Gap, and Validation`에 **Active Perception + BT Real2Sim**, **ManiDreams** 추가.

- `docs/reading-path.md`
  - 4단계(Active/Physics-Aware Real2Sim)에 Active Perception + BT, **ManiDreams**를 구체 항목으로 명시.
  - 디지털 트윈 트랙에 `construction`과 `synchronization`을 분리해 읽기 순서(구축→동기화→검증)로 정리.

## 메모

- 이번 스카우트는 2026-05-07 기준 최신 arXiv 메타데이터를 우선 확인함.
- 다음 큐레이션 단계에서 코드/라이선스/재현성(benchmark, simulator support, asset export format) 교차검증 권장.
