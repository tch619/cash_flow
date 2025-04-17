from api.views.views_cash_flow import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(r'cash-flow', CashFlowViewSet, basename='cash_flow')
router.register(r'status', StatusViewSet, basename='status')
router.register(r'type', TypeViewSet, basename='type')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'subcategory', SubCategoryViewSet, basename='subcategory')