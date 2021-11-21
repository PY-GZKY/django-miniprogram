from django.test import TestCase


# Create your tests here.


class Sn(TestCase):

    def test_sn(self):
        print("测试首页")
        response = self.client.get('/')  # 测试首页
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        print("测试详情页")
        response = self.client.get('/entities/1/?format=json')
        self.assertEqual(response.status_code, 200)
