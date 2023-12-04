from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import path
# from plemiona.views import village_list
from . import views
app_name = "plemiona"


# urlpatterns = [
#     path('', village_list, name='village_list'),
# ]
from .views import get_user_village, register, create_village_for_user, CustomLoginView, send_message, \
    received_messages_view, sent_messages_view, message_detail, send_reply

urlpatterns = [
    path('admin/create_village/', views.admin_create_village, name='admin_create_village'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('village/', views.get_user_village, name='get_user_village'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('map', views.map_view, name='map_view'),
    path('village_detail/<int:village_id>/', views.village_detail, name='village_detail'),
    path('add_village/<str:username>/', create_village_for_user, name='create_village_for_user'),
    # path('town_hall/',views.town_hall_view, name='town_hall'),
    path('town_hall/<int:village_id>/', views.town_hall_view, name='town_hall_view'),
    path('barracks/<int:village_id>/', views.barracks_view, name='barracks_view'),
    path('upgrade_building/<int:village_id>/<str:building_type>/', views.upgrade_building, name='upgrade_building'),
    path('recruit_units/<int:village_id>/', views.recruit_units, name='recruit_units'),
    path('place/<int:village_id>/', views.place_view, name='place_view'),
    path('attack_view/<int:village_id>/', views.attack_view, name='attack_view'),
    path('send_message/', send_message, name='send_message'),
    path('messages/sent/', sent_messages_view, name='sent_messages'),
    path('messages/received/', received_messages_view, name='received_messages'),
    path('messages/<int:message_id>/', message_detail, name='message_detail'),
    path('messages/reply/<int:message_id>/', send_reply, name='send_reply'),
]
# #
# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]