class Produto:
    def __init__(self, nome, id_produto, preco, categoria):
        self.nome = nome
        self.id_produto = id_produto
        self.preco = preco
        self.categoria = categoria

    def calcular_frete(self):
        raise NotImplementedError("Método 'calcular_frete' deve ser implementado na subclasse.")

    def __str__(self):
        return f"{self.nome} (ID: {self.id_produto}) - Categoria: {self.categoria} - Preço: R${self.preco:.2f}"


class ProdutoDigital(Produto):
    def __init__(self, nome, id_produto, preco, categoria, tamanho_arquivo):
        super().__init__(nome, id_produto, preco, categoria)
        self.tamanho_arquivo = tamanho_arquivo

    def calcular_frete(self):
        return 0.00

    def __str__(self):
        return f"{super().__str__()} - Tamanho do Arquivo: {self.tamanho_arquivo}GB"


class ProdutoFisico(Produto):
    def __init__(self, nome, id_produto, preco, categoria, peso):
        super().__init__(nome, id_produto, preco, categoria)
        self.peso = peso

    def calcular_frete(self):
        return 10.00 + (self.peso * 0.05)

    def __str__(self):
        return f"{super().__str__()} - Peso: {self.peso}kg"


class ProdutoAssinatura(Produto):
    def __init__(self, nome, id_produto, preco, categoria, duracao_meses):
        super().__init__(nome, id_produto, preco, categoria)
        self.duracao_meses = duracao_meses

    def calcular_frete(self):
        return 0.00

    def __str__(self):
        return f"{super().__str__()} - Duração: {self.duracao_meses} meses"


class Loja:
    def __init__(self):
        self.produtos = {
            "Roupas": [
                ProdutoFisico("Camiseta Siples", 101, 39.90, "Roupas", 0.4),
                ProdutoFisico("Calça Simples", 102, 66.50, "Roupas", 0.5)
            ],
            "Jogos": [
                ProdutoDigital("GTA 6", 201, 600.00, "Jogos", 423),
                ProdutoDigital("Blodborn(PC)", 202, 199.90, "Jogos", 80)
            ],
            "Assinaturas": [
                ProdutoAssinatura("Assinatura Netflix", 301, 29.90, "Assinaturas", 12),
                ProdutoAssinatura("Assinatura Spotify", 302, 19.90, "Assinaturas", 12)
            ]
        }

    def listar_categorias(self):
        print("\nCategorias disponíveis:")
        for idx, categoria in enumerate(self.produtos.keys(), 1):
            print(f"{idx}. {categoria}")

    def listar_produtos_por_categoria(self, categoria):
        print(f"\nProdutos na categoria '{categoria}':")
        for produto in self.produtos[categoria]:
            print(f"{produto.id_produto}. {produto.nome} - R${produto.preco:.2f}")

    def escolher_produto(self, id_produto):
        for categoria in self.produtos.values():
            for produto in categoria:
                if produto.id_produto == id_produto:
                    return produto
        return None


def main():
    loja = Loja()
    while True:
        loja.listar_categorias()
        try:
            categoria_escolhida = int(input("\nEscolha uma categoria (número): "))
            categorias = list(loja.produtos.keys())
            if 1 <= categoria_escolhida <= len(categorias):
                categoria = categorias[categoria_escolhida - 1]
                loja.listar_produtos_por_categoria(categoria)
                try:
                    id_produto = int(input("\nEscolha um produto pelo ID: "))
                    produto = loja.escolher_produto(id_produto)
                    if produto:
                        print(f"\nDetalhes do produto escolhido:\n{produto}")
                        print(f"Frete: R${produto.calcular_frete():.2f}")
                    else:
                        print("Produto não encontrado.")
                except ValueError:
                    print("ID inválido.")
            else:
                print("Categoria inválida.")
        except ValueError:
            print("Opção inválida.")

        continuar = input("\nDeseja escolher outro produto? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por visitar nossa loja!")
            break





if __name__ == "__main__":
    main()







#Fonte StackOverflow,Reddit,w3schools
#Escrito em python 3.0 usando zed
