from django.urls import path
from reviews import views

urlpatterns = [
    path('api/v1/reviews', views.ReviewList.as_view(), name='review_list'),
    path('api/v1/movie', views.MovieApi.as_view(), name='movie_api'),# 영화api 임시
    path('api/v1/reviews/recent', views.ReviewListRecent.as_view(), name='review_recent'),
    path('api/v1/reviews/<int:pk>', views.ReviewListDetail.as_view(), name='review_detail'),
]