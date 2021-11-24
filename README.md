# edgescan  

[![](https://img.shields.io/pypi/pyversions/edgescan)](https://pypi.org/project/edgescan/) [![](https://img.shields.io/pypi/wheel/edgescan)](https://pypi.org/project/edgescan/#files) [![](https://img.shields.io/pypi/l/edgescan)](https://github.com/whitfieldsdad/edgescan/blob/main/LICENSE.md)

---

`edgescan` is a client for [EdgeScan's](https://www.edgescan.com/) [REST API](https://s3-eu-west-1.amazonaws.com/live-cdn-content/docs/api-guide-latest.pdf) that allows you to:

- Query and count assets, hosts, vulnerabilities, and licenses via the command line or programmatically.

## Installation

To install `edgescan` using `pip`:

```shell
$ pip install edgescan
```

To install `edgescan` from source (requires [`poetry`](https://github.com/python-poetry/poetry)):

```shell
$ git clone git@github.com:whitfieldsdad/edgescan.git
$ cd edgescan
$ make install
```

To install `edgescan` from source using `setup.py` (i.e. if you're not using `poetry`):

```shell
$ git clone git@github.com:whitfieldsdad/edgescan.git
$ cd edgescan
$ python3 setup.py install
```

## Environment variables

|Name              |Default value      |Required|
|------------------|-------------------|--------|
|`EDGESCAN_API_KEY`|                   |true    |
|`EDGESCAN_HOST`   |`live.edgescan.com`|false   |

## Testing

You can run the unit tests and integration tests for this package as follows:

```shell
$ make test
```

## Tutorials

### Command-line interface

After installing `edgescan` you can access the command-line interface as follows:

If you're using `poetry`:

```shell
$ poetry run edgescan
Usage: edgescan [OPTIONS] COMMAND [ARGS]...

Options:
  --host TEXT     ${EDGESCAN_HOST} ✖
  --api-key TEXT  ${EDGESCAN_API_KEY} ✔
  --help

Commands:
  assets           Query or count assets.
  hosts            Query or count hosts.
  licenses         Query or count licenses.
  vulnerabilities  Query or count vulnerabilities.
```

If you're not using `poetry`:

```shell
$ python3 -m edgescan.cli
```

#### Assets

The following options are available when working with assets:

```shell
$ poetry run edgescan assets --help
Usage: edgescan assets [OPTIONS] COMMAND [ARGS]...

  Query or count assets.

Options:
  --help

Commands:
  count-assets
  get-asset
  get-asset-tags
  get-assets
```

##### List assets

The following options are available when listing assets:

```shell
$ poetry run edgescan assets get-assets --help
Usage: edgescan assets get-assets [OPTIONS]

Options:
  --ids TEXT
  --names TEXT
  --tags TEXT
  --limit INTEGER
  --help
```

#### Hosts

The following options are available when working with hosts:

```shell
$ poetry run edgescan hosts --help
Usage: edgescan hosts [OPTIONS] COMMAND [ARGS]...

  Query or count hosts.

Options:
  --help

Commands:
  count-hosts
  get-host
  get-hosts
```

##### List hosts

The following options are available when listing hosts:

```shell
$ poetry run edgescan hosts get-hosts --help
Usage: edgescan hosts get-hosts [OPTIONS]

Options:
  --ids TEXT
  --hostnames TEXT
  --asset-ids TEXT
  --asset-tags TEXT
  --ip-addresses TEXT
  --os-types TEXT
  --os-versions TEXT
  --alive / --dead
  --limit INTEGER
  --help
```

#### Licenses

The following options are available when working with licenses:

```shell
$ poetry run edgescan licenses --help
Usage: edgescan licenses [OPTIONS] COMMAND [ARGS]...

  Query or count licenses.

Options:
  --help

Commands:
  count-licenses
  get-license
  get-licenses
```

##### List licenses

The following options are available when listing licenses:

```shell
$ poetry run edgescan licenses get-licenses --help
Usage: edgescan licenses get-licenses [OPTIONS]

Options:
  --ids TEXT
  --names TEXT
  --expired / --not-expired
  --limit INTEGER
  --help
```

#### Vulnerabilities

The following options are available when working with vulnerabilities:

```shell
$ poetry run edgescan vulnerabilities --help
Usage: edgescan vulnerabilities [OPTIONS] COMMAND
                                [ARGS]...

  Query or count vulnerabilities.

Options:
  --help

Commands:
  count-vulnerabilities
  get-vulnerabilities
  get-vulnerability
```

##### List vulnerabilities

The following options are available when listing vulnerabilities:

```shell
$ poetry run edgescan vulnerabilities get-vulnerabilities --help
Usage: edgescan vulnerabilities get-vulnerabilities 
           [OPTIONS]

Options:
  --ids TEXT
  --names TEXT
  --cve-ids TEXT
  --asset-ids TEXT
  --asset-tags TEXT
  --ip-addresses TEXT
  --affects-pci-compliance / --does-not-affect-pci-compliance
  --include-application-layer-vulnerabilities / --exclude-application-layer-vulnerabilities
  --include-network-layer-vulnerabilities / --exclude-network-layer-vulnerabilities
  --limit INTEGER
  --help
```
