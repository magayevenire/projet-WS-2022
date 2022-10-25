# cookieapp/authenticate.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

# from rest_framework.authentication import CSRFCheck
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import exceptions

class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason

def enforce_csrf(request):
    check = CSRFCheck()
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    print(reason)
    if reason:
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)

class CustomAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        
        if header is None:

            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:

            raw_token = self.get_raw_token(header)
        if raw_token is None:

            return None

        validated_token = self.get_validated_token(raw_token)
        enforce_csrf(request)
        return self.get_user(validated_token), validated_token