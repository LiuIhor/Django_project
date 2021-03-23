from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import User, Profile, Tests, Categories, Questions, Answers  # , Tests_questions, Users_tests, Users_answers
from .forms import UserRegistrationForm, ProfileForm, UserLoginForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout


def index(request):
	# 	if not request.user.is_authenticated():
	# 		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	return render(request, 'main/index.html')


def auth_abit(request):
	if request.method == "POST":
		first_name = request.POST.get("first_name")
		second_name = request.POST.get("second_name")
		middle_name = request.POST.get("middle_name")
		print(middle_name)
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		role = 2

		abiturient = User.objects.create(first_name=first_name, second_name=second_name, middle_name=middle_name,
										 email=email, phone=phone, role_id_id=int(role))
		abiturients = User.objects.all()
		return render(request, "main/print_db.html", {"abiturients": abiturients, })
	else:
		return render(request, 'main/authorization.html')


def auth_tech(request):
	# if request.method == "POST":
	# 	email = request.POST.get("email")
	# 	password = request.POST.get("password")
	# 	print(f'Login: {email}, password: {password}')
	# 	if not Users.objects.filter(email=email):
	# 		pass
	# else:
	# 	return render(request, 'main/auth_teach.html')

	return render(request, 'main/auth_teach.html')


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.username = user_form.cleaned_data['email']
			new_user.password = user_form.cleaned_data['password']
			new_user.save()
			pf = Profile(
				user= new_user,
				middle_name= profile_form.cleaned_data.get('middle_name'),
				phone = profile_form.cleaned_data.get('phone')
			)
			pf.save()
			# new_user.profile.middle_name=profile_form.cleaned_data["middle_name"]
			new_user.groups.add(Group.objects.get(name='abiturient'))
			return render(request, 'main/register_done.html', {'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
		profile_form = ProfileForm()
	return render(request, 'main/authorization.html', {'user_form': user_form, 'profile_form': profile_form})


def start_test(request):

	return render(request, 'main/register_done.html')

'''
	Представление авторизации. Если пароль и логин корректны, то идет проверка на пренадлежность к группе
'''
def LoginView(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			users_in_group = Group.objects.get(name="abiturient").user_set.all()
			if user in users_in_group:
				return redirect('categories')
			else:
				return redirect('home')
	else:
		form = UserLoginForm()
	return render(request, 'registration/login.html', {"form":form})


