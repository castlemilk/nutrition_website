from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm
#admin.site.register(SignUp)

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    # class Meta:
    #     model = SignUp
    form = SignUpForm


admin.site.register(SignUp, SignUpAdmin)
