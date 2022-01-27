from odoo import fields, models


class recordCompany(models.Model):
    _name = 'musicstore.recordcompany'
    _description = 'Record Company'
    cod = fields.Char('Code', required=True)
    name = fields.Char(
        'Name',
        required=True
    )
    address = fields.Char();
    tlf = fields.Char('Phone')
