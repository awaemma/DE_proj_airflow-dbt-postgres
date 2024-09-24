# Setting Up and Using dbt with BigQuery

This guide will walk you through the steps to set up and use dbt (Data Build Tool) with BigQuery, using a service account JSON file for authentication.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [dbt CLI](https://docs.getdbt.com/docs/installation) (or dbt Cloud)

- Access to a Google Cloud Project with BigQuery enabled

## Step 1: Set Up a Service Account

1. **Create a Service Account**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to the "IAM & Admin" section and select "Service Accounts".
   - Create a new service account with appropriate permissions, such as "BigQuery Admin" or "BigQuery Data Editor".

2. **Download the Service Account Key**:
   - After creating the service account, download the JSON key file. This file will be used for authentication with BigQuery.

3. **Store the JSON Key Securely**:
   - Place the downloaded JSON file in a secure location on your machine.

## Step 2: Initialize dbt Project

1. **Navigate to Your Project Directory**:
   - Open a terminal and navigate to the directory where you want to initialize your dbt project.

    ```bash
    cd /path/to/your/project-directory
    ```
2. **Install Bigquery Adapter**:
    ```bash
    python -m pip install dbt-core dbt-bigquery
    ```

3. **Initialize dbt Project**:
   - Run the following command to initialize a new dbt project. During this process, specify BigQuery as your data warehouse and use the service account JSON file for authentication.

    ```bash
    dbt init your_dbt_project_name
    ```

    Follow the prompts to configure your profile, and when asked for authentication, specify the path to your service account JSON file.

## Step 3: Configure dbt Profiles

1. **Locate Your dbt Profiles File**:
   - The `profiles.yml` file is usually located in the `~/.dbt/` directory. Open this file in a text editor.

2. **Configure the BigQuery Profile**:
   - Update the `profiles.yml` file with the following configuration, ensuring you point to your service account JSON file:

    ```yaml
    my_profile:
      target: dev
      outputs:
        dev:
          type: bigquery
          method: service-account
          project: your-gcp-project-id
          dataset: your_dataset_name
          threads: 1
          keyfile: /path/to/your/service-account-file.json
          timeout_seconds: 300
          location: europe west1
          priority: interactive
          retries: 1
    ```

    - **project**: Replace with your Google Cloud Project ID.
    - **dataset**: Replace with the name of the BigQuery dataset you want to use.
    - **keyfile**: Replace with the path to your service account JSON file.
    - **location**: Specify the location of your BigQuery dataset (e.g., `europe west1`).

## Step 4: Run dbt Commands

1. **Test the Connection**:
   - Run the following command to test the connection between dbt and BigQuery:

    ```bash
    dbt debug --profile my_profile
    ```

    This command will verify that dbt can connect to your BigQuery instance using the service account.

2. **Run dbt Models**:
   - After setting up your dbt models, you can run them using the following command:

    ```bash
    dbt run --profile my_profile
    ```

## Step 5: Deploying dbt Models

1. **Materialize Models**:
   - To deploy your models as tables or views in BigQuery, define the materialization in your model files using `config()` blocks:

    ```sql
    {{config(materialized='table') }}

    SELECT *
    FROM your_source_table
    ```

2. **Execute the Deployment**:
   - Run `dbt run` again to materialize your models in BigQuery:

    ```bash
    dbt run
    ```
   - To run a specific model, use the below:
    ```bash
    dbt run --select model_file_name
    ```

---

