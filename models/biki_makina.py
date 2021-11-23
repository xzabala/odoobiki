# -*- coding: utf-8 -*-

from odoo import models, fields


class Makina(models.Model):
    _name = 'biki.makina'
    _description = 'Makina bakoitzaren informazioa gordetzeko'

    MakinaErref = fields.Char(size=20,index=True,required=True)
    MakinaMotaID = fields.Many2one('biki.makinamota', string='Makina mota', index=True)

