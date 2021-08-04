import sys
import os
sys.path.append(os.path.dirname(__file__) + "/..")

import preprocesser

def test():
  assert preprocesser.hello() == "hello"

def testRemoveHashtag():
  assert preprocesser.removeHashtag("hogehoge #huga") == "hogehoge "

def testRemoveUrl():
  assert preprocesser.removeUrl("hogehoge http://example.com/?user=1#hoge https://example.com/?user=1#hoge") == "hogehoge  "

def testRemoveMention():
  assert preprocesser.removeMention("@taro hello") == " hello"

# TODO
# def testRemoveRetweet():