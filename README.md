
# Personal Blog Website 📝

This is a **personal blog website** built using **Django**, where I share posts, ideas, and content in a simple and clean layout.
The project focuses on learning Django fundamentals such as models, views, templates, and authentication.


## 🚀 Features

* User authentication (login / logout)
* Create, edit, and delete blog posts
* Dynamic content using Django templates
* Admin panel for managing posts
* Responsive design (CSS/Bootstrap)
* Secure backend powered by Django

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Bootstrap)
* **Database:** SQLite (default Django database)
* **Version Control:** Git & GitHub

## 📂 Project Structure

```
personal-blog/
│
├── blog/            
├── personal_blog/           
├── profile_app/       
├── templates/          
├── manage.py
└── requirements.txt
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/abdalsamieali/personal_blog.git
   ```

2. **Navigate to the project folder**

   ```bash
   cd personal_blog
   ```

3. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**

   * Windows:

     ```bash
     venv\Scripts\activate
     ```
   * macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

9. Open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

---

## 🔐 Admin Panel

Access the Django admin panel at:

```
http://127.0.0.1:8000/admin/
```

Use the superuser credentials you created to manage blog posts and users.



## 📌 Future Improvements

* Add comments system
* Add categories and tags
* Improve UI/UX
* Deploy to production (Render / Railway / Heroku)
* Add REST API using Django REST Framework


## 👤 Author

**Abdalsamie Ali**
Personal project built to practice Django and web development.



## 📄 License

This project is for learning and personal use.


Just tell me 👍
