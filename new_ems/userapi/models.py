from django.db import models


# Create your models here.
class User(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, "female")
    )

    username = models.CharField(max_length=30)
    real_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "ems_admin"
        verbose_name = "管理员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
