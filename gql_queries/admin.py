from django.contrib import admin

# Register your models here.
from gql_queries.models import Banks,Branches

admin.site.register(Banks)
admin.site.register(Branches)
