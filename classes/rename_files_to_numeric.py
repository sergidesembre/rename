from classes.rename_files import RenameFiles, File

class RenameFilesToNumeric(RenameFiles):
    def rename(self):
        modified = self.original_files()
        counter = 0

        for key, file in modified.items():
            counter = counter + 1
            renamed_file = File("%s/%s.%s" % (file.path, counter, file.extension), str(file.id))

            self.modified.update({
                str(renamed_file.id): renamed_file
            })