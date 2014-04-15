from django.conf.urls import url
from apployment_site import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^login/', 'django.contrib.auth.views.login'),
	url(r'^signin/', views.signin, name="signin"),
	url(r'^signup/', views.signup, name="signup")
]