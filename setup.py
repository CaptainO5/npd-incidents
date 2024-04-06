from setuptools import setup, find_packages

setup(
	name='src',
	version='1.0',
	author='Suraj Kolla',
	author_email='n.kolla@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs', 'resources')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)