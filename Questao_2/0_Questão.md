# Questão 2 — Sistema de Funcionários

## Descrição

Este exercício implementa um sistema de gerenciamento de funcionários utilizando Programação Orientada a Objetos.

Foi criada a classe abstrata `Funcionario`, que define os atributos básicos de qualquer funcionário e o método abstrato `calcular_pagamento()`.

As subclasses implementadas foram:

- `FuncionarioAssalariado`
- `FuncionarioHorista`
- `FuncionarioComissionado`

Cada tipo de funcionário possui uma forma diferente de cálculo salarial, demonstrando polimorfismo e sobrescrita de métodos.

A classe `Empresa` é responsável por armazenar os funcionários e gerar a folha de pagamento.

## Conceitos Utilizados

- Herança
- Polimorfismo
- Classes Abstratas (ABC)
- Sobrescrita de métodos
- Organização modular
