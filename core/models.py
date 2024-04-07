from django.db import models
import uuid

# Create your models here.
class books_table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    editora = models.CharField(max_length=255)
    state = models.CharField(max_length=255)