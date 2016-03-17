import sys
import time

current_time = time.strftime('%Y-%m-%d-', time.localtime())
filename = current_time + sys.argv[1] + '.md'
f = open('I:/blog/_posts/' + filename, 'w')

content = '---\ntitle: \nlayout: post\ndate: ' + current_time[:-1] + '\ncategories: \n---\n'
f.write(content)
f.close()



