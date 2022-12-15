#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mesh-announce',
	version='1.0',
	# Modules to import from other scripts:
	packages=(find_packages(),
	#)+["announce", "config", "domain", "metasocketserver", "util"]),
	include_package_data=True,
	# Executables
	scripts=["announce.py", "respondd.py"],
)
