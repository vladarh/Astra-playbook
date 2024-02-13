                           /\       | |            
                          /  \   ___| |_ _ __ __ _ 
                         / /\ \ / __| __| '__/ _` |
                        / ____ \\__ \ |_| | | (_| |
                       /_/    \_\___/\__|_|  \__,_|               
<!--
Исходник ascii арта
а https://patorjk.com/software/taag  
Font: Big
Text: Astra
-->                                                                              
# Playbook для тестирования Astra 

ansible-playbook для автоматизации оценки соответствия ИС под Astra Linux

### Тех данные
`git - 2.39.2` \
`Ansible - 2.14.3` 
`Python - 3.11.2` \
Не требует python на хосте (все таски используют встроенные модули работающие без python)\
Используется кастомный конфиг для многопользовательского доступа (git и gitlab)

### Описание 
`tasks` - проверки 

`files` - эталонные файлы 

`roles` - будущие роли для кросплатформенных тестов 

`vars` - общие переменные для tasks 

`start.yml` - рабочий playbook 

`default_host.py` - callback plugin для разделения логов по хостам 

### Логирование
- Запуск собирает все конфиги в ```all_info\{{ansible_host}}``` (расположение прописано в задачах, путь взят из общих переменных) 
- playbook генерирует статистику по исполнению задач в ``` all_info\{{ansible_host}}\logs\sum_{{ansible_host}}.log``` (расположение прописано в задачах, путь взят из общих переменных) 
- Общий лог пишется из `start.yml` в `pre_tasks` 
- Лог по хостам пишется от `default_host.py` в ```all_info\{{ansible_host}}\logs\log_{{ansible_host}}.log```
- Статиситка по загрузке файлов нод пишется в ```download_summary```

### Локальные плагины



### Запуск

1. Запустить все таски на localhost (` ansible-playbook -l local start.yml `)
2. Таска aureport_auth  (` ansible-playbook -l local start.yml --tags=aureport_auth`)



```yaml
---
"{{ Ansible }}" is an orchestration tool written in Python.
...
```
