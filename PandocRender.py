import sublime, sublime_plugin
import webbrowser
import tempfile
import os
import re
import sys
import subprocess


plugin_path = os.path.dirname(os.path.abspath(__file__))
settings = sublime.load_settings('Pandoc.sublime-settings')

class PandocRenderCommand(sublime_plugin.TextCommand):
    """ render file contents to HTML and, optionally, open in your web browser"""

    def getTemplatePath(self, filename):
        path = os.path.join(plugin_path, filename)
        if not os.path.isfile(path):
            raise Exception(filename + " file not found!")
        return path

    def is_enabled(self):
        return self.view.score_selector(0, "text.html.markdown") > 0

    def is_visible(self):
        return True 

    def run(self, edit, target="html", openAfter=True, writeBeside=False, additionalArguments=[]):
        if not target in ["html","docx"]: raise Exception("target must be either 'html' or 'docx'")

        # determin pandoc binary
        pandoc_path = settings.get('pandoc_path')
        if pandoc_path is not None:
            pandoc_bin = os.path.join(os.path.expanduser(pandoc_path), 'pandoc')
        else:
            pandoc_bin = settings.get('pandoc_bin') or 'pandoc' # set to default in $PATH
            pandoc_bin = os.path.expanduser(pandoc_bin)
        if not os.path.exists(pandoc_bin):
            found = False
            if pandoc_bin == 'pandoc':
                bools = [os.path.exists(os.path.join(p, pandoc_bin)) for p in os.environ['PATH'].split(':')]
                if bools.count(True):
                    found = True
            if not found:
                sublime.error_message("Unable to load pandoc engine: {0}\n\nYou can specify Pandoc in settings.".format(pandoc_bin))
                return

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
        tmp_md.write(contents.encode(encoding))
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
        cmd = [pandoc_bin]
        cmd.append('-t')
        cmd.append({'html':'html5', 'docx':'docx'}[target])
        cmd.append('--standalone')
        cmd.append('--template=%s' % self.getTemplatePath("template.html"))
        cmd.append('--reference-docx=%s' % self.getTemplatePath("reference.docx"))
        cmd.append(tmp_md.name)
        cmd.append("-o")
        cmd.append(output_filename)
        cmd += additionalArguments

        # Extra arguments to pass into pandoc, e.g.:
        #     <!-- [[ PANDOC --smart --no-wrap ]] -->
        match = re.match(r'.*<!--\s+\[\[ PANDOC (?P<args>.*) \]\]\s+-->', contents)
        if match:
            cmd += match.groupdict()['args'].split(' ')


        try:
            subprocess.call(cmd)
        except Exception as e:
            sublime.error_message("Error in executing Pandoc.  \n\nDetails: {0}".format(e))


        print "Wrote:", output_filename

        if openAfter:
            if target == "html":
                webbrowser.open_new_tab(output_filename)
            # perhaps there is a better way of handling the DocX opening...?
            elif target == "docx" and sys.platform == "win32":
                os.startfile(output_filename)
            elif target == "docx" and sys.platform == "mac":
                subprocess.call(["open", output_filename])
            elif target == "docx" and sys.platform == "posix":
                subprocess.call(["xdg-open", output_filename])

