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

			if not attendee.full_name:
				attendee.full_name = get_full_name(attendee.attendee)

@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)
	
	# Concatenates by space if it has value
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))