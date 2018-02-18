from bs4 import BeautifulSoup

__author__ = 'cao'
# coding:utf-8


html = '''<table>
<tr>
    <td>Alex</td>
    <td>Ben</td>
    <td>Chris</td>
</tr>
<tr>
    <td>Alex</td>
    <td>Ben</td>
    <td>Chris</td>
</tr>
<tr>
    <td>Alex</td>
    <td>Ben</td>
    <td>Chris</td>
</tr>

</table>'''

bsObj = BeautifulSoup(html, "html.parser")
secondTds = bsObj.find_all('td')[1::3]
print(secondTds)