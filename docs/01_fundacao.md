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

## Configuração local do SQL Server

O serviço SQL Server está definido em `infra/docker-compose.yml`.
Ele usa a imagem SQL Server 2025 Developer, publica a porta `1433`
e guarda os dados no volume Docker `sqlserver_data`.

A senha é fornecida pela variável `MSSQL_SA_PASSWORD`. O arquivo
`infra/.env.example` mostra qual variável deve ser preenchida.
Em uma nova instalação, copie esse exemplo para `infra/.env` e
defina uma senha própria nesse novo arquivo.

O `.gitignore` exclui `.env` e `.venv` do Git. Assim, a configuração
pode ser compartilhada sem enviar a senha nem o ambiente Python.

Na raiz do projeto, este comando valida o Compose sem imprimir
a configuração com a senha expandida:

```powershell
docker compose --env-file infra/.env -f infra/docker-compose.yml config --quiet
```

O comando terminou sem erros nesta instalação. O banco
`CruzeiroAnalytics` foi criado depois, pela execução do script
`sql/ddl/001_create_database.sql` no SSMS.

## Como iniciar em uma nova instalação

Depois de copiar `infra/.env.example` para `infra/.env` e definir a
senha, execute na raiz do projeto:

```powershell
docker compose --env-file infra/.env -f infra/docker-compose.yml up -d
```

Quando o SQL Server estiver pronto, conecte o SSMS a `localhost,1433`
com o usuário `sa` e a senha definida em `infra/.env`. Abra e execute
`sql/ddl/001_create_database.sql`; depois atualize a lista de bancos
para confirmar que `CruzeiroAnalytics` aparece.