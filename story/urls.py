from django.urls import path
from . import views

urlpatterns=[
path('',views.test),
path('signin',views.signin),
path('login',views.login),
path('mainpg',views.mainpg),
path('fgpwd',views.fgpwd),
path('menu',views.menu),
path('reservation',views.reservation),
path('contactus',views.contactus),
path('aboutus',views.aboutus),
path('adminlog',views.adminlog),
path('log',views.log),
path('sign',views.sign),
path('reserv',views.reserv),
path('men',views.men),
path('main',views.main),
path('fp',views.fp),
path('contact',views.contact),
path('about',views.about),
path('admin',views.admin),
path('loghome',views.loghome),
path('inser',views.inser),
path('adminlogin',views.adminlogin),
path('reservv',views.reservv),
path('cont',views.cont),

path('showcust',views.showcust),
path('delc/<int:id>',views.delecust),
path('editc/<int:id>',views.editcust),
path('editc/<int:id>',views.editc),
path('edcode_c/<int:id>',views.edcode),

path('showad',views.showad),
path('dela/<int:id>',views.delead),
path('editad/<int:id>',views.editad),


path('showres',views.showres),
path('delr/<int:id>',views.deleres),
path('editres/<int:id>',views.editres),

path('showfeedback',views.showfeedback),

path('logg',views.logg),
#path('insertt',views.insertt)    
#path('signin',views.insertt),
#path('insertt',views.inserttt),
#path('inser',views.inserttt),
]