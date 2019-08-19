# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from ast import literal_eval

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    license_ids = fields.One2many(
        comodel_name='metrc.license', inverse_name='partner_id',
        string='Licenses')
    license_partner = fields.Boolean(string='Cannabis Licensed Contact')
    license_count = fields.Integer(compute='_compute_license_count', string="License Count")

    @api.depends('license_ids')
    def _compute_license_count(self):
        for partner in self:
            partner.license_count = len(partner.license_ids) + len(partner.child_ids.mapped('license_ids'))

    @api.multi
    def action_view_partner_licenses(self):
        self.ensure_one()
        action = self.env.ref('metrc.action_view_metrc_license').read()[0]
        action['domain'] = literal_eval(action['domain'])
        action['domain'].append(('partner_id', 'child_of', self.id))
        return action
