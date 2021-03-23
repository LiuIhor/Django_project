from django.contrib import admin
from . import models
from main.models import Profile, User

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'created_at', 'updated_at',)

class AnswersAdmin(admin.ModelAdmin):
	list_display = ('text_answer', 'is_correct', 'question_id', 'created_at', 'updated_at')
	search_fields = ('text_answer', 'created_at', 'updated_at')
	exclude = ('users',)

class QuestionsAdmin(admin.ModelAdmin):
	list_display = ('text_question','created_by_id', 'created_at', 'updated_at')
	search_fields = ('text_question', 'created_at', 'updated_at')

# class QuestionsInline(admin.StackedInline):
#     model = models.Questions
#     filter_horizontal = ('questions',)


class TestsAdmin(admin.ModelAdmin):
	list_display = ('name_test', 'created_at', 'updated_at')
	search_fields = ('name_test', 'created_at', 'updated_at')
	exclude = ('users',)
	# inlines = [QuestionsInline]

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('name_category', 'created_at', 'updated_at')
	search_fields = ('name_category', 'created_at', 'updated_at')

class RolesAdmin(admin.ModelAdmin):
	list_display = ('name_role', 'created_at', 'updated_at')
	search_fields = ('name_role', 'created_at', 'updated_at')

class TestsQuestionsAdmin(admin.ModelAdmin):
	list_display = ('test_id', 'question_id', 'created_at', 'updated_at')
	search_fields = ('test_id__name_test', 'question_id__text_question', 'created_at', 'updated_at')

admin.site.register(models.Answers, AnswersAdmin)
admin.site.register(models.Questions, QuestionsAdmin)
admin.site.register(models.Tests, TestsAdmin)
admin.site.register(models.Categories, CategoriesAdmin)
#admin.site.unregister(User)
admin.site.register(Profile, ProfileAdmin)
#admin.site.register(User)
# admin.site.register(models.Tests_questions, TestsQuestionsAdmin)
