### LEMBRE DE INSTALAR AS DEPENDÊNCIAS DO PROJETO EM REQUIREMENTS.TXT
##### OBS: A maior parte desse READ.ME foi gerado com Gemini IA
##### OBS: Para instalar o gemini utilize o comando '''pip install -q -U google-generativeai'''
##### OBS: É necessário configurar a API_KEY no .env para que o código funcione!
## Projeto Alura com Google

**Descrição do projeto:**

Este projeto tem como objetivo a criação de um chatbot capaz de responder a perguntas a partir de prompts programáveis. 

**Funcionalidades:**

* **Personalização:** O chatbot pode ser personalizado com base em diferentes características, como tipo de ser (humano, robô, etc.), nome, objetivo, personalidade e estilo de resposta.
* **Respostas baseadas em documentos:** O chatbot pode ser treinado em um conjunto de documentos para restringir suas respostas às informações presentes nesses documentos.
* **Respostas com apoio em documentos:** O chatbot pode utilizar um conjunto de documentos como apoio para suas respostas, mas também pode utilizar outros conhecimentos para melhorar a qualidade das respostas.
* **Respostas sem documentos:** O chatbot pode funcionar mesmo sem nenhum documento de treinamento, respondendo às perguntas com base em seu conhecimento geral.

**Como usar:**

1. **Personalização do chatbot:**
    * Defina o tipo de ser que o chatbot representará.
    * Atribua um nome ao chatbot.
    * Estabeleça o objetivo do chatbot.
    * Defina a personalidade do chatbot.
    * Escolha o estilo de resposta do chatbot.
2. **Treinamento com documentos (opcional):**
    * Reúna os documentos que serão utilizados para treinar o chatbot.
    * Defina se as respostas devem ser restritas aos documentos ou se os documentos servirão apenas como apoio.
3. **Interação com o chatbot:**
    * Inicie uma conversa com o chatbot digitando um prompt.
    * O chatbot responderá ao seu prompt com base em suas configurações e treinamento.
    * Continue a conversa digitando novos prompts.

**Exemplo de uso:**

**Personalização:**

![image](https://github.com/nickolasL13/gemini_ai/assets/76066959/1c10ba41-28e1-46b5-ba95-e255a59aa069)

**Treinamento com documentos:**

![image](https://github.com/nickolasL13/gemini_ai/assets/76066959/d094f306-299d-4e9e-a4bd-03e48060ad72)

**Interação com o chatbot:**

![image](https://github.com/nickolasL13/gemini_ai/assets/76066959/9dc3a981-d2e9-4404-ab05-07c126dc983f)

**Observações:**

* Este é apenas um exemplo de uso do chatbot. Você pode personalizar o chatbot e interagir com ele de acordo com suas necessidades.
* O chatbot ainda está em desenvolvimento e pode apresentar falhas ou limitações.
* É importante fornecer prompts claros e concisos para que o chatbot possa entender suas perguntas e fornecer respostas precisas.

**Questões Importantes** (Nickolas Aqui)

- Os documentos utilizados serão os documentos da pasta ./docs. Coloquei um documento lá para que a pasta aparecesse aqui no git.
- Alguns parâmetros podem ser modificados a vontade, fica a seu critério :)
- Lembre de configurar a sua própria API KEY no .env do projetoz
- Se eu esqueci de falar algo importante me perdoe. Se esse for o caso por favor avise para que eu possa explicar ou corrigir ;)

**Técnica RAG**

A técnica RAG funciona de maneira simples.
Em poucas palavras, seu conceito é de utilizar uma fonte de informação externa ao modelo para que ela sirva de apoio ou como fonte de informação principal.
Segue-se os seguintes passos:
1. Ao se fazer um prompt, será feito com ele uma busca no documento com o objetivo de encontrar onde a informação do prompt bate com a informação do documento, retornando assim o trecho que contém seu conteúdo mais próximo ao prompt. (Aqui entra a parte de indexação do documento, embeddings e tals)
2. Após essa fase, passa-se esse trecho para que a LLM trabalhe em cima para gerar um texto mais requintado.
3. Por fim, junta-se esse texto requintado como contexto junto ao prompt em uma query para o ChatBot que deverá responder a pergunta baseado no contexto fornecido.

   ![image](https://github.com/nickolasL13/gemini_ai/assets/76066959/fc6cf7ad-724e-40ba-88c8-2e9bf8d287aa)
