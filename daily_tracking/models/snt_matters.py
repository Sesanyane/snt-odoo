from odoo import api, fields, models


class Matter(models.Model):      
    _name = "snt.matter"

    _description = "Matter"

   

    _rec_name = "matter_no"

    matter_no = fields.Char(

    )

    tracker_id =  fields.One2many("snt.daily.tracker",
                                "matter_ids", string="Daily tracker")