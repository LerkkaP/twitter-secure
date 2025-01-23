from twitter.models import Post, Comment
from django.contrib import messages
from django.utils import timezone

def add_post(request, text):
    if request.method == "POST":
        text = request.POST.get("text")
        user_instance = request.user
        if len(text) == 0:
            print("Post cannot be empty")
            return None
        if len(text) > 280:
            print("Max post length is 280 characters")
            return None
        else:
            created_at = timezone.now().strftime("%Y-%m-%d")
            Post.objects.create(text=text, user=user_instance, created_at=created_at)
            print("Post added successfully!")

def add_comment(request, comment_text, post_id):
    if len(comment_text) == 0:
        messages.error(request, "Comment can't be empty")
        print("Comment cannot be empty")
        return False
    created_at = timezone.now().strftime("%Y-%m-%d") 
    user_instance = request.user 
    print(user_instance)
    post_instance = Post.objects.get(id=post_id)

    comment = Comment.objects.create(comment_text=comment_text, user=user_instance, post=post_instance, created_at=created_at)
    comment.save()
    return True

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post_owner = post.user.id
    user_id = request.user.id
    if user_id == post_owner:
        post.delete()
  

