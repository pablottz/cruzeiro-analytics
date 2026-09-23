# Cruzeiro Analytics ⚽💙

Projeto de análise de dados de futebol de ponta a ponta, com foco no **Cruzeiro Esporte Clube**.

O objetivo é construir uma plataforma de dados que reúna ingestão, armazenamento, transformação, modelagem, orquestração e visualização. O projeto também serve como ambiente prático de aprendizado em Engenharia de Dados, Python, SQL e Business Intelligence.

## 📚 Documentação

- [Fase 1 — Fundação](docs/01_fundacao.md): preparação do ambiente, estrutura inicial, criação do banco e configuração local do SQL Server.

## 🎯 Objetivos do Projeto

- Consumir dados de futebol por REST APIs.
- Construir uma arquitetura Medallion com camadas Bronze, Silver e Gold.
- Desenvolver pipelines de ingestão e transformação com Python.
- Armazenar dados brutos em JSON na Bronze.
- Processar a Silver com Apache Spark e armazená-la em Delta Lake.
- Usar DuckDB como ferramenta auxiliar para exploração e consultas.
- Armazenar o modelo analítico final no SQL Server.
- Implementar qualidade de dados e cargas incrementais.
- Construir um modelo dimensional com fatos e dimensões.
- Orquestrar os pipelines com Apache Airflow.
- Criar um modelo semântico e o dashboard **Cruzeiro 360** no Power BI.
- Versionar código, infraestrutura e documentação com Git e GitHub.

---

## 🏗️ Arquitetura planejada

```text
REST APIs de futebol
          │
          ▼
Ingestão com Python
          │
          ▼
MinIO — Bronze (JSON bruto)
          │
          ▼
Apache Spark — transformação
          │
          ▼
MinIO — Silver (Delta Lake)
          │
          ▼
SQL Server — Gold
          │
          ▼
Power BI

Apache Airflow orquestrará o pipeline.
DuckDB poderá apoiar a exploração e as consultas aos dados.
```

O projeto seguirá os princípios da **Arquitetura Medallion**: a Bronze preserva os dados recebidos, a Silver entrega dados tratados e a Gold organiza os dados para análise.

**Estado atual:** Python, Docker, SQL Server, o banco `CruzeiroAnalytics` e a estrutura inicial do repositório estão preparados. MinIO, Spark, Delta Lake, Airflow e Power BI fazem parte das próximas fases; ainda não foram implementados.

---

## 🛠️ Tecnologias

**Já utilizadas na fundação:**

- Python e ambiente virtual
- Docker e Docker Compose
- SQL Server 2025 Developer
- SQL Server Management Studio (SSMS)
- Git e GitHub

**Planejadas para as próximas fases:**

- MinIO
- Apache Spark e PySpark
- Delta Lake e Apache Parquet
- DuckDB como ferramenta auxiliar
- Apache Airflow
- Power BI

Outras bibliotecas e ferramentas poderão ser adicionadas conforme as necessidades do projeto.

---

## 🚀 Ambiente local

A configuração do SQL Server está em `infra/docker-compose.yml`. O arquivo `infra/.env.example` mostra a variável necessária para iniciar o serviço, sem conter uma senha real.

Em uma nova instalação:

1. Copie `infra/.env.example` para `infra/.env`.
2. Preencha `MSSQL_SA_PASSWORD` no arquivo `infra/.env` com uma senha forte.
3. Na raiz do projeto, valide e inicie o serviço:

```powershell
docker compose --env-file infra/.env -f infra/docker-compose.yml config --quiet
docker compose --env-file infra/.env -f infra/docker-compose.yml up -d
```

Depois que o SQL Server estiver pronto, conecte o SSMS a `localhost,1433` usando a autenticação do SQL Server, o usuário `sa` e a senha definida em `infra/.env`.

Abra e execute `sql/ddl/001_create_database.sql` no SSMS. Atualize a lista de bancos de dados e confirme que `CruzeiroAnalytics` aparece.

O arquivo `.gitignore` exclui `.env` e `.venv` do Git. A senha real e o ambiente virtual não devem ser enviados ao repositório.

