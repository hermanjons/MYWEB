from django.urls import path
from news.views import *




urlpatterns=[



    path("newsindex/",news_index,name="newsindex"),
    path("newsphone/",news_phone,name="newsphone"),
    path("newscomp/",news_comp,name="newscomp"),
    path("<slug>",news_detail,name="newsdetail"),

]
