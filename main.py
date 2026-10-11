import streamlit as st
import time
from datetime import datetime, timedelta
import pandas as pd

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Healthy Fit Buddy",
    page_icon="🏃‍♂️",
    layout="wide"
)

# Tajuk Utama
st.title("✨ HEALTHY FIT BUDDY ✨")
st.subheader("🏃‍♂️    RAKAN DIGITAL GAYA HIDUP SIHAT KAMU 🧘‍♀️")
st.markdown("---")

# Menu Navigasi di Sidebar
st.sidebar.title("📌 Menu Utama")
pilihan_menu = st.sidebar.radio(
    "Pilih Modul Kesihatan:",
    [
        "1. Kira BMI",
        "2. Kira Kalori Harian (BMR & TDEE)",
        "3. Target Air Minum",
        "4. Rutin & Pemasa Senaman Express",
        "5. Kalkulator Waktu Tidur Optima",
        "6. Cadangan Makanan Sihat",
        "7. Cadangan Aktiviti Harian",
        "8. Mood Check Harian",
        "9. Pilihan Makanan Sihat",
        "10. Cabaran Gaya Hidup Sihat"
    ]
)

# -----------------------------------------------------------------------------
# 1. PENGIRAAN BMI
# -----------------------------------------------------------------------------
if pilihan_menu == "1. Kira BMI":
    st.header("⚖️ 1. Pengiraan BMI (Tahap Ideal Badan)")
    
    col1, col2 = st.columns(2)
    with col1:
        berat = st.number_input("👉 Masukkan berat badan (kg):", min_value=1.0, max_value=300.0, value=60.0, step=0.5)
    with col2:
        tinggi_cm = st.number_input("👉 Masukkan tinggi (cm):", min_value=30.0, max_value=250.0, value=170.0, step=1.0)

    if st.button("Kira BMI"):
        tinggi_m = tinggi_cm / 100
        bmi = berat / (tinggi_m ** 2)

        st.metric(label="Skor BMI Kamu", value=f"{bmi:.2f}")

        if bmi < 18.5:
            status = "Terlalu Kurus / Underweight 🦴"
            nasihat = "Bolehlah tambah kuantiti makanan yang berzat & protein tinggi. Jom sado sikit! 💪"
            st.warning(f"**Status:** {status}\n\n💡 **Nasihat:** {nasihat}")
        elif 18.5 <= bmi < 25:
            status = "Mantap & Ideal / Normal 🌟"
            nasihat = "Bagus! Kekalkan pemakanan seimbang & gaya hidup aktif ni, steady! 🔥"
            st.success(f"**Status:** {status}\n\n💡 **Nasihat:** {nasihat}")
        elif 25 <= bmi < 30:
            status = "Terlebih Berat Badan / Overweight 🍕"
            nasihat = "Lakukan senaman berkala dan kawal saiz hidangan. Kurangkan snek malam tau! 😉"
            st.warning(f"**Status:** {status}\n\n💡 **Nasihat:** {nasihat}")
        else:
            status = "Obesiti ⚠️"
            nasihat = "Jom mula bertindak! Rajin-rajinkan diri bersenam dan jumpa pakar kesihatan kalau perlu! ❤️"
            st.error(f"**Status:** {status}\n\n💡 **Nasihat:** {nasihat}")

# -----------------------------------------------------------------------------
# 2. PENGIRAAN KALORI HARIAN
# -----------------------------------------------------------------------------
elif pilihan_menu == "2. Kira Kalori Harian (BMR & TDEE)":
    st.header("🔥 2. Pengiraan Kalori Harian")
    
    jantina = st.selectbox("👉 Jantina:", ["Lelaki", "Perempuan"])
    col1, col2, col3 = st.columns(3)
    with col1:
        umur = st.number_input("👉 Umur (tahun):", min_value=1, max_value=120, value=25)
    with col2:
        berat = st.number_input("👉 Berat badan (kg):", min_value=1.0, max_value=300.0, value=65.0)
    with col3:
        tinggi = st.number_input("👉 Tinggi (cm):", min_value=30.0, max_value=250.0, value=170.0)

    st.write("⚡ **Pilih Tahap Aktiviti Harian Kamu:**")
    aktiviti_dict = {
        "🛋️ Rendah (Banyak duduk / jarang senaman)": 1.2,
        "🚶‍♂️ Sederhana (Senaman ringan 1-3 hari/minggu)": 1.375,
        "🏃‍♂️ Aktif (Senaman 3-5 hari/minggu)": 1.55,
        "🏋️‍♂️ Sangat Aktif (Senaman padu 6-7 hari/minggu)": 1.725
    }
    pilihan_aktiviti = st.selectbox("Aktiviti Harian:", list(aktiviti_dict.keys()))

    if st.button("Kira Kalori"):
        faktor = aktiviti_dict[pilihan_aktiviti]
        
        # Formula BMR (Mifflin-St Jeor)
        if jantina == "Lelaki":
            bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) + 5
        else:
            bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) - 161

        tdee = bmr * faktor

        col_a, col_b = st.columns(2)
        col_a.metric("🔥 BMR (Kalori rehat)", f"~{bmr:.0f} kcal/hari")
        col_b.metric("⚡ TDEE (Jumlah Kalori Harian)", f"~{tdee:.0f} kcal/hari")

        st.markdown("### 💡 Panduan Pengiraan Kalori:")
        st.info(f"""
        * 🟢 **Kekal berat badan:** ~{tdee:.0f} kcal/hari
        * 🟡 **Kurangkan berat badan:** ~{tdee - 500:.0f} kcal/hari (-0.5kg seminggu)
        * 🔵 **Tambah berat badan:** ~{tdee + 500:.0f} kcal/hari (+0.5kg seminggu)
        """)

