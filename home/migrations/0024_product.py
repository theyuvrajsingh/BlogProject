# Generated by Django 4.1.7 on 2023-04-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_like_delete_post_blogpost_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('electronics', 'Electronics'), ('clothing', 'Clothing'), ('books', 'Books')], max_length=50)),
                ('subcategory', models.CharField(choices=[('tv', 'TV'), ('phone', 'Phone'), ('shirt', 'Shirt'), ('pants', 'Pants'), ('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction')], max_length=50)),
            ],
        ),
    ]
