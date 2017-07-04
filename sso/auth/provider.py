#!/usr/bin/env python
"""django-sso
Copyright (C) 2017 Andrew Ying

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

class JanoAccount(ProviderAccount):
	pass

class JanoProvider(OAuth2Provider):
	id = 'janosso'
	name = 'Jano Ticketing'
	account_class = JanoAccount

	def extract_uid(self, data):
	    return str(data['id'])

	def extract_common_fields(self, data):
	    return dict(
			email=data['email'],
			first_name=data['first_name'],
			last_name=data['last_name'],
			username=data['name']
	    )	   
		
	def get_default_scope(self):
        return ['profile:read']

provider_classes = [JanoProvider]
