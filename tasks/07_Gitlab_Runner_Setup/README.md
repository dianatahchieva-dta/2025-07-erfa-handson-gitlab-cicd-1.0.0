# Hands-On Exercises: GitLab Runner Setup

## Learning Objectives

By the end of this section, you will:
- Understand what GitLab Runners are and how they work
- Compare `shell` and `docker` executors
- Know when to use **shared** vs **specific** runners
- Be aware of runner job selection using tags and configurations
- Set up a GitLab Runner with a `docker` executors and test it

---

## Task 0 - GitLab Runner Executors

1. Read the [official documentation](https://docs.gitlab.com/runner/executors/) on the different kinds of GitLab Runner Executors.

2. Read the section [who has access to runners in the GitLab UI](https://docs.gitlab.com/runner/#who-has-access-to-runners-in-the-gitlab-ui) to find out about the different runner types.

---

## Task 1 - Register a GitLab Runner without tags using docker Executor

1. Register a GitLab Runner with `docker` executor without specifying any tags.
   - Documentation: [Registering runners](https://docs.gitlab.com/runner/register/)
   - Hint: You can register a Gitlab Runner for this project under Settings -> CI/CD -> Runners.
   - Hint: You can create a `docker-compose.yml` to create the Gitlab Runner container with the image `gitlab/gitlab-runner:latest`.
   - Hint: The additional container should have the docker socket mounted to enable containerized executions.
   - Hint: The Gitlab Runner should be on the same network as the Gitlab container.
   - Hint: To register a runner which works in the containerized Lab Setup run the following command: ```docker exec -it <container-name> gitlab-runner register --docker-network-mode lab_setup_gitlab-net --clone-url http://gitlab:8000```
   - Hint: Since we are using the docker network the Gitlab URL is `http://gitlab:8000` instead of `http://localhost:8000`.
   - Once you registered a runner, run the dummy job on the GitLab Runner.
   - What happens when you add a tag (e.g. `handson-erfa`) to the dummy job. Will it still execute? [Use tags](https://docs.gitlab.com/ci/runners/configure_runners/#use-tags-to-run-jobs-on-different-platforms)

---

## Task 2 - Register a GitLab Runner with tags (e.g. `handson-erfa`) using docker Executor

1. Register a Project GitLab Runner with `docker` executor which executes jobs with a certain tag (e.g., `handson-erfa`).
   - Does the runner pick up the job in the dummy pipeline without any tag?
   - Add the `handson-erfa` to the `dummy-job` and observe the behaviour.
   - Deploy a second runner with `handson-erfa` tags. Which runner will pick up the job if there are multiple capable of executing the job?
   - Documentation: [Registering runners](https://docs.gitlab.com/runner/register/)

---
