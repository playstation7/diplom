from django.forms import ModelForm, TextInput, Textarea
from diploms.models import Message, Comment, Interview  # Vacansia


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'text','file']
        labels = {'title': 'Заголовок', 'text': 'Текст', 'file': 'Загрузите файл при необходимости'}
        widgets = {
            'text': Textarea(attrs={

                'placeholder': 'Введите ваше сообщение...'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text']
        labels = {
            'title': 'Заголовок',
            'text': 'Текст сообщения'
        }

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Введите название темы...',
                'autocomplete': "off",
            }
            ),
            'text': Textarea(attrs={
                'rows': 5,
            }),
        }


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = ['first_name', 'middle_name', 'last_name', 'telephone', 'date', 'time']


"""
class VacansiaForm(ModelForm):
    class Meta:
        model = Vacansia
        fields = ['name', 'description', 'salary', 'address', 'is_active']
        labels = {
            'name': 'Название должности',
            'description':'Описание',
            'salary':'Ставка',
            'address':"Адрес",

        }
"""
