import json
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / ".env"
OUTPUT_FILE = ROOT / "data" / "raw" / "football_data" / "bsa_2026.json"
URL = "https://api.football-data.org/v4/competitions/BSA/matches?season=2026"
CRUZEIRO_ID = 1771


def carregar_token() -> str:
    for linha in ENV_FILE.read_text(encoding="utf-8").splitlines():
        if linha.startswith("FOOTBALL_DATA_TOKEN="):
            token = linha.split("=", 1)[1].strip()
            if token:
                return token
    raise RuntimeError("FOOTBALL_DATA_TOKEN não encontrado no .env da raiz.")


def main() -> None:
    pedido = Request(
        URL,
        headers={"X-Auth-Token": carregar_token(), "Accept": "application/json"},
    )

    with urlopen(pedido, timeout=30) as resposta:
        conteudo_original = resposta.read()

    dados = json.loads(conteudo_original)
    partidas = dados.get("matches")

    if not isinstance(partidas, list):
        raise RuntimeError("A resposta não contém uma lista de partidas.")

    partidas_cruzeiro = [
        partida
        for partida in partidas
        if (partida.get("homeTeam") or {}).get("id") == CRUZEIRO_ID
        or (partida.get("awayTeam") or {}).get("id") == CRUZEIRO_ID
    ]

    if not partidas_cruzeiro:
        raise RuntimeError("Nenhuma partida do Cruzeiro foi encontrada.")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(conteudo_original)

    print(f"JSON salvo em: {OUTPUT_FILE}")
    print(f"Partidas da Série A: {len(partidas)}")
    print(f"Partidas do Cruzeiro: {len(partidas_cruzeiro)}")


if __name__ == "__main__":
    main()