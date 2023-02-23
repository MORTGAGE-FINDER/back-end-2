from django.http import JsonResponse
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


def approval(request):
    if request.method == 'POST':
        data = request.POST
        prediction = 'house'
        return JsonResponse({'status': 'success', 'prediction': prediction})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
