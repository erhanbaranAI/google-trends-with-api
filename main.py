from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

def get_google_trends(keyword):
    pytrends = TrendReq(hl='tr-TR', tz=180)
    
    # Google Trends verisini al
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='TR', gprop='')
    
    # İlgili aramaları çek
    related_queries = pytrends.related_queries()
    
    # Eğer keyword için sonuç döndürmüyorsa None döndür
    if related_queries is None or keyword not in related_queries:
        print(f"Google Trends'te '{keyword}' için yeterli veri bulunamadı.")
        return None
    
    # Eğer top verisi yoksa None döndür
    top_queries = related_queries[keyword]['top']
    if top_queries is None:
        print(f"'{keyword}' için popüler arama verisi yok.")
        return None

    return top_queries

def plot_trends(keyword):
    data = get_google_trends(keyword)
    if data is None:
        return  # Veri yoksa fonksiyondan çık
    
    # İlk 10 arama kelimesini al
    top_searches = data.head(10)
    
    # Çubuk grafiği oluştur
    plt.figure(figsize=(10, 5))
    plt.bar(top_searches['query'], top_searches['value'], color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Arama Terimi')
    plt.ylabel('İlgi Seviyesi')
    plt.title(f"Google Trends - {keyword} için En Popüler Aramalar")
    plt.show()

if __name__ == "__main__":
    keyword = input("Hangi konuyu araştırmak istiyorsunuz? ")
    plot_trends(keyword)
