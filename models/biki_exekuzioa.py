# -*- coding: utf-8 -*-

from odoo import models, fields


class Exekuzioa(models.Model):
    _name = 'biki.emaitza'
    _description = 'Makina errealaren datuak kudeatzeko'

    NumPrograma = fields.Integer(index=True,required=True)
    TipoPrograma = fields.Integer()
    Ok = fields.Boolean()
    Ng = fields.Boolean()
    ResulSPAS = fields.Integer()
    ResulSTAE = fields.Integer()
    PosContacto = fields.Integer()
    PosFinal = fields.Integer()
    CargaFinal = fields.Integer()
    TiempoCiclo = fields.Integer()
    makinamota = fields.Many2one('biki.makina', string='Makina', index=True,required=True)
    makinamota = fields.Many2one('biki.programa', string='Programa', index=True,required=True)
    makinamota = fields.Many2one('biki.pieza', string='Pieza', index=True,required=True)

