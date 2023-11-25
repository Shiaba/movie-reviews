from . import views
from django.urls import path

urlpatterns = [
    path('', views.MovieList.as_view(), name='home'),
    path('review_detail/<slug:slug>/',
         views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
    path('create_review/', views.CreateReview.as_view(), name='create_review'),
    path('update_review/', views.CreateReview.as_view(), name='update_review'),
]
