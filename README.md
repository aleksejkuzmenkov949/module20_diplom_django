1.	Проект DiplomDjango — это веб-приложение, разработанное на основе фреймворка Django. 
Основное приложение, DjangoNotes, ориентировано на управление заметками, предлагая пользователям интуитивно понятный интерфейс для создания, редактирования и удаления заметок. 
Важным аспектом проекта является его архитектура MVT (Model-View-Template), MVT архитектура: Используются модели (Model) для представления данных заметок, представления (View) для обработки логики и шаблоны (Template) для интерфейса. Модель отвечает за структуру данных и их взаимодействие с базой данных, представления обрабатывают запросы и передают информацию, а шаблоны отображают ее пользователю.
 Кроме того, приложение активно использует Django Forms, что упрощает процесс создания и валидации форм для заметок. Django Forms: Применяются для создания и валидации форм, что упрощает процесс работы с пользовательским вводом и обработку ошибок.
Аутентификация: Пользовательские функции регистрации и входа в систему улучшены с использованием встроенных форм Django.
Это позволяет улучшить пользовательский опыт, обеспечивая надежность и удобство ввода данных.
 DjangoNotes не только демонстрирует возможности MVT и форм Django, но и предлагает пользователям эффективный инструмент для организации заметок, сочетающий простоту использования с мощным функционалом.

DiplomDjango/
    ├── DjangoNotes/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    ├── DiplomDjango/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── templates/
    │   ├── base.html
    │   ├── note_list.html
    │   ├── note_form.html
    │   ├── register.html
    │   ├── login.html
    ├── manage.py

Чтобы запустить проект в pycharm нужно прописать в терминале коанду :python manage.py runserver

Требования к проекту указаны в requirements.txt

При переходе по ссылке  http://127.0.0.1:8000/ запускается  проект.

Дальнейшие внутренние действия в проекте отображены в приложенных скриншотах.

Отображены все действия в соответствии с маршрутизацией :
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_list, name='note_list'),
    path('create/', note_create, name='note_create'),
    path('update/<int:pk>/', note_update, name='note_update'),
    path('delete/<int:pk>/', note_delete, name='note_delete'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),

]

студент Кузьменков Алексей
