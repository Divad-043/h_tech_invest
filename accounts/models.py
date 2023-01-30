from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings


username_validator = UnicodeUsernameValidator()

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=150,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
    )
    phone = models.PositiveIntegerField(blank=False)
    country = models.CharField(max_length=50, blank=False)
    ref_code = models.UUIDField(
        unique=True, 
        default=uuid.uuid4, 
        editable=False
    )
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.DO_NOTHING, 
        related_name="mentor",
        null=True,
        blank=True
    )
    total_amount_xaf = models.PositiveIntegerField(default=0)
    total_referral_amount_xaf = models.PositiveIntegerField(default=0)
    total_amount_eth = models.PositiveIntegerField(default=0)
    total_referral_amount_eth = models.PositiveIntegerField(default=0)
    total_amount_tron = models.PositiveIntegerField(default=0)
    total_referral_amount_tron = models.PositiveIntegerField(default=0)
    total_amount_usdt = models.PositiveIntegerField(default=0)
    total_referral_amount_usdt = models.PositiveIntegerField(default=0)
    total_amount_bonus_sub = models.PositiveIntegerField(default=500)
    total_amount_deposit = models.PositiveIntegerField(default=0)
    total_amount_withdraw = models.PositiveIntegerField(default=0)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone', 'country']
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.get_full_name()



class Partner(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='user_partner'
    )
    first_partern_added = models.OneToOneField(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name="first_partner", 
        blank=True
    )
    last_partern_added = models.OneToOneField(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        related_name="last_partner_added", 
        blank=True
    )
    next_youngest_brother = models.OneToOneField(
        User, 
        null=True, 
        on_delete=models.SET_NULL, 
        blank=True,
        # related_name="next_youngest_partner"
    )

    def __str__(self) -> str:
        return self.user.get_full_name()

    def getTotalNumberOfParternsByLevel(self, level):
        if level > 0:
            if level == 1:
                number_of_partners = 1
            else:
                current = self.first_partern_added
                number_of_partners = 0
                while current != None:
                    number_of_partners = number_of_partners + current.user_partner.getTotalNumberOfParternsByLevel(level-1)
                    current = current.user_partner.next_youngest_brother
            return  number_of_partners

    def getAllUserPartners(self):
        numbers_of_partners = 1
        list_of_partners = []
        current_partner = self.first_partern_added
        
        while current_partner is not None:
            # numbers_of_partners = numbers_of_partners + current_partner.user_partner.getAllUserPartners()
            list_of_partners = list_of_partners + current_partner.user_partner.getAllUserPartners()
            print(current_partner)
            list_of_partners.append(current_partner)
            current_partner = current_partner.user_partner.next_youngest_brother
        return list_of_partners


