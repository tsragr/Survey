from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_finish = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - date from {self.date_start} date to {self.date_finish}'


class Question(models.Model):
    CHOICES_OF_TYPE = [
        ('#1', 'ответ текстом'),
        ('#2', 'ответ с выбором одного варианта'),
        ('#3', 'ответ с выбором нескольких вариантов')
    ]
    text = models.TextField()
    type = models.CharField(max_length=50, choices=CHOICES_OF_TYPE, default='ответ текстом')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f'{self.survey.name} - {self.text[:45]}'


class PassedSurveys(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    surveys = models.ManyToManyField(Survey, related_name='passed_surveys', blank=True)

    def __str__(self):
        return f'{self.user.username}'
