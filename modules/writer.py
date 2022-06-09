class Writer:
    """Writes the solved maze in a .txt file and notifies user."""
    def maze_to_text_file(self, _maze, filename):
        with open(filename, "w+") as f:
            for line in _maze:
                for item in line:
                    f.write(item)
                    f.write("\t")
                f.write("\n")
        print("Solution in", filename)