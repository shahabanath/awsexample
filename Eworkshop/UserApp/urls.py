from django.contrib import admin
from django.urls import path
from UserApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('listmechanic',views.listmechanic,name="listmechanic"),
    path('deletemechanic/<int:userid>',views.deletemechanic,name="deletemechanic"),
    path('approve/<int:userid>',views.approve,name="approve"),
    # path('deleteapprove/<int:userid>',views.deleteapprove,name="deleteapprove"),
    path('listinsurance',views.listinsurance,name="listinsurance"),
    path('updateinsurance/<int:insuranceid>',views.updateinsurance,name="updateinsurance"),
    path('deleteinsurance/<int:insuranceid>',views.deleteinsurance,name="deleteinsurance"),

]
