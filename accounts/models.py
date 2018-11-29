from django.db import models
from django.contrib.auth.models import User
from random import choice
from django.shortcuts import reverse
from django.contrib.auth.validators import ASCIIUsernameValidator

gender= (
    ("Male","Male"),
    ("Female","Female")
)

languages= (
    ("Türkçe","Türkçe"),
    ("English","English")
)


class PROFILE(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    birthday    = models.DateField(verbose_name="Birthday",blank=False,null=False)
    gender      = models.CharField(max_length=15, blank=False,null=False,choices=gender)
    language    = models.CharField(max_length=20, blank=False,null=False,verbose_name="language",choices=languages)
    p_photo     = models.ImageField(verbose_name="ProfilePhoto",blank=True,upload_to="profile_photo")
    
    def set_token(self):

        self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])

    def save(self, *args, **kwargs):
        super(PROFILE, self).save(*args, **kwargs)
        self.set_token()

    class Meta:

        verbose_name_plural = 'PROFILE'
        ordering= ["id"]

    def __str__(self):
        return "{}".format(self.user.username)
    

 
class QUESTIONS(models.Model):
    author          = models.ForeignKey(User, on_delete=models.CASCADE) #KUllanıcıyı silince tüm sorular gidecek on_delete
    question        = models.CharField(max_length=150)
    answer_one      = models.CharField(max_length=20)
    answer_two      = models.CharField(max_length=20)
    answer_three    = models.CharField(max_length=20)
    answer_true     = models.CharField(max_length=20)
    created_date    = models.DateField(auto_now_add=True)
    coupling_number = models.IntegerField(default=1)
    coupling_count  = models.IntegerField(default=1)
    act_deact       = models.BooleanField(default=True)
    likes           = models.ManyToManyField(User,blank=True, related_name='post_likes')
    timestamp       = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("accounts:question", kwargs={"id": self.id})

    def get_like_url(self):
        return reverse("accounts:like-toggle", kwargs={"id": self.id})
    def get_api_like_url(self):
        return reverse("accounts:like-api-toggle", kwargs={"id": self.id})
    

    class Meta:
        verbose_name_plural = "QUESTIONS"
        ordering = ["-timestamp"]

    def __str__(self):
        return "{}".format(self.question)

class COUPLING(models.Model):
    match_user    = models.ForeignKey(User,on_delete=models.CASCADE,related_name="match_user")
    matched_user    = models.ForeignKey(User,on_delete=models.CASCADE,related_name="matched_user")
    
    
    class Meta:
        verbose_name_plural = "COUPLING"
        ordering = ["match_user"]

class LIKE_DISLIKE(models.Model):
    question        = models.ForeignKey(QUESTIONS, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    like_dislike    = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "LIKE_DISLIKE"
        ordering = ["question"]

    def __str__(self):
        return '%s ==== %s' % (self.question, self.user)

