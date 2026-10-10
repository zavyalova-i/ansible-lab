# Лабораторная работа — Конфигурационное управление (Ansible)

## Часть 1. Использование Ansible

- Развернут узел управления Ansible (Arch Linux)
- Подготовлен управляемый узел (Ubuntu Server 24.04)
- Настроен SSH-доступ
- Создан inventory-файл `hosts`
- Выполнены 3 ручные операции
- Собраны Facts
- Создана роль `nginx` с обработчиком
- Роль применена на управляемом сервере

### Команды применения роли

См. файл `commands.txt`.

```bash
ansible -i hosts -m ping all
ansible-playbook -i hosts play.yml
curl http://192.168.1.108
