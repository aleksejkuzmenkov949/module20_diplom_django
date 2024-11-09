from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Note
from .forms import NoteForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Список заметок
def note_list(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)
    else:
        notes = []  # Можно отобразить сообщение о необходимости авторизации
    return render(request, 'note_list.html', {'notes': notes})

# Создание новой заметки
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if request.user.is_authenticated and form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

# Обновление существующей заметки
def note_update(request, pk):
    if request.user.is_authenticated:
        note = Note.objects.get(pk=pk)
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('note_list')
        else:
            form = NoteForm(instance=note)
        return render(request, 'note_form.html', {'form': form})
    else:
        return redirect('login')  # Перенаправление на страницу входа для неавторизованных пользователей

# Удаление заметки
def note_delete(request, pk):
    if request.user.is_authenticated:
        note = Note.objects.get(pk=pk)
        note.delete()
        return redirect('note_list')
    else:
        return redirect('login')  # Перенаправление на страницу входа для неавторизованных пользователей

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Авторизация пользователя
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('note_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Выход из аккаунта
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('note_list')  # Перенаправление на список заметок после выхода
    return render(request, 'logout.html')
