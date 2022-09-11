#!/usr/bin/env python3

# BoBoBo

import os
from boon.protocol.context import _build_context


def test_build_context():
    context = _build_context(os.path.dirname(__file__) + '/conf.yaml',
                             'test-app')
    assert 'conf' in context and 'log' in context['conf']
