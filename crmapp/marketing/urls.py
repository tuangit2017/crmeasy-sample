from django.conf.urls import url
from . import views


urlpatterns = [

	#url(r'^$', posts.views.post_list, name = 'post_list'),
	 url(r'^$', views.index, name='index'),
	 url(r'^home/$', views.home, name='home'),
	
]

