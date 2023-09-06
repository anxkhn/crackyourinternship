class Codec:

    links = {}
    links2 = {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.links:
            x = len(self.links)
            self.links[longUrl] = x
            self.links2[x] = longUrl
            return x
        return self.links[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.links2[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))