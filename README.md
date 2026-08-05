# Playbook Steward

Playbook Steward is a Codex-first collection of focused skills for working with Ansible repositories.

The current experimental skill is:

- `playbook-steward-architecture` — audits an Ansible repository's structure and proposes proportionate improvements.

This is an early public development project.

## Install for your user

From this repository, run:

```sh
destination="$HOME/.agents/skills/playbook-steward-architecture"

if [ -e "$destination" ]; then
  printf 'Installation already exists: %s\n' "$destination" >&2
  exit 1
fi

mkdir -p "$HOME/.agents/skills"
cp -R skills/playbook-steward-architecture "$destination"
```

Start a fresh Codex session, then invoke it with `$playbook-steward-architecture`.
