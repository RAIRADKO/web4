from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/agenda')
def show_agenda():
    return render_template('agenda.html')

@main.route('/bidangIKP')
def bidang_ikp():
    return render_template('bidangIKP.html')

@main.route('/bidangPPLKC')
def bidang_pplkc():
    return render_template('bidangPPLKC.html')

@main.route('/bidangTISP')
def bidang_tisp():
    return render_template('bidangTISP.html')

@main.route('/budaya')
def show_budaya():
    return render_template('budaya.html')

@main.route('/dokumen-pelaksana')
def dokumen_pelaksana():
    return render_template('dokumen-pelaksana.html')

@main.route('/download')
def download_file():
    return render_template('download.html')

@main.route('/foto')
def galeri_foto():
    return render_template('foto.html')

@main.route('/hoaks')
def info_hoaks():
    return render_template('hoaks.html')

@main.route('/hubungi-kami')
def kontak():
    return render_template('hubungi-kami.html')

@main.route('/kebijakan')
def kebijakan():
    return render_template('kebijakan.html')

@main.route('/kebijakan-umum-s')
def kebijakan_umum():
    return render_template('kebijakan-umum-s.html')

@main.route('/kegiatan')
def kegiatan():
    return render_template('kegiatan.html')

@main.route('/kim')
def kim():
    return render_template('kim.html')

@main.route('/laporan-isu-hoaks')
def laporan_hoaks():
    return render_template('laporan-isu-hoaks.html')

@main.route('/layanan-skpd')
def layanan_skpd():
    return render_template('layanan-skpd.html')

@main.route('/LHKAN')
def lhkan():
    return render_template('LHKAN.html')

@main.route('/LKjIP')
def lkjip():
    return render_template('LKjIP.html')

@main.route('/moap')
def moap():
    return render_template('moap.html')

@main.route('/news')
def berita():
    return render_template('news.html')

@main.route('/pip')
def pip():
    return render_template('pip.html')

@main.route('/ppid')
def ppid():
    return render_template('ppid.html')

@main.route('/profil')
def profil():
    return render_template('profil.html')

@main.route('/rekrutmen')
def rekrutmen():
    return render_template('rekrutmen.html')

@main.route('/sekretariat')
def sekretariat():
    return render_template('sekretariat.html')

@main.route('/skm')
def skm():
    return render_template('skm.html')

@main.route('/smart-city')
def smart_city():
    return render_template('smart-city.html')

@main.route('/sosial')
def sosial():
    return render_template('sosial.html')

@main.route('/spbe')
def spbe():
    return render_template('spbe.html')

@main.route('/struktur-organisasi')
def struktur_organisasi():
    return render_template('struktur-organisasi.html')

@main.route('/subbagian-perencanaan-dan-keuangan')
def subbagian_perencanaan():
    return render_template('subbagian-perencanaan-dan-keuangan.html')

@main.route('/subbagian-umum-dan-kepegawaian')
def subbagian_umum():
    return render_template('subbagian-umum-dan-kepegawaian.html')

@main.route('/tugas-pokok-dan-fungsi')
def tupoksi():
    return render_template('tugas-pokok-dan-fungsi.html')

@main.route('/vidio')
def vidio():
    return render_template('vidio.html')

@main.route('/visi-dan-misi')
def visi_misi():
    return render_template('visi-dan-misi.html')
