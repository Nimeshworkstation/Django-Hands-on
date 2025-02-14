from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.

def post_list(request):
	all_post = Post.objects.all().order_by('id')	
	paginator = Paginator(all_post,3,orphans=1)
	page_num = request.GET.get('page')
	page_obj = paginator.get_page(page_num)
	print(page_obj)

	return render(request,'myapp/home.html',{'post':page_obj})