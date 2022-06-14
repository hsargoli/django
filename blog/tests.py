from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import blog_Post
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.blog_Post = blog_Post.objects.create(
        title='A good title',
        body='Nice body content',
        author=self.user,
        )
    def test_string_representation(self):
        post = blog_Post(title='A sample title')
        self.assertEqual(str(post), post.title)
    def test_blog_Post_content(self):
        self.assertEqual(f'{self.blog_Post.title}', 'A good title')
        self.assertEqual(f'{self.blog_Post.author}', 'testuser')
        self.assertEqual(f'{self.blog_Post.body}', 'Nice body content')
    def test_blog_Post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homee.html')
    def test_blog_Post_detail_view(self):
        response = self.client.get('/blog/post/1/')
        no_response = self.client.get('/blog/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    # Create your tests here.
