import sublime
import sublime_plugin
import subprocess


class JsCoffeeCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.view = self.window.active_view()
        self.js_file = self.view.file_name()

        if self.js_file:
            self.new_buffer()
        else:
            self.new_buffer(self.view_contents())

    def view_contents(self):
        whole_file = sublime.Region(0, self.view.size())
        return self.view.substr(whole_file)

    def new_buffer(self, contents=None):
        view = self.window.new_file()
        output = self.js2coffee(contents)
        if output:
            edit = view.begin_edit()
            view.insert(edit, 0, output)
            view.end_edit(edit)
            self.window.run_command('show_overlay', {"overlay": "command_palette", "text": "Set Syntax: CoffeeScript"})

    def js2coffee(self, contents=None):
        if contents:
            js2coffee = subprocess.Popen(
                'js2coffee',
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )
            output, error = js2coffee.communicate(contents)
        else:
            with open(self.js_file, 'r') as js:
                js2coffee = subprocess.Popen(
                    'js2coffee',
                    stdin=js,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                )
                output, error = js2coffee.communicate()
        if error:
            self.write_to_console(error)
            self.window.run_command("show_panel", {"panel": "output.exec"})
            return None
        return output

    def write_to_console(self, str):
        self.output_view = self.window.get_output_panel("exec")
        selection_was_at_end = (
            len(self.output_view.sel()) == 1 and
            self.output_view.sel()[0] == sublime.Region(self.output_view.size())
        )
        self.output_view.set_read_only(False)
        edit = self.output_view.begin_edit()
        self.output_view.insert(edit, self.output_view.size(), str)
        if selection_was_at_end:
            self.output_view.show(self.output_view.size())
        self.output_view.end_edit(edit)
        self.output_view.set_read_only(True)
