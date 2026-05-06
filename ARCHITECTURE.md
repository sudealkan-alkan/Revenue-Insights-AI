#  Revenue Insights AI - Teknik Mimari

Bu proje, küçük işletmelerin günlük finansal verilerini analiz etmek ve onlara stratejik iş tavsiyeleri sunmak amacıyla geliştirilmiş **Multi-Agent (Çoklu Ajan)** tabanlı bir yapay zeka sistemidir.

##  Teknoloji Yığını (Tech Stack)
- *AI Editör:* Geliştirme süreci, kod kalitesini ve hızını maksimize etmek için **Cursor AI** kullanılarak gerçekleştirilmiştir.
- *Framework:* Çoklu ajan mimarisi için **CrewAI** tercih edilmiştir.
- *Frontend:* Kullanıcı arayüzü ve anlık veri görselleştirme (grafikler) için **Streamlit** kullanılmıştır.
- *Dil:* Tüm sistem **Python** tabanlıdır.

##  AI Ajan Rolleri
Sistem, birbirini denetleyen ve tamamlayan iki uzman ajan üzerine kuruludur:

1. *Data Analyst Agent:* Kullanıcının girdiği ham gelir ve gider verilerini doğrular, net kâr hesaplamalarını yapar ve veriyi görselleştirme motoruna hazırlar.
2. *Business Advisor Agent:* Analiz edilen verileri yorumlayarak; maliyet tasarrufu, büyüme fırsatları ve operasyonel verimlilik konularında işletmeye özel stratejik tavsiyeler üretir.

## İş Akışı (Workflow)
1. *Veri Girişi:* Kullanıcı Streamlit dashboard üzerinden günlük finansal verilerini girer.
2. *Analiz:* Data Analyst ajanı matematiksel hesaplamaları tamamlar.
3. *Strateji:* Business Advisor ajanı, finansal duruma göre aksiyon planı hazırlar.
4. *Sunum:* Sonuçlar anlık grafikler ve AI yorumları olarak kullanıcıya sunulur.

---
*Bu proje, teknik şartnamede belirtilen inovasyon, teknik derinlik ve uygulanabilirlik kriterleri gözetilerek tasarlanmıştır.*
