from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)



class postdetails_model(models.Model):

    names = models.CharField(max_length=300)
    f_story= models.CharField(max_length=500)
    t_price = models.CharField(max_length=200)
    fcat = models.CharField(max_length=300)
    t_name = models.CharField(max_length=300)
    topics = models.CharField(max_length=300)
    c_name = models.CharField(max_length=300)
    senderstatus = models.CharField(default="process", max_length=300 )
    ratings = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    sanalysis= models.CharField(max_length=300)
    DT = models.CharField(max_length=300)


class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    fname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)
    rtype = models.CharField(max_length=300)

class attack_Model(models.Model):
    uname = models.CharField(max_length=100)
    dcont = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    pname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class rating_Model(models.Model):
    uname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    fc = models.CharField(max_length=100)
    dt = models.CharField(max_length=300)
    yc = models.CharField(max_length=300)
    rtype = models.CharField(max_length=300)
    rate = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    f_story= models.CharField(max_length=300)




