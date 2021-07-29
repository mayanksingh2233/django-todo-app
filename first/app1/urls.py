from django.urls import path,include
from .views import home,about,Contact, delete_as_complete, todo,mark_as_complete
urlpatterns = [
    path("",home,name="home"),
    path("contact/",Contact,name='contact'),
    path("about/",about,name="about"),
    path("todo/",todo,name="todo"),
    path("delete_as_complete/<id>",delete_as_complete , name="delete_as_complete"),
    path("mark_as_complete/<id>",mark_as_complete , name="mark_as_complete"),
]
