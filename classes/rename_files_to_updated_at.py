from classes.rename_files import RenameFiles, File
import time, os

class RenameFilesToUpdatedAt(RenameFiles):
    def rename(self):
        modified = self.original_files()

        for key, file in modified.items():
            renamed_file_name = time.strftime('%Y%m%d%H%M%S', time.gmtime(os.path.getmtime(str(file))))
            renamed_file = File("%s/%s.%s" % (file.path, renamed_file_name, file.extension), str(file.id))

            self.modified.update({
                str(renamed_file.id): renamed_file
            })