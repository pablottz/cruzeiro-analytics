# Cruzeiro Analytics ⚽💙

Projeto de análise de dados de futebol de ponta a ponta, com foco no **Cruzeiro Esporte Clube**.

O objetivo é construir uma plataforma completa de dados, contemplando desde a ingestão e armazenamento dos dados brutos até transformação, modelagem, orquestração e visualização das informações.

Além da construção de um produto analítico sobre o Cruzeiro, o projeto tem como objetivo servir como ambiente prático de aprendizado em **Engenharia de Dados, Python, SQL e Business Intelligence**.

## 🎯 Objetivos do Projeto

* Consumir dados de futebol através de REST APIs
* Construir uma arquitetura Medallion com camadas Bronze, Silver e Gold
* Desenvolver pipelines de ETL/ELT utilizando Python
* Trabalhar com arquivos JSON e Apache Parquet
* Utilizar DuckDB para processamento e consultas analíticas
* Armazenar o modelo analítico final em SQL Server
* Implementar processos de qualidade de dados
* Construir um modelo dimensional utilizando fatos e dimensões
* Implementar cargas incrementais
* Orquestrar os pipelines utilizando Apache Airflow
* Criar um modelo semântico no Power BI
* Desenvolver o dashboard **Cruzeiro 360**
* Automatizar o processo completo de atualização dos dados
* Utilizar Git e GitHub para versionamento e documentação do projeto

---

## 🏗️ Arquitetura

```text
                    REST API de Futebol
                            │
                            ▼
                    Ingestão com Python
                            │
                            ▼
                     Camada Bronze
                        JSON bruto
                            │
                            ▼
                  Python + DuckDB
                            │
                            ▼
                     Camada Silver
                         Parquet
                            │
                            ▼
                    Python + SQL
                            │
                            ▼
                      Camada Gold
                       SQL Server
                            │
                            ▼
                        Power BI


                   Apache Airflow
               Orquestração do Pipeline
```

O projeto seguirá os princípios da **Arquitetura Medallion**, separando os dados de acordo com seu nível de tratamento e finalidade.

---

## 🛠️ Tecnologias

* Python
* SQL Server
* DuckDB
* Apache Parquet
* Apache Airflow
* Docker
* Power BI
* Git
* GitHub

Outras bibliotecas e ferramentas poderão ser adicionadas conforme o projeto evoluir.

---

## 🥉 Camada Bronze

A camada Bronze será responsável por armazenar os dados brutos exatamente como forem recebidos das fontes.

Nesta camada, nenhuma regra de negócio deverá alterar o conteúdo original recebido da API.

O objetivo é preservar os dados de origem para permitir:

* auditoria;
* rastreabilidade;
* reprocessamento;
* investigação de problemas;
* comparação entre diferentes extrações.

**Formato principal:** JSON

Exemplo de organização:

```text
data/
└── bronze/
    └── api_football/
        ├── fixtures/
        ├── players/
        ├── events/
        ├── lineups/
        └── statistics/
```

---

## 🥈 Camada Silver

A camada Silver será responsável por transformar os dados brutos da Bronze em estruturas confiáveis, padronizadas e próprias para análise.

Nesta camada serão realizados processos como:

* leitura dos arquivos JSON;
* flatten de objetos e listas;
* conversão de tipos;
* tratamento de valores nulos;
* remoção de duplicidades;
* padronização de datas e horários;
* normalização dos dados;
* aplicação de regras de negócio;
* validações de qualidade;
* tratamento de registros inválidos.

**Formato principal:** Apache Parquet

O DuckDB será utilizado para realizar consultas SQL diretamente sobre os arquivos Parquet.

Exemplo:

```text
data/
└── silver/
    ├── partidas/
    ├── jogadores/
    ├── eventos/
    ├── escalacoes/
    └── estatisticas/
```

---

## 🥇 Camada Gold

