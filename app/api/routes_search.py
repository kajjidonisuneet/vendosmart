from app import api, db
from flask_restful import Api, Resource, reqparse, abort
from app.models import Vendor

vendor_search_get_args = reqparse.RequestParser()
vendor_search_get_args.add_argument(
    'name', type=str, help='Name must be a string', location='args')
vendor_search_get_args.add_argument(
    'rating', type=int,   help='Rating must be a float',  location='args')
vendor_search_get_args.add_argument(
    'location', type=str,  help='Location must be a string',  location='args')


class VendorSearch(Resource):
    def get(self):
        args = vendor_search_get_args.parse_args()
        if not (args['name'] or args['location'] or args['rating'] ):
            abort(400, message='please specify at least one valid parameter')

        all_filters = []

        if args['name']:
            all_filters.append(Vendor.name.contains( args['name']))

        if args['rating']:
            all_filters.append(Vendor.rating >= args['rating'])

        if args['location']:
            all_filters.append(Vendor.location.contains(args['location']))

        vendors = Vendor.query.filter(*all_filters).all()

        return Vendor.to_collection(vendors)


api.add_resource(VendorSearch, "/vendor_search")