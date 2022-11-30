# Copyright (c) 2022, Buzola and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		found = []
		for attendee in self.attendees:
			if attendee.attendee in found:
				frappe.throw(("El invitado {0} esta duplicado").format(attendee.attendee))
			
			found.append(attendee.attendee)
