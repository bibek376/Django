# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class A(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a'


class Accounts(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'accounts'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class B(models.Model):
    name_json = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'b'


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country_name


class Covid(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    days = models.DateField(blank=True, null=True)
    cases = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'covid'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

class GetRequestApiItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'get_request_api_item'


class MbDfsTrans(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_date = models.DateTimeField(blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    last_modified_by = models.BigIntegerField(blank=True, null=True)
    is_active = models.BooleanField()
    amount = models.FloatField(blank=True, null=True)
    bank_code = models.CharField(max_length=255, blank=True, null=True)
    bank_comm_amount = models.FloatField(blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    beneficiary_address = models.CharField(max_length=255, blank=True, null=True)
    beneficiary_name = models.CharField(max_length=255, blank=True, null=True)
    cbs_client_tran_id = models.BigIntegerField(blank=True, null=True)
    client_id = models.BigIntegerField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    customer_code = models.CharField(max_length=255, blank=True, null=True)
    customer_comm_amount = models.FloatField(blank=True, null=True)
    extra_amount = models.FloatField(blank=True, null=True)
    extra_amount_type = models.CharField(max_length=255, blank=True, null=True)
    gateway_comm_amount = models.FloatField(blank=True, null=True)
    hub_corp_comm_amount = models.FloatField(blank=True, null=True)
    imei = models.CharField(max_length=255, blank=True, null=True)
    inst_comm_amount = models.FloatField(blank=True, null=True)
    is_critical = models.BooleanField()
    log_id = models.BigIntegerField(blank=True, null=True)
    max_completion_date = models.CharField(max_length=255, blank=True, null=True)
    originating_unique_id = models.CharField(max_length=255, blank=True, null=True)
    process = models.CharField(max_length=255, blank=True, null=True)
    receiver_bank_ac = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    req_mobile = models.CharField(max_length=255, blank=True, null=True)
    reverse_voucher_number = models.CharField(max_length=255, blank=True, null=True)
    sender_address = models.CharField(max_length=255, blank=True, null=True)
    sender_identification = models.CharField(max_length=255, blank=True, null=True)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    service_info_id = models.CharField(max_length=255, blank=True, null=True)
    service_scope = models.CharField(max_length=255, blank=True, null=True)
    sms_timestamp = models.CharField(max_length=255, blank=True, null=True)
    source_ac = models.CharField(max_length=255, blank=True, null=True)
    status_code = models.CharField(max_length=255, blank=True, null=True)
    status_message = models.CharField(max_length=255, blank=True, null=True)
    tc_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_status = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    voucher_no = models.CharField(max_length=255, blank=True, null=True)
    service_option_id = models.BigIntegerField(blank=True, null=True)
    service_provider_id = models.BigIntegerField(blank=True, null=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    exception_message = models.CharField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    validation_id = models.CharField(max_length=255, blank=True, null=True)
    is_bank_qr = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mb_dfs_trans'


class MbPaymentTran(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ac_no = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    ben_mobile_no = models.CharField(max_length=255, blank=True, null=True)
    cbs_transaction_timestamp = models.CharField(max_length=255, blank=True, null=True)
    client_id = models.BigIntegerField(blank=True, null=True)
    cbs_client_tran_id = models.TextField(blank=True, null=True)
    cooperative_commission = models.FloatField(blank=True, null=True)
    customer_code = models.CharField(max_length=255, blank=True, null=True)
    customer_commission = models.FloatField(blank=True, null=True)
    http_code = models.IntegerField(blank=True, null=True)
    hub_commission = models.FloatField(blank=True, null=True)
    info_commission = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField()
    needs_resubmission = models.BooleanField(blank=True, null=True)
    payment_amt = models.FloatField(blank=True, null=True)
    payment_initiated_date = models.DateTimeField(blank=True, null=True)
    process_end = models.DateTimeField(blank=True, null=True)
    process_start = models.DateTimeField(blank=True, null=True)
    processed_from = models.IntegerField(blank=True, null=True)
    req_mobile = models.CharField(max_length=255, blank=True, null=True)
    request_id = models.CharField(max_length=255, blank=True, null=True)
    response_code = models.IntegerField()
    reverse_vch_no = models.CharField(max_length=255, blank=True, null=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    sms_timestamp = models.CharField(max_length=255, blank=True, null=True)
    total_commission = models.FloatField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    vendor_id = models.BigIntegerField(blank=True, null=True)
    vendor_transaction_id = models.TextField(blank=True, null=True)
    vch_no = models.TextField(blank=True, null=True)
    wallet_id = models.CharField(max_length=255, blank=True, null=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    counter_name = models.CharField(max_length=255, blank=True, null=True)
    exception_message = models.TextField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    session_id = models.CharField(max_length=255, blank=True, null=True)
    ebp_number = models.CharField(max_length=255, blank=True, null=True)
    status_message = models.CharField(max_length=255, blank=True, null=True)
    transaction_status = models.CharField(max_length=255, blank=True, null=True)
    reverse_wallet_id = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    transaction_mode = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mb_payment_tran'


class ParameterMappingTable(models.Model):
    id = models.AutoField(primary_key=True)
    reconcilation_id = models.IntegerField(blank=True, null=True)
    parameter_table_id = models.IntegerField(blank=True, null=True)
    validation = models.IntegerField(blank=True, null=True)
    data_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parameter_mapping_table'


class ParameterTable(models.Model):
    id = models.AutoField(primary_key=True)
    parameter_name = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parameter_table'


class ReconcilationCategory(models.Model):
    id = models.AutoField(primary_key=True)
    recon_name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reconcilation_category'


class ReconciliationCategory15(models.Model):
    amount = models.CharField(max_length=100, blank=True, null=True)
    tran_id = models.IntegerField(blank=True, null=True)
    drcr_type = models.CharField(max_length=50, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reconciliation_category_15'


class TestReconciliationCategory15(models.Model):
    amount = models.CharField(max_length=100, blank=True, null=True)
    tran_id = models.IntegerField(blank=True, null=True)
    drcr_type = models.CharField(max_length=50, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'test_reconciliation_category_15'
