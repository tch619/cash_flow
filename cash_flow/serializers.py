from rest_framework import serializers
from .models import EntryCashFlow, Status, Type, Category, SubCategory


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = '__all__'


class EntryCashFlowSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(format="%d.%m.%Y")
    status = StatusSerializer()
    type = TypeSerializer()
    category = CategorySerializer()
    subcategory = SubCategorySerializer()

    class Meta:
        model = EntryCashFlow
        fields = '__all__'
