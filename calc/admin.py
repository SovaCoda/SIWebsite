from django.contrib import admin
from calc.forms import NameForm

# Register your models here.
from django.forms import TextInput, Textarea
from django.db import models

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'60'})},
        models.TextField: {'widget': Textarea(attrs={'rows':40, 'cols':40})},
    }

admin.site.register(NameForm, YourModelAdmin)