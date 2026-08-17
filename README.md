# 🌱 SoulUp — Sistema de Gamificação Sustentável com Avatar Web3

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ESG & Sustainability](https://img.shields.io/badge/Impact-ESG%20%26%20Web3-00a86b.svg)](#)

O **SoulUp** é uma plataforma interativa de gamificação focada em sustentabilidade e impacto socioambiental (ESG). Através de um assistente de IA/Avatar interativo e validador em arquitetura conceitual **Web 3.0 / Blockchain**, os usuários registram ações ecológicas diárias, acumulam **Pontos ECOA**, sobem de nível e trocam suas pontuações por benefícios reais do ecossistema.

---

## 📌 Sumário
- [Recursos Principais](#-recursos-principais)
- [Níveis e Progressão](#-níveis-e-progressão)
- [Tabela de Ações e Pontuações](#-tabela-de-ações-e-pontuações)
- [Vitrine de Recompensas](#-vitrine-de-recompensas)
- [Arquitetura e Estrutura de Dados](#-arquitetura-e-estrutura-de-dados)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Exemplo de Uso no Terminal](#-exemplo-de-uso-no-terminal)
- [Roadmap Futuro](#-roadmap-futuro)
- [Licença](#-licença)

---

## 🚀 Recursos Principais

- **🎮 Gamificação e Níveis Dinâmicos:** Acompanhe a evolução do seu avatar ecológico de *Semente* até *Expert*.
- **📊 Dashboard Interativo:** Exibição do saldo de **Pontos ECOA**, total resgatado e posição no ranking semanal.
- **🌱 Ações Sustentáveis Validadas:** Registro de hábitos diários com pontuação automatizada.
- **🏆 Ranking Semanal Competitivo:** Tabela dinâmica que posiciona você entre outros membros da comunidade.
- **🎁 Vitrine de Benefícios Reais:** Troca de pontos por ações como plantio de árvores, cupons ecológicos e descontos na conta de luz.
- **🤖 Sugestão do Avatar:** Recomendação personalizada baseada no seu nível atual.
- **🔗 Registro Imutável (Simulado Web3):** Notificação de validação via ledger Blockchain.

---

## 🌲 Níveis e Progressão

| Nível | Pontuação Necessária | Descrição / Estágio |
| :--- | :---: | :--- |
| 🌱 **Semente** | `0` a `99` pts | Início da jornada de conscientização sustentável. |
| 🌿 **Broto** | `100` a `299` pts | Hábito em consolidação e primeiras recompensas liberadas. |
| 🌳 **Árvore** | `300` a `599` pts | Impacto visível e recorrente na comunidade. |
| 👑 **Expert** | `600+` pts | Líder ambiental e agente de transformação. |

---

## ⚡ Tabela de Ações e Pontuações

| Ação Sustentável | Pontos ECOA |
| :--- | :---: |
| 🌲 Plantio de Árvore | **100 pts** |
| 🚌 Transporte Público | **50 pts** |
| ♻️ Reciclagem | **30 pts** |
| 🚲 Bicicleta | **25 pts** |
| ⚡ Economia de Energia | **20 pts** |
| 🚿 Banho Rápido | **20 pts** |
| 💧 Economia de Água | **15 pts** |

---

## 🎁 Vitrine de Recompensas

| Recompensa | Custo (Pontos ECOA) |
| :--- | :---: |
| 🌳 Plantar 1 Árvore | 200 pts |
| ♻️ Kit Reciclagem | 250 pts |
| 🚌 Crédito Transporte (R$ 20) | 300 pts |
| 🥗 Cupom Mercado Orgânico (R$ 30) | 350 pts |
| 🚲 Aluguel de Bicicleta (1 sem. grátis) | 400 pts |
| ⚡ Desconto na Energia (10% na fatura) | 500 pts |
| 🏞️ Adotar uma Área Verde (1 mês) | 1500 pts |
| 💡 Mês de Energia Grátis | 2000 pts |

---

## 🛠️ Arquitetura e Estrutura de Dados

O projeto utiliza estruturas de dados fundamentais em Python para garantir eficiência e simplicidade:

- **Tupla (`tuple`):** Armazena a lista imutável de ações sustentáveis (`acoes`), garantindo a integridade dos dados oferecidos ao usuário.
- **Lista (`list`):** Mantém o histórico sequencial das ações realizadas (`historico`) e a estrutura do ranking semanal dinâmico (`competidores`).
- **Dicionário (`dict`):** Representa cada competidor do ranking (`{"nome": ..., "pontos": ...}`).
- **Match-Case & Tratamento de Exceções:** Garante navegação segura pelos menus com validação de tipos via `try-except`.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
- **Python 3.10** ou superior instalado no sistema.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/soulup-gamificacao.git](https://github.com/seu-usuario/soulup-gamificacao.git)
   cd soulup-gamificacao
