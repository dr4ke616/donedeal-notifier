from jinja2 import Environment, PackageLoader


class Render(object):

    template = 'email.tpl'

    def __init__(self, template=None):
        if template:
            self.template = template

        self.env = Environment(
            loader=PackageLoader('notifier', 'templates')
        )

    def execute(self, **kwargs):
        template = self.env.get_template(self.template)
        return template.render(**kwargs)
