from django.shortcuts import render, redirect
from .models import Message, Comment
from login_reg.models import User

def project_index(request):
    user_id = request.session['id']
    this_user = request.session['first_name']
    context = {
        'messages': Message.objects.all().order_by('-created_at'),
        'users': User.objects.all(),
        'comments': Comment.objects.all(),
        'user': User.objects.get(id= request.session['id']),

    }
    return render(request, 'project_index.html', context)
# Create your views here.
def add_message(request):
    this_message = Message.objects.create(
        message = request.POST['message'],
        user = User.objects.get(id = request.session['id'])
    )
    request.session['user_message'] = this_message.id
    return redirect('/wall')

def add_comment(request, message_id):
    this_comment = Comment.objects.create(
        comment = request.POST['comment'],
        message = Message.objects.get(id = message_id),
        user = User.objects.get(id=request.session['id'])
        )
    request.session['user_comment'] = this_comment.id
    print(this_comment.comment)
    return redirect('/wall')



def open_profile(request):
    user = User.objects.get(id= request.session['id'])
    messages = user.messages.all()
    print(messages)
    context = {
        'user': User.objects.get(id= request.session['id']),
        'message': Message.objects.get(id = request.session['user_message']),
    }
    all_messages = Message.objects.all()
    all_messages.order_by('added')
    return render(request, 'profile.html', context)

def delete_post(request, id):
        post =  Message.objects.get(id=id)
        post.delete()
        return redirect('/wall')

    

