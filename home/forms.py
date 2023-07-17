# from django import forms
# from .models import Profile, BlogPost, category

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )
     
        
# class BlogPostForm(forms.ModelForm):
#     # cat1 = forms.ModelChoiceField(queryset=category.objects.all(), empty_label="Select a category")
#     class Meta:
#         model = BlogPost
#         fields = ('title', 'slug','content', 'image','cat')
#         widgets = {
#             'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
#             'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
#             'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
#             'cat': forms.ModelChoiceField(queryset=category.objects.all(), empty_label="Select a category"),
#         }

from django import forms
from .models import Profile, BlogPost, category

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', )

class BlogPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=category.objects.all(), empty_label="Select a category")
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image', 'cat')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }
