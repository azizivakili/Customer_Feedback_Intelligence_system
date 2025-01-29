from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlite3

# Define the ETL functions
def extract_data():
    input_path = '/home/azizi/airflow_home/data/raw/sentiment-analysis.csv'
    df = pd.read_csv(input_path)
    df.to_csv('/home/azizi/airflow_home/data/processed/extracted.csv', index=False)

def transform_data():

    # Load the raw data
    input_path = '/home/azizi/airflow_home/data/processed/extracted.csv'
    output_path = '/home/azizi/airflow_home/data/processed/transformed.csv'
    df = pd.read_csv(input_path)
    
    # Define lists of keywords for sentiment analysis
    positive_keywords = ['great', 'good', 'excellent', 'amazing', 'love', 'wonderful', 'fantastic', 'awesome', 'satisfied']
    negative_keywords = ['bad', 'poor', 'terrible', 'awful', 'hate', 'worst', 'disappoint', 'horrible', 'not satisfied']
    
    # Define a function to classify sentiment
    def classify_sentiment(text):
        text = text.lower()  # Convert text to lowercase
        if any(word in text for word in positive_keywords):
            return 'Positive'  # Classify as Positive
        elif any(word in text for word in negative_keywords):
            return 'Negative'  # Classify as Negative
        else:
            return 'Neutral'   # Classify as Neutral if no keywords match

    # Apply sentiment classification to the `Text` column
    df['PredictedSentiment'] = df['Text'].apply(classify_sentiment)

    # Save the transformed data to a new CSV file
    df.to_csv(output_path, index=False)


def load_data():
    input_path = '/home/azizi/airflow_home/data/processed/transformed.csv'
    conn = sqlite3.connect('/home/azizi/airflow_home/data/processed/feedback.db')
    df = pd.read_csv(input_path)
    df.to_sql('feedback', conn, if_exists='replace', index=False)
    conn.close()

# Define the DAG
default_args = {'start_date': datetime(2025, 1, 1)}
with DAG('feedback_etl', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    extract_task = PythonOperator(task_id='extract_data', python_callable=extract_data)
    transform_task = PythonOperator(task_id='transform_data', python_callable=transform_data)
    load_task = PythonOperator(task_id='load_data', python_callable=load_data)

    extract_task >> transform_task >> load_task

