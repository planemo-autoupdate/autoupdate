"""
Output autoupdate PR text

Also update changelog
"""

import argparse
from datetime import date


parser = argparse.ArgumentParser()
parser.add_argument('--repo', help='Tool repo')
parser.add_argument('--log', help='Autoupdate log')
# parser.add_argument('--shed', help='Location of .shed.yml file input.')
parser.add_argument('--out', help='Output file.')
parser.add_argument('--changelog', help='Changelog location')
args = parser.parse_args()

text = []
new_changelog_lines = []

text.append(f"Hello! This is an automated update of the following workflow: **{args.repo}**. I created this PR because I think one or more of the component tools are out of date, i.e. there is a newer version available on the ToolShed.\n")
text.append("By comparing with the latest versions available on the ToolShed, it seems the following tools are outdated:")

with open(args.log) as f:
    for n in f.readlines():
        if ' -> ' in n:
            text.append(f"* `{n.split()[1]}` should be updated to `{n.split()[3]}`")
            new_changelog_lines.append(f"- `{n.split()[1]}` was updated to `{n.split()[3]}`")
        if 'The workflow release number has been updated' in n:
            release_line = n
            text.append(f"\n{release_line}")

with open(args.changelog, 'r+') as f:
    lines = f.readlines()
    new_change = [f"## [{release_line.split(' to ')[-1]}] {str(date.today()}", "", "### Automatic update:"] + new_changelog_lines
    new_lines = [lines[0]] + new_change + lines[1:]
    f.seek(0)
    f.write('\n'.join(new_lines))

with open(args.out, 'w') as f:
    f.write('\n'.join(text))

print(f"Updating {args.repo} {release_line.split('updated')[-1]}")
