#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: info_module
short_description: Модуль информации
description:
    - Возвращает информацию о модуле и приветствие.
version_added: "1.0"
author: Ирина
'''

EXAMPLES = '''
- name: Получить информацию
  info_module:
'''

RETURN = '''
info:
    description: Информация о модуле
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
        'info': {
            'message': 'Это модуль информации',
            'version': '1.0',
            'author': 'Ирина',
            'status': 'работает'
        }
    }

    module.exit_json(**result)


if __name__ == '__main__':
    main()