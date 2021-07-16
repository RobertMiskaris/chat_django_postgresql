from django.urls import path
from . import views
from user.views import signin, signup, Logout


urlpatterns = [
    path('logout/', Logout.as_view(), name = 'logout'),
    path('signin/', signin, name = 'signin'),
    path('signup/', signup, name = 'signup'),
    path('', views.home, name = 'home' ),
    path('messenger/', views.messenger, name = 'messenger' ),
    path('messenger/<int:room_id>/', views.message_id, name = 'message_id')

]
