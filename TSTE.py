import Menu
def additem():
   # cirando as variáveis input
   item = input("Digite o item: ")
   item = item.upper()
   quantidade = input("Digite quantidade: ")
   preco_unitario = int(input("Digite o preço unitário do produto: "))

   for (produto, valores) in Menu.produtos_tecnologia.items():
      if item.upper() == produto:
         # Modificando os valores existentes
         Menu.produtos_tecnologia[item] = (quantidade, preco_unitario)
         print("\nProduto Atualizado:\n")
         print("{:<10} {:<10} {}".format("Produto", "Quantidade", "Preço"))
         print("-" * 30)
         print("{:<10} {:<10} R${:.2f}".format(item, quantidade, preco_unitario))
         return

   # Adicionando o novo par chave-valor ao dicionário
   Menu.produtos_tecnologia[item] = quantidade, preco_unitario
   print("\nProdutos Adicionado:\n")
   print("{:<10} {:<10} {}".format("Produto", "Quantidade", "Preço"))
   print("-" * 30)
   print("{:<10} {:<10} R${:.2f}".format(item, quantidade, preco_unitario))




if __name__ == "__main__":
   additem()