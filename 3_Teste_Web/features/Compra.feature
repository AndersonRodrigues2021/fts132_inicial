Feature: Compra de produtos Pet
    # Descrevendo a compra de um produto no site "https://www.petz.com.br"

  Scenario: Compra de produto para o PET
    Given acesso o site PETZ
    When consulto um produto "coleira azul"
    And clico na lupa Pesquisa
    And seleciono a coleira Ferplast
    And comparo o nome produto "Coleira Ferplast Dayton Fantasy Azul para Cães"
    And comparo o valor produto "R$ 79,99"
    And clico na lupa "Adicionar Carrinho"
    And comparo o nome do produto carrinho
    Then comparo o preco do produto carrinho

