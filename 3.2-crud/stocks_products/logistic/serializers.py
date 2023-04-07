from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = '__all__'
        


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(
        many=True)
    

    class Meta:
        model = Stock
        fields = ['address', 'positions']
    
    # positions = ProductPositionSerializer(many=True)
    # настройте сериализатор для склада 
    def create(self, validated_data):
        stock = super().create(validated_data)
        positions = validated_data.pop('positions')
        for position in positions:
            StockProduct.objects.get_or_create(stock=stock, **position)
        return stock
            
#    def update(self, instance, validated_data):
