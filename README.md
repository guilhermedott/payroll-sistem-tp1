# Payroll System (Legado) – TP1 / TP2

Sistema legado de folha de pagamento.

## Como executar

```bash
python app.py
```

## Evolução TP2 — Relatório de custo total por departamento

Foi adicionada a opção **4** no menu, que apresenta o custo total da folha
agrupado por departamento (funcionários do departamento, custo individual,
quantidade, total e média por departamento, além do total geral da
empresa). Departamentos ausentes/inválidos nos dados são tratados e
identificados como "Not informed" (ausente) ou "Other" (desconhecido),
em vez de quebrar o relatório.

Detalhes completos (demanda, análise de impacto, estimativa, testes e
rastreabilidade) estão no relatório técnico entregue em PDF/DOCX.

## Como rodar os testes

```bash
pip install pytest
pytest tests/
```
