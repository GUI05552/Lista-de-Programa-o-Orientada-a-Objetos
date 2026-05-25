# Questão 4 — Sistema de Impressão com Protocol

## Descrição

Este exercício implementa um sistema de impressão utilizando `Protocol`, permitindo trabalhar com tipagem estrutural em Python.

Foi criado o protocolo `Imprimivel`, que define o método esperado `imprimir()`.

As classes implementadas foram:

- `Boleto`
- `Etiqueta`
- `RelatorioSimples`

Mesmo sem herança direta, todas as classes funcionam corretamente por possuírem o método compatível com o protocolo.

A função `processar_impressao(item)` recebe qualquer objeto compatível com `Imprimivel`.

## Conceitos Utilizados

- Protocol
- Duck Typing
- Tipagem estrutural
- Polimorfismo
- Flexibilidade estrutural
