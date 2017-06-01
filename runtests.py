#! /usr/bin/env python
# This script is taken from Django Rest Framework
# (https://github.com/tomchristie/django-rest-framework/blob/master/runtests.py)
from __future__ import print_function

import os
import subprocess
import sys


def runtests():
    import django

    from django.conf import settings
    from django.test.utils import get_runner

    os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.test_settings"
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["aa_intercom.tests"])
    sys.exit(bool(failures))


FLAKE8_ARGS = ["aa_intercom", "tests", "test_project", "--ignore=E501"]

sys.path.append(os.path.dirname(__file__))


def exit_on_failure(ret, message=None):
    if ret:
        sys.exit(ret)


def tests_main():
    print("Running tests")
    ret = subprocess.call(["coverage", "run", "-a", "--omit=aa_intercom/tests/*",
                           "--source=aa_intercom", "setup.py", "test"])
    print("tests failed" if ret else "tests passed")
    return ret


def flake8_main(args):
    print("Running flake8 code linting")
    ret = subprocess.call(["flake8"] + args)
    print("flake8 failed" if ret else "flake8 passed")
    return ret


def isort_main():
    print("Running isort code checking")
    ret = subprocess.call(["sh", "run_isort", "--check-only"])

    if ret:
        print("isort failed: Some modules have incorrectly ordered imports. Fix by running `isort --recursive .`")
    else:
        print("isort passed")

    return ret


def split_class_and_function(string):
    class_string, function_string = string.split(".", 1)
    return "{} and {}".format(class_string, function_string)


def is_function(string):
    # `True` if it looks like a test function is included in the string.
    return string.startswith("test_") or ".test_" in string


def is_class(string):
    # `True` if first character is uppercase - assume it"s a class name.
    return string[0] == string[0].upper()


if __name__ == "__main__":
    """ test runner - to be used by tox """
    try:
        sys.argv.remove("--nolint")
    except ValueError:
        run_flake8 = True
        run_isort = True
    else:
        run_flake8 = False
        run_isort = False

    try:
        sys.argv.remove("--lintonly")
    except ValueError:
        run_tests = True
    else:
        run_tests = False

    try:
        sys.argv.remove("--fast")
    except ValueError:
        style = "default"
    else:
        style = "fast"
        run_flake8 = False
        run_isort = False

    if run_tests:
        exit_on_failure(tests_main())

    if run_flake8:
        exit_on_failure(flake8_main(FLAKE8_ARGS))

    if run_isort:
        exit_on_failure(isort_main())
