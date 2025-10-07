# Django Internet Shop

Проект интернет-магазина, разрабатываемый в рамках учебного курса по Django.

## 🚀 Описание проекта

Это полнофункциональный интернет-магазин, который будет дорабатываться на протяжении всего курса. Проект включает в себя каталог товаров, страницу контактов и базовую структуру для дальнейшего расширения.

## 🛠️ Технологии

- **Backend**: Django 4.2+
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (для разработки)
- **Version Control**: Git + GitHub

## 📁 Структура проекта


├── catalog/                    
│   ├── migrations/             
│   ├── templates/              
│   ├── __init__.py             
│   ├── admin.py                
│   ├── apps.py                 
│   ├── models.py               
│   ├── tests.py               
│   ├── urls.py                 
│   └── views.py                

├── config/                      
│   ├── __init__.py             
│   ├── asgi.py                
│   ├── settings.py            
│   ├── urls.py                 
│   └── wsgi.py                
│
├── .gitignore                 
├── db.sqlite3                  
├── manage.py                  
├── poetry.lock                 
├── pyproject.toml              
└── README.md     

Для перехода в веб-приложение запустите команду python manage.py runserver и нажмите на ссылку в консоли http://127.0.0.1:8000/