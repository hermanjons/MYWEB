from django.db import models

from django.utils.text import slugify


from ckeditor.fields import RichTextField

class Users(models.Model):
    username=models.CharField(max_length=50,verbose_name="kullanıcı adı")
    userimage=models.ImageField(verbose_name="kullanının resmi")
    userrealname=models.CharField(max_length=100,verbose_name="kullanıcın gerçek ad-soyad'ı ")

class Infoabouttek(models.Model):
    infoname=models.CharField(max_length=100,verbose_name="Bilginin konusu")
    infotext=RichTextField(verbose_name="Konunun yazısı")





class Quote(models.Model):
    
    quoteday=models.CharField(max_length=120,verbose_name="Günün sözü")
    quoteown=models.CharField(max_length=50,verbose_name="sözün sahibi")


    def __str__(self):

        return self.quoteday








class Post(models.Model):
    user=models.ForeignKey('auth.User',verbose_name='yazar',on_delete=models.CASCADE,related_name='posts')
 
    genre=models.CharField(max_length=40,verbose_name="Tür")

    title=models.CharField(max_length=60,verbose_name="Başlık")
    imgfield=models.ImageField(verbose_name=" Ana Resim alanı",blank=True)
    text1=RichTextField(verbose_name="ana metin",blank=True)
    step1=models.CharField(max_length=120,verbose_name="adım 1",blank=True)
    imgfield1=models.ImageField(verbose_name="Resim alanı1",blank=True)
    text2=RichTextField(verbose_name="metin 1",blank=True)
    step2=models.CharField(max_length=120,verbose_name="adım 2",blank=True)
    imgfield2=models.ImageField(verbose_name="Resim alanı 2",blank=True)
    text3=RichTextField(verbose_name="metin 3",blank=True)
    step3=models.CharField(max_length=120,verbose_name="adım 3",blank=True)
    imgfield3=models.ImageField(verbose_name="Resim alanı 3",blank=True)
    text4=RichTextField(verbose_name="metin 4")

    step4=models.CharField(max_length=120,verbose_name="adım 4",blank=True)
    imgfield4=models.ImageField(verbose_name="Resim alanı 4",blank=True)
    text5=RichTextField(verbose_name="metin 5",blank=True)
    step5=models.CharField(max_length=120,verbose_name="adım 5",blank=True)
    imgfield5=models.ImageField(verbose_name="Resim alanı 5",blank=True)
    text6=RichTextField(verbose_name="metin 6",blank=True)
    publishing_date=models.DateTimeField(verbose_name="Tarih",auto_now_add=True)
    slug=models.SlugField(unique=True)





    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return "/post/{}".format(self.slug)

    class Meta:
        ordering=["-publishing_date","id"]    

   
            
    


