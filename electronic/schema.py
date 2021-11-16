import graphene
from graphene_django import DjangoObjectType
#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual
import sys
sys.path.append("..")
from products.models import Category, Product

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "products")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "brand","description","initprice","finalprice","category")


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_categories(root,info):
        return Category.objects.all()
    def resolve_all_products(root, info):
        # We can easily optimize query count in the resolve method
        return Product.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)