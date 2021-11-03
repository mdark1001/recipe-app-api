"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 01/11/21
@name: survey
"""
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class SurveyActiveManager(models.Manager):
    def get_queryset(self):
        return super(SurveyActiveManager, self).get_queryset().filter(is_active=True)


class Survey(models.Model):
    """Survey model store survey and owner """
    name = models.CharField(
        max_length=255,
        verbose_name=_('Survey name')
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_('Owner'),
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=False,
    )

    @property
    def total_questions(self):
        return Question.objects.filter(survey=self).count()

    # Custom manager for this model
    objects = models.Manager()
    actives = SurveyActiveManager()

    def __str__(self):
        return self.name


class Question(models.Model):
    """Questions in a survey  """
    name = models.CharField(
        verbose_name=_('Name of question'),
        max_length=150,
    )
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    def __str__(self):
        return self.name


class Option(models.Model):
    """Questions  has many or some options  """
    name = models.CharField(
        verbose_name=_('Option'),
        max_length=150,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
