## Hands-On Exercises: Advanced Pipelines

### Learning Objectives

By the end of this section, you will:
- Understand the difference between `rules:` and `only:/except:`
- Use `needs:` to control job dependencies and enable parallel execution
- Create parent-child pipelines
- Reuse logic across repositories using `include:`
- Build a central pipeline setup using CI/CD components
- Configure a basic matrix or multi-project pipeline

---

## Task 1 — Use needs: for Parallel Jobs and Optimized Execution


1. Manually start a pipeline on the `main` branch by clicking on `New pipeline` on the [Pipelines](http://localhost:8000/hands-on/06_advanced_pipelines/task_01/-/pipelines) page.
   - Click on the `running` Icon of the started pipeline.
   - Observe that the pipeline jobs may only start once the previous pipeline stage is done.
2. Use the `needs` keyword to enable out-of-order execution of jobs in different stages.
   - hint: [Needs](https://docs.gitlab.com/ci/yaml/needs/)
   - Optimize the execution time of the pipeline in this project using the keyword `needs`.
   - Each component has to be built before testing and tested before deploying.
   - Observe the out-of-order execution of your pipeline by clicking on the `running` Icon of the optimized pipeline.

---

## Task 2 - Define a Child Pipeline

1. Create a file named `child-pipeline.yml` in the project and add a simple dummy job to the pipeline.

2. Trigger the `child-pipeline.yml` in the `.gitlab-ci.yml`.
    - Documentation: [Downstream pipelines](https://docs.gitlab.com/ci/pipelines/downstream_pipelines/)

---

## Task 3 - Create and Use a Pipeline Template

1. Create a template called `.gitlab-ci-linting.yml`.

2. Include the template in your main `.gitlab-ci.yml` file.
    - Documentation: [Use CI/CD Configuration from other files](https://docs.gitlab.com/ci/yaml/includes/)

3. Add a parameter to the template and pass this parameter from the main pipeline.

---

## Task 4 - Create a centralized Pipeline Template

Similarly to templates within a GitLab repository, the templates may be used cross-repository. This allows central management of pipelines with minimal effort. To implement this, GitLab version 17.0 introduced [CI/CD Components](https://docs.gitlab.com/ci/components/).

1. Create a pipeline component called `gitlab-ci-linting.yml` in the component repository.

2. Use the component in the main `.gitlab-ci.yml` file in your repository.

---

## Task 5 - Create a Simple Matrix Pipeline

1. Create a matrix pipeline which executes a job in parallel for multiple parameters.
    - Documentation: [Matrix pipelines](https://docs.gitlab.com/ci/yaml/#needsparallelmatrix)

---
