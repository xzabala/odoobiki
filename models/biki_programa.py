# -*- coding: utf-8 -*-

from odoo import models, fields


class Programa(models.Model):
    _name = 'biki.programa'
    _description = 'Makina errealaren datuak kudeatzeko'

    id = fields.Integer(index=True,required=True)
    NumPrograma = fields.Integer()
    TipoPrograma = fields.Integer()
    PosInicial = fields.Float()
    PosComienzo = fields.Float()
    PosFinal = fields.Float()
    PosRefParada = fields.Float()
    VelAproximacion = fields.Float()
    VelContacto = fields.Float()
    VelPrensado = fields.Float()
    VelMaxima = fields.Float()
    VelRetroceso = fields.Float()
    VelHoming = fields.Float()
    VelJogFast = fields.Float()
    VelJogSlow = fields.Float()
    FuerzaMaxima = fields.Float()
    RelacionFuerza = fields.Float()
    CargaContacto = fields.Float()
    DistanciaPrensado = fields.Float()
    TiempoPrensado = fields.Integer()
    TiempoMantenimiento = fields.Integer()
    TiempoMaxPrensado = fields.Integer()
    SLAE = fields.Boolean()
    SLAESup = fields.Float()
    SLAEInf = fields.Float()
    SPAS = fields.Boolean()
    SPASSup = fields.Float()
    SPASInf = fields.Float()
    SPAE = fields.Boolean()
    SPAESup = fields.Float()
    SPAEInf = fields.Float()
