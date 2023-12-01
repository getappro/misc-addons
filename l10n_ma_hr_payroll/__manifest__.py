# -*- coding: utf-8 -*-
##############################################################################
#
#    GetapPRO SARL
#    Copyright (C) 2019-TODAY GetapPRO(<http://www.getap.pro>).
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Moroccan Payroll',
    'summary': 'Moroccan Payroll for odoo 16',
    'version': '16.0.2.0.0',
    'category': 'Human Resources',
    'author':'GetapPRO',
    'maintainer': 'GetapPRO',
    'website': 'http://www.getap.pro',
    'license': 'AGPL-3',
    'depends': ['base', 'hr','hr_payroll_community'],
    'data': [
        'views/l10n_ma_hr_payroll_views.xml',
        'views/res_company_views.xml',
        'views/hr_employee_view.xml',
        'views/hr_contract.xml',
        'security/ir.model.access.csv',
        'reports/l10n_ma_payroll_reports.xml',
        'reports/report_payslip_template.xml',
        'reports/report_payment_advice_template.xml',
        'data/l10n_ma_hr_payroll_data.xml',
        'data/l10n_ma_hr_payroll_sequence_data.xml',
        #'data/mail_template_data.xml',
    ],
    'application': True,
    'images': ['static/description/poster_image.png'],
}