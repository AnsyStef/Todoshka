from django.db import models

class Notes(models.Model):
    priority_list = (('3','Очень важно'),
        ('2','Важно'),
        ('1','Не важно'),)

    name = models.CharField('Название', max_length=50, blank= False)
    description = models.TextField('Описание', blank = True)
    priority = models.CharField('Важность', choices=priority_list, max_length=15)
    date = models.DateTimeField('Дата создания', auto_now = True)
    is_public = models.BooleanField('Публично', default=True)
    worker = models.CharField('Исполнитель', max_length=15, blank= True)
    status = models.CharField('Выполнено', max_length=50, blank=True, default='Ожидает исполнителя')
    creator = models.CharField('Создатель', max_length=15, blank=False, default='System')

    def __str__(self) -> str:
        return self.name.__str__()

class Group(models.Model):
    group_name = models.CharField('Название группы', max_length=15, blank=False)
    group_password = models.CharField('Пароль группы', max_length=30, blank=True)

class User(models.Model):
    username = models.CharField('Логин', max_length=15, blank=False)
    password = models.CharField('Пароль', max_length=30, blank=False)

class Profile(models.Model):
    from django.contrib.auth.models import User
    group = models.IntegerField('Группа пользователя', null=True, blank=True, default=0)
    rank = models.CharField('Должность', null=True, blank=True, default='Пользователь', max_length=13)
    trust_factor = models.IntegerField('Уровень доверия', null=False, blank=False, default=50)
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)
