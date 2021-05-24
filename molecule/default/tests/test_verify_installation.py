# -*- coding: utf-8 -*-
import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repo_configured(host):
    f = None

    if host.system_info.distribution in ['debian', 'ubuntu']:
        f = host.file('/etc/apt/sources.list.d/docker.list')

    if host.system_info.distribution in ['centos', 'fedora', 'redhat']:
        f = host.file('/etc/yum.repos.d/docker-ce.repo')

    assert f.exists
    assert f.contains(f'https://download.docker.com/linux/{host.system_info.distribution}')
    assert f.contains(host.system_info.distribution)


@pytest.mark.parametrize('pkg', [
    'docker-ce',
    'docker-ce-cli',
    'containerd.io',
])
def test_package_installed(host, pkg):
    assert host.package(pkg).is_installed
    assert host.run('docker --version').succeeded


def test_user_configured(host):
    assert host.group('docker').exists
    assert 'docker' in host.user('dude').groups

    # check if user can really call docker commands
    with host.sudo('dude'):
        assert host.run('docker info').succeeded


@pytest.mark.parametrize('path', [
    '/etc/docker/daemon.json',
    '/etc/systemd/system/docker.service.d/hosts.conf',
])
def test_config_files_exists(host, path):
    assert host.file(path).exists


def test_service_is_running(host):
    assert host.service('docker').is_enabled
    assert host.service('docker').is_running
    assert host.socket("unix:///var/run/docker.sock").is_listening
    assert host.socket("tcp://127.0.0.1:2375").is_listening
