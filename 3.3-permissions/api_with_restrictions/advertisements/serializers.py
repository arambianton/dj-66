from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        print('Validated_data: {}'.format(validated_data))
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        request = self.context.get('request')

        if request.method in ["POST", "PATCH", "DELETE"]:
            user = self.context["request"].user

            if request.method in ["POST"]:
                data['status'] = AdvertisementStatusChoices.OPEN

            if data['status'] == AdvertisementStatusChoices.OPEN:
                open_ads_count = Advertisement.objects.filter(creator=user, status='OPEN').count() + 1
                if open_ads_count > 10:
                    raise serializers.ValidationError('You can`t have more than 10 opened advertisements at the same time')
                
        return data
