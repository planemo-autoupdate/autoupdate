# Adding a new repo to auto updated repo list

## What should be on your repo

- If it is a workflow repo, each directory with a `.ga` should have a `CHANGELOG.md`

- If is is a tool repo, Tool version must contain @TOOL_VERSION@

## What should change in this repo (can be changed writting a pull request)

1. Add your repo info to [the workflow file](./.github/workflows/autoupdate.yml) in the `matrix/include` list.

2. Add the list of your skipped tools/workflows. It should be named: `${upstream_repo_owner}_${upstream_repo_branch}_skip_list`.

## What should change outside of this repo (requires to be part of planemo-autoupdate organization)

This is what the reviewer should do before merging the PR:

1. Fork the repository with planemo-autoupdate.

2. Gives write access to `gxydevbot` to this fork.

