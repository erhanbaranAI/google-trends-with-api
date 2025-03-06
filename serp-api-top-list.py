import matplotlib.pyplot as plt
import datetime
import serpapi 

# SerpApi ile Google Trends verisini çek
params = {
    "engine": "google_trends",
    "q": "diyetisyen, kilo verme, sağlık",
    "data_type": "TIMESERIES",
    "api_key": "88758674df4852fbc2a231c8436fa1d397a93cdd299364331962948c96efcd2b"
}

search = serpapi.search(params)
results = search.as_dict()

# API'den dönen veriyi kontrol edelim
#print("API Sonucu:", results)

# Zaman serisini al
interest_over_time = results.get("interest_over_time", {}).get("timeline_data", [])

# Eğer veri yoksa uyarı ver
if not interest_over_time:
    print("Google Trends'ten veri alınamadı. API anahtarınızı kontrol edin veya farklı bir sorgu deneyin.")
else:
    # Tarihleri ve ilgi değerlerini parse et
    dates = []
    values = {"diyetisyen": [], "kilo verme": [], "sağlık": []}  # Anahtar kelimeler için boş liste oluştur

    for item in interest_over_time:
        # Tarihi al ve formatla
        date_str = item["date"].split("–")[0].strip()  # "Mar 3 – 9, 2024" gibi verileri sadece başlangıç tarihini alarak düzelt
        parsed_date = datetime.datetime.strptime(date_str, "%b %d, %Y") if "," in date_str else datetime.datetime.strptime(date_str + " 2024", "%b %d %Y")
        dates.append(parsed_date)

        # Her kelimenin ilgi değerini al
        for entry in item["values"]:
            query = entry["query"]
            values[query].append(entry["extracted_value"])

    # Grafiği çiz
    plt.figure(figsize=(12, 6))

    for query, data in values.items():
        plt.plot(dates, data, label=query, marker="o")  # Çizgi grafiği

    plt.xlabel("Tarih")
    plt.ylabel("İlgi Seviyesi")
    plt.title("Google Trends Zaman Serisi")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()









# # Zaman serisini al
# interest_over_time = results.get("interest_over_time", {})

# # Eğer veri yoksa uyarı ver
# if not interest_over_time:
#     print("Google Trends'ten veri alınamadı. API anahtarınızı kontrol edin veya farklı bir sorgu deneyin.")
# else:
#     # Tarih ve ilgi değerlerini parse et
#     dates = [datetime.datetime.strptime(item['date'], "%Y-%m-%d") for item in interest_over_time]
#     values = {query: [item['values'][i] for item in interest_over_time] for i, query in enumerate(params["q"].split(", "))}

#     # Grafiği çiz
#     plt.figure(figsize=(12, 6))
    
#     for query, data in values.items():
#         plt.plot(dates, data, label=query, marker="o")  # Çizgi grafiği
    
#     plt.xlabel("Tarih")
#     plt.ylabel("İlgi Seviyesi")
#     plt.title("Google Trends Zaman Serisi")
#     plt.legend()
#     plt.xticks(rotation=45)  # Tarihlerin okunaklı olması için döndür
#     plt.grid(True)
#     plt.show()
