# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StudentDetails(models.Model):
	_inherit = 'res.partner'
	
	is_student = fields.Boolean(string="Is Student")
	age = fields.Integer(string='Age')
	standard = fields.Many2one('res.partner', string='Student', domain=[('is_student', '=', True)])
	allow = fields.Boolean(string='Result', readonly=True)
	sport_ids = fields.Many2many('sports', string="Sports")


class Sports(models.Model):
	_name="sports"

	name= fields.Char("Name")


	# @api.onchange('standard')
	# def onchange_standard(self):
	# 	if self.standard.age_limit != self.age :
	# 		raise UserError(_('%s is not eligible' % self.name) )
