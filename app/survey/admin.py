from django.contrib import admin
from survey.models.survey import Survey, Question,Option


class QuestionTabularModel(admin.TabularInline):
    model = Question


# Register your models here.
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """Survey admin model """
    list_display = ('name', 'owner','total_questions',)
    list_filter = ('created', 'is_active',)
    inlines = [
        QuestionTabularModel,
    ]


class OptionInlineStack(admin.StackedInline):
    model = Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """ Register questions  model in admin dashboard"""
    list_display = ('name', 'survey',)
    inlines = [
        OptionInlineStack
    ]