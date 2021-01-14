

from django.urls import path
from post.views import *


urlpatterns=[



    path("indexcomp/",post_index_computer,name="indexcomp"),

    path("indexphone/",post_index_phone,name="indexphone"),

    path("index/",post_index,name="index"),

    path("create/",post_create,name="create"),

    path("<slug>/delete/",post_delete,name="delete"),

    path("<slug>",post_detail,name="detail"),

    path("<slug>/update/",post_update,name="update"),

                                                ]