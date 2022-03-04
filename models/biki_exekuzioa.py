# -*- coding: utf-8 -*-

from odoo import models, fields


class Exekuzioa(models.Model):
    _name = 'biki.exekuzioa'
    _description = 'makina zehatz bateko programa baten exekuzio bat'

    id = fields.Integer(index=True,required=True)
    NPrograma = fields.Double()
    TipoPrograma = fields.Double()
    OK = fields.Bool()
    NG = fields.Bool()
    ResulSPAS = fields.Double()
    ResulSLAE = fields.Double()
    ResulSTAE = fields.Double()
    PosContacto = fields.Double()
    PosFinal = fields.Double()
    CargaFinal = fields.Double()
    TiempoCiclo = fields.Double()
 #   Makina = fields.Many2one('biki.makina', string='Makina', index=True,required=True)
 #   Programa = fields.Many2one('biki.programa', string='Programa', index=True,required=True)
 #   Pieza = fields.Many2one('biki.pieza', string='Pieza', index=True,required=True)

