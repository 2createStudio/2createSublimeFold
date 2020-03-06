import sublime, sublime_plugin

class CustomFoldUnfoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Fixing selection and toggleing
        for s in self.view.sel():
            r = s
            empty_region = r.empty()
            if empty_region:
                self.view.run_command("run_emmet_action", {"action": "balance_outward"})
        # ---------------------------------

        new_sel = []

        for s in self.view.sel():
            r = s
            empty_region = r.empty()
            if empty_region:
                r = sublime.Region(r.a - 1, r.a + 1)

            unfolded = self.view.unfold(r)
            if len(unfolded) == 0:
                self.view.fold(s)
            elif empty_region:
                for r in unfolded:
                    new_sel.append(r)

        if len(new_sel) > 0:
            self.view.sel().clear()
            for r in new_sel:
                self.view.sel().add(r)

