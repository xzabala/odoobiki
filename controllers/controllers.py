# -*- coding: utf-8 -*-
# from odoo import http


# class Biki(http.Controller):
#     @http.route('/biki/biki/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biki/biki/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('biki.listing', {
#             'root': '/biki/biki',
#             'objects': http.request.env['biki.biki'].search([]),
#         })

#     @http.route('/biki/biki/objects/<model("biki.biki"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biki.object', {
#             'object': obj
#         })
