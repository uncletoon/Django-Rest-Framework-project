<h1>PRODUCT LIST SAMPLE REST API</h1>

<p>“My API is the first api i built and deployed, which was very enjoyable to learn from, and practices that improved my skills in REST API and Django as well.”</p>

# 🌐 Django REST API 

A lightweight and scalable **REST API built with Django and Django REST Framework**, deployed on **Render Cloud**.
This API provides structured endpoints for CRUD operations, authentication, and data management.

---

## 🚀 **Live API Base URL**

https://rest-api-deploy-zotq.onrender.com/api/products/


---

# 📘 **Features**

* ✔️ Django REST Framework–powered endpoints
* ✔️ JWT Authentication 
* ✔️ Pagination, filtering & search support
* ✔️ Fully deployed on Render
* ✔️ Environment-based configuration
* ✔️ Admin panel enabled


# 🔧 **Tech Stack**

| Component  | Technology                          |
| ---------- | ----------------------------------- |
| Backend    | Django, Django REST Framework       |
| Auth       | JWT (djangorestframework-simplejwt) |
| Database   | PostgreSQL (Render)                 |
| Deployment | Render Web Service                  |

---

# ⚙️ **Setup & Installation**

## **1️⃣ Clone the Repository**

```bash
git clone https://github.com/username/repository.git
cd backend
```

## **2️⃣ Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

## **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

## **4️⃣ Apply Migrations**

```bash
python manage.py migrate
```

## **5️⃣ Create Superuser**

```bash
python manage.py createsuperuser
```

## **6️⃣ Run Locally**

```bash
python manage.py runserver
```

---

# 🌍 **Environment Variables (`.env`)**

Create a `.env` file:

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-render-postgres-url
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1

#Here I just used ALGORIA
ALGOLIA_APP_ID='Your ID'
ALGOLIA_API_KEY='Your Algolia key if you have one'
```


# 🧪 **Main API Endpoints**

## **📌 Authentication**

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| POST   | `/api/token/`   | Login and get JWT     |
| POST   | `/api/token/refresh/` | Refresh the JWT token |

---

<p>Username: staff</p>
<p>Password: Mumahanga</p>
<p>This user is for testing. You can Create, Update, Read, and Delete. except the Data that created by <u><b>ADMIN</b></u>.</p>

## **📌 Products / Items Example**

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| GET    | `/api/products/`      | List all products       |
| POST   | `/api/products/`      | Create a product        |
| GET    | `/api/products/<id>/` | Retrieve single product |
| PUT    | `/api/products/<id>/` | Update product          |
| DELETE | `/api/products/<id>/` | Delete product          |

---

## **📌 Search Endpoint**

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| GET    | `/api/search/?q=text` | Search products or data |

---

## **📌 API Documentaion / Items Example**

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| GET    | `api/api/schema/swagger-ui/`      | APO Documentation       |
| GET   | `/api/api/schema/redoc/`      | Redoc        |
| GET    | `api/api/schema/` | Schema ymal |


# 🛠 **How It Works**

### **1. Client sends a request**

The frontend or Postman sends HTTP requests to the `/api/...` endpoints.

### **2. Views process logic**

Django views handle CRUD operations using DRF serializers.

### **3. Database interaction**

If using Render PostgreSQL, the API reads/writes through `DATABASE_URL`.

### **4. Response returned**

JSON responses are structured like:

```json
{
  "owner": {
      "username": "toon",
      "id": 1
  },
  "url": "https://rest-api-deploy-zotq.onrender.com/api/products/1/",
  "pk": 1,
  "title": "Nike shoes",
  "content": "Best shoes in 2025",
  "price": "600.00",
  "sale_price": "480.00",
  "public": true
},
```

---

# 🧭 **Using the API With Postman**

1. Open Postman
2. Enter your Render URL:
   `https://your-app-name.onrender.com/api/products/`
3. For protected routes:

   * Add a **Bearer Token**
   * Paste JWT from `/api/token/`

---


# 📄 **Common Django Commands**

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
pip freeze > requirements.txt
```

---

# 🤝 **Contributing**

Pull requests are welcome!
For major changes, please open an issue first.

---

# 📝 **License**

MIT License — Free to use.

---
