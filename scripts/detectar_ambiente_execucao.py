#!/usr/bin/env python3
"""
Ajuda o orquestrador da skill dissecador-de-metodos a detectar em qual ambiente esta rodando.
Modo A (Claude Code com Task tool) vs Modo B (Claude.ai sem Task tool).

Este script executa checagens de ambiente e imprime um relatorio que orienta a decisao.
Ele NAO decide sozinho — a decisao final e do Claude orquestrador com base neste relatorio
somado as ferramentas disponiveis na sessao (que so o Claude LLM enxerga).

Uso:
    python3 detectar_ambiente_execucao.py
"""

import os
import sys
from pathlib import Path


def checar_claude_code_home() -> bool:
    """
    Claude Code tipicamente tem um diretorio ~/.claude/ com skills instaladas.
    """
    return Path.home().joinpath(".claude").exists()


def checar_mnt_user_data() -> bool:
    """
    Claude.ai com code execution habilitado tem /mnt/user-data/outputs/ para artifacts
    e /mnt/user-data/uploads/ para arquivos enviados pelo usuario.
    """
    return Path("/mnt/user-data").exists()


def checar_mnt_skills() -> bool:
    """
    Ambos os ambientes com skills tem /mnt/skills/ (public, user, examples, plugins).
    """
    return Path("/mnt/skills").exists()


def checar_home_claude_dir() -> bool:
    """
    Claude.ai com code execution roda em container temporario com HOME em /home/claude/.
    """
    return Path("/home/claude").exists() and os.environ.get("HOME") == "/home/claude"


def main():
    print("=" * 60)
    print("RELATORIO DE AMBIENTE — dissecador-de-metodos")
    print("=" * 60)
    print()

    tem_claude_home = checar_claude_code_home()
    tem_user_data = checar_mnt_user_data()
    tem_skills_dir = checar_mnt_skills()
    tem_home_claude = checar_home_claude_dir()

    print(f"~/.claude/ existe:                       {tem_claude_home}")
    print(f"/mnt/user-data/ existe:                  {tem_user_data}")
    print(f"/mnt/skills/ existe:                     {tem_skills_dir}")
    print(f"/home/claude/ e HOME apontam pra la:     {tem_home_claude}")
    print()

    # Heuristica de deteccao
    if tem_home_claude and tem_user_data and not tem_claude_home:
        provavel_ambiente = "Claude.ai com code execution (container temporario)"
        modo_recomendado = "Modo B (sequencial no mesmo contexto) — MAS o Claude LLM deve conferir se tem Task tool na sessao antes de decidir. Se tiver Task tool disponivel, usar Modo A."
    elif tem_claude_home:
        provavel_ambiente = "Claude Code (instalacao permanente do usuario)"
        modo_recomendado = "Modo A (subagents via Task tool) — recomendado, pois Task tool costuma estar disponivel"
    elif tem_user_data:
        provavel_ambiente = "Claude.ai ou Cowork (ambiente com file system)"
        modo_recomendado = "Verificar ferramentas disponiveis. Se Task tool esta na lista, Modo A. Senao, Modo B."
    else:
        provavel_ambiente = "Ambiente sem file system ou desconhecido"
        modo_recomendado = "Modo B (sequencial) por padrao. Documento final entregue no chat, sem uso de arquivos."

    print(f"Ambiente provavel: {provavel_ambiente}")
    print(f"Modo recomendado: {modo_recomendado}")
    print()
    print("DECISAO FINAL: o Claude LLM confere as ferramentas disponiveis na sessao")
    print("(Task tool ou equivalente) e decide o modo. Este relatorio e apenas orientativo.")


if __name__ == "__main__":
    main()
