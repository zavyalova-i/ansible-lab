#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Скрипт использования модулей Ansible.

Демонстрирует вызов двух пользовательских модулей:
- info_module — возвращает информацию о модуле.
- facts_module — собирает факты о системе.

Запуск через Ansible:
    ansible -i hosts -m info_module all
    ansible -i hosts -m facts_module all
"""


def print_header(title):
    """Печатает заголовок раздела."""
    print("=" * 50)
    print(title)
    print("=" * 50)


def main():
    print_header("Скрипт использования модулей Ansible")

    print("\nДоступные модули:")
    print("  1. info_module  — модуль информации")
    print("  2. facts_module — модуль фактов")

    print("\nКоманды для запуска через Ansible:")
    print("  ansible -i hosts -m info_module all")
    print("  ansible -i hosts -m facts_module all")

    print("\nОписание модулей:")
    print("  info_module  — возвращает информацию о модуле")
    print("                 (сообщение, версия, автор, hostname, ОС, версия Python)")
    print("  facts_module — собирает факты о системе")
    print("                 (hostname, ОС, версия Python, количество CPU, uptime)")

    print("\nГотово.")


if __name__ == '__main__':
    main()