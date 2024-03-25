from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
''' The first method uses set and get parameters and 30 seconds as time'''

def home(request):
	mv = cache.get('movie', 'has_expired')
	if mv == 'has_expired':
		cache.set('movie','The manjhi one tow', 30)
		mv = cache.get('movie')
	return render(request,'enroll/home.html',{'fm':mv})


''' The second method gets and sets both just by one line for 30 
seconds. If yes it will get the value and return it, if not, it 
will set the value as nimes@mail.com for 30 seconds and return it'''

def contact(request):
	mv = cache.get_or_set('email','nimes@gmail.com',30)
	return render(request,'enroll/home.html',{'fm':mv})

''' The third method is same as contact , difference is that 
it makes new version of the key email . The both version have same key but
different value and cache time'''

def contactversion(request):
	mv = cache.get_or_set('email','dhurba@mail.com',30,version=2)
	return render(request,'enroll/home.html',{'fm':mv})

''' Forth method sends dictionray as arguement '''
def details(request):
	data = {'name':'sonam1','roll':100 ,'housenum':100}
	cache.set_many(data,400)
	mv = cache.get_many(data)
	return render(request,'enroll/home.html',{'mv':mv})

''' It deletes the specified key and value from cache, here
we have deleted the cached key roll from fourth function' and version 
2 email from databasetable '''
def delete(request):
	cache.delete('roll')
	cache.delete('email',version = 2)
	return render(request,'enroll/home.html')

''' To increase or decrease the cache value with cached time
.To use hit url and comment the set part and again hit url. we can 
see increasing and decreasing values '''

def incrdecr(request):
	cache.set('roll',100,600)
	cache.set('housenum',100,600)
	ru = cache.get('roll')
	hu = cache.get('housenum')
	rv = cache.decr('roll', delta = 2)
	hv = cache.incr('housenum',delta = 1)
	return render(request,'enroll/home.html',{'ru':ru,'hu':hu,'rv':rv,'hv':hv})

''' It is used to remove all cache entries  '''
def ClearAll(request):
	cache.clear()
	return render(request,'enroll/home.html')


