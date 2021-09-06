<!--Power by https://github.com/pallets/flask/blob/main/CONTRIBUTING.rst-->

# CONTRIBUTING

Reporting issues
----------------

Include the following information in your post:

* Describe what you expected to happen.
* If possible, include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) to help us
    identify the issue. This also helps check that the issue is not with
    your own code.

* Describe what actually happened. Include the full traceback if there
    was an exception.

* List your Python and Sansorchi versions. If possible, check if this
    issue is already fixed in the latest releases or the latest code in
    the repository.

Submitting patches
----------------

If there is not an open issue for what you want to submit, prefer
opening one for discussion before working on a PR. You can work on any
issue that doesn't have an open PR linked to it or a maintainer assigned
to it. These show up in the sidebar. No need to ask if you can work on
an issue that interests you.

Include the following in your patch:

* Use [Black](https://black.readthedocs.io) to format your code. This and other tools will run automatically if you install [pre-commit](https://pre-commit.com) using the instructions below.
* Include tests if your patch adds or changes code. Make sure the test fails without your patch.

First time setup
----------------

* Download and install the [latest version of git](https://git-scm.com/downloads).
* Configure git with your [username](https://docs.github.com/en/github/using-git/setting-your-username-in-git) and [email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address).

```
git config --global user.name 'your name'
git config --global user.email 'your email'
```

* Make sure you have a [GitHub account](https://github.com/join).
* Fork Flask to your GitHub account by clicking the [Fork](https://github.com/komeilparseh/Sansorchi/fork) button.

* `Clone` the main repository locally.

```
git clone https://github.com/komeilparseh/Sansorchi
cd Sansorchi
```

* Add your fork as a remote to push your work to. Replace `{username}` with your username. This names the remote "fork", the

default Pallets remote is "origin".

```
git remote add fork https://github.com/{username}/Sansorchi
```

* Create a virtualenv.

**Linux/Macos**

```
python3 -m venv env
env/bin/activate
```

**Windowns**

```
py -3 -m venv env
env\Scripts\activate
```

* Upgrade pip and setuptools.

```
python -m pip install --upgrade pip setuptools
```

* Install the development dependencies, then install Flask in editable mode.

```
pip install -r requirements/dev.txt && pip install -e .
```

* Install the pre-commit hooks.

```
pre-commit install
```

Start coding
----------------

* Create a branch to identify the issue you would like to work on. If you're submitting a bug or branch off of the latest ".x" branch.

```
git fetch origin
git checkout -b your-branch-name origin/2.0.x
```

If you're submitting a feature addition or change, branch off of the"main" branch.

```
git fetch origin
git checkout -b your-branch-name origin/main
```

* Using your favorite editor, make your changes, committing as you go.

* Include tests that cover any code changes you make. Make sure the
    test fails without your patch. Run the tests as described below.

* Push your commits to your fork on GitHub and [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) Link to the issue being addressed with `fixes #123 ` in the pull request.

```
git push --set-upstream fork your-branch-name
```

Running the tests
----------------

Run the basic test suite with pytest.

```
pytest test/test.py
```

This runs the tests for the current environment, which is usually
sufficient. CI will run the full suite when you submit your pull
request. You can run the full test suite with tox if you don't want to
wait.

```
tox
```

Running test coverage
----------------

Generating a report of lines that do not have test coverage can indicate
where to start contributing. Run `pytest` using `coverage` and
generate a report.

```
pip install coverage
coverage run -m pytest test/test.py
```

Read more about `coverage <https://coverage.readthedocs.io>`
