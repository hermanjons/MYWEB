from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect

from post.models import Post

from django.contrib import messages
from post.forms import Postform
from django.utils.text import slugify

from django.core.paginator import Paginator

from django.db.models import Q


#posts=Post.objects.all()

def post_index_computer(request):
    post_list_computer=Post.objects.all()
    post_list_computer=post_list_computer.filter(genre__icontains="BİLGİSAYAR")


    paginator = Paginator(post_list_computer, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts1 = paginator.get_page(page_number)


    return render(request,"post/indexcomputer.html",{"postcomp":posts1})







def post_index_phone(request):
    post_list_phone=Post.objects.all()
    post_list_phone=post_list_phone.filter(genre__icontains="TELEFON")


    paginator = Paginator(post_list_phone, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)


    return render(request,"post/indexphone.html",{"postphone":posts})



def post_index(request):

    
    
    post_list = Post.objects.all()
    
    query=request.GET.get('q')
    

    if query:

        post_list=post_list.filter(
                                  Q(title__icontains=query)or
                
                                  Q(step1__icontains=query) or
                                  Q(step1__icontains=query) or
                                  Q(step2__icontains=query) or
                                  Q(step3__icontains=query)  or
                                  Q(step4__icontains=query) or
                                  Q(step5__icontains=query)or
                                  
                                  Q(text1__icontains=query)or
                                  Q(step2__icontains=query)                    
                                    ).distinct()



    paginator = Paginator(post_list, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)


    return render(request,"post/index.html",{"posts":posts})


def post_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)


    context={

        "post":post
    }
    return render(request,"post/detail.html",context)



def post_delete(request,slug):



    post=get_object_or_404(Post,slug=slug)
    post.delete()

    
    

    return redirect("/post/index")
 


def post_create(request):
    form=Postform(request.POST or None)
         
    if form.is_valid():


        post=form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context={

        "form":form,

    }

    return render(request,"post/form.html",context)   
   



def post_update(request,slug):


    post=get_object_or_404(Post,slug=slug)

    form=Postform(request.POST or None,instance=post)

           
    if form.is_valid():





        form.save()
        return HttpResponseRedirect(post.get_absolute_url())
        return messages.SUCCESS(request,"SORUN BAŞARIYLA ÇÖZÜLDÜ")



    context={



        "form":form,

    }





    return render(request,"post/form.html",context)            