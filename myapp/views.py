from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# PRODUCT CRUD
class ProductAPI(APIView):

    def get(self, request):
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


# CREATE CART
class CreateCart(APIView):
    def post(self, request):
        cart = Cart.objects.create()

        return Response(
            {
                "message": "Cart created successfully",
                "cart_id": cart.id
            },
            status=status.HTTP_201_CREATED
        )


# ADD TO CART
class AddToCart(APIView):
    def post(self, request):
        try:
            cart = Cart.objects.get(id=request.data['cart_id'])
            product = Product.objects.get(id=request.data['product_id'])
        except (Cart.DoesNotExist, Product.DoesNotExist):
            return Response({"error": "Cart or Product not found"}, status=404)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantity += request.data.get('quantity', 1)
            item.save()

        return Response({"message": "Added to cart"}, status=201)


# VIEW CART
class ViewCart(APIView):
    def get(self, request, cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)


class RemoveFromCart(APIView):
    def delete(self, request, item_id):
        cart_id = request.data.get('cart_id') or request.query_params.get('cart_id')

        if not cart_id:
            return Response(
                {"error": "cart_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            item = CartItem.objects.filter(cart_id=cart_id, id=item_id).first()
            if item is None:
                item = CartItem.objects.filter(cart_id=cart_id, product_id=item_id).first()

            if item is None:
                raise CartItem.DoesNotExist

            if item.quantity > 1:
                item.quantity -= 1
                item.save()
                return Response(
                    {"message": "Quantity decreased"},
                    status=status.HTTP_200_OK
                )

            item.delete()

            return Response(
                {"message": "Item removed"},
                status=status.HTTP_200_OK
            )

        except CartItem.DoesNotExist:
            return Response(
                {"error": "Item not found"},
                status=status.HTTP_404_NOT_FOUND
            )


# CHECKOUT
class Checkout(APIView):
    def post(self, request):
        try:
            cart = Cart.objects.get(id=request.data['cart_id'])
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

        total = 0
        for item in cart.items.all():
            total += item.product.price * item.quantity

        order = Order.objects.create(cart=cart, total_amount=total)
        Payment.objects.create(order=order)

        return Response({
            "order_id": order.id,
            "total": total,
            "payment": "success"
        }, status=status.HTTP_200_OK)
