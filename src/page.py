import math
from random import random

import pandas as pd

from src.components import IComponent, Header, Body, Footer


class Page:
    def __init__(self, components: dict[str, IComponent] = None):
        if components is None:
            components = dict()
        self.components: dict[str, IComponent] = components

    def layout(self, **kwargs):
        if self.components["header"] is not None:
            self.add_component("header", self.components["header"])
        if self.components["body"] is not None:
            self.add_component("body", self.components["body"])
        if self.components["footer"] is not None:
            self.add_component("footer", self.components["footer"])
        self.render()

    def render(self):
        for component in self.components.values():
            component.setup()

    def add_component(self, name: str, component: IComponent):
        self.components[name] = component

    def remove_component(self, name: str):
        del (self.components[name])


class TheftRadarPage(Page):
    def __init__(self):
        super().__init__({"header": Header(),
                          "body": Body(),
                          "footer": Footer()})
