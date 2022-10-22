from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import BlogPosts
# Create your tests here.


class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@sample.com',
            password='secret'
            )

        self.post = BlogPosts.objects.create(
            title='A sample title',
            content='This is a brand new post',
            author=self.user,
        )

    def test_string_representation(self) -> None:
        post = BlogPosts(title='A sample title')
        self.assertEqual(str(post.title), post.title)

    def test_get_absolute_url(self) -> None:
        self.assertEqual(self.post.get_absolute_url(), '/blog/1/')

    def test_post_content(self) -> None:
        self.assertEqual(f'{self.post.title}', 'A sample title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.content}', 'This is a brand new post')

    def test_post_list_view(self) -> None:
        response = self.client.get(reverse('blog_home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a brand new post')
        self.assertTemplateUsed(response, 'blog/blog_home.html')

    def test_post_detail_view(self) -> None:
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A sample title')
        self.assertTemplateUsed(response, 'blog/blog_post_detail.html')

    def test_post_create_view(self) -> None:
        response = self.client.post(reverse('blog_post_new'), {
            'title': 'New title',
            'content': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self) -> None:
        response = self.client.post(reverse('blog_post_edit', args='1'), {
            'title': 'Updated title',
            'content': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self) -> None:
        response = self.client.get(
            reverse('blog_post_delete', args='1'))
        self.assertEqual(response.status_code, 200)