---

## 🥉 Camada Bronze

A Bronze armazenará os dados brutos recebidos das fontes, sem aplicar regras de negócio que alterem o conteúdo original.

Preservar os dados de origem permitirá auditoria, rastreabilidade, reprocessamento e comparação entre diferentes extrações.

**Armazenamento planejado:** MinIO.  
**Formato principal planejado:** JSON.

Exemplo conceitual de organização:

```text
bronze/
└── api_football/
    ├── fixtures/
    ├── players/
    ├── events/
    ├── lineups/
    └── statistics/
```

Os nomes definitivos de buckets e caminhos serão definidos quando a Bronze for implementada.

---

## 🥈 Camada Silver

A Silver transformará os dados brutos da Bronze em conjuntos confiáveis, padronizados e próprios para análise.

As transformações planejadas incluem:

- leitura dos arquivos JSON;
- abertura de objetos e listas aninhados;
- conversão de tipos;
- tratamento de valores nulos e registros inválidos;
- remoção de duplicidades;
- padronização de datas e horários;
- aplicação de regras de negócio;
- validações de qualidade.

**Motor principal planejado:** Apache Spark com PySpark e SQL.  
**Armazenamento planejado:** Delta Lake no MinIO, sobre arquivos Parquet.

O DuckDB poderá ser usado para exploração e consultas auxiliares. Ele não será o motor principal de processamento da Silver.

Exemplo conceitual de organização:

```text
silver/
├── partidas/
├── jogadores/
├── eventos/
├── escalacoes/
└── estatisticas/
```

---

## 🥇 Camada Gold

A Gold disponibilizará dados em uma estrutura analítica preparada para consumo pelo Power BI. Seu armazenamento principal será o **SQL Server**, com um modelo dimensional formado por tabelas fato e dimensão.

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

Essa modelagem poderá mudar quando conhecermos os dados efetivamente disponíveis nas fontes.

---

## 🔄 Orquestração

O **Apache Airflow** será adotado depois que os processos individuais de ingestão, transformação e carga estiverem funcionando.

Ele será responsável por organizar dependências, agendar execuções, monitorar o pipeline, registrar falhas, executar novas tentativas e permitir reprocessamentos.

Fluxo planejado:

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
Qualidade dos dados
   │
   ▼
Dimensões e fatos na Gold
   │
   ▼
Validação
   │
   ▼
