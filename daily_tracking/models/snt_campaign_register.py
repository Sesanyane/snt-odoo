from odoo import api, fields, models


class CampaignRegister(models.Model):
    _name = "snt.campaign.register"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Campaign Register"
    # _rec_name = "campaign_no"

# _sql_constraints = [
    #     ("check_expected_price", "CHECK(outstanding_balance > 0)", "The expected "
    #                                                           "price must be"
    #                                                           " strictly "
    #                                                           "positive"),
    #     ("check_selling_price", "CHECK(selling_price >= 0)", "The offer "
    #                                                          "price must be "
    #                                                          "positive"),
    # ]
    name = fields.Char(

    )
    # campaign_no = fields.Char(string='Campaign Number', required=True,
    #                       readonly=True, default=lambda self: _('New'))

    date_requested = fields.Date(

    )

    req_run_date = fields.Date(

    )

    req_by = fields.Date(

    )

    start_date = fields.Date(

    )

    end_date = fields.Date(

    )

    agent = fields.Many2many("res.users", string="Agent",
                             )
    criteria = fields.Many2many("snt.criteria", string="Criteria",
                                )
    book_id = fields.Many2one("snt.book", string="Book",
                              required=True)

    @api.model
    def create(self, vals):
        if vals.get('campaign_no', _('New')) == _('New'):
            vals['campaign_no'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient') or _('New')
            res = super(CampaignRegister, self).create(vals)
        return res
