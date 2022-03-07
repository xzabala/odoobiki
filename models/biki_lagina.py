# -*- coding: utf-8 -*-

from odoo import models, fields


class Lagina(models.Model):
    _name = 'biki.lagina'
    _description = 'Laginak gordetzeko'

    NumMuestra = fields.Integer(index=True,required=True)
    PosicionReal = fields.integer()
    VelocidadReal = fields.integer()
    VelocidadConsigna = fields.integer()
    CargaReal = fields.integer()
    CargaContacto = fields.integer()
    Egoera = fields.Many2one('biki.egoera', string='Egoera', index=True,required=True)
    Exekuzioa = fields.Many2one('biki.exekuzioa', string='Exekuzioa', index=True,required=True)

    
    
