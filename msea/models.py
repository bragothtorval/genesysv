from django.db import models
from django.contrib.auth.models import User, Group
from common.models import TimeStampedModel


class Study(TimeStampedModel):
    short_name = models.CharField(max_length=32)
    display_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'studies'

    def __str__(self):
        return self.display_name


class Dataset(TimeStampedModel):
    study = models.ForeignKey(
        Study,
        on_delete=models.CASCADE,
    )
    short_name = models.CharField(max_length=32)
    display_name = models.CharField(max_length=255)
    es_index_name = models.CharField(max_length=255)
    es_type_name = models.CharField(max_length=255)
    es_host = models.CharField(max_length=255)
    es_port = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    allowed_groups = models.ManyToManyField(
        Group, related_name='msea_group', blank=True)

    def __str__(self):
        return self.display_name


class VariantSet(TimeStampedModel):
    short_name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name


class Gene(TimeStampedModel):
    gene_name = models.CharField(max_length=32)

    def __str__(self):
        return self.gene_name


class ReferenceSequence(TimeStampedModel):
    study = models.ForeignKey(
        'Study',
        on_delete=models.CASCADE,
    )
    rs_id = models.CharField(max_length=12)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    variants = models.ManyToManyField(VariantSet)

    def __str__(self):
        return self.rs_id
