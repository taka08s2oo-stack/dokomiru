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
        "title_en": 'Demon Slayer: Kimetsu no Yaiba',
        "synopsis_en": 'After his family is slaughtered by a demon, Tanjiro sets out to become a demon slayer and find a cure for his younger sister Nezuko, who has been turned into a demon herself.',
        "genre_en": 'Action, Fantasy',
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
        "title_en": 'Jujutsu Kaisen',
        "synopsis_en": 'High schooler Yuji Itadori swallows a cursed talisman to save his friends and becomes host to a powerful curse, joining a secret organization that fights deadly curses.',
        "genre_en": 'Action, Dark Fantasy',
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
        "title_en": 'SPY x FAMILY',
        "synopsis_en": 'A top spy must build a fake family for a mission, unknowingly adopting a telepathic girl and marrying an assassin, as all three hide their secrets from one another.',
        "genre_en": 'Comedy, Action',
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
        "title_en": "Frieren: Beyond Journey's End",
        "synopsis_en": "After the hero's party defeats the Demon King, the elf mage Frieren outlives her human companions and slowly comes to understand what their time together truly meant.",
        "genre_en": 'Fantasy, Drama',
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
        "title_en": 'One Piece',
        "synopsis_en": 'Monkey D. Luffy sets sail with his crew in search of the legendary treasure One Piece, aiming to become the next Pirate King.',
        "genre_en": 'Adventure, Action',
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
        "title_en": 'Attack on Titan',
        "synopsis_en": 'Humanity survives behind massive walls to escape man-eating Titans, until a boy who lost his mother to one vows to wipe them all out.',
        "genre_en": 'Action, Dark Fantasy',
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
        "title_en": 'My Hero Academia',
        "synopsis_en": 'In a world where most people have superpowers called Quirks, a powerless boy is chosen by the greatest hero to inherit his power and enrolls in a school for heroes.',
        "genre_en": 'Action, School',
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
        "title_en": 'Detective Conan (Case Closed)',
        "synopsis_en": "A high school detective is shrunk into a child's body by a mysterious poison and continues solving cases undercover while searching for the organization responsible.",
        "genre_en": 'Mystery, Detective',
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
        "title_en": 'Haikyu!!',
        "synopsis_en": 'A short but determined boy joins his high school volleyball team, aiming to overcome his height disadvantage and reach the national championship.',
        "genre_en": 'Sports, Youth',
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
        "title_en": 'The Quintessential Quintuplets',
        "synopsis_en": 'A tutor is hired to help five identical quintuplet sisters pass their exams, though only one of them wants his help at first — and one of them is his future wife.',
        "genre_en": 'Romantic Comedy, School',
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
        "title_en": 'Chainsaw Man',
        "synopsis_en": 'A poor young man merges with his pet devil to become part-chainsaw, part-human, and is recruited into a government agency that hunts devils.',
        "genre_en": 'Action, Dark Fantasy',
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
        "title_en": '[Oshi No Ko]',
        "synopsis_en": 'A doctor and his patient are reincarnated as the twin children of the pop idol they idolized, and grow up navigating the glamorous and ruthless entertainment industry.',
        "genre_en": 'Drama, Entertainment',
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
        "title_en": 'Delicious in Dungeon',
        "synopsis_en": "After a party loses a member to a dragon deep in a dungeon, the remaining adventurers decide to cook and eat the dungeon's monsters to survive their rescue mission.",
        "genre_en": 'Fantasy, Gourmet',
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
        "title_en": 'That Time I Got Reincarnated as a Slime',
        "synopsis_en": 'A man killed in modern-day Japan wakes up reincarnated as a slime in a fantasy world, gradually gaining unique powers and building a nation of monsters.',
        "genre_en": 'Fantasy, Isekai',
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
        "title_en": 'Tokyo Revengers',
        "synopsis_en": "An unremarkable young man travels back in time to his middle school days to save his ex-girlfriend from a tragic fate by confronting a delinquent gang's turf war.",
        "genre_en": 'Drama, Action',
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
        "title_en": 'Kaiju No. 8',
        "synopsis_en": 'A man who cleans up after kaiju battles suddenly gains the power to transform into a kaiju himself, and must hide his identity while joining the force meant to destroy monsters like him.',
        "genre_en": 'Action, Sci-Fi',
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
        "title_en": 'The Apothecary Diaries',
        "synopsis_en": 'A skilled young apothecary sold into servitude at the imperial palace uses her knowledge of medicine to solve mysteries and poisonings within the inner court.',
        "genre_en": 'Mystery, Historical Fantasy',
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
        "title_en": 'Dragon Ball',
        "synopsis_en": 'A young boy with a monkey tail and superhuman strength sets out on a journey to collect seven magical Dragon Balls, encountering martial artists and villains along the way.',
        "genre_en": 'Action, Adventure',
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
    {
        "slug": "hagane-no-renkinjutsushi",
        "title": "鋼の錬金術師 FULLMETAL ALCHEMIST",
        "title_kana": "はがねのれんきんじゅつし",
        "title_en": 'Fullmetal Alchemist',
        "synopsis_en": "Two brothers who lost their bodies in a forbidden alchemy ritual search for the legendary Philosopher's Stone to restore what they lost.",
        "genre_en": 'Action, Sci-Fi',
        "synopsis": "禁忌の人体錬成に手を出し、体の一部を失った兄弟が、"
                    "失ったものを取り戻すため賢者の石を探す旅に出るダークファンタジー。",
        "episode_count": 64,
        "release_year": 2009,
        "genre": "アクション,ファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
        ],
    },
    {
        "slug": "code-geass",
        "title": "コードギアス 反逆のルルーシュ",
        "title_kana": "こーどぎあすはんぎゃくのるるーしゅ",
        "title_en": 'Code Geass: Lelouch of the Rebellion',
        "synopsis_en": 'An exiled prince gains a mysterious power of absolute command and uses it to lead a rebellion against the empire that took everything from him.',
        "genre_en": 'Sci-Fi, Mecha',
        "synopsis": "巨大帝国ブリタニアに占領された日本を舞台に、"
                    "特殊な力「ギアス」を手に入れた少年が仮面の指導者として反逆を起こしていくSFロボットアニメ。",
        "episode_count": 25,
        "release_year": 2006,
        "genre": "SF,ロボット",
        "is_airing": 0,
        "availability": [
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "sword-art-online",
        "title": "ソードアート・オンライン",
        "title_kana": "そーどあーとおんらいん",
        "title_en": 'Sword Art Online',
        "synopsis_en": 'Thousands of players are trapped inside a virtual reality MMORPG where dying in the game means dying in real life, forcing them to fight their way to the final boss to escape.',
        "genre_en": 'Sci-Fi, Fantasy',
        "synopsis": "次世代VRMMORPGに閉じ込められたプレイヤーたちが、"
                    "ゲーム内の死が現実の死に直結する状況の中、生還を目指して戦うSFアドベンチャー。",
        "episode_count": 25,
        "release_year": 2012,
        "genre": "SF,ファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "vinland-saga",
        "title": "ヴィンランド・サガ",
        "title_kana": "う゛ぃんらんどさが",
        "title_en": 'Vinland Saga',
        "synopsis_en": 'After his father is killed by mercenaries, a young boy joins the very band responsible for the murder, waiting for his chance at revenge amid the chaos of war.',
        "genre_en": 'Action, Historical Drama',
        "synopsis": "父を殺された少年トルフィンは、仇である傭兵団に加わり復讐の機会をうかがう。"
                    "戦いに明け暮れる日々の中で、彼が本当に求めるべきものは何かが問われていく歴史群像劇。",
        "episode_count": 48,
        "release_year": 2019,
        "genre": "アクション,歴史,ドラマ",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "re-zero",
        "title": "Re:ゼロから始める異世界生活",
        "title_kana": "りぜろからはじめるいせかいせいかつ",
        "title_en": 'Re:ZERO -Starting Life in Another World-',
        "synopsis_en": 'Summoned to another world, high schooler Subaru discovers he can rewind time by dying, and uses this power to protect the people he comes to care about through repeated tragedy.',
        "genre_en": 'Fantasy, Isekai',
        "synopsis": "異世界に召喚された高校生ナツキ・スバルは、死ぬと時間が巻き戻る「死に戻り」の力を頼りに、"
                    "大切な仲間たちを守るため過酷な運命に立ち向かっていく異世界ファンタジー。",
        "episode_count": 19,
        "release_year": 2016,
        "genre": "ファンタジー,異世界",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "free", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "mushoku-tensei",
        "title": "無職転生 ～異世界行ったら本気だす～",
        "title_kana": "むしょくてんせいいせかいいったらほんきだす",
        "title_en": 'Mushoku Tensei: Jobless Reincarnation',
        "synopsis_en": 'A 34-year-old shut-in dies and is reborn as a baby in a fantasy world, determined to live this second life without regrets by mastering magic and swordsmanship.',
        "genre_en": 'Fantasy, Isekai',
        "synopsis": "34歳無職のまま人生を終えた男が、赤ん坊として異世界に転生。"
                    "今度こそ後悔しない人生を送ろうと、魔法の修行に励みながら新たな世界で本気の人生をやり直す。",
        "episode_count": 11,
        "release_year": 2021,
        "genre": "ファンタジー,異世界",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "free", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "blue-lock",
        "title": "ブルーロック",
        "title_kana": "ぶるーろっく",
        "title_en": 'Blue Lock',
        "synopsis_en": "300 of Japan's most talented young strikers are gathered into an unconventional training program designed to produce a single egotistical striker capable of leading the national team to a World Cup win.",
        "genre_en": 'Sports, Soccer',
        "synopsis": "日本サッカーをW杯優勝に導く「エゴイスト」ストライカーを育成するため、"
                    "300人の高校生FWたちが生き残りをかけて競い合う異色のサッカー育成プロジェクトを描く。",
        "episode_count": 38,
        "release_year": 2022,
        "genre": "スポーツ,サッカー",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "bocchi-the-rock",
        "title": "ぼっち・ざ・ろっく！",
        "title_kana": "ぼっちざろっく",
        "title_en": 'Bocchi the Rock!',
        "synopsis_en": "A painfully shy girl who only knows how to express herself through guitar is unexpectedly recruited into a girls' rock band, forcing her to face her fear of people.",
        "genre_en": 'Music, Comedy',
        "synopsis": "ギターを愛する孤独な少女・後藤ひとりが、ひょんなことからガールズバンド「結束バンド」に加入し、"
                    "人前での演奏に不慣れながらも仲間との絆を通じて成長していく青春音楽コメディ。",
        "episode_count": 12,
        "release_year": 2022,
        "genre": "音楽,青春,コメディ",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "ousama-ranking",
        "title": "王様ランキング",
        "title_kana": "おうさまらんきんぐ",
        "title_en": 'Ranking of Kings',
        "synopsis_en": 'Bojji, a deaf prince unable to speak or wield a sword, is dismissed by everyone as unfit to rule — until a mysterious shadow boy befriends him and helps him find his own strength.',
        "genre_en": 'Fantasy, Adventure',
        "synopsis": "耳が聞こえず言葉も話せない王子ボッジは、周囲から王の器ではないと見下されていた。"
                    "影の一族の少年カゲとの出会いをきっかけに、自分の力で道を切り開いていく感動の王道ファンタジー。",
        "episode_count": 23,
        "release_year": 2021,
        "genre": "ファンタジー,冒険,ドラマ",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "jigokuraku",
        "title": "地獄楽",
        "title_kana": "じごくらく",
        "title_en": "Hell's Paradise",
        "synopsis_en": 'A condemned ninja is offered a pardon if he can retrieve the elixir of immortality from a mysterious island, where death row convicts compete against monstrous inhabitants to survive.',
        "genre_en": 'Action, Dark Fantasy',
        "synopsis": "死罪を宣告された最強の忍・画眉丸は、不老不死の仙薬を持ち帰れば無罪放免になると告げられる。"
                    "極楽浄土と噂される異形の島を舞台に、死罪人たちによる仙薬争奪戦が幕を開ける忍法浪漫活劇。",
        "episode_count": 26,
        "release_year": 2023,
        "genre": "アクション,ダークファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "sono-bisque-doll",
        "title": "その着せ替え人形は恋をする",
        "title_kana": "そのきせかえにんぎょうはこいをする",
        "title_en": 'My Dress-Up Darling',
        "synopsis_en": 'A high schooler who dreams of making traditional dolls ends up helping his popular, cosplay-obsessed classmate sew costumes, sparking an unlikely friendship between two very different worlds.',
        "genre_en": 'Romance, School',
        "synopsis": "雛人形の頭師を目指す高校生・五条新菜と、クラスの人気者でコスプレに憧れる喜多川海夢。"
                    "秘密を共有したことをきっかけに、決して交わるはずのなかった2人の世界が動き出す青春ラブコメ。",
        "episode_count": 24,
        "release_year": 2022,
        "genre": "恋愛,青春,コメディ",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "dandadan",
        "title": "ダンダダン",
        "title_kana": "だんだだん",
        "title_en": "Dandadan",
        "synopsis_en": "A girl who firmly believes in ghosts and a boy obsessed with aliens make a bet over which one is real, only to find themselves dragged into genuinely supernatural, life-threatening chaos.",
        "genre_en": "Occult, Comedy, Action",
        "synopsis": "オカルト好きの少年オカルンと、霊感体質の少女モモ。宇宙人と幽霊、どちらが本物かを賭けて肝試しに挑んだ二人は、"
                    "想像を超えた怪異に巻き込まれ、命がけの逃走劇を繰り広げることになる。",
        "episode_count": 12,
        "release_year": 2024,
        "genre": "オカルト,コメディ,アクション",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "nigewakamiya",
        "title": "逃げ上手の若君",
        "title_kana": "にげじょうずのわかぎみ",
        "title_en": "The Elusive Samurai",
        "synopsis_en": "When the Kamakura shogunate falls to betrayal, its rightful heir Tokiyuki loses everything in a single night. Armed with nothing but his talent for running away, he sets out to reclaim what was taken from him.",
        "genre_en": "Historical, Action, Battle",
        "synopsis": "鎌倉幕府滅亡の混乱の中、正統な後継者である北条時行は幕臣の裏切りによって全てを失う。"
                    "生き延びるため「逃げる」ことを武器に、仲間と共に天下を取り戻す戦いに挑む歴史活劇。",
        "episode_count": 12,
        "release_year": 2024,
        "genre": "歴史,アクション,バトル",
        "is_airing": 1,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "sakamoto-days",
        "title": "SAKAMOTO DAYS",
        "title_kana": "さかもとでいず",
        "title_en": "SAKAMOTO DAYS",
        "synopsis_en": "A legendary hitman named Taro Sakamoto retires to live a quiet life as a convenience store owner after falling in love — but the underworld refuses to leave him alone, and assassins keep showing up at his door.",
        "genre_en": "Action, Comedy",
        "synopsis": "かつて伝説の殺し屋と呼ばれた坂本太郎は、最愛の女性と結婚し引退。今はコンビニ店主として平穏に暮らしていたが、"
                    "裏社会は彼を放っておかず、次々と刺客が送り込まれる日常が始まる。",
        "episode_count": 11,
        "release_year": 2025,
        "genre": "アクション,コメディ",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "mashle",
        "title": "マッシュル -MASHLE-",
        "title_kana": "ましゅる",
        "title_en": "Mashle: Magic and Muscles",
        "synopsis_en": "Born without magic in a world where magic is everything, Mash relies on nothing but raw muscle to punch his way through a school of elite wizards.",
        "genre_en": "Battle, Comedy, School",
        "synopsis": "魔法が絶対の世界に生まれながら魔力を持たない少年マッシュは、圧倒的な筋肉だけを武器に、"
                    "魔法使いたちの学校で成り上がっていく規格外バトルコメディ。",
        "episode_count": 12,
        "release_year": 2023,
        "genre": "バトル,コメディ,学園",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "makeine",
        "title": "負けヒロインが多すぎる！",
        "title_kana": "まけひろいんがおおすぎる",
        "title_en": "Too Many Losing Heroines!",
        "synopsis_en": "After the girl he liked chooses someone else, an unremarkable high schooler somehow gets tangled up with a group of \"losing heroines\" — girls whose hearts were broken the same way — in this bittersweet high school comedy.",
        "genre_en": "Romance, Youth, Comedy",
        "synopsis": "想いを寄せていた相手が別の女の子と付き合うことになり、失恋した「負けヒロイン」たち。"
                    "そんな彼女たちに何故か目をつけられてしまったモブ気質な高校生の、賑やかで切ない青春コメディ。",
        "episode_count": 12,
        "release_year": 2024,
        "genre": "恋愛,青春,コメディ",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "ao-no-hako",
        "title": "アオのハコ",
        "title_kana": "あおのはこ",
        "title_en": "Blue Box",
        "synopsis_en": "A boy on the badminton team quietly admires the star basketball player who's also his upperclassman, and now suddenly his housemate. This is a tender, slow-burn portrait of first love set against the backdrop of club activities.",
        "genre_en": "Romance, Youth, Sports",
        "synopsis": "バドミントン部の少年は、憧れの先輩でバスケ部のエースと、ひょんなことから同居生活を始めることに。"
                    "部活と恋、それぞれに真剣に向き合う高校生たちの、等身大の青春を丁寧に描くラブストーリー。",
        "episode_count": 25,
        "release_year": 2024,
        "genre": "恋愛,青春,スポーツ",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "youzitsu",
        "title": "ようこそ実力至上主義の教室へ",
        "title_kana": "ようこそじつりょくしじょうしゅぎのきょうしつへ",
        "title_en": "Classroom of the Elite",
        "synopsis_en": "At a prestigious high school where students are ranked and rewarded purely on merit, the aloof Kiyotaka Ayanomiya is placed in the lowest-ranked class — and slowly reveals a sharp, calculating mind beneath his indifferent exterior.",
        "genre_en": "Psychological, School, Drama",
        "synopsis": "進学率・就職率100%を誇る名門校、東京都高度育成高等学校。実力至上主義を掲げるこの学校で、"
                    "最下位クラスに配属されたやる気のない少年・綾小路清隆が、その裏に隠された知略を静かに発揮していく心理戦学園ドラマ。",
        "episode_count": 12,
        "release_year": 2017,
        "genre": "心理戦,学園,ドラマ",
        "is_airing": 1,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
        ],
    },
    {
        "slug": "kage-no-jitsuryokusha",
        "title": "陰の実力者になりたくて！",
        "title_kana": "かげのじつりょくしゃになりたくて",
        "title_en": "The Eminence in Shadow",
        "synopsis_en": "A boy obsessed with the fantasy of being a mysterious \"man behind the shadows\" dies and is reincarnated into another world, where his make-believe secret organization turns out to be dangerously real.",
        "genre_en": "Fantasy, Action, Comedy",
        "synopsis": "「陰の実力者」に憧れていた少年は事故で命を落とし、異世界に転生。妄想で作り上げた「闇の組織」設定を"
                    "楽しんでいたはずが、いつの間にか本物の陰の実力者として、世界の裏側を動かしていくことになる異世界コメディ。",
        "episode_count": 20,
        "release_year": 2022,
        "genre": "ファンタジー,アクション,コメディ",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "kaguya-sama",
        "title": "かぐや様は告らせたい",
        "title_kana": "かぐやさまはこくらせたい",
        "title_en": "Kaguya-sama: Love Is War",
        "synopsis_en": "The president and vice president of an elite school's student council are both geniuses and both secretly in love with each other — but neither will admit it first, turning their courtship into an elaborate battle of wits.",
        "genre_en": "Romantic Comedy, School",
        "synopsis": "名門学園の生徒会長と副会長は、互いに好意を寄せながらも、先に告白した方が「負け」というプライドから、"
                    "相手に告白させようと日々頭脳戦を繰り広げる天才たちの恋愛コメディ。",
        "episode_count": 12,
        "release_year": 2019,
        "genre": "ラブコメ,学園",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "tokyo-ghoul",
        "title": "東京喰種トーキョーグール",
        "title_kana": "とうきょうぐーる",
        "title_en": "Tokyo Ghoul",
        "synopsis_en": "An ordinary college student barely survives an attack by a ghoul — a human-eating creature disguised as a person — and wakes up half-ghoul himself, forced to navigate a hidden world where humans and ghouls are locked in violent conflict.",
        "genre_en": "Dark Fantasy, Action",
        "synopsis": "人を喰らう「喰種」に襲われた平凡な大学生は、一命を取り留めるも自らも半喰種の体になってしまう。"
                    "人間と喰種、どちらの世界にも属せない少年が、その狭間で葛藤しながら生きていくダークファンタジー。",
        "episode_count": 12,
        "release_year": 2014,
        "genre": "ダークファンタジー,アクション",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "one-punch-man",
        "title": "ワンパンマン",
        "title_kana": "わんぱんまん",
        "title_en": "One Punch Man",
        "synopsis_en": "Saitama can defeat any enemy with a single punch, which has left him bored with the very concept of being a hero. His search for a worthy opponent turns this over-the-top parody of the superhero genre into a hilarious action spectacle.",
        "genre_en": "Action, Comedy",
        "synopsis": "どんな敵も一撃で倒せてしまうがゆえに、ヒーローという行為そのものに退屈しきってしまった男・サイタマ。"
                    "強すぎるがゆえの悩みを抱えながら、歯応えのある敵を求めて戦い続ける、痛快バトルコメディ。",
        "episode_count": 12,
        "release_year": 2015,
        "genre": "アクション,コメディ",
        "is_airing": 0,
        "availability": [
            {"service": "Abema", "plan_type": "subscription", "watch_url": "https://abema.tv/"},
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
            {"service": "Netflix", "plan_type": "subscription", "watch_url": "https://www.netflix.com/jp/"},
            {"service": "Disney+", "plan_type": "subscription", "watch_url": "https://www.disneyplus.com/ja-jp"},
        ],
    },
    {
        "slug": "yakusoku-no-neverland",
        "title": "約束のネバーランド",
        "title_kana": "やくそくのねばーらんど",
        "title_en": "The Promised Neverland",
        "synopsis_en": "The children of an idyllic orphanage discover the horrifying truth behind their sheltered lives and band together to escape before they meet the same fate as the friend they lost.",
        "genre_en": "Mystery, Dark Fantasy",
        "synopsis": "楽園のような孤児院で幸せに暮らしていた子どもたちは、その裏に隠された恐ろしい真実を知ってしまう。"
                    "仲間を失う前に、全員での脱獄を目指して知略を尽くす少年少女たちを描くミステリーサスペンス。",
        "episode_count": 12,
        "release_year": 2019,
        "genre": "ミステリー,ダークファンタジー",
        "is_airing": 0,
        "availability": [
            {"service": "dアニメストア", "plan_type": "subscription", "watch_url": "https://anime.dmkt-sp.jp/"},
            {"service": "DMM TV", "plan_type": "subscription", "watch_url": "https://tv.dmm.com/vod/"},
            {"service": "U-NEXT", "plan_type": "subscription", "watch_url": "https://video.unext.jp/"},
            {"service": "Hulu", "plan_type": "subscription", "watch_url": "https://www.hulu.jp/"},
        ],
    },
]



