from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in meetings/__init__.py
from meetings import __version__ as version

setup(
	name="meetings",
	version=version,
	description="Control de reuniones y seguimiento de acuerdos",
	author="Buzola",
	author_email="it@buzola.mx",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
