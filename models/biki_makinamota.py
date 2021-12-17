# -*- coding: utf-8 -*-

from odoo import models, fields


class Makinamota(models.Model):
    _name = 'biki.makinamota'
    _description = 'Makina bakoitzaren informazioa gordetzeko'

    name = fields.Char(size=30,index=True,string="Mota",required=True)
 