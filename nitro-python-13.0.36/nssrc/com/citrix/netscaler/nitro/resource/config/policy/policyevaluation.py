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

class policyevaluation(base_resource) :
	""" Configuration for expr evaluation resource. """
	def __init__(self) :
		self._expression = None
		self._action = None
		self._type = None
		self._input = None
		self._pitmodifiedinputdata = None
		self._pitboolresult = None
		self._pitnumresult = None
		self._pitdoubleresult = None
		self._pitulongresult = None
		self._pitrefresult = None
		self._pitoffsetresult = None
		self._pitoffsetresultlen = None
		self._istruncatedrefresult = None
		self._pitboolevaltime = None
		self._pitnumevaltime = None
		self._pitdoubleevaltime = None
		self._pitulongevaltime = None
		self._pitrefevaltime = None
		self._pitoffsetevaltime = None
		self._pitactionevaltime = None
		self._pitoperationperformerarray = None
		self._pitoldoffsetarray = None
		self._pitnewoffsetarray = None
		self._pitoffsetlengtharray = None
		self._pitboolerrorresult = None
		self._pitnumerrorresult = None
		self._pitdoubleerrorresult = None
		self._pitulongerrorresult = None
		self._pitreferrorresult = None
		self._pitoffseterrorresult = None
		self._pitactionerrorresult = None
		self.___count = None

	@property
	def expression(self) :
		r"""Expression string. For example: http.req.body(100).contains("this").
		"""
		try :
			return self._expression
		except Exception as e:
			raise e

	@expression.setter
	def expression(self, expression) :
		r"""Expression string. For example: http.req.body(100).contains("this").
		"""
		try :
			self._expression = expression
		except Exception as e:
			raise e

	@property
	def action(self) :
		r"""Rewrite action name. Supported rewrite action types are:
		-delete
		-delete_all
		-delete_http_header
		-insert_after
		-insert_after_all
		-insert_before
		-insert_before_all
		-insert_http_header
		-replace
		-replace_all
		.<br/>Minimum length =  1.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		r"""Rewrite action name. Supported rewrite action types are:
		-delete
		-delete_all
		-delete_http_header
		-insert_after
		-insert_after_all
		-insert_before
		-insert_before_all
		-insert_http_header
		-replace
		-replace_all
		.<br/>Minimum length =  1
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Indicates request or response input packet.<br/>Possible values = HTTP_REQ, HTTP_RES, TEXT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Indicates request or response input packet.<br/>Possible values = HTTP_REQ, HTTP_RES, TEXT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def input(self) :
		r"""Text representation of input packet.
		"""
		try :
			return self._input
		except Exception as e:
			raise e

	@input.setter
	def input(self, input) :
		r"""Text representation of input packet.
		"""
		try :
			self._input = input
		except Exception as e:
			raise e

	@property
	def pitmodifiedinputdata(self) :
		r"""Text representation of packet after evaluating expression or rewrite action.
		"""
		try :
			return self._pitmodifiedinputdata
		except Exception as e:
			raise e

	@property
	def pitboolresult(self) :
		r"""Result of the expression in bool format.
		"""
		try :
			return self._pitboolresult
		except Exception as e:
			raise e

	@property
	def pitnumresult(self) :
		r"""Result of the expression in num format.
		"""
		try :
			return self._pitnumresult
		except Exception as e:
			raise e

	@property
	def pitdoubleresult(self) :
		r"""Result of the expression in double format.
		"""
		try :
			return self._pitdoubleresult
		except Exception as e:
			raise e

	@property
	def pitulongresult(self) :
		r"""Result of the expression in unsigned long format.
		"""
		try :
			return self._pitulongresult
		except Exception as e:
			raise e

	@property
	def pitrefresult(self) :
		r"""Result of the expression in string format.
		"""
		try :
			return self._pitrefresult
		except Exception as e:
			raise e

	@property
	def pitoffsetresult(self) :
		r"""Offset of the resultant sting.
		"""
		try :
			return self._pitoffsetresult
		except Exception as e:
			raise e

	@property
	def pitoffsetresultlen(self) :
		r"""Offset length of the resultant sting.
		"""
		try :
			return self._pitoffsetresultlen
		except Exception as e:
			raise e

	@property
	def istruncatedrefresult(self) :
		r"""Identify whether ref result is truncated result.
		"""
		try :
			return self._istruncatedrefresult
		except Exception as e:
			raise e

	@property
	def pitboolevaltime(self) :
		r"""Average evaluation time of bool type expression in nanoseconds.
		"""
		try :
			return self._pitboolevaltime
		except Exception as e:
			raise e

	@property
	def pitnumevaltime(self) :
		r"""Average evaluation time of num type expression in nanoseconds.
		"""
		try :
			return self._pitnumevaltime
		except Exception as e:
			raise e

	@property
	def pitdoubleevaltime(self) :
		r"""Average evaluation time of double type expression in nanoseconds.
		"""
		try :
			return self._pitdoubleevaltime
		except Exception as e:
			raise e

	@property
	def pitulongevaltime(self) :
		r"""Average evaluation time of unsigned long type expression in nanoseconds.
		"""
		try :
			return self._pitulongevaltime
		except Exception as e:
			raise e

	@property
	def pitrefevaltime(self) :
		r"""Average evaluation time of string type expression in nanoseconds.
		"""
		try :
			return self._pitrefevaltime
		except Exception as e:
			raise e

	@property
	def pitoffsetevaltime(self) :
		r"""Average evaluation time in finding offset of the resultant string in the input. Time is in nanoseconds.
		"""
		try :
			return self._pitoffsetevaltime
		except Exception as e:
			raise e

	@property
	def pitactionevaltime(self) :
		r"""Average evaluation time of rewrite action in nanoseconds.
		"""
		try :
			return self._pitactionevaltime
		except Exception as e:
			raise e

	@property
	def pitoperationperformerarray(self) :
		r"""Details of the operation Citrix ADC performed at various offsets during applying of rewrite action on input data. Operation can be insertion, modfication or deletion.<br/>Possible values = INSERT, MODIFY, DELETE.
		"""
		try :
			return self._pitoperationperformerarray
		except Exception as e:
			raise e

	@property
	def pitoldoffsetarray(self) :
		r"""Details of the offsets in the input data at which Citrix ADC either inserted or modified or deleted data during applying of rewrite action.
		"""
		try :
			return self._pitoldoffsetarray
		except Exception as e:
			raise e

	@property
	def pitnewoffsetarray(self) :
		r"""Details of the offsets in the output data at which Citrix ADC either inserted or modified or deleted data during applying of rewrite action.
		"""
		try :
			return self._pitnewoffsetarray
		except Exception as e:
			raise e

	@property
	def pitoffsetlengtharray(self) :
		r"""Details of the lengths of the data which Citrix ADC either inserted or modified or deleted during applying of rewrite action.
		"""
		try :
			return self._pitoffsetlengtharray
		except Exception as e:
			raise e

	@property
	def pitboolerrorresult(self) :
		r"""Result of the bool type expression if any error occurs during evaluation. Result will be in string format.
		"""
		try :
			return self._pitboolerrorresult
		except Exception as e:
			raise e

	@property
	def pitnumerrorresult(self) :
		r"""Result of the num type expression if any error occurs during evaluation. Result will be in string format.
		"""
		try :
			return self._pitnumerrorresult
		except Exception as e:
			raise e

	@property
	def pitdoubleerrorresult(self) :
		r"""Result of the double type expression if any error occurs during evaluation. Result will be in string format.
		"""
		try :
			return self._pitdoubleerrorresult
		except Exception as e:
			raise e

	@property
	def pitulongerrorresult(self) :
		r"""Result of the unsigned long type expression if any error occurs during evaluation. Result will be in string format.
		"""
		try :
			return self._pitulongerrorresult
		except Exception as e:
			raise e

	@property
	def pitreferrorresult(self) :
		r"""Result of the ref type expression if any error occurs during evaluation. Result will be in string format.
		"""
		try :
			return self._pitreferrorresult
		except Exception as e:
			raise e

	@property
	def pitoffseterrorresult(self) :
		r"""Result of the expression if any error occurs in calculating offset. Result will be in string format.
		"""
		try :
			return self._pitoffseterrorresult
		except Exception as e:
			raise e

	@property
	def pitactionerrorresult(self) :
		r"""Result of the action if any error occurs in evaluation. Result will be in string format.
		"""
		try :
			return self._pitactionerrorresult
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policyevaluation_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policyevaluation
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the policyevaluation resources that are configured on netscaler.
		"""
		try :
			if type(name) is not list :
				if type(name) == cls :
					raise Exception('Invalid parameter name:{0}'.format(type(name)))
				option_ = options()
				option_.args = nitro_util.object_to_string_withoutquotes(name)
				response = name.get_resource(client, option_)
			else :
				if name and len(name) > 0 :
					if type(name[0]) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
					response = [policyevaluation() for _ in range(len(name))]
					for i in range(len(name)) :
						option_ = options()
						option_.args = nitro_util.object_to_string_withoutquotes(name[i])
						response[i] = name[i].get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the policyevaluation resources that are configured on netscaler.
	# This uses policyevaluation_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = policyevaluation()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_, obj) :
		r""" Use this API to fetch filtered set of policyevaluation resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client, obj) :
		r""" Use this API to count the policyevaluation resources configured on NetScaler.
		"""
		try :
			option_ = options()
			option_.count = True
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_, obj) :
		r""" Use this API to count filtered the set of policyevaluation resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			option_ = options()
			option_.count = True
			option_.filter = filter_
			option_.args = nitro_util.object_to_string_withoutquotes(obj)
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Pitoperationperformerarray:
		INSERT = "INSERT"
		MODIFY = "MODIFY"
		DELETE = "DELETE"

	class Type:
		HTTP_REQ = "HTTP_REQ"
		HTTP_RES = "HTTP_RES"
		TEXT = "TEXT"

class policyevaluation_response(base_response) :
	def __init__(self, length=1) :
		self.policyevaluation = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policyevaluation = [policyevaluation() for _ in range(length)]

