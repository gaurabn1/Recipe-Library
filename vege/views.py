from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Please Enter a Valid Username')
            return redirect('login')

        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, 'Incorrect Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('recipe')

    return render(request, 'login.html')

def logout_page(request):
    
    logout(request)
    return redirect('login')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username already taken.')
            return redirect('register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
        )
        user.set_password(password)
        user.save()
        print(first_name)
        messages.info(request, 'Account created successfully.')
        return redirect('register')
    
    return render(request, 'register.html')


@login_required(login_url='/login/')
def recipe(request):
    
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')

        Recipe.objects.create(
            recipe_name = recipe_name, 
            recipe_description = recipe_desc,
            recipe_image =  recipe_img
        )
        return redirect('/recipes/')
    
    
    
    return render(request, 'add-recipes.html')

@login_required(login_url='login')
def import_recipe(request):
    queryset = Recipe.objects.all()
    context = {'recipes' : queryset}
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
        context = {'recipes': queryset}
        return render(request, 'recipes.html', context)
    return render(request, 'recipes.html', context)

    


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_img')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_desc
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        
        return redirect('/recipes/')

    context = {
        'recipe' : queryset
    }

    return render(request, 'update_recipes.html', context)




