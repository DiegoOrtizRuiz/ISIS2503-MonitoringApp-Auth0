from ..models import Solicitud

def get_solicitudes():
    queryset = Solicitud.objects.all()
    return (queryset)

def get_solicitud(id):
    solicitud = Solicitud.objects.raw("SELECT * FROM solicitudes_solicitud WHERE id=%s" % id)[0]
    return (solicitud)

def create_solicitud(form):
    measurement = form.save()
    measurement.save()
    return ()
