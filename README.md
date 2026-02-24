# Orquestrador de Incidentes IoT - Desafio Promont

Este projeto apresenta uma solução para o processamento de eventos assíncronos e desordenados de dispositivos IoT, utilizando n8n, Python e Inteligência Artificial.

## Stack Tecnológica

* 
**Orquestrador:** n8n.


* 
**Linguagens de Script:** Python (Lógica de segurança e splitter de dados) e JavaScript (Agrupamento por dispositivo).


* 
**IA:** LLM agnóstico (testado com Groq Cloud/Llama 3) via LangChain para análise de contexto e redação de alertas.


* 
**Banco de Dados:** Duas versões disponíveis (Supabase ou n8n DataTables).


* 
**Notificação:** Gmail API.



## Lógica de Estado e Segurança

O núcleo da solução reconstrói a cronologia dos eventos para identificar inconsistências baseadas nos sensores do hardware:

* 
**ID 32 (Cadeado):** 0: Fechado / 1: Aberto.


* 
**ID 33 (Travamento):** 0: Travado / 1: Destravado.



**Regras implementadas no nó Python:**

* 
**Vulnerabilidade:** Cadeado fechado (32=0), mas destravado (33=1).


* 
**Invasão:** Cadeado aberto (32=1) sem que tenha havido o destravamento prévio (33 permaneceu em 0).



## Versões do Workflow

### 1. Versão Banco Separado (Supabase)

Utiliza o Supabase para persistência de logs brutos e diagnósticos finais da IA. Ideal para ambientes de produção com auditoria externa.

### 2. Versão DataTables (n8n Native)

Utiliza o recurso nativo de DataTables do n8n para armazenamento interno.

* **Configuração:** Para utilizar esta versão, crie as tabelas importando os arquivos CSV fornecidos (disponíveis no repositório) através da função "Import from CSV" na interface de DataTables do n8n.

## Instruções de Teste

### Configuração de Credenciais

Para validar o fluxo, configure suas próprias chaves de API nos seguintes nós:

* **AI Model:** API Key da LLM de sua escolha.
* **Gmail Tool:** Autenticação OAuth2 para envio de e-mails.
* **Supabase (se aplicável):** URL e Service Role Key.

### Alteração do Destinatário

Para receber os alertas de segurança em seu e-mail:

1. Abra o nó **"Send email if Security risk"**.
2. No campo **"To Email"**, insira o seu endereço de e-mail.

### Execução da Rotina de 1 Minuto

Para simular um sistema em tempo real enviando dados periodicamente, utilize o script de teste `test_loop.py`:

1. Certifique-se de ter a biblioteca `requests` instalada (`pip install requests`).
2. Execute o script: `python test_loop.py`.
3. O script enviará o payload de teste para o Webhook e aguardará 60 segundos antes da próxima iteração, simulando o ciclo de inteligência solicitado.



---

**Dica final:** Ao enviar o e-mail para o Guilherme, certifique-se de que o repositório esteja público ou que ele tenha permissão de acesso. Desejo muito sucesso no processo seletivo! Precisa de ajuda com mais alguma coisa?
