import sublime, sublime_plugin
import webbrowser
import tempfile
import os
import sys

class PandocRenderCommand(sublime_plugin.TextCommand):
    """ render file contents to HTML and, optionally, open in your web browser"""

    def getTemplatePath(self):
        filename = 'template.html'
        # path via package manager
        path = os.path.join(sublime.packages_path(), 'SublimePandoc', filename)
        if not os.path.isfile(path):
            raise Exception(filename + " file not found!")
        return path

    def run(self, edit, openInBrowser=True, writeBeside=False):
        print edit, openInBrowser, self.getTemplatePath()
        region = sublime.Region(0, self.view.size())
        encoding = self.view.encoding()
        if encoding == 'Undefined':
            encoding = 'UTF-8'
        elif encoding == 'Western (Windows 1252)':
            encoding = 'windows-1252'
        contents = self.view.substr(region)

        tmp_md = tempfile.NamedTemporaryFile(delete=False, suffix=".md")
        tmp_md.write(contents)
        tmp_md.close()

        if writeBeside:
            output_filename = os.path.splitext(self.view.file_name())[0]+".html"
        else:
            tmp_html = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
            tmp_html.close()
            output_filename=tmp_html.name

        cmd = 'pandoc -t html5 --standalone --template="%s" "%s" -o "%s"' % (
            self.getTemplatePath(),
            tmp_md.name,           
            output_filename)
        if '[[TOC]]' in contents:
            cmd += " --toc"
        if '[[NUM]]' in contents:
            cmd += " -N"

        os.system(cmd)

        if openInBrowser:
            webbrowser.open_new_tab(tmp_html.name)
