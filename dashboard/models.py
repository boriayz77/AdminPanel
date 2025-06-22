
from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    banned = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'telegram_users'
