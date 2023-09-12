from django.urls import path
from . import views

urlpatterns=[
    path("dept/",views.deptapi),
    path("dept/<int:id>",views.deptapi),

    path("emp/",views.empapi),
    path("emp/<int:id>",views.empapi),
]