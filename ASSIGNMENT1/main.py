from fastapi import FastAPI

app = FastAPI()

# Temporary product database
product_list = [
    {"id": 1, "name": "Smartphone", "price": 19999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Bluetooth Speaker", "price": 2999, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Running Shoes", "price": 3999, "category": "Fashion", "in_stock": True},
    {"id": 4, "name": "Backpack", "price": 1499, "category": "Accessories", "in_stock": True},

    # Newly added products
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False}
]

# Home Endpoint
@app.get("/")
def welcome():
    return {"message": "Welcome to FastAPI Product Service"}

# Q1 - Get all products
@app.get("/products")
def list_products():
    return {
        "items": product_list,
        "total_products": len(product_list)
    }

# Q2 - Filter by category
@app.get("/products/category/{category_name}")
def category_products(category_name: str):

    filtered = []
    for item in product_list:
        if item["category"].lower() == category_name.lower():
            filtered.append(item)

    if len(filtered) == 0:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "results": filtered,
        "count": len(filtered)
    }

# Q3 - Only in stock products
@app.get("/products/instock")
def available_products():

    available = [item for item in product_list if item["in_stock"] == True]

    return {
        "available_products": available,
        "total_available": len(available)
    }

# Q4 - Store summary
@app.get("/store/summary")
def store_details():

    total = len(product_list)
    in_stock_count = sum(1 for item in product_list if item["in_stock"])
    out_stock_count = total - in_stock_count

    category_set = set()
    for item in product_list:
        category_set.add(item["category"])

    return {
        "store_name": "Online Store",
        "total_products": total,
        "in_stock_products": in_stock_count,
        "out_of_stock_products": out_stock_count,
        "categories": list(category_set)
    }

# Q5 - Search products
@app.get("/products/search/{keyword}")
def find_products(keyword: str):

    result = []
    for item in product_list:
        if keyword.lower() in item["name"].lower():
            result.append(item)

    if not result:
        return {"message": "No products matched your search"}

    return {
        "search_keyword": keyword,
        "results": result,
        "matches": len(result)
    }

# Q6 - Best deal and premium pick
@app.get("/products/deals")
def product_highlights():

    cheapest = min(product_list, key=lambda x: x["price"])
    expensive = max(product_list, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }
