from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Product
from app.permissions import TokenRequiredPermission
from app.serializers import ProductSerializer


class ProductView(APIView):
    permission_classes = [TokenRequiredPermission]

    def get(self, request, format=None):
        products = Product.get_all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        products = Product.get_all()

        for product in products:
            product.delete()

        return Response(status=status.HTTP_200_OK)


class ProductsDetail(APIView):
    permission_classes = [TokenRequiredPermission]

    def get_object(self, pk):
        try:
            return Product.get_by_id(pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsOfMonth(APIView):
    permission_classes = [TokenRequiredPermission]

    def get(self, request, format=None):
        products = Product.objects.filter(is_product_of_month=True)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductsInStock(APIView):
    permission_classes = [TokenRequiredPermission]

    def get(self, request, format=None):
        products = Product.objects.filter(is_in_stock=True)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductsInPickup(APIView):
    permission_classes = [TokenRequiredPermission]

    def get(self, request, format=None):
        products = Product.objects.filter(is_pickup=True)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
