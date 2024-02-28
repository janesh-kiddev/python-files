import  qrcode

def generate(text):
    
    qr = qrcode.QRCode(version = 1,error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4)
    
    qr.add_data(text)
    qr.make(fit = True)
    image = qr.make_image(fill_color = 'black',back_color = 'white')
    image.save("qr_img.png")

generate("https://www.apple.com/in/store?afid=p238%7Cs8Vs8GkTq-dc_mtid_187079nc38483_pcrid_689251521289_pgrid_112258962467_pntwk_g_pchan__pexid__&cid=aos-IN-kwgo-brand--slid---product")
