# Cruzeiro Analytics ⚽💙

End-to-end football data analytics project focused on Cruzeiro Esporte Clube.

The project aims to build a complete data platform, covering data ingestion, transformation, modeling, orchestration and visualization.

## Project Goals

- Consume football data from REST APIs
- Build a Medallion Architecture (Bronze, Silver and Gold)
- Develop ETL/ELT pipelines using Python
- Store analytical data using SQL Server
- Use Parquet and DuckDB for analytical processing
- Implement data quality checks
- Build a dimensional model
- Create a Power BI semantic model
- Develop the Cruzeiro 360 dashboard
- Automate and orchestrate the complete pipeline

## Architecture
```text
Football API
     |
     v
Python Ingestion
     |
     v
Bronze - JSON
     |
     v
Silver - Parquet
     |
     v
SQL Server - Gold
     |
     v
Power BI
```
## Technologies

Python
SQL Server
DuckDB
Parquet
Git / GitHub
Power BI
Prefect
Architecture

The project follows the Medallion Architecture:

## Bronze

Raw data exactly as received from the source APIs.

## Silver

Cleaned, standardized and normalized data stored in Parquet format.

## Gold

Dimensional analytical model containing facts and dimensions ready for consumption by Power BI.

## Project Status

🚧 Under development

Current phase:

Phase 1 - Project Foundation

Roadmap
 Phase 1 - Foundation
 Phase 2 - First Data Ingestion
 Phase 3 - Bronze Layer
 Phase 4 - Silver Layer
 Phase 5 - Gold Layer
 Phase 6 - Orchestration
 Phase 7 - Power BI
 Phase 8 - Evolution
Disclaimer

This is an independent educational project and is not officially affiliated with Cruzeiro Esporte Clube.
