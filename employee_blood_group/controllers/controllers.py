# -*- coding: utf-8 -*-
# from odoo import http


# class XlEmployeeBloodGroup(http.Controller):
#     @http.route('/xl_employee_blood_group/xl_employee_blood_group', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xl_employee_blood_group/xl_employee_blood_group/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('xl_employee_blood_group.listing', {
#             'root': '/xl_employee_blood_group/xl_employee_blood_group',
#             'objects': http.request.env['xl_employee_blood_group.xl_employee_blood_group'].search([]),
#         })

#     @http.route('/xl_employee_blood_group/xl_employee_blood_group/objects/<model("xl_employee_blood_group.xl_employee_blood_group"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xl_employee_blood_group.object', {
#             'object': obj
#         })

