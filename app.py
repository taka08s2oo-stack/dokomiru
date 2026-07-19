import sqlite3
from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)
DB_PATH = "anime_finder.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_all_genres(conn):
    """genreカラムはカンマ区切りで複数ジャンルが入っているので、
    重複を除いたジャンル一覧を作って絞り込みのプルダウンに使う。"""
    rows = conn.execute("SELECT DISTINCT genre FROM anime").fetchall()
    genre_set = set()
    for row in rows:
        for g in row["genre"].split(","):
            g = g.strip()
            if g:
                genre_set.add(g)
    return sorted(genre_set)


def get_all_services(conn):
    rows = conn.execute("SELECT name FROM service ORDER BY name").fetchall()
    return [row["name"] for row in rows]


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    genre = request.args.get("genre", "").strip()
    service = request.args.get("service", "").strip()
    conn = get_connection()

    sql = "SELECT DISTINCT anime.* FROM anime"
    conditions = []
    params = []

    if service:
        sql += """
            JOIN availability ON availability.anime_id = anime.id
            JOIN service ON service.id = availability.service_id
        """
        conditions.append("service.name = ?")
        params.append(service)

    if query:
        conditions.append("(anime.title LIKE ? OR anime.title_kana LIKE ?)")
        params.append(f"%{query}%")
        params.append(f"%{query}%")

    if genre:
        conditions.append("(',' || anime.genre || ',') LIKE ?")
        params.append(f"%,{genre},%")

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " ORDER BY anime.release_year DESC"

    rows = conn.execute(sql, params).fetchall()

    all_genres = get_all_genres(conn)
    all_services = get_all_services(conn)

    conn.close()
    return render_template(
        "index.html",
        anime_list=rows,
        query=query,
        selected_genre=genre,
        selected_service=service,
        all_genres=all_genres,
        all_services=all_services,
        en_path="/en/",
    )


@app.route("/anime/<slug>")
def anime_detail(slug):
    conn = get_connection()
    anime = conn.execute(
        "SELECT * FROM anime WHERE slug = ?", (slug,)
    ).fetchone()

    if anime is None:
        conn.close()
        abort(404)

    availability = conn.execute(
        """SELECT service.name AS service_name, service.official_url,
                  availability.plan_type, availability.watch_url,
                  availability.verified_at
           FROM availability
           JOIN service ON service.id = availability.service_id
           WHERE availability.anime_id = ?""",
        (anime["id"],),
    ).fetchall()

    seasons = conn.execute(
        """SELECT label, subtitle, kind, release_year, episode_count
           FROM season WHERE anime_id = ? ORDER BY display_order""",
        (anime["id"],),
    ).fetchall()

    conn.close()
    return render_template(
        "anime_detail.html", anime=anime, availability=availability, seasons=seasons,
        en_path=f"/en/anime/{slug}",
    )


def get_all_genres_en(conn):
    rows = conn.execute("SELECT DISTINCT genre_en FROM anime WHERE genre_en IS NOT NULL").fetchall()
    genre_set = set()
    for row in rows:
        for g in row["genre_en"].split(","):
            g = g.strip()
            if g:
                genre_set.add(g)
    return sorted(genre_set)


@app.route("/en/")
def index_en():
    query = request.args.get("q", "").strip()
    genre = request.args.get("genre", "").strip()
    service = request.args.get("service", "").strip()
    conn = get_connection()

    sql = "SELECT DISTINCT anime.* FROM anime"
    conditions = ["anime.title_en IS NOT NULL"]
    params = []

    if service:
        sql += """
            JOIN availability ON availability.anime_id = anime.id
            JOIN service ON service.id = availability.service_id
        """
        conditions.append("service.name = ?")
        params.append(service)

    if query:
        conditions.append("(anime.title_en LIKE ? OR anime.title LIKE ?)")
        params.append(f"%{query}%")
        params.append(f"%{query}%")

    if genre:
        conditions.append("(',' || anime.genre_en || ',') LIKE ?")
        params.append(f"%,{genre},%")

    sql += " WHERE " + " AND ".join(conditions)
    sql += " ORDER BY anime.release_year DESC"

    rows = conn.execute(sql, params).fetchall()

    all_genres = get_all_genres_en(conn)
    all_services = get_all_services(conn)

    conn.close()
    return render_template(
        "index_en.html",
        anime_list=rows,
        query=query,
        selected_genre=genre,
        selected_service=service,
        all_genres=all_genres,
        all_services=all_services,
        ja_path="/",
    )


