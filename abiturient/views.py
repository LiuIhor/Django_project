from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import User, Users_tests, Tests, Categories, Questions, Answers #, Tests_questions, Users_tests, Users_answers
import random
from collections import OrderedDict
from django.http import JsonResponse
from django.core import serializers

def shuffle_dict(d):
    keys = list(d.keys())
    random.shuffle(keys)
    return OrderedDict([(k, d[k]) for k in keys])

@login_required(login_url='/accounts/login/')
def categories(request):
	categories = Categories.objects.all()
	return render(request, 'abiturient/categories.html', {"categories":categories})


def tests(request, category_id):
	#tests = Tests.objects.raw('select * from main_tests where category_id_id = '+str(test_id))
	tests = Tests.objects.filter(category_id=category_id)
	print(tests)
	print(tests[0].name_test)
	return render(request, 'abiturient/tets.html', {"tests": tests})


def questions(request, test_id):
	start = 0
	if request.method == "GET":
		questions = Tests.objects.get(id=test_id).questions.all().order_by('?')
		# dict_ques = {}
		# i=0
		# for q in questions:
		# 	dict_ques[i]=q
		# 	i+=1
		# print(len(dict_ques))
		# questions_json = serializers.serialize('json', questions)
		# print("question", questions)
		# print("TYPE:",type(questions))
		# print("JSON", questions_json)
		# answers = Answers.objects.filter(question_id=dict_ques[start].id)
		# print(answers)
		return render(request, 'abiturient/questions.html', {"questions": questions})

	else:
		pass



# # получим все курсы студента
# courses = Student.objects.get(name="Tom").courses.all()
#
# # получаем всех студентов, которые посещают курс Алгебра
# studes = Student.objects.filter(courses__name="Algebra")
#Publication.objects.get(id=4).article_set.all()