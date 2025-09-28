from .combined_component import CombinedComponent
from fasthtml.common import Button, Form, Group

class FormGroup(CombinedComponent):

    id = ""
    action = ""
    method = ""
    children = []
    button_label = "Submit"

    # Default inline styles (can be overridden)
    container_style = "padding:1rem; background-color:#f9fafb; border-radius:1rem; box-shadow:0 1px 3px rgba(0,0,0,0.1);"
    group_style = "display:flex; gap:1rem; align-items:center;"
    button_style = "padding:0.5rem 1rem; background-color:#5A599D; color:white; border-radius:0.5rem; border:none; cursor:pointer;"


    def call_children(self, userid, model):
        children = super().call_children(userid, model)

        # append styled button to children
        children.append(Button(self.button_label, style=self.button_style))

        return children

    def outer_div(self, children, div_args):

        return Form(Group(*children, style=self.group_style), **div_args)
    
    def div_args(self, userid, model):

        return {
            'id': self.id,
            'action': self.action,
            'method': self.method,
            'style': self.container_style
        }