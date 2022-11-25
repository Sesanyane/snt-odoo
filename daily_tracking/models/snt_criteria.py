from odoo import fields, models


class Criteria(models.Model):
    # ------------------------------ Private Attributes -----------------------

    _name = "snt.criteria"
    _description = "Criteria"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]

    # ------------------------------- Fields Declaration ---------------------

    # Basic
    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")
