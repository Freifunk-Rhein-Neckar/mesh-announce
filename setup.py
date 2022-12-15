#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='mesh-announce',
	version='1.0',
	# Modules to import from other scripts:
	packages=(find_packages(
		where='/',
		include=['pkg*'],  # alternatively: `exclude=['additional*']`
	)+["announce.py", "config.py", "domain.py", "metasocketserver.py", "util.py"]),
	# Executables
	scripts=["announce.py", "respondd.py"],
)
