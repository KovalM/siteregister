from django.shortcuts import render_to_response
from django.contrib import auth

def main(request):
    return render_to_response('main.html', {'username':auth.get_user(request).username})