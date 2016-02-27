#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import

import slacker

import exception_slacker

import os
from mock import patch
from unittest import TestCase
from nose.tools import raises

class SlackerNotificationTestCase(TestCase):
    @raises(StandardError)
    def test_not_configured(self):
        raise RuntimeError("ERROR")

    @patch('slacker.Slacker')
    @raises(RuntimeError)
    def test_configured(self, mock_slacker):
        os.environ['EXCEPTION_SLACKER_TOKEN'] = "XXXXXXXXXX"
        os.environ['EXCEPTION_SLACKER_CHANNEL'] = "#notification-test"
        os.environ['EXCEPTION_SLACKER_NAME'] = "Exception Notifier"

        raise RuntimeError("ERROR")

        mock_slacker.assert_called_with(os.environ['EXCEPTION_SLACKER_TOKEN'])

