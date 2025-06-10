# Instalación de OpenPLC Runtime en Ubuntu Server 24.04

Este documento describe el proceso correcto y verificado para instalar el entorno de ejecución de OpenPLC junto con su interfaz web en una máquina virtual con Ubuntu Server 24.04 LTS.

---

## ✅ Requisitos

- Sistema operativo: Ubuntu Server 24.04
- Conectividad a internet
- Usuario con permisos sudo

---

## 🧰 Pasos de instalación

```bash
# 1. Instalar dependencias necesarias
sudo apt update
sudo apt install -y git build-essential python3 python3-pip libmodbus-dev python3-flask

# 2. Clonar el repositorio oficial
cd ~
git clone https://github.com/thiagoralves/OpenPLC_v3.git
cd OpenPLC_v3

# 3. Ejecutar el instalador con el parámetro correcto
sudo ./install.sh linux

# 4. Iniciar el servidor web de OpenPLC
sudo ./start_openplc.sh
```

---

## 🌐 Acceso a la interfaz web

Desde un navegador en el nodo controlador, acceder a:

```
http://<IP_DEL_PLC>:8080
```

---

## 🔐 Credenciales por defecto

- **Usuario**: `openplc`
- **Contraseña**: `openplc`

> Es recomendable cambiar la contraseña tras el primer inicio de sesión.

---

## 📁 Ubicación recomendada en el repositorio

Guardar este archivo como:

```
Doctorado/Ansible/docs/instalacion_openplc.md
```

---

## 🧪 Validación

Una vez instalado:
- El servicio debe estar escuchando en el puerto `8080`.
- Debe mostrarse la interfaz de OpenPLC al acceder desde un navegador remoto.
- El runtime debe poder activarse desde el panel.

---

## 🧯 Para desinstalar (si es necesario)

```bash
sudo apt remove --purge openplc_v3
rm -rf ~/OpenPLC_v3
```

---

## 📝 Notas

- En versiones anteriores del repositorio, las credenciales por defecto pueden variar. Esta documentación es válida para instalaciones realizadas con `install.sh linux` tras clonar el repositorio oficial en 2025.
