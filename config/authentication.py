from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

class CookieTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 1. Try the Authorization header
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Token '):
            token_key = auth_header.split(' ')[1]
        else:
            # 2. Fallback to the Authorization cookie
            token_cookie = request.COOKIES.get('Authorization')
            if token_cookie and token_cookie.startswith('Token '):
                token_key = token_cookie.split(' ')[1]
            else:
                return None  # No token found
        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return (token.user, token)
