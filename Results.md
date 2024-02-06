# Структура результата работы playbooks
[Дерево](https://tree.nathanfriend.io/?s=(%27options!(%27fancy!B~fullPath!false~trailingSlash!B~rootDot!B)~C(%27C%27all_infoG1*logs8errors91792793F.0.0.9n78results0BFfalseFerrorFexecuted78E_statA78logA.log8sumA751525354*.*.*.5nG2G36.6.6.Gn%27)~version!%271%27)*6%20-host_address_08%205*Eed_file_6%5Cn%207.txt8*%2090task_A_((-1))BtrueCsource!EfetchF70G6-%01GFECBA987650-*)
```bash
.
└── all_info/
    ├── host_address_1/
    │   ├── logs/
    │   │   ├── errors/
    │   │   │   ├── task_1.txt
    │   │   │   ├── task_2.txt
    │   │   │   ├── task_3.txt
    │   │   │   ├── .
    │   │   │   ├── .
    │   │   │   ├── .
    │   │   │   └── task_n.txt
    │   │   ├── results/
    │   │   │   ├── true.txt
    │   │   │   ├── false.txt
    │   │   │   ├── error.txt
    │   │   │   └── executed.txt
    │   │   ├── fetch_stat_{{host_address_1}}.txt
    │   │   ├── log_{{host_address_1}}.log
    │   │   └── sum_{{host_address_1}}.txt
    │   ├── fetched_file_1
    │   ├── fetched_file_2
    │   ├── fetched_file_3
    │   ├── fetched_file_4
    │   ├── .
    │   ├── .
    │   ├── .
    │   └── fetched_file_n
    ├── host_address_2
    ├── host_address_3
    ├── .
    ├── .
    ├── .
    └── host_address_n
```
