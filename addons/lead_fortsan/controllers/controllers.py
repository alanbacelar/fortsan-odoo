# -*- coding: utf-8 -*-
# from odoo import http


# class LeadFortsan(http.Controller):
#     @http.route('/lead_fortsan/lead_fortsan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lead_fortsan/lead_fortsan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lead_fortsan.listing', {
#             'root': '/lead_fortsan/lead_fortsan',
#             'objects': http.request.env['lead_fortsan.lead_fortsan'].search([]),
#         })

#     @http.route('/lead_fortsan/lead_fortsan/objects/<model("lead_fortsan.lead_fortsan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lead_fortsan.object', {
#             'object': obj
#         })
