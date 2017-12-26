# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SchoolStandard(models.Model):
	_name = "school.standard"
	_description = "School Standard"

	name = fields.Char(string='Name')
	code = fields.Integer(string='Code')
	student_ids = fields.One2many('student.details', 'standard', string='Students')
	age_limit = fields.Integer(string='Age Limit')
	