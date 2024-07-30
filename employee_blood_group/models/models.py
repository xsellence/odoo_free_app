# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    blood_group = fields.Selection([('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
                                    ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], string='Blood Group', tracking=True)


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    blood_group = fields.Selection(string='Blood Group', related='employee_id.blood_group', compute_sudo=True)
