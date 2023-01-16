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


class UserInfos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_ass')
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ref_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_amount = models.PositiveBigIntegerField(default=0)
    total_benefic_amount = models.PositiveBigIntegerField(default=0)

