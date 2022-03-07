# -*- coding: utf-8 -*-

from xml.dom.minidom import Identified
from odoo import models, fields


class InfoEzezaguna(models.Model):
    _name = 'biki.infoezezaguna'
    _description = 'Tratetzen ez diren balioak'
    
    id = fields.Integer(index=True,required=True)
    Gakoa = fields.Char(size=30,string='Gakoak')
    Balioa = fields.Char(size=30,string='Balioa')    
    
    
