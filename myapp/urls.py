from django.urls import  path

from myapp import views

app_name='myapp'


urlpatterns=[
    path('cafe',views.index2, name='index2'),
    path('<int:build_id>/',views.detail2, name='detail2'),
    path('',views.home,name='home'),
    path('<int:build_id>/vote/', views.vote, name='vote'),
    path('<int:build_id>/vote2/', views.vote2, name='vote2'),
    path('<int:build_id>/vote3/', views.vote3, name='vote3'),

]