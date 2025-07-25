import os
import gitlab
import semver
import re

# Initialize GitLab client
gl = gitlab.Gitlab('http://gitlab:8000', private_token=os.environ['GITLAB_TOKEN'])
project_id = os.environ['CI_PROJECT_ID']
project = gl.projects.get(project_id)

# Get latest commit on main
branch = os.getenv("CI_COMMIT_REF_NAME", "main")
commits = project.commits.list(ref_name=branch, per_page=1)
if not commits:
    raise Exception("No commits found on main")
latest_commit = commits[0]

# Find merged MR with this commit as merge_commit_sha
merge_requests = project.mergerequests.list(state="merged", order_by="updated_at", sort="desc")
target_mr = None
for mr in merge_requests:
    if mr.merge_commit_sha == latest_commit.id:
        target_mr = mr
        break

if not target_mr:
    print("No matching merge request found for latest commit. Skipping tag creation.")
    exit(0)

print(f"Found merged MR: !{target_mr.iid} with labels: {target_mr.labels}")

# Get latest tag
tags = project.tags.list(order_by='name', sort='desc')
version = "0.0.0"
for tag in tags:
    if re.match(r"v\d+\.\d+\.\d+$", tag.name):
        version = tag.name.lstrip('v')
        break
current_version = semver.VersionInfo.parse(version)

labels = [label.lower() for label in target_mr.labels]
if 'major' in labels:
    next_version = current_version.bump_major()
elif 'minor' in labels:
    next_version = current_version.bump_minor()
else:
    next_version = current_version.bump_patch()

next_version = str(next_version)
next_tag = f"v{next_version}"

# Create new tag
project.tags.create({
    'tag_name': next_tag,
    'ref': branch,
    'message': f'Release {next_tag}'
})
print(f"Created tag {next_tag}")
