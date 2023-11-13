# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models, api


class hr_employee(models.Model):
    _inherit = 'hr.employee'
    _description='Add fields for moroccan payroll'

    mat_cnss = fields.Char(
        string="CNSS ID",
        groups="hr.group_hr_user",
        required=False
    )
    mat_cimr = fields.Char(
        string="CIMR ID",
        groups="hr.group_hr_user",
        required=False
    )
    dependents = fields.Integer(
        string='Number of Dependent',
        groups="hr.group_hr_user",
    )

