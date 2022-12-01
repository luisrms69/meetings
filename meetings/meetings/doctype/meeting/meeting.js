// Copyright (c) 2022, Buzola and contributors
// For license information, please see license.txt

/*
frappe.ui.form.on('Meeting Attendees', {
	attendee: function(frm, cdt, cdn){
		var attendee = frappe.model.get_doc(cdt, cdn);
		if (attendee.attendee) {
			//if attendee, get full name
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
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
	},
});
*/

frappe.ui.form.on("Meeting Attendee", {
	attendee: function(frm, cdt, cdn) {
		var attendee = frappe.model.get_doc(cdt, cdn);
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
 	},
});


frappe.ui.form.on('Meetings', {
	send_emails: function(frm) {
		if(frm.doc.status==="Planeada") {
			frappe.call({
				method: "meeting.api.send_invitation_emails",
				args: {
					meeting: frm.doc.name
				}
			});
		}
	},
});