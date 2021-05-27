#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "736f7b32-b91e-4c6f-9c65-0a353030676c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ytmxkdUUTE4AwnD6kazhHhmJRxaxcytQs3H6CfXC8smnAGgX3wdJYmDd6Gt68CsJ")
