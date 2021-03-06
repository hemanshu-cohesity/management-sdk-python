# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.google_account_information
import cohesity_management_sdk.models.id_p_user_information
import cohesity_management_sdk.models.salesforce_account_information

class UserDetails(object):

    """Implementation of the 'User Details.' model.

    Specifies details about a user.

    Attributes:
        additional_group_names (list of string): Array of Additional Groups.
            Specifies the names of additional groups this User may belong to.
        created_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user account was created on the Cohesity
            Cluster.
        description (string): Specifies a description about the user.
        domain (string): Specifies the fully qualified domain name (FQDN) of
            an Active Directory or LOCAL for the default LOCAL domain on the
            Cohesity Cluster. A user is uniquely identified by combination of
            the username and the domain.
        effective_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user becomes effective. Until that time, the
            user cannot log in.
        email_address (string): Specifies the email address of the user.
        expired_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user becomes expired. After that, the user
            cannot log in.
        google_account (GoogleAccountInformation): Google Account Information
            of a Helios BaaS user.
        idp_user_info (IdPUserInformation): Specifies an IdP User's
            information logged in using an IdP. This information is not stored
            on the Cluster.
        last_updated_time_msecs (long|int): Specifies the epoch time in
            milliseconds when the user account was last modified on the
            Cohesity Cluster.
        password (string): Specifies the password of this user.
        primary_group_name (string): Specifies the name of the primary group
            of this User.
        restricted (bool): Whether the user is a restricted user. A restricted
            user can only view the objects he has permissions to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with the user such as such as 'Admin', 'Ops' or
            'View'. The Cohesity roles determine privileges on the Cohesity
            Cluster for this user.
        s_3_access_key_id (string): Specifies the S3 Account Access Key ID.
        s_3_account_id (string): Specifies the S3 Account Canonical User ID.
        s_3_secret_key (string): Specifies the S3 Account Secret Key.
        salesforce_account (SalesforceAccountInformation): Salesforce Account
            Information of a Helios user.
        sid (string): Specifies the unique Security ID (SID) of the user.
        tenant_id (string): Specifies the effective Tenant ID of the user.
        username (string): Specifies the login name of the user.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_group_names":'additionalGroupNames',
        "created_time_msecs":'createdTimeMsecs',
        "description":'description',
        "domain":'domain',
        "effective_time_msecs":'effectiveTimeMsecs',
        "email_address":'emailAddress',
        "expired_time_msecs":'expiredTimeMsecs',
        "google_account":'googleAccount',
        "idp_user_info":'idpUserInfo',
        "last_updated_time_msecs":'lastUpdatedTimeMsecs',
        "password":'password',
        "primary_group_name":'primaryGroupName',
        "restricted":'restricted',
        "roles":'roles',
        "s_3_access_key_id":'s3AccessKeyId',
        "s_3_account_id":'s3AccountId',
        "s_3_secret_key":'s3SecretKey',
        "salesforce_account":'salesforceAccount',
        "sid":'sid',
        "tenant_id":'tenantId',
        "username":'username'
    }

    def __init__(self,
                 additional_group_names=None,
                 created_time_msecs=None,
                 description=None,
                 domain=None,
                 effective_time_msecs=None,
                 email_address=None,
                 expired_time_msecs=None,
                 google_account=None,
                 idp_user_info=None,
                 last_updated_time_msecs=None,
                 password=None,
                 primary_group_name=None,
                 restricted=None,
                 roles=None,
                 s_3_access_key_id=None,
                 s_3_account_id=None,
                 s_3_secret_key=None,
                 salesforce_account=None,
                 sid=None,
                 tenant_id=None,
                 username=None):
        """Constructor for the UserDetails class"""

        # Initialize members of the class
        self.additional_group_names = additional_group_names
        self.created_time_msecs = created_time_msecs
        self.description = description
        self.domain = domain
        self.effective_time_msecs = effective_time_msecs
        self.email_address = email_address
        self.expired_time_msecs = expired_time_msecs
        self.google_account = google_account
        self.idp_user_info = idp_user_info
        self.last_updated_time_msecs = last_updated_time_msecs
        self.password = password
        self.primary_group_name = primary_group_name
        self.restricted = restricted
        self.roles = roles
        self.s_3_access_key_id = s_3_access_key_id
        self.s_3_account_id = s_3_account_id
        self.s_3_secret_key = s_3_secret_key
        self.salesforce_account = salesforce_account
        self.sid = sid
        self.tenant_id = tenant_id
        self.username = username


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        additional_group_names = dictionary.get('additionalGroupNames')
        created_time_msecs = dictionary.get('createdTimeMsecs')
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        effective_time_msecs = dictionary.get('effectiveTimeMsecs')
        email_address = dictionary.get('emailAddress')
        expired_time_msecs = dictionary.get('expiredTimeMsecs')
        google_account = cohesity_management_sdk.models.google_account_information.GoogleAccountInformation.from_dictionary(dictionary.get('googleAccount')) if dictionary.get('googleAccount') else None
        idp_user_info = cohesity_management_sdk.models.id_p_user_information.IdPUserInformation.from_dictionary(dictionary.get('idpUserInfo')) if dictionary.get('idpUserInfo') else None
        last_updated_time_msecs = dictionary.get('lastUpdatedTimeMsecs')
        password = dictionary.get('password')
        primary_group_name = dictionary.get('primaryGroupName')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')
        s_3_access_key_id = dictionary.get('s3AccessKeyId')
        s_3_account_id = dictionary.get('s3AccountId')
        s_3_secret_key = dictionary.get('s3SecretKey')
        salesforce_account = cohesity_management_sdk.models.salesforce_account_information.SalesforceAccountInformation.from_dictionary(dictionary.get('salesforceAccount')) if dictionary.get('salesforceAccount') else None
        sid = dictionary.get('sid')
        tenant_id = dictionary.get('tenantId')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(additional_group_names,
                   created_time_msecs,
                   description,
                   domain,
                   effective_time_msecs,
                   email_address,
                   expired_time_msecs,
                   google_account,
                   idp_user_info,
                   last_updated_time_msecs,
                   password,
                   primary_group_name,
                   restricted,
                   roles,
                   s_3_access_key_id,
                   s_3_account_id,
                   s_3_secret_key,
                   salesforce_account,
                   sid,
                   tenant_id,
                   username)


