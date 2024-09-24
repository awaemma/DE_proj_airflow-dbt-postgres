# README: Setting Up PostgreSQL Service with Docker Compose

This README provides instructions on how to set up and start a PostgreSQL service using Docker Compose. The setup includes initializing a PostgreSQL database with a specific user, password, and database name, and loading an initial SQL script.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Docker Compose File Overview

The `docker-compose.yml` file defines a PostgreSQL service with the following configurations:

- **Image**: The service uses the latest PostgreSQL image.
- **Environment Variables**:
  - `POSTGRES_USER`: The username for the PostgreSQL database.
  - `POSTGRES_PASSWORD`: The password for the PostgreSQL database.
  - `POSTGRES_DB`: The name of the database to be created.
- **Ports**: The PostgreSQL service is exposed on port `5434` on the host machine, mapping to port `5432` in the container.
- **Volumes**:
  - `./pg_data:/var/lib/postgresql/data`: Maps a local directory for persistent PostgreSQL data storage.
  - `./data:/data`: Maps a local directory for additional data.
  - `./infra_setup/init.sql:/docker-entrypoint-initdb.d/init.sql`: Maps a local SQL file for database initialization.

## Starting and Managing the PostgreSQL Service
- Navigate to the directory containing your docker-compose.yml file:
```bash
cd /path/to/project-directory
```
- Run the following command to start the PostgreSQL service:
```bash
docker-compose up -d
```
The -d flag runs the containers in detached mode, meaning they will run in the background.

- The -d flag runs the containers in detached mode, meaning they will run in the background.
```bash
docker ps
```
You should see a container running with the name project-directory_postgres_1.
- You can connect to the PostgreSQL database using a PostgreSQL client like psql, DBeaver, or any other SQL client. Use the following connection details assuming this was not changed in the docker-compose file:
   - Host: localhost
   - Port: 5434
   - Username: alt_school_user
   - Password: secretPassw0rd
   - Database: ecommerce

- To stop the PostgreSQL service, run:
```bash
docker-compose down
```
 

## Directory Structure

Ensure your project directory is structured as follows:

```plaintext
project-directory/
│
├── docker-compose.yml
├── pg_data/             # Directory for PostgreSQL data (automatically created if it doesn't exist)
├── data/                # Directory that holds the data to be loaded into the ecommerce db 
└── infra_setup/
    └── init.sql         # SQL file for creating all the required database objects and loading the files



