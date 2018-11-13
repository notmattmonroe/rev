from rev.review.models import Review, ReviewType, RatingKey
from django.contrib import admin


class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewType)
admin.site.register(RatingKey)
