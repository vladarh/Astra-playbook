# Описание TASKS по разделам

> **Note** \
> default config ansible.cfg requires: \
> stdout_callback = default \
> or \
> stdout_callback = default_host \
> and \
> bin_ansible_callbacks = True 


> **Warning** \
> python required \
> other stdout callbacks don't support russian (in python version < 3)

<div class="tg-wrap"><table class="tg">
<thead>
  <tr>
    <th class="tg-7btt"></th>
    <th class="tg-fymr">Раздел<br></th>
    <th class="tg-fymr">id<br></th>
    <th class="tg-fymr">Тег<br></th>
    <th class="tg-fymr">Описание</th>
    <th class="tg-fymr">Эталонные файлы*<br></th>
    <th class="tg-fymr">Переменные**</th>
    <th class="tg-fymr">Downloaded***<br></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7btt" rowspan="23">ПУД</td>
    <td class="tg-0pky" rowspan="20">ПУД1<br></td>
    <td class="tg-0pky">1</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/1_krb5_1.yml" target="_blank" rel="noopener noreferrer">krb5_1</a></td>
    <td class="tg-0pky">Проверка наличия домена Роснефти в конфиге Kerberos<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/krb5.conf</td>
  </tr>
  <tr>
    <td class="tg-0pky">2<br></td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/1_krb5_2.yml" target="_blank" rel="noopener noreferrer">krb5_2</a></td>
    <td class="tg-0pky">Проверка наличия домена Роснефти в конфиге Kerberos<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/krb5.conf</td>
  </tr>
  <tr>
    <td class="tg-0pky">3<br></td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/2.1_ad_group_lis.yml" target="_blank" rel="noopener noreferrer">ad_group_list</a></td>
    <td class="tg-0pky">Проверка соответствия списка групп эталонному</td>
    <td class="tg-0pky">ad_group</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/sssd/sssd.conf</td>
  </tr>
  <tr>
    <td class="tg-0pky">4</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/2.2_ad_user_list.yml" target="_blank" rel="noopener noreferrer">ad_user_list</a></td>
    <td class="tg-0pky">Проверка соответствия списка пользователей эталонному</td>
    <td class="tg-kwiq">ad_user</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/sssd/sssd.conf</td>
  </tr>
  <tr>
    <td class="tg-0pky">5</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/3.2loc_group_list.yml" target="_blank" rel="noopener noreferrer">loc_group_list</a></td>
    <td class="tg-0pky">Проверка соответствия локального списка групп эталонному</td>
    <td class="tg-kwiq">group_list</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/group<br>getent group &gt; group.txt</td>
  </tr>
  <tr>
    <td class="tg-0pky">6</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/3.1_loc_user_list.yml" target="_blank" rel="noopener noreferrer">loc_user_list</a></td>
    <td class="tg-0pky">Проверка соответствия локального списка пользователей эталонному</td>
    <td class="tg-0pky">user_list</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/group<br>getent group &gt; group.txt</td>
  </tr>
  <tr>
    <td class="tg-0pky">7</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/6_wheel_1.yml" target="_blank" rel="noopener noreferrer">wheel_1</a></td>
    <td class="tg-0pky">проверка наличия строки auth required pam_wheel.so</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/pam.d/su</td>
  </tr>
  <tr>
    <td class="tg-0pky">8</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/7_wheel_2.yml" target="_blank" rel="noopener noreferrer">wheel_2</a></td>
    <td class="tg-0pky">проверка отсутствия пользователей в группе wheel</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/pam.d/su</td>
  </tr>
  <tr>
    <td class="tg-0pky">9</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/9_pw_quality_1.yml" target="_blank" rel="noopener noreferrer">pw_quality_1</a></td>
    <td class="tg-0pky">Проверка соответствия&nbsp;&nbsp;параметры локального пароля эталонным значениям<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">pwquality_var</td>
    <td class="tg-0pky">/etc/security/pwquality.conf</td>
  </tr>
  <tr>
    <td class="tg-0pky">10</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/12_pw_quality_2.yml" target="_blank" rel="noopener noreferrer">pw_quality_2</a></td>
    <td class="tg-i1lm" colspan="4">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">11</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/13_pw_quality_3.yml" target="_blank" rel="noopener noreferrer">pw_quality_3</a></td>
    <td class="tg-0pky">проверка аткивных УЗ без без заданного пароля</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">getent passwd &gt; active_users.txt<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">12</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/10_pw_quality_4.yml" target="_blank" rel="noopener noreferrer">pw_quality_4</a></td>
    <td class="tg-0pky">проверка совпадения с эталонными параметрами пароля</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">login_defs_var</td>
    <td class="tg-0pky">/etc/login.defs</td>
  </tr>
  <tr>
    <td class="tg-0pky">13</td>
    <td class="tg-kwiq">common_password</td>
    <td class="tg-0pky">проверка наличия и активности локальных параметров пароля в /etc/pam.d/common-password</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">pswd_auth_1<br>pam_unix_1<br>pam_unix_2<br>pwquality_var</td>
    <td class="tg-0pky">/etc/pam.d/common-password</td>
  </tr>
  <tr>
    <td class="tg-0pky">14</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/15_include.yml" target="_blank" rel="noopener noreferrer">include</a></td>
    <td class="tg-0pky">проверка "директива неактивна" include/includedir</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/sudoers</td>
  </tr>
  <tr>
    <td class="tg-0pky">15</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/16_sudoersd.yml" target="_blank" rel="noopener noreferrer">sudoersd</a></td>
    <td class="tg-0pky">проверка, что директория /etc/sudoers.d пустая</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/sudoers.d</td>
  </tr>
  <tr>
    <td class="tg-0pky">16</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD1/19_securetty.yml" target="_blank" rel="noopener noreferrer">securetty</a></td>
    <td class="tg-0pky">проверка, что файл securetty пуст добавить вывод содержимого<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/securetty</td>
  </tr>
  <tr>
    <td class="tg-0pky">17</td>
    <td class="tg-kwiq"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">18</td>
    <td class="tg-kwiq"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">19</td>
    <td class="tg-kwiq"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">20</td>
    <td class="tg-kwiq"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">ПУД2<br></td>
    <td class="tg-0pky">1</td>
    <td class="tg-kwiq"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PUD2/ss.yml" target="_blank" rel="noopener noreferrer">ss</a></td>
    <td class="tg-0pky">Проверка наличия исходящих соединений ssh<br></td>
    <td class="tg-0pky">ip_list</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-1i2r">ПУД3<br></td>
    <td class="tg-1i2r">1</td>
    <td class="tg-i1lm" colspan="5">-</td>
  </tr>
  <tr>
    <td class="tg-73oq">ПУД4<br></td>
    <td class="tg-73oq">1</td>
    <td class="tg-73oq">getfacl</td>
    <td class="tg-mqa1">Запись в лог прав доступа для объектов <br><br>getfacl for i in[<br><br>\etc\passwd,<br>\etc\shadow,<br>\var\log\audit]<br><br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/var/log/audit/audit.log</td>
  </tr>
  <tr>
    <td class="tg-7btt" rowspan="10">ПРУ</td>
    <td class="tg-73oq" rowspan="3">ПРУ1</td>
    <td class="tg-73oq">1</td>
    <td class="tg-quyz"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PRU4/auditd_status.yml" target="_blank" rel="noopener noreferrer">auditd_status</a></td>
    <td class="tg-73oq">проверка статуса системы аудита auditd<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-deae">2</td>
    <td class="tg-deae">auditctl</td>
    <td class="tg-deae">Сравнение правил аудита <br>Сравнить правила "эталон" и вывод auditctl -l</td>
    <td class="tg-leq3"></td>
    <td class="tg-7btt"></td>
    <td class="tg-7btt"></td>
  </tr>
  <tr>
    <td class="tg-73oq">3</td>
    <td class="tg-73oq">aureport_auth</td>
    <td class="tg-73oq">проверка попыток аутентификации<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-73oq">ПРУ2</td>
    <td class="tg-73oq">1</td>
    <td class="tg-73oq">ausearch_process</td>
    <td class="tg-73oq">Проверка запуска процессов </td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-73oq" rowspan="2">ПРУ3</td>
    <td class="tg-73oq">1</td>
    <td class="tg-73oq">ausearch_file</td>
    <td class="tg-73oq">Регистрация попыток доступов к защищённым файлам</td>
    <td class="tg-0pky">local_user_list</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-73oq">2</td>
    <td class="tg-73oq">aureport_syscall</td>
    <td class="tg-73oq">Регистрация попыток входа/выхода</td>
    <td class="tg-0pky">local_user_list</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-73oq">ПРУ4</td>
    <td class="tg-73oq">1</td>
    <td class="tg-quyz"><a href="https://github.com/vladarh/Ansible_Astra/blob/main/tasks/PRU4/swap.yml" target="_blank" rel="noopener noreferrer">swap</a></td>
    <td class="tg-73oq">Проверка swap файла<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/cron.daily/swap_wipe</td>
  </tr>
  <tr>
    <td class="tg-73oq" rowspan="3">ПРУ5</td>
    <td class="tg-73oq">1</td>
    <td class="tg-73oq">aide_conf</td>
    <td class="tg-2jy6" colspan="3">забрать файл /etc/aide.conf</td>
    <td class="tg-0pky">ls /etc/cron.daily/ &gt; cron.daily<br></td>
  </tr>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">aide_cron</td>
    <td class="tg-i1lm" colspan="4">проверить наличие задания =&gt; забрать задание/etc/cron.daily</td>
  </tr>
  <tr>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">ksn_synch</td>
    <td class="tg-i1lm" colspan="4">-</td>
  </tr>
  <tr>
    <td class="tg-g7sd" rowspan="10">ПРОФИЛЬ</td>
    <td class="tg-0pky" rowspan="10">-</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">pr_password_quality_1</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">pr_password_quality_2</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">pr_password_quality_3</td>
    <td class="tg-0pky">для common-auth<br></td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/pam.d/common-auth</td>
  </tr>
  <tr>
    <td class="tg-0pky">4</td>
    <td class="tg-0pky">pr_mask</td>
    <td class="tg-0pky">/parsecfs/mode_mask<br> = '0000' Проверка значения<br></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky">/parsecfs/mode_mask</td>
  </tr>
  <tr>
    <td class="tg-0pky">-</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">6</td>
    <td class="tg-0pky">pr_astra_console<br></td>
    <td class="tg-0pky">systemctl is-enabled astra-console-lock<br>enabled включен<br>disabled выключен<br>Failed to get unit file state ... сервис не активирован</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">7</td>
    <td class="tg-0pky">pr_ulimits<br></td>
    <td class="tg-0pky">systemctl is-enabled astra-ulimits-control<br>enabled включен<br>disabled выключен<br>Failed to get unit file state ... сервис не активирован</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">8</td>
    <td class="tg-0pky">pr_sysctl</td>
    <td class="tg-0pky">Использование клавиши SysRq запрещен<br>/etc/sysctl.conf = 'kernel.sysrq=0'</td>
    <td class="tg-7btt">-</td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/etc/sysctl.conf</td>
  </tr>
  <tr>
    <td class="tg-0pky">9</td>
    <td class="tg-0pky">pr_screen</td>
    <td class="tg-0pky">Параметр «Блокировать экран через» имеет значение<br><br>/usr/share/fly-wm/theme/default.themerc<br> 'ScreenSaverDelay=600'</td>
    <td class="tg-0pky"></td>
    <td class="tg-7btt">-</td>
    <td class="tg-0pky">/usr/share/fly-wm/theme/default.themerc</td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table></div>
