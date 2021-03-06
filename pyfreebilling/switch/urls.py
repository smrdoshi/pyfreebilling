# -*- coding: utf-8 -*-
# Copyright 2013 Mathias WOLFF
# This file is part of pyfreebilling.
#
# pyfreebilling is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfreebilling is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfreebilling.  If not, see <http://www.gnu.org/licenses/>
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(
        r'^extranet/', include([
            url(
                regex=r'^FsServer/$',
                view=views.fs_status_view
            ),
            url(
                regex=r'^FsServerRegistry/$',
                view=views.fs_registry_view
            ),
            url(
                regex=r'^FsServerBCalls/$',
                view=views.fs_bcalls_view
            ),
            url(
                regex=r'^ServerStatus/$',
                view=views.server_status_view,
                name='ServerStatus'
            ),
        ])),
]
