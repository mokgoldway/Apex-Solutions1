# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    @api.model
    def _default_company_license_id(self):
        return self.env.user.company_id.default_license_id.id \
                    if self.env.user.company_id.default_license_id \
                    else False

    license_partner = fields.Boolean(related='partner_id.license_partner', string='Licensed Partner')

    company_license_id = fields.Many2one(comodel_name='metrc.license', string='Company License',
                                            default=_default_company_license_id,
                                            domain='[("base_type", "=", "Internal")]',
                                            ondelete='restrict', copy=False,  index=True,
                                            states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    customer_license_id = fields.Many2one(comodel_name='metrc.license', string='Customer License',
                                            domain='[("base_type", "=", "External")]',
                                            ondelete='restrict', copy=False,  index=True,
                                            states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    driver_id = fields.Many2one(comodel_name='res.partner', string='Driver',
                                            domain='[("driver", "=", True)]',
                                            ondelete='restrict', copy=False,  index=True,
                                            states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})

    @api.onchange('company_id')
    def onchange_company_id(self):
        self.company_license_id = self.company_id.default_license_id \
                                    if self.company_id and self.company_id.default_license_id \
                                    else False

    @api.onchange('picking_type_id')
    def onchange_warehouse_id(self):
        self.company_license_id = self.picking_type_id.warehouse_id.company_id.default_license_id \
                                    if self.picking_type_id and self.picking_type_id.warehouse_id \
                                            and self.picking_type_id.warehouse_id.company_id.default_license_id \
                                    else False

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.customer_license_id = self.group_id.sale_id.customer_license_id if self.group_id and self.group_id.sale_id else False
