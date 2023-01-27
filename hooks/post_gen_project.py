from __future__ import print_function
from cookiecutter.main import cookiecutter

import os
import shutil
import glob

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"

def main():

    project_name = "{{ cookiecutter.project_name }}"

    templates_repo = "{{ cookiecutter._templates_repo }}"
    template_dir = os.path.join("templates", "{{ cookiecutter.java_version }}")
    
    cookiecutter(   
                    templates_repo,
                    directory=template_dir,
                    no_input=True,
                    output_dir="..",
                    overwrite_if_exists=True,
                    extra_context={
                                    "project_name": project_name
                                  }
                )

    if '{{ cookiecutter.dependency_manager }}' == 'Maven':
        all_delete_files = glob.glob(os.path.join('.', '*gradle*'), recursive=True)
        for f in all_delete_files:
            shutil.rmtree(f) if os.path.isdir(f) else os.remove(f)
#         open('.versioning', 'a+').write(
#             '{}\
#             \nfilepath = "pom.xml"\
#             \npattern = "<version>{}</version>"\
#             '.format(ver_syntax, '${version}')
#         )
    else:
        os.remove('pom.xml')
        os.remove('mvnw')
        os.remove('mvnw.cmd')
#         open('.versioning', 'a+').write(
#             '{}\
#             \nfilepath = "gradle.properties"\
#             \npattern = "version={}"\
#             \n{}\
#             \nfilepath = "build.gradle"\
#             \npattern = "version = {}"\
#             '.format(ver_syntax, '${version}', ver_syntax, '${version}')
#         )

    print(SUCCESS +
          "Project initialized successfully! You can now jump to {} folder".
          format(project_name) + TERMINATOR)

if __name__ == '__main__':
    main()