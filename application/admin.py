from django.contrib import admin
from .models import Group
from .models import SubGroup
from .models import Account
from .models import Transaction

admin.site.register(Group)
admin.site.register(SubGroup)
admin.site.register(Account)
admin.site.register(Transaction)

#usuario = leandro
#senha = le010277