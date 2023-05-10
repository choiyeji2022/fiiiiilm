from django.urls import path
from reviews import views

urlpatterns = [
    path('movie/', views.MovieApiMain.as_view(), name='main_api'),# 영화api 임시
    path('movie/detail/', views.MovieApiDetail.as_view(), name='detail_api'),# 영화api 임시
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/recent/',views.ReviewListRecent.as_view(), name='review_recent'),
    path('reviews/<int:pk>/',views.ReviewUpdate.as_view(), name='review_detail'),
    path('reviews/<int:pk>/comments/',views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/',views.CommentDetail.as_view(), name='comment_detail'),
]
