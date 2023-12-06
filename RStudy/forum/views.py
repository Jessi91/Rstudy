from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum
from .forms import ForumForm

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