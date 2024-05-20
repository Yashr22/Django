from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('service/', views.servicepage, name='service'),
    path('contact/', views.contactpage, name='contact'),
    path('account/', views.accountpage, name='account'),
    # URLs for notes
    path('note/', views.note_list, name='note_list'),
    path('note/create/', views.create_note, name='create_note'),
    path('note/delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('note/update/<int:note_id>/', views.update_note, name='update_note'),
    # URLs for notes
    path('chatbot/', views.chatbot, name='chatbot'),
]