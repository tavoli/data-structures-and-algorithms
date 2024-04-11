class Page:
  def __init__(self, url: str, prev=None):
    self.url = url
    self.prev = prev
    self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
      self.current = Page(homepage)

    def visit(self, url: str) -> None:
      self.current.next = Page(url, self.current)
      self.current = self.current.next
        
    def back(self, steps: int) -> str:
      while steps > 0 and self.current.prev:
        self.current = self.current.prev
        steps -= 1 
      return self.current.url

    def forward(self, steps: int) -> str:
      while steps > 0 and self.current.next:
        self.current = self.current.next
        steps -= 1
      return self.current.ur
