from django.http import JsonResponse
from django.shortcuts import render
from bbm.models import Pins, Contacts


def index(request):
    pin1 = None
    pin2 = None

    print(request.GET['pin1'])

    if request.GET['pin1']:
        pin = request.GET['pin1']
        pin1 = Pins.objects.filter(pin=pin).first()
    else:
        data = {"message": "Error in Input1."}
        return JsonResponse(data)

    if request.GET['pin2']:
        pin = request.GET['pin2']
        pin2 = Pins.objects.filter(pin=pin).first()
    else:
        data = {"message": "Error in Input2."}
        return JsonResponse(data)


    pin_contact1 = Contacts.objects.filter(pin=pin1).values_list('contact', flat=True)
    pin_contact2 = Contacts.objects.filter(pin=pin2).values_list('contact', flat=True)

    common_contact = list(pin_contact1.intersection(pin_contact2))

    common_pins = Pins.objects.filter(id__in=common_contact)
    # print("{} | {} | common {}".format(pin_contact1, pin_contact2, common_pins))

    common = list(common_pins.values('pin'))

    # print(common)
    data = {
                'message': "It worked.",
                'pins': common,
            }
    return JsonResponse(data)
