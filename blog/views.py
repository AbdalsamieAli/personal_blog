from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q


from .models import Blog, Projects


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    ordering = ['-blog_date']
    template_name = 'blog/blog_list.html'
    paginate_by  = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query = query.strip()
            return Blog.objects.filter(Q(blog_title__icontains=query) | Q(blog_content__icontains=query))
        return super().get_queryset()
    

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog.html', {'blog': blog})


class ProjectListView(ListView):
    model = Projects
    context_object_name = 'projects'
    ordering = ['-endDate']
    template_name = 'blog/projects.html'
    paginate_by  = 5



