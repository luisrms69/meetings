# Copyright (c) 2022, Buzola and contributors
# For license information, please see license.txt

# from __future__ import unicode_literals
# import frappe
#from __future__ import unicode_literals
import frappe
#from frappe import _
from frappe.model.document import Document

class Meeting(Document):
	@frappe.whitelist()
	def before_save(self):
		frappe.throw(
    title='Error',
    msg='a que pendejo',
    exc=FileNotFoundError
)
#		frappe.throw(("Person's age must be at least 18"))
#		found = []
#		for attendee in self.attendees:
#			if attendee.attendee in found:
#				frappe.throw(_("Attendee {0} entered twice").format(attendee.attendee))
			
#			found.append(attendee.attendee)

#		"""Set missing names"""
#		for attendee in self.attendees:
#			if not attendee.full_name:
#				attendee.full_name = get_full_name(attendee.attendee)

#def get_full_name(attendee):
#	user = frappe.get_doc("User", attendee)

	# Concatenates by space if it has value
#	return attendee.full_name = " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))