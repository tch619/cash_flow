from rest_framework import viewsets
from cash_flow import models, serializers


class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = models.EntryCashFlow.objects.all()
    serializer_class = serializers.EntryCashFlowSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        type_id = self.kwargs.get('type_id')
        return models.Category.objects.filter(type_id=type_id)


class SubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return models.SubCategory.objects.filter(category_id=category_id)
