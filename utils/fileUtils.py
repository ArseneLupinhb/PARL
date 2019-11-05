import os


class file_utils:
	def exist_file(path):
		return os._exists(path)

	def delete_file(path):
		os.remove(path)
