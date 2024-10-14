from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserregistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')



def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request ,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    
    if request.method == "POST":
        form = TweetForm(request.POST , request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
            
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html',{'form': form})


@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id,  user = request.user) 
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance = tweet)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list') 
    else:
        form = TweetForm(instance = tweet)
    return render(request, 'tweet_form.html', {'form':form})


@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})
    
    
    
def register(request):
    if request.method == 'POST':
        form = UserregistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('tweet_list')   
    else:
        form = UserregistrationForm()
    return render(request,'registration/register.html',{'form':form})
 
 
def profile_view(request):
    return render(request, 'registration/profile.html')
  
  
 
def test_form(request):
    if request.method=='POST':
        print('hiiiii')
        print('➡ pythonwebsite/tweet/views.py:82 request type:', request.POST)
        name =  request.POST['name'] #request.POST.get('name)
        print('➡ pythonwebsite/tweet/views.py:86 name type:', name)
        address =  request.POST['address']
        print('➡ pythonwebsite/tweet/views.py:88 address type:', address)
        return HttpResponse('hii')
    return render(request, 'registration/test_from.html')
