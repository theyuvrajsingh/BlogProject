from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.utils.html import format_html    #me
from tinymce.models import HTMLField  #me

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)


# Model for category..........
class category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    description=models.TextField()
    slug=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self): #for showing name of category in admin panel.
        return str(self.title)
    
    # For showing image in category panel by me 
    def image_tag(self):
        return format_html('<img src="/media/{}" style=width:40px;height:40px;border-radius:50px />'.format(self.image))
    
    CATEGORY_CHOICES = (
        ('programming Languages', 'Programming Languages'),
        ('food', 'Food'),
        ('ipl', 'IPL'),
    )
    SUBCATEGORY_CHOICES = (
        ('c lanuage', 'C LANGUAGE'),
        ('c++', 'C++'),
        ('python', 'PYTHON'),
        ('java', 'JAVA'),
        ('western food', 'WESTERN FOOD'),
        ('indian', 'INDIAN'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,null=True)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES,null=True)
    
# class post(models.Model):
#     post_id=models.AutoField(primary_key=True)
#     title=models.CharField(max_length=250)
#     # description=models.TextField()
#     content= HTMLField(null=True)
#     slug=models.CharField(max_length=100)
#     image=models.ImageField(upload_to='post/')
#     cat=models.ForeignKey(category,null=True,on_delete=models.CASCADE)
#     add_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):# For showing the name ........
        return self.title
    
    # Function to add image....
    def image_tag(self):
        return format_html('<img src="/media/{}" style=width:40px;height:40px;border-radius:50px />'.format(self.image) )
    

class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    cat=models.ForeignKey(category,null=True,on_delete=models.CASCADE)#me....
    slug=models.CharField(max_length=130)
    content=models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', through='Like')
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +  " Comment: " + self.content
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)





