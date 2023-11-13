# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class HrPayrollAdvice(models.Model):
    '''
    Bank Advice
    '''
    _name = 'hr.payroll.advice'
    _description = "Moroccan HR Payroll Advice"

    def _get_default_date(self):
        return fields.Date.from_string(fields.Date.today())

    name = fields.Char(readonly=True, required=True, states={'draft': [('readonly', False)]})
    note = fields.Text(string='Description',
                       default='Please make the payroll transfer from above account number to the below mentioned account numbers towards employee salaries:')
    date = fields.Date(readonly=True, required=True, states={'draft': [('readonly', False)]}, default=_get_default_date,
                       help='Advice Date is used to search Payslips')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', index=True, readonly=True)
    number = fields.Char(string='Reference', readonly=True)
    line_ids = fields.One2many('hr.payroll.advice.line', 'advice_id', string='Employee Salary',
                               states={'draft': [('readonly', False)]}, readonly=True, copy=True)
    chaque_nos = fields.Char(string='Cheque Numbers')
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
                                 states={'draft': [('readonly', False)]}, default=lambda self: self.env.user.company_id)
    bank_id = fields.Many2one('res.bank', string='Bank', readonly=True, states={'draft': [('readonly', False)]},
                              help='Select the Bank from which the salary is going to be paid')
    batch_id = fields.Many2one('hr.payslip.run', string='Batch', readonly=True)

    def compute_advice(self):
        """
        Advice - Create Advice lines in Payment Advice and
        compute Advice lines.
        """
        for advice in self:
            old_lines = self.env['hr.payroll.advice.line'].search([('advice_id', '=', advice.id)])
            if old_lines:
                old_lines.unlink()
            payslips = self.env['hr.payslip'].search(
                [('date_from', '<=', advice.date), ('date_to', '>=', advice.date), ('state', '=', 'done')])
            for slip in payslips:
                if not slip.employee_id.bank_account_id and not slip.employee_id.bank_account_id.acc_number:
                    raise UserError(_('Please define bank account for the %s employee') % (slip.employee_id.name,))
                payslip_line = self.env['hr.payslip.line'].search([('slip_id', '=', slip.id), ('code', '=', 'NET')],
                                                                  limit=1)
                if payslip_line:
                    self.env['hr.payroll.advice.line'].create({
                        'advice_id': advice.id,
                        'name': slip.employee_id.bank_account_id.acc_number,
                        'employee_id': slip.employee_id.id,
                        'bysal': payslip_line.total
                    })
                slip.advice_id = advice.id

    def confirm_sheet(self):
        """
        confirm Advice - confirmed Advice after computing Advice Lines..
        """
        for advice in self:
            if not advice.line_ids:
                raise UserError(_('You can not confirm Payment advice without advice lines.'))
            date = fields.Date.from_string(fields.Date.today())
            advice_year = date.strftime('%m') + '-' + date.strftime('%Y')
            number = self.env['ir.sequence'].next_by_code('payment.advice')
            advice.write({
                'number': 'PAY' + '/' + advice_year + '/' + number,
                'state': 'confirm',
            })

   # def action_send_advice(self):
   #     """ Action to send Advice through Email."""
   #     self.ensure_one()
    #    template = self.env.ref('l10n_ma_hr_payroll.email_template_bank_advice')
    #    if template:
    #        self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)

    def set_to_draft(self):
        """Resets Advice as draft.
        """
        self.write({'state': 'draft'})

    def cancel_sheet(self):
        """Marks Advice as cancelled.
        """
        self.write({'state': 'cancel'})

    def _onchange_company_id(self):
        self.bank_id = self.company_id.partner_id.bank_ids and self.company_id.partner_id.bank_ids[
            0].bank_id.id or False


class HrPayrollAdviceLine(models.Model):
        '''
        Bank Advice Lines
        '''
        _name = 'hr.payroll.advice.line'
        _description = 'Bank Advice Lines'

        advice_id = fields.Many2one('hr.payroll.advice', string='Bank Advice')
        name = fields.Char('Bank Account No.', required=True)
        employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
        bysal = fields.Float(string='By Salary', digits=dp.get_precision('Payroll'))
        debit_credit = fields.Char(string='C/D', default='C')
        company_id = fields.Many2one('res.company', related='advice_id.company_id', string='Company', store=True,
                                     readonly=False)

class HrPayslip(models.Model):
    '''
    Employee Pay Slip
    '''
    _inherit = 'hr.payslip'
    _description = 'Pay Slips'

    advice_id = fields.Many2one('hr.payroll.advice', string='Bank Advice', copy=False)