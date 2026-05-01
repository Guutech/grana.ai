# 💰 Grana AI

Uma aplicação interativa construída com Python e Streamlit que permite ao usuário analisar seus dados financeiros a partir de um arquivo CSV, gerando insights automáticos de forma simples e acessível.

---

## 🚀 Objetivo

O projeto nasceu com o objetivo de resolver um problema comum:

> Analistas e usuários perdem tempo interpretando planilhas e respondendo perguntas repetitivas sobre dados financeiros.

A proposta é transformar dados brutos em **informações claras e acionáveis**, com suporte de inteligência (com ou sem IA).

---

## 🧠 Como funciona

O fluxo da aplicação segue uma arquitetura organizada em camadas:

1. 📥 O usuário envia um arquivo CSV com seus dados financeiros  
2. 🧠 O sistema interpreta a intenção da pergunta  
3. 📊 Os dados são processados e analisados  
4. 🤖 Uma resposta é gerada (com IA ou fallback local)  
5. 📈 Resultados são exibidos de forma simples no Streamlit  

---

## 🏗️ Arquitetura do Projeto

A estrutura de diretórios foi organizada seguindo princípios de separação de responsabilidades para facilitar a manutenção e escalabilidade:
```text

grana_ai/
├── app/          # Interface com usuário (Streamlit)
├── core/         # Orquestração e fluxo da aplicação
├── use_cases/    # Casos de uso (lógica de negócio)
├── domain/       # Regras e cálculos financeiros
├── data/         # Leitura e validação de dados
└── config/       # Configurações e integração com IA
```

## 📊 Formato do CSV

O sistema espera um arquivo com as seguintes colunas:

```csv
renda,despesa,categoria,data
5000,2000,moradia,2024-01-01
5000,500,lazer,2024-01-05
