from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('creation_date', 'last_modified_date',)

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
