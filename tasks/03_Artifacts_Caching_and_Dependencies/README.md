## Hands-On Exercises: Artifacts, Caching, & Dependencies

### Learning Objectives
By the end of this session you will:
- Configure `artifacts` to share files between stages
- Add a JUnit test report to your pipeline and view it in GitLab
- Implement `cache` for faster builds
- Be aware of GitLab's built-in support for other report types (e.g. security scans)

---

## Task 1 — Save Build Outputs as Artifacts

1. Add a `build_job` that writes output to a file.

2. Add a `test_job` that depends on the `build_job` and prints this artifact.
    - Hint: You can use `echo "Dummy Content" > build_output.txt` to write a file.
    - Hint: You can use `cat build_output.txt` to read and print the file.

---

## Task 2 - Generate a Unit Test Report

1. Simulate a unit test suite and produce a JUnit report.
    - Hint: To generate a JUnit report you can use the following command:
        ```bash
        echo '<testsuite tests="1" failures="0"><testcase classname="example" name="example_test"/></testsuite>' > reports/junit.xml
        ```
    - Documentation: [Unit test reports](https://docs.gitlab.com/ci/testing/unit_test_reports/)

2. Upload the JUnit report from the previous step as a JUnit pipeline artifact.
    - Observe the **Test Tab** in the pipeline run to see the parsed JUnit report.

---

## Task 3 - Speed up Builds with a Cache

1. Modify the `build_job` to cache a dependency directory (e.g., `node_modules/`).
   - Hint: We recommend to use the `node:slim` container image for the job.
   - Hint: With the command `npm install` all the dependencies in the `package.json` will be installed in the `node_modules` directory.
   - Hint: [Gitlab Caching](https://docs.gitlab.com/ci/caching/)
   - Hint: The use of a caching key is optional.
   - Observe that the second pipeline reuses the cached directory for faster build times.

---
