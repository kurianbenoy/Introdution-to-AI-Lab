# Task 1
#
# Build an Internet Shopping Agent that allows customers to search many
# online retailers and buy at the lowest price.
# • Environment: Website, Customers, retailers
# • Percept: User demand (Product, Price range, brand), Feedback
# • Action: List of products, suggestions

import pandas as pd

products = pd.read_csv("products.csv")
items = pd.read_csv("items.csv")


def select_product(product):
    res = []
    if product != "":
        product_id = ""
        if len(products[products["product"] == product]) > 0:
            res = items[
                items.product_id
                == products[products["product"] == product].iloc[0]["id"]
            ]
        else:
            raise Exception("Product Not Found in Inventory")
    return res


def select_brand(brand, res=items):
    if brand != "":
        if len(res[res["brand"] == brand]) > 0:
            res = res[res["brand"] == brand]
        else:
            raise Exception("Brnad Not Found in Inventory")
    return res


def select_range(minPrice: int, maxPrice: int, res=items):
    if minPrice > maxPrice:
        raise Exception("Min Price cannot be lower than Max Price")
    res = res[res["price"] >= int(minPrice)]
    return res[res["price"] <= int(maxPrice)]


if __name__ == "__main__":
    print("Products Available in Shop:", ", ".join(products["product"].tolist()))
    product_selected = input("Choose a Product: ")
    res = []
    if product_selected != "":
        res = select_product(product_selected)
    else:
        res = items

    print("Brands Available: ", ", ".join(res["brand"]))
    brand_selected = input("Brand Selected. Press 0 if no preferences\n")
    if brand_selected != "0":
        res = select_brand(brand_selected, res)

    print("Do you have a price preference?")
    minPrice = input("Minimum Price: ")
    maxPrice = input("Maximum Price: ")
    res = select_range(minPrice, maxPrice, res)

    if len(res) > 0:
        print("Here are your suggestions: ")
        print("--------------------")
        for index, row in res.iterrows():
            print("Brand:", row["brand"])
            print("Item Name:", row["name"])
            print("Price: Rs.", row["price"])
            print("--------------------")
    else:
        print("Sorry, there are no items according to your interest")
