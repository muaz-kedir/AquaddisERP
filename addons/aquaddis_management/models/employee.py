from odoo import models, fields


class AquaddisEmployee(models.Model):
    _name = 'aquaddis.employee'
    _description = 'AQUADDIS Employee'

    name = fields.Char(string='Employee Name', required=True)

    email = fields.Char(string='Email')

    phone = fields.Char(string='Phone Number')

    age = fields.Integer(string='Age')

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender'
    )

    active = fields.Boolean(default=True)
