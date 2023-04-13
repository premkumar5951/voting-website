from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    
    def create_user(self, adhaar, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not adhaar:
            raise ValueError('adhaar must be provided')
        user = self.model(adhaar=adhaar, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, adhaar , password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super user must have is_staff true'))
        
        return self.create_user(adhaar, password, **extra_fields)