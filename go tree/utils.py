# TODO : Kerjakan disini (Fitur 1)
import re
from datetime import datetime, timedelta

def validasi_tanggal(tanggal_input):
    pola = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pola, tanggal_input):
        print("❌ Format tanggal harus YYYY-MM-DD.")
        return None

    try:
        tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
        if tanggal > datetime.today().date():
            return None
        return tanggal
    except:
        return None
