from django.conf import settings
from apployment_site.models import User as CustomUser

class CustomAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None