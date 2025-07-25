## Hands-On Exercises: Environments & Deployments

### Learning Objectives

By the end of this section, you will:
- Define and configure environments in GitLab
- Use `environment.name`, `environment.url`, and `environment.on_stop`
- See deployments in GitLab UI (Environments tab and Deploy Boards)
- Implement a basic deploy-to-staging pipeline

---

## Task 1 - Define a Staging Environment and Manual Deploy Job

1. Add a `deploy-staging` job to your `.gitlab-ci.yml` which runs on an environment `staging` with URL `https://staging.example.com`.
    - Go to **Operate -> Environments** in GitLab to see the `staging` environment listed in the active environments.

2. Add a stop job (i.e., `stop-staging`) job for the environment. This job should be triggered manually.
    - After the `deploy-staging` job is finished, trigger the `stop-staging` jobs in the pipeline view.
    - Go to **Operate -> Environments** and observe the status change (i.e., the `staging` environment is listed in the stopped environments).

3. Connect the Deploy and Stop Jobs via `on_stop`.
    - Hint: The `on_stop` definition should be done in the `deploy-staging` job.
    - Observe that you can now stop the environment under **Operate -> Environments**.

---
