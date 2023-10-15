from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('creation_date', 'last_modified_date', 'owner',)

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        restricted_words = (
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
        )

        for restricted_word in restricted_words:
            if restricted_word in cleaned_data:
                raise forms.ValidationError('Введены запрещенные на портале слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        restricted_words = (
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
        )

        for restricted_word in restricted_words:
            if restricted_word in cleaned_data:
                raise forms.ValidationError('Введены запрещенные на портале слова')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
