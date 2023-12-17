from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from .models import Label, Note
from .serializers import LabelSerializer, NoteSerializer
# from .permissions import CustomPermission  # Importez vos permissions personnalisées si nécessaire




# @api_view(["GET"])
# def sendData(request):
#     dummy_dict = {
#         "id" : 1,
#         "name" : "jess"
#     }

#     return Response(dummy_dict)


def notes_view(request):
    return render(request, 'notes/notes.html')


class LabelCreateView(generics.CreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def perform_create(self, serializer):
        note_pk = self.kwargs.get('pk')
        # Ajoutez ici la logique pour traiter note_pk si nécessaire
        serializer.save()



class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # Pour la recherche
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('q')
        if query is not None:
            queryset = queryset.filter(title__icontains=query)
        return queryset

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer