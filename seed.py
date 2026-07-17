"""
初期データ投入スクリプト。

【重要】ここに入っているアニメの「配信状況」はテンプレート動作確認用の
サンプルデータです。実際の配信権は頻繁に変わるため、公開前に必ず
公式サイトで最新情報を確認し、正しい内容に差し替えてください。
"""
import sqlite3

DB_PATH = "anime_finder.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    with open("schema.sql", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


"""
初期データ投入スクリプト。

【重要】ここに入っている配信情報は2026年7月時点でWeb検索により確認した
ものですが、配信権は今後も変わる可能性があります。公開前や定期的に、
必ず公式サイトで最新情報を確認し、内容を更新してください。
"""
import sqlite3

DB_PATH = "anime_finder.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    with open("schema.sql", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


SERVICES = [
    {"name": "Abema", "logo_url": "", "official_url": "https://abema.tv/"},
    {"name": "Netflix", "logo_url": "", "official_url": "https://www.netflix.com/jp/"},
    {"name": "dアニメストア", "logo_url": "", "official_url": "https://anime.dmkt-sp.jp/"},
    {"name": "U-NEXT", "logo_url": "", "official_url": "https://video.unext.jp/"},
    {"name": "Disney+", "logo_url": "", "official_url": "https://www.disneyplus.com/ja-jp"},
    {"name": "Hulu", "logo_url": "", "official_url": "https://www.hulu.jp/"},
    {"name": "DMM TV", "logo_url": "", "official_url": "https://tv.dmm.com/vod/"},
]

