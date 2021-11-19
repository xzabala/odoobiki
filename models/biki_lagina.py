# -*- coding: utf-8 -*-

from odoo import models, fields


class Lagina(models.Model):
    _name = 'biki.lagina'
    _description = 'Laginak gordetzeko'

    NumMuestra = fields.Integer(index=True,required=True)
    PosicionCana = fields.Integer()
    VelocidadCana = fields.Integer()
    ConsignaVelocidad = fields.Integer()
    FuerzaRealizada = fields.Integer()
    
    
