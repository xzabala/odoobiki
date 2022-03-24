# -*- coding: utf-8 -*-

from odoo import models, fields


class Lagina(models.Model):
    _name = 'biki.lagina'
    _description = 'Laginak gordetzeko'

    NumMuestra = fields.Integer(index=True,required=True)
    PosicionReal = fields.Float()
    VelocidadReal = fields.Float()
    VelocidadConsigna = fields.Float()
    CargaReal = fields.Float()
    CargaContacto = fields.Float()
    Egoera = fields.Many2one('biki.egoera', string='Egoera', index=True, required=True)
    Exekuzioa = fields.Many2one('biki.exekuzioa', string='Exekuzioa', index=True, required=True)

    
    
