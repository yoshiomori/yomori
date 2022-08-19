from django.db import models


class Variavel(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=10000, verbose_name='descrição')

    class Meta:
        abstract = True


class VariavelQualitativoNominal(Variavel):
    pass


class VariavelQualitativoOrdinal(Variavel):
    pass


class VariavelQuantitativoDiscreto(Variavel):
    pass


class VariavelQuantitativoContinuo(Variavel):
    pass


class ValorQualitativoNominal(models.Model):
    variavel = models.ForeignKey(VariavelQualitativoNominal, models.PROTECT)
    valor = models.CharField(max_length=255)


class ValorQualitativoOrdinal(models.Model):
    variavel = models.ForeignKey(VariavelQualitativoNominal, models.PROTECT)
    valor = models.CharField(max_length=255)
    ordem = models.IntegerField()


class ValorQuantitativoDiscreto(models.Model):
    variavel = models.ForeignKey(VariavelQuantitativoDiscreto, models.PROTECT)
    valor = models.BigIntegerField()


class ValorQuantitativoContinuo(models.Model):
    variavel = models.ForeignKey(VariavelQuantitativoContinuo, models.PROTECT)
    valor = models.DecimalField(max_digits=64, decimal_places=30)


class GraficoBarrasParaVariaveisQualitativas(models.Model):
    """Gráfico de Barras Para Variáveis Qualitativas"""
    valor = models.CharField(max_length=255)  # Valor da Variável Qualitativa
    quantidade = models.PositiveIntegerField()

    class Meta:
        abstract = True


class GraficoBarrasParaVariaveisQualitativasNominais(GraficoBarrasParaVariaveisQualitativas):
    variavel = models.ForeignKey(VariavelQualitativoNominal, on_delete=models.PROTECT)


class GraficoBarrasParaVariaveisQualitativasOrdinais(GraficoBarrasParaVariaveisQualitativas):
    variavel = models.ForeignKey(VariavelQualitativoOrdinal, on_delete=models.PROTECT)
