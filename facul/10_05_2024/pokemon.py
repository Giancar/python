import requests
import json

def procurar_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        data =  response.json()
        if 'erro' not in data:
            return data
        else:
            return None
    else:
        print("Erro ao encontrar o pokemon.")
        return None


def main():
    continuar = True
    while continuar == True:
        print("")
        pokemon = input("Digite o nome do pokemon ou digite 'sair' para sair: ")
        
        if pokemon.lower() == "sair":
            print("Saindo....")
            break
        
        resultado = procurar_pokemon(pokemon)
        
        if resultado:
            print("Pokemon Encontrado")
            print(f"Nome: {resultado['name']}")
            print(f"Tipos: {resultado['types'][0]['type']['name']}")
        else:
            print("Pokemon não encontrado")
        print("")

if __name__ == "__main__":
    main()