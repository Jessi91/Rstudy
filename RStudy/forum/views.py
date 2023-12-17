from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            new_forum = form.save(commit=False)
            new_forum.save()
            # Ajoutez l'utilisateur actuel comme participant au forum
            new_forum.participants.add(request.user)
            return redirect('show_forum')  # Redirige vers la page de détail du forum
    else:
        form = ForumForm()

    return render(request, 'forum/create_forum.html', {'form': form})


def show(request):  
    forums = Forum.objects.all()  
    return render(request,"forum/show.html",{'forums':forums})  

@login_required
def edit(request, id):
    forum = Forum.objects.get(id_forum=id)
    form = ForumForm(instance=forum)
    return render(request, 'forum/edit.html', {'forum': forum, 'form': form})


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
    # Récupérer les messages liés à ce forum
    messages = ParticipationForum.objects.filter(forum=forum)

    return render(request, 'forum/forum_detail.html', {'forum': forum, 'messages': messages})

def send_message(request, id):
    forum = get_object_or_404(Forum, id_forum=id)
    if request.method == 'POST':
        form = ParticipationForumForm(request.POST)
        if form.is_valid():
            participation = form.save(commit=False)
            participation.user = request.user
            participation.forum = forum
            participation.save()
            return redirect('forum_detail', id=id)
    else:
        form = ParticipationForumForm()

    return render(request, 'forum/send_message.html', {'form': form, 'forum': forum})