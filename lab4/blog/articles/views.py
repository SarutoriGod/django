from django.shortcuts import render, Http404
from blog.articles.models import Article


def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, id):
	try:
		post = Article.objects.filter(id=id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404