# -----------------------------------------------------------------------------
# 3. TARGET AIR MINUM
# -----------------------------------------------------------------------------
elif pilihan_menu == "3. Target Air Minum":
    st.header("💧 3. Target Air Minum Harian")
    
    berat = st.number_input("👉 Masukkan berat badan kamu (kg):", min_value=1.0, max_value=300.0, value=60.0)

    if st.button("Kira Sasaran Air"):
        sasaran_ml = berat * 35
        sasaran_liter = sasaran_ml / 1000

        st.success(f"💦 **Sasaran Air Harian Kamu:** ~{sasaran_liter:.2f} Liter ({sasaran_ml:.0f} ml)")
        
        st.markdown("### 🗓️ Cadangan Jadual Minum Air (8 Gelas Sehari):")
        jadual = [
            {"⏰ Waktu": "08:00 PAGI", "🥛 Cadangan Minum": "1 Gelas lepas bangun tidur 🌅"},
            {"⏰ Waktu": "10:00 PAGI", "🥛 Cadangan Minum": "1 Gelas time buat kerja 💻"},
            {"⏰ Waktu": "12:30 T/HARI", "🥛 Cadangan Minum": "1 Gelas sebelum makan tengah hari 🍲"},
            {"⏰ Waktu": "02:30 PETANG", "🥛 Cadangan Minum": "1 Gelas biar tak ngantuk 😴"},
            {"⏰ Waktu": "04:30 PETANG", "🥛 Cadangan Minum": "1 Gelas petang ☕"},
            {"⏰ Waktu": "06:30 PETANG", "🥛 Cadangan Minum": "1 Gelas sebelum makan malam 🥗"},
            {"⏰ Waktu": "08:30 MALAM", "🥛 Cadangan Minum": "1 Gelas santai malam 🌙"},
            {"⏰ Waktu": "10:00 MALAM", "🥛 Cadangan Minum": "1 Gelas sebelum tidur 🛌"}
        ]
        
        df_jadual = pd.DataFrame(jadual)
        st.table(df_jadual)
        st.caption("✨ Tips: Bawa botol air ke mana-mana supaya tak lupa minum air!")

# -----------------------------------------------------------------------------
# 4. RUTIN & PEMASA SENAMAN EXPRESS
# -----------------------------------------------------------------------------
elif pilihan_menu == "4. Rutin & Pemasa Senaman Express":
    st.header("⏱️ 4. Rutin Senaman Express (Workout)")
    
    rutin = [
        ("⭐ Jumping Jacks (Lompat Bintang)", 30),
        ("🧘 Rehat & Hembus Nafas", 10),
        ("🦵 Bodyweight Squats (Cangkung)", 30),
        ("🧘 Rehat & Hembus Nafas", 10),
        ("💪 Push-ups (Tekan Tubi)", 30),
        ("🧘 Rehat & Hembus Nafas", 10),
        ("🧱 Plank (Tahan Badan)", 30)
    ]

    st.markdown("### 🔥 Senarai Rutin Litar Express:")
    for idx, (aktiviti, durasi) in enumerate(rutin, 1):
        st.write(f"**{idx}.** {aktiviti} ──▶ `{durasi} saat`")

    st.markdown("---")
    if st.button("🚀 Mula Workout Sekarang!"):
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        st.info("Ready! Workout bermula dalam 3 saat...")
        time.sleep(3)

        total_steps = len(rutin)
        for idx, (aktiviti, durasi) in enumerate(rutin):
            status_text.markdown(f"### 🔔 >>> {aktiviti.upper()} ({durasi} SAAT) <<<")
            timer_place = st.empty()
            
            for saat in range(durasi, -1, -1):
                timer_place.subheader(f"⏱️ Masa berbaki: `{saat}` saat...")
                time.sleep(1)
            
            progress_bar.progress((idx + 1) / total_steps)

        status_text.empty()
        st.balloons()
        st.success("🎉 Tahniah kamu! Berjaya habiskan rutin senaman hari ini! 🔥🥳")

