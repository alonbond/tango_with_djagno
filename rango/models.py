from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(unique=True, max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # for test_ensure_views_are_positive
        if self.views < 0:
            self.views = 0
        # for test_slug_line_creation
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Likns to a User model instance
    user = models.OneToOneField(User)

    # This additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    