from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации

    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]

    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    serializer_class = StockSerializer

    # при необходимости добавьте параметры фильтрации
    def get_queryset(self):
        queryset = Stock.objects.all()
        product_name = self.request.query_params.get("products")
        if product_name is not None:
            queryset = queryset.filter(products__title__icontains=product_name)
        return queryset

    pagination_class = LimitOffsetPagination
