######################################################################################################################################################

            # A ideia do projeto é criar um ChatBot que possa responder perguntas a partir de prompts programáveis, além de poder se 
            # especializar em certa área a partir da técnica RAG utilizando documentos. 

            # Walkthrough:

            # 1. Inicialmente responde-se algumas perguntas para configurar o system_prompt, que servirá como
            # base de todas as perguntas que serão feitas posteriormentes para o ChatBot.

            # 2. Após isso, deve-se responder se tem desejo de carregar algum documento. Esse documento poderá servir de duas formas:
            # uma seria limitar o conhecimento do ChatBot apenas para as informações presentes do documento, e a outra seria 
            # utilizar esse documento como fonte de informação adicional. 

            # A diferença dessas formas é que na segunda o ChatBot teria a liberdade de utilizar seu "próprio conhecimento" para responder 
            # as perguntas feitas a ele, enquanto na primeira ele só poderá responder utilizando as informações do documento passado.

######################################################################################################################################################

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ.get("API_KEY"))

generation_config = {
    'candidate_count': 1,
    'temperature': 0.5
}

safety_settings = {
    'HARASSMENT': 'BLOCK_NONE',
    'HATE': 'BLOCK_NONE',
    'SEXUAL': 'BLOCK_NONE',
    'DANGEROUS': 'BLOCK_NONE'
}

def system_instruction(being, nome, objetivo, personalidade, maneira):
    return f"""
    Você é um(a) {being} e seu nome é {nome} 
    Seu objetico é {objetivo}. 
    Você possui a personalidade {personalidade}.
    Responda as perguntas de maneira {maneira}.   
    """

being = input('O que sua IA ? R: ')
nome = input('Qual será o nome da sua IA? R: ')
objetivo = input('Qual o objetivo da sua IA? R: ')
personalidade = input('Qual é a personalidade da sua IA? R: ')
maneira = input('De qual maneira a sua IA responde as perguntas? R: ')

model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              system_instruction=system_instruction(being, nome, objetivo, personalidade, maneira)
                            )

chat = model.start_chat(history=[])
prompt = input("Esperando o prompt: ")

while prompt != 'fim':
    response = chat.send_message(prompt)
    print('Resposta: ', response.text, '\n')
    prompt = input("Esperando o prompt: ")

