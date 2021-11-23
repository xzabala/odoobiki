# -*- coding: utf-8 -*-

from odoo import models, fields


class Makinamota(models.Model):
    _name = 'biki.makinamota'
    _description = 'Makina bakoitzaren informazioa gordetzeko'

    MakinaMotaErref = fields.Char(size=10,index=True,required=True)
    Izena = fields.Char(size=30,index=True,required=True)
 