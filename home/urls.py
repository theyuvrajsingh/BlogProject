from django.conf import settings
from django.urls import include, path
from . import views
from .views import UpdatePostView
from django.conf.urls.static import static
# from .views import CategoryView
from .views import like_post

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),
    path("category/<slug:slug>/",views.catego, name="category"),
    path("category/<slug:slug>/", views.blogs, name="blogs"),# to see categories blogs 
    # path("category/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    # path("my_blogs/",views.itsme, name="my_blogs"),
    path('my_blogs/<str:author>/', views.myblogs, name='my_blogs'),
    
#     profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),

#    for Rich Text Editor (tinymce)
     path('tinymce/', include('tinymce.urls')),

     # Like 
     path('like/<int:pk>/', like_post, name='like_post'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#me