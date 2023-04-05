from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from blog_app.models import Blog, Comment


class CreateViewsTest(APITestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.blog = Blog.objects.create(title='title', content='content', user=self.user)
        self.comment = Comment.objects.create(blog=self.blog, text='text', user=self.user)

    def test_registration_blog_api(self):
        url = reverse('registration')
        data = {
            'username': 'farzana',
            'password': 'django',
            'email': 'testuser@example.com',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_blog_post(self):
        url = reverse('blogs')
        data = {'title': 'New Post', 'content': 'This is a new post.'}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_update_blog_post(self):
        url = reverse('blogs_id', kwargs={'pk': self.blog.pk})
        data = {'title': 'Updated Post', 'content': 'This post has been updated.'}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_blog_post(self):
        url = reverse('blogs_id', kwargs={'pk': self.blog.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_create_blog_comment(self):
        url = reverse('comments')
        data = {'blog': self.blog.pk, 'text': 'This is a new comment.'}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_update_blog_comment(self):
        url = reverse('comments_id', kwargs={'pk': self.comment.pk})
        data = {'blog': self.blog.pk, 'text': 'This comment has been updated.'}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_blog_comment(self):
        url = reverse('comments_id', kwargs={'pk': self.comment.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_get_all_blogs(self):
        url = reverse('blogs')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_get_by_id(self):
        url = reverse('blogs_id', kwargs={'pk': self.blog.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_all_comments(self):
        url = reverse('comments')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_comment_get_by_id(self):
        url = reverse('comments_id', kwargs={'pk': self.comment.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

