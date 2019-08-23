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

class sslaction(base_resource) :
	""" Configuration for SSL action resource. """
	def __init__(self) :
		self._name = None
		self._clientauth = None
		self._clientcertverification = None
		self._ssllogprofile = None
		self._clientcert = None
		self._certheader = None
		self._clientcertserialnumber = None
		self._certserialheader = None
		self._clientcertsubject = None
		self._certsubjectheader = None
		self._clientcerthash = None
		self._certhashheader = None
		self._clientcertfingerprint = None
		self._certfingerprintheader = None
		self._certfingerprintdigest = None
		self._clientcertissuer = None
		self._certissuerheader = None
		self._sessionid = None
		self._sessionidheader = None
		self._cipher = None
		self._cipherheader = None
		self._clientcertnotbefore = None
		self._certnotbeforeheader = None
		self._clientcertnotafter = None
		self._certnotafterheader = None
		self._owasupport = None
		self._forward = None
		self._cacertgrpname = None
		self._feature = None
		self._hits = None
		self._undefhits = None
		self._referencecount = None
		self._description = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the SSL action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the SSL action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clientauth(self) :
		r"""Perform client certificate authentication.<br/>Possible values = DOCLIENTAUTH, NOCLIENTAUTH.
		"""
		try :
			return self._clientauth
		except Exception as e:
			raise e

	@clientauth.setter
	def clientauth(self, clientauth) :
		r"""Perform client certificate authentication.<br/>Possible values = DOCLIENTAUTH, NOCLIENTAUTH
		"""
		try :
			self._clientauth = clientauth
		except Exception as e:
			raise e

	@property
	def clientcertverification(self) :
		r"""Client certificate verification is mandatory or optional.<br/>Default value: Mandatory<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._clientcertverification
		except Exception as e:
			raise e

	@clientcertverification.setter
	def clientcertverification(self, clientcertverification) :
		r"""Client certificate verification is mandatory or optional.<br/>Default value: Mandatory<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._clientcertverification = clientcertverification
		except Exception as e:
			raise e

	@property
	def ssllogprofile(self) :
		r"""The name of the ssllogprofile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._ssllogprofile
		except Exception as e:
			raise e

	@ssllogprofile.setter
	def ssllogprofile(self, ssllogprofile) :
		r"""The name of the ssllogprofile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._ssllogprofile = ssllogprofile
		except Exception as e:
			raise e

	@property
	def clientcert(self) :
		r"""Insert the entire client certificate into the HTTP header of the request being sent to the web server. The certificate is inserted in ASCII (PEM) format.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcert
		except Exception as e:
			raise e

	@clientcert.setter
	def clientcert(self, clientcert) :
		r"""Insert the entire client certificate into the HTTP header of the request being sent to the web server. The certificate is inserted in ASCII (PEM) format.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcert = clientcert
		except Exception as e:
			raise e

	@property
	def certheader(self) :
		r"""Name of the header into which to insert the client certificate.
		"""
		try :
			return self._certheader
		except Exception as e:
			raise e

	@certheader.setter
	def certheader(self, certheader) :
		r"""Name of the header into which to insert the client certificate.
		"""
		try :
			self._certheader = certheader
		except Exception as e:
			raise e

	@property
	def clientcertserialnumber(self) :
		r"""Insert the entire client serial number into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcertserialnumber
		except Exception as e:
			raise e

	@clientcertserialnumber.setter
	def clientcertserialnumber(self, clientcertserialnumber) :
		r"""Insert the entire client serial number into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcertserialnumber = clientcertserialnumber
		except Exception as e:
			raise e

	@property
	def certserialheader(self) :
		r"""Name of the header into which to insert the client serial number.
		"""
		try :
			return self._certserialheader
		except Exception as e:
			raise e

	@certserialheader.setter
	def certserialheader(self, certserialheader) :
		r"""Name of the header into which to insert the client serial number.
		"""
		try :
			self._certserialheader = certserialheader
		except Exception as e:
			raise e

	@property
	def clientcertsubject(self) :
		r"""Insert the client certificate subject, also known as the distinguished name (DN), into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcertsubject
		except Exception as e:
			raise e

	@clientcertsubject.setter
	def clientcertsubject(self, clientcertsubject) :
		r"""Insert the client certificate subject, also known as the distinguished name (DN), into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcertsubject = clientcertsubject
		except Exception as e:
			raise e

	@property
	def certsubjectheader(self) :
		r"""Name of the header into which to insert the client certificate subject.
		"""
		try :
			return self._certsubjectheader
		except Exception as e:
			raise e

	@certsubjectheader.setter
	def certsubjectheader(self, certsubjectheader) :
		r"""Name of the header into which to insert the client certificate subject.
		"""
		try :
			self._certsubjectheader = certsubjectheader
		except Exception as e:
			raise e

	@property
	def clientcerthash(self) :
		r"""Insert the certificate's signature into the HTTP header of the request being sent to the web server. The signature is the value extracted directly from the X.509 certificate signature field. All X.509 certificates contain a signature field.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcerthash
		except Exception as e:
			raise e

	@clientcerthash.setter
	def clientcerthash(self, clientcerthash) :
		r"""Insert the certificate's signature into the HTTP header of the request being sent to the web server. The signature is the value extracted directly from the X.509 certificate signature field. All X.509 certificates contain a signature field.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcerthash = clientcerthash
		except Exception as e:
			raise e

	@property
	def certhashheader(self) :
		r"""Name of the header into which to insert the client certificate signature (hash).
		"""
		try :
			return self._certhashheader
		except Exception as e:
			raise e

	@certhashheader.setter
	def certhashheader(self, certhashheader) :
		r"""Name of the header into which to insert the client certificate signature (hash).
		"""
		try :
			self._certhashheader = certhashheader
		except Exception as e:
			raise e

	@property
	def clientcertfingerprint(self) :
		r"""Insert the certificate's fingerprint into the HTTP header of the request being sent to the web server. The fingerprint is derived by computing the specified hash value (SHA256, for example) of the DER-encoding of the client certificate.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcertfingerprint
		except Exception as e:
			raise e

	@clientcertfingerprint.setter
	def clientcertfingerprint(self, clientcertfingerprint) :
		r"""Insert the certificate's fingerprint into the HTTP header of the request being sent to the web server. The fingerprint is derived by computing the specified hash value (SHA256, for example) of the DER-encoding of the client certificate.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcertfingerprint = clientcertfingerprint
		except Exception as e:
			raise e

	@property
	def certfingerprintheader(self) :
		r"""Name of the header into which to insert the client certificate fingerprint.
		"""
		try :
			return self._certfingerprintheader
		except Exception as e:
			raise e

	@certfingerprintheader.setter
	def certfingerprintheader(self, certfingerprintheader) :
		r"""Name of the header into which to insert the client certificate fingerprint.
		"""
		try :
			self._certfingerprintheader = certfingerprintheader
		except Exception as e:
			raise e

	@property
	def certfingerprintdigest(self) :
		r"""Digest algorithm used to compute the fingerprint of the client certificate.<br/>Possible values = SHA1, SHA224, SHA256, SHA384, SHA512.
		"""
		try :
			return self._certfingerprintdigest
		except Exception as e:
			raise e

	@certfingerprintdigest.setter
	def certfingerprintdigest(self, certfingerprintdigest) :
		r"""Digest algorithm used to compute the fingerprint of the client certificate.<br/>Possible values = SHA1, SHA224, SHA256, SHA384, SHA512
		"""
		try :
			self._certfingerprintdigest = certfingerprintdigest
		except Exception as e:
			raise e

	@property
	def clientcertissuer(self) :
		r"""Insert the certificate issuer details into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcertissuer
		except Exception as e:
			raise e

	@clientcertissuer.setter
	def clientcertissuer(self, clientcertissuer) :
		r"""Insert the certificate issuer details into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcertissuer = clientcertissuer
		except Exception as e:
			raise e

	@property
	def certissuerheader(self) :
		r"""Name of the header into which to insert the client certificate issuer details.
		"""
		try :
			return self._certissuerheader
		except Exception as e:
			raise e

	@certissuerheader.setter
	def certissuerheader(self, certissuerheader) :
		r"""Name of the header into which to insert the client certificate issuer details.
		"""
		try :
			self._certissuerheader = certissuerheader
		except Exception as e:
			raise e

	@property
	def sessionid(self) :
		r"""Insert the SSL session ID into the HTTP header of the request being sent to the web server. Every SSL connection that the client and the Citrix ADC share has a unique ID that identifies the specific connection.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionid
		except Exception as e:
			raise e

	@sessionid.setter
	def sessionid(self, sessionid) :
		r"""Insert the SSL session ID into the HTTP header of the request being sent to the web server. Every SSL connection that the client and the Citrix ADC share has a unique ID that identifies the specific connection.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionid = sessionid
		except Exception as e:
			raise e

	@property
	def sessionidheader(self) :
		r"""Name of the header into which to insert the Session ID.
		"""
		try :
			return self._sessionidheader
		except Exception as e:
			raise e

	@sessionidheader.setter
	def sessionidheader(self, sessionidheader) :
		r"""Name of the header into which to insert the Session ID.
		"""
		try :
			self._sessionidheader = sessionidheader
		except Exception as e:
			raise e

	@property
	def cipher(self) :
		r"""Insert the cipher suite that the client and the Citrix ADC negotiated for the SSL session into the HTTP header of the request being sent to the web server. The appliance inserts the cipher-suite name, SSL protocol, export or non-export string, and cipher strength bit, depending on the type of browser connecting to the SSL virtual server or service (for example, Cipher-Suite: RC4- MD5 SSLv3 Non-Export 128-bit).<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cipher
		except Exception as e:
			raise e

	@cipher.setter
	def cipher(self, cipher) :
		r"""Insert the cipher suite that the client and the Citrix ADC negotiated for the SSL session into the HTTP header of the request being sent to the web server. The appliance inserts the cipher-suite name, SSL protocol, export or non-export string, and cipher strength bit, depending on the type of browser connecting to the SSL virtual server or service (for example, Cipher-Suite: RC4- MD5 SSLv3 Non-Export 128-bit).<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cipher = cipher
		except Exception as e:
			raise e

	@property
	def cipherheader(self) :
		r"""Name of the header into which to insert the name of the cipher suite.
		"""
		try :
			return self._cipherheader
		except Exception as e:
			raise e

	@cipherheader.setter
	def cipherheader(self, cipherheader) :
		r"""Name of the header into which to insert the name of the cipher suite.
		"""
		try :
			self._cipherheader = cipherheader
		except Exception as e:
			raise e

	@property
	def clientcertnotbefore(self) :
		r"""Insert the date from which the certificate is valid into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time from which it is valid.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcertnotbefore
		except Exception as e:
			raise e

	@clientcertnotbefore.setter
	def clientcertnotbefore(self, clientcertnotbefore) :
		r"""Insert the date from which the certificate is valid into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time from which it is valid.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcertnotbefore = clientcertnotbefore
		except Exception as e:
			raise e

	@property
	def certnotbeforeheader(self) :
		r"""Name of the header into which to insert the date and time from which the certificate is valid.
		"""
		try :
			return self._certnotbeforeheader
		except Exception as e:
			raise e

	@certnotbeforeheader.setter
	def certnotbeforeheader(self, certnotbeforeheader) :
		r"""Name of the header into which to insert the date and time from which the certificate is valid.
		"""
		try :
			self._certnotbeforeheader = certnotbeforeheader
		except Exception as e:
			raise e

	@property
	def clientcertnotafter(self) :
		r"""Insert the date of expiry of the certificate into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time at which the certificate expires.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientcertnotafter
		except Exception as e:
			raise e

	@clientcertnotafter.setter
	def clientcertnotafter(self, clientcertnotafter) :
		r"""Insert the date of expiry of the certificate into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time at which the certificate expires.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientcertnotafter = clientcertnotafter
		except Exception as e:
			raise e

	@property
	def certnotafterheader(self) :
		r"""Name of the header into which to insert the certificate's expiry date.
		"""
		try :
			return self._certnotafterheader
		except Exception as e:
			raise e

	@certnotafterheader.setter
	def certnotafterheader(self, certnotafterheader) :
		r"""Name of the header into which to insert the certificate's expiry date.
		"""
		try :
			self._certnotafterheader = certnotafterheader
		except Exception as e:
			raise e

	@property
	def owasupport(self) :
		r"""If the appliance is in front of an Outlook Web Access (OWA) server, insert a special header field, FRONT-END-HTTPS: ON, into the HTTP requests going to the OWA server. This header communicates to the server that the transaction is HTTPS and not HTTP.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._owasupport
		except Exception as e:
			raise e

	@owasupport.setter
	def owasupport(self, owasupport) :
		r"""If the appliance is in front of an Outlook Web Access (OWA) server, insert a special header field, FRONT-END-HTTPS: ON, into the HTTP requests going to the OWA server. This header communicates to the server that the transaction is HTTPS and not HTTP.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._owasupport = owasupport
		except Exception as e:
			raise e

	@property
	def forward(self) :
		r"""This action takes an argument a vserver name, to this vserver one will be able to forward all the packets.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._forward
		except Exception as e:
			raise e

	@forward.setter
	def forward(self, forward) :
		r"""This action takes an argument a vserver name, to this vserver one will be able to forward all the packets.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._forward = forward
		except Exception as e:
			raise e

	@property
	def cacertgrpname(self) :
		r"""This action will allow to pick CA(s) from the specific CA group, to verify the client certificate.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._cacertgrpname
		except Exception as e:
			raise e

	@cacertgrpname.setter
	def cacertgrpname(self, cacertgrpname) :
		r"""This action will allow to pick CA(s) from the specific CA group, to verify the client certificate.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._cacertgrpname = cacertgrpname
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@feature.setter
	def feature(self, feature) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			self._feature = feature
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		r"""The number of times the action resulted in UNDEF.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		r"""The number of references to the action.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	@property
	def description(self) :
		r"""Description of the action.
		"""
		try :
			return self._description
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslaction
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
		r""" Use this API to add sslaction.
		"""
		try :
			if type(resource) is not list :
				addresource = sslaction()
				addresource.name = resource.name
				addresource.clientauth = resource.clientauth
				addresource.clientcertverification = resource.clientcertverification
				addresource.ssllogprofile = resource.ssllogprofile
				addresource.clientcert = resource.clientcert
				addresource.certheader = resource.certheader
				addresource.clientcertserialnumber = resource.clientcertserialnumber
				addresource.certserialheader = resource.certserialheader
				addresource.clientcertsubject = resource.clientcertsubject
				addresource.certsubjectheader = resource.certsubjectheader
				addresource.clientcerthash = resource.clientcerthash
				addresource.certhashheader = resource.certhashheader
				addresource.clientcertfingerprint = resource.clientcertfingerprint
				addresource.certfingerprintheader = resource.certfingerprintheader
				addresource.certfingerprintdigest = resource.certfingerprintdigest
				addresource.clientcertissuer = resource.clientcertissuer
				addresource.certissuerheader = resource.certissuerheader
				addresource.sessionid = resource.sessionid
				addresource.sessionidheader = resource.sessionidheader
				addresource.cipher = resource.cipher
				addresource.cipherheader = resource.cipherheader
				addresource.clientcertnotbefore = resource.clientcertnotbefore
				addresource.certnotbeforeheader = resource.certnotbeforeheader
				addresource.clientcertnotafter = resource.clientcertnotafter
				addresource.certnotafterheader = resource.certnotafterheader
				addresource.owasupport = resource.owasupport
				addresource.forward = resource.forward
				addresource.cacertgrpname = resource.cacertgrpname
				addresource.feature = resource.feature
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].clientauth = resource[i].clientauth
						addresources[i].clientcertverification = resource[i].clientcertverification
						addresources[i].ssllogprofile = resource[i].ssllogprofile
						addresources[i].clientcert = resource[i].clientcert
						addresources[i].certheader = resource[i].certheader
						addresources[i].clientcertserialnumber = resource[i].clientcertserialnumber
						addresources[i].certserialheader = resource[i].certserialheader
						addresources[i].clientcertsubject = resource[i].clientcertsubject
						addresources[i].certsubjectheader = resource[i].certsubjectheader
						addresources[i].clientcerthash = resource[i].clientcerthash
						addresources[i].certhashheader = resource[i].certhashheader
						addresources[i].clientcertfingerprint = resource[i].clientcertfingerprint
						addresources[i].certfingerprintheader = resource[i].certfingerprintheader
						addresources[i].certfingerprintdigest = resource[i].certfingerprintdigest
						addresources[i].clientcertissuer = resource[i].clientcertissuer
						addresources[i].certissuerheader = resource[i].certissuerheader
						addresources[i].sessionid = resource[i].sessionid
						addresources[i].sessionidheader = resource[i].sessionidheader
						addresources[i].cipher = resource[i].cipher
						addresources[i].cipherheader = resource[i].cipherheader
						addresources[i].clientcertnotbefore = resource[i].clientcertnotbefore
						addresources[i].certnotbeforeheader = resource[i].certnotbeforeheader
						addresources[i].clientcertnotafter = resource[i].clientcertnotafter
						addresources[i].certnotafterheader = resource[i].certnotafterheader
						addresources[i].owasupport = resource[i].owasupport
						addresources[i].forward = resource[i].forward
						addresources[i].cacertgrpname = resource[i].cacertgrpname
						addresources[i].feature = resource[i].feature
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete sslaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslaction() for _ in range(len(name))]
						obj = [sslaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslaction resources configured on NetScaler.
		"""
		try :
			obj = sslaction()
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
		r""" Use this API to count filtered the set of sslaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Clientcertnotafter:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcertverification:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Clientcertissuer:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcertnotbefore:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Certfingerprintdigest:
		SHA1 = "SHA1"
		SHA224 = "SHA224"
		SHA256 = "SHA256"
		SHA384 = "SHA384"
		SHA512 = "SHA512"

	class Clientcertserialnumber:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcert:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"

	class Owasupport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcertsubject:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcertfingerprint:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cipher:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcerthash:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientauth:
		DOCLIENTAUTH = "DOCLIENTAUTH"
		NOCLIENTAUTH = "NOCLIENTAUTH"

	class Sessionid:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class sslaction_response(base_response) :
	def __init__(self, length=1) :
		self.sslaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslaction = [sslaction() for _ in range(length)]

