from manegement import get_product_by_id, get_products_by_type, menu_report, add_product, calculate_tab


def main():
    # item_1 = get_product_by_id(31)
    # print(item_1)
    
    # item_2 = get_products_by_type('vegetable')
    # print(item_2)
    
    # item_3 = menu_report()
    # print(item_3)

    # new_product = {
    #     "title": "X-Python",
    #     "price": 5.0,
    #     "description": "Sanduiche de Python",
    #     "type": "fast-food",
    #     "rating": 5
    # }
    # new_list = []
    # add_product([], **new_product)
    
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    # print(calculate_tab(table_2))



if __name__ == "__main__":
    main()