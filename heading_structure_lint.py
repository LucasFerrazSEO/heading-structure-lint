#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
heading-structure-lint — checa a hierarquia de headings (H1-H6) de um HTML:
salto de nível (H2 direto para H4, sem H3), mais de um H1 na página (ou
nenhum, quando esperado) e heading vazio.

O QUE FAZ
    Lê um HTML e percorre a sequência de headings na ordem em que aparecem
    no documento, checando:

    1. **Salto de hierarquia.** Um H2 não pode pular direto para um H4 sem
       passar por um H3 — a estrutura em árvore que um leitor de tela ou um
       sistema de indexação usa para entender a organização do conteúdo
       fica quebrada.
    2. **H1 único.** Por padrão, espera exatamente um H1 na página (o modelo
       mais comum de HTML5 semântico). Ajustável para páginas que
       propositalmente não levam H1 (fragmento de conteúdo, glossário
       embutido em outro template).
    3. **Heading vazio.** Um heading sem texto (só espaço, ou só uma tag
       decorativa dentro) não serve para navegação nem para citação.

USO
    python heading_structure_lint.py pagina.html
    python heading_structure_lint.py fragmento.html --sem-h1
    python heading_structure_lint.py pagina.html --strict

LIMITAÇÕES
    Só a ordem dos headings no HTML, não a ordem visual renderizada (CSS que
    reordena visualmente não é detectado). Não avalia se o texto do heading
    é bom, só a estrutura.

Autor: Lucas Ferraz (lucasferraz.com) — dependência zero, só biblioteca padrão.
Licença: MIT.
"""
from __future__ import annotations

import argparse
import re
import sys

HEADING_RE = re.compile(r"(?is)<h([1-6])[^>]*>(.*?)</h\1>")


def strip_tags(html: str) -> str:
    html = re.sub(r"(?is)<(script|style).*?</\1>", " ", html)
    return re.sub(r"(?s)<[^>]+>", " ", html)


def normaliza(texto: str) -> str:
    return re.sub(r"\s+", " ", texto).strip()


def main() -> None:
    ap = argparse.ArgumentParser(description="Checa a hierarquia de headings de um HTML.")
    ap.add_argument("arquivo", help="arquivo .html")
    ap.add_argument("--sem-h1", action="store_true",
                     help="a página não deve ter H1 (fragmento/glossário embutido)")
    ap.add_argument("--strict", action="store_true", help="código de saída 1 se houver qualquer ATENÇÃO")
    args = ap.parse_args()

    try:
        with open(args.arquivo, encoding="utf-8") as fh:
            html = fh.read()
    except OSError as exc:
        print(f"Não consegui ler {args.arquivo}: {exc}", file=sys.stderr)
        sys.exit(2)

    headings = [(int(m.group(1)), normaliza(strip_tags(m.group(2)))) for m in HEADING_RE.finditer(html)]
    if not headings:
        print("Nenhum heading encontrado no arquivo.", file=sys.stderr)
        sys.exit(2)

    atencoes: list[str] = []

    n_h1 = sum(1 for nivel, _ in headings if nivel == 1)
    if args.sem_h1:
        if n_h1:
            atencoes.append(f"{n_h1} H1 encontrado(s), mas --sem-h1 pede zero")
    elif n_h1 == 0:
        atencoes.append("nenhum H1 na página (esperado exatamente 1)")
    elif n_h1 > 1:
        atencoes.append(f"{n_h1} H1 encontrados (esperado exatamente 1)")

    nivel_anterior = headings[0][0]
    for nivel, texto in headings:
        if not texto:
            atencoes.append(f"heading H{nivel} vazio (sem texto)")
        if nivel - nivel_anterior > 1:
            atencoes.append(
                f"salto de hierarquia: H{nivel_anterior} -> H{nivel} "
                f"(\"{texto[:50]}\") sem heading intermediário"
            )
        nivel_anterior = nivel

    print(f"\n=== heading-structure-lint: {args.arquivo} ===")
    print(f"{len(headings)} heading(s) | ATENÇÃO {len(atencoes)}\n")
    for h_nivel, h_texto in headings:
        print(f"  H{h_nivel}  {h_texto[:70]}")
    print()
    for a in atencoes:
        print("  ATENÇÃO  " + a)
    if not atencoes:
        print("  Nenhum ponto de atenção na hierarquia.")

    sys.exit(1 if (args.strict and atencoes) else 0)


if __name__ == "__main__":
    main()
