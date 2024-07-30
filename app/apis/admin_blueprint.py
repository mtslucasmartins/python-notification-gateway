import json
from flask import request, Blueprint, jsonify
from app.services import SmsService

sms_service = SmsService.get_instance()

admin_blueprint = Blueprint("admin_blueprint", __name__)

@admin_blueprint.route("/api/v1/admin/sms/consumer/start", methods=["GET"])
def consumer_start():
    result: bool = sms_service.consumer_start()
    return { "status": "ok", "result": result }

@admin_blueprint.route("/api/v1/admin/sms/consumer/stop", methods=["GET"])
def consumer_stop():
    result: bool = sms_service.consumer_stop()
    return { "status": "ok", "result": result }

@admin_blueprint.route("/api/v1/admin/sms/producer/produce", methods=["POST"])
def producer_produce():
    json_data = request.json
    sms_service.producer_produce(json.dumps(json_data))
    return { "status": "ok", "data": json_data }
