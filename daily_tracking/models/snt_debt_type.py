from odoo import fields, models


class DebtType(models.Model):
    # ------------------------------ Private Attributes -----------------------
    _inherit = ['mail.thread','mail.activity.mixin']
    _name = "snt.debt.type"
    _description = "Debt Type"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # ------------------------------- Fields Declaration ---------------------

    # Basic
    name = fields.Char(string="Name", required=True,track_visibility='onchange')
    description = fields.Text(string="Description",track_visibility='onchange')