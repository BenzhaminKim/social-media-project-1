from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView, PostUpdateView,PostDeleteView

urlpatterns = [
    path('', views.home, name='webapp-home'),
    path('note',PostListView.as_view(), name='note-list'),
    path('about',views.about, name='webapp-about'),
    path('note/<int:pk>/', PostDetailView.as_view(), name='note-detail' ),
    path('note/new/', views.PostCreate, name="note-create" ),
    path('note/<int:pk>/update/', PostUpdateView.as_view(), name='note-update' ),
    path('note/<int:pk>/delete/', PostDeleteView.as_view(), name='note-delete' ),
]
