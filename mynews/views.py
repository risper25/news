from django.shortcuts import render,redirect
from django.views import View
import requests
import json

# Create your views here.
#display news
headers = {
    'Accept-Language':"en-US",
    'x-bingapis-sdk': "true",
    'x-rapidapi-key': "b90508119cmsha60ac408cd5a74ep108fc0jsnbd3897bb2130",
    'x-rapidapi-host': "bing-news-search1.p.rapidapi.com"
    }
class News_view(View):
    template_name='news.html'
    url = "https://bing-news-search1.p.rapidapi.com/news"
    querystring = {"textFormat":"Raw","safeSearch":"Off","setLang":"en","cc":"en-US"}

    def get(self,request):
        response = requests.request("GET", self.url, headers=headers, params=self.querystring).json()
        
        context={'response':response,'range': range(10)}
        return render(request,self.template_name,context)

class Search_view(View):
    template_name='searched.html'
    url = "https://bing-news-search1.p.rapidapi.com/news/search"
   

    def get(self,request):
        q=request.GET.get('search')
        querystring = {"q":q,"safeSearch":"Off","textFormat":"Raw","freshness":"Day"}
        res = requests.request("GET", self.url, headers=headers, params=querystring).json()
        context={'res':res,'range': range(10)}
        return render(request,self.template_name,context)

class Category_view(View):
    template_name='category.html'
    url = "https://bing-news-search1.p.rapidapi.com/news"
    def get(self,request,*args,**kwargs):
        category_id=self.kwargs['category_id']
        q= {"textFormat":"Raw","safeSearch":"Off","setLang":"en","cc":"en-US","category":category_id}
        print(category_id)
        response_c = requests.request("GET", self.url, headers=headers, params=q).json()
        context={'response_c':response_c}
        return render(request,self.template_name,context)

                        


