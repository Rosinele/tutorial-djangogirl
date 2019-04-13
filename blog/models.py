from django.db import models
from django.utils import timezone

#Class significa que vamos definir um objeto
class Post(models.Model): #Post é o nome do nosso Modelo. Models.Model Indica que Post é um modelo do django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #ForeignKey link para outro modelo
    title = models.CharField(max_length=200) #CharField texto com numero limitado de caractere
    text = models.TextField() #TextField texto sem limite fixo
    create_date = models.DateTimeField( #Data e hora
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title