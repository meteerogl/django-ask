from django.contrib import admin

# Register your models here.

from .models import PROFILE
from .models import QUESTIONS
from .models import COUPLING
from .models import LIKE_DISLIKE

admin.site.register(PROFILE)
admin.site.register(QUESTIONS)
admin.site.register(COUPLING)
admin.site.register(LIKE_DISLIKE)

