from django.urls import path
from . import views
urlpatterns = [
    path('', views.list,name="list"),
    path('create', views.create, name="create"),
    #path('success',views.success),
    path('delete/<int:contact_id>',views.delete),
    path('update/<int:contact_id>', views.update)
]   