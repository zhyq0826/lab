import os
from jinja2 import Environment, FileSystemLoader
import re

template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

class BaseEnvironment(Environment):
    """find template location
    
    according to current parent and template relative path to find template path 

    args:
        template current template that needs to locate
        parent which call template with extends or include directive

    return:
        real template path

    example:
        input:
            template ../../base.html
            parent app/app/index.html
        output:
            base.html

        input:
            template header.html
            parent app/app/index.html
        output:
            app/app/header.html 

        input:
            template ../header.html
            parent app/app/index.html
        output:
            app/header.html 
    

    """
  
    relative_path = re.compile('(./|../)', re.IGNORECASE)
    relative_dir = re.compile('([^/\s]{1,}/)', re.IGNORECASE)
    real_name = re.compile('([^/\s]{1,}$)')

    def join_path(self, template, parent):
        t_group = self.relative_path.findall(template)
        p_group = self.relative_dir.findall(parent)

        t_group_length = len(t_group)
        template_name = template
        # 
        real_template_path = p_group
        if t_group_length:
            template_name = self.real_name.match(template, template.rfind('/')+1).group()        
            real_template_path = p_group[0:0-t_group_length]

        real_template_path.append(template_name)
        return ''.join(real_template_path)


env = BaseEnvironment(loader=FileSystemLoader(template_path))


def main():
    template = env.get_template('app/app/index.html')
    html = template.render()
    print(html)

if __name__ == '__main__':
    main()