from setuptools import setup,find_packages

setup(name="seguia",
	version="0.0.1",
	description="A Python client for Oasis",
	packages=['seguia'],
	author = 'Christophe Philemotte',
	author_email = 'christophe.philemotte@euranova.eu',
	url = 'https://github.com/toch/seguia',
	test_suite="tests",
	install_requires=["requests==2.18.4"],
  setup_requires=['pytest-runner'],
  tests_require=['pytest', 'pytest-cov', 'requests_mock'],
  )
