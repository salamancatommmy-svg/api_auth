"""Capa de presentación de la API: define los endpoints HTTP."""
from flask import Blueprint, jsonify, request
from servicios.servicio_auth import ErrorNegocio, ServicioAuth

def crear_blueprint(servicio: ServicioAuth | None = None) -> Blueprint:
    """Crea el Blueprint de autenticación."""
    bp = Blueprint("auth", __name__, url_prefix="/api")
    servicio = servicio or ServicioAuth()

    @bp.post("/registro")
    def registro():
        datos = request.get_json(silent=True) or {}
        try:
            creado = servicio.registrar(datos.get("usuario"), datos.get("clave"))
            return jsonify(mensaje="Registro exitoso.", **creado), 201
        except ErrorNegocio as e:
            return jsonify(error=e.mensaje), e.codigo

    @bp.post("/login")
    def login():
        datos = request.get_json(silent=True) or {}
        try:
            servicio.iniciar_sesion(datos.get("usuario"), datos.get("clave"))
            return jsonify(mensaje="Autenticación satisfactoria."), 200
        except ErrorNegocio as e:
            return jsonify(error=e.mensaje), e.codigo

    return bp