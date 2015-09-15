import os
import os.path
import sys

import setuptools


class RunTests(setuptools.Command):
  """Command to run all tests via py.test."""

  description = ''
  user_options = [('pytest-args=', 'a', 'arguments to pass to py.test')]

  def initialize_options(self):
    self.pytest_args = []

  def finalize_options(self):
    pass

  def run(self):
    # We import here to ensure that setup.py has had a chance to install the
    # relevant package eggs first.
    import pytest
    result = pytest.main(self.pytest_args)
    if result != 0:
      raise SystemExit(result)
