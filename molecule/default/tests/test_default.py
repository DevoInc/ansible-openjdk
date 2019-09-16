import os

import testinfra.utils.ansible_runner


def test_java_version(host):
    ansible_vars = host.ansible.get_variables()
    java_version = ansible_vars.get('java__version')
    java_output = host.run('java -version')
    assert str(java_version) in java_output.stderr
