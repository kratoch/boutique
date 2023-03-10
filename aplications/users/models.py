from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User

fsObj = FileSystemStorage(location='boutique/media')  # for change the path where django save objects images.


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(null=True, blank=True, max_length=200)
    cellphone = models.CharField(null=True, blank=True, max_length=20)
    phone = models.CharField(null=True, blank=True, max_length=20)
    profileImage = models.ImageField(upload_to='profiles_images_persons', blank=True, storage=fsObj,
                                     verbose_name="Imagen de perfil")
    changeImage = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return 'id: %s %s %s ---- Usuario: %s' % \
               (self.id, self.user.first_name, self.user.last_name, self.user.username)
