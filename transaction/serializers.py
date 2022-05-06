from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from transaction.models import UserTransaction

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']

class UserTransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserTransaction
        fields = '__all__'

class UserTransactionGetSerializer(serializers.ModelSerializer):
    transaction_with = UserSerializer()
    transaction_from = UserSerializer()
    
    class Meta:
        model = UserTransaction
        fields = '__all__'