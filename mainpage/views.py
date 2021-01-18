from django.shortcuts import render,HttpResponse

from post.models import Post

from post.models import Quote

from post.models import Infoabouttek

from post.models import Users


from django.core.paginator import Paginator













def Mainpage(request):
   

   
   post=Post.objects.all()
   user=Users.objects.all()
   quote=Quote.objects.all()
   info_tek=Infoabouttek.objects.all()
   paginator=Paginator(post,5)
   paginator=paginator.get_page(1)
  

   context={ 

   "posts":paginator,

   "soz":quote,
   "info":info_tek,
   "user":user,
   
   }
   

   return render(request,"main.html",context)
