from django.shortcuts import HttpResponse,render, render_to_response
import requests
import json

from requests.api import post, request

API_URL = 'https://api.github.com/search/users?q={}'


def query_api(search):
    
	try:
	    data = requests.get('https://api.github.com/search/users?q={}'.format(search)).json()
	except Exception as exc:
		data = None
	return data


def index(request):
    data = []
    title = 'Github Profile Searcher'
    if request.method == "POST":
        search = request.POST.get('username')
        result = query_api(search)
        if result:
            data.append(result)
        data = result
        return render(request,'result.html',{'data':data }) # data = result)
    return render(request,'index.html',{'title':title})
