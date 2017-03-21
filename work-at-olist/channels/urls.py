from django.conf.urls import url

from channels import views


urlpatterns = [
    url(r'^channels/list/', views.ChannelList.as_view()),
    url(r'^channels/categories/(?P<uuid>[^/]+)/$', views.CategoriesList.as_view()),
    url(r'^channels/category/(?P<uuid>[^/]+)/$', views.Category.as_view()),
]
