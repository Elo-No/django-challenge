from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد',
    )

    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ آخرین تغییر'
    )

    is_deleted = models.BooleanField(
        default=False,
        verbose_name='آیا حذف شده است؟'
    )

    is_archived = models.BooleanField(
        default=False,
        verbose_name='آیا آرشیو شده است؟',
    )

    class Meta:
        abstract = True