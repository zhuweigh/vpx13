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

class ipsecalgcounters_stats(base_resource) :
	r""" Statistics for counters resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._ipsecalgtotsessions = 0
		self._ipsecalgsessionsrate = 0
		self._ipsecalgtotdrsessions = 0
		self._ipsecalgdrsessionsrate = 0
		self._ipsecalgcuractsessions = 0
		self._ipsecalgcuractsessionsrate = 0
		self._ipsecalgcurblksessions = 0
		self._ipsecalgcurblksessionsrate = 0
		self._ipsecalgtotrxpkts = 0
		self._ipsecalgrxpktsrate = 0
		self._ipsecalgtottxpkts = 0
		self._ipsecalgtxpktsrate = 0

	@property
	def name(self) :
		r"""Name of IPSec ALG Profile.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of IPSec ALG Profile.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def ipsecalgdrsessionsrate(self) :
		r"""Rate (/s) counter for ipsecalgtotdrsessions.
		"""
		try :
			return self._ipsecalgdrsessionsrate
		except Exception as e:
			raise e

	@property
	def ipsecalgtotrxpkts(self) :
		r"""Total Packets received during IPsec ALG sessions.
		"""
		try :
			return self._ipsecalgtotrxpkts
		except Exception as e:
			raise e

	@property
	def ipsecalgtottxpkts(self) :
		r"""Total Packets sent during IPsec ALG sessions.
		"""
		try :
			return self._ipsecalgtottxpkts
		except Exception as e:
			raise e

	@property
	def ipsecalgtxpktsrate(self) :
		r"""Rate (/s) counter for ipsecalgtottxpkts.
		"""
		try :
			return self._ipsecalgtxpktsrate
		except Exception as e:
			raise e

	@property
	def ipsecalgtotsessions(self) :
		r"""Total session for IPSec ALG.
		"""
		try :
			return self._ipsecalgtotsessions
		except Exception as e:
			raise e

	@property
	def ipsecalgrxpktsrate(self) :
		r"""Rate (/s) counter for ipsecalgtotrxpkts.
		"""
		try :
			return self._ipsecalgrxpktsrate
		except Exception as e:
			raise e

	@property
	def ipsecalgtotdrsessions(self) :
		r"""Total Dropped IPsec ALG sessions.
		"""
		try :
			return self._ipsecalgtotdrsessions
		except Exception as e:
			raise e

	@property
	def ipsecalgcuractsessionsrate(self) :
		r"""Rate (/s) counter for ipsecalgcuractsessions.
		"""
		try :
			return self._ipsecalgcuractsessionsrate
		except Exception as e:
			raise e

	@property
	def ipsecalgsessionsrate(self) :
		r"""Rate (/s) counter for ipsecalgtotsessions.
		"""
		try :
			return self._ipsecalgsessionsrate
		except Exception as e:
			raise e

	@property
	def ipsecalgcuractsessions(self) :
		r"""Currently active IPsec ALG sessions.
		"""
		try :
			return self._ipsecalgcuractsessions
		except Exception as e:
			raise e

	@property
	def ipsecalgcurblksessions(self) :
		r"""Currently blocked sessions on ESP Gate.
		"""
		try :
			return self._ipsecalgcurblksessions
		except Exception as e:
			raise e

	@property
	def ipsecalgcurblksessionsrate(self) :
		r"""Rate (/s) counter for ipsecalgcurblksessions.
		"""
		try :
			return self._ipsecalgcurblksessionsrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ipsecalgcounters_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ipsecalgcounters
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all ipsecalgcounters_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = ipsecalgcounters_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class ipsecalgcounters_response(base_response) :
	def __init__(self, length=1) :
		self.ipsecalgcounters = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ipsecalgcounters = [ipsecalgcounters_stats() for _ in range(length)]

