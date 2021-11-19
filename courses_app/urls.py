from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses_page),
    path('add_course',views.add_course),
    path('courses/comments/<int:course_id>',views.comments_page,),
    path('courses/comments/<int:course_id>/post_comment',views.post_comment),
    path('courses/comments/<int:course_id>/<int:comment_id>/delete_comment',views.delete_comment),
    path('courses/destroy/<int:course_id>',views.delete_page,),
    path('remove_course_from_database/<int:course_id>',views.remove_course_from_database),
]