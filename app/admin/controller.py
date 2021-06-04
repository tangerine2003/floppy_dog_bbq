from flask import Blueprint, render_template, url_for

admin = Blueprint("admin", __name__, template_folder=".templates")


@admin.route("/sitemap")
def sitemap():
    links = []
    for rule in admin.url_map.iter_rules():
        if len(rule.defaults) >= len(rule.arguments):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return render_template("all_links.html", links=links)
