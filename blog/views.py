from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #投稿を表示（published_dateの昇順）
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #'posts'⇒名前(テンプレートで使う方)、posts ⇒クエリセット
    return render(request, 'blog/post_list.html', {'posts': posts})
 