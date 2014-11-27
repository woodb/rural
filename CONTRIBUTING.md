# Contribution Guidelines

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome.

[GitHub "issues" tab](https://github.com/woodb/rural/issues)

## Bug Reports

  - Please include a short, self-contained Python snippet reproducing the problem.
  - Explain what the expected behavior was, and what you saw instead.

## Pull Requests

  - Use [proper commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html):
    - a subject line with `< 80` chars.
    - One blank line.
    - Optionally, a commit message body.
  - Please reference relevant Github issues in your commit message using `GH1234`
    or `#1234`. Either style is fine but the '#' style generates noise when you
    rebase your PR.
  - Keep style fixes to a separate commit to make your PR more readable.
  - An informal commit message format is in effect for the project. Please try
    and adhere to it. Check `git log` for examples. Here are some common prefixes
    along with general guidelines for when to use them:
      - **ENH**: Enhancement, new functionality
      - **BUG**: Bug fix
      - **DOC**: Additions/updates to documentation
      - **TST**: Additions/updates to tests
      - **BLD**: Updates to the build process/scripts
      - **PERF**: Performance improvement
      - **CLN**: Code cleanup
  - Docstrings follow the [numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) format.
  - Write tests.
  - When writing tests, use 2.6 compatible `self.assertFoo` methods. Some polyfills such as `assertRaises`
    can be found in `pandas.util.testing`.
  - Do not attach doctrings to tests. Make the test itself readable and use
    comments if needed.
  - When you start working on a PR, start by creating a new branch pointing at the latest
    commit on github master.
  - **Do not** merge upstream into a branch you're going to submit as a PR.
    Use `git rebase` against the current github master.
  - For extra brownie points, you can squash and reorder the commits in your PR
    using `git rebase -i`. Use your own judgment to decide what history needs
    to be preserved. If git frightens you, that's OK too.
  - Use `raise AssertionError` over `assert` unless you want the assertion
    stripped by `python -o`.
  - On the subject of [PEP8](http://www.python.org/dev/peps/pep-0008/): yes.
  - On the subject of a massive PEP8-storm touching everything: not too often
    (once per release works).
