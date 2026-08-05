# Repository mapping

## Establish purpose

Identify these facts:

- what the repository automates
- who consumes it
- supported environments
- repository type

Record one repository type:

- playbook repository
- standalone-role repository
- collection
- mixed workspace

Record these declared versions:

- Ansible community package and `ansible-core`
- Python and collections
- quality and execution tools
- targets

Read these sources:

- version declarations
- supported-platform statements
- dependency files
- CI configuration

Keep each version identity separate. State missing or conflicting declarations as gaps.

## Map entry points

Map entry points before judging structure.

- Find top-level playbooks and imports or includes.
- Find roles and collections.
- Find collection content.
- Find inventories and wrappers.
- Find CI and execution environments.
- Find Molecule scenarios and other tests.
- Record major components and their direct relationships.

## Map responsibility

Map responsibility ownership.

- Identify role and collection boundaries.
- Identify inventory and variable ownership.
- Identify template and file ownership.
- Identify shared handlers and tasks.
- Identify plugins and modules.
- Separate project-specific content from reusable content.

## Trace data and dependencies

Trace these inputs:

- defaults and required inputs
- role variables and parameters
- inventory and environment values

Inspect argument specifications when present.

Record these dependencies:

- variable leakage and hidden dependencies
- imports and dynamic includes
- collection dependencies
- environment data in reusable content

Define a dynamic include as an include selected during play execution.

## Assess reuse and coupling

Assess duplicated task sequences, templates, and handlers. Assess these structural risks:

- near-identical roles and resource ownership
- circular and implicit dependencies
- unrelated responsibilities and over-fragmentation

## Assess tests and delivery

Compare these items with tests:

- components and platforms
- inputs and claimed behaviour
- scenario scope and CI versions
- execution-environment content

Compare each item with supported targets.

Finish this map before you recommend an architectural change.
