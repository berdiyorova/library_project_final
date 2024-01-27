from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'content', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # check title if it contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError({
                'status': False,
                'message': 'Sarlavha harflardan iborat bo\'lishi kerak'
            })
        # check title and author from database existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                'status': False,
                'message': 'Bu kitob bazada mavjud!'
            })

        return data


    def validate_price(self, data):
        if data < 100 or data > 1000000000:
            raise ValidationError({
                'status': False,
                'message': 'Narx noto\'g\'ri kiritilgan!'
            })
