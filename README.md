# Ansible Role: promtail

[![Build Status](https://travis-ci.org/patrickjahns/ansible-role-promtail.svg?branch=master)](https://travis-ci.org/patrickjahns/ansible-role-promtail)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-patrickjahns.promtail-blue.svg)](https://galaxy.ansible.com/patrickjahns/promtail/)
[![GitHub tag](https://img.shields.io/github/tag/patrickjahns/ansible-role-promtail.svg)](https://github.com/patrickjahns/ansible-role-promtail/tags)

## Description

Deploy [promtail](https://github.com/grafana/loki) using ansible.
For recent changes, please check the [CHANGELOG](/CHANGELOG.md) or have a look at [github releases](https://github.com/patrickjahns/ansible-role-promtail/releases)


## Requirements

- Ansible >= 2.7 

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `promtail_version` | "1.3.0" | promtail package version. Also accepts *latest* as parameter. |
| `promtail_config_dir` | /etc/promtail | Directory for storing promtail configuration file |
| `promtail_config_file` | "{{ promtail_config_dir }}/promtail.yml" | Configuration file used by promtail |
| `promtail_system_user` | promtail | User the promtail process will run at |
| `promtail_system_group` | "{{ promtail_system_user }}" | Group of the *promtail* user |
| `promtail_user_additional_groups` | "adm" | Additional groups to be added to *promtail* user to give access to allow scraping of specific log files |
| `promtail_config_clients` | see [defaults/main.yml](defaults/main.yml) | promtail [client_config](https://github.com/grafana/loki/blob/master/docs/clients/promtail/configuration.md#client_config) section |
| `promtail_loki_server_url` | http://127.0.0.1:3100 | Server url where promtail will push its result |
| `promtail_config_server` | see [defaults/main.yml](defaults/main.yml) | promtail [server_config](https://github.com/grafana/loki/blob/master/docs/clients/promtail/configuration.md#server_config) section |
| `promtail_config_positions` | {} | promtail [position_config](https://github.com/grafana/loki/blob/master/docs/clients/promtail/configuration.md#position_config) section |
| `promtail_config_scrap_configs` | [] | promtail [scrap_configs](https://github.com/grafana/loki/blob/master/docs/clients/promtail/configuration.md#scrape_config) section |
| `promtail_target_config` | {} | promtail [target_config](https://github.com/grafana/loki/blob/master/docs/clients/promtail/configuration.md#target_config) section |
| `promtail_log_level` | "info" | Loglevel of promtail (one of: `debug`,`info`,`warn`,`error` ) |

For each section (`promtail_config_clients`, `promtail_config_server`,`promtail_config_positions`,`promtail_config_scrap_configs`,`promtail_target_config`) the configuration can be passed accrodingly to the [official promtail configuration](https://github.com/grafana/loki/blob/master/docs/clients/promtail/configuration.md). 
The role will converte the ansible vars into the respective yaml configuration for loki.

## Example Playbook

Basic playbook that will assume that loki will be listening at `http://127.0.0.1:3100` and a simple configuration to scrape `/var/log` logs
```yaml
---
- hosts: all
  roles:
    - role: patrickjahns.promtail
      vars: 
        promtail_config_scrap_configs:
          - job_name: system
            entry_parser: raw
            static_configs:
            - targets:
                - localhost
              labels:
                job: varlogs
                __path__: /var/log/*log
```

More complex example, that overrides server, client, positions configuration and provides a scrap configuration for `/var/log`

```yaml
---
- hosts: all
  roles:
    - role: patrickjahns.promtail
      vars: 
        promtail_config_server:
          http_listen_port: 9080
          grpc_listen_port: 9081
        promtail_config_clients:
          - url: "http://prometheus.domain.tld:3100/loki/api/v1/push"
            external_labels:
              host: "{{ ansible_hostname }}"
        promtail_config_positions:
          filename: /tmp/positions.yaml

        promtail_config_scrap_configs:
          - job_name: system
            entry_parser: raw
            static_configs:
            - targets:
                - localhost
              labels:
                job: varlogs
                __path__: /var/log/*log
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v3.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e ansible29 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.

## Maintainers and Contributors

- [Patrick Jahns](https://github.com/patrickjahns)