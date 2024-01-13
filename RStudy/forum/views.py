from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.createur = request.user
            new_forum.save()

            return redirect('forum_detail', id=new_forum.id_forum)
    else:
        form = ForumForm()

    return render(request, 'forum/create_forum.html', {'form': form})

def show(request):  
    forums = Forum.objects.all()
    return render(request, "forum/show.html", {'forums': forums, 'user': request.user})  



@login_required
def update(request, id):
    forum = Forum.objects.get(id_forum=id)
    form = ForumForm(request.POST or None, instance=forum)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_forum')

    return render(request, 'forum/edit.html', {'form': form, 'forum': forum})


@login_required
def delete(request, id):  
    forum = Forum.objects.get(id_forum=id)  
    forum.delete()  
    return redirect("show_forum") 

def forum_detail(request, id):
    
    forum = get_object_or_404(Forum, id_forum=id)
    createur = forum.createur
    messages = ParticipationForum.objects.filter(forum=forum)
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'createur': createur, 'messages': messages})

@login_required
def send_message(request, id_forum):
    if request.method == 'POST':
        form = ParticipationForumForm(request.POST)
        if form.is_valid():
            participation = form.save(commit=False)
            participation.user = request.user
            forum = get_object_or_404(Forum, id_forum=id_forum)
            participation.forum = forum  # Assurez-vous de définir la valeur du forum
            participation.save()

        return redirect('forum_detail', id=id_forum)