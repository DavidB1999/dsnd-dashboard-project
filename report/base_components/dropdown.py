from .base_component import BaseComponent
from fasthtml.common import Select, Label, Div, Option

class Dropdown(BaseComponent):

    value_color = "#5A599D"

    def __init__(self, id="selector", name="entity-selection", label="", value_color="#5A599D", label_color=None):
        self.id = id
        self.name = name
        self.label = label
        self.value_color = value_color
        self.label_color = value_color if label_color == None else label_color

    def build_component(self, entity_id, model):
        options = []
        for text, value in self.component_data(entity_id, model):
            option = Option(text, value=value, selected="selected" if str(value) == str(entity_id) else "", style=f"color:{self.value_color};")
            options.append(option)


        dropdown_settings = {
            'name': self.name,
            'style': f'color:{self.value_color}'
            }
        
        # if model.name:
        #     dropdown_settings['disabled'] = 'disabled'

        selector = Select(
            *options,
            **dropdown_settings,
            )
        
        return selector
    
    def outer_div(self, child):

        return Div(
            Label(self.label, _for=self.id, style=f'color:{self.label_color}'),
            child,
            id=self.id,
        )
    