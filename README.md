# 🛡️ Python Security Tools

![Python Version](https://img.shields.io/badge/python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-educational-orange)

> Tres herramientas de ciberseguridad desarrolladas en Python para aprender y practicar conceptos fundamentales de seguridad informática.

---

## 📋 Tabla de Contenidos

- [🔧 Proyectos incluidos](#-proyectos-incluidos)
- [🚀 Cómo usar](#-cómo-usar)
- [📦 Requisitos](#-requisitos)
- [⚠️ Aviso legal](#️-aviso-legal)
- [👨‍💻 Autor](#-autor)

---

## 🔧 Proyectos incluidos

| Herramienta | Archivo | Descripción |
|-------------|---------|-------------|
| **Generador de contraseñas** | `password_generator_demo.ipynb` | Crea contraseñas robustas y aleatorias con parámetros personalizables (longitud, tipos de caracteres). |
| **Escáner de puertos** | `port_scanner.py` | Escanea puertos abiertos en una IP o dominio. Ideal para reconocimiento básico de servicios. |
| **Hash Cracker** | `hash_cracker.py` | Intenta descifrar hashes MD5, SHA1 o SHA256 mediante ataque de diccionario (uso educativo). |

---

## 🚀 Cómo usar

### 1️⃣ Generador de contraseñas

```bash
python password_generator.py
```
- Ingresa la longitud deseada (ej. 16).
- Recibirás una contraseña segura.

### 2️⃣ Escáner de puertos
```bash
python port_scanner.py
```
- Introduce la IP o dominio (ej. scanme.nmap.org).

- El programa listará los puertos abiertos encontrados.

### 3️⃣ Hash Cracker

```bash
python hash_cracker.py
```
- Proporciona el hash a crackear y su tipo (md5, sha1, sha256).
  
- El script usará un diccionario (rockyou.txt o similar) para intentar recuperar la contraseña original.

  💡 Nota: Para un mejor rendimiento, asegúrate de tener un archivo de diccionario en la misma carpeta.

  ### 📦 Requisitos
Python 3.x (no requiere librerías externas, solo módulos estándar: random, hashlib, socket, sys).

Conexión a internet (solo para el escáner de puertos).

### ⚠️ Aviso legal
Estas herramientas tienen fines estrictamente educativos. El escáner de puertos y el cracker de hashes no deben utilizarse en sistemas sin autorización explícita. El uso indebido puede violar leyes locales e internacionales. El autor no se hace responsable del mal uso de este material.

### 👨‍💻 Autor
Luca Ferrara
Licenciado en Comunicación Social | Programación & Data Analysis

https://www.linkedin.com/in/lucasferrara-data-comunicacion/

https://github.com/lucasferrara015

⭐ Si este proyecto te ayudó, no olvides darle una estrella en GitHub.
¡Contribuciones y sugerencias son bienvenidas!
