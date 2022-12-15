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


class User(models.Model):
    username = models.CharField('Логин', max_length=15, blank=False)
    password = models.CharField('Пароль', max_length=30, blank=False)