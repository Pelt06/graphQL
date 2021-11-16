import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from products.models import Category, Product


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'products']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'brand': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'initprice': ['exact', 'icontains'],
            'finalprice': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)