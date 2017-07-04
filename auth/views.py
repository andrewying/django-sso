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

import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import JanoProvider

class JanoOAuth2Adapter(OAuth2Adapter):
    provider_id = JanoProvider.id
    access_token_url = 'https://sso.janoticketing.com/oauth/token'
    authorize_url = 'https://sso.janoticketing.com/oauth/authorize'
    profile_url = 'https://sso.janoticketing.com/api/user'
    redirect_uri_protocol = 'https'
    supports_state = False

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(
            request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(JanoOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(JanoOAuth2Adapter)
