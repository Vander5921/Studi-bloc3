from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Promotion
from articles.models import Article, Category

class PromotionModelTest(TestCase):
    def test_str_representation(self):
        promotion = Promotion(pourcentage=10.5, date_debut=timezone.now(), date_fin=timezone.now() + timedelta(days=7))
        self.assertEqual(str(promotion), '10.5%')

class AddPromotionViewTest(TestCase):
    def test_add_promotion_view(self):
        category = Category.objects.create(name='Test Category')
        article = Article.objects.create(nom='Test Article', prix=3, categorie=category)
        url = reverse('add_promotion', args=[article.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'promotion/add_promotion.html')
