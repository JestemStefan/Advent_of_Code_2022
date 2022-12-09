import timeit


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.parent = parent
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name}"


class Directory:
    def __init__(self, name, parent=None, children=None):
        self._cached_size = None
        self.name = name
        self.parent = parent
        self.children = children if children else {}

    def add_subfolder(self, subfolder: "Directory"):
        self.children[subfolder.name] = subfolder

    def add_file(self, file: File):
        self.children[file.name] = file

    @property
    def size(self):
        if self._cached_size:
            return self._cached_size

        if not self.children:
            return 0

        self._cached_size = sum([child.size for child in self.children.values()])
        return self._cached_size

    def __str__(self):
        return f"{self.name} - {self.size}"


class FileSystem:
    def __init__(self):
        self.dir_list = []
        self.root = Directory(name="/", parent=None, children={})
        self.curr_dir = self.root

    def chdir(self, dir_name):
        if dir_name == "/":
            self.curr_dir = self.root

        elif dir_name == "..":
            self.curr_dir = self.curr_dir.parent

        else:
            self.curr_dir = self.curr_dir.children[dir_name]

    def mkdir(self, dir_name):
        if dir_name not in self.curr_dir.children:
            new_dir = Directory(name=dir_name, parent=self.curr_dir)
            self.curr_dir.add_subfolder(new_dir)
            self.dir_list.append(new_dir)

    def touch(self, file_name, file_size):
        if file_name not in self.curr_dir.children:
            new_file = File(name=file_name, size=int(file_size), parent=self.curr_dir)
            self.curr_dir.add_file(new_file)


def solution_part_1():
    file_system = FileSystem()
    with open("input_data.txt") as file:
        for line in file:
            data = line.strip().split()

            match data:
                case ["$", "cd", dir_name]:
                    file_system.chdir(dir_name)

                case ["$", "ls"]:
                    pass

                case ["dir", dir_name]:
                    file_system.mkdir(dir_name)

                case [file_size, file_name]:
                    file_system.touch(file_name, file_size)

    return sum(d.size for d in file_system.dir_list if d.size < 100_000)


def solution_part_2():
    total_disk_space = 70_000_000
    required_space = 30_000_000

    file_system = FileSystem()
    with open("input_data.txt") as file:
        for line in file:
            data = line.strip().split()

            match data:
                case ["$", "cd", dir_name]:
                    file_system.chdir(dir_name)

                case ["$", "ls"]:
                    pass

                case ["dir", dir_name]:
                    file_system.mkdir(dir_name)

                case [file_size, file_name]:
                    file_system.touch(file_name, file_size)

    minimum_space_free = required_space - (total_disk_space - file_system.root.size)

    return min(d.size for d in file_system.dir_list if d.size > minimum_space_free)


if __name__ == "__main__":
    times = 10_000
    print(
        f"Solution Part 1 = {solution_part_1()}, "
        f'Time = {timeit.timeit("solution_part_1()", globals=locals(), number=times)/(times) * 1000} ms'
    )
    print(
        f"Solution Part 2 = {solution_part_2()}, "
        f'Time = {timeit.timeit("solution_part_2()", globals=locals(), number=times)/(times) * 1000} ms'
    )
