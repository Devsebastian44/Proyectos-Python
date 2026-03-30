# PySysTools

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-0078D4?style=flat&logo=windows&logoColor=white)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Ready-f97316?style=flat&logo=shieldsdotio&logoColor=white)
![Code Style](https://img.shields.io/badge/Code%20Style-flake8-7c3aed?style=flat)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitLab%20Pipelines-FC6D26?style=flat&logo=gitlab&logoColor=white)


## 🧠 Overview

**PySysTools** es una suite de herramientas de administración de sistemas y operaciones de seguridad orientada a entornos empresariales. Está construida en Python como una librería instalable con CLI, y está diseñada para ingenieros de sistemas, administradores de infraestructura y profesionales de DevSecOps.

El proyecto cubre cuatro dominios operativos principales: monitoreo del sistema, análisis de redes, operaciones de seguridad y gestión de datos. Cada dominio está encapsulado en su propio módulo dentro del paquete `sysadmin_utils`, permitiendo un uso modular tanto desde la línea de comandos como mediante integración programática en otros proyectos Python.

Este proyecto sigue un enfoque de **Security by Design**: las herramientas de análisis y escaneo han sido diseñadas para uso defensivo y auditivo en infraestructuras propias o con autorización explícita.

> ⚠️ **Uso Responsable:** Las capacidades de análisis de seguridad incluidas en esta suite (escaneo de malware, análisis de hash, monitoreo de red) deben utilizarse únicamente en sistemas bajo propiedad o con autorización escrita del propietario. El autor no asume responsabilidad por usos no autorizados o ilegales de estas herramientas.

---

## ⚙️ Features

- **Generación de contraseñas seguras** con longitud y complejidad configurables
- **Escaneo de malware** en directorios locales mediante análisis de firmas y hashes
- **Monitoreo de red en tiempo real** con detección de interfaces y tráfico activo
- **Supervisión de recursos del sistema** (CPU, RAM, disco, procesos) vía `psutil`
- **Integración con protocolo SMB/CIFS** para operaciones sobre recursos compartidos de red
- **Automatización de interfaz gráfica** para tareas repetitivas en entornos de escritorio
- **Gestión de datos con MySQL** para almacenamiento y consulta de registros operativos
- **Procesamiento y análisis de datos** estructurados con `pandas`
- **Notificaciones nativas en Windows** mediante `winotify` para alertas del sistema
- **CLI unificada** que centraliza todos los módulos bajo un único punto de entrada
- **Arquitectura modular** que permite usar cada componente de forma independiente

---

## 🛠️ Tech Stack

| Categoría | Tecnología | Uso |
|---|---|---|
| Lenguaje | Python 3.8+ | Core del proyecto |
| Sistema | psutil | Monitoreo de procesos y recursos |
| Datos | pandas | Análisis y procesamiento de datos |
| Base de datos | MySQL + mysql-connector-python | Persistencia de registros |
| Red | pysmb | Operaciones SMB/CIFS |
| Automatización | pyautogui | Automatización de GUI |
| Notificaciones | winotify | Alertas nativas Windows |
| Calidad de código | flake8 | Linting y estilo |
| Seguridad estática | bandit | Análisis SAST |
| Testing | pytest | Pruebas unitarias e integración |
| Empaquetado | setuptools | Instalación como paquete Python |
| CI/CD | GitLab Pipelines | Automatización de builds y tests |
| Diagramas | Mermaid | Documentación de arquitectura |

---

## 📦 Installation

### Requisitos previos

- Python 3.8 o superior
- pip
- MySQL Server (opcional, para módulos de datos)
- Windows 10+ (para notificaciones nativas) o Linux

### Instalación desde el repositorio

```bash
# 1. Clonar el repositorio
git clone https://gitlab.com/group-programming-lab/PySysTools.git
cd PySysTools

# 2. Crear entorno virtual (recomendado)
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar el paquete en modo editable
pip install -e .
```

### Verificar la instalación

```bash
sysadmin_utils --help
```

---

## ▶️ Usage

PySysTools expone una CLI principal a través del comando `sysadmin_utils`. A continuación se muestran los comandos disponibles por módulo:

### 🔐 Seguridad

```bash
# Generar una contraseña segura de 20 caracteres
sysadmin_utils gen-pass -l 20

# Escanear un directorio en busca de archivos maliciosos
sysadmin_utils scan-malware "C:/Users/usuario/Downloads"
```

### 🌐 Red

```bash
# Iniciar monitoreo de red en tiempo real
sysadmin_utils net-monitor
```

### 🖥️ Sistema

```bash
# Ver estado general de recursos del sistema
sysadmin_utils sys-status
```

### Uso como librería en Python

```python
from sysadmin_utils.security import generate_password
from sysadmin_utils.network import monitor_network
from sysadmin_utils.system import get_system_info

# Generar contraseña
password = generate_password(length=20)

# Obtener info del sistema
info = get_system_info()
print(info)
```

---

## 📁 Project Structure

```
PySysTools/
│
├── data/                        # Muestras de datos CSV para pruebas y demos
│
├── diagrams/                    # Diagramas de arquitectura en formato Mermaid
│
├── docs/                        # Documentación técnica extendida del proyecto
│
├── examples/                    # Scripts de ejemplo para integración de la librería
│
├── src/
│   └── sysadmin_utils/          # Paquete principal instalable
│       ├── data/                # Módulo de conexión y operaciones con MySQL/pandas
│       ├── network/             # Módulo de monitoreo y análisis de red (SMB, interfaces)
│       ├── security/            # Módulo de seguridad: generador de passwords, scanner
│       ├── system/              # Módulo de monitoreo del sistema vía psutil
│       ├── ui/                  # Componentes de interfaz de usuario / notificaciones
│       └── utils/               # Funciones auxiliares y helpers compartidos
│
├── .flake8                      # Configuración del linter flake8
├── .gitignore                   # Archivos excluidos del control de versiones
├── LICENSE                      # Licencia MIT
├── requirements.txt             # Dependencias del proyecto
└── setup.py                     # Configuración de empaquetado con setuptools
```

> **Nota:** El directorio `tests/` con la suite completa de pruebas unitarias e integración, así como el archivo `.gitlab-ci.yml` del pipeline CI/CD, están disponibles en el repositorio completo de GitLab.

---

## 🔐 Security

PySysTools incorpora consideraciones de seguridad en múltiples niveles:

**Análisis estático de código:** El proyecto utiliza `bandit` como herramienta de SAST (Static Application Security Testing) en el pipeline CI/CD para detectar patrones de código inseguros antes de cada merge.

**Módulo de seguridad defensiva:** Las herramientas incluidas (escaneo de malware, análisis de hash) están orientadas a la detección y auditoría, no a la ejecución de código malicioso. Todo escaneo opera sobre rutas locales autorizadas.

**Gestión de credenciales:** No se almacenan credenciales en el código fuente. Las configuraciones sensibles deben gestionarse mediante variables de entorno o archivos de configuración externos excluidos del repositorio (`.gitignore` configurado).

**Principio de menor privilegio:** Se recomienda ejecutar la herramienta con los permisos mínimos necesarios para cada tarea específica.

**Contexto ético de uso:** Esta suite está diseñada para administración legítima de infraestructura propia. Cualquier uso sobre sistemas de terceros sin autorización escrita constituye una violación ética y potencialmente legal.

---

## 🌐 Repository Architecture

Este proyecto sigue una arquitectura de repositorio distribuido optimizada para flujos DevSecOps:

| Plataforma | Rol | Contenido |
|---|---|---|
| **GitLab** | Laboratorio completo + CI/CD | Código fuente íntegro, tests, pipeline, ramas de desarrollo |
| **GitHub** | Portafolio y presentación | Versión optimizada, documentación, demos públicas |

El desarrollo principal ocurre en GitLab, donde reside el ecosistema completo con pipeline de integración continua (linting con `flake8`, pruebas con `pytest`, análisis SAST con `bandit`). GitHub actúa como vitrina profesional del proyecto.

La sincronización entre ambas plataformas se gestiona mediante el script `publish_public.ps1`, que exporta una versión limpia y optimizada hacia el repositorio público de GitHub.

---

## 🔗 Full Source Code

El código fuente completo, incluyendo todos los módulos, suite de tests y pipeline CI/CD, está disponible en:

👉 **[https://gitlab.com/group-programming-lab/PySysTools](https://gitlab.com/group-programming-lab/PySysTools)**

---

## 🚀 Roadmap

- [ ] Soporte multiplataforma completo para Linux/macOS (módulos de notificaciones)
- [ ] Integración con APIs de VirusTotal para análisis de hashes en la nube
- [ ] Módulo de gestión de logs con parsing automatizado de formatos comunes
- [ ] Dashboard web ligero con Flask para visualización de métricas del sistema
- [ ] Soporte para exportación de reportes en PDF y JSON
- [ ] Integración con SIEM mediante syslog o webhooks
- [ ] Autenticación y roles para entornos multiusuario
- [ ] Publicación del paquete en PyPI
- [ ] Cobertura de tests al 80%+ documentada en pipeline
- [ ] Soporte para Docker y despliegue containerizado

---

## 📄 License

Este proyecto está licenciado bajo la **MIT License**.

Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

## 👨‍💻 Author

**Sebastian Zhunaula**

Desarrollador de software con enfoque en automatización de sistemas, seguridad defensiva y herramientas DevSecOps. Apasionado por la construcción de utilidades robustas para administración de infraestructura empresarial.

- 🐙 GitHub: [@devsebastian44](https://github.com/devsebastian44)
- 🦊 GitLab: [@group-programming-lab](https://gitlab.com/group-programming-lab)

---

<div align="center">
  <sub>Built with 🛠️ by Sebastian Zhunaula · MIT License · 2026</sub>
</div>