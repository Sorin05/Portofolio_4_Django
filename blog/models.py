from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Added"))


class Routine(models.Model):
    """Workout Routine Model"""
    routine_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="routines"
        )
    added_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    exercise = models.TextField()
    method = models.TextField()
    exercise_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User,
        related_name="routine_likes",
        blank=True
    )

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.routine_name

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.routine_name)
        super(Routine, self).save(*args, **kwargs)



class Comment(models.Model):
    """Comments Model"""
    routine = models.ForeignKey(
        Routine,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    likes = models.ManyToManyField(
        User,
        related_name="comment_likes",
        blank=True
    )
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['added_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_likes(self):
        return self.likes.count()