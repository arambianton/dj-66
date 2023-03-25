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

    def create(self, validated_data):
        print('ProductPositionSerializer')
        stock = self.context['stock']
        stock_product = StockProduct.objects.create(
            stock=stock, **validated_data)
        return stock_product


class StockSerializer(serializers.ModelSerializer):

    positions = ProductPositionSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    # positions = ProductPositionSerializer(many=True)
    # настройте сериализатор для склада

    def create(self, validated_data):
        print(validated_data)
        positions = validated_data.pop('positions')
        new_stock = Stock(address=validated_data['address'])
        new_stock.save()

        # for position in positions:
        #     prod = Product.objects.get(id=position['product'])
        #     new_stock.products.add(prod)
        # new_id = new_stock.id

        for position in positions:
            new_stockproduct = StockProduct.objects.create(
                stock=new_stock, **position)
            new_stockproduct.save()
        return new_stock

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
