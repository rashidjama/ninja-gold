from django.shortcuts import render, redirect
import random

import datetime
now = datetime.datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M %p")

# Create your views here.
def index(request):
  if 'dateTime' not in request.session:
    request.session['dateTime'] = now.strftime("%Y-%m-%d %H:%M %p");
  if 'gold' not in request.session:
    request.session['gold'] = 0
  if 'farm_gold' not in request.session:
    request.session['farm_gold'] = 0
  if 'cave_gold' not in request.session:
    request.session['cave_gold'] = 0
  if 'house_gold' not in request.session:
    request.session['house_gold'] = 0
  if 'casino_gold' not in request.session:
    request.session['casino_gold'] = 0

  return render(request, 'index.html')

def show_gold(request):
  return render(request, 'index.html', context)

def process(request):
  if request.POST['place'] == 'farm':
    request.session['farm_gold'] += random.randint(10, 20)
  elif request.POST['place'] == 'cave':
    request.session['cave_gold'] += random.randint(5,10)
  elif request.POST['place'] == 'house':
    request.session['house_gold'] += random.randint(2,5)
  
  request.session['gold'] = request.session['farm_gold'] +  request.session['cave_gold'] +  request.session['house_gold']

  if request.POST['place'] == 'casino':
    request.session['casino_gold'] += random.randint(0, 50)
    request.session['gold'] -= request.session['casino_gold']


  return redirect('/')


def reset(request):
  request.session.flush()
  return redirect('/')