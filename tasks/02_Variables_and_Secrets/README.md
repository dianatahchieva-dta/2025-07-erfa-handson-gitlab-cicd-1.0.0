## Hands-On Exercises: CI/CD Variables & Secrets

### Learning Objectives
By the end of this session you will:
- Know how to define variables in GitLab UI or in `.gitlab-ci.yml`.
- Configure *masked* and *protected* variables.
- Access common `CI_*` predefined variables in scripts.
- Scope variables to branches, tags, or environments.
- Store an API key as a secret and use it inside the pipeline securely.

---

## Task 1 — Define and Mask an API Key

1. Go to your project’s **Settings → CI/CD → Variables**.
2. Create two variables `API_ENDPOINT` and `API_KEY` with some arbitrary values.
    - Check **Mask variable** and **Protect variable** for the `API_KEY`.
3. Print the two variables to the pipeline output and observe the behavior.

---

## Task 2 - Explore Predefined Variables

1. Explore the predefined Gitlab CI/CD Variables [here](https://docs.gitlab.com/ci/variables/predefined_variables/).

2. Print some of the predefined Gitlab CI/CD Variables in a pipeline and observe its values.

---

## Task 3 - Scoped Variables by Environment

1. In **Operate -> Environments**, create the environments `staging` and `production`. (Environments are case sensitive!)

2. In **Settings -> CI/CD -> Variables**, add a new variable `DEPLOY_ENV`.

3. Under **Environment scope**, set one value for `production` and a different value for `staging`.

4. Adjust your pipeline to run a job in the `production` environment and observe the output when printing the `DEPLOY_ENV` variable.
   - Change the environment to `staging` and observe the output again.

---
