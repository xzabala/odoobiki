# -*- coding: utf-8 -*-

from odoo import models, fields


class Pieza(models.Model):
    _name = 'biki.pieza'
    _description = 'Pizak gordetzeko'
    
    name = fields.Char(size=20,string='Erreferentzia',index=True,required=True)
     
    
    
    
