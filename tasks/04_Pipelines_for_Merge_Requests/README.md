## Hands-On Exercises - Pipelines for Merge Requests

### Learning Objectives

By the end of this section, you will:
- Understand how MR pipelines work (`only: [merge_requests]`, `rules`)
- Configure a pipeline that runs only when a merge request is created or updated
- Add a linter to validate code formatting
- Add a unit test stage and visualize test coverage in the MR

---

## Task 1 — Create a Basic MR Pipeline

1. Modify the `.gitlab-ci.yml` to run the linting stage only when a merge requests is created.
    - To test the execution, create a pull request for a feature branch.
    - Documentation: [Merge request pipelines](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/)


---

## Task 2 - Add Test Coverage with Visual Feedback to the Merge Request

1. Modify the `.gitlab-ci.yml` to run a test stage in a merge request. The stage should capture the test coverage.
    - Hint: To simulate coverage output, you can simply use a dummy output which is matched by the defined coverage regex pattern (e.g., a dummy coverage output could be simulated with `echo "TOTAL      123      456      789      84%"`).
    - Documentation: [Code coverage](https://docs.gitlab.com/ci/testing/code_coverage/)
    - Observe that the coverage percentage is directly displayed in the Merge Request widget.

---
