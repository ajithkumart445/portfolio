from django.test import TestCase
from django.urls import reverse
from .models import Projectinfo, Blogs, Certification
from datetime import date

class PortfolioTests(TestCase):
    def setUp(self):
        self.project = Projectinfo.objects.create(
            project_name="Test Project",
            project_slug="test-project",
            project_description="A test project",
            technologies_used="Python, Django",
            role="Developer",
            start_timeline=date.today()
        )
        self.blog = Blogs.objects.create(
            blog_title="Test Blog",
            blog_slug="test-blog"
        )
        self.cert = Certification.objects.create(
            name="Test Cert",
            issuer="Test Issuer",
            date_earned=date.today()
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_project_detail_view(self):
        response = self.client.get(reverse('projects', args=[self.project.project_slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blogs', args=[self.blog.blog_slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")

    def test_certificate_page_status_code(self):
        response = self.client.get(reverse('certificate'))
        self.assertEqual(response.status_code, 200)
