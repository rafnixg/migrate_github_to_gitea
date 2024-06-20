# Migrate Github repositories to Gitea

Este proyecto permite migrar repositorios de GitHub a Gitea de manera automatizada.

## Pre-requisitos

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Este proyecto ha sido probado con Python 3.8.

## Instalación

Para instalar las dependencias necesarias, sigue estos pasos:

1. Clona este repositorio:

```sh
git clone https://tu-repositorio/migrate_github_to_gitea.git
cd migrate_github_to_gitea
```
2. Instala las dependencias utilizando pip. Es recomendable hacerlo dentro de un entorno virtual:

```sh
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el script, necesitas configurar las variables de entorno necesarias. Puedes hacerlo copiando el archivo `.env.example` a un nuevo archivo llamado `.env` y modificando los valores según corresponda:
```sh
cp .env.example .env
```
Edita el archivo `.env` con tus credenciales de GitHub y Gitea.

## Ejecución
Para iniciar la migración de los repositorios, ejecuta el siguiente comando:

```sh
python main.py
```

Este comando iniciará el proceso de migración según las configuraciones definidas en tu archivo `.env` y los scripts de migración implementados.

## Scripts adicionales
Este proyecto también incluye scripts de shell para interactuar con la API de Gitea:

- `gitea-migrate.sh`: Para migrar repositorios a Gitea.
- `gitea-delete-repos.sh`: Para eliminar repositorios de Gitea.

Para ejecutar estos scripts, primero asegúrate de que sean ejecutables:

```sh
chmod +x gitea-migrate.sh gitea-delete-repos.sh
```

Luego, puedes ejecutarlos directamente desde la terminal:

```sh
./gitea-migrate.sh
./gitea-delete-repos.sh
```

Asegúrate de haber configurado las variables de entorno necesarias antes de ejecutar estos scripts
