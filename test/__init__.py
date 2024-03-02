"""Initialization of tests for encrypted_config package."""

import logging

import boilerplates.logging


class TestsLogging(boilerplates.logging.Logging):
    """Test logging configuration."""

    packages = ['encrypted_config']


TestsLogging.configure()
