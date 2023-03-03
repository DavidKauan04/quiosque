from menu import products

def calculate_tab(table: list):
    soma = 0

    for product in table:
        find_product = [prod for prod in products if prod["_id"] == product["_id"]]

        print(find_product)
        print('*' * 50)

        soma = soma + find_product[0]["price"] * product["amount"]

    return {'subtotal': f"${round(soma, 2)}"}