# -----------------------------------------------------------------------------
# 5. KALKULATOR WAKTU TIDUR
# -----------------------------------------------------------------------------
elif pilihan_menu == "5. Kalkulator Waktu Tidur Optima":
    st.header("🌙 5. Kalkulator Waktu Tidur Optima")
    st.info("💡 1 Kitaran tidur mengambil masa ~90 minit.\n\n💡 Tidur yang segar perlukan 5-6 kitaran penuh (~7.5 - 9 jam).")

    waktu_bangun_input = st.time_input("👉 Pukul berapa kamu ingin bangun esok?", datetime.strptime("06:30", "%H:%M").time())

    if st.button("Kira Waktu Tidur"):
        waktu_bangun = datetime.combine(datetime.today(), waktu_bangun_input)
        masa_lena = 15  # purata 15 minit untuk lena

        st.markdown(f"### 😴 Nak bangun segar pukul `{waktu_bangun_input.strftime('%I:%M %p')}`? Sila mula tidur pada waktu ni:")

        for kitaran in [6, 5, 4]:
            jumlah_minit = (kitaran * 90) + masa_lena
            waktu_tidur = waktu_bangun - timedelta(minutes=jumlah_minit)
            jam = (kitaran * 90) / 60
            st.success(f"🛏️ **{waktu_tidur.strftime('%I:%M %p')}** ──▶ ({kitaran} kitaran / ~{jam:.1f} jam tidur)")

        st.caption("✨ Nota: Waktu di atas dah termasuk anggaran 15 minit masa untuk lelapkan mata.")

# -----------------------------------------------------------------------------
# 6. CADANGAN MAKANAN SIHAT
# -----------------------------------------------------------------------------
elif pilihan_menu == "6. Cadangan Makanan Sihat":
    st.header("🍎 6. Cadangan Makanan Sihat")
    
    pilihan = st.selectbox(
        "Pilih waktu makan untuk dapatkan cadangan makanan:",
        ["🌅 Sarapan", "☀️ Makan Tengah Hari", "🌙 Makan Malam", "🍎 Snek Sihat"]
    )

    menu = {
        "🌅 Sarapan": ["🥚 Telur rebus + roti gandum", "🥣 Oat + buah-buahan", "🍌 Pisang + yogurt"],
        "☀️ Makan Tengah Hari": ["🍚 Nasi + ayam panggang + sayur", "🐟 Ikan + nasi + ulam", "🥗 Nasi + telur + sayur"],
        "🌙 Makan Malam": ["🍲 Sup ayam + sayur", "🐟 Ikan bakar + sayur", "🥗 Salad + telur / ayam"],
        "🍎 Snek Sihat": ["🍌 Pisang", "🍎 Epal", "🥜 Kacang dalam kuantiti sederhana", "🥣 Yogurt"]
    }

    if pilihan in menu:
        st.markdown(f"### 🍽️ --- CADANGAN UNTUK {pilihan.upper()} ---")
        for item in menu[pilihan]:
            st.write(f"• {item}")
        st.info("💡 Tip: Pilih makanan yang seimbang dan pelbagaikan pilihan makanan.")

