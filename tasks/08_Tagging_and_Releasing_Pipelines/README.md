# Hands-On Exercises: Tagging & Releasing Pipelines

## Learning Objectives

By the end of this section, you will:
- Understand the difference between Git tags and GitLab Releases
- Use `CI_COMMIT_TAG` to identify versioned releases
- Automate changelog generation
- Create a GitLab Release that includes attached artifacts

---

## Task 1 - Semantic Versioning Pipeline

1. Create a semantic versioning pipeline which is triggered whenever a [GitLab Tag](https://docs.gitlab.com/user/project/repository/tags/) of the form `v1.2.3` is published to the repository.
    - Hint: Use the GitLab variable `CI_COMMIT_TAG` which includes the name of the tag being published.
    - To test the semantic versioning pipeline, create tag under **Code -> Tags**

2. [**Advanced task**]: Extend the pipeline to automatically create a new GitLab Tag when a feature branch is merged into `main`.
    - Will the semantic versioning pipeline from the first step be executed automatically after the merge?
    - Hint: Use the labels of the merge request to identify whether the change results in a `major`, `minor`, or `patch` release.
    - Hint: A `python` script with the `gitlab` and `semver` libraries may facilitate this task.
    - Hint: A GitLab CI/CD Variable `GITLAB_TOKEN` with API Repository access is configured in the repository.

---
