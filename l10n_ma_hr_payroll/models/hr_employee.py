# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models, api


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    mat_cnss = fields.Char(
        string="CNSS ID",
        required=False
    )
    mat_cimr = fields.Char(
        string="CIMR ID",
        required=False
    )
    matricule = fields.Char(
        string="Matricule",
        required=False
    )
    mutuelle = fields.Boolean(
        'Mutuelle Santé?',
        default=False
    )
    mat_mut = fields.Char(
        string="Mutuelle Santé ID",
        required=False
    )
    dependents = fields.Integer(
        string='Number of Dependent',
    )

