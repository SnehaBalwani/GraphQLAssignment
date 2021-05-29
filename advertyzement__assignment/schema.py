import graphene

import gql_queries.schema


class Query(gql_queries.schema.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass


schema = graphene.Schema(query=Query)