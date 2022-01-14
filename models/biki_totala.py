# -*- coding: utf-8 -*-

from odoo import models, fields


class Totala(models.Model):
    _name = 'biki.totala'
    _description = 'Makinaren totalak'

    id = fields.Integer(index=True,required=True)
    ContadorTotal = fields.Integer()
    OKTotal = fields.Integer()
    NGTotal = fields.Integer()
    PorcFallos = fields.Integer()
    Makina = fields.Many2one('biki.makina', string='Makina', index=True,required=True)
    
    
