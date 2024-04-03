from flask import Flask, request
from funcoes import obter_lista_de_cidades_por_estado, ordenar_nomes_de_cidades, obter_lista_de_cidades

app = Flask(__name__)

@app.route("/lista_ibge")       
def todas_cidades(): 
    # Retorna uma lista de todas as cidades do Brasil, ordenadas alfabeticamente.
    cidades = obter_lista_de_cidades() 
    ordenadas = ordenar_nomes_de_cidades(cidades) 
    return ordenadas 

@app.route("/consulta_ibge", methods=['GET'])  
def estado(): 
    # Retorna uma lista de cidades de um estado especificado pela sigla UF.
    # Parâmetros: UF (str): Sigla do estado brasileiro.
    UF = request.args.get('UF') 
    resposta = obter_lista_de_cidades_por_estado(UF) 
    return resposta 

@app.route("/ordenar_cidades", methods=['GET']) 
def ordenar(): 
    # Retorna uma lista de cidades de um estado especificado pela sigla UF, ordenadas alfabeticamente.
    # Parâmetros: UF (str): Sigla do estado brasileiro.
    UF = request.args.get('UF') 
    cidades = estado()  
    cidades_ordenadas = ordenar_nomes_de_cidades(cidades)  
    return {f"Cidades ordenadas de {UF}": cidades_ordenadas} 

if __name__ == "__main__":
    app.run(debug=True)
