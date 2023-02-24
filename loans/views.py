from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Loans
from .permissions import IsOwnerOrReadOnly
from .serializers import LoansSerializer
from .machine_model import pred_model


class LoansList(ListCreateAPIView):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer


class LoansDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer


@csrf_exempt
def approval(request):
    print('start', request)
    if request.method == 'POST':
        data = request.POST
        # print('*start', data['salary'])
        loan_amount = 200_000
        salary = 100_000
        prediction = pred_model(loan_amount, salary)
        return JsonResponse({'status': 'success', 'prediction': prediction})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
