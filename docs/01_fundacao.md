# Fase 1 — Fundação

## Objetivo

Preparar o ambiente e criar, de forma reproduzível, a base do projeto Cruzeiro Analytics.

## Ambiente preparado

- Python e ambiente virtual `.venv`
- Docker Desktop e SQL Server em container
- SSMS conectado ao SQL Server em `localhost,1433`
- Git local conectado ao repositório no GitHub

## Banco CruzeiroAnalytics

O script `sql/ddl/001_create_database.sql` verifica se o banco
`CruzeiroAnalytics` existe e o cria quando necessário.

Executamos o script no SSMS e confirmamos que `CruzeiroAnalytics`
apareceu na lista de bancos de dados. O script foi registrado em um
commit e enviado à branch `main` no GitHub.

## Estrutura inicial do projeto

- `infra/`: configuração dos serviços locais, como o SQL Server no Docker.
- `sql/ddl/`: scripts que criam a estrutura do banco de dados.
- `src/cruzeiro_analytics/`: código Python do projeto.
- `docs/`: explicações e decisões do projeto.
- `.venv/`: ambiente Python local; não deve ser enviado ao Git.

## Pendências desta fase
- Revisar e versionar `infra/docker-compose.yml`.
- Completar a documentação da configuração do ambiente.