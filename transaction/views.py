from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

import datetime

from transaction.models import UserTransaction
from transaction.serializers import UserTransactionSerializer, UserSerializer, UserTransactionGetSerializer

class GetTransactions(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        username = request.query_params.get('username')
        if username is None:
            return Response({'error': 'Please provide username'},
                            status=HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'error': 'User not exists'},
                            status=HTTP_404_NOT_FOUND)
        transactions = UserTransaction.objects.filter(transaction_from=user).order_by('-id')
        transactions_serializer = UserTransactionGetSerializer(transactions, many=True)
        return Response({'transactions': transactions_serializer.data},
                        status=HTTP_200_OK)


class AddTransactions(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        try:
            username = data['username']
            transaction_type = data['transaction_type']
            transaction_status = data['transaction_status']
            transaction_with = data['transaction_with']
            transaction_date= data['transaction_date']
            reason = data['reason']
        except Exception as e:
            return Response({
                'status': False,
                'code': HTTP_400_BAD_REQUEST,
                'message': str(e).replace("'", "")+' is required',
                'result': {}
            })
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'error': 'User not exists'},
                            status=HTTP_404_NOT_FOUND)
        user_transaction_data = {
            'transaction_from': user.id,
            'transaction_type': transaction_type,
            'transaction_status': transaction_status,
            'transaction_with': transaction_with,
            'transaction_date': datetime.datetime.strptime(transaction_date, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'reason': reason
        }
        user_transaction_serializer = UserTransactionSerializer(data=user_transaction_data)
        if user_transaction_serializer.is_valid():
            user_transaction_serializer.save()
        else:
            print("user_serializer FAILED", user_transaction_serializer.errors)
        return Response({
            'status': True,
            'code': HTTP_200_OK,
            'message': "Add Data success",
            'result': user_transaction_serializer.data
        })

class UpdateTransactionStatus(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id):
        
        user_transaction = UserTransaction.objects.filter(transaction_id=id)
        if user_transaction:
            transaction_data = {
                'transaction_status': 'Paid',
            }
            user_transaction.update(**transaction_data)
            user_transaction_update = UserTransaction.objects.filter(transaction_id=id).first()
            if user_transaction_update:
                user_transaction_update.save()
            return Response({
                'status': True,
                'code': HTTP_200_OK,
                'message': "Update Data success",
                'result': {}
            })
        return Response({'error': 'Transaction not exists'},
                            status=HTTP_404_NOT_FOUND)

class GetUsers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        print(user_serializer.data)
        return Response({
            'result': user_serializer.data,
            'message': "Users fetched successfully",
            'status': HTTP_200_OK})
        