A camada Gold será responsável por disponibilizar os dados em uma estrutura analítica preparada para consumo pelo Power BI.

Nesta camada será implementado um **modelo dimensional**, utilizando tabelas fato e dimensão.

O armazenamento principal será realizado no **SQL Server**.

### Dimensões planejadas

```text
dim_data
dim_time
dim_jogador
dim_competicao
dim_temporada
dim_estadio
dim_tecnico
dim_posicao
dim_resultado
```

### Fatos planejados

```text
fato_partida
fato_jogador_partida
fato_evento_partida
fato_classificacao_snapshot
fato_transferencia
```

A modelagem poderá sofrer alterações conforme conhecermos melhor os dados disponibilizados pelas fontes.

---

## 🔄 Orquestração

O **Apache Airflow** será utilizado para orquestrar e monitorar os pipelines do projeto.

Sua implementação acontecerá após os processos individuais de ingestão, transformação e carga estarem funcionando corretamente.

O Airflow será responsável por:

* organizar as etapas do pipeline;
* controlar dependências entre tarefas;
* criar agendamentos;
* executar retries em caso de falhas;
* monitorar execuções;
* centralizar logs;
* controlar cargas diárias;
* executar cargas pós-jogo;
* permitir reprocessamentos e backfills.

Fluxo esperado:

```text
Ingestão
   │
   ▼
Bronze
   │
   ▼
Silver
   │
   ▼
Qualidade dos Dados
   │
   ▼
Dimensões
   │
   ▼
Fatos
   │
   ▼
Validação da Gold
   │
   ▼
Power BI
```

---

## 📊 Cruzeiro 360

O produto analítico final do projeto será um dashboard desenvolvido no Power BI chamado:

# Cruzeiro 360

O dashboard deverá oferecer uma visão ampla sobre o desempenho esportivo do Cruzeiro.

Entre as análises planejadas estão:

* visão geral da temporada;
* partidas realizadas;
* vitórias, empates e derrotas;
* gols marcados e sofridos;
* saldo de gols;
* aproveitamento;
* desempenho como mandante e visitante;
* desempenho por competição;
* evolução mensal;
* forma recente;
* classificação por rodada;
* evolução da posição no campeonato;
* estatísticas dos jogadores;
* artilharia;
* assistências;
* participações em gols;
* escalações;
* formações utilizadas;
* detalhes das partidas;
* comparações entre temporadas.

Também será criada uma área dedicada ao acompanhamento da própria plataforma de dados, exibindo informações como:

* última atualização;
* quantidade de registros processados;
* status das execuções;
* falhas;
* qualidade dos dados;
* histórico das cargas.

---

## 📚 Objetivos de Aprendizado

O projeto também será utilizado como ambiente de aprendizado prático para desenvolver conhecimentos em:

### Engenharia de Dados

* Arquitetura Medallion
* Data Lake
* ETL/ELT
* REST APIs
* cargas incrementais
* pipelines de dados
* orquestração
* qualidade de dados
* logging
* modelagem dimensional

### Python

* consumo de APIs;
* manipulação de JSON;
* organização de projetos;
* tratamento de erros;
* funções reutilizáveis;
* orientação a objetos quando aplicável;
* manipulação de DataFrames;
* automação de processos;
* testes.

### SQL

* criação de bancos e schemas;
* DDL e DML;
* joins;
* CTEs;
* funções de janela;
* procedures;
* views;
* `MERGE`;
* constraints;
* modelagem dimensional;
* consultas analíticas;
* validação de qualidade.

### Business Intelligence

* modelagem semântica;
* relacionamentos;
* DAX;
* visualização de dados;
* storytelling;
* Power BI;
* criação de dashboards.

### DevOps e boas práticas

* Git;
* GitHub;
* controle de versão;
* documentação;
* Docker;
* testes automatizados;
* CI/CD.

---

## 🚧 Status do Projeto

**Em desenvolvimento**

Fase atual:

