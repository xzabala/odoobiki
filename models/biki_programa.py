# -*- coding: utf-8 -*-

from odoo import models, fields


class Programa(models.Model):
    _name = 'biki.programa'
    _description = 'Makina errealaren datuak kudeatzeko'

    id = fields.Integer(index=True,required=True)
    NumPrograma = fields.Double()
    TipoPrograma = fields.Double()
    PosInicial = fields.Double()
    PosComienzo = fields.Double()
    PosFinal = fields.Double()
    PosRefParada = fields.Double()
    VelAproximacion = fields.Double()
    VelContacto = fields.Double()
    VelPrensado = fields.Double()
    VelMaxima = fields.Double()
    VelRetroceso = fields.Double()
    VelHoming = fields.Double()
    VelJogFast = fields.Double()
    VelJogSlow = fields.Double()
    FuerzaMaxima = fields.Double()
    RelacionFuerza = fields.Double()
    CargaContacto = fields.Double()
    DistanciaPrensado = fields.Double()
    TiempoPrensado = fields.Double()
    TiempoMantenimiento = fields.Double()
    TiempoMaxPrensado = fields.Double()
    SLAE = fields.Bool()
    SLAESup = fields.Double()
    SLAEInf = fields.Double()
    SPAS = fields.Bool()
    SPASSup = fields.Double()
    SPASInf = fields.Double()
    STAE = fields.Bool()
    STAESup = fields.Double()
    STAEInf = fields.Double()
