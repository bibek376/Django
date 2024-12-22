# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApprovalInstance(models.Model):
    id = models.IntegerField(primary_key=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    last_modified_by = models.IntegerField(blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approver_designation_id = models.IntegerField(blank=True, null=True)
    approver_designation_name = models.CharField(blank=True, null=True)
    approver_name = models.CharField(blank=True, null=True)
    approver_user_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(blank=True, null=True)
    instance_code = models.IntegerField(blank=True, null=True)
    issuer = models.CharField(blank=True, null=True)
    operator_designation_id = models.IntegerField(blank=True, null=True)
    operator_designation_name = models.CharField(blank=True, null=True)
    operator_name = models.CharField(blank=True, null=True)
    reviewed_date = models.DateField(blank=True, null=True)
    reviewer_designation_id = models.IntegerField(blank=True, null=True)
    reviewer_designation_name = models.CharField(blank=True, null=True)
    reviewer_name = models.CharField(blank=True, null=True)
    reviewer_user_id = models.IntegerField(blank=True, null=True)
    office = models.ForeignKey('Offices', models.DO_NOTHING, blank=True, null=True)
    process = models.ForeignKey('Processes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval_instance'



class CitizenshipApplicantForeignCitizenshipDetails(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    first_citizenship_country = models.ForeignKey('Countries', models.DO_NOTHING, db_column='first_citizenship_country', blank=True, null=True)
    citizenship_first_citizenship_status = models.CharField(max_length=255, blank=True, null=True)
    foreign_citizenship_issued_date = models.DateTimeField(blank=True, null=True)
    foreign_citizenship_issued_date_bs = models.CharField(max_length=255, blank=True, null=True)
    renounced_process_initiation_date = models.DateTimeField(blank=True, null=True)
    renounced_process_initiation_date_bs = models.CharField(max_length=255, blank=True, null=True)
    renunciation_proof_submission_date = models.DateTimeField(blank=True, null=True)
    renunciation_proof_submission_date_bs = models.CharField(max_length=255, blank=True, null=True)
    citizenship_application = models.ForeignKey('CitizenshipApplication', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_applicant_foreign_citizenship_details'


class CitizenshipApplicantIdentifierDetail(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    citizenship_no = models.CharField(max_length=255, blank=True, null=True)
    identifier_first_name = models.CharField(max_length=255, blank=True, null=True)
    identifier_last_name = models.CharField(max_length=255, blank=True, null=True)
    identifier_middle_name = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street_np = models.CharField(max_length=255, blank=True, null=True)
    ward_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    ctz_issued_district = models.ForeignKey('Districts', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)
    local_body = models.ForeignKey('LocalBodies', models.DO_NOTHING, blank=True, null=True)
    relationship_type = models.ForeignKey('RelationshipTypes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_applicant_identifier_detail'


class CitizenshipApplication(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    last_modified_by = models.IntegerField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birth_country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)
    citizenship_application_type = models.CharField(blank=True, null=True)
    citizenship_reference = models.CharField(blank=True, null=True)
    contact_no = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    first_name_np = models.CharField(blank=True, null=True)
    middle_name = models.CharField(blank=True, null=True)
    middle_name_np = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    last_name_np = models.CharField(blank=True, null=True)
    approval_detail = models.ForeignKey('CitizenshipApplicationApprovalDetails', models.DO_NOTHING, blank=True, null=True)
    applicant_identifier_detail = models.ForeignKey(CitizenshipApplicantIdentifierDetail, models.DO_NOTHING, blank=True, null=True)
    education = models.ForeignKey('EducationQualifications', models.DO_NOTHING, db_column='education', blank=True, null=True)
    gender = models.ForeignKey('Genders', models.DO_NOTHING, blank=True, null=True)
    occupation = models.ForeignKey('Occupations', models.DO_NOTHING, blank=True, null=True)
    religion = models.ForeignKey('Religions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_application'


class CitizenshipApplicationAddresses(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255)
    started_living_since_ad = models.DateTimeField(blank=True, null=True)
    started_living_since_bs = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street_np = models.CharField(max_length=255, blank=True, null=True)
    total_years = models.CharField(max_length=255, blank=True, null=True)
    ward_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    citizenship_application = models.ForeignKey(CitizenshipApplication, models.DO_NOTHING)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)
    local_body = models.ForeignKey('LocalBodies', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_application_addresses'


class CitizenshipApplicationApprovalDetails(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    designation_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    district_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    forwarding_office_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    recommend_date_ad = models.DateTimeField(blank=True, null=True)
    recommend_date_bs = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    ward_head_first_name_np = models.CharField(max_length=500, blank=True, null=True)
    ward_head_last_name_np = models.CharField(max_length=255, blank=True, null=True)
    ward_head_middle_name_np = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_application_approval_details'


class CitizenshipCopies(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    copy_number = models.DecimalField(max_digits=10, decimal_places=0)
    copy_reason = models.CharField(max_length=255)
    decision_date_ad = models.DateTimeField(blank=True, null=True)
    decision_date_bs = models.CharField(max_length=255, blank=True, null=True)
    file_number = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    tippani = models.TextField(blank=True, null=True)
    approval_detail = models.ForeignKey(CitizenshipApplicationApprovalDetails, models.DO_NOTHING, blank=True, null=True)
    applicant_identifier_detail = models.ForeignKey(CitizenshipApplicantIdentifierDetail, models.DO_NOTHING, blank=True, null=True)
    citizenship_number_generation = models.ForeignKey('CitizenshipNumberGenerations', models.DO_NOTHING, blank=True, null=True)
    system_generated = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    employee_as_family_detail = models.ForeignKey('CitizenshipEmployeeAsFamilyDetails', models.DO_NOTHING, blank=True, null=True)
    husband_detail_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    data_correction_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    issuer_designation_name = models.CharField(max_length=255, blank=True, null=True)
    issuer_name = models.CharField(max_length=255, blank=True, null=True)
    sanakhat_designation_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    sanakhat_employee_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_copies'


class CitizenshipEmployeeAsFamilyDetails(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    first_name_np = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_name_np = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name_np = models.CharField(max_length=255, blank=True, null=True)
    office_join_date = models.DateTimeField(blank=True, null=True)
    office_join_date_np = models.CharField(max_length=255, blank=True, null=True)
    office_name = models.CharField(max_length=255, blank=True, null=True)
    sanket_no = models.CharField(max_length=255)
    street_np = models.CharField(max_length=255, blank=True, null=True)
    ward_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    citizenship_application = models.ForeignKey(CitizenshipApplication, models.DO_NOTHING)
    designation = models.ForeignKey('Designations', models.DO_NOTHING, blank=True, null=True)
    district = models.ForeignKey('Districts', models.DO_NOTHING, blank=True, null=True)
    local_body = models.ForeignKey('LocalBodies', models.DO_NOTHING, blank=True, null=True)
    position = models.ForeignKey('PositionHierarchies', models.DO_NOTHING, blank=True, null=True)
    system_generated = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_employee_as_family_details'


class CitizenshipFamilyDetails(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    citizenship_applicant_family_type = models.CharField(max_length=255, blank=True, null=True)
    citizenship_country = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    citizenship_number = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    first_name_np = models.CharField(max_length=255, blank=True, null=True)
    foreign_address = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    last_name_np = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name_np = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    citizenship_application = models.ForeignKey(CitizenshipApplication, models.DO_NOTHING)
    system_generated = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_family_details'


class CitizenshipNumberGenerations(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    citizenship_number = models.CharField(max_length=255, blank=True, null=True)
    citizenship_number_np = models.CharField(max_length=255, blank=True, null=True)
    created_date_np = models.CharField(max_length=255, blank=True, null=True)
    fy_code = models.CharField(max_length=255, blank=True, null=True)
    issued_date = models.DateTimeField(blank=True, null=True)
    serial_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    system_generated = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    citizenship_application = models.ForeignKey(CitizenshipApplication, models.DO_NOTHING)
    citizenship_issued_district = models.ForeignKey('Districts', models.DO_NOTHING, blank=True, null=True)
    issued_date_np = models.CharField(max_length=255, blank=True, null=True)
    office_code = models.CharField(max_length=255, blank=True, null=True)
    old_entry = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    entry_office_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_number_generations'


class CitizenshipReferenceDetails(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    citizenship_no = models.CharField(max_length=255, blank=True, null=True)
    citizenship_reference = models.CharField(max_length=255, blank=True, null=True)
    citizenship_type = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=600)
    first_name_np = models.CharField(max_length=600)
    last_name = models.CharField(max_length=600)
    last_name_np = models.CharField(max_length=600)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name_np = models.CharField(max_length=600, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street_np = models.CharField(max_length=255, blank=True, null=True)
    ward_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    citizenship_application = models.ForeignKey(CitizenshipApplication, models.DO_NOTHING)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)
    local_body = models.ForeignKey('LocalBodies', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_reference_details'


class CitizenshipStatuses(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citizenship_statuses'


class Countries(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    citizenship = models.CharField(max_length=100, blank=True, null=True)
    citizenship_np = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    nationality_np = models.CharField(max_length=255, blank=True, null=True)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Designations(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    alias_np = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=1000)
    name_np = models.CharField(max_length=1000)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    is_citizenship_office_designation = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designations'


class Districts(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(unique=True, max_length=100, blank=True, null=True)
    alias_np = models.CharField(unique=True, max_length=100, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    province = models.ForeignKey('Provinces', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'


class DocumentTypes(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    upload_file_type = models.CharField(max_length=255)
    upload_size_mb = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'document_types'


class EducationQualifications(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_qualifications'


class Genders(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    alias_np = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'


class LocalBodies(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    no_of_wards = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    district = models.ForeignKey(Districts, models.DO_NOTHING, blank=True, null=True)
    local_body_type = models.ForeignKey('LocalBodyTypes', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_bodies'


class LocalBodyTypes(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(unique=True, max_length=100, blank=True, null=True)
    alias_np = models.CharField(unique=True, max_length=100, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_body_types'


class MaritalStatus(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    alias_np = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    name_np = models.CharField(max_length=255, blank=True, null=True)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marital_status'


class Names(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'names'


class Occupations(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(unique=True, max_length=255, blank=True, null=True)
    alias_np = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occupations'


class Offices(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_np = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(unique=True, max_length=100)
    coverage_level = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    fax_no = models.CharField(max_length=50, blank=True, null=True)
    house_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    office_level_type = models.CharField(max_length=255)
    office_type = models.CharField(max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    po_box_no = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street_np = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    ward_no = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    former_vdc_municipality_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    local_body_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    requesting_office = models.ForeignKey('self', models.DO_NOTHING, related_name='offices_requesting_office_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offices'


class PositionHierarchies(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    alias_np = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    position_type = models.CharField(max_length=255)
    position_cd = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position_hierarchies'


class Processes(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    main_process = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    name = models.CharField(max_length=255)
    name_np = models.CharField(max_length=255)
    menu_id = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'processes'


class Provinces(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(unique=True, max_length=100, blank=True, null=True)
    alias_np = models.CharField(unique=True, max_length=100, blank=True, null=True)
    code = models.CharField(unique=True, max_length=20)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'


class RelationshipTypes(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    alias_np = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    applicable_for_minor = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relationship_types'


class Religions(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=19, decimal_places=0)
    created_by = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField()
    is_active = models.DecimalField(max_digits=1, decimal_places=0)
    last_modified_by = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    alias = models.CharField(max_length=100, blank=True, null=True)
    alias_np = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    name_np = models.CharField(unique=True, max_length=255)
    order_no = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'religions'
