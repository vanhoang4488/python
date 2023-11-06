#Nguồn: https://github.com/Mathpix/api-examples/blob/master/python/batch.py

import os
import sys
import time
import json
import requests

# Thiết lập môi trường kết nối.
# Cần có app_api và app_key khi đăng ký api trên Mathpix sẽ có.
# Tiến hành đọc thông tin cần thiết 

server = os.environ.get('MATHPIX_API', 'https://api.mathpix.com') # - server sẽ nhận 1 Mapping với Key = MATHPIX_API, Value = https://api.mathpix.com
app = os.environ['MATHPIX_APP_ID'] # - Lấy giá trị của trường có tên là MATHPIX_APP_ID
key = os.environ['MATHPIX_APP_KEY'] # - Lấy giá trị của trường có tên là MATHPIX_APP_KEY
headers = {'app_id': app, 'app_key': key, 'Content-type': 'application/json'} 

###

# Lấy ra danh sách file ảnh để tiến hành xử lý.

interactive = True # - Cài này thực tế dùng để làm gì, vẫn không hiểu?

urlbase = 'E:\\python\\_hoc_tap\\ImagesScanByMathpix\\image'
images = [
	'algebra.jpg', 'cases_hw.jpg', 'cases_printed_0.jpg', 'cases_printed_1.jpg',
	'cm_hw.jpg', 'determinant.jpg', 'fraction.jpg', 'graph.jpg', 'intergral.jpg',
	'limit.jpg', 'matrix_2x2.jpg', 'overline_printed.jpg', 'text_hw_0.jpg', 'vec_hw.jpg']

n = len(images)

urls = {}
for i, img in enumerate(images):
	urls['url-' + str(i+1).zfill(2)] = urlbase + img;

###

# Gửi dữ liệu lên Server dưới dạng Json và nhận về dữ liệu dưới dạng Json.
start = time.time()

body = {'urls': urls, 'formats': ['latex_normal']}
response = requests.post(server + '/v3/batch', headers=headers, data=json.dumps(urls))
info = response.text
print(info)
b = info['batch_id']
print("Batch_id is %s", b)

###

# - Tính toán thời gian thực hiện yêu cầu hàng loạt để tiến hành gọi lại.
# - Trên lý thuyết 1 yêu cầu hàng loại mất 1s.
# - Nhưng thực tế thời gian yêu cầu hàng loại còn phụ thuộc vào lưu lượng truy cập do yêu cầu hàng loại không thuộc loại được ưu tiên.

progress = 0
estimate = n

if interactive:
	maxwait = 2.0

while True:
	timeout = float(estimate)
	if interactive: 
		pct = float(100 * progress) /  n
		sys.stdout.write('\r{0:5.1f}%{1}/{2}\033[K'.format(pct, progess, n))
		sys.stdout.flush()
		timeout = min(timeout, maxwait)

	time.sleep(timeout) # Tạm dừng chương trình trong timeout giây.

	
	r = request.get(server + '/v3/batch' + b, headers=headers)
	current = json.loads(r.text)
	results = current['results']
	progress = len(results)
	if progess == n:
		if interactive:
			print('\r{0:5.1f}%{1}/{2}'.format(100.0, progess, n))

		print('Batch results:')
		for key in sorted(results):
			result = results[key]
			answer = result.get('latex_normal', '') or result.get('error', '???')
			print(key + ': ' + answer)
		
		break	
	
	# - Điều chỉnh thời gian ước tính để tiến hành gọi lại dựa trên số lượng yêu cầu còn lại cần xử lý.
	if (progress > 0):
		estimate = float(n - progress) * (time.time() - start) / float(progess)	

###	

