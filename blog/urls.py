from django.urls import path
from . import views # wszystkie widoki (które utworzymy) z aplikacji blog zostaną zaimportowane

urlpatterns = [
    path('', views.post_list, name='post_list'), # przyporządkowanie widoku post_list do strony głównej
    # views.post_list zostanie dopasowany do pustego ciągu znaków '', każdy kto wejdzie na 127.0.0.1 trafi na ten widok, name=post_list to nazwa url, która będzie używana do zidentyfikowania widoku
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/image/', views.image_fullscreen, name='image_fullscreen'),
]
