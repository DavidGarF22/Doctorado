# Doctorado – Automatización de la adquisición de evidencias digitales

Este repositorio contiene los artefactos experimentales utilizados en la tesis doctoral sobre **automatización de la adquisición remota de evidencias digitales en entornos corporativos e industriales**.

El objetivo del repositorio es facilitar la **reproducibilidad parcial de los experimentos**, así como proporcionar ejemplos de configuración utilizados durante la investigación.

El trabajo de investigación asociado incluye, entre otras publicaciones:

- "Forensic Technologies to Automate the Acquisition of Digital Evidences" (CSCI 2022)
- "Automatización de la adquisición de evidencias para el análisis forense" (JNIC 2023)
- Agentless and Automated Acquisition of Digital Evidence in Corporate and Industrial Networks: Architecture, Validation, and Compliance (Electronics 2026)
- "Marco para la adquisición remota y automatizada de evidencias digitales en entornos corporativos e industriales" (RECSI 2026)
- "Analysis of Remote Memory Acquisition Frameworks: Ansible in DFIR Applications" (en revisión)

---

# Estructura del repositorio

- **Ansible/**  
  Framework de adquisición forense *agentless* utilizado en los experimentos principales.

- **Velociraptor/**  
  Configuración utilizada para los experimentos comparativos con herramientas basadas en agentes.

- **ics-plc/**  
  Laboratorio simplificado de sistema industrial utilizado para pruebas en entornos ICS.

---

# Objetivo del repositorio

Este repositorio proporciona:

- Ejemplos de **playbooks de adquisición forense**
- Configuración de **herramientas DFIR**
- Artefactos utilizados en **experimentos comparativos**
- Elementos del **laboratorio experimental**

El código se publica con fines **académicos y de investigación**.

---

# Reproducibilidad

Los artefactos incluidos permiten reproducir parcialmente los experimentos descritos en la tesis, incluyendo:

- adquisición remota de memoria
- adquisición de evidencias en hosts Linux
- comparación entre enfoques **agentless** y **basados en agentes**
- captura de tráfico en entornos industriales simulados

No se incluyen todos los componentes del laboratorio original, ya que algunos dependen de infraestructura específica.

---

# Advertencias

Este repositorio:

- No está diseñado como herramienta DFIR lista para producción
- No debe desplegarse directamente en entornos operativos
- Contiene configuraciones simplificadas para experimentación

---

# Licencia

El contenido se publica con fines académicos y de investigación.
