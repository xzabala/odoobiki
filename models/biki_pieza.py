# -*- coding: utf-8 -*-

from odoo import models, fields


class Pieza(models.Model):
    _name = 'biki.pieza'
    _description = 'Pizak gordetzeko'
    
    NumPieza = fields.Integer()
    Altura = fields.Float()
    Diametro = fields.Float()
    Densidad = fields.Float()
    Peso = fields.Float()
    Material = fields.Char()
     
    
    
    
