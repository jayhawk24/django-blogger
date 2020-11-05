from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def approve(self):
        return self.comments.filter(approvedComment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post',
        related_name='comments',
        on_delete=models.CASCADE)
    author = models.CharField(max_length=250)
    text = models.TextField()
    createDate = models.DateTimeField(default=timezone.now)
    approvedComment = models.BooleanField(default=False)

    def approve(self):
        self.approvedComment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return Comment.text
