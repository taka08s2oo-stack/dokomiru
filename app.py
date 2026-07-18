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

    conn.close()
    return render_template("anime_detail.html", anime=anime, availability=availability)


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/sitemap.xml")
def sitemap():
    conn = get_connection()
    rows = conn.execute("SELECT slug, updated_at FROM anime").fetchall()
    conn.close()

    base_url = request.url_root.rstrip("/")
    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml_parts.append(f"<url><loc>{base_url}/</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/privacy</loc></url>")
    xml_parts.append(f"<url><loc>{base_url}/contact</loc></url>")
    for row in rows:
        xml_parts.append(
            f"<url><loc>{base_url}/anime/{row['slug']}</loc>"
            f"<lastmod>{row['updated_at'][:10]}</lastmod></url>"
        )
    xml_parts.append("</urlset>")

    return Response("\n".join(xml_parts), mimetype="application/xml")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
