# -*- coding: utf-8 -*-

from odoo import models, fields


class Makina(models.Model):
    _name = 'biki.makina'
    _description = 'Makina bakoitzaren informazioa gordetzeko'

    name = fields.Char(size=20,string='Erreferentzia',index=True,required=True)
#    makinamota = fields.Many2one('biki.makinamota', string='Makina mota', index=True,required=True)
    marka = fields.Char(size=20,string='Marka')
    modeloa = fields.Char(size=20,string='Modeloa')

    def name_get(self):
        """ 'Izena (Marka - Modeloa)' """
        res = []
        for mak in self:
            if mak.marka and mak.modeloa:
                name = mak.name + ' (' + mak.marka + ' - ' + mak.modeloa + ')'
            else:
                name = mak.name
            res.append((mak.id, name))
        return res


