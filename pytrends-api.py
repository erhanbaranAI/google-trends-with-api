from pytrends.request import TrendReq

# PyTrends bağlantısı oluşturuluyor (Türkçe dil ve Türkiye saat dilimi için)
pytrends = TrendReq(hl='tr-TR', tz=180)  # tz=180 dakika => UTC+3 (Türkiye saati)

# Google Trends'te Türkiye için günlük trend aramaları çekiliyor
trending_df = pytrends.trending_searches(pn='turkey')  # ülke adı küçük harfle verilir&#8203;:contentReference[oaicite:0]{index=0}

# Sonuç verisini ekrana yazdır (Türkiye'de trend olan aramalar)
print("Türkiye Google Arama Trendleri (Güncel):")
print(trending_df)
