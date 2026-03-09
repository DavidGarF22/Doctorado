# Configuración experimental de Velociraptor

Este directorio contiene la configuración utilizada para los experimentos realizados con **Velociraptor**, una plataforma DFIR basada en agentes.

Velociraptor se utilizó como **herramienta de referencia** para comparar el enfoque agentless basado en Ansible con una solución ampliamente utilizada en investigación forense digital.

---

## Componentes incluidos

El directorio contiene:

- configuración del **servidor Velociraptor**
- configuración del **cliente/agente**
- artefactos personalizados utilizados en los experimentos

---

## Estructura

```
Velociraptor/
├── server.config.yaml
├── client.config.yaml
├── artifacts/
└── tools/
```

**server.config.yaml**  
Configuración del servidor Velociraptor.

**client.config.yaml**  
Configuración del agente utilizado en los sistemas monitorizados.

**artifacts/**  
Artefactos personalizados utilizados en los experimentos.

**tools/**  
Herramientas auxiliares utilizadas durante la adquisición.

---

## Artefactos DFIR

Los artefactos incluidos permiten automatizar tareas como:

- adquisición de memoria
- recopilación de información del sistema
- captura de artefactos del sistema operativo

---

## Uso en los experimentos

Velociraptor fue utilizado para evaluar:

- tiempos de adquisición
- impacto en el sistema
- facilidad de despliegue
- automatización de procesos DFIR

Los resultados se compararon con el enfoque basado en Ansible.

---

## Nota de seguridad

Las configuraciones incluidas están adaptadas a un **laboratorio experimental**.

Antes de utilizarlas en un entorno real deben revisarse cuidadosamente:

- certificados
- rutas
- parámetros de red
