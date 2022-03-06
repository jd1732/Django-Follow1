from django.contrib import admin
from .models import Question, Choices

class ChoiceInline(admin.TabularInline):
    model=Choices
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    list_display=('__str__','pub_date','recently_Pub')
    list_filter=['pub_date']
    search_fields=['ques_text']
    #ads

admin.site.register(Question,QuestionAdmin)



# Register your models here.
