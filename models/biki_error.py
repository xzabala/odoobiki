# -*- coding: utf-8 -*-

from xml.dom.minidom import Identified
from odoo import models, fields


class Error(models.Model):
    _name = 'biki.error'
    _description = 'Makina erroreak gordetzeko'
    
    id = fields.Integer(index=True,required=True)
    ListoNuevoPrensado = fields.Boolean()
    EnMarcha = fields.Boolean()
    FaseAproximacion = fields.Boolean()
    FaseContacto = fields.Boolean()
    FasePrensado = fields.Boolean()
    FaseMantenimiento = fields.Boolean()
    FaseRetroceso = fields.Boolean()
    ProgValidado = fields.Boolean()
    ModoJog = fields.Boolean()
    ParadaAnomalo = fields.Boolean()
    ParadaSolicitada = fields.Boolean()
    PosInicioCompletado = fields.Boolean()
    Homing = fields.Boolean()
    ParadaEmergencia = fields.Boolean()
    RearmeSistema = fields.Boolean()
    No_CI = fields.Boolean()
    GrabandoDatos = fields.Boolean()
    CeroRefAlcanzado = fields.Boolean()
    MarchaActivada = fields.Boolean()
    EjeNoReferenciado = fields.Boolean()
    ReferenciadoActivado = fields.Boolean()
    CicloTerminado = fields.Boolean()
    NumeroPrograma = fields.Integer()
    TipoPrograma = fields.Integer()
    NumeroPieza = fields.Integer()
    Error = fields.Boolean()
    NumeroError = fields.Integer()    
    
    
