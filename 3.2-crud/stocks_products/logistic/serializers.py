from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
        


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(
        many=True)
    

    class Meta:
        model = Stock
        fields = ['address', 'positions']
    
    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.get_or_create(stock=stock, **position)

        return stock
            
    def update(self, instance, validated_data):
        positions = validated_data.pop('positions', None)

        instance.address = validated_data.get('address', instance.address)
        instance.save()
  
        if positions:
            for position in positions:
                product = position.get('product')

                stock_product_data = {
                    'stock': instance,
                    'product': product,
                    'quantity': position.get('quantity'),
                    'price': position.get('price')
                }   
                stock_product, created = StockProduct.objects.update_or_create(
                    stock=instance,
                    product=product,
                    defaults=stock_product_data
                )

                if not created:
                    stock_product.quantity = stock_product_data.get('quantity', stock_product.quantity)
                    stock_product.price = stock_product_data.get('price', stock_product.price)
                    stock_product.save()

        return instance
        