import os
import pytest
import yaml
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults():
    with open("./defaults/main.yml", 'r') as stream:
        return yaml.full_load(stream)


@pytest.mark.parametrize("dir", [
    "/opt/promtail",
    "/etc/promtail",
    "/etc/promtail/file_sd",
    "/var/lib/promtail",
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/systemd/system/promtail.service",
    "/usr/local/bin/promtail",
    "/etc/promtail/promtail.yml"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("promtail").exists
    assert host.user("promtail").exists


def test_service(host):
    s = host.service("promtail")
    assert s.is_running


def test_http_socket(host):
    s = host.socket("tcp://0.0.0.0:9080")
    assert s.is_listening


def test_grpc_socket(host):
    s = host.socket("tcp://0.0.0.0:9095")
    assert s.is_listening


def test_version(host, AnsibleDefaults):
    version = os.getenv('PROMTAIL', AnsibleDefaults['promtail_version'])
    out = host.run("/usr/local/bin/promtail --version").stdout
    assert version in out
    assert "promtail" in out
