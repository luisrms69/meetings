import frappe

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meeting", meeting)
    meeting.check_permission("email")

    if meeting.status == "Planeada":
        frappe.sendmail(
            recipients=[d.attendee for d in meeting.attendees],
            sender=frappe.session.user,
            subject=meeting.asunto,
            message=meeting.invitation_message,
            as_markdown=True
        )

        meeting.status = "Invitaciones Enviadas"
        meeting.save()

        frappe.msgprint("Invitaciones han sido enviadas")

    else:
        frappe.msgprint("No se pudieron enviar los correos, el estado de la reuni{on debe cambiarse a Planeadad")