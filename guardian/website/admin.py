from django.contrib import admin

# Register your models here.
from .models import produtos
from .models import Movimentacoes

admin.site.register(produtos)
admin.site.register(Movimentacoes)