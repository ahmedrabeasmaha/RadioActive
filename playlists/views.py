from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import Music, Profile, MusicType,Ads
from django.core import serializers
from random import choice

def home(request):
    context = {}
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        return redirect("home")
    elif request.method == 'POST' and 'logout' in request.POST:
        logout(request)
        return redirect("home")
    
    return render(request, 'index.html', context)

def play(request):
    if request.user.is_authenticated:
        type_id = []
        musicType = MusicType.objects.filter(profile=request.user.id)
        for i in musicType:
            musicTypeId = MusicType.objects.get(musicType=i).id
            music = Music.objects.filter(musicType=musicTypeId)
            for k in music:
                type_id.append(Music.objects.get(name=k).music)
        music = choice(type_id)
        music = Music.objects.get(music=music).id
        music = Music.objects.filter(id=music)
        data = serializers.serialize('json', music)
        return HttpResponse(data, content_type="application/json")

def end(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            type_id = []
            repeat = True
            musicType = MusicType.objects.filter(profile=request.user.id)
            for i in musicType:
                musicTypeId = MusicType.objects.get(musicType=i).id
                music = Music.objects.filter(musicType=musicTypeId)
                for k in music:
                    type_id.append(Music.objects.get(name=k).music)
            music = choice(type_id)
            music = Music.objects.get(music=music).id
            while repeat == True:
                rep = Music.objects.get(id=music).music
                if rep == request.GET.get('mui', None):
                    music = choice(type_id)
                    music = Music.objects.get(music=music).id
                else:
                    repeat = False
            music = Music.objects.filter(id=music)
            data = serializers.serialize('json', music)
            return HttpResponse(data, content_type="application/json")

def adnum(request):
    if request.user.is_authenticated:
        adsNumber = 0
        ads = Ads.objects.filter(profile=request.user.id)
        for i in ads:
            adsNumber += 1
        data = adsNumber
        return HttpResponse(data, content_type='application/json')

def ad(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            ads = []
            ads = Ads.objects.filter(profile=request.user.id).order_by('id')

            for i in ads:
                ads.append(i.music)
            data = ads[request.GET.get('mui', None)]
            return HttpResponse(data, content_type='application/json')