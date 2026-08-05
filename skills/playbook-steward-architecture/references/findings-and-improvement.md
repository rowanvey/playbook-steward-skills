# Findings and improvement

## Apply proportionate best practice

Define best practice as a version-compatible choice that solves an identified repository problem. The problem must concern one of these areas:

- correctness or safety
- ownership or maintenance
- discoverability or testability

Apply this order:

1. Observed repository goals and coherent conventions.
2. Supported versions.
3. Version-matched official guidance.
4. An established problem-solving pattern.
5. Clearly labelled optional modernisation.

Never recommend a change only for these reasons:

- modern repository or standard skeleton
- newer syntax or collection fashion
- model preference

Classify each finding as one of these types:

- correctness defect
- safety risk
- maintainability problem
- testability problem
- inconsistent architecture
- unsupported version choice
- optional modernisation
- style preference

Normally omit style preferences. Do not call age a defect.

## Report findings

Use this report order:

1. Repository purpose and map.
2. Strengths worth preserving.
3. Five highest-value structural findings.
4. Evidence, impact, and required or optional status for each finding.
5. Target architecture when a real problem justifies it.
6. Smallest staged improvement plan.
7. Important evidence gaps.
8. Explicit non-goals.

Describe responsibilities and boundaries before file moves. State observed facts separately from inference and unknowns.

Each improvement stage must solve one useful problem. Preserve supported behaviour and avoid unrelated cleanup. State these items:

- the main migration risk
- suitable validation
- a reversible action where practical

## Exclusions

Exclude these activities:

- ordinary task-level code review
- single runtime-failure diagnosis
- repository edits
- Ansible and infrastructure execution

Exclude these architecture claims:

- fashionable layouts
- collection conversion without need
- age-based defect claims

Exclude these specialist scopes:

- AAP and AWX
- EDA and Windows
- network and cloud
- Kubernetes and compliance architecture
- general workflow or orchestration
