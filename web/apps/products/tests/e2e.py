from django.urls import reverse
from core.tests import E2EBaseTestCase
from products.models import Brand, Product, Hashtag, ProductHashtag

class MemberCreateAPIViewTest(E2EBaseTestCase):
    url = reverse('products:list-create')

    @classmethod
    def setUpTestData(cls) -> None:
        brandQ = Brand.objects.create(
            brand_name='아낌없이주는나무'
        )
        prodQ1 = Product.objects.create(
            prod_name='대나무칫솔',
            prod_price=2000,
            brand_seq=brandQ
        )
        prodQ2 = Product.objects.create(
            prod_name='옥수수칫솔',
            prod_price=2000,
            brand_seq=brandQ
        )
        hashQ = Hashtag.objects.create(
            hash_name='칫솔',
            hash_avg_price=3000,
            room_type='RT11'
        )
        ProductHashtag.objects.create(
            prod_seq=prodQ1,
            hash_seq=hashQ
        )
        ProductHashtag.objects.create(
            prod_seq=prodQ2,
            hash_seq=hashQ
        )
    
    def test_success_SearchingByHashSeq(self):
        testEndpoint = self.url + '?hash_seq=1'
        res = self.generic_test(
            url=testEndpoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data['data']), 2)

    def test_failure_NotFoundHashSeq(self):
        testEndpoint = self.url + '?hash_seq=2'
        self.generic_test(
            url=testEndpoint,
            method="get",
            expectedStatusCode=404,
        )

    def test_success_PageParameter(self):
        '''
        한 페이지에 한 개의 상품을 조회하도록 테스트 케이스 작성
        '''
        testEndpoint = self.url + '?hash_seq=1&page=1&page_size=1'
        res = self.generic_test(
            url=testEndpoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(res.data['page'], 1)

        testEndpoint = self.url + '?hash_seq=1&page=2&page_size=1'
        res = self.generic_test(
            url=testEndpoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data['data']), 1)
        self.assertEqual(res.data['page'], 2)