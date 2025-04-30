# Airflow_poc

🎵 Spotify ETL & Analytics Pipeline using Apache Airflow

This project demonstrates a Proof of Concept (PoC) for building an automated ETL pipeline to extract and analyze data from Spotify using the Spotify Web API, with orchestration powered by Apache Airflow.

📌 Overview

The ETL pipeline performs the following tasks:

Extracts data for a list of Spotify artists.
Transforms the data to a structured format.
Loads the data into a MySQL database (can be replaced or extended).
The entire process is scheduled and automated using Airflow.

⚙️ Project Structure

📁 Spotify_ETL_Airflow_PoC/
├── Spotify_Etl.py              # Core ETL script (Extract, Transform)
├── Spotify_Dag.py              # Airflow DAG to orchestrate the pipeline
├── Artists_Urls.txt            # Input list of Spotify artist URLs
├── README.md                   # Project documentation

📈 Features

🔗 Connects to the Spotify API using client credentials
🎤 Fetches artist metadata and top tracks
💾 Stores structured data for downstream analytics
⏰ Orchestrates workflows using Apache Airflow
📚 Easy-to-extend and modular codebase

🧠 ETL Breakdown

Extraction :
  Parses artist IDs from Artists_Urls.txt
  Authenticates with Spotify API
  Retrieves artist metadata and top tracks
Transformation :
  Converts raw JSON into clean pandas DataFrames
  Handles missing/null fields
Loading :
  (Optional) Loads the final data into a MySQL database or saves as CSV



📅 DAG Details

Name : spotify_etl_dag
Schedule : Daily (configurable)
Tasks :
  start
  run_spotify_etl (calls Spotify_Etl.py)
  end
  

