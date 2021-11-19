# -*- coding: utf-8 -*-

from odoo import models, fields


class Emaitza(models.Model):
    _name = 'biki.emaitza'
    _description = 'Makina errealaren datuak kudeatzeko'

    NumPrograma = fields.Integer(index=True,required=True)
    TipoPrograma = fields.Integer()
    Ok = fields.Boolean()
    Ng = fields.Boolean()
    ResulSPAS = fields.Integer()
    ResulSTAE = fields.Integer()
    PosContacto = fields.Integer()
    PosFinal = fields.Integer()
    CargaFinal = fields.Integer()
    TiempoCiclo = fields.Integer()
    
