import qrcode
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont

ROOT = settings.BASE_DIR


def create_image(name, id, img):

	img = Image.open(ROOT / f'media/uploads/{img}')
	img_bg = img.copy()

	qr = qrcode.QRCode(
		box_size=12,
		version=1
	)

	qr.add_data(id)
	qr.make()

	img_qr = qr.make_image(fill_color='black', back_color='white')
	img_qr.save(ROOT / 'media/temp/qrcode_inset.png')

	qr_inset = Image.open(ROOT / 'media/temp/qrcode_inset.png')

	x = img_bg.width - (qr_inset.width + 290)
	y = img_bg.height - (qr_inset.height + 54)

	img_bg.paste(qr_inset, (x, y))
	img_bg.save(ROOT / 'media/temp/ticket.png')

	# Add text
	image = Image.open(ROOT / 'media/temp/ticket.png')
	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype(ROOT / 'static/fonts/RobotoSlab.ttf', 60)
	text_color = 'black'
	name_length = draw.textlength(name, font)

	x = (image.width - name_length) / 2
	y = image.height / 2 + 300
	name_position = (x, y)

	draw.text(name_position, name, fill=text_color, font=font)
	image.save(ROOT / 'media/temp/ticket_text.png')
