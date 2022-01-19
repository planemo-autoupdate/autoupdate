"""
Output autoupdate PR text
"""

import argparse

import yaml


parser = argparse.ArgumentParser()
parser.add_argument('--repo', help='Tool repo')
parser.add_argument('--log', help='Autoupdate log')
# parser.add_argument('--shed', help='Location of .shed.yml file input.')
parser.add_argument('--out', help='Output file.')
args = parser.parse_args()

text = []

text.append(f"Hello! This is an automated update of the following workflow: **{args.repo}**. I created this PR because I think one or more of the component tools are out of date, i.e. there is a newer version available on the ToolShed.\n")
text.append("The following tools have been updated:")

with open(args.log) as f:
    for n in f.readlines():
        if ' -> ' in n:
        text.append(f"* {n.split()[1]} was updated to {n.split()[1]}")
    else:
        raise Exception

with open(args.out, 'w') as f:
    f.write('\n'.join(text))

# print(f'Updating {args.repo} {update}')
print(f'Updating {args.repo}')
