import os
import argparse


class Dirsystem(object):

    def __init__(self, argv):
        self.root = argv.root
        self.base_abs_path = os.path.abspath(self.root)

    def walk(self):
        output_list = []

        files = [k for k in os.listdir(self.root)
                 if os.path.isfile(os.path.join(self.root, k))]
        directories = [k for k in os.listdir(self.root)
                       if os.path.isdir(os.path.join(self.root, k))]
        output_list.append((self.root, directories, files))

        self._recurse(self.root, output_list)

        return output_list

    def _recurse(self, parent_path, output_buff):
        all_dir = [k for k in os.listdir(parent_path)
                   if os.path.isdir(os.path.join(parent_path, k))]

        for folder in all_dir:
            curr_path = os.path.join(parent_path, folder)

            files = [k for k in os.listdir(curr_path)
                     if os.path.isfile(os.path.join(curr_path, k))]
            directories = [k for k in os.listdir(curr_path)
                           if os.path.isdir(os.path.join(curr_path, k))]
            output_buff.append((curr_path, directories, files))

            self._recurse(curr_path, output_buff)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    args = parser.parse_args()
    print(Dirsystem(args).walk())
