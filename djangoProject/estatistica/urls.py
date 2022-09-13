"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from estatistica import views

urlpatterns = [
    path('grafico/barras/nominal/', views.GraficoBarrasNominalView.as_view()),
    path('grafico/barras/ordinal/', views.GraficoBarrasOrdinalView.as_view()),
    path(
        'grafico/barras/js/nominal/',
        views.GraficoBarrasQualitativaNominalJSView.as_view(),
        name='grafico-barras-js-nominal'
    ),
    path(
        'grafico/barras/js/ordinal/',
        views.GraficoBarrasQualitativaOrdinalJSView.as_view(),
        name='grafico-barras-js-ordinal'
    ),
]