**Fase 1 — Fundação do Projeto**

---

## 🗺️ Roadmap

* [ ] **Fase 1 — Fundação**
* [ ] **Fase 2 — Primeira Ingestão**
* [ ] **Fase 3 — Camada Bronze**
* [ ] **Fase 4 — Camada Silver**
* [ ] **Fase 5 — Camada Gold**
* [ ] **Fase 6 — Orquestração com Apache Airflow**
* [ ] **Fase 7 — Power BI**
* [ ] **Fase 8 — Evolução**

### Fase 1 — Fundação

* [x] Criar repositório GitHub
* [ ] Configurar Python
* [ ] Criar ambiente virtual
* [ ] Instalar SQL Server
* [ ] Criar banco `CruzeiroAnalytics`
* [ ] Definir estrutura de pastas
* [ ] Criar arquivo `.env`
* [ ] Preparar documentação inicial

### Fase 2 — Primeira Ingestão

* [ ] Criar conta na API
* [ ] Identificar o Cruzeiro na API
* [ ] Consultar partidas do Cruzeiro
* [ ] Salvar o primeiro JSON
* [ ] Criar log de execução
* [ ] Analisar e documentar a resposta da API

### Fase 3 — Bronze

* [ ] Criar funções reutilizáveis
* [ ] Implementar endpoints
* [ ] Implementar paginação
* [ ] Implementar particionamento
* [ ] Controlar requisições
* [ ] Implementar retries
* [ ] Executar carga histórica

### Fase 4 — Silver

* [ ] Ler arquivos JSON
* [ ] Realizar flatten dos dados
* [ ] Aplicar tipagem
* [ ] Remover duplicidades
* [ ] Normalizar os dados
* [ ] Gravar arquivos Parquet
* [ ] Consultar Silver utilizando DuckDB
* [ ] Criar testes de qualidade

### Fase 5 — Gold

* [ ] Criar modelo estrela
* [ ] Criar dimensões
* [ ] Criar fatos
* [ ] Criar procedures de carga
* [ ] Implementar cargas incrementais
* [ ] Implementar `MERGE`
* [ ] Criar views analíticas
* [ ] Criar validações SQL

### Fase 6 — Orquestração

* [ ] Transformar os scripts em pipeline
* [ ] Configurar Apache Airflow
* [ ] Criar DAG principal
* [ ] Criar agendamentos
* [ ] Controlar falhas e retries
* [ ] Centralizar logs
* [ ] Criar carga pós-jogo

### Fase 7 — Power BI

* [ ] Conectar ao SQL Server
* [ ] Criar modelo semântico
* [ ] Criar medidas DAX
* [ ] Definir identidade visual
* [ ] Construir páginas do dashboard
* [ ] Publicar no Power BI

### Fase 8 — Evolução

* [ ] Configurar gateway
* [ ] Automatizar atualização do Power BI
* [ ] Criar testes unitários
* [ ] Implementar CI/CD
* [ ] Finalizar documentação
* [ ] Planejar futura migração para Microsoft Fabric

---

## 🔮 Evoluções Futuras

Após a conclusão da primeira versão, poderão ser exploradas evoluções como:

* inclusão de novas temporadas;
* análises históricas;
* comparação entre treinadores;
* análise de formações táticas;
* análise de desempenho por jogador;
* dados de transferências;
* modelos preditivos;
* previsão de pontos;
* probabilidades de resultado;
* integração com Microsoft Fabric;
* armazenamento no OneLake;
* utilização de Lakehouse;
* utilização de Direct Lake.

---

## ⚠️ Aviso

Este é um projeto independente criado exclusivamente para fins educacionais e de portfólio.

O projeto não possui vínculo oficial, patrocínio ou associação com o **Cruzeiro Esporte Clube**.

Os dados utilizados serão provenientes de fontes públicas ou de serviços cuja utilização esteja de acordo com seus respectivos termos de uso.
