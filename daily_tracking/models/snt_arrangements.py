from pydoc import doc
from odoo import api, fields, models
from datetime import date
import xml.etree.ElementTree as etree

class Arrangements(models.Model):
    _name = "snt.arrangements"
    _description = "Client Arrengements"
    _rec_name = "matter_id"
    _sql_constraints = [
        ("arrangement_unique", "CHECK(1==1)", 'Status cannot be repeated in an arrangement '),

        ("check_previous_date", "CHECK(amount > 1)", "The expected "
                                                              "price must be"
                                                              " strictly "
                                                              "positive"),
    ]

    today = date.today()

    client = fields.Char(string='Client',compute="update_value",
    )

    balance = fields.Float(string='Outstanding Balance',compute="update_balance",
    )
    amount = fields.Float("Expected Amount",
        required=True
    )
    ptp_expected_date = fields.Date( required=True,

    )

    arrangements_id = fields.Many2one("snt.arrangements", string="Arrangements",
                                  )

    arrangement_ids = fields.One2many("snt.arrangements",
                                "matter_id", string="Arrangemnts")
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("paid", "Paid"),
            ("partially", "Partially"),
            ("broken", "Broken"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )

    ptp_type = fields.Selection(
        selection=[
            ("settlement", "Settlement"),
            ("monthly", "Monthly"),
            ("once_off", "Once Off"),
        ],
        string="PTP Type",
        required=True,
        copy=False,
        default="once_off",

    )
# Relational
    user_id = fields.Many2one("res.users", string="Agent",readonly=True,
                              default=lambda self: self.env.user)

    matter_id = fields.Many2one("snt.matter",string="Matter Number",required=True
    )
    @api.depends('matter_id')
    def update_value(self):
        for rec in self:
            rec.client = rec.matter_id.book_id.client_id.name
            return rec

    @api.depends('matter_id')
    def update_balance(self):
        for rec in self:
            rec.balance = rec.matter_id.outstanding_balance
            return rec
    # @api.model
    # def fields_view_get(self,view_id=None,view_type='form',toolbar=False,submenu=False):
    #     res =super(Arrangements,self).fields_view_get(view_id=view_id,view_type=view_type,toolbar=toolbar,submenu=submenu)
    #     if view_type=="form":
    #         doc= etree.XML(res['arch'])
    #         for node in doc.xpath("//field[@name='ptp_expected_date']"):
    #             node.set('options',"{'datepicker':{'minDate':'%sT23:59:59'}}"% fields.Date.today().strftime(DEFAULT_SERVER_DATE_FORMAT))
    #         res['arch'] = etree.tostring(doc)
    #     return res     
                       