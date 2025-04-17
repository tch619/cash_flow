from django.contrib import admin
from .models import EntryCashFlow, Status, Type, Category, SubCategory
from django.forms import DateInput
from.forms import EntryCashFlowAdminForm


@admin.register(EntryCashFlow)
class EntryCashFlowAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'type', 'category', 'subcategory', 'sum', 'comment')
    search_fields = ('status', 'type', 'category', 'subcategory')
    list_filter = ('created_at', 'status', 'type', 'category', 'subcategory')
    form = EntryCashFlowAdminForm
    verbose_name_plural = "ДДТ"

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "created_at":
            kwargs['widget'] = DateInput(attrs={'type': 'date'}, format='%d.%m.%Y')
        return super().formfield_for_dbfield(db_field, **kwargs)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

