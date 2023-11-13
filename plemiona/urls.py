from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import path
# from plemiona.views import village_list
from . import views
app_name = "plemiona"


# urlpatterns = [
#     path('', village_list, name='village_list'),
# ]
from .views import get_user_village, UserLoginView, register, create_village_for_user

urlpatterns = [
    path('admin/create_village/', views.admin_create_village, name='admin_create_village'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('village/', get_user_village, name='get_user_village'),
    path('add_village/<str:username>/', create_village_for_user, name='create_village_for_user'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
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