from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import SolicitudForm
from .logic.solicitud_logic import get_solicitudes, get_solicitud, create_solicitud
from django.contrib.auth.decorators import login_required
# Descomentar cuando se cree el archivo monitoring/auth0backend.py
#from monitoring.auth0backend import getRole

@login_required
def solicitud_list(request):
    role = getRole(request)
    if role == "Asesor":
        solicitudes = get_solicitudes()
        context = {
            'solicitudes_list': solicitudes
        }
        return render(request, 'Solicitud/solicitudes.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_solicitud(request, id=0):
    solicitud = get_solicitud(id)
    context = {
        'solicitud': solicitud
    }
    return render(request, 'Solicitud/solicitud.html', context)

@login_required
def solicitud_create(request):
    role = getRole(request)
    if role == "Asesor":
        if request.method == 'POST':
            form = SolicitudForm(request.POST)
            if form.is_valid():
                create_solicitud(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created solicitud')
                return HttpResponseRedirect(reverse('solicitudCreate'))
            else:
                print(form.errors)
        else:
            form = SolicitudForm()

        context = {
            'form': form,
        }
        return render(request, 'Solicitud/solicitudCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
