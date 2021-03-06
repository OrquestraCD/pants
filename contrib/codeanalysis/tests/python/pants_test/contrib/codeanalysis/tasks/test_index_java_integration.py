# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

import glob
import os

from pants.testutil.pants_run_integration_test import PantsRunIntegrationTest


class TestIndexJavaIntegration(PantsRunIntegrationTest):
    def test_index_simple_java_code(self):
        # Very simple test that we can run the extractor and indexer on some
        # fairly trivial code without crashing, and that we produce something.
        args = ["index", "examples/src/java/org/pantsbuild/example/hello::"]
        with self.temporary_workdir(cleanup=False) as workdir:
            pants_run = self.run_pants_with_workdir(args, workdir)
            self.assert_success(pants_run)
            for tgt in [
                "examples.src.java.org.pantsbuild.example.hello.greet.greet",
                "examples.src.java.org.pantsbuild.example.hello.main.main-bin",
                "examples.src.java.org.pantsbuild.example.hello.simple.simple",
            ]:
                kzip_glob = os.path.join(
                    workdir, f"index/kythe-java-extract/current/{tgt}/current/*.kzip"
                )
                kzip_files = glob.glob(kzip_glob)
                self.assertEqual(1, len(kzip_files))
                kzip_file = kzip_files[0]
                self.assertTrue(os.path.isfile(kzip_file))
                self.assertGreater(os.path.getsize(kzip_file), 200)  # Make sure it's not trivial.

                entries_path = os.path.join(
                    workdir, f"index/kythe-java-index/current/{tgt}/current/index.entries"
                )
                self.assertTrue(os.path.isfile(entries_path))
                self.assertGreater(
                    os.path.getsize(entries_path), 1000
                )  # Make sure it's not trivial.
