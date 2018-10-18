from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=36, blank=False, null=False)  # null=False -> a title should be
    description = models.TextField(blank=True, null=True)  # unique=True if needed
    start_date = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='pictures', blank=False)  # How to avoid issues if already has a string w/o img?
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    file = models.FileField(upload_to='files', blank=True)  # Dir 'files' will be created automatically
    # 58:50 29092018; null=True иначе не даст накатить

    def __str__(self):
        return f'{self.name}'
