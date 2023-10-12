from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
# Create your views here.

class PostList(generic.ListView): 
    model = Post
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6 #max of 6 posts can be displayed , if more than Django adds navigation bar 

class PostDetail(View):

    def get(self,request, slug,*args, **kwargs):  #Identical to if ==POST: , just because this is a class we can define class based functions which will trigger
        queryset = Post.objects.filter(status = 1) # filter all posted posts (=1) , and assign 
        post = get_object_or_404(queryset, slug=slug) #Get the relevant object by its slug 
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked =False 
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                "post": post, 
                "comments": comments, 
                "liked": liked
            }
        )