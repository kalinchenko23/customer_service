from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
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


@receiver(models.signals.pre_save, sender=Document)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_pdf = Document.objects.get(pk=instance.pk).pdf
        except Document.DoesNotExist:
            return
        else:
            new_pdf = instance.pdf
            if old_pdf and old_pdf.url != new_pdf.url:
                old_pdf.delete(save=False)

@receiver(models.signals.pre_save, sender=Profile)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_img = Profile.objects.get(pk=instance.pk).image
        except Profile.DoesNotExist:
            return
        else:
            new_img = instance.image
            if old_img and old_img.url != new_img.url:
                old_img.delete(save=False)
