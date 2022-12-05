from odoo import fields, models


class Client(models.Model):
    _name = "snt.client"

    _description = "Client"

    _sql_constraints = [
        ('name', 'unique (name)', 'The name already Exists!'),
    ]

    name = fields.Char(
        string='Client',
    )

    out_standing_balance = fields.Float(

    )
    # Relational
    book_ids = fields.One2many("snt.book",
                               "client_id", string="Books")
    # matter_ids = fields.One2many("snt.matter",
    #                             "book_id", string="Matters")

# TODO oustannding balance for all books,book value(capital)
