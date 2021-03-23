from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    #
    # def __unicode__(self):
    # 	return u' %s %s %s ' % (self.user, self.middle_name, self.phone)

    def __str__(self):
        return f"{self.user.username} {self.user.last_name} {self.user.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
# def create_profile(sender, **kwargs):
#     user = kwargs['instance']
#     if kwargs['created']:
#         user_profile = Profile.objects.create(user=user)
#         user_profile.save()
#
# post_save.connect(create_profile, sender=User)


class Categories(models.Model):
    name_category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Questions(models.Model):
    category_id = models.ForeignKey(Categories, verbose_name="category", on_delete=models.CASCADE)
    created_by_id = models.ForeignKey(User,verbose_name="created", on_delete=models.CASCADE)
    text_question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.text_question[0:50]

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"

class Tests(models.Model):
    category_id = models.ForeignKey(Categories, verbose_name="category", on_delete=models.CASCADE)
    name_test = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    # users = models.ManyToManyField(Users)
    questions = models.ManyToManyField(Questions)

    def	__str__(self):
        return self.name_test

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"

class Users_tests(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
    result = models.FloatField(blank=True)
    passed_questions = ArrayField(models.CharField(max_length=200), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)



# class Tests_questions(models.Model):
# 	test_id = models.ForeignKey(Tests,verbose_name="test", on_delete=models.CASCADE)
# 	question_id = models.ForeignKey(Questions, verbose_name="question", on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
# 	updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
#
# 	class Meta:
# 		verbose_name = "question in test"
# 		verbose_name_plural = "questions in tests"

class Answers(models.Model):
    question_id = models.ForeignKey(Questions, verbose_name="question", on_delete=models.CASCADE)
    text_answer = models.TextField()
    is_correct = models.BooleanField()
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.text_answer[:50]
    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

# class Users_answers(models.Model):
# 	user_test_id = models.ForeignKey(Users_tests, on_delete=models.CASCADE)
# 	answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
# 	updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
# courses = models.ManyToManyField(Course)

