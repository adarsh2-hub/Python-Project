class Playlist:
    def __init__(self):
        self.list=["song a","song b","song c","song d","song e","song f"]
    def __len__(self):
        return len(self.list)
playlist=Playlist()
print(len(playlist))