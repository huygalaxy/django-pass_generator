from django.shortcuts import render
import random

def index(request):
	return render(request,'index/index.html');



def result(request):
	characters=list('abcdefghijklmnopqrstuvwxyz');
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYZ'));
	if request.GET.get('num'):
		characters.extend(list('0123456789'));
	if request.GET.get('special'):
		characters.extend(list('~!@#$%^&*()_+=-'));

	length=int(request.GET.get('length',12));

	res='';
	for _ in range(length):
		res+=random.choice(characters);

	return render(request,'index/result.html',{'password':res});

