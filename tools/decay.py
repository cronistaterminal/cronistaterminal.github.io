#!/usr/bin/env python3
"""Round-trip dos passos de apodrecimento da 404 entre texto e base64.

    just decay-edit   ->  data/decay.toml  ->  .decay.txt   (Zalgo legível, gitignored)
    just decay-save   ->  .decay.txt       ->  data/decay.toml   (base64, ASCII puro)

POR QUE base64, se ele deixa a linha MAIOR (o passo mais pesado vai de 1462
caracteres para ~5.9k)? Porque o problema do Zalgo nunca foi o tamanho: é que ele
QUEBRA A REGRA de que um caractere fica dentro da própria linha. Combining marks
(U+0300-036F) se empilham sobre o glifo e sangram para as linhas vizinhas do
editor, embaralham a navegação por caractere, a seleção e o `git diff`. base64 é
ASCII inerte — feio, mas obediente.

A REGRA que sustenta este arquivo: NENHUM arquivo VERSIONADO carrega Zalgo cru.
O .decay.txt é efêmero e gitignored; a única cópia no repo é o base64. Por isso
`decay-edit` REGENERA o scratch a partir do TOML: o TOML é a fonte da verdade,
o texto é a vista.
"""

import base64
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOML = ROOT / "data" / "decay.toml"
SCRATCH = ROOT / ".decay.txt"

HEADER = '''# Os passos do apodrecimento da 404 — um por segundo a partir de
# timing.decay_starts (ver data/404.toml). GERADO por tools/decay.py.
#
# NÃO EDITE ESTE ARQUIVO À MÃO. Ele é artefato, não fonte:
#
#   just decay-edit    decodifica para .decay.txt (Zalgo legível, fora do git)
#   $EDITOR .decay.txt aqui você abusa do unicode à vontade — uma linha por passo
#   just decay-save    recodifica para cá
#
# Está em base64 porque Zalgo cru sangra para as linhas vizinhas do editor e
# torna o diff ilegível. O Hugo decodifica em layouts/404.html, em tempo de
# build — o browser recebe o texto pronto, e o lost.js nem sabe que isto existe.

steps_b64 = [
'''


def load_steps() -> list[str]:
    """Os passos decodificados, na ordem. Explode se o base64 mentir."""
    if not TOML.exists():
        sys.exit(f"erro: {TOML.relative_to(ROOT)} não existe — nada a decodificar")

    data = tomllib.loads(TOML.read_text(encoding="utf-8"))
    raw = data.get("steps_b64") or []
    if not raw:
        sys.exit(f"erro: {TOML.relative_to(ROOT)} não tem steps_b64")

    steps = []
    for i, b in enumerate(raw):
        try:
            # validate=True: sem isto, o b64decode IGNORA silenciosamente qualquer
            # caractere fora do alfabeto — um TOML corrompido decodificaria para
            # lixo plausível em vez de falhar. Preferimos o erro.
            steps.append(base64.b64decode(b, validate=True).decode("utf-8"))
        except Exception as e:
            sys.exit(f"erro: steps_b64[{i}] não é base64/UTF-8 válido: {e}")
    return steps


def decode() -> None:
    steps = load_steps()
    SCRATCH.write_text("\n".join(steps) + "\n", encoding="utf-8")
    print(f"  {SCRATCH.name}  <-  {TOML.relative_to(ROOT)}  ({len(steps)} passos)")
    for i, s in enumerate(steps):
        print(f"    [{i}] {len(s):5} caracteres")
    print(f"\n  edite {SCRATCH.name} e rode `just decay-save`.")


def encode() -> None:
    if not SCRATCH.exists():
        sys.exit(f"erro: {SCRATCH.name} não existe — rode `just decay-edit` primeiro")

    # rstrip só do \n: espaço no fim de uma linha pode ser parte do passo.
    # Linhas em branco são separadores visuais, não passos.
    steps = [ln.rstrip("\n") for ln in SCRATCH.read_text(encoding="utf-8").splitlines()]
    steps = [s for s in steps if s.strip()]

    if not steps:
        sys.exit(f"erro: {SCRATCH.name} está vazio — o encode apagaria os passos")

    lines = [HEADER]
    for s in steps:
        b = base64.b64encode(s.encode("utf-8")).decode("ascii")
        lines.append(f'  "{b}",\n')
    lines.append("]\n")
    TOML.write_text("".join(lines), encoding="utf-8")

    # Verificação de ida-e-volta: reler do disco e comparar. Um encode que não
    # sobrevive ao próprio decode é pior que nenhum — ele corrompe em silêncio.
    if load_steps() != steps:
        sys.exit("erro: o round-trip não bateu — o TOML escrito NÃO decodifica de volta")

    print(f"  {TOML.relative_to(ROOT)}  <-  {SCRATCH.name}  ({len(steps)} passos, round-trip ok)")
    for i, s in enumerate(steps):
        print(f"    [{i}] {len(s):5} caracteres")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "decode":
        decode()
    elif cmd == "encode":
        encode()
    else:
        sys.exit(f"uso: {Path(__file__).name} decode|encode")
