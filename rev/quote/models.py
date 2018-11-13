from django.db import models
class Quote(models.Model):
    quote = models.TextField(help_text="Enter the quote")
    speaker = models.CharField(max_length=30, help_text="Enter the quote author")
    prepopulated_fields={"slug": ("title",)}
    def __str__(self):
        return self.quote
    class Admin:
        list_display = ('quote', 'by', 'slug')


