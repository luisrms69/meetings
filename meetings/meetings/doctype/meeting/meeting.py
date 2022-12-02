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

	def on_update(self):
		self.sync_todos()

	def sync_todos(self):
		"""Sync ToDos for assignments"""
		todos_added = [todo.name for todo in
			frappe.db.get_all("ToDo",
				filters={
					"reference_type": self.doctype,
					"reference_name": self.name,
					"assigned_by": ""
				})
			]

		for minute in self.minutes:
			if minute.assigned_to and minute.status=="Abierto":
				if not minute.todo:
					todo = frappe.get_doc({
						"doctype": "ToDo",
						"description": minute.description,
						"reference_type": self.doctype,
						"reference_name": self.name,
						"owner": minute.assigned_to
					})
					todo.insert()

					minute.db_set("todo", todo.name, update_modified=False)

				else:
					todos_added.remove(minute.todo)

			else:
				minute.db_set("todo", None, update_modified=False)

		for todo in todos_added:
			# remove closed or old todos
			todo = frappe.get_doc("ToDo", todo)
			todo.flags.from_meeting = True
			todo.delete()	
























@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)
	
	# Concatenates by space if it has value
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))