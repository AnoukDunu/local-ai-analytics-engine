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

~- Include safety measures for LLM (no DELETE, ALTER, CREATE priviledges)~

~- Fix Streamlit Buttons from refreshing entire session onclick~

~- Develop a ChatGPT style session-based chat with the local LLM and keep consisteny per session~

- Develop a cleaner UI for the front-end

- Upgrade project to use Airflow (with Docker) or Cron


local-ai-analytics-engine/
│
├── ai/                          # AI/LLM layer and logic
│   ├── db.py 
│   ├── guardrails.py
│   ├── llm.py
│   ├── pipeline.py
│   ├── query_engine.py
│   ├── response_generator.py
│   ├── schema.py
│   └── sql_generator.py
│
├── dashboard/                   # Streamlit dashboard
│   └── app.py 
│
├── data/                        # Optional: Local Data
│   └── data.csv 
│
├── logs/                        # Logs
│   └── pipeline.log 
│
├── src/
│   ├── config/                  # Configuration management
│   │   └── config.py
│   │
│   ├── database/                # Database connection logic
│   │   ├── connection.py
│   │   └── database schema
│   │
│   ├── extract/                 # Data ingestion layer
│   │   └── extract.py
│   │
│   ├── load/                    # Data loading logic
│   │   ├── load_final.py
│   │   └── load_staging.py
│   │
│   ├── transform/               # Data transformation logic
│   │   └── transform.py
│   │
│   ├── utilities/               #Reusable helpers
│   │   ├── logger.py
│   │   └── quality_checks.py
│   │   
│   └── main.py
│
├── .env                         # Environment variables (DB credentials)
├── README.md                    # Project dependencies
└── requirements.txt             # Project documentation



