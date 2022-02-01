from odoo import fields, models


class artists(models.Model):
    _name = 'musicstore.artists'
    _description = 'Artists'
    dni = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    surname = fields.Char('Surname')
    second_surname = fields.Char('Second Surname')
    tlf = fields.Char('Phone')
    email = fields.Char('Email')
