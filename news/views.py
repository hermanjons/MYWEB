from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect


from django.utils.text import slugify

from django.core.paginator import Paginator

from django.db.models import Q

from news.models import News

def news_comp(request):
    news=News.objects.all()
    news=news.filter(genre__icontains="BİLGİSAYAR")

    paginator=Paginator(news,10)
    page_number=request.GET.get('page')
    paginator=paginator.get_page(page_number)
    context={

        "newscomp":paginator
    }



    return render(request,"post/newscomp.html",context)

def news_phone(request):
    news=News.objects.all()
    news=news.filter(genre__icontains="TELEFON")

    paginator=Paginator(news,10)
    page_number=request.GET.get('page')
    paginator=paginator.get_page(page_number)
    context={

        "newsphone":paginator
    }



    return render(request,"post/newsphone.html",context)


    


def news_index(request):

    
    
    news = News.objects.all()
    paginator=Paginator(news,10)
    page_number = request.GET.get('page')
    paginator=paginator.get_page(page_number)
    




    return render(request,"post/newsindex.html",{"news":paginator})

def news_detail(request,slug):
    news=get_object_or_404(News,slug=slug)

    context={

        "news":news
    }
    return render(request,"post/newsdetail.html",context)

