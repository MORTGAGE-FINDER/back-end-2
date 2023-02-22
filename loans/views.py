from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Loans
from .permissions import IsOwnerOrReadOnly
from .serializers import LoansSerializer


class LoansList(ListCreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer


class LoansDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer
