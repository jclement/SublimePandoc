import sublime, sublime_plugin
import webbrowser
import tempfile
import os
import sys
import subprocess

class PandocRenderCommand(sublime_plugin.TextCommand):
    """ render file contents to HTML and, optionally, open in your web browser"""

    def getTemplatePath(self, filename):
        path = os.path.join(sublime.packages_path(), 'SublimePandoc', filename)
        if not os.path.isfile(path):
            raise Exception(filename + " file not found!")
        return path

    def run(self, edit, target="html", openAfter=True, writeBeside=False):
        if not target in ["html","docx"]: raise Exception("target must be either 'html' or 'docx'")

        # grab contents of buffer
        region = sublime.Region(0, self.view.size())
        encoding = self.view.encoding()
        if encoding == 'Undefined':
            encoding = 'UTF-8'
        elif encoding == 'Western (Windows 1252)':
            encoding = 'windows-1252'
        contents = self.view.substr(region)

        # write buffer to temporary file
        tmp_md = tempfile.NamedTemporaryFile(delete=False, suffix=".md")
        tmp_md.write(contents)
        tmp_md.close()

        # output file...
        suffix = "." + target
        if writeBeside:
            output_filename = os.path.splitext(self.view.file_name())[0]+suffix
            if not self.view.file_name(): raise Exception("Buffer must be saved before 'writeBeside' can be used.")
        else:
            tmp_html = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            tmp_html.close()
            output_filename=tmp_html.name

        # build output
        cmd = ['pandoc']
        cmd.append('-t')
        cmd.append({'html':'html5', 'docx':'docx'}[target])
        cmd.append('--standalone')
        cmd.append('--template=%s' % self.getTemplatePath("template.html"))
        cmd.append('--reference-docx=%s' % self.getTemplatePath("reference.docx"))
        cmd.append(tmp_md.name)
        cmd.append("-o")
        cmd.append(output_filename)
        if '[[TOC]]' in contents:
            cmd.append("--toc")
        if '[[NUM]]' in contents:
            cmd.append("-N")

        print subprocess.call(cmd)
        print "Wrote:", output_filename

        if openAfter:
            webbrowser.open_new_tab(output_filename)
