from django.contrib import admin
from apployment_site.models import User, Rating, Skill, hasSkill, Experience, hasExperience
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Skill)
admin.site.register(hasSkill)
admin.site.register(hasExperience)
admin.site.register(Experience)


