import TSTE
import TSTE2
import TSTE3


# criação das listas
# Produto: quantidade, preço, código do produto
produtos_tecnologia = {"CPU": (30, 500), "GPU": (25, 1500), "SSD": (68, 600), "HDD": (33, 300), "MONITOR": (21, 1200),
                      "GABINETE": (33, 250), "MB": (75, 300), "SUBWOOFER": (58, 5000), "TV": (12, 2500),
                      "FONTE": (89, 101), "RAM": (45, 300), "COOLER": (150, 150)}


# O código precisa ter: menu de direção, listagem de quantidade, listagem de preços de todos os produtos
# Depois listagem de quantida por limite de minimo, listagem de preço por busca.


# Função de MENU
def menu():
   while True:
       print("\nDigite Para Onde Gostaria de Ir")
       print("1. Para Adicionar ou Alterar um Item")
       print("2. Para Listar a Quantidade Atual em Estoque")
       print("3. Buscar Item")
       print("4. Para Voltar")


       opcao = input("---->")


       # Adicionando itens
       if opcao == "1":
           adicionaritem = TSTE.additem()
           print(adicionaritem)


       # Exibindo os produtos, suas quantidades e preços
       elif opcao == "2":
           estoqueatual = TSTE3.showlist()
           print(estoqueatual)


       elif opcao == "3":
           TSTE2.buscador()


       else:
           return True




if __name__ == "__main__":
   menu()
