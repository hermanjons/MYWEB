


from django.db import models



from django.utils.text import slugify


from ckeditor.fields import RichTextField




class News(models.Model):
    genre=models.CharField(max_length=40,verbose_name="Tür")
    Başlık=models.CharField(max_length=50,verbose_name="başlık")
    resim=models.ImageField(verbose_name="ana resim")
    resim2=models.ImageField(verbose_name="detay resim",blank=True)
    metin=RichTextField(verbose_name="metin alanı")
    slug=models.SlugField(verbose_name="slug")
    tarih=models.DateTimeField(auto_now_add=True,verbose_name="Tarih")

    
    def __str__(self):
        return self.Başlık


    def get_absolute_url(self):
        return "/teknohaber/{}".format(self.slug)

