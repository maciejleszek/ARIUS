from flask import Blueprint, request, jsonify
from app.models.stamp import Stamp
from app.models.review import Review
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

stamps = Blueprint('stamps', __name__)

@stamps.route('/stamps', methods=['GET'])
def get_stamps():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    stamps = Stamp.query.paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'stamps': [{
            'id': stamp.id,
            'name': stamp.name,
            'description': stamp.description,
            'price': stamp.price,
            'year_issued': stamp.year_issued,
            'country': stamp.country,
            'quantity_available': stamp.quantity_available,
            'image_url': stamp.image_url
        } for stamp in stamps.items],
        'total_pages': stamps.pages,
        'current_page': stamps.page
    }), 200

@stamps.route('/stamps/<int:stamp_id>', methods=['GET'])
def get_stamp(stamp_id):
    stamp = Stamp.query.get_or_404(stamp_id)
    reviews = Review.query.filter_by(stamp_id=stamp_id).all()
    
    avg_rating = 0
    if reviews:
        avg_rating = sum(review.rating for review in reviews) / len(reviews)
    
    return jsonify({
        'id': stamp.id,
        'name': stamp.name,
        'description': stamp.description,
        'price': stamp.price,
        'year_issued': stamp.year_issued,
        'country': stamp.country,
        'quantity_available': stamp.quantity_available,
        'image_url': stamp.image_url,
        'average_rating': round(avg_rating, 1),
        'reviews_count': len(reviews)
    }), 200

@stamps.route('/stamps/<int:stamp_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(stamp_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    # Check if user has bought this stamp
    # This logic would need to be implemented based on your order system
    
    review = Review(
        user_id=current_user_id,
        stamp_id=stamp_id,
        rating=data['rating'],
        comment=data.get('comment', '')
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify({'message': 'Review added successfully'}), 201

@stamps.route('/stamps/search', methods=['GET'])
def search_stamps():
    query = request.args.get('q', '')
    country = request.args.get('country', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    stamp_query = Stamp.query
    
    if query:
        stamp_query = stamp_query.filter(
            (Stamp.name.ilike(f'%{query}%')) | 
            (Stamp.description.ilike(f'%{query}%'))
        )
    
    if country:
        stamp_query = stamp_query.filter(Stamp.country == country)
        
    if min_price is not None:
        stamp_query = stamp_query.filter(Stamp.price >= min_price)
        
    if max_price is not None:
        stamp_query = stamp_query.filter(Stamp.price <= max_price)
    
    stamps = stamp_query.all()
    
    return jsonify({
        'stamps': [{
            'id': stamp.id,
            'name': stamp.name,
            'description': stamp.description,
            'price': stamp.price,
            'country': stamp.country,
            'image_url': stamp.image_url
        } for stamp in stamps]
    }), 200