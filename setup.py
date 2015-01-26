from setuptools import find_packages, setup

setup(
    name="termtrack",
    version="0.1.0",
    description="Track Earth-orbiting satellites from your terminal",
    author="Torsten Rehn",
    author_email="torsten@rehn.email",
    license="GPLv3",
    url="https://github.com/trehn/termtrack",
    keywords=["terminal", "track", "tracking", "satellite", "orbit", "iss"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    package_data={
        "termtrack": [
            "data/ne_110m_land.dbf",
            "data/ne_110m_land.shp",
            "data/ne_110m_land.shx",
        ],
    },
    install_requires=[
        "click >= 2.0",
        "pyephem >= 3.7.5.0",
        "pyshp >= 1.2.1",
    ],
    py_modules=['termtrack'],
    entry_points={
        'console_scripts': [
            "termtrack=termtrack.cli:main",
        ],
    },
)