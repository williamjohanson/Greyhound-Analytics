import webbrowser
import urllib.request

uf = urllib.request.urlopen('https://www.grnz.co.nz/catch-the-action/13906/result-summary.aspx')
#webbrowser.open_new('https://www.facebook.com/photo.php?fbid=1469428493165267&set=a.112206535554143&type=3&theater')

html = uf.read()

print(html)