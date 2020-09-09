#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from dataclasses import dataclass
from typing import Text


@dataclass
class Host:
    ip: Text
    mac: Text
    vendor: Text
    date: Text
    network: Text
    description: Text = str()
    id: int = int()

    def __post_init__(self: Host):
        self.mac = self.mac.lower()
