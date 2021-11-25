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

You can run the integration tests for this package as follows:

```shell
$ make test
```

> Note: the integration tests will only be run if the `EDGESCAN_API_KEY` environment variable has been set.

## Tutorials

### Command-line interface

- [Assets](#assets)
    - [List assets](#list-assets)
- [Hosts](#hosts)
    - [List hosts](#list-hosts)
- [Vulnerabilities](#vulnerabilities)
    - [List vulnerabilities](#list-vulnerabilities)
- [Licenses](#licenses)
    - [List licenses](#list-licenses)

#### Setup

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

### Development

- [Count assets by tag](#count-assets-by-tag)
- [Count hosts by asset tag](#count-hosts-by-asset-tag)
- [Count vulnerabilities by asset tag](#count-vulnerabilities-by-asset-tag)
- [Count hosts by OS type](#count-hosts-by-os-type)
- [Count hosts by OS version](#count-hosts-by-os-version)
- [Count hosts by asset group name](#count-hosts-by-asset-group-name)
- [Count vulnerabilities by asset group name](#count-vulnerabilities-by-asset-group-name)
- [Count vulnerabilities by location (i.e. by IP address or hostname)](#count-vulnerabilities-by-location-ie-by-ip-address-or-hostname)

#### Count assets by tag

Let's count the number of asset groups with a tag of "DMZ":

```python
from edgescan.api.client import EdgeScan

api = EdgeScan()
total = api.count_assets(tags=['DMZ'])
print(total)
```

```shell
1
```

#### Count hosts by asset tag

Let's count the number of hosts within any asset group with a tag of "DMZ":

```python
from edgescan.api.client import EdgeScan

api = EdgeScan()
total = api.count_hosts(asset_tags=['DMZ'])
print(total)
```

```shell
306
```

#### Count vulnerabilities by asset tag

Let's count the number of vulnerabilities present on any hosts within any asset group with an asset tag of "DMZ":

```python
from edgescan.api.client import EdgeScan

api = EdgeScan()
total = api.count_vulnerabilities(asset_tags=['DMZ'])
print(total)
```

```shell
1450
```

#### Count hosts by OS type

Here's an example of how to calculate the OS type distribution of all hosts:

```python
from edgescan.api.client import EdgeScan

import json
import collections

api = EdgeScan()

tally = collections.defaultdict(int)
for host in api.get_hosts():
    if host.os_type:
        tally[host.os_type] += 1

txt = json.dumps(tally, indent=4)
print(txt)
```

```shell
{
    "bsd": 168,
    "darwin": 7,
    "linux": 175,
    "other": 300,
    "solaris": 3,
    "windows": 50
}
```

#### Count hosts by OS version

Here's an example of how to calculate the OS version distribution of all Windows hosts:

```python
from edgescan.api.client import EdgeScan

import json
import collections

api = EdgeScan()

tally = collections.defaultdict(int)
for host in api.get_hosts(os_types=["windows"]):
    if host.os_version:
        tally[host.os_version] += 1

txt = json.dumps(tally, indent=4)
print(txt)
```

```shell
{
    "Microsoft Windows 2008": 9,
    "Microsoft Windows 2012": 15,
    "Microsoft Windows 2016": 5,
    "Microsoft Windows 7": 11,
    "Microsoft Windows Phone": 3,
    "Microsoft Windows Vista": 7
}
```

#### Count hosts by asset group name

Here's an example of how to calculate how many hosts are associated with each asset group:

```python
from edgescan.api.client import EdgeScan

import json

api = EdgeScan()

tally = {}
for asset in api.get_assets():
    tally[asset.name] = asset.host_count

txt = json.dumps(tally, indent=4)
print(txt)
```

```shell
{
    "External IP Monitoring 66.249.64.0 – 66.249.95.255": 62,
    "External IP Monitoring 72.14.192.0 – 72.14.255.255": 57,
    "104.154.0.0/15": 34,
    "64.233.160.0/19": 23,
    "66.102.0.0/20": 13,
    "208.117.224.0/19": 56
}
```

#### Count vulnerabilities by asset group name

Here's an example of how to calculate how many vulnerabilities are associated with hosts within each asset group:

```python
from edgescan.api.client import EdgeScan

import collections
import json

api = EdgeScan()

#: Count vulnerabilities by `asset.id`.
vulnerabilities_by_asset_id = collections.defaultdict(int)
for vulnerability in api.get_vulnerabilities():
    vulnerabilities_by_asset_id[vulnerability.asset_id] += 1

#: List the number of vulnerabilities by `asset.name`.
tally = {}
for asset in api.get_assets():
    if asset.id in vulnerabilities_by_asset_id:
        tally[asset.name] = vulnerabilities_by_asset_id[asset.id]

txt = json.dumps(tally, indent=4)
print(txt)
```

```shell
{
    "104.154.0.0/15": 1553,
    "64.233.160.0/19": 759,
    "66.102.0.0/20": 94,
    "208.117.224.0/19": 432
}
```

#### Count vulnerabilities by location (i.e. by IP address or hostname)

As an example, let's list the number of vulnerabilities associated with all Windows hosts by IP address:

```python
from edgescan.api.client import EdgeScan

import json
import collections
import ipaddress

api = EdgeScan()

tally = collections.defaultdict(int)
for vulnerability in api.get_vulnerabilities(os_types=['windows']):
    try:
        ip = str(ipaddress.ip_address(vulnerability.location))
    except ValueError:
        continue
    else:
        tally[ip] += 1

txt = json.dumps(tally, indent=4)
print(txt)
```

```shell
{
    "142.251.32.69": 75,
    "172.217.1.14": 56,
    "142.251.33.163": 47,
    "142.251.41.78": 41,
    "172.217.165.3": 33,
}
```

> Since the value of `vulnerability.location` can be either a hostname, or an IP address we can use the `ipaddress` module to distinguish between the two.
