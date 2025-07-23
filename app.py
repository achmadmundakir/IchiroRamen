from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data untuk website.
restaurant_info = {
    "name": "Ichiro Ramen",
    "tagline": "Ramen Jepang Otentik / 一郎ラーメン、日本の本格ラーメン",
    "location": "Agrowisata Loco Antik, Pabrik Gula Pangkah, Jl. Raya Timur, Pangkah, Kab. Tegal, Jawa Tengah",
    "whatsapp": "+62852 9182 9367",
    "whatsapp_link": "https://wa.me/6285291829367",
    "maps_link": "https://www.google.com/maps/place/Pabrik+Gula+Pangkah+(PG+Pangkah)+-+PTPN+IX/@-7.0522521,109.1333516,17z"
}

# Daftar menu ini sekarang akan berfungsi sebagai "database" sementara kita
menu_items = [
    {'img': 'images/shoyu.jpg', 'name': 'Shoyu Ramen', 'desc': 'Kaldu ayam gurih dengan bumbu shoyu, disajikan dengan chashu ayam, telur, dan nori.', 'price': 'Rp 35.000'},
    {'img': 'images/miso.jpg', 'name': 'Spicy Miso Ramen', 'desc': 'Kaldu miso pedas yang kaya rasa, toping daging ayam cincang pedas, jagung, dan daun bawang.', 'price': 'Rp 38.000'},
    {'img': 'images/tori.jpg', 'name': 'Tori Paitan', 'desc': 'Kaldu ayam kental dan creamy, memberikan rasa umami yang mendalam. Sempurna untuk pecinta ramen sejati.', 'price': 'Rp 40.000'},
    {'img': 'images/gyoza.jpg', 'name': 'Chicken Gyoza', 'desc': 'Pangsit Jepang berisi ayam dan sayuran, digoreng renyah di bagian bawah dan dikukus lembut.', 'price': 'Rp 25.000'}
]
promo_items = [
    {'img': 'images/karage.jpg', 'name': 'Karage Ramen Promo', 'desc': 'Makanan terbuat dari ayam yang berbalut tepung dan di bumbui khas jepang', 'price_original': 'Rp 42.000', 'price_promo': 'Rp 35.000'},
    {'img': 'images/ramenkeju.jpg', 'name': 'Cheese Ramen Special', 'desc': 'Perpaduan ramen creamy dengan keju mozarella meleleh di atasnya. Diskon 15%!', 'price_original': 'Rp 45.000', 'price_promo': 'Rp 38.500'},
    {'img': 'images/paket.jpg', 'name': 'Paket Combo Hemat', 'desc': '1 Shoyu Ramen + 3 pcs Gyoza + 1 Ocha. Lebih hemat!', 'price_original': 'Rp 65.000', 'price_promo': 'Rp 55.000'},
    {'img': 'images/Shusi.jpg', 'name': 'Shusi', 'desc': 'Makanan khas jepang terbuat dari nasi dan salmon yang di gulung.', 'price_original': 'Rp 40.000', 'price_promo': 'Rp 32.000'}
]

@app.route('/')
def home():
    return render_template('index.html', info=restaurant_info, menu=menu_items)

@app.route('/tentang')
def about():
    return render_template('about.html', info=restaurant_info)

@app.route('/menu')
def menu():
    return render_template('menu.html', 
                           info=restaurant_info, 
                           menu=menu_items, 
                           promos=promo_items)

@app.route('/tambah', methods=['GET', 'POST'])
def add_item_page():
    if request.method == 'POST':
        nama_baru = request.form['nama_makanan']
        harga_baru = request.form['harga']
        deskripsi_baru = request.form['deskripsi']

        menu_baru = {
            'img': 'images/placeholder.jpg',
            'name': nama_baru,
            'desc': deskripsi_baru,
            'price': harga_baru
        }
        menu_items.append(menu_baru)
        return redirect(url_for('menu'))
    return render_template('tambah.html', info=restaurant_info)

@app.route('/kontak')
def contact():
    return render_template('kontak.html', info=restaurant_info)

if __name__ == '__main__':
    app.run(debug=True)