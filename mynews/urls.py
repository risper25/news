from django.urls import path,include
from . import views
from .views import *


urlpatterns=[
	path('', News_view.as_view(),name="news"),
	path('search/', Search_view.as_view(),name="searched"),
	path('category/<str:category_id>', Category_view.as_view(),name="category")
]