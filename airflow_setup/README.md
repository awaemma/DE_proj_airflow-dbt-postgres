# README: Setting Up Apache Airflow with Astronomer

This README provides instructions on how to set up and start an Apache Airflow service locally using Astronomer. The setup includes initializing the Airflow environment with essential components and accessing the Airflow UI.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Astronomer CLI](https://docs.astronomer.io/astro/cli/install-cli)

### Project Contents

Your Astronomer project contains the following files and folders:

- **dags/**: Contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
  - `example_astronauts`: A simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. This DAG uses the TaskFlow API to define tasks in Python and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see the [Getting started tutorial](https://docs.astronomer.io/learn/get-started-with-airflow).
- **Dockerfile**: Contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- **include/**: Contains any additional files that you want to include as part of your project. It is empty by default.
- **packages.txt**: Allows you to install OS-level packages needed for your project by adding them to this file. It is empty by default.
- **requirements.txt**: Allows you to install Python packages needed for your project by adding them to this file. It is empty by default.
- **plugins/**: Add custom or community plugins for your project to this file. It is empty by default.
- **airflow_settings.yaml**: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

## Deploy Your Project Locally

### Steps to Start the Apache Airflow Service

1. **Start Airflow on your local machine:**

    ```bash
    astro dev start
    ```

    This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

    - **Postgres**: Airflow's Metadata Database
    - **Webserver**: The Airflow component responsible for rendering the Airflow UI
    - **Scheduler**: The Airflow component responsible for monitoring and triggering tasks
    - **Triggerer**: The Airflow component responsible for triggering deferred tasks

2. **Verify that all 4 Docker containers were created by running:**

    ```bash
    docker ps
    ```

    You should see containers running for the Postgres, Webserver, Scheduler, and Triggerer components.

3. **Access the Airflow UI for your local Airflow project:**

    Open your web browser and go to `http://localhost:8080/`. Log in with the following credentials:

    - **Username**: `admin`
    - **Password**: `admin`

    You should also be able to access your Postgres Database at `localhost:5432/postgres`.

4. **How to run the Dags:**

    Once the webserver is on, select any dag of choice and then run it by clicking on the play icon. The schedule within the dag is currently set to None so it has to be triggered manually. However, you can change this behaviour by setting the dag to automatically run at a desired time of choice, e.g @daily, @weekly e.t.c.


### Troubleshooting

- **Port Conflicts**: Running `astro dev start` will start your project with the Airflow Webserver exposed at port `8080` and Postgres exposed at port `5432`. If you already have either of those ports allocated, you can either stop your existing Docker containers or change the port.
---
