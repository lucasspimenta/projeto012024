import requests

def lista_Cidades(): 
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos" 
    resposta = requests.get(url) 
    return resposta.json() 


def sigla(UF): 
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/distritos"
    resposta = requests.get(url)  
    return resposta.json()  


def ordenar_cidades(cidades): 
    nomes_cidades = [] 
    for cidade in cidades: 
        nomes_cidades.append(cidade['nome']) 
    nomes_cidades.sort() 
    return nomes_cidades 