# -----------------------------------------------------------------------------
# 7. CADANGAN AKTIVITI HARIAN
# -----------------------------------------------------------------------------
elif pilihan_menu == "7. Cadangan Aktiviti Harian":
    st.header("🏃 7. Cadangan Aktiviti Harian")
    
    pilihan = st.radio(
        "Pilih aktiviti yang kamu nak buat:",
        ["🚶 Jalan Kaki", "🏃 Jogging", "🚴 Berbasikal", "🧘 Stretching"]
    )

    aktiviti = {
        "🚶 Jalan Kaki": ("20-30 minit", "Membantu badan kekal aktif dan sesuai untuk aktiviti santai."),
        "🏃 Jogging": ("15-30 minit", "Aktiviti kardio yang membantu meningkatkan kecergasan."),
        "🚴 Berbasikal": ("20-30 minit", "Aktiviti yang baik untuk melatih stamina dan kekuatan kaki."),
        "🧘 Stretching": ("5-10 minit", "Membantu meregangkan badan dan mengurangkan rasa tegang.")
    }

    tempoh, manfaat = aktiviti[pilihan]
    st.markdown(f"### 🔥 --- {pilihan} ---")
    st.write(f"⏱️ **Cadangan tempoh:** {tempoh}")
    st.write(f"💡 **Manfaat:** {manfaat}")
    st.caption("✨ Tip: Mulakan secara perlahan dan berhenti jika rasa tidak selesa.")

# -----------------------------------------------------------------------------
# 8. MOOD CHECK HARIAN
# -----------------------------------------------------------------------------
elif pilihan_menu == "8. Mood Check Harian":
    st.header("😊 8. Mood Check Harian")
    
    pilihan = st.select_slider(
        "Bagaimana mood kamu hari ini?",
        options=["😭 Sangat tidak baik", "😕 Kurang baik", "😐 Biasa", "🙂 Baik", "😁 Sangat baik"],
        value="😐 Biasa"
    )

    respons = {
        "😭 Sangat tidak baik": ("😭 Mood sangat rendah", "Cuba berehat seketika, tarik nafas perlahan dan lakukan aktiviti yang membuat kamu rasa tenang."),
        "😕 Kurang baik": ("😕 Mood kurang baik", "Ambil sedikit masa untuk berehat dan buat sesuatu yang kamu suka."),
        "😐 Biasa": ("😐 Mood biasa", "Tak apa! Cuba kekalkan rutin yang baik dan teruskan aktiviti harian."),
        "🙂 Baik": ("🙂 Mood baik", "Mantap! Kekalkan mood positif dengan aktiviti sihat."),
        "😁 Sangat baik": ("😁 Mood sangat baik", "Yay! Teruskan vibe positif dan kongsikan tenaga baik dengan orang sekeliling!")
    }

    status, nasihat = respons[pilihan]
    st.subheader(f"📊 Status : {status}")
    st.info(f"💡 **Cadangan:** {nasihat}")

# -----------------------------------------------------------------------------
# 9. PILIHAN MAKANAN SIHAT (KATEGORI)
# -----------------------------------------------------------------------------
elif pilihan_menu == "9. Pilihan Makanan Sihat":
    st.header("🥗 9. Pilihan Makanan Sihat")
    
    pilihan = st.selectbox(
        "Pilih kategori makanan untuk lihat contoh:",
        ["🍗 Protein", "🥦 Sayur", "🍚 Karbohidrat", "🍎 Buah"]
    )

    makanan = {
        "🍗 Protein": ["Ayam", "Ikan", "Telur", "Tauhu / Tempe"],
        "🥦 Sayur": ["Brokoli", "Bayam", "Lobak", "Sawi"],
        "🍚 Karbohidrat": ["Nasi", "Oat", "Roti gandum", "Kentang"],
        "🍎 Buah": ["Epal", "Pisang", "Oren", "Tembikai"]
    }

    st.markdown(f"### 🥗 --- SUMBER {pilihan.upper()} ---")
    for item in makanan[pilihan]:
        st.write(f"• {item}")
    st.info("💡 Tip: Cuba gabungkan beberapa kategori untuk hidangan yang lebih seimbang.")

