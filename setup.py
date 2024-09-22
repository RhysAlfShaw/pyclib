import os
import subprocess
from setuptools import setup, find_packages, Command
from setuptools.command.build_py import build_py


class MakeCommand(Command):
    description = "Run make command to compile C library"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.check_call(["make"], cwd="pyclib")


class CustomBuildCommand(build_py):
    def run(self):
        self.run_command("make")
        build_py.run(self)


setup(
    name="pyclib",
    version="0.0",
    author="Rhys Shaw",
    author_email="rhysalfshaw@gmail.com",
    description="Python wrapper for a custom C library",
    packages=["pyclib"],
    include_package_data=True,
    cmdclass={
        "make": MakeCommand,
        "build_py": CustomBuildCommand,
    },
    package_data={
        "pyclib": ["bin/*", "lib/*"],
    },
    install_requires=["numpy"],
    python_requires=">=3.10",
)
