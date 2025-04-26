# 🧱 Exemplo de Arquitetura Hexagonal em Python

## 📖 Descrição

Este projeto é um exemplo didático de como estruturar uma aplicação Python utilizando a **Arquitetura Hexagonal** (também conhecida como *Ports and Adapters*). O objetivo principal é servir como base para aprendizado e referência em projetos que desejam adotar esse padrão de arquitetura, independentemente da linguagem ou contexto.

A ideia central da Arquitetura Hexagonal é isolar o núcleo de regras de negócio da aplicação (domínio) de detalhes externos como bancos de dados, APIs, interfaces gráficas, etc., promovendo uma estrutura mais **manutenível**, **testável** e **flexível**.

---

## 🧠 Conceitos Aplicados

- **Separação clara entre domínio e infraestrutura**
- **Princípios SOLID**
- **Abstração de portas e adaptadores**
- **Facilidade para testes unitários e de integração**

---

## 📁 Estrutura do Projeto

```text
src/
├── core/
│   ├── domain/              # Núcleo do domínio
│   │   ├── entities/        # Entidades do domínio
│   │   ├── value_objects/   # Objetos de valor
│   │   └── aggregates/      # Agregados
│   ├── ports/
│   │   ├── input/           # Portas de entrada (interfaces dos casos de uso)
│   │   └── output/          # Portas de saída (interfaces de repositórios, serviços, etc)
│   └── usecases/            # Casos de uso (aplicação)
└── adapters/
    ├── primary/             # Adaptadores de entrada
    │   ├── api/             # Exposição via API REST
    │   └── cli/             # Interface via linha de comando
    └── secondary/           # Adaptadores de saída
        ├── persistence/     # Integração com banco de dados
        └── external/        # Integração com serviços externos
```

---

## 📚 Referências

- 📄 [Engenharia Moderna: O que é Arquitetura Hexagonal?](https://engsoftmoderna.info/artigos/arquitetura-hexagonal.html)  
- 📄 [Relação: Princípios S.O.L.I.D com Arquitetura Hexagonal](https://dev.to/pedropietro/relacao-principios-solid-e-a-arquitetura-hexagonal-103l)

---