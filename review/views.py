from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Review
from .forms import CommentForm, ReviewForm
from django.urls import reverse_lazy
from django.utils.text import slugify


class MovieList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'review_detail.html',
            {
                'review': review,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'review_detail.html',
            {
                'review': review,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm,
            },
        )

# Create, update & delete review


def createreview(request):
    return render(request, 'create_review.html', {})


class CreateReview(CreateView):

    model = Review
    template_name = 'create_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)
        success_message = "Success! Your review is awaiting approval."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class UpdateReview(UpdateView):

    model = Review
    template_name = 'update_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        form.instance.slug = slugify(form.instance.title)
        success_message = "Success! Your review is awaiting approval."
        messages.add_message(self.request, messages.SUCCESS, success_message)
        return super().form_valid(form)


class DeleteReview(DeleteView):

    model = Review
    template_name = 'delete_review.html'
    success_url = reverse_lazy('home')


# Like

class ReviewLike(View):

    def post(self, request, slug, *args, **kwargs):
        review = get_object_or_404(Review, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))
