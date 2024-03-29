# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/lsa.so
# by generator 1.138
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


# Variables with simple values

LSA_ACCOUNT_ADJUST_PRIVILEGES = 2
LSA_ACCOUNT_ADJUST_QUOTAS = 4

LSA_ACCOUNT_ADJUST_SYSTEM_ACCESS = 8

LSA_ACCOUNT_ALL_ACCESS = 983055

LSA_ACCOUNT_EXECUTE = 131072
LSA_ACCOUNT_READ = 131073
LSA_ACCOUNT_VIEW = 1
LSA_ACCOUNT_WRITE = 131086

LSA_AUDIT_CATEGORY_ACCOUNT_LOGON = 8
LSA_AUDIT_CATEGORY_ACCOUNT_MANAGEMENT = 6

LSA_AUDIT_CATEGORY_DIRECTORY_SERVICE_ACCESS = 7

LSA_AUDIT_CATEGORY_FILE_AND_OBJECT_ACCESS = 2

LSA_AUDIT_CATEGORY_LOGON = 1

LSA_AUDIT_CATEGORY_PROCCESS_TRACKING = 4

LSA_AUDIT_CATEGORY_SECURITY_POLICY_CHANGES = 5

LSA_AUDIT_CATEGORY_SYSTEM = 0

LSA_AUDIT_CATEGORY_USE_OF_USER_RIGHTS = 3

LSA_AUDIT_POLICY_ALL = 3
LSA_AUDIT_POLICY_CLEAR = 4
LSA_AUDIT_POLICY_FAILURE = 2
LSA_AUDIT_POLICY_NONE = 0
LSA_AUDIT_POLICY_SUCCESS = 1

LSA_CLIENT_REVISION_1 = 1
LSA_CLIENT_REVISION_2 = 2
LSA_CLIENT_REVISION_DNS = 2

LSA_CLIENT_REVISION_NO_DNS = 1

LSA_DOMAIN_INFO_POLICY_EFS = 2
LSA_DOMAIN_INFO_POLICY_KERBEROS = 3

LSA_ENUM_TRUST_DOMAIN_EX_MULTIPLIER = 82

LSA_ENUM_TRUST_DOMAIN_MULTIPLIER = 60

LSA_FOREST_TRUST_COLLISION_OTHER = 2
LSA_FOREST_TRUST_COLLISION_TDO = 0
LSA_FOREST_TRUST_COLLISION_XREF = 1

LSA_FOREST_TRUST_DOMAIN_INFO = 2

LSA_FOREST_TRUST_RECORD_TYPE_LAST = 3

LSA_FOREST_TRUST_TOP_LEVEL_NAME = 0

LSA_FOREST_TRUST_TOP_LEVEL_NAME_EX = 1

LSA_LOOKUP_NAMES_ALL = 1

LSA_LOOKUP_NAMES_DOMAINS_ONLY = 2

LSA_LOOKUP_NAMES_FOREST_TRUSTS_ONLY = 5

LSA_LOOKUP_NAMES_PRIMARY_DOMAIN_ONLY = 3

LSA_LOOKUP_NAMES_RODC_REFERRAL_TO_FULL_DC = 7

LSA_LOOKUP_NAMES_UPLEVEL_TRUSTS_ONLY = 4
LSA_LOOKUP_NAMES_UPLEVEL_TRUSTS_ONLY2 = 6

LSA_LOOKUP_OPTIONS_NO_ISOLATED = 2147483648

LSA_LOOKUP_OPTION_SEARCH_ISOLATED_NAMES = 0

LSA_LOOKUP_OPTION_SEARCH_ISOLATED_NAMES_LOCAL = -2147483648

LSA_NB_DISABLED_ADMIN = 4
LSA_NB_DISABLED_CONFLICT = 8

LSA_POLICY_ALL_ACCESS = 987135

LSA_POLICY_AUDIT_LOG_ADMIN = 512

LSA_POLICY_CREATE_ACCOUNT = 16
LSA_POLICY_CREATE_PRIVILEGE = 64
LSA_POLICY_CREATE_SECRET = 32

LSA_POLICY_EXECUTE = 133121

LSA_POLICY_GET_PRIVATE_INFORMATION = 4

LSA_POLICY_INFO_ACCOUNT_DOMAIN = 5

LSA_POLICY_INFO_AUDIT_EVENTS = 2

LSA_POLICY_INFO_AUDIT_FULL_QUERY = 11
LSA_POLICY_INFO_AUDIT_FULL_SET = 10

LSA_POLICY_INFO_AUDIT_LOG = 1

