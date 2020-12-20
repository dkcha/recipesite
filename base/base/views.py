from django.shortcuts import render

def index(request):
    #posts = Post.objects.all().order_by('-created_on')
    #context = {
    #    "posts": posts,
    #}
    return render(request, "index.html") #, context)
