import sublime, sublime_plugin

class QuackCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print('Saffs quack Snippets');
