# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StudentDetails(models.Model):
	_name = "student.details"
	_description = "Student Details"

	name = fields.Char(string='Name')
	address = fields.Text(string='Address')
	age = fields.Integer(string='Age')
	standard = fields.Many2one('school.standard', string='Standard')
	allow = fields.Boolean(string='Result', readonly=True)
	
	
	@api.onchange('standard')
	def onchange_standard(self):
		if self.standard.age_limit != self.age :
			raise UserError(_('%s is not eligible' % self.name) )