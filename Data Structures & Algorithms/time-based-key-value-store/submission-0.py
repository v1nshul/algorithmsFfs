class TimeMap:

    def __init__(self):
        self.timemap = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key] = [timestamp,value]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap.keys():
            if timestamp != self.timemap[key][0]:
                return self.timemap[key][1]
            return self.timemap[key][1]
        return ""
