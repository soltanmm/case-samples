import os
import os.path

import setuptools

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import commands

_PACKAGES = setuptools.find_packages('.')

_PACKAGE_DIRECTORIES = {
    '': '.',
}

_PACKAGE_DATA = {}

_SETUP_REQUIRES = (
    'pytest>=2.6',
    'pytest-cov>=2.0',
    'pytest-xdist>=1.11',
    'pytest-timeout>=0.5',
)

_INSTALL_REQUIRES = ()

_COMMAND_CLASS = {
    'test': commands.RunTests
}

setuptools.setup(
    name='example',
    version='0.1.0',
    packages=_PACKAGES,
    package_dir=_PACKAGE_DIRECTORIES,
    package_data=_PACKAGE_DATA,
    install_requires=_INSTALL_REQUIRES + _SETUP_REQUIRES,
    setup_requires=_SETUP_REQUIRES,
    cmdclass=_COMMAND_CLASS,
)
