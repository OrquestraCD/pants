# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

page(
  name='readme',
  sources=['README.md'],
)

python_library(
  name='parsers',
  sources=['parsers.py'],
  dependencies=[
    'src/python/pants/build_graph',
    'src/python/pants/engine:objects',
    'src/python/pants/engine:parser',
    'src/python/pants/util:memo',
  ],
  tags = {'partially_type_checked'},
)

resources(
  name='fs_test',
  # Note that this test data dir is bundled into a tarfile, to preserve symlink structure
  # when copied into a chroot.
  sources=['fs_test/**/*'],
)

resources(
  name='graph_test',
  sources=['graph_test/**/*'],
)

resources(
  name='mapper_test',
  sources=['mapper_test/**/*'],
)

resources(
  name='scheduler_inputs',
  sources=['scheduler_inputs/**/*'],
)
