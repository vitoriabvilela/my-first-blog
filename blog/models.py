from django.conf import settings
from django.db import models
from django.utils import timezone


# define o nosso modelo
class Post(models.Model):  # models.Model significa que o Post é um modelo de Django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)  # nao entendi os parametros

    def publish(self):
        self.published_date = timezone.now()    # isso significa que n eh obrigado a marcar?
        self.save()

#  quando chamarmos __str__(), obteremos um texto (string) com o título do Post.
    def __str__(self):
        return self.title

