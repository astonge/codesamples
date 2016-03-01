import sublime, sublime_plugin

class ListitemCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if(not region.empty()):
				line = self.view.line(region)
				line_contents = '<li>'+self.view.substr(line).strip()+'</li>'
				self.view.replace(edit,region,line_contents)

class AhrefitemCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for region in self.view.sel():
			if(not region.empty()):
				line = self.view.line(region)
				line_contents = '<a href="#">'+self.view.substr(line).strip()+'</a>'
				self.view.replace(edit,region,line_contents)				