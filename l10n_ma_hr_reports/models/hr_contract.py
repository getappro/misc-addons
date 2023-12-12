# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models, api

class hr_contract(models.Model):
    _inherit = 'hr.contract'
    _description='Add fields for reports moroccan payroll'

    wage_net = fields.Monetary('Salaire Net', required=False, tracking=True, help="Employee's monthly net wage.")