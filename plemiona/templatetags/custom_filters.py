from django import template

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value, arg):
    """Pobiera atrybut obiektu dynamicznie."""
    return getattr(value, arg, '')
