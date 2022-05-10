
from urllib import response
import requests
from requests.structures import CaseInsensitiveDict
import json


# Para aprender como a api funciona e o por que de cada passo nesse codigo, consulte a documentação através desse link: https://www.api-futebol.com.br/documentacao

# Insira a sua API KEY gerada
API_KEY = 'YOUR_API_KEY'

# Faz uma requisição via get para pegar os dados da tabela do brasileirão, no caso o campeonato que a gente quer é o campeonato com a numeração 10, caso queira pegar outros campeonatos
# é so modificar o numero 10 na URL para o numero do campeonato escolhido.

url = "https://api.api-futebol.com.br/v1/campeonatos/10/tabela"

#Precisamos passar no Headers o  token de acesso temporário (Bearer) e junto a chave API
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {API_KEY}"
resp = requests.get(url, headers=headers)

# Aqui usamos o metódo .json() para  mostrar os dados em formato de dicionario
tabela = resp.json()

# Aqui usamos o metódo .json.dumps() para  os dados em formato de json
tabela_json = json.dumps(tabela, indent = 4) 

# Criando o arquivo json para que depois possa consumir no Front-end
with open('tabela_brasileirao.json', 'w' ) as f:
      f.write(f'{tabela_json}')
    

# Criando o arquivo xml para que depois possa consumir no Front-end
with open('tabela_brasileirao.xml', 'w' ) as f:
      f.write(f'<rss version="2.0">\n')
      f.write(f'<channel>\n')
      
# Criamos um loop dentro da tabela para poder pegar as principais informações, caso queira pegar mais informações é só adicionar dentro do loop a informação que deseja     
for info in tabela:
    
    time = info['time']['nome_popular']
    pos = info['posicao']
    pontos = info['pontos']
    jogos = info['jogos']
    vitorias = info['vitorias']
    escudo = info['time']['escudo']
    saldo = info['saldo_gols']
    
    
    info = f'''  
                <item>
                    <posicao>{pos}</posicao>
                    <title>{time}</title>
                    <escudo>{escudo}</escudo>
                    <pontos>{pontos}</pontos>
                    <jogos>{jogos}</jogos>
                    <vitorias>{vitorias}</vitorias>
                    <saldo>{saldo}</saldo>
                 </item>'''
       
    # Precisamos usar o encode para passar os dados como UTF-8, caso contrário caractéres especiais como "áéó" não serão interpretados 
    info.encode('utf-8')   
    
    # Abrindo o arquivo tabela_brasileirao.xml para que a gente possa gravar as informações dentro
    with open('tabela_brasileirao.xml', 'a+', encoding='utf-8') as f:
      f.write(f"{info}")
# Continuação do arquivo xml, precisamos fechar a tag channel e a tag rss no fim do arquivo      
with open('tabela_brasileirao.xml', 'a+') as f:
 f.write(f'</channel>\n')  
 f.write(f'</rss>')




 