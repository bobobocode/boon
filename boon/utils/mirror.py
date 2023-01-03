#!/usr/bin/env python3

import os


def is_package(path):
    """
    Is the given path a Python package?
    """
    return os.path.isdir(path) and \
        os.path.exists(os.path.join(path, "__init__.py"))
