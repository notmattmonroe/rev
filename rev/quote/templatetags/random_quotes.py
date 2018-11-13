from django import template
from rev.quote.models import Quote

register = template.Library()

@register.inclusion_tag('quotes/random_quote.html')
def random_quote():
	quote = Quote.objects.order_by('?')[0]
	
	return {'quote': quote}