LSA_POLICY_INFO_DNS = 12

LSA_POLICY_INFO_DNS_INT = 13

LSA_POLICY_INFO_DOMAIN = 3

LSA_POLICY_INFO_L_ACCOUNT_DOMAIN = 14

LSA_POLICY_INFO_MOD = 9
LSA_POLICY_INFO_PD = 4
LSA_POLICY_INFO_QUOTA = 8
LSA_POLICY_INFO_REPLICA = 7
LSA_POLICY_INFO_ROLE = 6

LSA_POLICY_KERBEROS_VALIDATE_CLIENT = 128

LSA_POLICY_LOOKUP_NAMES = 2048

LSA_POLICY_NOTIFICATION = 4096
LSA_POLICY_READ = 131079

LSA_POLICY_SERVER_ADMIN = 1024

LSA_POLICY_SET_AUDIT_REQUIREMENTS = 256

LSA_POLICY_SET_DEFAULT_QUOTA_LIMITS = 128

LSA_POLICY_TRUST_ADMIN = 8

LSA_POLICY_VIEW_AUDIT_INFORMATION = 2

LSA_POLICY_VIEW_LOCAL_INFORMATION = 1

LSA_POLICY_WRITE = 133112

LSA_REF_DOMAIN_LIST_MULTIPLIER = 32

LSA_ROLE_BACKUP = 2
LSA_ROLE_PRIMARY = 3

LSA_SECRET_ALL_ACCESS = 983043

LSA_SECRET_EXECUTE = 131072

LSA_SECRET_QUERY_VALUE = 2

LSA_SECRET_READ = 131074

LSA_SECRET_SET_VALUE = 1

LSA_SECRET_WRITE = 131073

LSA_SID_DISABLED_ADMIN = 1
LSA_SID_DISABLED_CONFLICT = 2

LSA_TLN_DISABLED_ADMIN = 2
LSA_TLN_DISABLED_CONFLICT = 4
LSA_TLN_DISABLED_NEW = 1

LSA_TRUSTED_DOMAIN_ALL_ACCESS = 983167

LSA_TRUSTED_DOMAIN_EXECUTE = 131081

LSA_TRUSTED_DOMAIN_INFO_AUTH_INFO = 7

LSA_TRUSTED_DOMAIN_INFO_AUTH_INFO_INTERNAL = 9

LSA_TRUSTED_DOMAIN_INFO_BASIC = 5
LSA_TRUSTED_DOMAIN_INFO_CONTROLLERS = 2

LSA_TRUSTED_DOMAIN_INFO_FULL_INFO = 8

LSA_TRUSTED_DOMAIN_INFO_FULL_INFO_2_INTERNAL = 12

LSA_TRUSTED_DOMAIN_INFO_FULL_INFO_INTERNAL = 10

LSA_TRUSTED_DOMAIN_INFO_INFO_EX = 6

LSA_TRUSTED_DOMAIN_INFO_INFO_EX2_INTERNAL = 11

LSA_TRUSTED_DOMAIN_INFO_NAME = 1
LSA_TRUSTED_DOMAIN_INFO_PASSWORD = 4

LSA_TRUSTED_DOMAIN_INFO_POSIX_OFFSET = 3

LSA_TRUSTED_DOMAIN_READ = 131073

LSA_TRUSTED_DOMAIN_SUPPORTED_ENCRYPTION_TYPES = 13

LSA_TRUSTED_DOMAIN_WRITE = 131124

LSA_TRUSTED_QUERY_AUTH = 64
LSA_TRUSTED_QUERY_CONTROLLERS = 2

LSA_TRUSTED_QUERY_DOMAIN_NAME = 1

LSA_TRUSTED_QUERY_POSIX = 8

LSA_TRUSTED_SET_AUTH = 32
LSA_TRUSTED_SET_CONTROLLERS = 4
LSA_TRUSTED_SET_POSIX = 16

LSA_TRUST_ATTRIBUTE_CROSS_ORGANIZATION = 16

LSA_TRUST_ATTRIBUTE_FOREST_TRANSITIVE = 8

LSA_TRUST_ATTRIBUTE_NON_TRANSITIVE = 1

LSA_TRUST_ATTRIBUTE_QUARANTINED_DOMAIN = 4

LSA_TRUST_ATTRIBUTE_TREAT_AS_EXTERNAL = 64

LSA_TRUST_ATTRIBUTE_UPLEVEL_ONLY = 2

LSA_TRUST_ATTRIBUTE_USES_RC4_ENCRYPTION = 128

