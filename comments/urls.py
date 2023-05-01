from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/video_id/<str:v_id>', views.CommentList.as_view()),
    path('comments/comment_id/<int:c_id>', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
