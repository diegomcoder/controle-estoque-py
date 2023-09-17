menu_primary = """
    (1) Iniciar com estoque vazio
    (2) Carregar estoque demonstrativo
    (3) Fechar o controle de estoque
    """
    
menu_main = """
    (1) Inventário de estoque
    (2) Cadastrar novo produto
    (3) Consulta de estoque
    (4) Fechar o controle de estoque
    """
    
stock_status = """
    🔴 STATUS DE ESTOQUE - - - - - - - - - - - - - - - -

    SALDO QUANTIDADE DE PRODUTOS: @totquantity
    VALOR TOTAL EM ESTOQUE: R$ @totbalance
    PREÇO MÉDIO DOS PRODUTOS: R$ @avgprice
    PREÇO MÍNIMO: R$ @minprice
    PREÇO MÁXIMO: R$ @maxprice
    CAPACIDADE MÁXIMA DO ESTOQUE: @maxcapacity produtos
    NÍVEL DE ESTOQUE: @level %
    NÚMERO DE CATEGORIAS: @ctgcount

    """