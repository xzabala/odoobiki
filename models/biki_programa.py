# -*- coding: utf-8 -*-

from odoo import models, fields


class Programa(models.Model):
    _name = 'biki.programa'
    _description = 'Makina errealaren datuak kudeatzeko'

    id = fields.Integer(index=True,required=True)
    NumPrograma = fields.Integer()
    TipoPrograma = fields.Integer()
    PosInicial = fields.Integer()
    PosComienzo = fields.Integer()
    PosFinal = fields.Integer()
    PosRefParada = fields.Integer()
    VelAproximacion = fields.Integer()
    VelContacto = fields.Integer()
    VelPrensado = fields.Integer()
    VelMaxima = fields.Integer()
    VelRetroceso = fields.Integer()
    VelHoming = fields.Integer()
    VelJogFast = fields.Integer()
    VelJogSlow = fields.Integer()
    FuerzaMaxima = fields.Integer()
    RelacionFuerza = fields.Integer()
    CargaContacto = fields.Integer()
    DistanciaPrensado = fields.Integer()
    TiempoPrensado = fields.Integer()
    TiempoMantenimiento = fields.Integer()
    TiempoMaxPrensado = fields.Integer()
    SLAE = fields.Boolean()
    SLAESup = fields.Integer()
    SLAEInf = fields.Integer()
    SPAS = fields.Boolean()
    SPASSup = fields.Integer()
    SPASInf = fields.Integer()
    SPAE = fields.Boolean()
    SPAESup = fields.Integer()
    SPAEInf = fields.Integer()
