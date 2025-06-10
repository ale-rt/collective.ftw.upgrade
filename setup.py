from setuptools import find_packages
from setuptools import setup

import os


version = "3.3.2.dev0"

tests_require = [
    "ftw.testing >= 2.0.0.dev0",
    "ftw.testbrowser >= 2.1.0.dev0",
    "ftw.builder >= 2.0.0.dev0",
    "plone.testing",
    "plone.app.testing",
    "plone.app.intid",
    "plone.app.contenttypes",
    "zope.configuration",
    "zc.recipe.egg",
    "transaction",
    "Products.CMFPlacefulWorkflow",
]

extras_require = {
    "colors": ["blessed"],
    "tests": tests_require,
    "test_archetypes": ["Products.ATContentTypes"],
}

setup(
    name="ftw.upgrade",
    version=version,
    description="An upgrade control panel and upgrade " "helpers for plone upgrades.",
    long_description=open("README.rst").read()
    + "\n"
    + open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    keywords="plone ftw upgrade",
    author="4teamwork AG",
    author_email="mailto:info@4teamwork.ch",
    url="https://github.com/4teamwork/ftw.upgrade",
    license="GPL2",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["ftw"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.9",
    install_requires=[
        "argcomplete",
        "inflection",
        "path.py >= 6.2",
        "requests",
        "setuptools",
        "tarjan",
        "psutil",
        "AccessControl",
        "Acquisition",
        "transaction",
        "Products.BTreeFolder2",
        "Products.ZCatalog",
        "zope.component",
        "zope.interface",
        "zope.publisher",
        "Zope2",
        # Plone
        "Plone",
        "Products.GenericSetup",
        "plone.browserlayer",
        "Products.CMFCore",
        "Products.CMFPlone",
    ],
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        "z3c.autoinclude.plugin": ["target = plone"],
        "console_scripts": ["upgrade = ftw.upgrade.command:main"],
    },
)
