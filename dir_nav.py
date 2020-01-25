import os
import argparse


class FileTreeMaker2(object):

    def __init__(self, argv):
        self.root = argv.root

    def make(self):
        print("root:%s" % self.root)
        buf = []
        path_parts = self.root.rsplit(os.path.sep, 1)
        buf.append("[%s]" % (path_parts[-1],))
        self._recurse(self.root, os.listdir(self.root), "", buf)
        print("buf:",buf)
        output_str = "\n".join(buf)

        return output_str

    def _recurse(self, parent_path, file_list, prefix, output_buf):
        if len(file_list) == 0:
            return
        else:

            file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
            for idx, sub_path in enumerate(file_list):
                full_path = os.path.join(parent_path, sub_path)
                idc = "|-"
                if idx == len(file_list) - 1:
                    idc = "'-"
                if os.path.isdir(full_path):
                    output_buf.append("%s%s[%s]" % (prefix, idc, sub_path))
                    if len(file_list) > 1 and idx != len(file_list) - 1:
                        temp_prefix = prefix + "|  "
                    else:
                        temp_prefix = prefix + "   "
                    self._recurse(full_path, os.listdir(full_path), temp_prefix, output_buf)
                elif os.path.isfile(full_path):
                    output_buf.append("%s%s%s" % (prefix, idc, sub_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-o", "--output", help="output file name", default="")

    args = parser.parse_args()
    print(FileTreeMaker2(args).make())