@app.route("/en/anime/<slug>")
def anime_detail_en(slug):
    conn = get_connection()
    anime = conn.execute(
        "SELECT * FROM anime WHERE slug = ? AND title_en IS NOT NULL", (slug,)
    ).fetchone()

    if anime is None:
        conn.close()
        abort(404)

    availability = conn.execute(
        """SELECT service.name AS service_name, service.official_url,
                  availability.plan_type, availability.watch_url,
                  availability.verified_at
           FROM availability
           JOIN service ON service.id = availability.service_id
           WHERE availability.anime_id = ?""",
        (anime["id"],),
    ).fetchall()

    seasons = conn.execute(
        """SELECT label, subtitle, kind, release_year, episode_count
           FROM season WHERE anime_id = ? ORDER BY display_order""",
        (anime["id"],),
    ).fetchall()

    conn.close()
    return render_template(
        "anime_detail_en.html", anime=anime, availability=availability, seasons=seasons,
        ja_path=f"/anime/{slug}",
    )


@app.route("/en/privacy")
def privacy_en():
    return render_template("privacy_en.html", ja_path="/privacy")


@app.route("/en/contact")
def contact_en():
    return render_template("contact_en.html", ja_path="/contact")


@app.route("/about")
def about():
    return render_template("about.html", en_path="/en/about")


@app.route("/en/about")
def about_en():
    return render_template("about_en.html", ja_path="/about")


@app.route("/guides")
def guides():
    return render_template("guides.html", en_path="/en/")


@app.route("/guides/service-comparison")
def guide_service_comparison():
    return render_template("guide_service_comparison.html", en_path="/en/")


@app.route("/guides/free-anime")
def guide_free_anime():
    return render_template("guide_free_anime.html", en_path="/en/")


@app.route("/guides/beginner-guide")
def guide_beginner():
    return render_template("guide_beginner.html", en_path="/en/")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html", en_path="/en/privacy")


@app.route("/contact")
def contact():
    return render_template("contact.html", en_path="/en/contact")


@app.route("/ads.txt")
def ads_txt():
    content = "google.com, pub-7059621726238022, DIRECT, f08c47fec0942fa0"
    return Response(content, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    conn = get_connection()
    rows = conn.execute("SELECT slug, updated_at FROM anime").fetchall()
    conn.close()

    base_url = request.url_root.rstrip("/")
    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml_parts.append(f"<url><loc>{base_url}/</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/about</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/guides</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/guides/service-comparison</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/guides/free-anime</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/guides/beginner-guide</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/privacy</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/contact</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/en/</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/en/about</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/en/privacy</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/en/contact</loc></url>")
    for row in rows:
        xml_parts.append(
            f"<url><loc>{base_url}/anime/{row['slug']}</loc>"
            f"<lastmod>{row['updated_at'][:10]}</lastmod></url>"
        )
        xml_parts.append(
            f"<url><loc>{base_url}/en/anime/{row['slug']}</loc>"
            f"<lastmod>{row['updated_at'][:10]}</lastmod></url>"
        )
    xml_parts.append("</urlset>")

    return Response("\n".join(xml_parts), mimetype="application/xml")


@app.errorhandler(404)
def not_found(e):
    if request.path.startswith("/en/") or request.path == "/en":
        return render_template("404_en.html"), 404
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)