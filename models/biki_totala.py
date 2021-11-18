# -*- coding: utf-8 -*-

from odoo import models, fields


class Totala(models.Model):
    _name = 'biki.totala'
    _description = 'Makinaren totalak'

    NumTotal = fields.Integer(index=True,required=True)
    ContadorTotal = fields.Integer()
    OkTotal = fields.Integer()
    NgTotal = fields.Integer()
    PorcFallos = fields.Integer()
    
    
