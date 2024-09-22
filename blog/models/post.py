from django.db import models
from django.contrib.auth.models import User 

STATUS = (
    (0, "Rascunho"),
    (1, "Publicar")
)

class Post(models.Model):
    título = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postagem_do_blog')
    updated_on = models.DateTimeField(auto_now=True)
    conteúdo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.título

