import string
from odoo import fields, models


class Books(models.Model):
    _name = "snt.book"

    _description = "Test Model"

    name = fields.Char(
        string='Book Name',
    )
    instuction_fee = fields.Integer(
        string="Instruction Fee",
    )
    commision = fields.Float(

    )

    out_standing_balance = fields.Float(

    )
    client_id = fields.Many2one("snt.client", string="Client",
                                required=True)

    matter_ids = fields.One2many("snt.matter",
                                 "book_id", string="Matters")

    campaign_ids = fields.One2many("snt.campaign.register",
                                   "book_id", string="Matters")
