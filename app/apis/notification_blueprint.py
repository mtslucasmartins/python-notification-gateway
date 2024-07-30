from flask import request, Blueprint, jsonify

notifications_blueprint = Blueprint("notifications_blueprint", __name__)

@notifications_blueprint.route("/api/v1/notifications", methods=["GET"])
def get_notifications():
    return { "status": "ok" }

@notifications_blueprint.route("/api/v1/notifications", methods=["POST"])
def publish_notification():
    json_data = request.json
    return jsonify(json_data)
