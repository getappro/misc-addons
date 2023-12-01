# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models, api


class res_company(models.Model):
    _inherit = 'res.company'
    _description='Add fields for moroccan payroll'

    company_cnss_id = fields.Char(
        string="CNSS affiliation number",
        help="If the company is affiliated with the CNSS, include the CNSS number.",
        copy=False,
        required=False
    )
    cnss_limit = fields.Float(
        string="CNSS Base Salary Limit",
        help="Base salary ceiling for calculating the cnss",
        copy=False,
        default="6000"
    )
    employee_nbre = fields.Integer(
        string="Number of employees",
        copy=False,
        readonly=True,
        compute="_get_count_employee"
    )
    company_cimr_id = fields.Char(
        string="CIMR affiliation number",
        help="If the company is affiliated with the CIMR, include the CIMR number.",
        copy=False,
        required=False
    )

    def _get_count_employee(self):
        for emp in self:
            emp.employee_nbre = self.env['hr.employee'].search_count([('active', '=', True)])

