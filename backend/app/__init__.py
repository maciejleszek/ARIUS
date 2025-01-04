from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from config import config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()
cors = CORS()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(config[config_name])
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    
    # Register blueprints
    from app.routes.auth import auth
    from app.routes.stamps import stamps
    from app.routes.orders import orders
    from app.routes.reviews import reviews
    
    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(stamps, url_prefix='/api')
    app.register_blueprint(orders, url_prefix='/api')
    app.register_blueprint(reviews, url_prefix='/api')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
        
    return app