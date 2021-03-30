from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class MusicType(models.Model):
    musicType = models.CharField(max_length=200)

    def __str__(self):
        return str(self.musicType)

    class Meta:
        verbose_name = 'Music Type'

class Music(models.Model):
    name = models.CharField(max_length=200)
    music = models.FileField(upload_to='')
    musicType = models.ForeignKey(MusicType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Music'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    musicType = models.ManyToManyField(MusicType)

    def __str__(self):
        return str(self.user)

class Ads(models.Model):
    name = models.CharField(max_length=200)
    music = models.FileField(upload_to='ads')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Ad'

def createProfile(sender, **kwargs):
    if kwargs['created']:
        userProfile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)
# class EnClassicMusic(models.Model):
#     enClassic = models.FileField(upload_to='en_classic')

#     def __str__(self):
#         return str(self.enClassic)

#     class Meta:
#         verbose_name = 'Classic english'

# class ArPopMusic(models.Model):
#     arPop = models.FileField(upload_to='ar_pop')

#     def __str__(self):
#         return str(self.arPop)

#     class Meta:
#         verbose_name = 'Pop arabic'

# class ArRomanticMusic(models.Model):
#     arRomantic = models.FileField(upload_to='ar_romantic')

#     def __str__(self):
#         return str(self.arRomantic)

#     class Meta:
#         verbose_name = 'Romantic arabic'

# class ArClassicMusic(models.Model):
#     arClassic = models.FileField(upload_to='ar_classic')

#     def __str__(self):
#         return str(self.arClassic)

#     class Meta:
#         verbose_name = 'Classic arabic'