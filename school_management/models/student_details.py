# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StudentDetails(models.Model):
	_name = "student.details"
	_description = "Student Details"


	name = fields.Char(string='Name', required=True)
	address = fields.Text(string='Address')
	age = fields.Integer(string='Age')
	standard = fields.Selection(
		[
			('1', '1'), 
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
		])
