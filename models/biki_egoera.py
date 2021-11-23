# -*- coding: utf-8 -*-

from odoo import models, fields


class Egoera(models.Model):
    _name = 'biki.egoera'
    _description = 'Makina egoerak gordetzeko'
    
    NumEstado = fields.Integer(index=True,required=True)
    CeroRefCompletado = fields.Boolean ()
    BuscarCeroRef = fields.Boolean ()
    EnMarcha = fields.Boolean ()
    RestablecerTrasParada = fields.Boolean ()
    MarchaExt = fields.Boolean ()
    StopBajandoExt = fields.Boolean ()
    StopExt = fields.Boolean ()
    FuncAnomalo = fields.Boolean ()
    PosInicialCompletado = fields.Boolean ()
    SeleccionarProg = fields.Boolean ()
    CrearPrograma = fields.Boolean ()
    NProgSeleccionado = fields.Many2one('biki.programa', string='Aukeratutako programa', index=True)
    HomeExt = fields.Boolean ()
    ResetAlarma = fields.Boolean ()
    GrabarPrograma = fields.Boolean ()
    ConfirmarRunExt = fields.Boolean ()
    SalirModo = fields.Boolean ()
    JogExt = fields.Boolean ()
    JogUpSlow = fields.Boolean ()
    JogDownSlow = fields.Boolean ()
    JogUpFast = fields.Boolean ()
    JogDownFast = fields.Boolean ()
    CargarProg = fields.Boolean ()
    CondicionesIniciales = fields.Boolean ()
    MarchaExtActivada = fields.Boolean ()
    EmergenciaActiva = fields.Boolean ()
    EtapaActiva = fields.Boolean ()
    
    
    
    
