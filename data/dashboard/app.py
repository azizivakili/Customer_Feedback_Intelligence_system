import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def load_data():
    conn = sqlite3.connect('/home/azizi/airflow_home/data/processed/feedback.db')
    df = pd.read_sql('SELECT * FROM feedback', conn)
    conn.close()
    return df

st.title('Customer Feedback Analysis')

data = load_data()

st.subheader('Feedback Sentiment Overview')
# Bar chart for positive and negative sentiment counts
sentiment_counts = data['Sentiment'].value_counts()
fig, ax = plt.subplots()
ax.bar(sentiment_counts.index, sentiment_counts.values, color=['red', 'green'])
ax.set_title('Sentiment Distribution')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
st.pyplot(fig)

st.subheader('Feedback Details')
st.dataframe(data)
