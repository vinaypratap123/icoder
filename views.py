from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
# ---------------------------------------------Home Function-----------------------------------------------


def home(request):
    messages.success(request, 'Welcome to Home Page')
    return render(request, "home/home.html")
# ---------------------------------------------About Function-----------------------------------------------


def about(request):
    messages.success(request, 'Welcome to About Page')
    return render(request, "home/about.html")
# ---------------------------------------------Contact Function-----------------------------------------------


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(content) < 4:
            messages.error(request, 'Please fill the form correctly')
        else:
            contacts = Contact(name=name, email=email, phone=phone, content=content)
            contacts.save()
            messages.success(request, 'Your message has been successfully sent')
    return render(request, "home/contact.html")
# ---------------------------------------------Search Function-----------------------------------------------


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        all_post = Post.objects.none()
    else:
        all_post_title = Post.objects.filter(title__icontains=query)
        all_post_content = Post.objects.filter(content__icontains=query)
        all_post = all_post_title.union(all_post_content)

    if all_post.count() == 0:
        messages.warning(request, 'no search result found')
    params = {'allPost': all_post, 'query': query}
    return render(request, "home/search.html", params)
# ---------------------------------------------SignUp Handel Function-----------------------------------------------


def sign_up(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        phone = request.POST['phone']
        if len(username) > 20:
            messages.error(request, 'username must be under 20 character')
            return redirect('home')
        if password != password1:
            messages.error(request, 'password do not match')
        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = f_name
        my_user.last_name = l_name
        my_user.save()
        messages.success(request, "your account is created")
        return redirect('home')
    else:
        return HttpResponse("404 : page not found")
# ---------------------------------------------Login Handel Function-----------------------------------------------


def user_login(request):
    if request.method == 'POST':
        login_user2 = request.POST['login_user2']
        password2 = request.POST['password2']
        user = authenticate(username=login_user2, password=password2)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are Login')
            return redirect('home')
        else:
            messages.error(request, ' Login Failed Please Try Again')
            return redirect('home')
    return HttpResponse("404 : Page Not Found")
# ---------------------------------------------Logout Handel Function-----------------------------------------------


def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully Logout')
    return redirect('home')





