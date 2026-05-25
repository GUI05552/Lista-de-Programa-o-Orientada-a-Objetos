# Questão 3 — Sistema de Notificações com ABC

## Descrição

Este exercício implementa um sistema de notificações utilizando classes abstratas para definir um contrato formal entre os notificadores.

Foi criada a classe abstrata `Notificador`, contendo o método abstrato `notificar(mensagem)`.

As subclasses implementadas foram:

- `NotificadorEmail`
- `NotificadorSMS`
- `NotificadorApp`

Cada classe implementa o envio de mensagens de maneira específica.

A classe `CentralNotificacoes` gerencia os notificadores e envia mensagens para todos os objetos cadastrados.

## Conceitos Utilizados

- Classes Abstratas (ABC)
- Polimorfismo
- Herança
- Contrato formal por herança
- Sobrescrita de métodos
