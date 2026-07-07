# QueryMind: AI-Powered Data Analytics Engine
## Project Overview
A more robust ETL pipeline with a more personalised dashboard and an integrated AI layer which processes questions asked in natural language and produces results, explanations and downloadable graphs.

This project is an interation of the previous Data Analytics Pipeline project, but as not everyone is comfortable with integrating frontier or local LLMs to interact with sensitive databases, this is framed as a completely new project.

## Project Features

- End-to-end ETL pipeline
- Modular project structure
- Data transformation using Pandas
- PostgreSQL database integration
- Data quality checks before loading
- Centralised logging system
- REST API based data ingestion/extraction
- Dashboard for interactive data visualisation

## Pipeline Architecture

API → Extract → Staging Table → Transform → Quality Checks → Final Table → Dashboard

## Project Structure
<img width="597" height="888" alt="Screenshot 2026-07-07 at 4 10 48 pm" src="https://github.com/user-attachments/assets/8f2c56a4-b505-4def-a706-33c0e5b3d412" />

## Tech Stack
- Python
- PostgreSQL
- Streamlit
- REST API
- Ollama
- Local OpenSource LLMs/SLMs
- Apache AirFlow (Future implementation)

## Setup Instructions
- Mention how to install Ollama, LLM models etc.

## Screenshots
<img width="2856" height="1616" alt="WhatsApp Image 2026-07-07 at 12 29 10" src="https://github.com/user-attachments/assets/dda65111-4e45-4ed1-a967-0fb7bd524218" />

<img width="1428" height="808" alt="Screenshot 2026-07-07 at 12 31 23 pm" src="https://github.com/user-attachments/assets/5611236e-2dfe-42bf-ac97-872fe000948e" />

## Future Implementations/Improvements

- Develop a cleaner UI for the front-end

- Upgrade project to use Airflow (with Docker) or Cron



