"""
Output autoupdate PR text
"""

import argparse

import yaml


parser = argparse.ArgumentParser()
parser.add_argument("--repo", help="Tool repo")
parser.add_argument("--log", help="Autoupdate log")
parser.add_argument("--shed", help="Location of .shed.yml file input.")
parser.add_argument("--out", help="Output file.")
args = parser.parse_args()

with open(args.log) as f:
    lines = f.readlines()
    for line in lines:
        if "Updating" in line and "from version" in line:
            words = line.split()
            from_version = words[4]
            to_version = words[6]
            if from_version != to_version:
                update = f"from version {from_version} to {to_version}"
                break
    else:
        raise Exception(
            f"`Updating ... from version` line not found in {args.log}:\n{''.join(lines)}"
        )

text = []

text.append(
    f"Hello! This is an automated update of the following tool: **{args.repo}**. I created this PR because I think the tool's main dependency is out of date, i.e. there is a newer version available through conda."
)

text.append(f"I have updated {args.repo} {update}.")

with open(args.shed) as f:
    y = yaml.load(f, Loader=yaml.SafeLoader)

if y.get("homepage_url"):
    url = y.get("homepage_url").strip("/")
    if "github.com" in url:
        if len(url.split("github.com")[1].split("/")) > 1:
            url += "/releases"
    text.append(f"**Project home page:** {url}")

if y.get("maintainers"):
    text.append(
        "**Maintainers:** " + ", ".join([f"@{m}" for m in y.get("maintainers")])
    )

text.append(
    "For any comments, queries or criticism about the bot, not related to the tool being updated in this PR, please create an issue [here](https://github.com/planemo-autoupdate/autoupdate/issues/new)."
)

with open(args.out, "w") as f:
    f.write("\n\n".join(text))

print(f"Updating {args.repo} {update}")