# 2026年7月時点でWeb検索により確認したデータ。公開前に必ず最新情報を再確認すること。
ANIME = [
    {
        "slug": "kimetsu-no-yaiba",
        "title": "鬼滅の刃",
        "title_kana": "きめつのやいば",
        "synopsis": "家族を鬼に殺され、唯一生き残った妹も鬼にされてしまった少年が、"
                    "妹を人間に戻す方法を探しながら鬼殺隊士として鬼と戦っていく物語。",
        "episode_count": 26,
        "release_year": 2019,
        "genre": "アクション,ファンタジー",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
        ],
    },
    {
        "slug": "jujutsu-kaisen",
        "title": "呪術廻戦",
        "title_kana": "じゅじゅつかいせん",
        "synopsis": "特級呪物を飲み込んでしまった高校生が、呪術高専に入学し、"
                    "仲間たちと共に人々を脅かす呪いと戦っていくダークファンタジー。",
        "episode_count": 24,
        "release_year": 2020,
        "genre": "アクション,ダークファンタジー",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "free", "watch_url": "https://abema.tv/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
        ],
    },
    {
        "slug": "spy-family",
        "title": "SPY×FAMILY",
        "title_kana": "すぱいふぁみりー",
        "synopsis": "凄腕スパイと殺し屋、そして人の心を読める少女が、"
                    "それぞれの正体を隠したまま偽装家族として暮らすホームコメディ。",
        "episode_count": 25,
        "release_year": 2022,
        "genre": "コメディ,アクション",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "sousou-no-frieren",
        "title": "葬送のフリーレン",
        "title_kana": "そうそうのふりーれん",
        "synopsis": "魔王を倒した勇者パーティーの魔法使いフリーレンが、"
                    "亡き仲間たちとの記憶と向き合いながら長い旅を続けるファンタジー。",
        "episode_count": 28,
        "release_year": 2023,
        "genre": "ファンタジー,ドラマ",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "one-piece",
        "title": "ONE PIECE",
        "title_kana": "わんぴーす",
        "synopsis": "海賊王を目指す少年ルフィが、個性豊かな仲間たちと共に"
                    "大海原を冒険する、1999年放送開始の長寿アクション作品。",
        "episode_count": 1155,
        "release_year": 1999,
        "genre": "冒険,アクション",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "free", "watch_url": "https://abema.tv/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
        ],
    },
    {
        "slug": "shingeki-no-kyojin",
        "title": "進撃の巨人",
        "title_kana": "しんげきのきょじん",
        "synopsis": "巨大な人型の巨人に人類が追い詰められる世界で、"
                    "家族を奪われた少年が仲間と共に巨人の脅威に立ち向かうダークファンタジー。",
        "episode_count": 25,
        "release_year": 2013,
        "genre": "アクション,ダークファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
        ],
    },
    {
        "slug": "boku-no-hero-academia",
        "title": "僕のヒーローアカデミア",
        "title_kana": "ぼくのひーろーあかでみあ",
        "synopsis": "誰もが超常的な個性を持つ世界で、無個性に生まれた少年が"
                    "最高のヒーローを目指して成長していく学園アクション。",
        "episode_count": 13,
        "release_year": 2016,
        "genre": "アクション,学園",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
        ],
    },
    {
        "slug": "meitantei-conan",
        "title": "名探偵コナン",
        "title_kana": "めいたんていこなん",
        "synopsis": "謎の組織に薬を飲まされ小学生の姿にされてしまった高校生探偵が、"
                    "正体を隠しながら数々の難事件を解決していく国民的推理アニメ。",
        "episode_count": 1000,
        "release_year": 1996,
        "genre": "ミステリー,推理",
        "is_airing": 1,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "haikyuu",
        "title": "ハイキュー!!",
        "title_kana": "はいきゅー",
        "synopsis": "身長にコンプレックスを抱く少年がバレーボールと出会い、"
                    "仲間たちと共に全国大会を目指していく青春スポーツアニメ。",
        "episode_count": 25,
        "release_year": 2014,
        "genre": "スポーツ,青春",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "gotoubun-no-hanayome",
        "title": "五等分の花嫁",
        "title_kana": "ごとうぶんのはなよめ",
        "synopsis": "勉強が苦手な五つ子姉妹の家庭教師を任された高校生が、"
                    "彼女たちとの交流を通じて絆を深めていくラブコメディ。",
        "episode_count": 12,
        "release_year": 2019,
        "genre": "ラブコメ,学園",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
        ],
    },
    {
        "slug": "chainsaw-man",
        "title": "チェンソーマン",
        "title_kana": "ちぇんそーまん",
        "synopsis": "借金返済のため悪魔祓いをしていた少年が、相棒の悪魔と契約し"
                    "チェンソーの悪魔として蘇り、危険な任務に挑んでいくダークアクション。",
        "episode_count": 12,
        "release_year": 2022,
        "genre": "アクション,ダークファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
        ],
    },
    {
        "slug": "oshi-no-ko",
        "title": "【推しの子】",
        "title_kana": "おしのこ",
        "synopsis": "人気アイドルの子として転生した青年が、芸能界の華やかさと"
                    "その裏側の両方を目の当たりにしながら生きていく群像劇。",
        "episode_count": 11,
        "release_year": 2023,
        "genre": "ドラマ,芸能",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "free", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "dungeon-meshi",
        "title": "ダンジョン飯",
        "title_kana": "だんじょんめし",
        "synopsis": "ドラゴンに妹を食べられてしまったパーティーが、ダンジョンに生息する"
                    "魔物を食料にしながら妹の救出を目指すユニークなファンタジー。",
        "episode_count": 24,
        "release_year": 2024,
        "genre": "ファンタジー,グルメ",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "tensei-slime",
        "title": "転生したらスライムだった件",
        "title_kana": "てんせいしたらすらいむだったけん",
        "synopsis": "通り魔に刺され命を落としたサラリーマンが、異世界でスライムに転生し、"
                    "新たな仲間たちと国づくりに奮闘するファンタジー。",
        "episode_count": 24,
        "release_year": 2018,
        "genre": "ファンタジー,異世界",
        "is_airing": 1,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "tokyo-revengers",
        "title": "東京リベンジャーズ",
        "title_kana": "とうきょうりべんじゃーず",
        "synopsis": "冴えない青年が中学時代にタイムリープし、恋人を悲劇の運命から救うため"
                    "不良グループの抗争に立ち向かっていくヒューマンドラマ。",
        "episode_count": 24,
        "release_year": 2021,
        "genre": "ドラマ,アクション",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
        ],
    },
    {
        "slug": "kaiju-no-8",
        "title": "怪獣8号",
        "title_kana": "かいじゅうはちごう",
        "synopsis": "怪獣清掃業の青年が偶然怪獣の力を得てしまい、正体を隠しながら"
                    "怪獣を倒す防衛隊員として戦うことになる特撮風アクション。",
        "episode_count": 12,
        "release_year": 2024,
        "genre": "アクション,SF",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
        ],
    },
    {
        "slug": "kusuriya-no-hitorigoto",
        "title": "薬屋のひとりごと",
        "title_kana": "くすりやのひとりごと",
        "synopsis": "後宮に下働きとして売られた薬師の少女が、持ち前の知識で"
                    "宮廷内の謎や事件を解き明かしていく中華風ミステリー。",
        "episode_count": 24,
        "release_year": 2023,
        "genre": "ミステリー,中華ファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "dragon-ball",
        "title": "ドラゴンボール",
        "title_kana": "どらごんぼーる",
        "synopsis": "願いを叶える伝説の球を巡り、超人的な戦闘力を持つ少年が"
                    "仲間や強敵と出会いながら成長していく格闘冒険アニメ。",
        "episode_count": 153,
        "release_year": 1986,
        "genre": "アクション,冒険",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
        ],
    },
]


def seed():
    conn = get_connection()
    cur = conn.cursor()

    for s in SERVICES:
        cur.execute(
            "INSERT OR IGNORE INTO service (name, logo_url, official_url) VALUES (?, ?, ?)",
            (s["name"], s["logo_url"], s["official_url"]),
        )

    for a in ANIME:
        cur.execute(
            """INSERT OR IGNORE INTO anime
               (slug, title, title_kana, synopsis, episode_count, release_year, genre, is_airing)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                a["slug"], a["title"], a["title_kana"], a["synopsis"],
                a["episode_count"], a["release_year"], a["genre"], a["is_airing"],
            ),
        )
        cur.execute("SELECT id FROM anime WHERE slug = ?", (a["slug"],))
        anime_id = cur.fetchone()["id"]

        for av in a["availability"]:
            cur.execute("SELECT id FROM service WHERE name = ?", (av["service"],))
            service_row = cur.fetchone()
            if not service_row:
                continue
            cur.execute(
                """INSERT OR IGNORE INTO availability
                   (anime_id, service_id, plan_type, watch_url)
                   VALUES (?, ?, ?, ?)""",
                (anime_id, service_row["id"], av["plan_type"], av["watch_url"]),
            )

    conn.commit()
    conn.close()
    print("シードデータの投入が完了しました。")


if __name__ == "__main__":
    init_db()
    seed()
