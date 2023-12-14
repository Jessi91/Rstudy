
from django.urls import path

from .views import sendData

# from .views import ContentCreateView, ContentUpdateView, LabelCreateView, LabelListView, LabelUpdateView, MonTokenObtainPairView, NoteListCreateView, NoteRetrieveUpdateView, SettingAddCollaborator, SettingLabelCreate, SettingUpdateView

urlpatterns = [

    path("notes/", sendData)
    #path('api/notes/', NoteListCreateView.as_view(), name='note-list-create'),

    # path('ma_vue_protégée/', NoteListCreateView.as_view(), name='NoteListCreateView'),
    # path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    # path('api/token/', MonTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # Ajoutez d'autres URL au besoin

   
    # path('notes/<int:pk>/', NoteRetrieveUpdateView.as_view(), name='note-retrieve-update'),

    # path('notes/<int:pk>/contents/', ContentCreateView.as_view(), name="content-create"),
    # path('notes/<int:pk>/contents/<int:content_pk>/', ContentUpdateView.as_view(), name="content-update"),

    # path('notes/<int:pk>/setting/', SettingUpdateView.as_view(), name='setting-update'),
    # path('notes/<int:pk>/setting/collaborator/', SettingAddCollaborator.as_view(), name='setting-add-collaborator'),

    # path('labels/', LabelListView.as_view(), name='label-list'),
    # path('notes/<int:pk>/labels/', LabelCreateView.as_view(), name='label-create'),
    # path('notes/<int:pk>/labels/<int:label_pk>/', LabelUpdateView.as_view(), name='label-update'),

    # path('notes/<int:pk>/labels/<int:label_pk>/add/', SettingLabelCreate.as_view(), name='setting-add-label'),
]

