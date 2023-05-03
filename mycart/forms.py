from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# PRODUCT_SIZE_CHOICES = [
#     ('S', 'Small'),
#     ('M', 'Medium'),
#     ('L', 'Large'),
#     ('XL', 'Extra Large')
# ]

class AddProductInCart(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)# позволяет пользователю выбрать количество между 1-20. Мы используем поле TypedChoiceField с coerce=int для преобразования ввода в целое число.
    # size = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #                                       choices=PRODUCT_QUANTITY_CHOICES)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)#update : позволяет указать, следует ли добавлять сумму к любому существующему значению в корзине для данного продукта (False) или если существующее значение должно быть обновлено с заданным значением (True).

