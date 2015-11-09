# -*- coding: utf-8 -*-
from openerp import http

# class Acinventario(http.Controller):
#     @http.route('/acinventario/acinventario/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acinventario/acinventario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('acinventario.listing', {
#             'root': '/acinventario/acinventario',
#             'objects': http.request.env['acinventario.acinventario'].search([]),
#         })

#     @http.route('/acinventario/acinventario/objects/<model("acinventario.acinventario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acinventario.object', {
#             'object': obj
#         })