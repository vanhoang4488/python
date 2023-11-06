# Nguồn: https://github.com/Mathpix/api-examples/blob/master/python/formats.py

import mathpix
import json


# Ví dụ sử dụng Mathpix OCR với nhiều định dạng kết quả.
# Vì vậy ta setup giá trị của ocr là ['math', 'text']
# formats : ['text', 'latex_styled', 'asciimath', 'mathml']
# Ta xác định toán học trong kết quả văn bản bằng việc được bao quanh bằng "$"

r = mathpix.latex({
		'src': mathpix.image_uri('../images/mixed_text_match.jpg'),
		'ocr': ['math', 'text'],
		'skip_recrop': True,
		'formats': ['text', 'latex_styled', 'asciimath', 'mathml'],
		'format_options': {
			'text' : {
				'transforms': ['rm_spaces', 'rm_newlines'],
				'math_delims': ['$', '$']
			},
			'latex-styled' : {'transforms': ['rm_spaces']}
		}
	})

# Kết quả có thể khác so với LateX spacing hoặc thuộc tính MathML.

print('Expected for r["text"]: "$-10 x^{2}+5 x-3$ and $-7 x+4$"')
print('Expected for r["latex_styled"]: "-10 x^{2}+5 x-3 \\text { and }-7 x+4')
print('Expected for r["asciimath"]: "-10x^(2)+5x-3\\" and \\"-7x+4')
print('Expected for r["mathml"]: "<math><mo>\u2212</mo><mn>10</mn><msup><mi>x</mi><mn>2</mn></msup><mo><mn>5</mn><mi>x</mi><mo>\u2212</mo><mn>3</mn><mtext>\u00a0and\u00a0</mtext><mo>\u2212</mo><mn>7</mn><mi>x</mi><mo>+</mo><mn>4</mn></math>"')

print("\nResult object: ", json.dumps(r, indent=4, sort_keys=True))