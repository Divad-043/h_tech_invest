from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
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
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'phone', 'country']
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.get_full_name()


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_ass')
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ref_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_amount = models.PositiveIntegerField(default=0)
    total_referral_amount = models.PositiveIntegerField(default=0)
    total_amount_deposit = models.PositiveIntegerField(default=0)
    total_amount_withdraw = models.PositiveIntegerField(default=0)
    # total_referal = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.user

    def getTotalNumberOfParterns(self):
        pass

    def getTotalEarned(self):
        pass

    def getNumberOfClickOnTheReferralLink(self):
        return UserInformation.objects.filter(added_by=self.user).count()

