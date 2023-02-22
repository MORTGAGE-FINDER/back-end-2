from django.urls import path
from .views import LoansList, LoansDetail

urlpatterns = [
    path("", LoansList.as_view(), name="loans_list"),
    path("<int:pk>/", LoansDetail.as_view(), name="loans_detail"),
]
