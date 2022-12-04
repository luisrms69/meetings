// Copyright (c) 2022, Buzola and contributors
// For license information, please see license.txt


frappe.ui.form.on('Meeting', {
	send_emails(frm) {
		if(frm.doc.status==="Planeada") {
			frappe.call({
				method: "meetings.api.send_invitation_emails",
				args: {
					meeting: frm.doc.name
				}
			});
		}
	},


/* Esto lo estare haciendo porsteriormente para que se actualicen los valores en tiempo real
	sala(frm) {
		var sala_js = frappe.model.get_doc(frm)
		if (sala_js) {
			// Si la sala esta definida
			frappe.call({
				method: "meetings.meetings.doctype.meeting.meeting.get_service_list",
				args: {
					meeting_room: sala_js
				},
				callback: function(r) {
					frappe.model.set_value("servicios_de_la_sala", r.message);
				}
			});

		} else {
			// Si no hay sala
			frappe.model.set_value("servicios_de_la_sala", null);
		}
	}

*/


});


frappe.ui.form.on("Meeting Attendees", {
	attendee(frm, cdt, cdn) {
		var attendee = frappe.model.get_doc(cdt, cdn)
		if (attendee.attendee) {
			// if attendee, get full name
			frappe.call({
				method: "meetings.meetings.doctype.meeting.meeting.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "full_name", r.message);
				}
			});

		} else {
			// if no attendee, clear full name
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
	}
});
