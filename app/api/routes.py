from ast import Delete
from app import api
from flask_restful import Api, Resource, reqparse


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
        all_filters = []

        if args['name']:
            all_filters.append(args['name']) # change this to sql filter address
        
        if args['rating']:
            all_filters.append(args['rating'])
        
        if args['location']:
            all_filters.append(args['location'])

        print(all_filters)

        return {"data vendor search": args}


vendor_data_post_args = reqparse.RequestParser()
vendor_data_post_args.add_argument(
    'name', type=str, required=True, help='Name is required and must be a string')
vendor_data_post_args.add_argument(
    'location', type=str, required=True, help='Location is required and must be a string')
vendor_data_post_args.add_argument(
    'rating', type=int,  required=True, help='Rating is required and must be a float')
vendor_data_post_args.add_argument(
    'skills', type=str,  required=True, help='Skills is required and must be a string')


class VendorData(Resource):
    def post(self):
        args = vendor_data_post_args.parse_args()
        return {"data vendor post": args}

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(VendorSearch, "/vendor_search")
api.add_resource(VendorData, "/vendor_data")

