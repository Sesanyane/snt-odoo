from odoo import fields, models


class Payments(models.Model):
    _name = "snt.payments"

    _description = "Payments"


    matter_id = fields.Many2one("snt.matter",string="Matter Number"
    )
    account_no = fields.Integer(

    )
    date_paid = fields.Date(

    )


    confirmed_by = fields.Many2one("res.partner", string="Client",
                               readonly=True, copy=False)

    agent = fields.Many2one("res.users", string="Agent",
                              default=lambda self: self.env.user)

    location_paid = fields.Char(

    )

    amount_paid = fields.Float(

    )

    pop = fields.Binary(
        string="Proof of Payment"
    )

    paid_at = fields.Selection(
        selection=[
            ("client", "Client"),
            ("firm", "Firm"),
        ],
        string="Paid At",
        copy=False,
        default="client",
    )

    state = fields.Selection(
        selection=[
            ("request_confirmation", "Request For  confirmation"),
            ("sent_to_client", "Sent to Client"),
            ("paid", "Paid"),
            ("not_paid", "Not Paid"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    def action_sold(self):
        if "confirmed" in self.mapped("state"):
            raise UserError("confirmed property!!!!!!.")
        return self.write({"state": "confirmed"})

  
