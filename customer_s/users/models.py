from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Document(models.Model):
    created_by=models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    title =models.CharField(max_length=100)
    pdf = models.FileField(default='POV_Inspection_checklist.pdf', upload_to='profile_pdf')
    def __str__(self):
        return f'{self.created_by} Document'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
