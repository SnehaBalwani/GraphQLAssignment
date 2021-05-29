from graphene.types.tests.test_resolver import args
from graphene_django.types import DjangoObjectType
import graphene
import django_filters

from gql_queries.models import Banks, Branches


class BanksType(DjangoObjectType):
    class Meta:
        model = Banks
        fields = ["name", "id"]


class BranchesType(DjangoObjectType):
    class Meta:
        model = Branches
        fields = ["ifsc", "bank", "branch", "address", "city", "district", "state"]


class Query(graphene.ObjectType):
    banks = graphene.Field(BanksType, id=graphene.Int(), name=graphene.String())
    all_bankss = graphene.List(BanksType)
    branches = graphene.Field(BranchesType, ifsc=graphene.String(), branch=graphene.String(), city=graphene.String())
    all_branchess = graphene.List(BranchesType)
    branches_filter = graphene.List(BranchesType, city=graphene.String(), district=graphene.String(),
                                    state=graphene.String(), bank__name=graphene.String(), bank__id=graphene.Int())



    def resolve_all_bankss(self, context, **kwargs):
        return Banks.objects.all()

    def resolve_all_branchess(self, context, **kwargs):
        return Branches.objects.all()

    def resolve_banks(self, context, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Banks.objects.get(id=id)

        if name is not None:
            return Banks.objects.get(name=name)

        return None

    def resolve_branches(self, context, **kwargs):
        ifsc = kwargs.get('ifsc')
        branch = kwargs.get('branch')
        city = kwargs.get('city')

        if ifsc is not None:
            return Branches.objects.get(ifsc=ifsc)

        if branch is not None:
            return Branches.objects.get(branch=branch)
        if city is not None:
            return Branches.objects.filter(city__icontains=city)

        return None


    def resolve_branches_filter(self, context, **kwargs):
        city = kwargs.get('city')
        district = kwargs.get('district')
        state = kwargs.get('state')
        bank__name = kwargs.get('bank__name')
        bank__id = kwargs.get('bank__id')
        if city is not None:
            return Branches.objects.filter(city__icontains=city)

        if state is not None:
            return Branches.objects.filter(state__icontains=state)

        if district is not None:
            return Branches.objects.filter(district__icontains=district)

        if bank__name is not None:
            return Branches.objects.filter(bank__name__icontains=bank__name)

        if bank__id is not None:
            return  Branches.objects.filter(bank__id=bank__id)


