# Copyright 2018 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

"""Thrift code generator for Android.

See https://github.com/microsoft/thrifty.
"""

from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.goal.task_registrar import TaskRegistrar as task

from pants.contrib.thrifty.java_thrifty_gen import JavaThriftyGen
from pants.contrib.thrifty.java_thrifty_library import JavaThriftyLibrary as JavaThriftyLibraryV1
from pants.contrib.thrifty.targets import JavaThriftyLibrary


def build_file_aliases():
    return BuildFileAliases(targets={"java_thrifty_library": JavaThriftyLibraryV1})


def register_goals():
    task(name="thrifty", action=JavaThriftyGen).install("gen")


def targets2():
    return [JavaThriftyLibrary]
