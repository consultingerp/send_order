# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class pos_config(models.Model):
    _inherit = "pos.config"


    @api.model
    def _default_bus_id(self):
        try:
            return self.env.ref('send_order.pos_bus_store_default')
        except:
            pass

    send_pos_orders = fields.Boolean('Send pos orders', default=0)
    search_pos_orders = fields.Boolean('Search pos orders sent', default=0)
    prohibit_payment = fields.Boolean('Prohibit payment', default=0)
    print_shipment_ticket = fields.Boolean('Print shipment ticket', default=0)

    bus_id = fields.Many2one('pos.bus', string='Server',
    default= _default_bus_id )

  