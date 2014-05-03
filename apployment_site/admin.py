from django.contrib import admin
from apployment_site.models import User, Review, Skill, hasSkill, Experience, hasExperience
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Skill)
admin.site.register(hasSkill)
admin.site.register(hasExperience)
admin.site.register(Experience)


