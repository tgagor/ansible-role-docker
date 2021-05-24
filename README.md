Ansible role for Docker
=======================

This role will install Docker service on compatible platforms.

[![Molecule Test](https://github.com/tgagor/ansible-role-docker/actions/workflows/test-and-release.yml/badge.svg)](https://github.com/tgagor/ansible-role-docker/actions/workflows/test-and-release.yml)
![Ansible Role](https://img.shields.io/ansible/role/55040)
![Ansible Quality Score](https://img.shields.io/ansible/quality/55040?label=galaxy%20quality%20score)
![Ansible Role](https://img.shields.io/ansible/role/d/55040)

## Supported systems

* Ubuntu
  * 18.04
  * 20.04
  * 20.10
  * 21.04
* Debian
  * 10 (buster)
  * 11 (bullseye)
* CentOS
  * 7
  * 8
* Fedora
  * 32
  * 33
  * 34

## Requirements

As Docker's repo is available via HTTPS, role will install `apt-transport-https` if it's not present in the system.

## Role variables

Role doesn't require any custom variables.

## Dependencies

There are no dependencies on other roles.

## Example playbook

Just add to you playbook, to install it on `localhost`:

```yaml
- hosts: localhost
  connection: local
  gather_facts: true
  become: yes
  tasks:
    - name: Install Docker
      include_role:
        name: tgagor.docker
```

## License
-------

See [LICENSE](LICENSE)
