from django.db import models


class Variavel(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=10000, verbose_name='descrição')

    class Meta:
        abstract = True


class VariavelQualitativaOrdinal(Variavel):
    pass


class VariavelQualitativaNominal(Variavel):
    pass


class VariavelQuantitativaDiscreto(Variavel):
    pass


class VariavelQuantitativaContinuo(Variavel):
    pass


class ValorQualitativoNominal(models.Model):
    variavel = models.ForeignKey(VariavelQualitativaNominal, models.PROTECT)
    valor = models.CharField(max_length=255)


class ValorQualitativoOrdinal(models.Model):
    variavel = models.ForeignKey(VariavelQualitativaOrdinal, models.PROTECT)
    valor = models.CharField(max_length=255)
    ordem = models.IntegerField(null=True)


class ValorQuantitativoDiscreto(models.Model):
    variavel = models.ForeignKey(VariavelQuantitativaDiscreto, models.PROTECT)
    valor = models.BigIntegerField()


class ValorQuantitativoContinuo(models.Model):
    variavel = models.ForeignKey(VariavelQuantitativaContinuo, models.PROTECT)
    valor = models.DecimalField(max_digits=64, decimal_places=30)


class GraficoBarrasParaVariaveisQualitativas(models.Model):
    """Gráfico de Barras Para Variáveis Qualitativas"""
    valor = models.CharField(max_length=255)  # Valor da Variável Qualitativa
    quantidade = models.PositiveIntegerField()

    class Meta:
        abstract = True


class GraficoBarrasParaVariaveisQualitativasNominais(GraficoBarrasParaVariaveisQualitativas):
    """Ser populado a medida em que a variável qualitativa nominal for sendo populado. O registro deve ser feito por
    processos assíncronos"""
    variavel = models.ForeignKey(VariavelQualitativaNominal, on_delete=models.PROTECT)


class GraficoBarrasParaVariaveisQualitativasOrdinais(GraficoBarrasParaVariaveisQualitativas):
    """Ser populado a medida em que a variável qualitativa ordinal for sendo populado. O registro deve ser feito por
    processos assíncronos"""
    variavel = models.ForeignKey(VariavelQualitativaOrdinal, on_delete=models.PROTECT)
    ordem = models.IntegerField(null=True)
