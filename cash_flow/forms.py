from django import forms
from .models import EntryCashFlow, Category, SubCategory


class EntryCashFlowAdminForm(forms.ModelForm):
    class Meta:
        model = EntryCashFlow
        fields = ['status', 'type', 'category', 'subcategory', 'sum', 'comment']

    def clean(self):
        cleaned_data = super().clean()
        type_obj = cleaned_data.get('type')
        category_obj = cleaned_data.get('category')
        subcategory_obj = cleaned_data.get('subcategory')

        if category_obj and category_obj.type != type_obj:
            self.add_error('category', 'Категория должна относиться к выбранному типу.')

        if subcategory_obj and subcategory_obj.category != category_obj:
            self.add_error('subcategory', 'Подкатегория должна относиться к выбранной категории.')

        return cleaned_data
