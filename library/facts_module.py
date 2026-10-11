#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import platform
import socket
import os


DOCUMENTATION = '''
---
module: facts_module
short_description: Модуль фактов
description:
    - Собирает факты о системе и возвращает их как ansible_facts.
version_added: "1.0"
author: Ирина
'''

EXAMPLES = '''
- name: Получить факты о системе
  facts_module:
'''

RETURN = '''
ansible_facts:
    description: Факты о системе
    type: dict
    returned: always
'''


def main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    result = {
        'changed': False,
        'ansible_facts': {
            'my_hostname': socket.gethostname(),
            'my_os': platform.system(),
            'my_os_release': platform.release(),
            'my_python_version': platform.python_version(),
            'my_architecture': platform.machine(),
            'my_user': os.getenv('USER', 'unknown')
        }
    }

    module.exit_json(**result)


if __name__ == '__main__':
    main()