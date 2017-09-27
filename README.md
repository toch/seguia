# Seguia 🏞

Seguia is a Python client for [Oasis](https://github.com/toch/oasis).

[![Build Status](https://travis-ci.org/toch/seguia.svg?branch=master)](https://travis-ci.org/toch/seguia)
[![Coverage Status](https://coveralls.io/repos/github/toch/seguia/badge.svg?branch=master)](https://coveralls.io/github/toch/seguia?branch=master)
[![Dependency Status](https://gemnasium.com/badges/github.com/toch/seguia.svg)](https://gemnasium.com/github.com/toch/seguia)
[![version](https://img.shields.io/badge/version-unreleased-blue.svg)](./CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)

## Installation

```Bash
pip install git+https://github.com/toch/seguia
```

## Usage

```Python
from seguia.client import Client

client = Client(hostname='https://example.com')

json = client.index({'format': 'csv'})
client.upload(json['id'], 'example.csv')

json = client.search(format='csv')
client.download(json[0]['id'], 'myfile.csv')
```

## Run the tests

```Bash
python setup.py test
```

## License

This project is licensed under the terms of the MIT license.