Power BI
```

---

## 📊 Cruzeiro 360

O produto analítico planejado é um dashboard no Power BI chamado **Cruzeiro 360**.

Entre as análises desejadas estão:

- resultados, gols, saldo e aproveitamento;
- desempenho como mandante e visitante;
- desempenho por competição e temporada;
- forma recente e evolução mensal;
- classificação por rodada;
- estatísticas de jogadores, artilharia e assistências;
- escalações, formações e detalhes das partidas;
- comparações entre temporadas.

Também está planejada uma área de acompanhamento da plataforma, com última atualização, registros processados, estado das execuções, falhas e qualidade dos dados.

O conteúdo final dependerá dos dados disponíveis e das condições de uso das fontes.

---

## 📚 Objetivos de aprendizado

**Engenharia de Dados:** arquitetura Medallion, Data Lake, ingestão, ETL/ELT, cargas incrementais, qualidade, orquestração e modelagem dimensional.

**Python:** consumo de APIs, manipulação de JSON, organização de projetos, tratamento de erros, DataFrames, automação e testes.

**SQL:** criação de bancos e esquemas, DDL, DML, joins, CTEs, funções de janela, views, procedures, `MERGE` e consultas analíticas.

**Business Intelligence:** modelo semântico, relacionamentos, DAX, visualização, storytelling e Power BI.

**Boas práticas:** Git, GitHub, documentação, Docker, testes automatizados e CI/CD.

---

## 🚧 Status do Projeto

A **Fase 1 — Fundação** está concluída. O próximo marco é a **Fase 2 — Primeira Ingestão**. As ferramentas das fases seguintes aparecem neste README como planejamento, não como componentes já instalados ou executados.

---

## 🗺️ Roadmap

- [x] **Fase 1 — Fundação**
- [ ] **Fase 2 — Primeira Ingestão**
- [ ] **Fase 3 — Camada Bronze**
- [ ] **Fase 4 — Camada Silver**
- [ ] **Fase 5 — Camada Gold**
- [ ] **Fase 6 — Orquestração com Apache Airflow**
- [ ] **Fase 7 — Power BI**
- [ ] **Fase 8 — Evolução**

### Fase 1 — Fundação

- [x] Criar e conectar o repositório GitHub.
- [x] Configurar Python e o ambiente virtual `.venv`.
- [x] Executar o SQL Server em um container Docker.
- [x] Conectar e validar o SQL Server pelo SSMS.
- [x] Criar o banco `CruzeiroAnalytics` com um script SQL versionado.
- [x] Definir a estrutura inicial de pastas.
- [x] Proteger `infra/.env` com o `.gitignore`.
- [x] Versionar `infra/docker-compose.yml` e `infra/.env.example`.
- [x] Preparar a documentação inicial.

### Fase 2 — Primeira Ingestão

- [ ] Definir a API e verificar suas condições de uso.
- [ ] Identificar o Cruzeiro na API.
- [ ] Consultar partidas do Cruzeiro.
- [ ] Salvar o primeiro JSON.
- [ ] Criar um registro da execução.
- [ ] Analisar e documentar a resposta da API.

### Fase 3 — Camada Bronze

- [ ] Configurar o armazenamento no MinIO.
- [ ] Criar funções reutilizáveis de ingestão.
- [ ] Implementar os endpoints necessários.
- [ ] Tratar paginação, limites de requisição e novas tentativas.
- [ ] Organizar os dados brutos.
- [ ] Executar uma carga histórica.

### Fase 4 — Camada Silver

- [ ] Configurar Apache Spark e Delta Lake.
- [ ] Ler os dados brutos da Bronze.
- [ ] Abrir campos aninhados e aplicar tipagem.
- [ ] Tratar valores nulos e remover duplicidades.
- [ ] Normalizar e validar os dados.
- [ ] Gravar a Silver em Delta Lake no MinIO.
- [ ] Criar testes de qualidade.
- [ ] Avaliar DuckDB para consultas auxiliares.

### Fase 5 — Camada Gold

- [ ] Criar o modelo dimensional.
- [ ] Criar dimensões e fatos no SQL Server.
- [ ] Implementar cargas incrementais.
- [ ] Criar procedures e views conforme a necessidade.
- [ ] Implementar validações SQL.

### Fase 6 — Orquestração

- [ ] Configurar Apache Airflow.
- [ ] Integrar as etapas em um pipeline.
- [ ] Criar a DAG principal e os agendamentos.
- [ ] Controlar falhas, novas tentativas e logs.
- [ ] Criar a carga pós-jogo.

### Fase 7 — Power BI

- [ ] Conectar ao SQL Server.
- [ ] Criar o modelo semântico e as medidas DAX.
- [ ] Definir a identidade visual.
- [ ] Construir as páginas do Cruzeiro 360.
- [ ] Publicar e validar o dashboard.

### Fase 8 — Evolução

- [ ] Automatizar a atualização do Power BI.
- [ ] Ampliar os testes automatizados.
- [ ] Implementar CI/CD.
- [ ] Revisar e ampliar a documentação.
- [ ] Avaliar uma futura integração com Microsoft Fabric.

---

## 🔮 Evoluções futuras

Depois da primeira versão, poderão ser estudadas análises históricas, comparações entre treinadores, desempenho por jogador, transferências e modelos preditivos. Também poderão ser avaliados Microsoft Fabric, OneLake, Lakehouse e Direct Lake.

Essas possibilidades ainda não fazem parte da implementação atual.

---

## ⚠️ Aviso

Este é um projeto independente, criado para fins educacionais e de portfólio. Não possui vínculo oficial, patrocínio ou associação com o **Cruzeiro Esporte Clube**.

Os dados utilizados deverão vir de fontes públicas ou serviços usados de acordo com seus respectivos termos.