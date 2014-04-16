from django.conf.urls import url
from apployment_site import views
from django.contrib.auth import logout

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^login/', views.signin, name="signin"),
	url(r'^signup/', views.signup, name="signup"),
	url(r'^logout/', 'django.contrib.auth.views.logout', {"next_page" : "/"})
]