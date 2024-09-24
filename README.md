# Project Overview

This repository contains three main directories that work together to manage the end to end data engineering project. Each project is housed in its respective directory and includes a dedicated README file for detailed instructions, usage, and configuration. Below is a summary of each project. 
A typical flow of the project would be to start the postgres service, then airflow and dbt.

## 1. Postgres

The **Postgres** project is focused on setting up and managing the PostgreSQL database, which serves as the primary data storage solution. This project includes scripts and configurations necessary for initializing the database, managing schemas, and performing data operations.

- **Location:** `./postgres`
- **Details:** [Postgres README](./postgres_setup/README.md)

## 2. Airflow

The **Airflow** project is designed to orchestrate and automate data workflows. Apache Airflow is used to create, schedule, and monitor data pipelines, ensuring that data is moved and processed correctly between systems.

- **Location:** `./airflow`
- **Details:** [Airflow README](./airflow_setup/README.md)

## 3. dbt

The **dbt** (Data Build Tool) project is responsible for transforming raw data into a format suitable for analysis. dbt models are used to clean, aggregate, and transform data, which is then stored in a structured and accessible format.

- **Location:** `./dbt`
- **Details:** [dbt README](./dbt_setup/README.md)

---
