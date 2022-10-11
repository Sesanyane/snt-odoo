from datetime import date
from odoo import api, fields, models


class DailyTracker(models.Model):
    _name = "snt.daily.tracker"
    _inherit =['mail.thread','mail.activity.mixin']
    _description = "Daily Tracker"
    _rec_name = "matter_ids"


    user_id = fields.Many2one("res.users", string="Agent",readonly=True,
                              default=lambda self: self.env.user)

   
    status = fields.Selection(
        selection=[
            ("attempting_ptp", "Attempting PTP"),
            ("back_from_trace", "Back From Trace"),
            ("broken_ptp", "Broken PTP"),
            ("confirmed", "Confirmed"),
            ("deceased", "Deceased"),
            ("dispute", "Dispute"),
            ("follow_up_ptp", "Follow-up PTP"),
            ("in_progress", "In Progress"),
            ("internal_trace", "Internal Trace"),
            ("new_instruction", "New Istruction"),
            ("on_hold", "On Hold"),
            ("payment_arrangement", "Payment Arrangement"),
            ("potential_ptp", "Potential PTP"),
            ("query", "Query"),
            ("recalled", "Recalled"),
            ("re_opened", "Re-opened"),
            ("request_closure", "Request For Closure"),
        ],
        string="Status",
        required=True,
        copy=False,
        tracking=True
    )
    wrap_up = fields.Selection(
         selection=[
            ('awaiting_pop','Awaiting POP (With SMS & Email)'),
            ('awaiting_statement','Awaiting Statement'),
            ('balance_supplied','Balance supplied'),
            ('call_customer_later','Call customer later'),
            ('call_ended','Call ended'),
            ('customer_deceased','Customer deceased'),
            ('customer_emigrated','Customer emigrated'),
            ('engaged','Engaged'),
            ('invalid_number','Invalid Number'),
            ('left_message','Left Message'),
            ('no_answer','No Answer'),
            ('none','None'),
            ('payment_arrangement','Payment Arrangement'),
            ('payment_plan_sent','Payment Plan sent'),
            ('sequestrated','Sequestrated'),
            ('under_administration','Under Administration'),
        ],
        string="Wrap-up Selected",
        required=True,
        copy=False,
        tracking=True

    )

    ptp_date= fields.Date(tracking=True,
        
    )

    ptp_amount= fields.Float(tracking=True,
        
    )

    last_paid_date= fields.Date(tracking=True,
        
    )

    last_paid_amount= fields.Float(tracking=True,
        
    )

    source_of_income = fields.Char(tracking=True
        
    )

    employer_name= fields.Char(tracking=True
        
    )

    debtor= fields.Char(tracking=True,readonly=True,compute="update_value"
        
    )

    payment_trust= fields.Selection(
        selection=[
            ('firm','Firm'),
            ('client','Client'),],
            copy=False,
            default="firm",
            tracking=True
    )

    comments = fields.Text(
        tracking=True
    )


    matter_ids = fields.Many2one("snt.matter",string="Matter Number",required=True
    )

    @api.depends('matter_ids')
    def update_value(self):
        for rec in self:
            rec.debtor = rec.matter_ids.debtor
            return rec