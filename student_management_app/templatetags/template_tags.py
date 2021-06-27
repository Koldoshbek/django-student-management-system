from django import template

from student_management_app.models import Subjects

register = template.Library()


@register.simple_tag
def get_staff_name(name):
    try:
        staff = Subjects.objects.get(subject_name=name)
        full_name = f'{staff.staff_id.first_name} {staff.staff_id.last_name}'
    except:
        full_name = ""
    return full_name


@register.simple_tag
def get_average(values):
    marks_len = len([values['mark'] for key, values in dict(values).items()])
    return round(sum([values['mark'] for key, values in dict(values).items()]) / marks_len, 2)
