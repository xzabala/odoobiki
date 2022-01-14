# -*- coding: utf-8 -*-

from xml.dom.minidom import Identified
from odoo import models, fields


class Egoera(models.Model):
    _name = 'biki.egoera'
    _description = 'Makina egoerak gordetzeko'
    
    id = fields.Integer(index=True,required=True)
    ListoNuevoPrensado = fields.Bool()
    EnMarcha = fields.Bool()
    FaseAproximacion = fields.Bool()
    FaseContacto = fields.Bool()
    FasePrensado = fields.Bool()
    FaseMantenimiento = fields.Bool()
    FaseRetroceso = fields.Bool()
    GrabandoProg = fields.Bool()
    ProgValidado = fields.Bool()
    ModoJog = fields.Bool()
    ParadaAnomalo = fields.Bool()
    ParadaBimanual = fields.Bool()
    PosInicioCompletado = fields.Bool()
    Homing = fields.Bool()
    ParadaEmergencia = fields.Bool()
    RearmeSistema = fields.Bool()
    No_CI = fields.Bool()
    ParadaInicial = fields.Bool()
    GrabandoDatos = fields.Bool()
    CeroRefAlcanzado = fields.Bool()
    MarchaExtActivada = fields.Bool()
    BimanualActivado = fields.Bool()
    PrensadoEnCurso = fields.Bool()
    EjeNoReferenciado = fields.Bool()
    ReferenciadoActivado = fields.Bool()
    Exekuzioa = fields.Many2one('biki.exekuzioa', string='Exekuzioa', index=True)
    
    
    
