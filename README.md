# Customer Feedback Intelligence System
In this project, we are going to analyze customer feedback through Airflow pipelineing.
I’ll guide you step-by-step to set up and execute an ETL pipeline with Apache Airflow as if you’re a beginner. We’ll go from scratch, including installing Airflow, creating ETL pipeline, running it, and visualizing the results. Let's dive in!

## Step 1: Set Up Apache Airflow

Install Prerequisites:
Ensure you have Python (3.7–3.10) installed.
Install pip (Python's package manager).

Install Apache Airflow:
Create a virtual environment:
```
python -m venv airflow_env
source airflow_env/bin/activate  # Linux/Mac
```

Install Airflow (use version 2.6.0):
```
pip install apache-airflow
```

Initialize Airflow:

Set up the Airflow home directory:
```
export AIRFLOW_HOME=~/airflow  # Linux/Mac
```

Initialize Airflow's metadata database:
```
airflow db init
```
Create an Admin User:

Create a user to access the Airflow web UI:
```
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```
Start Airflow:
Run the web server and scheduler:
```
airflow webserver --port 8080
airflow scheduler
```
Access Airflow UI:
[ http://localhost:8080.]

## Step 2: Set Up the Project Structure

Let’s organize the project to keep it clean:
```
project_root/
├── airflow_home/                     # Airflow directory
│   ├── dags/                         # DAG files for workflows
│   │   └── feedback_etl_dag.py       # Our ETL pipeline
│   └── data/                         # Data files
│       ├── raw/                      # Raw input files
│       │   └── sentiment-analysis.csv
│       └── processed/                # Processed/Transformed data

```
## Step 3: Write the ETL Pipeline (Airflow DAG)
### 1. Create the DAG File:
In the **airflow_home/dags/** directory, create a file called    **feedback_etl_dag.py**
### 2. Define the DAG:
Add the following Python script to define the pipeline :

**Note:** from the following link you can reach to code 

[feedback_etl_dag.py](https://github.com/azizivakili/Customer_Feedback_Intelligence_system/blob/main/dags/feedback_etl_dag.py)



### Step 4: Test the ETL Pipeline

Restart the Airflow scheduler and webserver:
```
airflow scheduler
airflow webserver --port 8080
```
Log in to the Airflow UI at http://localhost:8080.

## Step 5: Create a Dashboard to Visualize Data

1. Install Streamlit:
```
pip install streamlit
```
2. Create the Dashboard:

In the dashboard/ folder, create a file **app.py** with the following:

[app.py](https://github.com/azizivakili/Customer_Feedback_Intelligence_system/blob/main/dashboard/app.py)

3. Run the Dashboard:
```
streamlit run dashboard/app.py
```

## step 6: See the final result 

[Airflow Pipeline](https://github.com/azizivakili/Customer_Feedback_Intelligence_system/blob/main/Images/Airflow-Pipeline.png)


[Visualization of Dashboard](https://github.com/azizivakili/Customer_Feedback_Intelligence_system/blob/main/Images/Dashboard.png)

