# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField

from pants.contrib.cpp.targets.cpp_target import CppTarget


class CppBinary(CppTarget):
    """A C++ binary."""

    def __init__(self, libraries=None, payload=None, **kwargs):
        """
        :param libraries: Libraries that this target depends on that are not pants targets.
        For example, 'm' or 'rt' that are expected to be installed on the local system.
        :type libraries: List of libraries to link against.
        """
        payload = payload or Payload()
        payload.add_field("libraries", PrimitiveField(libraries))
        super().__init__(payload=payload, **kwargs)

    @property
    def libraries(self):
        return self.payload.get_field_value("libraries")
