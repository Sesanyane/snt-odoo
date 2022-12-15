from odoo import api, fields, models

class Book(models.Model):

    _name = 'snt.book'

    _inherit = ['mail.thread','mail.activity.mixin']




    name = fields.Char(required=True, string="Book Name",track_visibility='onchange')

    client_id = fields.Many2one(

        "res.partner",

        string="Client",

        track_visibility='onchange',

        required=True,
        domain=[('is_company', '=', True)]

    )

   

    ## ----------------------------------------Basic Settings--------------------------------------

    instruction_received = fields.Date(track_visibility='onchange')

    instruction_fee = fields.Float(track_visibility='onchange')

    collection_commission = fields.Float(track_visibility='onchange')

    ptp_offset = fields.Float(track_visibility='onchange')

    matter_prefix = fields.Char(track_visibility='onchange') ## Attach to ir.sequence

    book_seq = fields.Char()

    ##------------------------------------------Book Stats---------------------------------------

    matter_ids = fields.One2many(
        "snt.matter",
        "book_id", string="Matters",
        track_visibility='onchange'
        )

    payment_ids = fields.Char(track_visibility='onchange')

    arrangement_ids = fields.Char(track_visibility='onchange')



    # --------------------------------------------Other Fields------------------------------------

    book_value = fields.Float(track_visibility='onchange')

    outstanding_value = fields.Float(track_visibility='onchange')

    amount_collected = fields.Float(track_visibility='onchange')

   # --------------------------------------------functions------------------------------------ 

    def action_show_matters(self):

        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": "Matters",
            "view_mode": "tree,form",
            "res_model": "snt.matter",
            "domain": [("book_id", "=", self.id)],
            "context": {'create': True,'default_book_id':self.id},

        }

    def action_show_arrangements(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Payments",
            "view_mode": "tree,form",
            "res_model": "snt.arrangements",
            "domain": [("matter_id", "=", self.id)],
            "context": {'create': False},
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
   
    @api.model
    def create(self, vals):

        book_seq = self.env['ir.sequence'].create({
            'name':vals['name'],
            'implementation':'standard',
            'code':vals['matter_prefix'],
            'prefix': vals['matter_prefix'],
            'padding':10,
            'number_increment':1,
            #'next_number':0
            })   

        vals['matter_prefix'] = book_seq.code
        
        # Update ccustomer to include is_a_collection_client

        return super(Book, self).create(vals)