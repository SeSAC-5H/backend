from django.urls import reverse_lazy
from core.tests import E2EBaseTestCase
from products.models import Brand, Product, Hashtag, ProductHashtag


class ProductModelViewSetTest(E2EBaseTestCase):
    url = reverse_lazy('products:list-create')

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = cls.createUser()
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
    
    def test_success_list_SearchingByHashSeq(self):
        testEndpoint = self.url + '?hash_seq=1'
        res = self.generic_test(
            url=testEndpoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data['data']), 2)

    def test_failure_list_NotFoundHashSeq(self):
        testEndpoint = self.url + '?hash_seq=2'
        self.generic_test(
            url=testEndpoint,
            method="get",
            expectedStatusCode=404,
        )

    def test_success_list_PageParameter(self):
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

    def test_success_create(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=201,
            authUser=self.user,
            prod_name="대나무칫솔",
            prod_link="http://",
            prod_discount=9000,
            prod_thumbnail="http://",
            brand_name="아낌없이주는나무",
        )

    def test_failure_create_WithoutAuthUser(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=401,
            prod_name="대나무칫솔",
            prod_link="http://",
            prod_discount=9000,
            prod_thumbnail="http://",
            brand_name="아낌없이주는나무",
        )

    def test_failure_create_WithoutProdName(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=500,
            authUser=self.user,
            prod_link="http://",
            prod_discount=9000,
            prod_thumbnail="http://",
            brand_name="아낌없이주는나무",
        )

    def test_failure_create_WithoutProdLink(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=500,
            authUser=self.user,
            prod_name="대나무칫솔",
            prod_discount=9000,
            prod_thumbnail="http://",
            brand_name="아낌없이주는나무",
        )

    def test_failure_create_WithoutBrandName(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=500,
            authUser=self.user,
            prod_name="대나무칫솔",
            prod_link="http://",
            prod_discount=9000,
            prod_thumbnail="http://",
        )