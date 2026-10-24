"""Product knowledge used by the lead sentinel.

Facts here are re-derived from the EHR-Cloud- source repo (README, docs/support/*.md,
INSTALLED_APPS, URL routes, models). Anything not found in that repo is deliberately
absent -- do not add pricing, customer counts, pilot status, compliance certifications,
uptime, hosting location or go-live status without a real source.
"""

# ASSUMPTION (inferred, not stated): the intended audience is Nigerian clinics and
# hospitals. EHR-Cloud-'s README does not say this. It is inferred from the code:
# Organization.default_currency defaults to "NGN", SMS goes through Termii, and billing
# targets NHIS (Nigeria's national health insurance scheme). Confirm with the owner.
#
# Terminology: the source README calls the product an "HMIS"; by decision, use "EHR"
# throughout.

EHR_CLOUD_KNOWLEDGE = """\
PRODUCT: Mega-Net EHR Cloud

WHAT IT IS
A cloud-hosted, multi-tenant EHR that lets a single clinic or a multi-facility hospital
network run patient records, scheduling, billing/claims, lab, pharmacy and inventory from
one platform. Built as a modular monolith (Django + PostgreSQL). Access is role-based and
scoped per facility. Billing is aimed at NHIS (capitation and fee-for-service, with
configurable HMO tariffs).

CONFIRMED MODULES (built, present in the code)
- Patient Registry / Front Office: patient registration, medical record numbers, next of
  kin, patient record corrections.
- Scheduling: appointments (book, confirm, check in, complete).
- Service Queue: patient queue management.
- Billing: invoices, line items, payments, voiding an invoice, insurance claims, payers,
  corporate coverage, tariff codes.
- Lab: test orders, specimens, result entry and verification, result flagging.
- Radiology: imaging orders, studies, reports with verification, critical-finding
  alerts and acknowledgement.
- Pharmacy: prescriptions and dispensing, drug list.
- Inventory: items, suppliers, purchase orders, stock movements, reorder-level list.
- Admissions / Ward Management.
- Inpatient Nursing (including shift handovers).
- Surgery: procedure catalog and surgery scheduling.
- Antenatal Care (ANC).
- Staff Messaging: internal direct and department-routed messages.
- Announcements: one-way in-app notices from Org Admins to staff.
- Documents: attach documents to patients, encounters, invoices, claims and similar records.
- Reporting / Business Insights: reports, scheduled reports, data export with an export log.
- Financial Sentinel: analysis runs that produce findings for billing/finance staff.
- Support tickets: in-app channel to Mega-Net support.
- Help center: help articles.
- Staff management and security: organizations, facilities, users, role memberships,
  audit logging, multi-factor authentication (MFA), Postgres row-level security for
  tenant isolation.
- A React front end is being built alongside the server-rendered screens (the repo is
  mid-migration).

AVAILABLE, MAY REQUIRE ENABLING PER CLIENT
These are built but are gated by configuration or per-organization settings. Do not
state they are active for every client.
- Public Booking: a public appointment-booking page per facility (/book/<org>/<facility>/)
  with CAPTCHA and throttling. Available, may require enabling per client.
- SMS notifications: patient SMS (appointment reminders, lab-results-ready alerts, bulk
  campaigns) through a third-party gateway (Termii), with an org credit balance.
  Available, may require enabling per client (gateway config and credits; appointment
  reminders are off by default per organization).
- Critical-finding SMS escalation (Radiology) for staff alerts. Available, may require
  enabling (needs an SMS provider configured).
- Image file upload for Radiology studies. Available, may require enabling per client
  (needs object storage configured).

ROLES (system roles in the code)
Super Admin (Mega-Net platform level), Org Admin, Physician/Clinician, Nurse, Front
Desk/Registration, Billing Clerk, Lab Technician, Pharmacist, Inventory Manager.

STAFF ROLES REQUIRING MANDATORY MFA (authoritative, from the code)
Six roles: Org Admin, Physician, Billing Clerk, Lab Technician, Inventory Manager,
Pharmacist. Mega-Net platform staff accounts also always require MFA. Nurse and Front
Desk do not require it. (Some support docs state different counts; they are out of date.)

NOT YET BUILT / KNOWN GAPS
- Billing: no way to correct or remove a single line item on an issued invoice. The only
  fix is to void the whole invoice and create a new one.
- Inventory: no automatic low-stock notifications; a low item is only visible when
  someone opens the reorder list.
- Radiology: orders can't be moved to scheduled, in-progress or cancelled; those states
  exist but nothing sets them.
- Lab: specimen barcode scanning is not wired into any screen.
- Scheduled background jobs: no worker queue is deployed yet, so some timed behaviour
  (e.g. critical-finding escalation delay) runs immediately instead of after a delay.
- Custom roles: roles are system-defined; org-defined custom roles are a later phase.
- Staff SMS provider for critical-finding alerts and object storage are not chosen/
  configured by default.

DO NOT CLAIM (no source in the repo)
Pricing, customer counts, pilot status, compliance certifications, uptime, hosting
location, go-live status.
"""
