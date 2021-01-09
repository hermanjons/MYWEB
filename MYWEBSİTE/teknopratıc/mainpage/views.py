from django.shortcuts import render,HttpResponse

from post.models import Post

from post.models import Quote

from post.models import Infoabouttek










def Mainpage(request):
   


   post=Post.objects.all()
   quote=Quote.objects.all()
   info_tek=Infoabouttek.objects.all()

   context={

   "posts":post,

   "soz":quote,
   "info":info_tek,
   }
   

   return render(request,"main.html",context)
