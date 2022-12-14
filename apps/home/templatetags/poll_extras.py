from django import template
import calendar
from apps.usuarios.models import Trabajadores
register = template.Library()

@register.filter
def month_name(month_number):
    return calendar.month_name[month_number].capitalize()[:3]


@register.filter
def agente_name(agente_id):
    return Trabajadores.objects.get(id=agente_id)