from django.urls import path
from . import views


urlpatterns = [
    path('add/',views.AddandShowView.as_view(),name = "addandshow"),
    path('update/<int:id>/',views.EditView.as_view(),name = "update"),
    path('delete/<int:id>/',views.UserDeleteView.as_view(),name = "delete")
]
