import Menu


def showlist():
   print("\nEstoque Atual:\n")
   print("{:<10} {:<10} {}".format("Produto", "Quantidade", "Preço"))
   print("-" * 30)
   for produto, valores in Menu.produtos_tecnologia.items():# como a lista é um Dicionario tem que declarar a Chave com o valroes com um só para depois declarar o valor de cada um
       quantidade, preco = valores # desse jeito faz o programa assumir que sempre vai ter dois valores dentro das chaves para mostrar
       print("{:<10} {:<10} R${:.2f}".format(produto, quantidade, preco))




if __name__ == "__main__":
   showlist()
