import urllib
import re

page = urllib.urlopen("http://www.gcsnc.com/pages/gcsnc/Departments/804180865931116562")
content = page.read()
print content
print re.findall(r"\+\d{2}\s?0?\d{10}",content)
print re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",content)
