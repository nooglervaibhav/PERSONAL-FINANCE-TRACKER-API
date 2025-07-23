from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet

router = DefaultRouter()
router.register('income', IncomeViewSet)
router.register('expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
