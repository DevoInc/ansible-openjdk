import subprocess
import pytest


@pytest.fixture
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])

    return ansible_vars


def test_java_version(host, get_vars):
    version = subprocess.check_output(
        ['java', '-version'],
        stderr=subprocess.STDOUT
    )
    assert str(get_vars['java__version']) in version
