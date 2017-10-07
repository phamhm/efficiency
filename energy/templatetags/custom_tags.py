from django.db.models import Avg
from django import template

register = template.Library()


@register.simple_tag
def average_energy(energy_capture_list):
    avg = energy_capture_list.aggregate(Avg('energy_level'))
    return avg.get('energy_level__avg')


@register.simple_tag(takes_context=True)
def print_context(context):
    return context


@register.inclusion_tag('energy_list.html')
def show_energy_list(energy_model_objects, item_counts=None):
    # TODO: find more efficient filter for last_N objects
    energy_list = energy_model_objects.order_by('-id')

    if item_counts:
        return {'energy_list': energy_list[:item_counts]}
    else:
        return {'energy_list': energy_list}
