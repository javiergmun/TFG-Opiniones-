from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


#class HelloWorld(View):
    #def get(self, request):
        #return HttpResponse(content=b'Hello World')

class HelloWorld(View):
    def get(self, request):
        return render(request, 'index.html')