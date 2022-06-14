from django.db.models import *
from django.urls import reverse
class blog_Post(Model):
# ----------------------------------------------------------
    title = CharField(max_length = 100)
# ----------------------------------------------------------
    author = ForeignKey(
    'auth.User',
    on_delete = CASCADE,
    )
# ----------------------------------------------------------
    body = TextField()
# ----------------------------------------------------------
    #SHIRT_SIZES = (('S', 'Small'),('M', 'Medium'),('L', 'Large'),)
    #shirt_size = CharField(max_length=1, choices=SHIRT_SIZES)
# ----------------------------------------------------------
    #MedalType = TextChoices('MedalType', 'GOLD SILVER BRONZE')
    #medal = CharField(blank=True, choices=MedalType.choices, max_length=10)\
# ----------------------------------------------------------

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args = [str(self.id)])