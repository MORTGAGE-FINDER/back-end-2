from django.urls import path
from .views_front import (
    LoansCreateView,
    LoansDeleteView,
    LoansDetailView,
    LoansListView,
    LoansUpdateView,
)

urlpatterns = [
    path("", LoansListView.as_view(), name="loans_list"),
    path("<int:pk>/", LoansDetailView.as_view(), name="loans_detail"),
    path("create/", LoansCreateView.as_view(), name="loans_create"),
    path("<int:pk>/update/", LoansUpdateView.as_view(), name="loans_update"),
    path("<int:pk>/delete/", LoansDeleteView.as_view(), name="loans_delete"),
]
