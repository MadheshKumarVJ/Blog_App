from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(ListView):
    queryset = Post.published.all()
    paginate_by = 3
    context_object_name = "posts"
    template_name = "blog/post/list.html"


def getCommentsoFPost(post):
    return post.comments.filter(active=True)


def check_valid_comment_to_save(comment_form, post):
    new_comment = comment_form.save(commit=False)
    new_comment.post = post
    new_comment.save()
    return new_comment


def check_comment_form_validity_and_save_comment(comment_form, post):
    if comment_form.is_valid():
        new_comment = check_valid_comment_to_save(comment_form, post)
        return new_comment


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = getCommentsoFPost(post)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        new_comment = check_comment_form_validity_and_save_comment(
            comment_form, post
        )

    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


class PostShareView(SuccessMessageMixin, FormView):
    form_class = EmailPostForm
    template_name = "blog/post/share.html"
    success_url = reverse_lazy("blog:post_list")
    success_message = "mail sent"

    def dispatch(self, request, *args, **kwargs):
        self.post_object = get_object_or_404(
            Post, id=self.kwargs.get("post_id")
        )
        return super().dispatch(request, args, kwargs)

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(PostShareView, self).form_valid(form)

    def send_mail(self, valid_data):
        post_url = self.request.build_absolute_uri(
            self.post_object.get_absolute_url()
        )
        send_mail(
            message=f"Read {self.post_object.title} at { post_url }\n\n"
            f"{valid_data['from_name']}'s message: {valid_data['share_message']}",
            from_email=valid_data["from_email"],
            subject=f"{valid_data['from_name']} recommends you read {self.post_object.title}",
            recipient_list=[valid_data["to_email"]],
        )
