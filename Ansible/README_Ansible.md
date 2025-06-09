# Automatización Forense con Ansible

Este módulo forma parte del Trabajo de Investigación Doctoral centrado en la adquisición remota de evidencias digitales, especialmente memoria volátil, en entornos corporativos e industriales.

La solución implementada permite la ejecución remota, sin agentes, de herramientas forenses en sistemas Linux y Windows, garantizando la trazabilidad, integridad y cumplimiento normativo del proceso.

---

## 📁 Estructura del proyecto

```
Ansible/
├── ansible.cfg              # Configuración principal de Ansible
├── site_memoryLinux.yml     # Playbook principal de adquisición en Linux
├── resetnodes.yml           # Playbook para reiniciar el estado de nodos
├── roles/                   # Módulos funcionales organizados por tareas
├── inventories/             # Inventario de nodos y variables por grupo/host
├── tests/                   # Playbooks de prueba y validación de conectividad
├── docs/                    # Documentación técnica y literaria para tesis
└── README.md
```

---

## ▶️ Uso básico

### Ejecutar adquisición de memoria en nodos definidos

```bash
ansible-playbook -i inventories/tid_hosts.yml site_memoryLinux.yml
```

### Reiniciar nodos (limpieza de estado)

```bash
ansible-playbook -i inventories/tid_hosts.yml resetnodes.yml
```

---

## 📚 Componentes clave

- `roles/`: contiene funciones específicas como:
  - `installlime`: descarga y compila LiME
  - `dumpmemorylinux`: realiza volcado de memoria
  - `checklime`: verifica existencia del módulo
  - `labelevidence`: etiqueta evidencia con metadatos
- `inventories/`: define los nodos objetivo organizados por:
  - `group_vars`: variables por grupo de sistemas (`aws`, `ubuntu`)
  - `host_vars`: variables específicas por IP o nodo
- `tests/`: contiene scripts de prueba como `PruebaAcceso.yml` o validaciones de conexión
- `docs/`: literaturas de apoyo como:
  - arquitectura del laboratorio
  - escenarios de validación
  - normativa de referencia
  - integración con la tesis doctoral

---

## ⚖️ Normativa y cumplimiento

Esta solución está alineada con las siguientes directrices y marcos regulatorios:

- **ISO/IEC 27037:2016** — Identificación, recogida, adquisición y preservación de evidencia digital
- **UNE 71506:2013** — Guía metodológica de análisis forense digital
- **Reglamento e-Evidence (UE)** y **Directiva NIS2**
- **Cadena de custodia**: se emplean firmas hash SHA-256, sellado temporal, registros de adquisición y logs automatizados

---

## 📌 Notas adicionales

- Esta solución ha sido probada en entornos locales virtualizados (VirtualBox), así como en nodos en AWS.
- La modularidad de Ansible permite extender el sistema fácilmente a nuevos entornos, incluidos sistemas industriales virtualizados como OpenPLC y SCADA.
- La documentación en `docs/` se integra con el desarrollo de la tesis para asegurar trazabilidad completa de los experimentos.

---
