import Menu
import TSTE




def buscador():
   busca = input("Digite o Item Procurado: ").casefold()
   for produto, valores in Menu.produtos_tecnologia.items():
       quantidade, preco = valores
       if produto.casefold() == busca:
           print("Produto:", produto)
           print("Preço: R${:.2f}".format(preco))
           print("Quantidade:", quantidade)
           return


   else:
       TSTE.additem()

# OU
# produto_procurado = input("Digite o produto:")
# produto_procurado = produto_procurado.lower()
# if produto_procurado in precos:
#    preco, quantos = precos[produto_procurado]

#    print(f"Produto: {produto_procurado}, Preço: R${preco}, quantos tem: {quantos}")
# else:
#    print("Produto não encontrado, tente novamente")


if __name__ == "__main__":
    buscador()