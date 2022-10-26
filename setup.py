# -*- coding: utf-8 -*-
# @Author : Junhui Yu
# @File : setup.py
# @Time : 2022/10/25 15:44

from setuptools import setup, find_packages
from setuptools.command.install import install
import shutil
from pathlib import Path

PACKAGE_NAME = "timeparser"
ALL_PROGRAM_ENTRIES = ['task_dispatcher = backend.task_master:main']
version = '1.0'

install_requires = []
try:
    import json
except ImportError:
    try:
        import simplejson
    except ImportError:
        install_requires.append('simplejson')


class CustomInstallCommand(install):
    """Customized setuptools install command """

    def run(self):
        install.run(self)
        self.run_after_install()

    def run_after_install(self):
        pass


def main():
    setup(
        name=PACKAGE_NAME,
        version=version,
        author="Junhui Yu",
        author_email="Junhuy@163.com",
        description=("Timing Parsering"),
        license="https://github.com/yujunhuics/timeparser",
        packages=find_packages(),
        include_package_data=True,
        install_requires=install_requires,
        cmdclass={
            'install': CustomInstallCommand,
        },
        entry_points={
            'console_scripts': ALL_PROGRAM_ENTRIES}
    )


if __name__ == "__main__":
    main()

    stale_egg_info = Path(__file__).parent / "timeparser.egg-info"
    build_info = Path(__file__).parent / "build"
    dist_info = Path(__file__).parent / "dist"
    if stale_egg_info.exists():
        shutil.rmtree(stale_egg_info)

    if build_info.exists():
        shutil.rmtree(build_info)

    if dist_info.exists():
        shutil.rmtree(dist_info)
