from django.contrib import admin
from .models import *

model_list = [EkoloskaNavika, DnevnikEkoloskihAktivnosti, Feedback, Korisnik]
admin.site.register(model_list)