import graphene

import products.schema


class Query(products.schema.Query, graphene.ObjectType):
    # Esta clase heredara de multiples consultas
    # segun vayamos agregando aplicaciones a nuestro proyecto
    pass

schema = graphene.Schema(query=Query)