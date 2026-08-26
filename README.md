# Cruzeiro Analytics ⚽💙

End-to-end football data analytics project focused on **Cruzeiro Esporte Clube**.

The project aims to build a complete data platform covering data ingestion, transformation, modeling, orchestration and visualization while applying modern Data Engineering and Business Intelligence concepts.

## 🎯 Project Goals

* Consume football data from REST APIs
* Build a Medallion Architecture (Bronze, Silver and Gold)
* Develop ETL/ELT pipelines using Python
* Store analytical data using SQL Server
* Use Parquet and DuckDB for analytical processing
* Implement automated data quality checks
* Build a dimensional data model
* Orchestrate data pipelines using Apache Airflow
* Create a Power BI semantic model
* Develop the **Cruzeiro 360** dashboard
* Automate the complete data pipeline
* Apply Git and GitHub for version control and project documentation

## 🏗️ Architecture

```text
                    Football REST API
                            |
                            v
                    Python Ingestion
                            |
                            v
                    Bronze Layer
                      Raw JSON
                            |
                            v
                Python + DuckDB
                            |
                            v
                    Silver Layer
                       Parquet
                            |
                            v
                  Python + SQL
                            |
                            v
                     Gold Layer
                     SQL Server
                            |
                            v
                       Power BI


              Apache Airflow
          orchestrates the pipeline
```

The project follows the **Medallion Architecture**, separating raw, processed and analytics-ready data into different layers.

## 🛠️ Technologies

* Python
* SQL Server
* DuckDB
* Apache Parquet
* Apache Airflow
* Docker
* Power BI
* Git
* GitHub

## 🥉 Bronze Layer

The Bronze layer stores the raw data exactly as received from the source APIs.

Its main purpose is to preserve the original source data, enabling auditing, historical tracking and data reprocessing when necessary.

**Format:** JSON

## 🥈 Silver Layer

The Silver layer contains cleaned, standardized, typed and normalized data.

In this layer, the project will perform operations such as:

* Data type conversion
* JSON flattening
* Duplicate removal
* Null value treatment
* Date and time standardization
* Business rule application
* Data quality validation

**Format:** Apache Parquet

DuckDB will be used to query and analyze the Parquet files using SQL.

## 🥇 Gold Layer

The Gold layer contains the analytical data model prepared for consumption by Power BI.

A dimensional model will be implemented using fact and dimension tables.

Examples of planned tables include:

```text
Dimensions

dim_date
dim_team
dim_player
dim_competition
dim_season
dim_stadium
dim_coach

Facts

fact_match
fact_player_match
fact_match_event
fact_standings_snapshot
```

The Gold layer will be stored in **SQL Server**.

## 🔄 Orchestration

Apache Airflow will be used to orchestrate and monitor the data pipelines.

The orchestration layer will be responsible for:

* Scheduling pipeline executions
* Managing task dependencies
* Handling retries and failures
* Monitoring pipeline execution
* Centralizing execution logs
* Running daily and post-match data updates

Airflow will be introduced after the ingestion, transformation and loading processes are developed and understood individually.

## 📊 Analytics

The final analytical product will be a Power BI dashboard called:

# Cruzeiro 360

The dashboard is planned to include analyses such as:

* Season overview
* Match results
* Goals scored and conceded
* Home vs. away performance
* Performance by competition
* League standings evolution
* Players statistics
* Top scorers and assists
* Match details
* Lineups and formations
* Recent form
* Historical season comparisons
* Data pipeline quality and monitoring

## 🚧 Project Status

**Under development**

Current phase:

**Phase 1 — Project Foundation**

## 🗺️ Roadmap

* [ ] **Phase 1 — Foundation**
* [ ] **Phase 2 — First Data Ingestion**
* [ ] **Phase 3 — Bronze Layer**
* [ ] **Phase 4 — Silver Layer**
* [ ] **Phase 5 — Gold Layer**
* [ ] **Phase 6 — Orchestration with Apache Airflow**
* [ ] **Phase 7 — Power BI**
* [ ] **Phase 8 — Evolution**

### Phase 1 — Foundation

* [x] Create GitHub repository
* [x] Configure Python
* [ ] Create virtual environment
* [ ] Install SQL Server
* [ ] Create `CruzeiroAnalytics` database
* [ ] Define project folder structure
* [ ] Configure environment variables
* [ ] Prepare initial documentation

## 📚 Learning Objectives

This project is also designed as a practical learning environment for developing skills in:

* Data Engineering
* Python
* SQL
* REST APIs
* ETL/ELT development
* Data Lake concepts
* Medallion Architecture
* Dimensional Modeling
* Data Quality
* Workflow Orchestration
* Power BI
* Git and GitHub

The project will evolve incrementally, with each component being implemented, tested and documented before moving to the next stage.

## ⚠️ Disclaimer

This is an independent educational and portfolio project.

It is not officially affiliated with, endorsed by or connected to **Cruzeiro Esporte Clube**.

All football data used in the project will originate from publicly accessible or properly licensed data sources.
