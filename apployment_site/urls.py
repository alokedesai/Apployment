from django.conf.urls import url
from apployment_site import views
from django.contrib.auth import logout

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^login/', views.signin, name="login"),
	url(r'^signup/', views.signup, name="signup"),
	url(r'^logout/', 'django.contrib.auth.views.logout', {"next_page" : "/"}),
	url(r'^profile/', views.profile, name="profile"),
	url(r'^search/', views.search, name="search"),
	url(r'^user/(?P<username>\w+)', views.user, name="user"),
]