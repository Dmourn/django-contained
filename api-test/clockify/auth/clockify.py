from rest_framework import authentication
from rest_framework import exceptions, HTTP_HEADER_ENCODING

# WHAT GOES HERE?
from .models import ClockifyWebhook

def get_authorization_header(request):
    auth = request.META.get('HTTP_CLOCKIFY_SIGNATURE', b'')
    print(f'gah len(auth): {len(auth)}')
    if isinstance(auth, str):
        auth = auth.encode(HTTP_HEADER_ENCODING)
    print(f'gah auth: {auth}')
    return auth

#class ClockifyAuthentication(authentication.BaseAuthentication):
class ClockifyAuthentication(authentication.TokenAuthentication):

    keyword = ' '
    model = ClockifyWebhook

    """
        Simple token based authentication.
        Clients should authenticate by passing the token key in the "Authorization"
        HTTP header, prepended with the string "Token ".  For example:
            Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a

        A custom token model may be used, but must have the following properties.
        * key -- The string identifying the token
        * user -- The user to which the token belongs
    """

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token


    def authenticate(self, request):
        
        #clockify_webhook_secret = get_authorization_header(request).split()

        auth = get_authorization_header(request)
        #auth = get_authorization_header(request).split()
        print(f"len(auth): {len(auth)}")
        #clockify_webhook_secret = request.META.get('HTTP_CLOCKIFY_SIGNATURE')
        #if not auth or auth[0].lower() != self.keyword.lower().encode():
        if not auth:
            return None

        #if len(auth) == 1:
        #    msg = _('Invalid token header. No credentials provided.')
        #    msg = 'Invalid token header. No credentials provided.'
        #    raise exceptions.AuthenticationFailed(msg)
        #if len(auth) > 2:
        #    msg = _('Invalid token header. Token string should not contain spaces.')
        #    raise exceptions.AuthenticationFailed(msg)

        try:
            print(f"auth1 {auth}")
            token = auth.decode()
        #except UnicodeError:
        except:
            print("wtf")
        #    msg = _('Invalid token header. Token string should not contain invalid characters.')
        #    raise exceptions.AuthenticationFailed(msg)
        return self.authenticate_credentials(token)
    """
        if not clockify_webhook_secret:
            return None
        try:
            # WHAT GOES HERE?
            clockify_webhook = ClockifyWebhook.objects.get(webhooksecret=clockify_webhook_secret)
        except ClockifyWebhook.DoesNotExsist:
            raise exceptions.AuthenticationFailed("Neo, you are not the One.\n")
        return (user, None)
    """

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')
            return (token.user, token)

        return (token.user, token)
    
    #Never read the documentation again
    def autheticate_header(self, request):
        self.keyword

"""
from rest_framework import permissions

class CustomerAccessPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
"""
