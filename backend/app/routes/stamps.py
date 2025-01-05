from flask import Blueprint, request, jsonify
from app.models.stamp import Stamp
from app.models.review import Review
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

stamps = Blueprint('stamps', __name__)

# Get a paginated list of stamps
@stamps.route('/', methods=['GET'])
def get_stamps():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Paginate the query
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

# Get details for a specific stamp
@stamps.route('/<int:stamp_id>', methods=['GET'])
def get_stamp(stamp_id):
    stamp = Stamp.query.get_or_404(stamp_id)
    reviews = Review.query.filter_by(stamp_id=stamp_id).all()
    
    # Calculate average rating
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

# Add a review for a stamp
@stamps.route('/<int:stamp_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(stamp_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    # Check if user has purchased this stamp
    # Example: Add your own logic based on your order model
    # purchased = Order.query.filter_by(user_id=current_user_id, stamp_id=stamp_id).first()
    # if not purchased:
    #     return jsonify({'message': 'You must purchase this stamp before reviewing it'}), 403
    
    # Add review
    review = Review(
        user_id=current_user_id,
        stamp_id=stamp_id,
        rating=data['rating'],
        comment=data.get('comment', '')
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify({'message': 'Review added successfully'}), 201

# Search for stamps by query, country, and price range
@stamps.route('/search', methods=['GET'])
def search_stamps():
    query = request.args.get('q', '')
    country = request.args.get('country', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    stamp_query = Stamp.query
    
    # Filter by name or description
    if query:
        stamp_query = stamp_query.filter(
            (Stamp.name.ilike(f'%{query}%')) | 
            (Stamp.description.ilike(f'%{query}%'))
        )
    
    # Filter by country
    if country:
        stamp_query = stamp_query.filter(Stamp.country == country)
        
    # Filter by price range
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
