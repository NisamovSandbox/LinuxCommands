# ¿Qué es eBPF?
eBPF es un motor de ejecución dentro del kernel de Linux que permite correr programas seguros y sandboxed.
Originalmente nació para filtrado de paquetes (BPF clásico), pero ahora es mucho más que networking.

Se puede usar para:
- Tracing (seguimiento de eventos)
- Monitoreo de rendimiento
- Seguridad (firewalls avanzados, auditoría)
- Networking y filtrado
Es exclusivo de Linux, aunque FreeBSD y otros han implementado algo similar.

## Conceptos
| Concepto | Descripción |
| ----------------- | --------------------------------------------------------------------------------- |
| **Mapas BPF**     | Estructuras de datos compartidas entre kernel y espacio usuario                   |
| **Program Types** | Tipos de programas eBPF: tracing, socket, XDP, cgroup, perf_event, kprobe, uprobe |
| **Hooks**         | Puntos del kernel donde se engancha eBPF: syscalls, network, scheduler            |
| **Sandbox**       | Kernel valida el programa antes de ejecutar                                       |
| **Bytecode**      | Código compilado a un formato seguro que interpreta el kernel                     |
| **bpftool**       | Herramienta oficial para cargar y depurar programas eBPF                          |

## Ejemplos de Uso
Contar llamadas a un syscall:
```bt
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s abrió %s\n", comm, str(args->filename)); }'
```
Medir duración de ejecución de un programa:
```bt
sudo bpftrace -e 'profile:hz:99 { @[comm] = count(); }'
```