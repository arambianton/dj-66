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
        read_only_fields = ('stock',)


class StockSerializer(serializers.ModelSerializer):

    positions = ProductPositionSerializer(
        many=True)
    

    class Meta:
        model = Stock
        fields = ['address', 'positions']
        read_only_fields = ('stock',)
    
    # positions = ProductPositionSerializer(many=True)
    # настройте сериализатор для склада 
    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, **position)
        return stock
            
    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        # positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        # stock = super().update(instance, validated_data)
        stock = super().update(instance, validated_data)
        # for position in positions:
        #     StockProduct.objects.update_or_create(stock=stock, **position)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
