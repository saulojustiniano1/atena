from django.contrib import admin

from .models import Curso, Disciplina, User

admin.site.register(User)
admin.site.register(Curso)
admin.site.register(Disciplina)
