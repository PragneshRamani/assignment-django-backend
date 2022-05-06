from django.contrib import admin
from transaction.models import UserBalance, UserTransaction

# Register your models here.
class UserBalanceAdmin(admin.ModelAdmin):
    list_per_page = 100

class UserTransactionAdmin(admin.ModelAdmin):
    list_per_page = 100

    
admin.site.register(UserBalance, UserBalanceAdmin)
admin.site.register(UserTransaction, UserTransactionAdmin)