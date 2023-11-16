from django import template
from plemiona.models import Village  # Zaimportuj model Village

register = template.Library()

@register.simple_tag
def get_active_village(request):
    village_id = request.session.get('active_village')
    if village_id:
        return Village.objects.filter(id=village_id).first()
    return None
