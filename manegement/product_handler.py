from menu import products

def get_product_by_id(id_busca: int):
    if type(id_busca) != int:
        raise TypeError("product id must be an int")
    
    for product in products:
        if id_busca == product.get('_id'):
            return product
        
    return {}


def get_products_by_type(type_product: str):
    if type(type_product) != str:
        raise TypeError("product type must be a str")
    filter_type = []
    for prod in products:
        if prod.get('type') == type_product:
            filter_type.append(prod)
            
    if len(filter_type) > 0 :
        return filter_type
    
    return {}


def menu_report():
    contagem_de_produtos = 0
    preco_medio = 0
    tipo_mais_comum = ''
    
    list_type = [product['type'] for product in products]
    
    for index, prod in enumerate(products):
        contagem_de_produtos = 1 + index
        price = prod.get('price')
        preco_medio = preco_medio + price

    for type in list_type:
        count_1 = 0
        count_2 = list_type.count(type)

        if count_2 > count_1:
            count_1 = count_2
            tipo_mais_comum = type
    
    preco_medio = round(preco_medio / contagem_de_produtos, 2)
    
    return f"Products Count: {contagem_de_produtos} - Average Price: {preco_medio} - Most Common Type: {tipo_mais_comum}"

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# add products features

def key_verification(dict: dict, *args: str):
    dictionary_keys = list(dict.keys())

    for key in args:
        if not dictionary_keys.count(key):
            raise KeyError(f'Está faltando um campo obrigatorio: --> {key} ')


def generate_id(menu):
    id = 1
    
    if len(menu) > 0:
        id_menu = [menu['_id'] for product in products]
        
        while id < len(id_menu):
            if not id_menu.count(id):
                return id
            else:
                id = id + 1
    
    else:
        return 1

    return id + 1


def add_product(menu: list, **kwargs):
    key_verification(kwargs, "description", "price", "rating", "title", "type")
    
    kwargs['_id'] = generate_id(menu)
    
    menu.append(kwargs)
    
    return kwargs

