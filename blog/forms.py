from django.forms import ModelForm
from blog.models import Post,Comment


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'title', 'short_des', 'genre', 'long_des')
        labels = {
            'short_des': 'Short Description',
            'long_des': 'Long Description'
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']


