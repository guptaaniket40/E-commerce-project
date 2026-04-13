# 🛒 Django DRF eCommerce API

A simple eCommerce backend built using **Django** and **Django REST Framework (DRF)** with **PostgreSQL**.

---

## 🚀 Features

* Product CRUD API
* Cart System
* Add to Cart
* View Cart
* Checkout System
* Order & Payment (Basic)
* PostgreSQL Database
* Environment Variables using `.env`

---

## 🏗️ Project Structure

```
ecommerce/
│
├── ecommerce/        # Project settings
├── shop/             # Main app (Product, Cart, Order)
├── manage.py
├── .env              # Environment variables
├── .gitignore
├── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ecommerce.git
cd ecommerce
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup `.env` file

Create a `.env` file in root:

```
DEBUG=True

SECRET_KEY=your_secret_key

DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Run server

```
python manage.py runserver
```

---

## 📡 API Endpoints

### 🔹 Product

* `GET /api/products/` → Get all products
* `POST /api/products/` → Create product
* `GET /api/products/<id>/` → Get single product
* `PUT /api/products/<id>/` → Update product
* `DELETE /api/products/<id>/` → Delete product

---

### 🔹 Cart

* `POST /api/cart/create/` → Create cart
* `POST /api/cart/add/` → Add product to cart
* `GET /api/cart/<cart_id>/` → View cart

---

### 🔹 Checkout

* `POST /api/checkout/` → Place order

---

## 🧪 Testing

Use tools like **Postman** to test APIs.

---

## 🔐 Environment Variables

Make sure `.env` file is not pushed to GitHub.
Add it to `.gitignore`.

---

## 📦 Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL

---

## 📌 Future Improvements

* User Authentication (JWT)
* Payment Gateway Integration (Razorpay/Stripe)
* Product Images
* Order History
* Admin Dashboard

---

## 👨‍💻 Author

Aniket Gupta

---

## ⭐ Note

This is a beginner to intermediate level project for learning Django REST Framework.
