# 💳 Django Razorpay Integration (Dynamic Payment)

This project demonstrates how to integrate **Razorpay Payment Gateway** with a **Django backend** and a **Bootstrap frontend**.  
It allows users to **enter a custom amount** and make payments securely via Razorpay.

---

## 🚀 Features
- Django backend with Razorpay SDK integration  
- Bootstrap 5 styled frontend  
- Dynamic amount entry by user  
- Secure order creation with Razorpay  
- Payment verification via signature check  
- Payment records stored in the database  
- Logging for debugging and error tracking  

---

## 📂 Project Structure
django-razorpay/
│── payments/ # Django app
│ ├── migrations/
│ ├── templates/
│ │ └── payment.html # Bootstrap payment page
│ ├── models.py # Payment model
│ ├── views.py # Razorpay integration logic
│ ├── urls.py # Routes for payment
│ └── admin.py # Register Payment model
│
├── django_razorpay/ # Main project folder
│ ├── settings.py # Django settings
│ └── urls.py # Project routes
│
├── db.sqlite3 # SQLite database (default)
├── manage.py # Django CLI
└── README.md # Documentation



---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-razorpay.git
cd django-razorpay
```
### 2. Create Virtual Environment & Install Dependencies
```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
(Create requirements.txt with at least Django and razorpay)
```
#### 3. Configure Razorpay Keys
Open settings.py and add your Razorpay API Keys:
```bash
RAZORPAY_KEY_ID = "your_key_id"
RAZORPAY_KEY_SECRET = "your_key_secret"
```
You can get these keys from the Razorpay Dashboard.

### 4. Run Migrations
```bash

python manage.py makemigrations
python manage.py migrate
```
### 5. Create Superuser (optional, for admin panel)
```bash
python manage.py createsuperuser
```
### 6. Run Development Server
```bash

python manage.py runserver
```
