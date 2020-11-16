from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ExifTags
from django.urls import reverse
from django.dispatch import receiver
import os


# Create your models here.
def rotate_image(filepath):
  try:
    image = Image.open(filepath)
    for orientation in ExifTags.TAGS.keys():
      if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    image.save(filepath)
    image.close()
  except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    rank = models.CharField(max_length=3,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            size = (400, 400)

            img.thumbnail(size, Image.ANTIALIAS)
            background = Image.new('RGBA', size, (255, 255, 255, 0))
            background.paste(
                img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
            background = background.convert("RGB")
            background.save(self.image.path)

class Document(models.Model):
    created_by=models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    title =models.CharField(max_length=100)
    pdf = models.FileField(blank=True, upload_to='profile_pdf')
    def __str__(self):
        return f'{self.created_by} Document'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)


class ACFT(models.Model):
    pushaps_choices=[tuple([x,x]) for x in range(1,61)]
    dead_lift_choices=[tuple([x,x]) for x in range(140,341,10)]
    leg_tucks_choices=[tuple([x,x]) for x in range(21)]


    owner=models.ForeignKey(User,null=True,on_delete= models.CASCADE)
    pushups=models.IntegerField(choices=pushaps_choices, max_length=2)
    ball=models.CharField(blank=True, max_length=4)
    sprint_drag=models.CharField(blank=True, max_length=5)
    leg_tucks=models.IntegerField(choices=leg_tucks_choices, max_length=2)
    run=models.CharField(blank=True, max_length=5)
    dead_lift=models.IntegerField(choices=dead_lift_choices, max_length=3)
    def __str__(self):
        return f'{self.owner} ACFT'



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


@receiver(models.signals.post_save, sender=Profile, dispatch_uid="update_image_profile")
def update_image(sender, instance, **kwargs):
  if instance.image:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fullpath = BASE_DIR + instance.image.url
    rotate_image(fullpath)
