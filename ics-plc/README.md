# PLC simulado para laboratorio ICS

Este directorio contiene una implementación simplificada de un **PLC simulado**, utilizada para generar tráfico de red representativo de sistemas industriales.

El PLC se ejecuta dentro de un contenedor Docker.

---

## Componentes

```
plc/
├── Dockerfile
└── server.py
```

**Dockerfile**  
Definición del contenedor utilizado para ejecutar el PLC simulado.

**server.py**  
Servidor que implementa la lógica básica del PLC.

---

## Construcción de la imagen

```
docker build -t simulated-plc .
```

---

## Ejecución

```
docker run -p 502:502 simulated-plc
```

---

## Objetivo

El PLC simulado permite:

- generar tráfico industrial
- capturar comunicaciones
- realizar análisis de red en escenarios DFIR

---

## Limitaciones

Este componente:

- no implementa completamente protocolos industriales
- no pretende replicar un PLC real
- está diseñado únicamente para experimentación académica
