from django.db.models import *
from django.urls import reverse
from django.contrib.auth import get_user_model

class blog(Model):

    title = CharField(max_length = 100)
# - - - - - -  - - -   -  - -   -  --  ----
    author = ForeignKey(
        get_user_model(),
        null=True,on_delete = CASCADE,)

# - - - - - -  - - -   -  - -   -  --  ----
    body = TextField()
# - - - - - -  - - -   -  - -   -  --  ----
# - - - - - -  - - -   -  - -   -  --  ----
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
        
class Comment(Model):
    article = ForeignKey(
    blog,
    on_delete=CASCADE,
    related_name='comments', # new
    )
    comment = CharField(max_length=200)
    author = ForeignKey(
    get_user_model(),
    on_delete=CASCADE,
    )
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')