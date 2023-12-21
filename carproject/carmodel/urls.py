from django.urls import path

from . import views
urlpatterns = [
    path('details/<int:id>/',views.Details.as_view() , name='details'),
    path('edit_view/',views.update_view , name='edit_view'),
    
    
]

