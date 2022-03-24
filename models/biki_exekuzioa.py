# -*- coding: utf-8 -*-

from odoo import models, fields


class Exekuzioa(models.Model):
    _name = 'biki.exekuzioa'
    _description = 'makina zehatz bateko programa baten exekuzio bat'

    id = fields.Integer(index=True,required=True)
    NPrograma = fields.Integer()
    TipoPrograma = fields.Integer()
    OK = fields.Boolean()
    NG = fields.Boolean()
    ResulSPAS = fields.Integer()
    ResulSLAE = fields.Integer()
    ResulSTAE = fields.Integer()
    PosContacto = fields.Float()
    PosFinal = fields.Float()
    PosFinalNA = fields.Boolean()
    CargaFinal = fields.Float()
    CargaFinalNA = fields.Boolean()
    TiempoCiclo = fields.Integer()
    Makina = fields.Many2one('biki.makina', string='Makina', index=True,required=True)
    Programa = fields.Many2one('biki.programa', string='Programa', index=True,required=True)
    Pieza = fields.Many2one('biki.pieza', string='Pieza', index=True,required=True)

