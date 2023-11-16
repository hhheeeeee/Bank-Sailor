from rest_framework import serializers
from .models import DepositProduct, DepositOption, SavingProduct, SavingOption, DepositProductList, SavingProductList


class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'


class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('depositproduct',)


class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'


class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('savingproduct',)


class DepositProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductList
        fields = '__all__'


class SavingProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProductList
        fields = '__all__'