from django.test import TestCase
from typing import Optional

# e2e tests
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Create your tests here.
class E2EBaseTestCase(TestCase):
    def generic_test(
        self,
        url,
        method,
        expectedStatusCode,
        authUser: Optional[User] = None,
        **data,
    ):
        request = getattr(self.client, method)

        header = self.getAuthHeaderByToken(self.getToken(authUser))
        response = request(
            url,
            data=data,
            format="json",
            content_type="application/json",
            **header
        )
        self.assertEqual(expectedStatusCode, response.status_code)
        return response
    

    @classmethod
    def createUser(cls, **kwargs):
        userKwargs = {"username": "yamkim", "password": "5933"}
        userKwargs.update(kwargs)
        return User.objects.createUser(**userKwargs)

    def getToken(self, user):
        if not user:
            return None
        serializer = TokenObtainPairSerializer(
            data={
                "username": "yamkim",
                "password": "5933",
            }
        )
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data
    
    def getAuthHeaderByToken(self, token):
        if not token:
            return {}
        return {"HTTP_AUTHORIZATION": f'Bearer {token["access"]}'}