# -----------------------------------------------------------------------------
# 10. CABARAN GAYA HIDUP SIHAT (PEMASA LIVE + VIDEO INTERAKTIF)
# -----------------------------------------------------------------------------
elif pilihan_menu == "10. Cabaran Gaya Hidup Sihat":
    st.header("🎯 10. Cabaran Gaya Hidup Sihat")
    
    pilihan = st.radio(
        "Pilih satu cabaran untuk hari ini:",
        ["💧 Minum Air Secukupnya", "👟 Jalan 5,000 Langkah", "😴 Tidur 7-9 Jam", "🏋️ Workout 10 Minit"]
    )

    if pilihan == "💧 Minum Air Secukupnya":
        st.markdown("### 💧 CABARAN AIR")
        st.write("📌 **Sasaran:** Cuba pastikan kamu minum air dengan kerap sepanjang hari.")
        st.write("💡 **Tip:** Bawa botol air bersama kamu.")
        st.video("https://www.youtube.com/watch?v=9iMGFqMmUFs")

    elif pilihan == "👟 Jalan 5,000 Langkah":
        st.markdown("### 👟 CABARAN LANGKAH")
        st.write("📌 **Sasaran:** Cuba capai 5,000 langkah hari ini.")
        st.write("💡 **Tip:** Gunakan peluang untuk berjalan kaki lebih banyak.")
        st.video("https://www.youtube.com/watch?v=enYITYwvHEQ")

    elif pilihan == "😴 Tidur 7-9 Jam":
        st.markdown("### 😴 CABARAN TIDUR")
        st.write("📌 **Sasaran:** Sasarkan tidur yang mencukupi malam ini.")
        st.write("💡 **Tip:** Kurangkan penggunaan telefon sebelum tidur.")
        st.video("https://www.youtube.com/watch?v=gedoSfZvBgE")

    elif pilihan == "🏋️ Workout 10 Minit":
        st.markdown("### 🏋️ CABARAN WORKOUT 10 MINIT INTERAKTIF")
        st.write("📌 **Sasaran:** Luangkan 10 minit untuk bergerak aktif mengikut senaman di bawah.")
        st.write("💡 **Tip:** Ulang rutin ini sebanyak 2 Pusingan (Rounds) untuk genap 10 minit!")
        
        # Senarai rutin senaman dengan URL video demonstrasi khusus
        rutin_workout = [
            ("⭐ Jumping Jacks (Lompat Bintang)", 45, "https://www.youtube.com/watch?v=c4DAnQ6DtF8"),
            ("🧘 Rehat (Rest & Tarik Nafas)", 15, "https://www.youtube.com/watch?v=inpok4MKVLM"),
            ("🦵 Bodyweight Squats (Cangkung)", 45, "https://www.youtube.com/watch?v=aclHkVaku9U"),
            ("🧘 Rehat (Rest & Tarik Nafas)", 15, "https://www.youtube.com/watch?v=inpok4MKVLM"),
            ("💪 Push-ups / Knee Push-ups", 45, "https://www.youtube.com/watch?v=IODxDxX7oi4"),
            ("🧘 Rehat (Rest & Tarik Nafas)", 15, "https://www.youtube.com/watch?v=inpok4MKVLM"),
            ("🏃 High Knees (Angkat Lutut)", 45, "https://www.youtube.com/watch?v=Z1EB9S_L9u4"),
            ("🧘 Rehat (Rest & Tarik Nafas)", 15, "https://www.youtube.com/watch?v=inpok4MKVLM"),
            ("🧱 Plank (Tahan Badan)", 45, "https://www.youtube.com/watch?v=pSHjTRCQxIw"),
            ("🧘 Rehat (Rest & Tarik Nafas)", 15, "https://www.youtube.com/watch?v=inpok4MKVLM")
        ]

        # Paparkan jadual rutin
        df_rutin = pd.DataFrame([{"⏱️ Masa": f"{durasi} Saat", "🏃 Jenis Senaman": nama} for nama, durasi, _ in rutin_workout])
        st.table(df_rutin)

        st.markdown("---")
        
        # Butang untuk memulakan pemasa + tayangan video automatik
        if st.button("▶️ Mula Workout 10 Minit Sekarang!"):
            st.info("Ready! Senaman akan bermula dalam 3 saat...")
            time.sleep(3)
            
            # Cipta ruang kolum secara dinamik untuk pemasa & video
            col_kiri, col_kanan = st.columns([1, 1])
            
            status_box = col_kiri.empty()
            timer_box = col_kiri.empty()
            progress_bar = col_kiri.progress(0)
            video_box = col_kanan.empty()

            total_langkah = len(rutin_workout)

            # Iterasi setiap senaman
            for idx, (nama_senaman, durasi_saat, video_url) in enumerate(rutin_workout):
                # Kemas kini maklumat senaman dan paparkan video berkaitan
                status_box.markdown(f"### 🔔 Senaman Sekarang:\n# **{nama_senaman}**")
                video_box.video(video_url)

                # Jalankan countdown timer
                for saat in range(durasi_saat, -1, -1):
                    timer_box.metric(label="⏱️ Masa Berbaki", value=f"{saat} Saat")
                    time.sleep(1)

                progress_bar.progress((idx + 1) / total_langkah)

            status_box.empty()
            timer_box.empty()
            video_box.empty()
            
            st.balloons()
            st.success("🎉 Tahniah kamu! Berjaya melengkapkan 1 pusingan senaman 5 minit! Ulang sekali lagi untuk cukupkan 10 minit! 🔥🥳")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Stay fit, stay positive & happy healthy lifestyle! 💪😊")
