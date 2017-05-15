import subprocess
import fire
from utility import templates

project_files = ['__init__.py', 'settings.py', 'app.py']
app_files = ['__init__.py', 'forms.py', 'views.py', 'models.py', 'app.py']


class Command(object):

    def __create_files(self, name, files=[]):
        cmd = "cd $(pwd)/ && mkdir {0}".format(name)
        subprocess.call(cmd, shell=True)

        print("creating...")
        for k in range(len(files)):
            cmd = "cd $(pwd)/{0} && touch {1}".format(name, files[k])
            print(name + "/" + files[k])
            subprocess.call(cmd, shell=True)

    def startproject(self, name):
        """ プロジェクトディレクトリを作成する
        @param name
        """
        print("------ project dir --------")
        self.__create_files(name, files=project_files)

        print("set app.py...")
        f = open('$(pwd)/app.py', 'w')
        f.write(templates.APP_TEMPLATE)
        f.close()

        print("set menu.py...")
        f = open('$(pwd)/menu.py', 'w')
        f.write(templates.MENU_TEMPLATE.format(name))
        f.close()

        copy_files = ['__init_.py', 'settings.py']
        for k in range(len(copy_files)):
            if copy_files[k] in project_files:
                cmd = "cp project_template/{0} $(pwd)/{1}/{2}".format(copy_files[k], name, project_files[k])
                subprocess.call(cmd, shell=True)
        print("end!!")

    def startapp(self, name):
        """ アプリディレクトリを作成する
        @param name
        """
        print("------ app dir --------")
        self.__create_files(name, files=app_files)

        path = '$(pwd)/{0}/{1}'

        print("set {file}...".format(file=app_files[1]))
        f = open(path.format(name, app_files[1]), 'w')
        f.write(templates.APP_FORM_TEMPERATE)
        f.close()

        print("set {file}...".format(file=app_files[2]))
        f = open(path.format(name, app_files[2]), 'w')
        f.write(templates.APP_VIEW_TEMPLATE)
        f.close()

        print("set {file}...".format(file=app_files[3]))
        f = open(path.format(name, app_files[3]), 'w')
        f.write(templates.APP_MODEL_TEMPLATE)
        f.close()

        print("end!!")

    def setup(self, name):
        """ アプリのセットアップ """
        pass


if __name__ == '__main__':
    fire.Fire(Command)
