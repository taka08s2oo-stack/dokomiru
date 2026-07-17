-- アニメ作品テーブル
CREATE TABLE IF NOT EXISTS anime (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT UNIQUE NOT NULL,        -- URLに使う識別子 (例: kimetsu-no-yaiba)
    title TEXT NOT NULL,              -- 表示タイトル (例: 鬼滅の刃)
    title_kana TEXT,                  -- 検索用ふりがな
    synopsis TEXT,                    -- あらすじ
    episode_count INTEGER,            -- 話数
    release_year INTEGER,             -- 放送年
    genre TEXT,                       -- ジャンル (カンマ区切り)
    cover_image_url TEXT,             -- サムネイル画像URL
    is_airing INTEGER DEFAULT 0,      -- 放送中かどうか (1=放送中)
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

-- 配信サービステーブル
CREATE TABLE IF NOT EXISTS service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,        -- サービス名 (例: Abema)
    logo_url TEXT,                    -- ロゴ画像URL
    official_url TEXT,                -- サービスの公式トップページURL
    affiliate_base_url TEXT           -- アフィリエイトリンクのベース (将来用、空でもOK)
);

-- 中間テーブル: どのアニメがどのサービスで見れるか
CREATE TABLE IF NOT EXISTS availability (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    anime_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    plan_type TEXT NOT NULL,          -- 'free'(見放題) / 'paid'(都度課金) / 'subscription'(サブスク内)
    watch_url TEXT,                   -- そのアニメの視聴ページへの直接リンク
    verified_at TEXT DEFAULT (datetime('now')),  -- 最終確認日 (情報の鮮度管理用)
    FOREIGN KEY (anime_id) REFERENCES anime(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service(id) ON DELETE CASCADE,
    UNIQUE(anime_id, service_id)
);

CREATE INDEX IF NOT EXISTS idx_anime_slug ON anime(slug);
CREATE INDEX IF NOT EXISTS idx_availability_anime ON availability(anime_id);