# シーズン・劇場版データ (作品slug -> [{"label", "subtitle", "kind", "release_year", "episode_count"}])
SEASONS = {
    "kimetsu-no-yaiba": [
        {"label": "シーズン1", "subtitle": "竈門炭治郎 立志編", "kind": "tv", "release_year": 2019, "episode_count": 26},
        {"label": "劇場版", "subtitle": "無限列車編", "kind": "movie", "release_year": 2020, "episode_count": None},
        {"label": "シーズン2", "subtitle": "遊郭編", "kind": "tv", "release_year": 2021, "episode_count": 11},
        {"label": "シーズン3", "subtitle": "刀鍛冶の里編", "kind": "tv", "release_year": 2023, "episode_count": 11},
        {"label": "シーズン4", "subtitle": "柱稽古編", "kind": "tv", "release_year": 2024, "episode_count": 8},
        {"label": "劇場版", "subtitle": "無限城編 第一章 猗窩座再来", "kind": "movie", "release_year": 2025, "episode_count": None},
    ],
    "jujutsu-kaisen": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2020, "episode_count": 24},
        {"label": "劇場版", "subtitle": "呪術廻戦 0", "kind": "movie", "release_year": 2021, "episode_count": None},
        {"label": "シーズン2", "subtitle": "渋谷事変", "kind": "tv", "release_year": 2023, "episode_count": 23},
        {"label": "シーズン3", "subtitle": "死滅回游", "kind": "tv", "release_year": 2026, "episode_count": None},
    ],
    "spy-family": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 25},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 12},
        {"label": "劇場版", "subtitle": "CODE: White", "kind": "movie", "release_year": 2023, "episode_count": None},
    ],
    "shingeki-no-kyojin": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2013, "episode_count": 25},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2017, "episode_count": 12},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2018, "episode_count": 22},
        {"label": "The Final Season", "subtitle": None, "kind": "tv", "release_year": 2020, "episode_count": 28},
    ],
    "boku-no-hero-academia": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2016, "episode_count": 13},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2017, "episode_count": 25},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2018, "episode_count": 25},
        {"label": "シーズン4", "subtitle": None, "kind": "tv", "release_year": 2019, "episode_count": 25},
        {"label": "シーズン5", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 25},
        {"label": "シーズン6", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 21},
        {"label": "シーズン7", "subtitle": "最終章", "kind": "tv", "release_year": 2023, "episode_count": 21},
    ],
    "meitantei-conan": [
        {"label": "TVシリーズ", "subtitle": "1996年〜放送中", "kind": "tv", "release_year": 1996, "episode_count": None},
        {"label": "劇場版シリーズ", "subtitle": "毎年春に新作公開", "kind": "movie", "release_year": None, "episode_count": None},
    ],
    "haikyuu": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2014, "episode_count": 25},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2015, "episode_count": 25},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2016, "episode_count": 10},
        {"label": "シーズン4", "subtitle": "烏野高校 VS 白鳥沢学園高校", "kind": "tv", "release_year": 2020, "episode_count": 25},
        {"label": "劇場版", "subtitle": "ゴミ捨て場の決戦", "kind": "movie", "release_year": 2024, "episode_count": None},
    ],
    "gotoubun-no-hanayome": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2019, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 12},
        {"label": "劇場版", "subtitle": None, "kind": "movie", "release_year": 2022, "episode_count": None},
    ],
    "chainsaw-man": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 12},
        {"label": "劇場版", "subtitle": "レゼ篇", "kind": "movie", "release_year": 2025, "episode_count": None},
    ],
    "oshi-no-ko": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 11},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 13},
    ],
    "tensei-slime": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2018, "episode_count": 24},
        {"label": "劇場版", "subtitle": "紅蓮の絆編", "kind": "movie", "release_year": 2022, "episode_count": None},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 24},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 16},
    ],
    "tokyo-revengers": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 24},
        {"label": "シーズン2", "subtitle": "血のハロウィン編", "kind": "tv", "release_year": 2023, "episode_count": 13},
        {"label": "シーズン3", "subtitle": "天竺編", "kind": "tv", "release_year": 2023, "episode_count": 25},
    ],
    "kusuriya-no-hitorigoto": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 24},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 24},
    ],
    "dragon-ball": [
        {"label": "ドラゴンボール", "subtitle": None, "kind": "tv", "release_year": 1986, "episode_count": 153},
        {"label": "ドラゴンボールZ", "subtitle": None, "kind": "tv", "release_year": 1989, "episode_count": 291},
        {"label": "ドラゴンボール超", "subtitle": None, "kind": "tv", "release_year": 2015, "episode_count": 131},
        {"label": "劇場版シリーズ", "subtitle": "複数作品あり", "kind": "movie", "release_year": None, "episode_count": None},
    ],
    "hagane-no-renkinjutsushi": [
        {"label": "TVシリーズ(2003年版)", "subtitle": None, "kind": "tv", "release_year": 2003, "episode_count": 51},
        {"label": "FULLMETAL ALCHEMIST", "subtitle": "BROTHERHOOD", "kind": "tv", "release_year": 2009, "episode_count": 64},
    ],
    "code-geass": [
        {"label": "シーズン1", "subtitle": "反逆のルルーシュ", "kind": "tv", "release_year": 2006, "episode_count": 25},
        {"label": "シーズン2", "subtitle": "反逆のルルーシュ R2", "kind": "tv", "release_year": 2008, "episode_count": 25},
        {"label": "劇場版三部作", "subtitle": "興道/叛道/皇道", "kind": "movie", "release_year": 2017, "episode_count": None},
    ],
    "sword-art-online": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2012, "episode_count": 25},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2014, "episode_count": 24},
        {"label": "劇場版", "subtitle": "オーディナル・スケール", "kind": "movie", "release_year": 2017, "episode_count": None},
        {"label": "アリシゼーション編", "subtitle": None, "kind": "tv", "release_year": 2018, "episode_count": 48},
    ],
    "vinland-saga": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2019, "episode_count": 24},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 24},
    ],
    "re-zero": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2016, "episode_count": 25},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2020, "episode_count": 25},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 16},
    ],
    "mushoku-tensei": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 23},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 24},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2025, "episode_count": None},
    ],
    "blue-lock": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 24},
        {"label": "シーズン2", "subtitle": "VS U-20 JAPAN", "kind": "tv", "release_year": 2024, "episode_count": 14},
    ],
    "ousama-ranking": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 23},
        {"label": "シーズン2", "subtitle": "勇気の宝箱", "kind": "tv", "release_year": 2024, "episode_count": None},
    ],
    "jigokuraku": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 13},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2026, "episode_count": 13},
    ],
    "sono-bisque-doll": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2025, "episode_count": 12},
    ],
    "one-piece": [
        {"label": "TVシリーズ", "subtitle": "1999年〜放送中", "kind": "tv", "release_year": 1999, "episode_count": None},
        {"label": "劇場版シリーズ", "subtitle": "複数作品あり", "kind": "movie", "release_year": None, "episode_count": None},
    ],
    "dandadan": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2025, "episode_count": 12},
        {"label": "シーズン3", "subtitle": "制作決定", "kind": "tv", "release_year": 2027, "episode_count": None},
    ],
    "nigewakamiya": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2026, "episode_count": None},
    ],
    "sakamoto-days": [
        {"label": "シーズン1 パート1", "subtitle": None, "kind": "tv", "release_year": 2025, "episode_count": 11},
        {"label": "シーズン1 パート2", "subtitle": None, "kind": "tv", "release_year": 2026, "episode_count": None},
    ],
    "mashle": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 12},
        {"label": "シーズン2", "subtitle": "神覚者候補選抜試験編", "kind": "tv", "release_year": 2024, "episode_count": 12},
        {"label": "シーズン3", "subtitle": "三魔対争神覚者最終試験編・制作決定", "kind": "tv", "release_year": 2027, "episode_count": None},
    ],
    "makeine": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 12},
        {"label": "シーズン2", "subtitle": "制作決定", "kind": "tv", "release_year": None, "episode_count": None},
    ],
    "ao-no-hako": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 25},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2026, "episode_count": None},
    ],
    "youzitsu": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2017, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 13},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2024, "episode_count": 13},
        {"label": "シーズン4", "subtitle": "2年生1学期", "kind": "tv", "release_year": 2026, "episode_count": None},
    ],
    "kage-no-jitsuryokusha": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 20},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2023, "episode_count": 12},
    ],
    "kaguya-sama": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2019, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2020, "episode_count": 12},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2022, "episode_count": 13},
        {"label": "劇場版", "subtitle": "ファーストキッスは終わらない", "kind": "movie", "release_year": 2022, "episode_count": None},
        {"label": "OVA", "subtitle": "大人への階段", "kind": "movie", "release_year": 2023, "episode_count": None},
    ],
    "tokyo-ghoul": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2014, "episode_count": 12},
        {"label": "シーズン2", "subtitle": "√A", "kind": "tv", "release_year": 2015, "episode_count": 12},
        {"label": "シーズン3", "subtitle": ":re", "kind": "tv", "release_year": 2018, "episode_count": 12},
        {"label": "シーズン4", "subtitle": ":re 最終章", "kind": "tv", "release_year": 2018, "episode_count": 12},
    ],
    "one-punch-man": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2015, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2019, "episode_count": 12},
        {"label": "シーズン3", "subtitle": None, "kind": "tv", "release_year": 2025, "episode_count": None},
    ],
    "yakusoku-no-neverland": [
        {"label": "シーズン1", "subtitle": None, "kind": "tv", "release_year": 2019, "episode_count": 12},
        {"label": "シーズン2", "subtitle": None, "kind": "tv", "release_year": 2021, "episode_count": 11},
    ],
}

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
               (slug, title, title_kana, synopsis, title_en, synopsis_en, genre_en,
                episode_count, release_year, genre, is_airing)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                a["slug"], a["title"], a["title_kana"], a["synopsis"],
                a.get("title_en"), a.get("synopsis_en"), a.get("genre_en"),
                a["episode_count"], a["release_year"], a["genre"], a["is_airing"],
            ),
        )
        # 既存行にも英語フィールドを常に同期させる(再デプロイ時の翻訳更新に対応)
        cur.execute(
            """UPDATE anime SET title_en = ?, synopsis_en = ?, genre_en = ?
               WHERE slug = ?""",
            (a.get("title_en"), a.get("synopsis_en"), a.get("genre_en"), a["slug"]),
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


    # シーズン・劇場版データの投入
    cur.execute("DELETE FROM season")  # 再デプロイのたびに最新のシーズン一覧に入れ替える
    for slug, season_list in SEASONS.items():
        cur.execute("SELECT id FROM anime WHERE slug = ?", (slug,))
        row = cur.fetchone()
        if row is None:
            continue
        anime_id = row["id"]
        for i, s in enumerate(season_list):
            cur.execute(
                """INSERT INTO season
                   (anime_id, label, subtitle, kind, release_year, episode_count, display_order)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (anime_id, s["label"], s.get("subtitle"), s["kind"],
                 s.get("release_year"), s.get("episode_count"), i),
            )

    conn.commit()
    conn.close()
    print("シードデータの投入が完了しました。")


if __name__ == "__main__":
    init_db()
    seed()