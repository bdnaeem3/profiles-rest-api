from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    '''
    Manger for UserProfile
    '''

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_stuff = True

        user.save(using._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    '''
    Database model users in the system
    '''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''
        Retrieve full name of user
        '''
        return self.name

    def get_short_name(self):
        '''
        Retrieve short name of user
        '''
        return self.name

    def __str__(self):
        return self.email