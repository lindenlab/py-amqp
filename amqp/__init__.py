"""Low-level AMQP client for Python (fork of amqplib)"""
# Copyright (C) 2007-2008 Barry Pederson <bp@barryp.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
from __future__ import absolute_import

VERSION = (0, 9, 4)
__version__ = '.'.join(map(str, VERSION[0:3])) + ''.join(VERSION[3:])
__author__ = 'Barry Pederson'
__maintainer__ = 'Ask Solem'
__contact__ = 'pyamqp@celeryproject.org'
__homepage__ = 'http://github.com/celery/py-amqp'
__docformat__ = 'restructuredtext'

# -eof meta-

#
# Pull in the public items from the various sub-modules
#
from .basic_message import Message
from .channel import Channel
from .connection import Connection
from .exceptions import (
    AMQPError,
    ConnectionError,
    ChannelError,
    ConsumerCancel,
)

__all__ = [
    'Connection',
    'Channel',
    'Message',
    'AMQPError',
    'ConnectionError',
    'ChannelError',
    'ConsumerCancel',
]
