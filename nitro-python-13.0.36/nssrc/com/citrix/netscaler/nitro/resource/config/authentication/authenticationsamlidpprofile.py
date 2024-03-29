#
# Copyright (c) 2008-2019 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class authenticationsamlidpprofile(base_resource) :
	""" Configuration for AAA Saml IdentityProvider (IdP) profile resource. """
	def __init__(self) :
		self._name = None
		self._samlspcertname = None
		self._samlidpcertname = None
		self._assertionconsumerserviceurl = None
		self._sendpassword = None
		self._samlissuername = None
		self._rejectunsignedrequests = None
		self._signaturealg = None
		self._digestmethod = None
		self._audience = None
		self._nameidformat = None
		self._nameidexpr = None
		self._attribute1 = None
		self._attribute1expr = None
		self._attribute1friendlyname = None
		self._attribute1format = None
		self._attribute2 = None
		self._attribute2expr = None
		self._attribute2friendlyname = None
		self._attribute2format = None
		self._attribute3 = None
		self._attribute3expr = None
		self._attribute3friendlyname = None
		self._attribute3format = None
		self._attribute4 = None
		self._attribute4expr = None
		self._attribute4friendlyname = None
		self._attribute4format = None
		self._attribute5 = None
		self._attribute5expr = None
		self._attribute5friendlyname = None
		self._attribute5format = None
		self._attribute6 = None
		self._attribute6expr = None
		self._attribute6friendlyname = None
		self._attribute6format = None
		self._attribute7 = None
		self._attribute7expr = None
		self._attribute7friendlyname = None
		self._attribute7format = None
		self._attribute8 = None
		self._attribute8expr = None
		self._attribute8friendlyname = None
		self._attribute8format = None
		self._attribute9 = None
		self._attribute9expr = None
		self._attribute9friendlyname = None
		self._attribute9format = None
		self._attribute10 = None
		self._attribute10expr = None
		self._attribute10friendlyname = None
		self._attribute10format = None
		self._attribute11 = None
		self._attribute11expr = None
		self._attribute11friendlyname = None
		self._attribute11format = None
		self._attribute12 = None
		self._attribute12expr = None
		self._attribute12friendlyname = None
		self._attribute12format = None
		self._attribute13 = None
		self._attribute13expr = None
		self._attribute13friendlyname = None
		self._attribute13format = None
		self._attribute14 = None
		self._attribute14expr = None
		self._attribute14friendlyname = None
		self._attribute14format = None
		self._attribute15 = None
		self._attribute15expr = None
		self._attribute15friendlyname = None
		self._attribute15format = None
		self._attribute16 = None
		self._attribute16expr = None
		self._attribute16friendlyname = None
		self._attribute16format = None
		self._encryptassertion = None
		self._encryptionalgorithm = None
		self._samlbinding = None
		self._skewtime = None
		self._serviceproviderid = None
		self._signassertion = None
		self._keytransportalg = None
		self._splogouturl = None
		self._logoutbinding = None
		self._defaultauthenticationgroup = None
		self._metadataurl = None
		self._metadatarefreshinterval = None
		self._signatureservice = None
		self._samlsigningcertversion = None
		self._samlspcertversion = None
		self._metadataimportstatus = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the new saml single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def samlspcertname(self) :
		r"""Name of the SSL certificate of SAML Relying Party. This certificate is used to verify signature of the incoming AuthnRequest from a Relying Party or Service Provider.<br/>Minimum length =  1.
		"""
		try :
			return self._samlspcertname
		except Exception as e:
			raise e

	@samlspcertname.setter
	def samlspcertname(self, samlspcertname) :
		r"""Name of the SSL certificate of SAML Relying Party. This certificate is used to verify signature of the incoming AuthnRequest from a Relying Party or Service Provider.<br/>Minimum length =  1
		"""
		try :
			self._samlspcertname = samlspcertname
		except Exception as e:
			raise e

	@property
	def samlidpcertname(self) :
		r"""Name of the certificate used to sign the SAMLResposne that is sent to Relying Party or Service Provider after successful authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._samlidpcertname
		except Exception as e:
			raise e

	@samlidpcertname.setter
	def samlidpcertname(self, samlidpcertname) :
		r"""Name of the certificate used to sign the SAMLResposne that is sent to Relying Party or Service Provider after successful authentication.<br/>Minimum length =  1
		"""
		try :
			self._samlidpcertname = samlidpcertname
		except Exception as e:
			raise e

	@property
	def assertionconsumerserviceurl(self) :
		r"""URL to which the assertion is to be sent.<br/>Minimum length =  1.
		"""
		try :
			return self._assertionconsumerserviceurl
		except Exception as e:
			raise e

	@assertionconsumerserviceurl.setter
	def assertionconsumerserviceurl(self, assertionconsumerserviceurl) :
		r"""URL to which the assertion is to be sent.<br/>Minimum length =  1
		"""
		try :
			self._assertionconsumerserviceurl = assertionconsumerserviceurl
		except Exception as e:
			raise e

	@property
	def sendpassword(self) :
		r"""Option to send password in assertion.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sendpassword
		except Exception as e:
			raise e

	@sendpassword.setter
	def sendpassword(self, sendpassword) :
		r"""Option to send password in assertion.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sendpassword = sendpassword
		except Exception as e:
			raise e

	@property
	def samlissuername(self) :
		r"""The name to be used in requests sent from	Citrix ADC to IdP to uniquely identify Citrix ADC.<br/>Minimum length =  1.
		"""
		try :
			return self._samlissuername
		except Exception as e:
			raise e

	@samlissuername.setter
	def samlissuername(self, samlissuername) :
		r"""The name to be used in requests sent from	Citrix ADC to IdP to uniquely identify Citrix ADC.<br/>Minimum length =  1
		"""
		try :
			self._samlissuername = samlissuername
		except Exception as e:
			raise e

	@property
	def rejectunsignedrequests(self) :
		r"""Option to Reject unsigned SAML Requests. ON option denies any authentication requests that arrive without signature.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._rejectunsignedrequests
		except Exception as e:
			raise e

	@rejectunsignedrequests.setter
	def rejectunsignedrequests(self, rejectunsignedrequests) :
		r"""Option to Reject unsigned SAML Requests. ON option denies any authentication requests that arrive without signature.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._rejectunsignedrequests = rejectunsignedrequests
		except Exception as e:
			raise e

	@property
	def signaturealg(self) :
		r"""Algorithm to be used to sign/verify SAML transactions.<br/>Default value: RSA-SHA256<br/>Possible values = RSA-SHA1, RSA-SHA256.
		"""
		try :
			return self._signaturealg
		except Exception as e:
			raise e

	@signaturealg.setter
	def signaturealg(self, signaturealg) :
		r"""Algorithm to be used to sign/verify SAML transactions.<br/>Default value: RSA-SHA256<br/>Possible values = RSA-SHA1, RSA-SHA256
		"""
		try :
			self._signaturealg = signaturealg
		except Exception as e:
			raise e

	@property
	def digestmethod(self) :
		r"""Algorithm to be used to compute/verify digest for SAML transactions.<br/>Default value: SHA256<br/>Possible values = SHA1, SHA256.
		"""
		try :
			return self._digestmethod
		except Exception as e:
			raise e

	@digestmethod.setter
	def digestmethod(self, digestmethod) :
		r"""Algorithm to be used to compute/verify digest for SAML transactions.<br/>Default value: SHA256<br/>Possible values = SHA1, SHA256
		"""
		try :
			self._digestmethod = digestmethod
		except Exception as e:
			raise e

	@property
	def audience(self) :
		r"""Audience for which assertion sent by IdP is applicable. This is typically entity name or url that represents ServiceProvider.
		"""
		try :
			return self._audience
		except Exception as e:
			raise e

	@audience.setter
	def audience(self, audience) :
		r"""Audience for which assertion sent by IdP is applicable. This is typically entity name or url that represents ServiceProvider.
		"""
		try :
			self._audience = audience
		except Exception as e:
			raise e

	@property
	def nameidformat(self) :
		r"""Format of Name Identifier sent in Assertion.<br/>Default value: transient<br/>Possible values = Unspecified, emailAddress, X509SubjectName, WindowsDomainQualifiedName, kerberos, entity, persistent, transient.
		"""
		try :
			return self._nameidformat
		except Exception as e:
			raise e

	@nameidformat.setter
	def nameidformat(self, nameidformat) :
		r"""Format of Name Identifier sent in Assertion.<br/>Default value: transient<br/>Possible values = Unspecified, emailAddress, X509SubjectName, WindowsDomainQualifiedName, kerberos, entity, persistent, transient
		"""
		try :
			self._nameidformat = nameidformat
		except Exception as e:
			raise e

	@property
	def nameidexpr(self) :
		r"""Expression that will be evaluated to obtain NameIdentifier to be sent in assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._nameidexpr
		except Exception as e:
			raise e

	@nameidexpr.setter
	def nameidexpr(self, nameidexpr) :
		r"""Expression that will be evaluated to obtain NameIdentifier to be sent in assertion.<br/>Maximum length =  128
		"""
		try :
			self._nameidexpr = nameidexpr
		except Exception as e:
			raise e

	@property
	def attribute1(self) :
		r"""Name of attribute1 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		r"""Name of attribute1 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute1expr(self) :
		r"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute1expr
		except Exception as e:
			raise e

	@attribute1expr.setter
	def attribute1expr(self, attribute1expr) :
		r"""Expression that will be evaluated to obtain attribute1's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute1expr = attribute1expr
		except Exception as e:
			raise e

	@property
	def attribute1friendlyname(self) :
		r"""User-Friendly Name of attribute1 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute1friendlyname
		except Exception as e:
			raise e

	@attribute1friendlyname.setter
	def attribute1friendlyname(self, attribute1friendlyname) :
		r"""User-Friendly Name of attribute1 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute1friendlyname = attribute1friendlyname
		except Exception as e:
			raise e

	@property
	def attribute1format(self) :
		r"""Format of Attribute1 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute1format
		except Exception as e:
			raise e

	@attribute1format.setter
	def attribute1format(self, attribute1format) :
		r"""Format of Attribute1 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute1format = attribute1format
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		r"""Name of attribute2 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		r"""Name of attribute2 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute2expr(self) :
		r"""Expression that will be evaluated to obtain attribute2's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute2expr
		except Exception as e:
			raise e

	@attribute2expr.setter
	def attribute2expr(self, attribute2expr) :
		r"""Expression that will be evaluated to obtain attribute2's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute2expr = attribute2expr
		except Exception as e:
			raise e

	@property
	def attribute2friendlyname(self) :
		r"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute2friendlyname
		except Exception as e:
			raise e

	@attribute2friendlyname.setter
	def attribute2friendlyname(self, attribute2friendlyname) :
		r"""User-Friendly Name of attribute2 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute2friendlyname = attribute2friendlyname
		except Exception as e:
			raise e

	@property
	def attribute2format(self) :
		r"""Format of Attribute2 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute2format
		except Exception as e:
			raise e

	@attribute2format.setter
	def attribute2format(self, attribute2format) :
		r"""Format of Attribute2 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute2format = attribute2format
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		r"""Name of attribute3 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		r"""Name of attribute3 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute3expr(self) :
		r"""Expression that will be evaluated to obtain attribute3's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute3expr
		except Exception as e:
			raise e

	@attribute3expr.setter
	def attribute3expr(self, attribute3expr) :
		r"""Expression that will be evaluated to obtain attribute3's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute3expr = attribute3expr
		except Exception as e:
			raise e

	@property
	def attribute3friendlyname(self) :
		r"""User-Friendly Name of attribute3 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute3friendlyname
		except Exception as e:
			raise e

	@attribute3friendlyname.setter
	def attribute3friendlyname(self, attribute3friendlyname) :
		r"""User-Friendly Name of attribute3 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute3friendlyname = attribute3friendlyname
		except Exception as e:
			raise e

	@property
	def attribute3format(self) :
		r"""Format of Attribute3 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute3format
		except Exception as e:
			raise e

	@attribute3format.setter
	def attribute3format(self, attribute3format) :
		r"""Format of Attribute3 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute3format = attribute3format
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		r"""Name of attribute4 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		r"""Name of attribute4 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute4expr(self) :
		r"""Expression that will be evaluated to obtain attribute4's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute4expr
		except Exception as e:
			raise e

	@attribute4expr.setter
	def attribute4expr(self, attribute4expr) :
		r"""Expression that will be evaluated to obtain attribute4's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute4expr = attribute4expr
		except Exception as e:
			raise e

	@property
	def attribute4friendlyname(self) :
		r"""User-Friendly Name of attribute4 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute4friendlyname
		except Exception as e:
			raise e

	@attribute4friendlyname.setter
	def attribute4friendlyname(self, attribute4friendlyname) :
		r"""User-Friendly Name of attribute4 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute4friendlyname = attribute4friendlyname
		except Exception as e:
			raise e

	@property
	def attribute4format(self) :
		r"""Format of Attribute4 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute4format
		except Exception as e:
			raise e

	@attribute4format.setter
	def attribute4format(self, attribute4format) :
		r"""Format of Attribute4 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute4format = attribute4format
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		r"""Name of attribute5 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		r"""Name of attribute5 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute5expr(self) :
		r"""Expression that will be evaluated to obtain attribute5's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute5expr
		except Exception as e:
			raise e

	@attribute5expr.setter
	def attribute5expr(self, attribute5expr) :
		r"""Expression that will be evaluated to obtain attribute5's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute5expr = attribute5expr
		except Exception as e:
			raise e

	@property
	def attribute5friendlyname(self) :
		r"""User-Friendly Name of attribute5 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute5friendlyname
		except Exception as e:
			raise e

	@attribute5friendlyname.setter
	def attribute5friendlyname(self, attribute5friendlyname) :
		r"""User-Friendly Name of attribute5 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute5friendlyname = attribute5friendlyname
		except Exception as e:
			raise e

	@property
	def attribute5format(self) :
		r"""Format of Attribute5 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute5format
		except Exception as e:
			raise e

	@attribute5format.setter
	def attribute5format(self, attribute5format) :
		r"""Format of Attribute5 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute5format = attribute5format
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		r"""Name of attribute6 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		r"""Name of attribute6 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute6expr(self) :
		r"""Expression that will be evaluated to obtain attribute6's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute6expr
		except Exception as e:
			raise e

	@attribute6expr.setter
	def attribute6expr(self, attribute6expr) :
		r"""Expression that will be evaluated to obtain attribute6's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute6expr = attribute6expr
		except Exception as e:
			raise e

	@property
	def attribute6friendlyname(self) :
		r"""User-Friendly Name of attribute6 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute6friendlyname
		except Exception as e:
			raise e

	@attribute6friendlyname.setter
	def attribute6friendlyname(self, attribute6friendlyname) :
		r"""User-Friendly Name of attribute6 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute6friendlyname = attribute6friendlyname
		except Exception as e:
			raise e

	@property
	def attribute6format(self) :
		r"""Format of Attribute6 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute6format
		except Exception as e:
			raise e

	@attribute6format.setter
	def attribute6format(self, attribute6format) :
		r"""Format of Attribute6 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute6format = attribute6format
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		r"""Name of attribute7 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		r"""Name of attribute7 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute7expr(self) :
		r"""Expression that will be evaluated to obtain attribute7's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute7expr
		except Exception as e:
			raise e

	@attribute7expr.setter
	def attribute7expr(self, attribute7expr) :
		r"""Expression that will be evaluated to obtain attribute7's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute7expr = attribute7expr
		except Exception as e:
			raise e

	@property
	def attribute7friendlyname(self) :
		r"""User-Friendly Name of attribute7 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute7friendlyname
		except Exception as e:
			raise e

	@attribute7friendlyname.setter
	def attribute7friendlyname(self, attribute7friendlyname) :
		r"""User-Friendly Name of attribute7 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute7friendlyname = attribute7friendlyname
		except Exception as e:
			raise e

	@property
	def attribute7format(self) :
		r"""Format of Attribute7 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute7format
		except Exception as e:
			raise e

	@attribute7format.setter
	def attribute7format(self, attribute7format) :
		r"""Format of Attribute7 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute7format = attribute7format
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		r"""Name of attribute8 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		r"""Name of attribute8 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute8expr(self) :
		r"""Expression that will be evaluated to obtain attribute8's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute8expr
		except Exception as e:
			raise e

	@attribute8expr.setter
	def attribute8expr(self, attribute8expr) :
		r"""Expression that will be evaluated to obtain attribute8's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute8expr = attribute8expr
		except Exception as e:
			raise e

	@property
	def attribute8friendlyname(self) :
		r"""User-Friendly Name of attribute8 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute8friendlyname
		except Exception as e:
			raise e

	@attribute8friendlyname.setter
	def attribute8friendlyname(self, attribute8friendlyname) :
		r"""User-Friendly Name of attribute8 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute8friendlyname = attribute8friendlyname
		except Exception as e:
			raise e

	@property
	def attribute8format(self) :
		r"""Format of Attribute8 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute8format
		except Exception as e:
			raise e

	@attribute8format.setter
	def attribute8format(self, attribute8format) :
		r"""Format of Attribute8 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute8format = attribute8format
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		r"""Name of attribute9 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		r"""Name of attribute9 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute9expr(self) :
		r"""Expression that will be evaluated to obtain attribute9's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute9expr
		except Exception as e:
			raise e

	@attribute9expr.setter
	def attribute9expr(self, attribute9expr) :
		r"""Expression that will be evaluated to obtain attribute9's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute9expr = attribute9expr
		except Exception as e:
			raise e

	@property
	def attribute9friendlyname(self) :
		r"""User-Friendly Name of attribute9 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute9friendlyname
		except Exception as e:
			raise e

	@attribute9friendlyname.setter
	def attribute9friendlyname(self, attribute9friendlyname) :
		r"""User-Friendly Name of attribute9 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute9friendlyname = attribute9friendlyname
		except Exception as e:
			raise e

	@property
	def attribute9format(self) :
		r"""Format of Attribute9 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute9format
		except Exception as e:
			raise e

	@attribute9format.setter
	def attribute9format(self, attribute9format) :
		r"""Format of Attribute9 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute9format = attribute9format
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		r"""Name of attribute10 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		r"""Name of attribute10 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute10expr(self) :
		r"""Expression that will be evaluated to obtain attribute10's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute10expr
		except Exception as e:
			raise e

	@attribute10expr.setter
	def attribute10expr(self, attribute10expr) :
		r"""Expression that will be evaluated to obtain attribute10's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute10expr = attribute10expr
		except Exception as e:
			raise e

	@property
	def attribute10friendlyname(self) :
		r"""User-Friendly Name of attribute10 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute10friendlyname
		except Exception as e:
			raise e

	@attribute10friendlyname.setter
	def attribute10friendlyname(self, attribute10friendlyname) :
		r"""User-Friendly Name of attribute10 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute10friendlyname = attribute10friendlyname
		except Exception as e:
			raise e

	@property
	def attribute10format(self) :
		r"""Format of Attribute10 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute10format
		except Exception as e:
			raise e

	@attribute10format.setter
	def attribute10format(self, attribute10format) :
		r"""Format of Attribute10 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute10format = attribute10format
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		r"""Name of attribute11 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		r"""Name of attribute11 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute11expr(self) :
		r"""Expression that will be evaluated to obtain attribute11's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute11expr
		except Exception as e:
			raise e

	@attribute11expr.setter
	def attribute11expr(self, attribute11expr) :
		r"""Expression that will be evaluated to obtain attribute11's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute11expr = attribute11expr
		except Exception as e:
			raise e

	@property
	def attribute11friendlyname(self) :
		r"""User-Friendly Name of attribute11 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute11friendlyname
		except Exception as e:
			raise e

	@attribute11friendlyname.setter
	def attribute11friendlyname(self, attribute11friendlyname) :
		r"""User-Friendly Name of attribute11 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute11friendlyname = attribute11friendlyname
		except Exception as e:
			raise e

	@property
	def attribute11format(self) :
		r"""Format of Attribute11 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute11format
		except Exception as e:
			raise e

	@attribute11format.setter
	def attribute11format(self, attribute11format) :
		r"""Format of Attribute11 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute11format = attribute11format
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		r"""Name of attribute12 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		r"""Name of attribute12 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute12expr(self) :
		r"""Expression that will be evaluated to obtain attribute12's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute12expr
		except Exception as e:
			raise e

	@attribute12expr.setter
	def attribute12expr(self, attribute12expr) :
		r"""Expression that will be evaluated to obtain attribute12's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute12expr = attribute12expr
		except Exception as e:
			raise e

	@property
	def attribute12friendlyname(self) :
		r"""User-Friendly Name of attribute12 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute12friendlyname
		except Exception as e:
			raise e

	@attribute12friendlyname.setter
	def attribute12friendlyname(self, attribute12friendlyname) :
		r"""User-Friendly Name of attribute12 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute12friendlyname = attribute12friendlyname
		except Exception as e:
			raise e

	@property
	def attribute12format(self) :
		r"""Format of Attribute12 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute12format
		except Exception as e:
			raise e

	@attribute12format.setter
	def attribute12format(self, attribute12format) :
		r"""Format of Attribute12 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute12format = attribute12format
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		r"""Name of attribute13 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		r"""Name of attribute13 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute13expr(self) :
		r"""Expression that will be evaluated to obtain attribute13's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute13expr
		except Exception as e:
			raise e

	@attribute13expr.setter
	def attribute13expr(self, attribute13expr) :
		r"""Expression that will be evaluated to obtain attribute13's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute13expr = attribute13expr
		except Exception as e:
			raise e

	@property
	def attribute13friendlyname(self) :
		r"""User-Friendly Name of attribute13 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute13friendlyname
		except Exception as e:
			raise e

	@attribute13friendlyname.setter
	def attribute13friendlyname(self, attribute13friendlyname) :
		r"""User-Friendly Name of attribute13 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute13friendlyname = attribute13friendlyname
		except Exception as e:
			raise e

	@property
	def attribute13format(self) :
		r"""Format of Attribute13 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute13format
		except Exception as e:
			raise e

	@attribute13format.setter
	def attribute13format(self, attribute13format) :
		r"""Format of Attribute13 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute13format = attribute13format
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		r"""Name of attribute14 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		r"""Name of attribute14 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute14expr(self) :
		r"""Expression that will be evaluated to obtain attribute14's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute14expr
		except Exception as e:
			raise e

	@attribute14expr.setter
	def attribute14expr(self, attribute14expr) :
		r"""Expression that will be evaluated to obtain attribute14's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute14expr = attribute14expr
		except Exception as e:
			raise e

	@property
	def attribute14friendlyname(self) :
		r"""User-Friendly Name of attribute14 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute14friendlyname
		except Exception as e:
			raise e

	@attribute14friendlyname.setter
	def attribute14friendlyname(self, attribute14friendlyname) :
		r"""User-Friendly Name of attribute14 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute14friendlyname = attribute14friendlyname
		except Exception as e:
			raise e

	@property
	def attribute14format(self) :
		r"""Format of Attribute14 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute14format
		except Exception as e:
			raise e

	@attribute14format.setter
	def attribute14format(self, attribute14format) :
		r"""Format of Attribute14 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute14format = attribute14format
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		r"""Name of attribute15 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		r"""Name of attribute15 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute15expr(self) :
		r"""Expression that will be evaluated to obtain attribute15's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute15expr
		except Exception as e:
			raise e

	@attribute15expr.setter
	def attribute15expr(self, attribute15expr) :
		r"""Expression that will be evaluated to obtain attribute15's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute15expr = attribute15expr
		except Exception as e:
			raise e

	@property
	def attribute15friendlyname(self) :
		r"""User-Friendly Name of attribute15 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute15friendlyname
		except Exception as e:
			raise e

	@attribute15friendlyname.setter
	def attribute15friendlyname(self, attribute15friendlyname) :
		r"""User-Friendly Name of attribute15 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute15friendlyname = attribute15friendlyname
		except Exception as e:
			raise e

	@property
	def attribute15format(self) :
		r"""Format of Attribute15 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute15format
		except Exception as e:
			raise e

	@attribute15format.setter
	def attribute15format(self, attribute15format) :
		r"""Format of Attribute15 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute15format = attribute15format
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		r"""Name of attribute16 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		r"""Name of attribute16 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	@property
	def attribute16expr(self) :
		r"""Expression that will be evaluated to obtain attribute16's value to be sent in Assertion.<br/>Maximum length =  128.
		"""
		try :
			return self._attribute16expr
		except Exception as e:
			raise e

	@attribute16expr.setter
	def attribute16expr(self, attribute16expr) :
		r"""Expression that will be evaluated to obtain attribute16's value to be sent in Assertion.<br/>Maximum length =  128
		"""
		try :
			self._attribute16expr = attribute16expr
		except Exception as e:
			raise e

	@property
	def attribute16friendlyname(self) :
		r"""User-Friendly Name of attribute16 that needs to be sent in SAML Assertion.
		"""
		try :
			return self._attribute16friendlyname
		except Exception as e:
			raise e

	@attribute16friendlyname.setter
	def attribute16friendlyname(self, attribute16friendlyname) :
		r"""User-Friendly Name of attribute16 that needs to be sent in SAML Assertion.
		"""
		try :
			self._attribute16friendlyname = attribute16friendlyname
		except Exception as e:
			raise e

	@property
	def attribute16format(self) :
		r"""Format of Attribute16 to be sent in Assertion.<br/>Possible values = URI, Basic.
		"""
		try :
			return self._attribute16format
		except Exception as e:
			raise e

	@attribute16format.setter
	def attribute16format(self, attribute16format) :
		r"""Format of Attribute16 to be sent in Assertion.<br/>Possible values = URI, Basic
		"""
		try :
			self._attribute16format = attribute16format
		except Exception as e:
			raise e

	@property
	def encryptassertion(self) :
		r"""Option to encrypt assertion when Citrix ADC IDP sends one.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._encryptassertion
		except Exception as e:
			raise e

	@encryptassertion.setter
	def encryptassertion(self, encryptassertion) :
		r"""Option to encrypt assertion when Citrix ADC IDP sends one.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._encryptassertion = encryptassertion
		except Exception as e:
			raise e

	@property
	def encryptionalgorithm(self) :
		r"""Algorithm to be used to encrypt SAML assertion.<br/>Default value: AES256<br/>Possible values = DES3, AES128, AES192, AES256.
		"""
		try :
			return self._encryptionalgorithm
		except Exception as e:
			raise e

	@encryptionalgorithm.setter
	def encryptionalgorithm(self, encryptionalgorithm) :
		r"""Algorithm to be used to encrypt SAML assertion.<br/>Default value: AES256<br/>Possible values = DES3, AES128, AES192, AES256
		"""
		try :
			self._encryptionalgorithm = encryptionalgorithm
		except Exception as e:
			raise e

	@property
	def samlbinding(self) :
		r"""This element specifies the transport mechanism of saml messages.<br/>Default value: POST<br/>Possible values = REDIRECT, POST, ARTIFACT.
		"""
		try :
			return self._samlbinding
		except Exception as e:
			raise e

	@samlbinding.setter
	def samlbinding(self, samlbinding) :
		r"""This element specifies the transport mechanism of saml messages.<br/>Default value: POST<br/>Possible values = REDIRECT, POST, ARTIFACT
		"""
		try :
			self._samlbinding = samlbinding
		except Exception as e:
			raise e

	@property
	def skewtime(self) :
		r"""This option specifies the number of minutes on either side of current time that the assertion would be valid. For example, if skewTime is 10, then assertion would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5.
		"""
		try :
			return self._skewtime
		except Exception as e:
			raise e

	@skewtime.setter
	def skewtime(self, skewtime) :
		r"""This option specifies the number of minutes on either side of current time that the assertion would be valid. For example, if skewTime is 10, then assertion would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5
		"""
		try :
			self._skewtime = skewtime
		except Exception as e:
			raise e

	@property
	def serviceproviderid(self) :
		r"""Unique identifier of the Service Provider that sends SAML Request. Citrix ADC will ensure that the Issuer of the SAML Request matches this URI.<br/>Minimum length =  1.
		"""
		try :
			return self._serviceproviderid
		except Exception as e:
			raise e

	@serviceproviderid.setter
	def serviceproviderid(self, serviceproviderid) :
		r"""Unique identifier of the Service Provider that sends SAML Request. Citrix ADC will ensure that the Issuer of the SAML Request matches this URI.<br/>Minimum length =  1
		"""
		try :
			self._serviceproviderid = serviceproviderid
		except Exception as e:
			raise e

	@property
	def signassertion(self) :
		r"""Option to sign portions of assertion when Citrix ADC IDP sends one. Based on the user selection, either Assertion or Response or Both or none can be signed.<br/>Default value: ASSERTION<br/>Possible values = NONE, ASSERTION, RESPONSE, BOTH.
		"""
		try :
			return self._signassertion
		except Exception as e:
			raise e

	@signassertion.setter
	def signassertion(self, signassertion) :
		r"""Option to sign portions of assertion when Citrix ADC IDP sends one. Based on the user selection, either Assertion or Response or Both or none can be signed.<br/>Default value: ASSERTION<br/>Possible values = NONE, ASSERTION, RESPONSE, BOTH
		"""
		try :
			self._signassertion = signassertion
		except Exception as e:
			raise e

	@property
	def keytransportalg(self) :
		r"""Key transport algorithm to be used in encryption of SAML assertion.<br/>Default value: RSA_OAEP<br/>Possible values = RSA-V1_5, RSA_OAEP.
		"""
		try :
			return self._keytransportalg
		except Exception as e:
			raise e

	@keytransportalg.setter
	def keytransportalg(self, keytransportalg) :
		r"""Key transport algorithm to be used in encryption of SAML assertion.<br/>Default value: RSA_OAEP<br/>Possible values = RSA-V1_5, RSA_OAEP
		"""
		try :
			self._keytransportalg = keytransportalg
		except Exception as e:
			raise e

	@property
	def splogouturl(self) :
		r"""Endpoint on the ServiceProvider (SP) to which logout messages are to be sent.<br/>Minimum length =  1.
		"""
		try :
			return self._splogouturl
		except Exception as e:
			raise e

	@splogouturl.setter
	def splogouturl(self, splogouturl) :
		r"""Endpoint on the ServiceProvider (SP) to which logout messages are to be sent.<br/>Minimum length =  1
		"""
		try :
			self._splogouturl = splogouturl
		except Exception as e:
			raise e

	@property
	def logoutbinding(self) :
		r"""This element specifies the transport mechanism of saml logout messages.<br/>Default value: POST<br/>Possible values = REDIRECT, POST.
		"""
		try :
			return self._logoutbinding
		except Exception as e:
			raise e

	@logoutbinding.setter
	def logoutbinding(self, logoutbinding) :
		r"""This element specifies the transport mechanism of saml logout messages.<br/>Default value: POST<br/>Possible values = REDIRECT, POST
		"""
		try :
			self._logoutbinding = logoutbinding
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups. This group can be used in policies to select specific authentication policy during logon.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups. This group can be used in policies to select specific authentication policy during logon.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def metadataurl(self) :
		r"""This URL is used for obtaining samlidp metadata.
		"""
		try :
			return self._metadataurl
		except Exception as e:
			raise e

	@metadataurl.setter
	def metadataurl(self, metadataurl) :
		r"""This URL is used for obtaining samlidp metadata.
		"""
		try :
			self._metadataurl = metadataurl
		except Exception as e:
			raise e

	@property
	def metadatarefreshinterval(self) :
		r"""Interval in minute for fetching metadata from specified metadata URL.<br/>Default value: 3600.
		"""
		try :
			return self._metadatarefreshinterval
		except Exception as e:
			raise e

	@metadatarefreshinterval.setter
	def metadatarefreshinterval(self, metadatarefreshinterval) :
		r"""Interval in minute for fetching metadata from specified metadata URL.<br/>Default value: 3600
		"""
		try :
			self._metadatarefreshinterval = metadatarefreshinterval
		except Exception as e:
			raise e

	@property
	def signatureservice(self) :
		r"""Name of the service in cloud used to sign the data.<br/>Minimum length =  1.
		"""
		try :
			return self._signatureservice
		except Exception as e:
			raise e

	@signatureservice.setter
	def signatureservice(self, signatureservice) :
		r"""Name of the service in cloud used to sign the data.<br/>Minimum length =  1
		"""
		try :
			self._signatureservice = signatureservice
		except Exception as e:
			raise e

	@property
	def samlsigningcertversion(self) :
		r"""version of the certificate in signature service used to sign the SAMLResposne that is sent to Relying Party or Service Provider after successful authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._samlsigningcertversion
		except Exception as e:
			raise e

	@samlsigningcertversion.setter
	def samlsigningcertversion(self, samlsigningcertversion) :
		r"""version of the certificate in signature service used to sign the SAMLResposne that is sent to Relying Party or Service Provider after successful authentication.<br/>Minimum length =  1
		"""
		try :
			self._samlsigningcertversion = samlsigningcertversion
		except Exception as e:
			raise e

	@property
	def samlspcertversion(self) :
		r"""version of the certificate in signature service used to verify the signature of the incoming AuthnRequest from a Relying Party or Service Provider.<br/>Minimum length =  1.
		"""
		try :
			return self._samlspcertversion
		except Exception as e:
			raise e

	@samlspcertversion.setter
	def samlspcertversion(self, samlspcertversion) :
		r"""version of the certificate in signature service used to verify the signature of the incoming AuthnRequest from a Relying Party or Service Provider.<br/>Minimum length =  1
		"""
		try :
			self._samlspcertversion = samlspcertversion
		except Exception as e:
			raise e

	@property
	def metadataimportstatus(self) :
		r"""Describes metadata import status.<br/>Default value: INIT<br/>Possible values = INIT, SUCCESS, FAIL.
		"""
		try :
			return self._metadataimportstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationsamlidpprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationsamlidpprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add authenticationsamlidpprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationsamlidpprofile()
				addresource.name = resource.name
				addresource.samlspcertname = resource.samlspcertname
				addresource.samlidpcertname = resource.samlidpcertname
				addresource.assertionconsumerserviceurl = resource.assertionconsumerserviceurl
				addresource.sendpassword = resource.sendpassword
				addresource.samlissuername = resource.samlissuername
				addresource.rejectunsignedrequests = resource.rejectunsignedrequests
				addresource.signaturealg = resource.signaturealg
				addresource.digestmethod = resource.digestmethod
				addresource.audience = resource.audience
				addresource.nameidformat = resource.nameidformat
				addresource.nameidexpr = resource.nameidexpr
				addresource.attribute1 = resource.attribute1
				addresource.attribute1expr = resource.attribute1expr
				addresource.attribute1friendlyname = resource.attribute1friendlyname
				addresource.attribute1format = resource.attribute1format
				addresource.attribute2 = resource.attribute2
				addresource.attribute2expr = resource.attribute2expr
				addresource.attribute2friendlyname = resource.attribute2friendlyname
				addresource.attribute2format = resource.attribute2format
				addresource.attribute3 = resource.attribute3
				addresource.attribute3expr = resource.attribute3expr
				addresource.attribute3friendlyname = resource.attribute3friendlyname
				addresource.attribute3format = resource.attribute3format
				addresource.attribute4 = resource.attribute4
				addresource.attribute4expr = resource.attribute4expr
				addresource.attribute4friendlyname = resource.attribute4friendlyname
				addresource.attribute4format = resource.attribute4format
				addresource.attribute5 = resource.attribute5
				addresource.attribute5expr = resource.attribute5expr
				addresource.attribute5friendlyname = resource.attribute5friendlyname
				addresource.attribute5format = resource.attribute5format
				addresource.attribute6 = resource.attribute6
				addresource.attribute6expr = resource.attribute6expr
				addresource.attribute6friendlyname = resource.attribute6friendlyname
				addresource.attribute6format = resource.attribute6format
				addresource.attribute7 = resource.attribute7
				addresource.attribute7expr = resource.attribute7expr
				addresource.attribute7friendlyname = resource.attribute7friendlyname
				addresource.attribute7format = resource.attribute7format
				addresource.attribute8 = resource.attribute8
				addresource.attribute8expr = resource.attribute8expr
				addresource.attribute8friendlyname = resource.attribute8friendlyname
				addresource.attribute8format = resource.attribute8format
				addresource.attribute9 = resource.attribute9
				addresource.attribute9expr = resource.attribute9expr
				addresource.attribute9friendlyname = resource.attribute9friendlyname
				addresource.attribute9format = resource.attribute9format
				addresource.attribute10 = resource.attribute10
				addresource.attribute10expr = resource.attribute10expr
				addresource.attribute10friendlyname = resource.attribute10friendlyname
				addresource.attribute10format = resource.attribute10format
				addresource.attribute11 = resource.attribute11
				addresource.attribute11expr = resource.attribute11expr
				addresource.attribute11friendlyname = resource.attribute11friendlyname
				addresource.attribute11format = resource.attribute11format
				addresource.attribute12 = resource.attribute12
				addresource.attribute12expr = resource.attribute12expr
				addresource.attribute12friendlyname = resource.attribute12friendlyname
				addresource.attribute12format = resource.attribute12format
				addresource.attribute13 = resource.attribute13
				addresource.attribute13expr = resource.attribute13expr
				addresource.attribute13friendlyname = resource.attribute13friendlyname
				addresource.attribute13format = resource.attribute13format
				addresource.attribute14 = resource.attribute14
				addresource.attribute14expr = resource.attribute14expr
				addresource.attribute14friendlyname = resource.attribute14friendlyname
				addresource.attribute14format = resource.attribute14format
				addresource.attribute15 = resource.attribute15
				addresource.attribute15expr = resource.attribute15expr
				addresource.attribute15friendlyname = resource.attribute15friendlyname
				addresource.attribute15format = resource.attribute15format
				addresource.attribute16 = resource.attribute16
				addresource.attribute16expr = resource.attribute16expr
				addresource.attribute16friendlyname = resource.attribute16friendlyname
				addresource.attribute16format = resource.attribute16format
				addresource.encryptassertion = resource.encryptassertion
				addresource.encryptionalgorithm = resource.encryptionalgorithm
				addresource.samlbinding = resource.samlbinding
				addresource.skewtime = resource.skewtime
				addresource.serviceproviderid = resource.serviceproviderid
				addresource.signassertion = resource.signassertion
				addresource.keytransportalg = resource.keytransportalg
				addresource.splogouturl = resource.splogouturl
				addresource.logoutbinding = resource.logoutbinding
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.metadataurl = resource.metadataurl
				addresource.metadatarefreshinterval = resource.metadatarefreshinterval
				addresource.signatureservice = resource.signatureservice
				addresource.samlsigningcertversion = resource.samlsigningcertversion
				addresource.samlspcertversion = resource.samlspcertversion
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationsamlidpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].samlspcertname = resource[i].samlspcertname
						addresources[i].samlidpcertname = resource[i].samlidpcertname
						addresources[i].assertionconsumerserviceurl = resource[i].assertionconsumerserviceurl
						addresources[i].sendpassword = resource[i].sendpassword
						addresources[i].samlissuername = resource[i].samlissuername
						addresources[i].rejectunsignedrequests = resource[i].rejectunsignedrequests
						addresources[i].signaturealg = resource[i].signaturealg
						addresources[i].digestmethod = resource[i].digestmethod
						addresources[i].audience = resource[i].audience
						addresources[i].nameidformat = resource[i].nameidformat
						addresources[i].nameidexpr = resource[i].nameidexpr
						addresources[i].attribute1 = resource[i].attribute1
						addresources[i].attribute1expr = resource[i].attribute1expr
						addresources[i].attribute1friendlyname = resource[i].attribute1friendlyname
						addresources[i].attribute1format = resource[i].attribute1format
						addresources[i].attribute2 = resource[i].attribute2
						addresources[i].attribute2expr = resource[i].attribute2expr
						addresources[i].attribute2friendlyname = resource[i].attribute2friendlyname
						addresources[i].attribute2format = resource[i].attribute2format
						addresources[i].attribute3 = resource[i].attribute3
						addresources[i].attribute3expr = resource[i].attribute3expr
						addresources[i].attribute3friendlyname = resource[i].attribute3friendlyname
						addresources[i].attribute3format = resource[i].attribute3format
						addresources[i].attribute4 = resource[i].attribute4
						addresources[i].attribute4expr = resource[i].attribute4expr
						addresources[i].attribute4friendlyname = resource[i].attribute4friendlyname
						addresources[i].attribute4format = resource[i].attribute4format
						addresources[i].attribute5 = resource[i].attribute5
						addresources[i].attribute5expr = resource[i].attribute5expr
						addresources[i].attribute5friendlyname = resource[i].attribute5friendlyname
						addresources[i].attribute5format = resource[i].attribute5format
						addresources[i].attribute6 = resource[i].attribute6
						addresources[i].attribute6expr = resource[i].attribute6expr
						addresources[i].attribute6friendlyname = resource[i].attribute6friendlyname
						addresources[i].attribute6format = resource[i].attribute6format
						addresources[i].attribute7 = resource[i].attribute7
						addresources[i].attribute7expr = resource[i].attribute7expr
						addresources[i].attribute7friendlyname = resource[i].attribute7friendlyname
						addresources[i].attribute7format = resource[i].attribute7format
						addresources[i].attribute8 = resource[i].attribute8
						addresources[i].attribute8expr = resource[i].attribute8expr
						addresources[i].attribute8friendlyname = resource[i].attribute8friendlyname
						addresources[i].attribute8format = resource[i].attribute8format
						addresources[i].attribute9 = resource[i].attribute9
						addresources[i].attribute9expr = resource[i].attribute9expr
						addresources[i].attribute9friendlyname = resource[i].attribute9friendlyname
						addresources[i].attribute9format = resource[i].attribute9format
						addresources[i].attribute10 = resource[i].attribute10
						addresources[i].attribute10expr = resource[i].attribute10expr
						addresources[i].attribute10friendlyname = resource[i].attribute10friendlyname
						addresources[i].attribute10format = resource[i].attribute10format
						addresources[i].attribute11 = resource[i].attribute11
						addresources[i].attribute11expr = resource[i].attribute11expr
						addresources[i].attribute11friendlyname = resource[i].attribute11friendlyname
						addresources[i].attribute11format = resource[i].attribute11format
						addresources[i].attribute12 = resource[i].attribute12
						addresources[i].attribute12expr = resource[i].attribute12expr
						addresources[i].attribute12friendlyname = resource[i].attribute12friendlyname
						addresources[i].attribute12format = resource[i].attribute12format
						addresources[i].attribute13 = resource[i].attribute13
						addresources[i].attribute13expr = resource[i].attribute13expr
						addresources[i].attribute13friendlyname = resource[i].attribute13friendlyname
						addresources[i].attribute13format = resource[i].attribute13format
						addresources[i].attribute14 = resource[i].attribute14
						addresources[i].attribute14expr = resource[i].attribute14expr
						addresources[i].attribute14friendlyname = resource[i].attribute14friendlyname
						addresources[i].attribute14format = resource[i].attribute14format
						addresources[i].attribute15 = resource[i].attribute15
						addresources[i].attribute15expr = resource[i].attribute15expr
						addresources[i].attribute15friendlyname = resource[i].attribute15friendlyname
						addresources[i].attribute15format = resource[i].attribute15format
						addresources[i].attribute16 = resource[i].attribute16
						addresources[i].attribute16expr = resource[i].attribute16expr
						addresources[i].attribute16friendlyname = resource[i].attribute16friendlyname
						addresources[i].attribute16format = resource[i].attribute16format
						addresources[i].encryptassertion = resource[i].encryptassertion
						addresources[i].encryptionalgorithm = resource[i].encryptionalgorithm
						addresources[i].samlbinding = resource[i].samlbinding
						addresources[i].skewtime = resource[i].skewtime
						addresources[i].serviceproviderid = resource[i].serviceproviderid
						addresources[i].signassertion = resource[i].signassertion
						addresources[i].keytransportalg = resource[i].keytransportalg
						addresources[i].splogouturl = resource[i].splogouturl
						addresources[i].logoutbinding = resource[i].logoutbinding
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].metadataurl = resource[i].metadataurl
						addresources[i].metadatarefreshinterval = resource[i].metadatarefreshinterval
						addresources[i].signatureservice = resource[i].signatureservice
						addresources[i].samlsigningcertversion = resource[i].samlsigningcertversion
						addresources[i].samlspcertversion = resource[i].samlspcertversion
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationsamlidpprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationsamlidpprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationsamlidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationsamlidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationsamlidpprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationsamlidpprofile()
				updateresource.name = resource.name
				updateresource.samlspcertname = resource.samlspcertname
				updateresource.samlidpcertname = resource.samlidpcertname
				updateresource.assertionconsumerserviceurl = resource.assertionconsumerserviceurl
				updateresource.sendpassword = resource.sendpassword
				updateresource.samlissuername = resource.samlissuername
				updateresource.rejectunsignedrequests = resource.rejectunsignedrequests
				updateresource.signaturealg = resource.signaturealg
				updateresource.digestmethod = resource.digestmethod
				updateresource.audience = resource.audience
				updateresource.nameidformat = resource.nameidformat
				updateresource.nameidexpr = resource.nameidexpr
				updateresource.attribute1 = resource.attribute1
				updateresource.attribute1expr = resource.attribute1expr
				updateresource.attribute1friendlyname = resource.attribute1friendlyname
				updateresource.attribute1format = resource.attribute1format
				updateresource.attribute2 = resource.attribute2
				updateresource.attribute2expr = resource.attribute2expr
				updateresource.attribute2friendlyname = resource.attribute2friendlyname
				updateresource.attribute2format = resource.attribute2format
				updateresource.attribute3 = resource.attribute3
				updateresource.attribute3expr = resource.attribute3expr
				updateresource.attribute3friendlyname = resource.attribute3friendlyname
				updateresource.attribute3format = resource.attribute3format
				updateresource.attribute4 = resource.attribute4
				updateresource.attribute4expr = resource.attribute4expr
				updateresource.attribute4friendlyname = resource.attribute4friendlyname
				updateresource.attribute4format = resource.attribute4format
				updateresource.attribute5 = resource.attribute5
				updateresource.attribute5expr = resource.attribute5expr
				updateresource.attribute5friendlyname = resource.attribute5friendlyname
				updateresource.attribute5format = resource.attribute5format
				updateresource.attribute6 = resource.attribute6
				updateresource.attribute6expr = resource.attribute6expr
				updateresource.attribute6friendlyname = resource.attribute6friendlyname
				updateresource.attribute6format = resource.attribute6format
				updateresource.attribute7 = resource.attribute7
				updateresource.attribute7expr = resource.attribute7expr
				updateresource.attribute7friendlyname = resource.attribute7friendlyname
				updateresource.attribute7format = resource.attribute7format
				updateresource.attribute8 = resource.attribute8
				updateresource.attribute8expr = resource.attribute8expr
				updateresource.attribute8friendlyname = resource.attribute8friendlyname
				updateresource.attribute8format = resource.attribute8format
				updateresource.attribute9 = resource.attribute9
				updateresource.attribute9expr = resource.attribute9expr
				updateresource.attribute9friendlyname = resource.attribute9friendlyname
				updateresource.attribute9format = resource.attribute9format
				updateresource.attribute10 = resource.attribute10
				updateresource.attribute10expr = resource.attribute10expr
				updateresource.attribute10friendlyname = resource.attribute10friendlyname
				updateresource.attribute10format = resource.attribute10format
				updateresource.attribute11 = resource.attribute11
				updateresource.attribute11expr = resource.attribute11expr
				updateresource.attribute11friendlyname = resource.attribute11friendlyname
				updateresource.attribute11format = resource.attribute11format
				updateresource.attribute12 = resource.attribute12
				updateresource.attribute12expr = resource.attribute12expr
				updateresource.attribute12friendlyname = resource.attribute12friendlyname
				updateresource.attribute12format = resource.attribute12format
				updateresource.attribute13 = resource.attribute13
				updateresource.attribute13expr = resource.attribute13expr
				updateresource.attribute13friendlyname = resource.attribute13friendlyname
				updateresource.attribute13format = resource.attribute13format
				updateresource.attribute14 = resource.attribute14
				updateresource.attribute14expr = resource.attribute14expr
				updateresource.attribute14friendlyname = resource.attribute14friendlyname
				updateresource.attribute14format = resource.attribute14format
				updateresource.attribute15 = resource.attribute15
				updateresource.attribute15expr = resource.attribute15expr
				updateresource.attribute15friendlyname = resource.attribute15friendlyname
				updateresource.attribute15format = resource.attribute15format
				updateresource.attribute16 = resource.attribute16
				updateresource.attribute16expr = resource.attribute16expr
				updateresource.attribute16friendlyname = resource.attribute16friendlyname
				updateresource.attribute16format = resource.attribute16format
				updateresource.encryptassertion = resource.encryptassertion
				updateresource.encryptionalgorithm = resource.encryptionalgorithm
				updateresource.samlbinding = resource.samlbinding
				updateresource.skewtime = resource.skewtime
				updateresource.serviceproviderid = resource.serviceproviderid
				updateresource.signassertion = resource.signassertion
				updateresource.keytransportalg = resource.keytransportalg
				updateresource.splogouturl = resource.splogouturl
				updateresource.logoutbinding = resource.logoutbinding
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.metadataurl = resource.metadataurl
				updateresource.metadatarefreshinterval = resource.metadatarefreshinterval
				updateresource.signatureservice = resource.signatureservice
				updateresource.samlsigningcertversion = resource.samlsigningcertversion
				updateresource.samlspcertversion = resource.samlspcertversion
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationsamlidpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].samlspcertname = resource[i].samlspcertname
						updateresources[i].samlidpcertname = resource[i].samlidpcertname
						updateresources[i].assertionconsumerserviceurl = resource[i].assertionconsumerserviceurl
						updateresources[i].sendpassword = resource[i].sendpassword
						updateresources[i].samlissuername = resource[i].samlissuername
						updateresources[i].rejectunsignedrequests = resource[i].rejectunsignedrequests
						updateresources[i].signaturealg = resource[i].signaturealg
						updateresources[i].digestmethod = resource[i].digestmethod
						updateresources[i].audience = resource[i].audience
						updateresources[i].nameidformat = resource[i].nameidformat
						updateresources[i].nameidexpr = resource[i].nameidexpr
						updateresources[i].attribute1 = resource[i].attribute1
						updateresources[i].attribute1expr = resource[i].attribute1expr
						updateresources[i].attribute1friendlyname = resource[i].attribute1friendlyname
						updateresources[i].attribute1format = resource[i].attribute1format
						updateresources[i].attribute2 = resource[i].attribute2
						updateresources[i].attribute2expr = resource[i].attribute2expr
						updateresources[i].attribute2friendlyname = resource[i].attribute2friendlyname
						updateresources[i].attribute2format = resource[i].attribute2format
						updateresources[i].attribute3 = resource[i].attribute3
						updateresources[i].attribute3expr = resource[i].attribute3expr
						updateresources[i].attribute3friendlyname = resource[i].attribute3friendlyname
						updateresources[i].attribute3format = resource[i].attribute3format
						updateresources[i].attribute4 = resource[i].attribute4
						updateresources[i].attribute4expr = resource[i].attribute4expr
						updateresources[i].attribute4friendlyname = resource[i].attribute4friendlyname
						updateresources[i].attribute4format = resource[i].attribute4format
						updateresources[i].attribute5 = resource[i].attribute5
						updateresources[i].attribute5expr = resource[i].attribute5expr
						updateresources[i].attribute5friendlyname = resource[i].attribute5friendlyname
						updateresources[i].attribute5format = resource[i].attribute5format
						updateresources[i].attribute6 = resource[i].attribute6
						updateresources[i].attribute6expr = resource[i].attribute6expr
						updateresources[i].attribute6friendlyname = resource[i].attribute6friendlyname
						updateresources[i].attribute6format = resource[i].attribute6format
						updateresources[i].attribute7 = resource[i].attribute7
						updateresources[i].attribute7expr = resource[i].attribute7expr
						updateresources[i].attribute7friendlyname = resource[i].attribute7friendlyname
						updateresources[i].attribute7format = resource[i].attribute7format
						updateresources[i].attribute8 = resource[i].attribute8
						updateresources[i].attribute8expr = resource[i].attribute8expr
						updateresources[i].attribute8friendlyname = resource[i].attribute8friendlyname
						updateresources[i].attribute8format = resource[i].attribute8format
						updateresources[i].attribute9 = resource[i].attribute9
						updateresources[i].attribute9expr = resource[i].attribute9expr
						updateresources[i].attribute9friendlyname = resource[i].attribute9friendlyname
						updateresources[i].attribute9format = resource[i].attribute9format
						updateresources[i].attribute10 = resource[i].attribute10
						updateresources[i].attribute10expr = resource[i].attribute10expr
						updateresources[i].attribute10friendlyname = resource[i].attribute10friendlyname
						updateresources[i].attribute10format = resource[i].attribute10format
						updateresources[i].attribute11 = resource[i].attribute11
						updateresources[i].attribute11expr = resource[i].attribute11expr
						updateresources[i].attribute11friendlyname = resource[i].attribute11friendlyname
						updateresources[i].attribute11format = resource[i].attribute11format
						updateresources[i].attribute12 = resource[i].attribute12
						updateresources[i].attribute12expr = resource[i].attribute12expr
						updateresources[i].attribute12friendlyname = resource[i].attribute12friendlyname
						updateresources[i].attribute12format = resource[i].attribute12format
						updateresources[i].attribute13 = resource[i].attribute13
						updateresources[i].attribute13expr = resource[i].attribute13expr
						updateresources[i].attribute13friendlyname = resource[i].attribute13friendlyname
						updateresources[i].attribute13format = resource[i].attribute13format
						updateresources[i].attribute14 = resource[i].attribute14
						updateresources[i].attribute14expr = resource[i].attribute14expr
						updateresources[i].attribute14friendlyname = resource[i].attribute14friendlyname
						updateresources[i].attribute14format = resource[i].attribute14format
						updateresources[i].attribute15 = resource[i].attribute15
						updateresources[i].attribute15expr = resource[i].attribute15expr
						updateresources[i].attribute15friendlyname = resource[i].attribute15friendlyname
						updateresources[i].attribute15format = resource[i].attribute15format
						updateresources[i].attribute16 = resource[i].attribute16
						updateresources[i].attribute16expr = resource[i].attribute16expr
						updateresources[i].attribute16friendlyname = resource[i].attribute16friendlyname
						updateresources[i].attribute16format = resource[i].attribute16format
						updateresources[i].encryptassertion = resource[i].encryptassertion
						updateresources[i].encryptionalgorithm = resource[i].encryptionalgorithm
						updateresources[i].samlbinding = resource[i].samlbinding
						updateresources[i].skewtime = resource[i].skewtime
						updateresources[i].serviceproviderid = resource[i].serviceproviderid
						updateresources[i].signassertion = resource[i].signassertion
						updateresources[i].keytransportalg = resource[i].keytransportalg
						updateresources[i].splogouturl = resource[i].splogouturl
						updateresources[i].logoutbinding = resource[i].logoutbinding
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].metadataurl = resource[i].metadataurl
						updateresources[i].metadatarefreshinterval = resource[i].metadatarefreshinterval
						updateresources[i].signatureservice = resource[i].signatureservice
						updateresources[i].samlsigningcertversion = resource[i].samlsigningcertversion
						updateresources[i].samlspcertversion = resource[i].samlspcertversion
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationsamlidpprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationsamlidpprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationsamlidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationsamlidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationsamlidpprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationsamlidpprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationsamlidpprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationsamlidpprofile() for _ in range(len(name))]
						obj = [authenticationsamlidpprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationsamlidpprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationsamlidpprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationsamlidpprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationsamlidpprofile resources configured on NetScaler.
		"""
		try :
			obj = authenticationsamlidpprofile()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of authenticationsamlidpprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationsamlidpprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Attribute3format:
		URI = "URI"
		Basic = "Basic"

	class Signassertion:
		NONE = "NONE"
		ASSERTION = "ASSERTION"
		RESPONSE = "RESPONSE"
		BOTH = "BOTH"

	class Encryptassertion:
		ON = "ON"
		OFF = "OFF"

	class Attribute6format:
		URI = "URI"
		Basic = "Basic"

	class Nameidformat:
		Unspecified = "Unspecified"
		emailAddress = "emailAddress"
		X509SubjectName = "X509SubjectName"
		WindowsDomainQualifiedName = "WindowsDomainQualifiedName"
		kerberos = "kerberos"
		entity = "entity"
		persistent = "persistent"
		Transient = "transient"

	class Attribute1format:
		URI = "URI"
		Basic = "Basic"

	class Attribute12format:
		URI = "URI"
		Basic = "Basic"

	class Attribute7format:
		URI = "URI"
		Basic = "Basic"

	class Attribute15format:
		URI = "URI"
		Basic = "Basic"

	class Digestmethod:
		SHA1 = "SHA1"
		SHA256 = "SHA256"

	class Rejectunsignedrequests:
		ON = "ON"
		OFF = "OFF"

	class Attribute4format:
		URI = "URI"
		Basic = "Basic"

	class Metadataimportstatus:
		INIT = "INIT"
		SUCCESS = "SUCCESS"
		FAIL = "FAIL"

	class Attribute13format:
		URI = "URI"
		Basic = "Basic"

	class Attribute14format:
		URI = "URI"
		Basic = "Basic"

	class Encryptionalgorithm:
		DES3 = "DES3"
		AES128 = "AES128"
		AES192 = "AES192"
		AES256 = "AES256"

	class Sendpassword:
		ON = "ON"
		OFF = "OFF"

	class Keytransportalg:
		RSA_V1_5 = "RSA-V1_5"
		RSA_OAEP = "RSA_OAEP"

	class Attribute10format:
		URI = "URI"
		Basic = "Basic"

	class Attribute9format:
		URI = "URI"
		Basic = "Basic"

	class Signaturealg:
		RSA_SHA1 = "RSA-SHA1"
		RSA_SHA256 = "RSA-SHA256"

	class Attribute8format:
		URI = "URI"
		Basic = "Basic"

	class Attribute5format:
		URI = "URI"
		Basic = "Basic"

	class Samlbinding:
		REDIRECT = "REDIRECT"
		POST = "POST"
		ARTIFACT = "ARTIFACT"

	class Attribute2format:
		URI = "URI"
		Basic = "Basic"

	class Logoutbinding:
		REDIRECT = "REDIRECT"
		POST = "POST"

	class Attribute16format:
		URI = "URI"
		Basic = "Basic"

	class Attribute11format:
		URI = "URI"
		Basic = "Basic"

class authenticationsamlidpprofile_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationsamlidpprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationsamlidpprofile = [authenticationsamlidpprofile() for _ in range(length)]

