"""
    Runs bioio_base's benchmark function against the test resources in this repository
"""
import pathlib

import bioio_base.benchmark

import bioio_imageio


# This file is under /scripts while the test resourcess are under /bioio_imageio/tests/resources
test_resources_dir = pathlib.Path(__file__).parent.parent / "bioio_imageio" / "tests" / "resources"
assert test_resources_dir.exists(), f"Test resources directory {test_resources_dir} does not exist"
test_files = [
    test_file
    for test_file in test_resources_dir.iterdir()
    if not test_file.name in {"example_invalid_frame_count.mp4", "example.bmp", "example.txt"}
]
print(f"Test files: {[file.name for file in test_files]}")
bioio_base.benchmark.benchmark(bioio_imageio.reader.Reader, test_files)
