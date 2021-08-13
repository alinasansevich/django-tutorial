from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline): # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”
    model = Choice
    extra = 3


# admin.site.register(Question) --> this is the first approach, that was replaced with:

#     ### first strategy: fields listed in the order provided in the fields attribute
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text'] # This particular change above makes the “Publication date” come before the “Question” field:

# admin.site.register(Question, QuestionAdmin) # You’ll follow this pattern – create a model admin class, then pass it as the second argument to admin.site.register() – any time you need to change the admin options for a model.

    ### second strategy: use fieldsets (for forms with many fields)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}), # The first element of each tuple in fieldsets is the title of the fieldset.
        ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object
    # to customize how it is displayed, use the @admin.display decorator in models.py
    list_filter = ['pub_date'] # This adds a “Filter” sidebar that lets people filter the change list by the pub_date field
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)






