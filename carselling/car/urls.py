from django.urls import path , include
from . import views


urlpatterns = [
	path('cars_list', views.cars_list, name='cars_list'),
	path('thank_you/<int:id>', views.thank_you, name='thank_you'),
    path('', views.find_cars, name='find_cars'),
    path('buy_car/<int:id>', views.buy_car, name='buy_car'),
    path('buy_success', views.buy_success, name='buy_success'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('make_available/<int:id>', views.make_available, name='make_available'),
]
