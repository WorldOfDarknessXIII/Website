from flask import abort
from flask import Blueprint
from flask import redirect
from flask import request
from wod13site import util

bp_redirects = Blueprint("redirects", __name__)


@bp_redirects.route("/join/<string:id>")
def page_join(id):
    server = util.get_server(id)
    return redirect("byond://{}:{}".format(server["host"], server["port"]))


@bp_redirects.route("/rules")
def page_rules():
    server_id = request.args.get("server", type=str, default=util.get_server_default()["id"])
    server = util.get_server(server_id)

    if not server:
        return abort(404)

    return redirect(server["rules_url"])


@bp_redirects.route("/forum")
def page_forum():
    return redirect("https://forums.wod13.org")


@bp_redirects.route("/maps")
def page_map_viewer():
    return redirect("https://webmap.affectedarc07.co.uk/maps/wod13/sanfran/")


@bp_redirects.route("/uptime")
def page_uptime():
    return redirect("https://status.wod13.")
