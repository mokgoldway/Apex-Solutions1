# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.model
    def _default_company_license_id(self):
        return self.env.user.company_id.default_license_id.id \
                    if self.env.user.company_id.default_license_id \
                    else False

    license_partner = fields.Boolean(related='partner_id.license_partner', string="Licensed Partner")

    company_license_id = fields.Many2one(comodel_name='metrc.license', string="Company License",
                                            default=_default_company_license_id,
                                            domain='[("base_type", "=", "Internal")]',
                                            readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                            index=True, track_visibility='always')
    customer_license_id = fields.Many2one(comodel_name='metrc.license', string="Customer License",
                                            domain='[("base_type", "=", "External")]',
                                            readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
                                            index=True, track_visibility='always')


    @api.multi
    def action_confirm(self):
        result = super(SaleOrder, self).action_confirm()
        for order in self:
            for pick in order.picking_ids.filtered(lambda sp: sp.state not in ('done', 'cancel')):
                if not pick.company_license_id:
                    pick.company_license_id = order.company_license_id
                if not pick.customer_license_id:
                    pick.customer_license_id = order.customer_license_id
        return result

    @api.onchange('company_id')
    def onchange_company_id(self):
        self.company_license_id = self.company_id.default_license_id \
                                    if self.company_id and self.company_id.default_license_id \
                                    else False

    @api.onchange('warehouse_id')
    def onchange_warehouse_id(self):
        self.company_license_id = self.warehouse_id.company_id.default_license_id \
                                    if self.warehouse_id and self.warehouse_id.company_id.default_license_id \
                                    else False


    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(SaleOrder, self).onchange_partner_id()
        self.customer_license_id = False
        return res
