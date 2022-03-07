# -*- coding: utf-8 -*-

from xml.dom.minidom import Identified
from odoo import models, fields


class Egoera(models.Model):
    _name = 'biki.egoera'
    _description = 'Makina egoerak gordetzeko'
    
    id = fields.Integer(index=True,required=True)
    ListoNuevoPrensado = fields.Boolean()
    EnMarcha = fields.Boolean()
    FaseAproximacion = fields.Boolean()
    FaseContacto = fields.Boolean()
    FasePrensado = fields.Boolean()
    FaseMantenimiento = fields.Boolean()
    FaseRetroceso = fields.Boolean()
    GrabandoProg = fields.Boolean()
    ProgValidado = fields.Boolean()
    ModoJog = fields.Boolean()
    ParadaAnomalo = fields.Boolean()
    ParadaBimanual = fields.Boolean()
    PosInicioCompletado = fields.Boolean()
    Homing = fields.Boolean()
    ParadaEmergencia = fields.Boolean()
    RearmeSistema = fields.Boolean()
    No_CI = fields.Boolean()
    ParadaInicial = fields.Boolean()
    GrabandoDatos = fields.Boolean()
    CeroRefAlcanzado = fields.Boolean()
    MarchaExtActivada = fields.Boolean()
    BimanualActivado = fields.Boolean()
    PrensadoEnCurso = fields.Boolean()
    EjeNoReferenciado = fields.Boolean()
    ReferenciadoActivado = fields.Boolean()
    Exekuzioa = fields.Many2one('biki.exekuzioa', string='Exekuzioa', index=True)
    
    
    
