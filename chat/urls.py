from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:id>', views.index, name='index'),
    path('receive-message/<uuid:id>', views.receive_message, name='receive_message'),
    path('get-item/<uuid:id>', views.get_item, name='get_item'),
    path('create-item', views.create_item, name='create_item'),
    path('create-portrayal', views.create_portrayal, name='create_portrayal'),
    path('add-charactor', views.add_charactor, name='add_charactor'),
    path('undo/<uuid:id>', views.undo, name='undo')
]
