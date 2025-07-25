## Hands-On Exercises: GitLab CI/CD Pipeline Fundamentals

### Learning Objectives

By the end of this hands-on, you will:

- Write a basic `.gitlab-ci.yml` file with multiple stages and jobs.
- Understand `before_script` and `after_script`.
- Configure return code behavior for jobs.
- Implement an `always`-executing cleanup job.
- See how to trigger jobs manually or on a schedule.

---

## Task 1 — Create a Basic Multi-Stage Pipeline

1. **Create the pipeline file**
    - In the GitLab project, add a new file at the project root named `.gitlab-ci.yml`.
    - Define **3 stages**: `build`, `test`, and `deploy`.
    - Implement one simple job per stage (e.g., a simple echo statement).
    - Confirm that a pipeline is triggered and all jobs pass.
    - Documentation: The [tutorial](https://docs.gitlab.com/ci/quick_start/) provides reference points on the syntax of `.gitlab-ci.yml` files.

---

## Task 2 — Customize `before_script` and `after_script`

1. Add a **global** `before_script` that prints environment variables.
    - Hint: You may use the `env` command to print the environment variables

2. Add a **global** `after_script` that prints a cleanup message.

---

## Task 3 — Test Job Return Codes and Job Status

1. Modify the `test_job` so that it fails intentionally.
    - Hint: Try exiting the script of the job with a non-zero exit code.
    - Observe what happens with subsequent jobs when a job in the pipeline fails.

2. Set the `allow_failure` property to `true` and observe the behavior.
    - Documentation: [`allow_failure` keyword](https://docs.gitlab.com/ci/yaml/#allow_failure)

3. How can you accept specific exit codes as valid runs and others as pipeline failures?

---

## Task 4 — Add a Cleanup Job That Always Runs

1. Add a `cleanup_job` to the end of the pipeline that runs regardless of the execution status of previous jobs.
    - Documentation: [`when` keyword](https://docs.gitlab.com/ci/yaml/#when)

---

## Task 5 — Manual Triggers

1. Configure the `deploy_job` to require manual execution.
    - Observe that the deploy job is now paused, waiting for manual approval.
    - Documentation: [Controlling how jobs run](https://docs.gitlab.com/ci/jobs/job_control/)

---

## Task 6 - Scheduled Triggers

1. Create a scheduled Gitlab Pipeline that runs every 5 minutes.
   - Hint: Go to **Build -> Pipeline schedules** in your GitLab project to setup the pipeline.
   - Hint: [Cron Job Syntax](https://linuxize.com/post/cron-jobs-every-5-10-15-minutes/)
   - Observe that scheduled pipeline runs appear automatically.

---
