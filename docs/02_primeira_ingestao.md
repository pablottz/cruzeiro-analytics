# Fase 2 — Primeira ingestão de dados

## Objetivo

Obter os dados brutos das partidas da Série A de 2026 pela API football-data.org e guardá-los localmente, preservando a resposta original para as próximas etapas do projeto.

## Fonte e identificação do Cruzeiro

- Fonte: API football-data.org.
- Competição: Campeonato Brasileiro Série A (`BSA`).
- Temporada consultada: `2026`.
- ID do Cruzeiro EC nessa API: `1771`.

Esse ID pertence à football-data.org. IDs de outras APIs podem ser diferentes.

## Acesso à API

A chave de acesso fica na variável `FOOTBALL_DATA_TOKEN`, no arquivo `.env` da **raiz do projeto**. O script envia a chave no cabeçalho HTTP `X-Auth-Token`.

Esse `.env` é diferente de `infra/.env`, que contém a senha do SQL Server. Ambos são arquivos locais ignorados pelo Git; nenhuma chave ou senha deve entrar em um commit.

## Script e execução

O código está em `src/cruzeiro_analytics/ingest_bsa.py`. Na raiz do projeto, execute:

```powershell
python src/cruzeiro_analytics/ingest_bsa.py
```

O script consulta:

```text
https://api.football-data.org/v4/competitions/BSA/matches?season=2026
```

Ele verifica se a resposta contém uma lista de partidas, conta aquelas em que o ID `1771` aparece como mandante ou visitante e salva a **resposta completa da API**, sem alterar o JSON, em:

```text
data/raw/football_data/bsa_2026.json
```

O arquivo salvo contém as partidas da competição inteira, não apenas as do Cruzeiro. Isso preserva o dado bruto e permite repetir análises e filtros depois.

## Resultado da primeira execução

Na primeira execução, a resposta continha 380 partidas previstas para a Série A de 2026. Dessas, 38 envolviam o Cruzeiro: 28 estavam finalizadas e 10 ainda não tinham acontecido. Os números registram o estado da resposta naquele momento; uma nova consulta pode trazer atualizações.

## Versionamento

O código do script e esta documentação devem ser versionados. A pasta `data/` está no `.gitignore`, portanto o JSON baixado permanece fora do repositório Git.