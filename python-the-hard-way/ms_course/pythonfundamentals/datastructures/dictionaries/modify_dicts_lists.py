shopping_list = ["apples", "bananas", "milk"]  # List for items
item_quantities = {"apples": 3, "bananas": 1}  # Dictionary for quantities

# User adds an item
shopping_list.append("eggs")
item_quantities["eggs"] = 12 

# User increases the quantity of bananas
item_quantities["bananas"] += 2

# User removes apples
shopping_list.remove("apples")
del item_quantities["apples"]

# Print updated list and dictionary
print(shopping_list)
print(item_quantities)

product_catalog = {
    "SKU123":{"name":"Widget A","price":19.99,"quantity":50},
    "SKU456":{"name":"Gadget B","price":34.95,"quantity":25},
    "SKU789":{"name":"Gizmo C","price":9.99,"quantity":100}
}

sku = product_catalog.get("SKU123")
price = sku.get("price")
print(price)