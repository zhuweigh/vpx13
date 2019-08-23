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

class authenticationsamlaction(base_resource) :
	""" Configuration for AAA Saml action resource. """
	def __init__(self) :
		self._name = None
		self._samlidpcertname = None
		self._samlsigningcertname = None
		self._samlredirecturl = None
		self._samlacsindex = None
		self._samluserfield = None
		self._samlrejectunsignedassertion = None
		self._samlissuername = None
		self._samltwofactor = None
		self._defaultauthenticationgroup = None
		self._attribute1 = None
		self._attribute2 = None
		self._attribute3 = None
		self._attribute4 = None
		self._attribute5 = None
		self._attribute6 = None
		self._attribute7 = None
		self._attribute8 = None
		self._attribute9 = None
		self._attribute10 = None
		self._attribute11 = None
		self._attribute12 = None
		self._attribute13 = None
		self._attribute14 = None
		self._attribute15 = None
		self._attribute16 = None
		self._attributes = None
		self._signaturealg = None
		self._digestmethod = None
		self._requestedauthncontext = None
		self._authnctxclassref = None
		self._samlbinding = None
		self._attributeconsumingserviceindex = None
		self._sendthumbprint = None
		self._enforceusername = None
		self._logouturl = None
		self._artifactresolutionserviceurl = None
		self._skewtime = None
		self._logoutbinding = None
		self._forceauthn = None
		self._groupnamefield = None
		self._audience = None
		self._metadataurl = None
		self._metadatarefreshinterval = None
		self._storesamlresponse = None
		self._metadataimportstatus = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the SAML server profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after SAML profile is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the SAML server profile (action). 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after SAML profile is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def samlidpcertname(self) :
		r"""Name of the SSL certificate used to verify responses from SAML Identity Provider (IdP).<br/>Minimum length =  1.
		"""
		try :
			return self._samlidpcertname
		except Exception as e:
			raise e

	@samlidpcertname.setter
	def samlidpcertname(self, samlidpcertname) :
		r"""Name of the SSL certificate used to verify responses from SAML Identity Provider (IdP).<br/>Minimum length =  1
		"""
		try :
			self._samlidpcertname = samlidpcertname
		except Exception as e:
			raise e

	@property
	def samlsigningcertname(self) :
		r"""Name of the SSL certificate to sign requests from ServiceProvider (SP) to Identity Provider (IdP).<br/>Minimum length =  1.
		"""
		try :
			return self._samlsigningcertname
		except Exception as e:
			raise e

	@samlsigningcertname.setter
	def samlsigningcertname(self, samlsigningcertname) :
		r"""Name of the SSL certificate to sign requests from ServiceProvider (SP) to Identity Provider (IdP).<br/>Minimum length =  1
		"""
		try :
			self._samlsigningcertname = samlsigningcertname
		except Exception as e:
			raise e

	@property
	def samlredirecturl(self) :
		r"""URL to which users are redirected for authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._samlredirecturl
		except Exception as e:
			raise e

	@samlredirecturl.setter
	def samlredirecturl(self, samlredirecturl) :
		r"""URL to which users are redirected for authentication.<br/>Minimum length =  1
		"""
		try :
			self._samlredirecturl = samlredirecturl
		except Exception as e:
			raise e

	@property
	def samlacsindex(self) :
		r"""Index/ID of the metadata entry corresponding to this configuration.<br/>Default value: 255<br/>Maximum length =  255.
		"""
		try :
			return self._samlacsindex
		except Exception as e:
			raise e

	@samlacsindex.setter
	def samlacsindex(self, samlacsindex) :
		r"""Index/ID of the metadata entry corresponding to this configuration.<br/>Default value: 255<br/>Maximum length =  255
		"""
		try :
			self._samlacsindex = samlacsindex
		except Exception as e:
			raise e

	@property
	def samluserfield(self) :
		r"""SAML user ID, as given in the SAML assertion.<br/>Minimum length =  1.
		"""
		try :
			return self._samluserfield
		except Exception as e:
			raise e

	@samluserfield.setter
	def samluserfield(self, samluserfield) :
		r"""SAML user ID, as given in the SAML assertion.<br/>Minimum length =  1
		"""
		try :
			self._samluserfield = samluserfield
		except Exception as e:
			raise e

	@property
	def samlrejectunsignedassertion(self) :
		r"""Reject unsigned SAML assertions. ON option results in rejection of Assertion that is received without signature. STRICT option ensures that both Response and Assertion are signed. OFF allows unsigned Assertions.<br/>Default value: ON<br/>Possible values = ON, OFF, STRICT.
		"""
		try :
			return self._samlrejectunsignedassertion
		except Exception as e:
			raise e

	@samlrejectunsignedassertion.setter
	def samlrejectunsignedassertion(self, samlrejectunsignedassertion) :
		r"""Reject unsigned SAML assertions. ON option results in rejection of Assertion that is received without signature. STRICT option ensures that both Response and Assertion are signed. OFF allows unsigned Assertions.<br/>Default value: ON<br/>Possible values = ON, OFF, STRICT
		"""
		try :
			self._samlrejectunsignedassertion = samlrejectunsignedassertion
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
	def samltwofactor(self) :
		r"""Option to enable second factor after SAML.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._samltwofactor
		except Exception as e:
			raise e

	@samltwofactor.setter
	def samltwofactor(self, samltwofactor) :
		r"""Option to enable second factor after SAML.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._samltwofactor = samltwofactor
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def attribute1(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute1. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute1. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute2. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute2. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute3. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute3. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute4. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute4. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute5. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute5. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute6. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute6. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute7. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute7. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute8. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute8. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute9. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute9. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute10. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute10. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute11. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute11. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute12. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute12. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute13. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute13. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute14. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute14. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute15. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute15. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute16. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		r"""Name of the attribute in SAML Assertion whose value needs to be extracted and stored as attribute16. Maximum length of the extracted attribute is 239 bytes.
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	@property
	def attributes(self) :
		r"""List of attribute names separated by ',' which needs to be extracted. 
		Note that preceeding and trailing spaces will be removed. 
		Attribute name can be 127 bytes and total length of this string should not cross 2047 bytes.
		These attributes have multi-value support separated by ',' and stored as key-value pair in AAA session.
		"""
		try :
			return self._attributes
		except Exception as e:
			raise e

	@attributes.setter
	def attributes(self, attributes) :
		r"""List of attribute names separated by ',' which needs to be extracted. 
		Note that preceeding and trailing spaces will be removed. 
		Attribute name can be 127 bytes and total length of this string should not cross 2047 bytes.
		These attributes have multi-value support separated by ',' and stored as key-value pair in AAA session.
		"""
		try :
			self._attributes = attributes
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
	def requestedauthncontext(self) :
		r"""This element specifies the authentication context requirements of authentication statements returned in the response.<br/>Default value: exact<br/>Possible values = exact, minimum, maximum, better.
		"""
		try :
			return self._requestedauthncontext
		except Exception as e:
			raise e

	@requestedauthncontext.setter
	def requestedauthncontext(self, requestedauthncontext) :
		r"""This element specifies the authentication context requirements of authentication statements returned in the response.<br/>Default value: exact<br/>Possible values = exact, minimum, maximum, better
		"""
		try :
			self._requestedauthncontext = requestedauthncontext
		except Exception as e:
			raise e

	@property
	def authnctxclassref(self) :
		r"""This element specifies the authentication class types that are requested from IdP (IdentityProvider).
		InternetProtocol: This is applicable when a principal is authenticated through the use of a provided IP address.
		InternetProtocolPassword: This is applicable when a principal is authenticated through the use of a provided IP address, in addition to a username/password.
		Kerberos: This is applicable when the principal has authenticated using a password to a local authentication authority, in order to acquire a Kerberos ticket.
		MobileOneFactorUnregistered: This indicates authentication of the mobile device without requiring explicit end-user interaction.
		MobileTwoFactorUnregistered: This indicates two-factor based authentication during mobile customer registration process, such as secure device and user PIN.
		MobileOneFactorContract: Reflects mobile contract customer registration procedures and a single factor authentication.
		MobileTwoFactorContract: Reflects mobile contract customer registration procedures and a two-factor based authentication.
		Password: This class is applicable when a principal authenticates using password over unprotected http session.
		PasswordProtectedTransport: This class is applicable when a principal authenticates to an authentication authority through the presentation of a password over a protected session.
		PreviousSession: This class is applicable when a principal had authenticated to an authentication authority at some point in the past using any authentication context.
		X509: This indicates that the principal authenticated by means of a digital signature where the key was validated as part of an X.509 Public Key Infrastructure.
		PGP: This indicates that the principal authenticated by means of a digital signature where the key was validated as part of a PGP Public Key Infrastructure.
		SPKI: This indicates that the principal authenticated by means of a digital signature where the key was validated via an SPKI Infrastructure.
		XMLDSig: This indicates that the principal authenticated by means of a digital signature according to the processing rules specified in the XML Digital Signature specification.
		Smartcard: This indicates that the principal has authenticated using smartcard.
		SmartcardPKI: This class is applicable when a principal authenticates to an authentication authority through a two-factor authentication mechanism using a smartcard with enclosed private key and a PIN.
		SoftwarePKI: This class is applicable when a principal uses an X.509 certificate stored in software to authenticate to the authentication authority.
		Telephony: This class is used to indicate that the principal authenticated via the provision of a fixed-line telephone number, transported via a telephony protocol such as ADSL.
		NomadTelephony: Indicates that the principal is "roaming" and authenticates via the means of the line number, a user suffix, and a password element.
		PersonalTelephony: This class is used to indicate that the principal authenticated via the provision of a fixed-line telephone.
		AuthenticatedTelephony: Indicates that the principal authenticated via the means of the line number, a user suffix, and a password element.
		SecureRemotePassword: This class is applicable when the authentication was performed by means of Secure Remote Password.
		TLSClient: This class indicates that the principal authenticated by means of a client certificate, secured with the SSL/TLS transport.
		TimeSyncToken: This is applicable when a principal authenticates through a time synchronization token.
		Unspecified: This indicates that the authentication was performed by unspecified means.
		Windows: This indicates that Windows integrated authentication is utilized for authentication.<br/>Possible values = InternetProtocol, InternetProtocolPassword, Kerberos, MobileOneFactorUnregistered, MobileTwoFactorUnregistered, MobileOneFactorContract, MobileTwoFactorContract, Password, PasswordProtectedTransport, PreviousSession, X509, PGP, SPKI, XMLDSig, Smartcard, SmartcardPKI, SoftwarePKI, Telephony, NomadTelephony, PersonalTelephony, AuthenticatedTelephony, SecureRemotePassword, TLSClient, TimeSyncToken, Unspecified, Windows.
		"""
		try :
			return self._authnctxclassref
		except Exception as e:
			raise e

	@authnctxclassref.setter
	def authnctxclassref(self, authnctxclassref) :
		r"""This element specifies the authentication class types that are requested from IdP (IdentityProvider).
		InternetProtocol: This is applicable when a principal is authenticated through the use of a provided IP address.
		InternetProtocolPassword: This is applicable when a principal is authenticated through the use of a provided IP address, in addition to a username/password.
		Kerberos: This is applicable when the principal has authenticated using a password to a local authentication authority, in order to acquire a Kerberos ticket.
		MobileOneFactorUnregistered: This indicates authentication of the mobile device without requiring explicit end-user interaction.
		MobileTwoFactorUnregistered: This indicates two-factor based authentication during mobile customer registration process, such as secure device and user PIN.
		MobileOneFactorContract: Reflects mobile contract customer registration procedures and a single factor authentication.
		MobileTwoFactorContract: Reflects mobile contract customer registration procedures and a two-factor based authentication.
		Password: This class is applicable when a principal authenticates using password over unprotected http session.
		PasswordProtectedTransport: This class is applicable when a principal authenticates to an authentication authority through the presentation of a password over a protected session.
		PreviousSession: This class is applicable when a principal had authenticated to an authentication authority at some point in the past using any authentication context.
		X509: This indicates that the principal authenticated by means of a digital signature where the key was validated as part of an X.509 Public Key Infrastructure.
		PGP: This indicates that the principal authenticated by means of a digital signature where the key was validated as part of a PGP Public Key Infrastructure.
		SPKI: This indicates that the principal authenticated by means of a digital signature where the key was validated via an SPKI Infrastructure.
		XMLDSig: This indicates that the principal authenticated by means of a digital signature according to the processing rules specified in the XML Digital Signature specification.
		Smartcard: This indicates that the principal has authenticated using smartcard.
		SmartcardPKI: This class is applicable when a principal authenticates to an authentication authority through a two-factor authentication mechanism using a smartcard with enclosed private key and a PIN.
		SoftwarePKI: This class is applicable when a principal uses an X.509 certificate stored in software to authenticate to the authentication authority.
		Telephony: This class is used to indicate that the principal authenticated via the provision of a fixed-line telephone number, transported via a telephony protocol such as ADSL.
		NomadTelephony: Indicates that the principal is "roaming" and authenticates via the means of the line number, a user suffix, and a password element.
		PersonalTelephony: This class is used to indicate that the principal authenticated via the provision of a fixed-line telephone.
		AuthenticatedTelephony: Indicates that the principal authenticated via the means of the line number, a user suffix, and a password element.
		SecureRemotePassword: This class is applicable when the authentication was performed by means of Secure Remote Password.
		TLSClient: This class indicates that the principal authenticated by means of a client certificate, secured with the SSL/TLS transport.
		TimeSyncToken: This is applicable when a principal authenticates through a time synchronization token.
		Unspecified: This indicates that the authentication was performed by unspecified means.
		Windows: This indicates that Windows integrated authentication is utilized for authentication.<br/>Possible values = InternetProtocol, InternetProtocolPassword, Kerberos, MobileOneFactorUnregistered, MobileTwoFactorUnregistered, MobileOneFactorContract, MobileTwoFactorContract, Password, PasswordProtectedTransport, PreviousSession, X509, PGP, SPKI, XMLDSig, Smartcard, SmartcardPKI, SoftwarePKI, Telephony, NomadTelephony, PersonalTelephony, AuthenticatedTelephony, SecureRemotePassword, TLSClient, TimeSyncToken, Unspecified, Windows
		"""
		try :
			self._authnctxclassref = authnctxclassref
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
	def attributeconsumingserviceindex(self) :
		r"""Index/ID of the attribute specification at Identity Provider (IdP). IdP will locate attributes requested by SP using this index and send those attributes in Assertion.<br/>Default value: 255<br/>Maximum length =  255.
		"""
		try :
			return self._attributeconsumingserviceindex
		except Exception as e:
			raise e

	@attributeconsumingserviceindex.setter
	def attributeconsumingserviceindex(self, attributeconsumingserviceindex) :
		r"""Index/ID of the attribute specification at Identity Provider (IdP). IdP will locate attributes requested by SP using this index and send those attributes in Assertion.<br/>Default value: 255<br/>Maximum length =  255
		"""
		try :
			self._attributeconsumingserviceindex = attributeconsumingserviceindex
		except Exception as e:
			raise e

	@property
	def sendthumbprint(self) :
		r"""Option to send thumbprint instead of x509 certificate in SAML request.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sendthumbprint
		except Exception as e:
			raise e

	@sendthumbprint.setter
	def sendthumbprint(self, sendthumbprint) :
		r"""Option to send thumbprint instead of x509 certificate in SAML request.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sendthumbprint = sendthumbprint
		except Exception as e:
			raise e

	@property
	def enforceusername(self) :
		r"""Option to choose whether the username that is extracted from SAML assertion can be edited in login page while doing second factor.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._enforceusername
		except Exception as e:
			raise e

	@enforceusername.setter
	def enforceusername(self, enforceusername) :
		r"""Option to choose whether the username that is extracted from SAML assertion can be edited in login page while doing second factor.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._enforceusername = enforceusername
		except Exception as e:
			raise e

	@property
	def logouturl(self) :
		r"""SingleLogout URL on IdP to which logoutRequest will be sent on Citrix ADC session cleanup.
		"""
		try :
			return self._logouturl
		except Exception as e:
			raise e

	@logouturl.setter
	def logouturl(self, logouturl) :
		r"""SingleLogout URL on IdP to which logoutRequest will be sent on Citrix ADC session cleanup.
		"""
		try :
			self._logouturl = logouturl
		except Exception as e:
			raise e

	@property
	def artifactresolutionserviceurl(self) :
		r"""URL of the Artifact Resolution Service on IdP to which Citrix ADC will post artifact to get actual SAML token.
		"""
		try :
			return self._artifactresolutionserviceurl
		except Exception as e:
			raise e

	@artifactresolutionserviceurl.setter
	def artifactresolutionserviceurl(self, artifactresolutionserviceurl) :
		r"""URL of the Artifact Resolution Service on IdP to which Citrix ADC will post artifact to get actual SAML token.
		"""
		try :
			self._artifactresolutionserviceurl = artifactresolutionserviceurl
		except Exception as e:
			raise e

	@property
	def skewtime(self) :
		r"""This option specifies the allowed clock skew in number of minutes that Citrix ADC ServiceProvider allows on an incoming assertion. For example, if skewTime is 10, then assertion would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5.
		"""
		try :
			return self._skewtime
		except Exception as e:
			raise e

	@skewtime.setter
	def skewtime(self, skewtime) :
		r"""This option specifies the allowed clock skew in number of minutes that Citrix ADC ServiceProvider allows on an incoming assertion. For example, if skewTime is 10, then assertion would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5
		"""
		try :
			self._skewtime = skewtime
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
	def forceauthn(self) :
		r"""Option that forces authentication at the Identity Provider (IdP) that receives Citrix ADC's request.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._forceauthn
		except Exception as e:
			raise e

	@forceauthn.setter
	def forceauthn(self, forceauthn) :
		r"""Option that forces authentication at the Identity Provider (IdP) that receives Citrix ADC's request.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._forceauthn = forceauthn
		except Exception as e:
			raise e

	@property
	def groupnamefield(self) :
		r"""Name of the tag in assertion that contains user groups.
		"""
		try :
			return self._groupnamefield
		except Exception as e:
			raise e

	@groupnamefield.setter
	def groupnamefield(self, groupnamefield) :
		r"""Name of the tag in assertion that contains user groups.
		"""
		try :
			self._groupnamefield = groupnamefield
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
	def metadataurl(self) :
		r"""This URL is used for obtaining saml metadata.
		"""
		try :
			return self._metadataurl
		except Exception as e:
			raise e

	@metadataurl.setter
	def metadataurl(self, metadataurl) :
		r"""This URL is used for obtaining saml metadata.
		"""
		try :
			self._metadataurl = metadataurl
		except Exception as e:
			raise e

	@property
	def metadatarefreshinterval(self) :
		r"""Interval in minutes for fetching metadata from specified metadata URL.<br/>Default value: 36000.
		"""
		try :
			return self._metadatarefreshinterval
		except Exception as e:
			raise e

	@metadatarefreshinterval.setter
	def metadatarefreshinterval(self, metadatarefreshinterval) :
		r"""Interval in minutes for fetching metadata from specified metadata URL.<br/>Default value: 36000
		"""
		try :
			self._metadatarefreshinterval = metadatarefreshinterval
		except Exception as e:
			raise e

	@property
	def storesamlresponse(self) :
		r"""Option to store entire SAML Response through the life of user session.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._storesamlresponse
		except Exception as e:
			raise e

	@storesamlresponse.setter
	def storesamlresponse(self, storesamlresponse) :
		r"""Option to store entire SAML Response through the life of user session.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._storesamlresponse = storesamlresponse
		except Exception as e:
			raise e

	@property
	def metadataimportstatus(self) :
		r"""Describes metadata import status.<br/>Default value: SUCCESS<br/>Possible values = INIT, SUCCESS, FAIL.
		"""
		try :
			return self._metadataimportstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationsamlaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationsamlaction
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
		r""" Use this API to add authenticationsamlaction.
		"""
		try :
			if type(resource) is not list :
				addresource = authenticationsamlaction()
				addresource.name = resource.name
				addresource.samlidpcertname = resource.samlidpcertname
				addresource.samlsigningcertname = resource.samlsigningcertname
				addresource.samlredirecturl = resource.samlredirecturl
				addresource.samlacsindex = resource.samlacsindex
				addresource.samluserfield = resource.samluserfield
				addresource.samlrejectunsignedassertion = resource.samlrejectunsignedassertion
				addresource.samlissuername = resource.samlissuername
				addresource.samltwofactor = resource.samltwofactor
				addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				addresource.attribute1 = resource.attribute1
				addresource.attribute2 = resource.attribute2
				addresource.attribute3 = resource.attribute3
				addresource.attribute4 = resource.attribute4
				addresource.attribute5 = resource.attribute5
				addresource.attribute6 = resource.attribute6
				addresource.attribute7 = resource.attribute7
				addresource.attribute8 = resource.attribute8
				addresource.attribute9 = resource.attribute9
				addresource.attribute10 = resource.attribute10
				addresource.attribute11 = resource.attribute11
				addresource.attribute12 = resource.attribute12
				addresource.attribute13 = resource.attribute13
				addresource.attribute14 = resource.attribute14
				addresource.attribute15 = resource.attribute15
				addresource.attribute16 = resource.attribute16
				addresource.attributes = resource.attributes
				addresource.signaturealg = resource.signaturealg
				addresource.digestmethod = resource.digestmethod
				addresource.requestedauthncontext = resource.requestedauthncontext
				addresource.authnctxclassref = resource.authnctxclassref
				addresource.samlbinding = resource.samlbinding
				addresource.attributeconsumingserviceindex = resource.attributeconsumingserviceindex
				addresource.sendthumbprint = resource.sendthumbprint
				addresource.enforceusername = resource.enforceusername
				addresource.logouturl = resource.logouturl
				addresource.artifactresolutionserviceurl = resource.artifactresolutionserviceurl
				addresource.skewtime = resource.skewtime
				addresource.logoutbinding = resource.logoutbinding
				addresource.forceauthn = resource.forceauthn
				addresource.groupnamefield = resource.groupnamefield
				addresource.audience = resource.audience
				addresource.metadataurl = resource.metadataurl
				addresource.metadatarefreshinterval = resource.metadatarefreshinterval
				addresource.storesamlresponse = resource.storesamlresponse
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationsamlaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].samlidpcertname = resource[i].samlidpcertname
						addresources[i].samlsigningcertname = resource[i].samlsigningcertname
						addresources[i].samlredirecturl = resource[i].samlredirecturl
						addresources[i].samlacsindex = resource[i].samlacsindex
						addresources[i].samluserfield = resource[i].samluserfield
						addresources[i].samlrejectunsignedassertion = resource[i].samlrejectunsignedassertion
						addresources[i].samlissuername = resource[i].samlissuername
						addresources[i].samltwofactor = resource[i].samltwofactor
						addresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						addresources[i].attribute1 = resource[i].attribute1
						addresources[i].attribute2 = resource[i].attribute2
						addresources[i].attribute3 = resource[i].attribute3
						addresources[i].attribute4 = resource[i].attribute4
						addresources[i].attribute5 = resource[i].attribute5
						addresources[i].attribute6 = resource[i].attribute6
						addresources[i].attribute7 = resource[i].attribute7
						addresources[i].attribute8 = resource[i].attribute8
						addresources[i].attribute9 = resource[i].attribute9
						addresources[i].attribute10 = resource[i].attribute10
						addresources[i].attribute11 = resource[i].attribute11
						addresources[i].attribute12 = resource[i].attribute12
						addresources[i].attribute13 = resource[i].attribute13
						addresources[i].attribute14 = resource[i].attribute14
						addresources[i].attribute15 = resource[i].attribute15
						addresources[i].attribute16 = resource[i].attribute16
						addresources[i].attributes = resource[i].attributes
						addresources[i].signaturealg = resource[i].signaturealg
						addresources[i].digestmethod = resource[i].digestmethod
						addresources[i].requestedauthncontext = resource[i].requestedauthncontext
						addresources[i].authnctxclassref = resource[i].authnctxclassref
						addresources[i].samlbinding = resource[i].samlbinding
						addresources[i].attributeconsumingserviceindex = resource[i].attributeconsumingserviceindex
						addresources[i].sendthumbprint = resource[i].sendthumbprint
						addresources[i].enforceusername = resource[i].enforceusername
						addresources[i].logouturl = resource[i].logouturl
						addresources[i].artifactresolutionserviceurl = resource[i].artifactresolutionserviceurl
						addresources[i].skewtime = resource[i].skewtime
						addresources[i].logoutbinding = resource[i].logoutbinding
						addresources[i].forceauthn = resource[i].forceauthn
						addresources[i].groupnamefield = resource[i].groupnamefield
						addresources[i].audience = resource[i].audience
						addresources[i].metadataurl = resource[i].metadataurl
						addresources[i].metadatarefreshinterval = resource[i].metadatarefreshinterval
						addresources[i].storesamlresponse = resource[i].storesamlresponse
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationsamlaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationsamlaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationsamlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationsamlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationsamlaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = authenticationsamlaction()
				updateresource.name = resource.name
				updateresource.samlidpcertname = resource.samlidpcertname
				updateresource.samlsigningcertname = resource.samlsigningcertname
				updateresource.samlredirecturl = resource.samlredirecturl
				updateresource.samlacsindex = resource.samlacsindex
				updateresource.samluserfield = resource.samluserfield
				updateresource.samlrejectunsignedassertion = resource.samlrejectunsignedassertion
				updateresource.samlissuername = resource.samlissuername
				updateresource.samltwofactor = resource.samltwofactor
				updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
				updateresource.attribute1 = resource.attribute1
				updateresource.attribute2 = resource.attribute2
				updateresource.attribute3 = resource.attribute3
				updateresource.attribute4 = resource.attribute4
				updateresource.attribute5 = resource.attribute5
				updateresource.attribute6 = resource.attribute6
				updateresource.attribute7 = resource.attribute7
				updateresource.attribute8 = resource.attribute8
				updateresource.attribute9 = resource.attribute9
				updateresource.attribute10 = resource.attribute10
				updateresource.attribute11 = resource.attribute11
				updateresource.attribute12 = resource.attribute12
				updateresource.attribute13 = resource.attribute13
				updateresource.attribute14 = resource.attribute14
				updateresource.attribute15 = resource.attribute15
				updateresource.attribute16 = resource.attribute16
				updateresource.attributes = resource.attributes
				updateresource.signaturealg = resource.signaturealg
				updateresource.digestmethod = resource.digestmethod
				updateresource.requestedauthncontext = resource.requestedauthncontext
				updateresource.authnctxclassref = resource.authnctxclassref
				updateresource.samlbinding = resource.samlbinding
				updateresource.attributeconsumingserviceindex = resource.attributeconsumingserviceindex
				updateresource.sendthumbprint = resource.sendthumbprint
				updateresource.enforceusername = resource.enforceusername
				updateresource.logouturl = resource.logouturl
				updateresource.artifactresolutionserviceurl = resource.artifactresolutionserviceurl
				updateresource.skewtime = resource.skewtime
				updateresource.logoutbinding = resource.logoutbinding
				updateresource.forceauthn = resource.forceauthn
				updateresource.groupnamefield = resource.groupnamefield
				updateresource.audience = resource.audience
				updateresource.metadataurl = resource.metadataurl
				updateresource.metadatarefreshinterval = resource.metadatarefreshinterval
				updateresource.storesamlresponse = resource.storesamlresponse
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationsamlaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].samlidpcertname = resource[i].samlidpcertname
						updateresources[i].samlsigningcertname = resource[i].samlsigningcertname
						updateresources[i].samlredirecturl = resource[i].samlredirecturl
						updateresources[i].samlacsindex = resource[i].samlacsindex
						updateresources[i].samluserfield = resource[i].samluserfield
						updateresources[i].samlrejectunsignedassertion = resource[i].samlrejectunsignedassertion
						updateresources[i].samlissuername = resource[i].samlissuername
						updateresources[i].samltwofactor = resource[i].samltwofactor
						updateresources[i].defaultauthenticationgroup = resource[i].defaultauthenticationgroup
						updateresources[i].attribute1 = resource[i].attribute1
						updateresources[i].attribute2 = resource[i].attribute2
						updateresources[i].attribute3 = resource[i].attribute3
						updateresources[i].attribute4 = resource[i].attribute4
						updateresources[i].attribute5 = resource[i].attribute5
						updateresources[i].attribute6 = resource[i].attribute6
						updateresources[i].attribute7 = resource[i].attribute7
						updateresources[i].attribute8 = resource[i].attribute8
						updateresources[i].attribute9 = resource[i].attribute9
						updateresources[i].attribute10 = resource[i].attribute10
						updateresources[i].attribute11 = resource[i].attribute11
						updateresources[i].attribute12 = resource[i].attribute12
						updateresources[i].attribute13 = resource[i].attribute13
						updateresources[i].attribute14 = resource[i].attribute14
						updateresources[i].attribute15 = resource[i].attribute15
						updateresources[i].attribute16 = resource[i].attribute16
						updateresources[i].attributes = resource[i].attributes
						updateresources[i].signaturealg = resource[i].signaturealg
						updateresources[i].digestmethod = resource[i].digestmethod
						updateresources[i].requestedauthncontext = resource[i].requestedauthncontext
						updateresources[i].authnctxclassref = resource[i].authnctxclassref
						updateresources[i].samlbinding = resource[i].samlbinding
						updateresources[i].attributeconsumingserviceindex = resource[i].attributeconsumingserviceindex
						updateresources[i].sendthumbprint = resource[i].sendthumbprint
						updateresources[i].enforceusername = resource[i].enforceusername
						updateresources[i].logouturl = resource[i].logouturl
						updateresources[i].artifactresolutionserviceurl = resource[i].artifactresolutionserviceurl
						updateresources[i].skewtime = resource[i].skewtime
						updateresources[i].logoutbinding = resource[i].logoutbinding
						updateresources[i].forceauthn = resource[i].forceauthn
						updateresources[i].groupnamefield = resource[i].groupnamefield
						updateresources[i].audience = resource[i].audience
						updateresources[i].metadataurl = resource[i].metadataurl
						updateresources[i].metadatarefreshinterval = resource[i].metadatarefreshinterval
						updateresources[i].storesamlresponse = resource[i].storesamlresponse
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationsamlaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationsamlaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationsamlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationsamlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationsamlaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationsamlaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationsamlaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationsamlaction() for _ in range(len(name))]
						obj = [authenticationsamlaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationsamlaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationsamlaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationsamlaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationsamlaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationsamlaction()
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
		r""" Use this API to count filtered the set of authenticationsamlaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationsamlaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Forceauthn:
		ON = "ON"
		OFF = "OFF"

	class Samltwofactor:
		ON = "ON"
		OFF = "OFF"

	class Samlrejectunsignedassertion:
		ON = "ON"
		OFF = "OFF"
		STRICT = "STRICT"

	class Digestmethod:
		SHA1 = "SHA1"
		SHA256 = "SHA256"

	class Metadataimportstatus:
		INIT = "INIT"
		SUCCESS = "SUCCESS"
		FAIL = "FAIL"

	class Requestedauthncontext:
		exact = "exact"
		minimum = "minimum"
		maximum = "maximum"
		better = "better"

	class Sendthumbprint:
		ON = "ON"
		OFF = "OFF"

	class Signaturealg:
		RSA_SHA1 = "RSA-SHA1"
		RSA_SHA256 = "RSA-SHA256"

	class Storesamlresponse:
		ON = "ON"
		OFF = "OFF"

	class Samlbinding:
		REDIRECT = "REDIRECT"
		POST = "POST"
		ARTIFACT = "ARTIFACT"

	class Authnctxclassref:
		InternetProtocol = "InternetProtocol"
		InternetProtocolPassword = "InternetProtocolPassword"
		Kerberos = "Kerberos"
		MobileOneFactorUnregistered = "MobileOneFactorUnregistered"
		MobileTwoFactorUnregistered = "MobileTwoFactorUnregistered"
		MobileOneFactorContract = "MobileOneFactorContract"
		MobileTwoFactorContract = "MobileTwoFactorContract"
		Password = "Password"
		PasswordProtectedTransport = "PasswordProtectedTransport"
		PreviousSession = "PreviousSession"
		X509 = "X509"
		PGP = "PGP"
		SPKI = "SPKI"
		XMLDSig = "XMLDSig"
		Smartcard = "Smartcard"
		SmartcardPKI = "SmartcardPKI"
		SoftwarePKI = "SoftwarePKI"
		Telephony = "Telephony"
		NomadTelephony = "NomadTelephony"
		PersonalTelephony = "PersonalTelephony"
		AuthenticatedTelephony = "AuthenticatedTelephony"
		SecureRemotePassword = "SecureRemotePassword"
		TLSClient = "TLSClient"
		TimeSyncToken = "TimeSyncToken"
		Unspecified = "Unspecified"
		Windows = "Windows"

	class Logoutbinding:
		REDIRECT = "REDIRECT"
		POST = "POST"

	class Enforceusername:
		ON = "ON"
		OFF = "OFF"

class authenticationsamlaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationsamlaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationsamlaction = [authenticationsamlaction() for _ in range(length)]

