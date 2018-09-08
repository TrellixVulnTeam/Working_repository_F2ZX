# File: ./backend/backend/schema.py

import graphene

import simple_app.schema

class Mutations(
    simple_app.schema.Mutation,
    graphene.ObjectType,
):
    pass


class Queries(
    simple_app.schema.Query,
    graphene.ObjectType
):
    dummy = graphene.String()


schema = graphene.Schema(query=Queries)
schema = graphene.Schema(query=Queries, mutation=Mutations)