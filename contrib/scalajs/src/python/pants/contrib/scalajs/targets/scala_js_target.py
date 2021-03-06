# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).


from pants.backend.jvm.subsystems.jvm_platform import JvmPlatform
from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField, PrimitivesSetField

from pants.contrib.scalajs.subsystems.scala_js_platform import ScalaJSPlatform


class ScalaJSTarget:
    """A mixin for ScalaJS targets to injects scala-js deps and request ScalaJS compilation."""

    @classmethod
    def subsystems(cls):
        return super().subsystems() + (JvmPlatform, ScalaJSPlatform)

    def __init__(self, address=None, payload=None, **kwargs):
        self.address = address  # Set in case a TargetDefinitionException is thrown early
        payload = payload or Payload()
        payload.add_fields(
            {"platform": PrimitiveField(None), "compiler_option_sets": PrimitivesSetField(None)}
        )
        super().__init__(address=address, payload=payload, **kwargs)

    @classmethod
    def compute_dependency_address_specs(cls, kwargs=None, payload=None):
        for address_spec in super().compute_dependency_address_specs(kwargs, payload):
            yield address_spec
        for address_spec in ScalaJSPlatform.global_instance().injectables_address_specs_for_key(
            "runtime"
        ):
            yield address_spec

    @property
    def strict_deps(self):
        return False

    @property
    def fatal_warnings(self):
        return False

    @property
    def compiler_option_sets(self):
        """For every element in this list, enable the corresponding flags on compilation of targets.

        :return: See constructor.
        :rtype: list
        """
        return self.payload.compiler_option_sets

    @property
    def zinc_file_manager(self):
        return False

    @property
    def platform(self):
        return JvmPlatform.global_instance().get_platform_for_target(self)
