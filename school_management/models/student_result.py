# -*- coding: utf-8 -*-

from odoo import api, fields, models

class StudentResult(models.Model):
	_name = "student.result"
	_description = "Student Result"

	student_id = fields.Many2one('student.details', string='Student')
	standard_id = fields.Many2one('school.standard', string='Standard')


	@api.model
	def create(self, vals):
		self = super(StudentResult, self).create(vals)
		print("VALS :::: ", vals)
		print("SELF :::: ", self)
		student = self.env['student.details'].search([('id', '=', vals['student_id'])])
		print("STUDENT :: ", student)
		student.write({'allow': True})
		return self

