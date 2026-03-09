**inventories/**  
Inventarios de hosts gestionados.

**group_vars/**  
Variables compartidas por grupos de sistemas.

**host_vars/**  
Variables específicas para cada host.

**roles/**  
Roles de Ansible que implementan tareas de adquisición forense.

**src/**  
Scripts auxiliares utilizados en los experimentos.

**tests/**  
Escenarios de prueba.

---

## Funcionalidades implementadas

El framework permite automatizar:

- adquisición de **memoria RAM**
- ejecución de herramientas forenses remotas
- captura de **tráfico de red**
- recopilación de metadatos del sistema
- cálculo de **hashes de integridad**
- transferencia segura de evidencias

---

## Requisitos

- Linux
- Ansible
- acceso SSH a los nodos gestionados
- privilegios adecuados para la adquisición de evidencias

---

## Ejecución básica

Ejemplo de ejecución de un playbook:

```
ansible-playbook playbook.yml -i inventories/hosts.yml
```

---

## Advertencia

Los playbooks incluidos se utilizaron en un **entorno experimental controlado**.

Antes de ejecutarlos en otros entornos deben revisarse:

- permisos
- rutas de almacenamiento
- impacto potencial sobre los sistemas

---

## Uso en la investigación

Este framework fue utilizado en los experimentos descritos en la tesis doctoral para evaluar:

- viabilidad operativa
- tiempos de adquisición
- integridad de las evidencias
- impacto en los sistemas objetivo
