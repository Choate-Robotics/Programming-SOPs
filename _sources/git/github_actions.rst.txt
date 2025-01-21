.. _github-actions-setup:

=====================================
Setting Up GitHub Actions for Testing
=====================================

This guide will walk you through setting up GitHub Actions for your FRC robotics programming team to automate code testing.

Overview
========
GitHub Actions allows you to define workflows that run automated processes, such as testing your code, whenever certain events occur in your repository. By setting up a workflow file, you can ensure your team’s code is tested automatically with every push or pull request.

Example code from 2025
======================

.. code-block:: yaml

    name: Tests

on:
  push:
  pull_request:
    branches: [master]

jobs:
  test:
    timeout-minutes: 5
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
        with:
          fetch-depth: 1

      - name: Set up Python 3.12
        uses: actions/setup-python@v1
        with:
          python-version: 3.12


      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python3 -m pip install robotpy==2025.2.1.0
          python3 -m robotpy sync


      - name: Run robotpy Tests
        run: |
          python3 -m robotpy test
Explanation of Workflow
========================
Below is an explanation of each line in your current test YAML file:

.. code-block:: yaml

    name: Tests

**Explanation:** Sets the name of the workflow as "Tests." This will appear in the Actions tab on GitHub.

    on:
      push:
      pull_request:
        branches: [master]

**Explanation:** Specifies the events that trigger this workflow. It runs on every push and pull request to the `master` branch.

    jobs:
      test:
        timeout-minutes: 5
        runs-on: ubuntu-latest

**Explanation:**
- `jobs:` Defines a job named `test`.
- `timeout-minutes: 5` Limits the job's execution time to 5 minutes to prevent long-running tests.
- `runs-on: ubuntu-latest` Specifies that the job will run on the latest Ubuntu runner provided by GitHub.

    steps:
      - uses: actions/checkout@v1
        with:
          fetch-depth: 1

**Explanation:**
- `uses: actions/checkout@v1`: Utilizes the `checkout` action to clone the repository into the runner.
- `with:` Provides configuration options for the `checkout` action.
- `fetch-depth: 1`: Specifies to fetch only the latest commit, reducing the amount of data transferred.

      - name: Set up Python 3.12
        uses: actions/setup-python@v1
        with:
          python-version: 3.12

**Explanation:**
- `name: Set up Python 3.12`: Names the step for clarity.
- `uses: actions/setup-python@v1`: Utilizes the `setup-python` action to install and configure Python.
- `with:` Provides options for this action.
- `python-version: 3.12`: Specifies Python version 3.12 to be set up in the environment.

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python3 -m pip install robotpy==2025.2.1.0
          python3 -m robotpy sync

**Explanation:**
- `name: Install dependencies`: Names the step for clarity.
- `run:` Executes the following commands in the runner's shell:
  - `python -m pip install --upgrade pip`: Updates pip to the latest version.
  - `python3 -m pip install robotpy==2025.2.1.0`: Installs a specific version of the `robotpy` library.
  - `python3 -m robotpy sync`: Synchronizes dependencies for the `robotpy` library.

      - name:Run robotpy Tests
        run: |
          python3 -m robotpy test

**Explanation:**
- `name:`: The name is `Run robotpy Tests` which indicates this is where the robotpy code is tested.
- `run: python3 -m robotpy test`: Runs the test suite for `robotpy` using Python 3.

Steps to Set Up GitHub Actions
==============================

1. **Create a Workflow Directory**

   In your repository, create a directory named ``.github/workflows`` if it doesn’t already exist.

   .. code-block:: bash

      mkdir -p .github/workflows

2. **Create a Workflow File**

   Inside the ``.github/workflows`` directory, create a YAML file. For example, ``test.yml``.

   .. code-block:: bash

      touch .github/workflows/test.yml

3. **Define the Workflow**

   Open the ``test.yml`` file in your editor and define the workflow based on the explained YAML file above.

4. **Commit the Workflow File**

   Add the workflow file to your repository and commit the changes:

   .. code-block:: bash

      git add .github/workflows/test.yml
      git commit -m "Add GitHub Actions workflow for testing"
      git push origin main

5. **Verify the Workflow**

   Push a change to your repository or open a pull request. Navigate to the **Actions** tab in your GitHub repository to see the workflow running. Ensure all tests pass successfully.

Troubleshooting
===============
- **Dependency Issues**: Check your ``pyproject.toml`` file to ensure all necessary dependencies are listed.
- **Failed Tests**: Review the output in the Actions tab to identify which tests failed and why.
- **Workflow Errors**: Validate your YAML file using an online tool like `YAML Lint <https://www.yamllint.com/>`_.

Advanced Topics
===============
- **Matrix Testing**: Run tests across multiple Python versions or environments by using a matrix strategy.
- **Cache Dependencies**: Use caching to speed up subsequent runs.

   Example:

   .. code-block:: yaml

      - name: Cache pip
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip

By following these steps, your FRC robotics programming team can ensure a smooth and automated process for testing code changes. This will help maintain code quality and streamline development workflows.
