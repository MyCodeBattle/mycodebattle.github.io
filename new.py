import sys
import time

current_time = time.strftime('%Y-%m-%d-', time.localtime())
filename = current_time + sys.argv[1] + '.md'
f = open('./_posts/' + filename, 'w')

content = '---\ntitle: {}\nlayout: post\ndate: '.format(sys.argv[1]) + current_time[:-1] + '\ncategories: \n---\n'
f.write(content)
f.close()



