from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re
from datetime import date
from .models import Ventas, VentasDetalles

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'fecha_orden_compra': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def clean_cliente(self):
        cliente = self.cleaned_data['cliente']
        if cliente == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un cliente'),
            )
        return cliente

    def clean_segmento(self):
        segmento = self.cleaned_data['segmento']
        if segmento == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un segmento'),
            )
        return segmento

    def clean_estado(self):
        estado = self.cleaned_data['estado']
        if estado == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un estado'),
            )
        return estado

    def clean_agente(self):
        agente = self.cleaned_data['agente']
        if agente == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione un agente'),
            )
        return agente

    def clean_cotizacion(self):
        return self.cleaned_data['cotizacion']

    def clean_descripcion(self):
        return self.cleaned_data['descripcion']

    def clean_clasificacion(self):
        clasificacion = self.cleaned_data['clasificacion']
        if clasificacion == 'SELECCIONE':
            raise ValidationError(
                _('Seleccione una clasificación'),
            )
        return clasificacion

    def clean_orden_compra(self):
        orden_compra = self.cleaned_data['orden_compra']
        if not re.match(r'^[0-9]+$', orden_compra):
            raise ValidationError(
                _('Ingrese un número de orden de compra válido'),
            )

        return orden_compra

    def clean_fecha_orden_compra(self):
        fecha_orden_compra = self.cleaned_data['fecha_orden_compra']
        if fecha_orden_compra > date.today():
            raise ValidationError(
                _('La fecha de orden de compra no puede ser mayor a la fecha actual'),
            )
        return fecha_orden_compra
    
    def __init__(self, *args, **kwargs):
        super(VentasForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = 'SELECCIONE'
        self.fields['segmento'].empty_label = 'SELECCIONE'
        self.fields['estado'].empty_label = 'SELECCIONE'
        self.fields['agente'].empty_label = 'SELECCIONE'
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['placeholder'] = field.label
        if field_name in ['fecha_orden_compra']:
                field.widget.attrs['onkeyup'] = ''
            
class DetallesVentasForm(forms.ModelForm):
    class Meta:
        model = VentasDetalles
        exclude = [ 'comision']
    
    def clean_concepto(self):
        return self.cleaned_data['concepto']


    def clean_monto_USD(self):
        monto_USD = self.cleaned_data['monto_USD']
        return monto_USD
    
    def clean_monto_MXN(self):
        monto_MXN = self.cleaned_data['monto_MXN']
        
        return monto_MXN

    def clean_incentivo(self):
        incentivo = self.cleaned_data['incentivo']
        
        return incentivo

    def clean_tipo_cambio_factura(self):
        tipo_cambio_factura = self.cleaned_data['tipo_cambio_factura']
       
        return tipo_cambio_factura

    def clean_tipo_cambio_oc(self):
        tipo_cambio_oc = self.cleaned_data['tipo_cambio_oc']
       
        return tipo_cambio_oc


    def clean_importe_USD(self):
        importe_USD = self.cleaned_data['importe_USD']
        return importe_USD
    
    
    def __init__(self, *args, **kwargs):
        super(DetallesVentasForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['onkeyup'] = 'javascript:this.value=this.value.toUpperCase()'
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['autocomplete'] = 'off'
            field.widget.attrs['accept'] = ''
                
                
