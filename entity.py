class Video:
    def __init__(self, path, title, description, keyword, viewCount):
        self.path = path
        self.title = title
        self.description = description
        self.keyword = keyword
        self.viewCount = viewCount

    def to_dict(self):
        return {
            "path": self.path,
            "title": self.title,
            "description": self.description,
            "keyword": self.keyword,
            "viewCount": self.viewCount,
        }
