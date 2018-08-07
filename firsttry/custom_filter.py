from django.template import Library

register = Library()

@register.filter("json")
def json(data):
    print(type(data))
    for i in data:
        # print(type (i))
        # print(i)
        if (i == 'results'):
            # print(type(json_var[i]))
            for j in data[i]:
                for z in j:
                    print(z, ":", j[z])