from django.urls import path, include
from .views import EmployeeViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"", EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),

]