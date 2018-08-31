from django.db import models
from django.urls import reverse

class Posts(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  imageUp = models.ImageField(upload_to ="", height_field=height_field, width_field = width_field)
  Updated = models.DateField(auto_now=True,auto_now_add=False)
  published = models.DateField(auto_now=False,auto_now_add=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("posts:detail" , kwargs={"id":self.id})

