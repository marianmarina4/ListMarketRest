from users.authentication import ExpiringTokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status, authentication, exceptions

class Authentication(authentication.BaseAuthentication):
    user = None
    user_token_expired = False
    
    def get_user(self, request):
        """
        Return:
            * user : User instance
            * message : Error Message
            * None : Corrupt Token
        """
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            
            token_expire = ExpiringTokenAuthentication()
            user, token, message, self.user_token_expired = token_expire.authenticate_credentials(token)
            
            if user != None and token != None:
                self.user = user
                return user
            return message
        return None
    
    
    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('Credenciales incorrectas')
        
        return (self.user, None)