from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My Trading Indicators'
LONG_DESCRIPTION = 'A collection of my trading indicators'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="sm_indicators",
    version=VERSION,
    author="Mohamed Slimani",
    author_email="mohamed@slimani.dev",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'indicators', 'trading indicators'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Linux :: Ubuntu 2022.10",
    ]
)
