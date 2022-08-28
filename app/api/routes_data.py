from app import api, db
from flask_restful import Api, Resource, reqparse, abort
from app.models import Vendor

vendor_data_post_args = reqparse.RequestParser()
vendor_data_post_args.add_argument(
    'name', type=str, required=True, help='Name is required and must be a string')
vendor_data_post_args.add_argument(
    'location', type=str, required=True, help='Location is required and must be a string')
vendor_data_post_args.add_argument(
    'rating', type=int,  required=True, help='Rating is required and must be a float')
vendor_data_post_args.add_argument(
    'skills', type=str,  required=True, help='Skills is required and must be a string')


vendor_data_put_args = reqparse.RequestParser()
vendor_data_put_args.add_argument(
    'name', type=str, help='Name must be a string')
vendor_data_put_args.add_argument(
    'location', type=str, help='Location must be a string')
vendor_data_put_args.add_argument(
    'rating', type=int,   help='Rating must be a float')
vendor_data_put_args.add_argument(
    'skills', type=str,  help='Skills must be a string')

class VendorData(Resource):
    def get(self, vendor_id):
       return Vendor.query.get_or_404(vendor_id).to_dict(include_id=True)

    def post(self):
        args = vendor_data_post_args.parse_args()
        print(args)
        if Vendor.query.filter_by(name=args['name'], location=args['location'], skills=args['skills']).first():
            abort(400, message='Vendor already exists')
        vendor = Vendor()
        vendor.from_dict(args)
        db.session.add(vendor)
        db.session.commit()
        return {"data vendor post": args}

    def put(self, vendor_id):
        vendor = Vendor.query.get_or_404(vendor_id)
        args = vendor_data_put_args.parse_args()
        if not (args['name'] or args['location'] or args['rating'] or args['skills'] ):
            abort(400, message='please specify at least one parameter')
        vendor.from_dict(args)
        db.session.add(vendor)
        db.session.commit()
        return {'vendor data updated': vendor.to_dict(include_id=True)}

    def delete(self, vendor_id):
        vendor = Vendor.query.get_or_404(vendor_id)
        db.session.delete(vendor)
        db.session.commit()
        return {'message': 'vendor data deleted'}


api.add_resource(VendorData, "/vendor_data","/vendor_data/<int:vendor_id>")