LSA_TRUST_ATTRIBUTE_WITHIN_FOREST = 32

LSA_TRUST_DIRECTION_INBOUND = 1
LSA_TRUST_DIRECTION_OUTBOUND = 2

LSA_TRUST_TYPE_DOWNLEVEL = 1
LSA_TRUST_TYPE_MIT = 3
LSA_TRUST_TYPE_UPLEVEL = 2

SID_NAME_ALIAS = 4
SID_NAME_COMPUTER = 9
SID_NAME_DELETED = 6
SID_NAME_DOMAIN = 3

SID_NAME_DOM_GRP = 2

SID_NAME_INVALID = 7
SID_NAME_UNKNOWN = 8
SID_NAME_USER = 1

SID_NAME_USE_NONE = 0

SID_NAME_WKN_GRP = 5

TRUST_AUTH_TYPE_CLEAR = 2
TRUST_AUTH_TYPE_NONE = 0
TRUST_AUTH_TYPE_NT4OWF = 1
TRUST_AUTH_TYPE_VERSION = 3

# no functions
# classes

from AsciiString import AsciiString
from AsciiStringLarge import AsciiStringLarge
from AuditEventsInfo import AuditEventsInfo
from AuditFullQueryInfo import AuditFullQueryInfo
from AuditFullSetInfo import AuditFullSetInfo
from AuditLogInfo import AuditLogInfo
from BinaryString import BinaryString
from DATA_BUF import DATA_BUF
from DATA_BUF2 import DATA_BUF2
from DATA_BUF_PTR import DATA_BUF_PTR
from DefaultQuotaInfo import DefaultQuotaInfo
from DnsDomainInfo import DnsDomainInfo
from DomainInfo import DomainInfo
from DomainInfoEfs import DomainInfoEfs
from DomainInfoKerberos import DomainInfoKerberos
from DomainList import DomainList
from DomainListEx import DomainListEx
from ForestTrustBinaryData import ForestTrustBinaryData
from ForestTrustCollisionInfo import ForestTrustCollisionInfo
from ForestTrustCollisionRecord import ForestTrustCollisionRecord
from ForestTrustDomainInfo import ForestTrustDomainInfo
from ForestTrustInformation import ForestTrustInformation
from ForestTrustRecord import ForestTrustRecord
from lsarpc import lsarpc
from LUID import LUID
from LUIDAttribute import LUIDAttribute
from ModificationInfo import ModificationInfo
from ObjectAttribute import ObjectAttribute
from PDAccountInfo import PDAccountInfo
from PrivArray import PrivArray
from PrivEntry import PrivEntry
from PrivilegeSet import PrivilegeSet
from QosInfo import QosInfo
from RefDomainList import RefDomainList
from ReplicaSourceInfo import ReplicaSourceInfo
from RightAttribute import RightAttribute
from RightSet import RightSet
from ServerRole import ServerRole
from SidArray import SidArray
from SidPtr import SidPtr
from String import String
from StringLarge import StringLarge
from Strings import Strings
from TranslatedName import TranslatedName
from TranslatedName2 import TranslatedName2
from TranslatedSid import TranslatedSid
from TranslatedSid2 import TranslatedSid2
from TranslatedSid3 import TranslatedSid3
from TransNameArray import TransNameArray
from TransNameArray2 import TransNameArray2
from TransSidArray import TransSidArray
from TransSidArray2 import TransSidArray2
from TransSidArray3 import TransSidArray3
from TrustDomainInfoAuthInfo import TrustDomainInfoAuthInfo
from TrustDomainInfoAuthInfoInternal import TrustDomainInfoAuthInfoInternal
from TrustDomainInfoBasic import TrustDomainInfoBasic
from TrustDomainInfoBuffer import TrustDomainInfoBuffer
from TrustDomainInfoControllers import TrustDomainInfoControllers
from TrustDomainInfoFullInfo import TrustDomainInfoFullInfo
from TrustDomainInfoFullInfo2Internal import TrustDomainInfoFullInfo2Internal
from TrustDomainInfoFullInfoInternal import TrustDomainInfoFullInfoInternal
from TrustDomainInfoInfoEx import TrustDomainInfoInfoEx
from TrustDomainInfoInfoEx2Internal import TrustDomainInfoInfoEx2Internal
from TrustDomainInfoName import TrustDomainInfoName
from TrustDomainInfoPassword import TrustDomainInfoPassword
from TrustDomainInfoPosixOffset import TrustDomainInfoPosixOffset
from TrustDomainInfoSupportedEncTypes import TrustDomainInfoSupportedEncTypes
