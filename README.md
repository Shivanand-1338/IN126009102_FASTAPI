# FastAPI Assignment 1 – REST API Development

This project demonstrates the implementation of basic **REST API endpoints using FastAPI**.  
All the endpoints are created inside a single file called **main.py**.  
The API simulates a simple **online store backend** that manages products and allows users to filter, search, and analyze product information.

---

## Technologies Used

- Python
- FastAPI
- Uvicorn

---

## Project Structure

```
FastAPI-Assignment-1
│
├── main.py
├── README.md
```

---

# API Endpoints

## 1. Get All Products

**Endpoint**

```
GET /products
```

**Description**

Returns the list of all available products in the store.

Three additional products were added:

- Laptop Stand
- Mechanical Keyboard
- Webcam

Each product contains the following fields:

- id
- name
- price
- category
- in_stock

---

## 2. Filter Products by Category

**Endpoint**

```
GET /products/category/{category_name}
```

**Description**

Returns products that belong to a specific category.

Example categories:

- Electronics
- Stationery

If no products are found in the given category:

```
{
  "error": "No products found in this category"
}
```

---

## 3. Show Only In-Stock Products

**Endpoint**

```
GET /products/instock
```

**Description**

Returns only products that are currently available in stock.

Response includes:

- List of in-stock products
- Total count of in-stock products

---

## 4. Store Summary Information

**Endpoint**

```
GET /store/summary
```

**Description**

Provides a summary of the store inventory.

Response includes:

- Total number of products
- Number of in-stock products
- Number of out-of-stock products
- List of unique product categories

---

## 5. Search Products by Name

**Endpoint**

```
GET /products/search/{keyword}
```

**Description**

Allows users to search for products using a keyword.

Features:

- Case-insensitive search
- Returns matched products
- Displays total number of matches

If no product matches:

```
{
  "message": "No products matched your search"
}
```

---

## 6. Cheapest & Most Expensive Product

**Endpoint**

```
GET /products/deals
```

**Description**

Returns special product highlights:

- **best_deal** → product with the lowest price
- **premium_pick** → product with the highest price

---

# How to Run the Project

### 1. Install FastAPI and Uvicorn

```
pip install fastapi uvicorn
```

### 2. Run the server

```
uvicorn main:app --reload
```

### 3. Open in browser

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Author

Developed as part of a **FastAPI REST API Assignment**.
