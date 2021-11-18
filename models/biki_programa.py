# -*- coding: utf-8 -*-

from odoo import models, fields


class Programa(models.Model):
    _name = 'biki.programa'
    _description = 'Makina errealaren datuak kudeatzeko'

    NumPrograma = fields.Integer(index=True,required=True)
    TipoPrograma = fields.Integer()
    PosInicial = fields.Integer()
    PosComienzo = fields.Integer()
    PosFinal = fields.Integer()
    PosRefParada = fields.Integer()
    VelAproximacion = fields.Integer()
    VelContacto = fields.Integer()
    VelPrensado = fields.Integer()
    VelMaxima = fields.Integer()
    FuerzaMaxima = fields.Integer()
    RelacionFuerza = fields.Integer()
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
    STAE = fields.Boolean()
    STAESup = fields.Integer()
    STAEInf = fields.Integer()

