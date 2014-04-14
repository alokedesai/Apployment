from django.conf.urls import url
from apployment_site import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^signup/', views.signup, name="signup")
]