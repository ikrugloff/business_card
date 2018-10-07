from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=36, blank=False, null=False)  # null=False -> a title should be
    photo = models.ImageField(blank=False, null=False)
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    # 58:50 29092018; null=True иначе не даст накатить

    def __str__(self):
        return f'{self.title}'
