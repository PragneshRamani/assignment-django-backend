from django.urls import path

from transaction.views import GetTransactions, AddTransactions, \
    UpdateTransactionStatus, GetUsers

urlpatterns = [
    path('get_users/', GetUsers.as_view(), name="get_users"),
    path('get_transactions/', GetTransactions.as_view(), name="get_transactions"),
    path('add_transactions/', AddTransactions.as_view(), name="add_transactions"),
    path('mark_paid/<uuid:id>/', UpdateTransactionStatus.as_view(), name="update_transactions_status"),
]
