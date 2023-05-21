import time 
from tqdm import tqdm
import pandas as pd
import requests

def metodo1():
    for _ in tqdm(range(100),
        desc = "Loading...",
        ascii = False , ncols=100):
        time.sleep(0.001)
    
    
    print("Loading Done!")
    

    
    
    


df = pd.DataFrame({'a':[1,2,3,4,5], 'b':[2,3,4,5,6]})    
tqdm.pandas()   
def metodo2(row):
    time.sleep(1)
    return row + 1

result = df['b'].progress_apply(metodo2)
print(result)



def metodo3():
    lista = [1,2,3,4,5,6,7,8,9]
    
    for item in tqdm(lista):
        time.sleep(1)
        
def metodo4():
    with tqdm(total=100) as barra_progresso:
        for i in range(20):
            time.sleep(1)
            barra_progresso.update(5)
            
def metodo5():
    

    with open("ceps.txt", "r") as arquivo:
        ceps = arquivo.read()
    
    enderecos_entrega = []
    ceps = ceps.split("\n")
    for cep in tqdm(ceps):
        link = f'https://cep.awesomeapi.com.br/json/{cep}'
        
        requisicao = requests.get(link)
        resposta = requisicao.json()
        cidade = resposta['city']
        bairro = resposta['district']
        
        if cidade == "Rio de Janeiro":
            enderecos_entrega.append(f"cep: {cep} - cidade: {cidade} - bairro: {bairro}")
    print(*enderecos_entrega, sep="\n")
    
    def metodo6():
        progress_bar = tqdm(total=50_000)
        for s in range(100):
            progress_bar.update(1)
            time.sleep(0.000001)
        progress_bar.close()
        
        
    
if __name__=='__main__':
    metodo5()