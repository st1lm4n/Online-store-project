from django import forms
from django.core.validators import FileExtensionValidator

from .models import Product

FORBIDDEN_WORDS = {
    "name": {
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    },
    "description": {
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    },
}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        for word in FORBIDDEN_WORDS["name"]:
            if word in name:
                raise forms.ValidationError(
                    f"Название содержит запрещенное слово: '{word}'"
                )
        return self.cleaned_data["name"]

    def clean_description(self):
        description = self.cleaned_data["description"].lower()
        for word in FORBIDDEN_WORDS["description"]:
            if word in description:
                raise forms.ValidationError(
                    f"Описание содержит запрещенное слово: '{word}'"
                )
        return self.cleaned_data["description"]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update({"class": "form-select"})

    image = forms.ImageField(
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
        ],
        widget=forms.FileInput(attrs={"accept": "image/jpeg, image/png"}),
        required=False,
    )

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError("Максимальный размер файла - 5 МБ")
        return image
