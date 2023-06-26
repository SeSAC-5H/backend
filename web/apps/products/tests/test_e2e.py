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

    def test_failure_create_WithWrongBrand(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=404,
            authUser=self.user,
            prod_name="대나무칫솔",
            prod_link="http://",
            prod_discount=9000,
            prod_thumbnail="http://",
            brand_name="아낌없이주는나무2",
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
            expectedStatusCode=400,
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
            expectedStatusCode=400,
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
            expectedStatusCode=400,
            authUser=self.user,
            prod_name="대나무칫솔",
            prod_link="http://",
            prod_discount=9000,
            prod_thumbnail="http://",
        )

class BrandCreateAPIViewTest(E2EBaseTestCase):
    url = reverse_lazy('brands:create')

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = cls.createUser()
    
    def test_success_create(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=201,
            authUser=self.user,
            brand_name="최고의브랜드",
        )

    def test_failure_create_WithoutAuthUser(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=401,
            brand_name="최고의브랜드",
        )

    def test_failure_create_WithoutBrandName(self):
        res = self.generic_test(
            url=self.url,
            method="post",
            expectedStatusCode=400,
            authUser=self.user,
        )

class HashtagModelViewSetTest(E2EBaseTestCase):
    url = reverse_lazy('hashtags:list-create')

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = cls.createUser()

        cls.hashQ1 = Hashtag.objects.create(
            hash_name='칫솔',
            hash_avg_price=3000,
            room_type='RT11'
        )
        cls.hashQ2 = Hashtag.objects.create(
            hash_name='치약',
            hash_avg_price=2000,
            room_type='RT12'
        )

    def test_success_list_FindStartswith(self):
        endPoint = self.url + '?room_type=RT1'
        res = self.generic_test(
            url=endPoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data), 2)

    def test_success_list_FindExactOne(self):
        endPoint = self.url + f'?room_type={self.hashQ1.room_type}'
        res = self.generic_test(
            url=endPoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['hash_name'], self.hashQ1.hash_name)

    def test_failure_list_WithoutQueryParam(self):
        endPoint = self.url
        res = self.generic_test(
            url=endPoint,
            method="get",
            expectedStatusCode=200,
        )
        self.assertEqual(len(res.data), 0)

    def test_success_create(self):
        endPoint = self.url
        res = self.generic_test(
            url=endPoint,
            method="post",
            expectedStatusCode=201,
            authUser=self.user,
            hash_name="칫솔케이스",
            room_type='RT13'
        )

    def test_failure_create_WithoutAuthUser(self):
        endPoint = self.url
        res = self.generic_test(
            url=endPoint,
            method="post",
            expectedStatusCode=401,
            hash_name="칫솔케이스",
            room_type='RT13'
        )

    def test_failure_create_WithoutHashName(self):
        endPoint = self.url
        res = self.generic_test(
            url=endPoint,
            method="post",
            expectedStatusCode=400,
            authUser=self.user,
            room_type='RT13'
        )

    def test_failure_create_WithoutRoomType(self):
        endPoint = self.url
        res = self.generic_test(
            url=endPoint,
            method="post",
            expectedStatusCode=400,
            authUser=self.user,
            hash_name="칫솔케이스",
        )

    def test_failure_create_NotUniqueHashName(self):
        endPoint = self.url
        res = self.generic_test(
            url=endPoint,
            method="post",
            expectedStatusCode=201,
            authUser=self.user,
            hash_name="칫솔케이스",
            room_type='RT13'
        )
        res = self.generic_test(
            url=endPoint,
            method="post",
            expectedStatusCode=400,
            authUser=self.user,
            hash_name="칫솔케이스",
            room_type='RT14'
        )