class Codec:

    links = {}
    links2 = {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.links:
            x = len(self.links)
            self.links[longUrl] = x
            self.links2[x] = longUrl
            return self.links[longUrl]    
        return     

    def decode(self, shortUrl: str) -> str:
        return self.links2[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))