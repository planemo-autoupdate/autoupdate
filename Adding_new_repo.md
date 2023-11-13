# Adding a new repo to auto updated repo list

## What should be on your repo

- If it is a workflow repo, each directory with a `.ga` workflow file should also contain a `CHANGELOG.md` file.

- If it is a tool repo, tool versions must use the @TOOL_VERSION@ macro as explained in https://galaxy-iuc-standards.readthedocs.io/en/latest/best_practices/tool_xml.html#tool-versions

## What should change in this repo (can be changed by opening a pull request)

1. Add your repo info to [the workflow file](./.github/workflows/autoupdate.yml) in the `matrix/include` list.

2. Add the list of tools/workflows that should be skipped (if any) in a file named `${upstream_repo_owner}_${upstream_repo_name}_skip_list`.

## What should change outside of this repo (requires to be part of planemo-autoupdate organization)

This is what the reviewer should do before merging the PR:

1. Fork the repository under the planemo-autoupdate organisation.

2. In the fork settings on GitHub, give write access to the `gxydevbot` account.

