import sqlite3
from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)
DB_PATH = "anime_finder.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    query = request.args.get("q", "").strip()
    conn = get_connection()

    if query:
        rows = conn.execute(
            """SELECT * FROM anime
               WHERE title LIKE ? OR title_kana LIKE ?
               ORDER BY release_year DESC""",
            (f"%{query}%", f"%{query}%"),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM anime ORDER BY release_year DESC"
        ).fetchall()

    conn.close()
    return render_template("index.html", anime_list=rows, query=query)


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


@app.route("/sitemap.xml")
def sitemap():
    conn = get_connection()
    rows = conn.execute("SELECT slug, updated_at FROM anime").fetchall()
    conn.close()

    base_url = request.url_root.rstrip("/")
    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml_parts.append(f"<url><loc>{base_url}/</loc></url>")
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
