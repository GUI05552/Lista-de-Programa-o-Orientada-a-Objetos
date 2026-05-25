# Questão 5 — Sistema de Armazenamento com ABC e Protocol

## Descrição

Este exercício compara duas abordagens de contratos em Python:

- Contrato formal utilizando Classes Abstratas (ABC)
- Contrato estrutural utilizando Protocol

Na primeira parte, foi criada a classe abstrata `Armazenador`, com as subclasses:

- `ArmazenadorArquivo`
- `ArmazenadorBanco`

Na segunda parte, foi utilizado o protocolo `Salvavel`, permitindo que a classe `ArmazenadorNuvem` funcione sem herança explícita.

O sistema também possui funções específicas para demonstrar as diferenças entre as abordagens formal e flexível.

## Conceitos Utilizados

- Classes Abstratas (ABC)
- Protocol
- Polimorfismo
- Duck Typing
- Contrato formal
- Contrato estrutural
- Comparação entre rigidez e flexibilidade em POO
