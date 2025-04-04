from django.shortcuts import render, redirect,  get_object_or_404
from cafeMain.models import Post, Comment
from cafeMain.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

def toL(request):
    return render(request, "ToL.html")

def toL_list(request):
    letters = Post.objects.all().order_by('-created_at')
    my_paginator = Paginator(letters, 5)
    page_num = request.GET.get('page')
    letters = my_paginator.get_page(page_num)
    
    return render(request, "toL_list.html", {"letters" : letters})

def toL_detail(request, letter_id):
    letter = get_object_or_404(Post, pk = letter_id)
    comment_form = CommentForm()
    context = {
        'letter' : letter,
        'comment_form' : comment_form
    }
    
    return render(request, "toL_detail.html", context)

def toL_update(request, id):
    letter = get_object_or_404(Post, pk = id)

    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance = letter)
        if form.is_valid():
            form.save()
            return redirect('toL_list')
    else:
        form = PostModelForm(instance = letter)
        return render(request, 'form_create.html', {'form' : form, 'id' : id})
    
def toL_delete(request, id):
    letter = Post.objects.get(pk = id)
    letter.delete()
    return redirect('toL_list')

# 왜 댓글 생성이 안될까 ㅅ ㅂ
def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk = id)
        finished_form.save()
    return redirect('toL_detail', id)

def update_comment(request, letter_id, com_id):
    comment = Comment.objects.get(id = com_id)

    if request.method == "POST":
        updated_form = CommentForm(request.POST, instance = comment)

        if updated_form.is_valid():
            updated_form.save()
            return redirect('toL_detail', letter_id)
    else:
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'comment_update.html', context)
    
def delete_comment(request, letter_id, com_id):
    comment = Comment.objects.get(id = com_id)
    comment.delete()
    return redirect('toL_detail', letter_id)