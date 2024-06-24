# Usage Examples

This document provides examples of how to interact with each microservice in the RusticPy Nexus project.

## Data Ingestion

### Fetching Data
Send a POST request to fetch data from an API:
```sh
curl -X POST http://localhost:5000/fetch -d '{"source": "api"}'
```

## Processing Core

### Processing Data
Send a POST request to process data using the Rust-powered core:
```sh
curl -X POST http://localhost:5001/process -d '{"data": [1, 2, 3, 4]}'
```

## Visualization

### Viewing Dashboard
Access the data visualization dashboard via web browser:
- URL: `http://localhost:5002`

## AI Model Creation

### Training a Model
Send a POST request to train a machine learning model:
```sh
curl -X POST http://localhost:5003/train -d '{"data": [[0.1, 0.2], [0.2, 0.3]], "target": [0, 1]}'
```

## Example Outputs

### Data Ingestion Response
Upon successful data fetch, you'll receive a JSON response:
```json
[1, 2, 3, 4, 5]
```

### Processing Core Output
Processed data will return transformed, aggregated, and analyzed results:
```json
{
  "transformed": [2, 4, 6, 8],
  "aggregated": 20,
  "analysis": 5.0
}
```

### AI Model Training Result
After training, you'll receive the accuracy score of the trained model:
```json
{
  "accuracy": 0.85
}
```

These examples illustrate how to interact with each microservice in the RusticPy Nexus project, showcasing the integration of Rust and Python for efficient data processing, visualization, and machine learning tasks.
```

### Explanation:
- **Data Ingestion**: Demonstrates how to fetch data using a POST request to the `/fetch` endpoint.
- **Processing Core**: Shows how to process data by sending a POST request to the `/process` endpoint, which utilizes Rust for intensive computations.
- **Visualization**: Provides guidance on accessing the visualization dashboard through a web browser.
- **AI Model Creation**: Details the process of training a machine learning model by sending a POST request to the `/train` endpoint.
- **Example Outputs**: Gives example JSON responses for each service to illustrate the expected outputs or results.
