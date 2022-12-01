import frappe

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meetings", meeting)
    meeting.check_permission("email")

    if meeting.status == "Planeada":
        frappe.sendmail(
            recipients=[d.attendee for d in meeting.attendees]
            sender=frappe.session.user,
            subject=meeting.title,
            message=meeting.invitation_message,
            reference_doctype=meeting.doctype,
            rerefence_name=meeting.name,
            as_bulk=True
        )

        meeting.status = "Invitaciones Enviadas"
        meeting.save()

        frappe.msgprint(_("Invitaciones han sido enviadas"))

    else:
        frappe.msgprint(_("No se pueden enviar invitaciones a la reunion, la etapa debe ser Planeada"))
