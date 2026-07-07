# QueryMind: AI-Powered Data Analytics Engine
## Project Overview
A more robust ETL pipeline with a more personalised dashboard and an integrated AI layer which processes questions asked in natural language and produces results, explanations and downloadable graphs.

This project is an interation of the previous [Data Analytics Pipeline project](https://github.com/AnoukDunu/DataFlow-Analytics-Pipeline), but as not everyone is comfortable with integrating frontier or local LLMs to interact with sensitive databases, this is framed as a completely new project.

## Project Features

- End-to-end ETL pipeline
- Dashboard for interactive data visualisation
- Local AI/LLM to process natural language and generate information
- AI/LLM generated graphs depending on query
- AI/LLM safeguards implemented to ensure safe queries 
- Modular project structure
- Data transformation using Pandas
- PostgreSQL database integration
- Data quality checks before loading
- Centralised logging system
- REST API based data ingestion/extraction


## Pipeline Architecture

API → Extract → Staging Table → Transform → Quality Checks → Final Table → Dashboard → AI/LLM

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
1. Follow the [instructions](https://github.com/AnoukDunu/DataFlow-Analytics-Pipeline#setup-instructions-mac) from the previous Data Analytics Pipeline project to get the pipeline up and running
2. Download and install Ollama from the [official website](https://ollama.com/download) or copy paste the following commands in the terminal.

   - Mac/Linux:
   ```
   curl -fsSL https://ollama.com/install.sh | sh
   ```
   - Windows:
   ```
   irm https://ollama.com/install.ps1 | iex
   ```
   (The official documentation is very detailed, so I don't see the need to re-iterate it here)
   
3. Choose and download an LLM from the Ollama app or [website](https://ollama.com/search).
4. In the ai/llm.py file, replace the variable 'model' with your chosen LLM/SLM.

<img width="422" height="216" alt="Screenshot 2026-07-07 at 4 28 28 pm" src="https://github.com/user-attachments/assets/7bb82a0a-3d85-49b8-bdbe-ece3cb47e268" />

5. While Ollama is running in the background, use the following command in your project's root:
```
PYTHONPATH=src streamlit run dashboard/app.py
```

## Screenshots
<img width="2856" height="1616" alt="WhatsApp Image 2026-07-07 at 12 29 10" src="https://github.com/user-attachments/assets/dda65111-4e45-4ed1-a967-0fb7bd524218" />

<img width="1428" height="808" alt="Screenshot 2026-07-07 at 12 31 23 pm" src="https://github.com/user-attachments/assets/5611236e-2dfe-42bf-ac97-872fe000948e" />

## Future Implementations/Improvements

- Develop a cleaner UI for the front-end
- Upgrade project to use Airflow (with Docker) or Cron
- Add the option to use Frontier models via API (but doubt I will implement this)

## ⚠️ Troubleshooting
- The Ollama application or a terminal instance needs to run simultaneously with the pipeline for the AI layer to function
- Consider your hardware when running LLMs/SLMs due to larger models with higher parameters requiring significant resources 


