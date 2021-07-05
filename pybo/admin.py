from django.contrib import admin
# ---------------------------------- [edit] ---------------------------------- #

from .models import Question
from .models import Answer


admin.site.register(Question)
admin.site.register(Answer)
# ---------------------------------------------------------------------------- #