from django.views import generic

from estatistica.models import GraficoBarrasParaVariaveisQualitativasNominais, \
    GraficoBarrasParaVariaveisQualitativasOrdinais


class GraficoBarrasView(generic.TemplateView):
    template_name = 'estatistica/grafico_barras.html'


class GraficoBarrasJSView(generic.TemplateView):
    template_name = 'estatistica/grafico_barras.js'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response['Content-Type'] = 'application/javascript'
        return response


class GraficoBarrasQualitativaNominalJSView(GraficoBarrasJSView):
    def get_context_data(self, **kwargs):
        manager = getattr(GraficoBarrasParaVariaveisQualitativasNominais, 'objects')
        queryset = manager.filter(variavel_id=self.request.GET.get('variavel_id'))
        return super().get_context_data(queryset=queryset, **kwargs)


class GraficoBarrasQualitativaOrdinalJSView(GraficoBarrasJSView):
    def get_context_data(self, **kwargs):
        manager = getattr(GraficoBarrasParaVariaveisQualitativasOrdinais, 'objects')
        queryset = manager.filter(variavel_id=self.request.GET.get('variavel_id'))
        return super().get_context_data(queryset=queryset, **kwargs)
