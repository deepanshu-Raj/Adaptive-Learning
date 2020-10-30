from django.shortcuts import render, HttpResponse, redirect
from discussions.models import Post, BlogComment, Reward
from django.contrib import messages
from django.contrib.auth.models import User
from discussions.templatetags import extras
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required
def discussionHome(request):
    allPosts = Post.objects.all() 
    context = {'allPosts': allPosts}
    return render(request, 'discussion_home.html', context)
@login_required
def discussionPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments= BlogComment.objects.filter(post=post,parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict' : replyDict}
    return render(request, 'discussion_detail.html', context)
@login_required
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your answer has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/discussions/{post.slug}")
@login_required
def newPost(request):
    return render(request, 'new_discussion.html')
@login_required
def createPost(request):
    if request.method == "POST":
        content = request.POST.get('content')
        title = request.POST.get('title')
        author = request.user
        slug1 = str(datetime.now().time())
        slug1 = slug1.replace(':','-')
        slug1 = slug1.replace('.','-')
        slug2 = str(datetime.now().date())
        slug = slug1 + '-' + slug2
        # timeStamp = now
        post = Post(title = title, author = author, content = content, slug = slug)
        post.save()
        messages.success(request, "Your post has been posted successfully")

    return redirect(f"/discussions")

def upVote(request):
    if request.method == 'POST':
        Sno = request.POST.get('Sno')
        slug = request.POST.get('Slug')
        comment = BlogComment.objects.get(sno=Sno)
        user = comment.user
        reward = Reward.objects.get(user = user)
        reward.coins = reward.coins + 1
        reward.save()
        return redirect(f"/discussions/{slug}")
    return redirect(f"/discussions")