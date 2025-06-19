from django.db import models
from django.contrib.auth.models import AbstractUser,  \
                                       BaseUserManager

from django.core.validators   import RegexValidator
from django.utils.translation import gettext_lazy as _


class AnalystManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, registration, password, **extra_fields):
        if not registration:
            raise ValueError(_('The registration field is required.'))

        extra_fields.setdefault('username', registration)

        user = self.model(registration=registration, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, registration, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(registration, password, **extra_fields)

    def create_superuser(self, registration, password, **extra_fields):
        extra_fields.setdefault('is_staff'    , True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields['is_staff']:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if not extra_fields['is_superuser']:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(registration, password, **extra_fields)


class Analyst(AbstractUser):
    RANK_CHOICES = [
        ("SD"   , "Soldado"        ),
        ("CB"   , "Cabo"           ),
        ("3 SGT", "3º Sargento"    ),
        ("2 SGT", "2º Sargento"    ),
        ("1 SGT", "1º Sargento"    ),
        ("ST"   , "Subtenente"     ),
        ("2 TEN", "2º Tenente"     ),
        ("1 TEN", "1º Tenente"     ),
        ("CAP"  , "Capitão"        ),
        ("MAJ"  , "Major"          ),
        ("TC"   , "Tenente-Coronel"),
        ("CEL"  , "Coronel"        ),
    ]

    registration = models.CharField(
        max_length=7,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^5\d{6}$',
                message=_("Registration must have exactly 7 digits and start with the number 5."),
                code='invalid_registration'
            )
        ],
        verbose_name=_("Registration Number")
    )
    rank = models.CharField(
        max_length=6,
        choices=RANK_CHOICES,
        default="CB",
        verbose_name=_("Position in the military hierarchy")
    )
    service_name = models.CharField(
        max_length=30,
        verbose_name=_("Name used in service")
    )

    USERNAME_FIELD  = 'registration'
    REQUIRED_FIELDS = ['rank'        ,
                       'service_name',
                       'first_name'  ,
                       'last_name'   ,
                       'email']

    objects = AnalystManager()

    def __str__(self):
        return f'{self.rank} {self.service_name}'
