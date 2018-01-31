# codding:utf-8
import os


class DiffFiles(object):

    def __init__(self):
        # self._root = root
        self._files = {}
        self._file_suffix = ['avi', 'mp4', 'wnv', 'flv', 'rmvb', 'rm']
        # self.f_suffix = set()

    @property
    def files(self):
        return self._files

    # @property
    # def root(self):
    #     return self._root
    #
    # @root.setter
    # def root(self, path):
    #     self._root = path

    def travel(self, file_path):
        for parent, dirs, files in os.walk(file_path):

            if dirs:
                for file_dir in dirs:
                    # print("current dirs is : " + parent + '/' + d)
                    self.travel(parent + '\\' + file_dir)
            else:
                for f in files:
                    # print(os.path.splitext(f)[1][1:])
                    if os.path.splitext(f)[1][1:] in self._file_suffix:
                        # print("current files is : " + f)
                        if not self._files.get(f):
                            self._files[f] = []
                        if parent + '\\' + f not in self._files[f]:
                            self._files[f].append(parent + '\\' + f)

    def travel_multiple_path(self, file_paths):
        for file_path in file_paths:
            self.travel(file_path)


if __name__ == '__main__':
    paths = ["G:\\Downloads", "F:\\ttt"]
    d = DiffFiles()
    d.travel_multiple_path(paths)

    f_out = open('file_list', 'w+', encoding='utf8')
    for key in sorted(d.files.keys()):
        # if len(d.files.get(key)) > 1:
            print('file: ' + key + ", path : " + str(d.files.get(key)))
            f_out.write('file: ' + key + ", path : " + str(d.files.get(key)) + "\r\n")
    f_out.close()
