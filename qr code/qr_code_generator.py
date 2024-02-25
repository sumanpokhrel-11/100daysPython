import qrcode

#enter the link of the url to create a qrcode
image = qrcode.make('https://github.com/sumanpokhrel-11')
#save the generated email of qrcode in png format
image.save('github_suman_qr.png')
