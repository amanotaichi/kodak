from datetime import date
from database import session
from projects.kodak.nakakita.tables import stations

# 登録するデータの編集
Stations = stations(

    #holi_date = date(2024, 1, 1),
    #holi_text = "元日",
    #holi_date = date(2024, 1, 8),
    #holi_text = "成人の日"
    #holi_date = date(2024, 2, 11),
    #holi_text = "建国記念の日"
    #holi_date = date(2024, 2, 12),
    #holi_text = "振替休日"
    #holi_date = date(2024, 2, 23),
    #holi_text = "天皇誕生日"
    #holi_date = date(2024, 3, 20),
    #holi_text = "春分の日"
    #holi_date = date(2024, 4, 29),
    #holi_text = "昭和の日"
    #holi_date = date(2024, 5, 3),
    #holi_text = "憲法記念日"
    #holi_date = date(2024, 5, 4),
    #holi_text = "みどりの日"
    #holi_date = date(2024, 5, 5),
    #holi_text = "こどもの日"
    #holi_date = date(2024, 5, 6),
    #holi_text = "振替休日"
    #holi_date = date(2024, 7, 15),
    #holi_text = "海の日"
    #holi_date = date(2024, 8, 11),
    #holi_text = "山の日"
    #holi_date = date(2024, 8, 12),
    #holi_text = "振替休日"
    #holi_date = date(2024, 9, 16),
    #holi_text = "敬老の日"
    #holi_date = date(2024, 9, 22),
    #holi_text = "秋分の日"
    #holi_date = date(2024, 9, 23),
    #holi_text = "振替休日"
    #holi_date = date(2024, 10, 14),
    #holi_text = "スポーツの日"
    #holi_date = date(2024, 11, 3),
    #holi_text = "文化の日"
    #holi_date = date(2024, 11, 4),
    #holi_text = "振替休日"
    holi_date = date(2024, 11, 23),
    holi_text = "勤労感謝の日"
)
#INSERT処理
session.add(stations)
#コミット
session.commit()
