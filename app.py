from flask import Flask, request, redirect, render_template, jsonify, abort, session, flash, url_for
from flask_cors import CORS
import os

def create_app(test_config=None):
    # Create and configure the app
    template_dir = os.path.abspath('templates')

    # Initialize the app
    app = Flask(__name__, template_folder=template_dir)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # Load default config from settings.py
    app.config.from_pyfile('settings.py')

    # Initialize Plugins
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    @app.route('/')
    def index():
        return render_template('pages/index.html')

    @app.route('/submit_form', methods=['POST'])
    def submit_form():
        data = request.get_json(force=True)
        latitude = data.get("latitude", None)
        longitude = data.get("longitude", None)

        if latitude is not None and longitude is not None:
            response_data = {
                "success": True,
                "latitude": latitude,
                "longitude": longitude
            }
            print(response_data)
        
        else:
            response_data = {
                "success": False,
                "message": "Latitude or longitude missing in the form data"
            }
            print(response_data)

        return jsonify(response_data)

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('pages/errors/403.html', data={
            'success': False,
            'error': 403,
            'message': 'Access forbidden'
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template('pages/errors/404.html',data={
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return render_template('pages/errors/405.html', data={
            'success': False,
            'error': 405,
            'message': 'Method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessed(error):
        return render_template('pages/errors/422.html',data={
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        }), 422

    @app.errorhandler(500)
    def unauthorized(error):
        return render_template('pages/errors/500.html',data={
            'success': False,
            'error': 500,
            'message': 'Unauthorized'
        }), 500
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)