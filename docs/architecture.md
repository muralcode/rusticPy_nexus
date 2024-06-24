# Project Architecture

## Overview
The data processing pipeline consists of four microservices:
1. Data Ingestion
2. Processing Core
3. Visualization
4. AI Model Creation

Each service is containerized using Docker and orchestrated with Docker Compose.

## Components
- **Data Ingestion**: Fetches and preprocesses raw data.
- **Processing Core**: Performs intensive data processing using Rust for computational tasks.
- **Visualization**: Generates and serves visualizations of processed data.
- **AI Model Creation**: Trains and evaluates machine learning models using processed data.

## Communication
Services communicate via REST APIs, and data is passed between services using JSON.
