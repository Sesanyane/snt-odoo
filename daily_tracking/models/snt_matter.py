from odoo import api, fields, models


class Matter(models.Model):      
    _name = "snt.matter"

    _description = "Matter"

    _rec_name = "matter_no"

    _sql_constraints = [
        ("check_expected_price", "CHECK(outstanding_balance > 0)", "The expected "
                                                              "price must be"
                                                              " strictly "
                                                              "positive"),
        ("check_selling_price", "CHECK(selling_price >= 0)", "The offer "
                                                             "price must be "
                                                             "positive"),
    ]

    matter_no = fields.Char(

    )
    outstanding_balance = fields.Float(

    )
    book_id = fields.Many2one("snt.book", string="Book",
                                  required=True)

    arrangement_ids = fields.One2many("snt.arrangements",
                                "matter_id", string="Arrangemnts")
    payments_ids = fields.One2many("snt.payments",
                                "matter_id", string="Payments")

    last_date_paid = fields.Date(compute="_compute_last_date_paid"

    )
    amount_paid = fields.Float( compute='payment_details'

    )
    last_paid_agent = fields.Char(compute="_compute_last_paid_agent"

    )

    debtor= fields.Char(tracking=True,readonly=True,
        
    )

    ptp_expected_date = fields.Date(compute="_compute_ptp_expected_date"

    )
    ptp_amount = fields.Float(compute="_compute_last_ptp_amount"

    )
    ptp_agent = fields.Char(compute="_compute_last_ptp_agent"

    )
    arrangements_count = fields.Integer(compute="_compute_arrangements_count")

    arrangement_count = fields.Integer(compute="_compute_arrangement_count")

    payments_count = fields.Integer(compute="_compute_payments_count")

    tracker_id =  fields.One2many("snt.daily.tracker",
                                "matter_ids", string="Daily tracker")

    # Computed
    total_ptp_amount = fields.Float(
        "Sum of Expected Payment Amount",
        compute="_compute_total_ptp_amont",
        help="Total area computed by summing all oustanding ptp amount",
    )

    def _compute_arrangement_count(self):
        totalArrangmenets = self.env['snt.matter.arrangemt_ids']


    def _compute_arrangements_count(self):
        for record in self:
            record.arrangements_count = len(self.arrangement_ids)

    def _compute_payments_count(self):
        for record in self:
            record.payments_count = len(self.payments_ids)
	
    @api.depends("outstanding_balance")
    def _compute_total_ptp_amont(self):
        for prop in self:
            prop.total_area = sum(prop.outstanding_balance)

    def action_show_arrangements(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Arrangements",
            "view_mode": "tree,form",
            "res_model": "snt.arrangements",
            "domain": [("matter_id", "=", self.id)],
            "context": "{'create': False}",
            }
    def action_show_payments(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Payments",
            "view_mode": "tree,form",
            "res_model": "snt.payments",
            "domain": [("matter_id", "=", self.id)],
            "context": "{'create': False}",
            }


    # @api.depends("payments_ids.date_paid")
    # def _compute_last_date_paid(self):
    #     for prop in self:
    #         prop.last_date_paid = max(prop.payments_ids.mapped("date_paid")) \
    #             if prop.payments_ids else 0.0


  
    def payment_details(self):
        for rec in self:
            rec.amount_paid = rec.env['snt.payments'].search([],order='date_paid desc')[0].amount_paid

    def _compute_last_date_paid(self):
        for rec in self:
            rec.last_date_paid = rec.env['snt.payments'].search([],order='date_paid desc ' )[0].date_paid 

    def _compute_last_paid_agent(self):
        for rec in self:
            rec.last_paid_agent = rec.env['snt.payments'].search([],order='date_paid desc')[0].agent.name      


    def _compute_ptp_expected_date(self):
        for rec in self:
            rec.ptp_expected_date = rec.env['snt.arrangements'].search([])[-1].ptp_expected_date

    def _compute_last_ptp_amount(self):
        for rec in self:
            rec.ptp_amount = rec.env['snt.arrangements'].search([] )[-1].amount

    def _compute_last_ptp_agent(self):
        for rec in self:
            rec.ptp_agent = rec.env['snt.arrangements'].search([])[-1].user_id.name  