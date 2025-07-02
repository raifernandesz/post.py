import requests 

url = "https://68641b8088359a373e978349.mockapi.io/produto"

produto = {
    "marca":"Nike-Raiane",
    "tamanho": "PP",
    "preco": 100.00
}

resposta = requests.post(url, json=produto)

print(resposta.json())
print(resposta.status_code)