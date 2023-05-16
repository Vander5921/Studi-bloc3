from django.test import TestCase
from .models import Category, Article


class CategoryModelTest(TestCase):
    def test_str_representation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')


class ArticleModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_str_representation(self):
        article = Article.objects.create(nom='Test Article', description='Test Description',
                                         categorie=self.category, prix=10.99)
        self.assertEqual(str(article), 'Test Article')
