from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import EnergyCaptureForm
from .models import EnergyCapture
# Create your views here.


class EnergyCaptureFormView(CreateView):
    template_name = 'energy_capture_form.djhtml'
    form_class = EnergyCaptureForm
    model = EnergyCapture
    success_url = reverse_lazy('energy-capture-list')

    def get_context_data(self, **kwargs):
        context = super(EnergyCaptureFormView, self).get_context_data(**kwargs)

        # TODO: we can filter the capture list by date
        context['energy_model_objects'] = self.model.objects

        return context
