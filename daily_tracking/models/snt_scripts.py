from odoo import fields, models


class Scripts(models.Model):
    _name = "snt.scripts"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Scripts"

    _sql_constraints = [
        ('name', 'unique (name)', 'The name already Exists!'),
    ]

    name = fields.Char(
        
    )

    script =fields.Text(

    )
